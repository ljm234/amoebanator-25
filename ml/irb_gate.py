"""
IRB compliance gate for the training pipeline.

Behavior:
  * If the dataset declares itself synthetic (column `source` exclusively
    contains values starting with `simulated`, `synthetic`, or `bridge`),
    the gate permits it without reading an IRB record and, when `emit_audit`
    is True (the default), logs a compliance-check audit event. Synthetic
    data does not require IRB approval.
  * Otherwise, the gate reads `outputs/irb/current_irb.json`. If the JSON
    contains an `irb_status` field whose value is APPROVED or
    CONDITIONALLY_APPROVED (case-insensitive, surrounding whitespace trimmed;
    hyphens and spaces count as underscores),
    training proceeds. Any other status - including missing file or
    malformed JSON - raises `IRBGateBlocked` with an actionable message.

The IRB record schema is intentionally minimal so it can be hand-edited.
`ml.data.compliance.IRBApplication.to_dict()` does not produce it: that
method writes the status under `status`, not `irb_status`, so its output is
blocked here as '(missing)'. The gate reads only `irb_status`; the other
fields document the approval for a reviewer and are not checked (the gate
does not compare `expiration_date` with today's date):

    {
      "irb_protocol_id":   "<short id>",
      "irb_status":        "approved" | "conditionally_approved" | ...,
      "approval_date":     "YYYY-MM-DD",
      "expiration_date":   "YYYY-MM-DD",
      "principal_investigator": "<name>"
    }

Configuration:
  * AMOEBANATOR_IRB_PATH - override path to current_irb.json
  * AMOEBANATOR_RESEARCH_MODE - when set to "1", "true", "TRUE" or "yes"
    (`research_mode_enabled`, the rule the Predict page also uses), skip the
    check entirely (synthetic-data research mode; the Docker image sets it
    to 1). The override is recorded in the audit log so it is never
    invisible.
"""
from __future__ import annotations

import json
import os
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

import pandas as pd

from ml.audit_hooks import _emit
from ml.data.audit_trail import AuditEventType
from ml.data.compliance import IRBStatus

IRB_PATH_ENV: str = "AMOEBANATOR_IRB_PATH"
RESEARCH_MODE_ENV: str = "AMOEBANATOR_RESEARCH_MODE"
_RESEARCH_MODE_VALUES: frozenset[str] = frozenset({"1", "true", "TRUE", "yes"})


def research_mode_enabled() -> bool:
    """True when AMOEBANATOR_RESEARCH_MODE is "1", "true", "TRUE" or "yes".

    Surrounding whitespace is ignored. The gate and the Predict page share
    this rule, so the page shows its research-mode banner for exactly the
    values that make the gate skip the IRB check.
    """
    return os.environ.get(RESEARCH_MODE_ENV, "").strip() in _RESEARCH_MODE_VALUES


_REPO_ROOT: Path = Path(__file__).resolve().parent.parent
DEFAULT_IRB_PATH: Path = _REPO_ROOT / "outputs" / "irb" / "current_irb.json"

_PERMITTED_STATUSES: frozenset[str] = frozenset({
    IRBStatus.APPROVED.value,
    IRBStatus.CONDITIONALLY_APPROVED.value,
})

# Source prefixes of synthetic rows. MIMIC-IV rows (source "mimic_iv", set by
# ml/mimic_iv_loader.py) are real, de-identified patient data, so they are not
# synthetic and need an IRB record like any other real dataset.
_SYNTHETIC_PREFIXES: tuple[str, ...] = ("simulated", "synthetic", "bridge")


class IRBGateBlocked(RuntimeError):
    """Raised when a training run hits a missing or non-approved IRB record."""


@dataclass(frozen=True)
class IRBDecision:
    permitted: bool
    reason: str
    status: str | None = None
    record: dict[str, Any] = field(default_factory=dict)


def default_irb_path() -> Path:
    override = os.environ.get(IRB_PATH_ENV)
    return Path(override).expanduser().resolve() if override else DEFAULT_IRB_PATH


def is_dataset_synthetic(df: pd.DataFrame) -> bool:
    """A dataset is treated as synthetic if every `source` value matches a known prefix."""
    if "source" not in df.columns or df.empty:
        return False
    sources = df["source"].astype(str).str.lower().str.strip()
    return bool(sources.apply(lambda s: any(s.startswith(p) for p in _SYNTHETIC_PREFIXES)).all())


def _normalize_status(raw: object) -> str:
    if raw is None:
        return ""
    return str(raw).strip().lower().replace("-", "_").replace(" ", "_")


def evaluate_irb_record(path: Path | None = None) -> IRBDecision:
    """Read the IRB JSON file and return an IRBDecision."""
    target = path or default_irb_path()
    if not target.exists():
        return IRBDecision(
            permitted=False,
            reason=(
                f"No IRB record found at {target}. "
                "Place a JSON record whose irb_status is \"approved\" or \"conditionally_approved\" at this path; "
                "set AMOEBANATOR_RESEARCH_MODE=1 (audit-logged) only while the data are synthetic."
            ),
            status=None,
            record={},
        )
    try:
        record = json.loads(target.read_text())
    except json.JSONDecodeError as e:
        return IRBDecision(
            permitted=False,
            reason=f"IRB record at {target} is not valid JSON: {e}",
            status=None,
            record={},
        )
    if not isinstance(record, dict):
        return IRBDecision(
            permitted=False,
            reason=f"IRB record at {target} must be a JSON object; got {type(record).__name__}.",
            status=None,
            record={},
        )
    status = _normalize_status(record.get("irb_status"))
    if status in _PERMITTED_STATUSES:
        return IRBDecision(permitted=True, reason="IRB status is approved", status=status, record=record)
    return IRBDecision(
        permitted=False,
        reason=(
            f"IRB status '{status or '(missing)'}' is not in the permitted set "
            f"{sorted(_PERMITTED_STATUSES)}. Update {target} once a valid approval lands."
        ),
        status=status or None,
        record=record,
    )


def check_irb_or_raise(
    df: pd.DataFrame | None = None,
    path: Path | None = None,
    *,
    emit_audit: bool = True,
) -> IRBDecision:
    """
    Top-level gate. Call from the training entry point. Raises `IRBGateBlocked`
    on failure with a clear remediation message; returns the decision on success.
    """
    research_mode = research_mode_enabled()
    if research_mode:
        decision = IRBDecision(permitted=True, reason="research mode via AMOEBANATOR_RESEARCH_MODE env var", status="research_mode")
        if emit_audit:
            _emit(
                AuditEventType.COMPLIANCE_CHECK,
                actor="ml.irb_gate.check_irb_or_raise",
                resource=str(path or default_irb_path()),
                action_detail="research mode via env var (no IRB required)",
                metadata={"research_mode": True},
            )
        return decision

    if df is not None and is_dataset_synthetic(df):
        decision = IRBDecision(permitted=True, reason="synthetic-only dataset", status="synthetic")
        if emit_audit:
            _emit(
                AuditEventType.COMPLIANCE_CHECK,
                actor="ml.irb_gate.check_irb_or_raise",
                resource="dataset",
                action_detail="synthetic dataset, IRB not required",
                metadata={"reason": "synthetic", "n_rows": int(len(df))},
            )
        return decision

    decision = evaluate_irb_record(path)
    if emit_audit:
        _emit(
            AuditEventType.IRB_STATUS_CHANGE if decision.permitted else AuditEventType.ACCESS_DENIED,
            actor="ml.irb_gate.check_irb_or_raise",
            resource=str(path or default_irb_path()),
            action_detail=decision.reason,
            metadata={"status": decision.status, "permitted": decision.permitted},
        )
    if not decision.permitted:
        raise IRBGateBlocked(decision.reason)
    return decision
