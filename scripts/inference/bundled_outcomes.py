"""
Outcome of each of the 30 bundled rows through the full inference pipeline.

Runs ml.infer.infer_one on every row of outputs/diagnosis_log_pro.csv, with
the columns the Predict page sends, and records each row's label, prediction,
abstain reason and p_high. The summary counts rows by outcome, overall and
per label, so the abstention figures the docs quote (how many rows abstain,
at which gate, and how the High rows fare) come from this artifact.

Output: outputs/metrics/bundled_outcomes.json

Usage:
  PYTHONPATH=. python scripts/inference/bundled_outcomes.py
"""
from __future__ import annotations

import json
import sys
from collections import Counter
from pathlib import Path
from typing import Any

import pandas as pd

REPO_ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(REPO_ROOT))

from ml.infer import infer_one  # noqa: E402

LOG_CSV = REPO_ROOT / "outputs" / "diagnosis_log_pro.csv"
OUT_JSON = REPO_ROOT / "outputs" / "metrics" / "bundled_outcomes.json"
INPUT_COLS = ["age", "csf_glucose", "csf_protein", "csf_wbc", "pcr", "microscopy", "exposure", "symptoms"]


def outcome(out: dict[str, Any]) -> str:
    """'High', 'Low', or 'ABSTAIN:<reason>'."""
    pred = str(out["prediction"])
    return f"ABSTAIN:{out.get('reason')}" if pred == "ABSTAIN" else pred


def summarize(rows: list[dict[str, Any]]) -> dict[str, Any]:
    by_label: dict[str, dict[str, int]] = {}
    for label in sorted({r["risk_label"] for r in rows}):
        by_label[label] = dict(sorted(Counter(r["outcome"] for r in rows if r["risk_label"] == label).items()))
    overall = dict(sorted(Counter(r["outcome"] for r in rows).items()))
    return {
        "n_rows": len(rows),
        "n_abstain": sum(1 for r in rows if r["prediction"] == "ABSTAIN"),
        "overall": overall,
        "by_label": by_label,
    }


def main() -> int:
    df = pd.read_csv(LOG_CSV)
    rows: list[dict[str, Any]] = []
    for _, r in df.iterrows():
        out = infer_one(r[INPUT_COLS])
        p = out.get("p_high")
        rows.append({
            "case_id": str(r["case_id"]),
            "risk_label": str(r["risk_label"]),
            "prediction": str(out["prediction"]),
            "reason": out.get("reason"),
            "outcome": outcome(out),
            "p_high": None if p is None else float(p),
        })
    payload = {"summary": summarize(rows), "rows": rows}
    OUT_JSON.parent.mkdir(parents=True, exist_ok=True)
    OUT_JSON.write_text(json.dumps(payload, indent=2))
    print(json.dumps(payload["summary"], indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
