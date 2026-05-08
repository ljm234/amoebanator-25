# Subphase 1.3 Wave 1 VIRAL Validation Report (Commit 5.3.5)

**Date:** 2026-05-08
**Scope:** 13 wave-1 VIRAL vignettes all anchored to Tyler KL 2018 NEJM clinical review of acute viral encephalitis (PMID 29490180, anchor_type=review). Pathogens: 3 HSV1 + 5 enterovirus + 2 HSV2 + 2 dengue + 1 EEE.
**Tag:** v2.3.3-subphase1.3-wave1-viral (LOCAL only per User Assignment; Jordan pushes manually)
**HEAD pre-commit:** 134b4a4 (Wave 2 BACT shipped, BACT class 30/30 complete)
**Architecture:** Helper functions extended from Wave 2 BACT industrialization at HEAD. Reused: `_bact_wave1_altitude`, `_bact_wave1_ethnicity`, `_build_literature_anchor`, `load_pmid_metadata`. New VIRAL-specific helpers: `_viral_wave1_case_id` (VIR-D3 prefix), `_viral_wave1_imaging_for` (HSV1 mesial-temporal MRI, EEE diffuse cerebral edema, EV no-imaging, HSV2/dengue normal MRI), `_viral_wave1_exposure` (dengue mosquito_endemic_area_exposure=true), `_viral_wave1_red_flags` (no Tyler-set red-flag enum matches), `_viral_wave1_adjudication` (VIRAL-WAVE1-PRE-ADJ sentinels, commit 5.3.5), `_viral_wave1_provenance` (commit 5.3.5), pathogen-specific dx_tests (HSV1 PCR, EV PCR, HSV2 PCR, dengue NS1+PCR with serotype, EEE IgM+PCR).

## Wave 1 VIRAL Slot Coverage

| ID | Pathogen | Demographics | Region | Stage | Outcome | Methodology | Ambiguity |
|---|---|---|---|---|---|---|---|
| v96 | HSV1 | 45F | other_global (NL) | mid | survived | tier_3_imputation_within_review | False |
| v99 | HSV1 | 38M | peru_lima_coast | mid | survived | tier_3_imputation_within_review | False |
| v102 | HSV1 | 50M | other_global (NL) | mid | survived | tier_3_imputation_within_review | False |
| v106 | enterovirus | 7F | us_south | early | survived | tier_3_imputation_within_review | False |
| v107 | enterovirus | 22F | other_global (NL) | mid | survived | tier_3_imputation_within_review | False |
| v108 | enterovirus | 11M | us_south | mid | survived | tier_3_imputation_within_review | False |
| v109 | enterovirus | 3F | other_global (NL) | mid | survived | tier_3_imputation_within_review | False |
| v111 | enterovirus | 5M | us_south | mid | survived | tier_3_imputation_within_review | False |
| v113 | HSV2 | 28F | other_global (NL) | mid | survived | tier_3_imputation_within_review | True |
| v114 | HSV2 | 35M | us_south | mid | survived | tier_3_imputation_within_review | False |
| v117 | dengue | 32F | peru_lima_coast | mid | survived | tier_4_imputation_peru_dengue_2024_anchored | True |
| v119 | dengue | 41M | peru_tumbes | mid | survived | tier_4_imputation_peru_dengue_2024_anchored | False |
| v120 | EEE | 58M | us_south | late | fatal | tier_3_imputation_within_review | False |

## Per-Vignette Validation Log

### v96 - vir_096_hsv1_adult.json
- Anchor: PMID 29490180 (Tyler 2018 NEJM, anchor_type=review)
- Demographic: 45yo F NL adult HSE (HSE bimodal age, adult peak).
- Schema validation: PASS
- CSF: WBC 220 (75 percent lymphocytes), glucose 55, protein 120, RBC 35 with xanthochromia (canonical hemorrhagic component).
- Imaging: mesial_temporal_t2_flair_hyperintensity (HSE canonical signature).
- Exam: focal_neurological_deficit=true (expressive aphasia), neck_stiffness=false (HSE typical).
- Outcome=survived_mild_memory_deficit. Acyclovir_hours=5.

### v99 - vir_099_hsv1_lima_adult.json
- Anchor: PMID 29490180 (Tyler 2018 NEJM)
- Demographic: 38yo M Lima Peru adult HSE.
- Schema validation: PASS
- CSF: WBC 180 (78 percent lymphocytes), glucose 58, protein 105, RBC 28 xanthochromia.
- Imaging: mesial_temporal_t2_flair_hyperintensity.
- Exam: focal_neurological_deficit=true (olfactory hallucinations + aphasia + partial seizure - classic limbic-dominant signature).
- Outcome=survived_mild_memory_deficit. Acyclovir_hours=8.

### v102 - vir_102_hsv1_adult.json
- Anchor: PMID 29490180 (Tyler 2018 NEJM)
- Demographic: 50yo M NL adult HSE with frontal-disinhibition + anomic aphasia (limbic + frontal extension).
- Schema validation: PASS
- CSF: WBC 250 (72 percent lymphocytes), glucose 52, protein 135, RBC 40 xanthochromia.
- Imaging: mesial_temporal_t2_flair_hyperintensity (bilateral asymmetric).
- Exam: focal_neurological_deficit=true. mental_status=somnolent.
- Outcome=survived_moderate_memory_deficit. Acyclovir_hours=4.

### v106 - vir_106_enterovirus_pediatric.json
- Anchor: PMID 29490180 (Tyler 2018 NEJM)
- Demographic: 7yo F US South summer pediatric EV.
- Schema validation: PASS
- CSF: WBC 95 (80 percent lymphocytes), glucose 60, protein 50 - textbook viral pattern.
- Imaging: none (uncomplicated benign aseptic meningitis).
- Exam: alert, neck_stiffness=true, no focal deficit. GCS 15.
- Outcome=survived_full_recovery in 5 days.

### v107 - vir_107_enterovirus_young_adult.json
- Anchor: PMID 29490180 (Tyler 2018 NEJM)
- Demographic: 22yo F NL young-adult summer EV.
- Schema validation: PASS
- CSF: WBC 220 (78 percent lymphocytes), glucose 55, protein 65.
- Imaging: none.
- Outcome=survived_full_recovery in 7 days.

### v108 - vir_108_enterovirus_school_outbreak.json
- Anchor: PMID 29490180 (Tyler 2018 NEJM)
- Demographic: 11yo M US South school-outbreak September pediatric EV.
- Schema validation: PASS
- CSF: WBC 180 (82 percent lymphocytes), glucose 58, protein 60.
- Outcome=survived_full_recovery in 6 days.

### v109 - vir_109_enterovirus_infant.json
- Anchor: PMID 29490180 (Tyler 2018 NEJM)
- Demographic: 3yo F NL early-childhood summer EV.
- Schema validation: PASS
- CSF: WBC 145 (85 percent lymphocytes), glucose 56, protein 55.
- Outcome=survived_full_recovery in 5 days.

### v111 - vir_111_enterovirus_pediatric.json
- Anchor: PMID 29490180 (Tyler 2018 NEJM)
- Demographic: 5yo M US South August pediatric EV.
- Schema validation: PASS
- CSF: WBC 165 (80 percent lymphocytes), glucose 55, protein 58.
- Outcome=survived_full_recovery in 6 days.

### v113 - vir_113_hsv2_mollaret_recurrent_ambiguity.json (AMBIGUITY)
- Anchor: PMID 29490180 (Tyler 2018 NEJM)
- Demographic: 28yo F NL HSV2 first-episode 2 weeks post primary genital herpes.
- Schema validation: PASS
- CSF: WBC 350 (65 percent lymphocytes, 35 percent neutrophils), glucose 48, protein 105 - prominent pleocytosis approaching bacterial-DDx threshold but lymphocyte-dominant.
- Diagnostic_ambiguity=true; type=hsv2_first_episode_with_prominent_meningismus_bacterial_ddx (verbatim from spec).
- HSV2 PCR confirms organism. MRI normal.
- Outcome=survived_full_recovery.

### v114 - vir_114_hsv2_first_episode.json
- Anchor: PMID 29490180 (Tyler 2018 NEJM)
- Demographic: 35yo M US South HSV2 first-episode 10 days post primary genital herpes.
- Schema validation: PASS
- CSF: WBC 280 (78 percent lymphocytes), glucose 55, protein 80.
- HSV2 PCR positive. MRI normal.
- Outcome=survived_full_recovery in 6 days.

### v117 - vir_117_dengue_lima_ambiguity.json (AMBIGUITY)
- Anchor: PMID 29490180 (Tyler 2018 NEJM)
- Demographic: 32yo F Lima Peru during 2024 dengue outbreak with prominent CNS-arbo-encephalitis-overlap phenotype.
- Schema validation: PASS
- CSF: WBC 110 (70 percent lymphocytes), glucose 58, protein 80.
- Platelets 75,000 (WHO 2009 dengue with warning signs threshold).
- Diagnostic_ambiguity=true; type=dengue_with_prominent_cns_arbo_encephalitis_overlap (verbatim from spec).
- NS1 + DENV-2 PCR confirm organism. mosquito_endemic_area_exposure=true.
- Outcome=survived.

### v119 - vir_119_dengue_tumbes.json
- Anchor: PMID 29490180 (Tyler 2018 NEJM)
- Demographic: 41yo M Tumbes Peru coastal community dengue with transient encephalopathy.
- Schema validation: PASS
- CSF: WBC 95 (72 percent lymphocytes), glucose 60, protein 75.
- Platelets 85,000 (WHO 2009 thrombocytopenia threshold).
- NS1 + DENV-2 PCR positive. MRI normal (metabolic / cytokine encephalopathy).
- Outcome=survived_full_recovery.

### v120 - vir_120_eee_northeast_us_fatal.json
- Anchor: PMID 29490180 (Tyler 2018 NEJM)
- Demographic: 58yo M US South older-adult mosquito-endemic-wooded-area exposure, severe EEE.
- Schema validation: PASS
- CSF: WBC 350 mixed-cellularity leaning lymphocytic (60 percent lymphocytes, 35 percent neutrophils, 5 percent eosinophils), glucose 48 (near master prompt 1.3.4 floor), protein 145.
- EEE IgM + PCR positive. MRI: diffuse_cerebral_edema_basilar_meningeal_enhancement (basal ganglia + thalamic involvement per Tyler review).
- Vitals: GCS 6, comatose. Focal neurological deficit (left-sided weakness).
- Outcome=fatal_hospital_day_4 per Tyler review case fatality approximately 30 percent.

## Schema-to-Spec Field Mapping Decisions

| Spec field | Schema rendering | Reason |
|---|---|---|
| diagnostic_ambiguity (v113, v117) + ambiguity_type | provenance.inclusion_decision_rationale + narrative + adjudication.anchoring_documentation | extra="forbid" prevents new keys; identical to BACT 5.3.3-5.3.4 D8 pattern |
| dengue mosquito-endemic-area exposure (v117, v119) | exposure.mosquito_endemic_area_exposure=True | schema ExposureHistory enum supports directly |
| HSV1 hemorrhagic CSF (v96, v99, v102) | csf.csf_xanthochromia_present=true + csf.csf_rbc_per_mm3>=20 + narrative | schema CSFProfile supports both fields |
| HSV1 mesial-temporal MRI (v96, v99, v102) | imaging.imaging_pattern="mesial_temporal_t2_flair_hyperintensity" | schema imaging_pattern enum supports directly (master prompt 1.3.4 mandate) |
| EV no-imaging (v106, v107, v108, v109, v111) | imaging.imaging_modality="none", imaging_pattern=null | schema supports null pattern when modality=none |
| EEE diffuse-edema MRI (v120) | imaging.imaging_pattern="diffuse_cerebral_edema_basilar_meningeal_enhancement" | schema supports; closest to thalamic+basal-ganglia EEE phenotype within 14-value enum |
| pre-adjudication structured fields | adjudication.anchoring_documentation per BACT 5.3.2-5.3.4 D8 | preserves verbatim self_review_disposition=hold_for_revision |
| Tyler authors_full Vancouver list | literature_anchors[0].pmid only; Vancouver list is in PMID_REGISTRY | schema LiteratureAnchor has 3 fields (anchor_type, pmid, doi); registry holds full metadata |

## Quality Gates Summary

| Gate | Result |
|---|---|
| 13 wave-1 VIRAL vignettes constructed | 13/13 |
| Schema validation pass rate | 13/13 |
| All v2/class_03_viral vignette JSONs validate | 16/16 (3 pilot + 13 wave-1) |
| Cross-class schema validation | 46/46 (30 BACT + 16 VIRAL) |
| Em-dashes (—) corpus-wide | 0 |
| En-dashes (–) corpus-wide | 0 |
| AI-tell vocabulary corpus-wide | 0 |
| Spanish narrative coverage | 13/13 in 700-900 char band (range 710-898) |
| English narrative coverage | 13/13 in 800-1200 char band (range 838-1145) |
| Anchor PMID resolves in PMID_REGISTRY | 13/13 (all to Tyler 29490180) |
| Anchor type "review" | 13/13 |
| Pre-adjudication hold_for_revision verbatim | 13/13 |
| Diagnostic ambiguity slots = 2 | 2/2 (v113, v117) |
| Peru-anchored slots = 3 | 3/3 (v99 Lima HSV1, v117 Lima dengue, v119 Tumbes dengue) |
| Pathogen distribution | 3 HSV1 + 5 enterovirus + 2 HSV2 + 2 dengue + 1 EEE (matches Tyler-anchored slot inventory) |
| HSV1 temporal lobe authenticity (focal/CN >=50 percent) | 3/3 (exceeds target — all HSV1 cases have focal_neurological_deficit=true) |
| Dengue thrombocytopenia (platelets <150,000) | 2/2 (v117=75k, v119=85k) |
| EEE severe outcome | 1/1 (v120 outcome=fatal, GCS 6 comatose) |
| ground_truth_class=3 | 13/13 |
| freshwater_exposure_within_14d=False | 13/13 |
| csf_lymphocyte_pct >= 50 (master prompt 1.3.4) | 13/13 |
| csf_neutrophil_pct < 50 | 13/13 |
| csf_glucose_mg_per_dL >= 40 (viral pattern) | 13/13 |
| Cross-field validators pass rate | 65/65 (5 invariants × 13 vignettes) |
| Wave-1 VIRAL lock-in tests | 80/80 passing |
| All Subphase 1.3 lock-in tests (pilot + wave1bact + wave2bact + wave1viral) | 219/219 |
| Full test suite parity post-commit | 2076 passed, 1 skipped, 1 xfailed (no regressions; was 1996 + 80 viral parametrized = 2076) |
| 5.3.0.3, 5.3.1, 5.3.2, 5.3.3, 5.3.4 lock-in tests | unchanged, all preserved |
| PMID_REGISTRY entries | 57 (no change; Tyler 29490180 pre-registered from 5.3.0.3) |

## Lock-in Test Architecture

`tests/test_subphase_1_3_wave1_viral_lockin.py` provides 18 named tests across 80 parametrized cases:
1. `test_viral_wave1_files_exist` (parametrized over 13 IDs)
2. `test_viral_wave1_schema_validates` (parametrized over 13 IDs)
3. `test_viral_wave1_demographics_match_spec` (parametrized over 13 IDs)
4. `test_viral_wave1_anchor_pmid_tyler` (parametrized over 13 IDs)
5. `test_viral_wave1_anchor_type_review` (parametrized over 13 IDs)
6. `test_viral_wave1_count_13` (cross-references VIRAL_DISTRIBUTION empirical extraction with hardcoded list)
7. `test_viral_wave1_freshwater_false`
8. `test_viral_wave1_class_id_3`
9. `test_viral_wave1_csf_lymphocytic` (>=50 percent)
10. `test_viral_wave1_csf_neutrophil_low` (<50 percent)
11. `test_viral_wave1_csf_glucose_normal_or_near` (>=40)
12. `test_viral_wave1_pre_adjudication_hold` (verbatim)
13. `test_viral_wave1_no_em_dashes`
14. `test_viral_wave1_no_ai_tells`
15. `test_viral_wave1_hsv1_temporal_lobe_focal` (HSV1 focal/CN signs >=50 percent of HSV1 cases)
16. `test_viral_wave1_dengue_thrombocytopenia` (dengue platelets <150,000)
17. `test_viral_wave1_eee_severe_outcome` (EEE outcome in {fatal, severe_sequelae})
18. `test_viral_wave1_pathogen_distribution` (3+5+2+2+1 set equality)
19. `test_viral_wave1_ambiguity_count` (set equality with {113, 117})
20. `test_viral_wave1_peru_anchors` (set equality with {99, 117, 119})

(20 named tests total; the user prompt mentioned 13+, this implementation includes additional pathogen-distribution + ambiguity + Peru tests for corpus-level rigor.)

TDD discipline: all tests confirmed RED (77 parametrized failures + 3 pre-passes on tests reading VIRAL_DISTRIBUTION specs not JSON files: `test_viral_wave1_count_13`, `test_viral_wave1_pathogen_distribution`, `test_viral_wave1_eee_severe_outcome`) before any helper function landed. After helper construction + JSON write, all 80 confirmed GREEN.

## Honest Disclosure

- All 13 wave-1 VIRAL vignettes carry pre-adjudication `hold_for_revision`. External clinical adjudication has NOT been performed.
- Tyler 29490180 verification_confidence in PMID_REGISTRY is 0.85 (pre-direct-fetch); the citation is locked from 5.3.0.3 and treated as established for anchor purposes. Vignettes draw on Tyler's clinical-review framework for pathogen-by-pathogen presentation patterns; specific epidemiologic numbers cited (HSE residual-deficit rate, EEE 30 percent case fatality, EEE 50 percent permanent sequelae in survivors) are within Tyler review ranges rather than verbatim numbers from the abstract.
- The Tyler review covers HSV1, HSV2, enterovirus, and arboviral encephalitis. Dengue with neurologic involvement (v117, v119) is contextually consistent with Tyler's discussion of arboviral encephalitis; the methodology field on these slots (`tier_4_imputation_peru_dengue_2024_anchored`) discloses that the Peru-2024-outbreak context layers on Tyler review primary anchor.
- v120 EEE imaging maps to `diffuse_cerebral_edema_basilar_meningeal_enhancement` from the schema's 14-value imaging_pattern enum. Tyler describes EEE predilection for basal ganglia and thalamus; the schema does not have a thalamic-basal-ganglia-specific enum value, so this is the closest schema-respecting mapping with the narrative documenting the thalamic + basal-ganglia involvement.
- Master prompt 1.3.4 mandates lymphocytic CSF (50-500 WBC range, normal-low glucose, mildly elevated protein) for Class 3. The 5.3.2 EV pilot v105 deliberately violates this with 65 percent neutrophil predominance per Michos 2007 cohort evidence; that is a Michos-anchored exception pre-existing this commit. All 13 Tyler-anchored vignettes in 5.3.5 honor the master prompt mandate (lymphocyte_pct >= 50, neutrophil_pct < 50, glucose >= 40).
- The 2 ambiguity vignettes (v113, v117) carry the slot spec's `ambiguity_type` verbatim:
  - v113: `hsv2_first_episode_with_prominent_meningismus_bacterial_ddx`
  - v117: `dengue_with_prominent_cns_arbo_encephalitis_overlap`
- HSV1 cases (v96, v99, v102) all have `focal_neurological_deficit=true` and `neck_stiffness=false`. This reflects HSE's predilection for limbic/frontal involvement and the pilot v92 pattern; HSE is one of the few CNS infections where neck stiffness is OFTEN absent on initial presentation despite parenchymal disease. The test `test_viral_wave1_hsv1_temporal_lobe_focal` requires >=50 percent of HSV1 cases to demonstrate focal/CN signs; all 3 do.
- Anchoring documentation follows: `stage=pre_adjudication; status=pending_external_review; self_review_disposition=hold_for_revision; self_review_notes=...; adjudicator_ids=VIRAL-WAVE1-PRE-ADJ-1, VIRAL-WAVE1-PRE-ADJ-2 (sentinel); cohen_kappa=0.0 placeholder; ... Subphase 1.3 commit 5.3.5 (2026-05-08).` Sentinel adjudicator IDs distinguish VIRAL Wave 1 from BACT Wave 1 (`WAVE1-PRE-ADJ-1/2`), BACT Wave 2 (`WAVE2-PRE-ADJ-1/2`), and pilot (`PILOT-PRE-ADJ-1/2`) adjudicators.
- The `_bact_wave1_case_id` helper (extended in Wave 2 with `.replace(" ", "-")` for multi-word journal codes) is shared by VIRAL via `_viral_wave1_case_id` only nominally; the VIRAL function rebuilds the case_id with VIR-D3 prefix and pathogen descriptor mapping, so this is a parallel-not-shared helper.

## Methodology Distribution After Commit 5.3.5

### Bacterial running totals (unchanged from 5.3.4)

| Tier | BACT running total |
|---|---|
| primary_source_direct (pilot) | 3/30 |
| tier_3_imputation_within_cohort_review (van de Beek) | 4/30 |
| tier_3_imputation_within_cohort_review (Bijlsma) | 6/30 |
| tier_3_imputation_within_cohort_review (Mylonakis) | 2/30 |
| tier_4_imputation_idsa_guideline_anchored (Tunkel) | 10/30 |
| tier_4_imputation_cdc_abcs_anchored (Soeters) | 5/30 |
| **TOTAL BACT** | **30/30 COMPLETE** |

### Viral running totals (post 5.3.5)

| Tier | VIRAL running total |
|---|---|
| primary_source_direct (pilot v92, v105, v118) | 3/30 |
| tier_3_imputation_within_review (Tyler) | 11/30 (v96, v99, v102, v106, v107, v108, v109, v111, v113, v114, v120) |
| tier_4_imputation_peru_dengue_2024_anchored (Tyler + Peru-dengue overlay) | 2/30 (v117, v119) |
| **TOTAL VIRAL** | **16/30 (53 percent)** |

## Subphase 1.3 Progress

| Class | Pre-5.3.5 | Post-5.3.5 |
|---|---|---|
| Bacterial (Class 2) | 30/30 COMPLETE | 30/30 COMPLETE (unchanged) |
| Viral (Class 3) | 3/30 | 16/30 |
| **Subphase 1.3 total** | **33/60 (55 percent)** | **46/60 (77 percent)** |

Tyler-anchored cohort (the largest single-anchor set in VIRAL_DISTRIBUTION) is now complete. Remaining VIRAL workstream: 14 slots covering remaining HSV1 (9 slots), HSV_PCR_negative_72h (2 slots), VZV (2 slots), and 1 dengue slot — anchored to non-Tyler PMIDs per VIRAL_DISTRIBUTION.

## Forward-Compatibility Notes

- The `_VIRAL_WAVE1_BUILDERS` dispatch table parallels the `_BACT_WAVE1_BUILDERS` and `_BACT_WAVE2_BUILDERS` patterns. Future viral waves can extend the same module-level pattern.
- `VIRAL_WAVE1_OUTPUT_DIR` shares the `data/vignettes/v2/class_03_viral` directory with the 3 pilots.
- `VIRAL_WAVE1_AMBIGUITY_IDS={113, 117}` and `VIRAL_WAVE1_PERU_IDS={99, 117, 119}` are exported as module-level constants for downstream tests + analysis scripts.
- `write_viral_wave1_corpus()` is idempotent: it overwrites existing JSONs in place and validates each before write.
- The pathogen-specific dx_test helpers (`_viral_wave1_dx_tests_hsv1_pcr`, `_viral_wave1_dx_tests_ev_pcr`, `_viral_wave1_dx_tests_hsv2_pcr`, `_viral_wave1_dx_tests_dengue`, `_viral_wave1_dx_tests_eee`) are parameterized by PMID and are reusable for future viral waves anchored to non-Tyler PMIDs (e.g., HSV-PCR-negative-72h slots, VZV slots).

## Quality Rating Table

[See commit message and final response for empirically-backed Quality Rating Table.]
