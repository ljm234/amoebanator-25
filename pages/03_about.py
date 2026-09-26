"""About page.

About page with a model card excerpt, a first-layer weight panel, an
interactive conformal explorer and the authorship note. The panels follow a
standard reporting order: architecture, training, calibration, weights,
uncertainty, authorship. Every number about the model (parameter count,
file size, layer shapes, temperature, weight range, calibration-set size)
is read from the shipped artifacts when the page renders.

The |w_i| panel renders ONLY here (NOT on the predict
page) because |w_i| is model-level, not per-prediction; rendering
adjacent to a result would falsely imply input-specificity.

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
from app.utils import min_calibration_rows
from ml.config import conformal_alpha, parse_alpha
from ml.conformal_advanced import finite_sample_rank
from ml.infer import calibration_info


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
def _model_state() -> dict[str, torch.Tensor]:
    """The shipped state_dict. Cached because the model is frozen."""
    state = torch.load(_MODEL_PATH, map_location="cpu", weights_only=True)
    if hasattr(state, "state_dict"):
        state = state.state_dict()
    return dict(state)


def _architecture_summary() -> tuple[str, int, float]:
    """Layer chain, parameter count and file size (KB) of the shipped model."""
    state = _model_state()
    weights = [k for k in state if k.endswith(".weight")]
    layers = [
        f"Linear({state[k].shape[1]}, {state[k].shape[0]})" for k in weights
    ]
    n_params = int(sum(t.numel() for t in state.values()))
    size_kb = _MODEL_PATH.stat().st_size / 1000.0
    return " -> ReLU -> ".join(layers), n_params, size_kb


def _first_layer_weights() -> pd.DataFrame:
    """Mean |w_i| of each input's first-layer weights, normalized to sum to 1."""
    w = _model_state()["net.0.weight"]  # shape (32, 10) - Linear(in=10, out=32)
    imp = w.abs().mean(dim=0).numpy()  # mean across 32 output dims -> (10,)
    imp_norm = imp / imp.sum()
    return pd.DataFrame({"feature": list(_FEATURE_NAMES), "|w_i|": imp_norm})


st.set_page_config(page_title="About - Amoebanator 25")
render_disclaimer()

st.title("About Amoebanator 25")

info = calibration_info()
T = float(info["T"])  # type: ignore[arg-type]
n_cal = info["n_cal"]


# -- section 1. Model architecture --------------------------------------------
st.subheader("Model architecture")
_chain, _n_params, _size_kb = _architecture_summary()
st.markdown(
    f"Tabular MLP, {_n_params} parameters, {_size_kb:.1f} KB serialized. "
    f"`{_chain}` - binary classifier (PAM risk: Low / High) with two output "
    "logits consumed by softmax + temperature scaling at inference time. "
    "The four continuous inputs (age, CSF glucose, protein and WBC) are "
    "z-scored with the training rows' means and standard deviations "
    "(`outputs/model/scaler.json`); the binary inputs stay 0/1. The layer "
    "shapes, parameter count and size above are read from "
    "`outputs/model/model.pt`."
)


# -- section 2. Training summary ----------------------------------------------
st.subheader("Training data")
st.markdown(
    "**n=30 synthetic rows created for this demo**; their age and sex "
    "distribution does not match the published PAM case series. "
    "Train/val split: n_train=24, n_val=6, `random_state=42`, "
    "`test_size=0.2`, `stratify=y`. Trained with Adam (lr 1e-3) for 500 "
    "full-batch steps, the point where the training loss has converged. "
    "No real PHI. Any clinical evaluation needs a real cohort, and none is "
    "part of this release. See `docs/data_card.md` (Gebru et al. 2021 "
    "datasheet format) for the full lineage."
)


# -- section 3. Calibration summary -------------------------------------------
st.subheader("Calibration")
_n_txt = f"n={n_cal}" if n_cal else "the"
_calibration = (
    "Temperature scaling (Guo et al. 2017), fitted by L-BFGS on the "
    f"{_n_txt} validation rows. Current `T = {T:.6f}`. "
)
if info["val_separated"]:
    _calibration += (
        "The raw logits already classify every validation row correctly: "
        "the rows are perfectly separated, so the validation loss has no "
        "finite minimum in T and the temperature is not identifiable. "
    )
    if abs(T - 1.0) < 1e-3:
        _calibration += (
            "The fit leaves T essentially at its starting value of 1.0, so "
            "the probabilities the Predict page shows are the model's own "
            "softmax outputs. "
        )
    else:
        _calibration += "The reported T is where the optimizer stopped. "
    _calibration += (
        "Treat T as a property of these six rows, not as evidence about the "
        "model's calibration. "
    )
elif T < 1.0:
    _calibration += "T < 1, so temperature scaling sharpens the probabilities. "
else:
    _calibration += "T > 1, so temperature scaling softens the probabilities. "
st.markdown(
    _calibration + "See `docs/model_card.md` section Caveats for the full discussion."
)


# -- section 4. First-layer weight magnitudes ----------------------
st.subheader("First-layer weight magnitudes (model-level)")
imp_df = _first_layer_weights()
st.bar_chart(imp_df, x="feature", y="|w_i|", horizontal=True)

# Weight-panel caption (model-level text).
st.caption(
    "Mean |w_i| of each input's weights in the first Linear layer, "
    "normalized to sum to 1. The inputs are standardized (continuous "
    "inputs in training-SD units, binary inputs 0/1), so the magnitudes "
    "are on comparable scales, but they describe only the first of three "
    "layers: they are not a measure of each input's influence on the "
    "output, and not per-prediction attribution. No per-prediction "
    "attribution method (such as SHAP) is implemented. "
    f"Current range: {imp_df['|w_i|'].min():.1%} to "
    f"{imp_df['|w_i|'].max():.1%}, max/min ratio "
    f"{imp_df['|w_i|'].max() / imp_df['|w_i|'].min():.2f}x."
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
    n = int(n_cal) if n_cal else 0  # the shipped calibration-set size
    k = finite_sample_rank(n, alpha)
    st.markdown(
        f"With `n_cal = {n}`, `alpha = {parse_alpha(alpha)}` -> "
        f"`k = ceil((n+1)(1-alpha)) = {k}`."
    )
    if n >= k and n >= 100:
        st.success(
            "ASYMPTOTIC: coverage >= 1-alpha holds on average under "
            "exchangeability; with untied scores the finite-sample bound "
            "1-alpha + 1/(n+1) is tight."
        )
    elif n >= k:
        st.info(
            "FINITE-SAMPLE: split conformal coverage still holds on average "
            f"under exchangeability, but with n = {n} the realized "
            "coverage varies widely."
        )
    else:
        st.error(
            f"INVALID: k = {k} > n = {n}, so no finite threshold "
            "guarantees 1-alpha coverage; qhat is +inf and every input "
            f"abstains. This alpha needs at least {min_calibration_rows(alpha)} "
            "calibration rows."
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
