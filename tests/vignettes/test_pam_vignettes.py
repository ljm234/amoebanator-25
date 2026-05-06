"""Tests for scripts/generate_pam_vignettes.py (Subphase 1.2 Day 1).

Validates the 20-vignette PAM corpus end-to-end: schema conformance,
PMID metadata completeness, distribution against the spec, and content
quality (no em-dashes, no AI-tells, Spanish accent integrity).

The DAY1_DISTRIBUTION list and PMID_REGISTRY in
``scripts/generate_pam_vignettes.py`` are the source of truth for these
tests. Where the Day 1 spec doc and the actual distribution disagree on
demographic tallies (the spec was drafted before final per-vignette
sex/age assignments), tests assert against the data and call out the
delta inline.
"""
from __future__ import annotations

import re
from typing import Any

import pytest

from ml.schemas.vignette import VignetteSchema
from scripts.generate_pam_vignettes import PMID_REGISTRY


pytestmark = pytest.mark.subphase_1_2


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
# Acceptable verification dates: Day 1 sweep + Day 2 corrections sweep + Day 2
# bonus canonization. See docs/PMID_CORRECTIONS_2026-05-04.md and
# docs/PMID_DAY2_BONUS_CANONIZATION_2026-05-05.md for the audit trails.
_VALID_VERIFICATION_DATES = {"2026-05-03", "2026-05-04", "2026-05-05"}


@pytest.mark.parametrize("pmid", sorted(PMID_REGISTRY.keys()))
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
        f"not in approved verification sweep dates "
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
# Spec doc (amoebanator_subphase_1_2_day1_distribution.md) listed
# Female=9 / Male=11 / Pediatric=13 / Adult=7. The final per-vignette
# table in the same doc resolves to Female={2,5,11,12,14}=5 and
# Adult={10,11,12,14,16,19}=6. The data is the source of truth here;
# the summary block in the spec was drafted earlier and is stale.


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
            em += s.count("—")  # em-dash
            en += s.count("–")  # en-dash
    assert em == 0, f"Found {em} em-dash(es) in generated content"
    assert en == 0, f"Found {en} en-dash(es) in generated content"


# ----------------------------------------------------------------------
# 6. No AI-tell vocabulary in generated content
# ----------------------------------------------------------------------


_AI_TELLS = (
    "leverage", "harness", "delve", "seamless", "comprehensive",
    "exceptional", "robust", "showcase", "elevate", "empower",
    "tapestry", "unleash",
)


def test_no_ai_tells_in_content(generated_vignettes):
    hits: dict[str, int] = {}
    for vignette in generated_vignettes:
        for s in _walk_strings(vignette):
            lower = s.lower()
            for token in _AI_TELLS:
                if token in lower:
                    hits[token] = hits.get(token, 0) + 1
    assert not hits, f"AI-tell tokens found in generated content: {hits}"


# ----------------------------------------------------------------------
# 7. Spanish narratives have proper UTF-8 accents
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
# 8. Survivor vs fatal outcome consistency
# ----------------------------------------------------------------------


def test_survivor_vignettes_have_correct_outcome(generated_vignettes):
    by_id = {v["case_id"].split("-")[2]: v for v in generated_vignettes}
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
# 9. literature_anchors[0].pmid matches DAY1_DISTRIBUTION assignment
# ----------------------------------------------------------------------


def test_pmid_assignments_match_distribution(distribution, generated_vignettes):
    by_id = {s["vignette_id"]: s for s in distribution}
    for vignette in generated_vignettes:
        vignette_id = int(vignette["case_id"].split("-")[2])
        spec = by_id[vignette_id]
        anchor_pmid = vignette["literature_anchors"][0]["pmid"]
        assert anchor_pmid == spec["pmid"], (
            f"vignette {vignette_id} literature_anchor pmid "
            f"{anchor_pmid!r} != distribution pmid {spec['pmid']!r}"
        )


# ----------------------------------------------------------------------
# 10. case_id format
# ----------------------------------------------------------------------


_ALLOWED_JOURNAL_CODES = {
    "MMWR", "JCM", "CID", "IDCases", "AJTMH", "EID", "IJP",
    # Vancouver MEDLINE-style abbreviations (Day 2 canonization 2026-05-04):
    "Emerg Infect Dis", "Front Microbiol", "Front Med (Lausanne)",
    "Pathogens", "Front Pediatr", "BMC Infect Dis", "J Trop Pediatr",
    "TexMed", "JPIDS", "EpidemiolInfect", "ExpertRevAntiInfect",
    # Day-2 pilot (commit 4 of 5):
    "Diagnostics", "Yonsei Med J", "Pediatrics",
}
# Journal portion may now contain spaces and parentheses (Vancouver style).
# Use a non-greedy capture for the journal segment, terminated by `-NNNN-`
# (a 4-digit year) so the journal can include any chars except newline.
# Day prefix is D1 (v1-v20) or D2 (v21-v60).
_CASE_ID_RE = re.compile(
    r"^PAM-D[12]-(\d{3})-(.+?)-(\d{4})-(.+)$"
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
# Day 2 distribution lock (v21-v60, 40 vignettes)
# ----------------------------------------------------------------------
# Tests below validate the Day-2 distribution data structure only.
# Vignette JSON generation for v21-v60 is deferred to Commits 4-5.
# Source of truth: DAY2_DISTRIBUTION in scripts/generate_pam_vignettes.py.
# Rationale doc: docs/DAY2_DISTRIBUTION_RATIONALE.md.
# ======================================================================


_EXPECTED_CLUSTERS_DAY2: dict[str, set[int]] = {
    "splash_pad": {23, 25, 50, 51, 52},
    "lake_pond": {22, 24, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40},
    "river": {21, 41, 42, 43, 44, 45, 46, 47, 48, 49},
    "nasal_irrigation": {53, 54, 55, 56, 57, 58},
    "hot_springs": {59},
    "pakistan_ablution": {60},
}

_DAY2_FILENAME_RE = re.compile(
    r"^pam_d2_(\d{3})_[a-z][a-z0-9_]*\.json$"
)

_REUSE_CAP = 6


def test_day2_distribution_length(day2_distribution):
    assert len(day2_distribution) == 40, (
        f"DAY2_DISTRIBUTION has {len(day2_distribution)} entries, expected 40"
    )


def test_day2_vignette_ids_contiguous(day2_distribution):
    ids = sorted(s["vignette_id"] for s in day2_distribution)
    assert ids == list(range(21, 61)), (
        f"Day-2 vignette_ids not contiguous 21-60: {ids}"
    )


def test_day2_cluster_distribution_matches_spec(day2_distribution):
    actual: dict[str, set[int]] = {}
    for spec in day2_distribution:
        actual.setdefault(spec["cluster"], set()).add(spec["vignette_id"])
    assert actual == _EXPECTED_CLUSTERS_DAY2, (
        f"Day-2 cluster distribution does not match spec.\n"
        f"  expected: {_EXPECTED_CLUSTERS_DAY2}\n"
        f"  actual:   {actual}"
    )


def test_day2_pmids_in_registry(day2_distribution, pmid_registry):
    for spec in day2_distribution:
        assert spec["pmid"] in pmid_registry, (
            f"Day-2 vignette {spec['vignette_id']} pmid {spec['pmid']!r} "
            f"not in PMID_REGISTRY"
        )


def test_combined_corpus_size_60(distribution, day2_distribution):
    assert len(distribution) + len(day2_distribution) == 60, (
        f"Combined corpus size = {len(distribution) + len(day2_distribution)}, "
        f"expected 60"
    )


def test_no_id_collisions(distribution, day2_distribution):
    day1_ids = {s["vignette_id"] for s in distribution}
    day2_ids = {s["vignette_id"] for s in day2_distribution}
    assert day1_ids.isdisjoint(day2_ids), (
        f"Day-1 and Day-2 vignette_ids overlap: "
        f"{sorted(day1_ids & day2_ids)}"
    )


def test_no_filename_collisions(distribution, day2_distribution):
    day1_files = {s["filename"] for s in distribution}
    day2_files = {s["filename"] for s in day2_distribution}
    assert day1_files.isdisjoint(day2_files), (
        f"Day-1 and Day-2 filenames overlap: "
        f"{sorted(day1_files & day2_files)}"
    )


def test_day2_filename_format(day2_distribution):
    for spec in day2_distribution:
        fname = spec["filename"]
        m = _DAY2_FILENAME_RE.match(fname)
        assert m, (
            f"Day-2 vignette {spec['vignette_id']} filename {fname!r} "
            f"does not match pam_d2_NNN_<tag>.json"
        )
        nnn = int(m.group(1))
        assert nnn == spec["vignette_id"], (
            f"filename {fname!r} NNN={nnn} != vignette_id {spec['vignette_id']}"
        )


def test_pmid_reuse_cap(distribution, day2_distribution):
    counts: dict[str, int] = {}
    for spec in distribution:
        counts[spec["pmid"]] = counts.get(spec["pmid"], 0) + 1
    for spec in day2_distribution:
        counts[spec["pmid"]] = counts.get(spec["pmid"], 0) + 1
    over_cap = {p: n for p, n in counts.items() if n > _REUSE_CAP}
    assert not over_cap, (
        f"PMIDs over reuse cap {_REUSE_CAP}x: {over_cap}"
    )


def test_day2_sex_enum(day2_distribution):
    for spec in day2_distribution:
        assert spec["sex"] in {"male", "female"}, (
            f"Day-2 vignette {spec['vignette_id']} has invalid sex "
            f"{spec['sex']!r}"
        )


def test_day2_outcome_enum(day2_distribution):
    for spec in day2_distribution:
        assert spec["outcome"] in {"fatal", "survived"}, (
            f"Day-2 vignette {spec['vignette_id']} has invalid outcome "
            f"{spec['outcome']!r}"
        )


def test_day2_stage_enum(day2_distribution):
    for spec in day2_distribution:
        assert spec["stage"] in {"early", "mid", "late"}, (
            f"Day-2 vignette {spec['vignette_id']} has invalid stage "
            f"{spec['stage']!r}"
        )


def test_combined_demographic_balance(distribution, day2_distribution):
    combined = list(distribution) + list(day2_distribution)
    n = len(combined)
    female = sum(1 for s in combined if s["sex"] == "female")
    adult = sum(1 for s in combined if s["age_years"] >= 18)
    assert female / n >= 0.20, (
        f"Combined female ratio {female}/{n} = {female/n:.2%} < 20% "
        f"(target 22% per locked decisions; floor 20% allowed)"
    )
    assert adult / n >= 0.25, (
        f"Combined adult ratio {adult}/{n} = {adult/n:.2%} < 25%"
    )


def test_combined_outcome_balance(distribution, day2_distribution):
    combined = list(distribution) + list(day2_distribution)
    n = len(combined)
    fatal = sum(1 for s in combined if s["outcome"] == "fatal")
    survived = sum(1 for s in combined if s["outcome"] == "survived")
    assert fatal / n >= 0.90, (
        f"Combined fatal ratio {fatal}/{n} = {fatal/n:.2%} < 90%"
    )
    assert survived / n >= 0.08, (
        f"Combined survivor ratio {survived}/{n} = {survived/n:.2%} < 8%"
    )


def test_combined_geographic_balance(distribution, day2_distribution):
    combined = list(distribution) + list(day2_distribution)
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


def test_day2_special_cases_present(day2_distribution):
    by_pmid = {s["pmid"]: s for s in day2_distribution}
    assert "39795618" in by_pmid, "Phung 2025 cryptic-exposure anchor missing"
    assert "39606118" in by_pmid, "Lin 2024 atypical-myocarditis anchor missing"
    assert "37727924" in by_pmid, "Hong 2023 travel-imported anchor missing"
    assert "25667249" in by_pmid, "Linam 2015 Kali Hardig survivor anchor missing"


# ======================================================================
# Day 2 pilot vignette content tests (v21-v25, commit 4 of 5)
# ----------------------------------------------------------------------
# These tests validate the 5 pilot JSON files generated by Commit 4 of 5.
# Each pilot vignette is anchored 100% in primary-source data verified
# via user PubMed UI direct fetch.
# ======================================================================

import json
from pathlib import Path

_PILOT_DATA_DIR = Path(__file__).resolve().parents[2] / "data" / "vignettes" / "pam"
_PILOT_IDS = [21, 22, 23, 24, 25]


@pytest.fixture(scope="session")
def pilot_vignettes(day2_distribution):
    """Load the 5 pilot JSON files from disk."""
    out: dict[int, dict[str, Any]] = {}
    by_id = {s["vignette_id"]: s for s in day2_distribution}
    for vid in _PILOT_IDS:
        spec = by_id[vid]
        fpath = _PILOT_DATA_DIR / spec["filename"]
        out[vid] = {
            "spec": spec,
            "path": fpath,
            "data": json.loads(fpath.read_text(encoding="utf-8")),
        }
    return out


@pytest.mark.parametrize("vid", _PILOT_IDS)
def test_pilot_file_exists(vid, pilot_vignettes):
    entry = pilot_vignettes[vid]
    assert entry["path"].exists(), f"v{vid} pilot JSON {entry['path']} missing"


@pytest.mark.parametrize("vid", _PILOT_IDS)
def test_pilot_schema_validates(vid, pilot_vignettes):
    entry = pilot_vignettes[vid]
    VignetteSchema.model_validate(entry["data"])


@pytest.mark.parametrize("vid", _PILOT_IDS)
def test_pilot_demographics_match_spec(vid, pilot_vignettes):
    entry = pilot_vignettes[vid]
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


@pytest.mark.parametrize("vid", _PILOT_IDS)
def test_pilot_anchor_pmid_matches(vid, pilot_vignettes):
    entry = pilot_vignettes[vid]
    anchors = entry["data"]["literature_anchors"]
    assert anchors, f"v{vid}: empty literature_anchors"
    assert anchors[0]["pmid"] == entry["spec"]["pmid"], (
        f"v{vid}: anchor pmid {anchors[0]['pmid']!r} != "
        f"spec pmid {entry['spec']['pmid']!r}"
    )


@pytest.mark.parametrize("vid", _PILOT_IDS)
def test_pilot_narrative_min_length(vid, pilot_vignettes):
    entry = pilot_vignettes[vid]
    en = entry["data"].get("narrative_en") or ""
    es = entry["data"].get("narrative_es") or ""
    assert len(en) >= 100, f"v{vid} narrative_en too short ({len(en)} chars)"
    assert len(es) >= 100, f"v{vid} narrative_es too short ({len(es)} chars)"


@pytest.mark.parametrize("vid", _PILOT_IDS)
def test_pilot_narrative_cites_anchor_pmid(vid, pilot_vignettes):
    entry = pilot_vignettes[vid]
    pmid = entry["spec"]["pmid"]
    en = entry["data"].get("narrative_en") or ""
    es = entry["data"].get("narrative_es") or ""
    needle = f"PMID {pmid}"
    assert needle in en, f"v{vid} narrative_en missing '{needle}'"
    assert needle in es, f"v{vid} narrative_es missing '{needle}'"


def test_v25_outcome_survived(pilot_vignettes):
    v25 = pilot_vignettes[25]
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


def test_v23_atypical_features_in_narrative(pilot_vignettes):
    v23 = pilot_vignettes[23]
    en = v23["data"]["narrative_en"].lower()
    es = v23["data"]["narrative_es"].lower()
    for token in ("myocarditis", "ecmo", "indoor heated"):
        assert token in en, f"v23 narrative_en missing {token!r}"
    for token in ("miocarditis", "ecmo", "piscina"):
        assert token in es, f"v23 narrative_es missing {token!r}"


def test_pilot_no_em_dashes(pilot_vignettes):
    em = chr(0x2014)
    en_dash = chr(0x2013)
    for vid in _PILOT_IDS:
        content = pilot_vignettes[vid]["path"].read_text(encoding="utf-8")
        assert content.count(em) == 0, f"v{vid} contains {em} em-dash(es)"
        assert content.count(en_dash) == 0, f"v{vid} contains {en_dash} en-dash(es)"


def test_pilot_no_ai_tells(pilot_vignettes):
    banned = (
        "delve", "tapestry", "navigate the realm", "in the realm of",
        "vibrant", "robust", "comprehensive", "intricate",
    )
    for vid in _PILOT_IDS:
        content = pilot_vignettes[vid]["path"].read_text(encoding="utf-8").lower()
        for w in banned:
            assert w not in content, f"v{vid} contains AI-tell {w!r}"
