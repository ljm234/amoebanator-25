"""WCAG-AA contrast and disclaimer-token assertions for ``app.disclaimer``.

These tests parse the colors out of the actual injected CSS (rather than
hard-coding a copy), so they stay in sync with ``_INJECTED_CSS``: if a color
is changed, the ratio is re-derived and re-checked. They back the claim in the
module docstring that every alert combo clears the WCAG-AA threshold of 4.5:1,
and that the disclaimer banner carries its mandatory tokens.
"""
from __future__ import annotations

import re

import pytest

from app.disclaimer import DISCLAIMER_TEXT, _INJECTED_CSS, wcag_contrast_ratio

AA_THRESHOLD = 4.5

# Pull (kind, foreground, background) out of each alert rule. Streamlit 1.52
# marks the alert kind only on the inner content node
# (data-testid="stAlertContent<Kind>"), so each rule styles that node.
_ALERT_BLOCK = re.compile(
    r'\.stAlert\s+\[data-testid="stAlertContent(?P<kind>[A-Z]\w+)"\]\s*\{'
    r"[^}]*?background:\s*(?P<bg>#[0-9A-Fa-f]{6})"
    r"[^}]*?color:\s*(?P<fg>#[0-9A-Fa-f]{6})",
    re.DOTALL,
)

ALERT_COMBOS: list[tuple[str, str, str]] = [
    (m.group("kind").lower(), m.group("fg"), m.group("bg"))
    for m in _ALERT_BLOCK.finditer(_INJECTED_CSS)
]

MANDATORY_TOKENS = (
    "NOT a medical device",
    "n=30",
    "limited to",
    "ORCID",
    "jordanmontenegroc.99@gmail.com",
)


def test_four_alert_combos_parsed() -> None:
    """The injected CSS defines exactly the four expected alert kinds."""
    kinds = {kind for kind, _, _ in ALERT_COMBOS}
    assert kinds == {"error", "warning", "info", "success"}


def test_alert_selectors_match_streamlit_markup() -> None:
    """
    The rules target the markup the pinned Streamlit frontend renders: the
    ``stAlert`` wrapper class and the ``stAlertContainer`` /
    ``stAlertContent<Kind>`` test ids, not a ``kind`` attribute. Streamlit 1.52
    puts no ``kind`` attribute on any alert element, so a ``[kind=...]``
    selector would match nothing.
    """
    import streamlit
    from pathlib import Path

    assert "[kind=" not in _INJECTED_CSS
    assert ":has(" not in _INJECTED_CSS  # :has() rules missed the first render in Chrome
    bundle = "".join(
        p.read_text(encoding="utf-8", errors="ignore")
        for p in (Path(streamlit.__file__).parent / "static" / "static" / "js").glob("index.*.js")
    )
    # every rule is scoped under the .stAlert wrapper that AlertElement renders
    assert 'className:"stAlert","data-testid":"stAlert"' in bundle
    assert '"data-testid":"stAlertContainer"' in bundle
    assert "stAlertContent${" in bundle


def test_outer_alert_box_rule_exists() -> None:
    """
    The kind rules color the inner content node; the outer
    [data-testid="stAlertContainer"] box must be made transparent, unpadded
    and untransitioned, or Streamlit's default wash and padding frame every
    alert (and its 0.2 s transition delays the change).
    """
    m = re.search(
        r'\.stAlert\s+\[data-testid="stAlertContainer"\]\s*\{(?P<body>[^}]*)\}',
        _INJECTED_CSS,
    )
    assert m, "outer alert box rule missing from _INJECTED_CSS"
    body = m.group("body")
    assert re.search(r"background:\s*transparent", body)
    assert re.search(r"padding:\s*0(?:px|rem|em)?\s*(?:;|$)", body)
    assert re.search(r"transition:\s*none", body)


@pytest.mark.parametrize("kind, fg, bg", ALERT_COMBOS)
def test_alert_combo_meets_aa(kind: str, fg: str, bg: str) -> None:
    """Each alert's text-on-wash contrast clears the AA threshold of 4.5:1."""
    ratio = wcag_contrast_ratio(fg, bg)
    assert ratio >= AA_THRESHOLD, (
        f"{kind}: {fg} on {bg} = {ratio:.2f}:1 < {AA_THRESHOLD}"
    )


# Contrast ratios documented inline in the ``app.disclaimer`` CSS comments,
# pinned here against the WCAG 2.0 computation so a comment can never silently
# drift from the math (2 dp, the precision the comments are written to).
CLAIMED_RATIOS: dict[str, float] = {
    "error": 5.75,
    "warning": 5.27,
    "info": 7.56,
    "success": 7.00,
}


@pytest.mark.parametrize("kind, fg, bg", ALERT_COMBOS)
def test_alert_combo_ratio_matches_claim(kind: str, fg: str, bg: str) -> None:
    """Each combo's computed ratio equals the value claimed in the CSS comment."""
    assert round(wcag_contrast_ratio(fg, bg), 2) == CLAIMED_RATIOS[kind]


def test_reference_black_on_white_is_21() -> None:
    """Maximum contrast (black on white) is 21:1."""
    assert abs(wcag_contrast_ratio("#000000", "#FFFFFF") - 21.0) < 0.01


def test_reference_identical_colors_is_1() -> None:
    """Identical colors have the minimum contrast ratio of 1:1."""
    assert abs(wcag_contrast_ratio("#777777", "#777777") - 1.0) < 1e-9


@pytest.mark.parametrize("token", MANDATORY_TOKENS)
def test_disclaimer_contains_mandatory_token(token: str) -> None:
    """The disclaimer banner carries every mandatory safety/contact token."""
    assert token in DISCLAIMER_TEXT
