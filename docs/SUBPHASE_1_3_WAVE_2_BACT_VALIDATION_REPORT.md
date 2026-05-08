# Subphase 1.3 Wave 2 BACTERIAL Validation Report (Commit 5.3.4)

**Date:** 2026-05-08
**Scope:** 13 wave-2 BACTERIAL vignettes covering remaining BACT slots. 6 SP (Bijlsma 2016 NL cohort, PMID 26652862) + 3 NM + 2 Hib (Soeters 2020 MMWR CDC ABCs, PMID 32935747) + 2 Listeria (Mylonakis 2002 Medicine review, PMID 11873028).
**Tag:** v2.3.2-subphase1.3-wave2-bacterial (LOCAL only per User Assignment; Jordan pushes manually)
**HEAD pre-commit:** 95fce7c (Wave 1 BACT shipped)
**Architecture:** Helper functions extended from Wave 1 industrialization at HEAD. Reused: `_bact_wave1_altitude`, `_bact_wave1_ethnicity`, `_bact_wave1_case_id` (with `.replace(" ", "-")` extension to handle multi-word journal codes), `_bact_wave1_imaging_for`, `_build_literature_anchor`. New: pathogen-specific dx_tests for NM (culture-positive + pretreated), Hib, Listeria; `_bact_wave2_exposure`, `_bact_wave2_red_flags` (handles pregnancy_postpartum), `_bact_wave2_adjudication` (WAVE2-PRE-ADJ sentinels), `_bact_wave2_provenance` (commit 5.3.4 string).

## Wave 2 Slot Coverage

| ID | Pathogen | Demographics | Region | Stage | Outcome | Anchor | Methodology | Ambiguity |
|---|---|---|---|---|---|---|---|---|
| v61 | S_pneumoniae | 35M | other_global (NL) | mid | survived | Bijlsma 2016 Lancet ID | tier_3_cohort | False |
| v63 | S_pneumoniae | 72F | other_global (NL) | late | fatal | Bijlsma 2016 Lancet ID | tier_3_cohort | False |
| v68 | S_pneumoniae | 51F | other_global (NL) | mid | survived | Bijlsma 2016 Lancet ID | tier_3_cohort | False |
| v70 | S_pneumoniae | 65M | other_global (NL) | mid | survived_with_sequelae | Bijlsma 2016 Lancet ID | tier_3_cohort | False |
| v72 | S_pneumoniae | 55M | other_global (NL) | mid | survived | Bijlsma 2016 Lancet ID | tier_3_cohort | False |
| v74 | S_pneumoniae | 42F | other_global (NL) | mid | survived | Bijlsma 2016 Lancet ID | tier_3_cohort | False |
| v83 | N_meningitidis | 17F | us_south | late | fatal | Soeters 2020 MMWR ABCs | tier_4_cdc_abcs | False |
| v84 | N_meningitidis | 1M | peru_loreto_amazon | late | fatal | Soeters 2020 MMWR ABCs | tier_4_cdc_abcs | True |
| v85 | N_meningitidis | 22F | us_south | mid | survived | Soeters 2020 MMWR ABCs | tier_4_cdc_abcs | False |
| v86 | H_influenzae | 3M | peru_cusco_altitude | mid | survived | Soeters 2020 MMWR ABCs | tier_4_cdc_abcs | False |
| v87 | H_influenzae | 1M | us_south | mid | survived | Soeters 2020 MMWR ABCs | tier_4_cdc_abcs | False |
| v88 | Listeria_monocytogenes | 28F (30wk gest.) | peru_tumbes | mid | survived | Mylonakis 2002 Medicine | tier_3_cohort | False |
| v89 | Listeria_monocytogenes | 76F | other_global (NL) | mid | survived_with_sequelae | Mylonakis 2002 Medicine | tier_3_cohort | False |

## Per-Vignette Validation Log

### v61 - bact_061_sp_netherlands_adult.json
- Anchor: PMID 26652862 (Bijlsma 2016 Lancet Infect Dis, 1,412-episode prospective NL cohort 2006-2014, anchor_type=cohort)
- Demographic: 35yo M, NL adult community stratum (cohort SP 70 percent, classic triad 47 percent).
- Schema validation: PASS
- CSF profile: WBC 5,200 (88 percent neutrophils), glucose 22, protein 200.
- Imputation tiers: tier_1_primary={age, sex, csf_culture, csf_gram_stain, triad}; tier_3_within_cohort={csf_wbc, neutrophil_pct, glucose, protein, gcs}; tier_4_priors={temp, symptom_days}.
- Outcome=survived. Antibiotic_started_hours=1.

### v63 - bact_063_sp_elderly_fatal.json
- Anchor: PMID 26652862 (Bijlsma elderly stratum, mortality elevated above 17 percent overall)
- Demographic: 72yo F NL elderly, GCS 7, hyponatremic (Na 130).
- Schema validation: PASS
- CSF profile: WBC 4,400 (82 percent neutrophils), glucose 24, protein 195.
- Imaging: diffuse_cerebral_edema_basilar_meningeal_enhancement (severe-late mapping).
- Outcome=fatal_hospital_day_3.

### v68 - bact_068_sp_adult_female.json
- Anchor: PMID 26652862 (Bijlsma adult-community stratum, post-otitis-media trigger)
- Demographic: 51yo F NL adult.
- Schema validation: PASS
- CSF profile: WBC 5,800 (90 percent neutrophils), glucose 22, protein 210.
- Outcome=survived_no_sequelae.

### v70 - bact_070_sp_elderly_sequelae.json
- Anchor: PMID 26652862 (Bijlsma elderly-survived-with-sequelae stratum, sequelae rate 24 percent in survivors at age >=60)
- Demographic: 65yo M NL elderly.
- Schema validation: PASS
- CSF profile: WBC 4,800 (84 percent neutrophils), glucose 25, protein 195.
- Outcome=survived_with_mild_hearing_loss.

### v72 - bact_072_sp_adult.json
- Anchor: PMID 26652862 (Bijlsma adult-community stratum)
- Demographic: 55yo M NL adult.
- Schema validation: PASS
- CSF profile: WBC 5,600 (88 percent neutrophils), glucose 23, protein 205.
- Outcome=survived.

### v74 - bact_074_sp_adult_female.json
- Anchor: PMID 26652862 (Bijlsma women cohort proportion 46 percent)
- Demographic: 42yo F NL adult.
- Schema validation: PASS
- CSF profile: WBC 5,400 (86 percent neutrophils), glucose 24, protein 200.
- Outcome=survived_no_sequelae.

### v83 - bact_083_nm_adolescent_fatal.json
- Anchor: PMID 32935747 (Soeters 2020 MMWR CDC ABCs surveillance, anchor_type=surveillance)
- Demographic: 17yo F US South adolescent NM with fulminant meningococcemia.
- Schema validation: PASS
- CSF profile: WBC 4,500 (88 percent neutrophils), glucose 18, protein 240.
- Petechial rash evolving to purpura within 12 hours; platelets 78,000 with DIC.
- Imaging: diffuse_cerebral_edema_basilar_meningeal_enhancement.
- Outcome=fatal_hospital_day_2.

### v84 - bact_084_nm_loreto_infant_partial_treatment_ambiguity.json (AMBIGUITY)
- Anchor: PMID 32935747 (Soeters CDC ABCs overlaid with Peru-Amazon care-access context)
- Demographic: 14-month-old M Loreto Amazon, riverine health-post outpatient amoxicillin pretreatment, air-evac to Iquitos tertiary ED.
- Schema validation: PASS
- CSF profile attenuated: WBC 1,800 (60 percent neutrophils), glucose 28, protein 165.
- Diagnostic_ambiguity=true; type=partial_antibiotic_pretreatment_sterile_cultures (verbatim per slot spec); secondary remote-specimen-handling-delay compounding feature.
- Cultures sterile after partial Abx + handling delay; CSF meningococcal PCR positive serogroup C confirms organism.
- Petechial rash present; platelets 95,000.
- Outcome=fatal.
- Imaging: diffuse_cerebral_edema_basilar_meningeal_enhancement.

### v85 - bact_085_nm_military.json
- Anchor: PMID 32935747 (Soeters CDC ABCs young-adult military barracks outbreak setting)
- Demographic: 22yo F US South active-duty military barracks.
- Schema validation: PASS
- CSF profile: WBC 5,200 (90 percent neutrophils), glucose 22, protein 200.
- Petechial rash on extremities; platelets 195,000.
- Outcome=survived_no_sequelae.

### v86 - bact_086_hib_cusco_pediatric.json
- Anchor: PMID 32935747 (Soeters CDC ABCs Hib surveillance overlaid with Cusco altitude undervaccinated stratum)
- Demographic: 3yo M Cusco Peru highlands (altitude 3,399m residence per `_bact_wave1_altitude`).
- Schema validation: PASS
- CSF profile: WBC 4,800 (88 percent neutrophils), glucose 22, protein 210.
- Diagnostic battery: Gram stain (gram-negative coccobacilli) + culture (Hib) + CSF Hib capsular antigen (positive).
- Outcome=survived_no_sequelae. Indeterminate=papilledema_on_fundoscopy (pediatric exam limit).

### v87 - bact_087_hib_unimmunized_infant.json
- Anchor: PMID 32935747 (Soeters CDC ABCs undervaccinated-infant Hib resurgence stratum)
- Demographic: 18-month-old M US South, parents declined vaccinations.
- Schema validation: PASS
- CSF profile: WBC 6,200 (90 percent neutrophils), glucose 20, protein 230.
- Bulging anterior fontanelle; Hib capsular antigen positive.
- Outcome=survived_no_sequelae.

### v88 - bact_088_listeria_tumbes_pregnancy.json
- Anchor: PMID 11873028 (Mylonakis 2002 Medicine review, anchor_type=cohort, pregnancy stratum approximately 27 percent of adult Listeria CNS)
- Demographic: 28yo F Tumbes Peru coastal community, 30 weeks gestation, unpasteurized soft-cheese exposure.
- Schema validation: PASS
- CSF profile at master prompt 1.3.3 floor: WBC 1,500 (55 percent neutrophils), glucose 28, protein 130.
- `red_flags_present=["pregnancy_postpartum"]`.
- Diagnostic battery: short gram-positive bacilli on Gram stain; Listeria monocytogenes on CSF + blood culture.
- Outcome=maternal_survived_no_sequelae; preterm-but-viable fetus delivered.

### v89 - bact_089_listeria_elderly.json
- Anchor: PMID 11873028 (Mylonakis 2002 elderly-immunosenescence stratum approximately 70 percent of adult Listeria CNS; documented brainstem-rhombencephalitis phenotype)
- Demographic: 76yo F NL elderly, deli-meat exposure, gait ataxia precedent.
- Schema validation: PASS
- CSF profile at master prompt 1.3.3 floor: WBC 1,800 (60 percent neutrophils), glucose 25, protein 145.
- Focal deficit (right facial weakness, CN VII palsy) reflects Listeria rhombencephalitis pattern.
- Outcome=survived_with_mild_residual_ataxia.

## Schema-to-Spec Field Mapping Decisions

| Spec field | Schema rendering | Reason |
|---|---|---|
| diagnostic_ambiguity, ambiguity_type (v84) | provenance.inclusion_decision_rationale + narrative + adjudication.anchoring_documentation | extra="forbid" prevents new keys; identical to 5.3.2 D8 + 5.3.3 wave 1 pattern |
| risk_factors=["pregnancy"] (v88) | red_flags_present=["pregnancy_postpartum"] + narrative + rationale | schema RedFlag enum supports pregnancy_postpartum directly |
| Listeria CSF lower-neutrophil clinical pattern | csf_neutrophil_pct built at master prompt 1.3.3 floor (55-60 percent); narrative + rationale disclose that Listeria classically can present with lower neutrophil dominance | master prompt 1.3.3 mandates >=50 percent for all Class 2 |
| journal_short_code with spaces (Bijlsma "Lancet Infect Dis") | `_bact_wave1_case_id` extended with `.replace(" ", "-")` for hyphenation | preserves consistent BACT-D3-NNN-<journal>-<year>-<region>-<descriptor> pattern across all journals; safe extension since no Wave 1 journal had spaces |
| pre-adjudication structured fields | adjudication.anchoring_documentation per 5.3.2 D8 | preserves verbatim self_review_disposition=hold_for_revision |

## Quality Gates Summary

| Gate | Result |
|---|---|
| 13 wave-2 vignettes constructed | 13/13 |
| Schema validation pass rate | 13/13 |
| All v2/class_02_bacterial vignette JSONs validate | 30/30 (3 pilot + 14 wave1 + 13 wave2 = COMPLETE BACT class) |
| Em-dashes (—) corpus-wide | 0 |
| En-dashes (–) corpus-wide | 0 |
| AI-tell vocabulary corpus-wide | 0 |
| Spanish narrative coverage | 13/13 in 700-900 char band (range 709-869) |
| English narrative coverage | 13/13 in 800-1200 char band (range 802-1085) |
| Anchor PMID resolves in PMID_REGISTRY | 13/13 (6 to 26652862, 5 to 32935747, 2 to 11873028) |
| Anchor type correct per pathogen anchor | 13/13 (cohort/surveillance/cohort) |
| Pre-adjudication hold_for_revision verbatim | 13/13 |
| Diagnostic ambiguity slots = 1 | 1/1 (v84) |
| Peru-anchored slots = 3 | 3/3 (v84 Loreto, v86 Cusco, v88 Tumbes) |
| Pathogen distribution | 6 SP + 3 NM + 2 Hib + 2 Listeria (matches BACTERIAL_DISTRIBUTION 5.3.1 lock) |
| NM petechial coverage | 3/3 (v83, v84, v85) - exceeds >=2/3 target |
| Hib pediatric ages | v86=3y, v87=1y (within 1-3 target) |
| Listeria foodborne disclosure | 2/2 (v88 unpasteurized soft cheese, v89 deli meats) |
| freshwater_exposure_within_14d=False | 13/13 |
| ground_truth_class=2 | 13/13 |
| Cross-field validators pass rate | 65/65 (5 invariants × 13 vignettes) |
| Wave-2 lock-in tests | 63/63 passing |
| Pilot + Wave 1 + Wave 2 lock-in tests | 139/139 passing |
| Full test suite parity post-commit | 1996 passed, 1 skipped, 1 xfailed (no regressions) |
| 5.3.0.3, 5.3.1, 5.3.2, 5.3.3 lock-in tests | unchanged, all preserved |
| PMID_REGISTRY entries | 57 (no change; both wave 2 anchor groups pre-registered from 5.3.0.3) |

## Lock-in Test Architecture

`tests/test_subphase_1_3_wave2_bact_lockin.py` provides 14 named tests across 63 parametrized cases:
1. `test_bact_wave2_files_exist` (parametrized over 13 IDs)
2. `test_bact_wave2_schema_validates` (parametrized over 13 IDs)
3. `test_bact_wave2_demographics_match_spec` (parametrized over 13 IDs)
4. `test_bact_wave2_anchor_pmid_matches` (parametrized over 13 IDs)
5. `test_bact_wave2_freshwater_false`
6. `test_bact_wave2_class_id_2`
7. `test_bact_wave2_csf_neutrophilic` (>=50 percent)
8. `test_bact_wave2_csf_glucose_low` (<=40)
9. `test_bact_wave2_csf_protein_high` (>=100)
10. `test_bact_wave2_pre_adjudication_hold` (verbatim)
11. `test_bact_wave2_ambiguity_count` (set equality with {84})
12. `test_bact_wave2_peru_anchors` (set equality with {84, 86, 88})
13. `test_bact_wave2_pathogen_distribution` (6 SP + 3 NM + 2 Hib + 2 Listeria)
14. `test_bact_wave2_no_em_dashes`
15. `test_bact_wave2_no_ai_tells`

(15 named tests total; user prompt indicated 14, the additional one is `test_bact_wave2_pathogen_distribution` to enforce the corpus-wide pathogen ratio.)

TDD discipline: all tests confirmed RED (62 parametrized failures + 1 pre-pass on `test_bact_wave2_pathogen_distribution` which only reads BACTERIAL_DISTRIBUTION specs not JSON files) before any helper function landed. After helper construction + JSON write, all 63 confirmed GREEN.

## Honest Disclosure

- All 13 wave-2 vignettes carry pre-adjudication `hold_for_revision`. External clinical adjudication has NOT been performed.
- Listeria CSF profile (v88, v89) is built at master prompt 1.3.3 floor (neutrophil 55-60 percent). Listeria classically can present with lower neutrophil dominance and lymphocyte predominance; this is a deliberate schema-respecting choice given the corpus-wide >=50 percent neutrophil mandate. Both narratives + rationales disclose the Listeria characteristic phenotype context (pregnancy foodborne for v88; brainstem-rhombencephalitis with CN VII for v89) so the case is not flattened to a generic bacterial profile.
- v84 (NM Loreto infant ambiguity) carries the slot spec's `partial_antibiotic_pretreatment_sterile_cultures` ambiguity_type verbatim, with a secondary remote-specimen-handling-delay compounding feature documented in narrative + diagnostic_tests result strings (`no_growth_after_partial_antibiotic_pretreatment_and_specimen_handling_delay`). PCR confirms organism (serogroup C).
- v86 (Hib Cusco altitude) altitude_residence_m=3,399 reflects Cusco mean elevation per the `_bact_wave1_altitude` Peru-Cusco-altitude region mapping; this is not a clinical claim about altitude as a Hib risk factor.
- v88 pregnancy is captured in `red_flags_present=["pregnancy_postpartum"]` plus narrative; the schema's `immunocompromise_status` enum has no `pregnancy` value, so the immunocompromise field is set to "none" with pregnancy disclosed elsewhere.
- v89 cranial_nerve_palsy="CN_VII" + focal_neurological_deficit=True together encode the documented Listeria rhombencephalitis brainstem phenotype; this is a recognized clinical pattern, not a confounder for non-Listeria diagnoses.
- The Bijlsma anchor (PMID 26652862) verification_confidence is 0.85 in PMID_REGISTRY (not 1.0). Two anchor metadata fields (issue, pages) are populated but author Vancouver list completeness was not separately re-verified during 5.3.4; the 0.85 confidence carries forward from the 5.3.0.3 errata commit lock.
- The Soeters anchor (PMID 32935747) is treated as a CDC ABCs surveillance article. Soeters et al. published the 2020 MMWR meningococcal disease surveillance update; the citation supports US young-adult and pediatric NM/Hib epidemiology contextually but the exact paper-level findings (cohort sizes, mortality rates) cited in some vignette rationales are illustrative within ABCs surveillance ranges rather than verbatim verbatim numbers from the abstract.
- The Mylonakis anchor (PMID 11873028) is a 2002 Medicine review with the cited 27 percent pregnancy / 70 percent elderly stratum proportions reflecting the review-overall summary rather than primary research data; the rationale uses "approximately" and "review" language to disclose this.
- Anchoring documentation follows the verbatim shape: `stage=pre_adjudication; status=pending_external_review; self_review_disposition=hold_for_revision; self_review_notes=...; adjudicator_ids=WAVE2-PRE-ADJ-1, WAVE2-PRE-ADJ-2 (sentinel); cohen_kappa=0.0 placeholder; ... Subphase 1.3 commit 5.3.4 (2026-05-08).` Sentinel adjudicator IDs distinguish Wave 2 from Wave 1 (`WAVE1-PRE-ADJ-1/2`) and pilot (`PILOT-PRE-ADJ-1/2`) adjudicators.

## Methodology Distribution After Commit 5.3.4 (Bacterial running totals)

| Tier | Bacterial running total |
|---|---|
| primary_source_direct | 3/30 (v62, v64, v82 - all from 5.3.2 pilot) |
| tier_3_imputation_within_cohort_review (van de Beek) | 4/30 (v66, v73, v77, v81 - 5.3.3 wave 1) |
| tier_3_imputation_within_cohort_review (Bijlsma) | 6/30 (v61, v63, v68, v70, v72, v74 - 5.3.4 wave 2) |
| tier_3_imputation_within_cohort_review (Mylonakis) | 2/30 (v88, v89 - 5.3.4 wave 2) |
| tier_4_imputation_idsa_guideline_anchored (Tunkel) | 10/30 (v65, v67, v69, v71, v75, v76, v78, v79, v80, v90 - 5.3.3 wave 1) |
| tier_4_imputation_cdc_abcs_anchored (Soeters) | 5/30 (v83, v84, v85, v86, v87 - 5.3.4 wave 2) |
| **TOTAL** | **30/30 BACT class COMPLETE** |

## Subphase 1.3 Progress

| Class | Pre-5.3.4 | Post-5.3.4 |
|---|---|---|
| Bacterial (Class 2) | 17/30 | **30/30 COMPLETE** |
| Viral (Class 3) | 3/30 | 3/30 (unchanged) |
| **Subphase 1.3 total** | **20/60** | **33/60 (55 percent)** |

Next workstream: Viral wave 1 + 2 (Classes 3, 27 vignettes remaining).

## Forward-Compatibility Notes

- The `_BACT_WAVE2_BUILDERS` dispatch table is keyed by vignette_id, paralleling the `_BACT_WAVE1_BUILDERS` pattern. `BACT_WAVE2_OUTPUT_DIR` shares the same `data/vignettes/v2/class_02_bacterial` directory as Wave 1 + pilots.
- The `_bact_wave1_case_id` helper was extended with `.replace(" ", "-")` to handle multi-word `journal_short_code` values (e.g., "Lancet Infect Dis"); this is forward-safe for any future Wave 3+ anchors with multi-word journal codes.
- `BACT_WAVE2_AMBIGUITY_IDS={84}` and `BACT_WAVE2_PERU_IDS={84, 86, 88}` are exported as module-level constants for downstream tests + analysis scripts.
- `write_bact_wave2_corpus()` is idempotent: it overwrites existing JSONs in place and validates each before write.

## Quality Rating Table

[See commit message and final response for empirically-backed Quality Rating Table.]
