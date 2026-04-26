"""
Live patient panel — single-case form input → wired inference output.

Phase 1.3 deliverable. Renders a Streamlit form for the 10 trained features,
calls ml.infer.infer_one on submit, and displays the prediction with all
safety-layer signals (calibrated probability, Mahalanobis OOD, primary
energy gate, secondary neg-energy gate, conformal bands).
"""
from __future__ import annotations

from typing import Any, Iterable

import streamlit as st

from ml.infer import infer_one

KNOWN_SYMPTOMS: tuple[str, ...] = (
    "fever",
    "headache",
    "nuchal_rigidity",
    "altered_mental_status",
    "photophobia",
    "nausea_vomiting",
    "seizure",
)


def build_row(
    age: float,
    csf_glucose: float,
    csf_protein: float,
    csf_wbc: float,
    pcr: bool,
    microscopy: bool,
    exposure: bool,
    symptoms: Iterable[str],
) -> dict[str, Any]:
    """Assemble a row dict in the schema infer_one expects."""
    return {
        "age": int(age),
        "csf_glucose": float(csf_glucose),
        "csf_protein": float(csf_protein),
        "csf_wbc": int(csf_wbc),
        "pcr": int(bool(pcr)),
        "microscopy": int(bool(microscopy)),
        "exposure": int(bool(exposure)),
        "symptoms": ";".join(s for s in symptoms if s),
    }


def decision_badge(prediction: str, reason: str | None) -> str:
    """Map a (prediction, reason) pair to a Streamlit-flavored markdown badge."""
    p = (prediction or "").strip()
    if p == "ABSTAIN":
        tag = reason if reason else "unspecified"
        return f":orange[ABSTAIN — {tag}]"
    if p == "High":
        return ":red[HIGH RISK]"
    if p == "Low":
        return ":green[LOW RISK]"
    if p == "Moderate":
        return ":blue[MODERATE]"
    return f":gray[{p or 'unknown'}]"


def _fmt_metric(out: dict[str, Any], key: str, fmt: str = "{:.3f}") -> str:
    val = out.get(key)
    if val is None:
        return "—"
    try:
        return fmt.format(float(val))
    except (TypeError, ValueError):
        return "—"


def render_live_patient_panel() -> None:
    """Render the live-patient prediction widget into the current Streamlit app."""
    with st.expander("🩺 Live Patient — single-case prediction", expanded=True):
        st.caption(
            "Research and educational use only. Not a medical device, not validated "
            "for clinical decisions. Outputs are calibrated probabilities under the "
            "training distribution; check the OOD and conformal signals before acting."
        )

        with st.form("live_patient_form", clear_on_submit=False):
            c1, c2 = st.columns(2)
            with c1:
                age = st.number_input(
                    "Age (years)", min_value=0, max_value=120, value=12, step=1,
                )
                csf_glucose = st.number_input(
                    "CSF glucose (mg/dL)", min_value=0.0, max_value=300.0,
                    value=18.0, step=1.0,
                    help="PAM typical: <40 mg/dL; normal range 50-80.",
                )
                csf_protein = st.number_input(
                    "CSF protein (mg/dL)", min_value=0.0, max_value=2000.0,
                    value=420.0, step=10.0,
                    help="PAM typical: >100 mg/dL; normal range 15-45.",
                )
                csf_wbc = st.number_input(
                    "CSF WBC (cells/µL)", min_value=0, max_value=20000,
                    value=2100, step=10,
                    help="PAM typical: >1000 with neutrophil predominance; normal <5.",
                )
            with c2:
                pcr = st.checkbox("Naegleria PCR positive", value=True)
                microscopy = st.checkbox("Microscopy: motile trophozoites", value=True)
                exposure = st.checkbox("Freshwater exposure within 14 days", value=True)
                symptoms = st.multiselect(
                    "Symptoms present",
                    options=list(KNOWN_SYMPTOMS),
                    default=["fever", "headache", "nuchal_rigidity"],
                )
            submitted = st.form_submit_button("Run inference")

        if not submitted:
            return

        row = build_row(age, csf_glucose, csf_protein, csf_wbc, pcr, microscopy, exposure, symptoms)

        try:
            out = infer_one(row)
        except FileNotFoundError as e:
            st.error(f"Model artifact missing: {e}")
            st.info("Run `python -m ml.training_calib_dca` to train and save the model.")
            return
        except Exception as e:
            st.error(f"Inference failed: {type(e).__name__}: {e}")
            return

        prediction = str(out.get("prediction", "unknown"))
        reason = out.get("reason")
        reason_str = reason if isinstance(reason, str) else None
        st.markdown(f"### Decision: {decision_badge(prediction, reason_str)}")

        p_high_raw = out.get("p_high")
        try:
            p_high = float(p_high_raw) if p_high_raw is not None else float("nan")
        except (TypeError, ValueError):
            p_high = float("nan")
        st.write(f"**Calibrated p(High) = {p_high:.4f}**")
        if p_high == p_high:
            st.progress(min(max(p_high, 0.0), 1.0))

        c1, c2, c3, c4 = st.columns(4)
        c1.metric("Mahalanobis d²", _fmt_metric(out, "mahalanobis_d2", "{:.2f}"))
        c2.metric("d² threshold τ", _fmt_metric(out, "d2_tau", "{:.2f}"))
        c3.metric("Logit-energy", _fmt_metric(out, "energy", "{:.2f}"))
        c4.metric("Logit-energy τ", _fmt_metric(out, "energy_tau", "{:.2f}"))

        c5, c6, c7, c8 = st.columns(4)
        c5.metric("Neg-energy(p)", _fmt_metric(out, "energy_neg"))
        c6.metric("Neg-energy τ", _fmt_metric(out, "energy_neg_tau"))
        c7.metric("q̂ (conformal)", _fmt_metric(out, "qhat"))
        c8.metric("α", _fmt_metric(out, "alpha", "{:.2f}"))

        bands: list[str] = []
        if out.get("include_high"):
            bands.append("High")
        if out.get("include_low"):
            bands.append("Low")
        if bands:
            st.write(f"Conformal prediction set: {{ {', '.join(bands)} }}")
        group = out.get("group")
        if isinstance(group, str) and group:
            st.write(f"Conformal group: **{group}**")

        if out.get("ood_abstain_energy_neg"):
            st.warning(
                "Secondary neg-energy gate is above its threshold — the model is "
                "uncertain enough that the prob-energy signal would also recommend abstaining."
            )

        with st.expander("Raw inference output"):
            st.json(out)
