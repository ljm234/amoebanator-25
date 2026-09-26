"""Predict page.

Form-based PAM risk prediction using the MLP at outputs/model/model.pt,
trained on 24 of the 30 synthetic rows. Wires ml.infer.infer_one into:

- 8 form widgets with NEUTRAL clinical defaults.
- 3 preset buttons (high_risk_pam / bacterial_meningitis_limitation /
  normal_csf).
- Limitation banner next to the result when the preset that sets
  ``limitation_banner`` is loaded and its inputs are submitted unchanged
  (after inference, not before).
- Correlation-ID error path: uuid4 full server-side, 12-char
  display + INTEGRITY_VIOLATION audit emit.
- Graceful FileNotFoundError banner when a model or threshold file is
  missing (missing Mahalanobis stats make every input ABSTAIN as OOD
  instead).
- Session-state debounce with 30s stale-lock recovery.
- Result badges: decision, the temperature T read from the model
  artifacts with a tooltip, a small-calibration-set warning if n_cal<30,
  and a 3-state conformal regime badge (green/blue/red).
- Research-mode env-var branch: AMOEBANATOR_RESEARCH_MODE set to
  1/true/TRUE/yes (ml.irb_gate.research_mode_enabled, the values the IRB
  gate accepts) -> red banner + IRB_STATUS_CHANGE emit.
"""
from __future__ import annotations

import html
import time
import uuid
from typing import Any

import streamlit as st

from app.disclaimer import render_disclaimer
from app.presets import PRESETS
from app.utils import (
    KNOWN_SYMPTOMS,
    _fmt_metric,
    build_row,
    decision_badge,
    min_calibration_rows,
    temperature_note,
)
from ml.audit_hooks import _emit
from ml.data.audit_trail import AuditEventType
from ml.config import conformal_alpha
from ml.conformal_advanced import finite_sample_rank
from ml.infer import calibration_info, infer_one
from ml.irb_gate import RESEARCH_MODE_ENV, research_mode_enabled


st.set_page_config(page_title="Predict - Amoebanator 25")
render_disclaimer()


# -- research-mode branch -------------
_research_mode_active = research_mode_enabled()
if _research_mode_active and not st.session_state.get("_research_mode_emitted"):
    _emit(
        AuditEventType.IRB_STATUS_CHANGE,
        actor="env_var",
        resource=RESEARCH_MODE_ENV,
        action_detail="synthetic-data research mode, no IRB required",
        metadata={"research_mode": True},
    )
    st.session_state["_research_mode_emitted"] = True

if _research_mode_active:
    st.error(
        "No IRB required: fully synthetic data, no human subjects, and no "
        "PHI. Any future use of real clinical data will require appropriate "
        "IRB and data-use approval before activation."
    )

st.title("PAM Risk Prediction")


# -- Form defaults ----------------------------------------------
# Streamlit keeps each widget's value in session_state under the widget key,
# ignores a widget's default once that key exists, and drops the key when the
# page is not shown. The last loaded values (defaults or a preset) are kept
# in form_values, which survives page changes, and any widget key that is
# missing is seeded from it before the form renders.
_FORM_DEFAULTS: dict[str, Any] = {
    "age": 12, "csf_glucose": 65.0, "csf_protein": 30.0, "csf_wbc": 3,
    "pcr": False, "microscopy": False, "exposure": False, "symptoms": [],
}
if "form_values" not in st.session_state:
    st.session_state["form_values"] = dict(_FORM_DEFAULTS)
for _field, _value in st.session_state["form_values"].items():
    if _field not in st.session_state:
        st.session_state[_field] = _value


def _preset_form_values(key: str) -> dict[str, Any]:
    """The form values a preset loads, typed like the form's defaults."""
    values = dict(_FORM_DEFAULTS)
    for field, value in PRESETS[key]["inputs"].items():
        default = _FORM_DEFAULTS[field]
        values[field] = list(value) if isinstance(default, list) else type(default)(value)
    return values


# -- Preset buttons (3 buttons + neutral default state) --------
_preset_cols = st.columns(3)
for _col, _key in zip(
    _preset_cols,
    ("high_risk_pam", "bacterial_meningitis_limitation", "normal_csf"),
):
    if _col.button(PRESETS[_key]["label"], key=f"preset_{_key}"):
        # The buttons render above the form, so the widget keys can still be
        # written in this run; the form shows the preset when it renders.
        _values = _preset_form_values(_key)
        st.session_state["form_values"] = _values
        for _field, _value in _values.items():
            st.session_state[_field] = _value
        st.session_state["active_preset"] = _key
        _emit(
            AuditEventType.WEB_PRESET_LOADED,
            actor="streamlit_user",
            resource="pages/01_predict.py",
            action_detail=f"preset_loaded={_key}",
            metadata={"preset": _key},
        )


# -- Form (NEUTRAL defaults) -----------------------------
with st.form("predict_form"):
    col1, col2 = st.columns(2)
    age = col1.number_input(
        "Age (years)", min_value=0, max_value=120, key="age",
    )
    csf_glucose = col1.number_input(
        "CSF glucose (mg/dL)", min_value=0.0, max_value=500.0,
        step=1.0, key="csf_glucose",
    )
    csf_protein = col1.number_input(
        "CSF protein (mg/dL)", min_value=0.0, max_value=1000.0,
        step=1.0, key="csf_protein",
    )
    csf_wbc = col1.number_input(
        "CSF WBC (cells/uL)", min_value=0, max_value=50000,
        step=1, key="csf_wbc",
    )
    pcr = col2.checkbox("PCR positive", key="pcr")
    microscopy = col2.checkbox("Microscopy positive", key="microscopy")
    exposure = col2.checkbox("Recent freshwater exposure", key="exposure")
    symptoms = col2.multiselect(
        "Symptoms", options=list(KNOWN_SYMPTOMS), key="symptoms",
    )
    submitted = st.form_submit_button("Run inference")


def _render_result(out: dict[str, Any]) -> None:
    """Render the decision, temperature and regime badges + key metrics."""
    badge = decision_badge(str(out.get("prediction", "")), out.get("reason"))
    st.markdown(f"### Result: {badge}")

    info = calibration_info()
    T = float(info["T"])  # type: ignore[arg-type]
    n_cal_raw = out.get("n_cal", info["n_cal"])
    n_cal = int(n_cal_raw) if n_cal_raw is not None else None
    separated = info["val_separated"]
    sep_flag = bool(separated) if separated is not None else None

    # Temperature badge with hover tooltip, both read from the artifacts.
    tooltip = html.escape(temperature_note(T, n_cal, sep_flag), quote=True)
    n_label = f" (n={n_cal})" if n_cal else ""
    st.markdown(
        f'<span title="{tooltip}"><sub>T={T:.2f}{n_label}</sub></span>',
        unsafe_allow_html=True,
    )

    if n_cal is None:
        _render_metrics(out)
        return

    # Small-calibration-set banner when n_cal < 30 (not the conformal
    # SmallCalibrationWarning, whose floor is 100).
    if n_cal < 30:
        st.warning(
            f"Calibration set is small (n={n_cal}). Probability estimates "
            "are indicative only. Do not use as a clinical confidence score."
        )

    # 3-state conformal regime badge from (n, alpha, k).
    alpha = float(out.get("alpha", conformal_alpha()))
    n = n_cal
    k = finite_sample_rank(n, alpha)
    if n >= k and n >= 100:
        st.success(
            "ASYMPTOTIC: coverage >= 1-alpha holds on average under "
            "exchangeability; with untied scores the finite-sample bound "
            "1-alpha + 1/(n+1) is tight."
        )
    elif n >= k:
        st.info(
            "FINITE-SAMPLE: split conformal coverage still holds on average "
            f"under exchangeability, but with n = {n} the realized coverage "
            "varies widely."
        )
    else:
        st.error(
            f"INVALID: k = {k} > n = {n}, so no finite threshold guarantees "
            "1-alpha coverage; qhat is +inf and every input abstains. "
            f"This alpha needs at least {min_calibration_rows(alpha)} "
            "calibration rows."
        )
    _render_metrics(out)


def _render_metrics(out: dict[str, Any]) -> None:
    """Key numeric metrics - _fmt_metric tolerates missing/None/garbage.

    p_high is shown to 6 significant digits because the conformal cut-offs
    (qhat and 1 - qhat) are finer than 0.001; the cut-offs follow it when
    the result carries a finite qhat (the conformal branches of infer_one).
    """
    try:
        qhat = float(out.get("qhat"))
    except (TypeError, ValueError):
        qhat = float("nan")
    cutoffs = (
        f" (Low if <= {qhat:.6g}, High if >= {1.0 - qhat:.6g})"
        if 0.0 <= qhat <= 1.0
        else ""
    )
    st.markdown(
        f"**p_high:** {_fmt_metric(out, 'p_high', '{:.6g}')}{cutoffs} &nbsp;&nbsp; "
        f"**Mahalanobis d^2:** {_fmt_metric(out, 'mahalanobis_d2')} "
        f"(tau={_fmt_metric(out, 'd2_tau')}) &nbsp;&nbsp; "
        f"**Logit energy:** {_fmt_metric(out, 'energy')} "
        f"(tau={_fmt_metric(out, 'energy_tau')})"
    )


# -- Submit handler ---------------------------------------------------
if submitted:
    # Session-state debounce with 30s stale-lock recovery.
    if st.session_state.get("predicting"):
        lock_age = time.time() - float(
            st.session_state.get("predicting_at", 0.0)
        )
        if lock_age < 30:
            st.warning(
                "Already processing - wait for the current prediction to "
                "complete before submitting again."
            )
            st.stop()
        # else: stale lock, fall through and re-acquire

    st.session_state["predicting"] = True
    st.session_state["predicting_at"] = time.time()
    try:
        row = build_row(
            age=int(age),
            csf_glucose=float(csf_glucose),
            csf_protein=float(csf_protein),
            csf_wbc=int(csf_wbc),
            pcr=bool(pcr),
            microscopy=bool(microscopy),
            exposure=bool(exposure),
            symptoms=list(symptoms),
        )
        _emit(
            AuditEventType.WEB_PREDICT_RECEIVED,
            actor="streamlit_user",
            resource="pages/01_predict.py",
            action_detail="form submitted",
            metadata={"row_keys": sorted(row.keys())},
        )
        out = infer_one(row)
        _render_result(out)
        # Limitation banner next to the result (after inference, not
        # before), only while the loaded preset's inputs are unchanged: once
        # the form is edited, the result no longer describes that preset.
        _active = st.session_state.get("active_preset")
        _submitted = {
            "age": age, "csf_glucose": csf_glucose, "csf_protein": csf_protein,
            "csf_wbc": csf_wbc, "pcr": pcr, "microscopy": microscopy,
            "exposure": exposure, "symptoms": sorted(symptoms),
        }
        if (
            _active in PRESETS
            and PRESETS[_active]["limitation_banner"]
            and _submitted == {
                **_preset_form_values(_active),
                "symptoms": sorted(PRESETS[_active]["inputs"]["symptoms"]),
            }
        ):
            st.error(PRESETS[_active]["description"])
        p_high = out.get("p_high")
        _emit(
            AuditEventType.WEB_PREDICT_RETURNED,
            actor="streamlit_user",
            resource="pages/01_predict.py",
            action_detail=f"prediction={out.get('prediction', '?')}",
            metadata={
                "p_high": None if p_high is None else float(p_high),
                "reason": out.get("reason"),
            },
        )
    except FileNotFoundError as e:
        # A model or threshold file is missing: show a banner instead of a
        # traceback.
        st.warning(
            f"A required artifact is missing ({e.filename or e}), so no "
            "prediction can be made. See docs/REPRODUCIBILITY.md section 4 "
            "for the command that regenerates every artifact."
        )
    except Exception as e:  # noqa: BLE001 - correlation-ID catch-all
        # uuid4 full server-side, 12-char display, audit emit.
        error_id_full = uuid.uuid4().hex
        error_id_user = error_id_full[:12]
        st.error(
            f"Prediction failed (error ID: {error_id_user}). "
            "Server-side log captured."
        )
        _emit(
            AuditEventType.INTEGRITY_VIOLATION,
            actor="streamlit_user",
            resource="pages/01_predict.py",
            action_detail=f"prediction error: {type(e).__name__}",
            metadata={
                "error_id": error_id_full,
                "exception_type": type(e).__name__,
                "exception_repr": repr(e),
            },
        )
    finally:
        st.session_state["predicting"] = False
        st.session_state["predicting_at"] = 0.0
