"""Bacterial vignettes anchored to Bijlsma 2016 and to N. meningitidis and Hib sources.

11 vignettes: Bijlsma 6 SP NL cohort + 5 NM/Hib re-anchored to MacNeil 2018
CID, Marcus 2022 OFID, Park 2022 JOGH, and Soeters 2018 CID. 1 ambiguity case
(v84 NM Loreto infant). 2 Peru anchors (v84 Loreto, v86 Cusco). The 2
Mylonakis 2002 Listeria slots (v88/v89) were removed (full-text verification
standard not met).

Each JSON must exist, validate, and match its BACTERIAL_DISTRIBUTION slot.
Across the set the tests check the bacterial CSF profile, no freshwater
exposure, the pre-adjudication hold, the ambiguity and Peru-anchored cases,
the pathogen mix, and the absence of em and en dashes.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import pytest

_REPO_ROOT = Path(__file__).resolve().parent.parent
if str(_REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(_REPO_ROOT))

from ml.schemas.vignette import VignetteSchema  # noqa: E402
from scripts.vignettes.generate_pam_vignettes import BACTERIAL_DISTRIBUTION  # noqa: E402


BACT_WAVE2_IDS = [61, 63, 68, 70, 72, 74, 83, 84, 85, 86, 87]
BACT_WAVE2_AMBIGUITY_IDS = {84}
BACT_WAVE2_PERU_IDS = {84, 86}
WAVE2_DIR = _REPO_ROOT / "data" / "vignettes" / "v2" / "class_02_bacterial"


def _wave2_slot(vid: int) -> dict:
    return next(s for s in BACTERIAL_DISTRIBUTION if s["vignette_id"] == vid)


def _wave2_json_path(vid: int) -> Path:
    matches = list(WAVE2_DIR.glob(f"bact_{vid:03d}_*.json"))
    assert len(matches) == 1, f"v{vid}: expected 1 match, got {matches!r}"
    return matches[0]


def _load(vid: int) -> dict:
    return json.loads(_wave2_json_path(vid).read_text(encoding="utf-8"))


# ----------------------------------------------------------------------
# Parametrized over the 11 vignettes
# ----------------------------------------------------------------------


@pytest.mark.parametrize("vid", BACT_WAVE2_IDS)
def test_bact_files_exist(vid):
    matches = list(WAVE2_DIR.glob(f"bact_{vid:03d}_*.json"))
    assert len(matches) == 1, f"v{vid} JSON missing or duplicate: {matches}"


@pytest.mark.parametrize("vid", BACT_WAVE2_IDS)
def test_bact_schema_validates(vid):
    VignetteSchema.model_validate(_load(vid))


@pytest.mark.parametrize("vid", BACT_WAVE2_IDS)
def test_bact_demographics_match_spec(vid):
    data = _load(vid)
    spec = _wave2_slot(vid)
    assert data["demographics"]["age_years"] == spec["age_years"], f"v{vid} age"
    assert data["demographics"]["sex"] == spec["sex"], f"v{vid} sex"
    assert (
        data["demographics"]["geography_region"] == spec["geography_region"]
    ), f"v{vid} region"


@pytest.mark.parametrize("vid", BACT_WAVE2_IDS)
def test_bact_anchor_pmid_matches(vid):
    data = _load(vid)
    spec = _wave2_slot(vid)
    assert data["literature_anchors"][0]["pmid"] == spec["pmid"], f"v{vid} PMID"


# ----------------------------------------------------------------------
# Invariants across the set
# ----------------------------------------------------------------------


def test_bact_freshwater_false():
    """No freshwater exposure in any Class 2 vignette."""
    for vid in BACT_WAVE2_IDS:
        data = _load(vid)
        assert (
            data["exposure"]["freshwater_exposure_within_14d"] is False
        ), f"v{vid}"


def test_bact_class_id_2():
    for vid in BACT_WAVE2_IDS:
        assert _load(vid)["ground_truth_class"] == 2, f"v{vid}"


def test_bact_csf_neutrophilic():
    """CSF is neutrophilic (>=50 percent). Listeria can be lower
    clinically; per spec, build at floor."""
    for vid in BACT_WAVE2_IDS:
        pct = _load(vid)["csf"]["csf_neutrophil_pct"]
        assert pct >= 50, f"v{vid} csf_neutrophil_pct={pct}"


def test_bact_csf_glucose_low():
    for vid in BACT_WAVE2_IDS:
        glucose = _load(vid)["csf"]["csf_glucose_mg_per_dL"]
        assert glucose <= 40, f"v{vid} csf_glucose_mg_per_dL={glucose}"


def test_bact_csf_protein_high():
    for vid in BACT_WAVE2_IDS:
        protein = _load(vid)["csf"]["csf_protein_mg_per_dL"]
        assert protein >= 100, f"v{vid} csf_protein_mg_per_dL={protein}"


def test_bact_pre_adjudication_hold():
    """Every vignette is on hold_for_revision, stated verbatim in anchoring_documentation."""
    for vid in BACT_WAVE2_IDS:
        data = _load(vid)
        assert (
            data["adjudication"]["inclusion_decision"] == "hold_for_revision"
        ), f"v{vid}"
        assert (
            "self_review_disposition=hold_for_revision"
            in data["adjudication"]["anchoring_documentation"]
        ), f"v{vid}"


# ----------------------------------------------------------------------
# Set-level checks
# ----------------------------------------------------------------------


def test_bact_ambiguity_count():
    """Exactly 1 of 11 (v84 NM Loreto infant) carries ambiguity markers."""
    ambiguous = []
    for vid in BACT_WAVE2_IDS:
        rationale = (
            _load(vid)["provenance"].get("inclusion_decision_rationale") or ""
        ).lower()
        if "diagnostic_ambiguity=true" in rationale or "type=" in rationale:
            ambiguous.append(vid)
    assert set(ambiguous) == BACT_WAVE2_AMBIGUITY_IDS, (
        f"Expected {BACT_WAVE2_AMBIGUITY_IDS}, got {set(ambiguous)}"
    )


def test_bact_peru_anchors():
    """Exactly 2 of 11 (v84, v86) are Peru-anchored."""
    peru = [
        vid for vid in BACT_WAVE2_IDS
        if _load(vid)["demographics"]["geography_region"].startswith("peru")
    ]
    assert set(peru) == BACT_WAVE2_PERU_IDS, (
        f"Expected {BACT_WAVE2_PERU_IDS}, got {set(peru)}"
    )


def test_bact_pathogen_distribution():
    """6 SP + 3 NM + 2 Hib (the 2 Listeria slots were removed)."""
    counts: dict[str, int] = {}
    for vid in BACT_WAVE2_IDS:
        p = _wave2_slot(vid)["pathogen"]
        counts[p] = counts.get(p, 0) + 1
    assert counts == {
        "S_pneumoniae": 6,
        "N_meningitidis": 3,
        "H_influenzae": 2,
    }, f"pathogen distribution: {counts}"


def test_bact_no_em_dashes():
    """No em-dashes (\\u2014) or en-dashes (\\u2013)."""
    for vid in BACT_WAVE2_IDS:
        text = _wave2_json_path(vid).read_text(encoding="utf-8")
        assert chr(0x2014) not in text, f"v{vid} contains em-dash"
        assert chr(0x2013) not in text, f"v{vid} contains en-dash"
