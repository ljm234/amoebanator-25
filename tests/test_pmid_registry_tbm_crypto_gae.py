"""PMID_REGISTRY entries for the TBM, cryptococcal, and GAE anchors.

Checks that the Class 4 (TBM) + Class 5 (Cryptococcal) + Class 6 (GAE)
anchor PMIDs resolve in PMID_REGISTRY with complete Vancouver metadata, a
valid anchor_type, a caveat naming the class each one anchors, and a
well-formed, unique DOI, and that each class has 5 to 7 anchors. All of
these anchors are PubMed-indexed numeric PMIDs.
"""
from __future__ import annotations

import sys
from pathlib import Path

import pytest

_REPO_ROOT = Path(__file__).resolve().parent.parent
if str(_REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(_REPO_ROOT))

from scripts.vignettes.generate_pam_vignettes import PMID_REGISTRY  # noqa: E402


CLASS_4_6_TBM_PMIDS: list[str] = [
    "15496623",  # Thwaites GE et al. NEJM 2004 dexamethasone TBM RCT
    "20822958",  # Marais S et al. Lancet ID 2010 TBM uniform case definition
    "24655399",  # van Toorn R, Solomons R Semin Pediatr Neurol 2014 pediatric TBM
    "26760084",  # Heemskerk AD et al. NEJM 2016 intensified TBM treatment RCT
    "35288778",  # Navarro-Flores A et al. J Neurol 2022 CNS-TB meta-analysis
]

CLASS_4_6_CRYPTO_PMIDS: list[str] = [
    "20047480",  # Perfect JR et al. CID 2010 IDSA cryptococcal guidelines
    "19182676",  # Park BJ et al. AIDS 2009 global HIV cryptococcal burden
    "17262720",  # Singh N et al. JID 2007 transplant cryptococcus calcineurin
    "24963568",  # Boulware DR et al. NEJM 2014 ART timing crypto-IRIS
    "35320642",  # Jarvis JN et al. NEJM 2022 AMBITION-cm single-dose lipo-AmpB
    "19757550",  # Datta K et al. EID 2009 C. gattii Pacific NW expansion
]

CLASS_4_6_GAE_PMIDS: list[str] = [
    "35059659",  # Alvarez P, Bravo F et al. JAAD Int 2022 cutaneous balamuthiasis clinicopathology
    "31758593",  # Cabello-Vilchez AM et al. Neuropathology 2020 fatal GAE Lima Peru pediatric
    "17428307",  # Visvesvara GS et al. FEMS Immunol Med Microbiol 2007 free-living amoebae review
    "30239654",  # Cope JR et al. CID 2019 Balamuthia US 1974-2016 epidemiology
    "34461057",  # Damhorst GL et al. Lancet ID 2022 Acanthamoeba AIDS case report
]

CLASS_4_6_ALL = (
    CLASS_4_6_TBM_PMIDS + CLASS_4_6_CRYPTO_PMIDS + CLASS_4_6_GAE_PMIDS
)

REQUIRED_FIELDS = [
    "authors_full",
    "authors_short",
    "journal",
    "year",
    "doi",
    "title",
    "verification_confidence",
]


@pytest.mark.parametrize("pmid", CLASS_4_6_ALL)
def test_anchor_pmid_in_registry(pmid):
    assert pmid in PMID_REGISTRY, f"PMID/key {pmid!r} not registered"


@pytest.mark.parametrize("pmid", CLASS_4_6_ALL)
def test_anchor_required_fields_present(pmid):
    entry = PMID_REGISTRY[pmid]
    for field in REQUIRED_FIELDS:
        assert field in entry, f"{pmid} missing field {field!r}"
        assert entry[field] not in (None, ""), f"{pmid} field {field!r} is empty"


@pytest.mark.parametrize("pmid", CLASS_4_6_ALL)
def test_anchor_authors_full_is_nonempty_list(pmid):
    authors = PMID_REGISTRY[pmid]["authors_full"]
    assert isinstance(authors, list), f"{pmid} authors_full must be list"
    assert len(authors) >= 1, f"{pmid} authors_full empty"


@pytest.mark.parametrize("pmid", CLASS_4_6_ALL)
def test_anchor_year_int_valid(pmid):
    year = PMID_REGISTRY[pmid]["year"]
    assert isinstance(year, int), f"{pmid} year must be int"
    assert 1990 <= year <= 2026, f"{pmid} year={year} out of range [1990, 2026]"


@pytest.mark.parametrize("pmid", CLASS_4_6_ALL)
def test_anchor_verification_confidence_in_unit_interval(pmid):
    vc = PMID_REGISTRY[pmid]["verification_confidence"]
    assert isinstance(vc, (int, float)), (
        f"{pmid} verification_confidence must be numeric; got {type(vc).__name__}"
    )
    assert 0.0 <= float(vc) <= 1.0, (
        f"{pmid} verification_confidence={vc} out of [0.0, 1.0]"
    )


@pytest.mark.parametrize("pmid", CLASS_4_6_ALL)
def test_anchor_type_present_and_valid(pmid):
    """Each entry carries an explicit anchor_type from the allowed set."""
    entry = PMID_REGISTRY[pmid]
    assert "anchor_type" in entry, f"{pmid} missing anchor_type"
    valid_types = {
        "case_report",
        "guideline",
        "review",
        "surveillance",
        "meta_analysis",
        "cohort",
        "rct",
        "prospective_observational",
        "case_series",
    }
    assert entry["anchor_type"] in valid_types, (
        f"{pmid} anchor_type={entry['anchor_type']!r} not in {valid_types}"
    )


def test_anchor_count_in_target_range():
    """15 to 18 anchors are registered across the three classes."""
    count = len(CLASS_4_6_ALL)
    assert 15 <= count <= 18, (
        f"Anchor count {count} outside [15, 18]"
    )


def test_per_class_anchor_count_in_target_range():
    """Each class has 5 to 7 anchors."""
    assert 5 <= len(CLASS_4_6_TBM_PMIDS) <= 7, (
        f"TBM count {len(CLASS_4_6_TBM_PMIDS)} outside [5,7]"
    )
    assert 5 <= len(CLASS_4_6_CRYPTO_PMIDS) <= 7, (
        f"Crypto count {len(CLASS_4_6_CRYPTO_PMIDS)} outside [5,7]"
    )
    assert 5 <= len(CLASS_4_6_GAE_PMIDS) <= 7, (
        f"GAE count {len(CLASS_4_6_GAE_PMIDS)} outside [5,7]"
    )


def test_anchor_caveat_names_provenance():
    """Each anchor's caveat opens by naming the class it anchors."""
    expected_class = {
        **{p: 4 for p in CLASS_4_6_TBM_PMIDS},
        **{p: 5 for p in CLASS_4_6_CRYPTO_PMIDS},
        **{p: 6 for p in CLASS_4_6_GAE_PMIDS},
    }
    for pmid in CLASS_4_6_ALL:
        entry = PMID_REGISTRY[pmid]
        caveat = (entry.get("caveat") or "") + " " + (entry.get("notes") or "")
        prefix = f"Anchor for Class {expected_class[pmid]} "
        assert caveat.startswith(prefix), (
            f"{pmid} caveat does not start with {prefix!r}: {caveat[:200]!r}"
        )


def test_anchor_doi_pattern_well_formed():
    """Every anchor DOI matches the ISO 26324 DOI pattern."""
    import re
    DOI_RE = re.compile(r"^10\.\d{4,9}/.+$")
    for pmid in CLASS_4_6_ALL:
        doi = PMID_REGISTRY[pmid]["doi"]
        assert DOI_RE.match(doi), f"{pmid} doi={doi!r} not well-formed"


def test_anchor_dois_unique():
    """No two anchors share a DOI."""
    dois = [PMID_REGISTRY[p]["doi"] for p in CLASS_4_6_ALL]
    assert len(set(dois)) == len(dois), (
        f"Duplicate DOI among these anchors: {dois}"
    )
