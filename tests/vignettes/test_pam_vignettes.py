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
# Acceptable verification dates: Day 1 sweep + Day 2 corrections sweep.
# See docs/PMID_CORRECTIONS_2026-05-04.md for the audit trail.
_VALID_VERIFICATION_DATES = {"2026-05-03", "2026-05-04"}


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


_ALLOWED_JOURNAL_CODES = {"MMWR", "JCM", "CID", "IDCases", "AJTMH", "EID", "IJP"}
_CASE_ID_RE = re.compile(
    r"^PAM-D1-(\d{3})-([A-Za-z]+)-(\d{4})-(.+)$"
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
