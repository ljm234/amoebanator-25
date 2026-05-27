# Day 2 Baseline Audit - Amoebanator Subphase 1.2

## Source
Generated 2026-05-04 from HEAD `3171f060` (tag `v2.1.2-day2-pmids-canonized`).
Read-only audit before launching Day 2 distribution research.

## Purpose
Ground-truth verification of:
1. `PMID_REGISTRY` actual state (28 entries expected)
2. Day 1 vignettes (v1-v20) demographic distribution
3. Schema constraints currently in force
4. Test coverage and gates
5. Day 2 gap analysis (PMID usage, cluster gaps, demographic gaps)

This document is **NOT staged for commit**. Reviewer reads, decides next step.

## Methodological note on Action 2

The user-supplied audit script for Action 2 referenced fields that do not exist in the actual `VignetteSchema` (`country`, `outcome.disposition`, single-arg `generate_vignette(vid)`). The script was adapted to use the real schema (`geography_region`, `adjudication.anchoring_documentation`, `generate_vignette(spec, pmid_meta)`). All other audit content unchanged.

---

## Section 1: PMID_REGISTRY State

**Total entries: 28** (target met for v2.1.2-day2-pmids-canonized).

### Field completeness

- All 28 entries have all 11 required fields (`pmid`, `doi`, `authors_short`, `authors_full`, `journal`, `journal_short_code`, `year`, `title`, `anchor_type`, `verification_confidence`, `last_verified_date`).
- 0 empty `authors_full` lists.
- 0 missing required fields.

### Per-entry summary table

| PMID | Lead Author | Year | journal_short_code | anchor_type | anchor_subtype | Conf |
|------|-------------|------|--------------------|-------------|----------------|------|
| 8458963 | Lares-Villa F | 1993 | JCM | case_report | - | VERIFIED |
| 8923775 | DeNapoli TS | 1996 | TexMed | **case_report_pediatric_river** | - | 99 |
| 19845995 | Yoder JS | 2010 | EpidemiolInfect | **review_us_surveillance_foundational** | - | 99 |
| 21291600 | Shakoor S | 2011 | EID | case_report | - | VERIFIED |
| 22238170 | Kemble SK | 2012 | CID | case_report | - | VERIFIED |
| 22919000 | Yoder JS | 2012 | CID | case_report | - | VERIFIED |
| 25595746 | Cope JR | 2015 | CID | **case_report_treated_tap_water** | - | 99 |
| 25625800 | Abrahams-Sandí E | 2015 | EID | case_report | - | VERIFIED |
| 26582886 | Capewell LG | 2015 | JPIDS | **review_us_surveillance** | - | 99 |
| 27123690 | Johnson RO | 2016 | MMWR | surveillance | - | VERIFIED |
| 29016297 | Ghanchi NK | 2017 | AJTMH | cohort | - | VERIFIED |
| 31513557 | Vugia DJ | 2019 | MMWR | surveillance | - | VERIFIED |
| 32369575 | Gharpure R | 2021 | CID | **review_global** | - | 99 |
| 32752181 | Retana Moreira L | 2020 | Pathogens | case_report | case_series_environmental_groundwater_central_america | 1.00 |
| 33350926 | Gharpure R | 2021 | EID | **review_us_geographic_range** | - | 99 |
| 33381798 | Celik Y | 2021 | J Trop Pediatr | case_report | case_report_newborn_fatal_extreme_age_atypical | 1.00 |
| 34307045 | Anjum SK | 2021 | IDCases | case_report | case_report_us_tap_water_north_florida | 1.00 |
| 34906097 | Huang S | 2021 | BMC Infect Dis | case_report | case_report_pediatric_fatal_mNGS_dual_compartment_china | 1.00 |
| 35463884 | Zhou W | 2022 | Front Pediatr | case_report | case_report_pediatric_fatal_misdiagnosis_as_bacterial_meningitis | 1.00 |
| 37460088 | Maloney P | 2023 | AJTMH | case_report | - | VERIFIED |
| 37470480 | Eger L | 2023 | JCM | case_report | - | VERIFIED |
| 38526236 | Burki AMK | 2024 | Emerg Infect Dis | case_report | case_report_adult_SURVIVOR_pakistan_first_pakistani_survivor | 1.00 |
| 39606118 | Lin L | 2024 | Front Microbiol | case_report | case_report_pediatric_fatal_atypical_myocarditis_indoor_pool | 1.00 |
| 40009134 | Rauf A | 2025 | IJP | case_report | - | VERIFIED |
| 40146665 | Dulski TM | 2025 | MMWR | surveillance | - | VERIFIED |
| 40440212 | Smith OA | 2025 | MMWR | surveillance | - | VERIFIED |
| 40697059 | Siddiqui R | 2025 | ExpertRevAntiInfect | **review_therapeutic_recent** | - | 99 |
| 40969815 | Li J | 2025 | Front Med (Lausanne) | surveillance | epi_field_investigation_pediatric_fatal_indoor_pool | 1.00 |

### Critical finding: 7 PMIDs hold non-schema-compliant `anchor_type` values

The schema's `LiteratureAnchor.anchor_type` is `Literal['case_report' | 'guideline' | 'review' | 'surveillance' | 'meta_analysis' | 'cohort' | 'rct' | 'prospective_observational']`. The 7 entries below carry descriptive long-forms that would fail `model_validate` if propagated into a `literature_anchors[0]` field:

| PMID | Current `anchor_type` | Recommended fix |
|---|---|---|
| 8923775 DeNapoli | `case_report_pediatric_river` | base `case_report` + move descriptive to `anchor_subtype` |
| 25595746 Cope-Louisiana | `case_report_treated_tap_water` | same pattern |
| 26582886 Capewell | `review_us_surveillance` | base `review` + descriptive to `anchor_subtype` |
| 33350926 Gharpure-EID | `review_us_geographic_range` | base `review` + descriptive to `anchor_subtype` |
| 32369575 Gharpure-CID | `review_global` | base `review` + descriptive to `anchor_subtype` |
| 19845995 Yoder-2010 | `review_us_surveillance_foundational` | base `review` + descriptive to `anchor_subtype` |
| 40697059 Siddiqui | `review_therapeutic_recent` | base `review` + descriptive to `anchor_subtype` |

**Time bomb for Day 2:** PMID 8923775 (DeNapoli) is slated for Day 2 v44 (Rio Grande pediatric river case) per the original distribution preview in the Day 1 spec doc. If used as the anchor without fixing `anchor_type`, vignette 44 will fail `VignetteSchema.model_validate`.

The other 6 entries are Tier 4 review anchors (Capewell 2015, Gharpure 2021 EID + CID, Yoder 2010, Siddiqui 2025) and the 2015 Cope Louisiana case. Whether any are anchored in Day 2 depends on the pending distribution plan; if any are, the same `anchor_type` cleanup is required before generation.

### Schema-shape + provenance metadata

| Field | Coverage |
|---|---|
| `anchor_subtype` (descriptive form, Day-2-style) | 8 / 28 entries |
| `author_aliases` | 1 / 28 (`38526236` Burki only) |
| Legacy `aliases` field (pre-Day-2) | 0 entries (cleanly migrated) |
| `verification_method` | 8 / 28 (only the Day-2-canonized entries; the 20 Day-1-locked entries lack this) |
| `pmc_id` populated | 19 / 28 |

### `verification_confidence` type heterogeneity

| Type | Count | Source |
|---|---|---|
| `str` (e.g., `"VERIFIED"`) | 13 | Day 1 originals |
| `int` (e.g., `99`) | 7 | 5-pass new entries (Capewell, Cope, Gharpure-EID, etc.) |
| `float` (`1.00`) | 8 | Day 2 canonization |

Test passes today because the assertion is truthiness-only. For corpus uniformity, consider normalizing to a single type in a future sweep.

### `last_verified_date` distribution

| Date | Count |
|---|---|
| `2026-05-04` | 27 |
| `2026-05-03` | 1 |

The single `2026-05-03` entry remains from a Day 1 sweep; not a defect, but represents the only PMID not touched by the 5-pass + Day-2 sweeps.

---

## Section 2: Day 1 Vignettes Demographic Audit

### Per-vignette table (v1-v20)

| Vid | Age | Sex | Geography | Cluster | Stage | Outcome | PMID |
|-----|-----|-----|-----------|---------|-------|---------|------|
| v01 | 16 months | male | Arkansas, US | splash_pad | late | fatal | 40146665 |
| v02 | 3 years | female | Arkansas, US | splash_pad | mid | fatal | 40146665 |
| v03 | 3 years | male | Texas, US | splash_pad | mid | fatal | 37470480 |
| v04 | 4 years | male | Texas, US | splash_pad | late | fatal | 37470480 |
| v05 | 7 years | female | Minnesota, US | lake_pond | late | fatal | 22238170 |
| v06 | 13 years | male | Florida, US | lake_pond | mid | fatal | 34307045 |
| v07 | 8 years | male | Nebraska, US | lake_pond | late | fatal | 37460088 |
| v08 | 9 years | male | Minnesota, US | lake_pond | mid | fatal | 22238170 |
| v09 | 14 years | male | Florida, US | lake_pond | late | fatal | 34307045 |
| v10 | 28 years | male | Louisiana, US | nasal_irrigation | mid | fatal | 22919000 |
| v11 | 51 years | female | Louisiana, US | nasal_irrigation | late | fatal | 22919000 |
| v12 | 71 years | female | Texas, US | nasal_irrigation | mid | fatal | 40440212 |
| v13 | 12 years | male | California, US | hot_springs | mid | fatal | 31513557 |
| v14 | 21 years | female | California, US | hot_springs | late | fatal | 27123690 |
| v15 | 13 years | male | Karachi, PK | pakistan_ablution | late | fatal | 21291600 |
| v16 | 28 years | male | Karachi, PK | pakistan_ablution | mid | fatal | 29016297 |
| v17 | 11 years | male | Florida (acquired Costa Rica) | latam | late | fatal | 25625800 |
| v18 | 9 years | male | Mexicali, MX | latam | mid | fatal | 8458963 |
| v19 | 22 years | male | Karachi, PK | survivor_adult | mid | survived | 38526236 |
| v20 | 14 years | male | Kerala, IN | survivor_pediatric | mid | survived | 40009134 |

### Cluster distribution

| Cluster | n | % |
|---|---|---|
| lake_pond | 5 | 25.0% |
| splash_pad | 4 | 20.0% |
| nasal_irrigation | 3 | 15.0% |
| hot_springs | 2 | 10.0% |
| pakistan_ablution | 2 | 10.0% |
| latam | 2 | 10.0% |
| survivor_adult | 1 | 5.0% |
| survivor_pediatric | 1 | 5.0% |

### Sex distribution

| Sex | n | % |
|---|---|---|
| male | 15 | 75.0% |
| female | 5 | 25.0% |

### Outcome distribution

| Outcome | n | % |
|---|---|---|
| fatal | 18 | 90.0% |
| survived | 2 | 10.0% |

### Stage distribution

| Stage | n | % |
|---|---|---|
| mid | 11 | 55.0% |
| late | 9 | 45.0% |

(Note: zero `early` stage in Day 1. Early-stage PAM is rarely PMID-anchored because patients typically present at mid- or late-stage; this is a clinical-realism feature, not a gap.)

### Age buckets

| Bucket | n | % |
|---|---|---|
| 0-4 (infant/toddler) | 4 | 20.0% |
| 5-12 (school-age) | 6 | 30.0% |
| 13-17 (adolescent) | 4 | 20.0% |
| 18-34 (young adult) | 4 | 20.0% |
| 35-64 (adult) | 1 | 5.0% |
| 65+ (elder) | 1 | 5.0% |

### Geography distribution

| Geography | n |
|---|---|
| Texas, US | 3 |
| Karachi, PK | 3 |
| Arkansas, US | 2 |
| Minnesota, US | 2 |
| Florida, US | 2 |
| Louisiana, US | 2 |
| California, US | 2 |
| Nebraska, US | 1 |
| Florida (acquired Costa Rica) | 1 |
| Mexicali, MX | 1 |
| Kerala, IN | 1 |

US: 14 (70%); Pakistan: 3; Mexico: 1; Costa Rica (US-acquired): 1; India: 1.

### PMID usage in Day 1

| Metric | Count |
|---|---|
| Distinct PMIDs used in Day 1 | 15 |
| Registry total | 28 |
| **PMIDs unused (Day 2 candidates)** | **13** |

Per-PMID Day 1 usage (5 PMIDs anchor 2 vignettes each; 10 anchor 1 each):

| Day 1 usage count | PMIDs |
|---|---|
| 2 | 40146665 (Dulski splash pad), 37470480 (Eger splash pad), 22238170 (Kemble Minnesota), 34307045 (Anjum Florida), 22919000 (Yoder Louisiana) |
| 1 | 37460088, 40440212, 31513557, 27123690, 21291600, 29016297, 25625800, 8458963, 38526236, 40009134 |

### 13 PMIDs available for Day 2 anchoring

| PMID | Year | Lead author | Anchor classification |
|---|---|---|---|
| 8923775 | 1996 | DeNapoli TS | case_report (Rio Grande pediatric river) |
| 19845995 | 2010 | Yoder JS | review (US surveillance, foundational, 1962-2008) |
| 25595746 | 2015 | Cope JR | case_report (treated tap water Louisiana) |
| 26582886 | 2015 | Capewell LG | review (US surveillance 1937-2013) |
| 32369575 | 2021 | Gharpure R | review (global, 381 cases 1937-2018) |
| 32752181 | 2020 | Retana Moreira L | case_report / case series (Costa Rica groundwater) |
| 33350926 | 2021 | Gharpure R | review (US geographic range 1978-2018) |
| 33381798 | 2021 | Celik Y | case_report (newborn extreme-age) |
| 34906097 | 2021 | Huang S | case_report (China mNGS dual-compartment) |
| 35463884 | 2022 | Zhou W | case_report (China misdiagnosis differential) |
| 39606118 | 2024 | Lin L | case_report (Sichuan myocarditis atypical) |
| 40697059 | 2025 | Siddiqui R | review (therapeutic, recent) |
| 40969815 | 2025 | Li J | surveillance (Chengdu epi field investigation, same patient as Lin 2024) |

**Reviews and review-style anchors (5):** Yoder 2010, Capewell 2015, Gharpure 2021 EID, Gharpure 2021 CID, Siddiqui 2025. These can each anchor multiple Day 2 vignettes (review-anchored Tier 4 IMPUTED_FROM_LITERATURE_REVIEW pattern).

**Direct case anchors (8):** DeNapoli, Cope-Louisiana, Retana Moreira, Celik, Huang, Zhou, Lin, Li.

---

## Section 3: Schema State

`ml/schemas/vignette.py` is **LOCKED at v2.0-schema-locked** (commit `cd3e30d`). No modifications during 5-pass or Day 2 sweeps.

### Top-level VignetteSchema fields

```
schema_version            Literal['2.0']
case_id                   str
ground_truth_class        ClassLabel
demographics              Demographics
history                   History
exposure                  ExposureHistory
vitals                    VitalSigns
exam                      PhysicalExam
labs                      Labs
csf                       CSFProfile
imaging                   Imaging
diagnostic_tests          DiagnosticTests
adjudication              AdjudicationMetadata
literature_anchors        List[LiteratureAnchor]
provenance                Provenance
narrative_es              Optional[str]
narrative_en              Optional[str]
```

### Critical Literal sets enforced by schema

**`LiteratureAnchor.anchor_type`** (8 values):
`case_report | guideline | review | surveillance | meta_analysis | cohort | rct | prospective_observational`

**`Demographics.geography_region`** (10 values):
`peru_lima_coast | peru_loreto_amazon | peru_cusco_altitude | peru_puno_altitude | peru_tumbes | peru_madre_de_dios | us_south | pakistan_karachi | other_latam | other_global`

**`ExposureHistory.freshwater_exposure_type`** (8 values):
`lake | river | hot_spring | splash_pad | swimming_pool_unchlorinated | neti_pot_tap_water | ritual_ablution_wudu | none`

**`Imaging.imaging_pattern`** (14 values, includes `normal` + 13 disease-specific patterns).

**`History.chief_complaint`** (10 values):
`headache | fever_with_headache | altered_mental_status | seizure | focal_deficit | neck_stiffness | vomiting | behavioral_change | thunderclap_headache | gait_ataxia`

### Length constraint

`Provenance.inclusion_decision_rationale` is `max_length=1000`. Generator's `_build_provenance` was patched in commit `3171f060` to budget-cap the appended `caveat` so verbose registry caveats (Burki, Anjum) don't blow this limit; truncates with `...` marker if overflow.

### Test-side journal-code allow-list (post-Day-2 widening)

```
{"MMWR", "JCM", "CID", "IDCases", "AJTMH", "EID", "IJP",
 "Emerg Infect Dis", "Front Microbiol", "Front Med (Lausanne)",
 "Pathogens", "Front Pediatr", "BMC Infect Dis", "J Trop Pediatr",
 "TexMed", "JPIDS", "EpidemiolInfect", "ExpertRevAntiInfect"}
```

### Test-side case_id regex

```
r"^PAM-D1-(\d{3})-(.+?)-(\d{4})-(.+)$"
```

Non-greedy journal capture allows Vancouver-style codes with spaces and parentheses (e.g., `Front Med (Lausanne)`).

---

## Section 4: Test Coverage

| Suite | Tests | Status |
|---|---|---|
| `tests/vignettes/test_pam_vignettes.py` | 37 | passed |
| `tests/schemas/` | 24 | passed (1 skipped) |
| **Combined** | **62 collected, 61 passed, 1 skipped** | **GREEN** |

`test_pmid_metadata_completeness` is parametrized over all 28 `PMID_REGISTRY` keys; growing the registry automatically grows test coverage.

`test_case_id_format` and `_ALLOWED_JOURNAL_CODES` accept Vancouver-style journal codes with spaces/parens.

Schema 20/20 dry-run for Day 1 vignettes: **20 PASS / 0 FAIL**.

Quality gates (script + audit doc):
- Em-dashes: 0 / 0
- AI-tells: 0 / 0
- AST parse: OK
- UTF-8 diacritics preserved: `Sandí` (175 occurrences in script across narratives + author lists + caveats), `Ertuğ` (3 occurrences)

---

## Section 5: Day 2 Gap Analysis Recommendations

Day 2 must add 40 vignettes (v21-v60) to reach the 60-vignette corpus target. The original Day 1 spec doc's "Day 2 Planned Distribution Preview" listed:

| Cluster | Day 2 add | Final 60 % |
|---|---|---|
| Lake/pond | 19 | 40% |
| River | 12 | 20% |
| Splash pad | 5 | 15% |
| Neti pot | 6 | 15% |
| Hot spring | 1 | 5% |
| Ablution | 1 | 5% |
| **Total** | **44** | -- |

The numbers sum to **44, not 40**. Reconciliation possibilities:
- **Option A (proportional trim):** Lake 17 + River 10 + Splash 5 + Neti 6 + Hot 1 + Ablution 1 = 40
- **Option B (fold survivor + LATAM into base clusters):** Day 1's LATAM (v17 hot-spring travel, v18 river canal) and survivor (v19 ablution, v20 lake) effectively belong to underlying clusters; if reclassified, Day 2 needs Lake 18 + River 11 + Splash 5 + Neti 6 + Hot 0 + Ablution 0 = 40

These are the two main interpretations. A formal Day 2 distribution plan should declare the chosen reconciliation and lock it.

### PMID supply analysis

Current available PMID anchor pool for Day 2:

- **13 unused PMIDs already in registry** (5 reviews + 8 case anchors).
- **13 bonus PMIDs from Day 1 spec doc not yet in registry** (Phung 2025 Vietnam infant cryptic, Wang 2018 China NGS, Wei 2024 Taiwan indoor surfing, Cogo 2004 Italy, Sazzad 2020 Bangladesh, Hong 2023 Korea travel-imported, Linam 2015 Kali Hardig + 28013053 LoC + 29241583 Response, Hall 2024 survivor review, Aurongzeb 2022 Iran J Parasitol Pakistan, Kou 2025 Henan bathhouse, CDC 2013 USVI ablution, Ghanchi 2016 EID Karachi water supply).

Total potential anchor pool: **26 PMIDs for 40 vignettes** (mean ~1.5 vignettes per PMID), sufficient.

### Pre-Day-2 cleanup recommendations

Before running Day 2 generation:

1. **Fix the 7 non-schema-compliant `anchor_type` values** in the registry. Pattern: move descriptive form to `anchor_subtype`, set base `anchor_type` to `case_report` or `review` per the schema's Literal set. This unblocks DeNapoli (v44 anchor) and any review-anchored Day 2 vignettes.
2. **Lock the 13 bonus PMIDs not yet in registry** via the same user-side PubMed UI direct fetch + verification methodology used for Day 2 canonization. Each entry will need verbatim author lists, PMC IDs, DOIs.
3. **Decide and lock Day 2 cluster reconciliation** (Option A or Option B above) before any vignette generation begins.
4. **Decide demographic targets for Day 2** that, combined with Day 1, yield the desired full-60 distribution. Day 1 alone is 75% male / 25% female and 90% fatal / 10% survived; if the 60-vignette target wants ~80% male and ~7-10% survivors, Day 2 should add roughly 8 female + 32 male and 4 survivors.
5. **Decide special-case requirements**: 1 cryptic (Phung 2025), 1 atypical presentation (Lin 2024 myocarditis), 1 travel-imported (Hong 2023), Linam 2015 Kali Hardig pair (3-PMID anchor chain).

### Anything else surfaced by the audit

- **Two LATAM vignettes (v17, v18) lack a true Latin-American geography_region**. Schema's `geography_region` doesn't have a Costa Rica or Mexico value; both v17 and v18 use `other_latam`. If Day 2 adds more LATAM cases, they'll all collapse to the same enum value, which is fine for class-conditional epidemiology but loses geographic granularity.
- **No early-stage PAM vignettes in Day 1** (0 / 20). PAM clinically presents mid-to-late, so this is realistic. If Day 2 wants a treatable-stage case (e.g., Burki-style early presentation that survived), it would be the first early-stage entry.
- **`verification_confidence` type heterogeneity** (str/int/float) is harmless but cosmetic. Could be normalized in a future sweep.
- **Diacritic provenance:** `Abrahams-Sandí` is the only diacritic-bearing author name in `authors_full` registry-wide (UTF-8 `c3 ad`). All Day 1 vignette `narrative_es` strings collectively contain ~175 instances of `c3 ad` plus other Spanish accents, which is the bulk of the UTF-8 footprint. `Ertuğ` (UTF-8 `c4 9f`) appears only in the Celik 2021 caveat documentary text.

### Day 2 readiness checklist (to be addressed BEFORE generation)

- [ ] Lock cluster reconciliation (Option A or B)
- [ ] Lock demographic targets for Day 2 alone (sex, outcome, age buckets)
- [ ] Lock special-case requirements (cryptic, atypical, travel, Kali Hardig pair)
- [ ] Fix 7 non-compliant `anchor_type` values (move to `anchor_subtype`)
- [ ] Add 13 bonus PMIDs to registry via user-side PubMed UI verification
- [ ] Re-confirm 28 -> ~41 registry size after PMID addition
- [ ] Lock 40-row Day 2 distribution table (vignette_id, cluster, PMID, age, sex, geography, stage, outcome, atypical_type)

---

## Status at audit completion

| | |
|---|---|
| Local HEAD | `3171f060` |
| origin/main | `3171f060` |
| hf/main | `3171f060` |
| Latest tag | `v2.1.2-day2-pmids-canonized` (object `c889424`, deref `3171f060`) |
| Registry size | 28 PMIDs |
| Day 1 vignettes | 20 (locked, 20/20 schema-validate) |
| Tests | 61 passed, 1 skipped, 0 failed |
| Diacritic preservation | OK (`Sandí`, `Ertuğ` byte-perfect) |
| Em-dash / AI-tell | 0 / 0 in script + all docs |

**No code, registry, test, or schema modifications were made during this audit.**
