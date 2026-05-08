# Subphase 1.3 Wave 1 BACTERIAL Validation Report (Commit 5.3.3)

**Date:** 2026-05-08
**Scope:** 14 wave-1 BACTERIAL vignettes (10 Tunkel-IDSA-anchored + 4 van de Beek-NEJM-anchored), all built into locked distribution slots per the Section 5.3.3 execution prompt.
**Tag:** v2.3.1-subphase1.3-wave1-bacterial (LOCAL only per User Assignment; Jordan pushes manually)
**HEAD pre-commit:** 0a0ec85 (Subphase 1.3.x errata locked)
**Architecture:** Helper functions (Decision #2 locked) - 14 per-slot `_build_bact_vignette_NNN` builders + shared `generate_bact_wave1_vignette` orchestrator + `write_bact_wave1_corpus` writer, all in `scripts/generate_pam_vignettes.py`.

## Wave 1 Slot Coverage

| ID | Pathogen | Demographics | Region | Stage | Outcome | Anchor | Methodology | Ambiguity |
|---|---|---|---|---|---|---|---|---|
| v65 | S_pneumoniae | 28M | us_south | mid | survived | Tunkel IDSA 2004 | tier_4_idsa | False |
| v66 | S_pneumoniae | 68M | other_global | late | fatal | van de Beek NEJM 2004 | tier_3_cohort | False |
| v67 | S_pneumoniae | 3M | us_south | mid | survived | Tunkel IDSA 2004 | tier_4_idsa | False |
| v69 | S_pneumoniae | 19M | us_south | mid | survived | Tunkel IDSA 2004 | tier_4_idsa | False |
| v71 | S_pneumoniae | 38F | peru_lima_coast | mid | survived | Tunkel IDSA 2004 | tier_4_idsa | False |
| v73 | S_pneumoniae | 70F | other_global | late | fatal | van de Beek NEJM 2004 | tier_3_cohort | False |
| v75 | S_pneumoniae | 25F | us_south | mid | survived | Tunkel IDSA 2004 | tier_4_idsa | True |
| v76 | S_pneumoniae | 60M | other_global | mid | survived | Tunkel IDSA 2004 | tier_4_idsa | True |
| v77 | S_pneumoniae | 18F | other_global | mid | survived | van de Beek NEJM 2004 | tier_3_cohort | False |
| v78 | S_pneumoniae | 50M | us_south | mid | survived | Tunkel IDSA 2004 | tier_4_idsa | False |
| v79 | S_pneumoniae | 45F | us_south | mid | survived | Tunkel IDSA 2004 | tier_4_idsa | True |
| v80 | S_pneumoniae | 33M | other_global | mid | survived | Tunkel IDSA 2004 | tier_4_idsa | True |
| v81 | S_pneumoniae | 79F | other_global | late | fatal | van de Beek NEJM 2004 | tier_3_cohort | False |
| v90 | gram_negative | 55M | us_south | late | fatal | Tunkel IDSA 2004 | tier_4_idsa | False |

## Per-Vignette Validation Log

### v65 - bact_065_sp_asplenia.json
- Anchor: PMID 15494903 (Tunkel IDSA 2004 CID, anchor_type=guideline)
- Demographic: 28yo M asplenic, US South region, encapsulated-organism risk stratum.
- Schema validation: PASS
- Pre-adjudication disposition: hold_for_revision (verbatim in anchoring_documentation)
- CSF profile: WBC 6,800/mm3 (92 percent neutrophils), glucose 18, protein 250 - bacterial range per Tunkel guideline cutoffs.
- Imputation tiers: tier_1_primary={age, sex, csf_culture, csf_gram_stain, asplenia risk factor}; tier_3_within_cohort={csf_wbc, neutrophil_pct, glucose, protein}; tier_4_priors={temp, gcs, symptom_days}.
- Diagnostic_ambiguity=false. Outcome=survived_no_sequelae. Antibiotic_started_hours=1.
- Note: schema `immunocompromise_status` enum lacks an "asplenia" value; mapped to "none" with asplenia documented in narrative + rationale + slot risk_factors.

### v66 - bact_066_sp_alcoholic_fatal.json
- Anchor: PMID 15509818 (van de Beek 2004 NEJM, anchor_type=cohort, 696-episode prospective Netherlands cohort 1998-2002)
- Demographic: 68yo M with 30-year alcohol history, Netherlands, late fatal.
- Schema validation: PASS
- CSF profile: WBC 5,400 (88 percent neutrophils), glucose 22, protein 220.
- Imputation tiers: tier_1_primary={age, sex, csf_culture, csf_gram_stain, alcohol risk}; tier_3_within_cohort={csf_wbc, neutrophil_pct, glucose, protein, gcs}; tier_4_priors={temp, symptom_days}.
- Diagnostic_ambiguity=false. Outcome=fatal_hospital_day_4. Antibiotic_started_hours=3.

### v67 - bact_067_sp_pediatric.json
- Anchor: PMID 15494903 (Tunkel IDSA pediatric SP recommendations)
- Demographic: 3yo M, US South region, post-otitis-media stratum.
- Schema validation: PASS
- CSF profile: WBC 7,200 (90 percent neutrophils), glucose 20, protein 240.
- Imputation tiers: tier_1_primary={age, sex, csf_culture, csf_gram_stain}; tier_3_within_cohort={csf_wbc, neutrophil_pct, glucose, protein}; tier_4_priors={temp, gcs, symptom_days, hr}.
- Indeterminate=papilledema_on_fundoscopy (null per pediatric exam limits).
- Outcome=survived_with_mild_hearing_loss.

### v69 - bact_069_sp_recurrent_csf_leak.json
- Anchor: PMID 15494903 (Tunkel IDSA recurrent SP recommendations)
- Demographic: 19yo M with skull-base fracture and uncorrected CSF rhinorrhea, US South.
- Schema validation: PASS
- CSF profile: WBC 4,200 (85 percent neutrophils), glucose 25, protein 180.
- Imputation tiers: tier_1_primary={age, sex, csf_culture, csf_gram_stain, anatomic_leak history}; tier_3_within_cohort={csf_wbc, neutrophil_pct, glucose, protein}; tier_4_priors={temp, gcs, symptom_days}.
- Outcome=survived.

### v71 - bact_071_sp_lima_adult.json
- Anchor: PMID 15494903 (Tunkel IDSA empiric ceftriaxone-vancomycin for adult community SP)
- Demographic: 38yo F, Lima Peru tertiary urban ED.
- Schema validation: PASS
- CSF profile: WBC 5,800 (88 percent neutrophils), glucose 22, protein 200.
- Peru-anchored geography (5/30 BACT slots assigned to Peru per 5.3.1 distribution lock; v71 fills 1 of 5).
- Imputation tiers: tier_1_primary={age, sex, region, csf_culture, csf_gram_stain}; tier_3_within_cohort={csf_wbc, neutrophil_pct, glucose, protein}; tier_4_priors={temp, gcs, symptom_days}.
- Outcome=survived_no_sequelae.

### v73 - bact_073_sp_elderly_fatal.json
- Anchor: PMID 15509818 (van de Beek elderly stratum mortality 41 percent at age >=65)
- Demographic: 70yo F, Netherlands, late fatal.
- Schema validation: PASS
- CSF profile: WBC 4,100 (80 percent neutrophils), glucose 25, protein 195.
- Outcome=fatal_hospital_day_3. Antibiotic_started_hours=2.

### v75 - bact_075_sp_partial_treatment_ambiguity.json (AMBIGUITY)
- Anchor: PMID 15494903 (Tunkel IDSA pretreated-suspected meningitis recommendations)
- Demographic: 25yo F, US South, outpatient amoxicillin 24h pretreatment.
- Schema validation: PASS
- CSF profile attenuated: WBC 1,850 (65 percent neutrophils), glucose 30, protein 165 - consistent with partial treatment per IDSA narrative.
- Diagnostic_ambiguity=true; type=partial_antibiotic_pretreatment_sterile_cultures (verbatim per slot spec).
- Cultures sterile after partial Abx; CSF pneumococcal antigen positive confirms organism.
- Imputation tiers: tier_1_primary={age, sex, csf_pneumococcal_antigen, pretreatment_history}; tier_3_within_cohort={csf_wbc, neutrophil_pct, glucose, protein attenuation}; tier_4_priors={temp, gcs, symptom_days}.
- Indeterminate=culture-based-organism-confirmation (sterile per pretreatment).

### v76 - bact_076_sp_partial_treatment_ambiguity.json (AMBIGUITY)
- Anchor: PMID 15494903 (Tunkel IDSA pretreated-suspected)
- Demographic: 60yo M, Netherlands, outpatient amoxicillin 48h pretreatment.
- Schema validation: PASS
- CSF profile attenuated: WBC 2,400 (70 percent neutrophils), glucose 26, protein 180.
- Diagnostic_ambiguity=true; type=partial_antibiotic_pretreatment_sterile_cultures.

### v77 - bact_077_sp_young_adult.json
- Anchor: PMID 15509818 (van de Beek young-adult subgroup, classic triad 44 percent)
- Demographic: 18yo F, Netherlands, sudden onset 12h.
- Schema validation: PASS
- CSF profile: WBC 6,400 (88 percent neutrophils), glucose 24, protein 210.
- Triad present (case sits in young-adult subgroup of van de Beek 2004 cohort).

### v78 - bact_078_sp_hiv_immunocompromised.json
- Anchor: PMID 15494903 (Tunkel IDSA HIV-specific empiric coverage)
- Demographic: 50yo M HIV+ on ART (CD4 285), US South.
- Schema validation: PASS
- CSF profile: WBC 5,200 (85 percent neutrophils), glucose 22, protein 195.
- CrAg negative (excludes co-incident cryptococcal infection).
- Schema fields: `hiv_status="positive_on_art"`, `cd4_count_cells_per_uL=285`, `immunocompromise_status="hiv_cd4_over200"`, `red_flags_present=["immunocompromise"]`.

### v79 - bact_079_sp_partial_treatment_ambiguity.json (AMBIGUITY)
- Anchor: PMID 15494903 (Tunkel IDSA pretreated-suspected)
- Demographic: 45yo F, US South, outpatient cefuroxime 36h pretreatment.
- Schema validation: PASS
- CSF profile attenuated: WBC 1,600 (60 percent neutrophils), glucose 32, protein 155 - most attenuated of the 4 ambiguity cases.
- Diagnostic_ambiguity=true; type=partial_antibiotic_pretreatment_sterile_cultures.

### v80 - bact_080_sp_partial_treatment_ambiguity.json (AMBIGUITY)
- Anchor: PMID 15494903 (Tunkel IDSA pretreated-suspected)
- Demographic: 33yo M, Netherlands, outpatient amoxicillin 30h pretreatment.
- Schema validation: PASS
- CSF profile attenuated: WBC 2,900 (68 percent neutrophils), glucose 28, protein 175.
- Diagnostic_ambiguity=true; type=partial_antibiotic_pretreatment_sterile_cultures.

### v81 - bact_081_sp_elderly_fatal.json
- Anchor: PMID 15509818 (van de Beek eldest stratum mortality 51 percent at age >=70)
- Demographic: 79yo F, Netherlands, GCS 6 on admission, hyponatremic.
- Schema validation: PASS
- CSF profile: WBC 3,800 (78 percent neutrophils), glucose 28, protein 170.
- Outcome=fatal_hospital_day_2. Imaging pattern: diffuse_cerebral_edema_basilar_meningeal_enhancement (severe-late mapping).

### v90 - bact_090_gn_post_neurosurgical_fatal.json
- Anchor: PMID 15494903 (Tunkel IDSA healthcare-associated meningitis recommendations)
- Demographic: 55yo M, US South, glioma resection day 9 with CSF leak, late fatal.
- Schema validation: PASS
- CSF profile: WBC 4,500 (86 percent neutrophils), glucose 16, protein 290 - high-protein gram-negative pattern.
- Gram-negative rods on Gram stain; CSF + blood culture Pseudomonas aeruginosa.
- `red_flags_present=["recent_neurosurgery"]`; `focal_neurological_deficit=true` (right hemiparesis post-op).
- Imaging pattern: diffuse_cerebral_edema_basilar_meningeal_enhancement.

## Schema-to-Spec Field Mapping Decisions

| Spec field | Schema rendering | Reason |
|---|---|---|
| diagnostic_ambiguity, ambiguity_type | provenance.inclusion_decision_rationale + narrative + adjudication.anchoring_documentation | extra="forbid" prevents new keys; identical to 5.3.2 pilot decision D8 |
| risk_factors=["asplenia"] | narrative + rationale (immunocompromise_status="none") | schema enum lacks "asplenia" value; documented but not enum-encoded |
| risk_factors=["immunocompromise"] (HIV) | hiv_status="positive_on_art" + cd4_count_cells_per_uL + immunocompromise_status="hiv_cd4_over200" + red_flags_present=["immunocompromise"] | full enum support for HIV-on-ART stratum |
| risk_factors=["immunocompromise"] (post-neurosurgical) | red_flags_present=["recent_neurosurgery"] + narrative | schema red_flag enum supports this directly |
| pre-adjudication structured fields (stage, status, self_review_disposition, self_review_notes, etc.) | adjudication.anchoring_documentation (max 2000 chars structured text) | per 5.3.2 D8; preserves verbatim self_review_disposition=hold_for_revision |
| imputation_tier_per_field, indeterminate_fields | provenance.inclusion_decision_rationale (structured text within 1000 char budget) | per 5.3.2 D8 |

## Quality Gates Summary

| Gate | Result |
|---|---|
| 14 wave-1 vignettes constructed | 14/14 |
| Schema validation pass rate | 14/14 |
| All v2/class_02_bacterial vignette JSONs validate | 17/17 (3 pilots + 14 wave-1) |
| Cross-corpus v2 vignette schema | 20/20 (3 BACT pilots + 14 BACT wave-1 + 3 VIRAL pilots) |
| Em-dashes (—) corpus-wide | 0 |
| En-dashes (–) corpus-wide | 0 |
| AI-tell vocabulary corpus-wide | 0 |
| Spanish narrative coverage | 14/14 |
| Spanish narrative length 700-900 char band | 14/14 (range 707-887) |
| English narrative length 750-1000 char band | 14/14 (range 754-987) |
| Anchor PMID resolves in PMID_REGISTRY | 14/14 (10 to 15494903 + 4 to 15509818) |
| Pre-adjudication hold_for_revision verbatim | 14/14 |
| Diagnostic ambiguity slots = 4 | 4/4 (v75, v76, v79, v80) |
| Tunkel anchor count = 10 | 10/10 |
| van de Beek anchor count = 4 | 4/4 |
| SP pathogen count = 13, GN pathogen count = 1 | 13+1/14 |
| freshwater_exposure_within_14d=False | 14/14 |
| ground_truth_class=2 | 14/14 |
| Cross-field validators pass rate | 70/70 (5 invariants x 14 vignettes) |
| Wave-1 lock-in tests | 65/65 passing |
| Full test suite parity post-commit | 1933 passed, 1 skipped, 1 xfailed (no regressions) |
| 5.3.1 lock-in tests | unchanged, all preserved |
| PMID_REGISTRY entries | 57 (no change; both Wave-1 anchors pre-registered) |

## Lock-in Test Architecture

`tests/test_subphase_1_3_wave1_bact_lockin.py` provides 13 named tests across 65 parametrized cases:
1. `test_bact_wave1_files_exist` (parametrized over 14 IDs)
2. `test_bact_wave1_schema_validates` (parametrized over 14 IDs)
3. `test_bact_wave1_demographics_match_spec` (parametrized over 14 IDs - asserts age, sex, geography_region)
4. `test_bact_wave1_anchor_pmid_matches` (parametrized over 14 IDs)
5. `test_bact_wave1_freshwater_false`
6. `test_bact_wave1_class_id_2`
7. `test_bact_wave1_csf_neutrophilic` (>=50 percent)
8. `test_bact_wave1_csf_glucose_low` (<=40)
9. `test_bact_wave1_csf_protein_high` (>=100)
10. `test_bact_wave1_pre_adjudication_hold` (verbatim)
11. `test_bact_wave1_ambiguity_count` (set equality with {75, 76, 79, 80})
12. `test_bact_wave1_no_em_dashes`
13. `test_bact_wave1_no_ai_tells`

TDD discipline: all 13 tests confirmed RED (65 failures) before any helper function landed. After helper construction + JSON write, all 13 confirmed GREEN.

## Honest Disclosure

- All 14 wave-1 vignettes carry pre-adjudication `hold_for_revision` status. External clinical adjudication has NOT been performed.
- Schema's `immunocompromise_status` enum lacks an "asplenia" value; v65 uses `immunocompromise_status="none"` with asplenia captured in prodrome_description, narrative, and inclusion_decision_rationale. This is a faithful schema-respecting mapping rather than a clinical claim that v65 is immunocompetent.
- Schema's `AdjudicationMetadata` has only 5 rigid fields; the structured pre-adjudication disclosure is embedded into `anchoring_documentation` per 5.3.2 D8.
- Schema's `Provenance` has only 5 rigid fields; the imputation_tier_per_field + indeterminate_fields metadata is embedded into `inclusion_decision_rationale` (max 1000 chars) per 5.3.2 D8.
- The 4 ambiguity vignettes (v75, v76, v79, v80) deliberately carry attenuated CSF profiles (WBC 1,600-2,900, neutrophil 60-70 percent) that lie at the lower end of the master prompt 1.3.3 bacterial range. This is intentional clinical heterogeneity per the partial-antibiotic-pretreatment IDSA narrative; the cases sit in the gray zone between bacterial and viral CSF profiles where pre-treatment pharmacology has attenuated the inflammatory response. Antigen + PCR confirms organism; cultures are sterile by design.
- v90 GN healthcare-associated meningitis culture organism (Pseudomonas aeruginosa) is one of several plausible gram-negative organisms covered by Tunkel IDSA HCA empiric meropenem regimen; choice was made as the most clinically informative single organism for the 1-of-30 GN slot in BACTERIAL_DISTRIBUTION rather than alternating across multiple GN species.
- Imaging pattern for fatal cases (v66, v73, v81, v90) maps to `diffuse_cerebral_edema_basilar_meningeal_enhancement` from the 14-value Literal enum. Mid-stage survived cases use `normal` per Tunkel narrative that admission CT is typically normal in early adult community-acquired bacterial meningitis.
- The 4 ambiguity rationale strings carry the explicit token `diagnostic_ambiguity=true` and the verbatim `type=partial_antibiotic_pretreatment_sterile_cultures` per slot spec. Test 11 enforces this set equality.
- Anchoring documentation follows the verbatim shape established by 5.3.2 pilots: `stage=pre_adjudication; status=pending_external_review; self_review_disposition=hold_for_revision; self_review_notes=...; adjudicator_ids=WAVE1-PRE-ADJ-1, WAVE1-PRE-ADJ-2 (sentinel); cohen_kappa=0.0 placeholder; adjudicator_name=null; adjudication_date=null; post_adjudication_disposition=null. Subphase 1.3 commit 5.3.3 (2026-05-08).` Sentinel adjudicator IDs distinguish Wave 1 from Pilot adjudicators.

## Methodology Distribution After Commit 5.3.3 (Bacterial running totals)

| Tier | Bacterial running total |
|---|---|
| primary_source_direct | 3/30 (v62, v64, v82 - all from 5.3.2 pilot) |
| tier_3_imputation_within_cohort_review (van de Beek-anchored) | 4/30 (v66, v73, v77, v81 - new 5.3.3) |
| tier_4_imputation_idsa_guideline_anchored (Tunkel-anchored) | 10/30 (v65, v67, v69, v71, v75, v76, v78, v79, v80, v90 - new 5.3.3) |
| tier_3 / tier_4 / not yet built (slot reserved) | 13/30 (v61, v63, v68, v70, v72, v74, v83-v89 + v90 etc per 5.3.1 distribution) |

## Forward-Compatibility Notes

- The `_BACT_WAVE1_BUILDERS` dispatch table is keyed by vignette_id, paralleling the `builders` dispatch in `generate_vignette()` for the PAM corpus. Future BACT waves (e.g., 5.3.4 wave 2 finishing the remaining 16 BACT slots) can either extend `_BACT_WAVE1_BUILDERS` (rename) or start a separate `_BACT_WAVE2_BUILDERS` table with its own writer.
- `BACT_WAVE1_OUTPUT_DIR` and `BACT_WAVE1_IDS` and `BACT_WAVE1_AMBIGUITY_IDS` are exported as module-level constants for downstream tests.
- `write_bact_wave1_corpus()` is idempotent: it overwrites existing JSONs in place and validates each before write. Safe to re-run.

## Quality Rating Table

[See commit message and final response for empirically-backed Quality Rating Table.]
