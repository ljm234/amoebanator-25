"""Tests for the vignettes built by scripts/vignettes/generate_pam_vignettes.py.

Covers the PAM vignettes, the bacterial and viral distributions, and the
PMID registry; each section below says what it checks.

The PAM_DISTRIBUTION_1_20, PAM_DISTRIBUTION_21_60, BACTERIAL_DISTRIBUTION,
VIRAL_DISTRIBUTION and PMID_REGISTRY in
``scripts/vignettes/generate_pam_vignettes.py`` are the source of truth for these
tests.
"""
from __future__ import annotations

import re
from typing import Any

import pytest

from ml.schemas.vignette import VignetteSchema
from scripts.vignettes.generate_pam_vignettes import PMID_REGISTRY


pytestmark = pytest.mark.pam_vignettes


# ----------------------------------------------------------------------
# Helpers
# ----------------------------------------------------------------------


def _walk_strings(node: Any):
    """Yield every str leaf in a nested dict/list structure."""
    if isinstance(node, str):
        yield node
    elif isinstance(node, dict):
        for v in node.values():
            yield from _walk_strings(v)
    elif isinstance(node, list):
        for item in node:
            yield from _walk_strings(item)


# ----------------------------------------------------------------------
# 1. Schema validation across all 20 vignettes
# ----------------------------------------------------------------------


def test_all_20_vignettes_load_valid_schema(generated_vignettes):
    assert len(generated_vignettes) == 20
    for vignette in generated_vignettes:
        VignetteSchema.model_validate(vignette)


# ----------------------------------------------------------------------
# 2. PMID_REGISTRY metadata completeness
# ----------------------------------------------------------------------


_REQUIRED_PMID_KEYS = {
    "pmid", "doi", "journal", "journal_short_code", "year", "volume",
    "issue", "pages", "authors_short", "authors_full", "anchor_type",
    "verification_confidence", "last_verified_date",
}
_PMID_DIGIT_RE = re.compile(r"^\d{7,8}$")
_DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
# Acceptable verification dates: the first PubMed check of the PAM anchors,
# the corrections check that followed, and the canonical-anchor check.
_VALID_VERIFICATION_DATES = {
    "2026-05-03", "2026-05-04", "2026-05-05",
    # 10 Bacterial + Viral consensus anchors added (van de Beek, Tunkel,
    # Bijlsma, Mylonakis, Heckenberg, Soeters, Whitley, Tunkel-encephalitis,
    # Granerod, Tyler) at verification_confidence=0.85, pending a direct
    # check against the PubMed record.
    "2026-05-06",
    # 5 new primary-source anchors added, checked against the PubMed record
    # on 2026-05-07 (Davalos 2016 Lima cohort 27831604, Heckenberg 2008
    # 18626301 corrected from 18626302, Whitley 2006 Antiviral Res HSE adult
    # review 16675036, Michos 2007 PLoS One enterovirus PMN-predominant cohort
    # 17668054, Munayco 2024 MMWR Peru dengue outbreak). The dengue vignette
    # vir_118 is now anchored to Bastos 2018 30540031 and Puccioni-Sohler 2023
    # 38157877, both last checked on 2026-06-10.
    "2026-05-07",
    # 16 Class 4 (TBM) + Class 5 (Cryptococcal) + Class 6 (GAE) anchor
    # PMIDs added, each checked against the PubMed record on 2026-05-11
    # (Thwaites NEJM 2004, Marais Lancet ID 2010, van Toorn Semin Pediatr
    # Neurol 2014, Heemskerk NEJM 2016, Navarro-Flores J Neurol 2022;
    # Perfect CID 2010, Park AIDS 2009, Singh JID 2007, Boulware NEJM 2014,
    # Jarvis NEJM 2022 AMBITION-cm, Datta EID 2009; Alvarez/Bravo JAAD Int
    # 2022, Cabello-Vilchez Neuropathology 2020, Visvesvara FEMS 2007,
    # Cope CID 2019, Damhorst Lancet ID 2022).
    "2026-05-11",
    # Correction (2026-05-30): removed PMID 32935747, a composite entry
    # whose PMID, DOI and author list came from three different papers;
    # the 5 NM/Hib slots (v83-v87) were re-anchored to 4 real
    # papers, each checked against the PubMed/PMC record on 2026-05-30:
    # MacNeil 2018 CID 29126310, Marcus 2022 OFID 35493127, Park 2022 JOGH
    # 35265327, Soeters 2018 CID 29509834.
    "2026-05-30",
    # Correction (2026-05-31): deleted both Mylonakis 2002 Listeria
    # vignettes (v88/v89; full-text check standard not met) and checked 3
    # BACT anchors against the PubMed full text on 2026-05-31: Tunkel 2004
    # CID 15494903, Bijlsma 2016 Lancet ID 26652862, Heckenberg 2008
    # Medicine 18626301. (van de Beek 15509818 was checked on 2026-05-30.)
    "2026-05-31",
    # Dates of the June 2026 PubMed check of the remaining anchors.
    "2026-06-06", "2026-06-07", "2026-06-08",
    "2026-06-09", "2026-06-10", "2026-06-11",
}


# Non-numeric registry keys (none at present) would be tested in
# tests/test_pmid_registry_tbm_crypto_gae.py rather than here, since
# this completeness test enforces a 7-8 digit pmid field via _PMID_DIGIT_RE.
def _numeric_pmid_keys() -> list[str]:
    return sorted(k for k in PMID_REGISTRY.keys() if k.isdigit())


@pytest.mark.parametrize("pmid", _numeric_pmid_keys())
def test_pmid_metadata_completeness(pmid, pmid_registry):
    meta = pmid_registry[pmid]
    missing = _REQUIRED_PMID_KEYS - set(meta.keys())
    assert not missing, f"PMID {pmid} missing keys: {missing}"
    assert _PMID_DIGIT_RE.match(meta["pmid"]), \
        f"PMID {pmid} has malformed pmid string: {meta['pmid']!r}"
    assert meta["pmid"] == pmid, \
        f"PMID {pmid} self-reference mismatch: {meta['pmid']!r}"
    assert meta["journal_short_code"], \
        f"PMID {pmid} has empty journal_short_code"
    assert isinstance(meta["year"], int) and 1990 <= meta["year"] <= 2030, \
        f"PMID {pmid} year out of range: {meta['year']!r}"
    assert _DATE_RE.match(meta["last_verified_date"]), \
        f"PMID {pmid} last_verified_date not YYYY-MM-DD: " \
        f"{meta['last_verified_date']!r}"
    assert meta["last_verified_date"] in _VALID_VERIFICATION_DATES, (
        f"PMID {pmid} last_verified_date {meta['last_verified_date']!r} "
        f"not in approved verification dates "
        f"{sorted(_VALID_VERIFICATION_DATES)}"
    )
    assert meta["verification_confidence"], \
        f"PMID {pmid} verification_confidence is empty"


# ----------------------------------------------------------------------
# 3. Cluster distribution
# ----------------------------------------------------------------------


_EXPECTED_CLUSTERS: dict[str, set[int]] = {
    "splash_pad": {1, 2, 3, 4},
    "lake_pond": {5, 6, 7, 8, 9},
    "nasal_irrigation": {10, 11, 12},
    "hot_springs": {13, 14},
    "pakistan_ablution": {15, 16},
    "latam": {17, 18},
    "survivor_adult": {19},
    "survivor_pediatric": {20},
}


def test_cluster_distribution_matches_spec(distribution):
    actual: dict[str, set[int]] = {}
    for spec in distribution:
        actual.setdefault(spec["cluster"], set()).add(spec["vignette_id"])
    assert actual == _EXPECTED_CLUSTERS


# ----------------------------------------------------------------------
# 4. Demographic distribution
# ----------------------------------------------------------------------
#
# The tests assert the data: Female={2,5,11,12,14}=5 and
# Adult={10,11,12,14,16,19}=6.


_FATAL_IDS = set(range(1, 19))
_SURVIVOR_IDS = {19, 20}
_FEMALE_IDS = {2, 5, 11, 12, 14}
_MALE_IDS = set(range(1, 21)) - _FEMALE_IDS
_ADULT_IDS = {10, 11, 12, 14, 16, 19}
_PEDIATRIC_IDS = set(range(1, 21)) - _ADULT_IDS


def test_demographic_distribution_matches_spec(distribution):
    by_id = {s["vignette_id"]: s for s in distribution}
    assert {i for i, s in by_id.items() if s["outcome"] == "fatal"} == _FATAL_IDS
    assert {i for i, s in by_id.items() if s["outcome"] == "survived"} == _SURVIVOR_IDS
    assert {i for i, s in by_id.items() if s["sex"] == "female"} == _FEMALE_IDS
    assert {i for i, s in by_id.items() if s["sex"] == "male"} == _MALE_IDS
    assert {i for i, s in by_id.items() if s["age_years"] >= 18} == _ADULT_IDS
    assert {i for i, s in by_id.items() if s["age_years"] < 18} == _PEDIATRIC_IDS
    # Sanity: counts add to 20
    assert len(_FATAL_IDS) + len(_SURVIVOR_IDS) == 20
    assert len(_FEMALE_IDS) + len(_MALE_IDS) == 20
    assert len(_ADULT_IDS) + len(_PEDIATRIC_IDS) == 20


# ----------------------------------------------------------------------
# 5. No em-dashes (or en-dashes) in generated content
# ----------------------------------------------------------------------


def test_no_em_dashes_in_content(generated_vignettes):
    em = 0
    en = 0
    for vignette in generated_vignettes:
        for s in _walk_strings(vignette):
            em += s.count(chr(0x2014))  # em-dash
            en += s.count(chr(0x2013))  # en-dash
    assert em == 0, f"Found {em} em-dash(es) in generated content"
    assert en == 0, f"Found {en} en-dash(es) in generated content"


# ----------------------------------------------------------------------
# 6. Spanish narratives have proper UTF-8 accents
# ----------------------------------------------------------------------


_SPANISH_ACCENT_CHARS = set("áéíóúñÁÉÍÓÚÑ")
# Tokens universal across the 20 narratives (verified empirically).
# "presentó" and "ingresó" both appear but are mutually exclusive per
# vignette: cases that present comatose use "ingresó en coma" instead
# of "presentó". "años" is absent from the 16-month-old infant case.
# These five tokens cover CSF/imaging language present in every case.
_REQUIRED_SPANISH_TOKENS = (
    "líquido", "presión", "cefalorraquídeo", "días", "mostró",
)


def test_spanish_narratives_have_proper_accents(generated_vignettes):
    for vignette in generated_vignettes:
        case_id = vignette["case_id"]
        narrative_es = vignette["narrative_es"]
        accent_chars = _SPANISH_ACCENT_CHARS & set(narrative_es)
        assert accent_chars, (
            f"{case_id} narrative_es contains no UTF-8 Spanish accents"
        )
        for token in _REQUIRED_SPANISH_TOKENS:
            assert token in narrative_es, (
                f"{case_id} narrative_es missing accented token "
                f"{token!r} (likely an unaccented spelling slipped in)"
            )


# ----------------------------------------------------------------------
# 7. Survivor vs fatal outcome consistency
# ----------------------------------------------------------------------


def test_survivor_vignettes_have_correct_outcome(generated_vignettes):
    by_id = {v["case_id"].split("-")[1]: v for v in generated_vignettes}
    # Survivors: 19, 20
    for vid_str in ("019", "020"):
        v = by_id[vid_str]
        anchoring = v["adjudication"]["anchoring_documentation"].lower()
        assert "outcome=survived" in anchoring, (
            f"vignette {vid_str} adjudication missing outcome=survived "
            f"({anchoring[:120]}...)"
        )
        narrative_en = v["narrative_en"].lower()
        assert "died" not in narrative_en, (
            f"vignette {vid_str} survivor narrative_en contains 'died'"
        )
        assert "survivor" in narrative_en or "discharged" in narrative_en, (
            f"vignette {vid_str} narrative_en lacks survivor/discharged "
            f"language"
        )
        narrative_es = v["narrative_es"].lower()
        assert (
            "sobreviviente" in narrative_es
            or "egresado" in narrative_es
            or "egresada" in narrative_es
        ), (
            f"vignette {vid_str} narrative_es lacks "
            f"sobreviviente/egresado language"
        )
    # Fatal: 1-18
    for i in range(1, 19):
        vid_str = f"{i:03d}"
        v = by_id[vid_str]
        anchoring = v["adjudication"]["anchoring_documentation"].lower()
        assert "outcome=fatal" in anchoring, (
            f"vignette {vid_str} adjudication missing outcome=fatal"
        )


# ----------------------------------------------------------------------
# 8. literature_anchors[0].pmid matches PAM_DISTRIBUTION_1_20 assignment
# ----------------------------------------------------------------------


def test_pmid_assignments_match_distribution(distribution, generated_vignettes):
    by_id = {s["vignette_id"]: s for s in distribution}
    for vignette in generated_vignettes:
        vignette_id = int(vignette["case_id"].split("-")[1])
        spec = by_id[vignette_id]
        anchor_pmid = vignette["literature_anchors"][0]["pmid"]
        assert anchor_pmid == spec["pmid"], (
            f"vignette {vignette_id} literature_anchor pmid "
            f"{anchor_pmid!r} != distribution pmid {spec['pmid']!r}"
        )


# ----------------------------------------------------------------------
# 9. case_id format
# ----------------------------------------------------------------------


_ALLOWED_JOURNAL_CODES = {
    "MMWR", "JCM", "CID", "IDCases", "AJTMH", "EID", "IJP",
    # Vancouver MEDLINE-style abbreviations (canonical forms set 2026-05-04):
    "Emerg Infect Dis", "Front Microbiol", "Front Med (Lausanne)",
    "Pathogens", "Front Pediatr", "BMC Infect Dis", "J Trop Pediatr",
    "TexMed", "JPIDS", "EpidemiolInfect", "ExpertRevAntiInfect",
    # Vignettes 21-25:
    "Diagnostics", "Yonsei Med J", "Pediatrics",
}
# Journal portion may now contain spaces and parentheses (Vancouver style).
# Use a non-greedy capture for the journal segment, terminated by `-NNNN-`
# (a 4-digit year) so the journal can include any chars except newline.
_CASE_ID_RE = re.compile(
    r"^PAM-(\d{3})-(.+?)-(\d{4})-(.+)$"
)


def test_case_id_format(generated_vignettes):
    seen_ids: set[str] = set()
    for vignette in generated_vignettes:
        case_id = vignette["case_id"]
        assert case_id not in seen_ids, f"duplicate case_id: {case_id}"
        seen_ids.add(case_id)
        m = _CASE_ID_RE.match(case_id)
        assert m, f"case_id {case_id!r} does not match pattern"
        nnn, journal, year, tail = m.groups()
        assert 1 <= int(nnn) <= 20, f"case_id {case_id} NNN out of range"
        assert journal in _ALLOWED_JOURNAL_CODES, (
            f"case_id {case_id} journal {journal!r} not in "
            f"{sorted(_ALLOWED_JOURNAL_CODES)}"
        )
        assert 1990 <= int(year) <= 2030, (
            f"case_id {case_id} year {year} out of range"
        )
        assert tail, f"case_id {case_id} missing region/cluster tail"


# ======================================================================
# Distribution of PAM vignettes 21-60 (40 vignettes)
# ----------------------------------------------------------------------
# Tests below validate the PAM_DISTRIBUTION_21_60 data structure in
# scripts/vignettes/generate_pam_vignettes.py.
# ======================================================================


_EXPECTED_CLUSTERS_21_60: dict[str, set[int]] = {
    "splash_pad": {23, 25, 50, 51, 52},
    "lake_pond": {22, 24, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40},
    "river": {21, 41, 42, 43, 44, 45, 46, 47, 48, 49},
    "nasal_irrigation": {53, 54, 55, 56, 57, 58},
    "hot_springs": {59},
    "pakistan_ablution": {60},
}

_FILENAME_21_60_RE = re.compile(
    r"^pam_(\d{3})_[a-z][a-z0-9_]*\.json$"
)

_REUSE_CAP = 6


def test_v21_v60_distribution_length(distribution_21_60):
    assert len(distribution_21_60) == 40, (
        f"PAM_DISTRIBUTION_21_60 has {len(distribution_21_60)} entries, expected 40"
    )


def test_v21_v60_vignette_ids_contiguous(distribution_21_60):
    ids = sorted(s["vignette_id"] for s in distribution_21_60)
    assert ids == list(range(21, 61)), (
        f"Vignette_ids 21-60 not contiguous: {ids}"
    )


def test_v21_v60_cluster_distribution_matches_spec(distribution_21_60):
    actual: dict[str, set[int]] = {}
    for spec in distribution_21_60:
        actual.setdefault(spec["cluster"], set()).add(spec["vignette_id"])
    assert actual == _EXPECTED_CLUSTERS_21_60, (
        f"Cluster distribution of vignettes 21-60 does not match spec.\n"
        f"  expected: {_EXPECTED_CLUSTERS_21_60}\n"
        f"  actual:   {actual}"
    )


def test_v21_v60_pmids_in_registry(distribution_21_60, pmid_registry):
    for spec in distribution_21_60:
        assert spec["pmid"] in pmid_registry, (
            f"Vignette {spec['vignette_id']} pmid {spec['pmid']!r} "
            f"not in PMID_REGISTRY"
        )


def test_combined_corpus_size_60(distribution, distribution_21_60):
    assert len(distribution) + len(distribution_21_60) == 60, (
        f"Combined corpus size = {len(distribution) + len(distribution_21_60)}, "
        f"expected 60"
    )


def test_no_id_collisions(distribution, distribution_21_60):
    ids_1_20 = {s["vignette_id"] for s in distribution}
    ids_21_60 = {s["vignette_id"] for s in distribution_21_60}
    assert ids_1_20.isdisjoint(ids_21_60), (
        f"Vignette_ids of vignettes 1-20 and 21-60 overlap: "
        f"{sorted(ids_1_20 & ids_21_60)}"
    )


def test_no_filename_collisions(distribution, distribution_21_60):
    files_1_20 = {s["filename"] for s in distribution}
    files_21_60 = {s["filename"] for s in distribution_21_60}
    assert files_1_20.isdisjoint(files_21_60), (
        f"Filenames of vignettes 1-20 and 21-60 overlap: "
        f"{sorted(files_1_20 & files_21_60)}"
    )


def test_v21_v60_filename_format(distribution_21_60):
    for spec in distribution_21_60:
        fname = spec["filename"]
        m = _FILENAME_21_60_RE.match(fname)
        assert m, (
            f"Vignette {spec['vignette_id']} filename {fname!r} "
            f"does not match pam_NNN_<tag>.json"
        )
        nnn = int(m.group(1))
        assert nnn == spec["vignette_id"], (
            f"filename {fname!r} NNN={nnn} != vignette_id {spec['vignette_id']}"
        )


def test_pmid_reuse_cap(distribution, distribution_21_60):
    counts: dict[str, int] = {}
    for spec in distribution:
        counts[spec["pmid"]] = counts.get(spec["pmid"], 0) + 1
    for spec in distribution_21_60:
        counts[spec["pmid"]] = counts.get(spec["pmid"], 0) + 1
    over_cap = {p: n for p, n in counts.items() if n > _REUSE_CAP}
    assert not over_cap, (
        f"PMIDs over reuse cap {_REUSE_CAP}x: {over_cap}"
    )


def test_v21_v60_sex_enum(distribution_21_60):
    for spec in distribution_21_60:
        assert spec["sex"] in {"male", "female"}, (
            f"Vignette {spec['vignette_id']} has invalid sex "
            f"{spec['sex']!r}"
        )


def test_v21_v60_outcome_enum(distribution_21_60):
    for spec in distribution_21_60:
        assert spec["outcome"] in {"fatal", "survived"}, (
            f"Vignette {spec['vignette_id']} has invalid outcome "
            f"{spec['outcome']!r}"
        )


def test_v21_v60_stage_enum(distribution_21_60):
    for spec in distribution_21_60:
        assert spec["stage"] in {"early", "mid", "late"}, (
            f"Vignette {spec['vignette_id']} has invalid stage "
            f"{spec['stage']!r}"
        )


def test_combined_demographic_balance(distribution, distribution_21_60):
    combined = list(distribution) + list(distribution_21_60)
    n = len(combined)
    female = sum(1 for s in combined if s["sex"] == "female")
    adult = sum(1 for s in combined if s["age_years"] >= 18)
    assert female / n >= 0.20, (
        f"Combined female ratio {female}/{n} = {female/n:.2%} < 20% "
        f"(design target 22%; floor 20% allowed)"
    )
    assert adult / n >= 0.25, (
        f"Combined adult ratio {adult}/{n} = {adult/n:.2%} < 25%"
    )


def test_combined_outcome_balance(distribution, distribution_21_60):
    combined = list(distribution) + list(distribution_21_60)
    n = len(combined)
    fatal = sum(1 for s in combined if s["outcome"] == "fatal")
    survived = sum(1 for s in combined if s["outcome"] == "survived")
    assert fatal / n >= 0.90, (
        f"Combined fatal ratio {fatal}/{n} = {fatal/n:.2%} < 90%"
    )
    assert survived / n >= 0.08, (
        f"Combined survivor ratio {survived}/{n} = {survived/n:.2%} < 8%"
    )


def test_combined_geographic_balance(distribution, distribution_21_60):
    combined = list(distribution) + list(distribution_21_60)
    n = len(combined)
    us_labels = {
        "Arkansas, US", "Florida, US", "Louisiana, US", "Texas, US",
        "Minnesota, US", "Nebraska, US", "California, US",
        "US South region", "Texas (Rio Grande), US",
    }
    non_us = sum(1 for s in combined if s["geography_label"] not in us_labels)
    assert non_us / n >= 0.30, (
        f"Combined non-US ratio {non_us}/{n} = {non_us/n:.2%} < 30%"
    )


def test_v21_v60_special_cases_present(distribution_21_60):
    by_pmid = {s["pmid"]: s for s in distribution_21_60}
    assert "39795618" in by_pmid, "Phung 2025 cryptic-exposure anchor missing"
    assert "39606118" in by_pmid, "Lin 2024 atypical-myocarditis anchor missing"
    assert "37727924" in by_pmid, "Hong 2023 travel-imported anchor missing"
    assert "25667249" in by_pmid, "Linam 2015 Kali Hardig survivor anchor missing"


# ======================================================================
# Content tests for PAM vignettes 21-25
# ----------------------------------------------------------------------
# These tests validate the 5 JSON files of vignettes 21-25.
# Each of these vignettes is anchored to a primary-source case report
# checked against its PubMed record; as each file's
# inclusion_decision_rationale records, the vitals and some labs are
# imputed from the literature.
# ======================================================================

import json
from pathlib import Path

_PAM_DATA_DIR = Path(__file__).resolve().parents[2] / "data" / "vignettes" / "pam"
_IDS_21_25 = [21, 22, 23, 24, 25]


@pytest.fixture(scope="session")
def vignettes_21_25(distribution_21_60):
    """Load the JSON files of vignettes 21-25 from disk."""
    out: dict[int, dict[str, Any]] = {}
    by_id = {s["vignette_id"]: s for s in distribution_21_60}
    for vid in _IDS_21_25:
        spec = by_id[vid]
        fpath = _PAM_DATA_DIR / spec["filename"]
        out[vid] = {
            "spec": spec,
            "path": fpath,
            "data": json.loads(fpath.read_text(encoding="utf-8")),
        }
    return out


@pytest.mark.parametrize("vid", _IDS_21_25)
def test_v21_25_file_exists(vid, vignettes_21_25):
    entry = vignettes_21_25[vid]
    assert entry["path"].exists(), f"v{vid} JSON {entry['path']} missing"


@pytest.mark.parametrize("vid", _IDS_21_25)
def test_v21_25_schema_validates(vid, vignettes_21_25):
    entry = vignettes_21_25[vid]
    VignetteSchema.model_validate(entry["data"])


@pytest.mark.parametrize("vid", _IDS_21_25)
def test_v21_25_demographics_match_spec(vid, vignettes_21_25):
    entry = vignettes_21_25[vid]
    spec = entry["spec"]
    demo = entry["data"]["demographics"]
    assert demo["age_years"] == spec["age_years"], (
        f"v{vid}: JSON age_years={demo['age_years']} != spec {spec['age_years']}"
    )
    assert demo["sex"] == spec["sex"], (
        f"v{vid}: JSON sex={demo['sex']!r} != spec {spec['sex']!r}"
    )
    assert demo["geography_region"] == spec["geography_region"], (
        f"v{vid}: JSON geography_region={demo['geography_region']!r} != spec "
        f"{spec['geography_region']!r}"
    )


@pytest.mark.parametrize("vid", _IDS_21_25)
def test_v21_25_anchor_pmid_matches(vid, vignettes_21_25):
    entry = vignettes_21_25[vid]
    anchors = entry["data"]["literature_anchors"]
    assert anchors, f"v{vid}: empty literature_anchors"
    assert anchors[0]["pmid"] == entry["spec"]["pmid"], (
        f"v{vid}: anchor pmid {anchors[0]['pmid']!r} != "
        f"spec pmid {entry['spec']['pmid']!r}"
    )


@pytest.mark.parametrize("vid", _IDS_21_25)
def test_v21_25_narrative_min_length(vid, vignettes_21_25):
    entry = vignettes_21_25[vid]
    en = entry["data"].get("narrative_en") or ""
    es = entry["data"].get("narrative_es") or ""
    assert len(en) >= 100, f"v{vid} narrative_en too short ({len(en)} chars)"
    assert len(es) >= 100, f"v{vid} narrative_es too short ({len(es)} chars)"


@pytest.mark.parametrize("vid", _IDS_21_25)
def test_v21_25_narrative_cites_anchor_pmid(vid, vignettes_21_25):
    entry = vignettes_21_25[vid]
    pmid = entry["spec"]["pmid"]
    en = entry["data"].get("narrative_en") or ""
    es = entry["data"].get("narrative_es") or ""
    needle = f"PMID {pmid}"
    assert needle in en, f"v{vid} narrative_en missing '{needle}'"
    assert needle in es, f"v{vid} narrative_es missing '{needle}'"


def test_v25_outcome_survived(vignettes_21_25):
    v25 = vignettes_21_25[25]
    spec = v25["spec"]
    assert spec["outcome"] == "survived", (
        f"v25 spec outcome {spec['outcome']!r} expected 'survived'"
    )
    anchoring = v25["data"]["adjudication"]["anchoring_documentation"].lower()
    assert "outcome=survived" in anchoring, (
        f"v25 adjudication missing outcome=survived "
        f"(anchoring snippet: {anchoring[:120]}...)"
    )
    en = v25["data"]["narrative_en"].lower()
    assert "survived" in en, "v25 narrative_en missing 'survived'"
    assert "miltefosine" in en, "v25 narrative_en missing miltefosine reference"


def test_v23_atypical_features_in_narrative(vignettes_21_25):
    v23 = vignettes_21_25[23]
    en = v23["data"]["narrative_en"].lower()
    es = v23["data"]["narrative_es"].lower()
    for token in ("myocarditis", "ecmo", "indoor heated"):
        assert token in en, f"v23 narrative_en missing {token!r}"
    for token in ("miocarditis", "ecmo", "piscina"):
        assert token in es, f"v23 narrative_es missing {token!r}"


def test_v21_25_no_em_dashes(vignettes_21_25):
    em = chr(0x2014)
    en_dash = chr(0x2013)
    for vid in _IDS_21_25:
        content = vignettes_21_25[vid]["path"].read_text(encoding="utf-8")
        assert content.count(em) == 0, f"v{vid} contains {em} em-dash(es)"
        assert content.count(en_dash) == 0, f"v{vid} contains {en_dash} en-dash(es)"


# ======================================================================
# Content tests for PAM vignettes 26-40
# ----------------------------------------------------------------------
# These tests validate the 15 JSON files of vignettes 26-40. Each uses
# imputation_within_anchor_epidemiology.
# ======================================================================

_IDS_26_40 = list(range(26, 41))


@pytest.fixture(scope="session")
def vignettes_26_40(distribution_21_60):
    out: dict[int, dict[str, Any]] = {}
    by_id = {s["vignette_id"]: s for s in distribution_21_60}
    for vid in _IDS_26_40:
        spec = by_id[vid]
        fpath = _PAM_DATA_DIR / spec["filename"]
        out[vid] = {
            "spec": spec,
            "path": fpath,
            "data": json.loads(fpath.read_text(encoding="utf-8")),
        }
    return out


@pytest.mark.parametrize("vid", _IDS_26_40)
def test_v26_40_file_exists(vid, vignettes_26_40):
    entry = vignettes_26_40[vid]
    assert entry["path"].exists(), f"v{vid} JSON {entry['path']} missing"


@pytest.mark.parametrize("vid", _IDS_26_40)
def test_v26_40_schema_validates(vid, vignettes_26_40):
    entry = vignettes_26_40[vid]
    VignetteSchema.model_validate(entry["data"])


@pytest.mark.parametrize("vid", _IDS_26_40)
def test_v26_40_demographics_match_spec(vid, vignettes_26_40):
    entry = vignettes_26_40[vid]
    spec = entry["spec"]
    demo = entry["data"]["demographics"]
    assert demo["age_years"] == spec["age_years"]
    assert demo["sex"] == spec["sex"]
    assert demo["geography_region"] == spec["geography_region"]


@pytest.mark.parametrize("vid", _IDS_26_40)
def test_v26_40_anchor_pmid_matches(vid, vignettes_26_40):
    entry = vignettes_26_40[vid]
    anchors = entry["data"]["literature_anchors"]
    assert anchors and anchors[0]["pmid"] == entry["spec"]["pmid"]


@pytest.mark.parametrize("vid", _IDS_26_40)
def test_v26_40_narrative_min_length(vid, vignettes_26_40):
    entry = vignettes_26_40[vid]
    en = entry["data"].get("narrative_en") or ""
    es = entry["data"].get("narrative_es") or ""
    assert len(en) >= 100, f"v{vid} narrative_en too short ({len(en)} chars)"
    assert len(es) >= 100, f"v{vid} narrative_es too short ({len(es)} chars)"


@pytest.mark.parametrize("vid", _IDS_26_40)
def test_v26_40_narrative_cites_anchor_pmid(vid, vignettes_26_40):
    entry = vignettes_26_40[vid]
    pmid = entry["spec"]["pmid"]
    needle = f"PMID {pmid}"
    en = entry["data"].get("narrative_en") or ""
    es = entry["data"].get("narrative_es") or ""
    assert needle in en, f"v{vid} narrative_en missing '{needle}'"
    assert needle in es, f"v{vid} narrative_es missing '{needle}'"


@pytest.mark.parametrize("vid", _IDS_26_40)
def test_v26_40_narrative_imputation_disclosure(vid, vignettes_26_40):
    """Each narrative of vignettes 26-40 must honestly disclose imputation basis."""
    entry = vignettes_26_40[vid]
    en = (entry["data"].get("narrative_en") or "").lower()
    # Phrases that disclose how missing values were imputed.
    disclosures = (
        "imputation", "imputed", "within-cohort", "within the anchor",
    )
    assert any(p in en for p in disclosures), (
        f"v{vid} narrative_en missing imputation disclosure "
        f"(expected one of {disclosures})"
    )


def test_v26_40_no_em_dashes(vignettes_26_40):
    em = chr(0x2014)
    en_dash = chr(0x2013)
    for vid in _IDS_26_40:
        content = vignettes_26_40[vid]["path"].read_text(encoding="utf-8")
        assert content.count(em) == 0, f"v{vid} contains em-dash"
        assert content.count(en_dash) == 0, f"v{vid} contains en-dash"


# ======================================================================
# Content tests for PAM vignettes 41-60
# ----------------------------------------------------------------------
# These tests validate the 20 JSON files of vignettes 41-60, a mix of primary-source-anchored
# newcomers (Zhou, Sazzad, Retana, DeNapoli, Wei, Cope), reuses of PMIDs
# from vignettes 1-20 (Lares-Villa, Rauf, Dulski, Eger, Yoder 2012 x2, Smith,
# Sandi, Burki - different demographics within the same anchor), and
# Tier-3/4 within-cohort imputations (Capewell river, Gharpure x3).
# ======================================================================

_IDS_41_60 = list(range(41, 61))


@pytest.fixture(scope="session")
def vignettes_41_60(distribution_21_60):
    out: dict[int, dict[str, Any]] = {}
    by_id = {s["vignette_id"]: s for s in distribution_21_60}
    for vid in _IDS_41_60:
        spec = by_id[vid]
        fpath = _PAM_DATA_DIR / spec["filename"]
        out[vid] = {
            "spec": spec,
            "path": fpath,
            "data": json.loads(fpath.read_text(encoding="utf-8")),
        }
    return out


@pytest.mark.parametrize("vid", _IDS_41_60)
def test_v41_60_file_exists(vid, vignettes_41_60):
    entry = vignettes_41_60[vid]
    assert entry["path"].exists(), f"v{vid} JSON {entry['path']} missing"


@pytest.mark.parametrize("vid", _IDS_41_60)
def test_v41_60_schema_validates(vid, vignettes_41_60):
    entry = vignettes_41_60[vid]
    VignetteSchema.model_validate(entry["data"])


@pytest.mark.parametrize("vid", _IDS_41_60)
def test_v41_60_demographics_match_spec(vid, vignettes_41_60):
    entry = vignettes_41_60[vid]
    spec = entry["spec"]
    demo = entry["data"]["demographics"]
    assert demo["age_years"] == spec["age_years"]
    assert demo["sex"] == spec["sex"]
    assert demo["geography_region"] == spec["geography_region"]


@pytest.mark.parametrize("vid", _IDS_41_60)
def test_v41_60_anchor_pmid_matches(vid, vignettes_41_60):
    entry = vignettes_41_60[vid]
    anchors = entry["data"]["literature_anchors"]
    assert anchors and anchors[0]["pmid"] == entry["spec"]["pmid"]


@pytest.mark.parametrize("vid", _IDS_41_60)
def test_v41_60_narrative_min_length(vid, vignettes_41_60):
    entry = vignettes_41_60[vid]
    en = entry["data"].get("narrative_en") or ""
    es = entry["data"].get("narrative_es") or ""
    assert len(en) >= 100, f"v{vid} narrative_en too short ({len(en)} chars)"
    assert len(es) >= 100, f"v{vid} narrative_es too short ({len(es)} chars)"


@pytest.mark.parametrize("vid", _IDS_41_60)
def test_v41_60_narrative_cites_anchor_pmid(vid, vignettes_41_60):
    entry = vignettes_41_60[vid]
    pmid = entry["spec"]["pmid"]
    needle = f"PMID {pmid}"
    en = entry["data"].get("narrative_en") or ""
    es = entry["data"].get("narrative_es") or ""
    assert needle in en, f"v{vid} narrative_en missing '{needle}'"
    assert needle in es, f"v{vid} narrative_es missing '{needle}'"


@pytest.mark.parametrize("vid", _IDS_41_60)
def test_v41_60_narrative_methodology_disclosure(vid, vignettes_41_60):
    """Each narrative of vignettes 41-60 must honestly disclose its methodology.

    Acceptable disclosures: imputation/reuse phrasing for imputed and
    reuses of an anchor from vignettes 1-20; "inferred from PAM-cohort epidemiology" or
    similar for primary-source-anchored newcomers where exact source
    values were not directly reported.
    """
    entry = vignettes_41_60[vid]
    en = (entry["data"].get("narrative_en") or "").lower()
    disclosures = (
        "imputation",
        "imputed",
        "within-cohort",
        "within the anchor",
        "vignettes 1-20 used",
        "inferred from pam-cohort",
        "pam-cohort epidemiology",
        "case context",
    )
    assert any(p in en for p in disclosures), (
        f"v{vid} narrative_en missing methodology disclosure "
        f"(expected one of {disclosures})"
    )


def test_v41_60_no_em_dashes(vignettes_41_60):
    em = chr(0x2014)
    en_dash = chr(0x2013)
    for vid in _IDS_41_60:
        content = vignettes_41_60[vid]["path"].read_text(encoding="utf-8")
        assert content.count(em) == 0, f"v{vid} contains em-dash"
        assert content.count(en_dash) == 0, f"v{vid} contains en-dash"


def test_v49_outcome_survived(vignettes_41_60):
    v49 = vignettes_41_60[49]
    spec = v49["spec"]
    assert spec["outcome"] == "survived"
    anchoring = v49["data"]["adjudication"]["anchoring_documentation"].lower()
    assert "outcome=survived" in anchoring
    en = v49["data"]["narrative_en"].lower()
    assert "miltefosine" in en, "v49 narrative_en missing miltefosine"
    assert "survivor" in en or "discharged" in en
    es = v49["data"]["narrative_es"].lower()
    assert "miltefosina" in es, "v49 narrative_es missing miltefosina"


def test_v60_outcome_survived(vignettes_41_60):
    v60 = vignettes_41_60[60]
    spec = v60["spec"]
    assert spec["outcome"] == "survived"
    anchoring = v60["data"]["adjudication"]["anchoring_documentation"].lower()
    assert "outcome=survived" in anchoring
    en = v60["data"]["narrative_en"].lower()
    assert "miltefosine" in en, "v60 narrative_en missing miltefosine"
    assert "survivor" in en or "discharged" in en
    es = v60["data"]["narrative_es"].lower()
    assert "miltefosina" in es, "v60 narrative_es missing miltefosina"


# ======================================================================
# Quality checks on the PAM vignettes 41-60
# ----------------------------------------------------------------------
# These six tests check jitter heterogeneity, stage-state consistency,
# cluster-exposure mapping, bilingual narrative coverage, survivor
# treatment completeness and the case_id format, so a regression in any of
# them fails CI before merge.
# ======================================================================


def test_v41_60_jitter_uniqueness(vignettes_41_60):
    """No two entries of vignettes 41-60 share the same (CSF WBC, protein, glucose, CRP, PCT)."""
    seen: dict[tuple, int] = {}
    for vid in _IDS_41_60:
        d = vignettes_41_60[vid]["data"]
        tup = (
            d["csf"]["csf_wbc_per_mm3"],
            d["csf"]["csf_protein_mg_per_dL"],
            d["csf"]["csf_glucose_mg_per_dL"],
            d["labs"]["crp_mg_per_L"],
            d["labs"]["procalcitonin_ng_per_mL"],
        )
        if tup in seen:
            raise AssertionError(
                f"Jitter collision in vignettes 41-60: v{vid} and v{seen[tup]} share "
                f"identical (CSF_WBC, protein, glucose, CRP, PCT) tuple {tup}"
            )
        seen[tup] = vid


@pytest.mark.parametrize("vid", _IDS_41_60)
def test_v41_60_stage_state_consistency(vid, vignettes_41_60, distribution_21_60):
    """GCS and mental_status_grade must match the spec's stage classification."""
    spec = next(s for s in distribution_21_60 if s["vignette_id"] == vid)
    stage = spec["stage"]
    d = vignettes_41_60[vid]["data"]
    gcs = d["vitals"]["glasgow_coma_scale"]
    ms = d["exam"]["mental_status_grade"]
    if stage == "early":
        assert gcs >= 14, f"v{vid} early stage requires GCS>=14, got {gcs}"
        assert ms == "alert", f"v{vid} early stage requires ms=alert, got {ms!r}"
    elif stage == "mid":
        # Survivors may sit at GCS 12-14 (e.g., v49=13, v60=12) and still
        # be classified mid-stage by the rapid-recognition convention.
        assert 9 <= gcs <= 14, f"v{vid} mid stage requires GCS 9-14, got {gcs}"
        assert ms in {"somnolent", "confused"}, (
            f"v{vid} mid stage requires somnolent/confused, got {ms!r}"
        )
    elif stage == "late":
        assert gcs <= 8, f"v{vid} late stage requires GCS<=8, got {gcs}"
        assert ms in {"stuporous", "comatose"}, (
            f"v{vid} late stage requires stuporous/comatose, got {ms!r}"
        )


_CLUSTER_EXPOSURE_MAP_41_60: dict[str, set[str]] = {
    "splash_pad": {"splash_pad"},
    "lake_pond": {"lake", "river", "swimming_pool_unchlorinated", "none"},
    "river": {"river"},
    "nasal_irrigation": {"neti_pot_tap_water"},
    "hot_springs": {"hot_spring"},
    "pakistan_ablution": {"ritual_ablution_wudu"},
}


@pytest.mark.parametrize("vid", _IDS_41_60)
def test_v41_60_cluster_exposure_mapping(vid, vignettes_41_60, distribution_21_60):
    """Each cluster value must enforce a specific freshwater_exposure_type subset."""
    spec = next(s for s in distribution_21_60 if s["vignette_id"] == vid)
    cluster = spec["cluster"]
    expo = vignettes_41_60[vid]["data"]["exposure"]["freshwater_exposure_type"]
    allowed = _CLUSTER_EXPOSURE_MAP_41_60.get(cluster)
    assert allowed is not None, (
        f"v{vid} cluster {cluster!r} not in _CLUSTER_EXPOSURE_MAP_41_60; "
        f"update the map if new clusters were added"
    )
    assert expo in allowed, (
        f"v{vid} cluster={cluster} has freshwater_exposure_type={expo!r}, "
        f"expected one of {sorted(allowed)}"
    )


@pytest.mark.parametrize("vid", _IDS_41_60)
def test_v41_60_spanish_required_tokens(vid, vignettes_41_60):
    """Each ES narrative of vignettes 41-60 carries the universal Spanish-accent token set."""
    es = vignettes_41_60[vid]["data"].get("narrative_es") or ""
    accent_chars = _SPANISH_ACCENT_CHARS & set(es)
    assert accent_chars, f"v{vid} narrative_es contains no UTF-8 Spanish accents"
    for token in _REQUIRED_SPANISH_TOKENS:
        assert token in es, (
            f"v{vid} narrative_es missing accented token {token!r}"
        )


def test_v41_60_survivor_completeness(vignettes_41_60):
    """v49 and v60 survivor narratives must include miltefosine + ICP control +
    cooling protocol + ICU + discharge in both languages."""
    for vid in (49, 60):
        d = vignettes_41_60[vid]["data"]
        en = d["narrative_en"].lower()
        es = d["narrative_es"].lower()
        assert "miltefosine" in en, f"v{vid} EN missing miltefosine"
        assert "miltefosina" in es, f"v{vid} ES missing miltefosina"
        assert "intracranial pressure" in en, f"v{vid} EN missing ICP control"
        assert "presión intracraneal" in es, f"v{vid} ES missing ICP control"
        # Cooling protocol: explicit hypothermia OR targeted temperature management.
        assert ("hypothermia" in en or "temperature management" in en), (
            f"v{vid} EN missing hypothermia/targeted temperature management"
        )
        assert ("hipotermia" in es or "manejo dirigido de temperatura" in es), (
            f"v{vid} ES missing hipotermia/manejo dirigido de temperatura"
        )
        assert ("intensive care" in en or "icu" in en), (
            f"v{vid} EN missing intensive-care/ICU language"
        )
        assert "discharged" in en, f"v{vid} EN missing 'discharged'"
        assert "egresado" in es, f"v{vid} ES missing 'egresado'"
        assert "outcome=survived" in (
            d["adjudication"]["anchoring_documentation"].lower()
        ), f"v{vid} adjudication missing outcome=survived"


@pytest.mark.parametrize("vid", _IDS_41_60)
def test_v41_60_case_id_format(vid, vignettes_41_60):
    """The case_id of vignettes 41-60 must follow PAM-NNN-<journal_short_code>-<year>-..."""
    case_id = vignettes_41_60[vid]["data"]["case_id"]
    assert case_id.startswith(f"PAM-{vid:03d}-"), (
        f"v{vid} case_id {case_id!r} does not follow PAM-NNN- pattern"
    )
    pmid = vignettes_41_60[vid]["data"]["literature_anchors"][0]["pmid"]
    journal_short = PMID_REGISTRY[pmid]["journal_short_code"]
    assert journal_short in case_id, (
        f"v{vid} case_id {case_id!r} missing journal_short_code "
        f"{journal_short!r}"
    )


# ======================================================================
# Methodology, GCS spread and CSF WBC range of PAM vignettes 41-60
# ----------------------------------------------------------------------
# A regression in methodology classification, stage-GCS spread, or CSF
# WBC tail coverage fails these three tests before merge.
# ======================================================================

_VALID_METHODOLOGY_CLASSES_41_60 = {
    "primary_source_direct",
    "pmid_reuse",
    "tier_3_imputation",
    "tier_4_imputation",
}


@pytest.mark.parametrize("vid", _IDS_41_60)
def test_v41_60_methodology_tag_present(vid, vignettes_41_60):
    """Each entry of vignettes 41-60 must carry a methodology=<class>; prefix at the
    start of adjudication.anchoring_documentation, with class drawn from
    the four canonical methodology categories."""
    anchoring = vignettes_41_60[vid]["data"]["adjudication"][
        "anchoring_documentation"
    ]
    m = re.match(r"^methodology=([a-z_0-9]+);\s+", anchoring)
    assert m, (
        f"v{vid} adjudication missing leading 'methodology=<class>; ' prefix; "
        f"first 80 chars: {anchoring[:80]!r}"
    )
    cls = m.group(1)
    assert cls in _VALID_METHODOLOGY_CLASSES_41_60, (
        f"v{vid} methodology={cls!r} not in valid classes "
        f"{sorted(_VALID_METHODOLOGY_CLASSES_41_60)}"
    )


def test_v41_60_gcs_distribution_spread(vignettes_41_60, distribution_21_60):
    """Mid-stage GCS values must span >= 5 distinct levels across
    {9, 10, 11, 12, 13}, and late-stage must span >= 5 distinct levels
    across {4, 5, 6, 7, 8}."""
    by_id = {s["vignette_id"]: s for s in distribution_21_60}
    mid: list[int] = []
    late: list[int] = []
    for vid in _IDS_41_60:
        spec = by_id[vid]
        gcs = vignettes_41_60[vid]["data"]["vitals"]["glasgow_coma_scale"]
        if spec["stage"] == "mid":
            mid.append(gcs)
        elif spec["stage"] == "late":
            late.append(gcs)
    assert len(set(mid)) >= 5, (
        f"Mid-stage GCS distribution has only {len(set(mid))} "
        f"distinct values: {sorted(set(mid))}; spec requires >= 5 across "
        f"{{9,10,11,12,13}}"
    )
    assert len(set(late)) >= 5, (
        f"Late-stage GCS distribution has only {len(set(late))} "
        f"distinct values: {sorted(set(late))}; spec requires >= 5 across "
        f"{{4,5,6,7,8}}"
    )


def test_v41_60_csf_wbc_range_extremes(vignettes_41_60):
    """The CSF WBC of vignettes 41-60 must include >= 3 entries below 2,000 AND >= 3
    entries at or above 4,500, covering the low- and high-tail extremes
    documented in PAM cohort epidemiology."""
    wbcs = [
        vignettes_41_60[vid]["data"]["csf"]["csf_wbc_per_mm3"]
        for vid in _IDS_41_60
    ]
    below_2000 = sum(1 for w in wbcs if w < 2000)
    at_or_above_4500 = sum(1 for w in wbcs if w >= 4500)
    assert below_2000 >= 3, (
        f"CSF WBC of vignettes 41-60 has only {below_2000} entries below 2,000; "
        f"spec requires >= 3 (extreme low tail). All values: "
        f"{sorted(wbcs)}"
    )
    assert at_or_above_4500 >= 3, (
        f"CSF WBC of vignettes 41-60 has only {at_or_above_4500} entries at or above "
        f"4,500; spec requires >= 3 (extreme high tail). All values: "
        f"{sorted(wbcs)}"
    )


# ======================================================================
# Bacterial and viral distribution tests
# ----------------------------------------------------------------------
# Eleven of these thirteen tests check the BACTERIAL_DISTRIBUTION (n=28)
# and VIRAL_DISTRIBUTION (n=30) lists in
# scripts/vignettes/generate_pam_vignettes.py. The other two check the
# marginals.json design files at
# data/vignettes/v2/class_02_bacterial/marginals.json and
# data/vignettes/v2/class_03_viral/marginals.json.
# ======================================================================

import collections as _collections
import json as _json
from pathlib import Path as _Path
from scripts.vignettes.generate_pam_vignettes import (  # noqa: E402
    BACTERIAL_DISTRIBUTION,
    VIRAL_DISTRIBUTION,
)


_PERU_GEOGRAPHY_REGIONS = {
    "peru_lima_coast", "peru_loreto_amazon", "peru_cusco_altitude",
    "peru_puno_altitude", "peru_tumbes", "peru_madre_de_dios",
}


def test_bacterial_distribution_count():
    assert len(BACTERIAL_DISTRIBUTION) == 28


def test_viral_distribution_count():
    assert len(VIRAL_DISTRIBUTION) == 30


def test_bacterial_pathogen_counts():
    """21 SP / 4 NM / 2 Hib / 0 Listeria / 1 GN (the 2 Listeria slots were
    removed in the 2026-05-31 correction)."""
    counts = _collections.Counter(
        s["pathogen"] for s in BACTERIAL_DISTRIBUTION
    )
    assert counts["S_pneumoniae"] == 21, counts
    assert counts["N_meningitidis"] == 4, counts
    assert counts["H_influenzae"] == 2, counts
    assert counts["Listeria_monocytogenes"] == 0, counts
    assert counts["gram_negative"] == 1, counts


def test_viral_pathogen_counts():
    """12 HSV-1 / 8 enterovirus / 4 HSV-2-VZV /
    4 arboviral (3 dengue + 1 EEE) / 2 HSV-PCR-negative-at-72h."""
    counts = _collections.Counter(
        s["pathogen"] for s in VIRAL_DISTRIBUTION
    )
    assert counts["HSV1"] == 12, counts
    assert counts["enterovirus"] == 8, counts
    assert (counts["HSV2"] + counts["VZV"]) == 4, counts
    assert counts["HSV2"] == 2, counts
    assert counts["VZV"] == 2, counts
    assert counts["dengue"] == 3, counts
    assert counts["EEE"] == 1, counts
    assert counts["HSV_PCR_negative_72h"] == 2, counts


def test_bacterial_peru_anchor_share():
    """4/28 Peru-anchored: 2 Lima SP + 1 Loreto NM + 1 Cusco Hib
    (1 Tumbes Listeria slot removed in the 2026-05-31 correction)."""
    peru = sum(
        1 for s in BACTERIAL_DISTRIBUTION
        if s["geography_region"] in _PERU_GEOGRAPHY_REGIONS
    )
    assert peru == 4


def test_viral_dengue_peru_anchor():
    """All 3 dengue cases must be Peru-anchored."""
    dengue_peru = sum(
        1 for s in VIRAL_DISTRIBUTION
        if s["pathogen"] == "dengue"
        and s["geography_region"] in _PERU_GEOGRAPHY_REGIONS
    )
    assert dengue_peru == 3


def test_bacterial_viral_specs_freshwater_false():
    """Sanity check: all 58 Class-2/3 specs (28 bacterial + 30 viral) must have
    freshwater_exposure_within_14d=False."""
    for spec in BACTERIAL_DISTRIBUTION + VIRAL_DISTRIBUTION:
        assert spec["freshwater_exposure_within_14d"] is False, spec[
            "vignette_id"
        ]


def test_diagnostic_ambiguity_count():
    """5 diagnostic ambiguity cases per class."""
    bact_amb = sum(
        1 for s in BACTERIAL_DISTRIBUTION if s.get("diagnostic_ambiguity")
    )
    viral_amb = sum(
        1 for s in VIRAL_DISTRIBUTION if s.get("diagnostic_ambiguity")
    )
    assert bact_amb == 5, bact_amb
    assert viral_amb == 5, viral_amb


def test_hsv1_imaging_mandate_present_in_specs():
    """Each of the 12 HSV1 specs carries the imaging_mandate field."""
    hsv1 = [s for s in VIRAL_DISTRIBUTION if s["pathogen"] == "HSV1"]
    assert len(hsv1) == 12
    for s in hsv1:
        assert s.get("imaging_mandate") == (
            "mesial_temporal_t2_flair_hyperintensity"
        ), s["vignette_id"]


def test_dengue_platelet_mandate_present_in_specs():
    """Each of the 3 dengue specs carries the platelet_mandate field."""
    dengue = [s for s in VIRAL_DISTRIBUTION if s["pathogen"] == "dengue"]
    assert len(dengue) == 3
    for s in dengue:
        assert s.get("platelet_mandate_below_per_uL") == 150000, s[
            "vignette_id"
        ]


def test_bacterial_viral_vignette_ids_contiguous():
    """Class 2 occupies 61-90 minus 88/89 (the 2 Listeria slots removed in
    the 2026-05-31 correction); Class 3 occupies 91-120; specs are disjoint
    from PAM vignettes 1-20 and 21-60."""
    bact_ids = sorted(s["vignette_id"] for s in BACTERIAL_DISTRIBUTION)
    viral_ids = sorted(s["vignette_id"] for s in VIRAL_DISTRIBUTION)
    assert bact_ids == [i for i in range(61, 91) if i not in (88, 89)]
    assert viral_ids == list(range(91, 121))


def test_marginals_files_exist_and_valid():
    """The Class 2 and Class 3 marginals.json design files are present and valid."""
    cases = [
        ("data/vignettes/v2/class_02_bacterial/marginals.json", 2, 28),
        ("data/vignettes/v2/class_03_viral/marginals.json", 3, 30),
    ]
    for path, class_id, total_n in cases:
        p = _Path(path)
        assert p.exists(), f"{path} missing"
        data = _json.loads(p.read_text(encoding="utf-8"))
        assert data["class_id"] == class_id, path
        assert data["total_n"] == total_n, path
        assert "pathogen_distribution" in data, path
        assert "csf_profile_ranges" in data, path
        assert "cited_anchors" in data, path
        assert isinstance(data["cited_anchors"], list) and len(
            data["cited_anchors"]
        ) >= 3, path
        # Pathogen distribution must match spec targets exactly.
        assert (
            data["pathogen_distribution"]
            == data["pathogen_distribution_target_per_spec"]
        ), f"{path} pathogen distribution drifted from spec"


def test_marginals_freshwater_sanity_and_adjudication_state():
    """marginals.json artifacts disclose pre-adjudication state and
    freshwater=False sanity for downstream auditors."""
    for path in (
        "data/vignettes/v2/class_02_bacterial/marginals.json",
        "data/vignettes/v2/class_03_viral/marginals.json",
    ):
        data = _json.loads(_Path(path).read_text(encoding="utf-8"))
        assert (
            data.get("freshwater_exposure_within_14d_for_all") is False
        ), path
        assert data.get("adjudication_state") == (
            "pre_adjudication_hold_for_revision"
        ), path


# ======================================================================
# PMID 29462145 must stay out of the registry
# ----------------------------------------------------------------------
# PMID 29462145 (Jiang YH 2018 PLoS One) is a urology paper with no
# meningitis, encephalitis or Zika content, found by manual PMC
# verification on 2026-05-07; it must not be in PMID_REGISTRY.
# ======================================================================


def test_pmid_29462145_excluded_from_registry():
    """Regression guard: PMID 29462145 (Jiang YH urology paper) MUST NOT be in registry.

    Verified PMID = "Videourodynamic findings of lower urinary tract
    dysfunctions in men with persistent storage lower urinary tract
    symptoms after medical treatment" (Jiang YH, Wang CC, Kuo HC. PLoS
    One 2018;13(2):e0190704). Topic is benign prostatic hyperplasia /
    bladder outlet obstruction, which has no Zika / meningitis /
    encephalitis content. Originally hinted as a companion to the Mehta R
    Zika systematic review; manual PMC verification on
    2026-05-07 confirmed it is unrelated.
    """
    assert "29462145" not in PMID_REGISTRY, (
        "PMID 29462145 (Jiang YH urology paper) must not be present."
    )


# =========================================================================
# Registry coverage for the bacterial and viral distributions
# -------------------------------------------------------------------------
# test_v21_v60_pmids_in_registry covers the PAM slots 21-60 only; this test
# covers all 58 bacterial and viral slots (IDs 61-120 without 88 and 89).
# =========================================================================


def test_bacterial_viral_distribution_pmids_in_registry():
    """All BACT + VIRAL slot anchor PMIDs must resolve in PMID_REGISTRY.

    Fails if any slot's anchor PMID is mistyped or missing from the
    registry.
    """
    from scripts.vignettes.generate_pam_vignettes import (
        BACTERIAL_DISTRIBUTION,
        VIRAL_DISTRIBUTION,
    )
    all_slots = list(BACTERIAL_DISTRIBUTION) + list(VIRAL_DISTRIBUTION)
    broken: list[tuple[object, object]] = []
    for slot in all_slots:
        vid = slot.get("vignette_id", "?")
        pmid = slot.get("anchor_pmid") or slot.get("pmid")
        if pmid not in PMID_REGISTRY:
            broken.append((vid, pmid))
    assert not broken, (
        f"BACT/VIRAL distribution slots reference PMIDs not in registry: "
        f"{broken}."
    )
