# Subphase 1.4 PAM Vignette Deep Audit — Sub-Bundle 04: Neti / Ritual / Tap / Thermal

**Date:** 2026-05-27
**Sub-bundle:** 04 of 12
**Scope:** PAM vignettes with exposure type matching neti pot, nasal rinse, ablution, ritual, tap water, hot spring, or geothermal sources.
**Status:** READ-ONLY raw extraction; cross-check vs paper truth + errata logging pending (Claude follow-up).
**Corpus denominator:** 270 vignettes total target (60 PAM shipped). Sub-Bundle 04 covers 26 vignettes = 9.6% of full corpus, 43.3% of PAM.

## Match Summary

| Filter | Count |
|---|---|
| Exposure-type regex (neti/tap/ritual/thermal/ablution) | 24 |
| PMID anchor sweep (Yoder 2012, Linam 2015, Yoder 2010, Cope 2015) | 9 |
| MMWR USVI / ablution / Virgin Islands sweep | 9 |
| **Union (de-duped)** | **26** |

**Scope discrepancy disclosed:** User prompt estimate was 10-15 vignettes; union = 26. Some matches likely incidental keyword hits (e.g. "thermal" or "tap" appearing in narrative text without being the primary exposure type). All matches extracted below; Claude will classify scope-fit during cross-check phase.

## Sub-Bundle 04 Confirmed Anchors (from prompt)

| Anchor PMID | First author | Year | Journal | Title (abbrev) |
|---|---|---|---|---|
| 22919000 | Yoder JS et al. | 2012 | Clin Infect Dis | PAM deaths associated with sinus irrigation using contaminated tap water |
| 25667249 | Linam WM et al. | 2015 | Pediatrics | Successful treatment of an adolescent with N. fowleri PAM |
| 19845995 | Yoder JS et al. | 2010 | Epidemiol Infect | Epidemiology of PAM in the USA, 1962-2008 |
| 25595746 | Cope JR et al. | 2015 | Clin Infect Dis | First association of PAM death with culturable N. fowleri in tap water from US treated public drinking water |
| MMWR USVI (no PMID in prompt) | CDC | n/a | MMWR | PAM associated with ritual nasal rinsing - US Virgin Islands |

## Per-Vignette Extraction Tables

Each block below is raw extraction from the JSON file. No opinions, no clinical interpretation — just data.

---

### Vignette 1 — `pam_d1_006_pond_pediatric.json`

**case_id:** PAM-D1-006-IDCases-2021-Florida-Lake-Pond

**Demographics:** age=13, sex=male, ethnicity=white_non_hispanic, geography=us_south, altitude_residence_m=100

**Exposure:** type=`lake`, within_14d=True, immunocomp=none, hiv=negative

**Literature anchors:** PMID 34307045 (case_report; DOI 10.1016/j.idcr.2021.e01208)

**CSF:** WBC=1800 /mm³, neut%=90, lymph%=8, glucose=30 mg/dL, protein=200 mg/dL, RBC=90 /mm³, opening_pressure=26.0 cmH₂O, wet_mount_motile=positive, crag_lfa=negative, lactate=5.0 mmol/L, ADA=None U/L

**Vitals:** temp=39.5°C, HR=124, RR=22, SBP/DBP=118/72, SpO₂=98%, GCS=13

**Exam:** neck_stiffness=True, kernig_brudzinski=True, mental_status_grade=confused, cranial_nerve_palsy=none, focal_neuro=False, papilledema=False, petechial_rash=False

**History:** chief=`fever_with_headache`, prodrome=`Three days of fever, severe occipital headache, vomiting, and progressive lethargy after recreational swimming in a private freshwater pond approximately five days before symptom onset; new-onset photophobia and neck stiffness in the 24 hours before admission.`, onset_to_presentation_d=4.0, red_flags=['fresh_water_exposure_14d']

**Ground truth class:** 1

**Adjudication anchoring_documentation:**

> Anchored to Anjum SK et al. IDCases 2021 (PMID 34307045). Demographics: 13 years male, Florida, US. Stage metadata: clinical_stage=mid, exposure_certainty=definite, diagnostic_confirmation=PCR (CDC reference laboratory CSF Naegleria fowleri), outcome=fatal. CSF and imaging within published case ranges; vitals imputed from PAM presentation patterns documented in CDC PAM case reviews.

**Provenance inclusion_decision_rationale:**

> Day 1 vignette 6 of 20 for Subphase 1.2 PAM corpus. Cluster: lake_pond. Atypical type: none. Outcome: fatal. Anchored to PMID 34307045 (Anjum SK et al., IDCases 2021). Sub-fields populated from published case where available; vitals and partial labs IMPUTED_FROM_LITERATURE consistent with mid-stage PAM clinical patterns documented in CDC PAM case reviews. Treatment per CDC six-drug protocol (amphotericin B, miltefosine, dexamethasone, fluconazole, azithromycin, rifampin); fatal outcome despite full regimen. Citation caveat: US tap-water-associated PAM 2020s. Pairs with USVI ablution case (PMID 24226628) for tap-water transmission cluster adjudication. 11 authors confirmed (Saccoccio FM at end). DOI is e01208 (NOT e01218). Author 8 'O'Laughlin K' preserves apostrophe. Author 6 'Ibne Karim M Ali' renders as Vancouver 'Ali IKM' (3 initials). Authors: Saad K Anjum, Karna Mangrola, Garrett Fitzpatrick, Kimberly Stockdale, Laura Matthias, Ibne Karim M Ali, Jennifer R Cope, Kevin O'Laughli...

---

### Vignette 2 — `pam_d1_009_lake_adolescent.json`

**case_id:** PAM-D1-009-IDCases-2021-Florida-Lake-Pond

**Demographics:** age=14, sex=male, ethnicity=white_non_hispanic, geography=us_south, altitude_residence_m=100

**Exposure:** type=`lake`, within_14d=True, immunocomp=none, hiv=negative

**Literature anchors:** PMID 34307045 (case_report; DOI 10.1016/j.idcr.2021.e01208)

**CSF:** WBC=4200 /mm³, neut%=95, lymph%=4, glucose=14 mg/dL, protein=400 mg/dL, RBC=680 /mm³, opening_pressure=44.0 cmH₂O, wet_mount_motile=positive, crag_lfa=negative, lactate=8.6 mmol/L, ADA=None U/L

**Vitals:** temp=39.8°C, HR=128, RR=28, SBP/DBP=102/60, SpO₂=93%, GCS=7

**Exam:** neck_stiffness=True, kernig_brudzinski=True, mental_status_grade=stuporous, cranial_nerve_palsy=none, focal_neuro=False, papilledema=True, petechial_rash=False

**History:** chief=`altered_mental_status`, prodrome=`Five days of fever, severe headache, photophobia, vomiting, and increasing lethargy after lake swimming and underwater diving approximately one week before symptom onset; one witnessed generalized seizure 18 hours before admission with progressive obtundation.`, onset_to_presentation_d=6.0, red_flags=['fresh_water_exposure_14d']

**Ground truth class:** 1

**Adjudication anchoring_documentation:**

> Anchored to Anjum SK et al. IDCases 2021 (PMID 34307045). Demographics: 14 years male, Florida, US. Stage metadata: clinical_stage=late, exposure_certainty=definite, diagnostic_confirmation=PCR (CDC reference laboratory CSF Naegleria fowleri), outcome=fatal. CSF and imaging within published case ranges; vitals imputed from PAM presentation patterns documented in CDC PAM case reviews.

**Provenance inclusion_decision_rationale:**

> Day 1 vignette 9 of 20 for Subphase 1.2 PAM corpus. Cluster: lake_pond. Atypical type: none. Outcome: fatal. Anchored to PMID 34307045 (Anjum SK et al., IDCases 2021). Sub-fields populated from published case where available; vitals and partial labs IMPUTED_FROM_LITERATURE consistent with late-stage PAM clinical patterns documented in CDC PAM case reviews. Treatment per CDC six-drug protocol (amphotericin B, miltefosine, dexamethasone, fluconazole, azithromycin, rifampin); fatal outcome despite full regimen. Citation caveat: US tap-water-associated PAM 2020s. Pairs with USVI ablution case (PMID 24226628) for tap-water transmission cluster adjudication. 11 authors confirmed (Saccoccio FM at end). DOI is e01208 (NOT e01218). Author 8 'O'Laughlin K' preserves apostrophe. Author 6 'Ibne Karim M Ali' renders as Vancouver 'Ali IKM' (3 initials). Authors: Saad K Anjum, Karna Mangrola, Garrett Fitzpatrick, Kimberly Stockdale, Laura Matthias, Ibne Karim M Ali, Jennifer R Cope, Kevin O'Laughl...

---

### Vignette 3 — `pam_d1_010_neti_pot_adult.json`

**case_id:** PAM-D1-010-CID-2012-Louisiana-Nasal-Irrigation

**Demographics:** age=28, sex=male, ethnicity=white_non_hispanic, geography=us_south, altitude_residence_m=100

**Exposure:** type=`neti_pot_tap_water`, within_14d=True, immunocomp=none, hiv=negative

**Literature anchors:** PMID 22919000 (case_report; DOI 10.1093/cid/cis626)

**CSF:** WBC=2400 /mm³, neut%=92, lymph%=6, glucose=26 mg/dL, protein=240 mg/dL, RBC=320 /mm³, opening_pressure=30.0 cmH₂O, wet_mount_motile=positive, crag_lfa=negative, lactate=6.2 mmol/L, ADA=None U/L

**Vitals:** temp=39.6°C, HR=122, RR=22, SBP/DBP=116/70, SpO₂=96%, GCS=12

**Exam:** neck_stiffness=True, kernig_brudzinski=True, mental_status_grade=somnolent, cranial_nerve_palsy=none, focal_neuro=False, papilledema=False, petechial_rash=False

**History:** chief=`fever_with_headache`, prodrome=`Three days of fever, severe frontal headache, photophobia, and one episode of emesis after several weeks of daily nasal irrigation with a neti pot filled with municipal tap water; on the day of admission he developed neck stiffness and increasing somnolence.`, onset_to_presentation_d=4.0, red_flags=['fresh_water_exposure_14d']

**Ground truth class:** 1

**Adjudication anchoring_documentation:**

> Anchored to Yoder JS et al. Clin Infect Dis 2012 (PMID 22919000). Demographics: 28 years male, Louisiana, US. Stage metadata: clinical_stage=mid, exposure_certainty=definite, diagnostic_confirmation=PCR (CDC reference laboratory CSF Naegleria fowleri), outcome=fatal. CSF and imaging within published case ranges; vitals imputed from PAM presentation patterns documented in CDC PAM case reviews.

**Provenance inclusion_decision_rationale:**

> Day 1 vignette 10 of 20 for Subphase 1.2 PAM corpus. Cluster: nasal_irrigation. Atypical type: adult_nasal_rinse. Outcome: fatal. Anchored to PMID 22919000 (Yoder JS et al., Clin Infect Dis 2012). Sub-fields populated from published case where available; vitals and partial labs IMPUTED_FROM_LITERATURE consistent with mid-stage PAM clinical patterns documented in CDC PAM case reviews. Treatment per CDC six-drug protocol (amphotericin B, miltefosine, dexamethasone, fluconazole, azithromycin, rifampin); fatal outcome despite full regimen. Citation caveat: PMC11307261 is an NIHMS author-manuscript deposit posted retroactively (2024) for the 2012 paper. Publisher of record is Clin Infect Dis 2012;55(9):e79-e85, DOI 10.1093/cid/cis626.

---

### Vignette 4 — `pam_d1_011_neti_pot_adult.json`

**case_id:** PAM-D1-011-CID-2012-Louisiana-Nasal-Irrigation

**Demographics:** age=51, sex=female, ethnicity=white_non_hispanic, geography=us_south, altitude_residence_m=100

**Exposure:** type=`neti_pot_tap_water`, within_14d=True, immunocomp=none, hiv=negative

**Literature anchors:** PMID 22919000 (case_report; DOI 10.1093/cid/cis626)

**CSF:** WBC=4800 /mm³, neut%=96, lymph%=3, glucose=12 mg/dL, protein=440 mg/dL, RBC=980 /mm³, opening_pressure=48.0 cmH₂O, wet_mount_motile=positive, crag_lfa=negative, lactate=9.0 mmol/L, ADA=None U/L

**Vitals:** temp=39.8°C, HR=134, RR=30, SBP/DBP=92/56, SpO₂=92%, GCS=6

**Exam:** neck_stiffness=True, kernig_brudzinski=True, mental_status_grade=comatose, cranial_nerve_palsy=none, focal_neuro=False, papilledema=True, petechial_rash=False

**History:** chief=`altered_mental_status`, prodrome=`Five days of fever, severe headache, vomiting, and increasing confusion following habitual neti-pot use with untreated household tap water; family found her unresponsive on the morning of admission with one witnessed generalized seizure during transport.`, onset_to_presentation_d=5.5, red_flags=['fresh_water_exposure_14d']

**Ground truth class:** 1

**Adjudication anchoring_documentation:**

> Anchored to Yoder JS et al. Clin Infect Dis 2012 (PMID 22919000). Demographics: 51 years female, Louisiana, US. Stage metadata: clinical_stage=late, exposure_certainty=definite, diagnostic_confirmation=PCR (CDC reference laboratory CSF Naegleria fowleri), outcome=fatal. CSF and imaging within published case ranges; vitals imputed from PAM presentation patterns documented in CDC PAM case reviews.

**Provenance inclusion_decision_rationale:**

> Day 1 vignette 11 of 20 for Subphase 1.2 PAM corpus. Cluster: nasal_irrigation. Atypical type: adult_nasal_rinse. Outcome: fatal. Anchored to PMID 22919000 (Yoder JS et al., Clin Infect Dis 2012). Sub-fields populated from published case where available; vitals and partial labs IMPUTED_FROM_LITERATURE consistent with late-stage PAM clinical patterns documented in CDC PAM case reviews. Treatment per CDC six-drug protocol (amphotericin B, miltefosine, dexamethasone, fluconazole, azithromycin, rifampin); fatal outcome despite full regimen. Citation caveat: PMC11307261 is an NIHMS author-manuscript deposit posted retroactively (2024) for the 2012 paper. Publisher of record is Clin Infect Dis 2012;55(9):e79-e85, DOI 10.1093/cid/cis626.

---

### Vignette 5 — `pam_d1_012_rv_nasal_adult.json`

**case_id:** PAM-D1-012-MMWR-2025-Texas-Nasal-Irrigation

**Demographics:** age=71, sex=female, ethnicity=white_non_hispanic, geography=us_south, altitude_residence_m=100

**Exposure:** type=`neti_pot_tap_water`, within_14d=True, immunocomp=none, hiv=negative

**Literature anchors:** PMID 40440212 (surveillance; DOI None)

**CSF:** WBC=2800 /mm³, neut%=91, lymph%=7, glucose=24 mg/dL, protein=260 mg/dL, RBC=280 /mm³, opening_pressure=32.0 cmH₂O, wet_mount_motile=positive, crag_lfa=negative, lactate=6.4 mmol/L, ADA=None U/L

**Vitals:** temp=39.4°C, HR=118, RR=24, SBP/DBP=122/72, SpO₂=95%, GCS=11

**Exam:** neck_stiffness=True, kernig_brudzinski=True, mental_status_grade=somnolent, cranial_nerve_palsy=none, focal_neuro=False, papilledema=False, petechial_rash=False

**History:** chief=`fever_with_headache`, prodrome=`Four days of fever, severe headache, photophobia, vomiting, and progressive lethargy after several days of nasal irrigation using water drawn from a recreational vehicle freshwater holding tank during an extended camping trip; no recreational swimming or lake exposure documented.`, onset_to_presentation_d=4.5, red_flags=['fresh_water_exposure_14d']

**Ground truth class:** 1

**Adjudication anchoring_documentation:**

> Anchored to Smith et al. MMWR Morb Mortal Wkly Rep 2025 (PMID 40440212). Demographics: 71 years female, Texas, US. Stage metadata: clinical_stage=mid, exposure_certainty=definite, diagnostic_confirmation=PCR (CDC reference laboratory CSF Naegleria fowleri), outcome=fatal. CSF and imaging within published case ranges; vitals imputed from PAM presentation patterns documented in CDC PAM case reviews.

**Provenance inclusion_decision_rationale:**

> Day 1 vignette 12 of 20 for Subphase 1.2 PAM corpus. Cluster: nasal_irrigation. Atypical type: rv_plumbing. Outcome: fatal. Anchored to PMID 40440212 (Smith et al., MMWR Morb Mortal Wkly Rep 2025). Sub-fields populated from published case where available; vitals and partial labs IMPUTED_FROM_LITERATURE consistent with mid-stage PAM clinical patterns documented in CDC PAM case reviews. Treatment per CDC six-drug protocol (amphotericin B, miltefosine, dexamethasone, fluconazole, azithromycin, rifampin); fatal outcome despite full regimen. Citation caveat: 5-pass verified 14 authors (NOT 13). Kunz J added as author #14 (corresponding author). Citation: MMWR 74(19):334-335.

---

### Vignette 6 — `pam_d1_013_hot_spring_pediatric.json`

**case_id:** PAM-D1-013-MMWR-2019-California-Hot-Springs

**Demographics:** age=12, sex=male, ethnicity=other, geography=other_global, altitude_residence_m=100

**Exposure:** type=`hot_spring`, within_14d=True, immunocomp=none, hiv=negative

**Literature anchors:** PMID 31513557 (surveillance; DOI None)

**CSF:** WBC=2200 /mm³, neut%=90, lymph%=8, glucose=28 mg/dL, protein=220 mg/dL, RBC=220 /mm³, opening_pressure=28.0 cmH₂O, wet_mount_motile=positive, crag_lfa=negative, lactate=5.6 mmol/L, ADA=None U/L

**Vitals:** temp=39.7°C, HR=128, RR=24, SBP/DBP=108/64, SpO₂=95%, GCS=12

**Exam:** neck_stiffness=True, kernig_brudzinski=True, mental_status_grade=somnolent, cranial_nerve_palsy=none, focal_neuro=False, papilledema=False, petechial_rash=False

**History:** chief=`fever_with_headache`, prodrome=`Four days of fever, frontal headache, vomiting, and increasing irritability after a multi-family camping trip in eastern California during which the child swam and submerged his head repeatedly in a geothermal hot-spring pool approximately six days before symptom onset.`, onset_to_presentation_d=4.0, red_flags=['fresh_water_exposure_14d']

**Ground truth class:** 1

**Adjudication anchoring_documentation:**

> Anchored to Vugia DJ et al. MMWR Morb Mortal Wkly Rep 2019 (PMID 31513557). Demographics: 12 years male, California, US. Stage metadata: clinical_stage=mid, exposure_certainty=definite, diagnostic_confirmation=PCR (CDC reference laboratory CSF Naegleria fowleri), outcome=fatal. CSF and imaging within published case ranges; vitals imputed from PAM presentation patterns documented in CDC PAM case reviews.

**Provenance inclusion_decision_rationale:**

> Day 1 vignette 13 of 20 for Subphase 1.2 PAM corpus. Cluster: hot_springs. Atypical type: none. Outcome: fatal. Anchored to PMID 31513557 (Vugia DJ et al., MMWR Morb Mortal Wkly Rep 2019). Sub-fields populated from published case where available; vitals and partial labs IMPUTED_FROM_LITERATURE consistent with mid-stage PAM clinical patterns documented in CDC PAM case reviews. Treatment per CDC six-drug protocol (amphotericin B, miltefosine, dexamethasone, fluconazole, azithromycin, rifampin); fatal outcome despite full regimen.

---

### Vignette 7 — `pam_d1_014_hot_spring_adult.json`

**case_id:** PAM-D1-014-MMWR-2016-California-Hot-Springs

**Demographics:** age=21, sex=female, ethnicity=other, geography=other_global, altitude_residence_m=100

**Exposure:** type=`swimming_pool_unchlorinated`, within_14d=True, immunocomp=none, hiv=negative

**Literature anchors:** PMID 27123690 (surveillance; DOI None)

**CSF:** WBC=4400 /mm³, neut%=95, lymph%=4, glucose=12 mg/dL, protein=420 mg/dL, RBC=880 /mm³, opening_pressure=46.0 cmH₂O, wet_mount_motile=positive, crag_lfa=negative, lactate=9.0 mmol/L, ADA=None U/L

**Vitals:** temp=39.9°C, HR=138, RR=30, SBP/DBP=96/58, SpO₂=92%, GCS=7

**Exam:** neck_stiffness=True, kernig_brudzinski=True, mental_status_grade=stuporous, cranial_nerve_palsy=none, focal_neuro=False, papilledema=True, petechial_rash=False

**History:** chief=`altered_mental_status`, prodrome=`Five days of fever, severe headache, vomiting, and progressive lethargy after recreational swimming in a private residential pool fed by overland piping from an upgradient natural spring; one witnessed generalized seizure 12 hours before admission.`, onset_to_presentation_d=6.0, red_flags=['fresh_water_exposure_14d']

**Ground truth class:** 1

**Adjudication anchoring_documentation:**

> Anchored to Johnson RO, Cope JR et al. MMWR Morb Mortal Wkly Rep 2016 (PMID 27123690). Demographics: 21 years female, California, US. Stage metadata: clinical_stage=late, exposure_certainty=definite, diagnostic_confirmation=PCR (CDC reference laboratory CSF Naegleria fowleri), outcome=fatal. CSF and imaging within published case ranges; vitals imputed from PAM presentation patterns documented in CDC PAM case reviews.

**Provenance inclusion_decision_rationale:**

> Day 1 vignette 14 of 20 for Subphase 1.2 PAM corpus. Cluster: hot_springs. Atypical type: overland_pipe. Outcome: fatal. Anchored to PMID 27123690 (Johnson RO, Cope JR et al., MMWR Morb Mortal Wkly Rep 2016). Sub-fields populated from published case where available; vitals and partial labs IMPUTED_FROM_LITERATURE consistent with late-stage PAM clinical patterns documented in CDC PAM case reviews. Treatment per CDC six-drug protocol (amphotericin B, miltefosine, dexamethasone, fluconazole, azithromycin, rifampin); fatal outcome despite full regimen.

---

### Vignette 8 — `pam_d1_015_ablution_pediatric.json`

**case_id:** PAM-D1-015-EID-2011-Karachi-Pakistan-Ablution

**Demographics:** age=13, sex=male, ethnicity=other, geography=pakistan_karachi, altitude_residence_m=100

**Exposure:** type=`ritual_ablution_wudu`, within_14d=True, immunocomp=none, hiv=negative

**Literature anchors:** PMID 21291600 (case_report; DOI None)

**CSF:** WBC=4800 /mm³, neut%=96, lymph%=3, glucose=12 mg/dL, protein=440 mg/dL, RBC=1040 /mm³, opening_pressure=48.0 cmH₂O, wet_mount_motile=positive, crag_lfa=negative, lactate=9.2 mmol/L, ADA=None U/L

**Vitals:** temp=39.8°C, HR=138, RR=32, SBP/DBP=94/58, SpO₂=91%, GCS=6

**Exam:** neck_stiffness=True, kernig_brudzinski=True, mental_status_grade=comatose, cranial_nerve_palsy=none, focal_neuro=False, papilledema=True, petechial_rash=False

**History:** chief=`altered_mental_status`, prodrome=`Four days of fever, severe headache, vomiting, and increasing lethargy in the context of daily ritual ablution (wudu) with municipal tap water several times per day; no recreational swimming or river exposure documented; one witnessed generalized seizure on the morning of admission.`, onset_to_presentation_d=5.0, red_flags=['fresh_water_exposure_14d']

**Ground truth class:** 1

**Adjudication anchoring_documentation:**

> Anchored to Shakoor S et al. Emerg Infect Dis 2011 (PMID 21291600). Demographics: 13 years male, Karachi, PK. Stage metadata: clinical_stage=late, exposure_certainty=definite, diagnostic_confirmation=PCR (CDC reference laboratory CSF Naegleria fowleri), outcome=fatal. CSF and imaging within published case ranges; vitals imputed from PAM presentation patterns documented in CDC PAM case reviews.

**Provenance inclusion_decision_rationale:**

> Day 1 vignette 15 of 20 for Subphase 1.2 PAM corpus. Cluster: pakistan_ablution. Atypical type: religious_ablution. Outcome: fatal. Anchored to PMID 21291600 (Shakoor S et al., Emerg Infect Dis 2011). Sub-fields populated from published case where available; vitals and partial labs IMPUTED_FROM_LITERATURE consistent with late-stage PAM clinical patterns documented in CDC PAM case reviews. Treatment per CDC six-drug protocol (amphotericin B, miltefosine, dexamethasone, fluconazole, azithromycin, rifampin); fatal outcome despite full regimen. Citation caveat: 13-case Karachi series; ritual ablution exposure inferred (no aquatic activity).

---

### Vignette 9 — `pam_d1_016_ablution_adult.json`

**case_id:** PAM-D1-016-AJTMH-2017-Karachi-Pakistan-Ablution

**Demographics:** age=28, sex=male, ethnicity=other, geography=pakistan_karachi, altitude_residence_m=100

**Exposure:** type=`ritual_ablution_wudu`, within_14d=True, immunocomp=none, hiv=negative

**Literature anchors:** PMID 29016297 (cohort; DOI None)

**CSF:** WBC=2600 /mm³, neut%=92, lymph%=6, glucose=24 mg/dL, protein=250 mg/dL, RBC=360 /mm³, opening_pressure=32.0 cmH₂O, wet_mount_motile=positive, crag_lfa=negative, lactate=6.4 mmol/L, ADA=None U/L

**Vitals:** temp=39.6°C, HR=124, RR=24, SBP/DBP=110/66, SpO₂=95%, GCS=11

**Exam:** neck_stiffness=True, kernig_brudzinski=True, mental_status_grade=somnolent, cranial_nerve_palsy=none, focal_neuro=False, papilledema=False, petechial_rash=False

**History:** chief=`fever_with_headache`, prodrome=`Four days of fever, severe headache, photophobia, vomiting, and progressive somnolence in the context of daily ritual ablution (wudu) with municipal public-supply tap water and household bathing; no recreational aquatic activity documented.`, onset_to_presentation_d=4.5, red_flags=['fresh_water_exposure_14d']

**Ground truth class:** 1

**Adjudication anchoring_documentation:**

> Anchored to Ghanchi NK et al. Am J Trop Med Hyg 2017 (PMID 29016297). Demographics: 28 years male, Karachi, PK. Stage metadata: clinical_stage=mid, exposure_certainty=definite, diagnostic_confirmation=PCR (CDC reference laboratory CSF Naegleria fowleri), outcome=fatal. CSF and imaging within published case ranges; vitals imputed from PAM presentation patterns documented in CDC PAM case reviews.

**Provenance inclusion_decision_rationale:**

> Day 1 vignette 16 of 20 for Subphase 1.2 PAM corpus. Cluster: pakistan_ablution. Atypical type: religious_ablution. Outcome: fatal. Anchored to PMID 29016297 (Ghanchi NK et al., Am J Trop Med Hyg 2017). Sub-fields populated from published case where available; vitals and partial labs IMPUTED_FROM_LITERATURE consistent with mid-stage PAM clinical patterns documented in CDC PAM case reviews. Treatment per CDC six-drug protocol (amphotericin B, miltefosine, dexamethasone, fluconazole, azithromycin, rifampin); fatal outcome despite full regimen. Citation caveat: Quote precisely: 19 PCR-confirmed cases of 116 suspected at AKU 2014-2015, median age 28y, 84% male, 16% female.

---

### Vignette 10 — `pam_d1_017_costa_rica_pediatric.json`

**case_id:** PAM-D1-017-EID-2015-Florida-(acquired-Costa-Rica)-Latam

**Demographics:** age=11, sex=male, ethnicity=other, geography=other_latam, altitude_residence_m=100

**Exposure:** type=`hot_spring`, within_14d=True, immunocomp=none, hiv=negative

**Literature anchors:** PMID 25625800 (case_report; DOI None)

**CSF:** WBC=5000 /mm³, neut%=96, lymph%=3, glucose=10 mg/dL, protein=460 mg/dL, RBC=1180 /mm³, opening_pressure=50.0 cmH₂O, wet_mount_motile=positive, crag_lfa=negative, lactate=9.4 mmol/L, ADA=None U/L

**Vitals:** temp=39.8°C, HR=140, RR=32, SBP/DBP=92/56, SpO₂=91%, GCS=6

**Exam:** neck_stiffness=True, kernig_brudzinski=True, mental_status_grade=comatose, cranial_nerve_palsy=none, focal_neuro=False, papilledema=True, petechial_rash=False

**History:** chief=`altered_mental_status`, prodrome=`Five days of fever, severe headache, photophobia, vomiting, and progressive lethargy beginning shortly after return to Florida from a family vacation in Costa Rica, during which the child swam and submerged his head in a public geothermal hot-spring pool approximately 12 days before symptom onset; two witnessed generalized seizures in the 18 hours before admission.`, onset_to_presentation_d=6.0, red_flags=['fresh_water_exposure_14d']

**Ground truth class:** 1

**Adjudication anchoring_documentation:**

> Anchored to Abrahams-Sandí E et al. Emerg Infect Dis 2015 (PMID 25625800). Demographics: 11 years male, Florida (acquired Costa Rica). Stage metadata: clinical_stage=late, exposure_certainty=definite, diagnostic_confirmation=PCR (CDC reference laboratory CSF Naegleria fowleri), outcome=fatal. CSF and imaging within published case ranges; vitals imputed from PAM presentation patterns documented in CDC PAM case reviews.

**Provenance inclusion_decision_rationale:**

> Day 1 vignette 17 of 20 for Subphase 1.2 PAM corpus. Cluster: latam. Atypical type: travel_acquired_hot_springs. Outcome: fatal. Anchored to PMID 25625800 (Abrahams-Sandí E et al., Emerg Infect Dis 2015). Sub-fields populated from published case where available; vitals and partial labs IMPUTED_FROM_LITERATURE consistent with late-stage PAM clinical patterns documented in CDC PAM case reviews. Treatment per CDC six-drug protocol (amphotericin B, miltefosine, dexamethasone, fluconazole, azithromycin, rifampin); fatal outcome despite full regimen. Citation caveat: Used as LATAM substitute; no Peru-specific PAM PMID exists. Diacritic on Sandí preserved per 5-pass UTF-8 verification.

---

### Vignette 11 — `pam_d1_019_burki_adult_survivor.json`

**case_id:** PAM-D1-019-Emerg Infect Dis-2024-Karachi-Survivor-Adult

**Demographics:** age=22, sex=male, ethnicity=other, geography=pakistan_karachi, altitude_residence_m=100

**Exposure:** type=`ritual_ablution_wudu`, within_14d=True, immunocomp=none, hiv=negative

**Literature anchors:** PMID 38526236 (case_report; DOI 10.3201/eid3004.230979)

**CSF:** WBC=1900 /mm³, neut%=88, lymph%=10, glucose=32 mg/dL, protein=200 mg/dL, RBC=180 /mm³, opening_pressure=28.0 cmH₂O, wet_mount_motile=positive, crag_lfa=negative, lactate=5.2 mmol/L, ADA=None U/L

**Vitals:** temp=39.4°C, HR=116, RR=22, SBP/DBP=118/72, SpO₂=96%, GCS=12

**Exam:** neck_stiffness=True, kernig_brudzinski=True, mental_status_grade=somnolent, cranial_nerve_palsy=none, focal_neuro=False, papilledema=False, petechial_rash=False

**History:** chief=`fever_with_headache`, prodrome=`Three days of fever, severe headache, photophobia, vomiting, and progressive somnolence in the context of daily ritual ablution (wudu) with municipal tap water; presented to the emergency department within hours of mental-status decline rather than progressing to coma at home.`, onset_to_presentation_d=4.0, red_flags=['fresh_water_exposure_14d']

**Ground truth class:** 1

**Adjudication anchoring_documentation:**

> Anchored to Burki AMK et al. Emerging Infectious Diseases 2024 (PMID 38526236). Demographics: 22 years male, Karachi, PK. Stage metadata: clinical_stage=mid, exposure_certainty=definite, diagnostic_confirmation=PCR (CSF Naegleria fowleri) plus CSF wet mount with motile trophozoites, outcome=survived. CSF and imaging within published case ranges; vitals imputed from PAM presentation patterns documented in CDC PAM case reviews.

**Provenance inclusion_decision_rationale:**

> Day 1 vignette 19 of 20 for Subphase 1.2 PAM corpus. Cluster: survivor_adult. Atypical type: adult_survivor_ablution. Outcome: survived. Anchored to PMID 38526236 (Burki AMK et al., Emerging Infectious Diseases 2024). Sub-fields populated from published case where available; vitals and partial labs IMPUTED_FROM_LITERATURE consistent with mid-stage PAM clinical patterns documented in CDC PAM case reviews. Treatment per CDC six-drug protocol (amphotericin B, miltefosine, dexamethasone, fluconazole, azithromycin, rifampin) with hypothermia and intracranial pressure management; survived to hospital discharge. Citation caveat: 22yo M Pakistan 2023, 8th confirmed N. fowleri SURVIVOR globally (1971-2023). PNS Shifa Hospital Karachi. Pairs naturally with Linam 2015 Kali Hardig (PMID 25667249) for outcome-contrast adjudication. Co-author Ghanchi NK also first author of PMID 27648572 (2016 EID Pakistan public water supply). Authors: Ahmed Mujadid Khan Burki, Luqman Satti, Saira Mahboob, Syed ...

---

### Vignette 12 — `pam_d2_023_lin_sichuan_myocarditis.json`

**case_id:** PAM-D2-023-Front Microbiol-2024-Sichuan-Splash-Pad

**Demographics:** age=6, sex=female, ethnicity=other, geography=other_global, altitude_residence_m=100

**Exposure:** type=`swimming_pool_unchlorinated`, within_14d=True, immunocomp=none, hiv=negative

**Literature anchors:** PMID 39606118 (case_report; DOI 10.3389/fmicb.2024.1463822)

**CSF:** WBC=960 /mm³, neut%=90, lymph%=9, glucose=85 mg/dL, protein=1000 mg/dL, RBC=3200 /mm³, opening_pressure=8.0 cmH₂O, wet_mount_motile=not_done, crag_lfa=not_done, lactate=7.8 mmol/L, ADA=None U/L

**Vitals:** temp=39.2°C, HR=184, RR=39, SBP/DBP=112/74, SpO₂=98%, GCS=8

**Exam:** neck_stiffness=True, kernig_brudzinski=True, mental_status_grade=stuporous, cranial_nerve_palsy=none, focal_neuro=True, papilledema=True, petechial_rash=False

**History:** chief=`seizure`, prodrome=`Two days of fever, headache, vomiting, and lethargy (initially diagnosed as acute upper respiratory tract infection plus acute gastritis at a local hospital, treated with oral cefaclor 48 hours prior to PICU admission). Three hours before admission a 5-minute seizure was followed by persistent coma. Patient had swum in an indoor heated public pool 7 days before symptom onset.`, onset_to_presentation_d=2.0, red_flags=['fresh_water_exposure_14d']

**Ground truth class:** 1

**Adjudication anchoring_documentation:**

> Anchored to Lin L et al. Frontiers in Microbiology 2024 (PMID 39606118). Demographics: 6 years female, Sichuan, CN. Stage metadata: clinical_stage=late, exposure_certainty=definite, diagnostic_confirmation=PCR (CDC reference laboratory CSF Naegleria fowleri), outcome=fatal. CSF and imaging within published case ranges; vitals imputed from PAM presentation patterns documented in CDC PAM case reviews.

**Provenance inclusion_decision_rationale:**

> Day 2 vignette 23 of 60 (v21-v60 set) for Subphase 1.2 PAM corpus. Cluster: splash_pad. Atypical type: indoor_heated_pool_fulminant_myocarditis. Outcome: fatal. Anchored to PMID 39606118 (Lin L et al., Frontiers in Microbiology 2024). Sub-fields populated from published case where available; vitals and partial labs IMPUTED_FROM_LITERATURE consistent with late-stage PAM clinical patterns documented in CDC PAM case reviews. Treatment per CDC six-drug protocol (amphotericin B, miltefosine, dexamethasone, fluconazole, azithromycin, rifampin); fatal outcome despite full regimen. Citation caveat: 6yo F Sichuan China, indoor heated pool 7d pre-onset April 2024, fulminant myocarditis presentation, ECMO-managed, novel candidate genotype k39_3, FATAL despite AmpB + rifampin. Same index patient as Li J 2025 Front Med (PMID 40969815) field investigation companion paper. Authors: Liangkang Lin, Lili Luo, Mei Wu, Jun Chen, Yi Liao, Haiyang Zhang.

---

### Vignette 13 — `pam_d2_024_hong_korea_thailand_travel.json`

**case_id:** PAM-D2-024-Yonsei Med J-2023-Korea-(acquired-Thailand)-Lake-Pond

**Demographics:** age=52, sex=male, ethnicity=other, geography=other_global, altitude_residence_m=100

**Exposure:** type=`lake`, within_14d=True, immunocomp=none, hiv=negative

**Literature anchors:** PMID 37727924 (case_report; DOI 10.3349/ymj.2023.0189)

**CSF:** WBC=1100 /mm³, neut%=94, lymph%=5, glucose=1 mg/dL, protein=1537 mg/dL, RBC=3168 /mm³, opening_pressure=26.0 cmH₂O, wet_mount_motile=not_done, crag_lfa=not_done, lactate=None mmol/L, ADA=None U/L

**Vitals:** temp=38.6°C, HR=108, RR=22, SBP/DBP=138/84, SpO₂=96%, GCS=14

**Exam:** neck_stiffness=True, kernig_brudzinski=True, mental_status_grade=alert, cranial_nerve_palsy=none, focal_neuro=False, papilledema=False, petechial_rash=False

**History:** chief=`fever_with_headache`, prodrome=`Three-day history of headache and fever in a 52-year-old male who had been a resident employee in Thailand for the past 4 months and returned to South Korea 1 day before presentation. No specific freshwater exposure type documented in primary source during the 4-month Thailand residence; rapid neurological deterioration from alert mental status on day 1 to stuporous within 8 hours, then apnea and fixed pupils requiring mechanical ventilation.`, onset_to_presentation_d=3.0, red_flags=['fresh_water_exposure_14d']

**Ground truth class:** 1

**Adjudication anchoring_documentation:**

> Anchored to Hong KW et al. Yonsei Medical Journal 2023 (PMID 37727924). Demographics: 52 years male, Korea (acquired Thailand). Stage metadata: clinical_stage=mid, exposure_certainty=definite, diagnostic_confirmation=PCR (CDC reference laboratory CSF Naegleria fowleri), outcome=fatal. CSF and imaging within published case ranges; vitals imputed from PAM presentation patterns documented in CDC PAM case reviews.

**Provenance inclusion_decision_rationale:**

> Day 2 vignette 24 of 60 (v21-v60 set) for Subphase 1.2 PAM corpus. Cluster: lake_pond. Atypical type: travel_imported_undocumented_exposure. Outcome: fatal. Anchored to PMID 37727924 (Hong KW et al., Yonsei Medical Journal 2023). Sub-fields populated from published case where available; vitals and partial labs IMPUTED_FROM_LITERATURE consistent with mid-stage PAM clinical patterns documented in CDC PAM case reviews. Treatment per CDC six-drug protocol (amphotericin B, miltefosine, dexamethasone, fluconazole, azithromycin, rifampin); fatal outcome despite full regimen. Citation caveat: Korean man in 50s, 4-month Thailand stay, returned Korea 10 Dec 2022, symptoms began evening of arrival, admitted 11 Dec, died 21 Dec 2022 (13d post-onset); first imported PAM case in Korea; KDCA-confirmed 99.6% genetic match to overseas PAM strain. atypical_type=travel_imported_lake. 6 authors with hyphenated Korean given names (Kyung-Wook, Jong-Hwan, Jung-Hyun, Sung-Hee, Jung-Won, In-Gyu). Authors: K...

---

### Vignette 14 — `pam_d2_025_linam_kali_hardig_survivor.json`

**case_id:** PAM-D2-025-Pediatrics-2015-Arkansas-Splash-Pad

**Demographics:** age=12, sex=female, ethnicity=white_non_hispanic, geography=us_south, altitude_residence_m=100

**Exposure:** type=`splash_pad`, within_14d=True, immunocomp=none, hiv=negative

**Literature anchors:** PMID 25667249 (case_report; DOI 10.1542/peds.2014-2292)

**CSF:** WBC=3675 /mm³, neut%=86, lymph%=14, glucose=22 mg/dL, protein=374 mg/dL, RBC=53 /mm³, opening_pressure=25.0 cmH₂O, wet_mount_motile=positive, crag_lfa=negative, lactate=None mmol/L, ADA=None U/L

**Vitals:** temp=39.4°C, HR=110, RR=18, SBP/DBP=110/68, SpO₂=98%, GCS=14

**Exam:** neck_stiffness=False, kernig_brudzinski=False, mental_status_grade=alert, cranial_nerve_palsy=none, focal_neuro=False, papilledema=None, petechial_rash=False

**History:** chief=`fever_with_headache`, prodrome=`Two-day history of headache and one-day history of fever (39.4 C) with nausea, vomiting, and somnolence in a previously healthy 12-year-old female. She reported swimming at an outdoor water park seven days prior to symptom onset. Time from symptom onset to hospital presentation: approximately 30 hours.`, onset_to_presentation_d=1.25, red_flags=['fresh_water_exposure_14d']

**Ground truth class:** 1

**Adjudication anchoring_documentation:**

> Anchored to Linam WM et al. Pediatrics 2015 (PMID 25667249). Demographics: 12 years female, Arkansas, US. Stage metadata: clinical_stage=late, exposure_certainty=definite, diagnostic_confirmation=PCR (CDC reference laboratory CSF Naegleria fowleri), outcome=survived. CSF and imaging within published case ranges; vitals imputed from PAM presentation patterns documented in CDC PAM case reviews.

**Provenance inclusion_decision_rationale:**

> Day 2 vignette 25 of 60 (v21-v60 set) for Subphase 1.2 PAM corpus. Cluster: splash_pad. Atypical type: kali_hardig_survivor. Outcome: survived. Anchored to PMID 25667249 (Linam WM et al., Pediatrics 2015). Sub-fields populated from published case where available; vitals and partial labs IMPUTED_FROM_LITERATURE consistent with late-stage PAM clinical patterns documented in CDC PAM case reviews. Treatment per CDC six-drug protocol (amphotericin B, miltefosine, dexamethasone, fluconazole, azithromycin, rifampin) with hypothermia and intracranial pressure management; survived to hospital discharge. Citation caveat: 12yo F (Kali Hardig); Willow Springs Water Park Arkansas July 2013; SURVIVED with combination antimicrobials (including miltefosine) + therapeutic hypothermia + ICP management on TBI principles; THIRD documented North American PAM survivor. 8 authors; preserve lowercase 'da' particle in 'da Silva AJ' per PubMed XML. Definitive case report subsequently invoked by Linam-Cope le...

---

### Vignette 15 — `pam_d2_035_anjum_florida_reuse_a.json`

**case_id:** PAM-D2-035-IDCases-2021-Florida-Lake-Pond

**Demographics:** age=10, sex=male, ethnicity=white_non_hispanic, geography=us_south, altitude_residence_m=100

**Exposure:** type=`lake`, within_14d=True, immunocomp=none, hiv=negative

**Literature anchors:** PMID 34307045 (case_report; DOI 10.1016/j.idcr.2021.e01208)

**CSF:** WBC=4260 /mm³, neut%=91, lymph%=8, glucose=16 mg/dL, protein=418 mg/dL, RBC=220 /mm³, opening_pressure=38.0 cmH₂O, wet_mount_motile=positive, crag_lfa=negative, lactate=7.4 mmol/L, ADA=None U/L

**Vitals:** temp=39.6°C, HR=128, RR=24, SBP/DBP=104/64, SpO₂=95%, GCS=7

**Exam:** neck_stiffness=True, kernig_brudzinski=True, mental_status_grade=stuporous, cranial_nerve_palsy=none, focal_neuro=True, papilledema=True, petechial_rash=False

**History:** chief=`altered_mental_status`, prodrome=`stupor with focal deficit and papilledema`, onset_to_presentation_d=4.0, red_flags=['fresh_water_exposure_14d']

**Ground truth class:** 1

**Adjudication anchoring_documentation:**

> Anchored to Anjum SK et al. IDCases 2021 (PMID 34307045). Demographics: 10 years male, Florida, US. Stage metadata: clinical_stage=late, exposure_certainty=definite, diagnostic_confirmation=PCR (CDC reference laboratory CSF Naegleria fowleri), outcome=fatal. CSF and imaging within published case ranges; vitals imputed from PAM presentation patterns documented in CDC PAM case reviews.

**Provenance inclusion_decision_rationale:**

> Day 2 vignette 35 of 60 (v21-v60 set) for Subphase 1.2 PAM corpus. Cluster: lake_pond. Atypical type: none. Outcome: fatal. Anchored to PMID 34307045 (Anjum SK et al., IDCases 2021). Sub-fields populated from published case where available; vitals and partial labs IMPUTED_FROM_LITERATURE consistent with late-stage PAM clinical patterns documented in CDC PAM case reviews. Treatment per CDC six-drug protocol (amphotericin B, miltefosine, dexamethasone, fluconazole, azithromycin, rifampin); fatal outcome despite full regimen. Citation caveat: US tap-water-associated PAM 2020s. Pairs with USVI ablution case (PMID 24226628) for tap-water transmission cluster adjudication. 11 authors confirmed (Saccoccio FM at end). DOI is e01208 (NOT e01218). Author 8 'O'Laughlin K' preserves apostrophe. Author 6 'Ibne Karim M Ali' renders as Vancouver 'Ali IKM' (3 initials). Authors: Saad K Anjum, Karna Mangrola, Garrett Fitzpatrick, Kimberly Stockdale, Laura Matthias, Ibne Karim M Ali, Jennifer R Cope,...

---

### Vignette 16 — `pam_d2_036_anjum_florida_reuse_b.json`

**case_id:** PAM-D2-036-IDCases-2021-Florida-Lake-Pond

**Demographics:** age=12, sex=female, ethnicity=white_non_hispanic, geography=us_south, altitude_residence_m=100

**Exposure:** type=`lake`, within_14d=True, immunocomp=none, hiv=negative

**Literature anchors:** PMID 34307045 (case_report; DOI 10.1016/j.idcr.2021.e01208)

**CSF:** WBC=3080 /mm³, neut%=91, lymph%=8, glucose=21 mg/dL, protein=356 mg/dL, RBC=220 /mm³, opening_pressure=28.0 cmH₂O, wet_mount_motile=not_done, crag_lfa=negative, lactate=7.4 mmol/L, ADA=None U/L

**Vitals:** temp=39.6°C, HR=116, RR=22, SBP/DBP=110/68, SpO₂=95%, GCS=11

**Exam:** neck_stiffness=True, kernig_brudzinski=True, mental_status_grade=somnolent, cranial_nerve_palsy=none, focal_neuro=False, papilledema=False, petechial_rash=False

**History:** chief=`fever_with_headache`, prodrome=`somnolence with neck stiffness`, onset_to_presentation_d=4.0, red_flags=['fresh_water_exposure_14d']

**Ground truth class:** 1

**Adjudication anchoring_documentation:**

> Anchored to Anjum SK et al. IDCases 2021 (PMID 34307045). Demographics: 12 years female, Florida, US. Stage metadata: clinical_stage=mid, exposure_certainty=definite, diagnostic_confirmation=PCR (CDC reference laboratory CSF Naegleria fowleri), outcome=fatal. CSF and imaging within published case ranges; vitals imputed from PAM presentation patterns documented in CDC PAM case reviews.

**Provenance inclusion_decision_rationale:**

> Day 2 vignette 36 of 60 (v21-v60 set) for Subphase 1.2 PAM corpus. Cluster: lake_pond. Atypical type: none. Outcome: fatal. Anchored to PMID 34307045 (Anjum SK et al., IDCases 2021). Sub-fields populated from published case where available; vitals and partial labs IMPUTED_FROM_LITERATURE consistent with mid-stage PAM clinical patterns documented in CDC PAM case reviews. Treatment per CDC six-drug protocol (amphotericin B, miltefosine, dexamethasone, fluconazole, azithromycin, rifampin); fatal outcome despite full regimen. Citation caveat: US tap-water-associated PAM 2020s. Pairs with USVI ablution case (PMID 24226628) for tap-water transmission cluster adjudication. 11 authors confirmed (Saccoccio FM at end). DOI is e01208 (NOT e01218). Author 8 'O'Laughlin K' preserves apostrophe. Author 6 'Ibne Karim M Ali' renders as Vancouver 'Ali IKM' (3 initials). Authors: Saad K Anjum, Karna Mangrola, Garrett Fitzpatrick, Kimberly Stockdale, Laura Matthias, Ibne Karim M Ali, Jennifer R Cope, ...

---

### Vignette 17 — `pam_d2_037_anjum_florida_reuse_c.json`

**case_id:** PAM-D2-037-IDCases-2021-Florida-Lake-Pond

**Demographics:** age=15, sex=male, ethnicity=white_non_hispanic, geography=us_south, altitude_residence_m=100

**Exposure:** type=`lake`, within_14d=True, immunocomp=none, hiv=negative

**Literature anchors:** PMID 34307045 (case_report; DOI 10.1016/j.idcr.2021.e01208)

**CSF:** WBC=4640 /mm³, neut%=91, lymph%=8, glucose=13 mg/dL, protein=458 mg/dL, RBC=220 /mm³, opening_pressure=38.0 cmH₂O, wet_mount_motile=positive, crag_lfa=negative, lactate=7.4 mmol/L, ADA=None U/L

**Vitals:** temp=39.6°C, HR=116, RR=22, SBP/DBP=110/68, SpO₂=95%, GCS=7

**Exam:** neck_stiffness=True, kernig_brudzinski=True, mental_status_grade=stuporous, cranial_nerve_palsy=none, focal_neuro=True, papilledema=True, petechial_rash=False

**History:** chief=`altered_mental_status`, prodrome=`rapid neurological deterioration to stupor`, onset_to_presentation_d=4.0, red_flags=['fresh_water_exposure_14d']

**Ground truth class:** 1

**Adjudication anchoring_documentation:**

> Anchored to Anjum SK et al. IDCases 2021 (PMID 34307045). Demographics: 15 years male, Florida, US. Stage metadata: clinical_stage=late, exposure_certainty=definite, diagnostic_confirmation=PCR (CDC reference laboratory CSF Naegleria fowleri), outcome=fatal. CSF and imaging within published case ranges; vitals imputed from PAM presentation patterns documented in CDC PAM case reviews.

**Provenance inclusion_decision_rationale:**

> Day 2 vignette 37 of 60 (v21-v60 set) for Subphase 1.2 PAM corpus. Cluster: lake_pond. Atypical type: none. Outcome: fatal. Anchored to PMID 34307045 (Anjum SK et al., IDCases 2021). Sub-fields populated from published case where available; vitals and partial labs IMPUTED_FROM_LITERATURE consistent with late-stage PAM clinical patterns documented in CDC PAM case reviews. Treatment per CDC six-drug protocol (amphotericin B, miltefosine, dexamethasone, fluconazole, azithromycin, rifampin); fatal outcome despite full regimen. Citation caveat: US tap-water-associated PAM 2020s. Pairs with USVI ablution case (PMID 24226628) for tap-water transmission cluster adjudication. 11 authors confirmed (Saccoccio FM at end). DOI is e01208 (NOT e01218). Author 8 'O'Laughlin K' preserves apostrophe. Author 6 'Ibne Karim M Ali' renders as Vancouver 'Ali IKM' (3 initials). Authors: Saad K Anjum, Karna Mangrola, Garrett Fitzpatrick, Kimberly Stockdale, Laura Matthias, Ibne Karim M Ali, Jennifer R Cope,...

---

### Vignette 18 — `pam_d2_040_yoder2010_us_review_imputed.json`

**case_id:** PAM-D2-040-EpidemiolInfect-2010-US-South-region-Lake-Pond

**Demographics:** age=14, sex=male, ethnicity=white_non_hispanic, geography=us_south, altitude_residence_m=100

**Exposure:** type=`lake`, within_14d=True, immunocomp=none, hiv=negative

**Literature anchors:** PMID 19845995 (review; DOI 10.1017/S0950268809991014)

**CSF:** WBC=2800 /mm³, neut%=89, lymph%=10, glucose=22 mg/dL, protein=340 mg/dL, RBC=160 /mm³, opening_pressure=30.0 cmH₂O, wet_mount_motile=not_done, crag_lfa=negative, lactate=6.6 mmol/L, ADA=None U/L

**Vitals:** temp=39.2°C, HR=116, RR=22, SBP/DBP=110/68, SpO₂=96%, GCS=11

**Exam:** neck_stiffness=True, kernig_brudzinski=True, mental_status_grade=somnolent, cranial_nerve_palsy=none, focal_neuro=False, papilledema=False, petechial_rash=False

**History:** chief=`fever_with_headache`, prodrome=`Five-day history of fever, headache, and progressive somnolence in a 14-year-old male from the US South region after recreational freshwater (lake) exposure. Demographics imputed within Yoder 2010 foundational US 1962-2008 PAM surveillance review.`, onset_to_presentation_d=5.0, red_flags=['fresh_water_exposure_14d']

**Ground truth class:** 1

**Adjudication anchoring_documentation:**

> Anchored to Yoder et al. Epidemiol Infect 2010 (PMID 19845995). Demographics: 14 years male, US South region. Stage metadata: clinical_stage=mid, exposure_certainty=definite, diagnostic_confirmation=PCR (CDC reference laboratory CSF Naegleria fowleri), outcome=fatal. CSF and imaging within published case ranges; vitals imputed from PAM presentation patterns documented in CDC PAM case reviews.

**Provenance inclusion_decision_rationale:**

> Day 2 vignette 40 of 60 (v21-v60 set) for Subphase 1.2 PAM corpus. Cluster: lake_pond. Atypical type: none. Outcome: fatal. Anchored to PMID 19845995 (Yoder et al., Epidemiol Infect 2010). Sub-fields populated from published case where available; vitals and partial labs IMPUTED_FROM_LITERATURE consistent with mid-stage PAM clinical patterns documented in CDC PAM case reviews. Treatment per CDC six-drug protocol (amphotericin B, miltefosine, dexamethasone, fluconazole, azithromycin, rifampin); fatal outcome despite full regimen. Citation caveat: Foundational US PAM surveillance covering 111 cases 1962-2008.

---

### Vignette 19 — `pam_d2_053_yoder2012_louisiana_reuse_a.json`

**case_id:** PAM-D2-053-CID-2012-Louisiana-Nasal-Irrigation

**Demographics:** age=35, sex=male, ethnicity=white_non_hispanic, geography=us_south, altitude_residence_m=100

**Exposure:** type=`neti_pot_tap_water`, within_14d=True, immunocomp=none, hiv=negative

**Literature anchors:** PMID 22919000 (case_report; DOI 10.1093/cid/cis626)

**CSF:** WBC=2940 /mm³, neut%=89, lymph%=10, glucose=22 mg/dL, protein=348 mg/dL, RBC=180 /mm³, opening_pressure=28.0 cmH₂O, wet_mount_motile=not_done, crag_lfa=negative, lactate=6.6 mmol/L, ADA=None U/L

**Vitals:** temp=39.0°C, HR=110, RR=20, SBP/DBP=124/78, SpO₂=96%, GCS=10

**Exam:** neck_stiffness=True, kernig_brudzinski=True, mental_status_grade=confused, cranial_nerve_palsy=none, focal_neuro=False, papilledema=False, petechial_rash=False

**History:** chief=`fever_with_headache`, prodrome=`Five days of fever, frontal headache, nasal congestion, and progressive somnolence in a 35-year-old man from Louisiana with daily neti-pot use of municipal tap water for chronic sinus symptoms over the prior month.`, onset_to_presentation_d=5.0, red_flags=['fresh_water_exposure_14d']

**Ground truth class:** 1

**Adjudication anchoring_documentation:**

> methodology=day1_pmid_reuse; Anchored to Yoder JS et al. Clin Infect Dis 2012 (PMID 22919000). Demographics: 35 years male, Louisiana, US. Stage metadata: clinical_stage=mid, exposure_certainty=definite, diagnostic_confirmation=PCR (CDC reference laboratory CSF Naegleria fowleri), outcome=fatal. CSF and imaging within published case ranges; vitals imputed from PAM presentation patterns documented in CDC PAM case reviews.

**Provenance inclusion_decision_rationale:**

> Day 2 vignette 53 of 60 (v21-v60 set) for Subphase 1.2 PAM corpus. Cluster: nasal_irrigation. Atypical type: none. Outcome: fatal. Anchored to PMID 22919000 (Yoder JS et al., Clin Infect Dis 2012). Sub-fields populated from published case where available; vitals and partial labs IMPUTED_FROM_LITERATURE consistent with mid-stage PAM clinical patterns documented in CDC PAM case reviews. Treatment per CDC six-drug protocol (amphotericin B, miltefosine, dexamethasone, fluconazole, azithromycin, rifampin); fatal outcome despite full regimen. Citation caveat: PMC11307261 is an NIHMS author-manuscript deposit posted retroactively (2024) for the 2012 paper. Publisher of record is Clin Infect Dis 2012;55(9):e79-e85, DOI 10.1093/cid/cis626.

---

### Vignette 20 — `pam_d2_054_yoder2012_louisiana_reuse_b.json`

**case_id:** PAM-D2-054-CID-2012-Louisiana-Nasal-Irrigation

**Demographics:** age=62, sex=female, ethnicity=white_non_hispanic, geography=us_south, altitude_residence_m=100

**Exposure:** type=`neti_pot_tap_water`, within_14d=True, immunocomp=none, hiv=negative

**Literature anchors:** PMID 22919000 (case_report; DOI 10.1093/cid/cis626)

**CSF:** WBC=4480 /mm³, neut%=92, lymph%=7, glucose=14 mg/dL, protein=446 mg/dL, RBC=260 /mm³, opening_pressure=38.0 cmH₂O, wet_mount_motile=positive, crag_lfa=negative, lactate=8.4 mmol/L, ADA=None U/L

**Vitals:** temp=39.3°C, HR=104, RR=22, SBP/DBP=130/80, SpO₂=95%, GCS=6

**Exam:** neck_stiffness=True, kernig_brudzinski=True, mental_status_grade=stuporous, cranial_nerve_palsy=none, focal_neuro=True, papilledema=True, petechial_rash=False

**History:** chief=`altered_mental_status`, prodrome=`Four days of fever, frontal headache, nasal congestion, and rapid progression to stupor in a 62-year-old woman from Louisiana with several weeks of daily neti-pot tap-water rinses for post-COVID sinus symptoms.`, onset_to_presentation_d=4.0, red_flags=['fresh_water_exposure_14d']

**Ground truth class:** 1

**Adjudication anchoring_documentation:**

> methodology=day1_pmid_reuse; Anchored to Yoder JS et al. Clin Infect Dis 2012 (PMID 22919000). Demographics: 62 years female, Louisiana, US. Stage metadata: clinical_stage=late, exposure_certainty=definite, diagnostic_confirmation=PCR (CDC reference laboratory CSF Naegleria fowleri), outcome=fatal. CSF and imaging within published case ranges; vitals imputed from PAM presentation patterns documented in CDC PAM case reviews.

**Provenance inclusion_decision_rationale:**

> Day 2 vignette 54 of 60 (v21-v60 set) for Subphase 1.2 PAM corpus. Cluster: nasal_irrigation. Atypical type: none. Outcome: fatal. Anchored to PMID 22919000 (Yoder JS et al., Clin Infect Dis 2012). Sub-fields populated from published case where available; vitals and partial labs IMPUTED_FROM_LITERATURE consistent with late-stage PAM clinical patterns documented in CDC PAM case reviews. Treatment per CDC six-drug protocol (amphotericin B, miltefosine, dexamethasone, fluconazole, azithromycin, rifampin); fatal outcome despite full regimen. Citation caveat: PMC11307261 is an NIHMS author-manuscript deposit posted retroactively (2024) for the 2012 paper. Publisher of record is Clin Infect Dis 2012;55(9):e79-e85, DOI 10.1093/cid/cis626.

---

### Vignette 21 — `pam_d2_055_smith_texas_rv_reuse.json`

**case_id:** PAM-D2-055-MMWR-2025-Texas-Nasal-Irrigation

**Demographics:** age=45, sex=male, ethnicity=white_non_hispanic, geography=us_south, altitude_residence_m=100

**Exposure:** type=`neti_pot_tap_water`, within_14d=True, immunocomp=none, hiv=negative

**Literature anchors:** PMID 40440212 (surveillance; DOI None)

**CSF:** WBC=3000 /mm³, neut%=90, lymph%=9, glucose=21 mg/dL, protein=354 mg/dL, RBC=180 /mm³, opening_pressure=28.0 cmH₂O, wet_mount_motile=not_done, crag_lfa=negative, lactate=6.8 mmol/L, ADA=None U/L

**Vitals:** temp=39.1°C, HR=108, RR=20, SBP/DBP=128/78, SpO₂=96%, GCS=11

**Exam:** neck_stiffness=True, kernig_brudzinski=True, mental_status_grade=somnolent, cranial_nerve_palsy=none, focal_neuro=False, papilledema=False, petechial_rash=False

**History:** chief=`fever_with_headache`, prodrome=`Five days of fever, frontal headache, nasal congestion, and progressive somnolence in a 45-year-old man from Texas with daily neti-pot use of recreational vehicle water-tank tap water during a multi-week travel trip.`, onset_to_presentation_d=5.0, red_flags=['fresh_water_exposure_14d']

**Ground truth class:** 1

**Adjudication anchoring_documentation:**

> methodology=day1_pmid_reuse; Anchored to Smith et al. MMWR Morb Mortal Wkly Rep 2025 (PMID 40440212). Demographics: 45 years male, Texas, US. Stage metadata: clinical_stage=mid, exposure_certainty=definite, diagnostic_confirmation=PCR (CDC reference laboratory CSF Naegleria fowleri), outcome=fatal. CSF and imaging within published case ranges; vitals imputed from PAM presentation patterns documented in CDC PAM case reviews.

**Provenance inclusion_decision_rationale:**

> Day 2 vignette 55 of 60 (v21-v60 set) for Subphase 1.2 PAM corpus. Cluster: nasal_irrigation. Atypical type: none. Outcome: fatal. Anchored to PMID 40440212 (Smith et al., MMWR Morb Mortal Wkly Rep 2025). Sub-fields populated from published case where available; vitals and partial labs IMPUTED_FROM_LITERATURE consistent with mid-stage PAM clinical patterns documented in CDC PAM case reviews. Treatment per CDC six-drug protocol (amphotericin B, miltefosine, dexamethasone, fluconazole, azithromycin, rifampin); fatal outcome despite full regimen. Citation caveat: 5-pass verified 14 authors (NOT 13). Kunz J added as author #14 (corresponding author). Citation: MMWR 74(19):334-335.

---

### Vignette 22 — `pam_d2_056_cope_louisiana_treated_tap.json`

**case_id:** PAM-D2-056-CID-2015-Louisiana-Nasal-Irrigation

**Demographics:** age=40, sex=male, ethnicity=white_non_hispanic, geography=us_south, altitude_residence_m=100

**Exposure:** type=`neti_pot_tap_water`, within_14d=True, immunocomp=none, hiv=negative

**Literature anchors:** PMID 25595746 (case_report; DOI 10.1093/cid/ciu936)

**CSF:** WBC=3120 /mm³, neut%=91, lymph%=8, glucose=20 mg/dL, protein=366 mg/dL, RBC=200 /mm³, opening_pressure=28.0 cmH₂O, wet_mount_motile=not_done, crag_lfa=negative, lactate=7.0 mmol/L, ADA=None U/L

**Vitals:** temp=39.0°C, HR=110, RR=20, SBP/DBP=122/76, SpO₂=96%, GCS=9

**Exam:** neck_stiffness=True, kernig_brudzinski=True, mental_status_grade=confused, cranial_nerve_palsy=none, focal_neuro=False, papilledema=False, petechial_rash=False

**History:** chief=`fever_with_headache`, prodrome=`Five days of fever, frontal headache, nasal congestion, and progressive somnolence in a 40-year-old man from southern Louisiana with daily nasal-rinse use of treated municipal tap water for chronic sinusitis.`, onset_to_presentation_d=5.0, red_flags=['fresh_water_exposure_14d']

**Ground truth class:** 1

**Adjudication anchoring_documentation:**

> methodology=primary_source_direct; Anchored to Cope et al. Clin Infect Dis 2015 (PMID 25595746). Demographics: 40 years male, Louisiana, US. Stage metadata: clinical_stage=mid, exposure_certainty=definite, diagnostic_confirmation=PCR (CDC reference laboratory CSF Naegleria fowleri), outcome=fatal. CSF and imaging within published case ranges; vitals imputed from PAM presentation patterns documented in CDC PAM case reviews.

**Provenance inclusion_decision_rationale:**

> Day 2 vignette 56 of 60 (v21-v60 set) for Subphase 1.2 PAM corpus. Cluster: nasal_irrigation. Atypical type: treated_tap_water. Outcome: fatal. Anchored to PMID 25595746 (Cope et al., Clin Infect Dis 2015). Sub-fields populated from published case where available; vitals and partial labs IMPUTED_FROM_LITERATURE consistent with mid-stage PAM clinical patterns documented in CDC PAM case reviews. Treatment per CDC six-drug protocol (amphotericin B, miltefosine, dexamethasone, fluconazole, azithromycin, rifampin); fatal outcome despite full regimen. Citation caveat: First reported PAM case associated with culturable N. fowleri in treated US tap water (Louisiana 2013). PMC ID confirmed PMC4627687 (NOT PMC4622028, which was the prior misattribution to Capewell 2015).

---

### Vignette 23 — `pam_d2_057_gharpure_eid_imputed_neti.json`

**case_id:** PAM-D2-057-EID-2021-US-South-region-Nasal-Irrigation

**Demographics:** age=38, sex=male, ethnicity=white_non_hispanic, geography=us_south, altitude_residence_m=100

**Exposure:** type=`neti_pot_tap_water`, within_14d=True, immunocomp=none, hiv=negative

**Literature anchors:** PMID 33350926 (review; DOI 10.3201/eid2701.202119)

**CSF:** WBC=2180 /mm³, neut%=89, lymph%=10, glucose=28 mg/dL, protein=242 mg/dL, RBC=160 /mm³, opening_pressure=26.0 cmH₂O, wet_mount_motile=not_done, crag_lfa=negative, lactate=5.2 mmol/L, ADA=None U/L

**Vitals:** temp=39.1°C, HR=110, RR=20, SBP/DBP=124/76, SpO₂=96%, GCS=12

**Exam:** neck_stiffness=True, kernig_brudzinski=True, mental_status_grade=somnolent, cranial_nerve_palsy=none, focal_neuro=False, papilledema=False, petechial_rash=False

**History:** chief=`fever_with_headache`, prodrome=`Five days of fever, frontal headache, nasal congestion, and progressive somnolence in a 38-year-old man from the US South region with daily neti-pot tap-water rinses for chronic sinus symptoms. Demographics imputed within Gharpure 2021 EID US 2010-2019 surveillance review (nasal-irrigation sub-bucket).`, onset_to_presentation_d=5.0, red_flags=['fresh_water_exposure_14d']

**Ground truth class:** 1

**Adjudication anchoring_documentation:**

> methodology=tier_4_imputation; Anchored to Gharpure et al. Emerg Infect Dis 2021 (PMID 33350926). Demographics: 38 years male, US South region. Stage metadata: clinical_stage=mid, exposure_certainty=definite, diagnostic_confirmation=PCR (CDC reference laboratory CSF Naegleria fowleri), outcome=fatal. CSF and imaging within published case ranges; vitals imputed from PAM presentation patterns documented in CDC PAM case reviews.

**Provenance inclusion_decision_rationale:**

> Day 2 vignette 57 of 60 (v21-v60 set) for Subphase 1.2 PAM corpus. Cluster: nasal_irrigation. Atypical type: none. Outcome: fatal. Anchored to PMID 33350926 (Gharpure et al., Emerg Infect Dis 2021). Sub-fields populated from published case where available; vitals and partial labs IMPUTED_FROM_LITERATURE consistent with mid-stage PAM clinical patterns documented in CDC PAM case reviews. Treatment per CDC six-drug protocol (amphotericin B, miltefosine, dexamethasone, fluconazole, azithromycin, rifampin); fatal outcome despite full regimen. Citation caveat: First author corrected from Cope to Gharpure. Documents northward range expansion 1978-2018.

---

### Vignette 24 — `pam_d2_058_gharpure_cid_imputed_neti.json`

**case_id:** PAM-D2-058-CID-2021-US-South-region-Nasal-Irrigation

**Demographics:** age=50, sex=male, ethnicity=white_non_hispanic, geography=us_south, altitude_residence_m=100

**Exposure:** type=`neti_pot_tap_water`, within_14d=True, immunocomp=none, hiv=negative

**Literature anchors:** PMID 32369575 (review; DOI 10.1093/cid/ciaa520)

**CSF:** WBC=4580 /mm³, neut%=92, lymph%=7, glucose=12 mg/dL, protein=468 mg/dL, RBC=280 /mm³, opening_pressure=38.0 cmH₂O, wet_mount_motile=positive, crag_lfa=negative, lactate=8.8 mmol/L, ADA=None U/L

**Vitals:** temp=39.4°C, HR=106, RR=22, SBP/DBP=132/80, SpO₂=95%, GCS=7

**Exam:** neck_stiffness=True, kernig_brudzinski=True, mental_status_grade=stuporous, cranial_nerve_palsy=none, focal_neuro=True, papilledema=True, petechial_rash=False

**History:** chief=`altered_mental_status`, prodrome=`Four days of fever, frontal headache, nasal congestion, and rapid progression to stupor in a 50-year-old man from the US South region with daily neti-pot tap-water rinses for chronic sinus symptoms. Demographics imputed within Gharpure 2021 CID global review (nasal-irrigation sub-bucket).`, onset_to_presentation_d=4.0, red_flags=['fresh_water_exposure_14d']

**Ground truth class:** 1

**Adjudication anchoring_documentation:**

> methodology=tier_4_imputation; Anchored to Gharpure et al. Clin Infect Dis 2021 (PMID 32369575). Demographics: 50 years male, US South region. Stage metadata: clinical_stage=late, exposure_certainty=definite, diagnostic_confirmation=PCR (CDC reference laboratory CSF Naegleria fowleri), outcome=fatal. CSF and imaging within published case ranges; vitals imputed from PAM presentation patterns documented in CDC PAM case reviews.

**Provenance inclusion_decision_rationale:**

> Day 2 vignette 58 of 60 (v21-v60 set) for Subphase 1.2 PAM corpus. Cluster: nasal_irrigation. Atypical type: none. Outcome: fatal. Anchored to PMID 32369575 (Gharpure et al., Clin Infect Dis 2021). Sub-fields populated from published case where available; vitals and partial labs IMPUTED_FROM_LITERATURE consistent with late-stage PAM clinical patterns documented in CDC PAM case reviews. Treatment per CDC six-drug protocol (amphotericin B, miltefosine, dexamethasone, fluconazole, azithromycin, rifampin); fatal outcome despite full regimen. Citation caveat: Global PAM review, 381 cases 1937-2018, US 41% / Pakistan 11% / Mexico 9%. Companion to Capewell 2015 (US-only).

---

### Vignette 25 — `pam_d2_059_sandi_costa_rica_reuse.json`

**case_id:** PAM-D2-059-EID-2015-Florida-(acquired-Costa-Rica)-Hot-Springs

**Demographics:** age=8, sex=female, ethnicity=other, geography=other_latam, altitude_residence_m=100

**Exposure:** type=`hot_spring`, within_14d=True, immunocomp=none, hiv=negative

**Literature anchors:** PMID 25625800 (case_report; DOI None)

**CSF:** WBC=3160 /mm³, neut%=90, lymph%=9, glucose=21 mg/dL, protein=364 mg/dL, RBC=200 /mm³, opening_pressure=28.0 cmH₂O, wet_mount_motile=not_done, crag_lfa=negative, lactate=6.8 mmol/L, ADA=None U/L

**Vitals:** temp=39.3°C, HR=130, RR=26, SBP/DBP=100/60, SpO₂=96%, GCS=11

**Exam:** neck_stiffness=True, kernig_brudzinski=True, mental_status_grade=somnolent, cranial_nerve_palsy=none, focal_neuro=False, papilledema=False, petechial_rash=False

**History:** chief=`fever_with_headache`, prodrome=`Four days of fever, frontal headache, vomiting, and progressive somnolence in an 8-year-old girl who returned to Florida from a family vacation in Costa Rica that included repeated bathing in natural hot-springs pools roughly ten days before symptom onset.`, onset_to_presentation_d=4.0, red_flags=['fresh_water_exposure_14d']

**Ground truth class:** 1

**Adjudication anchoring_documentation:**

> methodology=day1_pmid_reuse; Anchored to Abrahams-Sandí E et al. Emerg Infect Dis 2015 (PMID 25625800). Demographics: 8 years female, Florida (acquired Costa Rica). Stage metadata: clinical_stage=mid, exposure_certainty=definite, diagnostic_confirmation=PCR (CDC reference laboratory CSF Naegleria fowleri), outcome=fatal. CSF and imaging within published case ranges; vitals imputed from PAM presentation patterns documented in CDC PAM case reviews.

**Provenance inclusion_decision_rationale:**

> Day 2 vignette 59 of 60 (v21-v60 set) for Subphase 1.2 PAM corpus. Cluster: hot_springs. Atypical type: costa_rica_traveler_family. Outcome: fatal. Anchored to PMID 25625800 (Abrahams-Sandí E et al., Emerg Infect Dis 2015). Sub-fields populated from published case where available; vitals and partial labs IMPUTED_FROM_LITERATURE consistent with mid-stage PAM clinical patterns documented in CDC PAM case reviews. Treatment per CDC six-drug protocol (amphotericin B, miltefosine, dexamethasone, fluconazole, azithromycin, rifampin); fatal outcome despite full regimen. Citation caveat: Used as LATAM substitute; no Peru-specific PAM PMID exists. Diacritic on Sandí preserved per 5-pass UTF-8 verification.

---

### Vignette 26 — `pam_d2_060_burki_pakistan_survivor_reuse.json`

**case_id:** PAM-D2-060-Emerg Infect Dis-2024-Karachi-Pakistan-Ablution

**Demographics:** age=26, sex=male, ethnicity=other, geography=pakistan_karachi, altitude_residence_m=100

**Exposure:** type=`ritual_ablution_wudu`, within_14d=True, immunocomp=none, hiv=negative

**Literature anchors:** PMID 38526236 (case_report; DOI 10.3201/eid3004.230979)

**CSF:** WBC=1860 /mm³, neut%=88, lymph%=10, glucose=31 mg/dL, protein=198 mg/dL, RBC=180 /mm³, opening_pressure=28.0 cmH₂O, wet_mount_motile=positive, crag_lfa=negative, lactate=5.0 mmol/L, ADA=None U/L

**Vitals:** temp=39.5°C, HR=114, RR=22, SBP/DBP=122/74, SpO₂=96%, GCS=12

**Exam:** neck_stiffness=True, kernig_brudzinski=True, mental_status_grade=somnolent, cranial_nerve_palsy=none, focal_neuro=False, papilledema=False, petechial_rash=False

**History:** chief=`fever_with_headache`, prodrome=`Three days of fever, severe headache, photophobia, vomiting, and progressive somnolence in a 26-year-old man from Karachi performing daily ritual ablution (wudu) with municipal tap water; family recognition of early decline prompted emergency department arrival within hours of mental-status change.`, onset_to_presentation_d=4.0, red_flags=['fresh_water_exposure_14d']

**Ground truth class:** 1

**Adjudication anchoring_documentation:**

> methodology=day1_pmid_reuse; Anchored to Burki AMK et al. Emerging Infectious Diseases 2024 (PMID 38526236). Demographics: 26 years male, Karachi, PK. Stage metadata: clinical_stage=mid, exposure_certainty=definite, diagnostic_confirmation=PCR (CDC reference laboratory CSF Naegleria fowleri), outcome=survived. CSF and imaging within published case ranges; vitals imputed from PAM presentation patterns documented in CDC PAM case reviews.

**Provenance inclusion_decision_rationale:**

> Day 2 vignette 60 of 60 (v21-v60 set) for Subphase 1.2 PAM corpus. Cluster: pakistan_ablution. Atypical type: adult_survivor_ablution. Outcome: survived. Anchored to PMID 38526236 (Burki AMK et al., Emerging Infectious Diseases 2024). Sub-fields populated from published case where available; vitals and partial labs IMPUTED_FROM_LITERATURE consistent with mid-stage PAM clinical patterns documented in CDC PAM case reviews. Treatment per CDC six-drug protocol (amphotericin B, miltefosine, dexamethasone, fluconazole, azithromycin, rifampin) with hypothermia and intracranial pressure management; survived to hospital discharge. Citation caveat: 22yo M Pakistan 2023, 8th confirmed N. fowleri SURVIVOR globally (1971-2023). PNS Shifa Hospital Karachi. Pairs naturally with Linam 2015 Kali Hardig (PMID 25667249) for outcome-contrast adjudication. Co-author Ghanchi NK also first author of PMID 27648572 (2016 EID Pakistan public water supply). Authors: Ahmed Mujadid Khan Burki, Luqman Satti, Sai...

---

## Extraction stats

- Vignettes extracted: 26
- Source directory: `data/vignettes/pam/`
- Extraction method: Python json.load + structured field pull (replaced earlier jq attempt that hit parenthesis-balancing issues)
- Cross-check phase: PENDING (Claude to verify each vignette vs paper truth, flag scope-fit, log errata)

## Status statement

**READ-ONLY**: No vignette JSON files were modified during this extraction. The audit doc is the sole new artifact created.

**Cross-check pending**: Per established Sub-Bundle audit protocol, Claude will follow up with:
1. Scope-fit classification per vignette (Sub-Bundle 04 / different sub-bundle / out of scope)
2. Anchor-paper truth comparison (CSF values, demographics, outcome, treatment vs source paper)
3. Cross-vignette pattern detection (duplicate templates, copy-paste errors)
4. Filename flag verification (imputed_/reuse_/plain)
5. Errata logging to `AUDIT_PAM_vignette_errata_running.md` (currently at 20 ERR entries)
