"""About page.

Landing page with a model card excerpt, a feature-importance panel, an
interactive conformal explorer and the authorship note. The panels follow a
standard reporting order: architecture, training, calibration,
explainability, uncertainty, authorship.

The |w_i| panel renders ONLY here (NOT on the predict
page) because |w_i| is model-level, not per-prediction; rendering
adjacent to a result would falsely imply input-specificity. The
caption is fixed, model-level text.

The Advanced expander hosts the alpha slider, so a reader can move
alpha in {1/20, 1/10, 1/7, 1/5} and watch the rank k and the regime badge
respond. It is illustrative; the rest of the page does not depend on it.

The authorship section names the repository (github.com/ljm234/
amoebanator-25) and notes the companion HuggingFace Space is by the
same author.
"""
from __future__ import annotations

from pathlib import Path

import pandas as pd
import streamlit as st
import torch

from app.disclaimer import render_disclaimer
from ml.config import conformal_alpha, parse_alpha
from ml.conformal_advanced import finite_sample_rank


_MODEL_PATH = Path("outputs/model/model.pt")
_FEATURE_NAMES: tuple[str, ...] = (
    "age",
    "csf_glucose",
    "csf_protein",
    "csf_wbc",
    "pcr",
    "microscopy",
    "exposure",
    "sym_fever",
    "sym_headache",
    "sym_nuchal_rigidity",
)


@st.cache_resource
def _compute_feature_importance() -> pd.DataFrame:
    """Load model.pt, extract first Linear(10,32) layer weight, compute |w_i|.

    Returns a DataFrame with feature names + normalized |w_i| values
    suitable for st.bar_chart consumption. Cached because the model
    is frozen - recomputing every rerun would be wasted CPU.
    """
    state = torch.load(_MODEL_PATH, map_location="cpu", weights_only=True)
    if hasattr(state, "state_dict"):
        state = state.state_dict()
    w = state["net.0.weight"]  # shape (32, 10) - Linear(in=10, out=32)
    imp = w.abs().mean(dim=0).numpy()  # mean across 32 output dims -> (10,)
    imp_norm = imp / imp.sum()
    return pd.DataFrame({"feature": list(_FEATURE_NAMES), "|w_i|": imp_norm})


st.set_page_config(page_title="About - Amoebanator 25")
render_disclaimer()

st.title("About Amoebanator 25")


# -- section 1. Model architecture --------------------------------------------
st.subheader("Model architecture")
st.markdown(
    "Tabular MLP, 914 parameters, 6.4 KB serialized. "
    "`Linear(10, 32) -> ReLU -> Linear(32, 16) -> ReLU -> Linear(16, 2)` - "
    "binary classifier (PAM risk: Low / High) with two output logits "
    "consumed by softmax + temperature scaling at inference time. "
    "Architecture verified against `outputs/model/model.pt` "
    "tensor shapes."
)


# -- section 2. Training summary ----------------------------------------------
st.subheader("Training data")
st.markdown(
    "**n=30 synthetic rows created for this demo**; their age and sex "
    "distribution does not match the published PAM case series. "
    "Train/val split: n_train=24, n_val=6, `random_state=42`, "
    "`test_size=0.2`, `stratify=y`. No real PHI. Any clinical evaluation "
    "needs a real cohort, such as the planned MIMIC-IV study (target "
    "n >= 200). See `docs/data_card.md` (Gebru et al. 2021 datasheet "
    "format) for the full lineage."
)


# -- section 3. Calibration summary -------------------------------------------
st.subheader("Calibration")
st.markdown(
    "Temperature scaling (Guo et al. 2017) optimized via L-BFGS on the "
    "n=6 validation set. Current `T = 0.27`. **T < 1 means the calibrator "
    "amplifies the model's raw confidence** - the opposite of typical "
    "Guo 2017 behavior (T > 1 attenuates overconfidence). On n=6 the "
    "L-BFGS landscape lacks curvature to constrain T meaningfully, and a "
    "different set of six rows could give a very different T. Treat the "
    "reported T as a sample-specific point "
    "estimate, not as evidence of structural under-/over-confidence. "
    "See `docs/model_card.md` section Caveats for the full discussion."
)


# -- section 4. Feature importance via |w_i| ----------------------
st.subheader("Feature importance (model-level)")
imp_df = _compute_feature_importance()
st.bar_chart(imp_df, x="feature", y="|w_i|", horizontal=True)

# Feature-importance caption (model-level text).
st.caption(
    "Feature importance via |w_i| (model-level mean of first Linear "
    "layer weights, normalized). NOT per-prediction attribution - for "
    "that, see SHAP (deferred to a future MIMIC-IV retrain, n >= 200). "
    f"Current range: {imp_df['|w_i|'].min():.1%} to "
    f"{imp_df['|w_i|'].max():.1%}, max/min ratio "
    f"{imp_df['|w_i|'].max() / imp_df['|w_i|'].min():.2f}x. "
    "Interpretation: the model treats all 10 features near-equally, "
    "consistent with the n=30 training set limitation. SHAP with 30 "
    "background rows would not be informative, so this panel shows "
    "model-level weights instead. See `docs/model_card.md` "
    "section Caveats for full discussion."
)


# -- section 5. Conformal advanced expander (alpha slider) -------------------
with st.expander("Advanced: explore conformal coverage"):
    st.markdown(
        "Move the slider to see how the rank `k` and the regime badge "
        "respond to different significance levels. The 3-state regime "
        "badge (ASYMPTOTIC / FINITE-SAMPLE / INVALID) is "
        "computed from `(n_cal, alpha, k)` where "
        "`k = ceil((n_cal + 1)(1 - alpha))`."
    )
    demo_alpha = float(conformal_alpha())
    alpha = st.select_slider(
        "alpha (significance level)",
        options=sorted({0.05, 0.10, demo_alpha, 0.20}),
        value=demo_alpha,
        format_func=lambda a: str(parse_alpha(a)),
        key="conformal_alpha_slider",
    )
    n_cal = 6  # current n
    k = finite_sample_rank(n_cal, alpha)
    st.markdown(
        f"With `n_cal = {n_cal}`, `alpha = {parse_alpha(alpha)}` -> "
        f"`k = ceil((n+1)(1-alpha)) = {k}`."
    )
    if n_cal >= k and n_cal >= 100:
        st.success(
            "ASYMPTOTIC: Guarantee holds; "
            "finite-sample bound 1-alpha + 1/(n+1) is tight."
        )
    elif n_cal >= k:
        st.info(
            "FINITE-SAMPLE: split conformal coverage still holds on average "
            f"under exchangeability, but with n = {n_cal} the realized "
            "coverage varies widely."
        )
    else:
        st.error(
            f"INVALID: k = {k} > n = {n_cal}, so no finite threshold "
            "guarantees 1-alpha coverage; qhat is +inf and every input "
            "abstains. A future MIMIC-IV cohort (target n >= 200) will fix this."
        )


# -- section 6. Authorship + handle disclosure ------------------------
st.subheader("Authorship")
st.markdown(
    "Luis Jordan Montenegro-Calla - ORCID 0009-0000-7851-7139 - "
    "jordanmontenegroc.99@gmail.com"
)
st.caption(
    "Repo: github.com/ljm234/amoebanator-25. The companion "
    "HuggingFace Space is by the same author."
)
