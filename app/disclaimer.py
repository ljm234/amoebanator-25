"""Disclaimer + accessibility CSS injection for the web layer.

Three responsibilities, one module:

1. ``DISCLAIMER_TEXT``       - the disclaimer banner that
                                appears on every page. Tested for 5
                                mandatory tokens via the parametrized
                                ``test_disclaimer_contains_mandatory_token``.
2. ``_INJECTED_CSS``          - wash + border + deep-text WCAG-AA color
                                pattern for the error / warning / info /
                                success alert boxes, plus a
                                ``prefers-reduced-motion`` block. Single
                                source of truth - NO competing CSS in
                                other modules.
3. ``wcag_contrast_ratio()``  - hand-rolled relative-luminance ratio
                                math (WCAG 2.0). No axe-core dep. Used
                                by ``test_app_disclaimer.py`` to assert
                                each color combo achieves the
                                AA threshold of 4.5:1.

The render function injects the CSS, then renders the disclaimer with
``st.markdown`` as ordinary page text, not as an alert box. The CSS
restyles the alert boxes the pages render with ``st.error`` /
``st.warning`` / ``st.info`` / ``st.success``.
"""
from __future__ import annotations

import streamlit as st


# Disclaimer banner text. The 5
# mandatory tokens enforced by tests/test_app_disclaimer.py:
#   - "NOT a medical device"
#   - "n=30"
#   - "limited to"
#   - "ORCID"
#   - "jordanmontenegroc.99@gmail.com"
# Source URL: github.com/ljm234/amoebanator-25
DISCLAIMER_TEXT: str = (
    "Research prototype, NOT a medical device. Trained on n=30 "
    "synthetic patient vignettes (n_train=24, n_val=6); contains zero "
    "real PHI. Outputs are temperature-scaled probabilities (T fit on "
    "n=6 validation rows), **limited to** "
    "the n=30 training distribution - not diagnoses. Not for clinical "
    "decision support, not validated. Source + caveats: "
    "github.com/ljm234/amoebanator-25 - Contact: "
    "jordanmontenegroc.99@gmail.com (ORCID 0009-0000-7851-7139)"
)


# WCAG-AA color combos. Each combo clears the AA threshold of 4.5:1;
# measured contrast ranges 5.27:1 (warning) to 7.56:1 (info). The
# wash+border+deep-text pattern preserves visual hierarchy without
# alarmist tone:
# light wash background + 4px deep-saturation accent border + deep
# saturation text on the wash.
#
# Selectors: in Streamlit 1.52 an alert renders as div.stAlert holding a
# [data-testid="stAlertContainer"] box, and only the inner content node names
# the kind, as data-testid="stAlertContent<Kind>". The first rule makes the
# box transparent and unpadded, with its 0.2 s transition switched off so the
# change is not animated; each kind rule then puts the wash, border, text
# color and padding on the content node itself. The rules use plain
# attribute selectors (no :has()), so they apply on the first render too.
_INJECTED_CSS: str = """
<style>
/* -- WCAG-AA contrast pattern ------------------------------ */
.stAlert [data-testid="stAlertContainer"] {
    background: transparent;
    padding: 0;
    transition: none;
}
.stAlert [data-testid^="stAlertContent"] {
    padding: 1rem;
    border-radius: 0.5rem;
}
.stAlert [data-testid="stAlertContentError"] {
    background: #FFEBEE;            /* light red wash */
    border-left: 4px solid #B71C1C; /* deep red accent */
    color: #B71C1C;                 /* deep red text - contrast 5.75:1 */
}
.stAlert [data-testid="stAlertContentWarning"] {
    background: #FFF8E1;            /* light amber wash */
    border-left: 4px solid #BF360A; /* deep orange accent */
    color: #BF360A;                 /* deep orange text - contrast 5.27:1 */
}
.stAlert [data-testid="stAlertContentInfo"] {
    background: #E3F2FD;            /* light blue wash */
    border-left: 4px solid #0D47A1; /* deep blue accent (theme primary) */
    color: #0D47A1;                 /* deep blue text - contrast 7.56:1 */
}
.stAlert [data-testid="stAlertContentSuccess"] {
    background: #E8F5E9;            /* light green wash */
    border-left: 4px solid #1B5E20; /* deep green accent */
    color: #1B5E20;                 /* deep green text - contrast 7.00:1 */
}

/* -- prefers-reduced-motion -------------------------------- */
@media (prefers-reduced-motion: reduce) {
    *, *::before, *::after {
        animation-duration: 0.01ms !important;
        animation-iteration-count: 1 !important;
        transition-duration: 0.01ms !important;
    }
    .stSpinner { display: none !important; }
}
</style>
"""


def _channel_to_linear(c_srgb_byte: int) -> float:
    """Convert one sRGB channel byte (0-255) to linear-light (0-1).

    Per WCAG 2.0 relative-luminance formula:
      if c_srgb <= 0.03928: c_linear = c_srgb / 12.92
      else:                c_linear = ((c_srgb + 0.055) / 1.055) ** 2.4
    """
    c_srgb = c_srgb_byte / 255.0
    if c_srgb <= 0.03928:
        return c_srgb / 12.92
    return float(((c_srgb + 0.055) / 1.055) ** 2.4)


def _hex_to_relative_luminance(hex_color: str) -> float:
    """Compute WCAG 2.0 relative luminance from a ``#RRGGBB`` hex string."""
    h = hex_color.lstrip("#")
    if len(h) != 6:
        raise ValueError(f"expected #RRGGBB hex string, got {hex_color!r}")
    r = int(h[0:2], 16)
    g = int(h[2:4], 16)
    b = int(h[4:6], 16)
    r_lin = _channel_to_linear(r)
    g_lin = _channel_to_linear(g)
    b_lin = _channel_to_linear(b)
    return 0.2126 * r_lin + 0.7152 * g_lin + 0.0722 * b_lin


def wcag_contrast_ratio(text_hex: str, bg_hex: str) -> float:
    """Return the WCAG 2.0 contrast ratio between two ``#RRGGBB`` colors.

    Ratio is symmetric: ``(L_lighter + 0.05) / (L_darker + 0.05)``,
    range 1.0 (identical) to 21.0 (black-on-white). WCAG-AA threshold
    for normal text is 4.5:1; AAA is 7.0:1.
    """
    l1 = _hex_to_relative_luminance(text_hex)
    l2 = _hex_to_relative_luminance(bg_hex)
    lighter = max(l1, l2)
    darker = min(l1, l2)
    return (lighter + 0.05) / (darker + 0.05)


def render_disclaimer() -> None:
    """Inject the WCAG-AA + reduced-motion CSS and render the disclaimer.

    Called at the top of every page. Idempotent under Streamlit's rerun
    model (CSS injection is harmless to re-emit). The disclaimer is
    rendered with ``st.markdown`` as ordinary page text, not as an alert
    box; the injected CSS restyles the alert boxes that the pages render
    with ``st.error`` / ``st.warning`` / ``st.info`` / ``st.success``.
    """
    st.markdown(_INJECTED_CSS, unsafe_allow_html=True)
    st.markdown(DISCLAIMER_TEXT)
