"""Tests for pages/04_references.py — Phase 4.5 Mini-2 T2.5 (3 of 4)."""
from __future__ import annotations

from pathlib import Path

from streamlit.testing.v1 import AppTest


PAGE_PATH = "pages/04_references.py"


def test_module_imports_cleanly() -> None:
    at = AppTest.from_file(PAGE_PATH)
    at.run(timeout=30)
    assert len(at.exception) == 0


def test_references_page_renders_disclaimer() -> None:
    at = AppTest.from_file(PAGE_PATH)
    at.run(timeout=30)
    blob = "\n".join(m.value for m in at.markdown)
    for tok in [
        "NOT a medical device",
        "n=30",
        "limited to",
        "ORCID",
    ]:
        assert tok in blob, f"missing disclaimer token {tok!r}"


def test_references_page_title() -> None:
    at = AppTest.from_file(PAGE_PATH)
    at.run(timeout=30)
    assert "References" in [t.value for t in at.title]


def test_5_categories_rendered() -> None:
    at = AppTest.from_file(PAGE_PATH)
    at.run(timeout=30)
    subs = [s.value for s in at.subheader]
    expected = {
        "PAM clinical",
        "Calibration & conformal prediction",
        "Out-of-distribution detection",
        "Governance & model documentation",
        "Tools",
    }
    assert expected.issubset(set(subs))


def test_22_bib_keys_referenced() -> None:
    """Every entry in docs/references.bib appears in the rendered page."""
    src = Path(PAGE_PATH).read_text(encoding="utf-8")
    expected_keys = [
        "cope2016pam", "yoder2010pam", "capewell2015pam", "cdc2025pam",
        "tunkel2004idsa", "seehusen2003csf",
        "guo2017calibration", "vovk2005alrw", "vovk2013mondrian",
        "lei2018distributionfree", "platt1999probabilistic",
        "niculescu2005calibration",
        "lee2018mahalanobis", "liu2020energy",
        "mitchell2019modelcards", "vasey2022decideai", "collins2024tripodai",
        "collins2015tripod", "gebru2021datasheets", "hipaa2012deident",
        "vickers2006dca",
        "ke2017lightgbm",
    ]
    assert len(expected_keys) == 22
    for key in expected_keys:
        assert key in src, f"bib key {key!r} missing from references page"


def test_pam_clinical_includes_cope2016() -> None:
    """Spot-check: Cope 2016 PAM review must appear in PAM clinical section."""
    at = AppTest.from_file(PAGE_PATH)
    at.run(timeout=30)
    blob = "\n".join(m.value for m in at.markdown)
    assert "cope2016pam" in blob
    assert "Primary Amebic Meningoencephalitis" in blob


def test_governance_includes_mitchell2019() -> None:
    """Spot-check: Mitchell 2019 Model Cards must appear in governance section."""
    at = AppTest.from_file(PAGE_PATH)
    at.run(timeout=30)
    blob = "\n".join(m.value for m in at.markdown)
    assert "mitchell2019modelcards" in blob
    assert "Model Cards" in blob


def test_footer_caption_points_to_repo() -> None:
    at = AppTest.from_file(PAGE_PATH)
    at.run(timeout=30)
    captions = "\n".join(c.value for c in at.caption)
    assert "github.com/ljm234/amoebanator-25" in captions
    assert "references.bib" in captions
