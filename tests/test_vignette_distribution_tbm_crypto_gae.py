"""Slot distributions for TBM, cryptococcal, and GAE vignettes (Classes 4-6).

TBM_DISTRIBUTION (Class 4, vignette_id 121-150 without the retired 144 and
145), CRYPTO_DISTRIBUTION (Class 5, 151-180), and GAE_DISTRIBUTION (Class 6,
181-210). The tests check slot counts and id ranges, that every anchor PMID
is in PMID_REGISTRY, the counts of the anchor and set_assignment fields, the
demographic strata and clinical-feature targets of each class, and two schema
encoding workarounds:
- slots 184, 185 geography_region collapsed to peru_lima_coast (city in
  geography_label); schema enum lacks peru_lambayeque / peru_la_libertad keys.
- slots 177, 178 idiopathic CD4 lymphopenia HIV-neg encoded as
  immunocompromise_status="none" with cd4_count_cells_per_uL<200 at build time;
  schema lacks HIV-neutral T-cell-immunodeficiency enum.

These tests read the distribution lists only, not the vignette JSON files.
"""
from __future__ import annotations

import sys
from pathlib import Path

import pytest

_REPO_ROOT = Path(__file__).resolve().parent.parent
if str(_REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(_REPO_ROOT))

from scripts.vignettes.generate_pam_vignettes import (  # noqa: E402
    CRYPTO_DISTRIBUTION,
    GAE_DISTRIBUTION,
    PMID_REGISTRY,
    TBM_DISTRIBUTION,
)


TBM_ID_RANGE = sorted(set(range(121, 151)) - {144, 145})  # 144/145 retired
CRYPTO_ID_RANGE = range(151, 181)
GAE_ID_RANGE = range(181, 211)


# ----------------------------------------------------------------------
# Totals and ranges
# ----------------------------------------------------------------------


def test_total_slot_count_88():
    total = len(TBM_DISTRIBUTION) + len(CRYPTO_DISTRIBUTION) + len(GAE_DISTRIBUTION)
    assert total == 88, f"Expected 88, got {total}"


@pytest.mark.parametrize(
    ("dist_name", "dist", "expected_n"),
    [
        ("TBM_DISTRIBUTION", TBM_DISTRIBUTION, 28),
        ("CRYPTO_DISTRIBUTION", CRYPTO_DISTRIBUTION, 30),
        ("GAE_DISTRIBUTION", GAE_DISTRIBUTION, 30),
    ],
)
def test_per_class_slot_count(dist_name, dist, expected_n):
    assert len(dist) == expected_n, f"{dist_name} has {len(dist)}, expected {expected_n}"


def test_vignette_id_ranges():
    tbm_ids = {s["vignette_id"] for s in TBM_DISTRIBUTION}
    crypto_ids = {s["vignette_id"] for s in CRYPTO_DISTRIBUTION}
    gae_ids = {s["vignette_id"] for s in GAE_DISTRIBUTION}
    assert tbm_ids == set(TBM_ID_RANGE), f"TBM ids mismatch: {sorted(tbm_ids)}"
    assert crypto_ids == set(CRYPTO_ID_RANGE), f"CRYPTO ids mismatch: {sorted(crypto_ids)}"
    assert gae_ids == set(GAE_ID_RANGE), f"GAE ids mismatch: {sorted(gae_ids)}"


def test_vignette_ids_non_overlapping():
    tbm_ids = {s["vignette_id"] for s in TBM_DISTRIBUTION}
    crypto_ids = {s["vignette_id"] for s in CRYPTO_DISTRIBUTION}
    gae_ids = {s["vignette_id"] for s in GAE_DISTRIBUTION}
    assert tbm_ids.isdisjoint(crypto_ids)
    assert tbm_ids.isdisjoint(gae_ids)
    assert crypto_ids.isdisjoint(gae_ids)


# ----------------------------------------------------------------------
# Anchor PMID registry coverage
# ----------------------------------------------------------------------


@pytest.mark.parametrize(
    ("dist_name", "dist"),
    [
        ("TBM_DISTRIBUTION", TBM_DISTRIBUTION),
        ("CRYPTO_DISTRIBUTION", CRYPTO_DISTRIBUTION),
        ("GAE_DISTRIBUTION", GAE_DISTRIBUTION),
    ],
)
def test_anchor_pmid_in_registry(dist_name, dist):
    for slot in dist:
        anchor = slot["anchor_pmid"]
        assert anchor in PMID_REGISTRY, (
            f"{dist_name} vid={slot['vignette_id']} anchor_pmid={anchor!r} not in PMID_REGISTRY"
        )


# ----------------------------------------------------------------------
# Cross-class invariants
# ----------------------------------------------------------------------


def test_freshwater_exposure_within_14d_false_all_slots():
    for dist in (TBM_DISTRIBUTION, CRYPTO_DISTRIBUTION, GAE_DISTRIBUTION):
        for slot in dist:
            assert slot["freshwater_exposure_within_14d"] is False, (
                f"vid={slot['vignette_id']} must have freshwater_exposure_within_14d=False (PAM differential)"
            )


def test_anchor_flag_on_six_slots_two_per_class():
    flagged = [
        s for dist in (TBM_DISTRIBUTION, CRYPTO_DISTRIBUTION, GAE_DISTRIBUTION)
        for s in dist if s.get("anchor") is True
    ]
    assert len(flagged) == 6, (
        f"Expected 6 slots with anchor=True, got {len(flagged)}: "
        f"{[p['vignette_id'] for p in flagged]}"
    )
    # 2 per class
    for dist, name in (
        (TBM_DISTRIBUTION, "TBM"),
        (CRYPTO_DISTRIBUTION, "CRYPTO"),
        (GAE_DISTRIBUTION, "GAE"),
    ):
        n = sum(1 for s in dist if s.get("anchor") is True)
        assert n == 2, f"{name} slots with anchor=True: {n}, expected 2"


def test_set_assignment_counts():
    sets = {"anchor": 0, "set_a": 0, "set_b": 0}
    for dist in (TBM_DISTRIBUTION, CRYPTO_DISTRIBUTION, GAE_DISTRIBUTION):
        for slot in dist:
            sa = slot["set_assignment"]
            assert sa in sets, f"vid={slot['vignette_id']} bad set_assignment={sa!r}"
            sets[sa] += 1
    assert sets["anchor"] == 6, f"anchor total = {sets['anchor']}, expected 6"
    assert sets["set_a"] == 42, f"set_a total = {sets['set_a']}, expected 42"
    assert sets["set_b"] == 40, f"set_b total = {sets['set_b']}, expected 40"


# ----------------------------------------------------------------------
# Class 4 (TBM) stratum arithmetic
# ----------------------------------------------------------------------


def test_tbm_demographic_strata():
    counts: dict[str, int] = {}
    for slot in TBM_DISTRIBUTION:
        counts[slot["demographic_stratum"]] = counts.get(slot["demographic_stratum"], 0) + 1
    assert counts.get("adult_hiv_negative") == 16, counts
    assert counts.get("pediatric_median_6mo_2y") == 8, counts
    assert counts.get("hiv_coinfected_atypical") == 4, counts
    assert sum(counts.values()) == 28


def test_tbm_lmic_geography_ge_20_of_30():
    """At least 20 TBM slots have LMIC geography."""
    lmic_regions = {"peru_lima_coast", "peru_loreto_amazon", "peru_cusco_altitude",
                    "peru_puno_altitude", "peru_tumbes", "peru_madre_de_dios",
                    "other_latam"}
    # other_global hosts Vietnam HCMC, South Africa, India - also LMIC. Use
    # geography_label substring to disambiguate non-LMIC (UK, US, EU).
    non_lmic_label_markers = ("United Kingdom", "London", "United States",
                              "US ", "Europe", "Germany", "France")
    lmic_count = 0
    for slot in TBM_DISTRIBUTION:
        region = slot["geography_region"]
        label = slot["geography_label"]
        if region in lmic_regions:
            lmic_count += 1
        elif region == "other_global" and not any(m in label for m in non_lmic_label_markers):
            lmic_count += 1
    assert lmic_count >= 20, f"TBM LMIC count = {lmic_count}, target >=20/30"


def test_tbm_cn_vi_palsy_in_target_range():
    """Between 6 and 9 TBM slots have cn_vi_palsy=True."""
    n = sum(1 for s in TBM_DISTRIBUTION if s.get("cn_vi_palsy") is True)
    assert 6 <= n <= 9, f"TBM cn_vi_palsy=True count = {n}, target 6-9/30"


# ----------------------------------------------------------------------
# Class 5 (CRYPTO) stratum arithmetic
# ----------------------------------------------------------------------


def test_crypto_demographic_strata():
    counts: dict[str, int] = {}
    for slot in CRYPTO_DISTRIBUTION:
        counts[slot["demographic_stratum"]] = counts.get(slot["demographic_stratum"], 0) + 1
    assert counts.get("hiv_positive_cd4_under_100") == 22, counts
    assert counts.get("transplant_solid_organ") == 4, counts
    assert counts.get("idiopathic_cd4_lymphopenia") == 2, counts
    assert counts.get("c_gattii_immunocompetent") == 2, counts
    assert sum(counts.values()) == 30


def test_crypto_op_ge_25_ge_24_of_30():
    """OP>=25 cmH2O in at least 24 of 30 cryptococcal slots."""
    n = sum(1 for s in CRYPTO_DISTRIBUTION if s.get("op_geq_25") is True)
    assert n >= 24, f"CRYPTO op_geq_25=True count = {n}, target >=24/30"


def test_crypto_csf_crag_lfa_positive_ge_28_of_30():
    """csf_crag_lfa positive in at least 28 of 30 cryptococcal slots."""
    n = sum(1 for s in CRYPTO_DISTRIBUTION if s.get("csf_crag_lfa_positive") is True)
    assert n >= 28, f"CRYPTO csf_crag_lfa_positive=True count = {n}, target >=28/30"


# ----------------------------------------------------------------------
# Class 6 (GAE) stratum arithmetic
# ----------------------------------------------------------------------


def test_gae_balamuthia_acanthamoeba_split():
    bal = sum(1 for s in GAE_DISTRIBUTION
              if s["pathogen_subtype"].startswith("balamuthia"))
    aca = sum(1 for s in GAE_DISTRIBUTION
              if s["pathogen_subtype"].startswith("acanthamoeba"))
    assert bal == 15, f"Balamuthia count = {bal}, expected 15"
    assert aca == 15, f"Acanthamoeba count = {aca}, expected 15"
    assert bal + aca == 30


def test_gae_balamuthia_peru_or_hispanic_ge_12_of_15():
    """At least 12 of 15 Balamuthia slots are Peruvian or Hispanic
    (Alvarez/Bravo 10 + Cabello-Vilchez 2)."""
    n = 0
    for s in GAE_DISTRIBUTION:
        if not s["pathogen_subtype"].startswith("balamuthia"):
            continue
        peru_geo = s["geography_region"] in {
            "peru_lima_coast", "peru_loreto_amazon", "peru_cusco_altitude",
            "peru_puno_altitude", "peru_tumbes", "peru_madre_de_dios",
        }
        hispanic_eth = s.get("ethnicity") in {"hispanic_latino", "mestizo", "indigenous_andean"}
        if peru_geo or hispanic_eth:
            n += 1
    assert n >= 12, f"GAE Balamuthia Peru-or-Hispanic count = {n}, target >=12/15"


def test_gae_acanthamoeba_immunocompromised_10_of_15():
    n = sum(
        1 for s in GAE_DISTRIBUTION
        if s["demographic_stratum"] == "acanthamoeba_immunocompromised"
    )
    assert n == 10, f"GAE Acanthamoeba immunocompromised = {n}, expected 10/15"


def test_gae_acanthamoeba_corneal_cns_5_of_15():
    n = sum(
        1 for s in GAE_DISTRIBUTION
        if s["demographic_stratum"] == "acanthamoeba_corneal_with_cns_spread"
    )
    assert n == 5, f"GAE Acanthamoeba corneal-with-CNS-spread = {n}, expected 5/15"


def test_gae_skin_lesion_centrofacial_balamuthia_ge_12_of_15():
    """At least 12 of 15 Balamuthia slots have a chronic centrofacial skin lesion
    (Alvarez 2022 JAAD Int: centrofacial in 22/30; mean skin-lesion duration at
    diagnosis 15 months)."""
    n = sum(
        1 for s in GAE_DISTRIBUTION
        if s["pathogen_subtype"].startswith("balamuthia")
        and s.get("skin_lesion_centrofacial_chronic") is True
    )
    assert n >= 12, f"GAE Balamuthia skin_lesion_centrofacial_chronic count = {n}, target >=12/15"


def test_gae_all_30_chronic_ge_14_days():
    """Every GAE slot is chronic: >=14 days from symptom onset to presentation."""
    for s in GAE_DISTRIBUTION:
        assert s.get("symptom_to_presentation_days", 0) >= 14, (
            f"vid={s['vignette_id']} symptom_to_presentation_days="
            f"{s.get('symptom_to_presentation_days')}, must be >=14"
        )


def test_gae_skin_lesion_interval_window_when_present():
    """When skin_lesion_centrofacial_chronic=True, interval to CNS must be 6-30 months
    (Alvarez 2022 JAAD Int: mean skin-lesion duration at diagnosis 15 months,
    range 2 months to 5 years)."""
    for s in GAE_DISTRIBUTION:
        if s.get("skin_lesion_centrofacial_chronic") is True:
            interval = s.get("skin_lesion_to_cns_interval_months")
            assert interval is not None, f"vid={s['vignette_id']} missing interval"
            assert 6 <= interval <= 30, (
                f"vid={s['vignette_id']} skin_lesion_to_cns_interval_months={interval} "
                "out of 6-30 month window"
            )


# ----------------------------------------------------------------------
# Schema encoding workarounds
# ----------------------------------------------------------------------


def test_gae_184_185_geography_region_peru_lima_coast():
    """Slots 184, 185 (Lambayeque + La Libertad) collapsed to peru_lima_coast
    since schema enum lacks peru_lambayeque / peru_la_libertad keys."""
    for vid in (184, 185):
        slot = next(s for s in GAE_DISTRIBUTION if s["vignette_id"] == vid)
        assert slot["geography_region"] == "peru_lima_coast", (
            f"vid={vid} geography_region={slot['geography_region']!r}, "
            "expected peru_lima_coast"
        )
        label = slot["geography_label"]
        assert ("Lambayeque" in label) or ("La Libertad" in label), (
            f"vid={vid} geography_label={label!r} must retain city (Lambayeque / La Libertad)"
        )


def test_crypto_177_178_idiopathic_cd4_encoding():
    """Slots 177, 178 (idiopathic CD4 lymphopenia HIV-neg) encoded
    as immunocompromise_status='none' with cd4_count_cells_per_uL<200 at build time.
    Schema lacks HIV-neutral T-cell-immunodeficiency enum (only HIV-prefixed CD4 tiers)."""
    for vid in (177, 178):
        slot = next(s for s in CRYPTO_DISTRIBUTION if s["vignette_id"] == vid)
        assert slot["demographic_stratum"] == "idiopathic_cd4_lymphopenia", (
            f"vid={vid} demographic_stratum={slot['demographic_stratum']!r}"
        )
        assert slot["hiv_status"] == "negative", (
            f"vid={vid} hiv_status must be negative for idiopathic CD4 lymphopenia"
        )
        assert slot["immunocompromise_status"] == "none", (
            f"vid={vid} immunocompromise_status must be 'none' "
            "(schema lacks HIV-neutral T-cell-immunodeficiency enum; "
            f"got {slot['immunocompromise_status']!r})"
        )
        cd4 = slot.get("cd4_count_cells_per_uL")
        assert cd4 is not None and cd4 < 200, (
            f"vid={vid} cd4_count_cells_per_uL must encode <200 for idiopathic CD4 "
            f"lymphopenia (got {cd4!r})"
        )
