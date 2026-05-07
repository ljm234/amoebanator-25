# Subphase 1.3 Pilot Validation Report (Commit 5.3.2)

**Date:** 2026-05-07
**Scope:** 6 pilot vignettes (3 Bacterial + 3 Viral), all primary-source-direct, integrated into locked distribution slots per Section 5 protocol of the v3 prompt.
**Tag:** v2.3.0.1-subphase1.3-pilot-validated
**HEAD pre-commit:** cf42ad4 (Commit 5.3.1 ship)

## Per-Vignette Validation Log

### BACT pilot 1 (v64) - bact_064_sp_lima_pediatric.json
- Anchor PMID: 27831604 (Davalos 2016 RPMESP, multicenter Lima pediatric SP cohort 2006-2011)
- Slot: v64. Previously anchored to PMID 15494903 (Tunkel IDSA guideline, generic) with 4yo F demographic.
- Tier: primary_source_direct (Peru-cohort-anchored)
- Schema validation: PASS
- Cross-field validators: PASS (5/5: freshwater_exposure_within_14d=False, class_id=2, csf differential sums to 100, symptom_onset>0, all required schema fields present)
- Imputation tier breakdown: tier_1_primary={age, sex, geography_region, csf_culture, csf_gram_stain}; tier_3_within_cohort={csf_wbc, csf_neutrophil_pct, csf_glucose, csf_protein}; tier_4_priors={glasgow_coma_scale, temperature_celsius}
- Pre-adjudication disposition: hold_for_revision (verbatim per Q7 5.3.1 lock; embedded into AdjudicationMetadata.anchoring_documentation per D8)
- Notes: imaging_pattern enum lacks meningeal_enhancement_no_focal_lesion; mapped to normal with explicit narrative note in imaging_text_summary.

### BACT pilot 2 (v62) - bact_062_sp_netherlands_adult.json
- Anchor PMID: 15509818 (van de Beek 2004 NEJM, 696-episode prospective Netherlands cohort)
- Slot: v62. Previously anchored to same PMID 15509818 with 47yo F demographic.
- Tier: primary_source_direct
- Schema validation: PASS
- Cross-field validators: PASS (5/5)
- Imputation tier breakdown: tier_1_primary={age, sex, csf_culture, csf_gram_stain, classic_triad}; tier_3_within_cohort={csf_wbc, csf_neutrophil_pct, csf_glucose, csf_protein, glasgow_coma_scale}; tier_4_priors={temperature_celsius, symptom_onset_to_presentation_days}
- Pre-adjudication disposition: hold_for_revision
- Notes: PMID match retained; only age 47→55 strengthening to better match cohort age range. Classic triad documented as 44 percent cohort marker satisfaction.

### BACT pilot 3 (v82) - bact_082_nm_college_outbreak.json
- Anchor PMID: 18626301 (Heckenberg 2008 Medicine 87:185-192, 258-adult NM Netherlands cohort)
- Slot: v82. Previously anchored to PMID 18626302 (typo) with 19yo F demographic.
- Tier: primary_source_direct
- Schema validation: PASS
- Cross-field validators: PASS (5/5)
- Imputation tier breakdown: tier_1_primary={age, sex, csf_culture, csf_gram_stain, petechial_rash, classic_triad}; tier_3_within_cohort={csf_wbc, csf_neutrophil_pct, csf_glucose, csf_protein}; tier_4_priors={temperature_celsius, glasgow_coma_scale, symptom_onset_days}
- Pre-adjudication disposition: hold_for_revision
- Notes: errata fix PMID 18626302→18626301 documented in narrative + provenance + slot spec `errata_note` field. CSF WBC 2,100 sits within Heckenberg cohort IQR 1,820-12,225.

### VIRAL pilot 1 (v92) - vir_092_hsv1_adult.json
- Anchor PMID: 16675036 (Whitley 2006 Antiviral Res 71(2-3):141-148, HSE adolescents and adults review)
- Slot: v92. Previously anchored to PMID 29490180 (Tyler 2018 NEJM, generic) with 56yo M demographic.
- Tier: primary_source_direct
- Schema validation: PASS
- Cross-field validators: PASS (5/5 including HSV-1 imaging_pattern mandate)
- Imputation tier breakdown: tier_1_primary={age, sex, csf_hsv1_pcr, imaging_pattern (master prompt mandate)}; tier_3_within_cohort={csf_wbc, csf_neutrophil_pct, csf_glucose, csf_protein, csf_rbc, csf_xanthochromia, imaging_laterality}; tier_4_priors={temperature_celsius, glasgow_coma_scale, symptom_onset_days}
- Pre-adjudication disposition: hold_for_revision
- Notes: imaging_pattern set to mesial_temporal_t2_flair_hyperintensity per master prompt 1.3 HSV mandate (verified). Imaging laterality (left greater than right asymmetric) documented in imaging_text_summary since schema lacks dedicated field.

### VIRAL pilot 2 (v105) - vir_105_enterovirus_pediatric.json
- Anchor PMID: 17668054 (Michos 2007 PLoS One 2(7):e674, 506-child aseptic meningitis Athens cohort)
- Slot: v105. Previously anchored to PMID 29490180 (Tyler 2018 generic) with 4yo M US South demographic.
- Tier: primary_source_direct
- Schema validation: PASS
- Cross-field validators: PASS (5/5)
- Imputation tier breakdown: tier_1_primary={age, sex, csf_enterovirus_pcr, csf_neutrophil_pct (deliberately PMN per Michos 58.3 percent finding), season}; tier_3_within_cohort={csf_wbc, csf_glucose, csf_protein}; tier_4_priors={temperature_celsius, symptom_onset_days, glasgow_coma_scale}
- Pre-adjudication disposition: hold_for_revision
- Notes: Diagnostic_ambiguity_flag deliberately set True. Type=csf_neutrophil_predominant_in_confirmed_viral. Reflects Michos 2007 cohort evidence that 58.3 percent of EV PCR-positive cases have PMN predominance (CSF WBC 220 per uL, 65 percent neutrophils per cohort median).

### VIRAL pilot 3 (v118) - vir_118_dengue_loreto.json
- Anchor PMID: 38300858 (Munayco MMWR 2024 73(4):86-88, Peru 2023 dengue outbreak surveillance)
- Slot: v118. Previously anchored to PMID 29490180 (Tyler 2018 generic) with 28yo F Loreto demographic.
- Tier: primary_source_direct (Peru-cohort-anchored)
- Schema validation: PASS
- Cross-field validators: PASS (5/5 including dengue platelets-below-150k mandate)
- Imputation tier breakdown: tier_1_primary={age, sex, geography_region, denv_pcr_serotype, denv_ns1_antigen, platelets_per_uL, outbreak_context}; tier_3_within_cohort={csf_wbc, csf_glucose, csf_protein}; tier_4_priors={temperature_celsius, glasgow_coma_scale, symptom_onset_days}
- Pre-adjudication disposition: hold_for_revision
- Notes: platelets_per_uL=65,000 satisfies master prompt 1.3 dengue mandate of below 150,000 and reflects WHO 2009 dengue-with-warning-signs threshold. Encephalopathic clinical form documented; MRI normal (dengue encephalopathy is metabolic/cytokine-mediated in this presentation, not direct viral invasion).

## 5.3.1 Distribution Strengthening (Section 10 protocol)

| Slot | Before (PMID, demographics, methodology) | After (PMID, demographics, methodology) | Rationale |
|---|---|---|---|
| v64 | PMID 15494903 (Tunkel IDSA generic guideline), age 4 F, tier_4_imputation_idsa_guideline_anchored | PMID 27831604 (Davalos 2016 RPMESP real Lima cohort), age 1 (18 months) M, primary_source_direct | Real Peru-cohort primary source replaces generic IDSA guideline anchor |
| v62 | PMID 15509818 (van de Beek 2004 NEJM), age 47 F, tier_3_imputation_within_cohort_review | PMID 15509818 (same), age 55 F, primary_source_direct | PMID match retained; age strengthening within cohort range; tier upgraded since pilot is direct primary anchor |
| v82 | PMID 18626302 (typo), age 19 F, tier_3_imputation_within_cohort_review | PMID 18626301 (Heckenberg 2008 Medicine canonical), age 24 M, primary_source_direct | Typo errata fix + demographic shift to canonical NM cohort age/sex |
| v92 | PMID 29490180 (Tyler 2018 NEJM generic review), age 56 M us_south, tier_3_imputation_within_review | PMID 16675036 (Whitley 2006 Antiviral Res HSE-specific), age 42 M other_global, primary_source_direct | HSE-specific Whitley anchor replaces generic Tyler review |
| v105 | PMID 29490180 (Tyler 2018 generic), age 4 M us_south, tier_3, ambiguity False | PMID 17668054 (Michos 2007 PLoS One PMN-cohort), age 5 M other_global, primary_source_direct, ambiguity True (csf_neutrophil_predominant_in_confirmed_viral) | Michos cohort is the canonical PMN-predominant EV anchor; ambiguity quota slot moves from v107 to v105 |
| v107 | PMID 29490180, age 22 F other_global, tier_3, ambiguity True (enterovirus_with_initial_neutrophilic_csf_bacterial_mimic) | PMID 29490180 unchanged; ambiguity False; ambiguity_swap_note appended | Ambiguity slot moved to v105 per Michos primary anchor; v107 reverts to standard EV imputation. Total viral ambiguity count preserved at 5. |
| v118 | PMID 29490180 (Tyler 2018 generic), age 28 F peru_loreto_amazon, tier_4_imputation_peru_dengue_2024_anchored | PMID 38300858 (Munayco MMWR 2024 Peru outbreak), age 32 F peru_loreto_amazon, primary_source_direct | Real Peru 2023 outbreak surveillance replaces generic Tyler review |

## Errata Fixes

- **PMID 18626302 → 18626301:** PMID 18626302 in 5.3.1 PMID_REGISTRY was a typo for the Heckenberg 2008 Medicine 87(4):185-192 paper (`Clinical features, outcome, and meningococcal genotype in 258 adults with meningococcal meningitis: a prospective cohort study`). The correct PubMed ID is **18626301** (verified PubMed UI 2026-05-07 via Claude web research v4). The 18626302 entry was REMOVED from PMID_REGISTRY in this commit; new 18626301 entry added with full metadata; v82 BACTERIAL_DISTRIBUTION slot updated to reference 18626301; an `errata_note` field was added to the v82 spec.

## Schema Translation Notes

| v3 prompt field | Schema location | Translation rationale |
|---|---|---|
| symptom_duration_hours | history.symptom_onset_to_presentation_days | divide hours by 24 |
| altered_mental_status (bool) | exam.mental_status_grade (Literal enum) | true→confused/somnolent based on GCS clinical context; false→alert |
| gcs_score | vitals.glasgow_coma_scale | direct rename |
| petechial_rash | exam.petechial_or_purpuric_rash | direct rename |
| classic_triad_present (bool) | exam (no direct field) → narrative + provenance rationale | description of triad presence in prodrome and rationale text |
| imaging_modality: ct_head_non_contrast | imaging_modality enum: ct_noncontrast | rename |
| imaging_modality: mri_brain_with_contrast | imaging_modality enum: mri_with_dwi_flair | preferred for HSV |
| imaging_modality: mri_brain_non_contrast | imaging_modality enum: mri_with_dwi_flair (or mri_noncontrast) | uses dwi_flair for richer pattern detection |
| imaging_pattern: meningeal_enhancement_no_focal_lesion | imaging_pattern enum: normal (closest available) | closest match; meningeal enhancement narrative-noted in imaging_text_summary |
| imaging_laterality | (no schema field) → imaging_text_summary | free-text |
| outcome | provenance.inclusion_decision_rationale + narrative_en/es | structured-text per D8 |
| antibiotic_started_hours_from_presentation | provenance.inclusion_decision_rationale + narrative + history.prodrome_description | structured-text |
| dexamethasone_co_administered | provenance.inclusion_decision_rationale + narrative + history.prodrome_description | structured-text |
| acyclovir_started_hours_from_presentation | provenance.inclusion_decision_rationale + narrative + history.prodrome_description | structured-text |
| diagnostic_ambiguity_flag, diagnostic_ambiguity_type | provenance.inclusion_decision_rationale + narrative + slot spec | structured-text per D8 |
| (v3 prompt) provenance.adjudication nested object | top-level adjudication: AdjudicationMetadata sub-model | per D8 schema rigidity |
| (v3 prompt) provenance.imputation_tier_per_field | provenance.inclusion_decision_rationale (structured text per D8) | extra="forbid" prevents new keys |
| (v3 prompt) provenance.indeterminate_fields | provenance.inclusion_decision_rationale (structured text per D8) | same |

The schema's `AdjudicationMetadata` has only 5 rigid fields (`adjudicator_ids`, `cohen_kappa`, `disagreement_resolution`, `anchoring_documentation`, `inclusion_decision`). The v3 prompt's `stage`, `status`, `self_review_disposition`, `self_review_notes`, `adjudicator_name`, `adjudication_date`, `post_adjudication_disposition` fields do not exist in the schema. Per D8: the structured pre-adjudication disclosure was embedded into `anchoring_documentation` (max 2000 chars) with the exact verbatim phrase `self_review_disposition=hold_for_revision` per Q7 5.3.1 lock; `inclusion_decision="hold_for_revision"` set on every pilot.

## 5.3.1 Lock-in Test Updates

No 5.3.1 lock-in tests required updating. All existing tests continue to pass post-strengthening because:
- `test_bacterial_pathogen_counts`: pathogen counts (21/4/2/2/1) unchanged.
- `test_viral_pathogen_counts`: pathogen counts (12/8/2/2/3/1/2) unchanged.
- `test_bacterial_peru_anchor_share`: Peru count = 5 unchanged (v64 stays Peru, v82 stays other_global).
- `test_viral_dengue_peru_anchor`: 3 dengue Peru unchanged.
- `test_subphase_1_3_freshwater_false`: all 60 specs still freshwater=False.
- `test_diagnostic_ambiguity_count`: bacterial 5, viral 5 (preserved via v105/v107 swap).
- `test_subphase_1_3_vignette_ids_contiguous`: 61-90 + 91-120 unchanged.
- `test_marginals_files_exist_and_valid`: marginals.json regenerated; pathogen_distribution still matches master prompt targets.
- `test_marginals_freshwater_sanity_and_adjudication_state`: freshwater=False and pre_adjudication_hold_for_revision still in marginals.json.
- `test_pmid_metadata_completeness`: parametrized over PMID_REGISTRY keys; +5 new entries × 1 test each = +5 cases passing; -1 case removed for 18626302.

## Honest Disclosure

- All 6 vignettes carry pre-adjudication `hold_for_revision` status. External clinical adjudication has NOT been performed.
- Schema's `imaging_pattern` enum lacks `meningeal_enhancement_no_focal_lesion` value; bact pilot 1 mapped to `normal` with explicit narrative note.
- VIRAL pilot 2 deliberately violates the textbook viral-CSF-lymphocytic assumption per Michos 2007 cohort evidence (PMN predominance >50 percent in 58.3 percent of EV PCR-positive cases). Documented as intentional ambiguity contribution.
- VIRAL pilot 3 dengue serotype split (DENV-1 49 percent / DENV-2 49 percent / DENV-3 2 percent) cited in earlier prompt drafts is NOT explicitly present in the Munayco MMWR 2024 Notes-from-the-Field abstract. Vignette uses DENV-2 (independently verified as established circulating serotype in Peru since 2019). Full-text MMWR verification deferred to USER ASSIGNMENT 5.
- The schema's `AdjudicationMetadata` has only 5 rigid fields; the v3 prompt's nested `provenance.adjudication` structure with extra fields (`stage`, `status`, `self_review_disposition`, etc.) was rendered as structured text inside the schema's `adjudication.anchoring_documentation` field, preserving the `hold_for_revision` verbatim per Q7 5.3.1 lock semantically without adding fields to the locked schema.
- The schema's `Provenance` has only 5 rigid fields; the v3 prompt's requested `provenance.imputation_tier_per_field`, `provenance.indeterminate_fields` are rendered as structured text inside `provenance.inclusion_decision_rationale` per D8.
- Bacterial sex_distribution shifted by 2 F→M flips (v64 + v82) from 16F/14M to 14F/16M. No master prompt sex split mandate; marginals.json regenerated to reflect.

## Aggregate Metrics

| Metric | Value |
|---|---|
| Vignettes constructed | 6 |
| Schema validation pass rate | 6/6 |
| Cross-field validator pass rate | 30/30 (5 invariants × 6 vignettes) |
| Primary-source-direct count | 6/6 |
| Peru-anchored count | 2 (BACT pilot 1 v64 Lima + VIRAL pilot 3 v118 Loreto) |
| Diagnostic-ambiguity flagged count | 1 (VIRAL pilot 2 v105) |
| Pre-adjudication hold_for_revision | 6/6 |
| New PMIDs added to registry | 5 (27831604, 18626301, 16675036, 17668054, 38300858) |
| PMIDs removed from registry | 1 (18626302 typo) |
| Errata fixes documented | 1 (18626302 → 18626301) |
| PMID_REGISTRY total post-commit | 57 (was 53; +5 -1) |
| 5.3.1 lock-in tests modified | 0 (all preserved by design) |

## Methodology Distribution After Commit 5.3.2

| Tier | Bacterial running total | Viral running total |
|---|---|---|
| primary_source_direct | 3/30 (v62, v64, v82) | 3/30 (v92, v105, v118) |
| primary_source_direct (Peru-anchored) | 1/30 (v64) | 1/30 (v118) |
| tier_3_imputation_within_cohort_review | shifted | shifted |
| tier_4_imputation | shifted | shifted |

## Quality Rating Table

[See Section 16 in commit message and final response for full Quality Rating Table.]
