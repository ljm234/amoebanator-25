"""Utility functions for the Streamlit web layer.

Helpers consumed by `pages/01_predict.py` and the test suite:

- ``build_row``     - coerce 8 form widget values into the dict shape
                      ``ml.infer.infer_one`` accepts.
- ``decision_badge`` - render a Streamlit-markdown badge for the
                       prediction state. Bold label + color tag;
                       meaning preserved when color is stripped
                       (color-blind safety).
- ``_fmt_metric``    - tolerant numeric formatter; returns ``"-"`` for
                       missing / None / non-numeric values so partial
                       inference output dicts never crash the page.
- ``temperature_note`` - tooltip text for the temperature badge, worded
                       from the artifact values.
- ``min_calibration_rows`` - smallest calibration set a given alpha
                       needs for a finite conformal threshold.

Plus the module-level constant ``KNOWN_SYMPTOMS`` - the exact 3 symptoms
in the 30 synthetic rows the model was trained on. Other symptoms
(altered_mental_status, photophobia, nausea_vomiting, seizure) are not
offered because the model never saw them.
"""
from __future__ import annotations

from typing import Any

from ml.conformal_advanced import finite_sample_rank

# Only the 3 symptoms the model scores. Offering more in the UI would
# collect inputs the model ignores.
KNOWN_SYMPTOMS: tuple[str, str, str] = ("fever", "headache", "nuchal_rigidity")


# Bold-label + color mapping. Stripping the color
# tags must leave the bold label legible (achromatopsia + low-vision
# accessibility). The mapping is the single source of truth for badge
# rendering across pages.
_BADGE_MAP: dict[str, tuple[str, str]] = {
    "High":     ("HIGH",     "red"),
    "Low":      ("LOW",      "green"),
    "ABSTAIN":  ("ABSTAIN",  "orange"),
}


def build_row(
    age: int,
    csf_glucose: float,
    csf_protein: float,
    csf_wbc: int,
    pcr: bool,
    microscopy: bool,
    exposure: bool,
    symptoms: list[str],
) -> dict[str, Any]:
    """Convert form widget values to ``ml.infer.infer_one``'s input dict.

    Coerces booleans to int 0/1 (model expects numeric flags), joins the
    symptoms multiselect to a semicolon-delimited string, and strips
    blank tokens so an empty multiselect produces ``""`` rather than
    ``";;"``.

    The 8 keys returned match the form widget names exactly so a fresh
    reader of the page can grep keys -> widgets without indirection.
    """
    cleaned_symptoms = [s for s in symptoms if s and s.strip()]
    return {
        "age": int(age),
        "csf_glucose": float(csf_glucose),
        "csf_protein": float(csf_protein),
        "csf_wbc": int(csf_wbc),
        "pcr": int(bool(pcr)),
        "microscopy": int(bool(microscopy)),
        "exposure": int(bool(exposure)),
        "symptoms": ";".join(cleaned_symptoms),
    }


def decision_badge(prediction: str, reason: str | None = None) -> str:
    """Return a Streamlit-markdown badge for the prediction state.

    Format: ``:<color>[**<LABEL>**]`` for High/Low;
    ``:<color>[**ABSTAIN - <reason>**]`` for ABSTAIN. Empty or
    unrecognized prediction returns the literal ``"unknown"``.

    The bold label conveys the prediction state
    without relying on color, satisfying the color-blind safety
    contract: stripping the ``:<color>[...]`` wrapper still leaves the
    semantic content intact.
    """
    if not prediction:
        return "unknown"

    entry = _BADGE_MAP.get(prediction)
    if entry is None:
        return "unknown"

    label, color = entry
    if prediction == "ABSTAIN":
        suffix = reason if reason else "unspecified"
        return f":{color}[**{label} - {suffix}**]"
    return f":{color}[**{label}**]"


def _fmt_metric(out: dict[str, Any], key: str, fmt: str = "{:.3f}") -> str:
    """Format ``out[key]`` via ``fmt``; return ``"-"`` for missing values.

    Tolerates the three failure modes that occur in real inference output
    dicts: (1) the key is absent (some inference branches don't populate
    every field), (2) the value is ``None``, (3) the value is
    non-numeric (string sentinel, garbage). All three render as
    ``"-"`` (ASCII hyphen) so the page renders cleanly without ``KeyError``
    or ``TypeError``.
    """
    value = out.get(key)
    if value is None:
        return "-"
    try:
        return fmt.format(float(value))
    except (TypeError, ValueError):
        return "-"


def temperature_note(T: float, n_cal: int | None, separated: bool | None) -> str:
    """Tooltip text for the temperature badge, stated from the artifacts."""
    n_txt = f"the n={n_cal} validation rows" if n_cal else "the validation rows"
    note = f"Temperature scaling (Guo et al. 2017), fit by L-BFGS on {n_txt}. "
    if separated:
        note += (
            "Those rows are perfectly separated, so the validation loss has "
            "no finite minimum in T and the temperature is not identifiable. "
        )
        if abs(T - 1.0) < 1e-3:
            note += (
                f"The fit leaves T at {T:.6f}, essentially its starting value "
                "of 1.0, because the loss is already near zero there. The "
                "probabilities are the model's own softmax outputs."
            )
        else:
            note += f"T = {T:.4g} is where the optimizer stopped."
    elif T < 1.0:
        note += f"T = {T:.4g} is below 1, so it sharpens the model's probabilities."
    else:
        note += f"T = {T:.4g} is above 1, so it softens the model's probabilities."
    return note + " See docs/model_card.md section 9."


def min_calibration_rows(alpha: float) -> int:
    """Smallest calibration-set size n with k = ceil((n+1)(1-alpha)) <= n."""
    n = 1
    while finite_sample_rank(n, alpha) > n and n < 1_000_000:
        n += 1
    return n
