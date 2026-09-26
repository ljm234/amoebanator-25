"""Six bacterial and viral vignettes checked case by case.

The cases are bact_064, bact_062, and bact_082 (bacterial) and vir_092,
vir_105, and vir_118 (viral). One test per case checks its demographics,
anchor PMID, and the clinical anchor feature of that case. The cross-case
tests check that none of the six has freshwater exposure, the HSV-1
imaging pattern, dengue platelets below 150,000, the pre-adjudication
hold_for_revision state, and that PMID_REGISTRY holds all six anchor PMIDs
and not the 18626302 typo.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

_REPO_ROOT = Path(__file__).resolve().parent.parent
if str(_REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(_REPO_ROOT))

from ml.schemas.vignette import VignetteSchema  # noqa: E402
from scripts.vignettes.generate_pam_vignettes import PMID_REGISTRY  # noqa: E402


_BACT_DIR = _REPO_ROOT / "data" / "vignettes" / "v2" / "class_02_bacterial"
_VIR_DIR = _REPO_ROOT / "data" / "vignettes" / "v2" / "class_03_viral"


_SIX_CASE_PATHS = [
    _BACT_DIR / "bact_064_sp_lima_pediatric.json",
    _BACT_DIR / "bact_062_sp_netherlands_adult.json",
    _BACT_DIR / "bact_082_nm_college_outbreak.json",
    _VIR_DIR / "vir_092_hsv1_adult.json",
    _VIR_DIR / "vir_105_enterovirus_pediatric.json",
    _VIR_DIR / "vir_118_dengue_loreto.json",
]


def _load(path: Path) -> VignetteSchema:
    return VignetteSchema.model_validate(json.loads(path.read_text(encoding="utf-8")))


def _result_for(v: VignetteSchema, test_name: str) -> str | None:
    for r in v.diagnostic_tests.results:
        if r.test_name == test_name:
            return r.result
    return None


# ----------------------------------------------------------------------
# Per-case tests (6) - clinical anchor invariants
# ----------------------------------------------------------------------


def test_bact_064_lima_pediatric_anchor():
    """bact_064 (v64): SP Lima ped 18mo M, PMID 27831604 (Davalos 2016)."""
    v = _load(_BACT_DIR / "bact_064_sp_lima_pediatric.json")
    assert v.demographics.geography_region == "peru_lima_coast"
    assert v.demographics.age_years == 1
    assert v.demographics.sex == "male"
    assert v.ground_truth_class == 2
    assert "27831604" in v.provenance.inclusion_decision_rationale
    assert v.literature_anchors[0].pmid == "27831604"
    culture = _result_for(v, "csf_culture")
    assert culture is not None and "streptococcus_pneumoniae" in culture


def test_bact_062_netherlands_adult_anchor():
    """bact_062 (v62): SP Netherlands adult 55F, PMID 15509818 (van de Beek 2004)."""
    v = _load(_BACT_DIR / "bact_062_sp_netherlands_adult.json")
    assert v.demographics.geography_region == "other_global"
    assert v.demographics.age_years == 55
    assert v.demographics.sex == "female"
    assert v.ground_truth_class == 2
    assert "15509818" in v.provenance.inclusion_decision_rationale
    assert v.literature_anchors[0].pmid == "15509818"
    culture = _result_for(v, "csf_culture")
    assert culture is not None and "streptococcus_pneumoniae" in culture


def test_bact_082_nm_adult_anchor_notes_pmid_typo():
    """bact_082 (v82): NM Netherlands adult 24M, PMID 18626301 (Heckenberg 2008)."""
    v = _load(_BACT_DIR / "bact_082_nm_college_outbreak.json")
    assert v.demographics.geography_region == "other_global"
    assert v.demographics.age_years == 24
    assert v.demographics.sex == "male"
    assert v.ground_truth_class == 2
    assert "18626301" in v.provenance.inclusion_decision_rationale
    assert v.literature_anchors[0].pmid == "18626301"
    assert v.exam.petechial_or_purpuric_rash is True
    culture = _result_for(v, "csf_culture")
    assert culture is not None and "neisseria_meningitidis" in culture
    # The narrative notes the 18626302 PMID typo
    narrative_en = v.narrative_en or ""
    assert "18626302" in narrative_en, "note about 18626302 typo missing"


def test_vir_092_hsv1_anchor_with_temporal_imaging():
    """vir_092 (v92): HSV-1 adult 42M, PMID 16675036 (Whitley 2006 Antiviral Res)."""
    v = _load(_VIR_DIR / "vir_092_hsv1_adult.json")
    assert v.demographics.age_years == 42
    assert v.demographics.sex == "male"
    assert v.ground_truth_class == 3
    assert "16675036" in v.provenance.inclusion_decision_rationale
    assert v.literature_anchors[0].pmid == "16675036"
    # HSV-1 imaging requirement
    assert v.imaging.imaging_pattern == "mesial_temporal_t2_flair_hyperintensity"
    pcr = _result_for(v, "csf_hsv1_pcr")
    assert pcr == "positive"


def test_vir_105_enterovirus_pmn_predominant_ambiguity():
    """vir_105 (v105): EV ped 5M Greece, PMID 17668054 (Michos 2007 PMN-cohort)."""
    v = _load(_VIR_DIR / "vir_105_enterovirus_pediatric.json")
    assert v.demographics.age_years == 5
    assert v.demographics.sex == "male"
    assert v.ground_truth_class == 3
    assert "17668054" in v.provenance.inclusion_decision_rationale
    assert v.literature_anchors[0].pmid == "17668054"
    # Michos cohort PMN-predominance: this case deliberately PMN > 50 percent
    assert v.csf.csf_neutrophil_pct > 50
    pcr = _result_for(v, "csf_enterovirus_pcr")
    assert pcr == "positive"
    # Diagnostic ambiguity disclosure in rationale
    rat = v.provenance.inclusion_decision_rationale.lower()
    assert "ambiguity" in rat
    assert "csf_neutrophil_predominant_in_confirmed_viral" in rat


def test_vir_118_dengue_peru_low_platelets():
    """vir_118 (v118): dengue Loreto 32F, PMID 30540031 (Bastos 2018 dengue CNS Amazonia)."""
    v = _load(_VIR_DIR / "vir_118_dengue_loreto.json")
    assert v.demographics.geography_region == "peru_loreto_amazon"
    assert v.demographics.age_years == 32
    assert v.demographics.sex == "female"
    assert v.ground_truth_class == 3
    assert "30540031" in v.provenance.inclusion_decision_rationale
    assert v.literature_anchors[0].pmid == "30540031"
    # Dengue requirement: platelets below 150,000
    assert v.labs.platelets_per_uL < 150000
    pcr = _result_for(v, "denv_pcr")
    assert pcr is not None and "DENV_2" in pcr


# ----------------------------------------------------------------------
# Cross-case invariant tests (5)
# ----------------------------------------------------------------------


def test_all_six_cases_freshwater_exposure_false():
    """None of the six cases has freshwater exposure."""
    for path in _SIX_CASE_PATHS:
        v = _load(path)
        assert v.exposure.freshwater_exposure_within_14d is False, str(path)
        assert v.exposure.freshwater_exposure_type is None, str(path)


def test_vir_092_canonical_hsv1_imaging():
    """HSV-1 imaging pattern is mesial_temporal_t2_flair_hyperintensity."""
    v = _load(_VIR_DIR / "vir_092_hsv1_adult.json")
    assert v.imaging.imaging_pattern == "mesial_temporal_t2_flair_hyperintensity"


def test_vir_118_dengue_platelets_below_150k():
    """Dengue case has platelets below 150,000 per microliter."""
    v = _load(_VIR_DIR / "vir_118_dengue_loreto.json")
    assert v.labs.platelets_per_uL < 150000


def test_all_six_cases_pre_adjudication_hold_for_revision():
    """All six cases are in the pre-adjudication hold_for_revision state.

    The schema's AdjudicationMetadata has a fixed 5-field structure, so the
    structured pre-adjudication disclosure was embedded into
    anchoring_documentation, preserving the hold_for_revision phrase
    verbatim. This test checks both the inclusion_decision enum value and
    the verbatim-phrase disclosure inside anchoring_documentation.
    """
    for path in _SIX_CASE_PATHS:
        v = _load(path)
        assert v.adjudication.inclusion_decision == "hold_for_revision", str(path)
        assert (
            "self_review_disposition=hold_for_revision"
            in v.adjudication.anchoring_documentation
        ), str(path)
        assert (
            "stage=pre_adjudication"
            in v.adjudication.anchoring_documentation
        ), str(path)
        assert v.adjudication.cohen_kappa == 0.0, str(path)


def test_pmid_registry_contains_all_six_anchor_pmids_and_no_18626302():
    """Registry integrity: the 6 anchor PMIDs are present and the typo is not.

    Six anchor PMIDs (one per case): 27831604 (Davalos), 15509818 (van de
    Beek), 18626301 (Heckenberg, corrected from the typo 18626302), 16675036
    (Whitley HSE), 17668054 (Michos), 30540031 (Bastos 2018). The typo
    18626302 must not be in the registry.
    """
    expected = {
        "27831604", "15509818", "18626301",
        "16675036", "17668054", "30540031",
    }
    for pmid in expected:
        assert pmid in PMID_REGISTRY, f"missing anchor PMID {pmid}"
    assert "18626302" not in PMID_REGISTRY, (
        "typo PMID 18626302 is still in PMID_REGISTRY"
    )
