"""Tests for pages/03_about.py — Phase 4.5 Mini-2 T2.5 (2 of 4)."""
from __future__ import annotations

from pathlib import Path

from streamlit.testing.v1 import AppTest


PAGE_PATH = "pages/03_about.py"


def test_module_imports_cleanly() -> None:
    at = AppTest.from_file(PAGE_PATH)
    at.run(timeout=30)
    assert len(at.exception) == 0


def test_about_page_renders_disclaimer() -> None:
    at = AppTest.from_file(PAGE_PATH)
    at.run(timeout=30)
    blob = "\n".join(m.value for m in at.markdown)
    for tok in [
        "NOT a medical device",
        "n=30",
        "limited to",
        "ORCID",
        "lmontenegrocalla@mail.weber.edu",
    ]:
        assert tok in blob, f"missing disclaimer token {tok!r}"


def test_about_page_title() -> None:
    at = AppTest.from_file(PAGE_PATH)
    at.run(timeout=30)
    assert "About Amoebanator 25" in [t.value for t in at.title]


def test_5_subheaders_present() -> None:
    at = AppTest.from_file(PAGE_PATH)
    at.run(timeout=30)
    subs = [s.value for s in at.subheader]
    expected = {
        "Model architecture",
        "Training data",
        "Calibration",
        "Feature importance (model-level)",
        "Authorship",
    }
    assert expected.issubset(set(subs))


def test_w_i_caption_contains_q17c_phrases() -> None:
    """Q17.C verbatim caption phrases."""
    at = AppTest.from_file(PAGE_PATH)
    at.run(timeout=30)
    captions = "\n".join(c.value for c in at.caption)
    for phrase in [
        "NOT per-prediction attribution",
        "model treats all 10 features near-equally",
        "n=30 training set limitation",
        "SHAP",
        "Phase 6",
    ]:
        assert phrase in captions, f"missing Q17.C phrase {phrase!r}"


def test_alpha_slider_present() -> None:
    """Q4.A: Advanced expander hosts an α slider over {0.05, 0.10, 0.20}."""
    at = AppTest.from_file(PAGE_PATH)
    at.run(timeout=30)
    sliders = [s.label for s in at.slider]
    assert any("α" in s or "alpha" in s.lower() for s in sliders)


def test_3_state_regime_badge_invalid_at_default() -> None:
    """Default α=0.10 with n=6 → k=7 > 6 → 🔴 INVALID badge."""
    at = AppTest.from_file(PAGE_PATH)
    at.run(timeout=30)
    errors = [e.value for e in at.error]
    assert any("🔴 INVALID" in e for e in errors)


def test_handle_disclosure_one_liner_present() -> None:
    """Q19.D: 'Repo: github.com/ljm234/amoebanator-25 — HuggingFace Space: ...
    (same author, separate handles).'"""
    at = AppTest.from_file(PAGE_PATH)
    at.run(timeout=30)
    captions = "\n".join(c.value for c in at.caption)
    assert "github.com/ljm234/amoebanator-25" in captions
    assert "huggingface.co/spaces/luisjordanmontenegro/amoebanator-25" in captions
    assert "same author, separate handles" in captions


def test_orcid_in_authorship_section() -> None:
    """ORCID 0009-0000-7851-7139 appears under Authorship subheader."""
    at = AppTest.from_file(PAGE_PATH)
    at.run(timeout=30)
    blob = "\n".join(m.value for m in at.markdown)
    assert "0009-0000-7851-7139" in blob


def test_w_i_panel_uses_real_model_pt() -> None:
    """The page imports torch and reads outputs/model/model.pt at render time."""
    src = Path(PAGE_PATH).read_text(encoding="utf-8")
    assert "outputs/model/model.pt" in src
    assert "import torch" in src or "from torch" in src


def test_about_page_renders_under_5s() -> None:
    import time
    t0 = time.time()
    at = AppTest.from_file(PAGE_PATH)
    at.run(timeout=10)
    elapsed = time.time() - t0
    assert elapsed < 5.0, f"about page boot took {elapsed:.2f}s"
    assert len(at.exception) == 0
