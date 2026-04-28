"""Tests for app/app.py — Phase 4.5 Mini-2 T2.5 (4 of 4).

Covers the multi-page nav entry: 4 pages registered with absolute
path resolution + correct titles + icons + landing-page order.
"""
from __future__ import annotations

from pathlib import Path

from streamlit.testing.v1 import AppTest


APP_PATH = "app/app.py"


def test_module_imports_cleanly() -> None:
    at = AppTest.from_file(APP_PATH)
    at.run(timeout=30)
    assert len(at.exception) == 0


def test_app_app_boots_to_predict_landing() -> None:
    """First page in nav dict is Predict; AppTest renders that as default."""
    at = AppTest.from_file(APP_PATH)
    at.run(timeout=30)
    # Predict page renders 'PAM Risk Prediction' title
    assert "PAM Risk Prediction" in [t.value for t in at.title]


def test_4_pages_registered() -> None:
    """Source-level check: app/app.py registers exactly 4 pages."""
    src = Path(APP_PATH).read_text(encoding="utf-8")
    # Count st.Page() invocations
    assert src.count("st.Page(") == 4


def test_pages_resolved_to_absolute_paths() -> None:
    """T2.4 fix: paths must resolve via _PAGES_DIR (Path(__file__).parent.parent)."""
    src = Path(APP_PATH).read_text(encoding="utf-8")
    assert "_PAGES_DIR" in src
    assert "Path(__file__).resolve().parent.parent" in src


def test_predict_page_registered() -> None:
    src = Path(APP_PATH).read_text(encoding="utf-8")
    assert "01_predict.py" in src
    assert 'title="Predict"' in src


def test_audit_page_registered() -> None:
    src = Path(APP_PATH).read_text(encoding="utf-8")
    assert "02_audit.py" in src
    assert 'title="Audit"' in src


def test_about_page_registered() -> None:
    src = Path(APP_PATH).read_text(encoding="utf-8")
    assert "03_about.py" in src
    assert 'title="About"' in src


def test_references_page_registered() -> None:
    src = Path(APP_PATH).read_text(encoding="utf-8")
    assert "04_references.py" in src
    assert 'title="References"' in src


def test_page_icons_present() -> None:
    """All 4 pages have explicit icons."""
    src = Path(APP_PATH).read_text(encoding="utf-8")
    for icon in ["🔬", "📜", "ℹ️", "📚"]:
        assert icon in src, f"page icon {icon!r} missing"


def test_app_app_boots_under_5s() -> None:
    """Mini-2 closure gate criterion #3 inherits this — boot must stay <5s."""
    import time
    t0 = time.time()
    at = AppTest.from_file(APP_PATH)
    at.run(timeout=10)
    elapsed = time.time() - t0
    assert elapsed < 5.0, f"app/app.py boot took {elapsed:.2f}s"
    assert len(at.exception) == 0
