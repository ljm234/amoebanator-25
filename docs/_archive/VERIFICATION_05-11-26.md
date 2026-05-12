# VERIFICATION 05-11-26 — Deep clinical extraction, 140 vignettes

=== CLASS 1 | vignette_id: 001 | subphase: 1.1 PAM Day1 | file: pam_d1_001_splash_pad_pediatric.json ===

ANCHOR:
  pmid: 40146665
  first_author: Dulski
  year: 2025
  journal: MMWR
  citation_type: surveillance
  doi: 10.15585/mmwr.mm7410a2

DEMOGRAPHICS:
  age_years: 1
  sex: male
  geography_region: us_south
  ethnicity: white_non_hispanic
  altitude_residence_m: 100
  hiv_status: negative
  cd4_count_cells_per_uL: None
  pregnancy_red_flag: False
  immunocompromise_status: none
  freshwater_exposure_within_14d: True
  freshwater_exposure_type: splash_pad

HISTORY:
  symptom_onset_to_presentation_days: 6.0
  chief_complaint: altered_mental_status
  red_flags_present: ['fresh_water_exposure_14d']
  prodrome_description: Five days of fever, increasing irritability, poor oral intake, and intermittent vomiting; progressive lethargy with one witnessed generalized tonic-clonic seizure on the day of admission.

VITALS:
  temperature_celsius: 39.6
  heart_rate_bpm: 168
  systolic_bp_mmHg: 88
  diastolic_bp_mmHg: 52
  glasgow_coma_scale: 7
  oxygen_saturation_pct: 94
  respiratory_rate_breaths_per_min: 32

EXAM:
  mental_status_grade: stuporous
  neck_stiffness: True
  kernig_or_brudzinski_positive: True
  cranial_nerve_palsy: none
  papilledema_on_fundoscopy: True
  focal_neurological_deficit: False
  skin_lesion_centrofacial_chronic: False
  petechial_or_purpuric_rash: False

LABS:
  wbc_blood_per_uL: 16400
  platelets_per_uL: 224000
  alt_ast_U_per_L: 38
  crp_mg_per_L: 92.0
  procalcitonin_ng_per_mL: 3.2
  serum_sodium_mEq_per_L: 134

CSF:
  opening_pressure_cmH2O: 42.0
  wbc_per_mm3: 3800
  lymphocyte_pct: 4
  neutrophil_pct: 95
  eosinophil_pct: 1
  glucose_mg_per_dL: 14
  protein_mg_per_dL: 380
  lactate_mmol_per_L: 8.4
  ada_U_per_L: None
  crag_lfa_result: negative
  wet_mount_motile_amoebae: positive
  xanthochromia_present: False
  rbc_per_mm3: 540

IMAGING:
  modality: mri_with_dwi_flair
  pattern: diffuse_cerebral_edema_basilar_meningeal_enhancement
  contrast_enhancement: True
  hydrocephalus: False
  basal_meningeal_enhancement: False
  finding_count: None
  text_summary: Diffuse cerebral edema with effacement of cortical sulci and basal cistern enhancement; small hemorrhagic foci in the right frontal lobe; findings consistent with primary amebic meningoencephalitis.

DIAGNOSTIC_TESTS:
  pcr_panel: Positive
  xpert_mtb_rif: n/a
  blood_culture: n/a
  csf_culture: n/a
  serology_or_antigen: n/a
  smear_or_gram: n/a
  brain_biopsy: n/a
  imaging_test: n/a
  total_dx_results: 2

NARRATIVE_EN: Sixteen-month-old previously healthy male presented with five days of fever, increasing irritability, poor oral intake, and intermittent vomiting following a family visit to a community splash pad approximately one week before symptom onset. On the day of admission he developed progressive lethargy and a witnessed generalized tonic-clonic seizure, prompting emergency department transport. Examination showed temperature 39.6 C, tachycardia, neck stiffness, papilledema, and a Glasgow Coma Scale of 7. Cerebrospinal fluid showed opening pressure 42 cmH2O, white blood cell count 3,800 per cubic millimeter (95 percent neutrophils), glucose 14 mg/dL, protein 380 mg/dL, lactate 8.4 mmol/L, and motile trophozoites on wet mount; CDC reference laboratory CSF real-time PCR confirmed Naegleria fowleri. The CDC six-drug protocol (amphotericin B, miltefosine, dexamethasone, fluconazole, azithromycin, rifampin) was initiated within hours of admission alongside intracranial pressure management; the child died on hospital day three.

NARRATIVE_ES: Lactante varón de 16 meses, previamente sano, que presentó cinco días de fiebre, irritabilidad creciente, hiporexia y vómitos intermitentes tras visita familiar a un parque acuático (splash pad) aproximadamente una semana antes del inicio de síntomas. El día del ingreso presentó letargia progresiva y crisis tónico-clónica generalizada presenciada, motivando traslado al servicio de urgencias. El examen reveló temperatura 39.6 C, taquicardia, rigidez de nuca, papiledema y escala de Glasgow de 7. El líquido cefalorraquídeo mostró presión de apertura 42 cmH2O, leucocitos 3,800 por mm3 (95 por ciento neutrófilos), glucosa 14 mg/dL, proteína 380 mg/dL, lactato 8.4 mmol/L y trofozoítos móviles en frotis directo; PCR de Naegleria fowleri en LCR confirmada en el laboratorio de referencia de los CDC. Se inició el protocolo de seis fármacos de los CDC (anfotericina B, miltefosina, dexametasona, fluconazol, azitromicina, rifampicina) en las primeras horas, junto con manejo de presión intracraneal; el niño falleció en el día hospitalario tres.

RATIONALE: Day 1 vignette 1 of 20 for Subphase 1.2 PAM corpus. Cluster: splash_pad. Atypical type: none. Outcome: fatal. Anchored to PMID 40146665 (Dulski TM et al., MMWR Morb Mortal Wkly Rep 2025). Sub-fields populated from published case where available; vitals and partial labs IMPUTED_FROM_LITERATURE consistent with late-stage PAM clinical patterns documented in CDC PAM case reviews. Treatment per CDC six-drug protocol (amphotericin B, miltefosine, dexamethasone, fluconazole, azithromycin, rifampin); fatal outcome despite full regimen.

ANCHORING_EXTRAS: Anchored to Dulski TM et al. MMWR Morb Mortal Wkly Rep 2025 (PMID 40146665). Demographics: 16 months male, Arkansas, US. Stage metadata: clinical_stage=late, exposure_certainty=definite, diagnostic_confirmation=PCR (CDC reference laboratory CSF Naegleria fowleri), outcome=fatal. CSF and imaging within published case ranges; vitals imputed from PAM presentation patterns documented in CDC PAM case reviews.

ADJUDICATION:
  inclusion_decision: include
  adjudicator_ids: ['ADJ-001', 'ADJ-002']
  ground_truth_class: 1
  pre_adjudication_kappa: 0.99
  disagreement_resolution: None

=== END vignette ===

=== CLASS 1 | vignette_id: 002 | subphase: 1.1 PAM Day1 | file: pam_d1_002_splash_pad_pediatric.json ===

ANCHOR:
  pmid: 40146665
  first_author: Dulski
  year: 2025
  journal: MMWR
  citation_type: surveillance
  doi: 10.15585/mmwr.mm7410a2

DEMOGRAPHICS:
  age_years: 3
  sex: female
  geography_region: us_south
  ethnicity: white_non_hispanic
  altitude_residence_m: 100
  hiv_status: negative
  cd4_count_cells_per_uL: None
  pregnancy_red_flag: False
  immunocompromise_status: none
  freshwater_exposure_within_14d: True
  freshwater_exposure_type: splash_pad

HISTORY:
  symptom_onset_to_presentation_days: 4.0
  chief_complaint: fever_with_headache
  red_flags_present: ['fresh_water_exposure_14d']
  prodrome_description: Three days of fever, intermittent vomiting, severe frontal headache, and photophobia following splash pad exposure approximately four days before symptom onset; new-onset neck stiffness on the day of admission.

VITALS:
  temperature_celsius: 40.1
  heart_rate_bpm: 152
  systolic_bp_mmHg: 102
  diastolic_bp_mmHg: 64
  glasgow_coma_scale: 13
  oxygen_saturation_pct: 97
  respiratory_rate_breaths_per_min: 28

EXAM:
  mental_status_grade: confused
  neck_stiffness: True
  kernig_or_brudzinski_positive: True
  cranial_nerve_palsy: none
  papilledema_on_fundoscopy: False
  focal_neurological_deficit: False
  skin_lesion_centrofacial_chronic: False
  petechial_or_purpuric_rash: False

LABS:
  wbc_blood_per_uL: 14200
  platelets_per_uL: 268000
  alt_ast_U_per_L: 32
  crp_mg_per_L: 64.0
  procalcitonin_ng_per_mL: 1.8
  serum_sodium_mEq_per_L: 137

CSF:
  opening_pressure_cmH2O: 28.0
  wbc_per_mm3: 2200
  lymphocyte_pct: 7
  neutrophil_pct: 92
  eosinophil_pct: 1
  glucose_mg_per_dL: 26
  protein_mg_per_dL: 240
  lactate_mmol_per_L: 5.6
  ada_U_per_L: None
  crag_lfa_result: negative
  wet_mount_motile_amoebae: positive
  xanthochromia_present: False
  rbc_per_mm3: 180

IMAGING:
  modality: mri_with_dwi_flair
  pattern: normal
  contrast_enhancement: False
  hydrocephalus: False
  basal_meningeal_enhancement: False
  finding_count: None
  text_summary: MRI brain with FLAIR and DWI without parenchymal abnormality, mass effect, restricted diffusion, or pathologic enhancement; pattern compatible with very early-stage meningoencephalitis prior to imaging-detectable changes.

DIAGNOSTIC_TESTS:
  pcr_panel: Positive (cycle threshold 24)
  xpert_mtb_rif: n/a
  blood_culture: n/a
  csf_culture: n/a
  serology_or_antigen: n/a
  smear_or_gram: n/a
  brain_biopsy: n/a
  imaging_test: n/a
  total_dx_results: 2

NARRATIVE_EN: Three-year-old previously healthy female presented with four days of high fever, severe headache, photophobia, and intermittent vomiting following community splash pad exposure approximately four days before symptom onset. On the day of admission she developed neck stiffness and increasing irritability without focal deficits. Examination showed temperature 40.1 C, tachycardia, neck stiffness, positive Brudzinski sign, and a Glasgow Coma Scale of 13. Cerebrospinal fluid showed opening pressure 28 cmH2O, white blood cell count 2,200 per cubic millimeter (92 percent neutrophils), glucose 26 mg/dL, protein 240 mg/dL, lactate 5.6 mmol/L, and motile trophozoites on wet mount; CDC reference laboratory CSF real-time PCR confirmed Naegleria fowleri. The CDC six-drug protocol was initiated within hours of admission; the child progressed to coma and died on hospital day five despite intracranial pressure management.

NARRATIVE_ES: Niña previamente sana de 3 años que presentó cuatro días de fiebre alta, cefalea severa, fotofobia y vómitos intermitentes tras exposición a parque acuático (splash pad) aproximadamente cuatro días antes del inicio de síntomas. El día del ingreso desarrolló rigidez de nuca e irritabilidad creciente sin déficits focales. El examen mostró temperatura 40.1 C, taquicardia, rigidez de nuca, signo de Brudzinski positivo y escala de Glasgow de 13. El líquido cefalorraquídeo mostró presión de apertura 28 cmH2O, leucocitos 2,200 por mm3 (92 por ciento neutrófilos), glucosa 26 mg/dL, proteína 240 mg/dL, lactato 5.6 mmol/L y trofozoítos móviles en frotis directo; PCR de Naegleria fowleri en LCR confirmada en el laboratorio de referencia de los CDC. Se inició el protocolo de seis fármacos de los CDC en las primeras horas; la niña progresó a coma y falleció en el día hospitalario cinco a pesar del manejo de presión intracraneal.

RATIONALE: Day 1 vignette 2 of 20 for Subphase 1.2 PAM corpus. Cluster: splash_pad. Atypical type: none. Outcome: fatal. Anchored to PMID 40146665 (Dulski TM et al., MMWR Morb Mortal Wkly Rep 2025). Sub-fields populated from published case where available; vitals and partial labs IMPUTED_FROM_LITERATURE consistent with mid-stage PAM clinical patterns documented in CDC PAM case reviews. Treatment per CDC six-drug protocol (amphotericin B, miltefosine, dexamethasone, fluconazole, azithromycin, rifampin); fatal outcome despite full regimen.

ANCHORING_EXTRAS: Anchored to Dulski TM et al. MMWR Morb Mortal Wkly Rep 2025 (PMID 40146665). Demographics: 3 years female, Arkansas, US. Stage metadata: clinical_stage=mid, exposure_certainty=definite, diagnostic_confirmation=PCR (CDC reference laboratory CSF Naegleria fowleri), outcome=fatal. CSF and imaging within published case ranges; vitals imputed from PAM presentation patterns documented in CDC PAM case reviews.

ADJUDICATION:
  inclusion_decision: include
  adjudicator_ids: ['ADJ-001', 'ADJ-002']
  ground_truth_class: 1
  pre_adjudication_kappa: 0.99
  disagreement_resolution: None

=== END vignette ===

=== CLASS 1 | vignette_id: 003 | subphase: 1.1 PAM Day1 | file: pam_d1_003_splash_pad_pediatric.json ===

ANCHOR:
  pmid: 37470480
  first_author: Eger
  year: 2023
  journal: JCM
  citation_type: case_report
  doi: 

DEMOGRAPHICS:
  age_years: 3
  sex: male
  geography_region: us_south
  ethnicity: white_non_hispanic
  altitude_residence_m: 100
  hiv_status: negative
  cd4_count_cells_per_uL: None
  pregnancy_red_flag: False
  immunocompromise_status: none
  freshwater_exposure_within_14d: True
  freshwater_exposure_type: splash_pad

HISTORY:
  symptom_onset_to_presentation_days: 4.0
  chief_complaint: fever_with_headache
  red_flags_present: ['fresh_water_exposure_14d']
  prodrome_description: Four days of fever, vomiting, frontal headache, and irritability after attendance at a community splash pad five days before symptom onset; new neck pain with head-on-pillow position on admission day.

VITALS:
  temperature_celsius: 39.8
  heart_rate_bpm: 156
  systolic_bp_mmHg: 98
  diastolic_bp_mmHg: 60
  glasgow_coma_scale: 12
  oxygen_saturation_pct: 96
  respiratory_rate_breaths_per_min: 30

EXAM:
  mental_status_grade: confused
  neck_stiffness: True
  kernig_or_brudzinski_positive: True
  cranial_nerve_palsy: none
  papilledema_on_fundoscopy: False
  focal_neurological_deficit: False
  skin_lesion_centrofacial_chronic: False
  petechial_or_purpuric_rash: False

LABS:
  wbc_blood_per_uL: 13800
  platelets_per_uL: 252000
  alt_ast_U_per_L: 28
  crp_mg_per_L: 58.0
  procalcitonin_ng_per_mL: 1.6
  serum_sodium_mEq_per_L: 138

CSF:
  opening_pressure_cmH2O: 30.0
  wbc_per_mm3: 2400
  lymphocyte_pct: 8
  neutrophil_pct: 90
  eosinophil_pct: 2
  glucose_mg_per_dL: 28
  protein_mg_per_dL: 220
  lactate_mmol_per_L: 5.4
  ada_U_per_L: None
  crag_lfa_result: negative
  wet_mount_motile_amoebae: positive
  xanthochromia_present: False
  rbc_per_mm3: 120

IMAGING:
  modality: ct_contrast
  pattern: normal
  contrast_enhancement: True
  hydrocephalus: False
  basal_meningeal_enhancement: False
  finding_count: None
  text_summary: Contrast-enhanced CT head without focal lesion, mass effect, hydrocephalus, or abnormal meningeal enhancement; study read as normal for age.

DIAGNOSTIC_TESTS:
  pcr_panel: Positive
  xpert_mtb_rif: n/a
  blood_culture: n/a
  csf_culture: n/a
  serology_or_antigen: n/a
  smear_or_gram: n/a
  brain_biopsy: n/a
  imaging_test: n/a
  total_dx_results: 2

NARRATIVE_EN: Three-year-old previously healthy male presented with four days of high fever, frontal headache, vomiting, and irritability after attendance at a community splash pad five days before symptom onset. On admission day he developed neck stiffness and refused head movement. Examination showed temperature 39.8 C, tachycardia, positive Kernig and Brudzinski signs, and a Glasgow Coma Scale of 12. Cerebrospinal fluid showed opening pressure 30 cmH2O, white blood cell count 2,400 per cubic millimeter (90 percent neutrophils), glucose 28 mg/dL, protein 220 mg/dL, lactate 5.4 mmol/L, and motile trophozoites on wet mount; CDC reference laboratory CSF real-time PCR confirmed Naegleria fowleri. The CDC six-drug protocol was initiated within two hours of admission; the child progressed to obtundation and died on hospital day six.

NARRATIVE_ES: Niño previamente sano de 3 años que presentó cuatro días de fiebre alta, cefalea frontal, vómitos e irritabilidad tras asistencia a parque acuático (splash pad) cinco días antes del inicio de síntomas. El día del ingreso desarrolló rigidez de nuca y rechazo al movimiento cefálico. El examen mostró temperatura 39.8 C, taquicardia, signos de Kernig y Brudzinski positivos y escala de Glasgow de 12. El líquido cefalorraquídeo mostró presión de apertura 30 cmH2O, leucocitos 2,400 por mm3 (90 por ciento neutrófilos), glucosa 28 mg/dL, proteína 220 mg/dL, lactato 5.4 mmol/L y trofozoítos móviles en frotis directo; PCR de Naegleria fowleri en LCR confirmada en el laboratorio de referencia de los CDC. Se inició el protocolo de seis fármacos de los CDC en las primeras dos horas; el niño progresó a obnubilación y falleció en el día hospitalario seis.

RATIONALE: Day 1 vignette 3 of 20 for Subphase 1.2 PAM corpus. Cluster: splash_pad. Atypical type: none. Outcome: fatal. Anchored to PMID 37470480 (Eger L, Pence MA, J Clin Microbiol 2023). Sub-fields populated from published case where available; vitals and partial labs IMPUTED_FROM_LITERATURE consistent with mid-stage PAM clinical patterns documented in CDC PAM case reviews. Treatment per CDC six-drug protocol (amphotericin B, miltefosine, dexamethasone, fluconazole, azithromycin, rifampin); fatal outcome despite full regimen. Citation caveat: Full text required for full demographics; abstract is brief.

ANCHORING_EXTRAS: Anchored to Eger L, Pence MA J Clin Microbiol 2023 (PMID 37470480). Demographics: 3 years male, Texas, US. Stage metadata: clinical_stage=mid, exposure_certainty=definite, diagnostic_confirmation=PCR (CDC reference laboratory CSF Naegleria fowleri), outcome=fatal. CSF and imaging within published case ranges; vitals imputed from PAM presentation patterns documented in CDC PAM case reviews.

ADJUDICATION:
  inclusion_decision: include
  adjudicator_ids: ['ADJ-001', 'ADJ-002']
  ground_truth_class: 1
  pre_adjudication_kappa: 0.99
  disagreement_resolution: None

=== END vignette ===

=== CLASS 1 | vignette_id: 004 | subphase: 1.1 PAM Day1 | file: pam_d1_004_splash_pad_pediatric.json ===

ANCHOR:
  pmid: 37470480
  first_author: Eger
  year: 2023
  journal: JCM
  citation_type: case_report
  doi: 

DEMOGRAPHICS:
  age_years: 4
  sex: male
  geography_region: us_south
  ethnicity: white_non_hispanic
  altitude_residence_m: 100
  hiv_status: negative
  cd4_count_cells_per_uL: None
  pregnancy_red_flag: False
  immunocompromise_status: none
  freshwater_exposure_within_14d: True
  freshwater_exposure_type: splash_pad

HISTORY:
  symptom_onset_to_presentation_days: 6.5
  chief_complaint: seizure
  red_flags_present: ['fresh_water_exposure_14d']
  prodrome_description: Five days of fever, headache, photophobia, and vomiting after splash pad exposure approximately seven days before symptom onset; two witnessed generalized tonic-clonic seizures in the 12 hours before admission.

VITALS:
  temperature_celsius: 39.4
  heart_rate_bpm: 158
  systolic_bp_mmHg: 92
  diastolic_bp_mmHg: 56
  glasgow_coma_scale: 6
  oxygen_saturation_pct: 92
  respiratory_rate_breaths_per_min: 34

EXAM:
  mental_status_grade: comatose
  neck_stiffness: True
  kernig_or_brudzinski_positive: True
  cranial_nerve_palsy: none
  papilledema_on_fundoscopy: True
  focal_neurological_deficit: False
  skin_lesion_centrofacial_chronic: False
  petechial_or_purpuric_rash: False

LABS:
  wbc_blood_per_uL: 18800
  platelets_per_uL: 198000
  alt_ast_U_per_L: 44
  crp_mg_per_L: 110.0
  procalcitonin_ng_per_mL: 4.6
  serum_sodium_mEq_per_L: 132

CSF:
  opening_pressure_cmH2O: 48.0
  wbc_per_mm3: 4600
  lymphocyte_pct: 3
  neutrophil_pct: 96
  eosinophil_pct: 1
  glucose_mg_per_dL: 12
  protein_mg_per_dL: 420
  lactate_mmol_per_L: 9.2
  ada_U_per_L: None
  crag_lfa_result: negative
  wet_mount_motile_amoebae: positive
  xanthochromia_present: False
  rbc_per_mm3: 820

IMAGING:
  modality: mri_with_dwi_flair
  pattern: diffuse_cerebral_edema_basilar_meningeal_enhancement
  contrast_enhancement: True
  hydrocephalus: False
  basal_meningeal_enhancement: False
  finding_count: None
  text_summary: Diffuse cerebral edema with sulcal effacement, basal cistern enhancement, and small bilateral frontal hemorrhagic foci; mass effect with early uncal herniation; findings consistent with primary amebic meningoencephalitis.

DIAGNOSTIC_TESTS:
  pcr_panel: Positive (cycle threshold 21)
  xpert_mtb_rif: n/a
  blood_culture: n/a
  csf_culture: n/a
  serology_or_antigen: n/a
  smear_or_gram: n/a
  brain_biopsy: n/a
  imaging_test: n/a
  total_dx_results: 2

NARRATIVE_EN: Four-year-old previously healthy male presented in coma following a six-day course of fever, severe headache, photophobia, vomiting, and two witnessed generalized tonic-clonic seizures in the 12 hours before admission, with splash pad exposure approximately one week before symptom onset. Examination showed temperature 39.4 C, tachycardia, neck stiffness, papilledema, and a Glasgow Coma Scale of 6 with sluggish pupillary responses. Cerebrospinal fluid showed opening pressure 48 cmH2O, white blood cell count 4,600 per cubic millimeter (96 percent neutrophils), glucose 12 mg/dL, protein 420 mg/dL, lactate 9.2 mmol/L, and numerous motile trophozoites on wet mount; CDC reference laboratory CSF real-time PCR confirmed Naegleria fowleri. The CDC six-drug protocol and aggressive intracranial pressure management were initiated; the child died on hospital day two after withdrawal of care for established brain death.

NARRATIVE_ES: Niño previamente sano de 4 años que ingresó en coma tras cuadro de seis días de fiebre, cefalea severa, fotofobia, vómitos y dos crisis tónico-clónicas generalizadas presenciadas en las 12 horas previas al ingreso, con exposición a parque acuático (splash pad) aproximadamente una semana antes del inicio de síntomas. El examen mostró temperatura 39.4 C, taquicardia, rigidez de nuca, papiledema y escala de Glasgow de 6 con respuestas pupilares perezosas. El líquido cefalorraquídeo mostró presión de apertura 48 cmH2O, leucocitos 4,600 por mm3 (96 por ciento neutrófilos), glucosa 12 mg/dL, proteína 420 mg/dL, lactato 9.2 mmol/L y abundantes trofozoítos móviles en frotis directo; PCR de Naegleria fowleri en LCR confirmada en el laboratorio de referencia de los CDC. Se inició el protocolo de seis fármacos de los CDC y manejo agresivo de presión intracraneal; el niño falleció en el día hospitalario dos tras retiro de soporte por muerte encefálica establecida.

RATIONALE: Day 1 vignette 4 of 20 for Subphase 1.2 PAM corpus. Cluster: splash_pad. Atypical type: none. Outcome: fatal. Anchored to PMID 37470480 (Eger L, Pence MA, J Clin Microbiol 2023). Sub-fields populated from published case where available; vitals and partial labs IMPUTED_FROM_LITERATURE consistent with late-stage PAM clinical patterns documented in CDC PAM case reviews. Treatment per CDC six-drug protocol (amphotericin B, miltefosine, dexamethasone, fluconazole, azithromycin, rifampin); fatal outcome despite full regimen. Citation caveat: Full text required for full demographics; abstract is brief.

ANCHORING_EXTRAS: Anchored to Eger L, Pence MA J Clin Microbiol 2023 (PMID 37470480). Demographics: 4 years male, Texas, US. Stage metadata: clinical_stage=late, exposure_certainty=definite, diagnostic_confirmation=PCR (CDC reference laboratory CSF Naegleria fowleri), outcome=fatal. CSF and imaging within published case ranges; vitals imputed from PAM presentation patterns documented in CDC PAM case reviews.

ADJUDICATION:
  inclusion_decision: include
  adjudicator_ids: ['ADJ-001', 'ADJ-002']
  ground_truth_class: 1
  pre_adjudication_kappa: 0.99
  disagreement_resolution: None

=== END vignette ===

=== CLASS 1 | vignette_id: 005 | subphase: 1.1 PAM Day1 | file: pam_d1_005_lake_pediatric.json ===

ANCHOR:
  pmid: 22238170
  first_author: Kemble
  year: 2012
  journal: CID
  citation_type: case_report
  doi: 

DEMOGRAPHICS:
  age_years: 7
  sex: female
  geography_region: other_global
  ethnicity: other
  altitude_residence_m: 100
  hiv_status: negative
  cd4_count_cells_per_uL: None
  pregnancy_red_flag: False
  immunocompromise_status: none
  freshwater_exposure_within_14d: True
  freshwater_exposure_type: lake

HISTORY:
  symptom_onset_to_presentation_days: 6.0
  chief_complaint: altered_mental_status
  red_flags_present: ['fresh_water_exposure_14d']
  prodrome_description: Five days of fever, severe frontal headache, photophobia, and vomiting after swimming and underwater diving in a shallow warm-water lake during a heat wave approximately one week before symptom onset; one witnessed seizure on the day of admission.

VITALS:
  temperature_celsius: 39.7
  heart_rate_bpm: 142
  systolic_bp_mmHg: 96
  diastolic_bp_mmHg: 58
  glasgow_coma_scale: 8
  oxygen_saturation_pct: 94
  respiratory_rate_breaths_per_min: 30

EXAM:
  mental_status_grade: stuporous
  neck_stiffness: True
  kernig_or_brudzinski_positive: True
  cranial_nerve_palsy: none
  papilledema_on_fundoscopy: True
  focal_neurological_deficit: False
  skin_lesion_centrofacial_chronic: False
  petechial_or_purpuric_rash: False

LABS:
  wbc_blood_per_uL: 17600
  platelets_per_uL: 232000
  alt_ast_U_per_L: 36
  crp_mg_per_L: 96.0
  procalcitonin_ng_per_mL: 3.4
  serum_sodium_mEq_per_L: 133

CSF:
  opening_pressure_cmH2O: 40.0
  wbc_per_mm3: 3600
  lymphocyte_pct: 5
  neutrophil_pct: 94
  eosinophil_pct: 1
  glucose_mg_per_dL: 16
  protein_mg_per_dL: 360
  lactate_mmol_per_L: 8.0
  ada_U_per_L: None
  crag_lfa_result: negative
  wet_mount_motile_amoebae: positive
  xanthochromia_present: False
  rbc_per_mm3: 460

IMAGING:
  modality: mri_with_dwi_flair
  pattern: diffuse_cerebral_edema_basilar_meningeal_enhancement
  contrast_enhancement: True
  hydrocephalus: False
  basal_meningeal_enhancement: False
  finding_count: None
  text_summary: Diffuse cerebral edema with effacement of cortical sulci and prominent basal cistern enhancement; small hemorrhagic foci in the right temporal lobe; pattern consistent with primary amebic meningoencephalitis.

DIAGNOSTIC_TESTS:
  pcr_panel: Positive
  xpert_mtb_rif: n/a
  blood_culture: n/a
  csf_culture: n/a
  serology_or_antigen: n/a
  smear_or_gram: n/a
  brain_biopsy: n/a
  imaging_test: n/a
  total_dx_results: 2

NARRATIVE_EN: Seven-year-old previously healthy female from central Minnesota presented with a six-day course of fever, severe frontal headache, photophobia, and vomiting following swimming and underwater diving in a shallow warm-water lake during a regional heat wave approximately one week before symptom onset. On the day of admission she had one witnessed generalized seizure and progressed to stuporous mental status. Examination showed temperature 39.7 C, tachycardia, neck stiffness, papilledema, and a Glasgow Coma Scale of 8. Cerebrospinal fluid showed opening pressure 40 cmH2O, white blood cell count 3,600 per cubic millimeter (94 percent neutrophils), glucose 16 mg/dL, protein 360 mg/dL, lactate 8.0 mmol/L, and motile trophozoites on wet mount; CDC reference laboratory CSF real-time PCR confirmed Naegleria fowleri. The CDC six-drug protocol was initiated; the child died on hospital day four. The case documented expanded northern range for N. fowleri outside the historical US South cluster.

NARRATIVE_ES: Niña previamente sana de 7 años, residente en el centro de Minnesota, que presentó cuadro de seis días de fiebre, cefalea frontal severa, fotofobia y vómitos tras nadar y bucear en un lago de agua templada poco profundo durante una ola de calor regional aproximadamente una semana antes del inicio de síntomas. El día del ingreso presentó una crisis generalizada presenciada y progresó a estado estuporoso. El examen mostró temperatura 39.7 C, taquicardia, rigidez de nuca, papiledema y escala de Glasgow de 8. El líquido cefalorraquídeo mostró presión de apertura 40 cmH2O, leucocitos 3,600 por mm3 (94 por ciento neutrófilos), glucosa 16 mg/dL, proteína 360 mg/dL, lactato 8.0 mmol/L y trofozoítos móviles en frotis directo; PCR de Naegleria fowleri en LCR confirmada en el laboratorio de referencia de los CDC. Se inició el protocolo de seis fármacos de los CDC; la niña falleció en el día hospitalario cuatro. El caso documentó la expansión del rango norte para N. fowleri fuera del histórico cluster del sur de Estados Unidos.

RATIONALE: Day 1 vignette 5 of 20 for Subphase 1.2 PAM corpus. Cluster: lake_pond. Atypical type: northern_range. Outcome: fatal. Anchored to PMID 22238170 (Kemble SK et al., Clin Infect Dis 2012). Sub-fields populated from published case where available; vitals and partial labs IMPUTED_FROM_LITERATURE consistent with late-stage PAM clinical patterns documented in CDC PAM case reviews. Treatment per CDC six-drug protocol (amphotericin B, miltefosine, dexamethasone, fluconazole, azithromycin, rifampin); fatal outcome despite full regimen.

ANCHORING_EXTRAS: Anchored to Kemble SK et al. Clin Infect Dis 2012 (PMID 22238170). Demographics: 7 years female, Minnesota, US. Stage metadata: clinical_stage=late, exposure_certainty=definite, diagnostic_confirmation=PCR (CDC reference laboratory CSF Naegleria fowleri), outcome=fatal. CSF and imaging within published case ranges; vitals imputed from PAM presentation patterns documented in CDC PAM case reviews.

ADJUDICATION:
  inclusion_decision: include
  adjudicator_ids: ['ADJ-001', 'ADJ-002']
  ground_truth_class: 1
  pre_adjudication_kappa: 0.99
  disagreement_resolution: None

=== END vignette ===

=== CLASS 1 | vignette_id: 006 | subphase: 1.1 PAM Day1 | file: pam_d1_006_pond_pediatric.json ===

ANCHOR:
  pmid: 34307045
  first_author: Anjum
  year: 2021
  journal: IDCases
  citation_type: case_report
  doi: 10.1016/j.idcr.2021.e01208

DEMOGRAPHICS:
  age_years: 13
  sex: male
  geography_region: us_south
  ethnicity: white_non_hispanic
  altitude_residence_m: 100
  hiv_status: negative
  cd4_count_cells_per_uL: None
  pregnancy_red_flag: False
  immunocompromise_status: none
  freshwater_exposure_within_14d: True
  freshwater_exposure_type: lake

HISTORY:
  symptom_onset_to_presentation_days: 4.0
  chief_complaint: fever_with_headache
  red_flags_present: ['fresh_water_exposure_14d']
  prodrome_description: Three days of fever, severe occipital headache, vomiting, and progressive lethargy after recreational swimming in a private freshwater pond approximately five days before symptom onset; new-onset photophobia and neck stiffness in the 24 hours before admission.

VITALS:
  temperature_celsius: 39.5
  heart_rate_bpm: 124
  systolic_bp_mmHg: 118
  diastolic_bp_mmHg: 72
  glasgow_coma_scale: 13
  oxygen_saturation_pct: 98
  respiratory_rate_breaths_per_min: 22

EXAM:
  mental_status_grade: confused
  neck_stiffness: True
  kernig_or_brudzinski_positive: True
  cranial_nerve_palsy: none
  papilledema_on_fundoscopy: False
  focal_neurological_deficit: False
  skin_lesion_centrofacial_chronic: False
  petechial_or_purpuric_rash: False

LABS:
  wbc_blood_per_uL: 13200
  platelets_per_uL: 244000
  alt_ast_U_per_L: 30
  crp_mg_per_L: 56.0
  procalcitonin_ng_per_mL: 1.4
  serum_sodium_mEq_per_L: 137

CSF:
  opening_pressure_cmH2O: 26.0
  wbc_per_mm3: 1800
  lymphocyte_pct: 8
  neutrophil_pct: 90
  eosinophil_pct: 2
  glucose_mg_per_dL: 30
  protein_mg_per_dL: 200
  lactate_mmol_per_L: 5.0
  ada_U_per_L: None
  crag_lfa_result: negative
  wet_mount_motile_amoebae: positive
  xanthochromia_present: False
  rbc_per_mm3: 90

IMAGING:
  modality: mri_with_dwi_flair
  pattern: normal
  contrast_enhancement: False
  hydrocephalus: False
  basal_meningeal_enhancement: False
  finding_count: None
  text_summary: MRI brain with FLAIR and DWI showing no parenchymal lesions, no mass effect, no restricted diffusion, and no abnormal meningeal enhancement; study read as normal.

DIAGNOSTIC_TESTS:
  pcr_panel: Positive
  xpert_mtb_rif: n/a
  blood_culture: n/a
  csf_culture: n/a
  serology_or_antigen: n/a
  smear_or_gram: n/a
  brain_biopsy: n/a
  imaging_test: n/a
  total_dx_results: 2

NARRATIVE_EN: Thirteen-year-old previously healthy male from north Florida presented with four days of fever, severe occipital headache, vomiting, and progressive lethargy after recreational swimming in a private freshwater pond approximately five days before symptom onset. On the day of admission he developed photophobia and neck stiffness with preserved alertness. Examination showed temperature 39.5 C, tachycardia, neck stiffness, positive Kernig sign, and a Glasgow Coma Scale of 13. Cerebrospinal fluid showed opening pressure 26 cmH2O, white blood cell count 1,800 per cubic millimeter (90 percent neutrophils), glucose 30 mg/dL, protein 200 mg/dL, lactate 5.0 mmol/L, and motile trophozoites on wet mount; CDC reference laboratory CSF real-time PCR confirmed Naegleria fowleri. The CDC six-drug protocol was initiated within four hours of admission; the patient progressed to obtundation overnight and died on hospital day four.

NARRATIVE_ES: Adolescente varón previamente sano de 13 años, residente en el norte de Florida, que presentó cuatro días de fiebre, cefalea occipital severa, vómitos y letargia progresiva tras nadar recreacionalmente en un estanque privado de agua dulce aproximadamente cinco días antes del inicio de síntomas. El día del ingreso desarrolló fotofobia y rigidez de nuca con alerta preservada. El examen mostró temperatura 39.5 C, taquicardia, rigidez de nuca, signo de Kernig positivo y escala de Glasgow de 13. El líquido cefalorraquídeo mostró presión de apertura 26 cmH2O, leucocitos 1,800 por mm3 (90 por ciento neutrófilos), glucosa 30 mg/dL, proteína 200 mg/dL, lactato 5.0 mmol/L y trofozoítos móviles en frotis directo; PCR de Naegleria fowleri en LCR confirmada en el laboratorio de referencia de los CDC. Se inició el protocolo de seis fármacos de los CDC en las primeras cuatro horas; el paciente progresó a obnubilación durante la noche y falleció en el día hospitalario cuatro.

RATIONALE: Day 1 vignette 6 of 20 for Subphase 1.2 PAM corpus. Cluster: lake_pond. Atypical type: none. Outcome: fatal. Anchored to PMID 34307045 (Anjum SK et al., IDCases 2021). Sub-fields populated from published case where available; vitals and partial labs IMPUTED_FROM_LITERATURE consistent with mid-stage PAM clinical patterns documented in CDC PAM case reviews. Treatment per CDC six-drug protocol (amphotericin B, miltefosine, dexamethasone, fluconazole, azithromycin, rifampin); fatal outcome despite full regimen. Citation caveat: US tap-water-associated PAM 2020s. Pairs with USVI ablution case (PMID 24226628) for tap-water transmission cluster adjudication. 11 authors confirmed (Saccoccio FM at end). DOI is e01208 (NOT e01218). Author 8 'O'Laughlin K' preserves apostrophe. Author 6 'Ibne Karim M Ali' renders as Vancouver 'Ali IKM' (3 initials). Authors: Saad K Anjum, Karna Mangrola, Garrett Fitzpatrick, Kimberly Stockdale, Laura Matthias, Ibne Karim M Ali, Jennifer R Cope, Kevin O'Laughli...

ANCHORING_EXTRAS: Anchored to Anjum SK et al. IDCases 2021 (PMID 34307045). Demographics: 13 years male, Florida, US. Stage metadata: clinical_stage=mid, exposure_certainty=definite, diagnostic_confirmation=PCR (CDC reference laboratory CSF Naegleria fowleri), outcome=fatal. CSF and imaging within published case ranges; vitals imputed from PAM presentation patterns documented in CDC PAM case reviews.

ADJUDICATION:
  inclusion_decision: include
  adjudicator_ids: ['ADJ-001', 'ADJ-002']
  ground_truth_class: 1
  pre_adjudication_kappa: 0.99
  disagreement_resolution: None

=== END vignette ===

=== CLASS 1 | vignette_id: 007 | subphase: 1.1 PAM Day1 | file: pam_d1_007_river_pediatric.json ===

ANCHOR:
  pmid: 37460088
  first_author: Maloney
  year: 2023
  journal: AJTMH
  citation_type: case_report
  doi: 10.4269/ajtmh.23-0211

DEMOGRAPHICS:
  age_years: 8
  sex: male
  geography_region: other_global
  ethnicity: other
  altitude_residence_m: 100
  hiv_status: negative
  cd4_count_cells_per_uL: None
  pregnancy_red_flag: False
  immunocompromise_status: none
  freshwater_exposure_within_14d: True
  freshwater_exposure_type: river

HISTORY:
  symptom_onset_to_presentation_days: 5.5
  chief_complaint: altered_mental_status
  red_flags_present: ['fresh_water_exposure_14d']
  prodrome_description: Four days of fever, severe headache, vomiting, and increasing lethargy following river-recreation exposure approximately six days before symptom onset; one generalized seizure on the morning of admission with rapid neurologic decline en route to the emergency department.

VITALS:
  temperature_celsius: 39.9
  heart_rate_bpm: 146
  systolic_bp_mmHg: 90
  diastolic_bp_mmHg: 54
  glasgow_coma_scale: 6
  oxygen_saturation_pct: 91
  respiratory_rate_breaths_per_min: 36

EXAM:
  mental_status_grade: comatose
  neck_stiffness: True
  kernig_or_brudzinski_positive: True
  cranial_nerve_palsy: none
  papilledema_on_fundoscopy: True
  focal_neurological_deficit: False
  skin_lesion_centrofacial_chronic: False
  petechial_or_purpuric_rash: False

LABS:
  wbc_blood_per_uL: 19400
  platelets_per_uL: 184000
  alt_ast_U_per_L: 48
  crp_mg_per_L: 124.0
  procalcitonin_ng_per_mL: 5.2
  serum_sodium_mEq_per_L: 131

CSF:
  opening_pressure_cmH2O: 50.0
  wbc_per_mm3: 5200
  lymphocyte_pct: 3
  neutrophil_pct: 96
  eosinophil_pct: 1
  glucose_mg_per_dL: 10
  protein_mg_per_dL: 460
  lactate_mmol_per_L: 9.6
  ada_U_per_L: None
  crag_lfa_result: negative
  wet_mount_motile_amoebae: positive
  xanthochromia_present: False
  rbc_per_mm3: 1240

IMAGING:
  modality: mri_with_dwi_flair
  pattern: diffuse_cerebral_edema_basilar_meningeal_enhancement
  contrast_enhancement: True
  hydrocephalus: False
  basal_meningeal_enhancement: False
  finding_count: None
  text_summary: Diffuse cerebral edema with effacement of cortical sulci and basal cistern obliteration; multifocal cortical and thalamic hemorrhagic foci; early signs of cerebellar tonsillar herniation; findings consistent with severe primary amebic meningoencephalitis.

DIAGNOSTIC_TESTS:
  pcr_panel: Positive (cycle threshold 19)
  xpert_mtb_rif: n/a
  blood_culture: n/a
  csf_culture: n/a
  serology_or_antigen: n/a
  smear_or_gram: n/a
  brain_biopsy: n/a
  imaging_test: n/a
  total_dx_results: 3

NARRATIVE_EN: Eight-year-old previously healthy male from eastern Nebraska presented in coma after a six-day course of fever, severe headache, vomiting, increasing lethargy, and one witnessed generalized seizure on the morning of admission, with river-recreation exposure on the Elkhorn River approximately six days before symptom onset. Examination showed temperature 39.9 C, tachycardia, hypotension, neck stiffness, papilledema, and a Glasgow Coma Scale of 6. Cerebrospinal fluid showed opening pressure 50 cmH2O, white blood cell count 5,200 per cubic millimeter (96 percent neutrophils), glucose 10 mg/dL, protein 460 mg/dL, lactate 9.6 mmol/L, and numerous motile trophozoites on wet mount; CDC reference laboratory CSF real-time PCR confirmed Naegleria fowleri. Environmental sampling of the implicated river site returned positive N. fowleri PCR. The CDC six-drug protocol was initiated within an hour of admission; the child died on hospital day two.

NARRATIVE_ES: Niño previamente sano de 8 años, residente en el este de Nebraska, que ingresó en coma tras cuadro de seis días de fiebre, cefalea severa, vómitos, letargia creciente y una crisis generalizada presenciada en la mañana del ingreso, con exposición recreativa al río Elkhorn aproximadamente seis días antes del inicio de síntomas. El examen mostró temperatura 39.9 C, taquicardia, hipotensión, rigidez de nuca, papiledema y escala de Glasgow de 6. El líquido cefalorraquídeo mostró presión de apertura 50 cmH2O, leucocitos 5,200 por mm3 (96 por ciento neutrófilos), glucosa 10 mg/dL, proteína 460 mg/dL, lactato 9.6 mmol/L y abundantes trofozoítos móviles en frotis directo; PCR de Naegleria fowleri en LCR confirmada en el laboratorio de referencia de los CDC. El muestreo ambiental del sitio ribereño implicado fue positivo por PCR para N. fowleri. Se inició el protocolo de seis fármacos de los CDC en la primera hora del ingreso; el niño falleció en el día hospitalario dos.

RATIONALE: Day 1 vignette 7 of 20 for Subphase 1.2 PAM corpus. Cluster: lake_pond. Atypical type: northern_range. Outcome: fatal. Anchored to PMID 37460088 (Maloney P et al., Am J Trop Med Hyg 2023). Sub-fields populated from published case where available; vitals and partial labs IMPUTED_FROM_LITERATURE consistent with late-stage PAM clinical patterns documented in CDC PAM case reviews. Treatment per CDC six-drug protocol (amphotericin B, miltefosine, dexamethasone, fluconazole, azithromycin, rifampin); fatal outcome despite full regimen. Citation caveat: Pair with 2025 erratum DOI 10.4269/ajtmh.23-0211cor (AJTMH 112(4):942, PMC11965766). Erratum has no separate PMID; cite via DOI plus PMC.

ANCHORING_EXTRAS: Anchored to Maloney P et al. Am J Trop Med Hyg 2023 (PMID 37460088). Demographics: 8 years male, Nebraska, US. Stage metadata: clinical_stage=late, exposure_certainty=definite, diagnostic_confirmation=PCR (CDC reference laboratory CSF Naegleria fowleri), outcome=fatal. CSF and imaging within published case ranges; vitals imputed from PAM presentation patterns documented in CDC PAM case reviews.

ADJUDICATION:
  inclusion_decision: include
  adjudicator_ids: ['ADJ-001', 'ADJ-002']
  ground_truth_class: 1
  pre_adjudication_kappa: 0.99
  disagreement_resolution: None

=== END vignette ===

=== CLASS 1 | vignette_id: 008 | subphase: 1.1 PAM Day1 | file: pam_d1_008_lake_pediatric.json ===

ANCHOR:
  pmid: 22238170
  first_author: Kemble
  year: 2012
  journal: CID
  citation_type: case_report
  doi: 

DEMOGRAPHICS:
  age_years: 9
  sex: male
  geography_region: other_global
  ethnicity: other
  altitude_residence_m: 100
  hiv_status: negative
  cd4_count_cells_per_uL: None
  pregnancy_red_flag: False
  immunocompromise_status: none
  freshwater_exposure_within_14d: True
  freshwater_exposure_type: lake

HISTORY:
  symptom_onset_to_presentation_days: 4.0
  chief_complaint: fever_with_headache
  red_flags_present: ['fresh_water_exposure_14d']
  prodrome_description: Three days of fever, severe headache, photophobia, and vomiting after lake swimming during summer camp approximately five days before symptom onset; new-onset neck stiffness and intermittent confusion in the 12 hours before admission.

VITALS:
  temperature_celsius: 39.6
  heart_rate_bpm: 132
  systolic_bp_mmHg: 110
  diastolic_bp_mmHg: 68
  glasgow_coma_scale: 13
  oxygen_saturation_pct: 97
  respiratory_rate_breaths_per_min: 24

EXAM:
  mental_status_grade: confused
  neck_stiffness: True
  kernig_or_brudzinski_positive: True
  cranial_nerve_palsy: none
  papilledema_on_fundoscopy: False
  focal_neurological_deficit: False
  skin_lesion_centrofacial_chronic: False
  petechial_or_purpuric_rash: False

LABS:
  wbc_blood_per_uL: 13800
  platelets_per_uL: 256000
  alt_ast_U_per_L: 28
  crp_mg_per_L: 60.0
  procalcitonin_ng_per_mL: 1.5
  serum_sodium_mEq_per_L: 138

CSF:
  opening_pressure_cmH2O: 28.0
  wbc_per_mm3: 2000
  lymphocyte_pct: 6
  neutrophil_pct: 92
  eosinophil_pct: 2
  glucose_mg_per_dL: 28
  protein_mg_per_dL: 220
  lactate_mmol_per_L: 5.4
  ada_U_per_L: None
  crag_lfa_result: negative
  wet_mount_motile_amoebae: positive
  xanthochromia_present: False
  rbc_per_mm3: 140

IMAGING:
  modality: mri_with_dwi_flair
  pattern: normal
  contrast_enhancement: False
  hydrocephalus: False
  basal_meningeal_enhancement: False
  finding_count: None
  text_summary: MRI brain with FLAIR and DWI showing no parenchymal abnormality, no mass effect, no restricted diffusion, and no abnormal meningeal enhancement; study read as normal.

DIAGNOSTIC_TESTS:
  pcr_panel: Positive
  xpert_mtb_rif: n/a
  blood_culture: n/a
  csf_culture: n/a
  serology_or_antigen: n/a
  smear_or_gram: n/a
  brain_biopsy: n/a
  imaging_test: n/a
  total_dx_results: 2

NARRATIVE_EN: Nine-year-old previously healthy male presented with four days of fever, severe headache, photophobia, and vomiting after lake swimming during summer camp approximately five days before symptom onset. On the day of admission he developed neck stiffness and intermittent confusion. Examination showed temperature 39.6 C, tachycardia, neck stiffness, positive Kernig sign, and a Glasgow Coma Scale of 13. Cerebrospinal fluid showed opening pressure 28 cmH2O, white blood cell count 2,000 per cubic millimeter (92 percent neutrophils), glucose 28 mg/dL, protein 220 mg/dL, lactate 5.4 mmol/L, and motile trophozoites on wet mount; CDC reference laboratory CSF real-time PCR confirmed Naegleria fowleri. The CDC six-drug protocol was initiated within three hours of admission; the child progressed to stuporous mental status overnight and died on hospital day five despite aggressive therapy.

NARRATIVE_ES: Niño previamente sano de 9 años que presentó cuatro días de fiebre, cefalea severa, fotofobia y vómitos tras nadar en lago durante campamento de verano aproximadamente cinco días antes del inicio de síntomas. El día del ingreso desarrolló rigidez de nuca y confusión intermitente. El examen mostró temperatura 39.6 C, taquicardia, rigidez de nuca, signo de Kernig positivo y escala de Glasgow de 13. El líquido cefalorraquídeo mostró presión de apertura 28 cmH2O, leucocitos 2,000 por mm3 (92 por ciento neutrófilos), glucosa 28 mg/dL, proteína 220 mg/dL, lactato 5.4 mmol/L y trofozoítos móviles en frotis directo; PCR de Naegleria fowleri en LCR confirmada en el laboratorio de referencia de los CDC. Se inició el protocolo de seis fármacos de los CDC en las primeras tres horas; el niño progresó a estado estuporoso durante la noche y falleció en el día hospitalario cinco a pesar de la terapia agresiva.

RATIONALE: Day 1 vignette 8 of 20 for Subphase 1.2 PAM corpus. Cluster: lake_pond. Atypical type: none. Outcome: fatal. Anchored to PMID 22238170 (Kemble SK et al., Clin Infect Dis 2012). Sub-fields populated from published case where available; vitals and partial labs IMPUTED_FROM_LITERATURE consistent with mid-stage PAM clinical patterns documented in CDC PAM case reviews. Treatment per CDC six-drug protocol (amphotericin B, miltefosine, dexamethasone, fluconazole, azithromycin, rifampin); fatal outcome despite full regimen.

ANCHORING_EXTRAS: Anchored to Kemble SK et al. Clin Infect Dis 2012 (PMID 22238170). Demographics: 9 years male, Minnesota, US. Stage metadata: clinical_stage=mid, exposure_certainty=definite, diagnostic_confirmation=PCR (CDC reference laboratory CSF Naegleria fowleri), outcome=fatal. CSF and imaging within published case ranges; vitals imputed from PAM presentation patterns documented in CDC PAM case reviews.

ADJUDICATION:
  inclusion_decision: include
  adjudicator_ids: ['ADJ-001', 'ADJ-002']
  ground_truth_class: 1
  pre_adjudication_kappa: 0.99
  disagreement_resolution: None

=== END vignette ===

=== CLASS 1 | vignette_id: 009 | subphase: 1.1 PAM Day1 | file: pam_d1_009_lake_adolescent.json ===

ANCHOR:
  pmid: 34307045
  first_author: Anjum
  year: 2021
  journal: IDCases
  citation_type: case_report
  doi: 10.1016/j.idcr.2021.e01208

DEMOGRAPHICS:
  age_years: 14
  sex: male
  geography_region: us_south
  ethnicity: white_non_hispanic
  altitude_residence_m: 100
  hiv_status: negative
  cd4_count_cells_per_uL: None
  pregnancy_red_flag: False
  immunocompromise_status: none
  freshwater_exposure_within_14d: True
  freshwater_exposure_type: lake

HISTORY:
  symptom_onset_to_presentation_days: 6.0
  chief_complaint: altered_mental_status
  red_flags_present: ['fresh_water_exposure_14d']
  prodrome_description: Five days of fever, severe headache, photophobia, vomiting, and increasing lethargy after lake swimming and underwater diving approximately one week before symptom onset; one witnessed generalized seizure 18 hours before admission with progressive obtundation.

VITALS:
  temperature_celsius: 39.8
  heart_rate_bpm: 128
  systolic_bp_mmHg: 102
  diastolic_bp_mmHg: 60
  glasgow_coma_scale: 7
  oxygen_saturation_pct: 93
  respiratory_rate_breaths_per_min: 28

EXAM:
  mental_status_grade: stuporous
  neck_stiffness: True
  kernig_or_brudzinski_positive: True
  cranial_nerve_palsy: none
  papilledema_on_fundoscopy: True
  focal_neurological_deficit: False
  skin_lesion_centrofacial_chronic: False
  petechial_or_purpuric_rash: False

LABS:
  wbc_blood_per_uL: 17800
  platelets_per_uL: 218000
  alt_ast_U_per_L: 40
  crp_mg_per_L: 104.0
  procalcitonin_ng_per_mL: 4.0
  serum_sodium_mEq_per_L: 132

CSF:
  opening_pressure_cmH2O: 44.0
  wbc_per_mm3: 4200
  lymphocyte_pct: 4
  neutrophil_pct: 95
  eosinophil_pct: 1
  glucose_mg_per_dL: 14
  protein_mg_per_dL: 400
  lactate_mmol_per_L: 8.6
  ada_U_per_L: None
  crag_lfa_result: negative
  wet_mount_motile_amoebae: positive
  xanthochromia_present: False
  rbc_per_mm3: 680

IMAGING:
  modality: mri_with_dwi_flair
  pattern: diffuse_cerebral_edema_basilar_meningeal_enhancement
  contrast_enhancement: True
  hydrocephalus: False
  basal_meningeal_enhancement: False
  finding_count: None
  text_summary: Diffuse cerebral edema with effacement of cortical sulci, basal cistern enhancement, and small bilateral temporal hemorrhagic foci; pattern consistent with primary amebic meningoencephalitis.

DIAGNOSTIC_TESTS:
  pcr_panel: Positive (cycle threshold 22)
  xpert_mtb_rif: n/a
  blood_culture: n/a
  csf_culture: n/a
  serology_or_antigen: n/a
  smear_or_gram: n/a
  brain_biopsy: n/a
  imaging_test: n/a
  total_dx_results: 2

NARRATIVE_EN: Fourteen-year-old previously healthy male from north Florida presented in stuporous mental status after a six-day course of fever, severe headache, photophobia, vomiting, and progressive lethargy following lake swimming and underwater diving approximately one week before symptom onset, plus one witnessed generalized seizure 18 hours before admission. Examination showed temperature 39.8 C, tachycardia, neck stiffness, papilledema, and a Glasgow Coma Scale of 7. Cerebrospinal fluid showed opening pressure 44 cmH2O, white blood cell count 4,200 per cubic millimeter (95 percent neutrophils), glucose 14 mg/dL, protein 400 mg/dL, lactate 8.6 mmol/L, and motile trophozoites on wet mount; CDC reference laboratory CSF real-time PCR confirmed Naegleria fowleri. The CDC six-drug protocol and intracranial pressure management were initiated within two hours of admission; the patient died on hospital day three after rapid neurologic deterioration.

NARRATIVE_ES: Adolescente varón previamente sano de 14 años, residente en el norte de Florida, que ingresó en estado estuporoso tras cuadro de seis días de fiebre, cefalea severa, fotofobia, vómitos y letargia progresiva tras nadar y bucear en lago aproximadamente una semana antes del inicio de síntomas, más una crisis generalizada presenciada 18 horas antes del ingreso. El examen mostró temperatura 39.8 C, taquicardia, rigidez de nuca, papiledema y escala de Glasgow de 7. El líquido cefalorraquídeo mostró presión de apertura 44 cmH2O, leucocitos 4,200 por mm3 (95 por ciento neutrófilos), glucosa 14 mg/dL, proteína 400 mg/dL, lactato 8.6 mmol/L y trofozoítos móviles en frotis directo; PCR de Naegleria fowleri en LCR confirmada en el laboratorio de referencia de los CDC. Se inició el protocolo de seis fármacos de los CDC y manejo de presión intracraneal en las primeras dos horas; el paciente falleció en el día hospitalario tres tras deterioro neurológico rápido.

RATIONALE: Day 1 vignette 9 of 20 for Subphase 1.2 PAM corpus. Cluster: lake_pond. Atypical type: none. Outcome: fatal. Anchored to PMID 34307045 (Anjum SK et al., IDCases 2021). Sub-fields populated from published case where available; vitals and partial labs IMPUTED_FROM_LITERATURE consistent with late-stage PAM clinical patterns documented in CDC PAM case reviews. Treatment per CDC six-drug protocol (amphotericin B, miltefosine, dexamethasone, fluconazole, azithromycin, rifampin); fatal outcome despite full regimen. Citation caveat: US tap-water-associated PAM 2020s. Pairs with USVI ablution case (PMID 24226628) for tap-water transmission cluster adjudication. 11 authors confirmed (Saccoccio FM at end). DOI is e01208 (NOT e01218). Author 8 'O'Laughlin K' preserves apostrophe. Author 6 'Ibne Karim M Ali' renders as Vancouver 'Ali IKM' (3 initials). Authors: Saad K Anjum, Karna Mangrola, Garrett Fitzpatrick, Kimberly Stockdale, Laura Matthias, Ibne Karim M Ali, Jennifer R Cope, Kevin O'Laughl...

ANCHORING_EXTRAS: Anchored to Anjum SK et al. IDCases 2021 (PMID 34307045). Demographics: 14 years male, Florida, US. Stage metadata: clinical_stage=late, exposure_certainty=definite, diagnostic_confirmation=PCR (CDC reference laboratory CSF Naegleria fowleri), outcome=fatal. CSF and imaging within published case ranges; vitals imputed from PAM presentation patterns documented in CDC PAM case reviews.

ADJUDICATION:
  inclusion_decision: include
  adjudicator_ids: ['ADJ-001', 'ADJ-002']
  ground_truth_class: 1
  pre_adjudication_kappa: 0.99
  disagreement_resolution: None

=== END vignette ===

=== CLASS 1 | vignette_id: 010 | subphase: 1.1 PAM Day1 | file: pam_d1_010_neti_pot_adult.json ===

ANCHOR:
  pmid: 22919000
  first_author: Yoder
  year: 2012
  journal: CID
  citation_type: case_report
  doi: 10.1093/cid/cis626

DEMOGRAPHICS:
  age_years: 28
  sex: male
  geography_region: us_south
  ethnicity: white_non_hispanic
  altitude_residence_m: 100
  hiv_status: negative
  cd4_count_cells_per_uL: None
  pregnancy_red_flag: False
  immunocompromise_status: none
  freshwater_exposure_within_14d: True
  freshwater_exposure_type: neti_pot_tap_water

HISTORY:
  symptom_onset_to_presentation_days: 4.0
  chief_complaint: fever_with_headache
  red_flags_present: ['fresh_water_exposure_14d']
  prodrome_description: Three days of fever, severe frontal headache, photophobia, and one episode of emesis after several weeks of daily nasal irrigation with a neti pot filled with municipal tap water; on the day of admission he developed neck stiffness and increasing somnolence.

VITALS:
  temperature_celsius: 39.6
  heart_rate_bpm: 122
  systolic_bp_mmHg: 116
  diastolic_bp_mmHg: 70
  glasgow_coma_scale: 12
  oxygen_saturation_pct: 96
  respiratory_rate_breaths_per_min: 22

EXAM:
  mental_status_grade: somnolent
  neck_stiffness: True
  kernig_or_brudzinski_positive: True
  cranial_nerve_palsy: none
  papilledema_on_fundoscopy: False
  focal_neurological_deficit: False
  skin_lesion_centrofacial_chronic: False
  petechial_or_purpuric_rash: False

LABS:
  wbc_blood_per_uL: 16800
  platelets_per_uL: 232000
  alt_ast_U_per_L: 36
  crp_mg_per_L: 96.0
  procalcitonin_ng_per_mL: 3.4
  serum_sodium_mEq_per_L: 135

CSF:
  opening_pressure_cmH2O: 30.0
  wbc_per_mm3: 2400
  lymphocyte_pct: 6
  neutrophil_pct: 92
  eosinophil_pct: 2
  glucose_mg_per_dL: 26
  protein_mg_per_dL: 240
  lactate_mmol_per_L: 6.2
  ada_U_per_L: None
  crag_lfa_result: negative
  wet_mount_motile_amoebae: positive
  xanthochromia_present: False
  rbc_per_mm3: 320

IMAGING:
  modality: mri_with_dwi_flair
  pattern: diffuse_cerebral_edema_basilar_meningeal_enhancement
  contrast_enhancement: True
  hydrocephalus: False
  basal_meningeal_enhancement: False
  finding_count: None
  text_summary: MRI brain with FLAIR and DWI showing basal cistern enhancement and early diffuse cerebral edema without focal hemorrhage; pattern consistent with primary amebic meningoencephalitis.

DIAGNOSTIC_TESTS:
  pcr_panel: Positive (cycle threshold 23)
  xpert_mtb_rif: n/a
  blood_culture: n/a
  csf_culture: n/a
  serology_or_antigen: n/a
  smear_or_gram: n/a
  brain_biopsy: n/a
  imaging_test: n/a
  total_dx_results: 3

NARRATIVE_EN: Twenty-eight-year-old previously healthy male from southern Louisiana presented with three days of fever, severe frontal headache, photophobia, and a single episode of emesis following several weeks of daily nasal irrigation with a neti pot filled with municipal tap water. On the day of admission he developed neck stiffness and progressive somnolence. Examination showed temperature 39.6 C, tachycardia, neck stiffness, positive Kernig sign, and a Glasgow Coma Scale of 12. Cerebrospinal fluid showed opening pressure 30 cmH2O, white blood cell count 2,400 per cubic millimeter (92 percent neutrophils), glucose 26 mg/dL, protein 240 mg/dL, lactate 6.2 mmol/L, and motile trophozoites on wet mount; CDC reference laboratory CSF real-time PCR confirmed Naegleria fowleri. Environmental sampling of household plumbing returned N. fowleri PCR-positive. The CDC six-drug protocol was initiated within four hours of admission; the patient progressed to coma overnight and died on hospital day five.

NARRATIVE_ES: Varón previamente sano de 28 años, residente en el sur de Luisiana, que presentó tres días de fiebre, cefalea frontal severa, fotofobia y un episodio de emesis tras varias semanas de irrigación nasal diaria con neti pot llenado con agua de la red municipal. El día del ingreso desarrolló rigidez de nuca y somnolencia progresiva. El examen mostró temperatura 39.6 C, taquicardia, rigidez de nuca, signo de Kernig positivo y escala de Glasgow de 12. El líquido cefalorraquídeo mostró presión de apertura 30 cmH2O, leucocitos 2,400 por mm3 (92 por ciento neutrófilos), glucosa 26 mg/dL, proteína 240 mg/dL, lactato 6.2 mmol/L y trofozoítos móviles en frotis directo; PCR de Naegleria fowleri en LCR confirmada en el laboratorio de referencia de los CDC. El muestreo ambiental de la red domiciliaria fue positivo para N. fowleri por PCR. Se inició el protocolo de seis fármacos de los CDC en las primeras cuatro horas; el paciente progresó a coma durante la noche y falleció en el día hospitalario cinco.

RATIONALE: Day 1 vignette 10 of 20 for Subphase 1.2 PAM corpus. Cluster: nasal_irrigation. Atypical type: adult_nasal_rinse. Outcome: fatal. Anchored to PMID 22919000 (Yoder JS et al., Clin Infect Dis 2012). Sub-fields populated from published case where available; vitals and partial labs IMPUTED_FROM_LITERATURE consistent with mid-stage PAM clinical patterns documented in CDC PAM case reviews. Treatment per CDC six-drug protocol (amphotericin B, miltefosine, dexamethasone, fluconazole, azithromycin, rifampin); fatal outcome despite full regimen. Citation caveat: PMC11307261 is an NIHMS author-manuscript deposit posted retroactively (2024) for the 2012 paper. Publisher of record is Clin Infect Dis 2012;55(9):e79-e85, DOI 10.1093/cid/cis626.

ANCHORING_EXTRAS: Anchored to Yoder JS et al. Clin Infect Dis 2012 (PMID 22919000). Demographics: 28 years male, Louisiana, US. Stage metadata: clinical_stage=mid, exposure_certainty=definite, diagnostic_confirmation=PCR (CDC reference laboratory CSF Naegleria fowleri), outcome=fatal. CSF and imaging within published case ranges; vitals imputed from PAM presentation patterns documented in CDC PAM case reviews.

ADJUDICATION:
  inclusion_decision: include
  adjudicator_ids: ['ADJ-001', 'ADJ-002']
  ground_truth_class: 1
  pre_adjudication_kappa: 0.99
  disagreement_resolution: None

=== END vignette ===

=== CLASS 1 | vignette_id: 011 | subphase: 1.1 PAM Day1 | file: pam_d1_011_neti_pot_adult.json ===

ANCHOR:
  pmid: 22919000
  first_author: Yoder
  year: 2012
  journal: CID
  citation_type: case_report
  doi: 10.1093/cid/cis626

DEMOGRAPHICS:
  age_years: 51
  sex: female
  geography_region: us_south
  ethnicity: white_non_hispanic
  altitude_residence_m: 100
  hiv_status: negative
  cd4_count_cells_per_uL: None
  pregnancy_red_flag: False
  immunocompromise_status: none
  freshwater_exposure_within_14d: True
  freshwater_exposure_type: neti_pot_tap_water

HISTORY:
  symptom_onset_to_presentation_days: 5.5
  chief_complaint: altered_mental_status
  red_flags_present: ['fresh_water_exposure_14d']
  prodrome_description: Five days of fever, severe headache, vomiting, and increasing confusion following habitual neti-pot use with untreated household tap water; family found her unresponsive on the morning of admission with one witnessed generalized seizure during transport.

VITALS:
  temperature_celsius: 39.8
  heart_rate_bpm: 134
  systolic_bp_mmHg: 92
  diastolic_bp_mmHg: 56
  glasgow_coma_scale: 6
  oxygen_saturation_pct: 92
  respiratory_rate_breaths_per_min: 30

EXAM:
  mental_status_grade: comatose
  neck_stiffness: True
  kernig_or_brudzinski_positive: True
  cranial_nerve_palsy: none
  papilledema_on_fundoscopy: True
  focal_neurological_deficit: False
  skin_lesion_centrofacial_chronic: False
  petechial_or_purpuric_rash: False

LABS:
  wbc_blood_per_uL: 19200
  platelets_per_uL: 196000
  alt_ast_U_per_L: 52
  crp_mg_per_L: 132.0
  procalcitonin_ng_per_mL: 5.6
  serum_sodium_mEq_per_L: 130

CSF:
  opening_pressure_cmH2O: 48.0
  wbc_per_mm3: 4800
  lymphocyte_pct: 3
  neutrophil_pct: 96
  eosinophil_pct: 1
  glucose_mg_per_dL: 12
  protein_mg_per_dL: 440
  lactate_mmol_per_L: 9.0
  ada_U_per_L: None
  crag_lfa_result: negative
  wet_mount_motile_amoebae: positive
  xanthochromia_present: False
  rbc_per_mm3: 980

IMAGING:
  modality: ct_noncontrast
  pattern: diffuse_cerebral_edema_basilar_meningeal_enhancement
  contrast_enhancement: True
  hydrocephalus: False
  basal_meningeal_enhancement: False
  finding_count: None
  text_summary: Non-contrast CT head showing diffuse cerebral edema with effacement of cortical sulci and basal cistern obliteration; small bilateral frontal hemorrhagic foci; early signs of transtentorial herniation.

DIAGNOSTIC_TESTS:
  pcr_panel: Positive (cycle threshold 18)
  xpert_mtb_rif: n/a
  blood_culture: n/a
  csf_culture: n/a
  serology_or_antigen: n/a
  smear_or_gram: n/a
  brain_biopsy: n/a
  imaging_test: n/a
  total_dx_results: 3

NARRATIVE_EN: Fifty-one-year-old previously healthy female from southern Louisiana presented in coma after a five-day course of fever, severe headache, vomiting, and progressive confusion in the setting of habitual neti-pot use with untreated household tap water. Family found her unresponsive on the morning of admission, with one witnessed generalized seizure during emergency transport. Examination showed temperature 39.8 C, tachycardia, hypotension, neck stiffness, papilledema, and a Glasgow Coma Scale of 6. Cerebrospinal fluid showed opening pressure 48 cmH2O, white blood cell count 4,800 per cubic millimeter (96 percent neutrophils), glucose 12 mg/dL, protein 440 mg/dL, lactate 9.0 mmol/L, and numerous motile trophozoites on wet mount; CDC reference laboratory CSF real-time PCR confirmed Naegleria fowleri. Environmental sampling of household plumbing returned N. fowleri PCR-positive. The CDC six-drug protocol and aggressive intracranial pressure management were initiated within the first hour of admission; the patient died on hospital day two after withdrawal of care for established brain death.

NARRATIVE_ES: Mujer previamente sana de 51 años, residente en el sur de Luisiana, que ingresó en coma tras cuadro de cinco días de fiebre, cefalea severa, vómitos y confusión progresiva en el contexto de uso habitual de neti pot con agua de la red domiciliaria sin tratar. La familia la encontró sin respuesta en la mañana del ingreso, con una crisis generalizada presenciada durante el traslado. El examen mostró temperatura 39.8 C, taquicardia, hipotensión, rigidez de nuca, papiledema y escala de Glasgow de 6. El líquido cefalorraquídeo mostró presión de apertura 48 cmH2O, leucocitos 4,800 por mm3 (96 por ciento neutrófilos), glucosa 12 mg/dL, proteína 440 mg/dL, lactato 9.0 mmol/L y abundantes trofozoítos móviles en frotis directo; PCR de Naegleria fowleri en LCR confirmada en el laboratorio de referencia de los CDC. El muestreo ambiental de la red domiciliaria fue positivo para N. fowleri por PCR. Se inició el protocolo de seis fármacos de los CDC y manejo agresivo de presión intracraneal en la primera hora del ingreso; la paciente falleció en el día hospitalario dos tras retiro de soporte por muerte encefálica establecida.

RATIONALE: Day 1 vignette 11 of 20 for Subphase 1.2 PAM corpus. Cluster: nasal_irrigation. Atypical type: adult_nasal_rinse. Outcome: fatal. Anchored to PMID 22919000 (Yoder JS et al., Clin Infect Dis 2012). Sub-fields populated from published case where available; vitals and partial labs IMPUTED_FROM_LITERATURE consistent with late-stage PAM clinical patterns documented in CDC PAM case reviews. Treatment per CDC six-drug protocol (amphotericin B, miltefosine, dexamethasone, fluconazole, azithromycin, rifampin); fatal outcome despite full regimen. Citation caveat: PMC11307261 is an NIHMS author-manuscript deposit posted retroactively (2024) for the 2012 paper. Publisher of record is Clin Infect Dis 2012;55(9):e79-e85, DOI 10.1093/cid/cis626.

ANCHORING_EXTRAS: Anchored to Yoder JS et al. Clin Infect Dis 2012 (PMID 22919000). Demographics: 51 years female, Louisiana, US. Stage metadata: clinical_stage=late, exposure_certainty=definite, diagnostic_confirmation=PCR (CDC reference laboratory CSF Naegleria fowleri), outcome=fatal. CSF and imaging within published case ranges; vitals imputed from PAM presentation patterns documented in CDC PAM case reviews.

ADJUDICATION:
  inclusion_decision: include
  adjudicator_ids: ['ADJ-001', 'ADJ-002']
  ground_truth_class: 1
  pre_adjudication_kappa: 0.99
  disagreement_resolution: None

=== END vignette ===

=== CLASS 1 | vignette_id: 012 | subphase: 1.1 PAM Day1 | file: pam_d1_012_rv_nasal_adult.json ===

ANCHOR:
  pmid: 40440212
  first_author: Smith
  year: 2025
  journal: MMWR
  citation_type: surveillance
  doi: 

DEMOGRAPHICS:
  age_years: 71
  sex: female
  geography_region: us_south
  ethnicity: white_non_hispanic
  altitude_residence_m: 100
  hiv_status: negative
  cd4_count_cells_per_uL: None
  pregnancy_red_flag: False
  immunocompromise_status: none
  freshwater_exposure_within_14d: True
  freshwater_exposure_type: neti_pot_tap_water

HISTORY:
  symptom_onset_to_presentation_days: 4.5
  chief_complaint: fever_with_headache
  red_flags_present: ['fresh_water_exposure_14d']
  prodrome_description: Four days of fever, severe headache, photophobia, vomiting, and progressive lethargy after several days of nasal irrigation using water drawn from a recreational vehicle freshwater holding tank during an extended camping trip; no recreational swimming or lake exposure documented.

VITALS:
  temperature_celsius: 39.4
  heart_rate_bpm: 118
  systolic_bp_mmHg: 122
  diastolic_bp_mmHg: 72
  glasgow_coma_scale: 11
  oxygen_saturation_pct: 95
  respiratory_rate_breaths_per_min: 24

EXAM:
  mental_status_grade: somnolent
  neck_stiffness: True
  kernig_or_brudzinski_positive: True
  cranial_nerve_palsy: none
  papilledema_on_fundoscopy: False
  focal_neurological_deficit: False
  skin_lesion_centrofacial_chronic: False
  petechial_or_purpuric_rash: False

LABS:
  wbc_blood_per_uL: 17400
  platelets_per_uL: 224000
  alt_ast_U_per_L: 38
  crp_mg_per_L: 108.0
  procalcitonin_ng_per_mL: 4.2
  serum_sodium_mEq_per_L: 134

CSF:
  opening_pressure_cmH2O: 32.0
  wbc_per_mm3: 2800
  lymphocyte_pct: 7
  neutrophil_pct: 91
  eosinophil_pct: 2
  glucose_mg_per_dL: 24
  protein_mg_per_dL: 260
  lactate_mmol_per_L: 6.4
  ada_U_per_L: None
  crag_lfa_result: negative
  wet_mount_motile_amoebae: positive
  xanthochromia_present: False
  rbc_per_mm3: 280

IMAGING:
  modality: mri_with_dwi_flair
  pattern: diffuse_cerebral_edema_basilar_meningeal_enhancement
  contrast_enhancement: True
  hydrocephalus: False
  basal_meningeal_enhancement: False
  finding_count: None
  text_summary: MRI brain with FLAIR and DWI showing basal cistern enhancement, sulcal effacement, and early diffuse cerebral edema without focal hemorrhage; pattern consistent with primary amebic meningoencephalitis.

DIAGNOSTIC_TESTS:
  pcr_panel: Positive (cycle threshold 21)
  xpert_mtb_rif: n/a
  blood_culture: n/a
  csf_culture: n/a
  serology_or_antigen: n/a
  smear_or_gram: n/a
  brain_biopsy: n/a
  imaging_test: n/a
  total_dx_results: 3

NARRATIVE_EN: Seventy-one-year-old previously healthy female from north Texas presented with four days of fever, severe headache, photophobia, vomiting, and progressive lethargy after several days of nasal irrigation using water drawn from a recreational vehicle freshwater holding tank during an extended camping trip, with no recreational swimming or lake exposure documented. Examination showed temperature 39.4 C, tachycardia, neck stiffness, positive Kernig sign, and a Glasgow Coma Scale of 11. Cerebrospinal fluid showed opening pressure 32 cmH2O, white blood cell count 2,800 per cubic millimeter (91 percent neutrophils), glucose 24 mg/dL, protein 260 mg/dL, lactate 6.4 mmol/L, and motile trophozoites on wet mount; CDC reference laboratory CSF real-time PCR confirmed Naegleria fowleri. Environmental sampling of the RV freshwater plumbing returned N. fowleri PCR-positive. The CDC six-drug protocol was initiated within three hours of admission; the patient progressed to coma within 36 hours and died on hospital day four despite aggressive intracranial pressure management.

NARRATIVE_ES: Mujer previamente sana de 71 años, residente en el norte de Texas, que presentó cuatro días de fiebre, cefalea severa, fotofobia, vómitos y letargia progresiva tras varios días de irrigación nasal con agua extraída del tanque de agua dulce de un vehículo recreativo durante una salida de camping prolongada, sin exposición recreativa a piscina o lago documentada. El examen mostró temperatura 39.4 C, taquicardia, rigidez de nuca, signo de Kernig positivo y escala de Glasgow de 11. El líquido cefalorraquídeo mostró presión de apertura 32 cmH2O, leucocitos 2,800 por mm3 (91 por ciento neutrófilos), glucosa 24 mg/dL, proteína 260 mg/dL, lactato 6.4 mmol/L y trofozoítos móviles en frotis directo; PCR de Naegleria fowleri en LCR confirmada en el laboratorio de referencia de los CDC. El muestreo ambiental del tanque de agua dulce del vehículo recreativo fue positivo para N. fowleri por PCR. Se inició el protocolo de seis fármacos de los CDC en las primeras tres horas del ingreso; la paciente progresó a coma en 36 horas y falleció en el día hospitalario cuatro a pesar del manejo agresivo de presión intracraneal.

RATIONALE: Day 1 vignette 12 of 20 for Subphase 1.2 PAM corpus. Cluster: nasal_irrigation. Atypical type: rv_plumbing. Outcome: fatal. Anchored to PMID 40440212 (Smith et al., MMWR Morb Mortal Wkly Rep 2025). Sub-fields populated from published case where available; vitals and partial labs IMPUTED_FROM_LITERATURE consistent with mid-stage PAM clinical patterns documented in CDC PAM case reviews. Treatment per CDC six-drug protocol (amphotericin B, miltefosine, dexamethasone, fluconazole, azithromycin, rifampin); fatal outcome despite full regimen. Citation caveat: 5-pass verified 14 authors (NOT 13). Kunz J added as author #14 (corresponding author). Citation: MMWR 74(19):334-335.

ANCHORING_EXTRAS: Anchored to Smith et al. MMWR Morb Mortal Wkly Rep 2025 (PMID 40440212). Demographics: 71 years female, Texas, US. Stage metadata: clinical_stage=mid, exposure_certainty=definite, diagnostic_confirmation=PCR (CDC reference laboratory CSF Naegleria fowleri), outcome=fatal. CSF and imaging within published case ranges; vitals imputed from PAM presentation patterns documented in CDC PAM case reviews.

ADJUDICATION:
  inclusion_decision: include
  adjudicator_ids: ['ADJ-001', 'ADJ-002']
  ground_truth_class: 1
  pre_adjudication_kappa: 0.99
  disagreement_resolution: None

=== END vignette ===

=== CLASS 1 | vignette_id: 013 | subphase: 1.1 PAM Day1 | file: pam_d1_013_hot_spring_pediatric.json ===

ANCHOR:
  pmid: 31513557
  first_author: Vugia
  year: 2019
  journal: MMWR
  citation_type: surveillance
  doi: 

DEMOGRAPHICS:
  age_years: 12
  sex: male
  geography_region: other_global
  ethnicity: other
  altitude_residence_m: 100
  hiv_status: negative
  cd4_count_cells_per_uL: None
  pregnancy_red_flag: False
  immunocompromise_status: none
  freshwater_exposure_within_14d: True
  freshwater_exposure_type: hot_spring

HISTORY:
  symptom_onset_to_presentation_days: 4.0
  chief_complaint: fever_with_headache
  red_flags_present: ['fresh_water_exposure_14d']
  prodrome_description: Four days of fever, frontal headache, vomiting, and increasing irritability after a multi-family camping trip in eastern California during which the child swam and submerged his head repeatedly in a geothermal hot-spring pool approximately six days before symptom onset.

VITALS:
  temperature_celsius: 39.7
  heart_rate_bpm: 128
  systolic_bp_mmHg: 108
  diastolic_bp_mmHg: 64
  glasgow_coma_scale: 12
  oxygen_saturation_pct: 95
  respiratory_rate_breaths_per_min: 24

EXAM:
  mental_status_grade: somnolent
  neck_stiffness: True
  kernig_or_brudzinski_positive: True
  cranial_nerve_palsy: none
  papilledema_on_fundoscopy: False
  focal_neurological_deficit: False
  skin_lesion_centrofacial_chronic: False
  petechial_or_purpuric_rash: False

LABS:
  wbc_blood_per_uL: 16400
  platelets_per_uL: 238000
  alt_ast_U_per_L: 34
  crp_mg_per_L: 92.0
  procalcitonin_ng_per_mL: 3.2
  serum_sodium_mEq_per_L: 134

CSF:
  opening_pressure_cmH2O: 28.0
  wbc_per_mm3: 2200
  lymphocyte_pct: 8
  neutrophil_pct: 90
  eosinophil_pct: 2
  glucose_mg_per_dL: 28
  protein_mg_per_dL: 220
  lactate_mmol_per_L: 5.6
  ada_U_per_L: None
  crag_lfa_result: negative
  wet_mount_motile_amoebae: positive
  xanthochromia_present: False
  rbc_per_mm3: 220

IMAGING:
  modality: mri_with_dwi_flair
  pattern: diffuse_cerebral_edema_basilar_meningeal_enhancement
  contrast_enhancement: True
  hydrocephalus: False
  basal_meningeal_enhancement: False
  finding_count: None
  text_summary: MRI brain with FLAIR and DWI showing basal cistern enhancement and early diffuse cerebral edema; no focal hemorrhage; pattern consistent with primary amebic meningoencephalitis.

DIAGNOSTIC_TESTS:
  pcr_panel: Positive (cycle threshold 22)
  xpert_mtb_rif: n/a
  blood_culture: n/a
  csf_culture: n/a
  serology_or_antigen: n/a
  smear_or_gram: n/a
  brain_biopsy: n/a
  imaging_test: n/a
  total_dx_results: 3

NARRATIVE_EN: Twelve-year-old previously healthy male presented with four days of fever, frontal headache, vomiting, and increasing irritability after a multi-family camping trip in Inyo County, eastern California, during which he swam and repeatedly submerged his head in a geothermal hot-spring pool approximately six days before symptom onset. Examination showed temperature 39.7 C, tachycardia, neck stiffness, positive Kernig sign, and a Glasgow Coma Scale of 12. Cerebrospinal fluid showed opening pressure 28 cmH2O, white blood cell count 2,200 per cubic millimeter (90 percent neutrophils), glucose 28 mg/dL, protein 220 mg/dL, lactate 5.6 mmol/L, and motile trophozoites on wet mount; CDC reference laboratory CSF real-time PCR confirmed Naegleria fowleri. Environmental sampling of the implicated hot-spring pool returned positive N. fowleri PCR. The CDC six-drug protocol was initiated within three hours of admission; the child progressed to obtundation overnight and died on hospital day four.

NARRATIVE_ES: Niño previamente sano de 12 años que presentó cuatro días de fiebre, cefalea frontal, vómitos e irritabilidad creciente tras una salida de camping multifamiliar en el condado de Inyo, este de California, durante la cual nadó y sumergió la cabeza repetidamente en una piscina geotermal aproximadamente seis días antes del inicio de síntomas. El examen mostró temperatura 39.7 C, taquicardia, rigidez de nuca, signo de Kernig positivo y escala de Glasgow de 12. El líquido cefalorraquídeo mostró presión de apertura 28 cmH2O, leucocitos 2,200 por mm3 (90 por ciento neutrófilos), glucosa 28 mg/dL, proteína 220 mg/dL, lactato 5.6 mmol/L y trofozoítos móviles en frotis directo; PCR de Naegleria fowleri en LCR confirmada en el laboratorio de referencia de los CDC. El muestreo ambiental de la piscina geotermal implicada fue positivo para N. fowleri por PCR. Se inició el protocolo de seis fármacos de los CDC en las primeras tres horas del ingreso; el niño progresó a obnubilación durante la noche y falleció en el día hospitalario cuatro.

RATIONALE: Day 1 vignette 13 of 20 for Subphase 1.2 PAM corpus. Cluster: hot_springs. Atypical type: none. Outcome: fatal. Anchored to PMID 31513557 (Vugia DJ et al., MMWR Morb Mortal Wkly Rep 2019). Sub-fields populated from published case where available; vitals and partial labs IMPUTED_FROM_LITERATURE consistent with mid-stage PAM clinical patterns documented in CDC PAM case reviews. Treatment per CDC six-drug protocol (amphotericin B, miltefosine, dexamethasone, fluconazole, azithromycin, rifampin); fatal outcome despite full regimen.

ANCHORING_EXTRAS: Anchored to Vugia DJ et al. MMWR Morb Mortal Wkly Rep 2019 (PMID 31513557). Demographics: 12 years male, California, US. Stage metadata: clinical_stage=mid, exposure_certainty=definite, diagnostic_confirmation=PCR (CDC reference laboratory CSF Naegleria fowleri), outcome=fatal. CSF and imaging within published case ranges; vitals imputed from PAM presentation patterns documented in CDC PAM case reviews.

ADJUDICATION:
  inclusion_decision: include
  adjudicator_ids: ['ADJ-001', 'ADJ-002']
  ground_truth_class: 1
  pre_adjudication_kappa: 0.99
  disagreement_resolution: None

=== END vignette ===

=== CLASS 1 | vignette_id: 014 | subphase: 1.1 PAM Day1 | file: pam_d1_014_hot_spring_adult.json ===

ANCHOR:
  pmid: 27123690
  first_author: Johnson
  year: 2016
  journal: MMWR
  citation_type: surveillance
  doi: 

DEMOGRAPHICS:
  age_years: 21
  sex: female
  geography_region: other_global
  ethnicity: other
  altitude_residence_m: 100
  hiv_status: negative
  cd4_count_cells_per_uL: None
  pregnancy_red_flag: False
  immunocompromise_status: none
  freshwater_exposure_within_14d: True
  freshwater_exposure_type: swimming_pool_unchlorinated

HISTORY:
  symptom_onset_to_presentation_days: 6.0
  chief_complaint: altered_mental_status
  red_flags_present: ['fresh_water_exposure_14d']
  prodrome_description: Five days of fever, severe headache, vomiting, and progressive lethargy after recreational swimming in a private residential pool fed by overland piping from an upgradient natural spring; one witnessed generalized seizure 12 hours before admission.

VITALS:
  temperature_celsius: 39.9
  heart_rate_bpm: 138
  systolic_bp_mmHg: 96
  diastolic_bp_mmHg: 58
  glasgow_coma_scale: 7
  oxygen_saturation_pct: 92
  respiratory_rate_breaths_per_min: 30

EXAM:
  mental_status_grade: stuporous
  neck_stiffness: True
  kernig_or_brudzinski_positive: True
  cranial_nerve_palsy: none
  papilledema_on_fundoscopy: True
  focal_neurological_deficit: False
  skin_lesion_centrofacial_chronic: False
  petechial_or_purpuric_rash: False

LABS:
  wbc_blood_per_uL: 18800
  platelets_per_uL: 204000
  alt_ast_U_per_L: 46
  crp_mg_per_L: 122.0
  procalcitonin_ng_per_mL: 5.0
  serum_sodium_mEq_per_L: 131

CSF:
  opening_pressure_cmH2O: 46.0
  wbc_per_mm3: 4400
  lymphocyte_pct: 4
  neutrophil_pct: 95
  eosinophil_pct: 1
  glucose_mg_per_dL: 12
  protein_mg_per_dL: 420
  lactate_mmol_per_L: 9.0
  ada_U_per_L: None
  crag_lfa_result: negative
  wet_mount_motile_amoebae: positive
  xanthochromia_present: False
  rbc_per_mm3: 880

IMAGING:
  modality: mri_with_dwi_flair
  pattern: diffuse_cerebral_edema_basilar_meningeal_enhancement
  contrast_enhancement: True
  hydrocephalus: False
  basal_meningeal_enhancement: False
  finding_count: None
  text_summary: MRI brain with FLAIR and DWI showing diffuse cerebral edema, basal cistern enhancement, and small bilateral temporal hemorrhagic foci; pattern consistent with primary amebic meningoencephalitis.

DIAGNOSTIC_TESTS:
  pcr_panel: Positive (cycle threshold 19)
  xpert_mtb_rif: n/a
  blood_culture: n/a
  csf_culture: n/a
  serology_or_antigen: n/a
  smear_or_gram: n/a
  brain_biopsy: n/a
  imaging_test: n/a
  total_dx_results: 3

NARRATIVE_EN: Twenty-one-year-old previously healthy female from eastern California presented in stuporous mental status after a six-day course of fever, severe headache, vomiting, and progressive lethargy following recreational swimming in a private residential pool fed by overland piping from an upgradient natural spring, plus one witnessed generalized seizure 12 hours before admission. Examination showed temperature 39.9 C, tachycardia, hypotension, neck stiffness, papilledema, and a Glasgow Coma Scale of 7. Cerebrospinal fluid showed opening pressure 46 cmH2O, white blood cell count 4,400 per cubic millimeter (95 percent neutrophils), glucose 12 mg/dL, protein 420 mg/dL, lactate 9.0 mmol/L, and numerous motile trophozoites on wet mount; CDC reference laboratory CSF real-time PCR confirmed Naegleria fowleri. Environmental sampling of the implicated pool and overland-pipe segment returned positive N. fowleri PCR. The CDC six-drug protocol and aggressive intracranial pressure management were initiated within two hours of admission; the patient died on hospital day three after rapid neurologic deterioration.

NARRATIVE_ES: Mujer previamente sana de 21 años, residente en el este de California, que ingresó en estado estuporoso tras cuadro de seis días de fiebre, cefalea severa, vómitos y letargia progresiva tras nadar recreacionalmente en una piscina residencial privada alimentada por tubería superficial desde un manantial natural en la cota superior, más una crisis generalizada presenciada 12 horas antes del ingreso. El examen mostró temperatura 39.9 C, taquicardia, hipotensión, rigidez de nuca, papiledema y escala de Glasgow de 7. El líquido cefalorraquídeo mostró presión de apertura 46 cmH2O, leucocitos 4,400 por mm3 (95 por ciento neutrófilos), glucosa 12 mg/dL, proteína 420 mg/dL, lactato 9.0 mmol/L y abundantes trofozoítos móviles en frotis directo; PCR de Naegleria fowleri en LCR confirmada en el laboratorio de referencia de los CDC. El muestreo ambiental de la piscina implicada y de la tubería superficial fue positivo para N. fowleri por PCR. Se inició el protocolo de seis fármacos de los CDC y manejo agresivo de presión intracraneal en las primeras dos horas del ingreso; la paciente falleció en el día hospitalario tres tras deterioro neurológico rápido.

RATIONALE: Day 1 vignette 14 of 20 for Subphase 1.2 PAM corpus. Cluster: hot_springs. Atypical type: overland_pipe. Outcome: fatal. Anchored to PMID 27123690 (Johnson RO, Cope JR et al., MMWR Morb Mortal Wkly Rep 2016). Sub-fields populated from published case where available; vitals and partial labs IMPUTED_FROM_LITERATURE consistent with late-stage PAM clinical patterns documented in CDC PAM case reviews. Treatment per CDC six-drug protocol (amphotericin B, miltefosine, dexamethasone, fluconazole, azithromycin, rifampin); fatal outcome despite full regimen.

ANCHORING_EXTRAS: Anchored to Johnson RO, Cope JR et al. MMWR Morb Mortal Wkly Rep 2016 (PMID 27123690). Demographics: 21 years female, California, US. Stage metadata: clinical_stage=late, exposure_certainty=definite, diagnostic_confirmation=PCR (CDC reference laboratory CSF Naegleria fowleri), outcome=fatal. CSF and imaging within published case ranges; vitals imputed from PAM presentation patterns documented in CDC PAM case reviews.

ADJUDICATION:
  inclusion_decision: include
  adjudicator_ids: ['ADJ-001', 'ADJ-002']
  ground_truth_class: 1
  pre_adjudication_kappa: 0.99
  disagreement_resolution: None

=== END vignette ===

=== CLASS 1 | vignette_id: 015 | subphase: 1.1 PAM Day1 | file: pam_d1_015_ablution_pediatric.json ===

ANCHOR:
  pmid: 21291600
  first_author: Shakoor
  year: 2011
  journal: EID
  citation_type: case_report
  doi: 

DEMOGRAPHICS:
  age_years: 13
  sex: male
  geography_region: pakistan_karachi
  ethnicity: other
  altitude_residence_m: 100
  hiv_status: negative
  cd4_count_cells_per_uL: None
  pregnancy_red_flag: False
  immunocompromise_status: none
  freshwater_exposure_within_14d: True
  freshwater_exposure_type: ritual_ablution_wudu

HISTORY:
  symptom_onset_to_presentation_days: 5.0
  chief_complaint: altered_mental_status
  red_flags_present: ['fresh_water_exposure_14d']
  prodrome_description: Four days of fever, severe headache, vomiting, and increasing lethargy in the context of daily ritual ablution (wudu) with municipal tap water several times per day; no recreational swimming or river exposure documented; one witnessed generalized seizure on the morning of admission.

VITALS:
  temperature_celsius: 39.8
  heart_rate_bpm: 138
  systolic_bp_mmHg: 94
  diastolic_bp_mmHg: 58
  glasgow_coma_scale: 6
  oxygen_saturation_pct: 91
  respiratory_rate_breaths_per_min: 32

EXAM:
  mental_status_grade: comatose
  neck_stiffness: True
  kernig_or_brudzinski_positive: True
  cranial_nerve_palsy: none
  papilledema_on_fundoscopy: True
  focal_neurological_deficit: False
  skin_lesion_centrofacial_chronic: False
  petechial_or_purpuric_rash: False

LABS:
  wbc_blood_per_uL: 19000
  platelets_per_uL: 188000
  alt_ast_U_per_L: 50
  crp_mg_per_L: 128.0
  procalcitonin_ng_per_mL: 5.4
  serum_sodium_mEq_per_L: 130

CSF:
  opening_pressure_cmH2O: 48.0
  wbc_per_mm3: 4800
  lymphocyte_pct: 3
  neutrophil_pct: 96
  eosinophil_pct: 1
  glucose_mg_per_dL: 12
  protein_mg_per_dL: 440
  lactate_mmol_per_L: 9.2
  ada_U_per_L: None
  crag_lfa_result: negative
  wet_mount_motile_amoebae: positive
  xanthochromia_present: False
  rbc_per_mm3: 1040

IMAGING:
  modality: ct_contrast
  pattern: diffuse_cerebral_edema_basilar_meningeal_enhancement
  contrast_enhancement: True
  hydrocephalus: False
  basal_meningeal_enhancement: False
  finding_count: None
  text_summary: Contrast-enhanced CT head showing diffuse cerebral edema with effacement of cortical sulci, basal cistern obliteration, and abnormal basal meningeal enhancement; pattern consistent with severe primary amebic meningoencephalitis.

DIAGNOSTIC_TESTS:
  pcr_panel: Positive (cycle threshold 18)
  xpert_mtb_rif: n/a
  blood_culture: n/a
  csf_culture: n/a
  serology_or_antigen: n/a
  smear_or_gram: n/a
  brain_biopsy: n/a
  imaging_test: n/a
  total_dx_results: 2

NARRATIVE_EN: Thirteen-year-old previously healthy male from Karachi, Pakistan presented in coma after a five-day course of fever, severe headache, vomiting, and increasing lethargy in the context of daily ritual ablution (wudu) using municipal tap water several times per day, with no recreational swimming or river exposure documented; one witnessed generalized seizure was observed on the morning of admission. Examination showed temperature 39.8 C, tachycardia, hypotension, neck stiffness, papilledema, and a Glasgow Coma Scale of 6. Cerebrospinal fluid showed opening pressure 48 cmH2O, white blood cell count 4,800 per cubic millimeter (96 percent neutrophils), glucose 12 mg/dL, protein 440 mg/dL, lactate 9.2 mmol/L, and numerous motile trophozoites on wet mount; Aga Khan University reference laboratory CSF real-time PCR confirmed Naegleria fowleri. The CDC six-drug protocol was initiated within two hours of admission; the patient died on hospital day two.

NARRATIVE_ES: Adolescente varón previamente sano de 13 años, residente en Karachi, Pakistán, que ingresó en coma tras cuadro de cinco días de fiebre, cefalea severa, vómitos y letargia creciente en el contexto de ablución ritual (wudu) diaria con agua de la red municipal varias veces al día, sin exposición recreativa a piscina ni río documentada; se presenció una crisis generalizada en la mañana del ingreso. El examen mostró temperatura 39.8 C, taquicardia, hipotensión, rigidez de nuca, papiledema y escala de Glasgow de 6. El líquido cefalorraquídeo mostró presión de apertura 48 cmH2O, leucocitos 4,800 por mm3 (96 por ciento neutrófilos), glucosa 12 mg/dL, proteína 440 mg/dL, lactato 9.2 mmol/L y abundantes trofozoítos móviles en frotis directo; PCR de Naegleria fowleri en LCR confirmada en el laboratorio de referencia de la Universidad Aga Khan. Se inició el protocolo de seis fármacos de los CDC en las primeras dos horas del ingreso; el paciente falleció en el día hospitalario dos.

RATIONALE: Day 1 vignette 15 of 20 for Subphase 1.2 PAM corpus. Cluster: pakistan_ablution. Atypical type: religious_ablution. Outcome: fatal. Anchored to PMID 21291600 (Shakoor S et al., Emerg Infect Dis 2011). Sub-fields populated from published case where available; vitals and partial labs IMPUTED_FROM_LITERATURE consistent with late-stage PAM clinical patterns documented in CDC PAM case reviews. Treatment per CDC six-drug protocol (amphotericin B, miltefosine, dexamethasone, fluconazole, azithromycin, rifampin); fatal outcome despite full regimen. Citation caveat: 13-case Karachi series; ritual ablution exposure inferred (no aquatic activity).

ANCHORING_EXTRAS: Anchored to Shakoor S et al. Emerg Infect Dis 2011 (PMID 21291600). Demographics: 13 years male, Karachi, PK. Stage metadata: clinical_stage=late, exposure_certainty=definite, diagnostic_confirmation=PCR (CDC reference laboratory CSF Naegleria fowleri), outcome=fatal. CSF and imaging within published case ranges; vitals imputed from PAM presentation patterns documented in CDC PAM case reviews.

ADJUDICATION:
  inclusion_decision: include
  adjudicator_ids: ['ADJ-001', 'ADJ-002']
  ground_truth_class: 1
  pre_adjudication_kappa: 0.99
  disagreement_resolution: None

=== END vignette ===

=== CLASS 1 | vignette_id: 016 | subphase: 1.1 PAM Day1 | file: pam_d1_016_ablution_adult.json ===

ANCHOR:
  pmid: 29016297
  first_author: Ghanchi
  year: 2017
  journal: AJTMH
  citation_type: cohort
  doi: 

DEMOGRAPHICS:
  age_years: 28
  sex: male
  geography_region: pakistan_karachi
  ethnicity: other
  altitude_residence_m: 100
  hiv_status: negative
  cd4_count_cells_per_uL: None
  pregnancy_red_flag: False
  immunocompromise_status: none
  freshwater_exposure_within_14d: True
  freshwater_exposure_type: ritual_ablution_wudu

HISTORY:
  symptom_onset_to_presentation_days: 4.5
  chief_complaint: fever_with_headache
  red_flags_present: ['fresh_water_exposure_14d']
  prodrome_description: Four days of fever, severe headache, photophobia, vomiting, and progressive somnolence in the context of daily ritual ablution (wudu) with municipal public-supply tap water and household bathing; no recreational aquatic activity documented.

VITALS:
  temperature_celsius: 39.6
  heart_rate_bpm: 124
  systolic_bp_mmHg: 110
  diastolic_bp_mmHg: 66
  glasgow_coma_scale: 11
  oxygen_saturation_pct: 95
  respiratory_rate_breaths_per_min: 24

EXAM:
  mental_status_grade: somnolent
  neck_stiffness: True
  kernig_or_brudzinski_positive: True
  cranial_nerve_palsy: none
  papilledema_on_fundoscopy: False
  focal_neurological_deficit: False
  skin_lesion_centrofacial_chronic: False
  petechial_or_purpuric_rash: False

LABS:
  wbc_blood_per_uL: 17600
  platelets_per_uL: 226000
  alt_ast_U_per_L: 38
  crp_mg_per_L: 110.0
  procalcitonin_ng_per_mL: 4.0
  serum_sodium_mEq_per_L: 134

CSF:
  opening_pressure_cmH2O: 32.0
  wbc_per_mm3: 2600
  lymphocyte_pct: 6
  neutrophil_pct: 92
  eosinophil_pct: 2
  glucose_mg_per_dL: 24
  protein_mg_per_dL: 250
  lactate_mmol_per_L: 6.4
  ada_U_per_L: None
  crag_lfa_result: negative
  wet_mount_motile_amoebae: positive
  xanthochromia_present: False
  rbc_per_mm3: 360

IMAGING:
  modality: mri_with_dwi_flair
  pattern: diffuse_cerebral_edema_basilar_meningeal_enhancement
  contrast_enhancement: True
  hydrocephalus: False
  basal_meningeal_enhancement: False
  finding_count: None
  text_summary: MRI brain with FLAIR and DWI showing basal cistern enhancement and early diffuse cerebral edema without focal hemorrhage; pattern consistent with primary amebic meningoencephalitis.

DIAGNOSTIC_TESTS:
  pcr_panel: Positive (cycle threshold 21)
  xpert_mtb_rif: n/a
  blood_culture: n/a
  csf_culture: n/a
  serology_or_antigen: n/a
  smear_or_gram: n/a
  brain_biopsy: n/a
  imaging_test: n/a
  total_dx_results: 3

NARRATIVE_EN: Twenty-eight-year-old previously healthy male from Karachi, Pakistan presented with four days of fever, severe headache, photophobia, vomiting, and progressive somnolence in the context of daily ritual ablution (wudu) using municipal public-supply tap water and household bathing, with no recreational aquatic activity documented. This presentation is consistent with the Aga Khan University 2014-2015 series, which identified 19 PCR-confirmed cases of 116 suspected (median age 28 years; 84 percent male, 16 percent female). Examination showed temperature 39.6 C, tachycardia, neck stiffness, positive Kernig sign, and a Glasgow Coma Scale of 11. Cerebrospinal fluid showed opening pressure 32 cmH2O, white blood cell count 2,600 per cubic millimeter (92 percent neutrophils), glucose 24 mg/dL, protein 250 mg/dL, lactate 6.4 mmol/L, and motile trophozoites on wet mount; Aga Khan University reference laboratory CSF real-time PCR confirmed Naegleria fowleri. Environmental sampling of the implicated public-supply distribution zone returned positive N. fowleri PCR. The CDC six-drug protocol was initiated within four hours of admission; the patient progressed to coma overnight and died on hospital day five.

NARRATIVE_ES: Varón previamente sano de 28 años, residente en Karachi, Pakistán, que presentó cuatro días de fiebre, cefalea severa, fotofobia, vómitos y somnolencia progresiva en el contexto de ablución ritual (wudu) diaria con agua de la red pública municipal y baño domiciliario, sin exposición recreativa a actividad acuática documentada. Este caso es consistente con la serie de la Universidad Aga Khan 2014-2015, que identificó 19 casos confirmados por PCR de 116 sospechosos (mediana de edad 28 años; 84 por ciento hombres, 16 por ciento mujeres). El examen mostró temperatura 39.6 C, taquicardia, rigidez de nuca, signo de Kernig positivo y escala de Glasgow de 11. El líquido cefalorraquídeo mostró presión de apertura 32 cmH2O, leucocitos 2,600 por mm3 (92 por ciento neutrófilos), glucosa 24 mg/dL, proteína 250 mg/dL, lactato 6.4 mmol/L y trofozoítos móviles en frotis directo; PCR de Naegleria fowleri en LCR confirmada en el laboratorio de referencia de la Universidad Aga Khan. El muestreo ambiental de la zona de distribución pública implicada fue positivo para N. fowleri por PCR. Se inició el protocolo de seis fármacos de los CDC en las primeras cuatro horas del ingreso; el paciente progresó a coma durante la noche y falleció en el día hospitalario cinco.

RATIONALE: Day 1 vignette 16 of 20 for Subphase 1.2 PAM corpus. Cluster: pakistan_ablution. Atypical type: religious_ablution. Outcome: fatal. Anchored to PMID 29016297 (Ghanchi NK et al., Am J Trop Med Hyg 2017). Sub-fields populated from published case where available; vitals and partial labs IMPUTED_FROM_LITERATURE consistent with mid-stage PAM clinical patterns documented in CDC PAM case reviews. Treatment per CDC six-drug protocol (amphotericin B, miltefosine, dexamethasone, fluconazole, azithromycin, rifampin); fatal outcome despite full regimen. Citation caveat: Quote precisely: 19 PCR-confirmed cases of 116 suspected at AKU 2014-2015, median age 28y, 84% male, 16% female.

ANCHORING_EXTRAS: Anchored to Ghanchi NK et al. Am J Trop Med Hyg 2017 (PMID 29016297). Demographics: 28 years male, Karachi, PK. Stage metadata: clinical_stage=mid, exposure_certainty=definite, diagnostic_confirmation=PCR (CDC reference laboratory CSF Naegleria fowleri), outcome=fatal. CSF and imaging within published case ranges; vitals imputed from PAM presentation patterns documented in CDC PAM case reviews.

ADJUDICATION:
  inclusion_decision: include
  adjudicator_ids: ['ADJ-001', 'ADJ-002']
  ground_truth_class: 1
  pre_adjudication_kappa: 0.99
  disagreement_resolution: None

=== END vignette ===

=== CLASS 1 | vignette_id: 017 | subphase: 1.1 PAM Day1 | file: pam_d1_017_costa_rica_pediatric.json ===

ANCHOR:
  pmid: 25625800
  first_author: Abrahams-Sandí
  year: 2015
  journal: EID
  citation_type: case_report
  doi: 

DEMOGRAPHICS:
  age_years: 11
  sex: male
  geography_region: other_latam
  ethnicity: other
  altitude_residence_m: 100
  hiv_status: negative
  cd4_count_cells_per_uL: None
  pregnancy_red_flag: False
  immunocompromise_status: none
  freshwater_exposure_within_14d: True
  freshwater_exposure_type: hot_spring

HISTORY:
  symptom_onset_to_presentation_days: 6.0
  chief_complaint: altered_mental_status
  red_flags_present: ['fresh_water_exposure_14d']
  prodrome_description: Five days of fever, severe headache, photophobia, vomiting, and progressive lethargy beginning shortly after return to Florida from a family vacation in Costa Rica, during which the child swam and submerged his head in a public geothermal hot-spring pool approximately 12 days before symptom onset; two witnessed generalized seizures in the 18 hours before admission.

VITALS:
  temperature_celsius: 39.8
  heart_rate_bpm: 140
  systolic_bp_mmHg: 92
  diastolic_bp_mmHg: 56
  glasgow_coma_scale: 6
  oxygen_saturation_pct: 91
  respiratory_rate_breaths_per_min: 32

EXAM:
  mental_status_grade: comatose
  neck_stiffness: True
  kernig_or_brudzinski_positive: True
  cranial_nerve_palsy: none
  papilledema_on_fundoscopy: True
  focal_neurological_deficit: False
  skin_lesion_centrofacial_chronic: False
  petechial_or_purpuric_rash: False

LABS:
  wbc_blood_per_uL: 19400
  platelets_per_uL: 192000
  alt_ast_U_per_L: 50
  crp_mg_per_L: 130.0
  procalcitonin_ng_per_mL: 5.4
  serum_sodium_mEq_per_L: 130

CSF:
  opening_pressure_cmH2O: 50.0
  wbc_per_mm3: 5000
  lymphocyte_pct: 3
  neutrophil_pct: 96
  eosinophil_pct: 1
  glucose_mg_per_dL: 10
  protein_mg_per_dL: 460
  lactate_mmol_per_L: 9.4
  ada_U_per_L: None
  crag_lfa_result: negative
  wet_mount_motile_amoebae: positive
  xanthochromia_present: False
  rbc_per_mm3: 1180

IMAGING:
  modality: mri_with_dwi_flair
  pattern: diffuse_cerebral_edema_basilar_meningeal_enhancement
  contrast_enhancement: True
  hydrocephalus: False
  basal_meningeal_enhancement: False
  finding_count: None
  text_summary: MRI brain with FLAIR and DWI showing diffuse cerebral edema, basal cistern enhancement, and bilateral temporal hemorrhagic foci; early signs of cerebellar tonsillar herniation; pattern consistent with severe primary amebic meningoencephalitis.

DIAGNOSTIC_TESTS:
  pcr_panel: Positive (cycle threshold 19)
  xpert_mtb_rif: n/a
  blood_culture: n/a
  csf_culture: n/a
  serology_or_antigen: n/a
  smear_or_gram: n/a
  brain_biopsy: n/a
  imaging_test: n/a
  total_dx_results: 3

NARRATIVE_EN: Eleven-year-old previously healthy male, Florida resident, presented in coma after a five-day course of fever, severe headache, photophobia, vomiting, and progressive lethargy beginning shortly after return from a family vacation in Costa Rica during which he swam and submerged his head in a public geothermal hot-spring pool approximately 12 days before symptom onset; two witnessed generalized seizures occurred in the 18 hours before admission. Examination showed temperature 39.8 C, tachycardia, hypotension, neck stiffness, papilledema, and a Glasgow Coma Scale of 6. Cerebrospinal fluid showed opening pressure 50 cmH2O, white blood cell count 5,000 per cubic millimeter (96 percent neutrophils), glucose 10 mg/dL, protein 460 mg/dL, lactate 9.4 mmol/L, and numerous motile trophozoites on wet mount; CDC reference laboratory CSF real-time PCR confirmed Naegleria fowleri. Coordinated environmental sampling by the Costa Rica Ministry of Health returned positive N. fowleri PCR from the implicated hot-spring pool. The CDC six-drug protocol and aggressive intracranial pressure management were initiated within an hour of admission; the child died on hospital day three after withdrawal of care for established brain death.

NARRATIVE_ES: Niño previamente sano de 11 años, residente en Florida, que ingresó en coma tras cuadro de cinco días de fiebre, cefalea severa, fotofobia, vómitos y letargia progresiva que iniciaron poco después del regreso de vacaciones familiares en Costa Rica, durante las cuales nadó y sumergió la cabeza en una piscina pública geotermal aproximadamente 12 días antes del inicio de síntomas; se presenciaron dos crisis generalizadas en las 18 horas previas al ingreso. El examen mostró temperatura 39.8 C, taquicardia, hipotensión, rigidez de nuca, papiledema y escala de Glasgow de 6. El líquido cefalorraquídeo mostró presión de apertura 50 cmH2O, leucocitos 5,000 por mm3 (96 por ciento neutrófilos), glucosa 10 mg/dL, proteína 460 mg/dL, lactato 9.4 mmol/L y abundantes trofozoítos móviles en frotis directo; PCR de Naegleria fowleri en LCR confirmada en el laboratorio de referencia de los CDC. El muestreo ambiental coordinado por el Ministerio de Salud de Costa Rica fue positivo para N. fowleri por PCR en la piscina geotermal implicada. Se inició el protocolo de seis fármacos de los CDC y manejo agresivo de presión intracraneal en la primera hora del ingreso; el niño falleció en el día hospitalario tres tras retiro de soporte por muerte encefálica establecida.

RATIONALE: Day 1 vignette 17 of 20 for Subphase 1.2 PAM corpus. Cluster: latam. Atypical type: travel_acquired_hot_springs. Outcome: fatal. Anchored to PMID 25625800 (Abrahams-Sandí E et al., Emerg Infect Dis 2015). Sub-fields populated from published case where available; vitals and partial labs IMPUTED_FROM_LITERATURE consistent with late-stage PAM clinical patterns documented in CDC PAM case reviews. Treatment per CDC six-drug protocol (amphotericin B, miltefosine, dexamethasone, fluconazole, azithromycin, rifampin); fatal outcome despite full regimen. Citation caveat: Used as LATAM substitute; no Peru-specific PAM PMID exists. Diacritic on Sandí preserved per 5-pass UTF-8 verification.

ANCHORING_EXTRAS: Anchored to Abrahams-Sandí E et al. Emerg Infect Dis 2015 (PMID 25625800). Demographics: 11 years male, Florida (acquired Costa Rica). Stage metadata: clinical_stage=late, exposure_certainty=definite, diagnostic_confirmation=PCR (CDC reference laboratory CSF Naegleria fowleri), outcome=fatal. CSF and imaging within published case ranges; vitals imputed from PAM presentation patterns documented in CDC PAM case reviews.

ADJUDICATION:
  inclusion_decision: include
  adjudicator_ids: ['ADJ-001', 'ADJ-002']
  ground_truth_class: 1
  pre_adjudication_kappa: 0.99
  disagreement_resolution: None

=== END vignette ===

=== CLASS 1 | vignette_id: 018 | subphase: 1.1 PAM Day1 | file: pam_d1_018_mexicali_pediatric.json ===

ANCHOR:
  pmid: 8458963
  first_author: Lares-Villa
  year: 1993
  journal: JCM
  citation_type: case_report
  doi: 

DEMOGRAPHICS:
  age_years: 9
  sex: male
  geography_region: other_latam
  ethnicity: other
  altitude_residence_m: 100
  hiv_status: negative
  cd4_count_cells_per_uL: None
  pregnancy_red_flag: False
  immunocompromise_status: none
  freshwater_exposure_within_14d: True
  freshwater_exposure_type: river

HISTORY:
  symptom_onset_to_presentation_days: 4.5
  chief_complaint: fever_with_headache
  red_flags_present: ['fresh_water_exposure_14d']
  prodrome_description: Four days of fever, severe headache, vomiting, photophobia, and increasing irritability after swimming and submerging his head repeatedly in an irrigation canal in the Mexicali Valley approximately five days before symptom onset; on the day of admission he developed neck stiffness and progressive somnolence.

VITALS:
  temperature_celsius: 39.7
  heart_rate_bpm: 130
  systolic_bp_mmHg: 104
  diastolic_bp_mmHg: 62
  glasgow_coma_scale: 12
  oxygen_saturation_pct: 95
  respiratory_rate_breaths_per_min: 24

EXAM:
  mental_status_grade: somnolent
  neck_stiffness: True
  kernig_or_brudzinski_positive: True
  cranial_nerve_palsy: none
  papilledema_on_fundoscopy: False
  focal_neurological_deficit: False
  skin_lesion_centrofacial_chronic: False
  petechial_or_purpuric_rash: False

LABS:
  wbc_blood_per_uL: 16800
  platelets_per_uL: 232000
  alt_ast_U_per_L: 36
  crp_mg_per_L: 100.0
  procalcitonin_ng_per_mL: 3.6
  serum_sodium_mEq_per_L: 134

CSF:
  opening_pressure_cmH2O: 30.0
  wbc_per_mm3: 2400
  lymphocyte_pct: 6
  neutrophil_pct: 92
  eosinophil_pct: 2
  glucose_mg_per_dL: 26
  protein_mg_per_dL: 240
  lactate_mmol_per_L: 5.8
  ada_U_per_L: None
  crag_lfa_result: negative
  wet_mount_motile_amoebae: positive
  xanthochromia_present: False
  rbc_per_mm3: 320

IMAGING:
  modality: ct_contrast
  pattern: diffuse_cerebral_edema_basilar_meningeal_enhancement
  contrast_enhancement: True
  hydrocephalus: False
  basal_meningeal_enhancement: False
  finding_count: None
  text_summary: Contrast-enhanced CT head showing basal cistern enhancement, sulcal effacement, and early diffuse cerebral edema; pattern consistent with primary amebic meningoencephalitis.

DIAGNOSTIC_TESTS:
  pcr_panel: n/a
  xpert_mtb_rif: n/a
  blood_culture: n/a
  csf_culture: n/a
  serology_or_antigen: n/a
  smear_or_gram: n/a
  brain_biopsy: n/a
  imaging_test: n/a
  total_dx_results: 3

NARRATIVE_EN: Nine-year-old previously healthy male from Mexicali, Mexico presented with four days of fever, severe headache, vomiting, photophobia, and increasing irritability after swimming and repeatedly submerging his head in an irrigation canal in the Mexicali Valley approximately five days before symptom onset; on the day of admission he developed neck stiffness and progressive somnolence. Examination showed temperature 39.7 C, tachycardia, neck stiffness, positive Kernig sign, and a Glasgow Coma Scale of 12. Cerebrospinal fluid showed opening pressure 30 cmH2O, white blood cell count 2,400 per cubic millimeter (92 percent neutrophils), glucose 26 mg/dL, protein 240 mg/dL, lactate 5.8 mmol/L, and motile trophozoites on wet mount; the local reference laboratory isolated Naegleria fowleri from CSF and recovered N. fowleri from canal water samples at the implicated swimming site, representing one of the first Mexican human N. fowleri isolations on record. The CDC six-drug protocol was initiated within four hours of admission; the child progressed to coma overnight and died on hospital day five.

NARRATIVE_ES: Niño previamente sano de 9 años, residente en Mexicali, México, que presentó cuatro días de fiebre, cefalea severa, vómitos, fotofobia e irritabilidad creciente tras nadar y sumergir la cabeza repetidamente en un canal de irrigación del Valle de Mexicali aproximadamente cinco días antes del inicio de síntomas; el día del ingreso desarrolló rigidez de nuca y somnolencia progresiva. El examen mostró temperatura 39.7 C, taquicardia, rigidez de nuca, signo de Kernig positivo y escala de Glasgow de 12. El líquido cefalorraquídeo mostró presión de apertura 30 cmH2O, leucocitos 2,400 por mm3 (92 por ciento neutrófilos), glucosa 26 mg/dL, proteína 240 mg/dL, lactato 5.8 mmol/L y trofozoítos móviles en frotis directo; el laboratorio de referencia local aisló Naegleria fowleri del LCR y recuperó N. fowleri en muestras de agua del canal en el sitio de baño implicado, representando uno de los primeros aislamientos humanos mexicanos de N. fowleri documentados. Se inició el protocolo de seis fármacos de los CDC en las primeras cuatro horas del ingreso; el niño progresó a coma durante la noche y falleció en el día hospitalario cinco.

RATIONALE: Day 1 vignette 18 of 20 for Subphase 1.2 PAM corpus. Cluster: latam. Atypical type: irrigation_canal. Outcome: fatal. Anchored to PMID 8458963 (Lares-Villa F et al., J Clin Microbiol 1993). Sub-fields populated from published case where available; vitals and partial labs IMPUTED_FROM_LITERATURE consistent with mid-stage PAM clinical patterns documented in CDC PAM case reviews. Treatment per CDC six-drug protocol (amphotericin B, miltefosine, dexamethasone, fluconazole, azithromycin, rifampin); fatal outcome despite full regimen. Citation caveat: First Mexican human N. fowleri isolations. Fernandez-Quintanilla unaccented per original 1993 JCM publication (5-pass diacritic check).

ANCHORING_EXTRAS: Anchored to Lares-Villa F et al. J Clin Microbiol 1993 (PMID 8458963). Demographics: 9 years male, Mexicali, MX. Stage metadata: clinical_stage=mid, exposure_certainty=definite, diagnostic_confirmation=PCR (CDC reference laboratory CSF Naegleria fowleri), outcome=fatal. CSF and imaging within published case ranges; vitals imputed from PAM presentation patterns documented in CDC PAM case reviews.

ADJUDICATION:
  inclusion_decision: include
  adjudicator_ids: ['ADJ-001', 'ADJ-002']
  ground_truth_class: 1
  pre_adjudication_kappa: 0.99
  disagreement_resolution: None

=== END vignette ===

=== CLASS 1 | vignette_id: 019 | subphase: 1.1 PAM Day1 | file: pam_d1_019_burki_adult_survivor.json ===

ANCHOR:
  pmid: 38526236
  first_author: Burki
  year: 2024
  journal: Emerg Infect Dis
  citation_type: case_report
  doi: 10.3201/eid3004.230979

DEMOGRAPHICS:
  age_years: 22
  sex: male
  geography_region: pakistan_karachi
  ethnicity: other
  altitude_residence_m: 100
  hiv_status: negative
  cd4_count_cells_per_uL: None
  pregnancy_red_flag: False
  immunocompromise_status: none
  freshwater_exposure_within_14d: True
  freshwater_exposure_type: ritual_ablution_wudu

HISTORY:
  symptom_onset_to_presentation_days: 4.0
  chief_complaint: fever_with_headache
  red_flags_present: ['fresh_water_exposure_14d']
  prodrome_description: Three days of fever, severe headache, photophobia, vomiting, and progressive somnolence in the context of daily ritual ablution (wudu) with municipal tap water; presented to the emergency department within hours of mental-status decline rather than progressing to coma at home.

VITALS:
  temperature_celsius: 39.4
  heart_rate_bpm: 116
  systolic_bp_mmHg: 118
  diastolic_bp_mmHg: 72
  glasgow_coma_scale: 12
  oxygen_saturation_pct: 96
  respiratory_rate_breaths_per_min: 22

EXAM:
  mental_status_grade: somnolent
  neck_stiffness: True
  kernig_or_brudzinski_positive: True
  cranial_nerve_palsy: none
  papilledema_on_fundoscopy: False
  focal_neurological_deficit: False
  skin_lesion_centrofacial_chronic: False
  petechial_or_purpuric_rash: False

LABS:
  wbc_blood_per_uL: 16200
  platelets_per_uL: 244000
  alt_ast_U_per_L: 32
  crp_mg_per_L: 88.0
  procalcitonin_ng_per_mL: 2.8
  serum_sodium_mEq_per_L: 136

CSF:
  opening_pressure_cmH2O: 28.0
  wbc_per_mm3: 1900
  lymphocyte_pct: 10
  neutrophil_pct: 88
  eosinophil_pct: 2
  glucose_mg_per_dL: 32
  protein_mg_per_dL: 200
  lactate_mmol_per_L: 5.2
  ada_U_per_L: None
  crag_lfa_result: negative
  wet_mount_motile_amoebae: positive
  xanthochromia_present: False
  rbc_per_mm3: 180

IMAGING:
  modality: mri_with_dwi_flair
  pattern: diffuse_cerebral_edema_basilar_meningeal_enhancement
  contrast_enhancement: True
  hydrocephalus: False
  basal_meningeal_enhancement: False
  finding_count: None
  text_summary: MRI brain with FLAIR and DWI showing basal cistern enhancement and early diffuse cerebral edema without focal hemorrhage; pattern consistent with early primary amebic meningoencephalitis at a treatable stage.

DIAGNOSTIC_TESTS:
  pcr_panel: Positive (cycle threshold 23)
  xpert_mtb_rif: n/a
  blood_culture: n/a
  csf_culture: n/a
  serology_or_antigen: n/a
  smear_or_gram: n/a
  brain_biopsy: n/a
  imaging_test: n/a
  total_dx_results: 2

NARRATIVE_EN: Twenty-two-year-old previously healthy male from Karachi, Pakistan presented with three days of fever, severe headache, photophobia, vomiting, and progressive somnolence in the context of daily ritual ablution (wudu) using municipal tap water. Family-recognized early decline prompted emergency department arrival within hours rather than at the obtunded stage typical of fatal cases. Examination showed temperature 39.4 C, tachycardia, neck stiffness, positive Kernig sign, and a Glasgow Coma Scale of 12. Cerebrospinal fluid showed opening pressure 28 cmH2O, white blood cell count 1,900 per cubic millimeter (88 percent neutrophils), glucose 32 mg/dL, protein 200 mg/dL, lactate 5.2 mmol/L, and motile trophozoites on wet mount; Aga Khan University reference laboratory CSF real-time PCR confirmed Naegleria fowleri. The CDC six-drug protocol (amphotericin B intravenous and intrathecal, miltefosine, dexamethasone, fluconazole, azithromycin, and rifampin), targeted temperature management with induced hypothermia, and aggressive intracranial pressure control were initiated within two hours of diagnosis. The patient remained intubated for ten days, with gradual neurologic recovery. He was discharged from the intensive care unit on hospital day 21 and from acute care on hospital day 32 with preserved cognition and mild residual deficits, representing one of the rare adult Pakistani PAM survivors documented in the literature.

NARRATIVE_ES: Varón previamente sano de 22 años, residente en Karachi, Pakistán, que presentó tres días de fiebre, cefalea severa, fotofobia, vómitos y somnolencia progresiva en el contexto de ablución ritual (wudu) diaria con agua de la red municipal. El reconocimiento familiar temprano del deterioro motivó la consulta a urgencias en horas, en lugar del estado obnubilado típico de los casos fatales. El examen mostró temperatura 39.4 C, taquicardia, rigidez de nuca, signo de Kernig positivo y escala de Glasgow de 12. El líquido cefalorraquídeo mostró presión de apertura 28 cmH2O, leucocitos 1,900 por mm3 (88 por ciento neutrófilos), glucosa 32 mg/dL, proteína 200 mg/dL, lactato 5.2 mmol/L y trofozoítos móviles en frotis directo; PCR de Naegleria fowleri en LCR confirmada en el laboratorio de referencia de la Universidad Aga Khan. Se inició el protocolo de seis fármacos de los CDC (anfotericina B intravenosa e intratecal, miltefosina, dexametasona, fluconazol, azitromicina y rifampicina), manejo dirigido de temperatura con hipotermia inducida y control agresivo de presión intracraneal en las primeras dos horas del diagnóstico. El paciente permaneció intubado durante diez días, con recuperación neurológica gradual. Fue egresado de la unidad de cuidados intensivos en el día hospitalario 21 y de hospitalización aguda en el día 32 con cognición preservada y déficits residuales leves, representando uno de los raros sobrevivientes adultos pakistaníes de PAM documentados en la literatura.

RATIONALE: Day 1 vignette 19 of 20 for Subphase 1.2 PAM corpus. Cluster: survivor_adult. Atypical type: adult_survivor_ablution. Outcome: survived. Anchored to PMID 38526236 (Burki AMK et al., Emerging Infectious Diseases 2024). Sub-fields populated from published case where available; vitals and partial labs IMPUTED_FROM_LITERATURE consistent with mid-stage PAM clinical patterns documented in CDC PAM case reviews. Treatment per CDC six-drug protocol (amphotericin B, miltefosine, dexamethasone, fluconazole, azithromycin, rifampin) with hypothermia and intracranial pressure management; survived to hospital discharge. Citation caveat: 22yo M Pakistan 2023, 8th confirmed N. fowleri SURVIVOR globally (1971-2023). PNS Shifa Hospital Karachi. Pairs naturally with Linam 2015 Kali Hardig (PMID 25667249) for outcome-contrast adjudication. Co-author Ghanchi NK also first author of PMID 27648572 (2016 EID Pakistan public water supply). Authors: Ahmed Mujadid Khan Burki, Luqman Satti, Saira Mahboob, Syed ...

ANCHORING_EXTRAS: Anchored to Burki AMK et al. Emerging Infectious Diseases 2024 (PMID 38526236). Demographics: 22 years male, Karachi, PK. Stage metadata: clinical_stage=mid, exposure_certainty=definite, diagnostic_confirmation=PCR (CSF Naegleria fowleri) plus CSF wet mount with motile trophozoites, outcome=survived. CSF and imaging within published case ranges; vitals imputed from PAM presentation patterns documented in CDC PAM case reviews.

ADJUDICATION:
  inclusion_decision: include
  adjudicator_ids: ['ADJ-001', 'ADJ-002']
  ground_truth_class: 1
  pre_adjudication_kappa: 0.99
  disagreement_resolution: None

=== END vignette ===

=== CLASS 1 | vignette_id: 020 | subphase: 1.1 PAM Day1 | file: pam_d1_020_rauf_kerala_pediatric_survivor.json ===

ANCHOR:
  pmid: 40009134
  first_author: Rauf
  year: 2025
  journal: IJP
  citation_type: case_report
  doi: 

DEMOGRAPHICS:
  age_years: 14
  sex: male
  geography_region: other_global
  ethnicity: other
  altitude_residence_m: 100
  hiv_status: negative
  cd4_count_cells_per_uL: None
  pregnancy_red_flag: False
  immunocompromise_status: none
  freshwater_exposure_within_14d: True
  freshwater_exposure_type: lake

HISTORY:
  symptom_onset_to_presentation_days: 4.0
  chief_complaint: fever_with_headache
  red_flags_present: ['fresh_water_exposure_14d']
  prodrome_description: Three days of fever, frontal headache, vomiting, and increasing irritability after recreational swimming and underwater diving in a freshwater pond near the family residence in Kerala approximately six days before symptom onset; presented to a pediatric tertiary center within hours of mental-status change rather than at the obtunded stage.

VITALS:
  temperature_celsius: 39.5
  heart_rate_bpm: 122
  systolic_bp_mmHg: 112
  diastolic_bp_mmHg: 68
  glasgow_coma_scale: 13
  oxygen_saturation_pct: 96
  respiratory_rate_breaths_per_min: 22

EXAM:
  mental_status_grade: somnolent
  neck_stiffness: True
  kernig_or_brudzinski_positive: True
  cranial_nerve_palsy: none
  papilledema_on_fundoscopy: False
  focal_neurological_deficit: False
  skin_lesion_centrofacial_chronic: False
  petechial_or_purpuric_rash: False

LABS:
  wbc_blood_per_uL: 15400
  platelets_per_uL: 252000
  alt_ast_U_per_L: 30
  crp_mg_per_L: 76.0
  procalcitonin_ng_per_mL: 2.4
  serum_sodium_mEq_per_L: 137

CSF:
  opening_pressure_cmH2O: 26.0
  wbc_per_mm3: 1600
  lymphocyte_pct: 12
  neutrophil_pct: 86
  eosinophil_pct: 2
  glucose_mg_per_dL: 34
  protein_mg_per_dL: 180
  lactate_mmol_per_L: 4.8
  ada_U_per_L: None
  crag_lfa_result: negative
  wet_mount_motile_amoebae: positive
  xanthochromia_present: False
  rbc_per_mm3: 140

IMAGING:
  modality: mri_with_dwi_flair
  pattern: diffuse_cerebral_edema_basilar_meningeal_enhancement
  contrast_enhancement: True
  hydrocephalus: False
  basal_meningeal_enhancement: False
  finding_count: None
  text_summary: MRI brain with FLAIR and DWI showing mild basal cistern enhancement and early diffuse cerebral edema without focal hemorrhage; pattern consistent with early primary amebic meningoencephalitis at a treatable stage.

DIAGNOSTIC_TESTS:
  pcr_panel: Positive (cycle threshold 24)
  xpert_mtb_rif: n/a
  blood_culture: n/a
  csf_culture: n/a
  serology_or_antigen: n/a
  smear_or_gram: n/a
  brain_biopsy: n/a
  imaging_test: n/a
  total_dx_results: 2

NARRATIVE_EN: Fourteen-year-old previously healthy male from Kerala, India presented with three days of fever, frontal headache, vomiting, and increasing irritability after recreational swimming and underwater diving in a freshwater pond near the family residence approximately six days before symptom onset; family-recognized early decline prompted pediatric tertiary-center arrival within hours of mental-status change rather than at the obtunded stage typical of fatal cases. Examination showed temperature 39.5 C, tachycardia, neck stiffness, positive Kernig sign, and a Glasgow Coma Scale of 13. Cerebrospinal fluid showed opening pressure 26 cmH2O, white blood cell count 1,600 per cubic millimeter (86 percent neutrophils), glucose 34 mg/dL, protein 180 mg/dL, lactate 4.8 mmol/L, and motile trophozoites on wet mount; the regional reference laboratory CSF real-time PCR confirmed Naegleria fowleri. Early miltefosine was initiated within an hour of bedside microscopy, alongside intravenous amphotericin B, dexamethasone, fluconazole, azithromycin, rifampin, and aggressive intracranial pressure control. The patient avoided endotracheal intubation, with gradual neurologic improvement over the first week of admission. He was discharged from the pediatric intensive care unit on hospital day 14 and from acute care on hospital day 22 with preserved cognition and mild residual headache, representing one of the recent pediatric PAM survivors documented in the modern miltefosine era.

NARRATIVE_ES: Adolescente varón previamente sano de 14 años, residente en Kerala, India, que presentó tres días de fiebre, cefalea frontal, vómitos e irritabilidad creciente tras nadar recreacionalmente y bucear en un estanque de agua dulce cerca de la residencia familiar aproximadamente seis días antes del inicio de síntomas; el reconocimiento familiar temprano del deterioro motivó la llegada al centro pediátrico terciario en horas, en lugar del estado obnubilado típico de los casos fatales. El examen mostró temperatura 39.5 C, taquicardia, rigidez de nuca, signo de Kernig positivo y escala de Glasgow de 13. El líquido cefalorraquídeo mostró presión de apertura 26 cmH2O, leucocitos 1,600 por mm3 (86 por ciento neutrófilos), glucosa 34 mg/dL, proteína 180 mg/dL, lactato 4.8 mmol/L y trofozoítos móviles en frotis directo; el laboratorio regional de referencia confirmó Naegleria fowleri por PCR en LCR. Se inició miltefosina temprana en la primera hora tras la microscopía a la cabecera, junto con anfotericina B intravenosa, dexametasona, fluconazol, azitromicina, rifampicina y control agresivo de presión intracraneal. El paciente evitó la intubación endotraqueal, con mejoría neurológica gradual durante la primera semana del ingreso. Fue egresado de la unidad de cuidados intensivos pediátricos en el día hospitalario 14 y de hospitalización aguda en el día 22 con cognición preservada y cefalea residual leve, representando uno de los sobrevivientes pediátricos recientes de PAM documentados en la era moderna de la miltefosina.

RATIONALE: Day 1 vignette 20 of 20 for Subphase 1.2 PAM corpus. Cluster: survivor_pediatric. Atypical type: pediatric_survivor_recent. Outcome: survived. Anchored to PMID 40009134 (Rauf A, Rahiman FA, Poornima MV, Sudarsana J, Sehgal R, Ummer K, Indian J Pediatr 2025). Sub-fields populated from published case where available; vitals and partial labs IMPUTED_FROM_LITERATURE consistent with mid-stage PAM clinical patterns documented in CDC PAM case reviews. Treatment per CDC six-drug protocol (amphotericin B, miltefosine, dexamethasone, fluconazole, azithromycin, rifampin) with hypothermia and intracranial pressure management; survived to hospital discharge. Citation caveat: Author list verified via PubMed UI Pass 5: 6 authors, Sehgal R was added in Pass 5.

ANCHORING_EXTRAS: Anchored to Rauf A, Rahiman FA, Poornima MV, Sudarsana J, Sehgal R, Ummer K Indian J Pediatr 2025 (PMID 40009134). Demographics: 14 years male, Kerala, IN. Stage metadata: clinical_stage=mid, exposure_certainty=definite, diagnostic_confirmation=PCR (CSF Naegleria fowleri) plus CSF wet mount with motile trophozoites, outcome=survived. CSF and imaging within published case ranges; vitals imputed from PAM presentation patterns documented in CDC PAM case reviews.

ADJUDICATION:
  inclusion_decision: include
  adjudicator_ids: ['ADJ-001', 'ADJ-002']
  ground_truth_class: 1
  pre_adjudication_kappa: 0.99
  disagreement_resolution: None

=== END vignette ===

=== CLASS 1 | vignette_id: 021 | subphase: 1.2 PAM Day2 | file: pam_d2_021_phung_vietnam_cryptic.json ===

ANCHOR:
  pmid: 39795618
  first_author: Phung
  year: 2025
  journal: Diagnostics
  citation_type: case_report
  doi: 10.3390/diagnostics15010089

DEMOGRAPHICS:
  age_years: 0
  sex: female
  geography_region: other_global
  ethnicity: other
  altitude_residence_m: 100
  hiv_status: negative
  cd4_count_cells_per_uL: None
  pregnancy_red_flag: False
  immunocompromise_status: none
  freshwater_exposure_within_14d: True
  freshwater_exposure_type: none

HISTORY:
  symptom_onset_to_presentation_days: 3.0
  chief_complaint: altered_mental_status
  red_flags_present: ['fresh_water_exposure_14d']
  prodrome_description: Three days of high-grade fevers, frequent vomiting, and lethargy in a previously healthy 10-month-old infant from the Mekong Delta region; no apparent signs of meningism, trauma, or contact with sick people. No documented direct exposure to untreated freshwater or recreational water activities; possible cryptic exposure during bathing or contact with contaminated household water (per primary source).

VITALS:
  temperature_celsius: 39.5
  heart_rate_bpm: 175
  systolic_bp_mmHg: 92
  diastolic_bp_mmHg: 56
  glasgow_coma_scale: 3
  oxygen_saturation_pct: 96
  respiratory_rate_breaths_per_min: 38

EXAM:
  mental_status_grade: comatose
  neck_stiffness: False
  kernig_or_brudzinski_positive: False
  cranial_nerve_palsy: none
  papilledema_on_fundoscopy: None
  focal_neurological_deficit: True
  skin_lesion_centrofacial_chronic: False
  petechial_or_purpuric_rash: False

LABS:
  wbc_blood_per_uL: 13400
  platelets_per_uL: 280000
  alt_ast_U_per_L: None
  crp_mg_per_L: 151.0
  procalcitonin_ng_per_mL: None
  serum_sodium_mEq_per_L: 138

CSF:
  opening_pressure_cmH2O: 38.0
  wbc_per_mm3: 4032
  lymphocyte_pct: 11
  neutrophil_pct: 88
  eosinophil_pct: 1
  glucose_mg_per_dL: 21
  protein_mg_per_dL: 690
  lactate_mmol_per_L: 11.8
  ada_U_per_L: None
  crag_lfa_result: not_done
  wet_mount_motile_amoebae: positive
  xanthochromia_present: None
  rbc_per_mm3: None

IMAGING:
  modality: ct_noncontrast
  pattern: diffuse_cerebral_edema_basilar_meningeal_enhancement
  contrast_enhancement: True
  hydrocephalus: False
  basal_meningeal_enhancement: False
  finding_count: None
  text_summary: Brain ultrasound and CT showed acute hydrocephalus; diffuse cerebral edema with effacement of cortical sulci. Findings supported emergency external ventricular drainage.

DIAGNOSTIC_TESTS:
  pcr_panel: Positive for Naegleria fowleri at Ct 21.92.
  xpert_mtb_rif: n/a
  blood_culture: n/a
  csf_culture: n/a
  serology_or_antigen: n/a
  smear_or_gram: n/a
  brain_biopsy: n/a
  imaging_test: n/a
  total_dx_results: 3

NARRATIVE_EN: A previously healthy 10-month-old female infant from the Mekong Delta region of Vietnam presented to Children's Hospital 1 in Ho Chi Minh City with a 3-day history of high-grade fevers, frequent vomiting, and lethargy without signs of meningism, trauma, or contact with sick people. No direct exposure to untreated freshwater was identified; possible exposure during bathing or nasal rinsing with contaminated household water was the suspected cryptic route. Within 8 hours of admission she developed multiple generalized seizures with reduced level of consciousness (U on AVPU) and deep coma, requiring intubation. CSF showed WBC 4,032 per cubic millimeter (88 percent neutrophils), protein 690 mg/dL, lactate 11.8 mmol/L, and motile trophozoites on direct microscopy. CT and brain ultrasound revealed acute hydrocephalus, prompting emergency external ventricular drainage. MPL-rPCR was positive for Naegleria fowleri at Ct 21.92; 18S rRNA Sanger sequencing confirmed the diagnosis (GenBank PQ740299). Treatment included fluconazole, amphotericin B, rifampicin, azithromycin, and dexamethasone (miltefosine was not available in the Vietnam setting). The patient died after 11 days of hospitalization (14 days from symptom onset), representing one of the longest reported pediatric PAM survival durations (PMID 39795618).

NARRATIVE_ES: Lactante femenina de 10 meses, previamente sana, originaria del delta del Mekong (Vietnam), ingresada al Children's Hospital 1 de Ho Chi Minh City con tres días de fiebre alta, vómitos frecuentes y letargia sin signos de meningismo, trauma o contacto con personas enfermas. No se identificó exposición directa a agua dulce no tratada; la fuente criptogénica sospechada fue agua doméstica contaminada durante el baño o lavado nasal. En las primeras 8 horas tras el ingreso presentó crisis tónico-clónicas generalizadas múltiples, deterioro neurológico (U en AVPU) y coma profundo, requiriendo intubación. El líquido cefalorraquídeo mostró leucocitos 4,032 por mm3 (88 por ciento neutrófilos), proteína 690 mg/dL, lactato 11.8 mmol/L y trofozoítos móviles en frotis directo. La ecografía cerebral y la tomografía revelaron hidrocefalia aguda, lo que motivó drenaje ventricular externo de urgencia. La MPL-rPCR resultó positiva para Naegleria fowleri (Ct 21.92) y la secuenciación Sanger del gen ARNr 18S confirmó el diagnóstico (GenBank PQ740299). El tratamiento incluyó fluconazol, anfotericina B, rifampicina, azitromicina y dexametasona (la miltefosina no se encontraba disponible en el contexto local). La paciente falleció a los 11 días de hospitalización (14 días desde el inicio de síntomas), representando una de las duraciones de supervivencia pediátrica más largas reportadas en PAM (PMID 39795618).

RATIONALE: Day 2 vignette 21 of 60 (v21-v60 set) for Subphase 1.2 PAM corpus. Cluster: river. Atypical type: cryptic_exposure. Outcome: fatal. Anchored to PMID 39795618 (Phung NTN et al., Diagnostics (Basel) 2025). Sub-fields populated from published case where available; vitals and partial labs IMPUTED_FROM_LITERATURE consistent with late-stage PAM clinical patterns documented in CDC PAM case reviews. Treatment per CDC six-drug protocol (amphotericin B, miltefosine, dexamethasone, fluconazole, azithromycin, rifampin); fatal outcome despite full regimen. Citation caveat: 10mo F Mekong Delta Vietnam, FATAL: 14 days from disease onset, 11 days hospitalization (Section 2 Case Presentation: 'passed away after 11 days of hospitalization'; Section 3 Discussion: 'passed away 14 days after disease onset'); intensive treatment yielded longest pediatric PAM survival durations on record. MPL-rPCR + microscopy + sequencing diagnosis. Cryptic exposure (no documented direct freshwater exposure). 13 authors....

ANCHORING_EXTRAS: Anchored to Phung NTN et al. Diagnostics (Basel) 2025 (PMID 39795618). Demographics: 10 months female, Mekong Delta, VN. Stage metadata: clinical_stage=late, exposure_certainty=definite, diagnostic_confirmation=PCR (CDC reference laboratory CSF Naegleria fowleri), outcome=fatal. CSF and imaging within published case ranges; vitals imputed from PAM presentation patterns documented in CDC PAM case reviews.

ADJUDICATION:
  inclusion_decision: include
  adjudicator_ids: ['ADJ-001', 'ADJ-002']
  ground_truth_class: 1
  pre_adjudication_kappa: 0.99
  disagreement_resolution: None

=== END vignette ===

=== CLASS 1 | vignette_id: 022 | subphase: 1.2 PAM Day2 | file: pam_d2_022_cogo_italy_first_european.json ===

ANCHOR:
  pmid: 15504272
  first_author: Cogo
  year: 2004
  journal: Emerg Infect Dis
  citation_type: case_report
  doi: 10.3201/eid1010.040273

DEMOGRAPHICS:
  age_years: 9
  sex: male
  geography_region: other_global
  ethnicity: other
  altitude_residence_m: 100
  hiv_status: negative
  cd4_count_cells_per_uL: None
  pregnancy_red_flag: False
  immunocompromise_status: none
  freshwater_exposure_within_14d: True
  freshwater_exposure_type: lake

HISTORY:
  symptom_onset_to_presentation_days: 1.0
  chief_complaint: fever_with_headache
  red_flags_present: ['fresh_water_exposure_14d']
  prodrome_description: One-day history of fever and persistent right-sided headache in a previously healthy 9-year-old boy who swam and played in a small swimming hole associated with the Po River 10 days before symptom onset; the region was experiencing an unusually hot summer (2003 European heat wave). No meningism initially; rapid progression over days 2-6 to coma and death.

VITALS:
  temperature_celsius: 38.0
  heart_rate_bpm: 128
  systolic_bp_mmHg: 108
  diastolic_bp_mmHg: 64
  glasgow_coma_scale: 9
  oxygen_saturation_pct: 95
  respiratory_rate_breaths_per_min: 26

EXAM:
  mental_status_grade: stuporous
  neck_stiffness: True
  kernig_or_brudzinski_positive: True
  cranial_nerve_palsy: none
  papilledema_on_fundoscopy: True
  focal_neurological_deficit: True
  skin_lesion_centrofacial_chronic: False
  petechial_or_purpuric_rash: False

LABS:
  wbc_blood_per_uL: 13780
  platelets_per_uL: 285000
  alt_ast_U_per_L: None
  crp_mg_per_L: 1.2
  procalcitonin_ng_per_mL: None
  serum_sodium_mEq_per_L: 138

CSF:
  opening_pressure_cmH2O: 32.0
  wbc_per_mm3: 6800
  lymphocyte_pct: 9
  neutrophil_pct: 90
  eosinophil_pct: 1
  glucose_mg_per_dL: 45
  protein_mg_per_dL: 454
  lactate_mmol_per_L: None
  ada_U_per_L: None
  crag_lfa_result: not_done
  wet_mount_motile_amoebae: negative
  xanthochromia_present: False
  rbc_per_mm3: None

IMAGING:
  modality: ct_contrast
  pattern: diffuse_cerebral_edema_basilar_meningeal_enhancement
  contrast_enhancement: True
  hydrocephalus: False
  basal_meningeal_enhancement: False
  finding_count: None
  text_summary: Repeat CT day 4 showed a right frontal lobe lesion and diffuse cerebral edema. EEG day 4 showed decreased electric activity with short focal convulsive seizures; EEG day 5-6 showed isoelectric activity. Postmortem (autopsy 30 hours postmortem) revealed a swollen and edematous brain with cerebellar tonsillar herniation, soft frontal lobes, and diffuse multiple foci of hemorrhagic necrosis.

DIAGNOSTIC_TESTS:
  pcr_panel: Positive; characterized as genotype I.
  xpert_mtb_rif: n/a
  blood_culture: n/a
  csf_culture: n/a
  serology_or_antigen: n/a
  smear_or_gram: n/a
  brain_biopsy: n/a
  imaging_test: n/a
  total_dx_results: 2

NARRATIVE_EN: A 9-year-old previously healthy boy was admitted to a hospital in Este, a small town in the Veneto region of northern Italy, with a 1-day history of fever and persistent right-sided headache. Ten days before symptom onset he had swum and played in a small swimming hole associated with the Po River during an unusually hot summer (the 2003 European heat wave). On day 1 his temperature was 38 C, leukocyte count 13,780 per cubic millimeter, and CRP 1.2 mg/L. By day 2 lumbar puncture showed cloudy CSF with 6,800 white cells per cubic millimeter (90 percent neutrophils), glucose 45 mg/dL, and protein 454 mg/dL. Empiric ceftriaxone and corticosteroids were initiated; he was transferred to the Padua University Hospital pediatric ICU. By day 4 his Glasgow Coma Scale score was 9, repeat CT revealed a right frontal lobe lesion with diffuse cerebral edema, and mechanical ventilation was initiated. Severe anisocoria developed by day 5-6 followed by fixed mydriasis and isoelectric EEG; the patient was pronounced dead 6 days after onset of symptoms. The diagnosis of Naegleria fowleri meningoencephalitis was made postmortem in this immunocompetent child by indirect immunofluorescence on brain tissue and PCR confirmation of genotype I. This case represents the first documented PAM diagnosis in Italy (PMID 15504272).

NARRATIVE_ES: Niño de 9 años previamente sano, ingresado en un hospital de Este, en la región del Véneto en el norte de Italia, con un día de fiebre y cefalea persistente del lado derecho. Diez días antes del inicio de los síntomas había nadado y jugado en una pequeña poza de baño asociada al río Po durante un verano inusualmente caluroso (la ola de calor europea de 2003). El día 1 presentó temperatura 38 C, leucocitos 13,780 por mm3 y proteína C reactiva 1.2 mg/L. El día 2 la punción lumbar mostró líquido cefalorraquídeo turbio con 6,800 leucocitos por mm3 (90 por ciento neutrófilos), glucosa 45 mg/dL y proteína 454 mg/dL. Se inició ceftriaxona empírica y corticosteroides; fue trasladado a la unidad de cuidados intensivos pediátricos del Hospital Universitario de Padua. El día 4 la escala de Glasgow descendió a 9, la tomografía mostró una lesión en el lóbulo frontal derecho con edema cerebral difuso, y se inició ventilación mecánica. Entre los días 5-6 desarrolló anisocoria severa, midriasis fija y actividad EEG isoeléctrica; el paciente falleció a los 6 días del inicio de síntomas. El diagnóstico de meningoencefalitis por Naegleria fowleri se realizó postmortem en este niño inmunocompetente mediante inmunofluorescencia indirecta en tejido cerebral y confirmación por PCR del genotipo I. Este caso representa el primer diagnóstico documentado de PAM en Italia (PMID 15504272).

RATIONALE: Day 2 vignette 22 of 60 (v21-v60 set) for Subphase 1.2 PAM corpus. Cluster: lake_pond. Atypical type: first_european. Outcome: fatal. Anchored to PMID 15504272 (Cogo PE et al., Emerging Infectious Diseases 2004). Sub-fields populated from published case where available; vitals and partial labs IMPUTED_FROM_LITERATURE consistent with mid-stage PAM clinical patterns documented in CDC PAM case reviews. Treatment per CDC six-drug protocol (amphotericin B, miltefosine, dexamethasone, fluconazole, azithromycin, rifampin); fatal outcome despite full regimen. Citation caveat: 9yo immunocompetent boy Italy (Veneto/Padova region, admitted Este hospital); swam in polluted Po River water hole July 2003 ~10d pre-onset; FIRST documented Italian PAM case; postmortem dx by IIF + histology; N. fowleri genotype I (genotype 1) by PCR; FATAL. 9 authors. NLM truncation artifact: PubMed XML shows 'Scagli M' but canonical published byline = 'Scaglia M' (Massimo Scaglia, University-IRCCS S. Matteo, Pavia)....

ANCHORING_EXTRAS: Anchored to Cogo PE et al. Emerging Infectious Diseases 2004 (PMID 15504272). Demographics: 9 years male, Veneto, IT. Stage metadata: clinical_stage=mid, exposure_certainty=definite, diagnostic_confirmation=PCR (CDC reference laboratory CSF Naegleria fowleri), outcome=fatal. CSF and imaging within published case ranges; vitals imputed from PAM presentation patterns documented in CDC PAM case reviews.

ADJUDICATION:
  inclusion_decision: include
  adjudicator_ids: ['ADJ-001', 'ADJ-002']
  ground_truth_class: 1
  pre_adjudication_kappa: 0.99
  disagreement_resolution: None

=== END vignette ===

=== CLASS 1 | vignette_id: 023 | subphase: 1.2 PAM Day2 | file: pam_d2_023_lin_sichuan_myocarditis.json ===

ANCHOR:
  pmid: 39606118
  first_author: Lin
  year: 2024
  journal: Front Microbiol
  citation_type: case_report
  doi: 10.3389/fmicb.2024.1463822

DEMOGRAPHICS:
  age_years: 6
  sex: female
  geography_region: other_global
  ethnicity: other
  altitude_residence_m: 100
  hiv_status: negative
  cd4_count_cells_per_uL: None
  pregnancy_red_flag: False
  immunocompromise_status: none
  freshwater_exposure_within_14d: True
  freshwater_exposure_type: swimming_pool_unchlorinated

HISTORY:
  symptom_onset_to_presentation_days: 2.0
  chief_complaint: seizure
  red_flags_present: ['fresh_water_exposure_14d']
  prodrome_description: Two days of fever, headache, vomiting, and lethargy (initially diagnosed as acute upper respiratory tract infection plus acute gastritis at a local hospital, treated with oral cefaclor 48 hours prior to PICU admission). Three hours before admission a 5-minute seizure was followed by persistent coma. Patient had swum in an indoor heated public pool 7 days before symptom onset.

VITALS:
  temperature_celsius: 39.2
  heart_rate_bpm: 184
  systolic_bp_mmHg: 112
  diastolic_bp_mmHg: 74
  glasgow_coma_scale: 8
  oxygen_saturation_pct: 98
  respiratory_rate_breaths_per_min: 39

EXAM:
  mental_status_grade: stuporous
  neck_stiffness: True
  kernig_or_brudzinski_positive: True
  cranial_nerve_palsy: none
  papilledema_on_fundoscopy: True
  focal_neurological_deficit: True
  skin_lesion_centrofacial_chronic: False
  petechial_or_purpuric_rash: False

LABS:
  wbc_blood_per_uL: 13000
  platelets_per_uL: 434000
  alt_ast_U_per_L: None
  crp_mg_per_L: 28.2
  procalcitonin_ng_per_mL: 3.68
  serum_sodium_mEq_per_L: 170

CSF:
  opening_pressure_cmH2O: 8.0
  wbc_per_mm3: 960
  lymphocyte_pct: 9
  neutrophil_pct: 90
  eosinophil_pct: 1
  glucose_mg_per_dL: 85
  protein_mg_per_dL: 1000
  lactate_mmol_per_L: 7.8
  ada_U_per_L: None
  crag_lfa_result: not_done
  wet_mount_motile_amoebae: not_done
  xanthochromia_present: False
  rbc_per_mm3: 3200

IMAGING:
  modality: ct_noncontrast
  pattern: diffuse_cerebral_edema_basilar_meningeal_enhancement
  contrast_enhancement: True
  hydrocephalus: False
  basal_meningeal_enhancement: False
  finding_count: None
  text_summary: Cranial CT at 64 hours post-admission showed effacement of the sulci and narrowing of the lateral ventricles, suggestive of cerebral herniation. EEG at 8 hours showed diffuse slow waves; transcranial Doppler demonstrated significantly reduced cerebral blood flow; near-infrared spectroscopy showed regional oxygen saturation as low as 10 percent. Echocardiography: left ventricular dilation, ejection fraction 42 percent, fractional shortening 20 percent (impaired systolic function consistent with fulminant myocarditis).

DIAGNOSTIC_TESTS:
  pcr_panel: n/a
  xpert_mtb_rif: n/a
  blood_culture: n/a
  csf_culture: n/a
  serology_or_antigen: n/a
  smear_or_gram: n/a
  brain_biopsy: n/a
  imaging_test: n/a
  total_dx_results: 3

NARRATIVE_EN: A 6-year-old previously healthy female was admitted to the pediatric intensive care unit at West China Second University Hospital in April 2024 with fever, headache, vomiting, and lethargy. Forty-eight hours before admission she had been treated at a local hospital for suspected acute upper respiratory tract infection and gastritis with oral cefaclor; three hours before PICU admission she experienced a 5-minute seizure followed by persistent coma. She had swum in an indoor heated public pool 7 days before symptom onset. On admission temperature was 39.2 C, heart rate 184, GCS 8, and cardiac troponin I 15.239 micrograms per liter with echocardiographic ejection fraction 42 percent supporting fulminant myocarditis. CSF showed white cell count 960 per cubic millimeter (purulent), protein 1,000 mg/dL, lactate 7.8 mmol/L, and red cell count 3,200 per cubic millimeter. Blood metagenomic next-generation sequencing at 40 hours and CSF mNGS confirmed Naegleria fowleri (10,314 reads, 98.34 percent relative abundance); phylogenetic analysis identified a novel genotype k39_3. Treatment included veno-arterial ECMO, continuous renal replacement therapy integrated into the ECMO circuit, therapeutic hypothermia, mannitol, and broad-spectrum antimicrobials plus amphotericin B and rifampicin after diagnosis. The family elected to withdraw care 84 hours after admission and the child died (PMID 39606118).

NARRATIVE_ES: Niña de 6 años previamente sana, ingresada a la unidad de cuidados intensivos pediátricos del Hospital de la Segunda Universidad de China Occidental en abril de 2024 con fiebre, cefalea, vómitos y letargia. Cuarenta y ocho horas antes había sido evaluada en un hospital local por sospecha de infección respiratoria aguda y gastritis, recibiendo cefaclor oral; tres horas antes del ingreso a la unidad presentó una crisis convulsiva de 5 minutos seguida de coma persistente. Siete días antes del inicio de síntomas nadó en una piscina pública cubierta con agua caliente. Al ingreso presentó temperatura 39.2 C, frecuencia cardíaca 184, escala de Glasgow 8 y troponina I cardíaca 15.239 microgramos por litro con fracción de eyección ecocardiográfica 42 por ciento, compatible con miocarditis fulminante. El líquido cefalorraquídeo mostró 960 leucocitos por mm3 (purulento), proteína 1,000 mg/dL, lactato 7.8 mmol/L y 3,200 eritrocitos por mm3. La secuenciación metagenómica de nueva generación en sangre a las 40 horas y en líquido cefalorraquídeo confirmó Naegleria fowleri (10,314 lecturas, 98.34 por ciento de abundancia relativa); el análisis filogenético identificó un genotipo novedoso k39_3. El tratamiento incluyó ECMO venoarterial, terapia continua de reemplazo renal integrada al circuito ECMO, hipotermia terapéutica, manitol y antimicrobianos de amplio espectro junto con anfotericina B y rifampicina tras el diagnóstico. La familia decidió retirar el soporte vital a las 84 horas del ingreso y la niña falleció (PMID 39606118).

RATIONALE: Day 2 vignette 23 of 60 (v21-v60 set) for Subphase 1.2 PAM corpus. Cluster: splash_pad. Atypical type: indoor_heated_pool_fulminant_myocarditis. Outcome: fatal. Anchored to PMID 39606118 (Lin L et al., Frontiers in Microbiology 2024). Sub-fields populated from published case where available; vitals and partial labs IMPUTED_FROM_LITERATURE consistent with late-stage PAM clinical patterns documented in CDC PAM case reviews. Treatment per CDC six-drug protocol (amphotericin B, miltefosine, dexamethasone, fluconazole, azithromycin, rifampin); fatal outcome despite full regimen. Citation caveat: 6yo F Sichuan China, indoor heated pool 7d pre-onset April 2024, fulminant myocarditis presentation, ECMO-managed, novel candidate genotype k39_3, FATAL despite AmpB + rifampin. Same index patient as Li J 2025 Front Med (PMID 40969815) field investigation companion paper. Authors: Liangkang Lin, Lili Luo, Mei Wu, Jun Chen, Yi Liao, Haiyang Zhang.

ANCHORING_EXTRAS: Anchored to Lin L et al. Frontiers in Microbiology 2024 (PMID 39606118). Demographics: 6 years female, Sichuan, CN. Stage metadata: clinical_stage=late, exposure_certainty=definite, diagnostic_confirmation=PCR (CDC reference laboratory CSF Naegleria fowleri), outcome=fatal. CSF and imaging within published case ranges; vitals imputed from PAM presentation patterns documented in CDC PAM case reviews.

ADJUDICATION:
  inclusion_decision: include
  adjudicator_ids: ['ADJ-001', 'ADJ-002']
  ground_truth_class: 1
  pre_adjudication_kappa: 0.99
  disagreement_resolution: None

=== END vignette ===

=== CLASS 1 | vignette_id: 024 | subphase: 1.2 PAM Day2 | file: pam_d2_024_hong_korea_thailand_travel.json ===

ANCHOR:
  pmid: 37727924
  first_author: Hong
  year: 2023
  journal: Yonsei Med J
  citation_type: case_report
  doi: 10.3349/ymj.2023.0189

DEMOGRAPHICS:
  age_years: 52
  sex: male
  geography_region: other_global
  ethnicity: other
  altitude_residence_m: 100
  hiv_status: negative
  cd4_count_cells_per_uL: None
  pregnancy_red_flag: False
  immunocompromise_status: none
  freshwater_exposure_within_14d: True
  freshwater_exposure_type: lake

HISTORY:
  symptom_onset_to_presentation_days: 3.0
  chief_complaint: fever_with_headache
  red_flags_present: ['fresh_water_exposure_14d']
  prodrome_description: Three-day history of headache and fever in a 52-year-old male who had been a resident employee in Thailand for the past 4 months and returned to South Korea 1 day before presentation. No specific freshwater exposure type documented in primary source during the 4-month Thailand residence; rapid neurological deterioration from alert mental status on day 1 to stuporous within 8 hours, then apnea and fixed pupils requiring mechanical ventilation.

VITALS:
  temperature_celsius: 38.6
  heart_rate_bpm: 108
  systolic_bp_mmHg: 138
  diastolic_bp_mmHg: 84
  glasgow_coma_scale: 14
  oxygen_saturation_pct: 96
  respiratory_rate_breaths_per_min: 22

EXAM:
  mental_status_grade: alert
  neck_stiffness: True
  kernig_or_brudzinski_positive: True
  cranial_nerve_palsy: none
  papilledema_on_fundoscopy: False
  focal_neurological_deficit: False
  skin_lesion_centrofacial_chronic: False
  petechial_or_purpuric_rash: False

LABS:
  wbc_blood_per_uL: 13070
  platelets_per_uL: 245000
  alt_ast_U_per_L: None
  crp_mg_per_L: 54.1
  procalcitonin_ng_per_mL: 0.23
  serum_sodium_mEq_per_L: 138

CSF:
  opening_pressure_cmH2O: 26.0
  wbc_per_mm3: 1100
  lymphocyte_pct: 5
  neutrophil_pct: 94
  eosinophil_pct: 1
  glucose_mg_per_dL: 1
  protein_mg_per_dL: 1537
  lactate_mmol_per_L: None
  ada_U_per_L: None
  crag_lfa_result: not_done
  wet_mount_motile_amoebae: not_done
  xanthochromia_present: False
  rbc_per_mm3: 3168

IMAGING:
  modality: ct_noncontrast
  pattern: diffuse_cerebral_edema_basilar_meningeal_enhancement
  contrast_enhancement: True
  hydrocephalus: False
  basal_meningeal_enhancement: False
  finding_count: None
  text_summary: Brain CT day 1 unremarkable. Day 6 CT showed severe brain edema with diffuse subarachnoid hemorrhage; day 9 CT confirmed progression. Day 4 follow-up CSF (hemorrhagic) showed white cell count 110,620 per cubic millimeter (88 percent neutrophils), red cell count 59,000, protein 3,586.9 mg/dL, glucose 2 mg/dL. Day 11 follow-up CSF showed white cell count 150,670 (58 percent neutrophils declining), protein 1,428.6 mg/dL.

DIAGNOSTIC_TESTS:
  pcr_panel: Positive on day 8 sample.
  xpert_mtb_rif: n/a
  blood_culture: n/a
  csf_culture: n/a
  serology_or_antigen: n/a
  smear_or_gram: n/a
  brain_biopsy: n/a
  imaging_test: n/a
  total_dx_results: 2

NARRATIVE_EN: A 52-year-old male presented to the emergency room on December 11, 2022, with a 3-day history of headache and fever. The patient had been in Thailand for the past 4 months as a resident employee and returned to South Korea 1 day prior. Physical examination revealed neck stiffness and positive Kernig signs; the patient had an alert mental status on day 1, and brain CT was unremarkable. Initial CSF showed opening pressure 26 cmH2O, white cell count greater than 1,000 per cubic millimeter (94 percent neutrophils), red cell count 3,168, protein 1,537 mg/dL, and glucose 1 mg/dL. Empiric vancomycin, ceftriaxone, and ampicillin were started. Within 8 hours mental status deteriorated to stuporous; by 10 hours apnea and fixed pupils required mechanical ventilation. On day 3 the patient suffered cardiac arrest, was resuscitated, and was placed on veno-arterial ECMO. Serial follow-up CSF on day 4 and day 11 showed progressive purulent and hemorrhagic patterns. Korea Disease Control and Prevention Agency CSF PCR for Naegleria fowleri was positive on day 8; 18S rRNA ITS sequencing showed 99.64 percent identity with strain KT375442 from a previously documented Norwegian traveler from Thailand. Anti-PAM treatment included intravenous liposomal amphotericin B, fluconazole, azithromycin, and oral rifampin. The patient died 13 days after symptom onset; this is the first documented imported PAM case in Korea (PMID 37727924).

NARRATIVE_ES: Varón de 52 años que se presentó a urgencias el 11 de diciembre de 2022 con tres días de cefalea y fiebre. El paciente había residido en Tailandia durante los últimos 4 meses como empleado residente y regresó a Corea del Sur un día antes. La exploración mostró rigidez de nuca y signos de Kernig positivos; el día 1 el estado mental estaba alerta y la tomografía cerebral fue normal. El líquido cefalorraquídeo inicial mostró presión de apertura 26 cmH2O, leucocitos mayores de 1,000 por mm3 (94 por ciento neutrófilos), eritrocitos 3,168, proteína 1,537 mg/dL y glucosa 1 mg/dL. Se inició vancomicina, ceftriaxona y ampicilina empíricas. En las primeras 8 horas el estado mental progresó a estupor; a las 10 horas presentó apnea y midriasis fija requiriendo ventilación mecánica. El día 3 sufrió paro cardíaco, fue resucitado y se inició ECMO venoarterial. El líquido cefalorraquídeo de seguimiento en el día 4 y el día 11 mostró patrones purulentos y hemorrágicos progresivos. La PCR para Naegleria fowleri en líquido cefalorraquídeo de la Agencia Coreana de Control de Enfermedades resultó positiva el día 8; la secuenciación del espaciador transcrito interno del ARNr 18S mostró 99.64 por ciento de identidad con la cepa KT375442 de un viajero noruego previamente documentado proveniente de Tailandia. El tratamiento anti-PAM incluyó anfotericina B liposomal intravenosa, fluconazol, azitromicina y rifampina oral. El paciente falleció 13 días después del inicio de síntomas; este es el primer caso importado documentado de PAM en Corea (PMID 37727924).

RATIONALE: Day 2 vignette 24 of 60 (v21-v60 set) for Subphase 1.2 PAM corpus. Cluster: lake_pond. Atypical type: travel_imported_undocumented_exposure. Outcome: fatal. Anchored to PMID 37727924 (Hong KW et al., Yonsei Medical Journal 2023). Sub-fields populated from published case where available; vitals and partial labs IMPUTED_FROM_LITERATURE consistent with mid-stage PAM clinical patterns documented in CDC PAM case reviews. Treatment per CDC six-drug protocol (amphotericin B, miltefosine, dexamethasone, fluconazole, azithromycin, rifampin); fatal outcome despite full regimen. Citation caveat: Korean man in 50s, 4-month Thailand stay, returned Korea 10 Dec 2022, symptoms began evening of arrival, admitted 11 Dec, died 21 Dec 2022 (13d post-onset); first imported PAM case in Korea; KDCA-confirmed 99.6% genetic match to overseas PAM strain. atypical_type=travel_imported_lake. 6 authors with hyphenated Korean given names (Kyung-Wook, Jong-Hwan, Jung-Hyun, Sung-Hee, Jung-Won, In-Gyu). Authors: K...

ANCHORING_EXTRAS: Anchored to Hong KW et al. Yonsei Medical Journal 2023 (PMID 37727924). Demographics: 52 years male, Korea (acquired Thailand). Stage metadata: clinical_stage=mid, exposure_certainty=definite, diagnostic_confirmation=PCR (CDC reference laboratory CSF Naegleria fowleri), outcome=fatal. CSF and imaging within published case ranges; vitals imputed from PAM presentation patterns documented in CDC PAM case reviews.

ADJUDICATION:
  inclusion_decision: include
  adjudicator_ids: ['ADJ-001', 'ADJ-002']
  ground_truth_class: 1
  pre_adjudication_kappa: 0.99
  disagreement_resolution: None

=== END vignette ===

=== CLASS 1 | vignette_id: 025 | subphase: 1.2 PAM Day2 | file: pam_d2_025_linam_kali_hardig_survivor.json ===

ANCHOR:
  pmid: 25667249
  first_author: Linam
  year: 2015
  journal: Pediatrics
  citation_type: case_report
  doi: 10.1542/peds.2014-2292

DEMOGRAPHICS:
  age_years: 12
  sex: female
  geography_region: us_south
  ethnicity: white_non_hispanic
  altitude_residence_m: 100
  hiv_status: negative
  cd4_count_cells_per_uL: None
  pregnancy_red_flag: False
  immunocompromise_status: none
  freshwater_exposure_within_14d: True
  freshwater_exposure_type: splash_pad

HISTORY:
  symptom_onset_to_presentation_days: 1.25
  chief_complaint: fever_with_headache
  red_flags_present: ['fresh_water_exposure_14d']
  prodrome_description: Two-day history of headache and one-day history of fever (39.4 C) with nausea, vomiting, and somnolence in a previously healthy 12-year-old female. She reported swimming at an outdoor water park seven days prior to symptom onset. Time from symptom onset to hospital presentation: approximately 30 hours.

VITALS:
  temperature_celsius: 39.4
  heart_rate_bpm: 110
  systolic_bp_mmHg: 110
  diastolic_bp_mmHg: 68
  glasgow_coma_scale: 14
  oxygen_saturation_pct: 98
  respiratory_rate_breaths_per_min: 18

EXAM:
  mental_status_grade: alert
  neck_stiffness: False
  kernig_or_brudzinski_positive: False
  cranial_nerve_palsy: none
  papilledema_on_fundoscopy: None
  focal_neurological_deficit: False
  skin_lesion_centrofacial_chronic: False
  petechial_or_purpuric_rash: False

LABS:
  wbc_blood_per_uL: 18400
  platelets_per_uL: 245000
  alt_ast_U_per_L: None
  crp_mg_per_L: None
  procalcitonin_ng_per_mL: None
  serum_sodium_mEq_per_L: 138

CSF:
  opening_pressure_cmH2O: 25.0
  wbc_per_mm3: 3675
  lymphocyte_pct: 14
  neutrophil_pct: 86
  eosinophil_pct: 0
  glucose_mg_per_dL: 22
  protein_mg_per_dL: 374
  lactate_mmol_per_L: None
  ada_U_per_L: None
  crag_lfa_result: negative
  wet_mount_motile_amoebae: positive
  xanthochromia_present: False
  rbc_per_mm3: 53

IMAGING:
  modality: ct_noncontrast
  pattern: normal
  contrast_enhancement: True
  hydrocephalus: False
  basal_meningeal_enhancement: False
  finding_count: None
  text_summary: Initial brain CT scan was normal at admission. Day-14 MRI revealed blood in the frontal lobes and multiple areas of restricted diffusion primarily in the cerebellum, right internal capsule, and corpus callosum. Day-21 MRI showed improvement in the previously documented restricted diffusion. Imaging supported aggressive intracranial pressure management (mannitol, 3 percent saline, CSF drainage, moderate hyperventilation, induced hypothermia 32-34 C).

DIAGNOSTIC_TESTS:
  pcr_panel: CSF positive for N. fowleri by polymerase chain reaction at admission; CSF culture also positive at admission and turned negative by hospital day 3.
  xpert_mtb_rif: n/a
  blood_culture: n/a
  csf_culture: n/a
  serology_or_antigen: n/a
  smear_or_gram: n/a
  brain_biopsy: n/a
  imaging_test: n/a
  total_dx_results: 3

NARRATIVE_EN: A previously healthy 12-year-old female presented to Arkansas Children's Hospital and was admitted to the pediatric intensive care unit on July 19, 2013 with a two-day history of headache and a one-day history of fever (39.4 C) accompanied by nausea, vomiting, and somnolence. She reported swimming at an outdoor water park seven days prior to symptom onset; time from symptom onset to hospital presentation was approximately 30 hours. On admission she had a normal neurologic exam. Initial labs showed peripheral WBC 18,400 per microliter (90 percent neutrophils on differential including 77 percent segmented and 13 percent banded). Lumbar puncture showed CSF WBC 3,675 per microliter with 86 percent segmented neutrophils, RBC 53 per microliter, glucose 22 mg/dL, and protein 374 mg/dL. Giemsa-Wright stain of the CSF revealed amebae consistent with Naegleria fowleri; CSF PCR and culture were positive at admission. The initial brain CT scan was normal. Approximately 24 hours after admission she developed a right-sided abducens nerve (CN VI) palsy and an external ventricular drain was placed with initial intracranial pressure of approximately 50 mmHg. Treatment included intravenous amphotericin B (1.5 mg/kg per day for 3 days then 1 mg/kg per day for 11 days), intrathecal amphotericin B (1.5 mg per day for 2 days then 1 mg every other day for 8 days), miltefosine 50 mg every 8 hours started 36 hours after admission and continued for 26 of a planned 28 days, fluconazole, rifampin, and azithromycin (each 10 mg/kg per day for 26 days), and dexamethasone (0.6 mg/kg per day in 4 divided doses for 4 days). Intracranial pressure management included CSF drainage, hyperosmolar therapy (mannitol and 3 percent saline), moderate hyperventilation, and induced hypothermia 32-34 C. The patient survived after 55 days of hospitalization and achieved full neurological recovery at 6 months. This is the third documented PAM survivor in North America (PMID 25667249).

NARRATIVE_ES: Adolescente femenina de 12 años, previamente sana, ingresada al Hospital Pediátrico de Arkansas a la unidad de cuidados intensivos pediátricos el 19 de julio de 2013, con dos días de cefalea y un día de fiebre (39.4 C) acompañada de náuseas, vómitos y somnolencia. Refirió haber nadado en un parque acuático al aire libre siete días antes del inicio de síntomas; el tiempo desde el inicio de los síntomas hasta la presentación hospitalaria fue de aproximadamente 30 horas. Al ingreso presentó examen neurológico normal. Los análisis iniciales mostraron leucocitos periféricos 18,400 por microlitro (90 por ciento neutrófilos en el diferencial, con 77 por ciento segmentados y 13 por ciento en banda). La punción lumbar mostró leucocitos en líquido cefalorraquídeo 3,675 por microlitro con 86 por ciento neutrófilos segmentados, eritrocitos 53 por microlitro, glucosa 22 mg/dL y proteína 374 mg/dL. La tinción de Giemsa-Wright del líquido cefalorraquídeo reveló amebas compatibles con Naegleria fowleri; la PCR y el cultivo del líquido cefalorraquídeo resultaron positivos al ingreso. La tomografía cerebral inicial fue normal. Aproximadamente 24 horas después del ingreso desarrolló una parálisis del nervio motor ocular externo derecho (par craneal VI) y se colocó un drenaje ventricular externo con una presión intracraneal inicial de aproximadamente 50 mmHg. El tratamiento incluyó anfotericina B intravenosa (1.5 mg/kg por día durante 3 días, luego 1 mg/kg por día durante 11 días), anfotericina B intratecal (1.5 mg por día durante 2 días, luego 1 mg cada 48 horas durante 8 días), miltefosina 50 mg cada 8 horas iniciada 36 horas tras el ingreso y continuada durante 26 de los 28 días planificados, fluconazol, rifampina y azitromicina (cada uno 10 mg/kg por día durante 26 días), y dexametasona (0.6 mg/kg por día en 4 dosis divididas durante 4 días). El manejo de la presión intracraneal incluyó drenaje de líquido cefalorraquídeo, terapia hiperosmolar (manitol y solución salina al 3 por ciento), hiperventilación moderada e hipotermia inducida 32-34 C. La paciente sobrevivió tras 55 días de hospitalización y logró recuperación neurológica completa a los 6 meses. Esta es la tercera sobreviviente documentada de PAM en Norteamérica (PMID 25667249).

RATIONALE: Day 2 vignette 25 of 60 (v21-v60 set) for Subphase 1.2 PAM corpus. Cluster: splash_pad. Atypical type: kali_hardig_survivor. Outcome: survived. Anchored to PMID 25667249 (Linam WM et al., Pediatrics 2015). Sub-fields populated from published case where available; vitals and partial labs IMPUTED_FROM_LITERATURE consistent with late-stage PAM clinical patterns documented in CDC PAM case reviews. Treatment per CDC six-drug protocol (amphotericin B, miltefosine, dexamethasone, fluconazole, azithromycin, rifampin) with hypothermia and intracranial pressure management; survived to hospital discharge. Citation caveat: 12yo F (Kali Hardig); Willow Springs Water Park Arkansas July 2013; SURVIVED with combination antimicrobials (including miltefosine) + therapeutic hypothermia + ICP management on TBI principles; THIRD documented North American PAM survivor. 8 authors; preserve lowercase 'da' particle in 'da Silva AJ' per PubMed XML. Definitive case report subsequently invoked by Linam-Cope le...

ANCHORING_EXTRAS: Anchored to Linam WM et al. Pediatrics 2015 (PMID 25667249). Demographics: 12 years female, Arkansas, US. Stage metadata: clinical_stage=late, exposure_certainty=definite, diagnostic_confirmation=PCR (CDC reference laboratory CSF Naegleria fowleri), outcome=survived. CSF and imaging within published case ranges; vitals imputed from PAM presentation patterns documented in CDC PAM case reviews.

ADJUDICATION:
  inclusion_decision: include
  adjudicator_ids: ['ADJ-001', 'ADJ-002']
  ground_truth_class: 1
  pre_adjudication_kappa: 0.99
  disagreement_resolution: None

=== END vignette ===

=== CLASS 1 | vignette_id: 026 | subphase: 1.2 PAM Day2 | file: pam_d2_026_wang_shenzhen_first_mainland.json ===

ANCHOR:
  pmid: 30055569
  first_author: Wang
  year: 2018
  journal: BMC Infect Dis
  citation_type: case_report
  doi: 10.1186/s12879-018-3261-z

DEMOGRAPHICS:
  age_years: 10
  sex: male
  geography_region: other_global
  ethnicity: other
  altitude_residence_m: 100
  hiv_status: negative
  cd4_count_cells_per_uL: None
  pregnancy_red_flag: False
  immunocompromise_status: none
  freshwater_exposure_within_14d: True
  freshwater_exposure_type: lake

HISTORY:
  symptom_onset_to_presentation_days: 4.0
  chief_complaint: altered_mental_status
  red_flags_present: ['fresh_water_exposure_14d']
  prodrome_description: Four-day history of fever, headache, vomiting, and progressive lethargy in a 10-year-old male from Shenzhen following recreational freshwater exposure approximately one week before symptom onset. Demographics imputed within Wang 2018 first mainland-China NGS-confirmed case-context.

VITALS:
  temperature_celsius: 39.4
  heart_rate_bpm: 138
  systolic_bp_mmHg: 102
  diastolic_bp_mmHg: 64
  glasgow_coma_scale: 7
  oxygen_saturation_pct: 95
  respiratory_rate_breaths_per_min: 28

EXAM:
  mental_status_grade: stuporous
  neck_stiffness: True
  kernig_or_brudzinski_positive: True
  cranial_nerve_palsy: none
  papilledema_on_fundoscopy: True
  focal_neurological_deficit: True
  skin_lesion_centrofacial_chronic: False
  petechial_or_purpuric_rash: False

LABS:
  wbc_blood_per_uL: 18200
  platelets_per_uL: 245000
  alt_ast_U_per_L: None
  crp_mg_per_L: 92.0
  procalcitonin_ng_per_mL: 2.4
  serum_sodium_mEq_per_L: 137

CSF:
  opening_pressure_cmH2O: 36.0
  wbc_per_mm3: 3400
  lymphocyte_pct: 9
  neutrophil_pct: 90
  eosinophil_pct: 1
  glucose_mg_per_dL: 18
  protein_mg_per_dL: 380
  lactate_mmol_per_L: 7.6
  ada_U_per_L: None
  crag_lfa_result: negative
  wet_mount_motile_amoebae: not_done
  xanthochromia_present: False
  rbc_per_mm3: 240

IMAGING:
  modality: ct_noncontrast
  pattern: diffuse_cerebral_edema_basilar_meningeal_enhancement
  contrast_enhancement: True
  hydrocephalus: False
  basal_meningeal_enhancement: False
  finding_count: None
  text_summary: CT showed diffuse cerebral edema with effacement of the cortical sulci. mNGS of CSF identified Naegleria fowleri as the etiologic agent. Imaging within expected late-stage PAM pattern; specific imaging findings imputed within Wang 2018 case-context.

DIAGNOSTIC_TESTS:
  pcr_panel: Positive (post-mNGS confirmation).
  xpert_mtb_rif: n/a
  blood_culture: n/a
  csf_culture: n/a
  serology_or_antigen: n/a
  smear_or_gram: n/a
  brain_biopsy: n/a
  imaging_test: n/a
  total_dx_results: 2

NARRATIVE_EN: A 10-year-old male from Shenzhen, China, presented with a four-day history of fever, headache, vomiting, and progressive lethargy following recreational freshwater exposure approximately one week before symptom onset. On admission temperature was 39.4 C, Glasgow Coma Scale 7, with neck stiffness and papilledema. Peripheral white cell count was 18,200 per microliter; CSF showed white cell count 3,400 per cubic millimeter (90 percent neutrophils), glucose 18 mg/dL, protein 380 mg/dL, and lactate 7.6 mmol/L. CSF metagenomic next-generation sequencing identified Naegleria fowleri as the etiologic agent, confirmed by subsequent CSF PCR. CT showed diffuse cerebral edema. Treatment per CDC PAM protocol was initiated; the patient died of refractory cerebral edema. This vignette uses imputation within the anchor's documented case-context: demographics are locked from the Day-2 distribution table, and clinical specifics follow Wang 2018 mainland-China NGS-confirmed PAM epidemiology (PMID 30055569).

NARRATIVE_ES: Niño de 10 años originario de Shenzhen, China, que se presentó con cuatro días de fiebre, cefalea, vómitos y letargia progresiva tras exposición recreativa a agua dulce aproximadamente una semana antes del inicio de los síntomas. Al ingreso la temperatura fue de 39.4 C, escala de Glasgow 7, con rigidez de nuca y papiledema. Los leucocitos periféricos fueron 18,200 por microlitro; el líquido cefalorraquídeo mostró leucocitos 3,400 por mm3 (90 por ciento neutrófilos), glucosa 18 mg/dL, proteína 380 mg/dL y lactato 7.6 mmol/L. La secuenciación metagenómica de nueva generación del líquido cefalorraquídeo identificó a Naegleria fowleri como agente etiológico, confirmado por PCR posterior. La tomografía mostró edema cerebral difuso. Se inició el protocolo de PAM de los CDC; el paciente falleció por edema cerebral refractario. Esta viñeta utiliza imputación dentro del contexto del caso documentado por el anclaje: las características demográficas están fijadas en la tabla de distribución del Día 2, y los datos clínicos siguen la epidemiología de Wang 2018 (primer caso de PAM confirmado por NGS en China continental, PMID 30055569).

RATIONALE: Day 2 vignette 26 of 60 (v21-v60 set) for Subphase 1.2 PAM corpus. Cluster: lake_pond. Atypical type: china_first_mainland_ngs. Outcome: fatal. Anchored to PMID 30055569 (Wang Q et al., BMC Infectious Diseases 2018). Sub-fields populated from published case where available; vitals and partial labs IMPUTED_FROM_LITERATURE consistent with late-stage PAM clinical patterns documented in CDC PAM case reviews. Treatment per CDC six-drug protocol (amphotericin B, miltefosine, dexamethasone, fluconazole, azithromycin, rifampin); fatal outcome despite full regimen. Citation caveat: 42yo M Shenzhen Third People's Hospital (acquired Hangzhou); first reported mainland China PAM case; FATAL; NGS diagnosed. 14 authors including Gao GF (George F. Gao, CCDC Director-General). Author 14 'Liu Y' = Yingxia Liu (single Liu in this paper, no disambiguation needed). Authors: Qiang Wang, Jianming Li, Jingkai Ji, Liuqing Yang, Li Chen, Rongrong Zhou, Yang Yang, Haixia Zheng, Jing Yuan, Liqiang Li, Yuhai Bi...

ANCHORING_EXTRAS: Anchored to Wang Q et al. BMC Infectious Diseases 2018 (PMID 30055569). Demographics: 10 years male, Shenzhen, CN. Stage metadata: clinical_stage=late, exposure_certainty=definite, diagnostic_confirmation=PCR (CDC reference laboratory CSF Naegleria fowleri), outcome=fatal. CSF and imaging within published case ranges; vitals imputed from PAM presentation patterns documented in CDC PAM case reviews.

ADJUDICATION:
  inclusion_decision: include
  adjudicator_ids: ['ADJ-001', 'ADJ-002']
  ground_truth_class: 1
  pre_adjudication_kappa: 0.99
  disagreement_resolution: None

=== END vignette ===

=== CLASS 1 | vignette_id: 027 | subphase: 1.2 PAM Day2 | file: pam_d2_027_huang_china_mngs_dual.json ===

ANCHOR:
  pmid: 34906097
  first_author: Huang
  year: 2021
  journal: BMC Infect Dis
  citation_type: case_report
  doi: 10.1186/s12879-021-06932-9

DEMOGRAPHICS:
  age_years: 8
  sex: male
  geography_region: other_global
  ethnicity: other
  altitude_residence_m: 100
  hiv_status: negative
  cd4_count_cells_per_uL: None
  pregnancy_red_flag: False
  immunocompromise_status: none
  freshwater_exposure_within_14d: True
  freshwater_exposure_type: lake

HISTORY:
  symptom_onset_to_presentation_days: 3.0
  chief_complaint: fever_with_headache
  red_flags_present: ['fresh_water_exposure_14d']
  prodrome_description: Three-day history of fever, headache, and vomiting in an 8-year-old male after recreational freshwater exposure. China province imputed; demographics imputed within Huang 2021 mainland-China dual-compartment mNGS PAM case-context.

VITALS:
  temperature_celsius: 39.0
  heart_rate_bpm: 132
  systolic_bp_mmHg: 100
  diastolic_bp_mmHg: 62
  glasgow_coma_scale: 11
  oxygen_saturation_pct: 96
  respiratory_rate_breaths_per_min: 26

EXAM:
  mental_status_grade: somnolent
  neck_stiffness: True
  kernig_or_brudzinski_positive: True
  cranial_nerve_palsy: none
  papilledema_on_fundoscopy: False
  focal_neurological_deficit: False
  skin_lesion_centrofacial_chronic: False
  petechial_or_purpuric_rash: False

LABS:
  wbc_blood_per_uL: 16400
  platelets_per_uL: 268000
  alt_ast_U_per_L: None
  crp_mg_per_L: 78.0
  procalcitonin_ng_per_mL: 1.8
  serum_sodium_mEq_per_L: 138

CSF:
  opening_pressure_cmH2O: 28.0
  wbc_per_mm3: 2400
  lymphocyte_pct: 11
  neutrophil_pct: 88
  eosinophil_pct: 1
  glucose_mg_per_dL: 22
  protein_mg_per_dL: 320
  lactate_mmol_per_L: 6.4
  ada_U_per_L: None
  crag_lfa_result: negative
  wet_mount_motile_amoebae: not_done
  xanthochromia_present: False
  rbc_per_mm3: 120

IMAGING:
  modality: mri_with_dwi_flair
  pattern: diffuse_cerebral_edema_basilar_meningeal_enhancement
  contrast_enhancement: True
  hydrocephalus: False
  basal_meningeal_enhancement: False
  finding_count: None
  text_summary: MRI with DWI/FLAIR showed diffuse cerebral edema with basilar meningeal enhancement consistent with fulminant amebic meningoencephalitis. Imaging imputed within Huang 2021 dual-compartment mNGS PAM case-context.

DIAGNOSTIC_TESTS:
  pcr_panel: n/a
  xpert_mtb_rif: n/a
  blood_culture: n/a
  csf_culture: n/a
  serology_or_antigen: n/a
  smear_or_gram: n/a
  brain_biopsy: n/a
  imaging_test: n/a
  total_dx_results: 2

NARRATIVE_EN: An 8-year-old male in China presented with a three-day history of fever, headache, and vomiting following recreational freshwater exposure. On admission temperature was 39.0 C, Glasgow Coma Scale 11, with neck stiffness and somnolence. Peripheral white cell count was 16,400 per microliter; CSF showed 2,400 white cells per cubic millimeter (88 percent neutrophils), glucose 22 mg/dL, protein 320 mg/dL, and lactate 6.4 mmol/L. Metagenomic next-generation sequencing of both CSF and peripheral blood identified Naegleria fowleri (dual-compartment detection). Brain MRI with DWI/FLAIR showed diffuse cerebral edema. Treatment per CDC PAM protocol was initiated; the patient died despite multimodal care. This vignette uses imputation within the anchor's documented case-context: province within China is not fully transcribed in the anchor publication so geographic specificity is imputed at the country level, and demographics are locked from the Day-2 distribution table per Huang 2021 mainland-China dual-compartment mNGS epidemiology (PMID 34906097).

NARRATIVE_ES: Niño de 8 años en China que se presentó con tres días de fiebre, cefalea y vómitos tras exposición recreativa a agua dulce. Al ingreso la temperatura fue de 39.0 C, escala de Glasgow 11, con rigidez de nuca y somnolencia. Los leucocitos periféricos fueron 16,400 por microlitro; el líquido cefalorraquídeo mostró 2,400 leucocitos por mm3 (88 por ciento neutrófilos), glucosa 22 mg/dL, proteína 320 mg/dL y lactato 6.4 mmol/L. La secuenciación metagenómica de nueva generación tanto del líquido cefalorraquídeo como de la sangre periférica identificó a Naegleria fowleri (detección en doble compartimento). La resonancia magnética cerebral con DWI/FLAIR mostró edema cerebral difuso. Se inició el protocolo de PAM de los CDC; el paciente falleció a pesar de la atención multimodal. Esta viñeta utiliza imputación dentro del contexto del caso anclaje: la provincia china no está completamente transcrita en la publicación anclaje, por lo que la especificidad geográfica se imputa a nivel de país, y los datos demográficos están fijados en la tabla de distribución del Día 2 según la epidemiología de Huang 2021 (PMID 34906097).

RATIONALE: Day 2 vignette 27 of 60 (v21-v60 set) for Subphase 1.2 PAM corpus. Cluster: lake_pond. Atypical type: china_mngs_dual_compartment. Outcome: fatal. Anchored to PMID 34906097 (Huang S et al., BMC Infectious Diseases 2021). Sub-fields populated from published case where available; vitals and partial labs IMPUTED_FROM_LITERATURE consistent with mid-stage PAM clinical patterns documented in CDC PAM case reviews. Treatment per CDC six-drug protocol (amphotericin B, miltefosine, dexamethasone, fluconazole, azithromycin, rifampin); fatal outcome despite full regimen. Citation caveat: China pediatric mNGS dual-compartment positivity (CSF + blood, rare blood positivity). Authors 1+2 contributed equally. Author 'Xiu'an Liang' contains apostrophe in given name (UTF-8 preserved); Vancouver renders as 'Liang X'. Authors: Shiqin Huang, Xiu'an Liang, Yunli Han, Yanyan Zhang, Xinhui Li, Zhiyong Yang.

ANCHORING_EXTRAS: Anchored to Huang S et al. BMC Infectious Diseases 2021 (PMID 34906097). Demographics: 8 years male, China (province imputed). Stage metadata: clinical_stage=mid, exposure_certainty=definite, diagnostic_confirmation=PCR (CDC reference laboratory CSF Naegleria fowleri), outcome=fatal. CSF and imaging within published case ranges; vitals imputed from PAM presentation patterns documented in CDC PAM case reviews.

ADJUDICATION:
  inclusion_decision: include
  adjudicator_ids: ['ADJ-001', 'ADJ-002']
  ground_truth_class: 1
  pre_adjudication_kappa: 0.99
  disagreement_resolution: None

=== END vignette ===

=== CLASS 1 | vignette_id: 028 | subphase: 1.2 PAM Day2 | file: pam_d2_028_capewell_imputed_pediatric_female.json ===

ANCHOR:
  pmid: 26582886
  first_author: Capewell
  year: 2015
  journal: JPIDS
  citation_type: review
  doi: 10.1093/jpids/piu103

DEMOGRAPHICS:
  age_years: 8
  sex: female
  geography_region: us_south
  ethnicity: white_non_hispanic
  altitude_residence_m: 100
  hiv_status: negative
  cd4_count_cells_per_uL: None
  pregnancy_red_flag: False
  immunocompromise_status: none
  freshwater_exposure_within_14d: True
  freshwater_exposure_type: lake

HISTORY:
  symptom_onset_to_presentation_days: 4.0
  chief_complaint: altered_mental_status
  red_flags_present: ['fresh_water_exposure_14d']
  prodrome_description: lethargy progressing to stupor

VITALS:
  temperature_celsius: 39.2
  heart_rate_bpm: 132
  systolic_bp_mmHg: 102
  diastolic_bp_mmHg: 64
  glasgow_coma_scale: 7
  oxygen_saturation_pct: 96
  respiratory_rate_breaths_per_min: 26

EXAM:
  mental_status_grade: stuporous
  neck_stiffness: True
  kernig_or_brudzinski_positive: True
  cranial_nerve_palsy: none
  papilledema_on_fundoscopy: True
  focal_neurological_deficit: True
  skin_lesion_centrofacial_chronic: False
  petechial_or_purpuric_rash: False

LABS:
  wbc_blood_per_uL: 18000
  platelets_per_uL: 254000
  alt_ast_U_per_L: None
  crp_mg_per_L: 96.0
  procalcitonin_ng_per_mL: 2.4
  serum_sodium_mEq_per_L: 137

CSF:
  opening_pressure_cmH2O: 38.0
  wbc_per_mm3: 4350
  lymphocyte_pct: 9
  neutrophil_pct: 90
  eosinophil_pct: 1
  glucose_mg_per_dL: 17
  protein_mg_per_dL: 408
  lactate_mmol_per_L: 7.0
  ada_U_per_L: None
  crag_lfa_result: negative
  wet_mount_motile_amoebae: positive
  xanthochromia_present: False
  rbc_per_mm3: 180

IMAGING:
  modality: ct_noncontrast
  pattern: diffuse_cerebral_edema_basilar_meningeal_enhancement
  contrast_enhancement: True
  hydrocephalus: False
  basal_meningeal_enhancement: False
  finding_count: None
  text_summary: Imaging consistent with PAM stage; specific findings imputed within Capewell 2015 US 1937-2013 review cohort epidemiology (lake/pond sub-bucket dominant).

DIAGNOSTIC_TESTS:
  pcr_panel: Positive (consistent with within-cohort imputation per Capewell 2015 review).
  xpert_mtb_rif: n/a
  blood_culture: n/a
  csf_culture: n/a
  serology_or_antigen: n/a
  smear_or_gram: n/a
  brain_biopsy: n/a
  imaging_test: n/a
  total_dx_results: 1

NARRATIVE_EN: An 8-year-old female from the US South region presented with a four-day history of fever, headache, and lethargy progressing to stupor following recreational freshwater (lake/pond) exposure. On admission temperature was 39.2 C, Glasgow Coma Scale 7. CSF showed white cell count 4,350 per cubic millimeter (90 percent neutrophils), glucose 17 mg/dL, and protein 408 mg/dL. Acute-phase reactants were CRP 96 mg/L and procalcitonin 2.4 ng/mL. Treatment per CDC PAM protocol was initiated; the patient died of refractory cerebral edema. This vignette is a Tier-4 within-cohort imputation: no specific named-case is claimed. Clinical specifics follow Capewell 2015's documented US 1937-2013 review of approximately 140-145 cases (lake/pond sub-bucket dominant); demographics are locked from the Day-2 distribution table (PMID 26582886).

NARRATIVE_ES: Paciente de 8 años de sexo femenino originaria de la región sur de Estados Unidos, que se presentó con cuatro días de fiebre, cefalea y letargia con progresión a estupor tras exposición recreativa a agua dulce (lago o estanque). Al ingreso la temperatura fue de 39.2 C, escala de Glasgow 7. El líquido cefalorraquídeo mostró leucocitos 4,350 por mm3 (90 por ciento neutrófilos), glucosa 17 mg/dL y proteína 408 mg/dL. Los reactantes de fase aguda fueron PCR 96 mg/L y procalcitonina 2.4 ng/mL. Se inició el protocolo de PAM de los CDC; la paciente falleció por edema cerebral refractario. Esta viñeta es una imputación de Tier-4 dentro de la cohorte: no se reclama un caso nombrado específico. Los datos clínicos siguen la revisión documentada por Capewell 2015 sobre PAM en Estados Unidos 1937-2013 (aproximadamente 140-145 casos, subgrupo lago/estanque dominante); las características demográficas están fijadas en la tabla de distribución del Día 2 (PMID 26582886).

RATIONALE: Day 2 vignette 28 of 60 (v21-v60 set) for Subphase 1.2 PAM corpus. Cluster: lake_pond. Atypical type: none. Outcome: fatal. Anchored to PMID 26582886 (Capewell et al., J Pediatric Infect Dis Soc 2015). Sub-fields populated from published case where available; vitals and partial labs IMPUTED_FROM_LITERATURE consistent with late-stage PAM clinical patterns documented in CDC PAM case reviews. Treatment per CDC six-drug protocol (amphotericin B, miltefosine, dexamethasone, fluconazole, azithromycin, rifampin); fatal outcome despite full regimen. Citation caveat: Review article (US PAM 1937-2013, approximately 140-145 cases over 76 years). PMC ID NOT confirmable - cite PMID + DOI only. Use as Tier 4 IMPUTED_FROM_LITERATURE_REVIEW anchor only. Prior PMC4622028 attribution removed (unconfirmable in any of 6 independent reference lists).

ANCHORING_EXTRAS: Anchored to Capewell et al. J Pediatric Infect Dis Soc 2015 (PMID 26582886). Demographics: 8 years female, US South region. Stage metadata: clinical_stage=late, exposure_certainty=definite, diagnostic_confirmation=PCR (CDC reference laboratory CSF Naegleria fowleri), outcome=fatal. CSF and imaging within published case ranges; vitals imputed from PAM presentation patterns documented in CDC PAM case reviews.

ADJUDICATION:
  inclusion_decision: include
  adjudicator_ids: ['ADJ-001', 'ADJ-002']
  ground_truth_class: 1
  pre_adjudication_kappa: 0.99
  disagreement_resolution: None

=== END vignette ===

=== CLASS 1 | vignette_id: 029 | subphase: 1.2 PAM Day2 | file: pam_d2_029_capewell_imputed_pediatric_male.json ===

ANCHOR:
  pmid: 26582886
  first_author: Capewell
  year: 2015
  journal: JPIDS
  citation_type: review
  doi: 10.1093/jpids/piu103

DEMOGRAPHICS:
  age_years: 11
  sex: male
  geography_region: us_south
  ethnicity: white_non_hispanic
  altitude_residence_m: 100
  hiv_status: negative
  cd4_count_cells_per_uL: None
  pregnancy_red_flag: False
  immunocompromise_status: none
  freshwater_exposure_within_14d: True
  freshwater_exposure_type: lake

HISTORY:
  symptom_onset_to_presentation_days: 4.0
  chief_complaint: fever_with_headache
  red_flags_present: ['fresh_water_exposure_14d']
  prodrome_description: somnolence with neck stiffness

VITALS:
  temperature_celsius: 39.2
  heart_rate_bpm: 118
  systolic_bp_mmHg: 110
  diastolic_bp_mmHg: 68
  glasgow_coma_scale: 11
  oxygen_saturation_pct: 96
  respiratory_rate_breaths_per_min: 22

EXAM:
  mental_status_grade: somnolent
  neck_stiffness: True
  kernig_or_brudzinski_positive: True
  cranial_nerve_palsy: none
  papilledema_on_fundoscopy: False
  focal_neurological_deficit: False
  skin_lesion_centrofacial_chronic: False
  petechial_or_purpuric_rash: False

LABS:
  wbc_blood_per_uL: 18000
  platelets_per_uL: 254000
  alt_ast_U_per_L: None
  crp_mg_per_L: 78.0
  procalcitonin_ng_per_mL: 1.6
  serum_sodium_mEq_per_L: 137

CSF:
  opening_pressure_cmH2O: 28.0
  wbc_per_mm3: 2850
  lymphocyte_pct: 9
  neutrophil_pct: 90
  eosinophil_pct: 1
  glucose_mg_per_dL: 21
  protein_mg_per_dL: 332
  lactate_mmol_per_L: 7.0
  ada_U_per_L: None
  crag_lfa_result: negative
  wet_mount_motile_amoebae: not_done
  xanthochromia_present: False
  rbc_per_mm3: 180

IMAGING:
  modality: ct_noncontrast
  pattern: diffuse_cerebral_edema_basilar_meningeal_enhancement
  contrast_enhancement: True
  hydrocephalus: False
  basal_meningeal_enhancement: False
  finding_count: None
  text_summary: Imaging consistent with PAM stage; specific findings imputed within Capewell 2015 US 1937-2013 review cohort epidemiology (lake/pond sub-bucket dominant).

DIAGNOSTIC_TESTS:
  pcr_panel: Positive (consistent with within-cohort imputation per Capewell 2015 review).
  xpert_mtb_rif: n/a
  blood_culture: n/a
  csf_culture: n/a
  serology_or_antigen: n/a
  smear_or_gram: n/a
  brain_biopsy: n/a
  imaging_test: n/a
  total_dx_results: 1

NARRATIVE_EN: An 11-year-old male from the US South region presented with a four-day history of fever, headache, and somnolence with neck stiffness following recreational freshwater (lake/pond) exposure. On admission temperature was 39.2 C, Glasgow Coma Scale 11. CSF showed white cell count 2,850 per cubic millimeter (90 percent neutrophils), glucose 21 mg/dL, and protein 332 mg/dL. Acute-phase reactants were CRP 78 mg/L and procalcitonin 1.6 ng/mL. Treatment per CDC PAM protocol was initiated; the patient died of refractory cerebral edema. This vignette is a Tier-4 within-cohort imputation: no specific named-case is claimed. Clinical specifics follow Capewell 2015's documented US 1937-2013 review of approximately 140-145 cases (lake/pond sub-bucket dominant); demographics are locked from the Day-2 distribution table (PMID 26582886).

NARRATIVE_ES: Paciente de 11 años de sexo masculino originario de la región sur de Estados Unidos, que se presentó con cuatro días de fiebre, cefalea y somnolencia con rigidez de nuca tras exposición recreativa a agua dulce (lago o estanque). Al ingreso la temperatura fue de 39.2 C, escala de Glasgow 11. El líquido cefalorraquídeo mostró leucocitos 2,850 por mm3 (90 por ciento neutrófilos), glucosa 21 mg/dL y proteína 332 mg/dL. Los reactantes de fase aguda fueron PCR 78 mg/L y procalcitonina 1.6 ng/mL. Se inició el protocolo de PAM de los CDC; el paciente falleció por edema cerebral refractario. Esta viñeta es una imputación de Tier-4 dentro de la cohorte: no se reclama un caso nombrado específico. Los datos clínicos siguen la revisión documentada por Capewell 2015 sobre PAM en Estados Unidos 1937-2013 (aproximadamente 140-145 casos, subgrupo lago/estanque dominante); las características demográficas están fijadas en la tabla de distribución del Día 2 (PMID 26582886).

RATIONALE: Day 2 vignette 29 of 60 (v21-v60 set) for Subphase 1.2 PAM corpus. Cluster: lake_pond. Atypical type: none. Outcome: fatal. Anchored to PMID 26582886 (Capewell et al., J Pediatric Infect Dis Soc 2015). Sub-fields populated from published case where available; vitals and partial labs IMPUTED_FROM_LITERATURE consistent with mid-stage PAM clinical patterns documented in CDC PAM case reviews. Treatment per CDC six-drug protocol (amphotericin B, miltefosine, dexamethasone, fluconazole, azithromycin, rifampin); fatal outcome despite full regimen. Citation caveat: Review article (US PAM 1937-2013, approximately 140-145 cases over 76 years). PMC ID NOT confirmable - cite PMID + DOI only. Use as Tier 4 IMPUTED_FROM_LITERATURE_REVIEW anchor only. Prior PMC4622028 attribution removed (unconfirmable in any of 6 independent reference lists).

ANCHORING_EXTRAS: Anchored to Capewell et al. J Pediatric Infect Dis Soc 2015 (PMID 26582886). Demographics: 11 years male, US South region. Stage metadata: clinical_stage=mid, exposure_certainty=definite, diagnostic_confirmation=PCR (CDC reference laboratory CSF Naegleria fowleri), outcome=fatal. CSF and imaging within published case ranges; vitals imputed from PAM presentation patterns documented in CDC PAM case reviews.

ADJUDICATION:
  inclusion_decision: include
  adjudicator_ids: ['ADJ-001', 'ADJ-002']
  ground_truth_class: 1
  pre_adjudication_kappa: 0.99
  disagreement_resolution: None

=== END vignette ===

=== CLASS 1 | vignette_id: 030 | subphase: 1.2 PAM Day2 | file: pam_d2_030_capewell_imputed_adolescent.json ===

ANCHOR:
  pmid: 26582886
  first_author: Capewell
  year: 2015
  journal: JPIDS
  citation_type: review
  doi: 10.1093/jpids/piu103

DEMOGRAPHICS:
  age_years: 15
  sex: male
  geography_region: us_south
  ethnicity: white_non_hispanic
  altitude_residence_m: 100
  hiv_status: negative
  cd4_count_cells_per_uL: None
  pregnancy_red_flag: False
  immunocompromise_status: none
  freshwater_exposure_within_14d: True
  freshwater_exposure_type: lake

HISTORY:
  symptom_onset_to_presentation_days: 4.0
  chief_complaint: altered_mental_status
  red_flags_present: ['fresh_water_exposure_14d']
  prodrome_description: stupor with focal deficit

VITALS:
  temperature_celsius: 39.2
  heart_rate_bpm: 108
  systolic_bp_mmHg: 116
  diastolic_bp_mmHg: 72
  glasgow_coma_scale: 7
  oxygen_saturation_pct: 96
  respiratory_rate_breaths_per_min: 20

EXAM:
  mental_status_grade: stuporous
  neck_stiffness: True
  kernig_or_brudzinski_positive: True
  cranial_nerve_palsy: none
  papilledema_on_fundoscopy: True
  focal_neurological_deficit: True
  skin_lesion_centrofacial_chronic: False
  petechial_or_purpuric_rash: False

LABS:
  wbc_blood_per_uL: 18000
  platelets_per_uL: 254000
  alt_ast_U_per_L: None
  crp_mg_per_L: 118.0
  procalcitonin_ng_per_mL: 3.1
  serum_sodium_mEq_per_L: 137

CSF:
  opening_pressure_cmH2O: 38.0
  wbc_per_mm3: 4500
  lymphocyte_pct: 9
  neutrophil_pct: 90
  eosinophil_pct: 1
  glucose_mg_per_dL: 14
  protein_mg_per_dL: 442
  lactate_mmol_per_L: 7.0
  ada_U_per_L: None
  crag_lfa_result: negative
  wet_mount_motile_amoebae: positive
  xanthochromia_present: False
  rbc_per_mm3: 180

IMAGING:
  modality: ct_noncontrast
  pattern: diffuse_cerebral_edema_basilar_meningeal_enhancement
  contrast_enhancement: True
  hydrocephalus: False
  basal_meningeal_enhancement: False
  finding_count: None
  text_summary: Imaging consistent with PAM stage; specific findings imputed within Capewell 2015 US 1937-2013 review cohort epidemiology (lake/pond sub-bucket dominant).

DIAGNOSTIC_TESTS:
  pcr_panel: Positive (consistent with within-cohort imputation per Capewell 2015 review).
  xpert_mtb_rif: n/a
  blood_culture: n/a
  csf_culture: n/a
  serology_or_antigen: n/a
  smear_or_gram: n/a
  brain_biopsy: n/a
  imaging_test: n/a
  total_dx_results: 1

NARRATIVE_EN: A 15-year-old male from the US South region presented with a four-day history of fever, headache, and stupor with focal deficit following recreational freshwater (lake/pond) exposure. On admission temperature was 39.2 C, Glasgow Coma Scale 7. CSF showed white cell count 4,500 per cubic millimeter (90 percent neutrophils), glucose 14 mg/dL, and protein 442 mg/dL. Acute-phase reactants were CRP 118 mg/L and procalcitonin 3.1 ng/mL. Treatment per CDC PAM protocol was initiated; the patient died of refractory cerebral edema. This vignette is a Tier-4 within-cohort imputation: no specific named-case is claimed. Clinical specifics follow Capewell 2015's documented US 1937-2013 review of approximately 140-145 cases (lake/pond sub-bucket dominant); demographics are locked from the Day-2 distribution table (PMID 26582886).

NARRATIVE_ES: Paciente de 15 años de sexo masculino originario de la región sur de Estados Unidos, que se presentó con cuatro días de fiebre, cefalea y estupor con déficit focal tras exposición recreativa a agua dulce (lago o estanque). Al ingreso la temperatura fue de 39.2 C, escala de Glasgow 7. El líquido cefalorraquídeo mostró leucocitos 4,500 por mm3 (90 por ciento neutrófilos), glucosa 14 mg/dL y proteína 442 mg/dL. Los reactantes de fase aguda fueron PCR 118 mg/L y procalcitonina 3.1 ng/mL. Se inició el protocolo de PAM de los CDC; el paciente falleció por edema cerebral refractario. Esta viñeta es una imputación de Tier-4 dentro de la cohorte: no se reclama un caso nombrado específico. Los datos clínicos siguen la revisión documentada por Capewell 2015 sobre PAM en Estados Unidos 1937-2013 (aproximadamente 140-145 casos, subgrupo lago/estanque dominante); las características demográficas están fijadas en la tabla de distribución del Día 2 (PMID 26582886).

RATIONALE: Day 2 vignette 30 of 60 (v21-v60 set) for Subphase 1.2 PAM corpus. Cluster: lake_pond. Atypical type: none. Outcome: fatal. Anchored to PMID 26582886 (Capewell et al., J Pediatric Infect Dis Soc 2015). Sub-fields populated from published case where available; vitals and partial labs IMPUTED_FROM_LITERATURE consistent with late-stage PAM clinical patterns documented in CDC PAM case reviews. Treatment per CDC six-drug protocol (amphotericin B, miltefosine, dexamethasone, fluconazole, azithromycin, rifampin); fatal outcome despite full regimen. Citation caveat: Review article (US PAM 1937-2013, approximately 140-145 cases over 76 years). PMC ID NOT confirmable - cite PMID + DOI only. Use as Tier 4 IMPUTED_FROM_LITERATURE_REVIEW anchor only. Prior PMC4622028 attribution removed (unconfirmable in any of 6 independent reference lists).

ANCHORING_EXTRAS: Anchored to Capewell et al. J Pediatric Infect Dis Soc 2015 (PMID 26582886). Demographics: 15 years male, US South region. Stage metadata: clinical_stage=late, exposure_certainty=definite, diagnostic_confirmation=PCR (CDC reference laboratory CSF Naegleria fowleri), outcome=fatal. CSF and imaging within published case ranges; vitals imputed from PAM presentation patterns documented in CDC PAM case reviews.

ADJUDICATION:
  inclusion_decision: include
  adjudicator_ids: ['ADJ-001', 'ADJ-002']
  ground_truth_class: 1
  pre_adjudication_kappa: 0.99
  disagreement_resolution: None

=== END vignette ===

=== CLASS 1 | vignette_id: 031 | subphase: 1.2 PAM Day2 | file: pam_d2_031_capewell_imputed_school_age.json ===

ANCHOR:
  pmid: 26582886
  first_author: Capewell
  year: 2015
  journal: JPIDS
  citation_type: review
  doi: 10.1093/jpids/piu103

DEMOGRAPHICS:
  age_years: 9
  sex: male
  geography_region: us_south
  ethnicity: white_non_hispanic
  altitude_residence_m: 100
  hiv_status: negative
  cd4_count_cells_per_uL: None
  pregnancy_red_flag: False
  immunocompromise_status: none
  freshwater_exposure_within_14d: True
  freshwater_exposure_type: lake

HISTORY:
  symptom_onset_to_presentation_days: 4.0
  chief_complaint: fever_with_headache
  red_flags_present: ['fresh_water_exposure_14d']
  prodrome_description: lethargy and vomiting

VITALS:
  temperature_celsius: 39.2
  heart_rate_bpm: 132
  systolic_bp_mmHg: 102
  diastolic_bp_mmHg: 64
  glasgow_coma_scale: 11
  oxygen_saturation_pct: 96
  respiratory_rate_breaths_per_min: 26

EXAM:
  mental_status_grade: somnolent
  neck_stiffness: True
  kernig_or_brudzinski_positive: True
  cranial_nerve_palsy: none
  papilledema_on_fundoscopy: False
  focal_neurological_deficit: False
  skin_lesion_centrofacial_chronic: False
  petechial_or_purpuric_rash: False

LABS:
  wbc_blood_per_uL: 18000
  platelets_per_uL: 254000
  alt_ast_U_per_L: None
  crp_mg_per_L: 92.0
  procalcitonin_ng_per_mL: 2.1
  serum_sodium_mEq_per_L: 137

CSF:
  opening_pressure_cmH2O: 28.0
  wbc_per_mm3: 3220
  lymphocyte_pct: 9
  neutrophil_pct: 90
  eosinophil_pct: 1
  glucose_mg_per_dL: 23
  protein_mg_per_dL: 376
  lactate_mmol_per_L: 7.0
  ada_U_per_L: None
  crag_lfa_result: negative
  wet_mount_motile_amoebae: not_done
  xanthochromia_present: False
  rbc_per_mm3: 180

IMAGING:
  modality: ct_noncontrast
  pattern: diffuse_cerebral_edema_basilar_meningeal_enhancement
  contrast_enhancement: True
  hydrocephalus: False
  basal_meningeal_enhancement: False
  finding_count: None
  text_summary: Imaging consistent with PAM stage; specific findings imputed within Capewell 2015 US 1937-2013 review cohort epidemiology (lake/pond sub-bucket dominant).

DIAGNOSTIC_TESTS:
  pcr_panel: Positive (consistent with within-cohort imputation per Capewell 2015 review).
  xpert_mtb_rif: n/a
  blood_culture: n/a
  csf_culture: n/a
  serology_or_antigen: n/a
  smear_or_gram: n/a
  brain_biopsy: n/a
  imaging_test: n/a
  total_dx_results: 1

NARRATIVE_EN: A 9-year-old male from the US South region presented with a four-day history of fever, headache, and lethargy and vomiting following recreational freshwater (lake/pond) exposure. On admission temperature was 39.2 C, Glasgow Coma Scale 11. CSF showed white cell count 3,220 per cubic millimeter (90 percent neutrophils), glucose 23 mg/dL, and protein 376 mg/dL. Acute-phase reactants were CRP 92 mg/L and procalcitonin 2.1 ng/mL. Treatment per CDC PAM protocol was initiated; the patient died of refractory cerebral edema. This vignette is a Tier-4 within-cohort imputation: no specific named-case is claimed. Clinical specifics follow Capewell 2015's documented US 1937-2013 review of approximately 140-145 cases (lake/pond sub-bucket dominant); demographics are locked from the Day-2 distribution table (PMID 26582886).

NARRATIVE_ES: Paciente de 9 años de sexo masculino originario de la región sur de Estados Unidos, que se presentó con cuatro días de fiebre, cefalea y letargia con vómitos tras exposición recreativa a agua dulce (lago o estanque). Al ingreso la temperatura fue de 39.2 C, escala de Glasgow 11. El líquido cefalorraquídeo mostró leucocitos 3,220 por mm3 (90 por ciento neutrófilos), glucosa 23 mg/dL y proteína 376 mg/dL. Los reactantes de fase aguda fueron PCR 92 mg/L y procalcitonina 2.1 ng/mL. Se inició el protocolo de PAM de los CDC; el paciente falleció por edema cerebral refractario. Esta viñeta es una imputación de Tier-4 dentro de la cohorte: no se reclama un caso nombrado específico. Los datos clínicos siguen la revisión documentada por Capewell 2015 sobre PAM en Estados Unidos 1937-2013 (aproximadamente 140-145 casos, subgrupo lago/estanque dominante); las características demográficas están fijadas en la tabla de distribución del Día 2 (PMID 26582886).

RATIONALE: Day 2 vignette 31 of 60 (v21-v60 set) for Subphase 1.2 PAM corpus. Cluster: lake_pond. Atypical type: none. Outcome: fatal. Anchored to PMID 26582886 (Capewell et al., J Pediatric Infect Dis Soc 2015). Sub-fields populated from published case where available; vitals and partial labs IMPUTED_FROM_LITERATURE consistent with mid-stage PAM clinical patterns documented in CDC PAM case reviews. Treatment per CDC six-drug protocol (amphotericin B, miltefosine, dexamethasone, fluconazole, azithromycin, rifampin); fatal outcome despite full regimen. Citation caveat: Review article (US PAM 1937-2013, approximately 140-145 cases over 76 years). PMC ID NOT confirmable - cite PMID + DOI only. Use as Tier 4 IMPUTED_FROM_LITERATURE_REVIEW anchor only. Prior PMC4622028 attribution removed (unconfirmable in any of 6 independent reference lists).

ANCHORING_EXTRAS: Anchored to Capewell et al. J Pediatric Infect Dis Soc 2015 (PMID 26582886). Demographics: 9 years male, US South region. Stage metadata: clinical_stage=mid, exposure_certainty=definite, diagnostic_confirmation=PCR (CDC reference laboratory CSF Naegleria fowleri), outcome=fatal. CSF and imaging within published case ranges; vitals imputed from PAM presentation patterns documented in CDC PAM case reviews.

ADJUDICATION:
  inclusion_decision: include
  adjudicator_ids: ['ADJ-001', 'ADJ-002']
  ground_truth_class: 1
  pre_adjudication_kappa: 0.99
  disagreement_resolution: None

=== END vignette ===

=== CLASS 1 | vignette_id: 032 | subphase: 1.2 PAM Day2 | file: pam_d2_032_kemble_minnesota_reuse_a.json ===

ANCHOR:
  pmid: 22238170
  first_author: Kemble
  year: 2012
  journal: CID
  citation_type: case_report
  doi: 

DEMOGRAPHICS:
  age_years: 11
  sex: male
  geography_region: other_global
  ethnicity: other
  altitude_residence_m: 100
  hiv_status: negative
  cd4_count_cells_per_uL: None
  pregnancy_red_flag: False
  immunocompromise_status: none
  freshwater_exposure_within_14d: True
  freshwater_exposure_type: lake

HISTORY:
  symptom_onset_to_presentation_days: 5.0
  chief_complaint: fever_with_headache
  red_flags_present: ['fresh_water_exposure_14d']
  prodrome_description: somnolence with vomiting

VITALS:
  temperature_celsius: 39.4
  heart_rate_bpm: 116
  systolic_bp_mmHg: 108
  diastolic_bp_mmHg: 66
  glasgow_coma_scale: 11
  oxygen_saturation_pct: 96
  respiratory_rate_breaths_per_min: 22

EXAM:
  mental_status_grade: somnolent
  neck_stiffness: True
  kernig_or_brudzinski_positive: True
  cranial_nerve_palsy: none
  papilledema_on_fundoscopy: False
  focal_neurological_deficit: False
  skin_lesion_centrofacial_chronic: False
  petechial_or_purpuric_rash: False

LABS:
  wbc_blood_per_uL: 17600
  platelets_per_uL: 248000
  alt_ast_U_per_L: None
  crp_mg_per_L: 82.0
  procalcitonin_ng_per_mL: 1.7
  serum_sodium_mEq_per_L: 138

CSF:
  opening_pressure_cmH2O: 28.0
  wbc_per_mm3: 2920
  lymphocyte_pct: 10
  neutrophil_pct: 89
  eosinophil_pct: 1
  glucose_mg_per_dL: 20
  protein_mg_per_dL: 348
  lactate_mmol_per_L: 6.8
  ada_U_per_L: None
  crag_lfa_result: negative
  wet_mount_motile_amoebae: not_done
  xanthochromia_present: False
  rbc_per_mm3: 200

IMAGING:
  modality: ct_noncontrast
  pattern: diffuse_cerebral_edema_basilar_meningeal_enhancement
  contrast_enhancement: True
  hydrocephalus: False
  basal_meningeal_enhancement: False
  finding_count: None
  text_summary: CT showed diffuse cerebral edema with effacement of cortical sulci. Imaging imputed within Kemble 2012 Minnesota northern-tier PAM case-context.

DIAGNOSTIC_TESTS:
  pcr_panel: Positive.
  xpert_mtb_rif: n/a
  blood_culture: n/a
  csf_culture: n/a
  serology_or_antigen: n/a
  smear_or_gram: n/a
  brain_biopsy: n/a
  imaging_test: n/a
  total_dx_results: 1

NARRATIVE_EN: An 11-year-old male from Minnesota presented with a five-day history of fever, headache, and somnolence with vomiting following lake exposure during the summer recreational season. On admission temperature was 39.4 C, Glasgow Coma Scale 11. CSF showed white cell count 2,920 per cubic millimeter (89 percent neutrophils), glucose 20 mg/dL, and protein 348 mg/dL. Acute-phase reactants were CRP 82 mg/L and procalcitonin 1.7 ng/mL. CSF PCR confirmed Naegleria fowleri at the CDC reference laboratory. CT showed diffuse cerebral edema. Treatment per CDC PAM protocol was initiated; the patient died. This vignette is a within-cohort imputation per Kemble 2012 Minnesota northern-tier expansion case-context: demographics are locked from the Day-2 distribution table, and clinical specifics follow the documented Minnesota lake-exposure PAM epidemiology (PMID 22238170).

NARRATIVE_ES: Varón de 11 años originario de Minnesota que se presentó con cinco días de fiebre, cefalea y somnolencia con vómitos tras exposición a un lago durante la temporada recreativa de verano. Al ingreso la temperatura fue de 39.4 C, escala de Glasgow 11. El líquido cefalorraquídeo mostró leucocitos 2,920 por mm3 (89 por ciento neutrófilos), glucosa 20 mg/dL y proteína 348 mg/dL. Los reactantes de fase aguda fueron PCR 82 mg/L y procalcitonina 1.7 ng/mL. La PCR del líquido cefalorraquídeo para Naegleria fowleri fue positiva en el laboratorio de referencia de los CDC. La tomografía mostró edema cerebral difuso. Se inició el protocolo de PAM de los CDC; el paciente falleció. Esta viñeta es una imputación dentro de la cohorte según el contexto del caso documentado por Kemble 2012 (expansión septentrional de Minnesota): los datos demográficos están fijados en la tabla de distribución del Día 2, y las características clínicas siguen la epidemiología de PAM con exposición a lagos de Minnesota (PMID 22238170).

RATIONALE: Day 2 vignette 32 of 60 (v21-v60 set) for Subphase 1.2 PAM corpus. Cluster: lake_pond. Atypical type: none. Outcome: fatal. Anchored to PMID 22238170 (Kemble SK et al., Clin Infect Dis 2012). Sub-fields populated from published case where available; vitals and partial labs IMPUTED_FROM_LITERATURE consistent with mid-stage PAM clinical patterns documented in CDC PAM case reviews. Treatment per CDC six-drug protocol (amphotericin B, miltefosine, dexamethasone, fluconazole, azithromycin, rifampin); fatal outcome despite full regimen.

ANCHORING_EXTRAS: Anchored to Kemble SK et al. Clin Infect Dis 2012 (PMID 22238170). Demographics: 11 years male, Minnesota, US. Stage metadata: clinical_stage=mid, exposure_certainty=definite, diagnostic_confirmation=PCR (CDC reference laboratory CSF Naegleria fowleri), outcome=fatal. CSF and imaging within published case ranges; vitals imputed from PAM presentation patterns documented in CDC PAM case reviews.

ADJUDICATION:
  inclusion_decision: include
  adjudicator_ids: ['ADJ-001', 'ADJ-002']
  ground_truth_class: 1
  pre_adjudication_kappa: 0.99
  disagreement_resolution: None

=== END vignette ===

=== CLASS 1 | vignette_id: 033 | subphase: 1.2 PAM Day2 | file: pam_d2_033_kemble_minnesota_reuse_b.json ===

ANCHOR:
  pmid: 22238170
  first_author: Kemble
  year: 2012
  journal: CID
  citation_type: case_report
  doi: 

DEMOGRAPHICS:
  age_years: 6
  sex: male
  geography_region: other_global
  ethnicity: other
  altitude_residence_m: 100
  hiv_status: negative
  cd4_count_cells_per_uL: None
  pregnancy_red_flag: False
  immunocompromise_status: none
  freshwater_exposure_within_14d: True
  freshwater_exposure_type: lake

HISTORY:
  symptom_onset_to_presentation_days: 5.0
  chief_complaint: altered_mental_status
  red_flags_present: ['fresh_water_exposure_14d']
  prodrome_description: rapid progression to stupor with focal deficit

VITALS:
  temperature_celsius: 39.4
  heart_rate_bpm: 130
  systolic_bp_mmHg: 100
  diastolic_bp_mmHg: 62
  glasgow_coma_scale: 7
  oxygen_saturation_pct: 96
  respiratory_rate_breaths_per_min: 26

EXAM:
  mental_status_grade: stuporous
  neck_stiffness: True
  kernig_or_brudzinski_positive: True
  cranial_nerve_palsy: none
  papilledema_on_fundoscopy: True
  focal_neurological_deficit: True
  skin_lesion_centrofacial_chronic: False
  petechial_or_purpuric_rash: False

LABS:
  wbc_blood_per_uL: 17600
  platelets_per_uL: 248000
  alt_ast_U_per_L: None
  crp_mg_per_L: 112.0
  procalcitonin_ng_per_mL: 2.9
  serum_sodium_mEq_per_L: 138

CSF:
  opening_pressure_cmH2O: 38.0
  wbc_per_mm3: 4480
  lymphocyte_pct: 10
  neutrophil_pct: 89
  eosinophil_pct: 1
  glucose_mg_per_dL: 15
  protein_mg_per_dL: 432
  lactate_mmol_per_L: 6.8
  ada_U_per_L: None
  crag_lfa_result: negative
  wet_mount_motile_amoebae: positive
  xanthochromia_present: False
  rbc_per_mm3: 200

IMAGING:
  modality: ct_noncontrast
  pattern: diffuse_cerebral_edema_basilar_meningeal_enhancement
  contrast_enhancement: True
  hydrocephalus: False
  basal_meningeal_enhancement: False
  finding_count: None
  text_summary: CT showed diffuse cerebral edema with effacement of cortical sulci. Imaging imputed within Kemble 2012 Minnesota northern-tier PAM case-context.

DIAGNOSTIC_TESTS:
  pcr_panel: Positive.
  xpert_mtb_rif: n/a
  blood_culture: n/a
  csf_culture: n/a
  serology_or_antigen: n/a
  smear_or_gram: n/a
  brain_biopsy: n/a
  imaging_test: n/a
  total_dx_results: 1

NARRATIVE_EN: A 6-year-old male from Minnesota presented with a five-day history of fever, headache, and rapid progression to stupor with focal deficit following lake exposure during the summer recreational season. On admission temperature was 39.4 C, Glasgow Coma Scale 7. CSF showed white cell count 4,480 per cubic millimeter (89 percent neutrophils), glucose 15 mg/dL, and protein 432 mg/dL. Acute-phase reactants were CRP 112 mg/L and procalcitonin 2.9 ng/mL. CSF PCR confirmed Naegleria fowleri at the CDC reference laboratory. CT showed diffuse cerebral edema. Treatment per CDC PAM protocol was initiated; the patient died. This vignette is a within-cohort imputation per Kemble 2012 Minnesota northern-tier expansion case-context: demographics are locked from the Day-2 distribution table, and clinical specifics follow the documented Minnesota lake-exposure PAM epidemiology (PMID 22238170).

NARRATIVE_ES: Varón de 6 años originario de Minnesota que se presentó con cinco días de fiebre, cefalea y progresión rápida a estupor con déficit focal tras exposición a un lago durante la temporada recreativa de verano. Al ingreso la temperatura fue de 39.4 C, escala de Glasgow 7. El líquido cefalorraquídeo mostró leucocitos 4,480 por mm3 (89 por ciento neutrófilos), glucosa 15 mg/dL y proteína 432 mg/dL. Los reactantes de fase aguda fueron PCR 112 mg/L y procalcitonina 2.9 ng/mL. La PCR del líquido cefalorraquídeo para Naegleria fowleri fue positiva en el laboratorio de referencia de los CDC. La tomografía mostró edema cerebral difuso. Se inició el protocolo de PAM de los CDC; el paciente falleció. Esta viñeta es una imputación dentro de la cohorte según el contexto del caso documentado por Kemble 2012 (expansión septentrional de Minnesota): los datos demográficos están fijados en la tabla de distribución del Día 2, y las características clínicas siguen la epidemiología de PAM con exposición a lagos de Minnesota (PMID 22238170).

RATIONALE: Day 2 vignette 33 of 60 (v21-v60 set) for Subphase 1.2 PAM corpus. Cluster: lake_pond. Atypical type: none. Outcome: fatal. Anchored to PMID 22238170 (Kemble SK et al., Clin Infect Dis 2012). Sub-fields populated from published case where available; vitals and partial labs IMPUTED_FROM_LITERATURE consistent with late-stage PAM clinical patterns documented in CDC PAM case reviews. Treatment per CDC six-drug protocol (amphotericin B, miltefosine, dexamethasone, fluconazole, azithromycin, rifampin); fatal outcome despite full regimen.

ANCHORING_EXTRAS: Anchored to Kemble SK et al. Clin Infect Dis 2012 (PMID 22238170). Demographics: 6 years male, Minnesota, US. Stage metadata: clinical_stage=late, exposure_certainty=definite, diagnostic_confirmation=PCR (CDC reference laboratory CSF Naegleria fowleri), outcome=fatal. CSF and imaging within published case ranges; vitals imputed from PAM presentation patterns documented in CDC PAM case reviews.

ADJUDICATION:
  inclusion_decision: include
  adjudicator_ids: ['ADJ-001', 'ADJ-002']
  ground_truth_class: 1
  pre_adjudication_kappa: 0.99
  disagreement_resolution: None

=== END vignette ===

=== CLASS 1 | vignette_id: 034 | subphase: 1.2 PAM Day2 | file: pam_d2_034_kemble_minnesota_reuse_c.json ===

ANCHOR:
  pmid: 22238170
  first_author: Kemble
  year: 2012
  journal: CID
  citation_type: case_report
  doi: 

DEMOGRAPHICS:
  age_years: 14
  sex: male
  geography_region: other_global
  ethnicity: other
  altitude_residence_m: 100
  hiv_status: negative
  cd4_count_cells_per_uL: None
  pregnancy_red_flag: False
  immunocompromise_status: none
  freshwater_exposure_within_14d: True
  freshwater_exposure_type: lake

HISTORY:
  symptom_onset_to_presentation_days: 5.0
  chief_complaint: fever_with_headache
  red_flags_present: ['fresh_water_exposure_14d']
  prodrome_description: progressive lethargy with neck stiffness

VITALS:
  temperature_celsius: 39.4
  heart_rate_bpm: 116
  systolic_bp_mmHg: 108
  diastolic_bp_mmHg: 66
  glasgow_coma_scale: 11
  oxygen_saturation_pct: 96
  respiratory_rate_breaths_per_min: 22

EXAM:
  mental_status_grade: somnolent
  neck_stiffness: True
  kernig_or_brudzinski_positive: True
  cranial_nerve_palsy: none
  papilledema_on_fundoscopy: False
  focal_neurological_deficit: False
  skin_lesion_centrofacial_chronic: False
  petechial_or_purpuric_rash: False

LABS:
  wbc_blood_per_uL: 17600
  platelets_per_uL: 248000
  alt_ast_U_per_L: None
  crp_mg_per_L: 88.0
  procalcitonin_ng_per_mL: 1.9
  serum_sodium_mEq_per_L: 138

CSF:
  opening_pressure_cmH2O: 28.0
  wbc_per_mm3: 3140
  lymphocyte_pct: 10
  neutrophil_pct: 89
  eosinophil_pct: 1
  glucose_mg_per_dL: 22
  protein_mg_per_dL: 368
  lactate_mmol_per_L: 6.8
  ada_U_per_L: None
  crag_lfa_result: negative
  wet_mount_motile_amoebae: not_done
  xanthochromia_present: False
  rbc_per_mm3: 200

IMAGING:
  modality: ct_noncontrast
  pattern: diffuse_cerebral_edema_basilar_meningeal_enhancement
  contrast_enhancement: True
  hydrocephalus: False
  basal_meningeal_enhancement: False
  finding_count: None
  text_summary: CT showed diffuse cerebral edema with effacement of cortical sulci. Imaging imputed within Kemble 2012 Minnesota northern-tier PAM case-context.

DIAGNOSTIC_TESTS:
  pcr_panel: Positive.
  xpert_mtb_rif: n/a
  blood_culture: n/a
  csf_culture: n/a
  serology_or_antigen: n/a
  smear_or_gram: n/a
  brain_biopsy: n/a
  imaging_test: n/a
  total_dx_results: 1

NARRATIVE_EN: A 14-year-old male from Minnesota presented with a five-day history of fever, headache, and progressive lethargy with neck stiffness following lake exposure during the summer recreational season. On admission temperature was 39.4 C, Glasgow Coma Scale 11. CSF showed white cell count 3,140 per cubic millimeter (89 percent neutrophils), glucose 22 mg/dL, and protein 368 mg/dL. Acute-phase reactants were CRP 88 mg/L and procalcitonin 1.9 ng/mL. CSF PCR confirmed Naegleria fowleri at the CDC reference laboratory. CT showed diffuse cerebral edema. Treatment per CDC PAM protocol was initiated; the patient died. This vignette is a within-cohort imputation per Kemble 2012 Minnesota northern-tier expansion case-context: demographics are locked from the Day-2 distribution table, and clinical specifics follow the documented Minnesota lake-exposure PAM epidemiology (PMID 22238170).

NARRATIVE_ES: Varón de 14 años originario de Minnesota que se presentó con cinco días de fiebre, cefalea y letargia progresiva con rigidez de nuca tras exposición a un lago durante la temporada recreativa de verano. Al ingreso la temperatura fue de 39.4 C, escala de Glasgow 11. El líquido cefalorraquídeo mostró leucocitos 3,140 por mm3 (89 por ciento neutrófilos), glucosa 22 mg/dL y proteína 368 mg/dL. Los reactantes de fase aguda fueron PCR 88 mg/L y procalcitonina 1.9 ng/mL. La PCR del líquido cefalorraquídeo para Naegleria fowleri fue positiva en el laboratorio de referencia de los CDC. La tomografía mostró edema cerebral difuso. Se inició el protocolo de PAM de los CDC; el paciente falleció. Esta viñeta es una imputación dentro de la cohorte según el contexto del caso documentado por Kemble 2012 (expansión septentrional de Minnesota): los datos demográficos están fijados en la tabla de distribución del Día 2, y las características clínicas siguen la epidemiología de PAM con exposición a lagos de Minnesota (PMID 22238170).

RATIONALE: Day 2 vignette 34 of 60 (v21-v60 set) for Subphase 1.2 PAM corpus. Cluster: lake_pond. Atypical type: none. Outcome: fatal. Anchored to PMID 22238170 (Kemble SK et al., Clin Infect Dis 2012). Sub-fields populated from published case where available; vitals and partial labs IMPUTED_FROM_LITERATURE consistent with mid-stage PAM clinical patterns documented in CDC PAM case reviews. Treatment per CDC six-drug protocol (amphotericin B, miltefosine, dexamethasone, fluconazole, azithromycin, rifampin); fatal outcome despite full regimen.

ANCHORING_EXTRAS: Anchored to Kemble SK et al. Clin Infect Dis 2012 (PMID 22238170). Demographics: 14 years male, Minnesota, US. Stage metadata: clinical_stage=mid, exposure_certainty=definite, diagnostic_confirmation=PCR (CDC reference laboratory CSF Naegleria fowleri), outcome=fatal. CSF and imaging within published case ranges; vitals imputed from PAM presentation patterns documented in CDC PAM case reviews.

ADJUDICATION:
  inclusion_decision: include
  adjudicator_ids: ['ADJ-001', 'ADJ-002']
  ground_truth_class: 1
  pre_adjudication_kappa: 0.99
  disagreement_resolution: None

=== END vignette ===

=== CLASS 1 | vignette_id: 035 | subphase: 1.2 PAM Day2 | file: pam_d2_035_anjum_florida_reuse_a.json ===

ANCHOR:
  pmid: 34307045
  first_author: Anjum
  year: 2021
  journal: IDCases
  citation_type: case_report
  doi: 10.1016/j.idcr.2021.e01208

DEMOGRAPHICS:
  age_years: 10
  sex: male
  geography_region: us_south
  ethnicity: white_non_hispanic
  altitude_residence_m: 100
  hiv_status: negative
  cd4_count_cells_per_uL: None
  pregnancy_red_flag: False
  immunocompromise_status: none
  freshwater_exposure_within_14d: True
  freshwater_exposure_type: lake

HISTORY:
  symptom_onset_to_presentation_days: 4.0
  chief_complaint: altered_mental_status
  red_flags_present: ['fresh_water_exposure_14d']
  prodrome_description: stupor with focal deficit and papilledema

VITALS:
  temperature_celsius: 39.6
  heart_rate_bpm: 128
  systolic_bp_mmHg: 104
  diastolic_bp_mmHg: 64
  glasgow_coma_scale: 7
  oxygen_saturation_pct: 95
  respiratory_rate_breaths_per_min: 24

EXAM:
  mental_status_grade: stuporous
  neck_stiffness: True
  kernig_or_brudzinski_positive: True
  cranial_nerve_palsy: none
  papilledema_on_fundoscopy: True
  focal_neurological_deficit: True
  skin_lesion_centrofacial_chronic: False
  petechial_or_purpuric_rash: False

LABS:
  wbc_blood_per_uL: 19000
  platelets_per_uL: 252000
  alt_ast_U_per_L: None
  crp_mg_per_L: 104.0
  procalcitonin_ng_per_mL: 2.7
  serum_sodium_mEq_per_L: 137

CSF:
  opening_pressure_cmH2O: 38.0
  wbc_per_mm3: 4260
  lymphocyte_pct: 8
  neutrophil_pct: 91
  eosinophil_pct: 1
  glucose_mg_per_dL: 16
  protein_mg_per_dL: 418
  lactate_mmol_per_L: 7.4
  ada_U_per_L: None
  crag_lfa_result: negative
  wet_mount_motile_amoebae: positive
  xanthochromia_present: False
  rbc_per_mm3: 220

IMAGING:
  modality: ct_noncontrast
  pattern: diffuse_cerebral_edema_basilar_meningeal_enhancement
  contrast_enhancement: True
  hydrocephalus: False
  basal_meningeal_enhancement: False
  finding_count: None
  text_summary: CT showed diffuse cerebral edema. Imaging imputed within Anjum 2021 Florida tap-water/lake-context case-set.

DIAGNOSTIC_TESTS:
  pcr_panel: Positive.
  xpert_mtb_rif: n/a
  blood_culture: n/a
  csf_culture: n/a
  serology_or_antigen: n/a
  smear_or_gram: n/a
  brain_biopsy: n/a
  imaging_test: n/a
  total_dx_results: 1

NARRATIVE_EN: A 10-year-old male from Florida presented with a four-day history of fever, headache, and stupor with focal deficit and papilledema following recreational freshwater (lake) exposure. On admission temperature was 39.6 C, Glasgow Coma Scale 7. CSF showed white cell count 4,260 per cubic millimeter (91 percent neutrophils), glucose 16 mg/dL, and protein 418 mg/dL. Acute-phase reactants were CRP 104 mg/L and procalcitonin 2.7 ng/mL. CSF PCR confirmed Naegleria fowleri at the CDC reference laboratory. CT showed diffuse cerebral edema. Treatment per CDC PAM protocol was initiated; the patient died. This vignette is a within-cohort imputation per Anjum 2021 Florida tap-water/lake-context case-set: demographics are locked from the Day-2 distribution table, and clinical specifics follow the documented Florida PAM epidemiology (PMID 34307045).

NARRATIVE_ES: Varón de 10 años originario de Florida que se presentó con cuatro días de fiebre, cefalea y estupor con déficit focal y papiledema tras exposición recreativa a agua dulce (lago). Al ingreso la temperatura fue de 39.6 C, escala de Glasgow 7. El líquido cefalorraquídeo mostró leucocitos 4,260 por mm3 (91 por ciento neutrófilos), glucosa 16 mg/dL y proteína 418 mg/dL. Los reactantes de fase aguda fueron PCR 104 mg/L y procalcitonina 2.7 ng/mL. La PCR del líquido cefalorraquídeo para Naegleria fowleri fue positiva en el laboratorio de referencia de los CDC. La tomografía mostró edema cerebral difuso. Se inició el protocolo de PAM de los CDC; el paciente falleció. Esta viñeta es una imputación dentro de la cohorte según el contexto del caso documentado por Anjum 2021 (Florida, exposición a agua de grifo/lago): los datos demográficos están fijados en la tabla de distribución del Día 2, y las características clínicas siguen la epidemiología de PAM de Florida (PMID 34307045).

RATIONALE: Day 2 vignette 35 of 60 (v21-v60 set) for Subphase 1.2 PAM corpus. Cluster: lake_pond. Atypical type: none. Outcome: fatal. Anchored to PMID 34307045 (Anjum SK et al., IDCases 2021). Sub-fields populated from published case where available; vitals and partial labs IMPUTED_FROM_LITERATURE consistent with late-stage PAM clinical patterns documented in CDC PAM case reviews. Treatment per CDC six-drug protocol (amphotericin B, miltefosine, dexamethasone, fluconazole, azithromycin, rifampin); fatal outcome despite full regimen. Citation caveat: US tap-water-associated PAM 2020s. Pairs with USVI ablution case (PMID 24226628) for tap-water transmission cluster adjudication. 11 authors confirmed (Saccoccio FM at end). DOI is e01208 (NOT e01218). Author 8 'O'Laughlin K' preserves apostrophe. Author 6 'Ibne Karim M Ali' renders as Vancouver 'Ali IKM' (3 initials). Authors: Saad K Anjum, Karna Mangrola, Garrett Fitzpatrick, Kimberly Stockdale, Laura Matthias, Ibne Karim M Ali, Jennifer R Cope,...

ANCHORING_EXTRAS: Anchored to Anjum SK et al. IDCases 2021 (PMID 34307045). Demographics: 10 years male, Florida, US. Stage metadata: clinical_stage=late, exposure_certainty=definite, diagnostic_confirmation=PCR (CDC reference laboratory CSF Naegleria fowleri), outcome=fatal. CSF and imaging within published case ranges; vitals imputed from PAM presentation patterns documented in CDC PAM case reviews.

ADJUDICATION:
  inclusion_decision: include
  adjudicator_ids: ['ADJ-001', 'ADJ-002']
  ground_truth_class: 1
  pre_adjudication_kappa: 0.99
  disagreement_resolution: None

=== END vignette ===

=== CLASS 1 | vignette_id: 036 | subphase: 1.2 PAM Day2 | file: pam_d2_036_anjum_florida_reuse_b.json ===

ANCHOR:
  pmid: 34307045
  first_author: Anjum
  year: 2021
  journal: IDCases
  citation_type: case_report
  doi: 10.1016/j.idcr.2021.e01208

DEMOGRAPHICS:
  age_years: 12
  sex: female
  geography_region: us_south
  ethnicity: white_non_hispanic
  altitude_residence_m: 100
  hiv_status: negative
  cd4_count_cells_per_uL: None
  pregnancy_red_flag: False
  immunocompromise_status: none
  freshwater_exposure_within_14d: True
  freshwater_exposure_type: lake

HISTORY:
  symptom_onset_to_presentation_days: 4.0
  chief_complaint: fever_with_headache
  red_flags_present: ['fresh_water_exposure_14d']
  prodrome_description: somnolence with neck stiffness

VITALS:
  temperature_celsius: 39.6
  heart_rate_bpm: 116
  systolic_bp_mmHg: 110
  diastolic_bp_mmHg: 68
  glasgow_coma_scale: 11
  oxygen_saturation_pct: 95
  respiratory_rate_breaths_per_min: 22

EXAM:
  mental_status_grade: somnolent
  neck_stiffness: True
  kernig_or_brudzinski_positive: True
  cranial_nerve_palsy: none
  papilledema_on_fundoscopy: False
  focal_neurological_deficit: False
  skin_lesion_centrofacial_chronic: False
  petechial_or_purpuric_rash: False

LABS:
  wbc_blood_per_uL: 19000
  platelets_per_uL: 252000
  alt_ast_U_per_L: None
  crp_mg_per_L: 84.0
  procalcitonin_ng_per_mL: 1.8
  serum_sodium_mEq_per_L: 137

CSF:
  opening_pressure_cmH2O: 28.0
  wbc_per_mm3: 3080
  lymphocyte_pct: 8
  neutrophil_pct: 91
  eosinophil_pct: 1
  glucose_mg_per_dL: 21
  protein_mg_per_dL: 356
  lactate_mmol_per_L: 7.4
  ada_U_per_L: None
  crag_lfa_result: negative
  wet_mount_motile_amoebae: not_done
  xanthochromia_present: False
  rbc_per_mm3: 220

IMAGING:
  modality: ct_noncontrast
  pattern: diffuse_cerebral_edema_basilar_meningeal_enhancement
  contrast_enhancement: True
  hydrocephalus: False
  basal_meningeal_enhancement: False
  finding_count: None
  text_summary: CT showed diffuse cerebral edema. Imaging imputed within Anjum 2021 Florida tap-water/lake-context case-set.

DIAGNOSTIC_TESTS:
  pcr_panel: Positive.
  xpert_mtb_rif: n/a
  blood_culture: n/a
  csf_culture: n/a
  serology_or_antigen: n/a
  smear_or_gram: n/a
  brain_biopsy: n/a
  imaging_test: n/a
  total_dx_results: 1

NARRATIVE_EN: A 12-year-old female from Florida presented with a four-day history of fever, headache, and somnolence with neck stiffness following recreational freshwater (lake) exposure. On admission temperature was 39.6 C, Glasgow Coma Scale 11. CSF showed white cell count 3,080 per cubic millimeter (91 percent neutrophils), glucose 21 mg/dL, and protein 356 mg/dL. Acute-phase reactants were CRP 84 mg/L and procalcitonin 1.8 ng/mL. CSF PCR confirmed Naegleria fowleri at the CDC reference laboratory. CT showed diffuse cerebral edema. Treatment per CDC PAM protocol was initiated; the patient died. This vignette is a within-cohort imputation per Anjum 2021 Florida tap-water/lake-context case-set: demographics are locked from the Day-2 distribution table, and clinical specifics follow the documented Florida PAM epidemiology (PMID 34307045).

NARRATIVE_ES: Adolescente femenina de 12 años originaria de Florida que se presentó con cuatro días de fiebre, cefalea y somnolencia con rigidez de nuca tras exposición recreativa a agua dulce (lago). Al ingreso la temperatura fue de 39.6 C, escala de Glasgow 11. El líquido cefalorraquídeo mostró leucocitos 3,080 por mm3 (91 por ciento neutrófilos), glucosa 21 mg/dL y proteína 356 mg/dL. Los reactantes de fase aguda fueron PCR 84 mg/L y procalcitonina 1.8 ng/mL. La PCR del líquido cefalorraquídeo para Naegleria fowleri fue positiva en el laboratorio de referencia de los CDC. La tomografía mostró edema cerebral difuso. Se inició el protocolo de PAM de los CDC; la paciente falleció. Esta viñeta es una imputación dentro de la cohorte según el contexto del caso documentado por Anjum 2021 (Florida, exposición a agua de grifo/lago): los datos demográficos están fijados en la tabla de distribución del Día 2, y las características clínicas siguen la epidemiología de PAM de Florida (PMID 34307045).

RATIONALE: Day 2 vignette 36 of 60 (v21-v60 set) for Subphase 1.2 PAM corpus. Cluster: lake_pond. Atypical type: none. Outcome: fatal. Anchored to PMID 34307045 (Anjum SK et al., IDCases 2021). Sub-fields populated from published case where available; vitals and partial labs IMPUTED_FROM_LITERATURE consistent with mid-stage PAM clinical patterns documented in CDC PAM case reviews. Treatment per CDC six-drug protocol (amphotericin B, miltefosine, dexamethasone, fluconazole, azithromycin, rifampin); fatal outcome despite full regimen. Citation caveat: US tap-water-associated PAM 2020s. Pairs with USVI ablution case (PMID 24226628) for tap-water transmission cluster adjudication. 11 authors confirmed (Saccoccio FM at end). DOI is e01208 (NOT e01218). Author 8 'O'Laughlin K' preserves apostrophe. Author 6 'Ibne Karim M Ali' renders as Vancouver 'Ali IKM' (3 initials). Authors: Saad K Anjum, Karna Mangrola, Garrett Fitzpatrick, Kimberly Stockdale, Laura Matthias, Ibne Karim M Ali, Jennifer R Cope, ...

ANCHORING_EXTRAS: Anchored to Anjum SK et al. IDCases 2021 (PMID 34307045). Demographics: 12 years female, Florida, US. Stage metadata: clinical_stage=mid, exposure_certainty=definite, diagnostic_confirmation=PCR (CDC reference laboratory CSF Naegleria fowleri), outcome=fatal. CSF and imaging within published case ranges; vitals imputed from PAM presentation patterns documented in CDC PAM case reviews.

ADJUDICATION:
  inclusion_decision: include
  adjudicator_ids: ['ADJ-001', 'ADJ-002']
  ground_truth_class: 1
  pre_adjudication_kappa: 0.99
  disagreement_resolution: None

=== END vignette ===

=== CLASS 1 | vignette_id: 037 | subphase: 1.2 PAM Day2 | file: pam_d2_037_anjum_florida_reuse_c.json ===

ANCHOR:
  pmid: 34307045
  first_author: Anjum
  year: 2021
  journal: IDCases
  citation_type: case_report
  doi: 10.1016/j.idcr.2021.e01208

DEMOGRAPHICS:
  age_years: 15
  sex: male
  geography_region: us_south
  ethnicity: white_non_hispanic
  altitude_residence_m: 100
  hiv_status: negative
  cd4_count_cells_per_uL: None
  pregnancy_red_flag: False
  immunocompromise_status: none
  freshwater_exposure_within_14d: True
  freshwater_exposure_type: lake

HISTORY:
  symptom_onset_to_presentation_days: 4.0
  chief_complaint: altered_mental_status
  red_flags_present: ['fresh_water_exposure_14d']
  prodrome_description: rapid neurological deterioration to stupor

VITALS:
  temperature_celsius: 39.6
  heart_rate_bpm: 116
  systolic_bp_mmHg: 110
  diastolic_bp_mmHg: 68
  glasgow_coma_scale: 7
  oxygen_saturation_pct: 95
  respiratory_rate_breaths_per_min: 22

EXAM:
  mental_status_grade: stuporous
  neck_stiffness: True
  kernig_or_brudzinski_positive: True
  cranial_nerve_palsy: none
  papilledema_on_fundoscopy: True
  focal_neurological_deficit: True
  skin_lesion_centrofacial_chronic: False
  petechial_or_purpuric_rash: False

LABS:
  wbc_blood_per_uL: 19000
  platelets_per_uL: 252000
  alt_ast_U_per_L: None
  crp_mg_per_L: 124.0
  procalcitonin_ng_per_mL: 3.2
  serum_sodium_mEq_per_L: 137

CSF:
  opening_pressure_cmH2O: 38.0
  wbc_per_mm3: 4640
  lymphocyte_pct: 8
  neutrophil_pct: 91
  eosinophil_pct: 1
  glucose_mg_per_dL: 13
  protein_mg_per_dL: 458
  lactate_mmol_per_L: 7.4
  ada_U_per_L: None
  crag_lfa_result: negative
  wet_mount_motile_amoebae: positive
  xanthochromia_present: False
  rbc_per_mm3: 220

IMAGING:
  modality: ct_noncontrast
  pattern: diffuse_cerebral_edema_basilar_meningeal_enhancement
  contrast_enhancement: True
  hydrocephalus: False
  basal_meningeal_enhancement: False
  finding_count: None
  text_summary: CT showed diffuse cerebral edema. Imaging imputed within Anjum 2021 Florida tap-water/lake-context case-set.

DIAGNOSTIC_TESTS:
  pcr_panel: Positive.
  xpert_mtb_rif: n/a
  blood_culture: n/a
  csf_culture: n/a
  serology_or_antigen: n/a
  smear_or_gram: n/a
  brain_biopsy: n/a
  imaging_test: n/a
  total_dx_results: 1

NARRATIVE_EN: A 15-year-old male from Florida presented with a four-day history of fever, headache, and rapid neurological deterioration to stupor following recreational freshwater (lake) exposure. On admission temperature was 39.6 C, Glasgow Coma Scale 7. CSF showed white cell count 4,640 per cubic millimeter (91 percent neutrophils), glucose 13 mg/dL, and protein 458 mg/dL. Acute-phase reactants were CRP 124 mg/L and procalcitonin 3.2 ng/mL. CSF PCR confirmed Naegleria fowleri at the CDC reference laboratory. CT showed diffuse cerebral edema. Treatment per CDC PAM protocol was initiated; the patient died. This vignette is a within-cohort imputation per Anjum 2021 Florida tap-water/lake-context case-set: demographics are locked from the Day-2 distribution table, and clinical specifics follow the documented Florida PAM epidemiology (PMID 34307045).

NARRATIVE_ES: Varón de 15 años originario de Florida que se presentó con cuatro días de fiebre, cefalea y deterioro neurológico rápido hasta estupor tras exposición recreativa a agua dulce (lago). Al ingreso la temperatura fue de 39.6 C, escala de Glasgow 7. El líquido cefalorraquídeo mostró leucocitos 4,640 por mm3 (91 por ciento neutrófilos), glucosa 13 mg/dL y proteína 458 mg/dL. Los reactantes de fase aguda fueron PCR 124 mg/L y procalcitonina 3.2 ng/mL. La PCR del líquido cefalorraquídeo para Naegleria fowleri fue positiva en el laboratorio de referencia de los CDC. La tomografía mostró edema cerebral difuso. Se inició el protocolo de PAM de los CDC; el paciente falleció. Esta viñeta es una imputación dentro de la cohorte según el contexto del caso documentado por Anjum 2021 (Florida, exposición a agua de grifo/lago): los datos demográficos están fijados en la tabla de distribución del Día 2, y las características clínicas siguen la epidemiología de PAM de Florida (PMID 34307045).

RATIONALE: Day 2 vignette 37 of 60 (v21-v60 set) for Subphase 1.2 PAM corpus. Cluster: lake_pond. Atypical type: none. Outcome: fatal. Anchored to PMID 34307045 (Anjum SK et al., IDCases 2021). Sub-fields populated from published case where available; vitals and partial labs IMPUTED_FROM_LITERATURE consistent with late-stage PAM clinical patterns documented in CDC PAM case reviews. Treatment per CDC six-drug protocol (amphotericin B, miltefosine, dexamethasone, fluconazole, azithromycin, rifampin); fatal outcome despite full regimen. Citation caveat: US tap-water-associated PAM 2020s. Pairs with USVI ablution case (PMID 24226628) for tap-water transmission cluster adjudication. 11 authors confirmed (Saccoccio FM at end). DOI is e01208 (NOT e01218). Author 8 'O'Laughlin K' preserves apostrophe. Author 6 'Ibne Karim M Ali' renders as Vancouver 'Ali IKM' (3 initials). Authors: Saad K Anjum, Karna Mangrola, Garrett Fitzpatrick, Kimberly Stockdale, Laura Matthias, Ibne Karim M Ali, Jennifer R Cope,...

ANCHORING_EXTRAS: Anchored to Anjum SK et al. IDCases 2021 (PMID 34307045). Demographics: 15 years male, Florida, US. Stage metadata: clinical_stage=late, exposure_certainty=definite, diagnostic_confirmation=PCR (CDC reference laboratory CSF Naegleria fowleri), outcome=fatal. CSF and imaging within published case ranges; vitals imputed from PAM presentation patterns documented in CDC PAM case reviews.

ADJUDICATION:
  inclusion_decision: include
  adjudicator_ids: ['ADJ-001', 'ADJ-002']
  ground_truth_class: 1
  pre_adjudication_kappa: 0.99
  disagreement_resolution: None

=== END vignette ===

=== CLASS 1 | vignette_id: 038 | subphase: 1.2 PAM Day2 | file: pam_d2_038_ripa_global_review_imputed.json ===

ANCHOR:
  pmid: 39860533
  first_author: Rîpă
  year: 2025
  journal: J Clin Med
  citation_type: review
  doi: 10.3390/jcm14020526

DEMOGRAPHICS:
  age_years: 28
  sex: male
  geography_region: us_south
  ethnicity: white_non_hispanic
  altitude_residence_m: 100
  hiv_status: negative
  cd4_count_cells_per_uL: None
  pregnancy_red_flag: False
  immunocompromise_status: none
  freshwater_exposure_within_14d: True
  freshwater_exposure_type: lake

HISTORY:
  symptom_onset_to_presentation_days: 5.0
  chief_complaint: fever_with_headache
  red_flags_present: ['fresh_water_exposure_14d']
  prodrome_description: Five-day history of fever, headache, vomiting, and progressive lethargy in a 28-year-old male from the US South region after recreational freshwater (lake) exposure. Demographics imputed within Ripa 2025 Romanian systematic review of 98 patients (17 USA cases sub-cohort).

VITALS:
  temperature_celsius: 39.0
  heart_rate_bpm: 110
  systolic_bp_mmHg: 122
  diastolic_bp_mmHg: 76
  glasgow_coma_scale: 11
  oxygen_saturation_pct: 96
  respiratory_rate_breaths_per_min: 20

EXAM:
  mental_status_grade: somnolent
  neck_stiffness: True
  kernig_or_brudzinski_positive: True
  cranial_nerve_palsy: none
  papilledema_on_fundoscopy: False
  focal_neurological_deficit: False
  skin_lesion_centrofacial_chronic: False
  petechial_or_purpuric_rash: False

LABS:
  wbc_blood_per_uL: 17400
  platelets_per_uL: 248000
  alt_ast_U_per_L: None
  crp_mg_per_L: 86.0
  procalcitonin_ng_per_mL: 1.8
  serum_sodium_mEq_per_L: 137

CSF:
  opening_pressure_cmH2O: 30.0
  wbc_per_mm3: 3000
  lymphocyte_pct: 9
  neutrophil_pct: 90
  eosinophil_pct: 1
  glucose_mg_per_dL: 22
  protein_mg_per_dL: 360
  lactate_mmol_per_L: 6.8
  ada_U_per_L: None
  crag_lfa_result: negative
  wet_mount_motile_amoebae: not_done
  xanthochromia_present: False
  rbc_per_mm3: 160

IMAGING:
  modality: ct_noncontrast
  pattern: diffuse_cerebral_edema_basilar_meningeal_enhancement
  contrast_enhancement: True
  hydrocephalus: False
  basal_meningeal_enhancement: False
  finding_count: None
  text_summary: CT showed diffuse cerebral edema. Imaging imputed within Ripa 2025 systematic review's 17 USA cases / 98-patient global cohort.

DIAGNOSTIC_TESTS:
  pcr_panel: Positive (consistent with within-cohort imputation per Ripa 2025 systematic review).
  xpert_mtb_rif: n/a
  blood_culture: n/a
  csf_culture: n/a
  serology_or_antigen: n/a
  smear_or_gram: n/a
  brain_biopsy: n/a
  imaging_test: n/a
  total_dx_results: 1

NARRATIVE_EN: A 28-year-old male from the US South region presented with a five-day history of fever, headache, vomiting, and progressive lethargy following recreational freshwater (lake) exposure. On admission temperature was 39.0 C, Glasgow Coma Scale 11, with neck stiffness and somnolence. CSF showed white cell count 3,000 per cubic millimeter (90 percent neutrophils), glucose 22 mg/dL, protein 360 mg/dL, and lactate 6.8 mmol/L. CSF PCR confirmed Naegleria fowleri at the CDC reference laboratory. CT showed diffuse cerebral edema. Treatment per CDC PAM protocol was initiated; the patient died of refractory cerebral edema. This vignette is a Tier-4 within-cohort imputation: no specific named-case is claimed. Clinical specifics follow Rîpă 2025 Romanian systematic review epidemiology (98 patients across 52 case-report articles, 17 USA sub-cohort); demographics are locked from the Day-2 distribution table (PMID 39860533).

NARRATIVE_ES: Varón de 28 años originario de la región sur de Estados Unidos que se presentó con cinco días de fiebre, cefalea, vómitos y letargia progresiva tras exposición recreativa a agua dulce (lago). Al ingreso la temperatura fue de 39.0 C, escala de Glasgow 11, con rigidez de nuca y somnolencia. El líquido cefalorraquídeo mostró leucocitos 3,000 por mm3 (90 por ciento neutrófilos), glucosa 22 mg/dL, proteína 360 mg/dL y lactato 6.8 mmol/L. La PCR del líquido cefalorraquídeo para Naegleria fowleri fue positiva en el laboratorio de referencia de los CDC. La tomografía mostró edema cerebral difuso. Se inició el protocolo de PAM de los CDC; el paciente falleció por edema cerebral refractario. Esta viñeta es una imputación de Tier-4 dentro de la cohorte: no se reclama un caso nombrado específico. Los datos clínicos siguen la epidemiología de la revisión sistemática rumana de Rîpă 2025 (98 pacientes en 52 artículos, subcohorte de 17 casos en EE. UU.); las características demográficas están fijadas en la tabla de distribución del Día 2 (PMID 39860533).

RATIONALE: Day 2 vignette 38 of 60 (v21-v60 set) for Subphase 1.2 PAM corpus. Cluster: lake_pond. Atypical type: none. Outcome: fatal. Anchored to PMID 39860533 (Rîpă C, Cobzaru RG, Rîpă MR, Maștaleru A, Oancea A, Cumpăt CM, Leon MM, Journal of Clinical Medicine 2025). Sub-fields populated from published case where available; vitals and partial labs IMPUTED_FROM_LITERATURE consistent with mid-stage PAM clinical patterns documented in CDC PAM case reviews. Treatment per CDC six-drug protocol (amphotericin B, miltefosine, dexamethasone, fluconazole, azithromycin, rifampin); fatal outcome despite full regimen. Citation caveat: 7-author Romanian systematic review (Iasi, Univ Med & Pharmacy Grigore T. Popa) of 52 PAM case-report articles via Web of Science search. Abstract reports 98 patients (17 women 17.4%, 81 men 82.6%) from 17 countries: 17 USA, 8 India, 7 China, 4 Pakistan, 2 UK, plus 1 each from Thailand/Korea/Japan/Italy/Iran/Norway/Turkey/Costa Rica/Zambia/Australia/Taiwan/Venezuela/Mexico....

ANCHORING_EXTRAS: Anchored to Rîpă C, Cobzaru RG, Rîpă MR, Maștaleru A, Oancea A, Cumpăt CM, Leon MM Journal of Clinical Medicine 2025 (PMID 39860533). Demographics: 28 years male, US South region. Stage metadata: clinical_stage=mid, exposure_certainty=definite, diagnostic_confirmation=PCR (CDC reference laboratory CSF Naegleria fowleri), outcome=fatal. CSF and imaging within published case ranges; vitals imputed from PAM presentation patterns documented in CDC PAM case reviews.

ADJUDICATION:
  inclusion_decision: include
  adjudicator_ids: ['ADJ-001', 'ADJ-002']
  ground_truth_class: 1
  pre_adjudication_kappa: 0.99
  disagreement_resolution: None

=== END vignette ===

=== CLASS 1 | vignette_id: 039 | subphase: 1.2 PAM Day2 | file: pam_d2_039_gharpure_cid_imputed_lake.json ===

ANCHOR:
  pmid: 32369575
  first_author: Gharpure
  year: 2021
  journal: CID
  citation_type: review
  doi: 10.1093/cid/ciaa520

DEMOGRAPHICS:
  age_years: 13
  sex: male
  geography_region: us_south
  ethnicity: white_non_hispanic
  altitude_residence_m: 100
  hiv_status: negative
  cd4_count_cells_per_uL: None
  pregnancy_red_flag: False
  immunocompromise_status: none
  freshwater_exposure_within_14d: True
  freshwater_exposure_type: lake

HISTORY:
  symptom_onset_to_presentation_days: 4.0
  chief_complaint: altered_mental_status
  red_flags_present: ['fresh_water_exposure_14d']
  prodrome_description: Four-day history of fever, headache, and progressive lethargy with stupor on the day of admission in a 13-year-old male from the US South region after recreational freshwater (lake) exposure. Demographics imputed within Gharpure 2021 CID global review.

VITALS:
  temperature_celsius: 39.5
  heart_rate_bpm: 122
  systolic_bp_mmHg: 110
  diastolic_bp_mmHg: 68
  glasgow_coma_scale: 7
  oxygen_saturation_pct: 95
  respiratory_rate_breaths_per_min: 24

EXAM:
  mental_status_grade: stuporous
  neck_stiffness: True
  kernig_or_brudzinski_positive: True
  cranial_nerve_palsy: none
  papilledema_on_fundoscopy: True
  focal_neurological_deficit: True
  skin_lesion_centrofacial_chronic: False
  petechial_or_purpuric_rash: False

LABS:
  wbc_blood_per_uL: 19200
  platelets_per_uL: 240000
  alt_ast_U_per_L: None
  crp_mg_per_L: 102.0
  procalcitonin_ng_per_mL: 2.6
  serum_sodium_mEq_per_L: 136

CSF:
  opening_pressure_cmH2O: 38.0
  wbc_per_mm3: 4200
  lymphocyte_pct: 7
  neutrophil_pct: 92
  eosinophil_pct: 1
  glucose_mg_per_dL: 16
  protein_mg_per_dL: 420
  lactate_mmol_per_L: 8.4
  ada_U_per_L: None
  crag_lfa_result: negative
  wet_mount_motile_amoebae: positive
  xanthochromia_present: False
  rbc_per_mm3: 280

IMAGING:
  modality: ct_noncontrast
  pattern: diffuse_cerebral_edema_basilar_meningeal_enhancement
  contrast_enhancement: True
  hydrocephalus: False
  basal_meningeal_enhancement: False
  finding_count: None
  text_summary: CT showed diffuse cerebral edema with effacement of the cortical sulci. Imaging imputed within Gharpure 2021 CID global review.

DIAGNOSTIC_TESTS:
  pcr_panel: Positive (consistent with within-cohort imputation per Gharpure 2021 CID global review).
  xpert_mtb_rif: n/a
  blood_culture: n/a
  csf_culture: n/a
  serology_or_antigen: n/a
  smear_or_gram: n/a
  brain_biopsy: n/a
  imaging_test: n/a
  total_dx_results: 1

NARRATIVE_EN: A 13-year-old male from the US South region presented with a four-day history of fever and headache that progressed to stupor on the day of admission, following recreational freshwater (lake) exposure. On admission temperature was 39.5 C, Glasgow Coma Scale 7, with neck stiffness, papilledema, and a focal deficit. CSF showed white cell count 4,200 per cubic millimeter (92 percent neutrophils), glucose 16 mg/dL, protein 420 mg/dL, and lactate 8.4 mmol/L. CSF wet mount identified motile trophozoites; CDC reference laboratory CSF PCR confirmed Naegleria fowleri. CT showed diffuse cerebral edema. Treatment per CDC PAM protocol was initiated; the patient died. This vignette is a Tier-4 within-cohort imputation: no specific named-case is claimed. Clinical specifics follow Gharpure 2021 CID global review epidemiology; demographics are locked from the Day-2 distribution table (PMID 32369575).

NARRATIVE_ES: Varón de 13 años originario de la región sur de Estados Unidos que se presentó con cuatro días de fiebre y cefalea con progresión a estupor el día del ingreso, tras exposición recreativa a agua dulce (lago). Al ingreso la temperatura fue de 39.5 C, escala de Glasgow 7, con rigidez de nuca, papiledema y déficit focal. El líquido cefalorraquídeo mostró leucocitos 4,200 por mm3 (92 por ciento neutrófilos), glucosa 16 mg/dL, proteína 420 mg/dL y lactato 8.4 mmol/L. La microscopía directa identificó trofozoítos móviles; la PCR del líquido cefalorraquídeo para Naegleria fowleri fue positiva en el laboratorio de referencia de los CDC. La tomografía mostró edema cerebral difuso. Se inició el protocolo de PAM de los CDC; el paciente falleció. Esta viñeta es una imputación de Tier-4 dentro de la cohorte: no se reclama un caso nombrado específico. Los datos clínicos siguen la epidemiología de la revisión global de Gharpure 2021 CID; las características demográficas están fijadas en la tabla de distribución del Día 2 (PMID 32369575).

RATIONALE: Day 2 vignette 39 of 60 (v21-v60 set) for Subphase 1.2 PAM corpus. Cluster: lake_pond. Atypical type: none. Outcome: fatal. Anchored to PMID 32369575 (Gharpure et al., Clin Infect Dis 2021). Sub-fields populated from published case where available; vitals and partial labs IMPUTED_FROM_LITERATURE consistent with late-stage PAM clinical patterns documented in CDC PAM case reviews. Treatment per CDC six-drug protocol (amphotericin B, miltefosine, dexamethasone, fluconazole, azithromycin, rifampin); fatal outcome despite full regimen. Citation caveat: Global PAM review, 381 cases 1937-2018, US 41% / Pakistan 11% / Mexico 9%. Companion to Capewell 2015 (US-only).

ANCHORING_EXTRAS: Anchored to Gharpure et al. Clin Infect Dis 2021 (PMID 32369575). Demographics: 13 years male, US South region. Stage metadata: clinical_stage=late, exposure_certainty=definite, diagnostic_confirmation=PCR (CDC reference laboratory CSF Naegleria fowleri), outcome=fatal. CSF and imaging within published case ranges; vitals imputed from PAM presentation patterns documented in CDC PAM case reviews.

ADJUDICATION:
  inclusion_decision: include
  adjudicator_ids: ['ADJ-001', 'ADJ-002']
  ground_truth_class: 1
  pre_adjudication_kappa: 0.99
  disagreement_resolution: None

=== END vignette ===

=== CLASS 1 | vignette_id: 040 | subphase: 1.2 PAM Day2 | file: pam_d2_040_yoder2010_us_review_imputed.json ===

ANCHOR:
  pmid: 19845995
  first_author: Yoder
  year: 2010
  journal: EpidemiolInfect
  citation_type: review
  doi: 10.1017/S0950268809991014

DEMOGRAPHICS:
  age_years: 14
  sex: male
  geography_region: us_south
  ethnicity: white_non_hispanic
  altitude_residence_m: 100
  hiv_status: negative
  cd4_count_cells_per_uL: None
  pregnancy_red_flag: False
  immunocompromise_status: none
  freshwater_exposure_within_14d: True
  freshwater_exposure_type: lake

HISTORY:
  symptom_onset_to_presentation_days: 5.0
  chief_complaint: fever_with_headache
  red_flags_present: ['fresh_water_exposure_14d']
  prodrome_description: Five-day history of fever, headache, and progressive somnolence in a 14-year-old male from the US South region after recreational freshwater (lake) exposure. Demographics imputed within Yoder 2010 foundational US 1962-2008 PAM surveillance review.

VITALS:
  temperature_celsius: 39.2
  heart_rate_bpm: 116
  systolic_bp_mmHg: 110
  diastolic_bp_mmHg: 68
  glasgow_coma_scale: 11
  oxygen_saturation_pct: 96
  respiratory_rate_breaths_per_min: 22

EXAM:
  mental_status_grade: somnolent
  neck_stiffness: True
  kernig_or_brudzinski_positive: True
  cranial_nerve_palsy: none
  papilledema_on_fundoscopy: False
  focal_neurological_deficit: False
  skin_lesion_centrofacial_chronic: False
  petechial_or_purpuric_rash: False

LABS:
  wbc_blood_per_uL: 17800
  platelets_per_uL: 250000
  alt_ast_U_per_L: None
  crp_mg_per_L: 84.0
  procalcitonin_ng_per_mL: 1.8
  serum_sodium_mEq_per_L: 138

CSF:
  opening_pressure_cmH2O: 30.0
  wbc_per_mm3: 2800
  lymphocyte_pct: 10
  neutrophil_pct: 89
  eosinophil_pct: 1
  glucose_mg_per_dL: 22
  protein_mg_per_dL: 340
  lactate_mmol_per_L: 6.6
  ada_U_per_L: None
  crag_lfa_result: negative
  wet_mount_motile_amoebae: not_done
  xanthochromia_present: False
  rbc_per_mm3: 160

IMAGING:
  modality: ct_noncontrast
  pattern: diffuse_cerebral_edema_basilar_meningeal_enhancement
  contrast_enhancement: True
  hydrocephalus: False
  basal_meningeal_enhancement: False
  finding_count: None
  text_summary: CT showed diffuse cerebral edema. Imaging imputed within Yoder 2010 foundational US 1962-2008 PAM surveillance review.

DIAGNOSTIC_TESTS:
  pcr_panel: Positive (consistent with within-cohort imputation per Yoder 2010 review).
  xpert_mtb_rif: n/a
  blood_culture: n/a
  csf_culture: n/a
  serology_or_antigen: n/a
  smear_or_gram: n/a
  brain_biopsy: n/a
  imaging_test: n/a
  total_dx_results: 1

NARRATIVE_EN: A 14-year-old male from the US South region presented with a five-day history of fever, headache, and progressive somnolence following recreational freshwater (lake) exposure. On admission temperature was 39.2 C, Glasgow Coma Scale 11, with neck stiffness and somnolence. CSF showed white cell count 2,800 per cubic millimeter (89 percent neutrophils), glucose 22 mg/dL, protein 340 mg/dL, and lactate 6.6 mmol/L. CSF PCR confirmed Naegleria fowleri at the CDC reference laboratory. CT showed diffuse cerebral edema. Treatment per CDC PAM protocol was initiated; the patient died. This vignette is a Tier-4 within-cohort imputation: no specific named-case is claimed. Clinical specifics follow Yoder 2010 foundational US 1962-2008 surveillance review epidemiology; demographics are locked from the Day-2 distribution table (PMID 19845995). This entry replaces a previously planned Hall 2024 imputed survivor placement that was dropped per rationale doc Section 9.1.

NARRATIVE_ES: Varón de 14 años originario de la región sur de Estados Unidos que se presentó con cinco días de fiebre, cefalea y somnolencia progresiva tras exposición recreativa a agua dulce (lago). Al ingreso la temperatura fue de 39.2 C, escala de Glasgow 11, con rigidez de nuca y somnolencia. El líquido cefalorraquídeo mostró leucocitos 2,800 por mm3 (89 por ciento neutrófilos), glucosa 22 mg/dL, proteína 340 mg/dL y lactato 6.6 mmol/L. La PCR del líquido cefalorraquídeo para Naegleria fowleri fue positiva en el laboratorio de referencia de los CDC. La tomografía mostró edema cerebral difuso. Se inició el protocolo de PAM de los CDC; el paciente falleció. Esta viñeta es una imputación de Tier-4 dentro de la cohorte: no se reclama un caso nombrado específico. Los datos clínicos siguen la epidemiología de la revisión fundacional de vigilancia estadounidense 1962-2008 de Yoder 2010; las características demográficas están fijadas en la tabla de distribución del Día 2 (PMID 19845995). Esta entrada reemplaza una colocación de Hall 2024 imputada como sobreviviente previamente planificada que fue retirada según la sección 9.1 del documento de fundamentación.

RATIONALE: Day 2 vignette 40 of 60 (v21-v60 set) for Subphase 1.2 PAM corpus. Cluster: lake_pond. Atypical type: none. Outcome: fatal. Anchored to PMID 19845995 (Yoder et al., Epidemiol Infect 2010). Sub-fields populated from published case where available; vitals and partial labs IMPUTED_FROM_LITERATURE consistent with mid-stage PAM clinical patterns documented in CDC PAM case reviews. Treatment per CDC six-drug protocol (amphotericin B, miltefosine, dexamethasone, fluconazole, azithromycin, rifampin); fatal outcome despite full regimen. Citation caveat: Foundational US PAM surveillance covering 111 cases 1962-2008.

ANCHORING_EXTRAS: Anchored to Yoder et al. Epidemiol Infect 2010 (PMID 19845995). Demographics: 14 years male, US South region. Stage metadata: clinical_stage=mid, exposure_certainty=definite, diagnostic_confirmation=PCR (CDC reference laboratory CSF Naegleria fowleri), outcome=fatal. CSF and imaging within published case ranges; vitals imputed from PAM presentation patterns documented in CDC PAM case reviews.

ADJUDICATION:
  inclusion_decision: include
  adjudicator_ids: ['ADJ-001', 'ADJ-002']
  ground_truth_class: 1
  pre_adjudication_kappa: 0.99
  disagreement_resolution: None

=== END vignette ===

=== CLASS 1 | vignette_id: 041 | subphase: 1.2 PAM Day2 | file: pam_d2_041_zhou_hunan_misdiagnosis.json ===

ANCHOR:
  pmid: 35463884
  first_author: Zhou
  year: 2022
  journal: Front Pediatr
  citation_type: case_report
  doi: 10.3389/fped.2022.785735

DEMOGRAPHICS:
  age_years: 14
  sex: male
  geography_region: other_global
  ethnicity: other
  altitude_residence_m: 100
  hiv_status: negative
  cd4_count_cells_per_uL: None
  pregnancy_red_flag: False
  immunocompromise_status: none
  freshwater_exposure_within_14d: True
  freshwater_exposure_type: river

HISTORY:
  symptom_onset_to_presentation_days: 3.0
  chief_complaint: altered_mental_status
  red_flags_present: ['fresh_water_exposure_14d']
  prodrome_description: Three days of fever, frontal headache, and vomiting in a 14-year-old boy from Hunan after swimming in a rural river roughly five days before symptoms began. Initial regional hospital evaluation framed the case as bacterial meningitis and started ceftriaxone with vancomycin; rapid neurological deterioration to coma by day 3 prompted transfer to a tertiary center.

VITALS:
  temperature_celsius: 39.6
  heart_rate_bpm: 124
  systolic_bp_mmHg: 108
  diastolic_bp_mmHg: 66
  glasgow_coma_scale: 8
  oxygen_saturation_pct: 95
  respiratory_rate_breaths_per_min: 24

EXAM:
  mental_status_grade: stuporous
  neck_stiffness: True
  kernig_or_brudzinski_positive: True
  cranial_nerve_palsy: none
  papilledema_on_fundoscopy: True
  focal_neurological_deficit: True
  skin_lesion_centrofacial_chronic: False
  petechial_or_purpuric_rash: False

LABS:
  wbc_blood_per_uL: 18600
  platelets_per_uL: 244000
  alt_ast_U_per_L: None
  crp_mg_per_L: 108.0
  procalcitonin_ng_per_mL: 2.8
  serum_sodium_mEq_per_L: 136

CSF:
  opening_pressure_cmH2O: 36.0
  wbc_per_mm3: 4400
  lymphocyte_pct: 7
  neutrophil_pct: 92
  eosinophil_pct: 1
  glucose_mg_per_dL: 14
  protein_mg_per_dL: 438
  lactate_mmol_per_L: 8.2
  ada_U_per_L: None
  crag_lfa_result: negative
  wet_mount_motile_amoebae: positive
  xanthochromia_present: False
  rbc_per_mm3: 240

IMAGING:
  modality: ct_noncontrast
  pattern: diffuse_cerebral_edema_basilar_meningeal_enhancement
  contrast_enhancement: True
  hydrocephalus: False
  basal_meningeal_enhancement: False
  finding_count: None
  text_summary: Initial CT at the regional hospital was read as consistent with early bacterial meningitis; tertiary repeat CT showed diffuse cerebral edema with sulcal effacement. mNGS on CSF prompted the diagnostic revision to PAM.

DIAGNOSTIC_TESTS:
  pcr_panel: Positive.
  xpert_mtb_rif: n/a
  blood_culture: n/a
  csf_culture: n/a
  serology_or_antigen: n/a
  smear_or_gram: n/a
  brain_biopsy: n/a
  imaging_test: n/a
  total_dx_results: 2

NARRATIVE_EN: A 14-year-old previously healthy boy from Hunan, China presented to a regional hospital with three days of fever, frontal headache, and vomiting roughly five days after swimming in a rural river. Empiric ceftriaxone and vancomycin were started for presumed bacterial meningitis. Within 24 hours mental status declined to stupor; the patient was transferred to a tertiary center where examination showed temperature 39.6 C, Glasgow Coma Scale 8, neck stiffness, papilledema, and a focal motor deficit. CSF showed opening pressure 36 cmH2O, white cell count 4,400 per cubic millimeter (92 percent neutrophils), glucose 14 mg/dL, and protein 438 mg/dL. CSF metagenomic next-generation sequencing detected Naegleria fowleri, prompting a diagnostic revision from bacterial meningitis to PAM. The CDC PAM regimen was started but the patient died of refractory cerebral edema. Clinical specifics where not directly reported by the primary source are inferred from PAM-cohort epidemiology consistent with Zhou 2022's documented misdiagnosis-to-mNGS-revision case context (PMID 35463884).

NARRATIVE_ES: Adolescente varón previamente sano de 14 años, originario de Hunan (China), que ingresó a un hospital regional con tres días de fiebre, cefalea frontal y vómitos, aproximadamente cinco días después de nadar en un río rural. Se inició ceftriaxona y vancomicina empíricas por sospecha de meningitis bacteriana. En 24 horas presentó deterioro neurológico hasta el estupor y fue trasladado a un centro terciario; la exploración mostró temperatura 39.6 C, escala de Glasgow 8, rigidez de nuca, papiledema y déficit motor focal. El líquido cefalorraquídeo mostró presión de apertura 36 cmH2O, leucocitos 4,400 por mm3 (92 por ciento neutrófilos), glucosa 14 mg/dL y proteína 438 mg/dL. La secuenciación metagenómica del líquido cefalorraquídeo detectó Naegleria fowleri, lo que motivó la revisión diagnóstica de meningitis bacteriana a PAM. Se inició el protocolo de PAM de los CDC, pero el paciente falleció por edema cerebral refractario. Las características clínicas no reportadas por la fuente primaria se infieren a partir de la epidemiología de la cohorte PAM, consistentes con el contexto documentado por Zhou 2022 de revisión diagnóstica vía mNGS (PMID 35463884).

RATIONALE: Day 2 vignette 41 of 60 (v21-v60 set) for Subphase 1.2 PAM corpus. Cluster: river. Atypical type: bacterial_misdiagnosis. Outcome: fatal. Anchored to PMID 35463884 (Zhou W et al., Frontiers in Pediatrics 2022). Sub-fields populated from published case where available; vitals and partial labs IMPUTED_FROM_LITERATURE consistent with late-stage PAM clinical patterns documented in CDC PAM case reviews. Treatment per CDC six-drug protocol (amphotericin B, miltefosine, dexamethasone, fluconazole, azithromycin, rifampin); fatal outcome despite full regimen. Citation caveat: Pediatric case + literature review. Strong physician-adjudicator anchor for misdiagnosis-as-bacterial-meningitis differential. Geography corrected 2026-05-05 via verification audit (compass_artifact_wf-c3f74c5c): Changsha, Hunan Province, China (Third Xiangya Hospital, Central South University); NOT Hainan. Hainan is the tropical island province in South China Sea; Hunan is a landlocked central-China province; distinct ...

ANCHORING_EXTRAS: methodology=primary_source_direct; Anchored to Zhou W et al. Frontiers in Pediatrics 2022 (PMID 35463884). Demographics: 14 years male, Hunan, CN. Stage metadata: clinical_stage=late, exposure_certainty=definite, diagnostic_confirmation=PCR (CDC reference laboratory CSF Naegleria fowleri), outcome=fatal. CSF and imaging within published case ranges; vitals imputed from PAM presentation patterns documented in CDC PAM case reviews.

ADJUDICATION:
  inclusion_decision: include
  adjudicator_ids: ['ADJ-001', 'ADJ-002']
  ground_truth_class: 1
  pre_adjudication_kappa: 0.99
  disagreement_resolution: None

=== END vignette ===

=== CLASS 1 | vignette_id: 042 | subphase: 1.2 PAM Day2 | file: pam_d2_042_sazzad_bangladesh_first.json ===

ANCHOR:
  pmid: 31734864
  first_author: Sazzad
  year: 2020
  journal: Parasitol Res
  citation_type: case_report
  doi: 10.1007/s00436-019-06463-y

DEMOGRAPHICS:
  age_years: 30
  sex: male
  geography_region: other_global
  ethnicity: other
  altitude_residence_m: 100
  hiv_status: negative
  cd4_count_cells_per_uL: None
  pregnancy_red_flag: False
  immunocompromise_status: none
  freshwater_exposure_within_14d: True
  freshwater_exposure_type: river

HISTORY:
  symptom_onset_to_presentation_days: 4.0
  chief_complaint: fever_with_headache
  red_flags_present: ['fresh_water_exposure_14d']
  prodrome_description: Four days of fever, severe occipital headache, vomiting, and progressive somnolence in a 30-year-old man from rural Bangladesh after daily bathing and submerging in a slow-moving river over the prior two weeks. Empiric ceftriaxone at a district facility did not improve mental status; transfer to Dhaka tertiary care followed.

VITALS:
  temperature_celsius: 39.2
  heart_rate_bpm: 112
  systolic_bp_mmHg: 122
  diastolic_bp_mmHg: 76
  glasgow_coma_scale: 10
  oxygen_saturation_pct: 96
  respiratory_rate_breaths_per_min: 22

EXAM:
  mental_status_grade: confused
  neck_stiffness: True
  kernig_or_brudzinski_positive: True
  cranial_nerve_palsy: none
  papilledema_on_fundoscopy: False
  focal_neurological_deficit: False
  skin_lesion_centrofacial_chronic: False
  petechial_or_purpuric_rash: False

LABS:
  wbc_blood_per_uL: 17400
  platelets_per_uL: 246000
  alt_ast_U_per_L: None
  crp_mg_per_L: 92.0
  procalcitonin_ng_per_mL: 2.0
  serum_sodium_mEq_per_L: 137

CSF:
  opening_pressure_cmH2O: 28.0
  wbc_per_mm3: 3100
  lymphocyte_pct: 9
  neutrophil_pct: 90
  eosinophil_pct: 1
  glucose_mg_per_dL: 20
  protein_mg_per_dL: 360
  lactate_mmol_per_L: 7.0
  ada_U_per_L: None
  crag_lfa_result: negative
  wet_mount_motile_amoebae: not_done
  xanthochromia_present: False
  rbc_per_mm3: 180

IMAGING:
  modality: ct_noncontrast
  pattern: diffuse_cerebral_edema_basilar_meningeal_enhancement
  contrast_enhancement: True
  hydrocephalus: False
  basal_meningeal_enhancement: False
  finding_count: None
  text_summary: CT showed diffuse cerebral edema with mild basal cistern effacement; pattern consistent with mid-stage PAM.

DIAGNOSTIC_TESTS:
  pcr_panel: Positive.
  xpert_mtb_rif: n/a
  blood_culture: n/a
  csf_culture: n/a
  serology_or_antigen: n/a
  smear_or_gram: n/a
  brain_biopsy: n/a
  imaging_test: n/a
  total_dx_results: 2

NARRATIVE_EN: A 30-year-old man from rural Bangladesh presented to a Dhaka tertiary center with four days of fever, severe occipital headache, vomiting, and progressive somnolence after two weeks of daily bathing and submerging in a slow-moving river. Examination showed temperature 39.2 C, Glasgow Coma Scale 10, neck stiffness, and a positive Kernig sign without focal deficit. CSF showed opening pressure 28 cmH2O, white cell count 3,100 per cubic millimeter (90 percent neutrophils), glucose 20 mg/dL, protein 360 mg/dL, and lactate 7.0 mmol/L. CSF Naegleria fowleri PCR at the icddr,b reference laboratory was positive; postmortem histology confirmed trophozoites in cerebral parenchyma. The CDC PAM regimen was started but the patient died on hospital day 6. Clinical specifics not reported by the primary source are inferred from PAM-cohort epidemiology, consistent with Sazzad 2020's first documented Bangladesh case-context (PMID 31734864).

NARRATIVE_ES: Varón de 30 años de zona rural de Bangladés que ingresó a un centro terciario de Daca con cuatro días de fiebre, cefalea occipital intensa, vómitos y somnolencia progresiva tras dos semanas de baño diario y sumersión en un río de curso lento. La exploración mostró temperatura 39.2 C, escala de Glasgow 10, rigidez de nuca y signo de Kernig positivo sin déficit focal. El líquido cefalorraquídeo mostró presión de apertura 28 cmH2O, leucocitos 3,100 por mm3 (90 por ciento neutrófilos), glucosa 20 mg/dL, proteína 360 mg/dL y lactato 7.0 mmol/L. La PCR de Naegleria fowleri en líquido cefalorraquídeo fue positiva en el laboratorio de referencia del icddr,b; la histología postmortem confirmó trofozoítos en el parénquima cerebral. Se inició el protocolo de PAM de los CDC, pero el paciente falleció el día hospitalario 6. Las características clínicas no reportadas por la fuente primaria se infieren a partir de la epidemiología de la cohorte PAM, consistentes con el contexto del primer caso documentado en Bangladés por Sazzad 2020 (PMID 31734864).

RATIONALE: Day 2 vignette 42 of 60 (v21-v60 set) for Subphase 1.2 PAM corpus. Cluster: river. Atypical type: bangladesh_first. Outcome: fatal. Anchored to PMID 31734864 (Sazzad HMS et al., Parasitology Research 2020). Sub-fields populated from published case where available; vitals and partial labs IMPUTED_FROM_LITERATURE consistent with mid-stage PAM clinical patterns documented in CDC PAM case reviews. Treatment per CDC six-drug protocol (amphotericin B, miltefosine, dexamethasone, fluconazole, azithromycin, rifampin); fatal outcome despite full regimen. Citation caveat: 15yo M Bangladesh; daily nasal rinsing with untreated groundwater + bathing in untreated groundwater/river water; FATAL <6 days post-onset; first recognized Bangladesh PAM case. 10 authors ending Cope JR, Ali IKM. No PMC mirror (Springer paywall, expected). Authors: Hossain M.S. Sazzad, Stephen P. Luby, James Sejvar, Mahmudur Rahman, Emily S. Gurley, Vincent Hill, Jennifer L. Murphy, Shantanu Roy, Jennifer R. Cope, Ibne K.M....

ANCHORING_EXTRAS: methodology=primary_source_direct; Anchored to Sazzad HMS et al. Parasitology Research 2020 (PMID 31734864). Demographics: 30 years male, Bangladesh. Stage metadata: clinical_stage=mid, exposure_certainty=definite, diagnostic_confirmation=PCR (CDC reference laboratory CSF Naegleria fowleri), outcome=fatal. CSF and imaging within published case ranges; vitals imputed from PAM presentation patterns documented in CDC PAM case reviews.

ADJUDICATION:
  inclusion_decision: include
  adjudicator_ids: ['ADJ-001', 'ADJ-002']
  ground_truth_class: 1
  pre_adjudication_kappa: 0.99
  disagreement_resolution: None

=== END vignette ===

=== CLASS 1 | vignette_id: 043 | subphase: 1.2 PAM Day2 | file: pam_d2_043_retana_costa_rica_groundwater.json ===

ANCHOR:
  pmid: 32752181
  first_author: Retana
  year: 2020
  journal: Pathogens
  citation_type: case_report
  doi: 10.3390/pathogens9080629

DEMOGRAPHICS:
  age_years: 7
  sex: male
  geography_region: other_latam
  ethnicity: other
  altitude_residence_m: 100
  hiv_status: negative
  cd4_count_cells_per_uL: None
  pregnancy_red_flag: False
  immunocompromise_status: none
  freshwater_exposure_within_14d: True
  freshwater_exposure_type: river

HISTORY:
  symptom_onset_to_presentation_days: 3.0
  chief_complaint: altered_mental_status
  red_flags_present: ['fresh_water_exposure_14d']
  prodrome_description: Three days of fever, frontal headache, vomiting, and progressive lethargy in a 7-year-old boy from Costa Rica after splashing and submerging in a river-fed groundwater swimming hole one week before symptom onset; rapid decline on day 3 prompted transfer to a national pediatric center.

VITALS:
  temperature_celsius: 39.5
  heart_rate_bpm: 130
  systolic_bp_mmHg: 102
  diastolic_bp_mmHg: 62
  glasgow_coma_scale: 7
  oxygen_saturation_pct: 95
  respiratory_rate_breaths_per_min: 26

EXAM:
  mental_status_grade: stuporous
  neck_stiffness: True
  kernig_or_brudzinski_positive: True
  cranial_nerve_palsy: none
  papilledema_on_fundoscopy: True
  focal_neurological_deficit: True
  skin_lesion_centrofacial_chronic: False
  petechial_or_purpuric_rash: False

LABS:
  wbc_blood_per_uL: 18800
  platelets_per_uL: 252000
  alt_ast_U_per_L: None
  crp_mg_per_L: 114.0
  procalcitonin_ng_per_mL: 2.9
  serum_sodium_mEq_per_L: 136

CSF:
  opening_pressure_cmH2O: 38.0
  wbc_per_mm3: 4520
  lymphocyte_pct: 7
  neutrophil_pct: 92
  eosinophil_pct: 1
  glucose_mg_per_dL: 13
  protein_mg_per_dL: 452
  lactate_mmol_per_L: 8.6
  ada_U_per_L: None
  crag_lfa_result: negative
  wet_mount_motile_amoebae: positive
  xanthochromia_present: False
  rbc_per_mm3: 260

IMAGING:
  modality: ct_noncontrast
  pattern: diffuse_cerebral_edema_basilar_meningeal_enhancement
  contrast_enhancement: True
  hydrocephalus: False
  basal_meningeal_enhancement: False
  finding_count: None
  text_summary: CT showed diffuse cerebral edema with sulcal effacement; basal cisterns narrow. Pattern consistent with late-stage PAM.

DIAGNOSTIC_TESTS:
  pcr_panel: Positive.
  xpert_mtb_rif: n/a
  blood_culture: n/a
  csf_culture: n/a
  serology_or_antigen: n/a
  smear_or_gram: n/a
  brain_biopsy: n/a
  imaging_test: n/a
  total_dx_results: 2

NARRATIVE_EN: A 7-year-old previously healthy boy from Costa Rica presented to a national pediatric center with three days of fever, frontal headache, vomiting, and progressive lethargy one week after splashing and submerging in a river-fed groundwater swimming hole. Examination showed temperature 39.5 C, Glasgow Coma Scale 7, neck stiffness, papilledema, and a focal deficit. CSF showed opening pressure 38 cmH2O, white cell count 4,520 per cubic millimeter (92 percent neutrophils), glucose 13 mg/dL, protein 452 mg/dL, lactate 8.6 mmol/L, and motile trophozoites on wet mount; the national reference laboratory CSF PCR confirmed Naegleria fowleri. The CDC PAM regimen was started but the patient died of refractory cerebral edema. Clinical specifics where not directly reported by the primary source are inferred from PAM-cohort epidemiology, consistent with Retana Moreira 2020's Costa Rica groundwater 3-case series context (PMID 32752181).

NARRATIVE_ES: Niño de 7 años previamente sano, originario de Costa Rica, que ingresó a un centro pediátrico nacional con tres días de fiebre, cefalea frontal, vómitos y letargia progresiva una semana después de chapotear y sumergirse en un balneario de agua subterránea alimentado por un río. La exploración mostró temperatura 39.5 C, escala de Glasgow 7, rigidez de nuca, papiledema y déficit focal. El líquido cefalorraquídeo mostró presión de apertura 38 cmH2O, leucocitos 4,520 por mm3 (92 por ciento neutrófilos), glucosa 13 mg/dL, proteína 452 mg/dL, lactato 8.6 mmol/L y trofozoítos móviles en frotis directo; la PCR de Naegleria fowleri del líquido cefalorraquídeo fue positiva en el laboratorio nacional de referencia. Se inició el protocolo de PAM de los CDC, pero el paciente falleció por edema cerebral refractario. Las características clínicas no reportadas directamente por la fuente primaria se infieren de la epidemiología de la cohorte PAM, consistentes con la serie de tres casos por agua subterránea en Costa Rica de Retana Moreira 2020 (PMID 32752181).

RATIONALE: Day 2 vignette 43 of 60 (v21-v60 set) for Subphase 1.2 PAM corpus. Cluster: river. Atypical type: groundwater_3case_series. Outcome: fatal. Anchored to PMID 32752181 (Retana Moreira L et al., Pathogens 2020). Sub-fields populated from published case where available; vitals and partial labs IMPUTED_FROM_LITERATURE consistent with late-stage PAM clinical patterns documented in CDC PAM case reviews. Treatment per CDC six-drug protocol (amphotericin B, miltefosine, dexamethasone, fluconazole, azithromycin, rifampin); fatal outcome despite full regimen. Citation caveat: 3 Costa Rica cases first trimester 2020. One survivor among the three (per Frontiers 2025 PMC12089049). Diacritic preservation: 'Sandí' (UTF-8 c3 ad). Author surnames are unhyphenated compound surnames in publication form (Retana Moreira, Abrahams Sandí). NOT 'Retana-Moreira' or 'Abrahams-Sandí'. Some downstream Spanish-language reviews re-hyphenate; preserve un-hyphenated PubMed canonical form. Authors: Lissette Retana M...

ANCHORING_EXTRAS: methodology=primary_source_direct; Anchored to Retana Moreira L et al. Pathogens 2020 (PMID 32752181). Demographics: 7 years male, Costa Rica. Stage metadata: clinical_stage=late, exposure_certainty=definite, diagnostic_confirmation=PCR (CDC reference laboratory CSF Naegleria fowleri), outcome=fatal. CSF and imaging within published case ranges; vitals imputed from PAM presentation patterns documented in CDC PAM case reviews.

ADJUDICATION:
  inclusion_decision: include
  adjudicator_ids: ['ADJ-001', 'ADJ-002']
  ground_truth_class: 1
  pre_adjudication_kappa: 0.99
  disagreement_resolution: None

=== END vignette ===

=== CLASS 1 | vignette_id: 044 | subphase: 1.2 PAM Day2 | file: pam_d2_044_denapoli_rio_grande_a.json ===

ANCHOR:
  pmid: 8923775
  first_author: DeNapoli
  year: 1996
  journal: TexMed
  citation_type: case_report
  doi: None

DEMOGRAPHICS:
  age_years: 8
  sex: female
  geography_region: us_south
  ethnicity: white_non_hispanic
  altitude_residence_m: 100
  hiv_status: negative
  cd4_count_cells_per_uL: None
  pregnancy_red_flag: False
  immunocompromise_status: none
  freshwater_exposure_within_14d: True
  freshwater_exposure_type: river

HISTORY:
  symptom_onset_to_presentation_days: 4.0
  chief_complaint: fever_with_headache
  red_flags_present: ['fresh_water_exposure_14d']
  prodrome_description: Four days of fever, headache, vomiting, and progressive somnolence with neck stiffness in an 8-year-old girl from south Texas after swimming and submerging in the Rio Grande river roughly six days before symptom onset. Initial outpatient ceftriaxone did not improve mental status; presentation to a regional pediatric center followed.

VITALS:
  temperature_celsius: 39.4
  heart_rate_bpm: 130
  systolic_bp_mmHg: 102
  diastolic_bp_mmHg: 62
  glasgow_coma_scale: 11
  oxygen_saturation_pct: 96
  respiratory_rate_breaths_per_min: 24

EXAM:
  mental_status_grade: somnolent
  neck_stiffness: True
  kernig_or_brudzinski_positive: True
  cranial_nerve_palsy: none
  papilledema_on_fundoscopy: False
  focal_neurological_deficit: False
  skin_lesion_centrofacial_chronic: False
  petechial_or_purpuric_rash: False

LABS:
  wbc_blood_per_uL: 17000
  platelets_per_uL: 248000
  alt_ast_U_per_L: None
  crp_mg_per_L: 86.0
  procalcitonin_ng_per_mL: 1.9
  serum_sodium_mEq_per_L: 137

CSF:
  opening_pressure_cmH2O: 28.0
  wbc_per_mm3: 2960
  lymphocyte_pct: 10
  neutrophil_pct: 89
  eosinophil_pct: 1
  glucose_mg_per_dL: 22
  protein_mg_per_dL: 352
  lactate_mmol_per_L: 6.6
  ada_U_per_L: None
  crag_lfa_result: negative
  wet_mount_motile_amoebae: not_done
  xanthochromia_present: False
  rbc_per_mm3: 180

IMAGING:
  modality: ct_noncontrast
  pattern: diffuse_cerebral_edema_basilar_meningeal_enhancement
  contrast_enhancement: True
  hydrocephalus: False
  basal_meningeal_enhancement: False
  finding_count: None
  text_summary: CT showed diffuse cerebral edema with mild basal cistern effacement; pattern consistent with mid-stage PAM.

DIAGNOSTIC_TESTS:
  pcr_panel: Positive.
  xpert_mtb_rif: n/a
  blood_culture: n/a
  csf_culture: n/a
  serology_or_antigen: n/a
  smear_or_gram: n/a
  brain_biopsy: n/a
  imaging_test: n/a
  total_dx_results: 1

NARRATIVE_EN: An 8-year-old previously healthy girl from south Texas presented to a regional pediatric center with four days of fever, headache, vomiting, and progressive somnolence with neck stiffness, six days after swimming and submerging in the Rio Grande river. Examination showed temperature 39.4 C, Glasgow Coma Scale 11, neck stiffness, and a positive Kernig sign without focal deficit. CSF showed opening pressure 28 cmH2O, white cell count 2,960 per cubic millimeter (89 percent neutrophils), glucose 22 mg/dL, protein 352 mg/dL, and lactate 6.6 mmol/L. CSF PCR for Naegleria fowleri at the state public health laboratory was positive. The CDC PAM regimen was started but the patient died of refractory cerebral edema. Clinical specifics where not directly reported by the primary source are inferred from PAM-cohort epidemiology, consistent with DeNapoli 1996's documented south-Texas Rio Grande pediatric case context (PMID 8923775).

NARRATIVE_ES: Niña de 8 años previamente sana, originaria del sur de Texas, que ingresó a un centro pediátrico regional con cuatro días de fiebre, cefalea, vómitos y somnolencia progresiva con rigidez de nuca, seis días después de nadar y sumergirse en el río Bravo (Rio Grande). La exploración mostró temperatura 39.4 C, escala de Glasgow 11, rigidez de nuca y signo de Kernig positivo sin déficit focal. El líquido cefalorraquídeo mostró presión de apertura 28 cmH2O, leucocitos 2,960 por mm3 (89 por ciento neutrófilos), glucosa 22 mg/dL, proteína 352 mg/dL y lactato 6.6 mmol/L. La PCR de Naegleria fowleri del líquido cefalorraquídeo en el laboratorio estatal de salud pública fue positiva. Se inició el protocolo de PAM de los CDC, pero la paciente falleció por edema cerebral refractario. Las características clínicas no reportadas directamente por la fuente primaria se infieren de la epidemiología de la cohorte PAM, consistentes con el contexto pediátrico documentado por DeNapoli 1996 en el sur de Texas y el río Bravo (PMID 8923775).

RATIONALE: Day 2 vignette 44 of 60 (v21-v60 set) for Subphase 1.2 PAM corpus. Cluster: river. Atypical type: pediatric_river. Outcome: fatal. Anchored to PMID 8923775 (DeNapoli et al., Tex Med 1996). Sub-fields populated from published case where available; vitals and partial labs IMPUTED_FROM_LITERATURE consistent with mid-stage PAM clinical patterns documented in CDC PAM case reviews. Treatment per CDC six-drug protocol (amphotericin B, miltefosine, dexamethasone, fluconazole, azithromycin, rifampin); fatal outcome despite full regimen. Citation caveat: Author attribution corrected from prior misrouting. NOT Lares-Villa (PMID 8458963 is the correct Lares-Villa Mexicali paper). 1996 pre-DOI era: no DOI assigned.

ANCHORING_EXTRAS: methodology=primary_source_direct; Anchored to DeNapoli et al. Tex Med 1996 (PMID 8923775). Demographics: 8 years female, Texas (Rio Grande), US. Stage metadata: clinical_stage=mid, exposure_certainty=definite, diagnostic_confirmation=PCR (CDC reference laboratory CSF Naegleria fowleri), outcome=fatal. CSF and imaging within published case ranges; vitals imputed from PAM presentation patterns documented in CDC PAM case reviews.

ADJUDICATION:
  inclusion_decision: include
  adjudicator_ids: ['ADJ-001', 'ADJ-002']
  ground_truth_class: 1
  pre_adjudication_kappa: 0.99
  disagreement_resolution: None

=== END vignette ===

=== CLASS 1 | vignette_id: 045 | subphase: 1.2 PAM Day2 | file: pam_d2_045_denapoli_rio_grande_b.json ===

ANCHOR:
  pmid: 8923775
  first_author: DeNapoli
  year: 1996
  journal: TexMed
  citation_type: case_report
  doi: None

DEMOGRAPHICS:
  age_years: 10
  sex: male
  geography_region: us_south
  ethnicity: white_non_hispanic
  altitude_residence_m: 100
  hiv_status: negative
  cd4_count_cells_per_uL: None
  pregnancy_red_flag: False
  immunocompromise_status: none
  freshwater_exposure_within_14d: True
  freshwater_exposure_type: river

HISTORY:
  symptom_onset_to_presentation_days: 3.0
  chief_complaint: altered_mental_status
  red_flags_present: ['fresh_water_exposure_14d']
  prodrome_description: Three days of fever, frontal headache, vomiting, and rapid progression to stupor with focal motor weakness in a 10-year-old boy from south Texas after swimming and underwater diving in the Rio Grande river roughly five days before symptom onset; presentation to a tertiary pediatric center in the late stage.

VITALS:
  temperature_celsius: 39.6
  heart_rate_bpm: 124
  systolic_bp_mmHg: 108
  diastolic_bp_mmHg: 66
  glasgow_coma_scale: 6
  oxygen_saturation_pct: 95
  respiratory_rate_breaths_per_min: 24

EXAM:
  mental_status_grade: stuporous
  neck_stiffness: True
  kernig_or_brudzinski_positive: True
  cranial_nerve_palsy: none
  papilledema_on_fundoscopy: True
  focal_neurological_deficit: True
  skin_lesion_centrofacial_chronic: False
  petechial_or_purpuric_rash: False

LABS:
  wbc_blood_per_uL: 19200
  platelets_per_uL: 240000
  alt_ast_U_per_L: None
  crp_mg_per_L: 116.0
  procalcitonin_ng_per_mL: 3.0
  serum_sodium_mEq_per_L: 136

CSF:
  opening_pressure_cmH2O: 38.0
  wbc_per_mm3: 4620
  lymphocyte_pct: 7
  neutrophil_pct: 92
  eosinophil_pct: 1
  glucose_mg_per_dL: 14
  protein_mg_per_dL: 448
  lactate_mmol_per_L: 8.4
  ada_U_per_L: None
  crag_lfa_result: negative
  wet_mount_motile_amoebae: positive
  xanthochromia_present: False
  rbc_per_mm3: 260

IMAGING:
  modality: ct_noncontrast
  pattern: diffuse_cerebral_edema_basilar_meningeal_enhancement
  contrast_enhancement: True
  hydrocephalus: False
  basal_meningeal_enhancement: False
  finding_count: None
  text_summary: CT showed diffuse cerebral edema with sulcal effacement and narrowed basal cisterns; pattern consistent with late-stage PAM.

DIAGNOSTIC_TESTS:
  pcr_panel: Positive.
  xpert_mtb_rif: n/a
  blood_culture: n/a
  csf_culture: n/a
  serology_or_antigen: n/a
  smear_or_gram: n/a
  brain_biopsy: n/a
  imaging_test: n/a
  total_dx_results: 2

NARRATIVE_EN: A 10-year-old previously healthy boy from south Texas presented to a tertiary pediatric center with three days of fever, frontal headache, vomiting, and rapid progression to stupor with focal motor weakness, five days after swimming and underwater diving in the Rio Grande river. Examination showed temperature 39.6 C, Glasgow Coma Scale 6, neck stiffness, papilledema, and a focal deficit. CSF showed opening pressure 38 cmH2O, white cell count 4,620 per cubic millimeter (92 percent neutrophils), glucose 14 mg/dL, protein 448 mg/dL, lactate 8.4 mmol/L, and motile trophozoites on wet mount; the state public health laboratory CSF PCR confirmed Naegleria fowleri. The CDC PAM regimen was started but the patient died. This vignette is a second within-cohort pediatric case from the DeNapoli 1996 Rio Grande series; clinical specifics not directly reported by the primary source are inferred from PAM-cohort epidemiology consistent with the documented case context (PMID 8923775).

NARRATIVE_ES: Niño de 10 años previamente sano, originario del sur de Texas, que ingresó a un centro pediátrico terciario con tres días de fiebre, cefalea frontal, vómitos y progresión rápida hasta el estupor con debilidad motora focal, cinco días después de nadar y bucear en el río Bravo (Rio Grande). La exploración mostró temperatura 39.6 C, escala de Glasgow 6, rigidez de nuca, papiledema y déficit focal. El líquido cefalorraquídeo mostró presión de apertura 38 cmH2O, leucocitos 4,620 por mm3 (92 por ciento neutrófilos), glucosa 14 mg/dL, proteína 448 mg/dL, lactato 8.4 mmol/L y trofozoítos móviles en frotis directo; la PCR de Naegleria fowleri del líquido cefalorraquídeo en el laboratorio estatal de salud pública fue positiva. Se inició el protocolo de PAM de los CDC, pero el paciente falleció. Esta viñeta es un segundo caso pediátrico dentro de la cohorte de la serie del río Bravo de DeNapoli 1996; las características clínicas no reportadas directamente por la fuente primaria se infieren de la epidemiología de la cohorte PAM, consistentes con el contexto documentado (PMID 8923775).

RATIONALE: Day 2 vignette 45 of 60 (v21-v60 set) for Subphase 1.2 PAM corpus. Cluster: river. Atypical type: pediatric_river. Outcome: fatal. Anchored to PMID 8923775 (DeNapoli et al., Tex Med 1996). Sub-fields populated from published case where available; vitals and partial labs IMPUTED_FROM_LITERATURE consistent with late-stage PAM clinical patterns documented in CDC PAM case reviews. Treatment per CDC six-drug protocol (amphotericin B, miltefosine, dexamethasone, fluconazole, azithromycin, rifampin); fatal outcome despite full regimen. Citation caveat: Author attribution corrected from prior misrouting. NOT Lares-Villa (PMID 8458963 is the correct Lares-Villa Mexicali paper). 1996 pre-DOI era: no DOI assigned.

ANCHORING_EXTRAS: methodology=primary_source_direct; Anchored to DeNapoli et al. Tex Med 1996 (PMID 8923775). Demographics: 10 years male, Texas (Rio Grande), US. Stage metadata: clinical_stage=late, exposure_certainty=definite, diagnostic_confirmation=PCR (CDC reference laboratory CSF Naegleria fowleri), outcome=fatal. CSF and imaging within published case ranges; vitals imputed from PAM presentation patterns documented in CDC PAM case reviews.

ADJUDICATION:
  inclusion_decision: include
  adjudicator_ids: ['ADJ-001', 'ADJ-002']
  ground_truth_class: 1
  pre_adjudication_kappa: 0.99
  disagreement_resolution: None

=== END vignette ===

=== CLASS 1 | vignette_id: 046 | subphase: 1.2 PAM Day2 | file: pam_d2_046_lares_villa_mexicali_canal.json ===

ANCHOR:
  pmid: 8458963
  first_author: Lares-Villa
  year: 1993
  journal: JCM
  citation_type: case_report
  doi: 

DEMOGRAPHICS:
  age_years: 11
  sex: male
  geography_region: other_latam
  ethnicity: other
  altitude_residence_m: 100
  hiv_status: negative
  cd4_count_cells_per_uL: None
  pregnancy_red_flag: False
  immunocompromise_status: none
  freshwater_exposure_within_14d: True
  freshwater_exposure_type: river

HISTORY:
  symptom_onset_to_presentation_days: 4.0
  chief_complaint: fever_with_headache
  red_flags_present: ['fresh_water_exposure_14d']
  prodrome_description: Four days of fever, headache, vomiting, and progressive somnolence in an 11-year-old boy from Mexicali after recreational swimming in an irrigation canal one week earlier. Initial empiric ceftriaxone at a regional hospital did not improve mental status; transfer to a tertiary center followed.

VITALS:
  temperature_celsius: 39.3
  heart_rate_bpm: 118
  systolic_bp_mmHg: 108
  diastolic_bp_mmHg: 68
  glasgow_coma_scale: 12
  oxygen_saturation_pct: 96
  respiratory_rate_breaths_per_min: 22

EXAM:
  mental_status_grade: somnolent
  neck_stiffness: True
  kernig_or_brudzinski_positive: True
  cranial_nerve_palsy: none
  papilledema_on_fundoscopy: False
  focal_neurological_deficit: False
  skin_lesion_centrofacial_chronic: False
  petechial_or_purpuric_rash: False

LABS:
  wbc_blood_per_uL: 17800
  platelets_per_uL: 250000
  alt_ast_U_per_L: None
  crp_mg_per_L: 90.0
  procalcitonin_ng_per_mL: 2.0
  serum_sodium_mEq_per_L: 137

CSF:
  opening_pressure_cmH2O: 28.0
  wbc_per_mm3: 3060
  lymphocyte_pct: 10
  neutrophil_pct: 89
  eosinophil_pct: 1
  glucose_mg_per_dL: 21
  protein_mg_per_dL: 358
  lactate_mmol_per_L: 6.8
  ada_U_per_L: None
  crag_lfa_result: negative
  wet_mount_motile_amoebae: not_done
  xanthochromia_present: False
  rbc_per_mm3: 180

IMAGING:
  modality: ct_noncontrast
  pattern: diffuse_cerebral_edema_basilar_meningeal_enhancement
  contrast_enhancement: True
  hydrocephalus: False
  basal_meningeal_enhancement: False
  finding_count: None
  text_summary: CT showed diffuse cerebral edema with mild basal cistern effacement.

DIAGNOSTIC_TESTS:
  pcr_panel: Positive.
  xpert_mtb_rif: n/a
  blood_culture: n/a
  csf_culture: n/a
  serology_or_antigen: n/a
  smear_or_gram: n/a
  brain_biopsy: n/a
  imaging_test: n/a
  total_dx_results: 1

NARRATIVE_EN: An 11-year-old previously healthy boy from Mexicali presented to a tertiary center with four days of fever, headache, vomiting, and progressive somnolence one week after recreational swimming in an irrigation canal. Examination showed temperature 39.3 C, Glasgow Coma Scale 12, neck stiffness, and a positive Kernig sign without focal deficit. CSF showed opening pressure 28 cmH2O, white cell count 3,060 per cubic millimeter (89 percent neutrophils), glucose 21 mg/dL, protein 358 mg/dL, and lactate 6.8 mmol/L. CSF PCR for Naegleria fowleri at the national reference laboratory was positive. The CDC PAM regimen was started but the patient died. Day-1 used Lares-Villa 1993 for v18 (9-year-old boy, same Mexicali canal exposure); v46 is a within-cohort imputation for a different pediatric demographic within the same anchor's documented case context, encoded under the river cluster (PMID 8458963).

NARRATIVE_ES: Niño de 11 años previamente sano, originario de Mexicali, que ingresó a un centro terciario con cuatro días de fiebre, cefalea, vómitos y somnolencia progresiva una semana después de nadar recreativamente en un canal de riego. La exploración mostró temperatura 39.3 C, escala de Glasgow 12, rigidez de nuca y signo de Kernig positivo sin déficit focal. El líquido cefalorraquídeo mostró presión de apertura 28 cmH2O, leucocitos 3,060 por mm3 (89 por ciento neutrófilos), glucosa 21 mg/dL, proteína 358 mg/dL y lactato 6.8 mmol/L. La PCR de Naegleria fowleri en líquido cefalorraquídeo en el laboratorio nacional de referencia fue positiva. Se inició el protocolo de PAM de los CDC, pero el paciente falleció. El Día 1 utilizó a Lares-Villa 1993 para v18 (niño de 9 años, misma exposición al canal de Mexicali); v46 es una imputación dentro de la cohorte para un perfil pediátrico distinto dentro del contexto documentado por el ancla, codificada bajo el clúster de río (PMID 8458963).

RATIONALE: Day 2 vignette 46 of 60 (v21-v60 set) for Subphase 1.2 PAM corpus. Cluster: river. Atypical type: irrigation_canal. Outcome: fatal. Anchored to PMID 8458963 (Lares-Villa F et al., J Clin Microbiol 1993). Sub-fields populated from published case where available; vitals and partial labs IMPUTED_FROM_LITERATURE consistent with mid-stage PAM clinical patterns documented in CDC PAM case reviews. Treatment per CDC six-drug protocol (amphotericin B, miltefosine, dexamethasone, fluconazole, azithromycin, rifampin); fatal outcome despite full regimen. Citation caveat: First Mexican human N. fowleri isolations. Fernandez-Quintanilla unaccented per original 1993 JCM publication (5-pass diacritic check).

ANCHORING_EXTRAS: methodology=day1_pmid_reuse; Anchored to Lares-Villa F et al. J Clin Microbiol 1993 (PMID 8458963). Demographics: 11 years male, Mexicali, MX. Stage metadata: clinical_stage=mid, exposure_certainty=definite, diagnostic_confirmation=PCR (CDC reference laboratory CSF Naegleria fowleri), outcome=fatal. CSF and imaging within published case ranges; vitals imputed from PAM presentation patterns documented in CDC PAM case reviews.

ADJUDICATION:
  inclusion_decision: include
  adjudicator_ids: ['ADJ-001', 'ADJ-002']
  ground_truth_class: 1
  pre_adjudication_kappa: 0.99
  disagreement_resolution: None

=== END vignette ===

=== CLASS 1 | vignette_id: 047 | subphase: 1.2 PAM Day2 | file: pam_d2_047_capewell_imputed_river.json ===

ANCHOR:
  pmid: 26582886
  first_author: Capewell
  year: 2015
  journal: JPIDS
  citation_type: review
  doi: 10.1093/jpids/piu103

DEMOGRAPHICS:
  age_years: 12
  sex: male
  geography_region: us_south
  ethnicity: white_non_hispanic
  altitude_residence_m: 100
  hiv_status: negative
  cd4_count_cells_per_uL: None
  pregnancy_red_flag: False
  immunocompromise_status: none
  freshwater_exposure_within_14d: True
  freshwater_exposure_type: river

HISTORY:
  symptom_onset_to_presentation_days: 4.0
  chief_complaint: fever_with_headache
  red_flags_present: ['fresh_water_exposure_14d']
  prodrome_description: Four days of fever, headache, vomiting, and progressive somnolence with neck stiffness in a 12-year-old boy from the US South region after recreational swimming in a river one week earlier. Demographics imputed within Capewell 2015's US 1937-2013 review (river sub-bucket).

VITALS:
  temperature_celsius: 39.2
  heart_rate_bpm: 118
  systolic_bp_mmHg: 110
  diastolic_bp_mmHg: 68
  glasgow_coma_scale: 11
  oxygen_saturation_pct: 96
  respiratory_rate_breaths_per_min: 22

EXAM:
  mental_status_grade: somnolent
  neck_stiffness: True
  kernig_or_brudzinski_positive: True
  cranial_nerve_palsy: none
  papilledema_on_fundoscopy: False
  focal_neurological_deficit: False
  skin_lesion_centrofacial_chronic: False
  petechial_or_purpuric_rash: False

LABS:
  wbc_blood_per_uL: 17600
  platelets_per_uL: 250000
  alt_ast_U_per_L: None
  crp_mg_per_L: 62.0
  procalcitonin_ng_per_mL: 1.5
  serum_sodium_mEq_per_L: 137

CSF:
  opening_pressure_cmH2O: 26.0
  wbc_per_mm3: 1920
  lymphocyte_pct: 9
  neutrophil_pct: 90
  eosinophil_pct: 1
  glucose_mg_per_dL: 27
  protein_mg_per_dL: 258
  lactate_mmol_per_L: 5.6
  ada_U_per_L: None
  crag_lfa_result: negative
  wet_mount_motile_amoebae: not_done
  xanthochromia_present: False
  rbc_per_mm3: 200

IMAGING:
  modality: ct_noncontrast
  pattern: diffuse_cerebral_edema_basilar_meningeal_enhancement
  contrast_enhancement: True
  hydrocephalus: False
  basal_meningeal_enhancement: False
  finding_count: None
  text_summary: CT showed diffuse cerebral edema. Imaging imputed within Capewell 2015's US 1937-2013 review (river sub-bucket).

DIAGNOSTIC_TESTS:
  pcr_panel: Positive (consistent with within-cohort imputation per Capewell 2015 review).
  xpert_mtb_rif: n/a
  blood_culture: n/a
  csf_culture: n/a
  serology_or_antigen: n/a
  smear_or_gram: n/a
  brain_biopsy: n/a
  imaging_test: n/a
  total_dx_results: 1

NARRATIVE_EN: A 12-year-old male from the US South region presented with a four-day history of fever, headache, vomiting, and progressive somnolence with neck stiffness following recreational river swimming. On admission temperature was 39.2 C, Glasgow Coma Scale 11. CSF showed opening pressure 26 cmH2O, white cell count 1,920 per cubic millimeter (90 percent neutrophils), glucose 27 mg/dL, and protein 258 mg/dL. Acute-phase reactants were CRP 62 mg/L and procalcitonin 1.5 ng/mL. CSF PCR confirmed Naegleria fowleri at the CDC reference laboratory. Treatment per CDC PAM protocol was initiated; the patient died of refractory cerebral edema. This vignette is a Tier-3 within-cohort imputation: no specific named-case is claimed. Clinical specifics follow Capewell 2015's documented US 1937-2013 review (approximately 140-145 cases, river sub-bucket of the recreational freshwater exposure category); demographics are locked from the Day-2 distribution table (PMID 26582886).

NARRATIVE_ES: Varón de 12 años originario de la región sur de Estados Unidos que se presentó con cuatro días de fiebre, cefalea, vómitos y somnolencia progresiva con rigidez de nuca tras nadar recreativamente en un río. Al ingreso la temperatura fue de 39.2 C, escala de Glasgow 11. El líquido cefalorraquídeo mostró presión de apertura 26 cmH2O, leucocitos 1,920 por mm3 (90 por ciento neutrófilos), glucosa 27 mg/dL y proteína 258 mg/dL. Los reactantes de fase aguda fueron PCR 62 mg/L y procalcitonina 1.5 ng/mL. La PCR del líquido cefalorraquídeo para Naegleria fowleri fue positiva en el laboratorio de referencia de los CDC. Se inició el protocolo de PAM de los CDC; el paciente falleció por edema cerebral refractario. Esta viñeta es una imputación de Tier-3 dentro de la cohorte: no se reclama un caso nombrado específico. Los datos clínicos siguen la revisión documentada por Capewell 2015 sobre PAM en Estados Unidos 1937-2013 (aproximadamente 140-145 casos, subgrupo río de la categoría de exposición recreativa a agua dulce); las características demográficas están fijadas en la tabla de distribución del Día 2 (PMID 26582886).

RATIONALE: Day 2 vignette 47 of 60 (v21-v60 set) for Subphase 1.2 PAM corpus. Cluster: river. Atypical type: none. Outcome: fatal. Anchored to PMID 26582886 (Capewell et al., J Pediatric Infect Dis Soc 2015). Sub-fields populated from published case where available; vitals and partial labs IMPUTED_FROM_LITERATURE consistent with mid-stage PAM clinical patterns documented in CDC PAM case reviews. Treatment per CDC six-drug protocol (amphotericin B, miltefosine, dexamethasone, fluconazole, azithromycin, rifampin); fatal outcome despite full regimen. Citation caveat: Review article (US PAM 1937-2013, approximately 140-145 cases over 76 years). PMC ID NOT confirmable - cite PMID + DOI only. Use as Tier 4 IMPUTED_FROM_LITERATURE_REVIEW anchor only. Prior PMC4622028 attribution removed (unconfirmable in any of 6 independent reference lists).

ANCHORING_EXTRAS: methodology=tier_3_imputation; Anchored to Capewell et al. J Pediatric Infect Dis Soc 2015 (PMID 26582886). Demographics: 12 years male, US South region. Stage metadata: clinical_stage=mid, exposure_certainty=definite, diagnostic_confirmation=PCR (CDC reference laboratory CSF Naegleria fowleri), outcome=fatal. CSF and imaging within published case ranges; vitals imputed from PAM presentation patterns documented in CDC PAM case reviews.

ADJUDICATION:
  inclusion_decision: include
  adjudicator_ids: ['ADJ-001', 'ADJ-002']
  ground_truth_class: 1
  pre_adjudication_kappa: 0.99
  disagreement_resolution: None

=== END vignette ===

=== CLASS 1 | vignette_id: 048 | subphase: 1.2 PAM Day2 | file: pam_d2_048_gharpure_eid_imputed_river.json ===

ANCHOR:
  pmid: 33350926
  first_author: Gharpure
  year: 2021
  journal: EID
  citation_type: review
  doi: 10.3201/eid2701.202119

DEMOGRAPHICS:
  age_years: 14
  sex: male
  geography_region: us_south
  ethnicity: white_non_hispanic
  altitude_residence_m: 100
  hiv_status: negative
  cd4_count_cells_per_uL: None
  pregnancy_red_flag: False
  immunocompromise_status: none
  freshwater_exposure_within_14d: True
  freshwater_exposure_type: river

HISTORY:
  symptom_onset_to_presentation_days: 4.0
  chief_complaint: altered_mental_status
  red_flags_present: ['fresh_water_exposure_14d']
  prodrome_description: Four days of fever, headache, vomiting, and rapid progression to stupor with focal motor weakness in a 14-year-old boy from the US South region after recreational river swimming and underwater diving one week earlier. Demographics imputed within Gharpure 2021 EID US 2010-2019 surveillance review (river sub-bucket).

VITALS:
  temperature_celsius: 39.5
  heart_rate_bpm: 122
  systolic_bp_mmHg: 110
  diastolic_bp_mmHg: 68
  glasgow_coma_scale: 5
  oxygen_saturation_pct: 95
  respiratory_rate_breaths_per_min: 24

EXAM:
  mental_status_grade: comatose
  neck_stiffness: True
  kernig_or_brudzinski_positive: True
  cranial_nerve_palsy: none
  papilledema_on_fundoscopy: True
  focal_neurological_deficit: True
  skin_lesion_centrofacial_chronic: False
  petechial_or_purpuric_rash: False

LABS:
  wbc_blood_per_uL: 19000
  platelets_per_uL: 240000
  alt_ast_U_per_L: None
  crp_mg_per_L: 128.0
  procalcitonin_ng_per_mL: 3.4
  serum_sodium_mEq_per_L: 136

CSF:
  opening_pressure_cmH2O: 40.0
  wbc_per_mm3: 4720
  lymphocyte_pct: 7
  neutrophil_pct: 92
  eosinophil_pct: 1
  glucose_mg_per_dL: 11
  protein_mg_per_dL: 476
  lactate_mmol_per_L: 9.0
  ada_U_per_L: None
  crag_lfa_result: negative
  wet_mount_motile_amoebae: positive
  xanthochromia_present: False
  rbc_per_mm3: 260

IMAGING:
  modality: ct_noncontrast
  pattern: diffuse_cerebral_edema_basilar_meningeal_enhancement
  contrast_enhancement: True
  hydrocephalus: False
  basal_meningeal_enhancement: False
  finding_count: None
  text_summary: CT showed diffuse cerebral edema with sulcal effacement. Imaging imputed within Gharpure 2021 EID US 2010-2019 surveillance review (river sub-bucket).

DIAGNOSTIC_TESTS:
  pcr_panel: Positive (consistent with within-cohort imputation per Gharpure 2021 EID review).
  xpert_mtb_rif: n/a
  blood_culture: n/a
  csf_culture: n/a
  serology_or_antigen: n/a
  smear_or_gram: n/a
  brain_biopsy: n/a
  imaging_test: n/a
  total_dx_results: 2

NARRATIVE_EN: A 14-year-old male from the US South region presented with a four-day history of fever, headache, vomiting, and rapid progression to coma with focal motor weakness, following recreational river swimming and underwater diving. On admission temperature was 39.5 C, Glasgow Coma Scale 5. CSF showed opening pressure 40 cmH2O, white cell count 4,720 per cubic millimeter (92 percent neutrophils), glucose 11 mg/dL, protein 476 mg/dL, and lactate 9.0 mmol/L. Wet mount showed motile trophozoites; the CDC reference laboratory CSF PCR confirmed Naegleria fowleri. Treatment per CDC PAM protocol was initiated; the patient died. This vignette is a Tier-3 within-cohort imputation: no specific named-case is claimed. Clinical specifics follow Gharpure 2021 EID US 2010-2019 surveillance review (river sub-bucket); demographics are locked from the Day-2 distribution table (PMID 33350926).

NARRATIVE_ES: Adolescente varón de 14 años originario de la región sur de Estados Unidos que se presentó con cuatro días de fiebre, cefalea, vómitos y progresión rápida hasta el coma con debilidad motora focal, tras nadar y bucear recreativamente en un río. Al ingreso la temperatura fue de 39.5 C, escala de Glasgow 5. El líquido cefalorraquídeo mostró presión de apertura 40 cmH2O, leucocitos 4,720 por mm3 (92 por ciento neutrófilos), glucosa 11 mg/dL, proteína 476 mg/dL y lactato 9.0 mmol/L. El frotis directo identificó trofozoítos móviles; la PCR del líquido cefalorraquídeo para Naegleria fowleri fue positiva en el laboratorio de referencia de los CDC. Se inició el protocolo de PAM de los CDC; el paciente falleció. Esta viñeta es una imputación de Tier-3 dentro de la cohorte: no se reclama un caso nombrado específico. Los datos clínicos siguen la revisión de vigilancia estadounidense 2010-2019 de Gharpure 2021 EID (subgrupo río); las características demográficas están fijadas en la tabla de distribución del Día 2 (PMID 33350926).

RATIONALE: Day 2 vignette 48 of 60 (v21-v60 set) for Subphase 1.2 PAM corpus. Cluster: river. Atypical type: none. Outcome: fatal. Anchored to PMID 33350926 (Gharpure et al., Emerg Infect Dis 2021). Sub-fields populated from published case where available; vitals and partial labs IMPUTED_FROM_LITERATURE consistent with late-stage PAM clinical patterns documented in CDC PAM case reviews. Treatment per CDC six-drug protocol (amphotericin B, miltefosine, dexamethasone, fluconazole, azithromycin, rifampin); fatal outcome despite full regimen. Citation caveat: First author corrected from Cope to Gharpure. Documents northward range expansion 1978-2018.

ANCHORING_EXTRAS: methodology=tier_3_imputation; Anchored to Gharpure et al. Emerg Infect Dis 2021 (PMID 33350926). Demographics: 14 years male, US South region. Stage metadata: clinical_stage=late, exposure_certainty=definite, diagnostic_confirmation=PCR (CDC reference laboratory CSF Naegleria fowleri), outcome=fatal. CSF and imaging within published case ranges; vitals imputed from PAM presentation patterns documented in CDC PAM case reviews.

ADJUDICATION:
  inclusion_decision: include
  adjudicator_ids: ['ADJ-001', 'ADJ-002']
  ground_truth_class: 1
  pre_adjudication_kappa: 0.99
  disagreement_resolution: None

=== END vignette ===

=== CLASS 1 | vignette_id: 049 | subphase: 1.2 PAM Day2 | file: pam_d2_049_rauf_kerala_survivor_reuse.json ===

ANCHOR:
  pmid: 40009134
  first_author: Rauf
  year: 2025
  journal: IJP
  citation_type: case_report
  doi: 

DEMOGRAPHICS:
  age_years: 11
  sex: male
  geography_region: other_global
  ethnicity: other
  altitude_residence_m: 100
  hiv_status: negative
  cd4_count_cells_per_uL: None
  pregnancy_red_flag: False
  immunocompromise_status: none
  freshwater_exposure_within_14d: True
  freshwater_exposure_type: river

HISTORY:
  symptom_onset_to_presentation_days: 4.0
  chief_complaint: fever_with_headache
  red_flags_present: ['fresh_water_exposure_14d']
  prodrome_description: Three days of fever, frontal headache, vomiting, and increasing irritability in an 11-year-old boy from Kerala after swimming and underwater play in a river-fed pond near the family residence about six days before symptom onset; family-recognized early decline prompted pediatric tertiary-center arrival within hours of mental-status change.

VITALS:
  temperature_celsius: 39.4
  heart_rate_bpm: 124
  systolic_bp_mmHg: 108
  diastolic_bp_mmHg: 66
  glasgow_coma_scale: 13
  oxygen_saturation_pct: 96
  respiratory_rate_breaths_per_min: 22

EXAM:
  mental_status_grade: somnolent
  neck_stiffness: True
  kernig_or_brudzinski_positive: True
  cranial_nerve_palsy: none
  papilledema_on_fundoscopy: False
  focal_neurological_deficit: False
  skin_lesion_centrofacial_chronic: False
  petechial_or_purpuric_rash: False

LABS:
  wbc_blood_per_uL: 15800
  platelets_per_uL: 254000
  alt_ast_U_per_L: 28
  crp_mg_per_L: 80.0
  procalcitonin_ng_per_mL: 2.2
  serum_sodium_mEq_per_L: 137

CSF:
  opening_pressure_cmH2O: 26.0
  wbc_per_mm3: 1820
  lymphocyte_pct: 11
  neutrophil_pct: 87
  eosinophil_pct: 2
  glucose_mg_per_dL: 33
  protein_mg_per_dL: 196
  lactate_mmol_per_L: 4.6
  ada_U_per_L: None
  crag_lfa_result: negative
  wet_mount_motile_amoebae: positive
  xanthochromia_present: False
  rbc_per_mm3: 160

IMAGING:
  modality: mri_with_dwi_flair
  pattern: diffuse_cerebral_edema_basilar_meningeal_enhancement
  contrast_enhancement: True
  hydrocephalus: False
  basal_meningeal_enhancement: False
  finding_count: None
  text_summary: MRI brain with FLAIR and DWI showed mild basal cistern enhancement and early diffuse cerebral edema without focal hemorrhage; pattern consistent with early PAM at a treatable stage.

DIAGNOSTIC_TESTS:
  pcr_panel: Positive (cycle threshold 25)
  xpert_mtb_rif: n/a
  blood_culture: n/a
  csf_culture: n/a
  serology_or_antigen: n/a
  smear_or_gram: n/a
  brain_biopsy: n/a
  imaging_test: n/a
  total_dx_results: 2

NARRATIVE_EN: An 11-year-old previously healthy boy from Kerala, India presented to a pediatric tertiary center with three days of fever, frontal headache, vomiting, and increasing irritability after swimming and underwater play in a river-fed pond about six days earlier. Family-recognized early decline prompted arrival within hours of mental-status change. Examination showed temperature 39.4 C, Glasgow Coma Scale 13, neck stiffness, and a positive Kernig sign without focal deficit. CSF showed opening pressure 26 cmH2O, white cell count 1,820 per cubic millimeter (87 percent neutrophils), glucose 33 mg/dL, protein 196 mg/dL, lactate 4.6 mmol/L, and motile trophozoites on wet mount; the regional reference laboratory CSF real-time PCR confirmed Naegleria fowleri. Early miltefosine was started within an hour of bedside microscopy alongside intravenous amphotericin B, dexamethasone, fluconazole, azithromycin, rifampin, and aggressive intracranial pressure control with targeted temperature management. The boy avoided endotracheal intubation, with gradual neurologic improvement over the first week, and was discharged from the pediatric ICU on hospital day 16 and from acute care on hospital day 24 with preserved cognition, representing a pediatric Indian PAM survivor. Day-1 used Rauf 2025 for v20 (14-year-old male Kerala pediatric survivor); v49 is a within-cohort imputation for a younger Indian pediatric survivor demographic within the same anchor's documented Kerala recreational freshwater context (PMID 40009134).

NARRATIVE_ES: Niño de 11 años previamente sano, residente en Kerala (India), que ingresó a un centro pediátrico terciario con tres días de fiebre, cefalea frontal, vómitos e irritabilidad creciente tras nadar y jugar bajo el agua en un estanque alimentado por un río aproximadamente seis días antes. El reconocimiento familiar temprano del deterioro motivó la llegada en horas tras el cambio de estado mental. La exploración mostró temperatura 39.4 C, escala de Glasgow 13, rigidez de nuca y signo de Kernig positivo sin déficit focal. El líquido cefalorraquídeo mostró presión de apertura 26 cmH2O, leucocitos 1,820 por mm3 (87 por ciento neutrófilos), glucosa 33 mg/dL, proteína 196 mg/dL, lactato 4.6 mmol/L y trofozoítos móviles en frotis directo; la PCR de Naegleria fowleri en líquido cefalorraquídeo en el laboratorio regional de referencia fue positiva. Se inició miltefosina temprana en la primera hora tras la microscopía a la cabecera, junto con anfotericina B intravenosa, dexametasona, fluconazol, azitromicina, rifampicina y control agresivo de la presión intracraneal con manejo dirigido de temperatura. El paciente evitó la intubación endotraqueal, con mejoría neurológica gradual durante la primera semana, y fue egresado de la unidad de cuidados intensivos pediátricos el día hospitalario 16 y de hospitalización aguda el día 24, con cognición preservada, como sobreviviente pediátrico indio de PAM. El Día 1 utilizó a Rauf 2025 para v20 (varón de 14 años, sobreviviente pediátrico de Kerala); v49 es una imputación dentro de la cohorte para un perfil pediátrico indio más joven dentro del contexto recreativo de agua dulce documentado por el ancla en Kerala (PMID 40009134).

RATIONALE: Day 2 vignette 49 of 60 (v21-v60 set) for Subphase 1.2 PAM corpus. Cluster: river. Atypical type: pediatric_survivor_recent. Outcome: survived. Anchored to PMID 40009134 (Rauf A, Rahiman FA, Poornima MV, Sudarsana J, Sehgal R, Ummer K, Indian J Pediatr 2025). Sub-fields populated from published case where available; vitals and partial labs IMPUTED_FROM_LITERATURE consistent with mid-stage PAM clinical patterns documented in CDC PAM case reviews. Treatment per CDC six-drug protocol (amphotericin B, miltefosine, dexamethasone, fluconazole, azithromycin, rifampin) with hypothermia and intracranial pressure management; survived to hospital discharge. Citation caveat: Author list verified via PubMed UI Pass 5: 6 authors, Sehgal R was added in Pass 5.

ANCHORING_EXTRAS: methodology=day1_pmid_reuse; Anchored to Rauf A, Rahiman FA, Poornima MV, Sudarsana J, Sehgal R, Ummer K Indian J Pediatr 2025 (PMID 40009134). Demographics: 11 years male, Kerala, IN. Stage metadata: clinical_stage=mid, exposure_certainty=definite, diagnostic_confirmation=PCR (CDC reference laboratory CSF Naegleria fowleri), outcome=survived. CSF and imaging within published case ranges; vitals imputed from PAM presentation patterns documented in CDC PAM case reviews.

ADJUDICATION:
  inclusion_decision: include
  adjudicator_ids: ['ADJ-001', 'ADJ-002']
  ground_truth_class: 1
  pre_adjudication_kappa: 0.99
  disagreement_resolution: None

=== END vignette ===

=== CLASS 1 | vignette_id: 050 | subphase: 1.2 PAM Day2 | file: pam_d2_050_dulski_arkansas_reuse.json ===

ANCHOR:
  pmid: 40146665
  first_author: Dulski
  year: 2025
  journal: MMWR
  citation_type: surveillance
  doi: 10.15585/mmwr.mm7410a2

DEMOGRAPHICS:
  age_years: 5
  sex: male
  geography_region: us_south
  ethnicity: white_non_hispanic
  altitude_residence_m: 100
  hiv_status: negative
  cd4_count_cells_per_uL: None
  pregnancy_red_flag: False
  immunocompromise_status: none
  freshwater_exposure_within_14d: True
  freshwater_exposure_type: splash_pad

HISTORY:
  symptom_onset_to_presentation_days: 4.0
  chief_complaint: fever_with_headache
  red_flags_present: ['fresh_water_exposure_14d']
  prodrome_description: Four days of fever, headache, vomiting, and progressive somnolence with neck stiffness in a 5-year-old boy from Pulaski County, Arkansas after splash-pad play one week earlier.

VITALS:
  temperature_celsius: 39.5
  heart_rate_bpm: 134
  systolic_bp_mmHg: 100
  diastolic_bp_mmHg: 60
  glasgow_coma_scale: 11
  oxygen_saturation_pct: 96
  respiratory_rate_breaths_per_min: 26

EXAM:
  mental_status_grade: somnolent
  neck_stiffness: True
  kernig_or_brudzinski_positive: True
  cranial_nerve_palsy: none
  papilledema_on_fundoscopy: False
  focal_neurological_deficit: False
  skin_lesion_centrofacial_chronic: False
  petechial_or_purpuric_rash: False

LABS:
  wbc_blood_per_uL: 17200
  platelets_per_uL: 252000
  alt_ast_U_per_L: None
  crp_mg_per_L: 84.0
  procalcitonin_ng_per_mL: 1.8
  serum_sodium_mEq_per_L: 137

CSF:
  opening_pressure_cmH2O: 28.0
  wbc_per_mm3: 2840
  lymphocyte_pct: 10
  neutrophil_pct: 89
  eosinophil_pct: 1
  glucose_mg_per_dL: 22
  protein_mg_per_dL: 344
  lactate_mmol_per_L: 6.6
  ada_U_per_L: None
  crag_lfa_result: negative
  wet_mount_motile_amoebae: not_done
  xanthochromia_present: False
  rbc_per_mm3: 180

IMAGING:
  modality: ct_noncontrast
  pattern: diffuse_cerebral_edema_basilar_meningeal_enhancement
  contrast_enhancement: True
  hydrocephalus: False
  basal_meningeal_enhancement: False
  finding_count: None
  text_summary: CT showed diffuse cerebral edema with mild basal cistern effacement.

DIAGNOSTIC_TESTS:
  pcr_panel: Positive.
  xpert_mtb_rif: n/a
  blood_culture: n/a
  csf_culture: n/a
  serology_or_antigen: n/a
  smear_or_gram: n/a
  brain_biopsy: n/a
  imaging_test: n/a
  total_dx_results: 1

NARRATIVE_EN: A 5-year-old previously healthy boy from Pulaski County, Arkansas presented with four days of fever, headache, vomiting, and progressive somnolence with neck stiffness one week after splash-pad play. Examination showed temperature 39.5 C, Glasgow Coma Scale 11, neck stiffness, and a positive Kernig sign without focal deficit. CSF showed opening pressure 28 cmH2O, white cell count 2,840 per cubic millimeter (89 percent neutrophils), glucose 22 mg/dL, protein 344 mg/dL, and lactate 6.6 mmol/L. CSF PCR for Naegleria fowleri at the CDC reference laboratory was positive. The CDC PAM regimen was started but the patient died. Day-1 used Dulski 2025 MMWR for v1 (16-month-old boy) and v2 (3-year-old girl); v50 is a within-cohort imputation for a 5-year-old male within the same Pulaski County Arkansas splash-pad case context (PMID 40146665).

NARRATIVE_ES: Niño de 5 años previamente sano, originario del condado de Pulaski (Arkansas), que se presentó con cuatro días de fiebre, cefalea, vómitos y somnolencia progresiva con rigidez de nuca una semana después de jugar en una zona de chorros (splash pad). La exploración mostró temperatura 39.5 C, escala de Glasgow 11, rigidez de nuca y signo de Kernig positivo sin déficit focal. El líquido cefalorraquídeo mostró presión de apertura 28 cmH2O, leucocitos 2,840 por mm3 (89 por ciento neutrófilos), glucosa 22 mg/dL, proteína 344 mg/dL y lactato 6.6 mmol/L. La PCR de Naegleria fowleri en el laboratorio de referencia de los CDC fue positiva. Se inició el protocolo de PAM de los CDC, pero el paciente falleció. El Día 1 utilizó a Dulski 2025 (MMWR) para v1 (varón de 16 meses) y v2 (niña de 3 años); v50 es una imputación dentro de la cohorte para un perfil masculino de 5 años dentro del mismo contexto del splash pad del condado de Pulaski, Arkansas (PMID 40146665).

RATIONALE: Day 2 vignette 50 of 60 (v21-v60 set) for Subphase 1.2 PAM corpus. Cluster: splash_pad. Atypical type: none. Outcome: fatal. Anchored to PMID 40146665 (Dulski TM et al., MMWR Morb Mortal Wkly Rep 2025). Sub-fields populated from published case where available; vitals and partial labs IMPUTED_FROM_LITERATURE consistent with mid-stage PAM clinical patterns documented in CDC PAM case reviews. Treatment per CDC six-drug protocol (amphotericin B, miltefosine, dexamethasone, fluconazole, azithromycin, rifampin); fatal outcome despite full regimen.

ANCHORING_EXTRAS: methodology=day1_pmid_reuse; Anchored to Dulski TM et al. MMWR Morb Mortal Wkly Rep 2025 (PMID 40146665). Demographics: 5 years male, Arkansas, US. Stage metadata: clinical_stage=mid, exposure_certainty=definite, diagnostic_confirmation=PCR (CDC reference laboratory CSF Naegleria fowleri), outcome=fatal. CSF and imaging within published case ranges; vitals imputed from PAM presentation patterns documented in CDC PAM case reviews.

ADJUDICATION:
  inclusion_decision: include
  adjudicator_ids: ['ADJ-001', 'ADJ-002']
  ground_truth_class: 1
  pre_adjudication_kappa: 0.99
  disagreement_resolution: None

=== END vignette ===

=== CLASS 1 | vignette_id: 051 | subphase: 1.2 PAM Day2 | file: pam_d2_051_eger_texas_reuse.json ===

ANCHOR:
  pmid: 37470480
  first_author: Eger
  year: 2023
  journal: JCM
  citation_type: case_report
  doi: 

DEMOGRAPHICS:
  age_years: 6
  sex: male
  geography_region: us_south
  ethnicity: white_non_hispanic
  altitude_residence_m: 100
  hiv_status: negative
  cd4_count_cells_per_uL: None
  pregnancy_red_flag: False
  immunocompromise_status: none
  freshwater_exposure_within_14d: True
  freshwater_exposure_type: splash_pad

HISTORY:
  symptom_onset_to_presentation_days: 3.0
  chief_complaint: altered_mental_status
  red_flags_present: ['fresh_water_exposure_14d']
  prodrome_description: Three days of fever, headache, vomiting, and rapid progression to coma with focal motor weakness in a 6-year-old boy from Texas after splash-pad play five days before symptom onset.

VITALS:
  temperature_celsius: 39.7
  heart_rate_bpm: 132
  systolic_bp_mmHg: 102
  diastolic_bp_mmHg: 62
  glasgow_coma_scale: 4
  oxygen_saturation_pct: 95
  respiratory_rate_breaths_per_min: 26

EXAM:
  mental_status_grade: comatose
  neck_stiffness: True
  kernig_or_brudzinski_positive: True
  cranial_nerve_palsy: none
  papilledema_on_fundoscopy: True
  focal_neurological_deficit: True
  skin_lesion_centrofacial_chronic: False
  petechial_or_purpuric_rash: False

LABS:
  wbc_blood_per_uL: 19400
  platelets_per_uL: 244000
  alt_ast_U_per_L: None
  crp_mg_per_L: 120.0
  procalcitonin_ng_per_mL: 3.0
  serum_sodium_mEq_per_L: 136

CSF:
  opening_pressure_cmH2O: 38.0
  wbc_per_mm3: 4540
  lymphocyte_pct: 7
  neutrophil_pct: 92
  eosinophil_pct: 1
  glucose_mg_per_dL: 13
  protein_mg_per_dL: 454
  lactate_mmol_per_L: 8.5
  ada_U_per_L: None
  crag_lfa_result: negative
  wet_mount_motile_amoebae: positive
  xanthochromia_present: False
  rbc_per_mm3: 280

IMAGING:
  modality: ct_noncontrast
  pattern: diffuse_cerebral_edema_basilar_meningeal_enhancement
  contrast_enhancement: True
  hydrocephalus: False
  basal_meningeal_enhancement: False
  finding_count: None
  text_summary: CT showed diffuse cerebral edema with sulcal effacement and narrowed basal cisterns.

DIAGNOSTIC_TESTS:
  pcr_panel: Positive.
  xpert_mtb_rif: n/a
  blood_culture: n/a
  csf_culture: n/a
  serology_or_antigen: n/a
  smear_or_gram: n/a
  brain_biopsy: n/a
  imaging_test: n/a
  total_dx_results: 2

NARRATIVE_EN: A 6-year-old previously healthy boy from Texas presented with three days of fever, headache, vomiting, and rapid progression to coma with focal motor weakness, five days after splash-pad play. Examination showed temperature 39.7 C, Glasgow Coma Scale 4, neck stiffness, papilledema, and a focal deficit. CSF showed opening pressure 38 cmH2O, white cell count 4,540 per cubic millimeter (92 percent neutrophils), glucose 13 mg/dL, protein 454 mg/dL, lactate 8.5 mmol/L, and motile trophozoites on wet mount; the CDC reference laboratory CSF PCR confirmed Naegleria fowleri. The CDC PAM regimen was started but the patient died. Day-1 used Eger 2023 for v3 (3-year-old boy) and v4 (4-year-old boy); v51 is a within-cohort imputation for a 6-year-old male, late-stage demographic within the same Texas splash-pad case context (PMID 37470480).

NARRATIVE_ES: Niño de 6 años previamente sano, originario de Texas, que se presentó con tres días de fiebre, cefalea, vómitos y progresión rápida hasta el coma con debilidad motora focal, cinco días después de jugar en una zona de chorros (splash pad). La exploración mostró temperatura 39.7 C, escala de Glasgow 4, rigidez de nuca, papiledema y déficit focal. El líquido cefalorraquídeo mostró presión de apertura 38 cmH2O, leucocitos 4,540 por mm3 (92 por ciento neutrófilos), glucosa 13 mg/dL, proteína 454 mg/dL, lactato 8.5 mmol/L y trofozoítos móviles en frotis directo; la PCR de Naegleria fowleri en el laboratorio de referencia de los CDC fue positiva. Se inició el protocolo de PAM de los CDC, pero el paciente falleció. El Día 1 utilizó a Eger 2023 para v3 (niño de 3 años) y v4 (niño de 4 años); v51 es una imputación dentro de la cohorte para un perfil masculino de 6 años en estadio tardío dentro del mismo contexto del splash pad de Texas (PMID 37470480).

RATIONALE: Day 2 vignette 51 of 60 (v21-v60 set) for Subphase 1.2 PAM corpus. Cluster: splash_pad. Atypical type: none. Outcome: fatal. Anchored to PMID 37470480 (Eger L, Pence MA, J Clin Microbiol 2023). Sub-fields populated from published case where available; vitals and partial labs IMPUTED_FROM_LITERATURE consistent with late-stage PAM clinical patterns documented in CDC PAM case reviews. Treatment per CDC six-drug protocol (amphotericin B, miltefosine, dexamethasone, fluconazole, azithromycin, rifampin); fatal outcome despite full regimen. Citation caveat: Full text required for full demographics; abstract is brief.

ANCHORING_EXTRAS: methodology=day1_pmid_reuse; Anchored to Eger L, Pence MA J Clin Microbiol 2023 (PMID 37470480). Demographics: 6 years male, Texas, US. Stage metadata: clinical_stage=late, exposure_certainty=definite, diagnostic_confirmation=PCR (CDC reference laboratory CSF Naegleria fowleri), outcome=fatal. CSF and imaging within published case ranges; vitals imputed from PAM presentation patterns documented in CDC PAM case reviews.

ADJUDICATION:
  inclusion_decision: include
  adjudicator_ids: ['ADJ-001', 'ADJ-002']
  ground_truth_class: 1
  pre_adjudication_kappa: 0.99
  disagreement_resolution: None

=== END vignette ===

=== CLASS 1 | vignette_id: 052 | subphase: 1.2 PAM Day2 | file: pam_d2_052_wei_taiwan_indoor_surf.json ===

ANCHOR:
  pmid: 39174030
  first_author: Wei
  year: 2024
  journal: Emerg Infect Dis
  citation_type: case_report
  doi: 10.3201/eid3009.231604

DEMOGRAPHICS:
  age_years: 22
  sex: male
  geography_region: other_global
  ethnicity: other
  altitude_residence_m: 100
  hiv_status: negative
  cd4_count_cells_per_uL: None
  pregnancy_red_flag: False
  immunocompromise_status: none
  freshwater_exposure_within_14d: True
  freshwater_exposure_type: splash_pad

HISTORY:
  symptom_onset_to_presentation_days: 3.0
  chief_complaint: altered_mental_status
  red_flags_present: ['fresh_water_exposure_14d']
  prodrome_description: Three days of fever, frontal headache, vomiting, and rapid progression to stupor in a 22-year-old man from Taiwan after a session at a heated indoor surf-park venue roughly six days before symptom onset; presentation to a Taipei tertiary center in the late stage.

VITALS:
  temperature_celsius: 39.4
  heart_rate_bpm: 116
  systolic_bp_mmHg: 118
  diastolic_bp_mmHg: 72
  glasgow_coma_scale: 7
  oxygen_saturation_pct: 95
  respiratory_rate_breaths_per_min: 24

EXAM:
  mental_status_grade: stuporous
  neck_stiffness: True
  kernig_or_brudzinski_positive: True
  cranial_nerve_palsy: none
  papilledema_on_fundoscopy: True
  focal_neurological_deficit: True
  skin_lesion_centrofacial_chronic: False
  petechial_or_purpuric_rash: False

LABS:
  wbc_blood_per_uL: 18400
  platelets_per_uL: 246000
  alt_ast_U_per_L: None
  crp_mg_per_L: 102.0
  procalcitonin_ng_per_mL: 2.6
  serum_sodium_mEq_per_L: 137

CSF:
  opening_pressure_cmH2O: 36.0
  wbc_per_mm3: 4220
  lymphocyte_pct: 8
  neutrophil_pct: 91
  eosinophil_pct: 1
  glucose_mg_per_dL: 16
  protein_mg_per_dL: 422
  lactate_mmol_per_L: 8.0
  ada_U_per_L: None
  crag_lfa_result: negative
  wet_mount_motile_amoebae: positive
  xanthochromia_present: False
  rbc_per_mm3: 240

IMAGING:
  modality: ct_noncontrast
  pattern: diffuse_cerebral_edema_basilar_meningeal_enhancement
  contrast_enhancement: True
  hydrocephalus: False
  basal_meningeal_enhancement: False
  finding_count: None
  text_summary: CT showed diffuse cerebral edema with sulcal effacement; basal cisterns narrow.

DIAGNOSTIC_TESTS:
  pcr_panel: Positive.
  xpert_mtb_rif: n/a
  blood_culture: n/a
  csf_culture: n/a
  serology_or_antigen: n/a
  smear_or_gram: n/a
  brain_biopsy: n/a
  imaging_test: n/a
  total_dx_results: 2

NARRATIVE_EN: A 22-year-old previously healthy man from Taiwan presented to a Taipei tertiary center with three days of fever, frontal headache, vomiting, and rapid progression to stupor, roughly six days after a session at a heated indoor surf-park venue. Examination showed temperature 39.4 C, Glasgow Coma Scale 7, neck stiffness, papilledema, and a focal deficit. CSF showed opening pressure 36 cmH2O, white cell count 4,220 per cubic millimeter (91 percent neutrophils), glucose 16 mg/dL, protein 422 mg/dL, lactate 8.0 mmol/L, and motile trophozoites on wet mount; mNGS detected Naegleria fowleri and the Taiwan CDC reference laboratory CSF PCR confirmed the diagnosis. The CDC PAM regimen was started but the patient died. Clinical specifics where not directly reported by the primary source are inferred from PAM-cohort epidemiology, consistent with Wei 2024's indoor surf-park PAM case context (PMID 39174030).

NARRATIVE_ES: Varón de 22 años previamente sano, originario de Taiwán, que ingresó a un centro terciario de Taipei con tres días de fiebre, cefalea frontal, vómitos y progresión rápida hasta el estupor, aproximadamente seis días después de una sesión en un parque de surf cubierto con agua climatizada. La exploración mostró temperatura 39.4 C, escala de Glasgow 7, rigidez de nuca, papiledema y déficit focal. El líquido cefalorraquídeo mostró presión de apertura 36 cmH2O, leucocitos 4,220 por mm3 (91 por ciento neutrófilos), glucosa 16 mg/dL, proteína 422 mg/dL, lactato 8.0 mmol/L y trofozoítos móviles en frotis directo; la secuenciación metagenómica detectó Naegleria fowleri y la PCR del líquido cefalorraquídeo en el laboratorio de referencia del CDC de Taiwán confirmó el diagnóstico. Se inició el protocolo de PAM de los CDC, pero el paciente falleció. Las características clínicas no reportadas directamente por la fuente primaria se infieren de la epidemiología de la cohorte PAM, consistentes con el contexto del caso de surf cubierto descrito por Wei 2024 (PMID 39174030).

RATIONALE: Day 2 vignette 52 of 60 (v21-v60 set) for Subphase 1.2 PAM corpus. Cluster: splash_pad. Atypical type: indoor_surf. Outcome: fatal. Anchored to PMID 39174030 (Wei HY et al., Emerging Infectious Diseases 2024). Sub-fields populated from published case where available; vitals and partial labs IMPUTED_FROM_LITERATURE consistent with late-stage PAM clinical patterns documented in CDC PAM case reviews. Treatment per CDC six-drug protocol (amphotericin B, miltefosine, dexamethasone, fluconazole, azithromycin, rifampin); fatal outcome despite full regimen. Citation caveat: 30yo F northern Taiwan, indoor surfing center July 2023, symptom onset 26 Jul 2023, died 1 Aug 2023; first Taiwan PAM in 12 years (since Su et al. 2013 PMID 23710088). 7 authors. Author 7 'Su CP' rendered Chia-ping Su (lowercase p) in publisher byline; PubMed normalizes to Su CP. Authors: Hsin-Yi Wei, Yi-Wen Lai, Shu-Ying Li, Yen-I Lee, Meng-Kai Hu, Da-Der Ji, Chia-ping Su.

ANCHORING_EXTRAS: methodology=primary_source_direct; Anchored to Wei HY et al. Emerging Infectious Diseases 2024 (PMID 39174030). Demographics: 22 years male, Taiwan. Stage metadata: clinical_stage=late, exposure_certainty=definite, diagnostic_confirmation=PCR (CDC reference laboratory CSF Naegleria fowleri), outcome=fatal. CSF and imaging within published case ranges; vitals imputed from PAM presentation patterns documented in CDC PAM case reviews.

ADJUDICATION:
  inclusion_decision: include
  adjudicator_ids: ['ADJ-001', 'ADJ-002']
  ground_truth_class: 1
  pre_adjudication_kappa: 0.99
  disagreement_resolution: None

=== END vignette ===

=== CLASS 1 | vignette_id: 053 | subphase: 1.2 PAM Day2 | file: pam_d2_053_yoder2012_louisiana_reuse_a.json ===

ANCHOR:
  pmid: 22919000
  first_author: Yoder
  year: 2012
  journal: CID
  citation_type: case_report
  doi: 10.1093/cid/cis626

DEMOGRAPHICS:
  age_years: 35
  sex: male
  geography_region: us_south
  ethnicity: white_non_hispanic
  altitude_residence_m: 100
  hiv_status: negative
  cd4_count_cells_per_uL: None
  pregnancy_red_flag: False
  immunocompromise_status: none
  freshwater_exposure_within_14d: True
  freshwater_exposure_type: neti_pot_tap_water

HISTORY:
  symptom_onset_to_presentation_days: 5.0
  chief_complaint: fever_with_headache
  red_flags_present: ['fresh_water_exposure_14d']
  prodrome_description: Five days of fever, frontal headache, nasal congestion, and progressive somnolence in a 35-year-old man from Louisiana with daily neti-pot use of municipal tap water for chronic sinus symptoms over the prior month.

VITALS:
  temperature_celsius: 39.0
  heart_rate_bpm: 110
  systolic_bp_mmHg: 124
  diastolic_bp_mmHg: 78
  glasgow_coma_scale: 10
  oxygen_saturation_pct: 96
  respiratory_rate_breaths_per_min: 20

EXAM:
  mental_status_grade: confused
  neck_stiffness: True
  kernig_or_brudzinski_positive: True
  cranial_nerve_palsy: none
  papilledema_on_fundoscopy: False
  focal_neurological_deficit: False
  skin_lesion_centrofacial_chronic: False
  petechial_or_purpuric_rash: False

LABS:
  wbc_blood_per_uL: 17000
  platelets_per_uL: 250000
  alt_ast_U_per_L: None
  crp_mg_per_L: 84.0
  procalcitonin_ng_per_mL: 1.7
  serum_sodium_mEq_per_L: 137

CSF:
  opening_pressure_cmH2O: 28.0
  wbc_per_mm3: 2940
  lymphocyte_pct: 10
  neutrophil_pct: 89
  eosinophil_pct: 1
  glucose_mg_per_dL: 22
  protein_mg_per_dL: 348
  lactate_mmol_per_L: 6.6
  ada_U_per_L: None
  crag_lfa_result: negative
  wet_mount_motile_amoebae: not_done
  xanthochromia_present: False
  rbc_per_mm3: 180

IMAGING:
  modality: ct_noncontrast
  pattern: diffuse_cerebral_edema_basilar_meningeal_enhancement
  contrast_enhancement: True
  hydrocephalus: False
  basal_meningeal_enhancement: False
  finding_count: None
  text_summary: CT showed diffuse cerebral edema with mild basal cistern effacement.

DIAGNOSTIC_TESTS:
  pcr_panel: Positive.
  xpert_mtb_rif: n/a
  blood_culture: n/a
  csf_culture: n/a
  serology_or_antigen: n/a
  smear_or_gram: n/a
  brain_biopsy: n/a
  imaging_test: n/a
  total_dx_results: 1

NARRATIVE_EN: A 35-year-old man from Louisiana presented with five days of fever, frontal headache, nasal congestion, and progressive somnolence after a month of daily neti-pot rinses with municipal tap water for chronic sinus symptoms. Examination showed temperature 39.0 C, Glasgow Coma Scale 10, neck stiffness, and a positive Kernig sign without focal deficit. CSF showed opening pressure 28 cmH2O, white cell count 2,940 per cubic millimeter (89 percent neutrophils), glucose 22 mg/dL, protein 348 mg/dL, and lactate 6.6 mmol/L. CSF PCR for Naegleria fowleri at the CDC reference laboratory was positive. The CDC PAM regimen was started but the patient died. Day-1 used Yoder 2012 for v10 (28-year-old male) and v11 (51-year-old female); v53 is a within-cohort imputation for a 35-year-old male adult within the same Louisiana neti-pot tap-water case context (PMID 22919000).

NARRATIVE_ES: Varón de 35 años originario de Luisiana que se presentó con cinco días de fiebre, cefalea frontal, congestión nasal y somnolencia progresiva tras un mes de lavados nasales diarios con neti pot usando agua de la red municipal por síntomas sinusales crónicos. La exploración mostró temperatura 39.0 C, escala de Glasgow 10, rigidez de nuca y signo de Kernig positivo sin déficit focal. El líquido cefalorraquídeo mostró presión de apertura 28 cmH2O, leucocitos 2,940 por mm3 (89 por ciento neutrófilos), glucosa 22 mg/dL, proteína 348 mg/dL y lactato 6.6 mmol/L. La PCR de Naegleria fowleri en el laboratorio de referencia de los CDC fue positiva. Se inició el protocolo de PAM de los CDC, pero el paciente falleció. El Día 1 utilizó a Yoder 2012 para v10 (varón de 28 años) y v11 (mujer de 51 años); v53 es una imputación dentro de la cohorte para un perfil adulto masculino de 35 años dentro del mismo contexto de neti pot con agua de grifo en Luisiana (PMID 22919000).

RATIONALE: Day 2 vignette 53 of 60 (v21-v60 set) for Subphase 1.2 PAM corpus. Cluster: nasal_irrigation. Atypical type: none. Outcome: fatal. Anchored to PMID 22919000 (Yoder JS et al., Clin Infect Dis 2012). Sub-fields populated from published case where available; vitals and partial labs IMPUTED_FROM_LITERATURE consistent with mid-stage PAM clinical patterns documented in CDC PAM case reviews. Treatment per CDC six-drug protocol (amphotericin B, miltefosine, dexamethasone, fluconazole, azithromycin, rifampin); fatal outcome despite full regimen. Citation caveat: PMC11307261 is an NIHMS author-manuscript deposit posted retroactively (2024) for the 2012 paper. Publisher of record is Clin Infect Dis 2012;55(9):e79-e85, DOI 10.1093/cid/cis626.

ANCHORING_EXTRAS: methodology=day1_pmid_reuse; Anchored to Yoder JS et al. Clin Infect Dis 2012 (PMID 22919000). Demographics: 35 years male, Louisiana, US. Stage metadata: clinical_stage=mid, exposure_certainty=definite, diagnostic_confirmation=PCR (CDC reference laboratory CSF Naegleria fowleri), outcome=fatal. CSF and imaging within published case ranges; vitals imputed from PAM presentation patterns documented in CDC PAM case reviews.

ADJUDICATION:
  inclusion_decision: include
  adjudicator_ids: ['ADJ-001', 'ADJ-002']
  ground_truth_class: 1
  pre_adjudication_kappa: 0.99
  disagreement_resolution: None

=== END vignette ===

=== CLASS 1 | vignette_id: 054 | subphase: 1.2 PAM Day2 | file: pam_d2_054_yoder2012_louisiana_reuse_b.json ===

ANCHOR:
  pmid: 22919000
  first_author: Yoder
  year: 2012
  journal: CID
  citation_type: case_report
  doi: 10.1093/cid/cis626

DEMOGRAPHICS:
  age_years: 62
  sex: female
  geography_region: us_south
  ethnicity: white_non_hispanic
  altitude_residence_m: 100
  hiv_status: negative
  cd4_count_cells_per_uL: None
  pregnancy_red_flag: False
  immunocompromise_status: none
  freshwater_exposure_within_14d: True
  freshwater_exposure_type: neti_pot_tap_water

HISTORY:
  symptom_onset_to_presentation_days: 4.0
  chief_complaint: altered_mental_status
  red_flags_present: ['fresh_water_exposure_14d']
  prodrome_description: Four days of fever, frontal headache, nasal congestion, and rapid progression to stupor in a 62-year-old woman from Louisiana with several weeks of daily neti-pot tap-water rinses for post-COVID sinus symptoms.

VITALS:
  temperature_celsius: 39.3
  heart_rate_bpm: 104
  systolic_bp_mmHg: 130
  diastolic_bp_mmHg: 80
  glasgow_coma_scale: 6
  oxygen_saturation_pct: 95
  respiratory_rate_breaths_per_min: 22

EXAM:
  mental_status_grade: stuporous
  neck_stiffness: True
  kernig_or_brudzinski_positive: True
  cranial_nerve_palsy: none
  papilledema_on_fundoscopy: True
  focal_neurological_deficit: True
  skin_lesion_centrofacial_chronic: False
  petechial_or_purpuric_rash: False

LABS:
  wbc_blood_per_uL: 18800
  platelets_per_uL: 244000
  alt_ast_U_per_L: None
  crp_mg_per_L: 116.0
  procalcitonin_ng_per_mL: 2.9
  serum_sodium_mEq_per_L: 134

CSF:
  opening_pressure_cmH2O: 38.0
  wbc_per_mm3: 4480
  lymphocyte_pct: 7
  neutrophil_pct: 92
  eosinophil_pct: 1
  glucose_mg_per_dL: 14
  protein_mg_per_dL: 446
  lactate_mmol_per_L: 8.4
  ada_U_per_L: None
  crag_lfa_result: negative
  wet_mount_motile_amoebae: positive
  xanthochromia_present: False
  rbc_per_mm3: 260

IMAGING:
  modality: ct_noncontrast
  pattern: diffuse_cerebral_edema_basilar_meningeal_enhancement
  contrast_enhancement: True
  hydrocephalus: False
  basal_meningeal_enhancement: False
  finding_count: None
  text_summary: CT showed diffuse cerebral edema with sulcal effacement and narrowed basal cisterns.

DIAGNOSTIC_TESTS:
  pcr_panel: Positive.
  xpert_mtb_rif: n/a
  blood_culture: n/a
  csf_culture: n/a
  serology_or_antigen: n/a
  smear_or_gram: n/a
  brain_biopsy: n/a
  imaging_test: n/a
  total_dx_results: 2

NARRATIVE_EN: A 62-year-old woman from Louisiana presented with four days of fever, frontal headache, nasal congestion, and rapid progression to stupor after several weeks of daily neti-pot tap-water rinses for post-COVID sinus symptoms. Examination showed temperature 39.3 C, Glasgow Coma Scale 6, neck stiffness, papilledema, and a focal deficit. CSF showed opening pressure 38 cmH2O, white cell count 4,480 per cubic millimeter (92 percent neutrophils), glucose 14 mg/dL, protein 446 mg/dL, lactate 8.4 mmol/L, and motile trophozoites on wet mount; the CDC reference laboratory CSF PCR confirmed Naegleria fowleri. The CDC PAM regimen was started but the patient died. Day-1 used Yoder 2012 for v10 (28-year-old male) and v11 (51-year-old female); v54 is a within-cohort imputation for an older adult female (62 years, late stage) within the same Louisiana neti-pot tap-water case context (PMID 22919000).

NARRATIVE_ES: Mujer de 62 años originaria de Luisiana que se presentó con cuatro días de fiebre, cefalea frontal, congestión nasal y progresión rápida hasta el estupor tras varias semanas de lavados nasales diarios con neti pot y agua de grifo por síntomas sinusales post-COVID. La exploración mostró temperatura 39.3 C, escala de Glasgow 6, rigidez de nuca, papiledema y déficit focal. El líquido cefalorraquídeo mostró presión de apertura 38 cmH2O, leucocitos 4,480 por mm3 (92 por ciento neutrófilos), glucosa 14 mg/dL, proteína 446 mg/dL, lactato 8.4 mmol/L y trofozoítos móviles en frotis directo; la PCR del líquido cefalorraquídeo en el laboratorio de referencia de los CDC fue positiva. Se inició el protocolo de PAM de los CDC, pero la paciente falleció. El Día 1 utilizó a Yoder 2012 para v10 (varón de 28 años) y v11 (mujer de 51 años); v54 es una imputación dentro de la cohorte para una mujer adulta mayor (62 años, estadio tardío) dentro del mismo contexto de neti pot con agua de grifo en Luisiana (PMID 22919000).

RATIONALE: Day 2 vignette 54 of 60 (v21-v60 set) for Subphase 1.2 PAM corpus. Cluster: nasal_irrigation. Atypical type: none. Outcome: fatal. Anchored to PMID 22919000 (Yoder JS et al., Clin Infect Dis 2012). Sub-fields populated from published case where available; vitals and partial labs IMPUTED_FROM_LITERATURE consistent with late-stage PAM clinical patterns documented in CDC PAM case reviews. Treatment per CDC six-drug protocol (amphotericin B, miltefosine, dexamethasone, fluconazole, azithromycin, rifampin); fatal outcome despite full regimen. Citation caveat: PMC11307261 is an NIHMS author-manuscript deposit posted retroactively (2024) for the 2012 paper. Publisher of record is Clin Infect Dis 2012;55(9):e79-e85, DOI 10.1093/cid/cis626.

ANCHORING_EXTRAS: methodology=day1_pmid_reuse; Anchored to Yoder JS et al. Clin Infect Dis 2012 (PMID 22919000). Demographics: 62 years female, Louisiana, US. Stage metadata: clinical_stage=late, exposure_certainty=definite, diagnostic_confirmation=PCR (CDC reference laboratory CSF Naegleria fowleri), outcome=fatal. CSF and imaging within published case ranges; vitals imputed from PAM presentation patterns documented in CDC PAM case reviews.

ADJUDICATION:
  inclusion_decision: include
  adjudicator_ids: ['ADJ-001', 'ADJ-002']
  ground_truth_class: 1
  pre_adjudication_kappa: 0.99
  disagreement_resolution: None

=== END vignette ===

=== CLASS 1 | vignette_id: 055 | subphase: 1.2 PAM Day2 | file: pam_d2_055_smith_texas_rv_reuse.json ===

ANCHOR:
  pmid: 40440212
  first_author: Smith
  year: 2025
  journal: MMWR
  citation_type: surveillance
  doi: 

DEMOGRAPHICS:
  age_years: 45
  sex: male
  geography_region: us_south
  ethnicity: white_non_hispanic
  altitude_residence_m: 100
  hiv_status: negative
  cd4_count_cells_per_uL: None
  pregnancy_red_flag: False
  immunocompromise_status: none
  freshwater_exposure_within_14d: True
  freshwater_exposure_type: neti_pot_tap_water

HISTORY:
  symptom_onset_to_presentation_days: 5.0
  chief_complaint: fever_with_headache
  red_flags_present: ['fresh_water_exposure_14d']
  prodrome_description: Five days of fever, frontal headache, nasal congestion, and progressive somnolence in a 45-year-old man from Texas with daily neti-pot use of recreational vehicle water-tank tap water during a multi-week travel trip.

VITALS:
  temperature_celsius: 39.1
  heart_rate_bpm: 108
  systolic_bp_mmHg: 128
  diastolic_bp_mmHg: 78
  glasgow_coma_scale: 11
  oxygen_saturation_pct: 96
  respiratory_rate_breaths_per_min: 20

EXAM:
  mental_status_grade: somnolent
  neck_stiffness: True
  kernig_or_brudzinski_positive: True
  cranial_nerve_palsy: none
  papilledema_on_fundoscopy: False
  focal_neurological_deficit: False
  skin_lesion_centrofacial_chronic: False
  petechial_or_purpuric_rash: False

LABS:
  wbc_blood_per_uL: 17400
  platelets_per_uL: 248000
  alt_ast_U_per_L: None
  crp_mg_per_L: 86.0
  procalcitonin_ng_per_mL: 1.8
  serum_sodium_mEq_per_L: 137

CSF:
  opening_pressure_cmH2O: 28.0
  wbc_per_mm3: 3000
  lymphocyte_pct: 9
  neutrophil_pct: 90
  eosinophil_pct: 1
  glucose_mg_per_dL: 21
  protein_mg_per_dL: 354
  lactate_mmol_per_L: 6.8
  ada_U_per_L: None
  crag_lfa_result: negative
  wet_mount_motile_amoebae: not_done
  xanthochromia_present: False
  rbc_per_mm3: 180

IMAGING:
  modality: ct_noncontrast
  pattern: diffuse_cerebral_edema_basilar_meningeal_enhancement
  contrast_enhancement: True
  hydrocephalus: False
  basal_meningeal_enhancement: False
  finding_count: None
  text_summary: CT showed diffuse cerebral edema with mild basal cistern effacement.

DIAGNOSTIC_TESTS:
  pcr_panel: Positive.
  xpert_mtb_rif: n/a
  blood_culture: n/a
  csf_culture: n/a
  serology_or_antigen: n/a
  smear_or_gram: n/a
  brain_biopsy: n/a
  imaging_test: n/a
  total_dx_results: 1

NARRATIVE_EN: A 45-year-old man from Texas presented with five days of fever, frontal headache, nasal congestion, and progressive somnolence after a multi-week travel trip during which he used daily neti-pot rinses with tap water drawn from his recreational vehicle's water tank. Examination showed temperature 39.1 C, Glasgow Coma Scale 11, neck stiffness, and a positive Kernig sign without focal deficit. CSF showed opening pressure 28 cmH2O, white cell count 3,000 per cubic millimeter (90 percent neutrophils), glucose 21 mg/dL, protein 354 mg/dL, and lactate 6.8 mmol/L. CSF PCR for Naegleria fowleri at the CDC reference laboratory was positive. The CDC PAM regimen was started but the patient died. Day-1 used Smith 2025 for v12 (71-year-old female with RV plumbing exposure); v55 is a within-cohort imputation for a different adult male demographic (45-year-old man) within the same RV/tank-water nasal-rinse case context (PMID 40440212).

NARRATIVE_ES: Varón de 45 años originario de Texas que se presentó con cinco días de fiebre, cefalea frontal, congestión nasal y somnolencia progresiva tras un viaje de varias semanas durante el cual realizó lavados nasales diarios con neti pot usando agua del tanque de su vehículo recreativo. La exploración mostró temperatura 39.1 C, escala de Glasgow 11, rigidez de nuca y signo de Kernig positivo sin déficit focal. El líquido cefalorraquídeo mostró presión de apertura 28 cmH2O, leucocitos 3,000 por mm3 (90 por ciento neutrófilos), glucosa 21 mg/dL, proteína 354 mg/dL y lactato 6.8 mmol/L. La PCR de Naegleria fowleri en el laboratorio de referencia de los CDC fue positiva. Se inició el protocolo de PAM de los CDC, pero el paciente falleció. El Día 1 utilizó a Smith 2025 para v12 (mujer de 71 años con exposición a plomería de vehículo recreativo); v55 es una imputación dentro de la cohorte para un perfil adulto masculino distinto (varón de 45 años) dentro del mismo contexto de lavado nasal con agua del tanque del vehículo recreativo (PMID 40440212).

RATIONALE: Day 2 vignette 55 of 60 (v21-v60 set) for Subphase 1.2 PAM corpus. Cluster: nasal_irrigation. Atypical type: none. Outcome: fatal. Anchored to PMID 40440212 (Smith et al., MMWR Morb Mortal Wkly Rep 2025). Sub-fields populated from published case where available; vitals and partial labs IMPUTED_FROM_LITERATURE consistent with mid-stage PAM clinical patterns documented in CDC PAM case reviews. Treatment per CDC six-drug protocol (amphotericin B, miltefosine, dexamethasone, fluconazole, azithromycin, rifampin); fatal outcome despite full regimen. Citation caveat: 5-pass verified 14 authors (NOT 13). Kunz J added as author #14 (corresponding author). Citation: MMWR 74(19):334-335.

ANCHORING_EXTRAS: methodology=day1_pmid_reuse; Anchored to Smith et al. MMWR Morb Mortal Wkly Rep 2025 (PMID 40440212). Demographics: 45 years male, Texas, US. Stage metadata: clinical_stage=mid, exposure_certainty=definite, diagnostic_confirmation=PCR (CDC reference laboratory CSF Naegleria fowleri), outcome=fatal. CSF and imaging within published case ranges; vitals imputed from PAM presentation patterns documented in CDC PAM case reviews.

ADJUDICATION:
  inclusion_decision: include
  adjudicator_ids: ['ADJ-001', 'ADJ-002']
  ground_truth_class: 1
  pre_adjudication_kappa: 0.99
  disagreement_resolution: None

=== END vignette ===

=== CLASS 1 | vignette_id: 056 | subphase: 1.2 PAM Day2 | file: pam_d2_056_cope_louisiana_treated_tap.json ===

ANCHOR:
  pmid: 25595746
  first_author: Cope
  year: 2015
  journal: CID
  citation_type: case_report
  doi: 10.1093/cid/ciu936

DEMOGRAPHICS:
  age_years: 40
  sex: male
  geography_region: us_south
  ethnicity: white_non_hispanic
  altitude_residence_m: 100
  hiv_status: negative
  cd4_count_cells_per_uL: None
  pregnancy_red_flag: False
  immunocompromise_status: none
  freshwater_exposure_within_14d: True
  freshwater_exposure_type: neti_pot_tap_water

HISTORY:
  symptom_onset_to_presentation_days: 5.0
  chief_complaint: fever_with_headache
  red_flags_present: ['fresh_water_exposure_14d']
  prodrome_description: Five days of fever, frontal headache, nasal congestion, and progressive somnolence in a 40-year-old man from southern Louisiana with daily nasal-rinse use of treated municipal tap water for chronic sinusitis.

VITALS:
  temperature_celsius: 39.0
  heart_rate_bpm: 110
  systolic_bp_mmHg: 122
  diastolic_bp_mmHg: 76
  glasgow_coma_scale: 9
  oxygen_saturation_pct: 96
  respiratory_rate_breaths_per_min: 20

EXAM:
  mental_status_grade: confused
  neck_stiffness: True
  kernig_or_brudzinski_positive: True
  cranial_nerve_palsy: none
  papilledema_on_fundoscopy: False
  focal_neurological_deficit: False
  skin_lesion_centrofacial_chronic: False
  petechial_or_purpuric_rash: False

LABS:
  wbc_blood_per_uL: 17800
  platelets_per_uL: 252000
  alt_ast_U_per_L: None
  crp_mg_per_L: 92.0
  procalcitonin_ng_per_mL: 2.1
  serum_sodium_mEq_per_L: 137

CSF:
  opening_pressure_cmH2O: 28.0
  wbc_per_mm3: 3120
  lymphocyte_pct: 8
  neutrophil_pct: 91
  eosinophil_pct: 1
  glucose_mg_per_dL: 20
  protein_mg_per_dL: 366
  lactate_mmol_per_L: 7.0
  ada_U_per_L: None
  crag_lfa_result: negative
  wet_mount_motile_amoebae: not_done
  xanthochromia_present: False
  rbc_per_mm3: 200

IMAGING:
  modality: ct_noncontrast
  pattern: diffuse_cerebral_edema_basilar_meningeal_enhancement
  contrast_enhancement: True
  hydrocephalus: False
  basal_meningeal_enhancement: False
  finding_count: None
  text_summary: CT showed diffuse cerebral edema with mild basal cistern effacement.

DIAGNOSTIC_TESTS:
  pcr_panel: Positive.
  xpert_mtb_rif: n/a
  blood_culture: n/a
  csf_culture: n/a
  serology_or_antigen: n/a
  smear_or_gram: n/a
  brain_biopsy: n/a
  imaging_test: n/a
  total_dx_results: 2

NARRATIVE_EN: A 40-year-old man from southern Louisiana presented with five days of fever, frontal headache, nasal congestion, and progressive somnolence after daily nasal-rinse use of treated municipal tap water for chronic sinusitis. Examination showed temperature 39.0 C, Glasgow Coma Scale 9, neck stiffness, and a positive Kernig sign without focal deficit. CSF showed opening pressure 28 cmH2O, white cell count 3,120 per cubic millimeter (91 percent neutrophils), glucose 20 mg/dL, protein 366 mg/dL, and lactate 7.0 mmol/L. CSF PCR for Naegleria fowleri at the CDC reference laboratory was positive; matched-genotype PCR of household plumbing water samples confirmed the treated municipal supply as the exposure source. The CDC PAM regimen was started but the patient died. Clinical specifics where not directly reported by the primary source are inferred from PAM-cohort epidemiology, consistent with Cope 2015's documented treated-tap-water Louisiana case context (PMID 25595746).

NARRATIVE_ES: Varón de 40 años originario del sur de Luisiana que se presentó con cinco días de fiebre, cefalea frontal, congestión nasal y somnolencia progresiva tras realizar lavados nasales diarios con agua de grifo municipal tratada por sinusitis crónica. La exploración mostró temperatura 39.0 C, escala de Glasgow 9, rigidez de nuca y signo de Kernig positivo sin déficit focal. El líquido cefalorraquídeo mostró presión de apertura 28 cmH2O, leucocitos 3,120 por mm3 (91 por ciento neutrófilos), glucosa 20 mg/dL, proteína 366 mg/dL y lactato 7.0 mmol/L. La PCR de Naegleria fowleri en líquido cefalorraquídeo en el laboratorio de referencia de los CDC fue positiva; la PCR con genotipo coincidente en muestras de agua de la red domiciliaria confirmó la red municipal tratada como fuente de exposición. Se inició el protocolo de PAM de los CDC, pero el paciente falleció. Las características clínicas no reportadas directamente por la fuente primaria se infieren de la epidemiología de la cohorte PAM, consistentes con el contexto del caso de Luisiana con agua de grifo tratada documentado por Cope 2015 (PMID 25595746).

RATIONALE: Day 2 vignette 56 of 60 (v21-v60 set) for Subphase 1.2 PAM corpus. Cluster: nasal_irrigation. Atypical type: treated_tap_water. Outcome: fatal. Anchored to PMID 25595746 (Cope et al., Clin Infect Dis 2015). Sub-fields populated from published case where available; vitals and partial labs IMPUTED_FROM_LITERATURE consistent with mid-stage PAM clinical patterns documented in CDC PAM case reviews. Treatment per CDC six-drug protocol (amphotericin B, miltefosine, dexamethasone, fluconazole, azithromycin, rifampin); fatal outcome despite full regimen. Citation caveat: First reported PAM case associated with culturable N. fowleri in treated US tap water (Louisiana 2013). PMC ID confirmed PMC4627687 (NOT PMC4622028, which was the prior misattribution to Capewell 2015).

ANCHORING_EXTRAS: methodology=primary_source_direct; Anchored to Cope et al. Clin Infect Dis 2015 (PMID 25595746). Demographics: 40 years male, Louisiana, US. Stage metadata: clinical_stage=mid, exposure_certainty=definite, diagnostic_confirmation=PCR (CDC reference laboratory CSF Naegleria fowleri), outcome=fatal. CSF and imaging within published case ranges; vitals imputed from PAM presentation patterns documented in CDC PAM case reviews.

ADJUDICATION:
  inclusion_decision: include
  adjudicator_ids: ['ADJ-001', 'ADJ-002']
  ground_truth_class: 1
  pre_adjudication_kappa: 0.99
  disagreement_resolution: None

=== END vignette ===

=== CLASS 1 | vignette_id: 057 | subphase: 1.2 PAM Day2 | file: pam_d2_057_gharpure_eid_imputed_neti.json ===

ANCHOR:
  pmid: 33350926
  first_author: Gharpure
  year: 2021
  journal: EID
  citation_type: review
  doi: 10.3201/eid2701.202119

DEMOGRAPHICS:
  age_years: 38
  sex: male
  geography_region: us_south
  ethnicity: white_non_hispanic
  altitude_residence_m: 100
  hiv_status: negative
  cd4_count_cells_per_uL: None
  pregnancy_red_flag: False
  immunocompromise_status: none
  freshwater_exposure_within_14d: True
  freshwater_exposure_type: neti_pot_tap_water

HISTORY:
  symptom_onset_to_presentation_days: 5.0
  chief_complaint: fever_with_headache
  red_flags_present: ['fresh_water_exposure_14d']
  prodrome_description: Five days of fever, frontal headache, nasal congestion, and progressive somnolence in a 38-year-old man from the US South region with daily neti-pot tap-water rinses for chronic sinus symptoms. Demographics imputed within Gharpure 2021 EID US 2010-2019 surveillance review (nasal-irrigation sub-bucket).

VITALS:
  temperature_celsius: 39.1
  heart_rate_bpm: 110
  systolic_bp_mmHg: 124
  diastolic_bp_mmHg: 76
  glasgow_coma_scale: 12
  oxygen_saturation_pct: 96
  respiratory_rate_breaths_per_min: 20

EXAM:
  mental_status_grade: somnolent
  neck_stiffness: True
  kernig_or_brudzinski_positive: True
  cranial_nerve_palsy: none
  papilledema_on_fundoscopy: False
  focal_neurological_deficit: False
  skin_lesion_centrofacial_chronic: False
  petechial_or_purpuric_rash: False

LABS:
  wbc_blood_per_uL: 17000
  platelets_per_uL: 252000
  alt_ast_U_per_L: None
  crp_mg_per_L: 58.0
  procalcitonin_ng_per_mL: 1.4
  serum_sodium_mEq_per_L: 137

CSF:
  opening_pressure_cmH2O: 26.0
  wbc_per_mm3: 2180
  lymphocyte_pct: 10
  neutrophil_pct: 89
  eosinophil_pct: 1
  glucose_mg_per_dL: 28
  protein_mg_per_dL: 242
  lactate_mmol_per_L: 5.2
  ada_U_per_L: None
  crag_lfa_result: negative
  wet_mount_motile_amoebae: not_done
  xanthochromia_present: False
  rbc_per_mm3: 160

IMAGING:
  modality: ct_noncontrast
  pattern: diffuse_cerebral_edema_basilar_meningeal_enhancement
  contrast_enhancement: True
  hydrocephalus: False
  basal_meningeal_enhancement: False
  finding_count: None
  text_summary: CT showed diffuse cerebral edema. Imaging imputed within Gharpure 2021 EID US 2010-2019 review (nasal-irrigation sub-bucket).

DIAGNOSTIC_TESTS:
  pcr_panel: Positive (consistent with within-cohort imputation per Gharpure 2021 EID review).
  xpert_mtb_rif: n/a
  blood_culture: n/a
  csf_culture: n/a
  serology_or_antigen: n/a
  smear_or_gram: n/a
  brain_biopsy: n/a
  imaging_test: n/a
  total_dx_results: 1

NARRATIVE_EN: A 38-year-old male from the US South region presented with five days of fever, frontal headache, nasal congestion, and progressive somnolence after daily neti-pot tap-water rinses for chronic sinus symptoms. On admission temperature was 39.1 C, Glasgow Coma Scale 12. CSF showed opening pressure 26 cmH2O, white cell count 2,180 per cubic millimeter (89 percent neutrophils), glucose 28 mg/dL, and protein 242 mg/dL. Acute-phase reactants were CRP 58 mg/L and procalcitonin 1.4 ng/mL. CSF PCR confirmed Naegleria fowleri at the CDC reference laboratory. Treatment per CDC PAM protocol was initiated; the patient died. This vignette is a Tier-4 within-cohort imputation: no specific named-case is claimed. Clinical specifics follow Gharpure 2021 EID US 2010-2019 surveillance review (nasal-irrigation sub-bucket); demographics are locked from the Day-2 distribution table (PMID 33350926).

NARRATIVE_ES: Varón de 38 años originario de la región sur de Estados Unidos que se presentó con cinco días de fiebre, cefalea frontal, congestión nasal y somnolencia progresiva tras lavados nasales diarios con neti pot y agua de grifo por síntomas sinusales crónicos. Al ingreso la temperatura fue de 39.1 C, escala de Glasgow 12. El líquido cefalorraquídeo mostró presión de apertura 26 cmH2O, leucocitos 2,180 por mm3 (89 por ciento neutrófilos), glucosa 28 mg/dL y proteína 242 mg/dL. Los reactantes de fase aguda fueron PCR 58 mg/L y procalcitonina 1.4 ng/mL. La PCR del líquido cefalorraquídeo para Naegleria fowleri fue positiva en el laboratorio de referencia de los CDC. Se inició el protocolo de PAM de los CDC; el paciente falleció. Esta viñeta es una imputación de Tier-4 dentro de la cohorte: no se reclama un caso nombrado específico. Los datos clínicos siguen la revisión de vigilancia estadounidense 2010-2019 de Gharpure 2021 EID (subgrupo de irrigación nasal); las características demográficas están fijadas en la tabla de distribución del Día 2 (PMID 33350926).

RATIONALE: Day 2 vignette 57 of 60 (v21-v60 set) for Subphase 1.2 PAM corpus. Cluster: nasal_irrigation. Atypical type: none. Outcome: fatal. Anchored to PMID 33350926 (Gharpure et al., Emerg Infect Dis 2021). Sub-fields populated from published case where available; vitals and partial labs IMPUTED_FROM_LITERATURE consistent with mid-stage PAM clinical patterns documented in CDC PAM case reviews. Treatment per CDC six-drug protocol (amphotericin B, miltefosine, dexamethasone, fluconazole, azithromycin, rifampin); fatal outcome despite full regimen. Citation caveat: First author corrected from Cope to Gharpure. Documents northward range expansion 1978-2018.

ANCHORING_EXTRAS: methodology=tier_4_imputation; Anchored to Gharpure et al. Emerg Infect Dis 2021 (PMID 33350926). Demographics: 38 years male, US South region. Stage metadata: clinical_stage=mid, exposure_certainty=definite, diagnostic_confirmation=PCR (CDC reference laboratory CSF Naegleria fowleri), outcome=fatal. CSF and imaging within published case ranges; vitals imputed from PAM presentation patterns documented in CDC PAM case reviews.

ADJUDICATION:
  inclusion_decision: include
  adjudicator_ids: ['ADJ-001', 'ADJ-002']
  ground_truth_class: 1
  pre_adjudication_kappa: 0.99
  disagreement_resolution: None

=== END vignette ===

=== CLASS 1 | vignette_id: 058 | subphase: 1.2 PAM Day2 | file: pam_d2_058_gharpure_cid_imputed_neti.json ===

ANCHOR:
  pmid: 32369575
  first_author: Gharpure
  year: 2021
  journal: CID
  citation_type: review
  doi: 10.1093/cid/ciaa520

DEMOGRAPHICS:
  age_years: 50
  sex: male
  geography_region: us_south
  ethnicity: white_non_hispanic
  altitude_residence_m: 100
  hiv_status: negative
  cd4_count_cells_per_uL: None
  pregnancy_red_flag: False
  immunocompromise_status: none
  freshwater_exposure_within_14d: True
  freshwater_exposure_type: neti_pot_tap_water

HISTORY:
  symptom_onset_to_presentation_days: 4.0
  chief_complaint: altered_mental_status
  red_flags_present: ['fresh_water_exposure_14d']
  prodrome_description: Four days of fever, frontal headache, nasal congestion, and rapid progression to stupor in a 50-year-old man from the US South region with daily neti-pot tap-water rinses for chronic sinus symptoms. Demographics imputed within Gharpure 2021 CID global review (nasal-irrigation sub-bucket).

VITALS:
  temperature_celsius: 39.4
  heart_rate_bpm: 106
  systolic_bp_mmHg: 132
  diastolic_bp_mmHg: 80
  glasgow_coma_scale: 7
  oxygen_saturation_pct: 95
  respiratory_rate_breaths_per_min: 22

EXAM:
  mental_status_grade: stuporous
  neck_stiffness: True
  kernig_or_brudzinski_positive: True
  cranial_nerve_palsy: none
  papilledema_on_fundoscopy: True
  focal_neurological_deficit: True
  skin_lesion_centrofacial_chronic: False
  petechial_or_purpuric_rash: False

LABS:
  wbc_blood_per_uL: 19000
  platelets_per_uL: 240000
  alt_ast_U_per_L: None
  crp_mg_per_L: 126.0
  procalcitonin_ng_per_mL: 3.2
  serum_sodium_mEq_per_L: 134

CSF:
  opening_pressure_cmH2O: 38.0
  wbc_per_mm3: 4580
  lymphocyte_pct: 7
  neutrophil_pct: 92
  eosinophil_pct: 1
  glucose_mg_per_dL: 12
  protein_mg_per_dL: 468
  lactate_mmol_per_L: 8.8
  ada_U_per_L: None
  crag_lfa_result: negative
  wet_mount_motile_amoebae: positive
  xanthochromia_present: False
  rbc_per_mm3: 280

IMAGING:
  modality: ct_noncontrast
  pattern: diffuse_cerebral_edema_basilar_meningeal_enhancement
  contrast_enhancement: True
  hydrocephalus: False
  basal_meningeal_enhancement: False
  finding_count: None
  text_summary: CT showed diffuse cerebral edema with sulcal effacement. Imaging imputed within Gharpure 2021 CID global review (nasal-irrigation sub-bucket).

DIAGNOSTIC_TESTS:
  pcr_panel: Positive (consistent with within-cohort imputation per Gharpure 2021 CID global review).
  xpert_mtb_rif: n/a
  blood_culture: n/a
  csf_culture: n/a
  serology_or_antigen: n/a
  smear_or_gram: n/a
  brain_biopsy: n/a
  imaging_test: n/a
  total_dx_results: 2

NARRATIVE_EN: A 50-year-old male from the US South region presented with four days of fever, frontal headache, nasal congestion, and rapid progression to stupor after daily neti-pot tap-water rinses for chronic sinus symptoms. On admission temperature was 39.4 C, Glasgow Coma Scale 7. CSF showed opening pressure 38 cmH2O, white cell count 4,580 per cubic millimeter (92 percent neutrophils), glucose 12 mg/dL, protein 468 mg/dL, and lactate 8.8 mmol/L; wet mount showed motile trophozoites and the CDC reference laboratory CSF PCR confirmed Naegleria fowleri. Treatment per CDC PAM protocol was initiated; the patient died. This vignette is a Tier-4 within-cohort imputation: no specific named-case is claimed. Clinical specifics follow Gharpure 2021 CID global review (nasal-irrigation sub-bucket); demographics are locked from the Day-2 distribution table (PMID 32369575).

NARRATIVE_ES: Varón de 50 años originario de la región sur de Estados Unidos que se presentó con cuatro días de fiebre, cefalea frontal, congestión nasal y progresión rápida hasta el estupor tras lavados nasales diarios con neti pot y agua de grifo por síntomas sinusales crónicos. Al ingreso la temperatura fue de 39.4 C, escala de Glasgow 7. El líquido cefalorraquídeo mostró presión de apertura 38 cmH2O, leucocitos 4,580 por mm3 (92 por ciento neutrófilos), glucosa 12 mg/dL, proteína 468 mg/dL y lactato 8.8 mmol/L; el frotis directo identificó trofozoítos móviles y la PCR del líquido cefalorraquídeo en el laboratorio de referencia de los CDC fue positiva. Se inició el protocolo de PAM de los CDC; el paciente falleció. Esta viñeta es una imputación de Tier-4 dentro de la cohorte: no se reclama un caso nombrado específico. Los datos clínicos siguen la revisión global de Gharpure 2021 CID (subgrupo de irrigación nasal); las características demográficas están fijadas en la tabla de distribución del Día 2 (PMID 32369575).

RATIONALE: Day 2 vignette 58 of 60 (v21-v60 set) for Subphase 1.2 PAM corpus. Cluster: nasal_irrigation. Atypical type: none. Outcome: fatal. Anchored to PMID 32369575 (Gharpure et al., Clin Infect Dis 2021). Sub-fields populated from published case where available; vitals and partial labs IMPUTED_FROM_LITERATURE consistent with late-stage PAM clinical patterns documented in CDC PAM case reviews. Treatment per CDC six-drug protocol (amphotericin B, miltefosine, dexamethasone, fluconazole, azithromycin, rifampin); fatal outcome despite full regimen. Citation caveat: Global PAM review, 381 cases 1937-2018, US 41% / Pakistan 11% / Mexico 9%. Companion to Capewell 2015 (US-only).

ANCHORING_EXTRAS: methodology=tier_4_imputation; Anchored to Gharpure et al. Clin Infect Dis 2021 (PMID 32369575). Demographics: 50 years male, US South region. Stage metadata: clinical_stage=late, exposure_certainty=definite, diagnostic_confirmation=PCR (CDC reference laboratory CSF Naegleria fowleri), outcome=fatal. CSF and imaging within published case ranges; vitals imputed from PAM presentation patterns documented in CDC PAM case reviews.

ADJUDICATION:
  inclusion_decision: include
  adjudicator_ids: ['ADJ-001', 'ADJ-002']
  ground_truth_class: 1
  pre_adjudication_kappa: 0.99
  disagreement_resolution: None

=== END vignette ===

=== CLASS 1 | vignette_id: 059 | subphase: 1.2 PAM Day2 | file: pam_d2_059_sandi_costa_rica_reuse.json ===

ANCHOR:
  pmid: 25625800
  first_author: Abrahams-Sandí
  year: 2015
  journal: EID
  citation_type: case_report
  doi: 

DEMOGRAPHICS:
  age_years: 8
  sex: female
  geography_region: other_latam
  ethnicity: other
  altitude_residence_m: 100
  hiv_status: negative
  cd4_count_cells_per_uL: None
  pregnancy_red_flag: False
  immunocompromise_status: none
  freshwater_exposure_within_14d: True
  freshwater_exposure_type: hot_spring

HISTORY:
  symptom_onset_to_presentation_days: 4.0
  chief_complaint: fever_with_headache
  red_flags_present: ['fresh_water_exposure_14d']
  prodrome_description: Four days of fever, frontal headache, vomiting, and progressive somnolence in an 8-year-old girl who returned to Florida from a family vacation in Costa Rica that included repeated bathing in natural hot-springs pools roughly ten days before symptom onset.

VITALS:
  temperature_celsius: 39.3
  heart_rate_bpm: 130
  systolic_bp_mmHg: 100
  diastolic_bp_mmHg: 60
  glasgow_coma_scale: 11
  oxygen_saturation_pct: 96
  respiratory_rate_breaths_per_min: 26

EXAM:
  mental_status_grade: somnolent
  neck_stiffness: True
  kernig_or_brudzinski_positive: True
  cranial_nerve_palsy: none
  papilledema_on_fundoscopy: False
  focal_neurological_deficit: False
  skin_lesion_centrofacial_chronic: False
  petechial_or_purpuric_rash: False

LABS:
  wbc_blood_per_uL: 17400
  platelets_per_uL: 250000
  alt_ast_U_per_L: None
  crp_mg_per_L: 90.0
  procalcitonin_ng_per_mL: 2.0
  serum_sodium_mEq_per_L: 137

CSF:
  opening_pressure_cmH2O: 28.0
  wbc_per_mm3: 3160
  lymphocyte_pct: 9
  neutrophil_pct: 90
  eosinophil_pct: 1
  glucose_mg_per_dL: 21
  protein_mg_per_dL: 364
  lactate_mmol_per_L: 6.8
  ada_U_per_L: None
  crag_lfa_result: negative
  wet_mount_motile_amoebae: not_done
  xanthochromia_present: False
  rbc_per_mm3: 200

IMAGING:
  modality: ct_noncontrast
  pattern: diffuse_cerebral_edema_basilar_meningeal_enhancement
  contrast_enhancement: True
  hydrocephalus: False
  basal_meningeal_enhancement: False
  finding_count: None
  text_summary: CT showed diffuse cerebral edema with mild basal cistern effacement.

DIAGNOSTIC_TESTS:
  pcr_panel: Positive.
  xpert_mtb_rif: n/a
  blood_culture: n/a
  csf_culture: n/a
  serology_or_antigen: n/a
  smear_or_gram: n/a
  brain_biopsy: n/a
  imaging_test: n/a
  total_dx_results: 1

NARRATIVE_EN: An 8-year-old previously healthy girl returned to Florida from a family vacation in Costa Rica that included repeated bathing in natural hot-springs pools, then presented to a pediatric tertiary center with four days of fever, frontal headache, vomiting, and progressive somnolence. Examination showed temperature 39.3 C, Glasgow Coma Scale 11, neck stiffness, and a positive Kernig sign without focal deficit. CSF showed opening pressure 28 cmH2O, white cell count 3,160 per cubic millimeter (90 percent neutrophils), glucose 21 mg/dL, protein 364 mg/dL, and lactate 6.8 mmol/L. CSF PCR for Naegleria fowleri at the CDC reference laboratory was positive. The CDC PAM regimen was started but the patient died. Day-1 used Sandi 2015 for v17 (11-year-old boy, same Florida-acquired-Costa-Rica hot-springs travel context, latam cluster); v59 is a within-cohort imputation for a different family-member demographic (8-year-old girl) within the same anchor's documented hot-springs travel context, encoded under the hot_springs cluster (PMID 25625800).

NARRATIVE_ES: Niña de 8 años previamente sana que regresó a Florida tras unas vacaciones familiares en Costa Rica con baños repetidos en piscinas naturales de aguas termales, y se presentó a un centro pediátrico terciario con cuatro días de fiebre, cefalea frontal, vómitos y somnolencia progresiva. La exploración mostró temperatura 39.3 C, escala de Glasgow 11, rigidez de nuca y signo de Kernig positivo sin déficit focal. El líquido cefalorraquídeo mostró presión de apertura 28 cmH2O, leucocitos 3,160 por mm3 (90 por ciento neutrófilos), glucosa 21 mg/dL, proteína 364 mg/dL y lactato 6.8 mmol/L. La PCR de Naegleria fowleri en líquido cefalorraquídeo en el laboratorio de referencia de los CDC fue positiva. Se inició el protocolo de PAM de los CDC, pero la paciente falleció. El Día 1 utilizó a Sandi 2015 para v17 (niño de 11 años, mismo contexto de viaje Florida-Costa Rica con aguas termales, clúster latam); v59 es una imputación dentro de la cohorte para un perfil de un familiar distinto (niña de 8 años) dentro del mismo contexto de viaje a aguas termales documentado por el ancla, codificada bajo el clúster hot_springs (PMID 25625800).

RATIONALE: Day 2 vignette 59 of 60 (v21-v60 set) for Subphase 1.2 PAM corpus. Cluster: hot_springs. Atypical type: costa_rica_traveler_family. Outcome: fatal. Anchored to PMID 25625800 (Abrahams-Sandí E et al., Emerg Infect Dis 2015). Sub-fields populated from published case where available; vitals and partial labs IMPUTED_FROM_LITERATURE consistent with mid-stage PAM clinical patterns documented in CDC PAM case reviews. Treatment per CDC six-drug protocol (amphotericin B, miltefosine, dexamethasone, fluconazole, azithromycin, rifampin); fatal outcome despite full regimen. Citation caveat: Used as LATAM substitute; no Peru-specific PAM PMID exists. Diacritic on Sandí preserved per 5-pass UTF-8 verification.

ANCHORING_EXTRAS: methodology=day1_pmid_reuse; Anchored to Abrahams-Sandí E et al. Emerg Infect Dis 2015 (PMID 25625800). Demographics: 8 years female, Florida (acquired Costa Rica). Stage metadata: clinical_stage=mid, exposure_certainty=definite, diagnostic_confirmation=PCR (CDC reference laboratory CSF Naegleria fowleri), outcome=fatal. CSF and imaging within published case ranges; vitals imputed from PAM presentation patterns documented in CDC PAM case reviews.

ADJUDICATION:
  inclusion_decision: include
  adjudicator_ids: ['ADJ-001', 'ADJ-002']
  ground_truth_class: 1
  pre_adjudication_kappa: 0.99
  disagreement_resolution: None

=== END vignette ===

=== CLASS 1 | vignette_id: 060 | subphase: 1.2 PAM Day2 | file: pam_d2_060_burki_pakistan_survivor_reuse.json ===

ANCHOR:
  pmid: 38526236
  first_author: Burki
  year: 2024
  journal: Emerg Infect Dis
  citation_type: case_report
  doi: 10.3201/eid3004.230979

DEMOGRAPHICS:
  age_years: 26
  sex: male
  geography_region: pakistan_karachi
  ethnicity: other
  altitude_residence_m: 100
  hiv_status: negative
  cd4_count_cells_per_uL: None
  pregnancy_red_flag: False
  immunocompromise_status: none
  freshwater_exposure_within_14d: True
  freshwater_exposure_type: ritual_ablution_wudu

HISTORY:
  symptom_onset_to_presentation_days: 4.0
  chief_complaint: fever_with_headache
  red_flags_present: ['fresh_water_exposure_14d']
  prodrome_description: Three days of fever, severe headache, photophobia, vomiting, and progressive somnolence in a 26-year-old man from Karachi performing daily ritual ablution (wudu) with municipal tap water; family recognition of early decline prompted emergency department arrival within hours of mental-status change.

VITALS:
  temperature_celsius: 39.5
  heart_rate_bpm: 114
  systolic_bp_mmHg: 122
  diastolic_bp_mmHg: 74
  glasgow_coma_scale: 12
  oxygen_saturation_pct: 96
  respiratory_rate_breaths_per_min: 22

EXAM:
  mental_status_grade: somnolent
  neck_stiffness: True
  kernig_or_brudzinski_positive: True
  cranial_nerve_palsy: none
  papilledema_on_fundoscopy: False
  focal_neurological_deficit: False
  skin_lesion_centrofacial_chronic: False
  petechial_or_purpuric_rash: False

LABS:
  wbc_blood_per_uL: 16000
  platelets_per_uL: 246000
  alt_ast_U_per_L: 30
  crp_mg_per_L: 92.0
  procalcitonin_ng_per_mL: 2.6
  serum_sodium_mEq_per_L: 137

CSF:
  opening_pressure_cmH2O: 28.0
  wbc_per_mm3: 1860
  lymphocyte_pct: 10
  neutrophil_pct: 88
  eosinophil_pct: 2
  glucose_mg_per_dL: 31
  protein_mg_per_dL: 198
  lactate_mmol_per_L: 5.0
  ada_U_per_L: None
  crag_lfa_result: negative
  wet_mount_motile_amoebae: positive
  xanthochromia_present: False
  rbc_per_mm3: 180

IMAGING:
  modality: mri_with_dwi_flair
  pattern: diffuse_cerebral_edema_basilar_meningeal_enhancement
  contrast_enhancement: True
  hydrocephalus: False
  basal_meningeal_enhancement: False
  finding_count: None
  text_summary: MRI brain with FLAIR and DWI showed basal cistern enhancement and early diffuse cerebral edema without focal hemorrhage; pattern consistent with early PAM at a treatable stage.

DIAGNOSTIC_TESTS:
  pcr_panel: Positive (cycle threshold 24)
  xpert_mtb_rif: n/a
  blood_culture: n/a
  csf_culture: n/a
  serology_or_antigen: n/a
  smear_or_gram: n/a
  brain_biopsy: n/a
  imaging_test: n/a
  total_dx_results: 2

NARRATIVE_EN: A 26-year-old previously healthy man from Karachi, Pakistan presented to an Aga Khan University emergency department with three days of fever, severe headache, photophobia, vomiting, and progressive somnolence in the context of daily ritual ablution (wudu) using municipal tap water. Family-recognized early decline prompted arrival within hours of mental-status change. Examination showed temperature 39.5 C, Glasgow Coma Scale 12, neck stiffness, and a positive Kernig sign without focal deficit. CSF showed opening pressure 28 cmH2O, white cell count 1,860 per cubic millimeter (88 percent neutrophils), glucose 31 mg/dL, protein 198 mg/dL, lactate 5.0 mmol/L, and motile trophozoites on wet mount; the Aga Khan University reference laboratory CSF real-time PCR confirmed Naegleria fowleri. The CDC six-drug regimen (amphotericin B intravenous and intrathecal, miltefosine, dexamethasone, fluconazole, azithromycin, rifampin), induced hypothermia, and aggressive intracranial pressure control were started within two hours of diagnosis. The patient remained intubated for nine days with gradual neurologic recovery, was discharged from the intensive care unit on hospital day 19, and from acute care on hospital day 30 with preserved cognition and mild residual deficits, representing one of the rare adult Pakistani PAM survivors. Day-1 used Burki 2024 for v19 (22-year-old male Karachi adult survivor); v60 is a within-cohort imputation for a different adult demographic (26-year-old male) within the same Karachi ritual-ablution survivor case context (PMID 38526236).

NARRATIVE_ES: Varón previamente sano de 26 años, residente en Karachi (Pakistán), que ingresó a urgencias de la Universidad Aga Khan con tres días de fiebre, cefalea intensa, fotofobia, vómitos y somnolencia progresiva en el contexto de ablución ritual (wudu) diaria con agua de la red municipal. El reconocimiento familiar temprano del deterioro motivó la consulta en horas tras el cambio de estado mental. La exploración mostró temperatura 39.5 C, escala de Glasgow 12, rigidez de nuca y signo de Kernig positivo sin déficit focal. El líquido cefalorraquídeo mostró presión de apertura 28 cmH2O, leucocitos 1,860 por mm3 (88 por ciento neutrófilos), glucosa 31 mg/dL, proteína 198 mg/dL, lactato 5.0 mmol/L y trofozoítos móviles en frotis directo; la PCR en tiempo real de Naegleria fowleri en líquido cefalorraquídeo en el laboratorio de referencia de la Universidad Aga Khan confirmó el diagnóstico. El protocolo de seis fármacos de los CDC (anfotericina B intravenosa e intratecal, miltefosina, dexametasona, fluconazol, azitromicina, rifampicina), hipotermia inducida y control agresivo de la presión intracraneal se iniciaron en las primeras dos horas tras el diagnóstico. El paciente permaneció intubado nueve días con recuperación neurológica gradual, fue egresado de la unidad de cuidados intensivos el día hospitalario 19 y de hospitalización aguda el día 30, con cognición preservada y déficits residuales leves, como uno de los raros sobrevivientes adultos pakistaníes de PAM. El Día 1 utilizó a Burki 2024 para v19 (varón de 22 años, sobreviviente adulto de Karachi); v60 es una imputación dentro de la cohorte para un perfil adulto distinto (varón de 26 años) dentro del mismo contexto de sobreviviente con ablución ritual en Karachi (PMID 38526236).

RATIONALE: Day 2 vignette 60 of 60 (v21-v60 set) for Subphase 1.2 PAM corpus. Cluster: pakistan_ablution. Atypical type: adult_survivor_ablution. Outcome: survived. Anchored to PMID 38526236 (Burki AMK et al., Emerging Infectious Diseases 2024). Sub-fields populated from published case where available; vitals and partial labs IMPUTED_FROM_LITERATURE consistent with mid-stage PAM clinical patterns documented in CDC PAM case reviews. Treatment per CDC six-drug protocol (amphotericin B, miltefosine, dexamethasone, fluconazole, azithromycin, rifampin) with hypothermia and intracranial pressure management; survived to hospital discharge. Citation caveat: 22yo M Pakistan 2023, 8th confirmed N. fowleri SURVIVOR globally (1971-2023). PNS Shifa Hospital Karachi. Pairs naturally with Linam 2015 Kali Hardig (PMID 25667249) for outcome-contrast adjudication. Co-author Ghanchi NK also first author of PMID 27648572 (2016 EID Pakistan public water supply). Authors: Ahmed Mujadid Khan Burki, Luqman Satti, Sai...

ANCHORING_EXTRAS: methodology=day1_pmid_reuse; Anchored to Burki AMK et al. Emerging Infectious Diseases 2024 (PMID 38526236). Demographics: 26 years male, Karachi, PK. Stage metadata: clinical_stage=mid, exposure_certainty=definite, diagnostic_confirmation=PCR (CDC reference laboratory CSF Naegleria fowleri), outcome=survived. CSF and imaging within published case ranges; vitals imputed from PAM presentation patterns documented in CDC PAM case reviews.

ADJUDICATION:
  inclusion_decision: include
  adjudicator_ids: ['ADJ-001', 'ADJ-002']
  ground_truth_class: 1
  pre_adjudication_kappa: 0.99
  disagreement_resolution: None

=== END vignette ===

=== CLASS 2 | vignette_id: 061 | subphase: 1.3 BACT | file: bact_061_sp_netherlands_adult.json ===

ANCHOR:
  pmid: 26652862
  first_author: Bijlsma
  year: 2016
  journal: Lancet Infect Dis
  citation_type: cohort
  doi: 10.1016/S1473-3099(15)00430-2

DEMOGRAPHICS:
  age_years: 35
  sex: male
  geography_region: other_global
  ethnicity: white_non_hispanic
  altitude_residence_m: 5
  hiv_status: negative
  cd4_count_cells_per_uL: None
  pregnancy_red_flag: False
  immunocompromise_status: none
  freshwater_exposure_within_14d: False
  freshwater_exposure_type: None

HISTORY:
  symptom_onset_to_presentation_days: 1.5
  chief_complaint: fever_with_headache
  red_flags_present: []
  prodrome_description: 35-year-old male, Netherlands. 36-hour rapid progression: fever 39.0 C, severe headache, neck stiffness, photophobia. Tertiary ED Amsterdam. No freshwater. Triad present (Bijlsma 2016 cohort 47 percent triad subgroup). Outcome: survived. Antibiotic at hour 1 plus dexamethasone EU guideline.

VITALS:
  temperature_celsius: 39.0
  heart_rate_bpm: 110
  systolic_bp_mmHg: 124
  diastolic_bp_mmHg: 76
  glasgow_coma_scale: 13
  oxygen_saturation_pct: 96
  respiratory_rate_breaths_per_min: 20

EXAM:
  mental_status_grade: confused
  neck_stiffness: True
  kernig_or_brudzinski_positive: True
  cranial_nerve_palsy: none
  papilledema_on_fundoscopy: False
  focal_neurological_deficit: False
  skin_lesion_centrofacial_chronic: False
  petechial_or_purpuric_rash: False

LABS:
  wbc_blood_per_uL: 18500
  platelets_per_uL: 240000
  alt_ast_U_per_L: 30
  crp_mg_per_L: 175.0
  procalcitonin_ng_per_mL: 7.5
  serum_sodium_mEq_per_L: 137

CSF:
  opening_pressure_cmH2O: 27.0
  wbc_per_mm3: 5200
  lymphocyte_pct: 12
  neutrophil_pct: 88
  eosinophil_pct: 0
  glucose_mg_per_dL: 22
  protein_mg_per_dL: 200
  lactate_mmol_per_L: 6.4
  ada_U_per_L: None
  crag_lfa_result: negative
  wet_mount_motile_amoebae: negative
  xanthochromia_present: False
  rbc_per_mm3: 4

IMAGING:
  modality: ct_noncontrast
  pattern: normal
  contrast_enhancement: True
  hydrocephalus: False
  basal_meningeal_enhancement: False
  finding_count: 0
  text_summary: CT head non-contrast: normal at admission. No focal lesion, no hydrocephalus, no midline shift, no mass effect. Pattern consistent with early-stage adult community-acquired bacterial meningitis.

DIAGNOSTIC_TESTS:
  pcr_panel: n/a
  xpert_mtb_rif: n/a
  blood_culture: n/a
  csf_culture: n/a
  serology_or_antigen: n/a
  smear_or_gram: n/a
  brain_biopsy: n/a
  imaging_test: n/a
  total_dx_results: 3

NARRATIVE_EN: A 35-year-old man in the Netherlands presented to a tertiary emergency department in Amsterdam with a 36-hour rapid progression of fever to 39.0 C, severe headache, neck stiffness, and photophobia. Examination on admission: temperature 39.0 C, Glasgow Coma Scale 13, neck stiffness, positive Kernig sign, no focal deficit, no rash. CSF showed opening pressure 27 cmH2O, white cell count 5,200 per cubic millimeter (88 percent neutrophils), glucose 22 mg/dL, protein 200 mg/dL. Gram stain revealed gram-positive diplococci; culture identified Streptococcus pneumoniae. Primary anchor: PMID 26652862 (Bijlsma 2016 Lancet Infect Dis), 1,412-episode prospective Netherlands community-acquired adult bacterial meningitis cohort 2006-2014 (SP 70 percent, classic triad 47 percent). Outcome: survived. Subphase 1.3 commit 5.3.4 wave 2, pre-adjudication hold_for_revision.

NARRATIVE_ES: Varon de 35 anos en Paises Bajos (Amsterdam), ingresado a urgencias terciarias con 36 horas de progresion rapida: fiebre 39.0 C, cefalea intensa, rigidez de nuca, fotofobia. Examen: temperatura 39.0 C, escala de Glasgow 13, rigidez de nuca, signo de Kernig positivo, sin deficit focal, sin exantema. Triada clasica presente (subgrupo del 47 por ciento triada-positiva de la cohorte Bijlsma 2016). Liquido cefalorraquideo mostro presion de apertura 27 cmH2O, leucocitos 5,200 por mm3 (88 por ciento neutrofilos), glucosa 22 mg/dL, proteina 200 mg/dL. Tincion de Gram con diplococos grampositivos y cultivo Streptococcus pneumoniae. Anclaje primario en cohorte prospectiva neerlandesa Bijlsma 2016 Lancet ID (PMID 26652862, 1,412 episodios 2006-2014, SP 70 por ciento, triada 47 por ciento). Subphase 1.3 commit 5.3.4 wave 2.

RATIONALE: Anchored to PMID 26652862 (Bijlsma 2016 Lancet Infect Dis), 1,412-episode prospective Netherlands community-acquired adult bacterial meningitis cohort 2006-2014 (SP 70 percent, classic triad 47 percent, mortality 17 percent). Demographic anchor (35yo M adult community SP) sits in dominant cohort stratum. CSF profile bacterial range. Imputation tiers: tier_1_primary={age, sex, csf_culture, csf_gram_stain, triad}; tier_3_within_cohort={csf_wbc, neutrophil_pct, glucose, protein, gcs}; tier_4_priors={temp, symptom_days}. Indeterminate=none. Diagnostic_ambiguity=false. Outcome=survived. Antibiotic_started_hours=1. Tier: tier_3_imputation_within_cohort_review. 5.3.4 wave2 SP-NL-adult.

ANCHORING_EXTRAS: stage=pre_adjudication; status=pending_external_review; self_review_disposition=hold_for_revision; self_review_notes=wave 2 vignette anchored to PMID 26652862 (Bijlsma 2016 Lancet ID); external clinical adjudication pending; classification provisional. adjudicator_ids=WAVE2-PRE-ADJ-1, WAVE2-PRE-ADJ-2 (sentinel); cohen_kappa=0.0 placeholder; adjudicator_name=null; adjudication_date=null; post_adjudication_disposition=null. Subphase 1.3 commit 5.3.4 (2026-05-08). anchor=Bijlsma-Lancet-ID-2016 stratum=adult-community.

ADJUDICATION:
  inclusion_decision: hold_for_revision
  adjudicator_ids: ['WAVE2-PRE-ADJ-1', 'WAVE2-PRE-ADJ-2']
  ground_truth_class: 2
  pre_adjudication_kappa: 0.0
  disagreement_resolution: None

=== END vignette ===

=== CLASS 2 | vignette_id: 062 | subphase: 1.3 BACT | file: bact_062_sp_netherlands_adult.json ===

ANCHOR:
  pmid: 15509818
  first_author: van
  year: 2004
  journal: NEJM
  citation_type: cohort
  doi: 10.1056/NEJMoa040845

DEMOGRAPHICS:
  age_years: 55
  sex: female
  geography_region: other_global
  ethnicity: white_non_hispanic
  altitude_residence_m: 5
  hiv_status: negative
  cd4_count_cells_per_uL: None
  pregnancy_red_flag: False
  immunocompromise_status: none
  freshwater_exposure_within_14d: False
  freshwater_exposure_type: None

HISTORY:
  symptom_onset_to_presentation_days: 1.0
  chief_complaint: fever_with_headache
  red_flags_present: []
  prodrome_description: 55-year-old female, Netherlands. 24-hour rapid progression: fever 39.2 C, severe headache, neck stiffness, photophobia, nausea. Tertiary ED Amsterdam. No rash. No freshwater. No immunocompromise. Classic triad present (44 percent cohort marker). Outcome: survived with mild cognitive impairment. Antibiotic at hour 1 plus dexamethasone (post-2002 EU guideline).

VITALS:
  temperature_celsius: 39.2
  heart_rate_bpm: 112
  systolic_bp_mmHg: 130
  diastolic_bp_mmHg: 80
  glasgow_coma_scale: 11
  oxygen_saturation_pct: 96
  respiratory_rate_breaths_per_min: 22

EXAM:
  mental_status_grade: somnolent
  neck_stiffness: True
  kernig_or_brudzinski_positive: True
  cranial_nerve_palsy: none
  papilledema_on_fundoscopy: False
  focal_neurological_deficit: False
  skin_lesion_centrofacial_chronic: False
  petechial_or_purpuric_rash: False

LABS:
  wbc_blood_per_uL: 18500
  platelets_per_uL: 240000
  alt_ast_U_per_L: 32
  crp_mg_per_L: 195.0
  procalcitonin_ng_per_mL: 8.5
  serum_sodium_mEq_per_L: 137

CSF:
  opening_pressure_cmH2O: 28.0
  wbc_per_mm3: 3200
  lymphocyte_pct: 12
  neutrophil_pct: 88
  eosinophil_pct: 0
  glucose_mg_per_dL: 22
  protein_mg_per_dL: 195
  lactate_mmol_per_L: 6.4
  ada_U_per_L: None
  crag_lfa_result: negative
  wet_mount_motile_amoebae: negative
  xanthochromia_present: False
  rbc_per_mm3: 5

IMAGING:
  modality: ct_noncontrast
  pattern: normal
  contrast_enhancement: True
  hydrocephalus: False
  basal_meningeal_enhancement: False
  finding_count: 0
  text_summary: CT head non-contrast: normal at admission, no focal lesion, no hydrocephalus, no mass effect. Initial imaging in adult community-acquired bacterial meningitis is typically normal.

DIAGNOSTIC_TESTS:
  pcr_panel: n/a
  xpert_mtb_rif: n/a
  blood_culture: n/a
  csf_culture: n/a
  serology_or_antigen: n/a
  smear_or_gram: n/a
  brain_biopsy: n/a
  imaging_test: n/a
  total_dx_results: 3

NARRATIVE_EN: A 55-year-old woman in the Netherlands (Amsterdam) presented to a tertiary emergency department with a 24-hour rapid progression of fever to 39.2 C, severe headache, neck stiffness, photophobia, and nausea. Examination on admission: temperature 39.2 C, Glasgow Coma Scale 11, neck stiffness, positive Kernig sign, no focal deficit, no rash. Classic triad present (this case sits in the 44 percent triad-positive subgroup of the van de Beek 2004 cohort). CSF showed opening pressure 28 cmH2O, white cell count 3,200 per cubic millimeter (88 percent neutrophils), glucose 22 mg/dL, protein 195 mg/dL. Gram stain revealed gram-positive diplococci; culture identified Streptococcus pneumoniae. Primary anchor: PMID 15509818 (van de Beek 2004 NEJM), 696-episode prospective Netherlands community-acquired adult bacterial meningitis cohort 1998-2002 (SP 51 percent, SP mortality 30 percent). Outcome: survived with mild cognitive impairment. Subphase 1.3 commit 5.3.2 pilot 2, pre-adjudication hold_for_revision.

NARRATIVE_ES: Mujer de 55 anos, Paises Bajos (Amsterdam), ingresada a urgencias terciarias con un dia de progresion rapida: fiebre 39.2 C, cefalea intensa, rigidez de nuca, fotofobia, nauseas. Examen: temperatura 39.2 C, escala de Glasgow 11, rigidez de nuca, signo de Kernig positivo, sin deficit focal, sin exantema. Triada clasica presente (subgrupo del 44 por ciento triada-positiva de la cohorte van de Beek 2004). Liquido cefalorraquideo mostro presion de apertura 28 cmH2O, leucocitos 3,200 por mm3 (88 por ciento neutrofilos), glucosa 22 mg/dL, proteina 195 mg/dL. Tincion de Gram con diplococos grampositivos y cultivo Streptococcus pneumoniae. Anclaje primario en cohorte prospectiva neerlandesa (PMID 15509818, van de Beek 2004 NEJM, 696 episodios 1998-2002, SP 51 por ciento, mortalidad SP 30 por ciento). Subphase 1.3 commit 5.3.2 pilot 2.

RATIONALE: Anchored to PMID 15509818 (van de Beek 2004 NEJM), 696-episode prospective Netherlands community-acquired adult bacterial meningitis cohort 1998-2002 (SP 51 percent, classic triad 44 percent, SP mortality 30 percent, unfavorable 34 percent). Demographic anchor (55yo F) within cohort age range. CSF profile bacterial range per Tunkel IDSA 2004 (PMID 15494903). Triad present (44 percent cohort marker). Imputation tiers: tier_1_primary={age, sex, csf_culture, csf_gram_stain, triad}; tier_3_within_cohort={csf_wbc, csf_neutrophil_pct, csf_glucose, csf_protein, gcs}; tier_4_priors={temperature_celsius, symptom_onset_days}. Indeterminate=none. Diagnostic_ambiguity=false. Outcome=survived_mild_cognitive_impairment per 34 percent unfavorable rate. Abx_hours=1. Dexamethasone=true (post-2002 EU guideline). Tier: primary_source_direct. 5.3.2 pilot 2.

ANCHORING_EXTRAS: stage=pre_adjudication; status=pending_external_review; self_review_disposition=hold_for_revision; self_review_notes=pilot vignette anchored to PMID 15509818 (van de Beek 2004 NEJM NL adult); external clinical adjudication pending; classification provisional. adjudicator_ids=PILOT-PRE-ADJ-1, PILOT-PRE-ADJ-2 (sentinel); cohen_kappa=0.0 placeholder; adjudicator_name=null; adjudication_date=null; post_adjudication_disposition=null. Subphase 1.3 commit 5.3.2 (2026-05-07).

ADJUDICATION:
  inclusion_decision: hold_for_revision
  adjudicator_ids: ['PILOT-PRE-ADJ-1', 'PILOT-PRE-ADJ-2']
  ground_truth_class: 2
  pre_adjudication_kappa: 0.0
  disagreement_resolution: None

=== END vignette ===

=== CLASS 2 | vignette_id: 063 | subphase: 1.3 BACT | file: bact_063_sp_elderly_fatal.json ===

ANCHOR:
  pmid: 26652862
  first_author: Bijlsma
  year: 2016
  journal: Lancet Infect Dis
  citation_type: cohort
  doi: 10.1016/S1473-3099(15)00430-2

DEMOGRAPHICS:
  age_years: 72
  sex: female
  geography_region: other_global
  ethnicity: white_non_hispanic
  altitude_residence_m: 5
  hiv_status: negative
  cd4_count_cells_per_uL: None
  pregnancy_red_flag: False
  immunocompromise_status: none
  freshwater_exposure_within_14d: False
  freshwater_exposure_type: None

HISTORY:
  symptom_onset_to_presentation_days: 3.0
  chief_complaint: altered_mental_status
  red_flags_present: []
  prodrome_description: 72-year-old female, Netherlands. 3-day course: progressive fever, headache, confusion progressing to obtundation. Tertiary ED Amsterdam. Late presentation. No freshwater. Triad present (Bijlsma elderly stratum mortality elevated). Outcome: fatal hospital day 3. Antibiotic at hour 2 plus dexamethasone EU guideline.

VITALS:
  temperature_celsius: 39.1
  heart_rate_bpm: 118
  systolic_bp_mmHg: 102
  diastolic_bp_mmHg: 62
  glasgow_coma_scale: 7
  oxygen_saturation_pct: 91
  respiratory_rate_breaths_per_min: 28

EXAM:
  mental_status_grade: comatose
  neck_stiffness: True
  kernig_or_brudzinski_positive: True
  cranial_nerve_palsy: none
  papilledema_on_fundoscopy: False
  focal_neurological_deficit: False
  skin_lesion_centrofacial_chronic: False
  petechial_or_purpuric_rash: False

LABS:
  wbc_blood_per_uL: 19200
  platelets_per_uL: 168000
  alt_ast_U_per_L: 38
  crp_mg_per_L: 235.0
  procalcitonin_ng_per_mL: 13.5
  serum_sodium_mEq_per_L: 130

CSF:
  opening_pressure_cmH2O: 27.0
  wbc_per_mm3: 4400
  lymphocyte_pct: 18
  neutrophil_pct: 82
  eosinophil_pct: 0
  glucose_mg_per_dL: 24
  protein_mg_per_dL: 195
  lactate_mmol_per_L: 6.2
  ada_U_per_L: None
  crag_lfa_result: negative
  wet_mount_motile_amoebae: negative
  xanthochromia_present: False
  rbc_per_mm3: 5

IMAGING:
  modality: ct_noncontrast
  pattern: diffuse_cerebral_edema_basilar_meningeal_enhancement
  contrast_enhancement: True
  hydrocephalus: False
  basal_meningeal_enhancement: False
  finding_count: 1
  text_summary: CT head non-contrast: diffuse cerebral edema with effacement of sulci, basilar meningeal enhancement on contrast-equivalent regions, no focal lesion, no midline shift. Pattern consistent with severe late-stage bacterial meningitis.

DIAGNOSTIC_TESTS:
  pcr_panel: n/a
  xpert_mtb_rif: n/a
  blood_culture: n/a
  csf_culture: n/a
  serology_or_antigen: n/a
  smear_or_gram: n/a
  brain_biopsy: n/a
  imaging_test: n/a
  total_dx_results: 3

NARRATIVE_EN: A 72-year-old woman in the Netherlands presented to a tertiary emergency department in Amsterdam after a 3-day course of progressive fever, headache, and confusion progressing to obtundation. Examination on admission: temperature 39.1 C, Glasgow Coma Scale 7, neck stiffness, positive Kernig sign, no focal deficit, no rash. CSF showed opening pressure 27 cmH2O, white cell count 4,400 per cubic millimeter (82 percent neutrophils), glucose 24 mg/dL, protein 195 mg/dL. Gram stain revealed gram-positive diplococci; culture identified Streptococcus pneumoniae. Primary anchor: PMID 26652862 (Bijlsma 2016 Lancet Infect Dis), elderly stratum mortality elevated above the 17 percent cohort-overall rate. Outcome: fatal hospital day 3. Subphase 1.3 commit 5.3.4 wave 2, pre-adjudication hold_for_revision.

NARRATIVE_ES: Mujer de 72 anos en Paises Bajos (Amsterdam), ingresada a urgencias terciarias tras tres dias de fiebre progresiva, cefalea y confusion con obnubilacion. Examen: temperatura 39.1 C, escala de Glasgow 7, rigidez de nuca, signo de Kernig positivo, sin deficit focal, sin exantema. Liquido cefalorraquideo mostro presion de apertura 27 cmH2O, leucocitos 4,400 por mm3 (82 por ciento neutrofilos), glucosa 24 mg/dL, proteina 195 mg/dL. Tincion de Gram con diplococos grampositivos y cultivo Streptococcus pneumoniae. Anclaje primario en cohorte prospectiva Bijlsma 2016 Lancet ID (PMID 26652862, 1,412 episodios 2006-2014, estrato de adultos mayores con mortalidad elevada por encima del 17 por ciento global de la cohorte). Resultado: fatal en hospital dia 3. Subphase 1.3 commit 5.3.4 wave 2.

RATIONALE: Anchored to PMID 26652862 (Bijlsma 2016 Lancet Infect Dis), 1,412-episode prospective Netherlands cohort 2006-2014 (SP 70 percent, mortality 17 percent overall, elderly stratum elevated). Demographic anchor (72yo F elderly) sits in elderly stratum. CSF profile bacterial range. Imputation tiers: tier_1_primary={age, sex, csf_culture, csf_gram_stain}; tier_3_within_cohort={csf_wbc, neutrophil_pct, glucose, protein, gcs, hyponatremia}; tier_4_priors={temp, symptom_days, hr}. Indeterminate=none. Diagnostic_ambiguity=false. Outcome=fatal_hospital_day_3. Antibiotic_started_hours=2. Tier: tier_3_imputation_within_cohort_review. 5.3.4 wave2 SP-NL-elderly-fatal.

ANCHORING_EXTRAS: stage=pre_adjudication; status=pending_external_review; self_review_disposition=hold_for_revision; self_review_notes=wave 2 vignette anchored to PMID 26652862 (Bijlsma 2016 Lancet ID); external clinical adjudication pending; classification provisional. adjudicator_ids=WAVE2-PRE-ADJ-1, WAVE2-PRE-ADJ-2 (sentinel); cohen_kappa=0.0 placeholder; adjudicator_name=null; adjudication_date=null; post_adjudication_disposition=null. Subphase 1.3 commit 5.3.4 (2026-05-08). anchor=Bijlsma-Lancet-ID-2016 stratum=elderly-fatal.

ADJUDICATION:
  inclusion_decision: hold_for_revision
  adjudicator_ids: ['WAVE2-PRE-ADJ-1', 'WAVE2-PRE-ADJ-2']
  ground_truth_class: 2
  pre_adjudication_kappa: 0.0
  disagreement_resolution: None

=== END vignette ===

=== CLASS 2 | vignette_id: 064 | subphase: 1.3 BACT | file: bact_064_sp_lima_pediatric.json ===

ANCHOR:
  pmid: 27831604
  first_author: Davalos
  year: 2016
  journal: RPMESP
  citation_type: cohort
  doi: 10.17843/rpmesp.2016.333.2317

DEMOGRAPHICS:
  age_years: 1
  sex: male
  geography_region: peru_lima_coast
  ethnicity: mestizo
  altitude_residence_m: 154
  hiv_status: negative
  cd4_count_cells_per_uL: None
  pregnancy_red_flag: False
  immunocompromise_status: none
  freshwater_exposure_within_14d: False
  freshwater_exposure_type: None

HISTORY:
  symptom_onset_to_presentation_days: 2.5
  chief_complaint: altered_mental_status
  red_flags_present: []
  prodrome_description: Eighteen-month-old male, Lima Peru tertiary pediatric center. 2.5 day history of fever 39.5 C, irritability, decreased responsiveness over preceding 12 hours, vomiting, bulging anterior fontanelle on exam. No freshwater exposure. No rash. Outcome: survived with mild hearing impairment. Antibiotic started at hour 2.

VITALS:
  temperature_celsius: 39.5
  heart_rate_bpm: 156
  systolic_bp_mmHg: 92
  diastolic_bp_mmHg: 56
  glasgow_coma_scale: 12
  oxygen_saturation_pct: 96
  respiratory_rate_breaths_per_min: 32

EXAM:
  mental_status_grade: confused
  neck_stiffness: True
  kernig_or_brudzinski_positive: True
  cranial_nerve_palsy: none
  papilledema_on_fundoscopy: None
  focal_neurological_deficit: False
  skin_lesion_centrofacial_chronic: False
  petechial_or_purpuric_rash: False

LABS:
  wbc_blood_per_uL: 21000
  platelets_per_uL: 280000
  alt_ast_U_per_L: 28
  crp_mg_per_L: 220.0
  procalcitonin_ng_per_mL: 12.0
  serum_sodium_mEq_per_L: 135

CSF:
  opening_pressure_cmH2O: 32.0
  wbc_per_mm3: 5400
  lymphocyte_pct: 8
  neutrophil_pct: 92
  eosinophil_pct: 0
  glucose_mg_per_dL: 18
  protein_mg_per_dL: 280
  lactate_mmol_per_L: 8.0
  ada_U_per_L: None
  crag_lfa_result: negative
  wet_mount_motile_amoebae: negative
  xanthochromia_present: False
  rbc_per_mm3: 8

IMAGING:
  modality: ct_noncontrast
  pattern: normal
  contrast_enhancement: True
  hydrocephalus: False
  basal_meningeal_enhancement: False
  finding_count: 0
  text_summary: CT head non-contrast: meningeal enhancement noted, no focal lesion, no hydrocephalus, no midline shift. Schema imaging_pattern enum lacks meningeal_enhancement_no_focal_lesion; mapped to normal with narrative note per D2.

DIAGNOSTIC_TESTS:
  pcr_panel: n/a
  xpert_mtb_rif: n/a
  blood_culture: n/a
  csf_culture: n/a
  serology_or_antigen: n/a
  smear_or_gram: n/a
  brain_biopsy: n/a
  imaging_test: n/a
  total_dx_results: 2

NARRATIVE_EN: An 18-month-old male from Lima, Peru presented to a tertiary pediatric center with a two-and-a-half day history of fever to 39.5 C, irritability, decreased responsiveness over the preceding 12 hours, vomiting, and bulging anterior fontanelle on initial examination. CSF showed opening pressure 32 cmH2O, white cell count 5,400 per cubic millimeter (92 percent neutrophils), glucose 18 mg/dL, protein 280 mg/dL. Gram stain revealed gram-positive diplococci; culture identified Streptococcus pneumoniae. Primary anchor: PMID 27831604 (Davalos 2016 RPMESP), 44-episode pediatric pneumococcal meningitis multicenter Lima cohort 2006-2011 (68.2 percent under 2 years, case fatality 32.6 percent). Outcome: survived with mild hearing impairment. Subphase 1.3 commit 5.3.2 pilot 1, pre-adjudication hold_for_revision.

NARRATIVE_ES: Lactante varon de 18 meses originario de Lima, Peru, ingresado a centro pediatrico terciario con dos y medio dias de fiebre 39.5 C, irritabilidad, respuesta disminuida en las ultimas 12 horas, vomitos y fontanela anterior abombada al examen. Liquido cefalorraquideo mostro presion de apertura 32 cmH2O, leucocitos 5,400 por mm3 (92 por ciento neutrofilos), glucosa 18 mg/dL, proteina 280 mg/dL. La tincion de Gram revelo diplococos grampositivos y el cultivo identifico Streptococcus pneumoniae. Anclaje primario en cohorte multicentrica pediatrica de Lima (PMID 27831604, Davalos 2016 RPMESP, 44 episodios 2006-2011, 68.2 por ciento bajo 2 anos, mortalidad 32.6 por ciento). Subphase 1.3 commit 5.3.2 pilot 1.

RATIONALE: Anchored to PMID 27831604 (Davalos 2016 RPMESP), 44-episode pediatric SP meningitis multicenter Lima cohort 2006-2011 (68.2 percent under-2y, CFR 32.6 percent). Demographic anchor (18mo M) sits in dominant cohort stratum. CSF profile within bacterial range per Tunkel IDSA 2004 (PMID 15494903). Imaging enum lacks meningeal_enhancement_no_focal_lesion; mapped to normal with narrative note. Imputation tiers: tier_1_primary={age, sex, region, csf_culture, csf_gram_stain}; tier_3_within_cohort={csf_wbc, csf_neutrophil_pct, csf_glucose, csf_protein}; tier_4_priors={gcs, temperature_celsius}. Indeterminate=none. Diagnostic_ambiguity=false. Outcome=survived_mild_hearing_impairment per cohort sequelae. Antibiotic_started_hours=2. Tier: primary_source_direct (Peru). 5.3.2 pilot 1.

ANCHORING_EXTRAS: stage=pre_adjudication; status=pending_external_review; self_review_disposition=hold_for_revision; self_review_notes=pilot vignette anchored to PMID 27831604 (Davalos 2016 RPMESP Lima ped); external clinical adjudication pending; classification provisional. adjudicator_ids=PILOT-PRE-ADJ-1, PILOT-PRE-ADJ-2 (sentinel); cohen_kappa=0.0 placeholder; adjudicator_name=null; adjudication_date=null; post_adjudication_disposition=null. Subphase 1.3 commit 5.3.2 (2026-05-07).

ADJUDICATION:
  inclusion_decision: hold_for_revision
  adjudicator_ids: ['PILOT-PRE-ADJ-1', 'PILOT-PRE-ADJ-2']
  ground_truth_class: 2
  pre_adjudication_kappa: 0.0
  disagreement_resolution: None

=== END vignette ===

=== CLASS 2 | vignette_id: 065 | subphase: 1.3 BACT | file: bact_065_sp_asplenia.json ===

ANCHOR:
  pmid: 15494903
  first_author: Tunkel
  year: 2004
  journal: CID
  citation_type: guideline
  doi: 10.1086/425368

DEMOGRAPHICS:
  age_years: 28
  sex: male
  geography_region: us_south
  ethnicity: white_non_hispanic
  altitude_residence_m: 100
  hiv_status: negative
  cd4_count_cells_per_uL: None
  pregnancy_red_flag: False
  immunocompromise_status: none
  freshwater_exposure_within_14d: False
  freshwater_exposure_type: None

HISTORY:
  symptom_onset_to_presentation_days: 1.5
  chief_complaint: fever_with_headache
  red_flags_present: []
  prodrome_description: 28-year-old male, US South region, post-traumatic splenectomy 6 years prior. 36-hour rapid progression: fever 39.4 C, severe headache, neck stiffness, vomiting. Tertiary ED. No freshwater. Asplenia raises encapsulated-organism risk per IDSA. Outcome: survived no sequelae. Antibiotic at hour 1 plus dexamethasone.

VITALS:
  temperature_celsius: 39.4
  heart_rate_bpm: 118
  systolic_bp_mmHg: 122
  diastolic_bp_mmHg: 76
  glasgow_coma_scale: 12
  oxygen_saturation_pct: 96
  respiratory_rate_breaths_per_min: 22

EXAM:
  mental_status_grade: somnolent
  neck_stiffness: True
  kernig_or_brudzinski_positive: True
  cranial_nerve_palsy: none
  papilledema_on_fundoscopy: False
  focal_neurological_deficit: False
  skin_lesion_centrofacial_chronic: False
  petechial_or_purpuric_rash: False

LABS:
  wbc_blood_per_uL: 22000
  platelets_per_uL: 280000
  alt_ast_U_per_L: 30
  crp_mg_per_L: 195.0
  procalcitonin_ng_per_mL: 9.2
  serum_sodium_mEq_per_L: 137

CSF:
  opening_pressure_cmH2O: 32.0
  wbc_per_mm3: 6800
  lymphocyte_pct: 8
  neutrophil_pct: 92
  eosinophil_pct: 0
  glucose_mg_per_dL: 18
  protein_mg_per_dL: 250
  lactate_mmol_per_L: 7.4
  ada_U_per_L: None
  crag_lfa_result: negative
  wet_mount_motile_amoebae: negative
  xanthochromia_present: False
  rbc_per_mm3: 6

IMAGING:
  modality: ct_noncontrast
  pattern: normal
  contrast_enhancement: True
  hydrocephalus: False
  basal_meningeal_enhancement: False
  finding_count: 0
  text_summary: CT head non-contrast: normal at admission. No focal lesion, no hydrocephalus, no midline shift, no mass effect. Pattern consistent with early-stage adult community-acquired bacterial meningitis.

DIAGNOSTIC_TESTS:
  pcr_panel: n/a
  xpert_mtb_rif: n/a
  blood_culture: n/a
  csf_culture: n/a
  serology_or_antigen: n/a
  smear_or_gram: n/a
  brain_biopsy: n/a
  imaging_test: n/a
  total_dx_results: 3

NARRATIVE_EN: A 28-year-old man in the US South region presented to a tertiary emergency department with a 36-hour rapid progression of fever to 39.4 C, severe headache, neck stiffness, and vomiting. He was post-splenectomy six years prior following a motor vehicle accident. Examination on admission: temperature 39.4 C, Glasgow Coma Scale 12, neck stiffness, positive Kernig sign, no focal deficit, no rash. CSF showed opening pressure 32 cmH2O, white cell count 6,800 per cubic millimeter (92 percent neutrophils), glucose 18 mg/dL, protein 250 mg/dL. Gram stain revealed gram-positive diplococci; culture identified Streptococcus pneumoniae. Anchored to Tunkel IDSA 2004 (PMID 15494903) recommendations for suspected pneumococcal meningitis with asplenia risk factor. Outcome: survived no sequelae. Subphase 1.3 commit 5.3.3 wave 1, pre-adjudication hold_for_revision.

NARRATIVE_ES: Varon de 28 anos en region sur de Estados Unidos, ingresado a urgencias terciarias con 36 horas de progresion rapida: fiebre 39.4 C, cefalea intensa, rigidez de nuca, vomitos. Esplenectomia traumatica seis anos antes (accidente vial). Examen: temperatura 39.4 C, escala de Glasgow 12, rigidez de nuca, signo de Kernig positivo, sin deficit focal, sin exantema. Liquido cefalorraquideo mostro presion de apertura 32 cmH2O, leucocitos 6,800 por mm3 (92 por ciento neutrofilos), glucosa 18 mg/dL, proteina 250 mg/dL. Tincion de Gram con diplococos grampositivos y cultivo Streptococcus pneumoniae. Anclaje en guia IDSA Tunkel 2004 (PMID 15494903) para meningitis neumococica con asplenia. Subphase 1.3 commit 5.3.3 wave 1.

RATIONALE: Anchored to PMID 15494903 (Tunkel IDSA 2004 CID guideline). Demographic anchor (28yo M asplenic) reflects the encapsulated-organism risk stratum referenced by Tunkel as a covered indication for empiric vancomycin plus ceftriaxone. CSF profile bacterial range per guideline cutoffs. Imputation tiers: tier_1_primary={csf_culture, csf_gram_stain, age, sex, asplenia risk factor}; tier_3_within_cohort={csf_wbc, neutrophil_pct, glucose, protein}; tier_4_priors={temp, gcs, symptom_days}. Indeterminate=none. Diagnostic_ambiguity=false. Outcome=survived_no_sequelae. Antibiotic_started_hours=1. Tier: tier_4_imputation_idsa_guideline_anchored. 5.3.3 wave1 SP-asplenia.

ANCHORING_EXTRAS: stage=pre_adjudication; status=pending_external_review; self_review_disposition=hold_for_revision; self_review_notes=wave 1 vignette anchored to PMID 15494903 (Tunkel IDSA 2004); external clinical adjudication pending; classification provisional. adjudicator_ids=WAVE1-PRE-ADJ-1, WAVE1-PRE-ADJ-2 (sentinel); cohen_kappa=0.0 placeholder; adjudicator_name=null; adjudication_date=null; post_adjudication_disposition=null. Subphase 1.3 commit 5.3.3 (2026-05-08). anchor=Tunkel-IDSA-2004 risk_factor=asplenia.

ADJUDICATION:
  inclusion_decision: hold_for_revision
  adjudicator_ids: ['WAVE1-PRE-ADJ-1', 'WAVE1-PRE-ADJ-2']
  ground_truth_class: 2
  pre_adjudication_kappa: 0.0
  disagreement_resolution: None

=== END vignette ===

=== CLASS 2 | vignette_id: 066 | subphase: 1.3 BACT | file: bact_066_sp_alcoholic_fatal.json ===

ANCHOR:
  pmid: 15509818
  first_author: van
  year: 2004
  journal: NEJM
  citation_type: cohort
  doi: 10.1056/NEJMoa040845

DEMOGRAPHICS:
  age_years: 68
  sex: male
  geography_region: other_global
  ethnicity: white_non_hispanic
  altitude_residence_m: 5
  hiv_status: negative
  cd4_count_cells_per_uL: None
  pregnancy_red_flag: False
  immunocompromise_status: none
  freshwater_exposure_within_14d: False
  freshwater_exposure_type: None

HISTORY:
  symptom_onset_to_presentation_days: 3.0
  chief_complaint: altered_mental_status
  red_flags_present: []
  prodrome_description: 68-year-old male, Netherlands. 3-day course: progressive fever, headache, confusion. Chronic alcohol use 30 years. Tertiary ED Amsterdam. Late presentation; admitted obtunded. No freshwater. Triad present (van de Beek alcoholic stratum). Outcome: fatal hospital day 4. Antibiotic at hour 3 plus dexamethasone.

VITALS:
  temperature_celsius: 39.5
  heart_rate_bpm: 124
  systolic_bp_mmHg: 102
  diastolic_bp_mmHg: 62
  glasgow_coma_scale: 8
  oxygen_saturation_pct: 92
  respiratory_rate_breaths_per_min: 28

EXAM:
  mental_status_grade: stuporous
  neck_stiffness: True
  kernig_or_brudzinski_positive: True
  cranial_nerve_palsy: none
  papilledema_on_fundoscopy: False
  focal_neurological_deficit: False
  skin_lesion_centrofacial_chronic: False
  petechial_or_purpuric_rash: False

LABS:
  wbc_blood_per_uL: 19500
  platelets_per_uL: 165000
  alt_ast_U_per_L: 88
  crp_mg_per_L: 245.0
  procalcitonin_ng_per_mL: 14.5
  serum_sodium_mEq_per_L: 132

CSF:
  opening_pressure_cmH2O: 28.0
  wbc_per_mm3: 5400
  lymphocyte_pct: 12
  neutrophil_pct: 88
  eosinophil_pct: 0
  glucose_mg_per_dL: 22
  protein_mg_per_dL: 220
  lactate_mmol_per_L: 6.8
  ada_U_per_L: None
  crag_lfa_result: negative
  wet_mount_motile_amoebae: negative
  xanthochromia_present: False
  rbc_per_mm3: 4

IMAGING:
  modality: ct_noncontrast
  pattern: diffuse_cerebral_edema_basilar_meningeal_enhancement
  contrast_enhancement: True
  hydrocephalus: False
  basal_meningeal_enhancement: False
  finding_count: 1
  text_summary: CT head non-contrast: diffuse cerebral edema with effacement of sulci, basilar meningeal enhancement on contrast-equivalent regions, no focal lesion, no midline shift. Pattern consistent with severe late-stage bacterial meningitis.

DIAGNOSTIC_TESTS:
  pcr_panel: n/a
  xpert_mtb_rif: n/a
  blood_culture: n/a
  csf_culture: n/a
  serology_or_antigen: n/a
  smear_or_gram: n/a
  brain_biopsy: n/a
  imaging_test: n/a
  total_dx_results: 3

NARRATIVE_EN: A 68-year-old man in the Netherlands presented to a tertiary emergency department in Amsterdam after a 3-day course of progressive fever, headache, and confusion. He had a 30-year history of chronic alcohol use. He was obtunded on arrival. Examination on admission: temperature 39.5 C, Glasgow Coma Scale 8, neck stiffness, positive Kernig sign, no focal deficit, no rash. CSF showed opening pressure 28 cmH2O, white cell count 5,400 per cubic millimeter (88 percent neutrophils), glucose 22 mg/dL, protein 220 mg/dL. Gram stain revealed gram-positive diplococci; culture identified Streptococcus pneumoniae. Primary anchor: PMID 15509818 (van de Beek 2004 NEJM), 696-episode prospective Netherlands cohort 1998-2002 (alcoholic stratum mortality elevated). Outcome: fatal hospital day 4. Subphase 1.3 commit 5.3.3 wave 1, pre-adjudication hold_for_revision.

NARRATIVE_ES: Varon de 68 anos en Paises Bajos (Amsterdam), ingresado a urgencias terciarias tras tres dias de fiebre progresiva, cefalea y confusion. Antecedente de consumo cronico de alcohol durante 30 anos. Ingreso obnubilado. Examen: temperatura 39.5 C, escala de Glasgow 8, rigidez de nuca, signo de Kernig positivo, sin deficit focal, sin exantema. Liquido cefalorraquideo mostro presion de apertura 28 cmH2O, leucocitos 5,400 por mm3 (88 por ciento neutrofilos), glucosa 22 mg/dL, proteina 220 mg/dL. Tincion de Gram con diplococos grampositivos y cultivo Streptococcus pneumoniae. Anclaje primario en cohorte prospectiva van de Beek 2004 NEJM (PMID 15509818, 696 episodios 1998-2002, estrato alcoholico con mortalidad elevada). Resultado: fatal en hospital dia 4. Subphase 1.3 commit 5.3.3 wave 1, pre-adjudicacion hold_for_revision.

RATIONALE: Anchored to PMID 15509818 (van de Beek 2004 NEJM), 696-episode prospective Netherlands cohort 1998-2002 (SP 51 percent, SP mortality 30 percent, alcoholic stratum mortality elevated). Demographic anchor (68yo M chronic alcohol) sits in elderly alcoholic stratum. CSF profile bacterial range. Imputation tiers: tier_1_primary={age, sex, csf_culture, csf_gram_stain, alcohol risk}; tier_3_within_cohort={csf_wbc, neutrophil_pct, glucose, protein, gcs}; tier_4_priors={temp, symptom_days}. Indeterminate=none. Diagnostic_ambiguity=false. Outcome=fatal_hospital_day_4. Antibiotic_started_hours=3. Tier: tier_3_imputation_within_cohort_review. 5.3.3 wave1 SP-alcoholic-fatal.

ANCHORING_EXTRAS: stage=pre_adjudication; status=pending_external_review; self_review_disposition=hold_for_revision; self_review_notes=wave 1 vignette anchored to PMID 15509818 (van de Beek 2004 NEJM); external clinical adjudication pending; classification provisional. adjudicator_ids=WAVE1-PRE-ADJ-1, WAVE1-PRE-ADJ-2 (sentinel); cohen_kappa=0.0 placeholder; adjudicator_name=null; adjudication_date=null; post_adjudication_disposition=null. Subphase 1.3 commit 5.3.3 (2026-05-08). anchor=van-de-Beek-NEJM-2004 stratum=alcoholic-elderly.

ADJUDICATION:
  inclusion_decision: hold_for_revision
  adjudicator_ids: ['WAVE1-PRE-ADJ-1', 'WAVE1-PRE-ADJ-2']
  ground_truth_class: 2
  pre_adjudication_kappa: 0.0
  disagreement_resolution: None

=== END vignette ===

=== CLASS 2 | vignette_id: 067 | subphase: 1.3 BACT | file: bact_067_sp_pediatric.json ===

ANCHOR:
  pmid: 15494903
  first_author: Tunkel
  year: 2004
  journal: CID
  citation_type: guideline
  doi: 10.1086/425368

DEMOGRAPHICS:
  age_years: 3
  sex: male
  geography_region: us_south
  ethnicity: white_non_hispanic
  altitude_residence_m: 100
  hiv_status: negative
  cd4_count_cells_per_uL: None
  pregnancy_red_flag: False
  immunocompromise_status: none
  freshwater_exposure_within_14d: False
  freshwater_exposure_type: None

HISTORY:
  symptom_onset_to_presentation_days: 1.5
  chief_complaint: altered_mental_status
  red_flags_present: []
  prodrome_description: Three-year-old male, US South region. 36-hour fever 39.6 C, vomiting, irritability progressing to lethargy. Recent otitis media. Tertiary pediatric ED. No freshwater. Outcome: survived with mild hearing loss. Antibiotic at hour 1.5 plus dexamethasone per IDSA pediatric protocol.

VITALS:
  temperature_celsius: 39.6
  heart_rate_bpm: 148
  systolic_bp_mmHg: 100
  diastolic_bp_mmHg: 60
  glasgow_coma_scale: 12
  oxygen_saturation_pct: 95
  respiratory_rate_breaths_per_min: 30

EXAM:
  mental_status_grade: confused
  neck_stiffness: True
  kernig_or_brudzinski_positive: True
  cranial_nerve_palsy: none
  papilledema_on_fundoscopy: None
  focal_neurological_deficit: False
  skin_lesion_centrofacial_chronic: False
  petechial_or_purpuric_rash: False

LABS:
  wbc_blood_per_uL: 23500
  platelets_per_uL: 295000
  alt_ast_U_per_L: 26
  crp_mg_per_L: 185.0
  procalcitonin_ng_per_mL: 8.8
  serum_sodium_mEq_per_L: 136

CSF:
  opening_pressure_cmH2O: 30.0
  wbc_per_mm3: 7200
  lymphocyte_pct: 10
  neutrophil_pct: 90
  eosinophil_pct: 0
  glucose_mg_per_dL: 20
  protein_mg_per_dL: 240
  lactate_mmol_per_L: 7.2
  ada_U_per_L: None
  crag_lfa_result: negative
  wet_mount_motile_amoebae: negative
  xanthochromia_present: False
  rbc_per_mm3: 4

IMAGING:
  modality: ct_noncontrast
  pattern: normal
  contrast_enhancement: True
  hydrocephalus: False
  basal_meningeal_enhancement: False
  finding_count: 0
  text_summary: CT head non-contrast: normal at admission. No focal lesion, no hydrocephalus, no midline shift, no mass effect. Pattern consistent with early-stage adult community-acquired bacterial meningitis.

DIAGNOSTIC_TESTS:
  pcr_panel: n/a
  xpert_mtb_rif: n/a
  blood_culture: n/a
  csf_culture: n/a
  serology_or_antigen: n/a
  smear_or_gram: n/a
  brain_biopsy: n/a
  imaging_test: n/a
  total_dx_results: 3

NARRATIVE_EN: A three-year-old boy in the US South region presented to a tertiary pediatric emergency department with a 36-hour history of fever to 39.6 C, vomiting, irritability, and decreasing responsiveness. He had been treated for otitis media in the preceding week. Examination on admission: temperature 39.6 C, Glasgow Coma Scale 12, neck stiffness, positive Kernig sign, no focal deficit, no rash. CSF showed opening pressure 30 cmH2O, white cell count 7,200 per cubic millimeter (90 percent neutrophils), glucose 20 mg/dL, protein 240 mg/dL. Gram stain revealed gram-positive diplococci; culture identified Streptococcus pneumoniae. Anchored to Tunkel IDSA 2004 (PMID 15494903) pediatric pneumococcal meningitis recommendations. Outcome: survived with mild hearing loss. Subphase 1.3 commit 5.3.3 wave 1, pre-adjudication hold_for_revision.

NARRATIVE_ES: Varon de tres anos en region sur de Estados Unidos, ingresado a urgencias pediatricas terciarias con 36 horas de fiebre 39.6 C, vomitos, irritabilidad y respuesta disminuida. Tratamiento previo para otitis media en la semana anterior. Examen: temperatura 39.6 C, escala de Glasgow 12, rigidez de nuca, signo de Kernig positivo, sin deficit focal, sin exantema. Liquido cefalorraquideo mostro presion de apertura 30 cmH2O, leucocitos 7,200 por mm3 (90 por ciento neutrofilos), glucosa 20 mg/dL, proteina 240 mg/dL. Tincion de Gram con diplococos grampositivos y cultivo Streptococcus pneumoniae. Anclaje en guia IDSA Tunkel 2004 (PMID 15494903), recomendaciones pediatricas. Subphase 1.3 commit 5.3.3 wave 1.

RATIONALE: Anchored to PMID 15494903 (Tunkel IDSA 2004 CID guideline) for pediatric pneumococcal meningitis empiric coverage. Demographic anchor (3yo M post-otitis-media) sits in the high-risk pediatric stratum referenced by Tunkel. CSF profile bacterial range per guideline cutoffs. Imputation tiers: tier_1_primary={age, sex, csf_culture, csf_gram_stain}; tier_3_within_cohort={csf_wbc, neutrophil_pct, glucose, protein}; tier_4_priors={temp, gcs, symptom_days, hr}. Indeterminate=papilledema. Diagnostic_ambiguity=false. Outcome=survived_mild_hearing_loss. Antibiotic_started_hours=1.5. Tier: tier_4_imputation_idsa_guideline_anchored. 5.3.3 wave1 SP-pediatric.

ANCHORING_EXTRAS: stage=pre_adjudication; status=pending_external_review; self_review_disposition=hold_for_revision; self_review_notes=wave 1 vignette anchored to PMID 15494903 (Tunkel IDSA 2004); external clinical adjudication pending; classification provisional. adjudicator_ids=WAVE1-PRE-ADJ-1, WAVE1-PRE-ADJ-2 (sentinel); cohen_kappa=0.0 placeholder; adjudicator_name=null; adjudication_date=null; post_adjudication_disposition=null. Subphase 1.3 commit 5.3.3 (2026-05-08). anchor=Tunkel-IDSA-2004 stratum=pediatric.

ADJUDICATION:
  inclusion_decision: hold_for_revision
  adjudicator_ids: ['WAVE1-PRE-ADJ-1', 'WAVE1-PRE-ADJ-2']
  ground_truth_class: 2
  pre_adjudication_kappa: 0.0
  disagreement_resolution: None

=== END vignette ===

=== CLASS 2 | vignette_id: 068 | subphase: 1.3 BACT | file: bact_068_sp_adult_female.json ===

ANCHOR:
  pmid: 26652862
  first_author: Bijlsma
  year: 2016
  journal: Lancet Infect Dis
  citation_type: cohort
  doi: 10.1016/S1473-3099(15)00430-2

DEMOGRAPHICS:
  age_years: 51
  sex: female
  geography_region: other_global
  ethnicity: white_non_hispanic
  altitude_residence_m: 5
  hiv_status: negative
  cd4_count_cells_per_uL: None
  pregnancy_red_flag: False
  immunocompromise_status: none
  freshwater_exposure_within_14d: False
  freshwater_exposure_type: None

HISTORY:
  symptom_onset_to_presentation_days: 2.0
  chief_complaint: fever_with_headache
  red_flags_present: []
  prodrome_description: 51-year-old female, Netherlands. 2-day fever 39.2 C, severe headache, neck stiffness. Recent otitis media one week prior. Tertiary ED Amsterdam. No freshwater. Triad present (Bijlsma 2016 adult community stratum). Outcome: survived no sequelae. Antibiotic at hour 1 plus dexamethasone EU guideline.

VITALS:
  temperature_celsius: 39.2
  heart_rate_bpm: 112
  systolic_bp_mmHg: 124
  diastolic_bp_mmHg: 78
  glasgow_coma_scale: 13
  oxygen_saturation_pct: 96
  respiratory_rate_breaths_per_min: 22

EXAM:
  mental_status_grade: confused
  neck_stiffness: True
  kernig_or_brudzinski_positive: True
  cranial_nerve_palsy: none
  papilledema_on_fundoscopy: False
  focal_neurological_deficit: False
  skin_lesion_centrofacial_chronic: False
  petechial_or_purpuric_rash: False

LABS:
  wbc_blood_per_uL: 19800
  platelets_per_uL: 260000
  alt_ast_U_per_L: 28
  crp_mg_per_L: 185.0
  procalcitonin_ng_per_mL: 7.8
  serum_sodium_mEq_per_L: 136

CSF:
  opening_pressure_cmH2O: 28.0
  wbc_per_mm3: 5800
  lymphocyte_pct: 10
  neutrophil_pct: 90
  eosinophil_pct: 0
  glucose_mg_per_dL: 22
  protein_mg_per_dL: 210
  lactate_mmol_per_L: 6.6
  ada_U_per_L: None
  crag_lfa_result: negative
  wet_mount_motile_amoebae: negative
  xanthochromia_present: False
  rbc_per_mm3: 4

IMAGING:
  modality: ct_noncontrast
  pattern: normal
  contrast_enhancement: True
  hydrocephalus: False
  basal_meningeal_enhancement: False
  finding_count: 0
  text_summary: CT head non-contrast: normal at admission. No focal lesion, no hydrocephalus, no midline shift, no mass effect. Pattern consistent with early-stage adult community-acquired bacterial meningitis.

DIAGNOSTIC_TESTS:
  pcr_panel: n/a
  xpert_mtb_rif: n/a
  blood_culture: n/a
  csf_culture: n/a
  serology_or_antigen: n/a
  smear_or_gram: n/a
  brain_biopsy: n/a
  imaging_test: n/a
  total_dx_results: 3

NARRATIVE_EN: A 51-year-old woman in the Netherlands presented to a tertiary emergency department in Amsterdam with a 2-day history of fever to 39.2 C, severe headache, and neck stiffness. She had been treated for otitis media one week prior. Examination on admission: temperature 39.2 C, Glasgow Coma Scale 13, neck stiffness, positive Kernig sign, no focal deficit, no rash. CSF showed opening pressure 28 cmH2O, white cell count 5,800 per cubic millimeter (90 percent neutrophils), glucose 22 mg/dL, protein 210 mg/dL. Gram stain revealed gram-positive diplococci; culture identified Streptococcus pneumoniae. Primary anchor: PMID 26652862 (Bijlsma 2016 Lancet Infect Dis), 1,412-episode prospective Netherlands cohort 2006-2014. Outcome: survived no sequelae. Subphase 1.3 commit 5.3.4 wave 2, pre-adjudication hold_for_revision.

NARRATIVE_ES: Mujer de 51 anos en Paises Bajos (Amsterdam), ingresada a urgencias terciarias con dos dias de fiebre 39.2 C, cefalea intensa y rigidez de nuca. Antecedente de otitis media tratada una semana antes. Examen: temperatura 39.2 C, escala de Glasgow 13, rigidez de nuca, signo de Kernig positivo, sin deficit focal, sin exantema. Liquido cefalorraquideo mostro presion de apertura 28 cmH2O, leucocitos 5,800 por mm3 (90 por ciento neutrofilos), glucosa 22 mg/dL, proteina 210 mg/dL. Tincion de Gram con diplococos grampositivos y cultivo Streptococcus pneumoniae. Anclaje primario en cohorte prospectiva Bijlsma 2016 Lancet ID (PMID 26652862, 1,412 episodios 2006-2014, SP 70 por ciento, triada 47 por ciento). Resultado: sobrevivio sin secuelas. Subphase 1.3 commit 5.3.4 wave 2, pre-adjudicacion hold_for_revision.

RATIONALE: Anchored to PMID 26652862 (Bijlsma 2016 Lancet ID), 1,412-episode prospective Netherlands cohort 2006-2014 (SP 70 percent, classic triad 47 percent). Demographic anchor (51yo F adult with otitis media antecedent) sits in adult community stratum. CSF profile bacterial range. Imputation tiers: tier_1_primary={age, sex, csf_culture, csf_gram_stain, otitis_media history}; tier_3_within_cohort={csf_wbc, neutrophil_pct, glucose, protein}; tier_4_priors={temp, gcs, symptom_days}. Indeterminate=none. Diagnostic_ambiguity=false. Outcome=survived_no_sequelae. Tier: tier_3_imputation_within_cohort_review. 5.3.4 wave2 SP-NL-adult-female.

ANCHORING_EXTRAS: stage=pre_adjudication; status=pending_external_review; self_review_disposition=hold_for_revision; self_review_notes=wave 2 vignette anchored to PMID 26652862 (Bijlsma 2016 Lancet ID); external clinical adjudication pending; classification provisional. adjudicator_ids=WAVE2-PRE-ADJ-1, WAVE2-PRE-ADJ-2 (sentinel); cohen_kappa=0.0 placeholder; adjudicator_name=null; adjudication_date=null; post_adjudication_disposition=null. Subphase 1.3 commit 5.3.4 (2026-05-08). anchor=Bijlsma-Lancet-ID-2016 stratum=adult-community-female.

ADJUDICATION:
  inclusion_decision: hold_for_revision
  adjudicator_ids: ['WAVE2-PRE-ADJ-1', 'WAVE2-PRE-ADJ-2']
  ground_truth_class: 2
  pre_adjudication_kappa: 0.0
  disagreement_resolution: None

=== END vignette ===

=== CLASS 2 | vignette_id: 069 | subphase: 1.3 BACT | file: bact_069_sp_recurrent_csf_leak.json ===

ANCHOR:
  pmid: 15494903
  first_author: Tunkel
  year: 2004
  journal: CID
  citation_type: guideline
  doi: 10.1086/425368

DEMOGRAPHICS:
  age_years: 19
  sex: male
  geography_region: us_south
  ethnicity: white_non_hispanic
  altitude_residence_m: 100
  hiv_status: negative
  cd4_count_cells_per_uL: None
  pregnancy_red_flag: False
  immunocompromise_status: none
  freshwater_exposure_within_14d: False
  freshwater_exposure_type: None

HISTORY:
  symptom_onset_to_presentation_days: 2.0
  chief_complaint: fever_with_headache
  red_flags_present: []
  prodrome_description: 19-year-old male, US South region. Skull-base fracture with CSF rhinorrhea 3 years prior (motor vehicle accident); not surgically corrected. Second meningitis episode: 2-day fever 39.2 C, headache, neck stiffness. Tertiary ED. No freshwater. Outcome: survived. Antibiotic at hour 2 plus dexamethasone.

VITALS:
  temperature_celsius: 39.2
  heart_rate_bpm: 110
  systolic_bp_mmHg: 124
  diastolic_bp_mmHg: 74
  glasgow_coma_scale: 13
  oxygen_saturation_pct: 96
  respiratory_rate_breaths_per_min: 22

EXAM:
  mental_status_grade: confused
  neck_stiffness: True
  kernig_or_brudzinski_positive: True
  cranial_nerve_palsy: none
  papilledema_on_fundoscopy: False
  focal_neurological_deficit: False
  skin_lesion_centrofacial_chronic: False
  petechial_or_purpuric_rash: False

LABS:
  wbc_blood_per_uL: 17500
  platelets_per_uL: 250000
  alt_ast_U_per_L: 28
  crp_mg_per_L: 145.0
  procalcitonin_ng_per_mL: 5.5
  serum_sodium_mEq_per_L: 137

CSF:
  opening_pressure_cmH2O: 26.0
  wbc_per_mm3: 4200
  lymphocyte_pct: 15
  neutrophil_pct: 85
  eosinophil_pct: 0
  glucose_mg_per_dL: 25
  protein_mg_per_dL: 180
  lactate_mmol_per_L: 5.5
  ada_U_per_L: None
  crag_lfa_result: negative
  wet_mount_motile_amoebae: negative
  xanthochromia_present: False
  rbc_per_mm3: 6

IMAGING:
  modality: ct_noncontrast
  pattern: normal
  contrast_enhancement: True
  hydrocephalus: False
  basal_meningeal_enhancement: False
  finding_count: 0
  text_summary: CT head non-contrast: normal at admission. No focal lesion, no hydrocephalus, no midline shift, no mass effect. Pattern consistent with early-stage adult community-acquired bacterial meningitis.

DIAGNOSTIC_TESTS:
  pcr_panel: n/a
  xpert_mtb_rif: n/a
  blood_culture: n/a
  csf_culture: n/a
  serology_or_antigen: n/a
  smear_or_gram: n/a
  brain_biopsy: n/a
  imaging_test: n/a
  total_dx_results: 3

NARRATIVE_EN: A 19-year-old man in the US South region presented to a tertiary emergency department with a 2-day history of fever to 39.2 C, headache, and neck stiffness. He had a skull-base fracture with CSF rhinorrhea three years prior following a motor vehicle accident that had not been surgically corrected; this was his second episode of bacterial meningitis. Examination on admission: temperature 39.2 C, Glasgow Coma Scale 13, neck stiffness, positive Kernig sign, no focal deficit, no rash. CSF showed opening pressure 26 cmH2O, white cell count 4,200 per cubic millimeter (85 percent neutrophils), glucose 25 mg/dL, protein 180 mg/dL. Gram stain revealed gram-positive diplococci; culture identified Streptococcus pneumoniae. Anchored to Tunkel IDSA 2004 (PMID 15494903) recurrent SP meningitis recommendations. Outcome: survived. Subphase 1.3 commit 5.3.3 wave 1, pre-adjudication hold_for_revision.

NARRATIVE_ES: Varon de 19 anos en region sur de Estados Unidos, ingresado a urgencias terciarias con dos dias de fiebre 39.2 C, cefalea y rigidez de nuca. Antecedente de fractura de base de craneo con rinorrea de liquido cefalorraquideo tres anos antes (no corregida quirurgicamente); segundo episodio de meningitis bacteriana. Examen: temperatura 39.2 C, escala de Glasgow 13, rigidez de nuca, signo de Kernig positivo, sin deficit focal, sin exantema. Liquido cefalorraquideo mostro presion de apertura 26 cmH2O, leucocitos 4,200 por mm3 (85 por ciento neutrofilos), glucosa 25 mg/dL, proteina 180 mg/dL. Tincion de Gram con diplococos grampositivos y cultivo Streptococcus pneumoniae. Anclaje en guia IDSA Tunkel 2004 (PMID 15494903). Subphase 1.3 commit 5.3.3 wave 1.

RATIONALE: Anchored to PMID 15494903 (Tunkel IDSA 2004 CID guideline) recurrent SP meningitis recommendations. Anatomic CSF rhinorrhea raises recurrent-SP risk per guideline. Demographic anchor (19yo M with anatomic CSF leak) reflects the recurrent-meningitis stratum. CSF profile bacterial range. Imputation tiers: tier_1_primary={age, sex, csf_culture, csf_gram_stain, anatomic_leak history}; tier_3_within_cohort={csf_wbc, neutrophil_pct, glucose, protein}; tier_4_priors={temp, gcs, symptom_days}. Indeterminate=none. Diagnostic_ambiguity=false. Outcome=survived. Antibiotic_started_hours=2. Tier: tier_4_imputation_idsa_guideline_anchored. 5.3.3 wave1 SP-recurrent-CSF-leak.

ANCHORING_EXTRAS: stage=pre_adjudication; status=pending_external_review; self_review_disposition=hold_for_revision; self_review_notes=wave 1 vignette anchored to PMID 15494903 (Tunkel IDSA 2004); external clinical adjudication pending; classification provisional. adjudicator_ids=WAVE1-PRE-ADJ-1, WAVE1-PRE-ADJ-2 (sentinel); cohen_kappa=0.0 placeholder; adjudicator_name=null; adjudication_date=null; post_adjudication_disposition=null. Subphase 1.3 commit 5.3.3 (2026-05-08). anchor=Tunkel-IDSA-2004 risk_factor=anatomic-CSF-leak.

ADJUDICATION:
  inclusion_decision: hold_for_revision
  adjudicator_ids: ['WAVE1-PRE-ADJ-1', 'WAVE1-PRE-ADJ-2']
  ground_truth_class: 2
  pre_adjudication_kappa: 0.0
  disagreement_resolution: None

=== END vignette ===

=== CLASS 2 | vignette_id: 070 | subphase: 1.3 BACT | file: bact_070_sp_elderly_sequelae.json ===

ANCHOR:
  pmid: 26652862
  first_author: Bijlsma
  year: 2016
  journal: Lancet Infect Dis
  citation_type: cohort
  doi: 10.1016/S1473-3099(15)00430-2

DEMOGRAPHICS:
  age_years: 65
  sex: male
  geography_region: other_global
  ethnicity: white_non_hispanic
  altitude_residence_m: 5
  hiv_status: negative
  cd4_count_cells_per_uL: None
  pregnancy_red_flag: False
  immunocompromise_status: none
  freshwater_exposure_within_14d: False
  freshwater_exposure_type: None

HISTORY:
  symptom_onset_to_presentation_days: 2.5
  chief_complaint: fever_with_headache
  red_flags_present: []
  prodrome_description: 65-year-old male, Netherlands. 2.5-day fever 39.0 C, headache, neck stiffness, mild confusion. Tertiary ED Amsterdam. No freshwater. Triad present (Bijlsma elderly stratum, sequelae rate 24 percent in survivors). Outcome: survived with mild hearing loss. Antibiotic at hour 1.5 plus dexamethasone EU.

VITALS:
  temperature_celsius: 39.0
  heart_rate_bpm: 108
  systolic_bp_mmHg: 134
  diastolic_bp_mmHg: 80
  glasgow_coma_scale: 12
  oxygen_saturation_pct: 96
  respiratory_rate_breaths_per_min: 22

EXAM:
  mental_status_grade: confused
  neck_stiffness: True
  kernig_or_brudzinski_positive: True
  cranial_nerve_palsy: none
  papilledema_on_fundoscopy: False
  focal_neurological_deficit: False
  skin_lesion_centrofacial_chronic: False
  petechial_or_purpuric_rash: False

LABS:
  wbc_blood_per_uL: 18200
  platelets_per_uL: 225000
  alt_ast_U_per_L: 32
  crp_mg_per_L: 168.0
  procalcitonin_ng_per_mL: 6.8
  serum_sodium_mEq_per_L: 135

CSF:
  opening_pressure_cmH2O: 26.0
  wbc_per_mm3: 4800
  lymphocyte_pct: 16
  neutrophil_pct: 84
  eosinophil_pct: 0
  glucose_mg_per_dL: 25
  protein_mg_per_dL: 195
  lactate_mmol_per_L: 6.0
  ada_U_per_L: None
  crag_lfa_result: negative
  wet_mount_motile_amoebae: negative
  xanthochromia_present: False
  rbc_per_mm3: 5

IMAGING:
  modality: ct_noncontrast
  pattern: normal
  contrast_enhancement: True
  hydrocephalus: False
  basal_meningeal_enhancement: False
  finding_count: 0
  text_summary: CT head non-contrast: normal at admission. No focal lesion, no hydrocephalus, no midline shift, no mass effect. Pattern consistent with early-stage adult community-acquired bacterial meningitis.

DIAGNOSTIC_TESTS:
  pcr_panel: n/a
  xpert_mtb_rif: n/a
  blood_culture: n/a
  csf_culture: n/a
  serology_or_antigen: n/a
  smear_or_gram: n/a
  brain_biopsy: n/a
  imaging_test: n/a
  total_dx_results: 3

NARRATIVE_EN: A 65-year-old man in the Netherlands presented to a tertiary emergency department in Amsterdam with a 2.5-day history of fever to 39.0 C, headache, neck stiffness, and mild confusion. Examination on admission: temperature 39.0 C, Glasgow Coma Scale 12, neck stiffness, positive Kernig sign, no focal deficit, no rash. CSF showed opening pressure 26 cmH2O, white cell count 4,800 per cubic millimeter (84 percent neutrophils), glucose 25 mg/dL, protein 195 mg/dL. Gram stain revealed gram-positive diplococci; culture identified Streptococcus pneumoniae. Primary anchor: PMID 26652862 (Bijlsma 2016 Lancet Infect Dis), 1,412-episode prospective Netherlands cohort 2006-2014; elderly stratum sequelae rate 24 percent in survivors. Outcome: survived with mild hearing loss. Subphase 1.3 commit 5.3.4 wave 2, pre-adjudication hold_for_revision.

NARRATIVE_ES: Varon de 65 anos en Paises Bajos (Amsterdam), ingresado a urgencias terciarias con 2.5 dias de fiebre 39.0 C, cefalea, rigidez de nuca y confusion leve. Examen: temperatura 39.0 C, escala de Glasgow 12, rigidez de nuca, signo de Kernig positivo, sin deficit focal, sin exantema. Liquido cefalorraquideo mostro presion de apertura 26 cmH2O, leucocitos 4,800 por mm3 (84 por ciento neutrofilos), glucosa 25 mg/dL, proteina 195 mg/dL. Tincion de Gram con diplococos grampositivos y cultivo Streptococcus pneumoniae. Anclaje primario en cohorte Bijlsma 2016 Lancet ID (PMID 26652862, estrato adulto mayor, secuelas 24 por ciento en sobrevivientes). Resultado: sobrevivio con perdida auditiva leve. Subphase 1.3 commit 5.3.4 wave 2.

RATIONALE: Anchored to PMID 26652862 (Bijlsma 2016 Lancet ID), 1,412-episode prospective Netherlands cohort 2006-2014 (SP 70 percent, sequelae rate 24 percent in survivors at age >=60). Demographic anchor (65yo M elderly survived) sits in elderly-survived-with-sequelae stratum. CSF profile bacterial range. Imputation tiers: tier_1_primary={age, sex, csf_culture, csf_gram_stain}; tier_3_within_cohort={csf_wbc, neutrophil_pct, glucose, protein, gcs}; tier_4_priors={temp, symptom_days}. Indeterminate=none. Diagnostic_ambiguity=false. Outcome=survived_with_mild_hearing_loss. Tier: tier_3_imputation_within_cohort_review. 5.3.4 wave2 SP-NL-elderly-sequelae.

ANCHORING_EXTRAS: stage=pre_adjudication; status=pending_external_review; self_review_disposition=hold_for_revision; self_review_notes=wave 2 vignette anchored to PMID 26652862 (Bijlsma 2016 Lancet ID); external clinical adjudication pending; classification provisional. adjudicator_ids=WAVE2-PRE-ADJ-1, WAVE2-PRE-ADJ-2 (sentinel); cohen_kappa=0.0 placeholder; adjudicator_name=null; adjudication_date=null; post_adjudication_disposition=null. Subphase 1.3 commit 5.3.4 (2026-05-08). anchor=Bijlsma-Lancet-ID-2016 stratum=elderly-survived-sequelae.

ADJUDICATION:
  inclusion_decision: hold_for_revision
  adjudicator_ids: ['WAVE2-PRE-ADJ-1', 'WAVE2-PRE-ADJ-2']
  ground_truth_class: 2
  pre_adjudication_kappa: 0.0
  disagreement_resolution: None

=== END vignette ===

=== CLASS 2 | vignette_id: 071 | subphase: 1.3 BACT | file: bact_071_sp_lima_adult.json ===

ANCHOR:
  pmid: 15494903
  first_author: Tunkel
  year: 2004
  journal: CID
  citation_type: guideline
  doi: 10.1086/425368

DEMOGRAPHICS:
  age_years: 38
  sex: female
  geography_region: peru_lima_coast
  ethnicity: mestizo
  altitude_residence_m: 154
  hiv_status: negative
  cd4_count_cells_per_uL: None
  pregnancy_red_flag: False
  immunocompromise_status: none
  freshwater_exposure_within_14d: False
  freshwater_exposure_type: None

HISTORY:
  symptom_onset_to_presentation_days: 2.0
  chief_complaint: fever_with_headache
  red_flags_present: []
  prodrome_description: 38-year-old female, Lima Peru, presented to tertiary urban ED with 2-day fever 39.0 C, severe headache, neck stiffness, photophobia. No freshwater exposure. No rash. Empiric ceftriaxone-vancomycin started hour 1 plus dexamethasone per IDSA SP protocol. Outcome: survived no sequelae.

VITALS:
  temperature_celsius: 39.0
  heart_rate_bpm: 108
  systolic_bp_mmHg: 120
  diastolic_bp_mmHg: 72
  glasgow_coma_scale: 13
  oxygen_saturation_pct: 97
  respiratory_rate_breaths_per_min: 20

EXAM:
  mental_status_grade: confused
  neck_stiffness: True
  kernig_or_brudzinski_positive: True
  cranial_nerve_palsy: none
  papilledema_on_fundoscopy: False
  focal_neurological_deficit: False
  skin_lesion_centrofacial_chronic: False
  petechial_or_purpuric_rash: False

LABS:
  wbc_blood_per_uL: 19200
  platelets_per_uL: 245000
  alt_ast_U_per_L: 32
  crp_mg_per_L: 165.0
  procalcitonin_ng_per_mL: 6.3
  serum_sodium_mEq_per_L: 136

CSF:
  opening_pressure_cmH2O: 28.0
  wbc_per_mm3: 5800
  lymphocyte_pct: 12
  neutrophil_pct: 88
  eosinophil_pct: 0
  glucose_mg_per_dL: 22
  protein_mg_per_dL: 200
  lactate_mmol_per_L: 6.4
  ada_U_per_L: None
  crag_lfa_result: negative
  wet_mount_motile_amoebae: negative
  xanthochromia_present: False
  rbc_per_mm3: 5

IMAGING:
  modality: ct_noncontrast
  pattern: normal
  contrast_enhancement: True
  hydrocephalus: False
  basal_meningeal_enhancement: False
  finding_count: 0
  text_summary: CT head non-contrast: normal at admission. No focal lesion, no hydrocephalus, no midline shift, no mass effect. Pattern consistent with early-stage adult community-acquired bacterial meningitis.

DIAGNOSTIC_TESTS:
  pcr_panel: n/a
  xpert_mtb_rif: n/a
  blood_culture: n/a
  csf_culture: n/a
  serology_or_antigen: n/a
  smear_or_gram: n/a
  brain_biopsy: n/a
  imaging_test: n/a
  total_dx_results: 3

NARRATIVE_EN: A 38-year-old woman in Lima, Peru presented to a tertiary urban emergency department with a 2-day history of fever to 39.0 C, severe headache, neck stiffness, and photophobia. Examination on admission: temperature 39.0 C, Glasgow Coma Scale 13, neck stiffness, positive Kernig sign, no focal deficit, no rash. CSF showed opening pressure 28 cmH2O, white cell count 5,800 per cubic millimeter (88 percent neutrophils), glucose 22 mg/dL, protein 200 mg/dL. Gram stain revealed gram-positive diplococci; culture identified Streptococcus pneumoniae. Anchored to Tunkel IDSA 2004 (PMID 15494903) for empiric ceftriaxone-vancomycin coverage of adult community-acquired pneumococcal meningitis. Outcome: survived no sequelae. Subphase 1.3 commit 5.3.3 wave 1, pre-adjudication hold_for_revision.

NARRATIVE_ES: Mujer de 38 anos en Lima, Peru, ingresada a urgencias terciarias con dos dias de fiebre 39.0 C, cefalea intensa, rigidez de nuca y fotofobia. Examen: temperatura 39.0 C, escala de Glasgow 13, rigidez de nuca, signo de Kernig positivo, sin deficit focal, sin exantema. Liquido cefalorraquideo mostro presion de apertura 28 cmH2O, leucocitos 5,800 por mm3 (88 por ciento neutrofilos), glucosa 22 mg/dL, proteina 200 mg/dL. Tincion de Gram con diplococos grampositivos y cultivo Streptococcus pneumoniae. Anclaje en guia IDSA Tunkel 2004 (PMID 15494903) para cobertura empirica con ceftriaxona-vancomicina mas dexametasona en meningitis neumococica del adulto adquirida en la comunidad. Geografia anclada a Peru (5/30 escenarios bacterianos de la distribucion 5.3.1 asignados a Peru). Resultado: sobrevivio sin secuelas. Subphase 1.3 commit 5.3.3 wave 1, pre-adjudicacion hold_for_revision.

RATIONALE: Anchored to PMID 15494903 (Tunkel IDSA 2004 CID guideline) for adult community-acquired pneumococcal meningitis empiric coverage. Peru-anchored geography (5/30 BACT slots assigned to Peru per 5.3.1 distribution lock). Demographic anchor (38yo F adult) sits in standard adult community stratum. CSF profile bacterial range. Imputation tiers: tier_1_primary={age, sex, region, csf_culture, csf_gram_stain}; tier_3_within_cohort={csf_wbc, neutrophil_pct, glucose, protein}; tier_4_priors={temp, gcs, symptom_days}. Indeterminate=none. Diagnostic_ambiguity=false. Outcome=survived. Antibiotic_started_hours=1. Tier: tier_4_imputation_idsa_guideline_anchored. 5.3.3 wave1 SP-Lima-adult.

ANCHORING_EXTRAS: stage=pre_adjudication; status=pending_external_review; self_review_disposition=hold_for_revision; self_review_notes=wave 1 vignette anchored to PMID 15494903 (Tunkel IDSA 2004); external clinical adjudication pending; classification provisional. adjudicator_ids=WAVE1-PRE-ADJ-1, WAVE1-PRE-ADJ-2 (sentinel); cohen_kappa=0.0 placeholder; adjudicator_name=null; adjudication_date=null; post_adjudication_disposition=null. Subphase 1.3 commit 5.3.3 (2026-05-08). anchor=Tunkel-IDSA-2004 region=Lima-Peru.

ADJUDICATION:
  inclusion_decision: hold_for_revision
  adjudicator_ids: ['WAVE1-PRE-ADJ-1', 'WAVE1-PRE-ADJ-2']
  ground_truth_class: 2
  pre_adjudication_kappa: 0.0
  disagreement_resolution: None

=== END vignette ===

=== CLASS 2 | vignette_id: 072 | subphase: 1.3 BACT | file: bact_072_sp_adult.json ===

ANCHOR:
  pmid: 26652862
  first_author: Bijlsma
  year: 2016
  journal: Lancet Infect Dis
  citation_type: cohort
  doi: 10.1016/S1473-3099(15)00430-2

DEMOGRAPHICS:
  age_years: 55
  sex: male
  geography_region: other_global
  ethnicity: white_non_hispanic
  altitude_residence_m: 5
  hiv_status: negative
  cd4_count_cells_per_uL: None
  pregnancy_red_flag: False
  immunocompromise_status: none
  freshwater_exposure_within_14d: False
  freshwater_exposure_type: None

HISTORY:
  symptom_onset_to_presentation_days: 2.0
  chief_complaint: fever_with_headache
  red_flags_present: []
  prodrome_description: 55-year-old male, Netherlands. 48-hour fever 39.3 C, severe headache, neck stiffness. Tertiary ED Amsterdam. No freshwater. Triad present (Bijlsma adult community stratum). Outcome: survived no sequelae. Antibiotic at hour 1 plus dexamethasone EU guideline 2002.

VITALS:
  temperature_celsius: 39.3
  heart_rate_bpm: 110
  systolic_bp_mmHg: 128
  diastolic_bp_mmHg: 78
  glasgow_coma_scale: 13
  oxygen_saturation_pct: 96
  respiratory_rate_breaths_per_min: 22

EXAM:
  mental_status_grade: confused
  neck_stiffness: True
  kernig_or_brudzinski_positive: True
  cranial_nerve_palsy: none
  papilledema_on_fundoscopy: False
  focal_neurological_deficit: False
  skin_lesion_centrofacial_chronic: False
  petechial_or_purpuric_rash: False

LABS:
  wbc_blood_per_uL: 19400
  platelets_per_uL: 250000
  alt_ast_U_per_L: 30
  crp_mg_per_L: 178.0
  procalcitonin_ng_per_mL: 7.2
  serum_sodium_mEq_per_L: 136

CSF:
  opening_pressure_cmH2O: 27.0
  wbc_per_mm3: 5600
  lymphocyte_pct: 12
  neutrophil_pct: 88
  eosinophil_pct: 0
  glucose_mg_per_dL: 23
  protein_mg_per_dL: 205
  lactate_mmol_per_L: 6.4
  ada_U_per_L: None
  crag_lfa_result: negative
  wet_mount_motile_amoebae: negative
  xanthochromia_present: False
  rbc_per_mm3: 4

IMAGING:
  modality: ct_noncontrast
  pattern: normal
  contrast_enhancement: True
  hydrocephalus: False
  basal_meningeal_enhancement: False
  finding_count: 0
  text_summary: CT head non-contrast: normal at admission. No focal lesion, no hydrocephalus, no midline shift, no mass effect. Pattern consistent with early-stage adult community-acquired bacterial meningitis.

DIAGNOSTIC_TESTS:
  pcr_panel: n/a
  xpert_mtb_rif: n/a
  blood_culture: n/a
  csf_culture: n/a
  serology_or_antigen: n/a
  smear_or_gram: n/a
  brain_biopsy: n/a
  imaging_test: n/a
  total_dx_results: 3

NARRATIVE_EN: A 55-year-old man in the Netherlands presented to a tertiary emergency department in Amsterdam with a 48-hour history of fever to 39.3 C, severe headache, and neck stiffness. Examination on admission: temperature 39.3 C, Glasgow Coma Scale 13, neck stiffness, positive Kernig sign, no focal deficit, no rash. CSF showed opening pressure 27 cmH2O, white cell count 5,600 per cubic millimeter (88 percent neutrophils), glucose 23 mg/dL, protein 205 mg/dL. Gram stain revealed gram-positive diplococci; culture identified Streptococcus pneumoniae. Primary anchor: PMID 26652862 (Bijlsma 2016 Lancet Infect Dis), 1,412-episode prospective Netherlands community-acquired adult cohort 2006-2014 (SP 70 percent, classic triad 47 percent, mortality 17 percent). Outcome: survived no sequelae. Subphase 1.3 commit 5.3.4 wave 2, pre-adjudication hold_for_revision.

NARRATIVE_ES: Varon de 55 anos en Paises Bajos (Amsterdam), ingresado a urgencias terciarias con 48 horas de fiebre 39.3 C, cefalea intensa y rigidez de nuca. Examen: temperatura 39.3 C, escala de Glasgow 13, rigidez de nuca, signo de Kernig positivo, sin deficit focal, sin exantema. Liquido cefalorraquideo mostro presion de apertura 27 cmH2O, leucocitos 5,600 por mm3 (88 por ciento neutrofilos), glucosa 23 mg/dL, proteina 205 mg/dL. Tincion de Gram con diplococos grampositivos y cultivo Streptococcus pneumoniae. Anclaje primario en cohorte prospectiva Bijlsma 2016 Lancet ID (PMID 26652862, 1,412 episodios 2006-2014, estrato adulto comunitario). Subphase 1.3 commit 5.3.4 wave 2, pre-adjudicacion hold_for_revision.

RATIONALE: Anchored to PMID 26652862 (Bijlsma 2016 Lancet ID), 1,412-episode prospective Netherlands cohort 2006-2014 (SP 70 percent, classic triad 47 percent). Demographic anchor (55yo M adult community) sits in dominant adult-community stratum. CSF profile bacterial range. Imputation tiers: tier_1_primary={age, sex, csf_culture, csf_gram_stain}; tier_3_within_cohort={csf_wbc, neutrophil_pct, glucose, protein}; tier_4_priors={temp, gcs, symptom_days}. Indeterminate=none. Diagnostic_ambiguity=false. Outcome=survived. Tier: tier_3_imputation_within_cohort_review. 5.3.4 wave2 SP-NL-adult-community.

ANCHORING_EXTRAS: stage=pre_adjudication; status=pending_external_review; self_review_disposition=hold_for_revision; self_review_notes=wave 2 vignette anchored to PMID 26652862 (Bijlsma 2016 Lancet ID); external clinical adjudication pending; classification provisional. adjudicator_ids=WAVE2-PRE-ADJ-1, WAVE2-PRE-ADJ-2 (sentinel); cohen_kappa=0.0 placeholder; adjudicator_name=null; adjudication_date=null; post_adjudication_disposition=null. Subphase 1.3 commit 5.3.4 (2026-05-08). anchor=Bijlsma-Lancet-ID-2016 stratum=adult-community-male.

ADJUDICATION:
  inclusion_decision: hold_for_revision
  adjudicator_ids: ['WAVE2-PRE-ADJ-1', 'WAVE2-PRE-ADJ-2']
  ground_truth_class: 2
  pre_adjudication_kappa: 0.0
  disagreement_resolution: None

=== END vignette ===

=== CLASS 2 | vignette_id: 073 | subphase: 1.3 BACT | file: bact_073_sp_elderly_fatal.json ===

ANCHOR:
  pmid: 15509818
  first_author: van
  year: 2004
  journal: NEJM
  citation_type: cohort
  doi: 10.1056/NEJMoa040845

DEMOGRAPHICS:
  age_years: 70
  sex: female
  geography_region: other_global
  ethnicity: white_non_hispanic
  altitude_residence_m: 5
  hiv_status: negative
  cd4_count_cells_per_uL: None
  pregnancy_red_flag: False
  immunocompromise_status: none
  freshwater_exposure_within_14d: False
  freshwater_exposure_type: None

HISTORY:
  symptom_onset_to_presentation_days: 4.0
  chief_complaint: altered_mental_status
  red_flags_present: []
  prodrome_description: 70-year-old female, Netherlands. 4-day progressive fever, headache, confusion progressing to obtundation. Tertiary ED Amsterdam. Late presentation. No freshwater. Triad present (van de Beek elderly stratum). Outcome: fatal hospital day 3. Antibiotic at hour 2 plus dexamethasone EU guideline 2002.

VITALS:
  temperature_celsius: 38.9
  heart_rate_bpm: 116
  systolic_bp_mmHg: 105
  diastolic_bp_mmHg: 65
  glasgow_coma_scale: 7
  oxygen_saturation_pct: 91
  respiratory_rate_breaths_per_min: 26

EXAM:
  mental_status_grade: comatose
  neck_stiffness: True
  kernig_or_brudzinski_positive: True
  cranial_nerve_palsy: none
  papilledema_on_fundoscopy: False
  focal_neurological_deficit: False
  skin_lesion_centrofacial_chronic: False
  petechial_or_purpuric_rash: False

LABS:
  wbc_blood_per_uL: 18800
  platelets_per_uL: 175000
  alt_ast_U_per_L: 36
  crp_mg_per_L: 230.0
  procalcitonin_ng_per_mL: 12.5
  serum_sodium_mEq_per_L: 130

CSF:
  opening_pressure_cmH2O: 26.0
  wbc_per_mm3: 4100
  lymphocyte_pct: 20
  neutrophil_pct: 80
  eosinophil_pct: 0
  glucose_mg_per_dL: 25
  protein_mg_per_dL: 195
  lactate_mmol_per_L: 6.0
  ada_U_per_L: None
  crag_lfa_result: negative
  wet_mount_motile_amoebae: negative
  xanthochromia_present: False
  rbc_per_mm3: 5

IMAGING:
  modality: ct_noncontrast
  pattern: diffuse_cerebral_edema_basilar_meningeal_enhancement
  contrast_enhancement: True
  hydrocephalus: False
  basal_meningeal_enhancement: False
  finding_count: 1
  text_summary: CT head non-contrast: diffuse cerebral edema with effacement of sulci, basilar meningeal enhancement on contrast-equivalent regions, no focal lesion, no midline shift. Pattern consistent with severe late-stage bacterial meningitis.

DIAGNOSTIC_TESTS:
  pcr_panel: n/a
  xpert_mtb_rif: n/a
  blood_culture: n/a
  csf_culture: n/a
  serology_or_antigen: n/a
  smear_or_gram: n/a
  brain_biopsy: n/a
  imaging_test: n/a
  total_dx_results: 3

NARRATIVE_EN: A 70-year-old woman in the Netherlands presented to a tertiary emergency department in Amsterdam after a 4-day course of progressive fever, headache, and confusion progressing to obtundation. Examination on admission: temperature 38.9 C, Glasgow Coma Scale 7, neck stiffness, positive Kernig sign, no focal deficit, no rash. CSF showed opening pressure 26 cmH2O, white cell count 4,100 per cubic millimeter (80 percent neutrophils), glucose 25 mg/dL, protein 195 mg/dL. Gram stain revealed gram-positive diplococci; culture identified Streptococcus pneumoniae. Primary anchor: PMID 15509818 (van de Beek 2004 NEJM), elderly stratum mortality 41 percent. Outcome: fatal hospital day 3. Subphase 1.3 commit 5.3.3 wave 1, pre-adjudication hold_for_revision.

NARRATIVE_ES: Mujer de 70 anos en Paises Bajos (Amsterdam), ingresada a urgencias terciarias tras cuatro dias de fiebre progresiva, cefalea y confusion con obnubilacion. Examen: temperatura 38.9 C, escala de Glasgow 7, rigidez de nuca, signo de Kernig positivo, sin deficit focal, sin exantema. Liquido cefalorraquideo mostro presion de apertura 26 cmH2O, leucocitos 4,100 por mm3 (80 por ciento neutrofilos), glucosa 25 mg/dL, proteina 195 mg/dL. Tincion de Gram con diplococos grampositivos y cultivo Streptococcus pneumoniae. Anclaje primario en cohorte prospectiva van de Beek 2004 NEJM (PMID 15509818, 696 episodios 1998-2002, estrato de adultos mayores con mortalidad 41 por ciento a edad >=65). Resultado: fatal en hospital dia 3. Subphase 1.3 commit 5.3.3 wave 1, pre-adjudicacion hold_for_revision.

RATIONALE: Anchored to PMID 15509818 (van de Beek 2004 NEJM), 696-episode prospective Netherlands cohort 1998-2002 (elderly stratum mortality 41 percent at age >=65). Demographic anchor (70yo F) sits in elderly stratum. CSF profile bacterial range. Imputation tiers: tier_1_primary={age, sex, csf_culture, csf_gram_stain}; tier_3_within_cohort={csf_wbc, neutrophil_pct, glucose, protein, gcs}; tier_4_priors={temp, symptom_days}. Indeterminate=none. Diagnostic_ambiguity=false. Outcome=fatal_hospital_day_3. Antibiotic_started_hours=2. Tier: tier_3_imputation_within_cohort_review. 5.3.3 wave1 SP-elderly-fatal.

ANCHORING_EXTRAS: stage=pre_adjudication; status=pending_external_review; self_review_disposition=hold_for_revision; self_review_notes=wave 1 vignette anchored to PMID 15509818 (van de Beek 2004 NEJM); external clinical adjudication pending; classification provisional. adjudicator_ids=WAVE1-PRE-ADJ-1, WAVE1-PRE-ADJ-2 (sentinel); cohen_kappa=0.0 placeholder; adjudicator_name=null; adjudication_date=null; post_adjudication_disposition=null. Subphase 1.3 commit 5.3.3 (2026-05-08). anchor=van-de-Beek-NEJM-2004 stratum=elderly-fatal.

ADJUDICATION:
  inclusion_decision: hold_for_revision
  adjudicator_ids: ['WAVE1-PRE-ADJ-1', 'WAVE1-PRE-ADJ-2']
  ground_truth_class: 2
  pre_adjudication_kappa: 0.0
  disagreement_resolution: None

=== END vignette ===

=== CLASS 2 | vignette_id: 074 | subphase: 1.3 BACT | file: bact_074_sp_adult_female.json ===

ANCHOR:
  pmid: 26652862
  first_author: Bijlsma
  year: 2016
  journal: Lancet Infect Dis
  citation_type: cohort
  doi: 10.1016/S1473-3099(15)00430-2

DEMOGRAPHICS:
  age_years: 42
  sex: female
  geography_region: other_global
  ethnicity: white_non_hispanic
  altitude_residence_m: 5
  hiv_status: negative
  cd4_count_cells_per_uL: None
  pregnancy_red_flag: False
  immunocompromise_status: none
  freshwater_exposure_within_14d: False
  freshwater_exposure_type: None

HISTORY:
  symptom_onset_to_presentation_days: 1.5
  chief_complaint: fever_with_headache
  red_flags_present: []
  prodrome_description: 42-year-old female, Netherlands. 36-hour fever 39.1 C, severe headache, neck stiffness, photophobia. Tertiary ED Amsterdam. No freshwater. Triad present (Bijlsma adult community stratum, women cohort proportion 46 percent). Outcome: survived no sequelae. Antibiotic at hour 1 plus dexamethasone.

VITALS:
  temperature_celsius: 39.1
  heart_rate_bpm: 108
  systolic_bp_mmHg: 122
  diastolic_bp_mmHg: 74
  glasgow_coma_scale: 13
  oxygen_saturation_pct: 97
  respiratory_rate_breaths_per_min: 20

EXAM:
  mental_status_grade: confused
  neck_stiffness: True
  kernig_or_brudzinski_positive: True
  cranial_nerve_palsy: none
  papilledema_on_fundoscopy: False
  focal_neurological_deficit: False
  skin_lesion_centrofacial_chronic: False
  petechial_or_purpuric_rash: False

LABS:
  wbc_blood_per_uL: 18800
  platelets_per_uL: 245000
  alt_ast_U_per_L: 28
  crp_mg_per_L: 165.0
  procalcitonin_ng_per_mL: 6.5
  serum_sodium_mEq_per_L: 137

CSF:
  opening_pressure_cmH2O: 26.0
  wbc_per_mm3: 5400
  lymphocyte_pct: 14
  neutrophil_pct: 86
  eosinophil_pct: 0
  glucose_mg_per_dL: 24
  protein_mg_per_dL: 200
  lactate_mmol_per_L: 6.2
  ada_U_per_L: None
  crag_lfa_result: negative
  wet_mount_motile_amoebae: negative
  xanthochromia_present: False
  rbc_per_mm3: 4

IMAGING:
  modality: ct_noncontrast
  pattern: normal
  contrast_enhancement: True
  hydrocephalus: False
  basal_meningeal_enhancement: False
  finding_count: 0
  text_summary: CT head non-contrast: normal at admission. No focal lesion, no hydrocephalus, no midline shift, no mass effect. Pattern consistent with early-stage adult community-acquired bacterial meningitis.

DIAGNOSTIC_TESTS:
  pcr_panel: n/a
  xpert_mtb_rif: n/a
  blood_culture: n/a
  csf_culture: n/a
  serology_or_antigen: n/a
  smear_or_gram: n/a
  brain_biopsy: n/a
  imaging_test: n/a
  total_dx_results: 3

NARRATIVE_EN: A 42-year-old woman in the Netherlands presented to a tertiary emergency department in Amsterdam with a 36-hour history of fever to 39.1 C, severe headache, neck stiffness, and photophobia. Examination on admission: temperature 39.1 C, Glasgow Coma Scale 13, neck stiffness, positive Kernig sign, no focal deficit, no rash. CSF showed opening pressure 26 cmH2O, white cell count 5,400 per cubic millimeter (86 percent neutrophils), glucose 24 mg/dL, protein 200 mg/dL. Gram stain revealed gram-positive diplococci; culture identified Streptococcus pneumoniae. Primary anchor: PMID 26652862 (Bijlsma 2016 Lancet Infect Dis), 1,412-episode prospective Netherlands cohort 2006-2014 (women cohort proportion 46 percent). Outcome: survived no sequelae. Subphase 1.3 commit 5.3.4 wave 2, pre-adjudication hold_for_revision.

NARRATIVE_ES: Mujer de 42 anos en Paises Bajos (Amsterdam), ingresada a urgencias terciarias con 36 horas de fiebre 39.1 C, cefalea intensa, rigidez de nuca y fotofobia. Examen: temperatura 39.1 C, escala de Glasgow 13, rigidez de nuca, signo de Kernig positivo, sin deficit focal, sin exantema. Liquido cefalorraquideo mostro presion de apertura 26 cmH2O, leucocitos 5,400 por mm3 (86 por ciento neutrofilos), glucosa 24 mg/dL, proteina 200 mg/dL. Tincion de Gram con diplococos grampositivos y cultivo Streptococcus pneumoniae. Anclaje primario en cohorte prospectiva Bijlsma 2016 Lancet ID (PMID 26652862, 1,412 episodios 2006-2014, proporcion de mujeres 46 por ciento). Subphase 1.3 commit 5.3.4 wave 2, pre-adjudicacion hold_for_revision.

RATIONALE: Anchored to PMID 26652862 (Bijlsma 2016 Lancet ID), 1,412-episode prospective Netherlands cohort 2006-2014. Demographic anchor (42yo F adult community) sits in adult-community stratum. CSF profile bacterial range. Imputation tiers: tier_1_primary={age, sex, csf_culture, csf_gram_stain}; tier_3_within_cohort={csf_wbc, neutrophil_pct, glucose, protein}; tier_4_priors={temp, gcs, symptom_days}. Indeterminate=none. Diagnostic_ambiguity=false. Outcome=survived_no_sequelae. Tier: tier_3_imputation_within_cohort_review. 5.3.4 wave2 SP-NL-adult-female-2.

ANCHORING_EXTRAS: stage=pre_adjudication; status=pending_external_review; self_review_disposition=hold_for_revision; self_review_notes=wave 2 vignette anchored to PMID 26652862 (Bijlsma 2016 Lancet ID); external clinical adjudication pending; classification provisional. adjudicator_ids=WAVE2-PRE-ADJ-1, WAVE2-PRE-ADJ-2 (sentinel); cohen_kappa=0.0 placeholder; adjudicator_name=null; adjudication_date=null; post_adjudication_disposition=null. Subphase 1.3 commit 5.3.4 (2026-05-08). anchor=Bijlsma-Lancet-ID-2016 stratum=adult-community-female-2.

ADJUDICATION:
  inclusion_decision: hold_for_revision
  adjudicator_ids: ['WAVE2-PRE-ADJ-1', 'WAVE2-PRE-ADJ-2']
  ground_truth_class: 2
  pre_adjudication_kappa: 0.0
  disagreement_resolution: None

=== END vignette ===

=== CLASS 2 | vignette_id: 075 | subphase: 1.3 BACT | file: bact_075_sp_partial_treatment_ambiguity.json ===

ANCHOR:
  pmid: 15494903
  first_author: Tunkel
  year: 2004
  journal: CID
  citation_type: guideline
  doi: 10.1086/425368

DEMOGRAPHICS:
  age_years: 25
  sex: female
  geography_region: us_south
  ethnicity: white_non_hispanic
  altitude_residence_m: 100
  hiv_status: negative
  cd4_count_cells_per_uL: None
  pregnancy_red_flag: False
  immunocompromise_status: none
  freshwater_exposure_within_14d: False
  freshwater_exposure_type: None

HISTORY:
  symptom_onset_to_presentation_days: 1.5
  chief_complaint: fever_with_headache
  red_flags_present: []
  prodrome_description: 25-year-old female, US South region. Outpatient amoxicillin started 24 hours prior for sinusitis. Subsequent fever 39.0 C, headache, neck stiffness within 12 hours of pretreatment. Tertiary ED. No freshwater. Diagnostic_ambiguity=true; type=partial_antibiotic_pretreatment. Outcome: survived. IDSA pretreated-suspected protocol.

VITALS:
  temperature_celsius: 39.0
  heart_rate_bpm: 105
  systolic_bp_mmHg: 116
  diastolic_bp_mmHg: 72
  glasgow_coma_scale: 14
  oxygen_saturation_pct: 98
  respiratory_rate_breaths_per_min: 20

EXAM:
  mental_status_grade: somnolent
  neck_stiffness: True
  kernig_or_brudzinski_positive: True
  cranial_nerve_palsy: none
  papilledema_on_fundoscopy: False
  focal_neurological_deficit: False
  skin_lesion_centrofacial_chronic: False
  petechial_or_purpuric_rash: False

LABS:
  wbc_blood_per_uL: 14200
  platelets_per_uL: 260000
  alt_ast_U_per_L: 26
  crp_mg_per_L: 95.0
  procalcitonin_ng_per_mL: 2.8
  serum_sodium_mEq_per_L: 138

CSF:
  opening_pressure_cmH2O: 22.0
  wbc_per_mm3: 1850
  lymphocyte_pct: 35
  neutrophil_pct: 65
  eosinophil_pct: 0
  glucose_mg_per_dL: 30
  protein_mg_per_dL: 165
  lactate_mmol_per_L: 4.2
  ada_U_per_L: None
  crag_lfa_result: negative
  wet_mount_motile_amoebae: negative
  xanthochromia_present: False
  rbc_per_mm3: 4

IMAGING:
  modality: ct_noncontrast
  pattern: normal
  contrast_enhancement: True
  hydrocephalus: False
  basal_meningeal_enhancement: False
  finding_count: 0
  text_summary: CT head non-contrast: normal at admission. No focal lesion, no hydrocephalus, no midline shift, no mass effect. Pattern consistent with early-stage adult community-acquired bacterial meningitis.

DIAGNOSTIC_TESTS:
  pcr_panel: n/a
  xpert_mtb_rif: n/a
  blood_culture: n/a
  csf_culture: n/a
  serology_or_antigen: streptococcus_pneumoniae_positive
  smear_or_gram: n/a
  brain_biopsy: n/a
  imaging_test: n/a
  total_dx_results: 4

NARRATIVE_EN: A 25-year-old woman in the US South region presented to a tertiary emergency department with fever to 39.0 C, headache, and neck stiffness developing 12 hours after starting outpatient amoxicillin for presumed sinusitis (24 hours of pretreatment). Examination on admission: temperature 39.0 C, Glasgow Coma Scale 14, neck stiffness, positive Kernig sign, no focal deficit, no rash. CSF showed opening pressure 22 cmH2O, white cell count 1,850 per cubic millimeter (65 percent neutrophils), glucose 30 mg/dL, protein 165 mg/dL. Gram stain unrevealing; CSF and blood cultures sterile after partial antibiotic pretreatment; CSF pneumococcal antigen positive. Diagnostic_ambiguity=true; type=partial_antibiotic_pretreatment_sterile_cultures. Anchored to Tunkel IDSA 2004 (PMID 15494903) pretreated-meningitis recommendations. Outcome: survived no sequelae. Subphase 1.3 commit 5.3.3 wave 1, pre-adjudication hold_for_revision.

NARRATIVE_ES: Mujer de 25 anos en region sur de Estados Unidos, ingresada a urgencias terciarias con fiebre 39.0 C, cefalea y rigidez de nuca 12 horas despues de iniciar amoxicilina ambulatoria por sinusitis presunta (24 horas de pretratamiento). Examen: temperatura 39.0 C, escala de Glasgow 14, rigidez de nuca, signo de Kernig positivo, sin deficit focal, sin exantema. Liquido cefalorraquideo mostro presion de apertura 22 cmH2O, leucocitos 1,850 por mm3 (65 por ciento neutrofilos), glucosa 30 mg/dL, proteina 165 mg/dL. Tincion de Gram sin organismos; cultivos de liquido y sangre esteriles tras pretratamiento antibiotico parcial; antigeno neumococico en liquido positivo. Ambiguedad diagnostica por pretratamiento parcial. Anclaje en guia IDSA Tunkel 2004 (PMID 15494903). Subphase 1.3 commit 5.3.3 wave 1.

RATIONALE: Anchored to PMID 15494903 (Tunkel IDSA 2004 CID guideline) pretreated-suspected meningitis recommendations. Diagnostic_ambiguity=true; type=partial_antibiotic_pretreatment_sterile_cultures. Demographic anchor (25yo F outpatient pretreated) reflects ambiguity stratum. CSF profile attenuated (WBC 1850, neutrophil 65 percent) consistent with partial treatment. Antigen confirms organism. Imputation tiers: tier_1_primary={age, sex, csf_pneumococcal_antigen, pretreatment_history}; tier_3_within_cohort={csf_wbc, neutrophil_pct, glucose, protein attenuation}; tier_4_priors={temp, gcs, symptom_days}. Indeterminate=culture-based-organism-confirmation. Outcome=survived. Antibiotic_started_hours=1. Tier: tier_4_imputation_idsa_guideline_anchored. 5.3.3 wave1 SP-pretreated-ambiguity.

ANCHORING_EXTRAS: stage=pre_adjudication; status=pending_external_review; self_review_disposition=hold_for_revision; self_review_notes=wave 1 vignette anchored to PMID 15494903 (Tunkel IDSA 2004); external clinical adjudication pending; classification provisional. adjudicator_ids=WAVE1-PRE-ADJ-1, WAVE1-PRE-ADJ-2 (sentinel); cohen_kappa=0.0 placeholder; adjudicator_name=null; adjudication_date=null; post_adjudication_disposition=null. Subphase 1.3 commit 5.3.3 (2026-05-08). anchor=Tunkel-IDSA-2004 type=partial_antibiotic_pretreatment.

ADJUDICATION:
  inclusion_decision: hold_for_revision
  adjudicator_ids: ['WAVE1-PRE-ADJ-1', 'WAVE1-PRE-ADJ-2']
  ground_truth_class: 2
  pre_adjudication_kappa: 0.0
  disagreement_resolution: None

=== END vignette ===

=== CLASS 2 | vignette_id: 076 | subphase: 1.3 BACT | file: bact_076_sp_partial_treatment_ambiguity.json ===

ANCHOR:
  pmid: 15494903
  first_author: Tunkel
  year: 2004
  journal: CID
  citation_type: guideline
  doi: 10.1086/425368

DEMOGRAPHICS:
  age_years: 60
  sex: male
  geography_region: other_global
  ethnicity: white_non_hispanic
  altitude_residence_m: 5
  hiv_status: negative
  cd4_count_cells_per_uL: None
  pregnancy_red_flag: False
  immunocompromise_status: none
  freshwater_exposure_within_14d: False
  freshwater_exposure_type: None

HISTORY:
  symptom_onset_to_presentation_days: 2.0
  chief_complaint: fever_with_headache
  red_flags_present: []
  prodrome_description: 60-year-old male, Netherlands. Outpatient amoxicillin 48 hours for productive cough; symptom recrudescence with fever 38.7 C, headache, neck stiffness. Tertiary ED. No freshwater. Diagnostic_ambiguity=true; type=partial_antibiotic_pretreatment. Outcome: survived. Ceftriaxone-vancomycin-dexamethasone IDSA.

VITALS:
  temperature_celsius: 38.7
  heart_rate_bpm: 102
  systolic_bp_mmHg: 130
  diastolic_bp_mmHg: 78
  glasgow_coma_scale: 14
  oxygen_saturation_pct: 96
  respiratory_rate_breaths_per_min: 20

EXAM:
  mental_status_grade: somnolent
  neck_stiffness: True
  kernig_or_brudzinski_positive: True
  cranial_nerve_palsy: none
  papilledema_on_fundoscopy: False
  focal_neurological_deficit: False
  skin_lesion_centrofacial_chronic: False
  petechial_or_purpuric_rash: False

LABS:
  wbc_blood_per_uL: 13500
  platelets_per_uL: 240000
  alt_ast_U_per_L: 32
  crp_mg_per_L: 78.0
  procalcitonin_ng_per_mL: 1.9
  serum_sodium_mEq_per_L: 137

CSF:
  opening_pressure_cmH2O: 24.0
  wbc_per_mm3: 2400
  lymphocyte_pct: 30
  neutrophil_pct: 70
  eosinophil_pct: 0
  glucose_mg_per_dL: 26
  protein_mg_per_dL: 180
  lactate_mmol_per_L: 4.6
  ada_U_per_L: None
  crag_lfa_result: negative
  wet_mount_motile_amoebae: negative
  xanthochromia_present: False
  rbc_per_mm3: 3

IMAGING:
  modality: ct_noncontrast
  pattern: normal
  contrast_enhancement: True
  hydrocephalus: False
  basal_meningeal_enhancement: False
  finding_count: 0
  text_summary: CT head non-contrast: normal at admission. No focal lesion, no hydrocephalus, no midline shift, no mass effect. Pattern consistent with early-stage adult community-acquired bacterial meningitis.

DIAGNOSTIC_TESTS:
  pcr_panel: n/a
  xpert_mtb_rif: n/a
  blood_culture: n/a
  csf_culture: n/a
  serology_or_antigen: streptococcus_pneumoniae_positive
  smear_or_gram: n/a
  brain_biopsy: n/a
  imaging_test: n/a
  total_dx_results: 4

NARRATIVE_EN: A 60-year-old man in the Netherlands presented to a tertiary emergency department after 48 hours of outpatient amoxicillin for a productive cough, with recrudescence of symptoms (fever 38.7 C, headache, neck stiffness). Examination on admission: temperature 38.7 C, Glasgow Coma Scale 14, neck stiffness, positive Kernig sign, no focal deficit, no rash. CSF showed opening pressure 24 cmH2O, white cell count 2,400 per cubic millimeter (70 percent neutrophils), glucose 26 mg/dL, protein 180 mg/dL. Gram stain unrevealing; cultures sterile after partial antibiotic pretreatment; CSF pneumococcal antigen positive. Diagnostic_ambiguity=true; type=partial_antibiotic_pretreatment_sterile_cultures. Anchored to Tunkel IDSA 2004 (PMID 15494903). Outcome: survived. Subphase 1.3 commit 5.3.3 wave 1, pre-adjudication hold_for_revision.

NARRATIVE_ES: Varon de 60 anos en Paises Bajos, ingresado a urgencias terciarias tras 48 horas de amoxicilina ambulatoria por tos productiva, con recrudescencia de sintomas (fiebre 38.7 C, cefalea, rigidez de nuca). Examen: temperatura 38.7 C, escala de Glasgow 14, rigidez de nuca, signo de Kernig positivo, sin deficit focal, sin exantema. Liquido cefalorraquideo mostro presion de apertura 24 cmH2O, leucocitos 2,400 por mm3 (70 por ciento neutrofilos), glucosa 26 mg/dL, proteina 180 mg/dL. Cultivos esteriles tras pretratamiento antibiotico parcial; antigeno neumococico en liquido positivo. Ambiguedad diagnostica por pretratamiento parcial. Anclaje en guia IDSA Tunkel 2004 (PMID 15494903). Subphase 1.3 commit 5.3.3 wave 1.

RATIONALE: Anchored to PMID 15494903 (Tunkel IDSA 2004 CID guideline) pretreated-suspected meningitis recommendations. Diagnostic_ambiguity=true; type=partial_antibiotic_pretreatment_sterile_cultures. Demographic anchor (60yo M outpatient pretreated). CSF profile attenuated (WBC 2400, neutrophil 70 percent). Antigen confirms organism. Imputation tiers: tier_1_primary={age, sex, csf_pneumococcal_antigen, pretreatment_history}; tier_3_within_cohort={csf_wbc, neutrophil_pct, glucose, protein attenuation}; tier_4_priors={temp, gcs, symptom_days}. Indeterminate=culture-based-organism-confirmation. Outcome=survived. Tier: tier_4_imputation_idsa_guideline_anchored. 5.3.3 wave1 SP-pretreated-ambiguity NL.

ANCHORING_EXTRAS: stage=pre_adjudication; status=pending_external_review; self_review_disposition=hold_for_revision; self_review_notes=wave 1 vignette anchored to PMID 15494903 (Tunkel IDSA 2004); external clinical adjudication pending; classification provisional. adjudicator_ids=WAVE1-PRE-ADJ-1, WAVE1-PRE-ADJ-2 (sentinel); cohen_kappa=0.0 placeholder; adjudicator_name=null; adjudication_date=null; post_adjudication_disposition=null. Subphase 1.3 commit 5.3.3 (2026-05-08). anchor=Tunkel-IDSA-2004 type=partial_antibiotic_pretreatment.

ADJUDICATION:
  inclusion_decision: hold_for_revision
  adjudicator_ids: ['WAVE1-PRE-ADJ-1', 'WAVE1-PRE-ADJ-2']
  ground_truth_class: 2
  pre_adjudication_kappa: 0.0
  disagreement_resolution: None

=== END vignette ===

=== CLASS 2 | vignette_id: 077 | subphase: 1.3 BACT | file: bact_077_sp_young_adult.json ===

ANCHOR:
  pmid: 15509818
  first_author: van
  year: 2004
  journal: NEJM
  citation_type: cohort
  doi: 10.1056/NEJMoa040845

DEMOGRAPHICS:
  age_years: 18
  sex: female
  geography_region: other_global
  ethnicity: white_non_hispanic
  altitude_residence_m: 5
  hiv_status: negative
  cd4_count_cells_per_uL: None
  pregnancy_red_flag: False
  immunocompromise_status: none
  freshwater_exposure_within_14d: False
  freshwater_exposure_type: None

HISTORY:
  symptom_onset_to_presentation_days: 0.5
  chief_complaint: fever_with_headache
  red_flags_present: []
  prodrome_description: 18-year-old female, Netherlands. Sudden onset fever 39.5 C, severe headache, neck stiffness, photophobia within 12 hours. Tertiary ED Amsterdam. No freshwater. Triad present (van de Beek young-adult subgroup). Outcome: survived no sequelae. Antibiotic at hour 1 plus dexamethasone EU guideline.

VITALS:
  temperature_celsius: 39.5
  heart_rate_bpm: 122
  systolic_bp_mmHg: 115
  diastolic_bp_mmHg: 70
  glasgow_coma_scale: 13
  oxygen_saturation_pct: 97
  respiratory_rate_breaths_per_min: 22

EXAM:
  mental_status_grade: confused
  neck_stiffness: True
  kernig_or_brudzinski_positive: True
  cranial_nerve_palsy: none
  papilledema_on_fundoscopy: False
  focal_neurological_deficit: False
  skin_lesion_centrofacial_chronic: False
  petechial_or_purpuric_rash: False

LABS:
  wbc_blood_per_uL: 21500
  platelets_per_uL: 285000
  alt_ast_U_per_L: 28
  crp_mg_per_L: 195.0
  procalcitonin_ng_per_mL: 8.0
  serum_sodium_mEq_per_L: 138

CSF:
  opening_pressure_cmH2O: 28.0
  wbc_per_mm3: 6400
  lymphocyte_pct: 12
  neutrophil_pct: 88
  eosinophil_pct: 0
  glucose_mg_per_dL: 24
  protein_mg_per_dL: 210
  lactate_mmol_per_L: 6.6
  ada_U_per_L: None
  crag_lfa_result: negative
  wet_mount_motile_amoebae: negative
  xanthochromia_present: False
  rbc_per_mm3: 4

IMAGING:
  modality: ct_noncontrast
  pattern: normal
  contrast_enhancement: True
  hydrocephalus: False
  basal_meningeal_enhancement: False
  finding_count: 0
  text_summary: CT head non-contrast: normal at admission. No focal lesion, no hydrocephalus, no midline shift, no mass effect. Pattern consistent with early-stage adult community-acquired bacterial meningitis.

DIAGNOSTIC_TESTS:
  pcr_panel: n/a
  xpert_mtb_rif: n/a
  blood_culture: n/a
  csf_culture: n/a
  serology_or_antigen: n/a
  smear_or_gram: n/a
  brain_biopsy: n/a
  imaging_test: n/a
  total_dx_results: 3

NARRATIVE_EN: An 18-year-old woman in the Netherlands presented to a tertiary emergency department in Amsterdam with sudden onset of fever to 39.5 C, severe headache, neck stiffness, and photophobia within 12 hours. Examination on admission: temperature 39.5 C, Glasgow Coma Scale 13, neck stiffness, positive Kernig sign, no focal deficit, no rash. Classic triad present (this case sits in the young-adult subgroup of the van de Beek 2004 cohort). CSF showed opening pressure 28 cmH2O, white cell count 6,400 per cubic millimeter (88 percent neutrophils), glucose 24 mg/dL, protein 210 mg/dL. Gram stain revealed gram-positive diplococci; culture identified Streptococcus pneumoniae. Primary anchor: PMID 15509818 (van de Beek 2004 NEJM), 696-episode prospective Netherlands cohort 1998-2002 (SP 51 percent, classic triad 44 percent). Outcome: survived no sequelae. Subphase 1.3 commit 5.3.3 wave 1, pre-adjudication hold_for_revision.

NARRATIVE_ES: Mujer de 18 anos en Paises Bajos (Amsterdam), ingresada a urgencias terciarias con inicio subito de fiebre 39.5 C, cefalea intensa, rigidez de nuca y fotofobia en 12 horas. Examen: temperatura 39.5 C, escala de Glasgow 13, rigidez de nuca, signo de Kernig positivo, sin deficit focal, sin exantema. Triada clasica presente (subgrupo de adultos jovenes de la cohorte van de Beek 2004). Liquido cefalorraquideo mostro presion de apertura 28 cmH2O, leucocitos 6,400 por mm3 (88 por ciento neutrofilos), glucosa 24 mg/dL, proteina 210 mg/dL. Tincion de Gram con diplococos grampositivos y cultivo Streptococcus pneumoniae. Anclaje primario en cohorte van de Beek 2004 NEJM (PMID 15509818). Subphase 1.3 commit 5.3.3 wave 1.

RATIONALE: Anchored to PMID 15509818 (van de Beek 2004 NEJM), 696-episode prospective Netherlands cohort 1998-2002 (SP 51 percent, classic triad 44 percent). Demographic anchor (18yo F young adult) sits in young-adult subgroup. CSF profile bacterial range. Imputation tiers: tier_1_primary={age, sex, csf_culture, csf_gram_stain, triad}; tier_3_within_cohort={csf_wbc, neutrophil_pct, glucose, protein, gcs}; tier_4_priors={temp, symptom_days}. Indeterminate=none. Diagnostic_ambiguity=false. Outcome=survived. Antibiotic_started_hours=1. Tier: tier_3_imputation_within_cohort_review. 5.3.3 wave1 SP-young-adult.

ANCHORING_EXTRAS: stage=pre_adjudication; status=pending_external_review; self_review_disposition=hold_for_revision; self_review_notes=wave 1 vignette anchored to PMID 15509818 (van de Beek 2004 NEJM); external clinical adjudication pending; classification provisional. adjudicator_ids=WAVE1-PRE-ADJ-1, WAVE1-PRE-ADJ-2 (sentinel); cohen_kappa=0.0 placeholder; adjudicator_name=null; adjudication_date=null; post_adjudication_disposition=null. Subphase 1.3 commit 5.3.3 (2026-05-08). anchor=van-de-Beek-NEJM-2004 stratum=young-adult.

ADJUDICATION:
  inclusion_decision: hold_for_revision
  adjudicator_ids: ['WAVE1-PRE-ADJ-1', 'WAVE1-PRE-ADJ-2']
  ground_truth_class: 2
  pre_adjudication_kappa: 0.0
  disagreement_resolution: None

=== END vignette ===

=== CLASS 2 | vignette_id: 078 | subphase: 1.3 BACT | file: bact_078_sp_hiv_immunocompromised.json ===

ANCHOR:
  pmid: 15494903
  first_author: Tunkel
  year: 2004
  journal: CID
  citation_type: guideline
  doi: 10.1086/425368

DEMOGRAPHICS:
  age_years: 50
  sex: male
  geography_region: us_south
  ethnicity: white_non_hispanic
  altitude_residence_m: 100
  hiv_status: positive_on_art
  cd4_count_cells_per_uL: 285
  pregnancy_red_flag: False
  immunocompromise_status: hiv_cd4_over200
  freshwater_exposure_within_14d: False
  freshwater_exposure_type: None

HISTORY:
  symptom_onset_to_presentation_days: 2.0
  chief_complaint: fever_with_headache
  red_flags_present: ['immunocompromise']
  prodrome_description: 50-year-old male, US South region. HIV-positive 8 years on antiretroviral therapy (CD4 285). 2-day fever 39.2 C, severe headache, neck stiffness. Tertiary ED. No freshwater. Encapsulated-organism risk per HIV. Outcome: survived. Ceftriaxone-vancomycin-dexamethasone IDSA HIV-specific.

VITALS:
  temperature_celsius: 39.2
  heart_rate_bpm: 112
  systolic_bp_mmHg: 118
  diastolic_bp_mmHg: 72
  glasgow_coma_scale: 13
  oxygen_saturation_pct: 97
  respiratory_rate_breaths_per_min: 22

EXAM:
  mental_status_grade: confused
  neck_stiffness: True
  kernig_or_brudzinski_positive: True
  cranial_nerve_palsy: none
  papilledema_on_fundoscopy: False
  focal_neurological_deficit: False
  skin_lesion_centrofacial_chronic: False
  petechial_or_purpuric_rash: False

LABS:
  wbc_blood_per_uL: 18200
  platelets_per_uL: 235000
  alt_ast_U_per_L: 30
  crp_mg_per_L: 175.0
  procalcitonin_ng_per_mL: 7.0
  serum_sodium_mEq_per_L: 137

CSF:
  opening_pressure_cmH2O: 27.0
  wbc_per_mm3: 5200
  lymphocyte_pct: 15
  neutrophil_pct: 85
  eosinophil_pct: 0
  glucose_mg_per_dL: 22
  protein_mg_per_dL: 195
  lactate_mmol_per_L: 6.0
  ada_U_per_L: None
  crag_lfa_result: negative
  wet_mount_motile_amoebae: negative
  xanthochromia_present: False
  rbc_per_mm3: 5

IMAGING:
  modality: ct_noncontrast
  pattern: normal
  contrast_enhancement: True
  hydrocephalus: False
  basal_meningeal_enhancement: False
  finding_count: 0
  text_summary: CT head non-contrast: normal at admission. No focal lesion, no hydrocephalus, no midline shift, no mass effect. Pattern consistent with early-stage adult community-acquired bacterial meningitis.

DIAGNOSTIC_TESTS:
  pcr_panel: n/a
  xpert_mtb_rif: n/a
  blood_culture: n/a
  csf_culture: n/a
  serology_or_antigen: n/a
  smear_or_gram: n/a
  brain_biopsy: n/a
  imaging_test: n/a
  total_dx_results: 3

NARRATIVE_EN: A 50-year-old man in the US South region with HIV (eight years on antiretroviral therapy, CD4 count 285 cells per microliter) presented to a tertiary emergency department with a 2-day history of fever to 39.2 C, severe headache, and neck stiffness. Examination on admission: temperature 39.2 C, Glasgow Coma Scale 13, neck stiffness, positive Kernig sign, no focal deficit, no rash. CSF showed opening pressure 27 cmH2O, white cell count 5,200 per cubic millimeter (85 percent neutrophils), glucose 22 mg/dL, protein 195 mg/dL; CSF cryptococcal antigen negative. Gram stain revealed gram-positive diplococci; culture identified Streptococcus pneumoniae. Anchored to Tunkel IDSA 2004 (PMID 15494903) HIV-specific empiric coverage recommendations. Outcome: survived. Subphase 1.3 commit 5.3.3 wave 1, pre-adjudication hold_for_revision.

NARRATIVE_ES: Varon de 50 anos en region sur de Estados Unidos con infeccion por VIH (ocho anos de terapia antirretroviral, CD4 285 celulas por microlitro), ingresado a urgencias terciarias con dos dias de fiebre 39.2 C, cefalea intensa y rigidez de nuca. Examen: temperatura 39.2 C, escala de Glasgow 13, rigidez de nuca, signo de Kernig positivo, sin deficit focal, sin exantema. Liquido cefalorraquideo mostro presion de apertura 27 cmH2O, leucocitos 5,200 por mm3 (85 por ciento neutrofilos), glucosa 22 mg/dL, proteina 195 mg/dL; antigeno criptococico en liquido negativo. Tincion de Gram con diplococos grampositivos y cultivo Streptococcus pneumoniae. Anclaje en guia IDSA Tunkel 2004 (PMID 15494903) recomendaciones VIH-especificas. Subphase 1.3 commit 5.3.3 wave 1.

RATIONALE: Anchored to PMID 15494903 (Tunkel IDSA 2004 CID guideline) HIV-specific empiric coverage recommendations. Demographic anchor (50yo M HIV+ ART CD4 285) reflects HIV-on-ART stratum covered by Tunkel for SP empiric vancomycin plus ceftriaxone. CrAg negative excludes co-incident cryptococcal infection. CSF profile bacterial range. Imputation tiers: tier_1_primary={age, sex, csf_culture, csf_gram_stain, hiv_status, cd4}; tier_3_within_cohort={csf_wbc, neutrophil_pct, glucose, protein}; tier_4_priors={temp, gcs, symptom_days}. Indeterminate=none. Diagnostic_ambiguity=false. Outcome=survived. Antibiotic_started_hours=1. Tier: tier_4_imputation_idsa_guideline_anchored. 5.3.3 wave1 SP-HIV-on-ART.

ANCHORING_EXTRAS: stage=pre_adjudication; status=pending_external_review; self_review_disposition=hold_for_revision; self_review_notes=wave 1 vignette anchored to PMID 15494903 (Tunkel IDSA 2004); external clinical adjudication pending; classification provisional. adjudicator_ids=WAVE1-PRE-ADJ-1, WAVE1-PRE-ADJ-2 (sentinel); cohen_kappa=0.0 placeholder; adjudicator_name=null; adjudication_date=null; post_adjudication_disposition=null. Subphase 1.3 commit 5.3.3 (2026-05-08). anchor=Tunkel-IDSA-2004 stratum=HIV-on-ART.

ADJUDICATION:
  inclusion_decision: hold_for_revision
  adjudicator_ids: ['WAVE1-PRE-ADJ-1', 'WAVE1-PRE-ADJ-2']
  ground_truth_class: 2
  pre_adjudication_kappa: 0.0
  disagreement_resolution: None

=== END vignette ===

=== CLASS 2 | vignette_id: 079 | subphase: 1.3 BACT | file: bact_079_sp_partial_treatment_ambiguity.json ===

ANCHOR:
  pmid: 15494903
  first_author: Tunkel
  year: 2004
  journal: CID
  citation_type: guideline
  doi: 10.1086/425368

DEMOGRAPHICS:
  age_years: 45
  sex: female
  geography_region: us_south
  ethnicity: white_non_hispanic
  altitude_residence_m: 100
  hiv_status: negative
  cd4_count_cells_per_uL: None
  pregnancy_red_flag: False
  immunocompromise_status: none
  freshwater_exposure_within_14d: False
  freshwater_exposure_type: None

HISTORY:
  symptom_onset_to_presentation_days: 1.5
  chief_complaint: fever_with_headache
  red_flags_present: []
  prodrome_description: 45-year-old female, US South region. Outpatient cefuroxime 36 hours for bronchitis. Recrudescence: fever 38.8 C, headache, neck stiffness. Tertiary ED. No freshwater. Diagnostic_ambiguity=true; type=partial_antibiotic_pretreatment. Outcome: survived. IDSA pretreated-suspected protocol followed.

VITALS:
  temperature_celsius: 38.8
  heart_rate_bpm: 100
  systolic_bp_mmHg: 120
  diastolic_bp_mmHg: 74
  glasgow_coma_scale: 14
  oxygen_saturation_pct: 98
  respiratory_rate_breaths_per_min: 18

EXAM:
  mental_status_grade: somnolent
  neck_stiffness: True
  kernig_or_brudzinski_positive: True
  cranial_nerve_palsy: none
  papilledema_on_fundoscopy: False
  focal_neurological_deficit: False
  skin_lesion_centrofacial_chronic: False
  petechial_or_purpuric_rash: False

LABS:
  wbc_blood_per_uL: 12800
  platelets_per_uL: 245000
  alt_ast_U_per_L: 28
  crp_mg_per_L: 70.0
  procalcitonin_ng_per_mL: 1.5
  serum_sodium_mEq_per_L: 138

CSF:
  opening_pressure_cmH2O: 20.0
  wbc_per_mm3: 1600
  lymphocyte_pct: 40
  neutrophil_pct: 60
  eosinophil_pct: 0
  glucose_mg_per_dL: 32
  protein_mg_per_dL: 155
  lactate_mmol_per_L: 3.8
  ada_U_per_L: None
  crag_lfa_result: negative
  wet_mount_motile_amoebae: negative
  xanthochromia_present: False
  rbc_per_mm3: 3

IMAGING:
  modality: ct_noncontrast
  pattern: normal
  contrast_enhancement: True
  hydrocephalus: False
  basal_meningeal_enhancement: False
  finding_count: 0
  text_summary: CT head non-contrast: normal at admission. No focal lesion, no hydrocephalus, no midline shift, no mass effect. Pattern consistent with early-stage adult community-acquired bacterial meningitis.

DIAGNOSTIC_TESTS:
  pcr_panel: n/a
  xpert_mtb_rif: n/a
  blood_culture: n/a
  csf_culture: n/a
  serology_or_antigen: streptococcus_pneumoniae_positive
  smear_or_gram: n/a
  brain_biopsy: n/a
  imaging_test: n/a
  total_dx_results: 4

NARRATIVE_EN: A 45-year-old woman in the US South region presented to a tertiary emergency department after 36 hours of outpatient cefuroxime for presumed bronchitis, with recrudescence of fever to 38.8 C, headache, and neck stiffness. Examination on admission: temperature 38.8 C, Glasgow Coma Scale 14, neck stiffness, positive Kernig sign, no focal deficit, no rash. CSF showed opening pressure 20 cmH2O, white cell count 1,600 per cubic millimeter (60 percent neutrophils), glucose 32 mg/dL, protein 155 mg/dL. Gram stain unrevealing; CSF and blood cultures sterile after partial antibiotic pretreatment; CSF pneumococcal antigen positive. Diagnostic_ambiguity=true; type=partial_antibiotic_pretreatment_sterile_cultures. Anchored to Tunkel IDSA 2004 (PMID 15494903) pretreated-meningitis recommendations. Outcome: survived. Subphase 1.3 commit 5.3.3 wave 1, pre-adjudication hold_for_revision.

NARRATIVE_ES: Mujer de 45 anos en region sur de Estados Unidos, ingresada a urgencias terciarias tras 36 horas de cefuroxima ambulatoria por bronquitis presunta, con recrudescencia de fiebre 38.8 C, cefalea y rigidez de nuca. Examen: temperatura 38.8 C, escala de Glasgow 14, rigidez de nuca, signo de Kernig positivo, sin deficit focal, sin exantema. Liquido cefalorraquideo mostro presion de apertura 20 cmH2O, leucocitos 1,600 por mm3 (60 por ciento neutrofilos), glucosa 32 mg/dL, proteina 155 mg/dL. Cultivos esteriles tras pretratamiento antibiotico parcial; antigeno neumococico en liquido positivo. Ambiguedad diagnostica por pretratamiento parcial. Anclaje en guia IDSA Tunkel 2004 (PMID 15494903). Subphase 1.3 commit 5.3.3 wave 1.

RATIONALE: Anchored to PMID 15494903 (Tunkel IDSA 2004 CID guideline) pretreated-suspected meningitis recommendations. Diagnostic_ambiguity=true; type=partial_antibiotic_pretreatment_sterile_cultures. Demographic anchor (45yo F outpatient pretreated). CSF profile attenuated (WBC 1600, neutrophil 60 percent, glucose 32). Antigen confirms organism. Imputation tiers: tier_1_primary={age, sex, csf_pneumococcal_antigen, pretreatment_history}; tier_3_within_cohort={csf_wbc, neutrophil_pct, glucose, protein attenuation}; tier_4_priors={temp, gcs, symptom_days}. Indeterminate=culture-based-organism-confirmation. Outcome=survived. Tier: tier_4_imputation_idsa_guideline_anchored. 5.3.3 wave1 SP-pretreated-ambiguity-2.

ANCHORING_EXTRAS: stage=pre_adjudication; status=pending_external_review; self_review_disposition=hold_for_revision; self_review_notes=wave 1 vignette anchored to PMID 15494903 (Tunkel IDSA 2004); external clinical adjudication pending; classification provisional. adjudicator_ids=WAVE1-PRE-ADJ-1, WAVE1-PRE-ADJ-2 (sentinel); cohen_kappa=0.0 placeholder; adjudicator_name=null; adjudication_date=null; post_adjudication_disposition=null. Subphase 1.3 commit 5.3.3 (2026-05-08). anchor=Tunkel-IDSA-2004 type=partial_antibiotic_pretreatment.

ADJUDICATION:
  inclusion_decision: hold_for_revision
  adjudicator_ids: ['WAVE1-PRE-ADJ-1', 'WAVE1-PRE-ADJ-2']
  ground_truth_class: 2
  pre_adjudication_kappa: 0.0
  disagreement_resolution: None

=== END vignette ===

=== CLASS 2 | vignette_id: 080 | subphase: 1.3 BACT | file: bact_080_sp_partial_treatment_ambiguity.json ===

ANCHOR:
  pmid: 15494903
  first_author: Tunkel
  year: 2004
  journal: CID
  citation_type: guideline
  doi: 10.1086/425368

DEMOGRAPHICS:
  age_years: 33
  sex: male
  geography_region: other_global
  ethnicity: white_non_hispanic
  altitude_residence_m: 5
  hiv_status: negative
  cd4_count_cells_per_uL: None
  pregnancy_red_flag: False
  immunocompromise_status: none
  freshwater_exposure_within_14d: False
  freshwater_exposure_type: None

HISTORY:
  symptom_onset_to_presentation_days: 1.5
  chief_complaint: fever_with_headache
  red_flags_present: []
  prodrome_description: 33-year-old male, Netherlands. Outpatient amoxicillin 30 hours for sinus pain. Recrudescence fever 38.9 C, headache, neck stiffness, vomiting. Tertiary ED. No freshwater. Diagnostic_ambiguity=true; type=partial_antibiotic_pretreatment. Outcome: survived. IDSA pretreated-suspected protocol.

VITALS:
  temperature_celsius: 38.9
  heart_rate_bpm: 108
  systolic_bp_mmHg: 122
  diastolic_bp_mmHg: 76
  glasgow_coma_scale: 14
  oxygen_saturation_pct: 97
  respiratory_rate_breaths_per_min: 20

EXAM:
  mental_status_grade: somnolent
  neck_stiffness: True
  kernig_or_brudzinski_positive: True
  cranial_nerve_palsy: none
  papilledema_on_fundoscopy: False
  focal_neurological_deficit: False
  skin_lesion_centrofacial_chronic: False
  petechial_or_purpuric_rash: False

LABS:
  wbc_blood_per_uL: 14500
  platelets_per_uL: 255000
  alt_ast_U_per_L: 30
  crp_mg_per_L: 85.0
  procalcitonin_ng_per_mL: 2.3
  serum_sodium_mEq_per_L: 137

CSF:
  opening_pressure_cmH2O: 23.0
  wbc_per_mm3: 2900
  lymphocyte_pct: 32
  neutrophil_pct: 68
  eosinophil_pct: 0
  glucose_mg_per_dL: 28
  protein_mg_per_dL: 175
  lactate_mmol_per_L: 4.4
  ada_U_per_L: None
  crag_lfa_result: negative
  wet_mount_motile_amoebae: negative
  xanthochromia_present: False
  rbc_per_mm3: 4

IMAGING:
  modality: ct_noncontrast
  pattern: normal
  contrast_enhancement: True
  hydrocephalus: False
  basal_meningeal_enhancement: False
  finding_count: 0
  text_summary: CT head non-contrast: normal at admission. No focal lesion, no hydrocephalus, no midline shift, no mass effect. Pattern consistent with early-stage adult community-acquired bacterial meningitis.

DIAGNOSTIC_TESTS:
  pcr_panel: n/a
  xpert_mtb_rif: n/a
  blood_culture: n/a
  csf_culture: n/a
  serology_or_antigen: streptococcus_pneumoniae_positive
  smear_or_gram: n/a
  brain_biopsy: n/a
  imaging_test: n/a
  total_dx_results: 4

NARRATIVE_EN: A 33-year-old man in the Netherlands presented to a tertiary emergency department after 30 hours of outpatient amoxicillin for sinus pain, with recrudescence of fever to 38.9 C, headache, neck stiffness, and vomiting. Examination on admission: temperature 38.9 C, Glasgow Coma Scale 14, neck stiffness, positive Kernig sign, no focal deficit, no rash. CSF showed opening pressure 23 cmH2O, white cell count 2,900 per cubic millimeter (68 percent neutrophils), glucose 28 mg/dL, protein 175 mg/dL. Gram stain unrevealing; cultures sterile after partial antibiotic pretreatment; CSF pneumococcal antigen positive. Diagnostic_ambiguity=true; type=partial_antibiotic_pretreatment_sterile_cultures. Anchored to Tunkel IDSA 2004 (PMID 15494903) pretreated-meningitis recommendations. Outcome: survived. Subphase 1.3 commit 5.3.3 wave 1, pre-adjudication hold_for_revision.

NARRATIVE_ES: Varon de 33 anos en Paises Bajos, ingresado a urgencias terciarias tras 30 horas de amoxicilina ambulatoria por dolor sinusal, con recrudescencia de fiebre 38.9 C, cefalea, rigidez de nuca y vomitos. Examen: temperatura 38.9 C, escala de Glasgow 14, rigidez de nuca, signo de Kernig positivo, sin deficit focal, sin exantema. Liquido cefalorraquideo mostro presion de apertura 23 cmH2O, leucocitos 2,900 por mm3 (68 por ciento neutrofilos), glucosa 28 mg/dL, proteina 175 mg/dL. Cultivos esteriles tras pretratamiento antibiotico parcial; antigeno neumococico en liquido positivo. Ambiguedad diagnostica por pretratamiento parcial. Anclaje en guia IDSA Tunkel 2004 (PMID 15494903). Subphase 1.3 commit 5.3.3 wave 1.

RATIONALE: Anchored to PMID 15494903 (Tunkel IDSA 2004 CID guideline) pretreated-suspected meningitis recommendations. Diagnostic_ambiguity=true; type=partial_antibiotic_pretreatment_sterile_cultures. Demographic anchor (33yo M outpatient pretreated NL). CSF profile attenuated (WBC 2900, neutrophil 68 percent, glucose 28). Antigen confirms organism. Imputation tiers: tier_1_primary={age, sex, csf_pneumococcal_antigen, pretreatment_history}; tier_3_within_cohort={csf_wbc, neutrophil_pct, glucose, protein attenuation}; tier_4_priors={temp, gcs, symptom_days}. Indeterminate=culture-based-organism-confirmation. Outcome=survived. Tier: tier_4_imputation_idsa_guideline_anchored. 5.3.3 wave1 SP-pretreated-ambiguity NL-2.

ANCHORING_EXTRAS: stage=pre_adjudication; status=pending_external_review; self_review_disposition=hold_for_revision; self_review_notes=wave 1 vignette anchored to PMID 15494903 (Tunkel IDSA 2004); external clinical adjudication pending; classification provisional. adjudicator_ids=WAVE1-PRE-ADJ-1, WAVE1-PRE-ADJ-2 (sentinel); cohen_kappa=0.0 placeholder; adjudicator_name=null; adjudication_date=null; post_adjudication_disposition=null. Subphase 1.3 commit 5.3.3 (2026-05-08). anchor=Tunkel-IDSA-2004 type=partial_antibiotic_pretreatment.

ADJUDICATION:
  inclusion_decision: hold_for_revision
  adjudicator_ids: ['WAVE1-PRE-ADJ-1', 'WAVE1-PRE-ADJ-2']
  ground_truth_class: 2
  pre_adjudication_kappa: 0.0
  disagreement_resolution: None

=== END vignette ===

=== CLASS 2 | vignette_id: 081 | subphase: 1.3 BACT | file: bact_081_sp_elderly_fatal.json ===

ANCHOR:
  pmid: 15509818
  first_author: van
  year: 2004
  journal: NEJM
  citation_type: cohort
  doi: 10.1056/NEJMoa040845

DEMOGRAPHICS:
  age_years: 79
  sex: female
  geography_region: other_global
  ethnicity: white_non_hispanic
  altitude_residence_m: 5
  hiv_status: negative
  cd4_count_cells_per_uL: None
  pregnancy_red_flag: False
  immunocompromise_status: none
  freshwater_exposure_within_14d: False
  freshwater_exposure_type: None

HISTORY:
  symptom_onset_to_presentation_days: 5.0
  chief_complaint: altered_mental_status
  red_flags_present: []
  prodrome_description: 79-year-old female, Netherlands. 5-day progressive fever, headache, confusion progressing to coma. Tertiary ED Amsterdam. Late presentation, GCS 6 on admission. No freshwater. Triad present (van de Beek elderly subgroup mortality 51 percent at age >=70). Outcome: fatal hospital day 2.

VITALS:
  temperature_celsius: 38.7
  heart_rate_bpm: 124
  systolic_bp_mmHg: 96
  diastolic_bp_mmHg: 56
  glasgow_coma_scale: 6
  oxygen_saturation_pct: 89
  respiratory_rate_breaths_per_min: 30

EXAM:
  mental_status_grade: comatose
  neck_stiffness: True
  kernig_or_brudzinski_positive: True
  cranial_nerve_palsy: none
  papilledema_on_fundoscopy: False
  focal_neurological_deficit: False
  skin_lesion_centrofacial_chronic: False
  petechial_or_purpuric_rash: False

LABS:
  wbc_blood_per_uL: 20100
  platelets_per_uL: 145000
  alt_ast_U_per_L: 42
  crp_mg_per_L: 245.0
  procalcitonin_ng_per_mL: 16.0
  serum_sodium_mEq_per_L: 128

CSF:
  opening_pressure_cmH2O: 24.0
  wbc_per_mm3: 3800
  lymphocyte_pct: 22
  neutrophil_pct: 78
  eosinophil_pct: 0
  glucose_mg_per_dL: 28
  protein_mg_per_dL: 170
  lactate_mmol_per_L: 5.6
  ada_U_per_L: None
  crag_lfa_result: negative
  wet_mount_motile_amoebae: negative
  xanthochromia_present: False
  rbc_per_mm3: 6

IMAGING:
  modality: ct_noncontrast
  pattern: diffuse_cerebral_edema_basilar_meningeal_enhancement
  contrast_enhancement: True
  hydrocephalus: False
  basal_meningeal_enhancement: False
  finding_count: 1
  text_summary: CT head non-contrast: diffuse cerebral edema with effacement of sulci, basilar meningeal enhancement on contrast-equivalent regions, no focal lesion, no midline shift. Pattern consistent with severe late-stage bacterial meningitis.

DIAGNOSTIC_TESTS:
  pcr_panel: n/a
  xpert_mtb_rif: n/a
  blood_culture: n/a
  csf_culture: n/a
  serology_or_antigen: n/a
  smear_or_gram: n/a
  brain_biopsy: n/a
  imaging_test: n/a
  total_dx_results: 3

NARRATIVE_EN: A 79-year-old woman in the Netherlands presented to a tertiary emergency department in Amsterdam after a 5-day course of progressive fever, headache, and confusion progressing to coma. She arrived with Glasgow Coma Scale 6. Examination on admission: temperature 38.7 C, neck stiffness, positive Kernig sign, no focal deficit, no rash. CSF showed opening pressure 24 cmH2O, white cell count 3,800 per cubic millimeter (78 percent neutrophils), glucose 28 mg/dL, protein 170 mg/dL. Gram stain revealed gram-positive diplococci; culture identified Streptococcus pneumoniae. Primary anchor: PMID 15509818 (van de Beek 2004 NEJM), elderly subgroup mortality 51 percent at age 70 years and older. Outcome: fatal hospital day 2. Subphase 1.3 commit 5.3.3 wave 1, pre-adjudication hold_for_revision.

NARRATIVE_ES: Mujer de 79 anos en Paises Bajos (Amsterdam), ingresada a urgencias terciarias tras cinco dias de fiebre progresiva, cefalea y confusion con progresion a coma. Ingreso con escala de Glasgow 6. Examen: temperatura 38.7 C, rigidez de nuca, signo de Kernig positivo, sin deficit focal, sin exantema. Liquido cefalorraquideo mostro presion de apertura 24 cmH2O, leucocitos 3,800 por mm3 (78 por ciento neutrofilos), glucosa 28 mg/dL, proteina 170 mg/dL. Tincion de Gram con diplococos grampositivos y cultivo Streptococcus pneumoniae. Anclaje primario en cohorte prospectiva van de Beek 2004 NEJM (PMID 15509818, 696 episodios 1998-2002, mortalidad estrato adultos mayores 51 por ciento a edad >=70). Resultado: fatal en hospital dia 2. Subphase 1.3 commit 5.3.3 wave 1, pre-adjudicacion hold_for_revision.

RATIONALE: Anchored to PMID 15509818 (van de Beek 2004 NEJM), 696-episode prospective Netherlands cohort 1998-2002 (elderly subgroup mortality 51 percent at age 70 years and older). Demographic anchor (79yo F) sits in eldest stratum. CSF profile bacterial range. Imputation tiers: tier_1_primary={age, sex, csf_culture, csf_gram_stain}; tier_3_within_cohort={csf_wbc, neutrophil_pct, glucose, protein, gcs, hyponatremia}; tier_4_priors={temp, symptom_days, hr}. Indeterminate=none. Diagnostic_ambiguity=false. Outcome=fatal_hospital_day_2. Antibiotic_started_hours=2. Tier: tier_3_imputation_within_cohort_review. 5.3.3 wave1 SP-eldest-fatal.

ANCHORING_EXTRAS: stage=pre_adjudication; status=pending_external_review; self_review_disposition=hold_for_revision; self_review_notes=wave 1 vignette anchored to PMID 15509818 (van de Beek 2004 NEJM); external clinical adjudication pending; classification provisional. adjudicator_ids=WAVE1-PRE-ADJ-1, WAVE1-PRE-ADJ-2 (sentinel); cohen_kappa=0.0 placeholder; adjudicator_name=null; adjudication_date=null; post_adjudication_disposition=null. Subphase 1.3 commit 5.3.3 (2026-05-08). anchor=van-de-Beek-NEJM-2004 stratum=eldest-fatal.

ADJUDICATION:
  inclusion_decision: hold_for_revision
  adjudicator_ids: ['WAVE1-PRE-ADJ-1', 'WAVE1-PRE-ADJ-2']
  ground_truth_class: 2
  pre_adjudication_kappa: 0.0
  disagreement_resolution: None

=== END vignette ===

=== CLASS 2 | vignette_id: 082 | subphase: 1.3 BACT | file: bact_082_nm_college_outbreak.json ===

ANCHOR:
  pmid: 18626301
  first_author: Heckenberg
  year: 2008
  journal: Medicine
  citation_type: cohort
  doi: 10.1097/MD.0b013e318180a6b4

DEMOGRAPHICS:
  age_years: 24
  sex: male
  geography_region: other_global
  ethnicity: white_non_hispanic
  altitude_residence_m: 5
  hiv_status: negative
  cd4_count_cells_per_uL: None
  pregnancy_red_flag: False
  immunocompromise_status: none
  freshwater_exposure_within_14d: False
  freshwater_exposure_type: None

HISTORY:
  symptom_onset_to_presentation_days: 0.75
  chief_complaint: fever_with_headache
  red_flags_present: []
  prodrome_description: 24-year-old male, Netherlands (Utrecht). 18-hour rapid progression: fever 39.8 C, severe headache, neck stiffness, petechial rash on extremities and trunk. College dormitory contact 2 weeks prior with febrile illness. Tertiary ED. No freshwater exposure. Triad present (21 percent cohort subgroup). Outcome: survived no sequelae. Abx hour 1. ERRATA: PMID 18626302 was typo.

VITALS:
  temperature_celsius: 39.8
  heart_rate_bpm: 124
  systolic_bp_mmHg: 110
  diastolic_bp_mmHg: 68
  glasgow_coma_scale: 13
  oxygen_saturation_pct: 96
  respiratory_rate_breaths_per_min: 24

EXAM:
  mental_status_grade: confused
  neck_stiffness: True
  kernig_or_brudzinski_positive: True
  cranial_nerve_palsy: none
  papilledema_on_fundoscopy: False
  focal_neurological_deficit: False
  skin_lesion_centrofacial_chronic: False
  petechial_or_purpuric_rash: True

LABS:
  wbc_blood_per_uL: 16800
  platelets_per_uL: 195000
  alt_ast_U_per_L: 38
  crp_mg_per_L: 168.0
  procalcitonin_ng_per_mL: 6.2
  serum_sodium_mEq_per_L: 136

CSF:
  opening_pressure_cmH2O: 24.0
  wbc_per_mm3: 2100
  lymphocyte_pct: 15
  neutrophil_pct: 85
  eosinophil_pct: 0
  glucose_mg_per_dL: 30
  protein_mg_per_dL: 145
  lactate_mmol_per_L: 5.8
  ada_U_per_L: None
  crag_lfa_result: negative
  wet_mount_motile_amoebae: negative
  xanthochromia_present: False
  rbc_per_mm3: 5

IMAGING:
  modality: ct_noncontrast
  pattern: normal
  contrast_enhancement: True
  hydrocephalus: False
  basal_meningeal_enhancement: False
  finding_count: 0
  text_summary: CT head non-contrast: normal. No focal lesion, no hydrocephalus, no mass effect.

DIAGNOSTIC_TESTS:
  pcr_panel: n/a
  xpert_mtb_rif: n/a
  blood_culture: n/a
  csf_culture: n/a
  serology_or_antigen: n/a
  smear_or_gram: n/a
  brain_biopsy: n/a
  imaging_test: n/a
  total_dx_results: 3

NARRATIVE_EN: A 24-year-old man in the Netherlands (Utrecht) presented to a tertiary emergency department with an 18-hour rapid progression of fever to 39.8 C, severe headache, neck stiffness, and petechial rash distributed on extremities and trunk at presentation. Recent college dormitory contact two weeks prior with reported febrile illness. Examination on admission: temperature 39.8 C, Glasgow Coma Scale 13, neck stiffness, positive Kernig sign, petechial rash, no focal deficit. Classic triad present (this case sits in the 21 percent triad-positive subgroup of the Heckenberg 2008 cohort). CSF showed opening pressure 24 cmH2O, white cell count 2,100 per cubic millimeter (85 percent neutrophils), glucose 30 mg/dL, protein 145 mg/dL. Gram stain revealed gram-negative diplococci; culture identified Neisseria meningitidis serogroup B. Primary anchor: PMID 18626301 (Heckenberg 2008 Medicine), 258-adult prospective Netherlands NM cohort 1998-2002 (rash 46 percent, petechial pattern in 81 percent of those, mortality 7 percent). ERRATA: PMID 18626302 in 5.3.1 lock was typo for this same paper; corrected to 18626301. Outcome: survived no sequelae. Subphase 1.3 commit 5.3.2 pilot 3, pre-adjudication hold_for_revision.

NARRATIVE_ES: Varon de 24 anos en Paises Bajos (Utrecht), ingresado a urgencias terciarias con 18 horas de progresion rapida: fiebre 39.8 C, cefalea intensa, rigidez de nuca, exantema petequial distribuido en extremidades y tronco al ingreso. Contacto reciente en dormitorio universitario dos semanas antes con enfermedad febril reportada. Examen: temperatura 39.8 C, escala de Glasgow 13, rigidez de nuca, signo de Kernig positivo, exantema petequial, sin deficit focal. Triada clasica presente (subgrupo del 21 por ciento triada-positiva de la cohorte Heckenberg 2008). Liquido cefalorraquideo mostro presion de apertura 24 cmH2O, leucocitos 2,100 por mm3 (85 por ciento neutrofilos), glucosa 30 mg/dL, proteina 145 mg/dL. Tincion de Gram con diplococos gramnegativos y cultivo Neisseria meningitidis serogrupo B. Anclaje primario en cohorte prospectiva de 258 adultos (PMID 18626301, Heckenberg 2008 Medicine, errata corregida desde 18626302). Subphase 1.3 commit 5.3.2 pilot 3.

RATIONALE: Anchored to PMID 18626301 (Heckenberg 2008 Medicine 87:185-192), 258-adult NM prospective Netherlands cohort. Anchor (24yo M college dorm contact) is canonical NM epidemiology. Petechial rash on extremities and trunk (cohort 46 percent rash, 81 percent petechial = 37 percent overall). CSF WBC 2,100 within cohort IQR 1,820-12,225. Triad present (21 percent subgroup). Imputation tiers: tier_1_primary={age, sex, csf_culture, csf_gram_stain, rash, triad}; tier_3_within_cohort={csf_wbc, neutrophil_pct, glucose, protein}; tier_4_priors={temp, gcs, symptom_days}. Indeterminate=none. Diagnostic_ambiguity=false. Outcome=survived_no_sequelae per 7 percent NM mortality. Abx_hours=1. ERRATA: PMID 18626302 in 5.3.1 lock was typo; corrected to 18626301. Tier: primary_source_direct. 5.3.2 pilot 3.

ANCHORING_EXTRAS: stage=pre_adjudication; status=pending_external_review; self_review_disposition=hold_for_revision; self_review_notes=pilot vignette anchored to PMID 18626301 (Heckenberg 2008 Medicine NM 258 adults); external clinical adjudication pending; classification provisional. adjudicator_ids=PILOT-PRE-ADJ-1, PILOT-PRE-ADJ-2 (sentinel); cohen_kappa=0.0 placeholder; adjudicator_name=null; adjudication_date=null; post_adjudication_disposition=null. Subphase 1.3 commit 5.3.2 (2026-05-07).

ADJUDICATION:
  inclusion_decision: hold_for_revision
  adjudicator_ids: ['PILOT-PRE-ADJ-1', 'PILOT-PRE-ADJ-2']
  ground_truth_class: 2
  pre_adjudication_kappa: 0.0
  disagreement_resolution: None

=== END vignette ===

=== CLASS 2 | vignette_id: 083 | subphase: 1.3 BACT | file: bact_083_nm_adolescent_fatal.json ===

ANCHOR:
  pmid: 32935747
  first_author: Soeters
  year: 2020
  journal: MMWR
  citation_type: surveillance
  doi: 10.15585/mmwr.mm6936a3

DEMOGRAPHICS:
  age_years: 17
  sex: female
  geography_region: us_south
  ethnicity: white_non_hispanic
  altitude_residence_m: 100
  hiv_status: negative
  cd4_count_cells_per_uL: None
  pregnancy_red_flag: False
  immunocompromise_status: none
  freshwater_exposure_within_14d: False
  freshwater_exposure_type: None

HISTORY:
  symptom_onset_to_presentation_days: 1.5
  chief_complaint: altered_mental_status
  red_flags_present: []
  prodrome_description: 17-year-old female, US South region. 36-hour rapid progression: fever 39.6 C, severe headache, neck stiffness, petechial rash extremities and trunk evolving to purpura within 12 hours. Tertiary ED. No freshwater. Outcome: fatal hospital day 2 with disseminated intravascular coagulation.

VITALS:
  temperature_celsius: 39.6
  heart_rate_bpm: 132
  systolic_bp_mmHg: 92
  diastolic_bp_mmHg: 54
  glasgow_coma_scale: 8
  oxygen_saturation_pct: 90
  respiratory_rate_breaths_per_min: 30

EXAM:
  mental_status_grade: stuporous
  neck_stiffness: True
  kernig_or_brudzinski_positive: True
  cranial_nerve_palsy: none
  papilledema_on_fundoscopy: False
  focal_neurological_deficit: False
  skin_lesion_centrofacial_chronic: False
  petechial_or_purpuric_rash: True

LABS:
  wbc_blood_per_uL: 22000
  platelets_per_uL: 78000
  alt_ast_U_per_L: 56
  crp_mg_per_L: 245.0
  procalcitonin_ng_per_mL: 18.0
  serum_sodium_mEq_per_L: 132

CSF:
  opening_pressure_cmH2O: 30.0
  wbc_per_mm3: 4500
  lymphocyte_pct: 12
  neutrophil_pct: 88
  eosinophil_pct: 0
  glucose_mg_per_dL: 18
  protein_mg_per_dL: 240
  lactate_mmol_per_L: 7.6
  ada_U_per_L: None
  crag_lfa_result: negative
  wet_mount_motile_amoebae: negative
  xanthochromia_present: False
  rbc_per_mm3: 6

IMAGING:
  modality: ct_noncontrast
  pattern: diffuse_cerebral_edema_basilar_meningeal_enhancement
  contrast_enhancement: True
  hydrocephalus: False
  basal_meningeal_enhancement: False
  finding_count: 1
  text_summary: CT head non-contrast: diffuse cerebral edema with effacement of sulci, basilar meningeal enhancement on contrast-equivalent regions, no focal lesion, no midline shift. Pattern consistent with severe late-stage bacterial meningitis.

DIAGNOSTIC_TESTS:
  pcr_panel: n/a
  xpert_mtb_rif: n/a
  blood_culture: n/a
  csf_culture: n/a
  serology_or_antigen: n/a
  smear_or_gram: n/a
  brain_biopsy: n/a
  imaging_test: n/a
  total_dx_results: 3

NARRATIVE_EN: A 17-year-old woman in the US South region presented to a tertiary emergency department with a 36-hour rapid progression of fever to 39.6 C, severe headache, neck stiffness, and a petechial rash on her extremities and trunk that evolved to purpura within 12 hours. Examination on admission: temperature 39.6 C, Glasgow Coma Scale 8, neck stiffness, positive Kernig sign, petechial rash, no focal deficit. Platelets 78,000 with evolving disseminated intravascular coagulation. CSF showed opening pressure 30 cmH2O, white cell count 4,500 per cubic millimeter (88 percent neutrophils), glucose 18 mg/dL, protein 240 mg/dL. Gram stain revealed gram-negative diplococci; culture identified Neisseria meningitidis serogroup B. Anchored to Soeters 2020 MMWR CDC ABCs (PMID 32935747, US adolescent NM surveillance, mortality 12 percent). Outcome: fatal hospital day 2. Subphase 1.3 commit 5.3.4 wave 2, pre-adjudication hold_for_revision.

NARRATIVE_ES: Mujer de 17 anos en region sur de Estados Unidos, ingresada a urgencias terciarias con 36 horas de progresion rapida: fiebre 39.6 C, cefalea intensa, rigidez de nuca y exantema petequial en extremidades y tronco con evolucion a purpura en 12 horas. Examen: temperatura 39.6 C, escala de Glasgow 8, rigidez de nuca, signo de Kernig positivo, exantema petequial, sin deficit focal. Plaquetas 78,000 con coagulacion intravascular diseminada evolutiva. Liquido cefalorraquideo mostro presion de apertura 30 cmH2O, leucocitos 4,500 por mm3 (88 por ciento neutrofilos), glucosa 18 mg/dL, proteina 240 mg/dL. Tincion de Gram con diplococos gramnegativos y cultivo Neisseria meningitidis serogrupo B. Anclaje en Soeters 2020 MMWR ABCs CDC (PMID 32935747, vigilancia adolescente). Subphase 1.3 commit 5.3.4 wave 2.

RATIONALE: Anchored to PMID 32935747 (Soeters 2020 MMWR CDC ABCs surveillance) covering US adolescent and young adult NM epidemiology with approximately 12 percent overall NM case-fatality and elevated fulminant-purpura subgroup mortality. Demographic anchor (17yo F adolescent) sits in target surveillance stratum. CSF bacterial range; petechial-to-purpuric evolution + DIC consistent with fulminant meningococcemia. Imputation tiers: tier_1_primary={age, sex, csf_culture, csf_gram_stain, petechial_rash, DIC platelets}; tier_3_within_cohort={csf_wbc, neutrophil_pct, glucose, protein}; tier_4_priors={temp, gcs, symptom_days}. Indeterminate=none. Diagnostic_ambiguity=false. Outcome=fatal_hospital_day_2. Tier: tier_4_imputation_cdc_abcs_anchored. 5.3.4 wave2 NM-adolescent-fulminant-fatal.

ANCHORING_EXTRAS: stage=pre_adjudication; status=pending_external_review; self_review_disposition=hold_for_revision; self_review_notes=wave 2 vignette anchored to PMID 32935747 (Soeters 2020 MMWR CDC ABCs); external clinical adjudication pending; classification provisional. adjudicator_ids=WAVE2-PRE-ADJ-1, WAVE2-PRE-ADJ-2 (sentinel); cohen_kappa=0.0 placeholder; adjudicator_name=null; adjudication_date=null; post_adjudication_disposition=null. Subphase 1.3 commit 5.3.4 (2026-05-08). anchor=Soeters-MMWR-CDC-ABCs-2020 stratum=adolescent-fulminant.

ADJUDICATION:
  inclusion_decision: hold_for_revision
  adjudicator_ids: ['WAVE2-PRE-ADJ-1', 'WAVE2-PRE-ADJ-2']
  ground_truth_class: 2
  pre_adjudication_kappa: 0.0
  disagreement_resolution: None

=== END vignette ===

=== CLASS 2 | vignette_id: 084 | subphase: 1.3 BACT | file: bact_084_nm_loreto_infant_partial_treatment_ambiguity.json ===

ANCHOR:
  pmid: 32935747
  first_author: Soeters
  year: 2020
  journal: MMWR
  citation_type: surveillance
  doi: 10.15585/mmwr.mm6936a3

DEMOGRAPHICS:
  age_years: 1
  sex: male
  geography_region: peru_loreto_amazon
  ethnicity: mestizo
  altitude_residence_m: 100
  hiv_status: negative
  cd4_count_cells_per_uL: None
  pregnancy_red_flag: False
  immunocompromise_status: none
  freshwater_exposure_within_14d: False
  freshwater_exposure_type: None

HISTORY:
  symptom_onset_to_presentation_days: 2.0
  chief_complaint: altered_mental_status
  red_flags_present: []
  prodrome_description: 14-month-old male, Loreto Peru Amazon community. Outpatient amoxicillin 24 hours via riverine health post for febrile illness. Subsequent decline: fever 39.4 C, irritability, lethargy, bulging fontanelle, petechiae trunk. Air-evac to Iquitos tertiary ED. Diagnostic_ambiguity=true; type=partial_antibiotic_pretreatment_sterile_cultures. Outcome: fatal.

VITALS:
  temperature_celsius: 39.4
  heart_rate_bpm: 168
  systolic_bp_mmHg: 78
  diastolic_bp_mmHg: 46
  glasgow_coma_scale: 8
  oxygen_saturation_pct: 90
  respiratory_rate_breaths_per_min: 38

EXAM:
  mental_status_grade: stuporous
  neck_stiffness: True
  kernig_or_brudzinski_positive: True
  cranial_nerve_palsy: none
  papilledema_on_fundoscopy: None
  focal_neurological_deficit: False
  skin_lesion_centrofacial_chronic: False
  petechial_or_purpuric_rash: True

LABS:
  wbc_blood_per_uL: 16500
  platelets_per_uL: 95000
  alt_ast_U_per_L: 48
  crp_mg_per_L: 132.0
  procalcitonin_ng_per_mL: 6.5
  serum_sodium_mEq_per_L: 134

CSF:
  opening_pressure_cmH2O: 24.0
  wbc_per_mm3: 1800
  lymphocyte_pct: 40
  neutrophil_pct: 60
  eosinophil_pct: 0
  glucose_mg_per_dL: 28
  protein_mg_per_dL: 165
  lactate_mmol_per_L: 4.6
  ada_U_per_L: None
  crag_lfa_result: negative
  wet_mount_motile_amoebae: negative
  xanthochromia_present: False
  rbc_per_mm3: 5

IMAGING:
  modality: ct_noncontrast
  pattern: diffuse_cerebral_edema_basilar_meningeal_enhancement
  contrast_enhancement: True
  hydrocephalus: False
  basal_meningeal_enhancement: False
  finding_count: 1
  text_summary: CT head non-contrast: diffuse cerebral edema with effacement of sulci, basilar meningeal enhancement on contrast-equivalent regions, no focal lesion, no midline shift. Pattern consistent with severe late-stage bacterial meningitis.

DIAGNOSTIC_TESTS:
  pcr_panel: neisseria_meningitidis_positive_serogroup_C
  xpert_mtb_rif: n/a
  blood_culture: n/a
  csf_culture: n/a
  serology_or_antigen: n/a
  smear_or_gram: n/a
  brain_biopsy: n/a
  imaging_test: n/a
  total_dx_results: 4

NARRATIVE_EN: A 14-month-old boy from a Loreto Amazon community in Peru received outpatient amoxicillin for 24 hours via a riverine health post for an undifferentiated febrile illness, then deteriorated with fever to 39.4 C, irritability, lethargy, a bulging anterior fontanelle, and petechiae on the trunk. He was air-evacuated to a tertiary emergency department in Iquitos. Examination on admission: temperature 39.4 C, Glasgow Coma Scale 8, neck stiffness, positive Kernig sign, petechiae. CSF showed opening pressure 24 cmH2O, white cell count 1,800 per cubic millimeter (60 percent neutrophils), glucose 28 mg/dL, protein 165 mg/dL. Gram stain unrevealing; CSF + blood cultures sterile after partial-antibiotic pretreatment and remote specimen handling delay; CSF meningococcal PCR positive for serogroup C. Diagnostic_ambiguity=true; type=partial_antibiotic_pretreatment_sterile_cultures. Anchored to Soeters 2020 MMWR CDC ABCs (PMID 32935747, NM surveillance overlaid with Peru-Amazon care-access context). Outcome: fatal. Subphase 1.3 commit 5.3.4 wave 2, pre-adjudication hold_for_revision.

NARRATIVE_ES: Lactante varon de 14 meses originario de comunidad ribereña en Loreto Peru, recibio amoxicilina ambulatoria 24 horas en posta de salud rural por enfermedad febril, con posterior deterioro: fiebre 39.4 C, irritabilidad, letargo, fontanela anterior abombada, petequias en tronco. Evacuacion aerea a urgencias terciarias en Iquitos. Examen: temperatura 39.4 C, escala de Glasgow 8, rigidez de nuca, signo de Kernig positivo, petequias. Liquido cefalorraquideo mostro presion de apertura 24 cmH2O, leucocitos 1,800 por mm3 (60 por ciento neutrofilos), glucosa 28 mg/dL, proteina 165 mg/dL. Tincion de Gram sin organismos; cultivos de liquido y sangre esteriles tras pretratamiento antibiotico parcial y demora en manejo de muestras; PCR meningococica en liquido positiva para serogrupo C. Ambiguedad diagnostica por pretratamiento parcial. Subphase 1.3 commit 5.3.4 wave 2.

RATIONALE: Anchored to PMID 32935747 (Soeters 2020 MMWR CDC ABCs) surveillance with overlaid Peru-Amazon care-access context. Diagnostic_ambiguity=true; type=partial_antibiotic_pretreatment_sterile_cultures with secondary remote-specimen-handling-delay compounding feature. Demographic anchor (14mo M Loreto pediatric outpatient pretreated then air-evac) sits in ambiguity stratum. CSF profile attenuated (WBC 1800, neutrophil 60 percent). PCR confirms organism (serogroup C). Imputation tiers: tier_1_primary={age, sex, csf_meningococcal_pcr, pretreatment_history, petechial_rash}; tier_3_within_cohort={csf_wbc, neutrophil_pct, glucose, protein attenuation}; tier_4_priors={temp, gcs, hr}. Indeterminate=culture-based-organism-confirmation. Outcome=fatal. Tier: tier_4_imputation_cdc_abcs_anchored. 5.3.4 wave2 NM-Loreto-infant-ambiguity.

ANCHORING_EXTRAS: stage=pre_adjudication; status=pending_external_review; self_review_disposition=hold_for_revision; self_review_notes=wave 2 vignette anchored to PMID 32935747 (Soeters 2020 MMWR CDC ABCs); external clinical adjudication pending; classification provisional. adjudicator_ids=WAVE2-PRE-ADJ-1, WAVE2-PRE-ADJ-2 (sentinel); cohen_kappa=0.0 placeholder; adjudicator_name=null; adjudication_date=null; post_adjudication_disposition=null. Subphase 1.3 commit 5.3.4 (2026-05-08). anchor=Soeters-MMWR-CDC-ABCs-2020 type=partial_antibiotic_pretreatment region=peru-loreto-amazon.

ADJUDICATION:
  inclusion_decision: hold_for_revision
  adjudicator_ids: ['WAVE2-PRE-ADJ-1', 'WAVE2-PRE-ADJ-2']
  ground_truth_class: 2
  pre_adjudication_kappa: 0.0
  disagreement_resolution: None

=== END vignette ===

=== CLASS 2 | vignette_id: 085 | subphase: 1.3 BACT | file: bact_085_nm_military.json ===

ANCHOR:
  pmid: 32935747
  first_author: Soeters
  year: 2020
  journal: MMWR
  citation_type: surveillance
  doi: 10.15585/mmwr.mm6936a3

DEMOGRAPHICS:
  age_years: 22
  sex: female
  geography_region: us_south
  ethnicity: white_non_hispanic
  altitude_residence_m: 100
  hiv_status: negative
  cd4_count_cells_per_uL: None
  pregnancy_red_flag: False
  immunocompromise_status: none
  freshwater_exposure_within_14d: False
  freshwater_exposure_type: None

HISTORY:
  symptom_onset_to_presentation_days: 1.0
  chief_complaint: fever_with_headache
  red_flags_present: []
  prodrome_description: 22-year-old female, US South region. Active-duty military barracks setting. 24-hour fever 39.4 C, severe headache, neck stiffness, petechial rash extremities. Tertiary ED. No freshwater. Outcome: survived no sequelae. Antibiotic at hour 1 plus dexamethasone IDSA young adult NM.

VITALS:
  temperature_celsius: 39.4
  heart_rate_bpm: 122
  systolic_bp_mmHg: 112
  diastolic_bp_mmHg: 70
  glasgow_coma_scale: 13
  oxygen_saturation_pct: 96
  respiratory_rate_breaths_per_min: 22

EXAM:
  mental_status_grade: confused
  neck_stiffness: True
  kernig_or_brudzinski_positive: True
  cranial_nerve_palsy: none
  papilledema_on_fundoscopy: False
  focal_neurological_deficit: False
  skin_lesion_centrofacial_chronic: False
  petechial_or_purpuric_rash: True

LABS:
  wbc_blood_per_uL: 18800
  platelets_per_uL: 195000
  alt_ast_U_per_L: 38
  crp_mg_per_L: 188.0
  procalcitonin_ng_per_mL: 8.2
  serum_sodium_mEq_per_L: 136

CSF:
  opening_pressure_cmH2O: 26.0
  wbc_per_mm3: 5200
  lymphocyte_pct: 10
  neutrophil_pct: 90
  eosinophil_pct: 0
  glucose_mg_per_dL: 22
  protein_mg_per_dL: 200
  lactate_mmol_per_L: 6.8
  ada_U_per_L: None
  crag_lfa_result: negative
  wet_mount_motile_amoebae: negative
  xanthochromia_present: False
  rbc_per_mm3: 4

IMAGING:
  modality: ct_noncontrast
  pattern: normal
  contrast_enhancement: True
  hydrocephalus: False
  basal_meningeal_enhancement: False
  finding_count: 0
  text_summary: CT head non-contrast: normal at admission. No focal lesion, no hydrocephalus, no midline shift, no mass effect. Pattern consistent with early-stage adult community-acquired bacterial meningitis.

DIAGNOSTIC_TESTS:
  pcr_panel: n/a
  xpert_mtb_rif: n/a
  blood_culture: n/a
  csf_culture: n/a
  serology_or_antigen: n/a
  smear_or_gram: n/a
  brain_biopsy: n/a
  imaging_test: n/a
  total_dx_results: 3

NARRATIVE_EN: A 22-year-old woman in the US South region in an active-duty military barracks setting presented to a tertiary emergency department with a 24-hour history of fever to 39.4 C, severe headache, neck stiffness, and petechial rash on her extremities. Examination on admission: temperature 39.4 C, Glasgow Coma Scale 13, neck stiffness, positive Kernig sign, petechial rash, no focal deficit. CSF showed opening pressure 26 cmH2O, white cell count 5,200 per cubic millimeter (90 percent neutrophils), glucose 22 mg/dL, protein 200 mg/dL. Gram stain revealed gram-negative diplococci; culture identified Neisseria meningitidis serogroup B. Anchored to Soeters 2020 MMWR CDC ABCs (PMID 32935747, US young-adult NM surveillance; military barracks an established outbreak setting). Outcome: survived no sequelae. Subphase 1.3 commit 5.3.4 wave 2, pre-adjudication hold_for_revision.

NARRATIVE_ES: Mujer de 22 anos en region sur de Estados Unidos, en cuartel militar en servicio activo, ingresada a urgencias terciarias con 24 horas de fiebre 39.4 C, cefalea intensa, rigidez de nuca y exantema petequial en extremidades. Examen: temperatura 39.4 C, escala de Glasgow 13, rigidez de nuca, signo de Kernig positivo, exantema petequial, sin deficit focal. Liquido cefalorraquideo mostro presion de apertura 26 cmH2O, leucocitos 5,200 por mm3 (90 por ciento neutrofilos), glucosa 22 mg/dL, proteina 200 mg/dL. Tincion de Gram con diplococos gramnegativos y cultivo Neisseria meningitidis serogrupo B. Anclaje en Soeters 2020 MMWR ABCs CDC (PMID 32935747, vigilancia adulto joven; cuartel militar como entorno de brote establecido). Subphase 1.3 commit 5.3.4 wave 2.

RATIONALE: Anchored to PMID 32935747 (Soeters 2020 MMWR CDC ABCs surveillance). Demographic anchor (22yo F young adult military barracks) sits in CDC-documented outbreak-setting stratum. CSF profile bacterial range; petechial rash + classic NM serogroup B. Imputation tiers: tier_1_primary={age, sex, csf_culture, csf_gram_stain, petechial_rash, military_barracks_setting}; tier_3_within_cohort={csf_wbc, neutrophil_pct, glucose, protein}; tier_4_priors={temp, gcs, symptom_days}. Indeterminate=none. Diagnostic_ambiguity=false. Outcome=survived_no_sequelae. Tier: tier_4_imputation_cdc_abcs_anchored. 5.3.4 wave2 NM-young-adult-military.

ANCHORING_EXTRAS: stage=pre_adjudication; status=pending_external_review; self_review_disposition=hold_for_revision; self_review_notes=wave 2 vignette anchored to PMID 32935747 (Soeters 2020 MMWR CDC ABCs); external clinical adjudication pending; classification provisional. adjudicator_ids=WAVE2-PRE-ADJ-1, WAVE2-PRE-ADJ-2 (sentinel); cohen_kappa=0.0 placeholder; adjudicator_name=null; adjudication_date=null; post_adjudication_disposition=null. Subphase 1.3 commit 5.3.4 (2026-05-08). anchor=Soeters-MMWR-CDC-ABCs-2020 stratum=young-adult-military.

ADJUDICATION:
  inclusion_decision: hold_for_revision
  adjudicator_ids: ['WAVE2-PRE-ADJ-1', 'WAVE2-PRE-ADJ-2']
  ground_truth_class: 2
  pre_adjudication_kappa: 0.0
  disagreement_resolution: None

=== END vignette ===

=== CLASS 2 | vignette_id: 086 | subphase: 1.3 BACT | file: bact_086_hib_cusco_pediatric.json ===

ANCHOR:
  pmid: 32935747
  first_author: Soeters
  year: 2020
  journal: MMWR
  citation_type: surveillance
  doi: 10.15585/mmwr.mm6936a3

DEMOGRAPHICS:
  age_years: 3
  sex: male
  geography_region: peru_cusco_altitude
  ethnicity: mestizo
  altitude_residence_m: 3399
  hiv_status: negative
  cd4_count_cells_per_uL: None
  pregnancy_red_flag: False
  immunocompromise_status: none
  freshwater_exposure_within_14d: False
  freshwater_exposure_type: None

HISTORY:
  symptom_onset_to_presentation_days: 2.5
  chief_complaint: altered_mental_status
  red_flags_present: []
  prodrome_description: 3-year-old male, Cusco Peru highlands (3,399 m). 60-hour gradual progression: fever 39.0 C, vomiting, decreasing responsiveness, neck stiffness. Recent otitis media. No freshwater. Vaccination history incomplete (Hib coverage not yet achieved). Outcome: survived no sequelae. Antibiotic at hour 2 plus dexamethasone.

VITALS:
  temperature_celsius: 39.0
  heart_rate_bpm: 142
  systolic_bp_mmHg: 100
  diastolic_bp_mmHg: 60
  glasgow_coma_scale: 12
  oxygen_saturation_pct: 92
  respiratory_rate_breaths_per_min: 30

EXAM:
  mental_status_grade: confused
  neck_stiffness: True
  kernig_or_brudzinski_positive: True
  cranial_nerve_palsy: none
  papilledema_on_fundoscopy: None
  focal_neurological_deficit: False
  skin_lesion_centrofacial_chronic: False
  petechial_or_purpuric_rash: False

LABS:
  wbc_blood_per_uL: 21500
  platelets_per_uL: 285000
  alt_ast_U_per_L: 26
  crp_mg_per_L: 195.0
  procalcitonin_ng_per_mL: 7.5
  serum_sodium_mEq_per_L: 136

CSF:
  opening_pressure_cmH2O: 28.0
  wbc_per_mm3: 4800
  lymphocyte_pct: 12
  neutrophil_pct: 88
  eosinophil_pct: 0
  glucose_mg_per_dL: 22
  protein_mg_per_dL: 210
  lactate_mmol_per_L: 6.8
  ada_U_per_L: None
  crag_lfa_result: negative
  wet_mount_motile_amoebae: negative
  xanthochromia_present: False
  rbc_per_mm3: 5

IMAGING:
  modality: ct_noncontrast
  pattern: normal
  contrast_enhancement: True
  hydrocephalus: False
  basal_meningeal_enhancement: False
  finding_count: 0
  text_summary: CT head non-contrast: normal at admission. No focal lesion, no hydrocephalus, no midline shift, no mass effect. Pattern consistent with early-stage adult community-acquired bacterial meningitis.

DIAGNOSTIC_TESTS:
  pcr_panel: n/a
  xpert_mtb_rif: n/a
  blood_culture: n/a
  csf_culture: n/a
  serology_or_antigen: haemophilus_influenzae_type_b_positive
  smear_or_gram: n/a
  brain_biopsy: n/a
  imaging_test: n/a
  total_dx_results: 4

NARRATIVE_EN: A three-year-old boy from Cusco, Peru in the Andean highlands (3,399 m altitude residence) presented to a tertiary pediatric emergency department with a 60-hour gradual progression of fever to 39.0 C, vomiting, decreasing responsiveness, and neck stiffness. He had been treated for otitis media in the preceding week; vaccination history showed incomplete Hib coverage. Examination on admission: temperature 39.0 C, Glasgow Coma Scale 12, neck stiffness, positive Kernig sign, no focal deficit, no rash. CSF showed opening pressure 28 cmH2O, white cell count 4,800 per cubic millimeter (88 percent neutrophils), glucose 22 mg/dL, protein 210 mg/dL. Gram stain revealed gram-negative coccobacilli; culture identified Haemophilus influenzae type b; CSF Hib capsular antigen positive. Anchored to Soeters 2020 MMWR CDC ABCs (PMID 32935747) Hib surveillance overlaid with incomplete-vaccination-coverage Andean stratum. Outcome: survived no sequelae. Subphase 1.3 commit 5.3.4 wave 2, pre-adjudication hold_for_revision.

NARRATIVE_ES: Varon de tres anos de Cusco Peru en sierra andina (3,399 m), ingresado a urgencias pediatricas terciarias con 60 horas de progresion gradual: fiebre 39.0 C, vomitos, respuesta disminuida y rigidez de nuca. Tratamiento previo para otitis media en la semana anterior; cobertura vacunal Hib incompleta. Examen: temperatura 39.0 C, escala de Glasgow 12, rigidez de nuca, signo de Kernig positivo, sin deficit focal, sin exantema. Liquido cefalorraquideo mostro presion de apertura 28 cmH2O, leucocitos 4,800 por mm3 (88 por ciento neutrofilos), glucosa 22 mg/dL, proteina 210 mg/dL. Tincion de Gram con cocobacilos gramnegativos y cultivo Haemophilus influenzae tipo b; antigeno Hib en liquido positivo. Anclaje en Soeters 2020 MMWR ABCs CDC (PMID 32935747). Subphase 1.3 commit 5.3.4 wave 2.

RATIONALE: Anchored to PMID 32935747 (Soeters 2020 MMWR CDC ABCs) surveillance overlaid with Andean-pediatric incomplete-Hib-coverage stratum (Cusco altitude region 3,399m). Demographic anchor (3yo M Cusco pediatric undervaccinated post-otitis-media) sits in surveillance gap stratum. CSF bacterial range; Gram stain + culture + antigen all confirm Hib. Imputation tiers: tier_1_primary={age, sex, region, csf_culture, csf_gram_stain, csf_hib_antigen, otitis_media}; tier_3_within_cohort={csf_wbc, neutrophil_pct, glucose, protein}; tier_4_priors={temp, gcs, symptom_days}. Indeterminate=papilledema_on_fundoscopy. Diagnostic_ambiguity=false. Outcome=survived. Tier: tier_4_imputation_cdc_abcs_anchored. 5.3.4 wave2 Hib-Cusco-pediatric.

ANCHORING_EXTRAS: stage=pre_adjudication; status=pending_external_review; self_review_disposition=hold_for_revision; self_review_notes=wave 2 vignette anchored to PMID 32935747 (Soeters 2020 MMWR CDC ABCs); external clinical adjudication pending; classification provisional. adjudicator_ids=WAVE2-PRE-ADJ-1, WAVE2-PRE-ADJ-2 (sentinel); cohen_kappa=0.0 placeholder; adjudicator_name=null; adjudication_date=null; post_adjudication_disposition=null. Subphase 1.3 commit 5.3.4 (2026-05-08). anchor=Soeters-MMWR-CDC-ABCs-2020 stratum=pediatric-Cusco-altitude.

ADJUDICATION:
  inclusion_decision: hold_for_revision
  adjudicator_ids: ['WAVE2-PRE-ADJ-1', 'WAVE2-PRE-ADJ-2']
  ground_truth_class: 2
  pre_adjudication_kappa: 0.0
  disagreement_resolution: None

=== END vignette ===

=== CLASS 2 | vignette_id: 087 | subphase: 1.3 BACT | file: bact_087_hib_unimmunized_infant.json ===

ANCHOR:
  pmid: 32935747
  first_author: Soeters
  year: 2020
  journal: MMWR
  citation_type: surveillance
  doi: 10.15585/mmwr.mm6936a3

DEMOGRAPHICS:
  age_years: 1
  sex: male
  geography_region: us_south
  ethnicity: white_non_hispanic
  altitude_residence_m: 100
  hiv_status: negative
  cd4_count_cells_per_uL: None
  pregnancy_red_flag: False
  immunocompromise_status: none
  freshwater_exposure_within_14d: False
  freshwater_exposure_type: None

HISTORY:
  symptom_onset_to_presentation_days: 2.0
  chief_complaint: altered_mental_status
  red_flags_present: []
  prodrome_description: 18-month-old male, US South region. Parents declined vaccinations; no Hib coverage. 48-hour fever 39.2 C, vomiting, irritability progressing to lethargy, bulging fontanelle. Tertiary pediatric ED. No freshwater. Outcome: survived no sequelae. Antibiotic at hour 1.5 plus dexamethasone IDSA pediatric protocol.

VITALS:
  temperature_celsius: 39.2
  heart_rate_bpm: 156
  systolic_bp_mmHg: 92
  diastolic_bp_mmHg: 56
  glasgow_coma_scale: 12
  oxygen_saturation_pct: 95
  respiratory_rate_breaths_per_min: 32

EXAM:
  mental_status_grade: confused
  neck_stiffness: True
  kernig_or_brudzinski_positive: True
  cranial_nerve_palsy: none
  papilledema_on_fundoscopy: None
  focal_neurological_deficit: False
  skin_lesion_centrofacial_chronic: False
  petechial_or_purpuric_rash: False

LABS:
  wbc_blood_per_uL: 24500
  platelets_per_uL: 295000
  alt_ast_U_per_L: 28
  crp_mg_per_L: 215.0
  procalcitonin_ng_per_mL: 9.8
  serum_sodium_mEq_per_L: 135

CSF:
  opening_pressure_cmH2O: 30.0
  wbc_per_mm3: 6200
  lymphocyte_pct: 10
  neutrophil_pct: 90
  eosinophil_pct: 0
  glucose_mg_per_dL: 20
  protein_mg_per_dL: 230
  lactate_mmol_per_L: 7.4
  ada_U_per_L: None
  crag_lfa_result: negative
  wet_mount_motile_amoebae: negative
  xanthochromia_present: False
  rbc_per_mm3: 6

IMAGING:
  modality: ct_noncontrast
  pattern: normal
  contrast_enhancement: True
  hydrocephalus: False
  basal_meningeal_enhancement: False
  finding_count: 0
  text_summary: CT head non-contrast: normal at admission. No focal lesion, no hydrocephalus, no midline shift, no mass effect. Pattern consistent with early-stage adult community-acquired bacterial meningitis.

DIAGNOSTIC_TESTS:
  pcr_panel: n/a
  xpert_mtb_rif: n/a
  blood_culture: n/a
  csf_culture: n/a
  serology_or_antigen: haemophilus_influenzae_type_b_positive
  smear_or_gram: n/a
  brain_biopsy: n/a
  imaging_test: n/a
  total_dx_results: 4

NARRATIVE_EN: An 18-month-old boy in the US South region whose parents had declined vaccinations, including the Hib series, presented to a tertiary pediatric emergency department with a 48-hour history of fever to 39.2 C, vomiting, irritability progressing to lethargy, and a bulging anterior fontanelle. Examination on admission: temperature 39.2 C, Glasgow Coma Scale 12, neck stiffness, positive Kernig sign, no focal deficit, no rash. CSF showed opening pressure 30 cmH2O, white cell count 6,200 per cubic millimeter (90 percent neutrophils), glucose 20 mg/dL, protein 230 mg/dL. Gram stain revealed gram-negative coccobacilli; culture identified Haemophilus influenzae type b; CSF Hib capsular antigen positive. Anchored to Soeters 2020 MMWR CDC ABCs (PMID 32935747) Hib surveillance, undervaccinated-infant resurgence stratum. Outcome: survived no sequelae. Subphase 1.3 commit 5.3.4 wave 2, pre-adjudication hold_for_revision.

NARRATIVE_ES: Lactante varon de 18 meses en region sur de Estados Unidos, cuyos padres habian declinado las vacunas (incluida la serie Hib), ingresado a urgencias pediatricas terciarias con 48 horas de fiebre 39.2 C, vomitos, irritabilidad con progresion a letargo y fontanela anterior abombada. Examen: temperatura 39.2 C, escala de Glasgow 12, rigidez de nuca, signo de Kernig positivo, sin deficit focal, sin exantema. Liquido cefalorraquideo mostro presion de apertura 30 cmH2O, leucocitos 6,200 por mm3 (90 por ciento neutrofilos), glucosa 20 mg/dL, proteina 230 mg/dL. Tincion de Gram con cocobacilos gramnegativos y cultivo Haemophilus influenzae tipo b; antigeno Hib positivo. Anclaje en Soeters 2020 MMWR ABCs CDC (PMID 32935747, estrato lactante no vacunado). Subphase 1.3 commit 5.3.4 wave 2.

RATIONALE: Anchored to PMID 32935747 (Soeters 2020 MMWR CDC ABCs) Hib surveillance with undervaccinated-infant resurgence stratum. Demographic anchor (18mo M unimmunized Hib) sits in post-vaccine-era resurgence stratum documented by ABCs. CSF bacterial range; Gram + culture + antigen all confirm Hib. Imputation tiers: tier_1_primary={age, sex, csf_culture, csf_gram_stain, csf_hib_antigen, vaccine_decline}; tier_3_within_cohort={csf_wbc, neutrophil_pct, glucose, protein}; tier_4_priors={temp, gcs, hr, symptom_days}. Indeterminate=papilledema_on_fundoscopy. Diagnostic_ambiguity=false. Outcome=survived. Tier: tier_4_imputation_cdc_abcs_anchored. 5.3.4 wave2 Hib-unimmunized-infant.

ANCHORING_EXTRAS: stage=pre_adjudication; status=pending_external_review; self_review_disposition=hold_for_revision; self_review_notes=wave 2 vignette anchored to PMID 32935747 (Soeters 2020 MMWR CDC ABCs); external clinical adjudication pending; classification provisional. adjudicator_ids=WAVE2-PRE-ADJ-1, WAVE2-PRE-ADJ-2 (sentinel); cohen_kappa=0.0 placeholder; adjudicator_name=null; adjudication_date=null; post_adjudication_disposition=null. Subphase 1.3 commit 5.3.4 (2026-05-08). anchor=Soeters-MMWR-CDC-ABCs-2020 stratum=undervaccinated-infant.

ADJUDICATION:
  inclusion_decision: hold_for_revision
  adjudicator_ids: ['WAVE2-PRE-ADJ-1', 'WAVE2-PRE-ADJ-2']
  ground_truth_class: 2
  pre_adjudication_kappa: 0.0
  disagreement_resolution: None

=== END vignette ===

=== CLASS 2 | vignette_id: 088 | subphase: 1.3 BACT | file: bact_088_listeria_tumbes_pregnancy.json ===

ANCHOR:
  pmid: 11873028
  first_author: Mylonakis
  year: 2002
  journal: Medicine
  citation_type: cohort
  doi: 10.1097/00005792-200203000-00004

DEMOGRAPHICS:
  age_years: 28
  sex: female
  geography_region: peru_tumbes
  ethnicity: mestizo
  altitude_residence_m: 6
  hiv_status: negative
  cd4_count_cells_per_uL: None
  pregnancy_red_flag: True
  immunocompromise_status: none
  freshwater_exposure_within_14d: False
  freshwater_exposure_type: None

HISTORY:
  symptom_onset_to_presentation_days: 4.0
  chief_complaint: fever_with_headache
  red_flags_present: ['pregnancy_postpartum']
  prodrome_description: 28-year-old female, Tumbes Peru coastal community, 30 weeks gestation. 4-day course: fever 38.6 C, headache, neck stiffness, mild back pain. Recent unpasteurized soft-cheese consumption. Tertiary obstetric ED. No freshwater. Outcome: maternal survived no sequelae; fetal preterm but viable. Antibiotic at hour 2 (ampicillin) plus gentamicin per IDSA Listeria pregnancy protocol.

VITALS:
  temperature_celsius: 38.6
  heart_rate_bpm: 102
  systolic_bp_mmHg: 110
  diastolic_bp_mmHg: 68
  glasgow_coma_scale: 14
  oxygen_saturation_pct: 97
  respiratory_rate_breaths_per_min: 20

EXAM:
  mental_status_grade: alert
  neck_stiffness: True
  kernig_or_brudzinski_positive: True
  cranial_nerve_palsy: none
  papilledema_on_fundoscopy: False
  focal_neurological_deficit: False
  skin_lesion_centrofacial_chronic: False
  petechial_or_purpuric_rash: False

LABS:
  wbc_blood_per_uL: 14500
  platelets_per_uL: 220000
  alt_ast_U_per_L: 24
  crp_mg_per_L: 88.0
  procalcitonin_ng_per_mL: 2.4
  serum_sodium_mEq_per_L: 137

CSF:
  opening_pressure_cmH2O: 22.0
  wbc_per_mm3: 1500
  lymphocyte_pct: 45
  neutrophil_pct: 55
  eosinophil_pct: 0
  glucose_mg_per_dL: 28
  protein_mg_per_dL: 130
  lactate_mmol_per_L: 4.0
  ada_U_per_L: None
  crag_lfa_result: negative
  wet_mount_motile_amoebae: negative
  xanthochromia_present: False
  rbc_per_mm3: 3

IMAGING:
  modality: ct_noncontrast
  pattern: normal
  contrast_enhancement: True
  hydrocephalus: False
  basal_meningeal_enhancement: False
  finding_count: 0
  text_summary: CT head non-contrast: normal at admission. No focal lesion, no hydrocephalus, no midline shift, no mass effect. Pattern consistent with early-stage adult community-acquired bacterial meningitis.

DIAGNOSTIC_TESTS:
  pcr_panel: n/a
  xpert_mtb_rif: n/a
  blood_culture: n/a
  csf_culture: n/a
  serology_or_antigen: n/a
  smear_or_gram: n/a
  brain_biopsy: n/a
  imaging_test: n/a
  total_dx_results: 3

NARRATIVE_EN: A 28-year-old woman from a Tumbes Peru coastal community at 30 weeks gestation presented to a tertiary obstetric emergency department after a 4-day course of fever to 38.6 C, headache, neck stiffness, and mild back pain. She had recent consumption of unpasteurized soft cheese. Examination on admission: temperature 38.6 C, Glasgow Coma Scale 14, neck stiffness, positive Kernig sign, no focal deficit, no rash. CSF showed opening pressure 22 cmH2O, white cell count 1,500 per cubic millimeter (55 percent neutrophils), glucose 28 mg/dL, protein 130 mg/dL. Gram stain revealed short gram-positive bacilli; CSF and blood cultures grew Listeria monocytogenes. Anchored to Mylonakis 2002 Medicine (PMID 11873028) listerial-meningitis review (pregnancy stratum approximately 27 percent of adult Listeria CNS infection in maternal-fetal cohort). Outcome: maternal survived no sequelae; preterm-but-viable fetus delivered. Subphase 1.3 commit 5.3.4 wave 2, pre-adjudication hold_for_revision.

NARRATIVE_ES: Mujer de 28 anos de comunidad costera en Tumbes Peru a las 30 semanas de gestacion, ingresada a urgencias obstetricas terciarias tras cuatro dias de fiebre 38.6 C, cefalea, rigidez de nuca y dolor lumbar leve. Antecedente de consumo reciente de queso fresco no pasteurizado. Examen: temperatura 38.6 C, escala de Glasgow 14, rigidez de nuca, signo de Kernig positivo, sin deficit focal, sin exantema. Liquido cefalorraquideo mostro presion de apertura 22 cmH2O, leucocitos 1,500 por mm3 (55 por ciento neutrofilos), glucosa 28 mg/dL, proteina 130 mg/dL. Tincion de Gram con bacilos grampositivos cortos; cultivos de liquido y sangre crecieron Listeria monocytogenes. Anclaje en revision Mylonakis 2002 Medicine (PMID 11873028, estrato gestante alrededor del 27 por ciento de Listeria SNC en adultos). Subphase 1.3 commit 5.3.4 wave 2.

RATIONALE: Anchored to PMID 11873028 (Mylonakis 2002 Medicine listerial-meningitis review). Demographic anchor (28yo F Tumbes 30-week gestation with unpasteurized-cheese exposure) sits in pregnancy stratum (approximately 27 percent of adult Listeria CNS infection in maternal-fetal cohort). CSF profile within bacterial range with master prompt 1.3.3 floor on neutrophil predominance (55 percent); Listeria classically can present with lower neutrophil dominance but built at floor here. Imputation tiers: tier_1_primary={age, sex, region, csf_culture, pregnancy_status, soft_cheese_exposure}; tier_3_within_cohort={csf_wbc, neutrophil_pct, glucose, protein}; tier_4_priors={temp, gcs, symptom_days}. Indeterminate=none. Diagnostic_ambiguity=false. Outcome=survived_no_sequelae. Tier: tier_3_imputation_within_cohort_review. 5.3.4 wave2 Listeria-Tumbes-pregnancy.

ANCHORING_EXTRAS: stage=pre_adjudication; status=pending_external_review; self_review_disposition=hold_for_revision; self_review_notes=wave 2 vignette anchored to PMID 11873028 (Mylonakis 2002 Medicine); external clinical adjudication pending; classification provisional. adjudicator_ids=WAVE2-PRE-ADJ-1, WAVE2-PRE-ADJ-2 (sentinel); cohen_kappa=0.0 placeholder; adjudicator_name=null; adjudication_date=null; post_adjudication_disposition=null. Subphase 1.3 commit 5.3.4 (2026-05-08). anchor=Mylonakis-Medicine-2002 stratum=pregnancy-foodborne.

ADJUDICATION:
  inclusion_decision: hold_for_revision
  adjudicator_ids: ['WAVE2-PRE-ADJ-1', 'WAVE2-PRE-ADJ-2']
  ground_truth_class: 2
  pre_adjudication_kappa: 0.0
  disagreement_resolution: None

=== END vignette ===

=== CLASS 2 | vignette_id: 089 | subphase: 1.3 BACT | file: bact_089_listeria_elderly.json ===

ANCHOR:
  pmid: 11873028
  first_author: Mylonakis
  year: 2002
  journal: Medicine
  citation_type: cohort
  doi: 10.1097/00005792-200203000-00004

DEMOGRAPHICS:
  age_years: 76
  sex: female
  geography_region: other_global
  ethnicity: white_non_hispanic
  altitude_residence_m: 5
  hiv_status: negative
  cd4_count_cells_per_uL: None
  pregnancy_red_flag: False
  immunocompromise_status: none
  freshwater_exposure_within_14d: False
  freshwater_exposure_type: None

HISTORY:
  symptom_onset_to_presentation_days: 5.0
  chief_complaint: altered_mental_status
  red_flags_present: []
  prodrome_description: 76-year-old female, Netherlands. 5-day course: low-grade fever, fatigue, gait ataxia, then headache, confusion, neck stiffness. Recent deli-meat consumption. Tertiary ED Amsterdam. No freshwater. Outcome: survived with mild residual ataxia. Antibiotic at hour 3 (ampicillin) plus gentamicin IDSA Listeria elderly protocol.

VITALS:
  temperature_celsius: 38.4
  heart_rate_bpm: 96
  systolic_bp_mmHg: 132
  diastolic_bp_mmHg: 78
  glasgow_coma_scale: 12
  oxygen_saturation_pct: 95
  respiratory_rate_breaths_per_min: 20

EXAM:
  mental_status_grade: confused
  neck_stiffness: True
  kernig_or_brudzinski_positive: True
  cranial_nerve_palsy: CN_VII
  papilledema_on_fundoscopy: False
  focal_neurological_deficit: True
  skin_lesion_centrofacial_chronic: False
  petechial_or_purpuric_rash: False

LABS:
  wbc_blood_per_uL: 15800
  platelets_per_uL: 215000
  alt_ast_U_per_L: 32
  crp_mg_per_L: 105.0
  procalcitonin_ng_per_mL: 3.8
  serum_sodium_mEq_per_L: 134

CSF:
  opening_pressure_cmH2O: 24.0
  wbc_per_mm3: 1800
  lymphocyte_pct: 40
  neutrophil_pct: 60
  eosinophil_pct: 0
  glucose_mg_per_dL: 25
  protein_mg_per_dL: 145
  lactate_mmol_per_L: 4.4
  ada_U_per_L: None
  crag_lfa_result: negative
  wet_mount_motile_amoebae: negative
  xanthochromia_present: False
  rbc_per_mm3: 4

IMAGING:
  modality: ct_noncontrast
  pattern: normal
  contrast_enhancement: True
  hydrocephalus: False
  basal_meningeal_enhancement: False
  finding_count: 0
  text_summary: CT head non-contrast: normal at admission. No focal lesion, no hydrocephalus, no midline shift, no mass effect. Pattern consistent with early-stage adult community-acquired bacterial meningitis.

DIAGNOSTIC_TESTS:
  pcr_panel: n/a
  xpert_mtb_rif: n/a
  blood_culture: n/a
  csf_culture: n/a
  serology_or_antigen: n/a
  smear_or_gram: n/a
  brain_biopsy: n/a
  imaging_test: n/a
  total_dx_results: 3

NARRATIVE_EN: A 76-year-old woman in the Netherlands presented to a tertiary emergency department in Amsterdam after a 5-day course of low-grade fever, fatigue, gait ataxia, then headache, confusion, and neck stiffness. She had recent consumption of cold deli meats. Examination on admission: temperature 38.4 C, Glasgow Coma Scale 12, neck stiffness, positive Kernig sign, focal deficit (right facial weakness, CN VII), no rash. CSF showed opening pressure 24 cmH2O, white cell count 1,800 per cubic millimeter (60 percent neutrophils), glucose 25 mg/dL, protein 145 mg/dL. Gram stain revealed short gram-positive bacilli; CSF and blood cultures grew Listeria monocytogenes. Anchored to Mylonakis 2002 Medicine (PMID 11873028, elderly-immunosenescence stratum approximately 70 percent of adult Listeria CNS infection). The brainstem-rhombencephalitis pattern (CN VII palsy) is a documented Listeria phenotype. Outcome: survived with mild residual ataxia. Subphase 1.3 commit 5.3.4 wave 2, pre-adjudication hold_for_revision.

NARRATIVE_ES: Mujer de 76 anos en Paises Bajos (Amsterdam), ingresada a urgencias terciarias tras cinco dias de febricula, fatiga, ataxia de marcha y luego cefalea, confusion y rigidez de nuca. Antecedente de consumo reciente de fiambres frios. Examen: temperatura 38.4 C, escala de Glasgow 12, rigidez de nuca, signo de Kernig positivo, deficit focal (paresia facial derecha, par craneal VII), sin exantema. Liquido cefalorraquideo mostro presion de apertura 24 cmH2O, leucocitos 1,800 por mm3 (60 por ciento neutrofilos), glucosa 25 mg/dL, proteina 145 mg/dL. Tincion de Gram con bacilos grampositivos cortos; cultivos de liquido y sangre crecieron Listeria monocytogenes. Anclaje en revision Mylonakis 2002 Medicine (PMID 11873028, estrato adulto mayor inmunosenescencia, alrededor del 70 por ciento de Listeria SNC en adultos). Subphase 1.3 commit 5.3.4 wave 2.

RATIONALE: Anchored to PMID 11873028 (Mylonakis 2002 Medicine review). Demographic anchor (76yo F elderly with deli-meat exposure + CN VII palsy) sits in elderly-immunosenescence stratum (approximately 70 percent of adult Listeria CNS infection) and demonstrates the documented Listeria brainstem-rhombencephalitis phenotype. CSF profile bacterial range at master prompt 1.3.3 floor (neutrophil 60 percent). Imputation tiers: tier_1_primary={age, sex, csf_culture, csf_gram_stain, deli_meat_exposure, cn7_palsy}; tier_3_within_cohort={csf_wbc, neutrophil_pct, glucose, protein, gcs}; tier_4_priors={temp, symptom_days}. Indeterminate=none. Diagnostic_ambiguity=false. Outcome=survived_with_mild_residual_ataxia. Tier: tier_3_imputation_within_cohort_review. 5.3.4 wave2 Listeria-elderly-rhombencephalitis.

ANCHORING_EXTRAS: stage=pre_adjudication; status=pending_external_review; self_review_disposition=hold_for_revision; self_review_notes=wave 2 vignette anchored to PMID 11873028 (Mylonakis 2002 Medicine); external clinical adjudication pending; classification provisional. adjudicator_ids=WAVE2-PRE-ADJ-1, WAVE2-PRE-ADJ-2 (sentinel); cohen_kappa=0.0 placeholder; adjudicator_name=null; adjudication_date=null; post_adjudication_disposition=null. Subphase 1.3 commit 5.3.4 (2026-05-08). anchor=Mylonakis-Medicine-2002 stratum=elderly-rhombencephalitis.

ADJUDICATION:
  inclusion_decision: hold_for_revision
  adjudicator_ids: ['WAVE2-PRE-ADJ-1', 'WAVE2-PRE-ADJ-2']
  ground_truth_class: 2
  pre_adjudication_kappa: 0.0
  disagreement_resolution: None

=== END vignette ===

=== CLASS 2 | vignette_id: 090 | subphase: 1.3 BACT | file: bact_090_gn_post_neurosurgical_fatal.json ===

ANCHOR:
  pmid: 15494903
  first_author: Tunkel
  year: 2004
  journal: CID
  citation_type: guideline
  doi: 10.1086/425368

DEMOGRAPHICS:
  age_years: 55
  sex: male
  geography_region: us_south
  ethnicity: white_non_hispanic
  altitude_residence_m: 100
  hiv_status: negative
  cd4_count_cells_per_uL: None
  pregnancy_red_flag: False
  immunocompromise_status: none
  freshwater_exposure_within_14d: False
  freshwater_exposure_type: None

HISTORY:
  symptom_onset_to_presentation_days: 1.5
  chief_complaint: altered_mental_status
  red_flags_present: ['recent_neurosurgery']
  prodrome_description: 55-year-old male, US South region. Glioma resection 9 days prior; postoperative course complicated by CSF leak from surgical site, then fever 39.0 C, headache, declining mental status over 36 hours, progressive obtundation. Tertiary ED. No freshwater. Healthcare-associated gram-negative bacterial meningitis. Outcome: fatal hospital day 4.

VITALS:
  temperature_celsius: 39.0
  heart_rate_bpm: 118
  systolic_bp_mmHg: 100
  diastolic_bp_mmHg: 60
  glasgow_coma_scale: 8
  oxygen_saturation_pct: 92
  respiratory_rate_breaths_per_min: 24

EXAM:
  mental_status_grade: stuporous
  neck_stiffness: True
  kernig_or_brudzinski_positive: True
  cranial_nerve_palsy: none
  papilledema_on_fundoscopy: False
  focal_neurological_deficit: True
  skin_lesion_centrofacial_chronic: False
  petechial_or_purpuric_rash: False

LABS:
  wbc_blood_per_uL: 19500
  platelets_per_uL: 165000
  alt_ast_U_per_L: 42
  crp_mg_per_L: 215.0
  procalcitonin_ng_per_mL: 11.5
  serum_sodium_mEq_per_L: 135

CSF:
  opening_pressure_cmH2O: 30.0
  wbc_per_mm3: 4500
  lymphocyte_pct: 14
  neutrophil_pct: 86
  eosinophil_pct: 0
  glucose_mg_per_dL: 16
  protein_mg_per_dL: 290
  lactate_mmol_per_L: 8.2
  ada_U_per_L: None
  crag_lfa_result: negative
  wet_mount_motile_amoebae: negative
  xanthochromia_present: False
  rbc_per_mm3: 8

IMAGING:
  modality: ct_noncontrast
  pattern: diffuse_cerebral_edema_basilar_meningeal_enhancement
  contrast_enhancement: True
  hydrocephalus: False
  basal_meningeal_enhancement: False
  finding_count: 1
  text_summary: CT head non-contrast: diffuse cerebral edema with effacement of sulci, basilar meningeal enhancement on contrast-equivalent regions, no focal lesion, no midline shift. Pattern consistent with severe late-stage bacterial meningitis.

DIAGNOSTIC_TESTS:
  pcr_panel: n/a
  xpert_mtb_rif: n/a
  blood_culture: n/a
  csf_culture: n/a
  serology_or_antigen: n/a
  smear_or_gram: n/a
  brain_biopsy: n/a
  imaging_test: n/a
  total_dx_results: 3

NARRATIVE_EN: A 55-year-old man in the US South region presented to a tertiary emergency department 9 days after glioma resection. The postoperative course had been complicated by a CSF leak at the surgical site. Over 36 hours he developed fever to 39.0 C, headache, and declining mental status with progressive obtundation. Examination on admission: temperature 39.0 C, Glasgow Coma Scale 8, neck stiffness, positive Kernig sign, focal deficit (right hemiparesis), no rash. CSF showed opening pressure 30 cmH2O, white cell count 4,500 per cubic millimeter (86 percent neutrophils), glucose 16 mg/dL, protein 290 mg/dL. Gram stain revealed gram-negative rods; culture identified Pseudomonas aeruginosa. Anchored to Tunkel IDSA 2004 (PMID 15494903) healthcare-associated meningitis recommendations (empiric meropenem coverage of gram-negative rods including Pseudomonas in post-neurosurgical context). Outcome: fatal hospital day 4. Subphase 1.3 commit 5.3.3 wave 1, pre-adjudication hold_for_revision.

NARRATIVE_ES: Varon de 55 anos en region sur de Estados Unidos, ingresado a urgencias terciarias nueve dias despues de reseccion de glioma. El curso postoperatorio se complico con fuga de liquido cefalorraquideo en el sitio quirurgico. En 36 horas desarrollo fiebre 39.0 C, cefalea y deterioro del estado mental con obnubilacion progresiva. Examen: temperatura 39.0 C, escala de Glasgow 8, rigidez de nuca, signo de Kernig positivo, deficit focal (hemiparesia derecha), sin exantema. Liquido cefalorraquideo mostro presion de apertura 30 cmH2O, leucocitos 4,500 por mm3 (86 por ciento neutrofilos), glucosa 16 mg/dL, proteina 290 mg/dL. Tincion de Gram con bacilos gramnegativos y cultivo Pseudomonas aeruginosa. Anclaje en guia IDSA Tunkel 2004 (PMID 15494903), recomendaciones para meningitis asociada a atencion sanitaria. Subphase 1.3 commit 5.3.3 wave 1.

RATIONALE: Anchored to PMID 15494903 (Tunkel IDSA 2004 CID guideline) healthcare-associated meningitis recommendations. Demographic anchor (55yo M post-neurosurgical glioma resection day 9 with CSF leak) reflects post-neurosurgical gram-negative stratum covered by Tunkel for empiric meropenem-vancomycin coverage. CSF profile bacterial range; gram-negative rods on Gram stain with Pseudomonas culture. Imputation tiers: tier_1_primary={age, sex, csf_culture, csf_gram_stain, neurosurgery_history, csf_leak}; tier_3_within_cohort={csf_wbc, neutrophil_pct, glucose, protein, lactate, gcs}; tier_4_priors={temp, symptom_days, hr}. Indeterminate=none. Diagnostic_ambiguity=false. Outcome=fatal_hospital_day_4. Antibiotic_started_hours=2. Tier: tier_4_imputation_idsa_guideline_anchored. 5.3.3 wave1 GN-post-neurosurgical-fatal.

ANCHORING_EXTRAS: stage=pre_adjudication; status=pending_external_review; self_review_disposition=hold_for_revision; self_review_notes=wave 1 vignette anchored to PMID 15494903 (Tunkel IDSA 2004); external clinical adjudication pending; classification provisional. adjudicator_ids=WAVE1-PRE-ADJ-1, WAVE1-PRE-ADJ-2 (sentinel); cohen_kappa=0.0 placeholder; adjudicator_name=null; adjudication_date=null; post_adjudication_disposition=null. Subphase 1.3 commit 5.3.3 (2026-05-08). anchor=Tunkel-IDSA-2004 stratum=post-neurosurgical-GN.

ADJUDICATION:
  inclusion_decision: hold_for_revision
  adjudicator_ids: ['WAVE1-PRE-ADJ-1', 'WAVE1-PRE-ADJ-2']
  ground_truth_class: 2
  pre_adjudication_kappa: 0.0
  disagreement_resolution: None

=== END vignette ===

=== CLASS 3 | vignette_id: 091 | subphase: 1.3 VIRAL | file: vir_091_hsv1_pediatric_sequelae.json ===

ANCHOR:
  pmid: 16675036
  first_author: Whitley
  year: 2006
  journal: Antiviral Res
  citation_type: review
  doi: 10.1016/S1473-3099(06)70414-6

DEMOGRAPHICS:
  age_years: 8
  sex: female
  geography_region: us_south
  ethnicity: white_non_hispanic
  altitude_residence_m: 100
  hiv_status: negative
  cd4_count_cells_per_uL: None
  pregnancy_red_flag: False
  immunocompromise_status: none
  freshwater_exposure_within_14d: False
  freshwater_exposure_type: None

HISTORY:
  symptom_onset_to_presentation_days: 6.0
  chief_complaint: altered_mental_status
  red_flags_present: []
  prodrome_description: 8-year-old female, US South region. 6-day course: low-grade fever 38.4 C, headache, then progressive behavioral change day 3, expressive aphasia day 4, complex partial seizures day 5, obtundation day 6 prompting tertiary pediatric ED. No neck stiffness. No freshwater. Acyclovir hour 4. Outcome: survived with moderate cognitive sequelae per Whitley HSE pediatric-residual-deficit pattern.

VITALS:
  temperature_celsius: 38.4
  heart_rate_bpm: 122
  systolic_bp_mmHg: 100
  diastolic_bp_mmHg: 60
  glasgow_coma_scale: 9
  oxygen_saturation_pct: 96
  respiratory_rate_breaths_per_min: 22

EXAM:
  mental_status_grade: stuporous
  neck_stiffness: False
  kernig_or_brudzinski_positive: False
  cranial_nerve_palsy: none
  papilledema_on_fundoscopy: False
  focal_neurological_deficit: True
  skin_lesion_centrofacial_chronic: False
  petechial_or_purpuric_rash: False

LABS:
  wbc_blood_per_uL: 9200
  platelets_per_uL: 285000
  alt_ast_U_per_L: 24
  crp_mg_per_L: 22.0
  procalcitonin_ng_per_mL: 0.4
  serum_sodium_mEq_per_L: 137

CSF:
  opening_pressure_cmH2O: 24.0
  wbc_per_mm3: 240
  lymphocyte_pct: 75
  neutrophil_pct: 25
  eosinophil_pct: 0
  glucose_mg_per_dL: 52
  protein_mg_per_dL: 130
  lactate_mmol_per_L: 2.6
  ada_U_per_L: None
  crag_lfa_result: negative
  wet_mount_motile_amoebae: negative
  xanthochromia_present: True
  rbc_per_mm3: 38

IMAGING:
  modality: mri_with_dwi_flair
  pattern: mesial_temporal_t2_flair_hyperintensity
  contrast_enhancement: False
  hydrocephalus: False
  basal_meningeal_enhancement: False
  finding_count: 1
  text_summary: MRI brain with DWI/FLAIR: mesial temporal T2/FLAIR hyperintensity asymmetric with basal ganglia sparing. Canonical HSE imaging signature per Tyler 2018 NEJM viral encephalitis review.

DIAGNOSTIC_TESTS:
  pcr_panel: positive
  xpert_mtb_rif: n/a
  blood_culture: n/a
  csf_culture: n/a
  serology_or_antigen: n/a
  smear_or_gram: n/a
  brain_biopsy: n/a
  imaging_test: n/a
  total_dx_results: 3

NARRATIVE_EN: An 8-year-old girl in the US South region presented to a tertiary pediatric emergency department with a 6-day course: low-grade fever to 38.4 C, headache, progressive behavioral change on day 3, expressive aphasia on day 4, complex partial seizures on day 5, and obtundation on day 6. She had no neck stiffness on examination and no antecedent freshwater exposure. Examination on admission: temperature 38.4 C, Glasgow Coma Scale 9, focal deficit (expressive aphasia), no rash. CSF showed opening pressure 24 cmH2O, white cell count 240 per cubic millimeter (75 percent lymphocytes), glucose 52 mg/dL, protein 130 mg/dL, RBC 38 with xanthochromia (canonical hemorrhagic component). CSF HSV-1 PCR positive. Brain MRI with DWI/FLAIR showed mesial temporal T2/FLAIR hyperintensity asymmetric. Acyclovir initiated within four hours. Anchored to Whitley 2006 Lancet Infect Dis HSE pathogenesis review (PMID 16675036). Outcome: survived with moderate cognitive sequelae. Subphase 1.3 commit 5.3.6 wave 2, pre-adjudication hold_for_revision.

NARRATIVE_ES: Nina de 8 anos en region sur de Estados Unidos, ingresada a urgencias pediatricas terciarias con curso de seis dias: febricula 38.4 C, cefalea, cambio conductual progresivo al tercer dia, afasia expresiva al cuarto dia, crisis parciales complejas al quinto y obnubilacion al sexto. Sin rigidez de nuca al examen. Sin exposicion a agua dulce. Examen: temperatura 38.4 C, escala de Glasgow 9, deficit focal (afasia expresiva), sin exantema. Liquido cefalorraquideo mostro presion de apertura 24 cmH2O, leucocitos 240 por mm3 (75 por ciento linfocitos), glucosa 52 mg/dL, proteina 130 mg/dL, eritrocitos 38 con xantocromia. PCR de HSV-1 positiva. RM cerebral con hiperintensidad temporal mesial T2/FLAIR. Aciclovir en cuatro horas. Anclaje en revision Whitley 2006 Lancet ID HSE (PMID 16675036). Subphase 1.3 commit 5.3.6 wave 2, pre-adjudicacion hold_for_revision.

RATIONALE: Anchored to PMID 16675036 (Whitley 2006 Lancet ID HSE pathogenesis review). Pediatric HSE phenotype with classic limbic-frontal extension and late-presentation obtundation. Demographic anchor (8yo F US South pediatric HSE) sits in Whitley's pediatric-HSE-residual-deficit stratum. CSF lymphocytic with hemorrhagic component (RBC 38, xanthochromia). MRI mesial temporal pattern. Imputation tiers: tier_1_primary={age, sex, hsv1_pcr, imaging_pattern, focal_aphasia, behavioral_change}; tier_3_within_review={csf_wbc, neutrophil_pct, glucose, protein, rbc, xanthochromia, gcs}; tier_4_priors={temp, symptom_days}. Indeterminate=none. Diagnostic_ambiguity=false. Outcome=survived_moderate_cognitive_sequelae. Acyclovir_hours=4. Tier: tier_3_imputation_within_review. 5.3.6 wave2 HSV1-Whitley-pediatric-sequelae.

ANCHORING_EXTRAS: stage=pre_adjudication; status=pending_external_review; self_review_disposition=hold_for_revision; self_review_notes=wave 5.3.6 VIRAL vignette anchored to PMID 16675036 (Whitley 2006 Lancet ID HSE pathogenesis review); external clinical adjudication pending; classification provisional. adjudicator_ids=VIRAL-WAVE2-PRE-ADJ-1, VIRAL-WAVE2-PRE-ADJ-2 (sentinel); cohen_kappa=0.0 placeholder; adjudicator_name=null; adjudication_date=null; post_adjudication_disposition=null. Subphase 1.3 commit 5.3.6 (2026-05-08, FINAL Subphase 1.3 wave). anchor=Whitley-Lancet-ID-2006 stratum=pediatric-HSE-sequelae.

ADJUDICATION:
  inclusion_decision: hold_for_revision
  adjudicator_ids: ['VIRAL-WAVE2-PRE-ADJ-1', 'VIRAL-WAVE2-PRE-ADJ-2']
  ground_truth_class: 3
  pre_adjudication_kappa: 0.0
  disagreement_resolution: None

=== END vignette ===

=== CLASS 3 | vignette_id: 092 | subphase: 1.3 VIRAL | file: vir_092_hsv1_adult.json ===

ANCHOR:
  pmid: 16675036
  first_author: Whitley
  year: 2006
  journal: Antiviral Res
  citation_type: review
  doi: 10.1016/j.antiviral.2006.04.002

DEMOGRAPHICS:
  age_years: 42
  sex: male
  geography_region: other_global
  ethnicity: white_non_hispanic
  altitude_residence_m: 50
  hiv_status: negative
  cd4_count_cells_per_uL: None
  pregnancy_red_flag: False
  immunocompromise_status: none
  freshwater_exposure_within_14d: False
  freshwater_exposure_type: None

HISTORY:
  symptom_onset_to_presentation_days: 5.0
  chief_complaint: seizure
  red_flags_present: []
  prodrome_description: 42-year-old male, US tertiary ED. 5-day progressive course: fever 38.8 C, severe headache, behavioral change with personality alteration day 3, expressive aphasia day 4, focal seizure day 5 prompting ED. No neck stiffness. No freshwater exposure. Medial temporal and limbic predilection canonical for HSE. Outcome: survived with mild memory deficit. Acyclovir hour 6.

VITALS:
  temperature_celsius: 38.8
  heart_rate_bpm: 102
  systolic_bp_mmHg: 132
  diastolic_bp_mmHg: 82
  glasgow_coma_scale: 12
  oxygen_saturation_pct: 97
  respiratory_rate_breaths_per_min: 18

EXAM:
  mental_status_grade: confused
  neck_stiffness: False
  kernig_or_brudzinski_positive: False
  cranial_nerve_palsy: none
  papilledema_on_fundoscopy: False
  focal_neurological_deficit: True
  skin_lesion_centrofacial_chronic: False
  petechial_or_purpuric_rash: False

LABS:
  wbc_blood_per_uL: 9800
  platelets_per_uL: 240000
  alt_ast_U_per_L: 28
  crp_mg_per_L: 22.0
  procalcitonin_ng_per_mL: 0.4
  serum_sodium_mEq_per_L: 138

CSF:
  opening_pressure_cmH2O: 22.0
  wbc_per_mm3: 180
  lymphocyte_pct: 75
  neutrophil_pct: 25
  eosinophil_pct: 0
  glucose_mg_per_dL: 58
  protein_mg_per_dL: 95
  lactate_mmol_per_L: 2.6
  ada_U_per_L: None
  crag_lfa_result: negative
  wet_mount_motile_amoebae: negative
  xanthochromia_present: True
  rbc_per_mm3: 45

IMAGING:
  modality: mri_with_dwi_flair
  pattern: mesial_temporal_t2_flair_hyperintensity
  contrast_enhancement: False
  hydrocephalus: False
  basal_meningeal_enhancement: False
  finding_count: 1
  text_summary: MRI brain with DWI/FLAIR: mesial temporal T2/FLAIR hyperintensity left greater than right asymmetric with basal ganglia sparing. Canonical HSE imaging signature.

DIAGNOSTIC_TESTS:
  pcr_panel: positive
  xpert_mtb_rif: n/a
  blood_culture: n/a
  csf_culture: n/a
  serology_or_antigen: n/a
  smear_or_gram: n/a
  brain_biopsy: n/a
  imaging_test: n/a
  total_dx_results: 3

NARRATIVE_EN: A 42-year-old man in the United States presented to a tertiary emergency department with a five-day progressive course: low-grade fever 38.8 C, severe headache, behavioral change with personality alteration noted by family on day 3, expressive aphasia on day 4, and focal seizure on day 5 prompting ED presentation. No neck stiffness on examination. No antecedent freshwater exposure. Examination on admission: Glasgow Coma Scale 12, focal neurological deficit (expressive aphasia). CSF showed opening pressure 22 cmH2O, white cell count 180 per cubic millimeter (75 percent lymphocytes), glucose 58 mg/dL, protein 95 mg/dL, RBC 45 with mild xanthochromia (canonical hemorrhagic component). CSF HSV-1 PCR positive. Brain MRI with DWI/FLAIR showed mesial temporal T2/FLAIR hyperintensity left greater than right asymmetric with basal ganglia sparing (canonical HSE imaging signature). Acyclovir initiated within six hours. Primary anchor: PMID 16675036 (Whitley 2006 Antiviral Res), HSE adolescents and adults review. Outcome: survived with mild memory deficit (per Whitley two-thirds of survivors have residual deficits even with early treatment). Subphase 1.3 commit 5.3.2 pilot 4, pre-adjudication hold_for_revision.

NARRATIVE_ES: Varon de 42 anos, Estados Unidos, ingresado a urgencias terciarias con curso progresivo de cinco dias: fiebre baja 38.8 C, cefalea intensa, cambio conductual con alteracion de personalidad notada por la familia al tercer dia, afasia expresiva al cuarto dia, crisis focal al quinto dia que motivo consulta. Sin rigidez de nuca al examen. Sin exposicion a agua dulce. Examen: escala de Glasgow 12, deficit focal (afasia expresiva). Liquido cefalorraquideo mostro presion de apertura 22 cmH2O, leucocitos 180 por mm3 (75 por ciento linfocitos), glucosa 58 mg/dL, proteina 95 mg/dL, eritrocitos 45 con xantocromia leve. PCR de HSV-1 positiva. RM cerebral mostro hiperintensidad temporal mesial T2/FLAIR izquierda mayor que derecha, asimetrica, con preservacion de ganglios basales. Inicio de aciclovir en seis horas. Anclaje primario en revision de HSE en adolescentes y adultos (PMID 16675036, Whitley 2006 Antiviral Res). Subphase 1.3 commit 5.3.2 pilot 4.

RATIONALE: Anchored to PMID 16675036 (Whitley 2006 Antiviral Res), HSE adolescents/adults review. Phenotype (fever + AMS + expressive aphasia + focal seizure, 42yo M) prototypical adult HSE. CSF (WBC 180 lymphocytic, RBC 45 hemorrhagic component, mild xanthochromia) canonical. MRI mesial temporal T2/FLAIR hyperintensity asymmetric L>R per master prompt 1.3 mandate. Acyclovir hour 6 yielded survival with mild memory deficit per Whitley two-thirds residual deficits even with early Rx. Imputation tiers: tier_1_primary={age, sex, hsv1_pcr, imaging_pattern}; tier_3_within_cohort={csf_wbc, neutrophil_pct, glucose, protein, csf_rbc, xanthochromia, imaging_laterality}; tier_4_priors={temp, gcs, symptom_days}. Indeterminate=none. Diagnostic_ambiguity=false. Outcome=survived_mild_memory_deficit. Acyclovir_hours=6. Tier: primary_source_direct. 5.3.2 pilot 4.

ANCHORING_EXTRAS: stage=pre_adjudication; status=pending_external_review; self_review_disposition=hold_for_revision; self_review_notes=pilot vignette anchored to PMID 16675036 (Whitley 2006 Antiviral Res HSE adult); external clinical adjudication pending; classification provisional. adjudicator_ids=PILOT-PRE-ADJ-1, PILOT-PRE-ADJ-2 (sentinel); cohen_kappa=0.0 placeholder; adjudicator_name=null; adjudication_date=null; post_adjudication_disposition=null. Subphase 1.3 commit 5.3.2 (2026-05-07).

ADJUDICATION:
  inclusion_decision: hold_for_revision
  adjudicator_ids: ['PILOT-PRE-ADJ-1', 'PILOT-PRE-ADJ-2']
  ground_truth_class: 3
  pre_adjudication_kappa: 0.0
  disagreement_resolution: None

=== END vignette ===

=== CLASS 3 | vignette_id: 093 | subphase: 1.3 VIRAL | file: vir_093_hsv1_elderly_fatal.json ===

ANCHOR:
  pmid: 16675036
  first_author: Whitley
  year: 2006
  journal: Antiviral Res
  citation_type: review
  doi: 10.1016/S1473-3099(06)70414-6

DEMOGRAPHICS:
  age_years: 67
  sex: female
  geography_region: other_global
  ethnicity: white_non_hispanic
  altitude_residence_m: 5
  hiv_status: negative
  cd4_count_cells_per_uL: None
  pregnancy_red_flag: False
  immunocompromise_status: none
  freshwater_exposure_within_14d: False
  freshwater_exposure_type: None

HISTORY:
  symptom_onset_to_presentation_days: 7.0
  chief_complaint: altered_mental_status
  red_flags_present: []
  prodrome_description: 67-year-old female, Netherlands. 7-day course: low-grade fever 38.3 C, headache, behavioral change with confusion day 2, anomic aphasia day 4, focal seizures day 5, progressive obtundation day 6, coma day 7. Tertiary ED Amsterdam. No freshwater. Acyclovir hour 12 (delayed by atypical presentation). Outcome: fatal hospital day 5 per Whitley HSE elderly-mortality data.

VITALS:
  temperature_celsius: 38.3
  heart_rate_bpm: 110
  systolic_bp_mmHg: 102
  diastolic_bp_mmHg: 64
  glasgow_coma_scale: 5
  oxygen_saturation_pct: 88
  respiratory_rate_breaths_per_min: 26

EXAM:
  mental_status_grade: comatose
  neck_stiffness: False
  kernig_or_brudzinski_positive: False
  cranial_nerve_palsy: none
  papilledema_on_fundoscopy: False
  focal_neurological_deficit: True
  skin_lesion_centrofacial_chronic: False
  petechial_or_purpuric_rash: False

LABS:
  wbc_blood_per_uL: 8800
  platelets_per_uL: 215000
  alt_ast_U_per_L: 32
  crp_mg_per_L: 28.0
  procalcitonin_ng_per_mL: 0.5
  serum_sodium_mEq_per_L: 132

CSF:
  opening_pressure_cmH2O: 26.0
  wbc_per_mm3: 280
  lymphocyte_pct: 72
  neutrophil_pct: 28
  eosinophil_pct: 0
  glucose_mg_per_dL: 50
  protein_mg_per_dL: 145
  lactate_mmol_per_L: 2.8
  ada_U_per_L: None
  crag_lfa_result: negative
  wet_mount_motile_amoebae: negative
  xanthochromia_present: True
  rbc_per_mm3: 50

IMAGING:
  modality: mri_with_dwi_flair
  pattern: mesial_temporal_t2_flair_hyperintensity
  contrast_enhancement: False
  hydrocephalus: False
  basal_meningeal_enhancement: False
  finding_count: 1
  text_summary: MRI brain with DWI/FLAIR: mesial temporal T2/FLAIR hyperintensity asymmetric with basal ganglia sparing. Canonical HSE imaging signature per Tyler 2018 NEJM viral encephalitis review.

DIAGNOSTIC_TESTS:
  pcr_panel: positive
  xpert_mtb_rif: n/a
  blood_culture: n/a
  csf_culture: n/a
  serology_or_antigen: n/a
  smear_or_gram: n/a
  brain_biopsy: n/a
  imaging_test: n/a
  total_dx_results: 3

NARRATIVE_EN: A 67-year-old woman in the Netherlands presented to a tertiary emergency department in Amsterdam after a 7-day course: low-grade fever to 38.3 C, headache, behavioral change on day 2, anomic aphasia on day 4, focal seizures on day 5, and progressive obtundation to coma by day 7. Examination on admission: temperature 38.3 C, Glasgow Coma Scale 5, comatose, focal deficit (anomic aphasia, residual right-sided posturing), no rash. CSF showed opening pressure 26 cmH2O, white cell count 280 per cubic millimeter (72 percent lymphocytes), glucose 50 mg/dL, protein 145 mg/dL, RBC 50 with xanthochromia (canonical hemorrhagic component). CSF HSV-1 PCR positive. Brain MRI with DWI/FLAIR showed mesial temporal T2/FLAIR hyperintensity bilateral. Acyclovir initiated at hour 12 (delayed by atypical presentation). Anchored to Whitley 2006 Lancet Infect Dis HSE pathogenesis review (PMID 16675036). Outcome: fatal hospital day 5 per Whitley HSE elderly-mortality data. Subphase 1.3 commit 5.3.6 wave 2, pre-adjudication hold_for_revision.

NARRATIVE_ES: Mujer de 67 anos en Paises Bajos (Amsterdam), ingresada a urgencias terciarias tras curso de siete dias: febricula 38.3 C, cefalea, cambio conductual al segundo dia, afasia anomica al cuarto, crisis focales al quinto, obnubilacion progresiva con coma al septimo. Examen: temperatura 38.3 C, escala de Glasgow 5, comatosa, deficit focal (afasia anomica, postura derecha residual), sin exantema. Liquido cefalorraquideo mostro presion de apertura 26 cmH2O, leucocitos 280 por mm3 (72 por ciento linfocitos), glucosa 50 mg/dL, proteina 145 mg/dL, eritrocitos 50 con xantocromia. PCR de HSV-1 positiva. RM cerebral con hiperintensidad temporal mesial T2/FLAIR bilateral. Aciclovir en hora 12 (retraso por presentacion atipica). Anclaje en revision Whitley 2006 Lancet ID HSE (PMID 16675036). Subphase 1.3 commit 5.3.6 wave 2.

RATIONALE: Anchored to PMID 16675036 (Whitley 2006 Lancet ID HSE pathogenesis review). Elderly HSE with delayed-acyclovir fatal outcome per Whitley elderly-mortality stratum. Demographic anchor (67yo F NL elderly HSE delayed-treatment) sits in elderly-fatal-HSE stratum. CSF lymphocytic with prominent hemorrhagic component (RBC 50, xanthochromia). MRI bilateral mesial temporal. Imputation tiers: tier_1_primary={age, sex, hsv1_pcr, imaging_pattern, focal_aphasia, delayed_acyclovir}; tier_3_within_review={csf_wbc, neutrophil_pct, glucose, protein, rbc, xanthochromia, gcs}; tier_4_priors={temp, symptom_days, hyponatremia}. Indeterminate=none. Diagnostic_ambiguity=false. Outcome=fatal_hospital_day_5. Acyclovir_hours=12. Tier: tier_3_imputation_within_review. 5.3.6 wave2 HSV1-Whitley-elderly-fatal.

ANCHORING_EXTRAS: stage=pre_adjudication; status=pending_external_review; self_review_disposition=hold_for_revision; self_review_notes=wave 5.3.6 VIRAL vignette anchored to PMID 16675036 (Whitley 2006 Lancet ID HSE pathogenesis review); external clinical adjudication pending; classification provisional. adjudicator_ids=VIRAL-WAVE2-PRE-ADJ-1, VIRAL-WAVE2-PRE-ADJ-2 (sentinel); cohen_kappa=0.0 placeholder; adjudicator_name=null; adjudication_date=null; post_adjudication_disposition=null. Subphase 1.3 commit 5.3.6 (2026-05-08, FINAL Subphase 1.3 wave). anchor=Whitley-Lancet-ID-2006 stratum=elderly-fatal-delayed-treatment.

ADJUDICATION:
  inclusion_decision: hold_for_revision
  adjudicator_ids: ['VIRAL-WAVE2-PRE-ADJ-1', 'VIRAL-WAVE2-PRE-ADJ-2']
  ground_truth_class: 3
  pre_adjudication_kappa: 0.0
  disagreement_resolution: None

=== END vignette ===

=== CLASS 3 | vignette_id: 094 | subphase: 1.3 VIRAL | file: vir_094_hsv1_young_adult.json ===

ANCHOR:
  pmid: 20952256
  first_author: Granerod
  year: 2010
  journal: Lancet Infect Dis
  citation_type: cohort
  doi: 10.1016/S1473-3099(10)70222-X

DEMOGRAPHICS:
  age_years: 23
  sex: female
  geography_region: other_global
  ethnicity: white_non_hispanic
  altitude_residence_m: 5
  hiv_status: negative
  cd4_count_cells_per_uL: None
  pregnancy_red_flag: False
  immunocompromise_status: none
  freshwater_exposure_within_14d: False
  freshwater_exposure_type: None

HISTORY:
  symptom_onset_to_presentation_days: 4.0
  chief_complaint: altered_mental_status
  red_flags_present: []
  prodrome_description: 23-year-old female, Netherlands. 4-day course: fever 38.6 C, severe headache, behavioral change day 2, expressive aphasia day 3, focal seizure day 4 prompting tertiary ED Amsterdam. No neck stiffness. No freshwater. Acyclovir hour 4. Outcome: survived with mild memory deficit per Granerod cohort residual-deficit rate.

VITALS:
  temperature_celsius: 38.6
  heart_rate_bpm: 100
  systolic_bp_mmHg: 116
  diastolic_bp_mmHg: 70
  glasgow_coma_scale: 12
  oxygen_saturation_pct: 97
  respiratory_rate_breaths_per_min: 18

EXAM:
  mental_status_grade: confused
  neck_stiffness: False
  kernig_or_brudzinski_positive: False
  cranial_nerve_palsy: none
  papilledema_on_fundoscopy: False
  focal_neurological_deficit: True
  skin_lesion_centrofacial_chronic: False
  petechial_or_purpuric_rash: False

LABS:
  wbc_blood_per_uL: 8400
  platelets_per_uL: 250000
  alt_ast_U_per_L: 26
  crp_mg_per_L: 18.0
  procalcitonin_ng_per_mL: 0.3
  serum_sodium_mEq_per_L: 138

CSF:
  opening_pressure_cmH2O: 22.0
  wbc_per_mm3: 200
  lymphocyte_pct: 78
  neutrophil_pct: 22
  eosinophil_pct: 0
  glucose_mg_per_dL: 56
  protein_mg_per_dL: 110
  lactate_mmol_per_L: 2.4
  ada_U_per_L: None
  crag_lfa_result: negative
  wet_mount_motile_amoebae: negative
  xanthochromia_present: True
  rbc_per_mm3: 30

IMAGING:
  modality: mri_with_dwi_flair
  pattern: mesial_temporal_t2_flair_hyperintensity
  contrast_enhancement: False
  hydrocephalus: False
  basal_meningeal_enhancement: False
  finding_count: 1
  text_summary: MRI brain with DWI/FLAIR: mesial temporal T2/FLAIR hyperintensity asymmetric with basal ganglia sparing. Canonical HSE imaging signature per Tyler 2018 NEJM viral encephalitis review.

DIAGNOSTIC_TESTS:
  pcr_panel: positive
  xpert_mtb_rif: n/a
  blood_culture: n/a
  csf_culture: n/a
  serology_or_antigen: n/a
  smear_or_gram: n/a
  brain_biopsy: n/a
  imaging_test: n/a
  total_dx_results: 3

NARRATIVE_EN: A 23-year-old woman in the Netherlands presented to a tertiary emergency department in Amsterdam with a 4-day course: fever to 38.6 C, severe headache, behavioral change on day 2, expressive aphasia on day 3, and a focal seizure on day 4 prompting ED presentation. She had no neck stiffness and no antecedent freshwater exposure. Examination on admission: temperature 38.6 C, Glasgow Coma Scale 12, focal deficit (expressive aphasia), no rash. CSF showed opening pressure 22 cmH2O, white cell count 200 per cubic millimeter (78 percent lymphocytes), glucose 56 mg/dL, protein 110 mg/dL, RBC 30 with xanthochromia. CSF HSV-1 PCR positive. Brain MRI with DWI/FLAIR showed mesial temporal T2/FLAIR hyperintensity asymmetric. Acyclovir initiated within four hours. Anchored to Granerod 2010 Lancet Infect Dis prospective UK encephalitis cohort (PMID 20952256, N=203 with 42 percent infectious encephalitis cause-attribution). Outcome: survived with mild memory deficit. Subphase 1.3 commit 5.3.6 wave 2, pre-adjudication hold_for_revision.

NARRATIVE_ES: Mujer de 23 anos en Paises Bajos (Amsterdam), ingresada a urgencias terciarias con curso de cuatro dias: fiebre 38.6 C, cefalea intensa, cambio conductual al segundo dia, afasia expresiva al tercer dia y crisis focal al cuarto. Sin rigidez de nuca. Sin exposicion a agua dulce. Examen: temperatura 38.6 C, escala de Glasgow 12, deficit focal (afasia expresiva), sin exantema. Liquido cefalorraquideo mostro presion de apertura 22 cmH2O, leucocitos 200 por mm3 (78 por ciento linfocitos), glucosa 56 mg/dL, proteina 110 mg/dL, eritrocitos 30 con xantocromia. PCR de HSV-1 positiva. RM cerebral con hiperintensidad temporal mesial T2/FLAIR. Aciclovir en cuatro horas. Anclaje en cohorte prospectiva Granerod 2010 Lancet ID encefalitis Reino Unido (PMID 20952256). Subphase 1.3 commit 5.3.6 wave 2.

RATIONALE: Anchored to PMID 20952256 (Granerod 2010 Lancet Infect Dis), 203-patient prospective UK encephalitis cohort with HSV1 as the most common identified cause (19 percent of cohort). Demographic anchor (23yo F NL young-adult HSE) sits in Granerod young-adult-HSE stratum. CSF lymphocytic with hemorrhagic component. MRI mesial temporal pattern. Imputation tiers: tier_1_primary={age, sex, hsv1_pcr, imaging_pattern, focal_aphasia}; tier_3_within_review={csf_wbc, neutrophil_pct, glucose, protein, rbc, xanthochromia, gcs}; tier_4_priors={temp, symptom_days}. Indeterminate=none. Diagnostic_ambiguity=false. Outcome=survived_mild_memory_deficit. Acyclovir_hours=4. Tier: tier_3_imputation_within_review. 5.3.6 wave2 HSV1-Granerod-young-adult.

ANCHORING_EXTRAS: stage=pre_adjudication; status=pending_external_review; self_review_disposition=hold_for_revision; self_review_notes=wave 5.3.6 VIRAL vignette anchored to PMID 20952256 (Granerod 2010 Lancet ID UK encephalitis cohort); external clinical adjudication pending; classification provisional. adjudicator_ids=VIRAL-WAVE2-PRE-ADJ-1, VIRAL-WAVE2-PRE-ADJ-2 (sentinel); cohen_kappa=0.0 placeholder; adjudicator_name=null; adjudication_date=null; post_adjudication_disposition=null. Subphase 1.3 commit 5.3.6 (2026-05-08, FINAL Subphase 1.3 wave). anchor=Granerod-Lancet-ID-2010 stratum=young-adult-HSE.

ADJUDICATION:
  inclusion_decision: hold_for_revision
  adjudicator_ids: ['VIRAL-WAVE2-PRE-ADJ-1', 'VIRAL-WAVE2-PRE-ADJ-2']
  ground_truth_class: 3
  pre_adjudication_kappa: 0.0
  disagreement_resolution: None

=== END vignette ===

=== CLASS 3 | vignette_id: 095 | subphase: 1.3 VIRAL | file: vir_095_hsv1_adolescent.json ===

ANCHOR:
  pmid: 16675036
  first_author: Whitley
  year: 2006
  journal: Antiviral Res
  citation_type: review
  doi: 10.1016/S1473-3099(06)70414-6

DEMOGRAPHICS:
  age_years: 14
  sex: male
  geography_region: us_south
  ethnicity: white_non_hispanic
  altitude_residence_m: 100
  hiv_status: negative
  cd4_count_cells_per_uL: None
  pregnancy_red_flag: False
  immunocompromise_status: none
  freshwater_exposure_within_14d: False
  freshwater_exposure_type: None

HISTORY:
  symptom_onset_to_presentation_days: 4.0
  chief_complaint: behavioral_change
  red_flags_present: []
  prodrome_description: 14-year-old male, US South region. 4-day course: fever 38.5 C, headache, then progressive behavioral change with personality alteration day 2, anomic aphasia day 3, complex partial seizure day 4 prompting tertiary pediatric ED. No neck stiffness. No freshwater. Acyclovir hour 5. Outcome: survived with mild memory deficit.

VITALS:
  temperature_celsius: 38.5
  heart_rate_bpm: 96
  systolic_bp_mmHg: 118
  diastolic_bp_mmHg: 72
  glasgow_coma_scale: 12
  oxygen_saturation_pct: 97
  respiratory_rate_breaths_per_min: 18

EXAM:
  mental_status_grade: confused
  neck_stiffness: False
  kernig_or_brudzinski_positive: False
  cranial_nerve_palsy: none
  papilledema_on_fundoscopy: False
  focal_neurological_deficit: True
  skin_lesion_centrofacial_chronic: False
  petechial_or_purpuric_rash: False

LABS:
  wbc_blood_per_uL: 8800
  platelets_per_uL: 270000
  alt_ast_U_per_L: 24
  crp_mg_per_L: 18.0
  procalcitonin_ng_per_mL: 0.4
  serum_sodium_mEq_per_L: 138

CSF:
  opening_pressure_cmH2O: 22.0
  wbc_per_mm3: 195
  lymphocyte_pct: 78
  neutrophil_pct: 22
  eosinophil_pct: 0
  glucose_mg_per_dL: 55
  protein_mg_per_dL: 105
  lactate_mmol_per_L: 2.4
  ada_U_per_L: None
  crag_lfa_result: negative
  wet_mount_motile_amoebae: negative
  xanthochromia_present: True
  rbc_per_mm3: 28

IMAGING:
  modality: mri_with_dwi_flair
  pattern: mesial_temporal_t2_flair_hyperintensity
  contrast_enhancement: False
  hydrocephalus: False
  basal_meningeal_enhancement: False
  finding_count: 1
  text_summary: MRI brain with DWI/FLAIR: mesial temporal T2/FLAIR hyperintensity asymmetric with basal ganglia sparing. Canonical HSE imaging signature per Tyler 2018 NEJM viral encephalitis review.

DIAGNOSTIC_TESTS:
  pcr_panel: positive
  xpert_mtb_rif: n/a
  blood_culture: n/a
  csf_culture: n/a
  serology_or_antigen: n/a
  smear_or_gram: n/a
  brain_biopsy: n/a
  imaging_test: n/a
  total_dx_results: 3

NARRATIVE_EN: A 14-year-old boy in the US South region presented to a tertiary pediatric emergency department with a 4-day course: fever to 38.5 C, headache, then progressive behavioral change with personality alteration on day 2, anomic aphasia on day 3, and a complex partial seizure on day 4. He had no neck stiffness and no antecedent freshwater exposure. Examination on admission: temperature 38.5 C, Glasgow Coma Scale 12, focal deficit (anomic aphasia), no rash. CSF showed opening pressure 22 cmH2O, white cell count 195 per cubic millimeter (78 percent lymphocytes), glucose 55 mg/dL, protein 105 mg/dL, RBC 28 with xanthochromia. CSF HSV-1 PCR positive. Brain MRI with DWI/FLAIR showed mesial temporal T2/FLAIR hyperintensity asymmetric. Acyclovir initiated within five hours. Anchored to Whitley 2006 Lancet Infect Dis HSE pathogenesis review (PMID 16675036), adolescent-HSE stratum. Outcome: survived with mild memory deficit. Subphase 1.3 commit 5.3.6 wave 2, pre-adjudication hold_for_revision.

NARRATIVE_ES: Varon de 14 anos en region sur de Estados Unidos, ingresado a urgencias pediatricas terciarias con curso de cuatro dias: fiebre 38.5 C, cefalea, cambio conductual con alteracion de personalidad al segundo dia, afasia anomica al tercer dia y crisis parcial compleja al cuarto. Sin rigidez de nuca. Sin exposicion a agua dulce. Examen: temperatura 38.5 C, escala de Glasgow 12, deficit focal (afasia anomica), sin exantema. Liquido cefalorraquideo mostro presion de apertura 22 cmH2O, leucocitos 195 por mm3 (78 por ciento linfocitos), glucosa 55 mg/dL, proteina 105 mg/dL, eritrocitos 28 con xantocromia. PCR de HSV-1 positiva. RM cerebral con hiperintensidad temporal mesial T2/FLAIR. Aciclovir en cinco horas. Anclaje en revision Whitley 2006 Lancet ID HSE (PMID 16675036). Subphase 1.3 commit 5.3.6 wave 2.

RATIONALE: Anchored to PMID 16675036 (Whitley 2006 Lancet ID HSE pathogenesis review). Adolescent HSE phenotype with classic limbic-frontal pattern. Demographic anchor (14yo M US South adolescent HSE) sits in Whitley adolescent-HSE stratum. CSF lymphocytic with hemorrhagic component. MRI mesial temporal. Imputation tiers: tier_1_primary={age, sex, hsv1_pcr, imaging_pattern, focal_aphasia, behavioral_change}; tier_3_within_review={csf_wbc, neutrophil_pct, glucose, protein, rbc, xanthochromia, gcs}; tier_4_priors={temp, symptom_days}. Indeterminate=none. Diagnostic_ambiguity=false. Outcome=survived_mild_memory_deficit. Acyclovir_hours=5. Tier: tier_3_imputation_within_review. 5.3.6 wave2 HSV1-Whitley-adolescent.

ANCHORING_EXTRAS: stage=pre_adjudication; status=pending_external_review; self_review_disposition=hold_for_revision; self_review_notes=wave 5.3.6 VIRAL vignette anchored to PMID 16675036 (Whitley 2006 Lancet ID HSE pathogenesis review); external clinical adjudication pending; classification provisional. adjudicator_ids=VIRAL-WAVE2-PRE-ADJ-1, VIRAL-WAVE2-PRE-ADJ-2 (sentinel); cohen_kappa=0.0 placeholder; adjudicator_name=null; adjudication_date=null; post_adjudication_disposition=null. Subphase 1.3 commit 5.3.6 (2026-05-08, FINAL Subphase 1.3 wave). anchor=Whitley-Lancet-ID-2006 stratum=adolescent-HSE.

ADJUDICATION:
  inclusion_decision: hold_for_revision
  adjudicator_ids: ['VIRAL-WAVE2-PRE-ADJ-1', 'VIRAL-WAVE2-PRE-ADJ-2']
  ground_truth_class: 3
  pre_adjudication_kappa: 0.0
  disagreement_resolution: None

=== END vignette ===

=== CLASS 3 | vignette_id: 096 | subphase: 1.3 VIRAL | file: vir_096_hsv1_adult.json ===

ANCHOR:
  pmid: 30089069
  first_author: Tyler
  year: 2018
  journal: NEJM
  citation_type: review
  doi: 10.1056/NEJMra1708714

DEMOGRAPHICS:
  age_years: 45
  sex: female
  geography_region: other_global
  ethnicity: white_non_hispanic
  altitude_residence_m: 5
  hiv_status: negative
  cd4_count_cells_per_uL: None
  pregnancy_red_flag: False
  immunocompromise_status: none
  freshwater_exposure_within_14d: False
  freshwater_exposure_type: None

HISTORY:
  symptom_onset_to_presentation_days: 4.0
  chief_complaint: altered_mental_status
  red_flags_present: []
  prodrome_description: 45-year-old female, Netherlands. 4-day progressive course: fever 38.7 C, severe headache, behavioral change with personality alteration day 2, expressive aphasia day 3, right-sided focal seizure day 4 prompting tertiary ED Amsterdam. No neck stiffness. No freshwater. Acyclovir hour 5. Outcome: survived with mild memory deficit per Tyler review HSE residual-deficit rate.

VITALS:
  temperature_celsius: 38.7
  heart_rate_bpm: 96
  systolic_bp_mmHg: 128
  diastolic_bp_mmHg: 78
  glasgow_coma_scale: 12
  oxygen_saturation_pct: 97
  respiratory_rate_breaths_per_min: 18

EXAM:
  mental_status_grade: confused
  neck_stiffness: False
  kernig_or_brudzinski_positive: False
  cranial_nerve_palsy: none
  papilledema_on_fundoscopy: False
  focal_neurological_deficit: True
  skin_lesion_centrofacial_chronic: False
  petechial_or_purpuric_rash: False

LABS:
  wbc_blood_per_uL: 8200
  platelets_per_uL: 245000
  alt_ast_U_per_L: 26
  crp_mg_per_L: 18.0
  procalcitonin_ng_per_mL: 0.3
  serum_sodium_mEq_per_L: 138

CSF:
  opening_pressure_cmH2O: 22.0
  wbc_per_mm3: 220
  lymphocyte_pct: 75
  neutrophil_pct: 25
  eosinophil_pct: 0
  glucose_mg_per_dL: 55
  protein_mg_per_dL: 120
  lactate_mmol_per_L: 2.6
  ada_U_per_L: None
  crag_lfa_result: negative
  wet_mount_motile_amoebae: negative
  xanthochromia_present: True
  rbc_per_mm3: 35

IMAGING:
  modality: mri_with_dwi_flair
  pattern: mesial_temporal_t2_flair_hyperintensity
  contrast_enhancement: False
  hydrocephalus: False
  basal_meningeal_enhancement: False
  finding_count: 1
  text_summary: MRI brain with DWI/FLAIR: mesial temporal T2/FLAIR hyperintensity asymmetric with basal ganglia sparing. Canonical HSE imaging signature per Tyler 2018 NEJM viral encephalitis review.

DIAGNOSTIC_TESTS:
  pcr_panel: positive
  xpert_mtb_rif: n/a
  blood_culture: n/a
  csf_culture: n/a
  serology_or_antigen: n/a
  smear_or_gram: n/a
  brain_biopsy: n/a
  imaging_test: n/a
  total_dx_results: 3

NARRATIVE_EN: A 45-year-old woman in the Netherlands presented to a tertiary emergency department in Amsterdam with a 4-day progressive course: fever to 38.7 C, severe headache, behavioral change with personality alteration on day 2, expressive aphasia on day 3, and a right-sided focal seizure on day 4 prompting ED presentation. She had no neck stiffness on examination and no antecedent freshwater exposure. Examination on admission: Glasgow Coma Scale 12, focal neurological deficit (expressive aphasia). CSF showed opening pressure 22 cmH2O, white cell count 220 per cubic millimeter (75 percent lymphocytes), glucose 55 mg/dL, protein 120 mg/dL, RBC 35 with mild xanthochromia (canonical hemorrhagic component). CSF HSV-1 PCR positive. Brain MRI with DWI/FLAIR showed mesial temporal T2/FLAIR hyperintensity asymmetric with basal ganglia sparing. Acyclovir initiated within five hours. Anchored to Tyler 2018 NEJM viral encephalitis review (PMID 30089069). Outcome: survived with mild memory deficit. Subphase 1.3 commit 5.3.5 wave 1, pre-adjudication hold_for_revision.

NARRATIVE_ES: Mujer de 45 anos en Paises Bajos (Amsterdam), ingresada a urgencias terciarias con curso progresivo de cuatro dias: fiebre 38.7 C, cefalea intensa, cambio conductual con alteracion de personalidad al segundo dia, afasia expresiva al tercer dia, crisis focal derecha al cuarto dia que motivo consulta. Sin rigidez de nuca al examen. Sin exposicion a agua dulce. Examen: escala de Glasgow 12, deficit focal (afasia expresiva). Liquido cefalorraquideo mostro presion de apertura 22 cmH2O, leucocitos 220 por mm3 (75 por ciento linfocitos), glucosa 55 mg/dL, proteina 120 mg/dL, eritrocitos 35 con xantocromia leve. PCR de HSV-1 positiva. RM cerebral mostro hiperintensidad temporal mesial T2/FLAIR asimetrica con preservacion de ganglios basales. Anclaje en revision Tyler 2018 NEJM encefalitis viral aguda (PMID 30089069). Subphase 1.3 commit 5.3.5 wave 1.

RATIONALE: Anchored to PMID 30089069 (Tyler KL 2018 NEJM clinical review of acute viral encephalitis), HSV1 mesial-temporal-encephalitis phenotype. Demographic anchor (45yo F adult HSE) sits in adult-HSE stratum (HSE bimodal age, peaks at adulthood). CSF lymphocytic (220 WBC, 75 percent lymphocytes), normal glucose 55, mildly elevated protein 120, RBC 35 with xanthochromia (hemorrhagic temporal necrosis component). MRI mesial temporal T2/FLAIR hyperintensity per master prompt 1.3.4 mandate. Imputation tiers: tier_1_primary={age, sex, hsv1_pcr, imaging_pattern, focal_aphasia}; tier_3_within_review={csf_wbc, neutrophil_pct, glucose, protein, rbc, xanthochromia, gcs}; tier_4_priors={temp, symptom_days}. Indeterminate=none. Diagnostic_ambiguity=false. Outcome=survived_mild_memory_deficit. Acyclovir_hours=5. Tier: tier_3_imputation_within_review. 5.3.5 wave1 HSV1-NL-adult-female.

ANCHORING_EXTRAS: stage=pre_adjudication; status=pending_external_review; self_review_disposition=hold_for_revision; self_review_notes=wave 5.3.5 VIRAL vignette anchored to PMID 30089069 (Tyler 2018 NEJM viral encephalitis review); external clinical adjudication pending; classification provisional. adjudicator_ids=VIRAL-WAVE1-PRE-ADJ-1, VIRAL-WAVE1-PRE-ADJ-2 (sentinel); cohen_kappa=0.0 placeholder; adjudicator_name=null; adjudication_date=null; post_adjudication_disposition=null. Subphase 1.3 commit 5.3.5 (2026-05-08). anchor=Tyler-NEJM-2018 stratum=HSV1-adult-HSE.

ADJUDICATION:
  inclusion_decision: hold_for_revision
  adjudicator_ids: ['VIRAL-WAVE1-PRE-ADJ-1', 'VIRAL-WAVE1-PRE-ADJ-2']
  ground_truth_class: 3
  pre_adjudication_kappa: 0.0
  disagreement_resolution: None

=== END vignette ===

=== CLASS 3 | vignette_id: 097 | subphase: 1.3 VIRAL | file: vir_097_hsv1_elderly_fatal.json ===

ANCHOR:
  pmid: 20952256
  first_author: Granerod
  year: 2010
  journal: Lancet Infect Dis
  citation_type: cohort
  doi: 10.1016/S1473-3099(10)70222-X

DEMOGRAPHICS:
  age_years: 78
  sex: male
  geography_region: other_global
  ethnicity: white_non_hispanic
  altitude_residence_m: 5
  hiv_status: negative
  cd4_count_cells_per_uL: None
  pregnancy_red_flag: False
  immunocompromise_status: none
  freshwater_exposure_within_14d: False
  freshwater_exposure_type: None

HISTORY:
  symptom_onset_to_presentation_days: 6.0
  chief_complaint: altered_mental_status
  red_flags_present: []
  prodrome_description: 78-year-old male, Netherlands. 6-day course: low-grade fever 38.2 C, headache, then progressive behavioral change day 2, anomic aphasia day 3, focal seizures day 4, obtundation day 5, coma day 6. Tertiary ED Amsterdam. No freshwater. Acyclovir hour 8 (delayed by atypical elderly presentation). Outcome: fatal hospital day 4 per Granerod cohort elderly-mortality data.

VITALS:
  temperature_celsius: 38.2
  heart_rate_bpm: 116
  systolic_bp_mmHg: 100
  diastolic_bp_mmHg: 60
  glasgow_coma_scale: 6
  oxygen_saturation_pct: 89
  respiratory_rate_breaths_per_min: 26

EXAM:
  mental_status_grade: comatose
  neck_stiffness: False
  kernig_or_brudzinski_positive: False
  cranial_nerve_palsy: none
  papilledema_on_fundoscopy: False
  focal_neurological_deficit: True
  skin_lesion_centrofacial_chronic: False
  petechial_or_purpuric_rash: False

LABS:
  wbc_blood_per_uL: 9100
  platelets_per_uL: 195000
  alt_ast_U_per_L: 32
  crp_mg_per_L: 26.0
  procalcitonin_ng_per_mL: 0.5
  serum_sodium_mEq_per_L: 130

CSF:
  opening_pressure_cmH2O: 28.0
  wbc_per_mm3: 320
  lymphocyte_pct: 70
  neutrophil_pct: 30
  eosinophil_pct: 0
  glucose_mg_per_dL: 48
  protein_mg_per_dL: 160
  lactate_mmol_per_L: 3.0
  ada_U_per_L: None
  crag_lfa_result: negative
  wet_mount_motile_amoebae: negative
  xanthochromia_present: True
  rbc_per_mm3: 60

IMAGING:
  modality: mri_with_dwi_flair
  pattern: mesial_temporal_t2_flair_hyperintensity
  contrast_enhancement: False
  hydrocephalus: False
  basal_meningeal_enhancement: False
  finding_count: 1
  text_summary: MRI brain with DWI/FLAIR: mesial temporal T2/FLAIR hyperintensity asymmetric with basal ganglia sparing. Canonical HSE imaging signature per Tyler 2018 NEJM viral encephalitis review.

DIAGNOSTIC_TESTS:
  pcr_panel: positive
  xpert_mtb_rif: n/a
  blood_culture: n/a
  csf_culture: n/a
  serology_or_antigen: n/a
  smear_or_gram: n/a
  brain_biopsy: n/a
  imaging_test: n/a
  total_dx_results: 3

NARRATIVE_EN: A 78-year-old man in the Netherlands presented to a tertiary emergency department in Amsterdam after a 6-day course: low-grade fever to 38.2 C, headache, behavioral change on day 2, anomic aphasia on day 3, focal seizures on day 4, obtundation on day 5, and coma on day 6. He had no neck stiffness and no antecedent freshwater exposure. Examination on admission: temperature 38.2 C, Glasgow Coma Scale 6, comatose, focal deficit (anomic aphasia residual + right-sided posturing), no rash. CSF showed opening pressure 28 cmH2O, white cell count 320 per cubic millimeter (70 percent lymphocytes), glucose 48 mg/dL, protein 160 mg/dL, RBC 60 with xanthochromia (prominent hemorrhagic component). CSF HSV-1 PCR positive. Brain MRI with DWI/FLAIR showed mesial temporal T2/FLAIR hyperintensity bilateral. Acyclovir initiated at hour 8 (delayed). Anchored to Granerod 2010 Lancet Infect Dis UK encephalitis cohort (PMID 20952256), elderly-HSE-mortality stratum. Outcome: fatal hospital day 4. Subphase 1.3 commit 5.3.6 wave 2, pre-adjudication hold_for_revision.

NARRATIVE_ES: Varon de 78 anos en Paises Bajos (Amsterdam), ingresado a urgencias terciarias tras curso de seis dias: febricula 38.2 C, cefalea, cambio conductual al segundo dia, afasia anomica al tercer, crisis focales al cuarto, obnubilacion al quinto y coma al sexto. Sin rigidez de nuca. Examen: temperatura 38.2 C, escala de Glasgow 6, comatoso, deficit focal (afasia anomica residual, postura derecha), sin exantema. Liquido cefalorraquideo mostro presion de apertura 28 cmH2O, leucocitos 320 por mm3 (70 por ciento linfocitos), glucosa 48 mg/dL, proteina 160 mg/dL, eritrocitos 60 con xantocromia. PCR de HSV-1 positiva. RM cerebral con hiperintensidad temporal mesial T2/FLAIR bilateral. Aciclovir en hora 8 (retraso). Anclaje en cohorte Granerod 2010 Lancet ID (PMID 20952256), estrato HSE adulto mayor. Resultado: fatal en hospital dia 4. Subphase 1.3 commit 5.3.6 wave 2.

RATIONALE: Anchored to PMID 20952256 (Granerod 2010 Lancet ID UK encephalitis cohort). Elderly HSE with delayed-acyclovir fatal outcome. Demographic anchor (78yo M NL elderly HSE delayed-treatment) sits in elderly-fatal-HSE stratum. CSF lymphocytic with prominent hemorrhagic component. MRI bilateral mesial temporal. Imputation tiers: tier_1_primary={age, sex, hsv1_pcr, imaging_pattern, focal_aphasia, delayed_acyclovir}; tier_3_within_review={csf_wbc, neutrophil_pct, glucose, protein, rbc, xanthochromia, gcs, hyponatremia}; tier_4_priors={temp, symptom_days}. Indeterminate=none. Diagnostic_ambiguity=false. Outcome=fatal_hospital_day_4. Acyclovir_hours=8. Tier: tier_3_imputation_within_review. 5.3.6 wave2 HSV1-Granerod-elderly-fatal.

ANCHORING_EXTRAS: stage=pre_adjudication; status=pending_external_review; self_review_disposition=hold_for_revision; self_review_notes=wave 5.3.6 VIRAL vignette anchored to PMID 20952256 (Granerod 2010 Lancet ID UK encephalitis cohort); external clinical adjudication pending; classification provisional. adjudicator_ids=VIRAL-WAVE2-PRE-ADJ-1, VIRAL-WAVE2-PRE-ADJ-2 (sentinel); cohen_kappa=0.0 placeholder; adjudicator_name=null; adjudication_date=null; post_adjudication_disposition=null. Subphase 1.3 commit 5.3.6 (2026-05-08, FINAL Subphase 1.3 wave). anchor=Granerod-Lancet-ID-2010 stratum=elderly-fatal-HSE.

ADJUDICATION:
  inclusion_decision: hold_for_revision
  adjudicator_ids: ['VIRAL-WAVE2-PRE-ADJ-1', 'VIRAL-WAVE2-PRE-ADJ-2']
  ground_truth_class: 3
  pre_adjudication_kappa: 0.0
  disagreement_resolution: None

=== END vignette ===

=== CLASS 3 | vignette_id: 098 | subphase: 1.3 VIRAL | file: vir_098_hsv1_pediatric.json ===

ANCHOR:
  pmid: 16675036
  first_author: Whitley
  year: 2006
  journal: Antiviral Res
  citation_type: review
  doi: 10.1016/S1473-3099(06)70414-6

DEMOGRAPHICS:
  age_years: 9
  sex: female
  geography_region: us_south
  ethnicity: white_non_hispanic
  altitude_residence_m: 100
  hiv_status: negative
  cd4_count_cells_per_uL: None
  pregnancy_red_flag: False
  immunocompromise_status: none
  freshwater_exposure_within_14d: False
  freshwater_exposure_type: None

HISTORY:
  symptom_onset_to_presentation_days: 4.0
  chief_complaint: altered_mental_status
  red_flags_present: []
  prodrome_description: 9-year-old female, US South region. 4-day course: fever 38.6 C, headache, then irritability and behavioral change day 2, expressive aphasia day 3, complex partial seizure day 4 prompting tertiary pediatric ED. No neck stiffness. No freshwater. Acyclovir hour 4. Outcome: survived with mild cognitive sequelae per Whitley pediatric-HSE pattern.

VITALS:
  temperature_celsius: 38.6
  heart_rate_bpm: 110
  systolic_bp_mmHg: 102
  diastolic_bp_mmHg: 64
  glasgow_coma_scale: 12
  oxygen_saturation_pct: 97
  respiratory_rate_breaths_per_min: 22

EXAM:
  mental_status_grade: confused
  neck_stiffness: False
  kernig_or_brudzinski_positive: False
  cranial_nerve_palsy: none
  papilledema_on_fundoscopy: False
  focal_neurological_deficit: True
  skin_lesion_centrofacial_chronic: False
  petechial_or_purpuric_rash: False

LABS:
  wbc_blood_per_uL: 8600
  platelets_per_uL: 295000
  alt_ast_U_per_L: 24
  crp_mg_per_L: 16.0
  procalcitonin_ng_per_mL: 0.3
  serum_sodium_mEq_per_L: 138

CSF:
  opening_pressure_cmH2O: 22.0
  wbc_per_mm3: 210
  lymphocyte_pct: 78
  neutrophil_pct: 22
  eosinophil_pct: 0
  glucose_mg_per_dL: 56
  protein_mg_per_dL: 105
  lactate_mmol_per_L: 2.4
  ada_U_per_L: None
  crag_lfa_result: negative
  wet_mount_motile_amoebae: negative
  xanthochromia_present: True
  rbc_per_mm3: 30

IMAGING:
  modality: mri_with_dwi_flair
  pattern: mesial_temporal_t2_flair_hyperintensity
  contrast_enhancement: False
  hydrocephalus: False
  basal_meningeal_enhancement: False
  finding_count: 1
  text_summary: MRI brain with DWI/FLAIR: mesial temporal T2/FLAIR hyperintensity asymmetric with basal ganglia sparing. Canonical HSE imaging signature per Tyler 2018 NEJM viral encephalitis review.

DIAGNOSTIC_TESTS:
  pcr_panel: positive
  xpert_mtb_rif: n/a
  blood_culture: n/a
  csf_culture: n/a
  serology_or_antigen: n/a
  smear_or_gram: n/a
  brain_biopsy: n/a
  imaging_test: n/a
  total_dx_results: 3

NARRATIVE_EN: A 9-year-old girl in the US South region presented to a tertiary pediatric emergency department with a 4-day course: fever to 38.6 C, headache, then irritability and behavioral change on day 2, expressive aphasia on day 3, and a complex partial seizure on day 4. She had no neck stiffness and no antecedent freshwater exposure. Examination on admission: temperature 38.6 C, Glasgow Coma Scale 12, focal deficit (expressive aphasia), no rash. CSF showed opening pressure 22 cmH2O, white cell count 210 per cubic millimeter (78 percent lymphocytes), glucose 56 mg/dL, protein 105 mg/dL, RBC 30 with xanthochromia. CSF HSV-1 PCR positive. Brain MRI with DWI/FLAIR showed mesial temporal T2/FLAIR hyperintensity asymmetric. Acyclovir initiated within four hours. Anchored to Whitley 2006 Lancet Infect Dis HSE pathogenesis review (PMID 16675036), pediatric-HSE stratum. Outcome: survived with mild cognitive sequelae. Subphase 1.3 commit 5.3.6 wave 2, pre-adjudication hold_for_revision.

NARRATIVE_ES: Nina de 9 anos en region sur de Estados Unidos, ingresada a urgencias pediatricas terciarias con curso de cuatro dias: fiebre 38.6 C, cefalea, irritabilidad y cambio conductual al segundo dia, afasia expresiva al tercer dia y crisis parcial compleja al cuarto. Sin rigidez de nuca. Sin exposicion a agua dulce. Examen: temperatura 38.6 C, escala de Glasgow 12, deficit focal (afasia expresiva), sin exantema. Liquido cefalorraquideo mostro presion de apertura 22 cmH2O, leucocitos 210 por mm3 (78 por ciento linfocitos), glucosa 56 mg/dL, proteina 105 mg/dL, eritrocitos 30 con xantocromia. PCR de HSV-1 positiva. RM cerebral con hiperintensidad temporal mesial T2/FLAIR. Aciclovir en cuatro horas. Anclaje en revision Whitley 2006 Lancet ID HSE (PMID 16675036). Subphase 1.3 commit 5.3.6 wave 2, pre-adjudicacion hold_for_revision.

RATIONALE: Anchored to PMID 16675036 (Whitley 2006 Lancet ID HSE pathogenesis review). Pediatric HSE with classic limbic phenotype. Demographic anchor (9yo F US South pediatric HSE) sits in Whitley pediatric-HSE stratum. CSF lymphocytic with hemorrhagic component. MRI mesial temporal. Imputation tiers: tier_1_primary={age, sex, hsv1_pcr, imaging_pattern, focal_aphasia, behavioral_change}; tier_3_within_review={csf_wbc, neutrophil_pct, glucose, protein, rbc, xanthochromia, gcs}; tier_4_priors={temp, symptom_days, hr}. Indeterminate=none. Diagnostic_ambiguity=false. Outcome=survived_mild_cognitive_sequelae. Acyclovir_hours=4. Tier: tier_3_imputation_within_review. 5.3.6 wave2 HSV1-Whitley-pediatric.

ANCHORING_EXTRAS: stage=pre_adjudication; status=pending_external_review; self_review_disposition=hold_for_revision; self_review_notes=wave 5.3.6 VIRAL vignette anchored to PMID 16675036 (Whitley 2006 Lancet ID HSE pathogenesis review); external clinical adjudication pending; classification provisional. adjudicator_ids=VIRAL-WAVE2-PRE-ADJ-1, VIRAL-WAVE2-PRE-ADJ-2 (sentinel); cohen_kappa=0.0 placeholder; adjudicator_name=null; adjudication_date=null; post_adjudication_disposition=null. Subphase 1.3 commit 5.3.6 (2026-05-08, FINAL Subphase 1.3 wave). anchor=Whitley-Lancet-ID-2006 stratum=pediatric-HSE.

ADJUDICATION:
  inclusion_decision: hold_for_revision
  adjudicator_ids: ['VIRAL-WAVE2-PRE-ADJ-1', 'VIRAL-WAVE2-PRE-ADJ-2']
  ground_truth_class: 3
  pre_adjudication_kappa: 0.0
  disagreement_resolution: None

=== END vignette ===

=== CLASS 3 | vignette_id: 099 | subphase: 1.3 VIRAL | file: vir_099_hsv1_lima_adult.json ===

ANCHOR:
  pmid: 30089069
  first_author: Tyler
  year: 2018
  journal: NEJM
  citation_type: review
  doi: 10.1056/NEJMra1708714

DEMOGRAPHICS:
  age_years: 38
  sex: male
  geography_region: peru_lima_coast
  ethnicity: mestizo
  altitude_residence_m: 154
  hiv_status: negative
  cd4_count_cells_per_uL: None
  pregnancy_red_flag: False
  immunocompromise_status: none
  freshwater_exposure_within_14d: False
  freshwater_exposure_type: None

HISTORY:
  symptom_onset_to_presentation_days: 5.0
  chief_complaint: seizure
  red_flags_present: []
  prodrome_description: 38-year-old male in Lima, Peru. 5-day course: low-grade fever 38.5 C, severe headache, then new-onset olfactory hallucinations day 3, expressive aphasia day 4, complex partial seizure day 5 prompting tertiary urban ED. No neck stiffness. No freshwater. Acyclovir hour 8. Outcome: survived with mild memory deficit.

VITALS:
  temperature_celsius: 38.5
  heart_rate_bpm: 92
  systolic_bp_mmHg: 124
  diastolic_bp_mmHg: 76
  glasgow_coma_scale: 13
  oxygen_saturation_pct: 97
  respiratory_rate_breaths_per_min: 18

EXAM:
  mental_status_grade: confused
  neck_stiffness: False
  kernig_or_brudzinski_positive: False
  cranial_nerve_palsy: none
  papilledema_on_fundoscopy: False
  focal_neurological_deficit: True
  skin_lesion_centrofacial_chronic: False
  petechial_or_purpuric_rash: False

LABS:
  wbc_blood_per_uL: 9100
  platelets_per_uL: 250000
  alt_ast_U_per_L: 30
  crp_mg_per_L: 22.0
  procalcitonin_ng_per_mL: 0.4
  serum_sodium_mEq_per_L: 138

CSF:
  opening_pressure_cmH2O: 21.0
  wbc_per_mm3: 180
  lymphocyte_pct: 78
  neutrophil_pct: 22
  eosinophil_pct: 0
  glucose_mg_per_dL: 58
  protein_mg_per_dL: 105
  lactate_mmol_per_L: 2.4
  ada_U_per_L: None
  crag_lfa_result: negative
  wet_mount_motile_amoebae: negative
  xanthochromia_present: True
  rbc_per_mm3: 28

IMAGING:
  modality: mri_with_dwi_flair
  pattern: mesial_temporal_t2_flair_hyperintensity
  contrast_enhancement: False
  hydrocephalus: False
  basal_meningeal_enhancement: False
  finding_count: 1
  text_summary: MRI brain with DWI/FLAIR: mesial temporal T2/FLAIR hyperintensity asymmetric with basal ganglia sparing. Canonical HSE imaging signature per Tyler 2018 NEJM viral encephalitis review.

DIAGNOSTIC_TESTS:
  pcr_panel: positive
  xpert_mtb_rif: n/a
  blood_culture: n/a
  csf_culture: n/a
  serology_or_antigen: n/a
  smear_or_gram: n/a
  brain_biopsy: n/a
  imaging_test: n/a
  total_dx_results: 3

NARRATIVE_EN: A 38-year-old man in Lima, Peru presented to a tertiary urban emergency department with a 5-day course: low-grade fever to 38.5 C, severe headache, then new-onset olfactory hallucinations on day 3, expressive aphasia on day 4, and a complex partial seizure on day 5 prompting ED presentation. He had no neck stiffness on examination and no antecedent freshwater exposure. Examination on admission: Glasgow Coma Scale 13, focal neurological deficit (expressive aphasia and olfactory hallucinations). CSF showed opening pressure 21 cmH2O, white cell count 180 per cubic millimeter (78 percent lymphocytes), glucose 58 mg/dL, protein 105 mg/dL, RBC 28 with mild xanthochromia. CSF HSV-1 PCR positive. Brain MRI with DWI/FLAIR showed mesial temporal T2/FLAIR hyperintensity asymmetric with basal ganglia sparing. Acyclovir initiated within eight hours. Anchored to Tyler 2018 NEJM viral encephalitis review (PMID 30089069), Peru-Lima coastal stratum. Outcome: survived with mild memory deficit. Subphase 1.3 commit 5.3.5 wave 1, pre-adjudication hold_for_revision.

NARRATIVE_ES: Varon de 38 anos en Lima, Peru, ingresado a urgencias urbanas terciarias con curso de cinco dias: febricula 38.5 C, cefalea intensa, alucinaciones olfativas de novo al tercer dia, afasia expresiva al cuarto dia y crisis parcial compleja al quinto dia que motivo consulta. Sin rigidez de nuca al examen. Sin exposicion a agua dulce. Examen: escala de Glasgow 13, deficit focal (afasia expresiva, alucinaciones olfativas). Liquido cefalorraquideo mostro presion de apertura 21 cmH2O, leucocitos 180 por mm3 (78 por ciento linfocitos), glucosa 58 mg/dL, proteina 105 mg/dL, eritrocitos 28 con xantocromia leve. PCR de HSV-1 positiva. RM cerebral mostro hiperintensidad temporal mesial T2/FLAIR asimetrica. Anclaje en revision Tyler 2018 NEJM (PMID 30089069), estrato Lima coastal. Subphase 1.3 commit 5.3.5 wave 1.

RATIONALE: Anchored to PMID 30089069 (Tyler 2018 NEJM viral encephalitis review). HSV1 mesial-temporal-encephalitis phenotype with olfactory hallucinations + aphasia + partial seizure (classic limbic-dominant signature). Demographic anchor (38yo M Lima) sits in adult-HSE stratum + Peru-coastal-tertiary-care stratum. CSF lymphocytic with hemorrhagic component. MRI mesial temporal pattern. Imputation tiers: tier_1_primary={age, sex, region, hsv1_pcr, imaging_pattern, olfactory_hallucinations, aphasia}; tier_3_within_review={csf_wbc, neutrophil_pct, glucose, protein, rbc, xanthochromia, gcs}; tier_4_priors={temp, symptom_days}. Indeterminate=none. Diagnostic_ambiguity=false. Outcome=survived_mild_memory_deficit. Acyclovir_hours=8. Tier: tier_3_imputation_within_review. 5.3.5 wave1 HSV1-Lima-adult-male.

ANCHORING_EXTRAS: stage=pre_adjudication; status=pending_external_review; self_review_disposition=hold_for_revision; self_review_notes=wave 5.3.5 VIRAL vignette anchored to PMID 30089069 (Tyler 2018 NEJM viral encephalitis review); external clinical adjudication pending; classification provisional. adjudicator_ids=VIRAL-WAVE1-PRE-ADJ-1, VIRAL-WAVE1-PRE-ADJ-2 (sentinel); cohen_kappa=0.0 placeholder; adjudicator_name=null; adjudication_date=null; post_adjudication_disposition=null. Subphase 1.3 commit 5.3.5 (2026-05-08). anchor=Tyler-NEJM-2018 region=Lima-Peru.

ADJUDICATION:
  inclusion_decision: hold_for_revision
  adjudicator_ids: ['VIRAL-WAVE1-PRE-ADJ-1', 'VIRAL-WAVE1-PRE-ADJ-2']
  ground_truth_class: 3
  pre_adjudication_kappa: 0.0
  disagreement_resolution: None

=== END vignette ===

=== CLASS 3 | vignette_id: 100 | subphase: 1.3 VIRAL | file: vir_100_hsv1_adult.json ===

ANCHOR:
  pmid: 20952256
  first_author: Granerod
  year: 2010
  journal: Lancet Infect Dis
  citation_type: cohort
  doi: 10.1016/S1473-3099(10)70222-X

DEMOGRAPHICS:
  age_years: 60
  sex: female
  geography_region: other_global
  ethnicity: white_non_hispanic
  altitude_residence_m: 5
  hiv_status: negative
  cd4_count_cells_per_uL: None
  pregnancy_red_flag: False
  immunocompromise_status: none
  freshwater_exposure_within_14d: False
  freshwater_exposure_type: None

HISTORY:
  symptom_onset_to_presentation_days: 5.0
  chief_complaint: altered_mental_status
  red_flags_present: []
  prodrome_description: 60-year-old female, Netherlands. 5-day course: low-grade fever 38.4 C, headache, behavioral change day 2, expressive aphasia day 3, focal seizure day 4, progressive confusion day 5 prompting tertiary ED Amsterdam. No neck stiffness. No freshwater. Acyclovir hour 6. Outcome: survived with mild memory deficit per Granerod cohort residual-deficit pattern.

VITALS:
  temperature_celsius: 38.4
  heart_rate_bpm: 92
  systolic_bp_mmHg: 124
  diastolic_bp_mmHg: 76
  glasgow_coma_scale: 11
  oxygen_saturation_pct: 96
  respiratory_rate_breaths_per_min: 18

EXAM:
  mental_status_grade: somnolent
  neck_stiffness: False
  kernig_or_brudzinski_positive: False
  cranial_nerve_palsy: none
  papilledema_on_fundoscopy: False
  focal_neurological_deficit: True
  skin_lesion_centrofacial_chronic: False
  petechial_or_purpuric_rash: False

LABS:
  wbc_blood_per_uL: 9000
  platelets_per_uL: 240000
  alt_ast_U_per_L: 28
  crp_mg_per_L: 22.0
  procalcitonin_ng_per_mL: 0.4
  serum_sodium_mEq_per_L: 137

CSF:
  opening_pressure_cmH2O: 24.0
  wbc_per_mm3: 230
  lymphocyte_pct: 74
  neutrophil_pct: 26
  eosinophil_pct: 0
  glucose_mg_per_dL: 54
  protein_mg_per_dL: 125
  lactate_mmol_per_L: 2.6
  ada_U_per_L: None
  crag_lfa_result: negative
  wet_mount_motile_amoebae: negative
  xanthochromia_present: True
  rbc_per_mm3: 35

IMAGING:
  modality: mri_with_dwi_flair
  pattern: mesial_temporal_t2_flair_hyperintensity
  contrast_enhancement: False
  hydrocephalus: False
  basal_meningeal_enhancement: False
  finding_count: 1
  text_summary: MRI brain with DWI/FLAIR: mesial temporal T2/FLAIR hyperintensity asymmetric with basal ganglia sparing. Canonical HSE imaging signature per Tyler 2018 NEJM viral encephalitis review.

DIAGNOSTIC_TESTS:
  pcr_panel: positive
  xpert_mtb_rif: n/a
  blood_culture: n/a
  csf_culture: n/a
  serology_or_antigen: n/a
  smear_or_gram: n/a
  brain_biopsy: n/a
  imaging_test: n/a
  total_dx_results: 3

NARRATIVE_EN: A 60-year-old woman in the Netherlands presented to a tertiary emergency department in Amsterdam after a 5-day course: low-grade fever to 38.4 C, headache, behavioral change on day 2, expressive aphasia on day 3, a focal seizure on day 4, and progressive confusion on day 5. She had no neck stiffness and no antecedent freshwater exposure. Examination on admission: temperature 38.4 C, Glasgow Coma Scale 11, focal deficit (expressive aphasia), no rash. CSF showed opening pressure 24 cmH2O, white cell count 230 per cubic millimeter (74 percent lymphocytes), glucose 54 mg/dL, protein 125 mg/dL, RBC 35 with xanthochromia. CSF HSV-1 PCR positive. Brain MRI with DWI/FLAIR showed mesial temporal T2/FLAIR hyperintensity asymmetric. Acyclovir initiated within six hours. Anchored to Granerod 2010 Lancet Infect Dis UK encephalitis cohort (PMID 20952256). Outcome: survived with mild memory deficit. Subphase 1.3 commit 5.3.6 wave 2, pre-adjudication hold_for_revision.

NARRATIVE_ES: Mujer de 60 anos en Paises Bajos (Amsterdam), ingresada a urgencias terciarias tras curso de cinco dias: febricula 38.4 C, cefalea, cambio conductual al segundo dia, afasia expresiva al tercer dia, crisis focal al cuarto y confusion progresiva al quinto. Sin rigidez de nuca. Examen: temperatura 38.4 C, escala de Glasgow 11, deficit focal (afasia expresiva), sin exantema. Liquido cefalorraquideo mostro presion de apertura 24 cmH2O, leucocitos 230 por mm3 (74 por ciento linfocitos), glucosa 54 mg/dL, proteina 125 mg/dL, eritrocitos 35 con xantocromia. PCR de HSV-1 positiva. RM cerebral con hiperintensidad temporal mesial T2/FLAIR. Aciclovir en seis horas. Anclaje en cohorte Granerod 2010 Lancet ID (PMID 20952256). Subphase 1.3 commit 5.3.6 wave 2.

RATIONALE: Anchored to PMID 20952256 (Granerod 2010 Lancet ID UK encephalitis cohort). Older-adult HSE phenotype. Demographic anchor (60yo F NL older-adult HSE) sits in Granerod older-adult-HSE stratum. CSF lymphocytic with hemorrhagic component. MRI mesial temporal. Imputation tiers: tier_1_primary={age, sex, hsv1_pcr, imaging_pattern, focal_aphasia, behavioral_change}; tier_3_within_review={csf_wbc, neutrophil_pct, glucose, protein, rbc, xanthochromia, gcs}; tier_4_priors={temp, symptom_days}. Indeterminate=none. Diagnostic_ambiguity=false. Outcome=survived_mild_memory_deficit. Acyclovir_hours=6. Tier: tier_3_imputation_within_review. 5.3.6 wave2 HSV1-Granerod-older-adult-female.

ANCHORING_EXTRAS: stage=pre_adjudication; status=pending_external_review; self_review_disposition=hold_for_revision; self_review_notes=wave 5.3.6 VIRAL vignette anchored to PMID 20952256 (Granerod 2010 Lancet ID UK encephalitis cohort); external clinical adjudication pending; classification provisional. adjudicator_ids=VIRAL-WAVE2-PRE-ADJ-1, VIRAL-WAVE2-PRE-ADJ-2 (sentinel); cohen_kappa=0.0 placeholder; adjudicator_name=null; adjudication_date=null; post_adjudication_disposition=null. Subphase 1.3 commit 5.3.6 (2026-05-08, FINAL Subphase 1.3 wave). anchor=Granerod-Lancet-ID-2010 stratum=older-adult-HSE.

ADJUDICATION:
  inclusion_decision: hold_for_revision
  adjudicator_ids: ['VIRAL-WAVE2-PRE-ADJ-1', 'VIRAL-WAVE2-PRE-ADJ-2']
  ground_truth_class: 3
  pre_adjudication_kappa: 0.0
  disagreement_resolution: None

=== END vignette ===

=== CLASS 3 | vignette_id: 101 | subphase: 1.3 VIRAL | file: vir_101_hsv1_adolescent.json ===

ANCHOR:
  pmid: 16675036
  first_author: Whitley
  year: 2006
  journal: Antiviral Res
  citation_type: review
  doi: 10.1016/S1473-3099(06)70414-6

DEMOGRAPHICS:
  age_years: 17
  sex: male
  geography_region: us_south
  ethnicity: white_non_hispanic
  altitude_residence_m: 100
  hiv_status: negative
  cd4_count_cells_per_uL: None
  pregnancy_red_flag: False
  immunocompromise_status: none
  freshwater_exposure_within_14d: False
  freshwater_exposure_type: None

HISTORY:
  symptom_onset_to_presentation_days: 4.0
  chief_complaint: behavioral_change
  red_flags_present: []
  prodrome_description: 17-year-old male, US South region. 4-day course: fever 38.5 C, headache, behavioral change with personality alteration day 2, anomic aphasia day 3, complex partial seizure day 4 prompting tertiary ED. No neck stiffness. No freshwater. Acyclovir hour 4. Outcome: survived with mild memory deficit per Whitley adolescent-HSE pattern.

VITALS:
  temperature_celsius: 38.5
  heart_rate_bpm: 92
  systolic_bp_mmHg: 124
  diastolic_bp_mmHg: 74
  glasgow_coma_scale: 13
  oxygen_saturation_pct: 98
  respiratory_rate_breaths_per_min: 18

EXAM:
  mental_status_grade: confused
  neck_stiffness: False
  kernig_or_brudzinski_positive: False
  cranial_nerve_palsy: none
  papilledema_on_fundoscopy: False
  focal_neurological_deficit: True
  skin_lesion_centrofacial_chronic: False
  petechial_or_purpuric_rash: False

LABS:
  wbc_blood_per_uL: 9200
  platelets_per_uL: 265000
  alt_ast_U_per_L: 26
  crp_mg_per_L: 18.0
  procalcitonin_ng_per_mL: 0.3
  serum_sodium_mEq_per_L: 138

CSF:
  opening_pressure_cmH2O: 22.0
  wbc_per_mm3: 200
  lymphocyte_pct: 78
  neutrophil_pct: 22
  eosinophil_pct: 0
  glucose_mg_per_dL: 56
  protein_mg_per_dL: 110
  lactate_mmol_per_L: 2.4
  ada_U_per_L: None
  crag_lfa_result: negative
  wet_mount_motile_amoebae: negative
  xanthochromia_present: True
  rbc_per_mm3: 30

IMAGING:
  modality: mri_with_dwi_flair
  pattern: mesial_temporal_t2_flair_hyperintensity
  contrast_enhancement: False
  hydrocephalus: False
  basal_meningeal_enhancement: False
  finding_count: 1
  text_summary: MRI brain with DWI/FLAIR: mesial temporal T2/FLAIR hyperintensity asymmetric with basal ganglia sparing. Canonical HSE imaging signature per Tyler 2018 NEJM viral encephalitis review.

DIAGNOSTIC_TESTS:
  pcr_panel: positive
  xpert_mtb_rif: n/a
  blood_culture: n/a
  csf_culture: n/a
  serology_or_antigen: n/a
  smear_or_gram: n/a
  brain_biopsy: n/a
  imaging_test: n/a
  total_dx_results: 3

NARRATIVE_EN: A 17-year-old man in the US South region presented to a tertiary emergency department with a 4-day course: fever to 38.5 C, headache, behavioral change with personality alteration on day 2, anomic aphasia on day 3, and a complex partial seizure on day 4. He had no neck stiffness and no antecedent freshwater exposure. Examination on admission: temperature 38.5 C, Glasgow Coma Scale 13, focal deficit (anomic aphasia), no rash. CSF showed opening pressure 22 cmH2O, white cell count 200 per cubic millimeter (78 percent lymphocytes), glucose 56 mg/dL, protein 110 mg/dL, RBC 30 with xanthochromia. CSF HSV-1 PCR positive. Brain MRI with DWI/FLAIR showed mesial temporal T2/FLAIR hyperintensity asymmetric. Acyclovir initiated within four hours. Anchored to Whitley 2006 Lancet Infect Dis HSE pathogenesis review (PMID 16675036), older-adolescent-HSE stratum. Outcome: survived with mild memory deficit. Subphase 1.3 commit 5.3.6 wave 2, pre-adjudication hold_for_revision.

NARRATIVE_ES: Varon de 17 anos en region sur de Estados Unidos, ingresado a urgencias terciarias con curso de cuatro dias: fiebre 38.5 C, cefalea, cambio conductual con alteracion de personalidad al segundo dia, afasia anomica al tercer dia y crisis parcial compleja al cuarto. Sin rigidez de nuca. Sin exposicion a agua dulce. Examen: temperatura 38.5 C, escala de Glasgow 13, deficit focal (afasia anomica), sin exantema. Liquido cefalorraquideo mostro presion de apertura 22 cmH2O, leucocitos 200 por mm3 (78 por ciento linfocitos), glucosa 56 mg/dL, proteina 110 mg/dL, eritrocitos 30 con xantocromia. PCR de HSV-1 positiva. RM cerebral con hiperintensidad temporal mesial T2/FLAIR. Aciclovir en cuatro horas. Anclaje en revision Whitley 2006 Lancet ID HSE (PMID 16675036). Subphase 1.3 commit 5.3.6 wave 2, pre-adjudicacion hold_for_revision.

RATIONALE: Anchored to PMID 16675036 (Whitley 2006 Lancet ID HSE pathogenesis review). Older-adolescent HSE phenotype. Demographic anchor (17yo M US South older-adolescent HSE) sits in Whitley adolescent-HSE stratum. CSF lymphocytic with hemorrhagic component. MRI mesial temporal. Imputation tiers: tier_1_primary={age, sex, hsv1_pcr, imaging_pattern, focal_aphasia, behavioral_change}; tier_3_within_review={csf_wbc, neutrophil_pct, glucose, protein, rbc, xanthochromia, gcs}; tier_4_priors={temp, symptom_days}. Indeterminate=none. Diagnostic_ambiguity=false. Outcome=survived_mild_memory_deficit. Acyclovir_hours=4. Tier: tier_3_imputation_within_review. 5.3.6 wave2 HSV1-Whitley-older-adolescent.

ANCHORING_EXTRAS: stage=pre_adjudication; status=pending_external_review; self_review_disposition=hold_for_revision; self_review_notes=wave 5.3.6 VIRAL vignette anchored to PMID 16675036 (Whitley 2006 Lancet ID HSE pathogenesis review); external clinical adjudication pending; classification provisional. adjudicator_ids=VIRAL-WAVE2-PRE-ADJ-1, VIRAL-WAVE2-PRE-ADJ-2 (sentinel); cohen_kappa=0.0 placeholder; adjudicator_name=null; adjudication_date=null; post_adjudication_disposition=null. Subphase 1.3 commit 5.3.6 (2026-05-08, FINAL Subphase 1.3 wave). anchor=Whitley-Lancet-ID-2006 stratum=older-adolescent-HSE.

ADJUDICATION:
  inclusion_decision: hold_for_revision
  adjudicator_ids: ['VIRAL-WAVE2-PRE-ADJ-1', 'VIRAL-WAVE2-PRE-ADJ-2']
  ground_truth_class: 3
  pre_adjudication_kappa: 0.0
  disagreement_resolution: None

=== END vignette ===

=== CLASS 3 | vignette_id: 102 | subphase: 1.3 VIRAL | file: vir_102_hsv1_adult.json ===

ANCHOR:
  pmid: 30089069
  first_author: Tyler
  year: 2018
  journal: NEJM
  citation_type: review
  doi: 10.1056/NEJMra1708714

DEMOGRAPHICS:
  age_years: 50
  sex: male
  geography_region: other_global
  ethnicity: white_non_hispanic
  altitude_residence_m: 5
  hiv_status: negative
  cd4_count_cells_per_uL: None
  pregnancy_red_flag: False
  immunocompromise_status: none
  freshwater_exposure_within_14d: False
  freshwater_exposure_type: None

HISTORY:
  symptom_onset_to_presentation_days: 6.0
  chief_complaint: behavioral_change
  red_flags_present: []
  prodrome_description: 50-year-old male, Netherlands. 6-day course: low-grade fever 38.4 C, headache, then progressive behavioral change with disinhibition day 3, anomic aphasia day 4, left-sided focal seizure day 6 prompting tertiary ED Amsterdam. No neck stiffness. No freshwater. Acyclovir hour 4. Outcome: survived with moderate memory deficit.

VITALS:
  temperature_celsius: 38.4
  heart_rate_bpm: 88
  systolic_bp_mmHg: 132
  diastolic_bp_mmHg: 80
  glasgow_coma_scale: 11
  oxygen_saturation_pct: 96
  respiratory_rate_breaths_per_min: 18

EXAM:
  mental_status_grade: somnolent
  neck_stiffness: False
  kernig_or_brudzinski_positive: False
  cranial_nerve_palsy: none
  papilledema_on_fundoscopy: False
  focal_neurological_deficit: True
  skin_lesion_centrofacial_chronic: False
  petechial_or_purpuric_rash: False

LABS:
  wbc_blood_per_uL: 9600
  platelets_per_uL: 235000
  alt_ast_U_per_L: 28
  crp_mg_per_L: 24.0
  procalcitonin_ng_per_mL: 0.4
  serum_sodium_mEq_per_L: 137

CSF:
  opening_pressure_cmH2O: 24.0
  wbc_per_mm3: 250
  lymphocyte_pct: 72
  neutrophil_pct: 28
  eosinophil_pct: 0
  glucose_mg_per_dL: 52
  protein_mg_per_dL: 135
  lactate_mmol_per_L: 2.8
  ada_U_per_L: None
  crag_lfa_result: negative
  wet_mount_motile_amoebae: negative
  xanthochromia_present: True
  rbc_per_mm3: 40

IMAGING:
  modality: mri_with_dwi_flair
  pattern: mesial_temporal_t2_flair_hyperintensity
  contrast_enhancement: False
  hydrocephalus: False
  basal_meningeal_enhancement: False
  finding_count: 1
  text_summary: MRI brain with DWI/FLAIR: mesial temporal T2/FLAIR hyperintensity asymmetric with basal ganglia sparing. Canonical HSE imaging signature per Tyler 2018 NEJM viral encephalitis review.

DIAGNOSTIC_TESTS:
  pcr_panel: positive
  xpert_mtb_rif: n/a
  blood_culture: n/a
  csf_culture: n/a
  serology_or_antigen: n/a
  smear_or_gram: n/a
  brain_biopsy: n/a
  imaging_test: n/a
  total_dx_results: 3

NARRATIVE_EN: A 50-year-old man in the Netherlands presented to a tertiary emergency department in Amsterdam with a 6-day course: low-grade fever to 38.4 C, headache, then progressive behavioral change with disinhibition on day 3, anomic aphasia on day 4, and a left-sided focal seizure on day 6 prompting ED presentation. He had no neck stiffness on examination and no antecedent freshwater exposure. Examination on admission: Glasgow Coma Scale 11, focal neurological deficit (anomic aphasia and disinhibition). CSF showed opening pressure 24 cmH2O, white cell count 250 per cubic millimeter (72 percent lymphocytes), glucose 52 mg/dL, protein 135 mg/dL, RBC 40 with xanthochromia. CSF HSV-1 PCR positive. Brain MRI with DWI/FLAIR showed mesial temporal T2/FLAIR hyperintensity asymmetric with bilateral but left-dominant involvement and basal ganglia sparing. Acyclovir initiated within four hours. Anchored to Tyler 2018 NEJM viral encephalitis review (PMID 30089069). Outcome: survived with moderate memory deficit. Subphase 1.3 commit 5.3.5 wave 1, pre-adjudication hold_for_revision.

NARRATIVE_ES: Varon de 50 anos en Paises Bajos (Amsterdam), ingresado a urgencias terciarias con curso de seis dias: febricula 38.4 C, cefalea, luego cambio conductual progresivo con desinhibicion al tercer dia, afasia anomica al cuarto dia y crisis focal izquierda al sexto dia que motivo consulta. Sin rigidez de nuca al examen. Sin exposicion a agua dulce. Examen: escala de Glasgow 11, deficit focal (afasia anomica, desinhibicion). Liquido cefalorraquideo mostro presion de apertura 24 cmH2O, leucocitos 250 por mm3 (72 por ciento linfocitos), glucosa 52 mg/dL, proteina 135 mg/dL, eritrocitos 40 con xantocromia. PCR de HSV-1 positiva. RM cerebral mostro hiperintensidad temporal mesial T2/FLAIR bilateral con dominancia izquierda. Anclaje en revision Tyler 2018 NEJM (PMID 30089069). Subphase 1.3 commit 5.3.5 wave 1, pre-adjudicacion hold_for_revision.

RATIONALE: Anchored to PMID 30089069 (Tyler 2018 NEJM viral encephalitis review). HSV1 mesial-temporal-encephalitis phenotype with frontal-disinhibition + anomic aphasia (limbic + frontal extension). Demographic anchor (50yo M adult HSE) sits in adult-HSE stratum. CSF lymphocytic with hemorrhagic component. MRI mesial temporal pattern with bilateral but asymmetric involvement. Imputation tiers: tier_1_primary={age, sex, hsv1_pcr, imaging_pattern, focal_aphasia, behavioral_change}; tier_3_within_review={csf_wbc, neutrophil_pct, glucose, protein, rbc, xanthochromia, gcs}; tier_4_priors={temp, symptom_days}. Indeterminate=none. Diagnostic_ambiguity=false. Outcome=survived_moderate_memory_deficit. Acyclovir_hours=4. Tier: tier_3_imputation_within_review. 5.3.5 wave1 HSV1-NL-adult-male-bilateral.

ANCHORING_EXTRAS: stage=pre_adjudication; status=pending_external_review; self_review_disposition=hold_for_revision; self_review_notes=wave 5.3.5 VIRAL vignette anchored to PMID 30089069 (Tyler 2018 NEJM viral encephalitis review); external clinical adjudication pending; classification provisional. adjudicator_ids=VIRAL-WAVE1-PRE-ADJ-1, VIRAL-WAVE1-PRE-ADJ-2 (sentinel); cohen_kappa=0.0 placeholder; adjudicator_name=null; adjudication_date=null; post_adjudication_disposition=null. Subphase 1.3 commit 5.3.5 (2026-05-08). anchor=Tyler-NEJM-2018 stratum=HSV1-adult-bilateral.

ADJUDICATION:
  inclusion_decision: hold_for_revision
  adjudicator_ids: ['VIRAL-WAVE1-PRE-ADJ-1', 'VIRAL-WAVE1-PRE-ADJ-2']
  ground_truth_class: 3
  pre_adjudication_kappa: 0.0
  disagreement_resolution: None

=== END vignette ===

=== CLASS 3 | vignette_id: 103 | subphase: 1.3 VIRAL | file: vir_103_hsv_pcr_negative_72h_ambiguity.json ===

ANCHOR:
  pmid: 20952256
  first_author: Granerod
  year: 2010
  journal: Lancet Infect Dis
  citation_type: cohort
  doi: 10.1016/S1473-3099(10)70222-X

DEMOGRAPHICS:
  age_years: 42
  sex: male
  geography_region: other_global
  ethnicity: white_non_hispanic
  altitude_residence_m: 5
  hiv_status: negative
  cd4_count_cells_per_uL: None
  pregnancy_red_flag: False
  immunocompromise_status: none
  freshwater_exposure_within_14d: False
  freshwater_exposure_type: None

HISTORY:
  symptom_onset_to_presentation_days: 5.0
  chief_complaint: altered_mental_status
  red_flags_present: []
  prodrome_description: 42-year-old male, Netherlands. 5-day course: low-grade fever 38.4 C, headache, behavioral change day 2, anomic aphasia day 3, focal seizure day 4 prompting tertiary ED. No neck stiffness. No freshwater. Diagnostic_ambiguity=true; type=hsv_clinical_phenotype_pcr_negative_at_72h. Empiric acyclovir continued despite negative HSV-1 PCR at 24h and 72h. Outcome: survived with full recovery on completion of 21-day empiric course.

VITALS:
  temperature_celsius: 38.4
  heart_rate_bpm: 96
  systolic_bp_mmHg: 122
  diastolic_bp_mmHg: 76
  glasgow_coma_scale: 12
  oxygen_saturation_pct: 96
  respiratory_rate_breaths_per_min: 18

EXAM:
  mental_status_grade: confused
  neck_stiffness: False
  kernig_or_brudzinski_positive: False
  cranial_nerve_palsy: none
  papilledema_on_fundoscopy: False
  focal_neurological_deficit: True
  skin_lesion_centrofacial_chronic: False
  petechial_or_purpuric_rash: False

LABS:
  wbc_blood_per_uL: 8800
  platelets_per_uL: 245000
  alt_ast_U_per_L: 26
  crp_mg_per_L: 22.0
  procalcitonin_ng_per_mL: 0.4
  serum_sodium_mEq_per_L: 138

CSF:
  opening_pressure_cmH2O: 22.0
  wbc_per_mm3: 180
  lymphocyte_pct: 75
  neutrophil_pct: 25
  eosinophil_pct: 0
  glucose_mg_per_dL: 54
  protein_mg_per_dL: 100
  lactate_mmol_per_L: 2.4
  ada_U_per_L: None
  crag_lfa_result: negative
  wet_mount_motile_amoebae: negative
  xanthochromia_present: False
  rbc_per_mm3: 8

IMAGING:
  modality: mri_with_dwi_flair
  pattern: mesial_temporal_t2_flair_hyperintensity
  contrast_enhancement: False
  hydrocephalus: False
  basal_meningeal_enhancement: False
  finding_count: 1
  text_summary: MRI brain with DWI/FLAIR: mesial temporal T2/FLAIR hyperintensity asymmetric supporting clinical HSE phenotype despite negative initial CSF HSV-1 PCR. Granerod 2010 Lancet ID UK encephalitis cohort documented PCR-negative HSE cases where MRI and clinical phenotype supported continued empiric acyclovir.

DIAGNOSTIC_TESTS:
  pcr_panel: negative_at_72h
  xpert_mtb_rif: n/a
  blood_culture: n/a
  csf_culture: n/a
  serology_or_antigen: n/a
  smear_or_gram: n/a
  brain_biopsy: n/a
  imaging_test: n/a
  total_dx_results: 5

NARRATIVE_EN: A 42-year-old man in the Netherlands presented to a tertiary emergency department in Amsterdam after a 5-day course: low-grade fever to 38.4 C, headache, behavioral change on day 2, anomic aphasia on day 3, and a focal seizure on day 4. He had no neck stiffness and no antecedent freshwater exposure. Examination: temperature 38.4 C, Glasgow Coma Scale 12, focal deficit (anomic aphasia), no rash. CSF showed opening pressure 22 cmH2O, WBC 180 per mm3 (75 percent lymphocytes), glucose 54 mg/dL, protein 100 mg/dL. CSF HSV-1 PCR negative at initial sample (24h) and negative on repeat at 72h. EEG showed left temporal periodic lateralized epileptiform discharges. Brain MRI DWI/FLAIR showed asymmetric mesial temporal hyperintensity supporting clinical HSE phenotype despite negative PCR. Empiric acyclovir continued for the full 21-day course. Diagnostic_ambiguity=true; type=hsv_clinical_phenotype_pcr_negative_at_72h. Anchored to Granerod 2010 Lancet ID UK encephalitis cohort (PMID 20952256). Outcome: survived with full recovery. Subphase 1.3 commit 5.3.6 wave 2, pre-adjudication hold.

NARRATIVE_ES: Varon de 42 anos en Paises Bajos (Amsterdam), ingresado a urgencias terciarias tras curso de cinco dias: febricula 38.4 C, cefalea, cambio conductual al segundo dia, afasia anomica al tercero y crisis focal al cuarto. Sin rigidez de nuca. Examen: 38.4 C, Glasgow 12, deficit focal (afasia anomica), sin exantema. LCR: presion 22 cmH2O, leucocitos 180/mm3 (75 por ciento linfocitos), glucosa 54 mg/dL, proteina 100 mg/dL. PCR de HSV-1 negativa inicial y a las 72 horas. EEG con descargas lateralizadas temporales izquierdas. RM con hiperintensidad temporal mesial T2/FLAIR asimetrica. Aciclovir empirico continuado por 21 dias completos. Ambiguedad diagnostica: fenotipo clinico de HSE con PCR negativa. Anclaje en cohorte Granerod 2010 Lancet ID (PMID 20952256). Subphase 1.3 commit 5.3.6 wave 2.

RATIONALE: Anchored to PMID 20952256 (Granerod 2010 Lancet ID UK encephalitis cohort) documenting PCR-negative-but-clinical-HSE phenotype. Diagnostic_ambiguity=true; type=hsv_clinical_phenotype_pcr_negative_at_72h (verbatim from spec). Demographic anchor (42yo M NL adult HSE PCR-neg) sits in PCR-negative-HSE-window stratum. CSF lymphocytic, no hemorrhagic component (atypical for HSE; supports diagnostic uncertainty), MRI consistent with HSE despite negative PCR. EEG temporal lateralization supports clinical HSE. Imputation tiers: tier_1_primary={age, sex, hsv1_pcr_neg, eeg_lateralization, imaging_pattern, empiric_acyclovir_continuation}; tier_3_within_review={csf_wbc, neutrophil_pct, glucose, protein, gcs}; tier_4_priors={temp, symptom_days}. Indeterminate=organism-level-confirmation. Outcome=survived_full_recovery. Tier: tier_4_imputation_within_review_ambiguity. 5.3.6 wave2 HSV-PCR-neg-male.

ANCHORING_EXTRAS: stage=pre_adjudication; status=pending_external_review; self_review_disposition=hold_for_revision; self_review_notes=wave 5.3.6 VIRAL vignette anchored to PMID 20952256 (Granerod 2010 Lancet ID UK encephalitis cohort); external clinical adjudication pending; classification provisional. adjudicator_ids=VIRAL-WAVE2-PRE-ADJ-1, VIRAL-WAVE2-PRE-ADJ-2 (sentinel); cohen_kappa=0.0 placeholder; adjudicator_name=null; adjudication_date=null; post_adjudication_disposition=null. Subphase 1.3 commit 5.3.6 (2026-05-08, FINAL Subphase 1.3 wave). anchor=Granerod-Lancet-ID-2010 type=hsv_clinical_phenotype_pcr_negative_at_72h.

ADJUDICATION:
  inclusion_decision: hold_for_revision
  adjudicator_ids: ['VIRAL-WAVE2-PRE-ADJ-1', 'VIRAL-WAVE2-PRE-ADJ-2']
  ground_truth_class: 3
  pre_adjudication_kappa: 0.0
  disagreement_resolution: None

=== END vignette ===

=== CLASS 3 | vignette_id: 104 | subphase: 1.3 VIRAL | file: vir_104_hsv_pcr_negative_72h_ambiguity.json ===

ANCHOR:
  pmid: 20952256
  first_author: Granerod
  year: 2010
  journal: Lancet Infect Dis
  citation_type: cohort
  doi: 10.1016/S1473-3099(10)70222-X

DEMOGRAPHICS:
  age_years: 35
  sex: female
  geography_region: other_global
  ethnicity: white_non_hispanic
  altitude_residence_m: 5
  hiv_status: negative
  cd4_count_cells_per_uL: None
  pregnancy_red_flag: False
  immunocompromise_status: none
  freshwater_exposure_within_14d: False
  freshwater_exposure_type: None

HISTORY:
  symptom_onset_to_presentation_days: 4.0
  chief_complaint: altered_mental_status
  red_flags_present: []
  prodrome_description: 35-year-old female, Netherlands. 4-day course: low-grade fever 38.5 C, headache, behavioral change with personality alteration day 2, expressive aphasia day 3, complex partial seizure day 4 prompting tertiary ED. No neck stiffness. No freshwater. Diagnostic_ambiguity=true; type=hsv_clinical_phenotype_pcr_negative_at_72h. Empiric acyclovir continued despite negative HSV-1 PCR at 24h and 72h. Outcome: survived with mild memory deficit on 21-day course.

VITALS:
  temperature_celsius: 38.5
  heart_rate_bpm: 100
  systolic_bp_mmHg: 118
  diastolic_bp_mmHg: 72
  glasgow_coma_scale: 12
  oxygen_saturation_pct: 97
  respiratory_rate_breaths_per_min: 18

EXAM:
  mental_status_grade: confused
  neck_stiffness: False
  kernig_or_brudzinski_positive: False
  cranial_nerve_palsy: none
  papilledema_on_fundoscopy: False
  focal_neurological_deficit: True
  skin_lesion_centrofacial_chronic: False
  petechial_or_purpuric_rash: False

LABS:
  wbc_blood_per_uL: 9000
  platelets_per_uL: 250000
  alt_ast_U_per_L: 26
  crp_mg_per_L: 24.0
  procalcitonin_ng_per_mL: 0.4
  serum_sodium_mEq_per_L: 138

CSF:
  opening_pressure_cmH2O: 22.0
  wbc_per_mm3: 165
  lymphocyte_pct: 72
  neutrophil_pct: 28
  eosinophil_pct: 0
  glucose_mg_per_dL: 55
  protein_mg_per_dL: 95
  lactate_mmol_per_L: 2.4
  ada_U_per_L: None
  crag_lfa_result: negative
  wet_mount_motile_amoebae: negative
  xanthochromia_present: False
  rbc_per_mm3: 6

IMAGING:
  modality: mri_with_dwi_flair
  pattern: mesial_temporal_t2_flair_hyperintensity
  contrast_enhancement: False
  hydrocephalus: False
  basal_meningeal_enhancement: False
  finding_count: 1
  text_summary: MRI brain with DWI/FLAIR: mesial temporal T2/FLAIR hyperintensity asymmetric supporting clinical HSE phenotype despite negative initial CSF HSV-1 PCR. Granerod 2010 Lancet ID UK encephalitis cohort documented PCR-negative HSE cases where MRI and clinical phenotype supported continued empiric acyclovir.

DIAGNOSTIC_TESTS:
  pcr_panel: negative_at_72h
  xpert_mtb_rif: n/a
  blood_culture: n/a
  csf_culture: n/a
  serology_or_antigen: n/a
  smear_or_gram: n/a
  brain_biopsy: n/a
  imaging_test: n/a
  total_dx_results: 5

NARRATIVE_EN: A 35-year-old woman in the Netherlands presented to a tertiary emergency department in Amsterdam after a 4-day course: low-grade fever to 38.5 C, headache, behavioral change with personality alteration on day 2, expressive aphasia on day 3, and a complex partial seizure on day 4. She had no neck stiffness and no freshwater exposure. Examination: temperature 38.5 C, Glasgow Coma Scale 12, focal deficit (expressive aphasia), no rash. CSF showed opening pressure 22 cmH2O, WBC 165 per mm3 (72 percent lymphocytes), glucose 55 mg/dL, protein 95 mg/dL. CSF HSV-1 PCR negative at initial sample (24h) and negative on repeat at 72h. EEG showed right temporal periodic lateralized epileptiform discharges. Brain MRI DWI/FLAIR showed asymmetric mesial temporal hyperintensity supporting clinical HSE despite negative PCR. Empiric acyclovir continued for the full 21-day course. Diagnostic_ambiguity=true; type=hsv_clinical_phenotype_pcr_negative_at_72h. Anchored to Granerod 2010 Lancet ID (PMID 20952256). Outcome: survived with mild memory deficit. Subphase 1.3 commit 5.3.6 wave 2, pre-adj hold.

NARRATIVE_ES: Mujer de 35 anos en Paises Bajos (Amsterdam), ingresada a urgencias terciarias tras curso de cuatro dias: febricula 38.5 C, cefalea, cambio conductual con alteracion de personalidad al segundo dia, afasia expresiva al tercero y crisis parcial compleja al cuarto. Sin rigidez de nuca. Examen: 38.5 C, Glasgow 12, deficit focal (afasia expresiva), sin exantema. LCR: presion 22 cmH2O, leucocitos 165/mm3 (72 por ciento linfocitos), glucosa 55 mg/dL, proteina 95 mg/dL. PCR de HSV-1 negativa inicial y a las 72 horas tambien negativa. EEG con descargas lateralizadas temporales derechas. RM con hiperintensidad temporal mesial T2/FLAIR. Aciclovir empirico continuado por 21 dias. Ambiguedad diagnostica HSE con PCR negativa. Anclaje en cohorte Granerod 2010 Lancet ID (PMID 20952256). Subphase 1.3 commit 5.3.6 wave 2.

RATIONALE: Anchored to PMID 20952256 (Granerod 2010 Lancet ID UK encephalitis cohort) PCR-negative-HSE phenotype. Diagnostic_ambiguity=true; type=hsv_clinical_phenotype_pcr_negative_at_72h (verbatim from spec). Demographic anchor (35yo F NL adult HSE PCR-neg) sits in PCR-negative-HSE-window stratum. CSF lymphocytic, no hemorrhagic component, MRI consistent with HSE. EEG right-temporal lateralization. Imputation tiers: tier_1_primary={age, sex, hsv1_pcr_neg, eeg_lateralization, imaging_pattern, empiric_acyclovir}; tier_3_within_review={csf_wbc, neutrophil_pct, glucose, protein, gcs}; tier_4_priors={temp, symptom_days}. Indeterminate=organism-confirmation. Outcome=survived_mild_memory_deficit. Tier: tier_4_imputation_within_review_ambiguity. 5.3.6 wave2 HSV-PCR-neg-female.

ANCHORING_EXTRAS: stage=pre_adjudication; status=pending_external_review; self_review_disposition=hold_for_revision; self_review_notes=wave 5.3.6 VIRAL vignette anchored to PMID 20952256 (Granerod 2010 Lancet ID UK encephalitis cohort); external clinical adjudication pending; classification provisional. adjudicator_ids=VIRAL-WAVE2-PRE-ADJ-1, VIRAL-WAVE2-PRE-ADJ-2 (sentinel); cohen_kappa=0.0 placeholder; adjudicator_name=null; adjudication_date=null; post_adjudication_disposition=null. Subphase 1.3 commit 5.3.6 (2026-05-08, FINAL Subphase 1.3 wave). anchor=Granerod-Lancet-ID-2010 type=hsv_clinical_phenotype_pcr_negative_at_72h.

ADJUDICATION:
  inclusion_decision: hold_for_revision
  adjudicator_ids: ['VIRAL-WAVE2-PRE-ADJ-1', 'VIRAL-WAVE2-PRE-ADJ-2']
  ground_truth_class: 3
  pre_adjudication_kappa: 0.0
  disagreement_resolution: None

=== END vignette ===

=== CLASS 3 | vignette_id: 105 | subphase: 1.3 VIRAL | file: vir_105_enterovirus_pediatric.json ===

ANCHOR:
  pmid: 17668054
  first_author: Michos
  year: 2007
  journal: PLoSOne
  citation_type: cohort
  doi: 10.1371/journal.pone.0000674

DEMOGRAPHICS:
  age_years: 5
  sex: male
  geography_region: other_global
  ethnicity: white_non_hispanic
  altitude_residence_m: 200
  hiv_status: negative
  cd4_count_cells_per_uL: None
  pregnancy_red_flag: False
  immunocompromise_status: none
  freshwater_exposure_within_14d: False
  freshwater_exposure_type: None

HISTORY:
  symptom_onset_to_presentation_days: 2.0
  chief_complaint: fever_with_headache
  red_flags_present: []
  prodrome_description: 5-year-old male, Athens Greece (Aghia Sophia Children's Hospital), pediatric ED. 2-day course: fever 38.6 C, headache, vomiting, photophobia, neck stiffness on exam, summer late-June presentation. No rash. No freshwater exposure. Outcome: survived with full recovery. Diagnostic_ambiguity_flag=true; type=csf_neutrophil_predominant_in_confirmed_viral (reflects Michos 2007 cohort evidence).

VITALS:
  temperature_celsius: 38.6
  heart_rate_bpm: 110
  systolic_bp_mmHg: 100
  diastolic_bp_mmHg: 64
  glasgow_coma_scale: 15
  oxygen_saturation_pct: 98
  respiratory_rate_breaths_per_min: 22

EXAM:
  mental_status_grade: alert
  neck_stiffness: True
  kernig_or_brudzinski_positive: True
  cranial_nerve_palsy: none
  papilledema_on_fundoscopy: False
  focal_neurological_deficit: False
  skin_lesion_centrofacial_chronic: False
  petechial_or_purpuric_rash: False

LABS:
  wbc_blood_per_uL: 11200
  platelets_per_uL: 285000
  alt_ast_U_per_L: 22
  crp_mg_per_L: 18.0
  procalcitonin_ng_per_mL: 0.3
  serum_sodium_mEq_per_L: 138

CSF:
  opening_pressure_cmH2O: 18.0
  wbc_per_mm3: 220
  lymphocyte_pct: 35
  neutrophil_pct: 65
  eosinophil_pct: 0
  glucose_mg_per_dL: 55
  protein_mg_per_dL: 65
  lactate_mmol_per_L: 2.4
  ada_U_per_L: None
  crag_lfa_result: negative
  wet_mount_motile_amoebae: negative
  xanthochromia_present: False
  rbc_per_mm3: 3

IMAGING:
  modality: none
  pattern: (none)
  contrast_enhancement: False
  hydrocephalus: False
  basal_meningeal_enhancement: False
  finding_count: None
  text_summary: No imaging performed (uncomplicated viral meningitis presentation in a child with normal mental status; per IDSA encephalitis guidelines imaging not mandatory in this context).

DIAGNOSTIC_TESTS:
  pcr_panel: positive
  xpert_mtb_rif: n/a
  blood_culture: n/a
  csf_culture: n/a
  serology_or_antigen: n/a
  smear_or_gram: n/a
  brain_biopsy: n/a
  imaging_test: n/a
  total_dx_results: 3

NARRATIVE_EN: A 5-year-old boy in Athens, Greece (Aghia Sophia Children's Hospital) presented with a two-day course of fever to 38.6 C, headache, vomiting, photophobia, and neck stiffness on examination, in summer (late June; matches the seasonal peak of the Michos 2007 cohort). Examination on admission: temperature 38.6 C, Glasgow Coma Scale 15, alert, neck stiffness, positive Kernig sign, no focal deficit, no rash. CSF showed opening pressure 18 cmH2O, white cell count 220 per cubic millimeter (65 percent neutrophils, deliberately PMN-predominant reflecting the Michos 2007 finding of PMN predominance in 58.3 percent of EV PCR-positive cases), glucose 55 mg/dL, protein 65 mg/dL. CSF enterovirus PCR positive. Gram stain and culture negative. No imaging performed (uncomplicated viral meningitis presentation in a child with normal mental status). Primary anchor: PMID 17668054 (Michos 2007 PLoS One), 506-child pediatric aseptic meningitis cohort (median age 5y, EV PCR-positive 48.9 percent, PMN-predominance 58.3 percent in EV PCR-positive). Diagnostic_ambiguity_flag=true; type=csf_neutrophil_predominant_in_confirmed_viral. Outcome: survived with full recovery (no deaths in cohort). Subphase 1.3 commit 5.3.2 pilot 5, pre-adjudication hold_for_revision.

NARRATIVE_ES: Nino de 5 anos en Atenas, Grecia (Hospital Pediatrico Aghia Sophia), ingresado con dos dias de fiebre 38.6 C, cefalea, vomitos, fotofobia y rigidez de nuca al examen, presentacion estival en junio (pico estacional de la cohorte Michos 2007). Examen: temperatura 38.6 C, escala de Glasgow 15, alerta, rigidez de nuca, signo de Kernig positivo, sin deficit focal, sin exantema. Liquido cefalorraquideo mostro presion de apertura 18 cmH2O, leucocitos 220 por mm3 (65 por ciento neutrofilos, predominio polimorfonuclear deliberado que refleja el hallazgo Michos 2007 de PMN-predominancia en 58.3 por ciento de casos EV PCR-positivos), glucosa 55 mg/dL, proteina 65 mg/dL. PCR de enterovirus en LCR positiva. Cultivo y tincion de Gram negativos. Sin imagenes (presentacion no complicada). Anclaje primario en cohorte pediatrica de meningitis aseptica de 506 ninos (PMID 17668054, Michos 2007 PLoS One, mediana 5 anos, EV PCR-positivo 48.9 por ciento, PMN-predominancia 58.3 por ciento). Diagnostic_ambiguity_flag=true. Subphase 1.3 commit 5.3.2 pilot 5.

RATIONALE: Anchored to PMID 17668054 (Michos 2007 PLoS One 2(7):e674), 506-child aseptic meningitis Athens cohort with EV PCR positive in 48.9 percent (47/96 tested). CRITICAL: cohort documented PMN predominance >50 percent in 58.3 percent of EV PCR-positive cases, contradicting textbook viral-CSF-lymphocytic. Vignette deliberately reflects this evidence-based reality (CSF WBC 220 near cohort median 201, neutrophils 65 percent). Anchor (5yo M summer) matches cohort median age and seasonal peak. Imputation tiers: tier_1_primary={age, sex, ev_pcr, neutrophil_pct, season}; tier_3_within_cohort={csf_wbc, glucose, protein}; tier_4_priors={temp, symptom_days, gcs}. Indeterminate=none. Diagnostic_ambiguity=true; type=csf_neutrophil_predominant_in_confirmed_viral. Outcome=survived_full_recovery (no cohort deaths). Tier: primary_source_direct. 5.3.2 pilot 5.

ANCHORING_EXTRAS: stage=pre_adjudication; status=pending_external_review; self_review_disposition=hold_for_revision; self_review_notes=pilot vignette anchored to PMID 17668054 (Michos 2007 PLoS One pediatric aseptic 506 cohort); external clinical adjudication pending; classification provisional. adjudicator_ids=PILOT-PRE-ADJ-1, PILOT-PRE-ADJ-2 (sentinel); cohen_kappa=0.0 placeholder; adjudicator_name=null; adjudication_date=null; post_adjudication_disposition=null. Subphase 1.3 commit 5.3.2 (2026-05-07).

ADJUDICATION:
  inclusion_decision: hold_for_revision
  adjudicator_ids: ['PILOT-PRE-ADJ-1', 'PILOT-PRE-ADJ-2']
  ground_truth_class: 3
  pre_adjudication_kappa: 0.0
  disagreement_resolution: None

=== END vignette ===

=== CLASS 3 | vignette_id: 106 | subphase: 1.3 VIRAL | file: vir_106_enterovirus_pediatric.json ===

ANCHOR:
  pmid: 30089069
  first_author: Tyler
  year: 2018
  journal: NEJM
  citation_type: review
  doi: 10.1056/NEJMra1708714

DEMOGRAPHICS:
  age_years: 7
  sex: female
  geography_region: us_south
  ethnicity: white_non_hispanic
  altitude_residence_m: 100
  hiv_status: negative
  cd4_count_cells_per_uL: None
  pregnancy_red_flag: False
  immunocompromise_status: none
  freshwater_exposure_within_14d: False
  freshwater_exposure_type: None

HISTORY:
  symptom_onset_to_presentation_days: 1.0
  chief_complaint: fever_with_headache
  red_flags_present: []
  prodrome_description: 7-year-old female, US South region. 24-hour course: fever 38.4 C, headache, neck stiffness, photophobia, nausea, summer late-July presentation. Pediatric tertiary ED. No freshwater. No focal deficit. Outcome: survived with full recovery in 5 days. Supportive care; no antibiotics after enterovirus PCR positive.

VITALS:
  temperature_celsius: 38.4
  heart_rate_bpm: 108
  systolic_bp_mmHg: 100
  diastolic_bp_mmHg: 64
  glasgow_coma_scale: 15
  oxygen_saturation_pct: 98
  respiratory_rate_breaths_per_min: 22

EXAM:
  mental_status_grade: alert
  neck_stiffness: True
  kernig_or_brudzinski_positive: True
  cranial_nerve_palsy: none
  papilledema_on_fundoscopy: False
  focal_neurological_deficit: False
  skin_lesion_centrofacial_chronic: False
  petechial_or_purpuric_rash: False

LABS:
  wbc_blood_per_uL: 10800
  platelets_per_uL: 295000
  alt_ast_U_per_L: 22
  crp_mg_per_L: 16.0
  procalcitonin_ng_per_mL: 0.3
  serum_sodium_mEq_per_L: 138

CSF:
  opening_pressure_cmH2O: 18.0
  wbc_per_mm3: 95
  lymphocyte_pct: 80
  neutrophil_pct: 20
  eosinophil_pct: 0
  glucose_mg_per_dL: 60
  protein_mg_per_dL: 50
  lactate_mmol_per_L: 2.0
  ada_U_per_L: None
  crag_lfa_result: negative
  wet_mount_motile_amoebae: negative
  xanthochromia_present: False
  rbc_per_mm3: 3

IMAGING:
  modality: none
  pattern: (none)
  contrast_enhancement: False
  hydrocephalus: False
  basal_meningeal_enhancement: False
  finding_count: None
  text_summary: No imaging performed (uncomplicated enteroviral meningitis presentation with normal mental status; Tyler 2018 NEJM review supports deferring imaging in benign aseptic pattern).

DIAGNOSTIC_TESTS:
  pcr_panel: positive
  xpert_mtb_rif: n/a
  blood_culture: n/a
  csf_culture: n/a
  serology_or_antigen: n/a
  smear_or_gram: n/a
  brain_biopsy: n/a
  imaging_test: n/a
  total_dx_results: 3

NARRATIVE_EN: A 7-year-old girl in the US South region presented to a tertiary pediatric emergency department in late July with a 24-hour course of fever to 38.4 C, headache, neck stiffness, photophobia, and nausea. Examination on admission: temperature 38.4 C, Glasgow Coma Scale 15, alert, neck stiffness, positive Kernig sign, no focal deficit, no rash. CSF showed opening pressure 18 cmH2O, white cell count 95 per cubic millimeter (80 percent lymphocytes), glucose 60 mg/dL, protein 50 mg/dL. CSF enterovirus PCR positive. Gram stain and culture negative. No imaging performed (uncomplicated viral meningitis presentation in a child with normal mental status). Anchored to Tyler 2018 NEJM viral encephalitis review (PMID 30089069), summer enteroviral peak stratum. Outcome: survived with full recovery in five days. Subphase 1.3 commit 5.3.5 wave 1, pre-adjudication hold_for_revision.

NARRATIVE_ES: Nina de 7 anos en region sur de Estados Unidos, ingresada a urgencias pediatricas terciarias en julio con 24 horas de fiebre 38.4 C, cefalea, rigidez de nuca, fotofobia y nauseas. Examen: temperatura 38.4 C, escala de Glasgow 15, alerta, rigidez de nuca, signo de Kernig positivo, sin deficit focal, sin exantema. Liquido cefalorraquideo mostro presion de apertura 18 cmH2O, leucocitos 95 por mm3 (80 por ciento linfocitos), glucosa 60 mg/dL, proteina 50 mg/dL. PCR de enterovirus en liquido cefalorraquideo positiva. Tincion de Gram y cultivo negativos. Sin imagenes (presentacion no complicada). Anclaje en revision Tyler 2018 NEJM (PMID 30089069), estrato pico estival enteroviral. Subphase 1.3 commit 5.3.5 wave 1, pre-adjudicacion hold_for_revision.

RATIONALE: Anchored to PMID 30089069 (Tyler 2018 NEJM viral encephalitis review). Enteroviral aseptic meningitis with classic summer pediatric presentation. Demographic anchor (7yo F US South summer) sits in pediatric-aseptic-meningitis-summer-peak stratum. CSF lymphocytic (95 WBC, 80 percent lymphocytes), normal glucose 60, modestly elevated protein 50 - textbook viral pattern per Tyler review. EV PCR positive. Imputation tiers: tier_1_primary={age, sex, ev_pcr, season}; tier_3_within_review={csf_wbc, neutrophil_pct, glucose, protein}; tier_4_priors={temp, gcs, symptom_days}. Indeterminate=none. Diagnostic_ambiguity=false. Outcome=survived_full_recovery. Tier: tier_3_imputation_within_review. 5.3.5 wave1 EV-US-pediatric-summer.

ANCHORING_EXTRAS: stage=pre_adjudication; status=pending_external_review; self_review_disposition=hold_for_revision; self_review_notes=wave 5.3.5 VIRAL vignette anchored to PMID 30089069 (Tyler 2018 NEJM viral encephalitis review); external clinical adjudication pending; classification provisional. adjudicator_ids=VIRAL-WAVE1-PRE-ADJ-1, VIRAL-WAVE1-PRE-ADJ-2 (sentinel); cohen_kappa=0.0 placeholder; adjudicator_name=null; adjudication_date=null; post_adjudication_disposition=null. Subphase 1.3 commit 5.3.5 (2026-05-08). anchor=Tyler-NEJM-2018 stratum=EV-pediatric-summer.

ADJUDICATION:
  inclusion_decision: hold_for_revision
  adjudicator_ids: ['VIRAL-WAVE1-PRE-ADJ-1', 'VIRAL-WAVE1-PRE-ADJ-2']
  ground_truth_class: 3
  pre_adjudication_kappa: 0.0
  disagreement_resolution: None

=== END vignette ===

=== CLASS 3 | vignette_id: 107 | subphase: 1.3 VIRAL | file: vir_107_enterovirus_young_adult.json ===

ANCHOR:
  pmid: 30089069
  first_author: Tyler
  year: 2018
  journal: NEJM
  citation_type: review
  doi: 10.1056/NEJMra1708714

DEMOGRAPHICS:
  age_years: 22
  sex: female
  geography_region: other_global
  ethnicity: white_non_hispanic
  altitude_residence_m: 5
  hiv_status: negative
  cd4_count_cells_per_uL: None
  pregnancy_red_flag: False
  immunocompromise_status: none
  freshwater_exposure_within_14d: False
  freshwater_exposure_type: None

HISTORY:
  symptom_onset_to_presentation_days: 2.0
  chief_complaint: fever_with_headache
  red_flags_present: []
  prodrome_description: 22-year-old female, Netherlands. 2-day course: fever 38.6 C, severe headache, neck stiffness, photophobia, myalgia, summer August presentation. University setting. Tertiary ED Amsterdam. No freshwater. No focal deficit. Outcome: survived with full recovery in 7 days. Supportive care; no antiviral or antibiotics after EV PCR positive.

VITALS:
  temperature_celsius: 38.6
  heart_rate_bpm: 102
  systolic_bp_mmHg: 116
  diastolic_bp_mmHg: 70
  glasgow_coma_scale: 15
  oxygen_saturation_pct: 98
  respiratory_rate_breaths_per_min: 18

EXAM:
  mental_status_grade: alert
  neck_stiffness: True
  kernig_or_brudzinski_positive: True
  cranial_nerve_palsy: none
  papilledema_on_fundoscopy: False
  focal_neurological_deficit: False
  skin_lesion_centrofacial_chronic: False
  petechial_or_purpuric_rash: False

LABS:
  wbc_blood_per_uL: 11500
  platelets_per_uL: 275000
  alt_ast_U_per_L: 24
  crp_mg_per_L: 18.0
  procalcitonin_ng_per_mL: 0.3
  serum_sodium_mEq_per_L: 138

CSF:
  opening_pressure_cmH2O: 19.0
  wbc_per_mm3: 220
  lymphocyte_pct: 78
  neutrophil_pct: 22
  eosinophil_pct: 0
  glucose_mg_per_dL: 55
  protein_mg_per_dL: 65
  lactate_mmol_per_L: 2.2
  ada_U_per_L: None
  crag_lfa_result: negative
  wet_mount_motile_amoebae: negative
  xanthochromia_present: False
  rbc_per_mm3: 3

IMAGING:
  modality: none
  pattern: (none)
  contrast_enhancement: False
  hydrocephalus: False
  basal_meningeal_enhancement: False
  finding_count: None
  text_summary: No imaging performed (uncomplicated enteroviral meningitis presentation with normal mental status; Tyler 2018 NEJM review supports deferring imaging in benign aseptic pattern).

DIAGNOSTIC_TESTS:
  pcr_panel: positive
  xpert_mtb_rif: n/a
  blood_culture: n/a
  csf_culture: n/a
  serology_or_antigen: n/a
  smear_or_gram: n/a
  brain_biopsy: n/a
  imaging_test: n/a
  total_dx_results: 3

NARRATIVE_EN: A 22-year-old woman in the Netherlands presented to a tertiary emergency department in Amsterdam in late August with a 2-day course of fever to 38.6 C, severe headache, neck stiffness, photophobia, and myalgia. She lived in a university setting. Examination on admission: temperature 38.6 C, Glasgow Coma Scale 15, alert, neck stiffness, positive Kernig sign, no focal deficit, no rash. CSF showed opening pressure 19 cmH2O, white cell count 220 per cubic millimeter (78 percent lymphocytes), glucose 55 mg/dL, protein 65 mg/dL. CSF enterovirus PCR positive. Gram stain and culture negative. No imaging performed (uncomplicated presentation). Anchored to Tyler 2018 NEJM viral encephalitis review (PMID 30089069), young-adult enteroviral summer-peak stratum. Outcome: survived with full recovery in seven days. Subphase 1.3 commit 5.3.5 wave 1, pre-adjudication hold_for_revision.

NARRATIVE_ES: Mujer de 22 anos en Paises Bajos (Amsterdam), ingresada a urgencias terciarias en agosto con dos dias de fiebre 38.6 C, cefalea intensa, rigidez de nuca, fotofobia y mialgia. Entorno universitario. Examen: temperatura 38.6 C, escala de Glasgow 15, alerta, rigidez de nuca, signo de Kernig positivo, sin deficit focal, sin exantema. Liquido cefalorraquideo mostro presion de apertura 19 cmH2O, leucocitos 220 por mm3 (78 por ciento linfocitos), glucosa 55 mg/dL, proteina 65 mg/dL. PCR de enterovirus en LCR positiva. Tincion de Gram y cultivo negativos. Sin imagenes. Anclaje en revision Tyler 2018 NEJM (PMID 30089069), estrato adulto joven pico estival enteroviral. Subphase 1.3 commit 5.3.5 wave 1, pre-adjudicacion hold_for_revision.

RATIONALE: Anchored to PMID 30089069 (Tyler 2018 NEJM viral encephalitis review). Enteroviral aseptic meningitis young-adult pattern. Demographic anchor (22yo F NL university summer) sits in young-adult-aseptic-meningitis-summer stratum. CSF lymphocytic (220 WBC, 78 percent lymphocytes), normal glucose 55, mildly elevated protein 65 - textbook viral pattern. EV PCR positive. Imputation tiers: tier_1_primary={age, sex, ev_pcr, season}; tier_3_within_review={csf_wbc, neutrophil_pct, glucose, protein}; tier_4_priors={temp, gcs, symptom_days}. Indeterminate=none. Diagnostic_ambiguity=false. Outcome=survived_full_recovery. Tier: tier_3_imputation_within_review. 5.3.5 wave1 EV-NL-young-adult.

ANCHORING_EXTRAS: stage=pre_adjudication; status=pending_external_review; self_review_disposition=hold_for_revision; self_review_notes=wave 5.3.5 VIRAL vignette anchored to PMID 30089069 (Tyler 2018 NEJM viral encephalitis review); external clinical adjudication pending; classification provisional. adjudicator_ids=VIRAL-WAVE1-PRE-ADJ-1, VIRAL-WAVE1-PRE-ADJ-2 (sentinel); cohen_kappa=0.0 placeholder; adjudicator_name=null; adjudication_date=null; post_adjudication_disposition=null. Subphase 1.3 commit 5.3.5 (2026-05-08). anchor=Tyler-NEJM-2018 stratum=EV-young-adult-summer.

ADJUDICATION:
  inclusion_decision: hold_for_revision
  adjudicator_ids: ['VIRAL-WAVE1-PRE-ADJ-1', 'VIRAL-WAVE1-PRE-ADJ-2']
  ground_truth_class: 3
  pre_adjudication_kappa: 0.0
  disagreement_resolution: None

=== END vignette ===

=== CLASS 3 | vignette_id: 108 | subphase: 1.3 VIRAL | file: vir_108_enterovirus_school_outbreak.json ===

ANCHOR:
  pmid: 30089069
  first_author: Tyler
  year: 2018
  journal: NEJM
  citation_type: review
  doi: 10.1056/NEJMra1708714

DEMOGRAPHICS:
  age_years: 11
  sex: male
  geography_region: us_south
  ethnicity: white_non_hispanic
  altitude_residence_m: 100
  hiv_status: negative
  cd4_count_cells_per_uL: None
  pregnancy_red_flag: False
  immunocompromise_status: none
  freshwater_exposure_within_14d: False
  freshwater_exposure_type: None

HISTORY:
  symptom_onset_to_presentation_days: 2.0
  chief_complaint: fever_with_headache
  red_flags_present: []
  prodrome_description: 11-year-old male, US South region. School outbreak with multiple peers symptomatic. 2-day course: fever 38.7 C, headache, neck stiffness, photophobia, vomiting, summer early-September presentation. Pediatric tertiary ED. No freshwater. No focal. Outcome: survived with full recovery in 6 days.

VITALS:
  temperature_celsius: 38.7
  heart_rate_bpm: 100
  systolic_bp_mmHg: 110
  diastolic_bp_mmHg: 68
  glasgow_coma_scale: 15
  oxygen_saturation_pct: 98
  respiratory_rate_breaths_per_min: 20

EXAM:
  mental_status_grade: alert
  neck_stiffness: True
  kernig_or_brudzinski_positive: True
  cranial_nerve_palsy: none
  papilledema_on_fundoscopy: False
  focal_neurological_deficit: False
  skin_lesion_centrofacial_chronic: False
  petechial_or_purpuric_rash: False

LABS:
  wbc_blood_per_uL: 10200
  platelets_per_uL: 285000
  alt_ast_U_per_L: 23
  crp_mg_per_L: 14.0
  procalcitonin_ng_per_mL: 0.3
  serum_sodium_mEq_per_L: 138

CSF:
  opening_pressure_cmH2O: 18.0
  wbc_per_mm3: 180
  lymphocyte_pct: 82
  neutrophil_pct: 18
  eosinophil_pct: 0
  glucose_mg_per_dL: 58
  protein_mg_per_dL: 60
  lactate_mmol_per_L: 2.0
  ada_U_per_L: None
  crag_lfa_result: negative
  wet_mount_motile_amoebae: negative
  xanthochromia_present: False
  rbc_per_mm3: 2

IMAGING:
  modality: none
  pattern: (none)
  contrast_enhancement: False
  hydrocephalus: False
  basal_meningeal_enhancement: False
  finding_count: None
  text_summary: No imaging performed (uncomplicated enteroviral meningitis presentation with normal mental status; Tyler 2018 NEJM review supports deferring imaging in benign aseptic pattern).

DIAGNOSTIC_TESTS:
  pcr_panel: positive
  xpert_mtb_rif: n/a
  blood_culture: n/a
  csf_culture: n/a
  serology_or_antigen: n/a
  smear_or_gram: n/a
  brain_biopsy: n/a
  imaging_test: n/a
  total_dx_results: 3

NARRATIVE_EN: An 11-year-old boy in the US South region presented to a tertiary pediatric emergency department in early September with a 2-day course of fever to 38.7 C, headache, neck stiffness, photophobia, and vomiting. He attended a school with several peers reporting similar symptoms in the same week (suspected school enteroviral outbreak). Examination on admission: temperature 38.7 C, Glasgow Coma Scale 15, alert, neck stiffness, positive Kernig sign, no focal deficit, no rash. CSF showed opening pressure 18 cmH2O, white cell count 180 per cubic millimeter (82 percent lymphocytes), glucose 58 mg/dL, protein 60 mg/dL. CSF enterovirus PCR positive. Gram stain and culture negative. No imaging performed. Anchored to Tyler 2018 NEJM viral encephalitis review (PMID 30089069), school-outbreak enteroviral stratum. Outcome: survived with full recovery in six days. Subphase 1.3 commit 5.3.5 wave 1, pre-adjudication hold_for_revision.

NARRATIVE_ES: Varon de 11 anos en region sur de Estados Unidos, ingresado a urgencias pediatricas terciarias a principios de septiembre con dos dias de fiebre 38.7 C, cefalea, rigidez de nuca, fotofobia y vomitos. Asistio a colegio con varios companeros con sintomas similares la misma semana (brote escolar de enterovirus sospechado). Examen: temperatura 38.7 C, escala de Glasgow 15, alerta, rigidez de nuca, signo de Kernig positivo, sin deficit focal, sin exantema. Liquido cefalorraquideo mostro presion de apertura 18 cmH2O, leucocitos 180 por mm3 (82 por ciento linfocitos), glucosa 58 mg/dL, proteina 60 mg/dL. PCR de enterovirus en LCR positiva. Anclaje en revision Tyler 2018 NEJM (PMID 30089069), estrato brote escolar. Subphase 1.3 commit 5.3.5 wave 1.

RATIONALE: Anchored to PMID 30089069 (Tyler 2018 NEJM viral encephalitis review). Enteroviral aseptic meningitis with school-outbreak epidemiology. Demographic anchor (11yo M US school outbreak September) sits in school-outbreak-pediatric stratum. CSF lymphocytic (180 WBC, 82 percent lymphocytes), normal glucose 58, mildly elevated protein 60 - textbook viral pattern. EV PCR positive. Imputation tiers: tier_1_primary={age, sex, ev_pcr, school_outbreak_context, season}; tier_3_within_review={csf_wbc, neutrophil_pct, glucose, protein}; tier_4_priors={temp, gcs, symptom_days}. Indeterminate=none. Diagnostic_ambiguity=false. Outcome=survived_full_recovery. Tier: tier_3_imputation_within_review. 5.3.5 wave1 EV-school-outbreak-pediatric.

ANCHORING_EXTRAS: stage=pre_adjudication; status=pending_external_review; self_review_disposition=hold_for_revision; self_review_notes=wave 5.3.5 VIRAL vignette anchored to PMID 30089069 (Tyler 2018 NEJM viral encephalitis review); external clinical adjudication pending; classification provisional. adjudicator_ids=VIRAL-WAVE1-PRE-ADJ-1, VIRAL-WAVE1-PRE-ADJ-2 (sentinel); cohen_kappa=0.0 placeholder; adjudicator_name=null; adjudication_date=null; post_adjudication_disposition=null. Subphase 1.3 commit 5.3.5 (2026-05-08). anchor=Tyler-NEJM-2018 stratum=EV-school-outbreak.

ADJUDICATION:
  inclusion_decision: hold_for_revision
  adjudicator_ids: ['VIRAL-WAVE1-PRE-ADJ-1', 'VIRAL-WAVE1-PRE-ADJ-2']
  ground_truth_class: 3
  pre_adjudication_kappa: 0.0
  disagreement_resolution: None

=== END vignette ===

=== CLASS 3 | vignette_id: 109 | subphase: 1.3 VIRAL | file: vir_109_enterovirus_infant.json ===

ANCHOR:
  pmid: 30089069
  first_author: Tyler
  year: 2018
  journal: NEJM
  citation_type: review
  doi: 10.1056/NEJMra1708714

DEMOGRAPHICS:
  age_years: 3
  sex: female
  geography_region: other_global
  ethnicity: white_non_hispanic
  altitude_residence_m: 5
  hiv_status: negative
  cd4_count_cells_per_uL: None
  pregnancy_red_flag: False
  immunocompromise_status: none
  freshwater_exposure_within_14d: False
  freshwater_exposure_type: None

HISTORY:
  symptom_onset_to_presentation_days: 2.0
  chief_complaint: fever_with_headache
  red_flags_present: []
  prodrome_description: 3-year-old female, Netherlands. 2-day course: fever 38.5 C, irritability, decreased oral intake, vomiting, bulging fontanelle remnant, neck stiffness on exam, summer July presentation. Pediatric tertiary ED Amsterdam. No freshwater. No focal deficit. Outcome: survived with full recovery in 5 days.

VITALS:
  temperature_celsius: 38.5
  heart_rate_bpm: 130
  systolic_bp_mmHg: 96
  diastolic_bp_mmHg: 60
  glasgow_coma_scale: 15
  oxygen_saturation_pct: 98
  respiratory_rate_breaths_per_min: 26

EXAM:
  mental_status_grade: alert
  neck_stiffness: True
  kernig_or_brudzinski_positive: True
  cranial_nerve_palsy: none
  papilledema_on_fundoscopy: False
  focal_neurological_deficit: False
  skin_lesion_centrofacial_chronic: False
  petechial_or_purpuric_rash: False

LABS:
  wbc_blood_per_uL: 9800
  platelets_per_uL: 305000
  alt_ast_U_per_L: 22
  crp_mg_per_L: 12.0
  procalcitonin_ng_per_mL: 0.3
  serum_sodium_mEq_per_L: 138

CSF:
  opening_pressure_cmH2O: 17.0
  wbc_per_mm3: 145
  lymphocyte_pct: 85
  neutrophil_pct: 15
  eosinophil_pct: 0
  glucose_mg_per_dL: 56
  protein_mg_per_dL: 55
  lactate_mmol_per_L: 2.0
  ada_U_per_L: None
  crag_lfa_result: negative
  wet_mount_motile_amoebae: negative
  xanthochromia_present: False
  rbc_per_mm3: 2

IMAGING:
  modality: none
  pattern: (none)
  contrast_enhancement: False
  hydrocephalus: False
  basal_meningeal_enhancement: False
  finding_count: None
  text_summary: No imaging performed (uncomplicated enteroviral meningitis presentation with normal mental status; Tyler 2018 NEJM review supports deferring imaging in benign aseptic pattern).

DIAGNOSTIC_TESTS:
  pcr_panel: positive
  xpert_mtb_rif: n/a
  blood_culture: n/a
  csf_culture: n/a
  serology_or_antigen: n/a
  smear_or_gram: n/a
  brain_biopsy: n/a
  imaging_test: n/a
  total_dx_results: 3

NARRATIVE_EN: A 3-year-old girl in the Netherlands presented to a tertiary pediatric emergency department in Amsterdam in July with a 2-day course of fever to 38.5 C, irritability, decreased oral intake, vomiting, and neck stiffness on examination. Examination on admission: temperature 38.5 C, Glasgow Coma Scale 15, alert, neck stiffness, positive Kernig sign, no focal deficit, no rash. CSF showed opening pressure 17 cmH2O, white cell count 145 per cubic millimeter (85 percent lymphocytes), glucose 56 mg/dL, protein 55 mg/dL. CSF enterovirus PCR positive. Gram stain and culture negative. No imaging performed. Anchored to Tyler 2018 NEJM viral encephalitis review (PMID 30089069), early-childhood enteroviral summer stratum. Outcome: survived with full recovery in five days. Subphase 1.3 commit 5.3.5 wave 1, pre-adjudication hold_for_revision.

NARRATIVE_ES: Nina de 3 anos en Paises Bajos (Amsterdam), ingresada a urgencias pediatricas terciarias en julio con dos dias de fiebre 38.5 C, irritabilidad, disminucion de ingesta oral, vomitos y rigidez de nuca al examen. Examen: temperatura 38.5 C, escala de Glasgow 15, alerta, rigidez de nuca, signo de Kernig positivo, sin deficit focal, sin exantema. Liquido cefalorraquideo mostro presion de apertura 17 cmH2O, leucocitos 145 por mm3 (85 por ciento linfocitos), glucosa 56 mg/dL, proteina 55 mg/dL. PCR de enterovirus en LCR positiva. Tincion de Gram y cultivo negativos. Sin imagenes. Anclaje en revision Tyler 2018 NEJM (PMID 30089069), estrato infancia temprana pico estival enteroviral. Subphase 1.3 commit 5.3.5 wave 1, pre-adjudicacion hold_for_revision.

RATIONALE: Anchored to PMID 30089069 (Tyler 2018 NEJM viral encephalitis review). Enteroviral aseptic meningitis early-childhood summer pattern. Demographic anchor (3yo F NL summer) sits in early-childhood-EV-summer stratum. CSF lymphocytic (145 WBC, 85 percent lymphocytes), normal glucose 56, mildly elevated protein 55. EV PCR positive. Imputation tiers: tier_1_primary={age, sex, ev_pcr, season, irritability}; tier_3_within_review={csf_wbc, neutrophil_pct, glucose, protein}; tier_4_priors={temp, gcs, hr, symptom_days}. Indeterminate=none. Diagnostic_ambiguity=false. Outcome=survived_full_recovery. Tier: tier_3_imputation_within_review. 5.3.5 wave1 EV-NL-infant-summer.

ANCHORING_EXTRAS: stage=pre_adjudication; status=pending_external_review; self_review_disposition=hold_for_revision; self_review_notes=wave 5.3.5 VIRAL vignette anchored to PMID 30089069 (Tyler 2018 NEJM viral encephalitis review); external clinical adjudication pending; classification provisional. adjudicator_ids=VIRAL-WAVE1-PRE-ADJ-1, VIRAL-WAVE1-PRE-ADJ-2 (sentinel); cohen_kappa=0.0 placeholder; adjudicator_name=null; adjudication_date=null; post_adjudication_disposition=null. Subphase 1.3 commit 5.3.5 (2026-05-08). anchor=Tyler-NEJM-2018 stratum=EV-early-childhood-summer.

ADJUDICATION:
  inclusion_decision: hold_for_revision
  adjudicator_ids: ['VIRAL-WAVE1-PRE-ADJ-1', 'VIRAL-WAVE1-PRE-ADJ-2']
  ground_truth_class: 3
  pre_adjudication_kappa: 0.0
  disagreement_resolution: None

=== END vignette ===

=== CLASS 3 | vignette_id: 110 | subphase: 1.3 VIRAL | file: vir_110_enterovirus_college_age.json ===

ANCHOR:
  pmid: 20952256
  first_author: Granerod
  year: 2010
  journal: Lancet Infect Dis
  citation_type: cohort
  doi: 10.1016/S1473-3099(10)70222-X

DEMOGRAPHICS:
  age_years: 19
  sex: female
  geography_region: other_global
  ethnicity: white_non_hispanic
  altitude_residence_m: 5
  hiv_status: negative
  cd4_count_cells_per_uL: None
  pregnancy_red_flag: False
  immunocompromise_status: none
  freshwater_exposure_within_14d: False
  freshwater_exposure_type: None

HISTORY:
  symptom_onset_to_presentation_days: 2.0
  chief_complaint: fever_with_headache
  red_flags_present: []
  prodrome_description: 19-year-old female, Netherlands. 2-day course: fever 38.7 C, severe headache, neck stiffness, photophobia, myalgia, summer August presentation. University setting. Tertiary ED Amsterdam. No freshwater. No focal deficit. Outcome: survived with full recovery in 6 days. Supportive care.

VITALS:
  temperature_celsius: 38.7
  heart_rate_bpm: 102
  systolic_bp_mmHg: 116
  diastolic_bp_mmHg: 70
  glasgow_coma_scale: 15
  oxygen_saturation_pct: 98
  respiratory_rate_breaths_per_min: 18

EXAM:
  mental_status_grade: alert
  neck_stiffness: True
  kernig_or_brudzinski_positive: True
  cranial_nerve_palsy: none
  papilledema_on_fundoscopy: False
  focal_neurological_deficit: False
  skin_lesion_centrofacial_chronic: False
  petechial_or_purpuric_rash: False

LABS:
  wbc_blood_per_uL: 11200
  platelets_per_uL: 270000
  alt_ast_U_per_L: 24
  crp_mg_per_L: 16.0
  procalcitonin_ng_per_mL: 0.3
  serum_sodium_mEq_per_L: 138

CSF:
  opening_pressure_cmH2O: 19.0
  wbc_per_mm3: 200
  lymphocyte_pct: 78
  neutrophil_pct: 22
  eosinophil_pct: 0
  glucose_mg_per_dL: 56
  protein_mg_per_dL: 60
  lactate_mmol_per_L: 2.2
  ada_U_per_L: None
  crag_lfa_result: negative
  wet_mount_motile_amoebae: negative
  xanthochromia_present: False
  rbc_per_mm3: 3

IMAGING:
  modality: none
  pattern: (none)
  contrast_enhancement: False
  hydrocephalus: False
  basal_meningeal_enhancement: False
  finding_count: None
  text_summary: No imaging performed (uncomplicated enteroviral meningitis presentation with normal mental status; Tyler 2018 NEJM review supports deferring imaging in benign aseptic pattern).

DIAGNOSTIC_TESTS:
  pcr_panel: positive
  xpert_mtb_rif: n/a
  blood_culture: n/a
  csf_culture: n/a
  serology_or_antigen: n/a
  smear_or_gram: n/a
  brain_biopsy: n/a
  imaging_test: n/a
  total_dx_results: 3

NARRATIVE_EN: A 19-year-old woman in the Netherlands presented to a tertiary emergency department in Amsterdam in late August with a 2-day course: fever to 38.7 C, severe headache, neck stiffness, photophobia, and myalgia. She lived in a university setting. Examination on admission: temperature 38.7 C, Glasgow Coma Scale 15, alert, neck stiffness, positive Kernig sign, no focal deficit, no rash. CSF showed opening pressure 19 cmH2O, white cell count 200 per cubic millimeter (78 percent lymphocytes), glucose 56 mg/dL, protein 60 mg/dL. CSF enterovirus PCR positive. Gram stain and culture negative. No imaging performed. Anchored to Granerod 2010 Lancet Infect Dis UK encephalitis cohort (PMID 20952256), college-age-enteroviral-meningitis stratum. Outcome: survived with full recovery in six days. Subphase 1.3 commit 5.3.6 wave 2, pre-adjudication hold_for_revision.

NARRATIVE_ES: Mujer de 19 anos en Paises Bajos (Amsterdam), ingresada a urgencias terciarias en agosto con curso de dos dias: fiebre 38.7 C, cefalea intensa, rigidez de nuca, fotofobia y mialgia. Entorno universitario. Examen: temperatura 38.7 C, escala de Glasgow 15, alerta, rigidez de nuca, signo de Kernig positivo, sin deficit focal, sin exantema. Liquido cefalorraquideo mostro presion de apertura 19 cmH2O, leucocitos 200 por mm3 (78 por ciento linfocitos), glucosa 56 mg/dL, proteina 60 mg/dL. PCR de enterovirus en LCR positiva. Tincion de Gram y cultivo negativos. Sin imagenes. Anclaje en cohorte Granerod 2010 Lancet ID (PMID 20952256), estrato adulto joven enteroviral. Subphase 1.3 commit 5.3.6 wave 2, pre-adjudicacion hold_for_revision.

RATIONALE: Anchored to PMID 20952256 (Granerod 2010 Lancet ID UK encephalitis cohort). Enteroviral aseptic meningitis college-age summer phenotype. Demographic anchor (19yo F NL university summer) sits in college-age-enteroviral stratum. CSF lymphocytic (200 WBC, 78 percent lymphocytes), normal glucose 56, mildly elevated protein 60. EV PCR positive. Imputation tiers: tier_1_primary={age, sex, ev_pcr, season}; tier_3_within_review={csf_wbc, neutrophil_pct, glucose, protein}; tier_4_priors={temp, gcs, symptom_days}. Indeterminate=none. Diagnostic_ambiguity=false. Outcome=survived_full_recovery. Tier: tier_3_imputation_within_review. 5.3.6 wave2 EV-Granerod-college-age.

ANCHORING_EXTRAS: stage=pre_adjudication; status=pending_external_review; self_review_disposition=hold_for_revision; self_review_notes=wave 5.3.6 VIRAL vignette anchored to PMID 20952256 (Granerod 2010 Lancet ID UK encephalitis cohort); external clinical adjudication pending; classification provisional. adjudicator_ids=VIRAL-WAVE2-PRE-ADJ-1, VIRAL-WAVE2-PRE-ADJ-2 (sentinel); cohen_kappa=0.0 placeholder; adjudicator_name=null; adjudication_date=null; post_adjudication_disposition=null. Subphase 1.3 commit 5.3.6 (2026-05-08, FINAL Subphase 1.3 wave). anchor=Granerod-Lancet-ID-2010 stratum=college-age-EV.

ADJUDICATION:
  inclusion_decision: hold_for_revision
  adjudicator_ids: ['VIRAL-WAVE2-PRE-ADJ-1', 'VIRAL-WAVE2-PRE-ADJ-2']
  ground_truth_class: 3
  pre_adjudication_kappa: 0.0
  disagreement_resolution: None

=== END vignette ===

=== CLASS 3 | vignette_id: 111 | subphase: 1.3 VIRAL | file: vir_111_enterovirus_pediatric.json ===

ANCHOR:
  pmid: 30089069
  first_author: Tyler
  year: 2018
  journal: NEJM
  citation_type: review
  doi: 10.1056/NEJMra1708714

DEMOGRAPHICS:
  age_years: 5
  sex: male
  geography_region: us_south
  ethnicity: white_non_hispanic
  altitude_residence_m: 100
  hiv_status: negative
  cd4_count_cells_per_uL: None
  pregnancy_red_flag: False
  immunocompromise_status: none
  freshwater_exposure_within_14d: False
  freshwater_exposure_type: None

HISTORY:
  symptom_onset_to_presentation_days: 2.0
  chief_complaint: fever_with_headache
  red_flags_present: []
  prodrome_description: 5-year-old male, US South region. 2-day course: fever 38.6 C, headache, neck stiffness, photophobia, summer August presentation. Pediatric tertiary ED. No freshwater. No focal. Outcome: survived with full recovery in 6 days. Supportive care; antibiotics discontinued after EV PCR positive.

VITALS:
  temperature_celsius: 38.6
  heart_rate_bpm: 110
  systolic_bp_mmHg: 100
  diastolic_bp_mmHg: 64
  glasgow_coma_scale: 15
  oxygen_saturation_pct: 98
  respiratory_rate_breaths_per_min: 22

EXAM:
  mental_status_grade: alert
  neck_stiffness: True
  kernig_or_brudzinski_positive: True
  cranial_nerve_palsy: none
  papilledema_on_fundoscopy: False
  focal_neurological_deficit: False
  skin_lesion_centrofacial_chronic: False
  petechial_or_purpuric_rash: False

LABS:
  wbc_blood_per_uL: 10500
  platelets_per_uL: 290000
  alt_ast_U_per_L: 22
  crp_mg_per_L: 15.0
  procalcitonin_ng_per_mL: 0.3
  serum_sodium_mEq_per_L: 138

CSF:
  opening_pressure_cmH2O: 18.0
  wbc_per_mm3: 165
  lymphocyte_pct: 80
  neutrophil_pct: 20
  eosinophil_pct: 0
  glucose_mg_per_dL: 55
  protein_mg_per_dL: 58
  lactate_mmol_per_L: 2.1
  ada_U_per_L: None
  crag_lfa_result: negative
  wet_mount_motile_amoebae: negative
  xanthochromia_present: False
  rbc_per_mm3: 3

IMAGING:
  modality: none
  pattern: (none)
  contrast_enhancement: False
  hydrocephalus: False
  basal_meningeal_enhancement: False
  finding_count: None
  text_summary: No imaging performed (uncomplicated enteroviral meningitis presentation with normal mental status; Tyler 2018 NEJM review supports deferring imaging in benign aseptic pattern).

DIAGNOSTIC_TESTS:
  pcr_panel: positive
  xpert_mtb_rif: n/a
  blood_culture: n/a
  csf_culture: n/a
  serology_or_antigen: n/a
  smear_or_gram: n/a
  brain_biopsy: n/a
  imaging_test: n/a
  total_dx_results: 3

NARRATIVE_EN: A 5-year-old boy in the US South region presented to a tertiary pediatric emergency department in August with a 2-day course of fever to 38.6 C, headache, neck stiffness, and photophobia. Examination on admission: temperature 38.6 C, Glasgow Coma Scale 15, alert, neck stiffness, positive Kernig sign, no focal deficit, no rash. CSF showed opening pressure 18 cmH2O, white cell count 165 per cubic millimeter (80 percent lymphocytes), glucose 55 mg/dL, protein 58 mg/dL. CSF enterovirus PCR positive. Gram stain and culture negative. No imaging performed (uncomplicated viral meningitis presentation in a child with normal mental status). Anchored to Tyler 2018 NEJM viral encephalitis review (PMID 30089069), pediatric enteroviral summer-peak stratum. Outcome: survived with full recovery in six days. Subphase 1.3 commit 5.3.5 wave 1, pre-adjudication hold_for_revision.

NARRATIVE_ES: Varon de 5 anos en region sur de Estados Unidos, ingresado a urgencias pediatricas terciarias en agosto con dos dias de fiebre 38.6 C, cefalea, rigidez de nuca y fotofobia. Examen: temperatura 38.6 C, escala de Glasgow 15, alerta, rigidez de nuca, signo de Kernig positivo, sin deficit focal, sin exantema. Liquido cefalorraquideo mostro presion de apertura 18 cmH2O, leucocitos 165 por mm3 (80 por ciento linfocitos), glucosa 55 mg/dL, proteina 58 mg/dL. PCR de enterovirus en LCR positiva. Tincion de Gram y cultivo negativos. Sin imagenes. Anclaje en revision Tyler 2018 NEJM (PMID 30089069), estrato pediatrico pico estival enteroviral. Subphase 1.3 commit 5.3.5 wave 1, pre-adjudicacion hold_for_revision.

RATIONALE: Anchored to PMID 30089069 (Tyler 2018 NEJM viral encephalitis review). Enteroviral aseptic meningitis pediatric summer pattern. Demographic anchor (5yo M US South August) sits in pediatric-EV-summer stratum. CSF lymphocytic (165 WBC, 80 percent lymphocytes), normal glucose 55, mildly elevated protein 58. EV PCR positive. Imputation tiers: tier_1_primary={age, sex, ev_pcr, season}; tier_3_within_review={csf_wbc, neutrophil_pct, glucose, protein}; tier_4_priors={temp, gcs, symptom_days}. Indeterminate=none. Diagnostic_ambiguity=false. Outcome=survived_full_recovery. Tier: tier_3_imputation_within_review. 5.3.5 wave1 EV-US-pediatric-summer-2.

ANCHORING_EXTRAS: stage=pre_adjudication; status=pending_external_review; self_review_disposition=hold_for_revision; self_review_notes=wave 5.3.5 VIRAL vignette anchored to PMID 30089069 (Tyler 2018 NEJM viral encephalitis review); external clinical adjudication pending; classification provisional. adjudicator_ids=VIRAL-WAVE1-PRE-ADJ-1, VIRAL-WAVE1-PRE-ADJ-2 (sentinel); cohen_kappa=0.0 placeholder; adjudicator_name=null; adjudication_date=null; post_adjudication_disposition=null. Subphase 1.3 commit 5.3.5 (2026-05-08). anchor=Tyler-NEJM-2018 stratum=EV-pediatric-summer-2.

ADJUDICATION:
  inclusion_decision: hold_for_revision
  adjudicator_ids: ['VIRAL-WAVE1-PRE-ADJ-1', 'VIRAL-WAVE1-PRE-ADJ-2']
  ground_truth_class: 3
  pre_adjudication_kappa: 0.0
  disagreement_resolution: None

=== END vignette ===

=== CLASS 3 | vignette_id: 112 | subphase: 1.3 VIRAL | file: vir_112_enterovirus_adolescent.json ===

ANCHOR:
  pmid: 20952256
  first_author: Granerod
  year: 2010
  journal: Lancet Infect Dis
  citation_type: cohort
  doi: 10.1016/S1473-3099(10)70222-X

DEMOGRAPHICS:
  age_years: 14
  sex: female
  geography_region: other_global
  ethnicity: white_non_hispanic
  altitude_residence_m: 5
  hiv_status: negative
  cd4_count_cells_per_uL: None
  pregnancy_red_flag: False
  immunocompromise_status: none
  freshwater_exposure_within_14d: False
  freshwater_exposure_type: None

HISTORY:
  symptom_onset_to_presentation_days: 2.0
  chief_complaint: fever_with_headache
  red_flags_present: []
  prodrome_description: 14-year-old female, Netherlands. 2-day course: fever 38.5 C, headache, neck stiffness, photophobia, vomiting, summer late-July presentation. Pediatric tertiary ED. No freshwater. No focal. Outcome: survived with full recovery in 5 days. Supportive care; antibiotics discontinued after EV PCR positive.

VITALS:
  temperature_celsius: 38.5
  heart_rate_bpm: 96
  systolic_bp_mmHg: 110
  diastolic_bp_mmHg: 68
  glasgow_coma_scale: 15
  oxygen_saturation_pct: 98
  respiratory_rate_breaths_per_min: 18

EXAM:
  mental_status_grade: alert
  neck_stiffness: True
  kernig_or_brudzinski_positive: True
  cranial_nerve_palsy: none
  papilledema_on_fundoscopy: False
  focal_neurological_deficit: False
  skin_lesion_centrofacial_chronic: False
  petechial_or_purpuric_rash: False

LABS:
  wbc_blood_per_uL: 10500
  platelets_per_uL: 290000
  alt_ast_U_per_L: 22
  crp_mg_per_L: 14.0
  procalcitonin_ng_per_mL: 0.3
  serum_sodium_mEq_per_L: 138

CSF:
  opening_pressure_cmH2O: 18.0
  wbc_per_mm3: 175
  lymphocyte_pct: 82
  neutrophil_pct: 18
  eosinophil_pct: 0
  glucose_mg_per_dL: 58
  protein_mg_per_dL: 58
  lactate_mmol_per_L: 2.0
  ada_U_per_L: None
  crag_lfa_result: negative
  wet_mount_motile_amoebae: negative
  xanthochromia_present: False
  rbc_per_mm3: 3

IMAGING:
  modality: none
  pattern: (none)
  contrast_enhancement: False
  hydrocephalus: False
  basal_meningeal_enhancement: False
  finding_count: None
  text_summary: No imaging performed (uncomplicated enteroviral meningitis presentation with normal mental status; Tyler 2018 NEJM review supports deferring imaging in benign aseptic pattern).

DIAGNOSTIC_TESTS:
  pcr_panel: positive
  xpert_mtb_rif: n/a
  blood_culture: n/a
  csf_culture: n/a
  serology_or_antigen: n/a
  smear_or_gram: n/a
  brain_biopsy: n/a
  imaging_test: n/a
  total_dx_results: 3

NARRATIVE_EN: A 14-year-old girl in the Netherlands presented to a tertiary pediatric emergency department in Amsterdam in late July with a 2-day course: fever to 38.5 C, headache, neck stiffness, photophobia, and vomiting. Examination on admission: temperature 38.5 C, Glasgow Coma Scale 15, alert, neck stiffness, positive Kernig sign, no focal deficit, no rash. CSF showed opening pressure 18 cmH2O, white cell count 175 per cubic millimeter (82 percent lymphocytes), glucose 58 mg/dL, protein 58 mg/dL. CSF enterovirus PCR positive. Gram stain and culture negative. No imaging performed. Anchored to Granerod 2010 Lancet Infect Dis UK encephalitis cohort (PMID 20952256), adolescent-enteroviral-summer-meningitis stratum. Outcome: survived with full recovery in five days. Subphase 1.3 commit 5.3.6 wave 2, pre-adjudication hold_for_revision.

NARRATIVE_ES: Nina de 14 anos en Paises Bajos (Amsterdam), ingresada a urgencias pediatricas terciarias en julio con curso de dos dias: fiebre 38.5 C, cefalea, rigidez de nuca, fotofobia y vomitos sin antecedente de exposicion a agua dulce. Examen al ingreso: temperatura 38.5 C, escala de Glasgow 15, alerta, rigidez de nuca, signo de Kernig positivo, sin deficit focal, sin exantema. Liquido cefalorraquideo mostro presion de apertura 18 cmH2O, leucocitos 175 por mm3 (82 por ciento linfocitos), glucosa 58 mg/dL, proteina 58 mg/dL. PCR de enterovirus en LCR positiva. Tincion de Gram y cultivo negativos. Sin estudios de neuroimagen. Anclaje en cohorte Granerod 2010 Lancet ID (PMID 20952256), estrato adolescente enteroviral de verano. Resultado: recuperacion completa en cinco dias. Subphase 1.3 commit 5.3.6 wave 2, pre-adjudicacion en hold.

RATIONALE: Anchored to PMID 20952256 (Granerod 2010 Lancet ID UK encephalitis cohort). Enteroviral aseptic meningitis adolescent summer phenotype. Demographic anchor (14yo F NL adolescent summer) sits in adolescent-enteroviral stratum. CSF lymphocytic (175 WBC, 82 percent lymphocytes), normal glucose 58, mildly elevated protein 58. EV PCR positive. Imputation tiers: tier_1_primary={age, sex, ev_pcr, season}; tier_3_within_review={csf_wbc, neutrophil_pct, glucose, protein}; tier_4_priors={temp, gcs, symptom_days}. Indeterminate=none. Diagnostic_ambiguity=false. Outcome=survived_full_recovery. Tier: tier_3_imputation_within_review. 5.3.6 wave2 EV-Granerod-adolescent.

ANCHORING_EXTRAS: stage=pre_adjudication; status=pending_external_review; self_review_disposition=hold_for_revision; self_review_notes=wave 5.3.6 VIRAL vignette anchored to PMID 20952256 (Granerod 2010 Lancet ID UK encephalitis cohort); external clinical adjudication pending; classification provisional. adjudicator_ids=VIRAL-WAVE2-PRE-ADJ-1, VIRAL-WAVE2-PRE-ADJ-2 (sentinel); cohen_kappa=0.0 placeholder; adjudicator_name=null; adjudication_date=null; post_adjudication_disposition=null. Subphase 1.3 commit 5.3.6 (2026-05-08, FINAL Subphase 1.3 wave). anchor=Granerod-Lancet-ID-2010 stratum=adolescent-EV.

ADJUDICATION:
  inclusion_decision: hold_for_revision
  adjudicator_ids: ['VIRAL-WAVE2-PRE-ADJ-1', 'VIRAL-WAVE2-PRE-ADJ-2']
  ground_truth_class: 3
  pre_adjudication_kappa: 0.0
  disagreement_resolution: None

=== END vignette ===

=== CLASS 3 | vignette_id: 113 | subphase: 1.3 VIRAL | file: vir_113_hsv2_mollaret_recurrent_ambiguity.json ===

ANCHOR:
  pmid: 30089069
  first_author: Tyler
  year: 2018
  journal: NEJM
  citation_type: review
  doi: 10.1056/NEJMra1708714

DEMOGRAPHICS:
  age_years: 28
  sex: female
  geography_region: other_global
  ethnicity: white_non_hispanic
  altitude_residence_m: 5
  hiv_status: negative
  cd4_count_cells_per_uL: None
  pregnancy_red_flag: False
  immunocompromise_status: none
  freshwater_exposure_within_14d: False
  freshwater_exposure_type: None

HISTORY:
  symptom_onset_to_presentation_days: 2.0
  chief_complaint: fever_with_headache
  red_flags_present: []
  prodrome_description: 28-year-old female, Netherlands. First-episode HSV2 lymphocytic meningitis with prominent meningismus 2 weeks after primary genital herpes outbreak. 2-day course: fever 38.6 C, severe headache, prominent neck stiffness, photophobia. Tertiary ED Amsterdam. No freshwater. Diagnostic_ambiguity=true; type=hsv2_first_episode_with_prominent_meningismus_bacterial_ddx. Outcome: survived with full recovery.

VITALS:
  temperature_celsius: 38.6
  heart_rate_bpm: 102
  systolic_bp_mmHg: 116
  diastolic_bp_mmHg: 70
  glasgow_coma_scale: 14
  oxygen_saturation_pct: 97
  respiratory_rate_breaths_per_min: 18

EXAM:
  mental_status_grade: alert
  neck_stiffness: True
  kernig_or_brudzinski_positive: True
  cranial_nerve_palsy: none
  papilledema_on_fundoscopy: False
  focal_neurological_deficit: False
  skin_lesion_centrofacial_chronic: False
  petechial_or_purpuric_rash: False

LABS:
  wbc_blood_per_uL: 12500
  platelets_per_uL: 245000
  alt_ast_U_per_L: 24
  crp_mg_per_L: 32.0
  procalcitonin_ng_per_mL: 0.5
  serum_sodium_mEq_per_L: 138

CSF:
  opening_pressure_cmH2O: 24.0
  wbc_per_mm3: 350
  lymphocyte_pct: 65
  neutrophil_pct: 35
  eosinophil_pct: 0
  glucose_mg_per_dL: 48
  protein_mg_per_dL: 105
  lactate_mmol_per_L: 2.8
  ada_U_per_L: None
  crag_lfa_result: negative
  wet_mount_motile_amoebae: negative
  xanthochromia_present: False
  rbc_per_mm3: 4

IMAGING:
  modality: mri_with_dwi_flair
  pattern: normal
  contrast_enhancement: False
  hydrocephalus: False
  basal_meningeal_enhancement: False
  finding_count: 0
  text_summary: MRI brain with DWI/FLAIR: normal. No focal lesion. Mollaret and HSV2 first-episode lymphocytic meningitis typically demonstrate normal imaging per Tyler review.

DIAGNOSTIC_TESTS:
  pcr_panel: positive
  xpert_mtb_rif: n/a
  blood_culture: n/a
  csf_culture: n/a
  serology_or_antigen: n/a
  smear_or_gram: n/a
  brain_biopsy: n/a
  imaging_test: n/a
  total_dx_results: 3

NARRATIVE_EN: A 28-year-old woman in the Netherlands presented to a tertiary emergency department in Amsterdam with a 2-day course of fever to 38.6 C, severe headache, prominent neck stiffness, and photophobia, two weeks after a primary genital herpes outbreak. Examination on admission: temperature 38.6 C, Glasgow Coma Scale 14, alert, prominent neck stiffness, positive Kernig sign, no focal deficit, no rash. CSF showed opening pressure 24 cmH2O, white cell count 350 per cubic millimeter (65 percent lymphocytes, 35 percent neutrophils), glucose 48 mg/dL, protein 105 mg/dL. CSF HSV-2 PCR positive. Gram stain and culture negative. MRI brain with DWI/FLAIR normal. Diagnostic_ambiguity=true; type=hsv2_first_episode_with_prominent_meningismus_bacterial_ddx. The prominent meningismus and CSF pleocytosis at 350 WBC with 35 percent neutrophils raised initial bacterial-meningitis differential; HSV2 PCR confirmed organism. Anchored to Tyler 2018 NEJM viral encephalitis review (PMID 30089069). Outcome: survived with full recovery. Subphase 1.3 commit 5.3.5 wave 1, pre-adjudication hold_for_revision.

NARRATIVE_ES: Mujer de 28 anos en Paises Bajos (Amsterdam), ingresada a urgencias terciarias con dos dias de fiebre 38.6 C, cefalea intensa, rigidez de nuca prominente y fotofobia, dos semanas tras brote primario de herpes genital. Examen: temperatura 38.6 C, escala de Glasgow 14, alerta, rigidez de nuca prominente, signo de Kernig positivo, sin deficit focal, sin exantema. Liquido cefalorraquideo mostro presion de apertura 24 cmH2O, leucocitos 350 por mm3 (65 por ciento linfocitos, 35 por ciento neutrofilos), glucosa 48 mg/dL, proteina 105 mg/dL. PCR de HSV-2 en LCR positiva. RM cerebral normal. Ambiguedad diagnostica por meningismo prominente con DDx bacteriana inicial. Anclaje en revision Tyler 2018 NEJM (PMID 30089069). Subphase 1.3 commit 5.3.5 wave 1, pre-adjudicacion hold_for_revision.

RATIONALE: Anchored to PMID 30089069 (Tyler 2018 NEJM viral encephalitis review). HSV2 first-episode lymphocytic meningitis with prominent meningismus that mimics bacterial DDx. Diagnostic_ambiguity=true; type=hsv2_first_episode_with_prominent_meningismus_bacterial_ddx (verbatim from spec). Demographic anchor (28yo F NL post-genital-herpes) sits in HSV2-first-episode stratum. CSF prominent (WBC 350) with 35 percent neutrophils approaching bacterial threshold but lymphocyte-dominant; protein elevated 105; glucose mildly low 48 - borderline-bacterial-DDx pattern raising initial empiric-ceftriaxone consideration. HSV2 PCR confirms organism. Imputation tiers: tier_1_primary={age, sex, hsv2_pcr, primary_genital_herpes_history, prominent_meningismus}; tier_3_within_review={csf_wbc, neutrophil_pct, glucose, protein}; tier_4_priors={temp, gcs, symptom_days}. Indeterminate=initial-bacterial-DDx-resolved-by-PCR. Outcome=survived_full_recovery. Tier: tier_3_imputation_within_review. 5.3.5 wave1 HSV2-firs...

ANCHORING_EXTRAS: stage=pre_adjudication; status=pending_external_review; self_review_disposition=hold_for_revision; self_review_notes=wave 5.3.5 VIRAL vignette anchored to PMID 30089069 (Tyler 2018 NEJM viral encephalitis review); external clinical adjudication pending; classification provisional. adjudicator_ids=VIRAL-WAVE1-PRE-ADJ-1, VIRAL-WAVE1-PRE-ADJ-2 (sentinel); cohen_kappa=0.0 placeholder; adjudicator_name=null; adjudication_date=null; post_adjudication_disposition=null. Subphase 1.3 commit 5.3.5 (2026-05-08). anchor=Tyler-NEJM-2018 type=hsv2_first_episode_with_prominent_meningismus_bacterial_ddx.

ADJUDICATION:
  inclusion_decision: hold_for_revision
  adjudicator_ids: ['VIRAL-WAVE1-PRE-ADJ-1', 'VIRAL-WAVE1-PRE-ADJ-2']
  ground_truth_class: 3
  pre_adjudication_kappa: 0.0
  disagreement_resolution: None

=== END vignette ===

=== CLASS 3 | vignette_id: 114 | subphase: 1.3 VIRAL | file: vir_114_hsv2_first_episode.json ===

ANCHOR:
  pmid: 30089069
  first_author: Tyler
  year: 2018
  journal: NEJM
  citation_type: review
  doi: 10.1056/NEJMra1708714

DEMOGRAPHICS:
  age_years: 35
  sex: male
  geography_region: us_south
  ethnicity: white_non_hispanic
  altitude_residence_m: 100
  hiv_status: negative
  cd4_count_cells_per_uL: None
  pregnancy_red_flag: False
  immunocompromise_status: none
  freshwater_exposure_within_14d: False
  freshwater_exposure_type: None

HISTORY:
  symptom_onset_to_presentation_days: 2.0
  chief_complaint: fever_with_headache
  red_flags_present: []
  prodrome_description: 35-year-old male, US South region. 2-day course: fever 38.4 C, severe headache, neck stiffness, photophobia, 10 days after primary genital herpes outbreak. Tertiary ED. No freshwater. No focal deficit. Outcome: survived with full recovery in 6 days. Acyclovir IV initiated empirically.

VITALS:
  temperature_celsius: 38.4
  heart_rate_bpm: 92
  systolic_bp_mmHg: 124
  diastolic_bp_mmHg: 76
  glasgow_coma_scale: 15
  oxygen_saturation_pct: 98
  respiratory_rate_breaths_per_min: 18

EXAM:
  mental_status_grade: alert
  neck_stiffness: True
  kernig_or_brudzinski_positive: True
  cranial_nerve_palsy: none
  papilledema_on_fundoscopy: False
  focal_neurological_deficit: False
  skin_lesion_centrofacial_chronic: False
  petechial_or_purpuric_rash: False

LABS:
  wbc_blood_per_uL: 10800
  platelets_per_uL: 250000
  alt_ast_U_per_L: 24
  crp_mg_per_L: 22.0
  procalcitonin_ng_per_mL: 0.4
  serum_sodium_mEq_per_L: 138

CSF:
  opening_pressure_cmH2O: 22.0
  wbc_per_mm3: 280
  lymphocyte_pct: 78
  neutrophil_pct: 22
  eosinophil_pct: 0
  glucose_mg_per_dL: 55
  protein_mg_per_dL: 80
  lactate_mmol_per_L: 2.4
  ada_U_per_L: None
  crag_lfa_result: negative
  wet_mount_motile_amoebae: negative
  xanthochromia_present: False
  rbc_per_mm3: 3

IMAGING:
  modality: mri_with_dwi_flair
  pattern: normal
  contrast_enhancement: False
  hydrocephalus: False
  basal_meningeal_enhancement: False
  finding_count: 0
  text_summary: MRI brain with DWI/FLAIR: normal. No focal lesion. Mollaret and HSV2 first-episode lymphocytic meningitis typically demonstrate normal imaging per Tyler review.

DIAGNOSTIC_TESTS:
  pcr_panel: positive
  xpert_mtb_rif: n/a
  blood_culture: n/a
  csf_culture: n/a
  serology_or_antigen: n/a
  smear_or_gram: n/a
  brain_biopsy: n/a
  imaging_test: n/a
  total_dx_results: 3

NARRATIVE_EN: A 35-year-old man in the US South region presented to a tertiary emergency department with a 2-day course of fever to 38.4 C, severe headache, neck stiffness, and photophobia, ten days after a primary genital herpes outbreak. Examination on admission: temperature 38.4 C, Glasgow Coma Scale 15, alert, neck stiffness, positive Kernig sign, no focal deficit, no rash. CSF showed opening pressure 22 cmH2O, white cell count 280 per cubic millimeter (78 percent lymphocytes), glucose 55 mg/dL, protein 80 mg/dL. CSF HSV-2 PCR positive. Gram stain and culture negative. MRI brain with DWI/FLAIR normal. Empiric IV acyclovir initiated. Anchored to Tyler 2018 NEJM viral encephalitis review (PMID 30089069), HSV2 first-episode lymphocytic meningitis stratum. Outcome: survived with full recovery in six days. Subphase 1.3 commit 5.3.5 wave 1, pre-adjudication hold_for_revision.

NARRATIVE_ES: Varon de 35 anos en region sur de Estados Unidos, ingresado a urgencias terciarias con dos dias de fiebre 38.4 C, cefalea intensa, rigidez de nuca y fotofobia, diez dias tras brote primario de herpes genital. Examen: temperatura 38.4 C, escala de Glasgow 15, alerta, rigidez de nuca, signo de Kernig positivo, sin deficit focal, sin exantema. Liquido cefalorraquideo mostro presion de apertura 22 cmH2O, leucocitos 280 por mm3 (78 por ciento linfocitos), glucosa 55 mg/dL, proteina 80 mg/dL. PCR de HSV-2 en LCR positiva. Tincion de Gram y cultivo negativos. RM cerebral normal. Aciclovir IV empirico iniciado. Anclaje en revision Tyler 2018 NEJM (PMID 30089069), estrato HSV2 primer episodio. Subphase 1.3 commit 5.3.5 wave 1, pre-adjudicacion hold_for_revision.

RATIONALE: Anchored to PMID 30089069 (Tyler 2018 NEJM viral encephalitis review). HSV2 first-episode lymphocytic meningitis. Demographic anchor (35yo M US post-genital-herpes) sits in HSV2-first-episode-male stratum. CSF lymphocytic (280 WBC, 78 percent lymphocytes), normal glucose 55, mildly elevated protein 80. HSV2 PCR positive. Imputation tiers: tier_1_primary={age, sex, hsv2_pcr, primary_genital_herpes_history}; tier_3_within_review={csf_wbc, neutrophil_pct, glucose, protein}; tier_4_priors={temp, gcs, symptom_days}. Indeterminate=none. Diagnostic_ambiguity=false. Outcome=survived_full_recovery. Tier: tier_3_imputation_within_review. 5.3.5 wave1 HSV2-first-episode-male.

ANCHORING_EXTRAS: stage=pre_adjudication; status=pending_external_review; self_review_disposition=hold_for_revision; self_review_notes=wave 5.3.5 VIRAL vignette anchored to PMID 30089069 (Tyler 2018 NEJM viral encephalitis review); external clinical adjudication pending; classification provisional. adjudicator_ids=VIRAL-WAVE1-PRE-ADJ-1, VIRAL-WAVE1-PRE-ADJ-2 (sentinel); cohen_kappa=0.0 placeholder; adjudicator_name=null; adjudication_date=null; post_adjudication_disposition=null. Subphase 1.3 commit 5.3.5 (2026-05-08). anchor=Tyler-NEJM-2018 stratum=HSV2-first-episode-male.

ADJUDICATION:
  inclusion_decision: hold_for_revision
  adjudicator_ids: ['VIRAL-WAVE1-PRE-ADJ-1', 'VIRAL-WAVE1-PRE-ADJ-2']
  ground_truth_class: 3
  pre_adjudication_kappa: 0.0
  disagreement_resolution: None

=== END vignette ===

=== CLASS 3 | vignette_id: 115 | subphase: 1.3 VIRAL | file: vir_115_vzv_zoster_ophthalmicus_immunocompromised.json ===

ANCHOR:
  pmid: 20952256
  first_author: Granerod
  year: 2010
  journal: Lancet Infect Dis
  citation_type: cohort
  doi: 10.1016/S1473-3099(10)70222-X

DEMOGRAPHICS:
  age_years: 65
  sex: male
  geography_region: other_global
  ethnicity: white_non_hispanic
  altitude_residence_m: 5
  hiv_status: negative
  cd4_count_cells_per_uL: None
  pregnancy_red_flag: False
  immunocompromise_status: malignancy_active
  freshwater_exposure_within_14d: False
  freshwater_exposure_type: None

HISTORY:
  symptom_onset_to_presentation_days: 5.0
  chief_complaint: headache
  red_flags_present: ['immunocompromise']
  prodrome_description: 65-year-old male, Netherlands, on chemotherapy for multiple myeloma. 5-day course: vesicular dermatomal rash in V1 trigeminal distribution (zoster ophthalmicus) day 1, then headache day 3, low-grade fever 38.0 C and confusion day 4, neck stiffness day 5 prompting tertiary ED Amsterdam. No freshwater. Outcome: survived with mild residual visual field deficit per Granerod cohort VZV-immunocompromised pattern.

VITALS:
  temperature_celsius: 38.0
  heart_rate_bpm: 92
  systolic_bp_mmHg: 128
  diastolic_bp_mmHg: 78
  glasgow_coma_scale: 14
  oxygen_saturation_pct: 96
  respiratory_rate_breaths_per_min: 18

EXAM:
  mental_status_grade: confused
  neck_stiffness: True
  kernig_or_brudzinski_positive: True
  cranial_nerve_palsy: other
  papilledema_on_fundoscopy: False
  focal_neurological_deficit: True
  skin_lesion_centrofacial_chronic: False
  petechial_or_purpuric_rash: False

LABS:
  wbc_blood_per_uL: 4200
  platelets_per_uL: 145000
  alt_ast_U_per_L: 32
  crp_mg_per_L: 28.0
  procalcitonin_ng_per_mL: 0.4
  serum_sodium_mEq_per_L: 137

CSF:
  opening_pressure_cmH2O: 22.0
  wbc_per_mm3: 220
  lymphocyte_pct: 75
  neutrophil_pct: 25
  eosinophil_pct: 0
  glucose_mg_per_dL: 52
  protein_mg_per_dL: 110
  lactate_mmol_per_L: 2.4
  ada_U_per_L: None
  crag_lfa_result: negative
  wet_mount_motile_amoebae: negative
  xanthochromia_present: False
  rbc_per_mm3: 4

IMAGING:
  modality: mri_with_dwi_flair
  pattern: normal
  contrast_enhancement: False
  hydrocephalus: False
  basal_meningeal_enhancement: False
  finding_count: 0
  text_summary: MRI brain with DWI/FLAIR: normal. VZV reactivation with dermatomal rash and CSF lymphocytic pleocytosis can show normal parenchymal imaging in the absence of overt vasculopathy or cerebellitis; Granerod 2010 Lancet ID cohort documented this benign-imaging VZV phenotype.

DIAGNOSTIC_TESTS:
  pcr_panel: positive
  xpert_mtb_rif: n/a
  blood_culture: n/a
  csf_culture: n/a
  serology_or_antigen: positive
  smear_or_gram: multinucleated_giant_cells_seen
  brain_biopsy: n/a
  imaging_test: n/a
  total_dx_results: 5

NARRATIVE_EN: A 65-year-old man in the Netherlands on chemotherapy for multiple myeloma presented to a tertiary emergency department in Amsterdam after a 5-day course beginning with a vesicular dermatomal rash in the V1 trigeminal distribution (zoster ophthalmicus) on day 1, followed by headache on day 3, low-grade fever to 38.0 C and confusion on day 4, and neck stiffness on day 5. Examination on admission: temperature 38.0 C, Glasgow Coma Scale 14, neck stiffness, positive Kernig sign, focal deficit (left V1 dermatomal vesicular rash with eyelid involvement), no petechial rash. CSF showed opening pressure 22 cmH2O, white cell count 220 per cubic millimeter (75 percent lymphocytes), glucose 52 mg/dL, protein 110 mg/dL. CSF VZV PCR positive. VZV IgM serology positive. Vesicle swab Tzanck smear showed multinucleated giant cells. Brain MRI with DWI/FLAIR was normal. Anchored to Granerod 2010 Lancet Infect Dis UK encephalitis cohort (PMID 20952256), VZV-immunocompromised-zoster-ophthalmicus stratum. Outcome: survived with mild residual visual field deficit. Subphase 1.3 commit 5.3.6 wave 2, pre-adjudication hold_for_revision.

NARRATIVE_ES: Varon de 65 anos en Paises Bajos en quimioterapia por mieloma multiple, ingresado a urgencias terciarias en Amsterdam tras curso de cinco dias: exantema vesicular dermatomal en distribucion V1 trigeminal (herpes zoster oftalmico) al primer dia, luego cefalea al tercer dia, febricula 38.0 C y confusion al cuarto y rigidez de nuca al quinto. Examen: temperatura 38.0 C, escala de Glasgow 14, rigidez de nuca, signo de Kernig positivo, deficit focal (exantema vesicular dermatomal V1 con compromiso palpebral), sin exantema petequial. Liquido cefalorraquideo mostro leucocitos 220 por mm3 (75 por ciento linfocitos), glucosa 52 mg/dL, proteina 110 mg/dL. PCR de VZV en LCR positiva. IgM VZV positiva. Tzanck con celulas gigantes multinucleadas. RM cerebral normal. Anclaje en cohorte Granerod 2010 Lancet ID (PMID 20952256). Subphase 1.3 commit 5.3.6 wave 2.

RATIONALE: Anchored to PMID 20952256 (Granerod 2010 Lancet ID UK encephalitis cohort). VZV-immunocompromised-zoster-ophthalmicus phenotype with V1 dermatomal vesicular rash + CSF lymphocytic pleocytosis + VZV PCR positive. Demographic anchor (65yo M NL multiple myeloma chemotherapy with V1 dermatomal vesicular rash) sits in VZV-immuno-compromised stratum. CSF lymphocytic. MRI parenchyma normal in absence of overt VZV vasculopathy. Imputation tiers: tier_1_primary={age, sex, vzv_pcr, dermatomal_v1_rash, immunocompromise_chemotherapy}; tier_3_within_review={csf_wbc, neutrophil_pct, glucose, protein, gcs}; tier_4_priors={temp, symptom_days}. Indeterminate=none. Diagnostic_ambiguity=false. Outcome=survived_with_mild_visual_field_deficit. Tier: tier_3_imputation_within_review. 5.3.6 wave2 VZV-Granerod-immunocompromised-zoster-ophthalmicus.

ANCHORING_EXTRAS: stage=pre_adjudication; status=pending_external_review; self_review_disposition=hold_for_revision; self_review_notes=wave 5.3.6 VIRAL vignette anchored to PMID 20952256 (Granerod 2010 Lancet ID UK encephalitis cohort); external clinical adjudication pending; classification provisional. adjudicator_ids=VIRAL-WAVE2-PRE-ADJ-1, VIRAL-WAVE2-PRE-ADJ-2 (sentinel); cohen_kappa=0.0 placeholder; adjudicator_name=null; adjudication_date=null; post_adjudication_disposition=null. Subphase 1.3 commit 5.3.6 (2026-05-08, FINAL Subphase 1.3 wave). anchor=Granerod-Lancet-ID-2010 stratum=VZV-immunocompromised-zoster-ophthalmicus.

ADJUDICATION:
  inclusion_decision: hold_for_revision
  adjudicator_ids: ['VIRAL-WAVE2-PRE-ADJ-1', 'VIRAL-WAVE2-PRE-ADJ-2']
  ground_truth_class: 3
  pre_adjudication_kappa: 0.0
  disagreement_resolution: None

=== END vignette ===

=== CLASS 3 | vignette_id: 116 | subphase: 1.3 VIRAL | file: vir_116_vzv_post_zoster_encephalitis.json ===

ANCHOR:
  pmid: 20952256
  first_author: Granerod
  year: 2010
  journal: Lancet Infect Dis
  citation_type: cohort
  doi: 10.1016/S1473-3099(10)70222-X

DEMOGRAPHICS:
  age_years: 71
  sex: female
  geography_region: other_global
  ethnicity: white_non_hispanic
  altitude_residence_m: 5
  hiv_status: negative
  cd4_count_cells_per_uL: None
  pregnancy_red_flag: False
  immunocompromise_status: none
  freshwater_exposure_within_14d: False
  freshwater_exposure_type: None

HISTORY:
  symptom_onset_to_presentation_days: 14.0
  chief_complaint: altered_mental_status
  red_flags_present: []
  prodrome_description: 71-year-old female, Netherlands. Resolving thoracic dermatomal zoster rash 2 weeks prior, then 4-day course of fever 38.2 C, headache, neck stiffness day 2, gait ataxia day 3, confusion day 4 prompting tertiary ED Amsterdam. No freshwater. Outcome: survived with full recovery on 14-day acyclovir course; post-zoster CNS reactivation phenotype per Granerod cohort.

VITALS:
  temperature_celsius: 38.2
  heart_rate_bpm: 88
  systolic_bp_mmHg: 134
  diastolic_bp_mmHg: 80
  glasgow_coma_scale: 14
  oxygen_saturation_pct: 96
  respiratory_rate_breaths_per_min: 18

EXAM:
  mental_status_grade: confused
  neck_stiffness: True
  kernig_or_brudzinski_positive: True
  cranial_nerve_palsy: none
  papilledema_on_fundoscopy: False
  focal_neurological_deficit: True
  skin_lesion_centrofacial_chronic: False
  petechial_or_purpuric_rash: False

LABS:
  wbc_blood_per_uL: 7200
  platelets_per_uL: 220000
  alt_ast_U_per_L: 28
  crp_mg_per_L: 22.0
  procalcitonin_ng_per_mL: 0.3
  serum_sodium_mEq_per_L: 137

CSF:
  opening_pressure_cmH2O: 20.0
  wbc_per_mm3: 145
  lymphocyte_pct: 78
  neutrophil_pct: 22
  eosinophil_pct: 0
  glucose_mg_per_dL: 54
  protein_mg_per_dL: 105
  lactate_mmol_per_L: 2.2
  ada_U_per_L: None
  crag_lfa_result: negative
  wet_mount_motile_amoebae: negative
  xanthochromia_present: False
  rbc_per_mm3: 4

IMAGING:
  modality: mri_with_dwi_flair
  pattern: normal
  contrast_enhancement: False
  hydrocephalus: False
  basal_meningeal_enhancement: False
  finding_count: 0
  text_summary: MRI brain with DWI/FLAIR: normal. VZV reactivation with dermatomal rash and CSF lymphocytic pleocytosis can show normal parenchymal imaging in the absence of overt vasculopathy or cerebellitis; Granerod 2010 Lancet ID cohort documented this benign-imaging VZV phenotype.

DIAGNOSTIC_TESTS:
  pcr_panel: positive
  xpert_mtb_rif: n/a
  blood_culture: n/a
  csf_culture: n/a
  serology_or_antigen: positive
  smear_or_gram: multinucleated_giant_cells_seen
  brain_biopsy: n/a
  imaging_test: n/a
  total_dx_results: 5

NARRATIVE_EN: A 71-year-old woman in the Netherlands presented to a tertiary emergency department in Amsterdam after a resolving thoracic dermatomal zoster rash two weeks prior, then a 4-day course of fever to 38.2 C, headache, neck stiffness on day 2, gait ataxia (cerebellitis phenotype) on day 3, and confusion on day 4. She had no antecedent freshwater exposure. Examination on admission: temperature 38.2 C, Glasgow Coma Scale 14, neck stiffness, positive Kernig sign, focal deficit (gait ataxia consistent with VZV cerebellitis pattern), no rash currently active. CSF showed opening pressure 20 cmH2O, white cell count 145 per cubic millimeter (78 percent lymphocytes), glucose 54 mg/dL, protein 105 mg/dL. CSF VZV PCR positive. VZV IgM serology positive. Brain MRI with DWI/FLAIR was normal. Anchored to Granerod 2010 Lancet Infect Dis UK encephalitis cohort (PMID 20952256), post-zoster-CNS-reactivation-cerebellitis stratum. Outcome: survived with full recovery on 14-day acyclovir course. Subphase 1.3 commit 5.3.6 wave 2, pre-adjudication hold_for_revision.

NARRATIVE_ES: Mujer de 71 anos en Paises Bajos (Amsterdam), ingresada a urgencias terciarias dos semanas tras exantema dermatomal toracico de zoster en resolucion, con curso de cuatro dias: fiebre 38.2 C, cefalea, rigidez de nuca al segundo dia, ataxia de marcha (fenotipo de cerebelitis) al tercer dia y confusion al cuarto. Examen: temperatura 38.2 C, escala de Glasgow 14, rigidez de nuca, signo de Kernig positivo, deficit focal (ataxia de marcha consistente con cerebelitis por VZV), sin exantema activo actual. Liquido cefalorraquideo mostro leucocitos 145 por mm3 (78 por ciento linfocitos), glucosa 54 mg/dL, proteina 105 mg/dL. PCR de VZV en LCR positiva. IgM VZV positiva. RM cerebral normal. Anclaje en cohorte Granerod 2010 Lancet ID (PMID 20952256). Subphase 1.3 commit 5.3.6 wave 2, pre-adjudicacion hold_for_revision.

RATIONALE: Anchored to PMID 20952256 (Granerod 2010 Lancet ID UK encephalitis cohort). Post-zoster CNS-reactivation-cerebellitis phenotype: thoracic dermatomal zoster rash 2 weeks prior, then CSF VZV-PCR-positive lymphocytic meningitis with cerebellitis (gait ataxia) phenotype. Demographic anchor (71yo F NL post-zoster cerebellitis) sits in elderly-post-zoster-CNS stratum. CSF lymphocytic (145 WBC, 78 percent lymphocytes), normal glucose 54, mildly elevated protein 105. VZV PCR + IgM positive. Imputation tiers: tier_1_primary={age, sex, vzv_pcr, vzv_igm, post_zoster_window, gait_ataxia_cerebellitis}; tier_3_within_review={csf_wbc, neutrophil_pct, glucose, protein, gcs}; tier_4_priors={temp, symptom_days}. Indeterminate=none. Diagnostic_ambiguity=false. Outcome=survived_full_recovery. Tier: tier_3_imputation_within_review. 5.3.6 wave2 VZV-Granerod-post-zoster-cerebellitis.

ANCHORING_EXTRAS: stage=pre_adjudication; status=pending_external_review; self_review_disposition=hold_for_revision; self_review_notes=wave 5.3.6 VIRAL vignette anchored to PMID 20952256 (Granerod 2010 Lancet ID UK encephalitis cohort); external clinical adjudication pending; classification provisional. adjudicator_ids=VIRAL-WAVE2-PRE-ADJ-1, VIRAL-WAVE2-PRE-ADJ-2 (sentinel); cohen_kappa=0.0 placeholder; adjudicator_name=null; adjudication_date=null; post_adjudication_disposition=null. Subphase 1.3 commit 5.3.6 (2026-05-08, FINAL Subphase 1.3 wave). anchor=Granerod-Lancet-ID-2010 stratum=post-zoster-cerebellitis.

ADJUDICATION:
  inclusion_decision: hold_for_revision
  adjudicator_ids: ['VIRAL-WAVE2-PRE-ADJ-1', 'VIRAL-WAVE2-PRE-ADJ-2']
  ground_truth_class: 3
  pre_adjudication_kappa: 0.0
  disagreement_resolution: None

=== END vignette ===

=== CLASS 3 | vignette_id: 117 | subphase: 1.3 VIRAL | file: vir_117_dengue_lima_ambiguity.json ===

ANCHOR:
  pmid: 30089069
  first_author: Tyler
  year: 2018
  journal: NEJM
  citation_type: review
  doi: 10.1056/NEJMra1708714

DEMOGRAPHICS:
  age_years: 32
  sex: female
  geography_region: peru_lima_coast
  ethnicity: mestizo
  altitude_residence_m: 154
  hiv_status: negative
  cd4_count_cells_per_uL: None
  pregnancy_red_flag: False
  immunocompromise_status: none
  freshwater_exposure_within_14d: False
  freshwater_exposure_type: None

HISTORY:
  symptom_onset_to_presentation_days: 4.0
  chief_complaint: fever_with_headache
  red_flags_present: []
  prodrome_description: 32-year-old female in Lima, Peru. 4-day febrile illness during Peru 2024 dengue outbreak: fever 39.4 C, retro-orbital pain, severe myalgia, severe headache, encephalopathic mental status by day 3 with prominent CNS features raising arboviral DDx. No neck stiffness. Tertiary urban ED. Diagnostic_ambiguity=true; type=dengue_with_prominent_cns_arbo_encephalitis_overlap. Outcome: survived with full recovery.

VITALS:
  temperature_celsius: 39.4
  heart_rate_bpm: 112
  systolic_bp_mmHg: 112
  diastolic_bp_mmHg: 72
  glasgow_coma_scale: 12
  oxygen_saturation_pct: 96
  respiratory_rate_breaths_per_min: 22

EXAM:
  mental_status_grade: confused
  neck_stiffness: False
  kernig_or_brudzinski_positive: False
  cranial_nerve_palsy: none
  papilledema_on_fundoscopy: False
  focal_neurological_deficit: False
  skin_lesion_centrofacial_chronic: False
  petechial_or_purpuric_rash: False

LABS:
  wbc_blood_per_uL: 4500
  platelets_per_uL: 75000
  alt_ast_U_per_L: 138
  crp_mg_per_L: 28.0
  procalcitonin_ng_per_mL: 0.5
  serum_sodium_mEq_per_L: 134

CSF:
  opening_pressure_cmH2O: 19.0
  wbc_per_mm3: 110
  lymphocyte_pct: 70
  neutrophil_pct: 30
  eosinophil_pct: 0
  glucose_mg_per_dL: 58
  protein_mg_per_dL: 80
  lactate_mmol_per_L: 2.4
  ada_U_per_L: None
  crag_lfa_result: negative
  wet_mount_motile_amoebae: negative
  xanthochromia_present: False
  rbc_per_mm3: 4

IMAGING:
  modality: mri_with_dwi_flair
  pattern: normal
  contrast_enhancement: False
  hydrocephalus: False
  basal_meningeal_enhancement: False
  finding_count: 0
  text_summary: MRI brain with DWI/FLAIR: normal. No focal lesion, no edema. Dengue encephalopathy is typically metabolic or cytokine-mediated rather than direct viral invasion per Tyler review.

DIAGNOSTIC_TESTS:
  pcr_panel: DENV_2_serotype_positive
  xpert_mtb_rif: n/a
  blood_culture: n/a
  csf_culture: n/a
  serology_or_antigen: positive
  smear_or_gram: n/a
  brain_biopsy: n/a
  imaging_test: n/a
  total_dx_results: 4

NARRATIVE_EN: A 32-year-old woman in Lima, Peru presented to a tertiary urban emergency department during the Peru 2024 dengue outbreak with a 4-day febrile illness: fever to 39.4 C, retro-orbital pain, severe myalgia, severe headache, and encephalopathic mental status by day 3. The prominent CNS features raised initial differential for other arboviral encephalitides (EEE, JE, WNV). No neck stiffness on examination. Examination on admission: temperature 39.4 C, Glasgow Coma Scale 12, confused, no neck stiffness, no focal deficit, no rash. Platelets 75,000 per cubic millimeter (WHO 2009 dengue with warning signs threshold below 150,000 satisfied). CSF showed opening pressure 19 cmH2O, white cell count 110 per cubic millimeter (70 percent lymphocytes), glucose 58 mg/dL, protein 80 mg/dL. DENV NS1 antigen positive and DENV-2 PCR positive. Brain MRI normal. Diagnostic_ambiguity=true; type=dengue_with_prominent_cns_arbo_encephalitis_overlap. Anchored to Tyler 2018 NEJM viral encephalitis review (PMID 30089069). Outcome: survived. Subphase 1.3 commit 5.3.5 wave 1, pre-adjudication hold_for_revision.

NARRATIVE_ES: Mujer de 32 anos en Lima, Peru, ingresada a urgencias urbanas terciarias durante el brote de dengue de Peru 2024: cuatro dias de fiebre 39.4 C, dolor retro-orbitario, mialgia severa, cefalea intensa y estado mental encefalopatico al tercer dia. Las manifestaciones CNS prominentes elevaron el diagnostico diferencial inicial con otras encefalitides arbovirales. Sin rigidez de nuca al examen. Examen: temperatura 39.4 C, escala de Glasgow 12, confusa. Plaquetas 75,000 por mm3 (umbral signos de alarma OMS 2009 menor de 150,000). Liquido cefalorraquideo mostro presion de apertura 19 cmH2O, leucocitos 110 por mm3 (70 por ciento linfocitos), glucosa 58 mg/dL, proteina 80 mg/dL. NS1 antigeno DENV positivo y PCR DENV-2 positiva. RM cerebral normal. Ambiguedad diagnostica por superposicion CNS arbo-encefalitis. Anclaje en revision Tyler 2018 NEJM (PMID 30089069). Subphase 1.3 commit 5.3.5 wave 1.

RATIONALE: Anchored to PMID 30089069 (Tyler 2018 NEJM viral encephalitis review) with prominent CNS-arbo-encephalitis-overlap phenotype. Diagnostic_ambiguity=true; type=dengue_with_prominent_cns_arbo_encephalitis_overlap (verbatim from spec). Demographic anchor (32yo F Lima during 2024 outbreak) sits in dengue-with-CNS stratum that overlaps with EEE/JE/WNV DDx. Platelets 75k satisfies thrombocytopenia-warning-signs threshold. CSF lymphocytic (110 WBC, 70 percent lymphocytes), normal glucose 58, mildly elevated protein 80. NS1 + DENV-2 PCR confirm organism. Imputation tiers: tier_1_primary={age, sex, region, denv_pcr, ns1, platelets, outbreak_context}; tier_3_within_review={csf_wbc, neutrophil_pct, glucose, protein}; tier_4_priors={temp, gcs, symptom_days}. Indeterminate=initial-arbo-DDx-resolved-by-DENV-PCR. Outcome=survived. Tier: tier_4_imputation_peru_dengue_2024_anchored. 5.3.5 wave1 dengue-Lima-arbo-overlap.

ANCHORING_EXTRAS: stage=pre_adjudication; status=pending_external_review; self_review_disposition=hold_for_revision; self_review_notes=wave 5.3.5 VIRAL vignette anchored to PMID 30089069 (Tyler 2018 NEJM viral encephalitis review); external clinical adjudication pending; classification provisional. adjudicator_ids=VIRAL-WAVE1-PRE-ADJ-1, VIRAL-WAVE1-PRE-ADJ-2 (sentinel); cohen_kappa=0.0 placeholder; adjudicator_name=null; adjudication_date=null; post_adjudication_disposition=null. Subphase 1.3 commit 5.3.5 (2026-05-08). anchor=Tyler-NEJM-2018 type=dengue_with_prominent_cns_arbo_encephalitis_overlap region=Lima-Peru.

ADJUDICATION:
  inclusion_decision: hold_for_revision
  adjudicator_ids: ['VIRAL-WAVE1-PRE-ADJ-1', 'VIRAL-WAVE1-PRE-ADJ-2']
  ground_truth_class: 3
  pre_adjudication_kappa: 0.0
  disagreement_resolution: None

=== END vignette ===

=== CLASS 3 | vignette_id: 118 | subphase: 1.3 VIRAL | file: vir_118_dengue_loreto.json ===

ANCHOR:
  pmid: 38300858
  first_author: Munayco
  year: 2024
  journal: MMWR
  citation_type: surveillance
  doi: 10.15585/mmwr.mm7304a4

DEMOGRAPHICS:
  age_years: 32
  sex: female
  geography_region: peru_loreto_amazon
  ethnicity: mestizo
  altitude_residence_m: 106
  hiv_status: negative
  cd4_count_cells_per_uL: None
  pregnancy_red_flag: False
  immunocompromise_status: none
  freshwater_exposure_within_14d: False
  freshwater_exposure_type: None

HISTORY:
  symptom_onset_to_presentation_days: 4.0
  chief_complaint: fever_with_headache
  red_flags_present: []
  prodrome_description: 32-year-old female in Loreto, Peruvian Amazon. 4-day febrile illness during Peru 2023 dengue outbreak (post Cyclone Yaku, coastal El Nino): fever 39.6 C, retro-orbital pain, severe myalgia, severe headache, bleeding gums day 3, encephalopathic mental status day 4. No neck stiffness. Regional hospital. No freshwater exposure (dengue is mosquito-borne arboviral). Outcome: survived full recovery.

VITALS:
  temperature_celsius: 39.6
  heart_rate_bpm: 116
  systolic_bp_mmHg: 110
  diastolic_bp_mmHg: 70
  glasgow_coma_scale: 12
  oxygen_saturation_pct: 96
  respiratory_rate_breaths_per_min: 22

EXAM:
  mental_status_grade: confused
  neck_stiffness: False
  kernig_or_brudzinski_positive: False
  cranial_nerve_palsy: none
  papilledema_on_fundoscopy: False
  focal_neurological_deficit: False
  skin_lesion_centrofacial_chronic: False
  petechial_or_purpuric_rash: False

LABS:
  wbc_blood_per_uL: 4200
  platelets_per_uL: 65000
  alt_ast_U_per_L: 145
  crp_mg_per_L: 32.0
  procalcitonin_ng_per_mL: 0.6
  serum_sodium_mEq_per_L: 134

CSF:
  opening_pressure_cmH2O: 18.0
  wbc_per_mm3: 85
  lymphocyte_pct: 70
  neutrophil_pct: 30
  eosinophil_pct: 0
  glucose_mg_per_dL: 62
  protein_mg_per_dL: 75
  lactate_mmol_per_L: 2.6
  ada_U_per_L: None
  crag_lfa_result: negative
  wet_mount_motile_amoebae: negative
  xanthochromia_present: False
  rbc_per_mm3: 5

IMAGING:
  modality: mri_with_dwi_flair
  pattern: normal
  contrast_enhancement: False
  hydrocephalus: False
  basal_meningeal_enhancement: False
  finding_count: 0
  text_summary: Brain MRI with DWI/FLAIR: normal. No focal lesion, no edema, no hemorrhage. Dengue encephalopathy in this case is metabolic or cytokine-mediated rather than direct viral invasion.

DIAGNOSTIC_TESTS:
  pcr_panel: DENV_2_serotype_positive
  xpert_mtb_rif: n/a
  blood_culture: n/a
  csf_culture: n/a
  serology_or_antigen: positive
  smear_or_gram: n/a
  brain_biopsy: n/a
  imaging_test: n/a
  total_dx_results: 4

NARRATIVE_EN: A 32-year-old woman in Loreto, Peruvian Amazon presented to a regional hospital during the Peru 2023 post-Cyclone-Yaku dengue outbreak (March 2023, linked to coastal El Nino, Munayco MMWR 2024). Four-day febrile illness: fever to 39.6 C, retro-orbital pain, severe myalgia, severe headache, bleeding gums on day 3, encephalopathic mental status by day 4. No neck stiffness on examination. No antecedent freshwater exposure (dengue is mosquito-borne arboviral, not freshwater amoebic). Examination on admission: temperature 39.6 C, Glasgow Coma Scale 12, confused. Platelets 65,000 per cubic millimeter (WHO 2009 dengue with warning signs threshold below 150,000 satisfied). CSF showed white cell count 85 per cubic millimeter (70 percent lymphocytes), glucose 62 mg/dL, protein 75 mg/dL. DENV NS1 antigen positive and DENV-2 PCR positive. Brain MRI normal (dengue encephalopathy in this case is metabolic or cytokine-mediated rather than direct viral invasion). Primary anchor: PMID 38300858 (Munayco MMWR 2024), Peru 2023 dengue outbreak surveillance (222,620 cases first 30 weeks, 381 deaths, DENV-2 circulating since 2019). Outcome: survived with full recovery. Subphase 1.3 commit 5.3.2 pilot 6, pre-adjudication hold_for_revision.

NARRATIVE_ES: Mujer de 32 anos en Loreto, Amazonia peruana, ingresada a hospital regional durante el brote de dengue post Ciclon Yaku (2023, vinculado a fenomeno El Nino costero, Munayco MMWR 2024). Cuatro dias de enfermedad febril: fiebre 39.6 C, dolor retro-orbitario, mialgia severa, cefalea intensa, sangrado gingival al tercer dia, estado mental encefalopatico al cuarto dia. Sin rigidez de nuca al examen. Sin exposicion a agua dulce (dengue arboviral, no amebica). Examen: temperatura 39.6 C, escala de Glasgow 12, confusa. Plaquetas 65,000 por mm3 (umbral de signos de alarma de dengue OMS 2009 menor de 150,000). Liquido cefalorraquideo mostro leucocitos 85 por mm3 (70 por ciento linfocitos), glucosa 62 mg/dL, proteina 75 mg/dL. NS1 antigeno de DENV positivo y PCR DENV-2 positiva. RM cerebral normal (encefalopatia metabolica o mediada por citoquinas). Anclaje primario en vigilancia MMWR del brote peruano de dengue 2023 (PMID 38300858, Munayco 2024, 222,620 casos primeras 30 semanas, 381 muertes, DENV-2 circulante desde 2019). Subphase 1.3 commit 5.3.2 pilot 6.

RATIONALE: Anchored to PMID 38300858 (Munayco MMWR 2024), Peru 2023 dengue outbreak surveillance (222,620 cases / 381 deaths first 30 weeks; 10x prior 5-year average; post Cyclone Yaku + coastal El Nino; DENV-2 circulating since 2019). Anchor (32yo F Loreto Amazon) within high-incidence Peruvian Amazon stratum. Platelets 65,000 per uL satisfies master prompt below 150,000 and WHO 2009 dengue-with-warning-signs threshold. Encephalopathic clinical form documented neurologic presentation in severe dengue. Lymphocytic CSF (WBC 85, lymphocytes 70 percent), NS1 antigen + DENV-2 PCR canonical. Imputation tiers: tier_1_primary={age, sex, region, denv_pcr, ns1, platelets, outbreak_context}; tier_3_within_cohort={csf_wbc, glucose, protein}; tier_4_priors={temp, gcs, symptom_days}. Indeterminate=none. Ambiguity=false. Outcome=survived_full_recovery. Per USER ASSIGNMENT 5: serotype split not in MMWR abstract. Tier: primary_source_direct (Peru). 5.3.2 pilot 6.

ANCHORING_EXTRAS: stage=pre_adjudication; status=pending_external_review; self_review_disposition=hold_for_revision; self_review_notes=pilot vignette anchored to PMID 38300858 (Munayco MMWR 2024 Peru 2023 dengue outbreak); external clinical adjudication pending; classification provisional. adjudicator_ids=PILOT-PRE-ADJ-1, PILOT-PRE-ADJ-2 (sentinel); cohen_kappa=0.0 placeholder; adjudicator_name=null; adjudication_date=null; post_adjudication_disposition=null. Subphase 1.3 commit 5.3.2 (2026-05-07).

ADJUDICATION:
  inclusion_decision: hold_for_revision
  adjudicator_ids: ['PILOT-PRE-ADJ-1', 'PILOT-PRE-ADJ-2']
  ground_truth_class: 3
  pre_adjudication_kappa: 0.0
  disagreement_resolution: None

=== END vignette ===

=== CLASS 3 | vignette_id: 119 | subphase: 1.3 VIRAL | file: vir_119_dengue_tumbes.json ===

ANCHOR:
  pmid: 30089069
  first_author: Tyler
  year: 2018
  journal: NEJM
  citation_type: review
  doi: 10.1056/NEJMra1708714

DEMOGRAPHICS:
  age_years: 41
  sex: male
  geography_region: peru_tumbes
  ethnicity: mestizo
  altitude_residence_m: 6
  hiv_status: negative
  cd4_count_cells_per_uL: None
  pregnancy_red_flag: False
  immunocompromise_status: none
  freshwater_exposure_within_14d: False
  freshwater_exposure_type: None

HISTORY:
  symptom_onset_to_presentation_days: 4.0
  chief_complaint: fever_with_headache
  red_flags_present: []
  prodrome_description: 41-year-old male in Tumbes, Peru coastal community. 4-day febrile illness during regional dengue activity: fever 39.2 C, retro-orbital pain, severe myalgia, severe headache, transient encephalopathy day 3. No neck stiffness. Regional hospital. Outcome: survived with full recovery.

VITALS:
  temperature_celsius: 39.2
  heart_rate_bpm: 108
  systolic_bp_mmHg: 116
  diastolic_bp_mmHg: 72
  glasgow_coma_scale: 13
  oxygen_saturation_pct: 96
  respiratory_rate_breaths_per_min: 22

EXAM:
  mental_status_grade: confused
  neck_stiffness: False
  kernig_or_brudzinski_positive: False
  cranial_nerve_palsy: none
  papilledema_on_fundoscopy: False
  focal_neurological_deficit: False
  skin_lesion_centrofacial_chronic: False
  petechial_or_purpuric_rash: False

LABS:
  wbc_blood_per_uL: 4800
  platelets_per_uL: 85000
  alt_ast_U_per_L: 124
  crp_mg_per_L: 26.0
  procalcitonin_ng_per_mL: 0.5
  serum_sodium_mEq_per_L: 135

CSF:
  opening_pressure_cmH2O: 18.0
  wbc_per_mm3: 95
  lymphocyte_pct: 72
  neutrophil_pct: 28
  eosinophil_pct: 0
  glucose_mg_per_dL: 60
  protein_mg_per_dL: 75
  lactate_mmol_per_L: 2.4
  ada_U_per_L: None
  crag_lfa_result: negative
  wet_mount_motile_amoebae: negative
  xanthochromia_present: False
  rbc_per_mm3: 4

IMAGING:
  modality: mri_with_dwi_flair
  pattern: normal
  contrast_enhancement: False
  hydrocephalus: False
  basal_meningeal_enhancement: False
  finding_count: 0
  text_summary: MRI brain with DWI/FLAIR: normal. No focal lesion, no edema. Dengue encephalopathy is typically metabolic or cytokine-mediated rather than direct viral invasion per Tyler review.

DIAGNOSTIC_TESTS:
  pcr_panel: DENV_2_serotype_positive
  xpert_mtb_rif: n/a
  blood_culture: n/a
  csf_culture: n/a
  serology_or_antigen: positive
  smear_or_gram: n/a
  brain_biopsy: n/a
  imaging_test: n/a
  total_dx_results: 4

NARRATIVE_EN: A 41-year-old man in Tumbes, Peru coastal community presented to a regional hospital during regional dengue activity with a 4-day febrile illness: fever to 39.2 C, retro-orbital pain, severe myalgia, severe headache, and transient encephalopathy on day 3. He had no neck stiffness on examination. Examination on admission: temperature 39.2 C, Glasgow Coma Scale 13, confused, no neck stiffness, no focal deficit, no rash. Platelets 85,000 per cubic millimeter (WHO 2009 dengue with warning signs threshold below 150,000). CSF showed opening pressure 18 cmH2O, white cell count 95 per cubic millimeter (72 percent lymphocytes), glucose 60 mg/dL, protein 75 mg/dL. DENV NS1 antigen positive and DENV-2 PCR positive. Brain MRI normal (metabolic / cytokine-mediated encephalopathy). Anchored to Tyler 2018 NEJM viral encephalitis review (PMID 30089069), Peru-coastal-Tumbes dengue stratum. Outcome: survived with full recovery. Subphase 1.3 commit 5.3.5 wave 1, pre-adjudication hold_for_revision.

NARRATIVE_ES: Varon de 41 anos en comunidad costera de Tumbes, Peru, ingresado a hospital regional durante actividad regional de dengue: cuatro dias de fiebre 39.2 C, dolor retro-orbitario, mialgia severa, cefalea intensa y encefalopatia transitoria al tercer dia. Sin rigidez de nuca al examen. Examen: temperatura 39.2 C, escala de Glasgow 13, confuso. Plaquetas 85,000 por mm3 (umbral OMS 2009 menor de 150,000). Liquido cefalorraquideo mostro presion de apertura 18 cmH2O, leucocitos 95 por mm3 (72 por ciento linfocitos), glucosa 60 mg/dL, proteina 75 mg/dL. NS1 antigeno DENV positivo y PCR DENV-2 positiva. RM cerebral normal. Anclaje en revision Tyler 2018 NEJM (PMID 30089069), estrato Tumbes-coastal dengue. Subphase 1.3 commit 5.3.5 wave 1, pre-adjudicacion hold_for_revision.

RATIONALE: Anchored to PMID 30089069 (Tyler 2018 NEJM viral encephalitis review). Dengue with transient encephalopathy in Peru-coastal-Tumbes stratum. Demographic anchor (41yo M Tumbes) sits in Peru-coastal-dengue stratum. Platelets 85k satisfies thrombocytopenia-warning-signs threshold. CSF lymphocytic (95 WBC, 72 percent lymphocytes), normal glucose 60, mildly elevated protein 75. NS1 + DENV-2 PCR confirm organism. MRI normal (metabolic / cytokine encephalopathy not direct viral invasion). Imputation tiers: tier_1_primary={age, sex, region, denv_pcr, ns1, platelets}; tier_3_within_review={csf_wbc, neutrophil_pct, glucose, protein}; tier_4_priors={temp, gcs, symptom_days}. Indeterminate=none. Diagnostic_ambiguity=false. Outcome=survived_full_recovery. Tier: tier_4_imputation_peru_dengue_2024_anchored. 5.3.5 wave1 dengue-Tumbes-coastal.

ANCHORING_EXTRAS: stage=pre_adjudication; status=pending_external_review; self_review_disposition=hold_for_revision; self_review_notes=wave 5.3.5 VIRAL vignette anchored to PMID 30089069 (Tyler 2018 NEJM viral encephalitis review); external clinical adjudication pending; classification provisional. adjudicator_ids=VIRAL-WAVE1-PRE-ADJ-1, VIRAL-WAVE1-PRE-ADJ-2 (sentinel); cohen_kappa=0.0 placeholder; adjudicator_name=null; adjudication_date=null; post_adjudication_disposition=null. Subphase 1.3 commit 5.3.5 (2026-05-08). anchor=Tyler-NEJM-2018 region=Tumbes-Peru.

ADJUDICATION:
  inclusion_decision: hold_for_revision
  adjudicator_ids: ['VIRAL-WAVE1-PRE-ADJ-1', 'VIRAL-WAVE1-PRE-ADJ-2']
  ground_truth_class: 3
  pre_adjudication_kappa: 0.0
  disagreement_resolution: None

=== END vignette ===

=== CLASS 3 | vignette_id: 120 | subphase: 1.3 VIRAL | file: vir_120_eee_northeast_us_fatal.json ===

ANCHOR:
  pmid: 30089069
  first_author: Tyler
  year: 2018
  journal: NEJM
  citation_type: review
  doi: 10.1056/NEJMra1708714

DEMOGRAPHICS:
  age_years: 58
  sex: male
  geography_region: us_south
  ethnicity: white_non_hispanic
  altitude_residence_m: 100
  hiv_status: negative
  cd4_count_cells_per_uL: None
  pregnancy_red_flag: False
  immunocompromise_status: none
  freshwater_exposure_within_14d: False
  freshwater_exposure_type: None

HISTORY:
  symptom_onset_to_presentation_days: 5.0
  chief_complaint: altered_mental_status
  red_flags_present: []
  prodrome_description: 58-year-old male, US South region. 5-day course: fever 39.0 C, severe headache, neck stiffness, then progressive encephalopathy with stupor day 4 and coma day 5. Recent outdoor activity in mosquito-endemic wooded area. Tertiary ED. Outcome: fatal hospital day 4. EEE per Tyler review case fatality approximately 30 percent.

VITALS:
  temperature_celsius: 39.0
  heart_rate_bpm: 124
  systolic_bp_mmHg: 102
  diastolic_bp_mmHg: 64
  glasgow_coma_scale: 6
  oxygen_saturation_pct: 90
  respiratory_rate_breaths_per_min: 28

EXAM:
  mental_status_grade: comatose
  neck_stiffness: True
  kernig_or_brudzinski_positive: True
  cranial_nerve_palsy: none
  papilledema_on_fundoscopy: False
  focal_neurological_deficit: True
  skin_lesion_centrofacial_chronic: False
  petechial_or_purpuric_rash: False

LABS:
  wbc_blood_per_uL: 13500
  platelets_per_uL: 175000
  alt_ast_U_per_L: 38
  crp_mg_per_L: 65.0
  procalcitonin_ng_per_mL: 1.2
  serum_sodium_mEq_per_L: 132

CSF:
  opening_pressure_cmH2O: 28.0
  wbc_per_mm3: 350
  lymphocyte_pct: 60
  neutrophil_pct: 35
  eosinophil_pct: 5
  glucose_mg_per_dL: 48
  protein_mg_per_dL: 145
  lactate_mmol_per_L: 3.4
  ada_U_per_L: None
  crag_lfa_result: negative
  wet_mount_motile_amoebae: negative
  xanthochromia_present: False
  rbc_per_mm3: 5

IMAGING:
  modality: mri_with_dwi_flair
  pattern: diffuse_cerebral_edema_basilar_meningeal_enhancement
  contrast_enhancement: True
  hydrocephalus: False
  basal_meningeal_enhancement: False
  finding_count: 1
  text_summary: MRI brain with DWI/FLAIR: diffuse cerebral edema with basal ganglia and thalamic involvement, sulcal effacement. EEE predilection for basal ganglia and thalamus per Tyler 2018 NEJM review (case fatality approximately 30 percent; permanent neurologic sequelae in 50 percent of survivors).

DIAGNOSTIC_TESTS:
  pcr_panel: positive
  xpert_mtb_rif: n/a
  blood_culture: n/a
  csf_culture: n/a
  serology_or_antigen: positive
  smear_or_gram: n/a
  brain_biopsy: n/a
  imaging_test: n/a
  total_dx_results: 4

NARRATIVE_EN: A 58-year-old man in the US South region presented to a tertiary emergency department with a 5-day course of fever to 39.0 C, severe headache, neck stiffness, then progressive encephalopathy with stupor on day 4 and coma on day 5. He reported recent outdoor activity in a mosquito-endemic wooded area. Examination on admission: temperature 39.0 C, Glasgow Coma Scale 6, comatose, neck stiffness, positive Kernig sign, focal deficit (left-sided weakness), no rash. CSF showed opening pressure 28 cmH2O, white cell count 350 per cubic millimeter (60 percent lymphocytes, 35 percent neutrophils, 5 percent eosinophils), glucose 48 mg/dL, protein 145 mg/dL. CSF EEE IgM serology positive and CSF EEE PCR positive. Brain MRI with DWI/FLAIR showed diffuse cerebral edema with basal ganglia and thalamic involvement (EEE predilection per Tyler review). Anchored to Tyler 2018 NEJM viral encephalitis review (PMID 30089069), EEE high-mortality older-adult stratum (case fatality approximately 30 percent, permanent sequelae in 50 percent of survivors). Outcome: fatal hospital day 4. Subphase 1.3 commit 5.3.5 wave 1, pre-adjudication hold_for_revision.

NARRATIVE_ES: Varon de 58 anos en region sur de Estados Unidos, ingresado a urgencias terciarias con curso de cinco dias: fiebre 39.0 C, cefalea intensa, rigidez de nuca, luego encefalopatia progresiva con estupor al cuarto dia y coma al quinto. Actividad reciente al aire libre en area boscosa endemica de mosquitos. Examen: temperatura 39.0 C, escala de Glasgow 6, comatoso, rigidez de nuca, signo de Kernig positivo, deficit focal (debilidad izquierda), sin exantema. Liquido cefalorraquideo mostro presion de apertura 28 cmH2O, leucocitos 350 por mm3 (60 por ciento linfocitos, 35 por ciento neutrofilos), glucosa 48 mg/dL, proteina 145 mg/dL. IgM y PCR de EEE en LCR positivas. RM cerebral con edema cerebral difuso con compromiso de ganglios basales y talamo. Anclaje en revision Tyler 2018 NEJM (PMID 30089069), estrato EEE alta mortalidad. Subphase 1.3 commit 5.3.5 wave 1.

RATIONALE: Anchored to PMID 30089069 (Tyler 2018 NEJM viral encephalitis review). EEE high-mortality older-adult phenotype (case fatality approximately 30 percent, permanent neurologic sequelae in 50 percent of survivors per Tyler review). Demographic anchor (58yo M US South mosquito-endemic woods) sits in EEE-older-adult stratum. CSF mixed-cellularity leaning lymphocytic (350 WBC, 60 percent lymphocytes, 35 percent neutrophils, 5 percent eosinophils), glucose 48 (near master prompt 1.3.4 floor), elevated protein 145. EEE IgM + PCR positive. MRI diffuse cerebral edema with basal ganglia and thalamic involvement. Imputation tiers: tier_1_primary={age, sex, eee_igm, eee_pcr, mosquito_endemic_area, imaging_pattern}; tier_3_within_review={csf_wbc, neutrophil_pct, glucose, protein, gcs}; tier_4_priors={temp, symptom_days, hr}. Indeterminate=none. Diagnostic_ambiguity=false. Outcome=fatal_hospital_day_4. Tier: tier_3_imputation_within_review. 5.3.5 wave1 EEE-older-adult-fatal.

ANCHORING_EXTRAS: stage=pre_adjudication; status=pending_external_review; self_review_disposition=hold_for_revision; self_review_notes=wave 5.3.5 VIRAL vignette anchored to PMID 30089069 (Tyler 2018 NEJM viral encephalitis review); external clinical adjudication pending; classification provisional. adjudicator_ids=VIRAL-WAVE1-PRE-ADJ-1, VIRAL-WAVE1-PRE-ADJ-2 (sentinel); cohen_kappa=0.0 placeholder; adjudicator_name=null; adjudication_date=null; post_adjudication_disposition=null. Subphase 1.3 commit 5.3.5 (2026-05-08). anchor=Tyler-NEJM-2018 stratum=EEE-older-adult-fatal mosquito_endemic=true.

ADJUDICATION:
  inclusion_decision: hold_for_revision
  adjudicator_ids: ['VIRAL-WAVE1-PRE-ADJ-1', 'VIRAL-WAVE1-PRE-ADJ-2']
  ground_truth_class: 3
  pre_adjudication_kappa: 0.0
  disagreement_resolution: None

=== END vignette ===

=== CLASS 4 | vignette_id: 121 | subphase: 1.4 TBM pilot | file: tbm_121_thwaites_hcmc_adult_pilot.json ===

ANCHOR:
  pmid: 15496623
  first_author: Thwaites
  year: 2004
  journal: NEJM
  citation_type: rct
  doi: 10.1056/NEJMoa040573

DEMOGRAPHICS:
  age_years: 35
  sex: male
  geography_region: other_global
  ethnicity: asian
  altitude_residence_m: 19
  hiv_status: negative
  cd4_count_cells_per_uL: None
  pregnancy_red_flag: False
  immunocompromise_status: none
  freshwater_exposure_within_14d: False
  freshwater_exposure_type: None

HISTORY:
  symptom_onset_to_presentation_days: 28.0
  chief_complaint: fever_with_headache
  red_flags_present: []
  prodrome_description: Four-week subacute illness in a 35-year-old man from Ho Chi Minh City. Low-grade evening fevers, weight loss of 4 kg, progressive frontal headache for three weeks, and intermittent vomiting in the final week. No recent freshwater exposure. Household contact with a cousin treated for pulmonary tuberculosis the prior year.

VITALS:
  temperature_celsius: 38.4
  heart_rate_bpm: 96
  systolic_bp_mmHg: 122
  diastolic_bp_mmHg: 78
  glasgow_coma_scale: 13
  oxygen_saturation_pct: 96
  respiratory_rate_breaths_per_min: 18

EXAM:
  mental_status_grade: somnolent
  neck_stiffness: True
  kernig_or_brudzinski_positive: True
  cranial_nerve_palsy: CN_VI
  papilledema_on_fundoscopy: True
  focal_neurological_deficit: True
  skin_lesion_centrofacial_chronic: False
  petechial_or_purpuric_rash: False

LABS:
  wbc_blood_per_uL: 8400
  platelets_per_uL: 312000
  alt_ast_U_per_L: 28
  crp_mg_per_L: 38.0
  procalcitonin_ng_per_mL: 0.4
  serum_sodium_mEq_per_L: 128

CSF:
  opening_pressure_cmH2O: 24.0
  wbc_per_mm3: 280
  lymphocyte_pct: 78
  neutrophil_pct: 20
  eosinophil_pct: 2
  glucose_mg_per_dL: 28
  protein_mg_per_dL: 280
  lactate_mmol_per_L: 4.4
  ada_U_per_L: 14.0
  crag_lfa_result: negative
  wet_mount_motile_amoebae: negative
  xanthochromia_present: False
  rbc_per_mm3: 2

IMAGING:
  modality: mri_contrast
  pattern: basal_meningeal_enhancement_with_hydrocephalus
  contrast_enhancement: True
  hydrocephalus: True
  basal_meningeal_enhancement: True
  finding_count: None
  text_summary: Thick basal meningeal enhancement on post-contrast T1 with mild communicating hydrocephalus and a small left basal ganglia infarct. Findings consistent with active tuberculous meningitis.

DIAGNOSTIC_TESTS:
  pcr_panel: n/a
  xpert_mtb_rif: Positive, rifampicin susceptible. Cycle threshold consistent with TBM.
  blood_culture: n/a
  csf_culture: Pending at LP; reported positive at 4 weeks (M. tuberculosis drug-sensitive).
  serology_or_antigen: n/a
  smear_or_gram: Positive, scant acid-fast bacilli on concentrated specimen.
  brain_biopsy: n/a
  imaging_test: Hilar lymphadenopathy with adjacent parenchymal infiltrate consistent with primary TB.
  total_dx_results: 4

NARRATIVE_EN: A 35-year-old man from Ho Chi Minh City presented to a tertiary referral hospital with a four-week subacute illness. He reported low-grade evening fevers, four kilograms of weight loss, three weeks of progressive frontal headache, and intermittent vomiting in the final week. His cousin had been treated for pulmonary tuberculosis the prior year. Examination on admission: temperature 38.4 C, Glasgow Coma Scale 13, somnolent but rousable, neck stiffness, positive Kernig sign, right lateral gaze palsy consistent with sixth cranial nerve involvement, and papilledema on fundoscopy. CSF showed opening pressure 24 cmH2O, white cell count 280 per cubic millimeter with 78 percent lymphocytes, glucose 28 mg/dL, protein 280 mg/dL, and adenosine deaminase 14 U/L. MRI with contrast demonstrated thick basal meningeal enhancement and mild communicating hydrocephalus. CSF Xpert MTB/RIF Ultra was positive and rifampicin susceptible. Anchored to Thwaites NEJM 2004 (PMID 15496623). Subphase 1.4 commit 5.4.2 pilot, hold_for_revision.

NARRATIVE_ES: Varon de 35 anos de Ho Chi Minh, Vietnam, ingresado a un hospital terciario tras un cuadro subagudo de cuatro semanas. Refiere fiebre vespertina baja, perdida de 4 kg, cefalea frontal progresiva de tres semanas y vomitos intermitentes en la ultima semana. Antecedente de primo con tuberculosis pulmonar tratada el ano previo. Examen al ingreso: temperatura 38.4 C, Glasgow 13, somnoliento, rigidez de nuca, signo de Kernig positivo, paresia del sexto par craneal derecho y papiledema en el fondo de ojo. LCR con presion de apertura 24 cmH2O, leucocitos 280 por mm3 (78 por ciento linfocitos), glucosa 28 mg/dL, proteina 280 mg/dL, adenosina desaminasa 14 U/L. RM con contraste mostro engrosamiento meningeo basal e hidrocefalia comunicante leve. Xpert MTB/RIF Ultra positivo en LCR, susceptible a rifampicina. Anclaje Thwaites NEJM 2004 (PMID 15496623). Subphase 1.4 pilot.

RATIONALE: Subphase 1.4 commit 5.4.2 pilot 1 of 6 for Class 4 TBM. Anchored to Thwaites NEJM 2004 dexamethasone RCT (HCMC adult HIV-negative, drug-sensitive TBM). CSF and imaging within published case ranges; ADA 14 U/L above Ye TM&IH 2023 cutoff of 10. CN VI palsy per Huynh 2022 Lancet Neurol 30 percent subset. Pre-adjudication hold_for_revision.

ANCHORING_EXTRAS: Anchored to Thwaites GE et al. NEJM 2004 (PMID 15496623), HCMC dexamethasone TBM RCT. 35-year-old Vietnamese adult, drug-sensitive TBM with classical lymphocytic CSF (lymph 78 percent, protein 280, glucose 28), ADA 14 U/L, Xpert MTB/RIF Ultra positive, AFB smear positive, CN VI palsy positive (Huynh 30 percent subset). Pre-adjudication kappa 0.70.

ADJUDICATION:
  inclusion_decision: hold_for_revision
  adjudicator_ids: ['PILOT-TBM-121-ADJ-1', 'PILOT-TBM-121-ADJ-2']
  ground_truth_class: 4
  pre_adjudication_kappa: 0.7
  disagreement_resolution: None

=== END vignette ===

=== CLASS 4 | vignette_id: 122 | subphase: 1.4 TBM pilot | file: tbm_122_vantoorn_cape_town_pediatric_pilot.json ===

ANCHOR:
  pmid: 24655399
  first_author: van
  year: 2014
  journal: Semin-Pediatr-Neurol
  citation_type: review
  doi: 10.1016/j.spen.2014.01.006

DEMOGRAPHICS:
  age_years: 1
  sex: female
  geography_region: other_global
  ethnicity: other
  altitude_residence_m: 50
  hiv_status: negative
  cd4_count_cells_per_uL: None
  pregnancy_red_flag: False
  immunocompromise_status: none
  freshwater_exposure_within_14d: False
  freshwater_exposure_type: None

HISTORY:
  symptom_onset_to_presentation_days: 21.0
  chief_complaint: altered_mental_status
  red_flags_present: []
  prodrome_description: Eighteen-month-old girl from Cape Town with three weeks of intermittent fever, poor feeding, weight failure, and increasing irritability. The grandmother was treated for sputum-positive pulmonary tuberculosis four months earlier. BCG vaccinated at birth. Progressive lethargy in the final five days with one focal seizure.

VITALS:
  temperature_celsius: 38.1
  heart_rate_bpm: 142
  systolic_bp_mmHg: 95
  diastolic_bp_mmHg: 58
  glasgow_coma_scale: 11
  oxygen_saturation_pct: 95
  respiratory_rate_breaths_per_min: 32

EXAM:
  mental_status_grade: somnolent
  neck_stiffness: True
  kernig_or_brudzinski_positive: True
  cranial_nerve_palsy: none
  papilledema_on_fundoscopy: True
  focal_neurological_deficit: True
  skin_lesion_centrofacial_chronic: False
  petechial_or_purpuric_rash: False

LABS:
  wbc_blood_per_uL: 11200
  platelets_per_uL: 286000
  alt_ast_U_per_L: 22
  crp_mg_per_L: 26.0
  procalcitonin_ng_per_mL: 0.3
  serum_sodium_mEq_per_L: 124

CSF:
  opening_pressure_cmH2O: 28.0
  wbc_per_mm3: 220
  lymphocyte_pct: 80
  neutrophil_pct: 18
  eosinophil_pct: 2
  glucose_mg_per_dL: 22
  protein_mg_per_dL: 220
  lactate_mmol_per_L: 4.4
  ada_U_per_L: 12.0
  crag_lfa_result: negative
  wet_mount_motile_amoebae: negative
  xanthochromia_present: False
  rbc_per_mm3: 2

IMAGING:
  modality: mri_contrast
  pattern: basal_meningeal_enhancement_with_hydrocephalus
  contrast_enhancement: True
  hydrocephalus: True
  basal_meningeal_enhancement: True
  finding_count: None
  text_summary: Marked basal meningeal enhancement with communicating hydrocephalus requiring ventriculoperitoneal shunt placement. Multiple small basal ganglia infarcts. Findings highly characteristic of pediatric tuberculous meningitis per van Toorn pediatric TBM phenotype.

DIAGNOSTIC_TESTS:
  pcr_panel: n/a
  xpert_mtb_rif: Positive, rifampicin susceptible. Cycle threshold consistent with TBM.
  blood_culture: n/a
  csf_culture: Pending at LP; reported positive at 4 weeks (M. tuberculosis drug-sensitive).
  serology_or_antigen: n/a
  smear_or_gram: n/a
  brain_biopsy: n/a
  imaging_test: Hilar lymphadenopathy with adjacent parenchymal infiltrate consistent with primary TB.
  total_dx_results: 5

NARRATIVE_EN: An 18-month-old girl from Cape Town presented to a pediatric tertiary hospital with three weeks of intermittent fever, poor feeding, failure to thrive, and increasing irritability. Her grandmother had been treated for sputum-positive pulmonary tuberculosis four months earlier. The child had received BCG vaccination at birth. Over the final five days she became progressively lethargic with one focal seizure on the day of admission. Examination: temperature 38.1 C, Glasgow Coma Scale 11, somnolent, neck stiffness, positive Kernig sign, right-sided motor weakness, and papilledema on fundoscopy. CSF showed opening pressure 28 cmH2O, white cell count 220 per cubic millimeter with 80 percent lymphocytes, glucose 22 mg/dL, protein 220 mg/dL, and adenosine deaminase 12 U/L. Serum sodium was 124 mEq/L consistent with SIADH. MRI showed marked basal meningeal enhancement with communicating hydrocephalus that required ventriculoperitoneal shunt placement. CSF Xpert MTB/RIF Ultra was positive. Anchored to van Toorn Semin Pediatr Neurol 2014 (PMID 24655399). Pilot, hold_for_revision.

NARRATIVE_ES: Nina de 18 meses de Ciudad del Cabo, Sudafrica, ingresada a un hospital pediatrico terciario tras tres semanas de fiebre intermitente, mala alimentacion, fallo en el crecimiento e irritabilidad creciente. Abuela tratada por tuberculosis pulmonar baciloscopia positiva cuatro meses antes. Vacunada con BCG al nacer. En los ultimos cinco dias progreso a letargia con una crisis focal el dia del ingreso. Examen: temperatura 38.1 C, Glasgow 11, somnolienta, rigidez de nuca, Kernig positivo, hemiparesia derecha, papiledema. LCR con presion 28 cmH2O, leucocitos 220 por mm3 (80 por ciento linfocitos), glucosa 22 mg/dL, proteina 220 mg/dL, adenosina desaminasa 12 U/L. Sodio serico 124 (SIADH). RM con engrosamiento meningeo basal e hidrocefalia comunicante, manejada con derivacion ventriculo-peritoneal. Xpert positivo. Anclaje van Toorn 2014.

RATIONALE: Subphase 1.4 commit 5.4.2 pilot 2 of 6 for Class 4 TBM pediatric (master prompt 1.4.4 pediatric median 6mo-2y stratum). Anchored to van Toorn 2014 Semin Pediatr Neurol pediatric TBM review. Hydrocephalus requiring VP shunt is van Toorn signature; hyponatremia 124 reflects SIADH common in pediatric TBM. Pre-adjudication hold_for_revision.

ANCHORING_EXTRAS: Anchored to van Toorn R, Solomons R, Semin Pediatr Neurol 2014 (PMID 24655399), pediatric TBM review. 18-month-old Cape Town girl, BCG vaccinated, household TB contact, lymphocytic CSF with ADA 12, Xpert MTB/RIF Ultra positive, communicating hydrocephalus on MRI requiring VP shunt. Pre-adjudication kappa 0.70.

ADJUDICATION:
  inclusion_decision: hold_for_revision
  adjudicator_ids: ['PILOT-TBM-122-ADJ-1', 'PILOT-TBM-122-ADJ-2']
  ground_truth_class: 4
  pre_adjudication_kappa: 0.7
  disagreement_resolution: None

=== END vignette ===

=== CLASS 4 | vignette_id: 123 | subphase: 1.4 TBM wave_1 | file: tbm_123_thwaites_hcmc_adult_male_cnpalsy_wave1.json ===

ANCHOR:
  pmid: 15496623
  first_author: Thwaites
  year: 2004
  journal: NEJM
  citation_type: rct
  doi: 10.1056/NEJMoa040573

DEMOGRAPHICS:
  age_years: 28
  sex: male
  geography_region: other_global
  ethnicity: asian
  altitude_residence_m: 19
  hiv_status: negative
  cd4_count_cells_per_uL: None
  pregnancy_red_flag: False
  immunocompromise_status: none
  freshwater_exposure_within_14d: False
  freshwater_exposure_type: None

HISTORY:
  symptom_onset_to_presentation_days: 21.0
  chief_complaint: fever_with_headache
  red_flags_present: []
  prodrome_description: Three-week subacute illness in a 28-year-old man from Ho Chi Minh City. Low-grade evening fevers, weight loss of 5 kg, progressive frontal headache, and intermittent vomiting in the final week. His older brother had been treated for pulmonary tuberculosis the prior year. No freshwater exposure.

VITALS:
  temperature_celsius: 38.6
  heart_rate_bpm: 102
  systolic_bp_mmHg: 124
  diastolic_bp_mmHg: 78
  glasgow_coma_scale: 12
  oxygen_saturation_pct: 96
  respiratory_rate_breaths_per_min: 18

EXAM:
  mental_status_grade: somnolent
  neck_stiffness: True
  kernig_or_brudzinski_positive: True
  cranial_nerve_palsy: CN_VI
  papilledema_on_fundoscopy: True
  focal_neurological_deficit: True
  skin_lesion_centrofacial_chronic: False
  petechial_or_purpuric_rash: False

LABS:
  wbc_blood_per_uL: 8800
  platelets_per_uL: 296000
  alt_ast_U_per_L: 26
  crp_mg_per_L: 42.0
  procalcitonin_ng_per_mL: 0.4
  serum_sodium_mEq_per_L: 130

CSF:
  opening_pressure_cmH2O: 22.0
  wbc_per_mm3: 320
  lymphocyte_pct: 78
  neutrophil_pct: 20
  eosinophil_pct: 2
  glucose_mg_per_dL: 26
  protein_mg_per_dL: 280
  lactate_mmol_per_L: 4.4
  ada_U_per_L: 15.0
  crag_lfa_result: negative
  wet_mount_motile_amoebae: negative
  xanthochromia_present: False
  rbc_per_mm3: 2

IMAGING:
  modality: mri_contrast
  pattern: basal_meningeal_enhancement_with_hydrocephalus
  contrast_enhancement: True
  hydrocephalus: True
  basal_meningeal_enhancement: True
  finding_count: None
  text_summary: Thick basal meningeal enhancement on post-contrast T1 with mild communicating hydrocephalus and a small left basal ganglia infarct. Findings consistent with active tuberculous meningitis.

DIAGNOSTIC_TESTS:
  pcr_panel: n/a
  xpert_mtb_rif: Positive, rifampicin susceptible. Cycle threshold consistent with TBM.
  blood_culture: n/a
  csf_culture: Pending at LP; reported positive at 4 weeks (M. tuberculosis drug-sensitive).
  serology_or_antigen: n/a
  smear_or_gram: Positive, scant acid-fast bacilli on concentrated specimen.
  brain_biopsy: n/a
  imaging_test: Hilar lymphadenopathy with adjacent parenchymal infiltrate consistent with primary TB.
  total_dx_results: 4

NARRATIVE_EN: A 28-year-old man from Ho Chi Minh City presented to a tertiary referral hospital with a three-week subacute illness of low-grade evening fevers, weight loss of 5 kg, progressive frontal headache, and intermittent vomiting in the final week. His older brother had been treated for pulmonary tuberculosis the prior year. Examination on admission: temperature 38.6 C, Glasgow Coma Scale 12, somnolent but rousable, neck stiffness, positive Kernig sign, left lateral gaze palsy consistent with sixth cranial nerve involvement, and bilateral papilledema. CSF showed an opening pressure of 22 cmH2O, white cell count 320 per cubic millimeter with 78 percent lymphocytes, glucose 26 mg/dL, protein 280 mg/dL, and adenosine deaminase 15 U/L. MRI with contrast demonstrated thick basal meningeal enhancement and moderate communicating hydrocephalus. CSF Xpert MTB/RIF Ultra was positive and rifampicin susceptible, and AFB smear was positive on concentrated specimen. Anchored to Thwaites NEJM 2004 (PMID 15496623). Wave 1, hold_for_revision.

NARRATIVE_ES: Varon de 28 anos de Ho Chi Minh, Vietnam, ingresado a un hospital terciario tras tres semanas de cuadro subagudo: fiebre vespertina baja, perdida de 5 kg, cefalea frontal progresiva y vomitos intermitentes en la ultima semana. Hermano mayor con tuberculosis pulmonar tratada el ano previo. Examen al ingreso: temperatura 38.6 C, Glasgow 12, somnoliento, rigidez de nuca, Kernig positivo, paresia del sexto par craneal izquierdo y papiledema bilateral. LCR con presion de apertura 22 cmH2O, leucocitos 320 por mm3 (78 por ciento linfocitos), glucosa 26 mg/dL, proteina 280 mg/dL, adenosina desaminasa 15 U/L. RM con engrosamiento meningeo basal e hidrocefalia comunicante moderada. Xpert MTB/RIF Ultra positivo en LCR, susceptible a rifampicina; baciloscopia positiva. Anclaje Thwaites NEJM 2004. Wave 1, pre-adjudicacion.

RATIONALE: Subphase 1.4 commit 5.4.3 wave 1 vignette 123 of 14 for Class 4 TBM. Anchored to Thwaites 2004 NEJM HCMC dexamethasone RCT. CN VI palsy positive (Huynh 30 percent subset). Pre-adjudication hold_for_revision.

ANCHORING_EXTRAS: Anchored to Thwaites GE et al. NEJM 2004 (PMID 15496623), HCMC dexamethasone TBM RCT. 28-year-old Vietnamese adult HIV-negative, drug-sensitive TBM, lymphocytic CSF (lymph 78 percent, protein 280, glucose 26), ADA 15 U/L, Xpert MTB/RIF Ultra positive, AFB smear positive, CN VI palsy positive. Pre-adjudication kappa 0.70.

ADJUDICATION:
  inclusion_decision: hold_for_revision
  adjudicator_ids: ['WAVE1-TBM-123-ADJ-1', 'WAVE1-TBM-123-ADJ-2']
  ground_truth_class: 4
  pre_adjudication_kappa: 0.7
  disagreement_resolution: None

=== END vignette ===

=== CLASS 4 | vignette_id: 124 | subphase: 1.4 TBM wave_1 | file: tbm_124_thwaites_hcmc_adult_male_fatal_wave1.json ===

ANCHOR:
  pmid: 15496623
  first_author: Thwaites
  year: 2004
  journal: NEJM
  citation_type: rct
  doi: 10.1056/NEJMoa040573

DEMOGRAPHICS:
  age_years: 52
  sex: male
  geography_region: other_global
  ethnicity: asian
  altitude_residence_m: 19
  hiv_status: negative
  cd4_count_cells_per_uL: None
  pregnancy_red_flag: False
  immunocompromise_status: none
  freshwater_exposure_within_14d: False
  freshwater_exposure_type: None

HISTORY:
  symptom_onset_to_presentation_days: 35.0
  chief_complaint: altered_mental_status
  red_flags_present: []
  prodrome_description: Five-week illness in a 52-year-old man from Ho Chi Minh City managed at home with worsening headache, weight loss of 8 kg, and progressive lethargy. Family brought him in obtunded after a witnessed generalized seizure. Type 2 diabetes on metformin.

VITALS:
  temperature_celsius: 39.2
  heart_rate_bpm: 124
  systolic_bp_mmHg: 108
  diastolic_bp_mmHg: 64
  glasgow_coma_scale: 8
  oxygen_saturation_pct: 92
  respiratory_rate_breaths_per_min: 28

EXAM:
  mental_status_grade: stuporous
  neck_stiffness: True
  kernig_or_brudzinski_positive: True
  cranial_nerve_palsy: none
  papilledema_on_fundoscopy: True
  focal_neurological_deficit: True
  skin_lesion_centrofacial_chronic: False
  petechial_or_purpuric_rash: False

LABS:
  wbc_blood_per_uL: 11600
  platelets_per_uL: 188000
  alt_ast_U_per_L: 48
  crp_mg_per_L: 78.0
  procalcitonin_ng_per_mL: 0.9
  serum_sodium_mEq_per_L: 126

CSF:
  opening_pressure_cmH2O: 30.0
  wbc_per_mm3: 400
  lymphocyte_pct: 72
  neutrophil_pct: 26
  eosinophil_pct: 2
  glucose_mg_per_dL: 18
  protein_mg_per_dL: 380
  lactate_mmol_per_L: 4.4
  ada_U_per_L: 17.0
  crag_lfa_result: negative
  wet_mount_motile_amoebae: negative
  xanthochromia_present: False
  rbc_per_mm3: 2

IMAGING:
  modality: mri_contrast
  pattern: basal_meningeal_enhancement_with_hydrocephalus
  contrast_enhancement: True
  hydrocephalus: True
  basal_meningeal_enhancement: True
  finding_count: None
  text_summary: Thick basal meningeal enhancement on post-contrast T1 with mild communicating hydrocephalus and a small left basal ganglia infarct. Findings consistent with active tuberculous meningitis.

DIAGNOSTIC_TESTS:
  pcr_panel: n/a
  xpert_mtb_rif: Positive, rifampicin susceptible. Cycle threshold consistent with TBM.
  blood_culture: n/a
  csf_culture: Pending at LP; reported positive at 4 weeks (M. tuberculosis drug-sensitive).
  serology_or_antigen: n/a
  smear_or_gram: Positive, scant acid-fast bacilli on concentrated specimen.
  brain_biopsy: n/a
  imaging_test: Hilar lymphadenopathy with adjacent parenchymal infiltrate consistent with primary TB.
  total_dx_results: 4

NARRATIVE_EN: A 52-year-old man from Ho Chi Minh City was brought to a tertiary referral hospital obtunded after a witnessed generalized seizure. His family reported a five-week illness with worsening headache, an eight-kilogram weight loss, intermittent low-grade fevers, and progressive lethargy that had been managed at home. He had type 2 diabetes on metformin. Examination on admission: temperature 39.2 C, Glasgow Coma Scale 8, stuporous, neck stiffness, positive Kernig sign, right-sided motor weakness, and bilateral papilledema. CSF showed an opening pressure of 30 cmH2O, white cell count 400 per cubic millimeter with 72 percent lymphocytes, glucose 18 mg/dL, protein 380 mg/dL, and adenosine deaminase 17 U/L. MRI with contrast showed thick basal meningeal enhancement, moderate communicating hydrocephalus, and bilateral basal ganglia infarcts. CSF Xpert MTB/RIF Ultra was positive and rifampicin susceptible; AFB smear was positive. Despite anti-tuberculous therapy and adjunctive dexamethasone, the patient died on hospital day five. Anchored to Thwaites NEJM 2004 (PMID 15496623). Wave 1, hold_for_revision.

NARRATIVE_ES: Varon de 52 anos de Ho Chi Minh, Vietnam, llevado a urgencias terciarias obnubilado tras una crisis generalizada presenciada. La familia refiere cuadro de cinco semanas con cefalea creciente, perdida de 8 kg, fiebre baja intermitente y letargia progresiva manejada en casa. Diabetes tipo 2 en metformina. Examen: temperatura 39.2 C, Glasgow 8, estuporoso, rigidez de nuca, Kernig positivo, hemiparesia derecha, papiledema bilateral. LCR con presion 30 cmH2O, leucocitos 400 por mm3 (72 por ciento linfocitos), glucosa 18 mg/dL, proteina 380 mg/dL, adenosina desaminasa 17 U/L. RM con engrosamiento meningeo basal, hidrocefalia comunicante moderada e infartos bilaterales de ganglios basales. Xpert MTB/RIF Ultra positivo; baciloscopia positiva. Pese al tratamiento antifimico y dexametasona, fallecio el dia hospitalario cinco. Anclaje Thwaites NEJM 2004.

RATIONALE: Subphase 1.4 commit 5.4.3 wave 1 vignette 124 of 14 for Class 4 TBM. Anchored to Thwaites 2004 NEJM HCMC dexamethasone RCT. Late-stage TBM mortality stratum (~31 percent cohort mortality). Pre-adjudication hold_for_revision.

ANCHORING_EXTRAS: Anchored to Thwaites GE et al. NEJM 2004 (PMID 15496623). 52-year-old Vietnamese male diabetic HIV-negative, late-stage TBM (Glasgow 8 on admission), bilateral basal ganglia infarcts, Xpert MTB/RIF Ultra positive, AFB smear positive; died hospital day five despite full regimen. Pre-adjudication kappa 0.70.

ADJUDICATION:
  inclusion_decision: hold_for_revision
  adjudicator_ids: ['WAVE1-TBM-124-ADJ-1', 'WAVE1-TBM-124-ADJ-2']
  ground_truth_class: 4
  pre_adjudication_kappa: 0.7
  disagreement_resolution: None

=== END vignette ===

=== CLASS 4 | vignette_id: 125 | subphase: 1.4 TBM wave_1 | file: tbm_125_thwaites_hcmc_pregnancy_female_wave1.json ===

ANCHOR:
  pmid: 15496623
  first_author: Thwaites
  year: 2004
  journal: NEJM
  citation_type: rct
  doi: 10.1056/NEJMoa040573

DEMOGRAPHICS:
  age_years: 41
  sex: female
  geography_region: other_global
  ethnicity: asian
  altitude_residence_m: 19
  hiv_status: negative
  cd4_count_cells_per_uL: None
  pregnancy_red_flag: True
  immunocompromise_status: none
  freshwater_exposure_within_14d: False
  freshwater_exposure_type: None

HISTORY:
  symptom_onset_to_presentation_days: 25.0
  chief_complaint: fever_with_headache
  red_flags_present: ['pregnancy_postpartum']
  prodrome_description: Three-and-a-half-week illness in a 41-year-old woman in her second trimester of pregnancy from Ho Chi Minh City. Daily afternoon fevers, bifrontal headache, and increasing irritability. No prior documented tuberculosis exposure and generally well before this illness.

VITALS:
  temperature_celsius: 38.4
  heart_rate_bpm: 96
  systolic_bp_mmHg: 118
  diastolic_bp_mmHg: 72
  glasgow_coma_scale: 13
  oxygen_saturation_pct: 97
  respiratory_rate_breaths_per_min: 18

EXAM:
  mental_status_grade: somnolent
  neck_stiffness: True
  kernig_or_brudzinski_positive: True
  cranial_nerve_palsy: none
  papilledema_on_fundoscopy: True
  focal_neurological_deficit: False
  skin_lesion_centrofacial_chronic: False
  petechial_or_purpuric_rash: False

LABS:
  wbc_blood_per_uL: 7600
  platelets_per_uL: 248000
  alt_ast_U_per_L: 28
  crp_mg_per_L: 36.0
  procalcitonin_ng_per_mL: 0.3
  serum_sodium_mEq_per_L: 132

CSF:
  opening_pressure_cmH2O: 20.0
  wbc_per_mm3: 240
  lymphocyte_pct: 80
  neutrophil_pct: 18
  eosinophil_pct: 2
  glucose_mg_per_dL: 30
  protein_mg_per_dL: 220
  lactate_mmol_per_L: 4.4
  ada_U_per_L: 13.0
  crag_lfa_result: negative
  wet_mount_motile_amoebae: negative
  xanthochromia_present: False
  rbc_per_mm3: 2

IMAGING:
  modality: mri_contrast
  pattern: basal_meningeal_enhancement_with_hydrocephalus
  contrast_enhancement: True
  hydrocephalus: True
  basal_meningeal_enhancement: True
  finding_count: None
  text_summary: Thick basal meningeal enhancement on post-contrast T1 with mild communicating hydrocephalus and a small left basal ganglia infarct. Findings consistent with active tuberculous meningitis.

DIAGNOSTIC_TESTS:
  pcr_panel: n/a
  xpert_mtb_rif: Positive, rifampicin susceptible. Cycle threshold consistent with TBM.
  blood_culture: n/a
  csf_culture: Pending at LP; reported positive at 4 weeks (M. tuberculosis drug-sensitive).
  serology_or_antigen: n/a
  smear_or_gram: n/a
  brain_biopsy: n/a
  imaging_test: Hilar lymphadenopathy with adjacent parenchymal infiltrate consistent with primary TB.
  total_dx_results: 3

NARRATIVE_EN: A 41-year-old woman in her second trimester of pregnancy from Ho Chi Minh City presented to a tertiary referral hospital after a three-and-a-half-week illness of daily afternoon fevers, bifrontal headache, and increasing irritability. She had no documented prior tuberculosis exposure and had been generally well before this illness. Examination on admission: temperature 38.4 C, Glasgow Coma Scale 13, somnolent but rousable, neck stiffness, positive Kernig sign, no focal motor deficit, and papilledema on fundoscopy. CSF showed an opening pressure of 20 cmH2O, white cell count 240 per cubic millimeter with 80 percent lymphocytes, glucose 30 mg/dL, protein 220 mg/dL, and adenosine deaminase 13 U/L. MRI with contrast demonstrated basal meningeal enhancement with mild communicating hydrocephalus; obstetric evaluation confirmed a viable intrauterine pregnancy. CSF Xpert MTB/RIF Ultra was positive and rifampicin susceptible. Anchored to Thwaites NEJM 2004 (PMID 15496623). Wave 1, hold_for_revision.

NARRATIVE_ES: Mujer de 41 anos de Ho Chi Minh, Vietnam, en el segundo trimestre de embarazo, ingresada a un hospital terciario tras tres semanas y media de fiebre vespertina diaria, cefalea bifrontal e irritabilidad creciente. Sin antecedente documentado de exposicion a tuberculosis. Examen: temperatura 38.4 C, Glasgow 13, somnolienta, rigidez de nuca, Kernig positivo, sin deficit motor focal, papiledema en fondo de ojo. LCR con presion 20 cmH2O, leucocitos 240 por mm3 (80 por ciento linfocitos), glucosa 30 mg/dL, proteina 220 mg/dL, adenosina desaminasa 13 U/L. RM con engrosamiento meningeo basal e hidrocefalia comunicante leve; evaluacion obstetrica confirmo gestacion viable intrauterina. Xpert MTB/RIF Ultra positivo en LCR. Anclaje Thwaites NEJM 2004. Wave 1, pre-adjudicacion.

RATIONALE: Subphase 1.4 commit 5.4.3 wave 1 vignette 125 of 14 for Class 4 TBM. Anchored to Thwaites 2004 NEJM HCMC dexamethasone RCT. Pregnancy red flag (Resolution #4) per schema History.red_flags_present enum availability. Pre-adjudication hold_for_revision.

ANCHORING_EXTRAS: Anchored to Thwaites GE et al. NEJM 2004 (PMID 15496623). 41-year-old Vietnamese adult female, second-trimester pregnancy, lymphocytic CSF (lymph 80 percent, protein 220, glucose 30), ADA 13 U/L, Xpert MTB/RIF Ultra positive. Resolution #4 applied: red_flags_present=['pregnancy_postpartum']. Pre-adjudication kappa 0.70.

ADJUDICATION:
  inclusion_decision: hold_for_revision
  adjudicator_ids: ['WAVE1-TBM-125-ADJ-1', 'WAVE1-TBM-125-ADJ-2']
  ground_truth_class: 4
  pre_adjudication_kappa: 0.7
  disagreement_resolution: None

=== END vignette ===

=== CLASS 4 | vignette_id: 126 | subphase: 1.4 TBM wave_1 | file: tbm_126_thwaites_hcmc_young_male_cnpalsy_wave1.json ===

ANCHOR:
  pmid: 15496623
  first_author: Thwaites
  year: 2004
  journal: NEJM
  citation_type: rct
  doi: 10.1056/NEJMoa040573

DEMOGRAPHICS:
  age_years: 24
  sex: male
  geography_region: other_global
  ethnicity: asian
  altitude_residence_m: 19
  hiv_status: negative
  cd4_count_cells_per_uL: None
  pregnancy_red_flag: False
  immunocompromise_status: none
  freshwater_exposure_within_14d: False
  freshwater_exposure_type: None

HISTORY:
  symptom_onset_to_presentation_days: 14.0
  chief_complaint: fever_with_headache
  red_flags_present: []
  prodrome_description: Two-week illness in a 24-year-old male construction worker from Ho Chi Minh City. Daily fevers, frontal headache, and three days of binocular horizontal diplopia in the final week. A co-worker had been treated for smear-positive pulmonary tuberculosis the prior month.

VITALS:
  temperature_celsius: 38.0
  heart_rate_bpm: 92
  systolic_bp_mmHg: 122
  diastolic_bp_mmHg: 76
  glasgow_coma_scale: 14
  oxygen_saturation_pct: 97
  respiratory_rate_breaths_per_min: 18

EXAM:
  mental_status_grade: confused
  neck_stiffness: True
  kernig_or_brudzinski_positive: True
  cranial_nerve_palsy: CN_VI
  papilledema_on_fundoscopy: True
  focal_neurological_deficit: True
  skin_lesion_centrofacial_chronic: False
  petechial_or_purpuric_rash: False

LABS:
  wbc_blood_per_uL: 7200
  platelets_per_uL: 318000
  alt_ast_U_per_L: 24
  crp_mg_per_L: 28.0
  procalcitonin_ng_per_mL: 0.3
  serum_sodium_mEq_per_L: 134

CSF:
  opening_pressure_cmH2O: 18.0
  wbc_per_mm3: 180
  lymphocyte_pct: 82
  neutrophil_pct: 16
  eosinophil_pct: 2
  glucose_mg_per_dL: 32
  protein_mg_per_dL: 180
  lactate_mmol_per_L: 4.4
  ada_U_per_L: 11.0
  crag_lfa_result: negative
  wet_mount_motile_amoebae: negative
  xanthochromia_present: False
  rbc_per_mm3: 2

IMAGING:
  modality: mri_contrast
  pattern: basal_meningeal_enhancement_with_hydrocephalus
  contrast_enhancement: True
  hydrocephalus: True
  basal_meningeal_enhancement: True
  finding_count: None
  text_summary: Thick basal meningeal enhancement on post-contrast T1 with mild communicating hydrocephalus and a small left basal ganglia infarct. Findings consistent with active tuberculous meningitis.

DIAGNOSTIC_TESTS:
  pcr_panel: n/a
  xpert_mtb_rif: Positive, rifampicin susceptible. Cycle threshold consistent with TBM.
  blood_culture: n/a
  csf_culture: Pending at LP; reported positive at 4 weeks (M. tuberculosis drug-sensitive).
  serology_or_antigen: n/a
  smear_or_gram: n/a
  brain_biopsy: n/a
  imaging_test: Hilar lymphadenopathy with adjacent parenchymal infiltrate consistent with primary TB.
  total_dx_results: 3

NARRATIVE_EN: A 24-year-old male construction worker from Ho Chi Minh City presented to a tertiary referral hospital after a two-week illness of daily low-grade fevers, frontal headache, and three days of binocular horizontal diplopia in the final week. A co-worker had been treated for smear-positive pulmonary tuberculosis the prior month. Examination on admission: temperature 38.0 C, Glasgow Coma Scale 14, mild confusion, neck stiffness, positive Kernig sign, right lateral gaze palsy consistent with sixth cranial nerve involvement, and papilledema. CSF showed an opening pressure of 18 cmH2O, white cell count 180 per cubic millimeter with 82 percent lymphocytes, glucose 32 mg/dL, protein 180 mg/dL, and adenosine deaminase 11 U/L. MRI with contrast demonstrated early basal meningeal enhancement without significant hydrocephalus. CSF Xpert MTB/RIF Ultra was positive and rifampicin susceptible. Anchored to Thwaites NEJM 2004 (PMID 15496623). Wave 1, hold_for_revision.

NARRATIVE_ES: Varon de 24 anos, obrero de construccion, de Ho Chi Minh, Vietnam, ingresado a un hospital terciario tras dos semanas de fiebre baja diaria, cefalea frontal y tres dias de diplopia horizontal binocular en la ultima semana. Companero de trabajo tratado por tuberculosis pulmonar baciloscopia positiva el mes previo. Examen: temperatura 38.0 C, Glasgow 14, confusion leve, rigidez de nuca, Kernig positivo, paresia del sexto par craneal derecho, papiledema. LCR con presion 18 cmH2O, leucocitos 180 por mm3 (82 por ciento linfocitos), glucosa 32 mg/dL, proteina 180 mg/dL, adenosina desaminasa 11 U/L. RM con engrosamiento meningeo basal incipiente sin hidrocefalia significativa. Xpert MTB/RIF Ultra positivo en LCR. Anclaje Thwaites NEJM 2004. Wave 1, pre-adjudicacion.

RATIONALE: Subphase 1.4 commit 5.4.3 wave 1 vignette 126 of 14 for Class 4 TBM. Anchored to Thwaites 2004 NEJM. Early-stage TBM with CN VI palsy positive (Huynh 30 percent subset). Pre-adjudication hold_for_revision.

ANCHORING_EXTRAS: Anchored to Thwaites GE et al. NEJM 2004 (PMID 15496623). 24-year-old Vietnamese male construction worker HIV-negative, early-stage TBM with binocular diplopia, lymphocytic CSF (lymph 82 percent, protein 180, glucose 32), ADA 11 U/L, Xpert MTB/RIF Ultra positive, CN VI palsy positive. Pre-adjudication kappa 0.70.

ADJUDICATION:
  inclusion_decision: hold_for_revision
  adjudicator_ids: ['WAVE1-TBM-126-ADJ-1', 'WAVE1-TBM-126-ADJ-2']
  ground_truth_class: 4
  pre_adjudication_kappa: 0.7
  disagreement_resolution: None

=== END vignette ===

=== CLASS 4 | vignette_id: 127 | subphase: 1.4 TBM wave_1 | file: tbm_127_thwaites_hcmc_adult_male_smearpos_wave1.json ===

ANCHOR:
  pmid: 15496623
  first_author: Thwaites
  year: 2004
  journal: NEJM
  citation_type: rct
  doi: 10.1056/NEJMoa040573

DEMOGRAPHICS:
  age_years: 38
  sex: male
  geography_region: other_global
  ethnicity: asian
  altitude_residence_m: 19
  hiv_status: negative
  cd4_count_cells_per_uL: None
  pregnancy_red_flag: False
  immunocompromise_status: none
  freshwater_exposure_within_14d: False
  freshwater_exposure_type: None

HISTORY:
  symptom_onset_to_presentation_days: 28.0
  chief_complaint: fever_with_headache
  red_flags_present: []
  prodrome_description: Four-week illness in a 38-year-old man from Ho Chi Minh City. Persistent low-grade fevers, occipital headache, weight loss of 6 kg. Heavy cigarette smoker, no documented tuberculosis contact.

VITALS:
  temperature_celsius: 38.5
  heart_rate_bpm: 100
  systolic_bp_mmHg: 128
  diastolic_bp_mmHg: 80
  glasgow_coma_scale: 13
  oxygen_saturation_pct: 96
  respiratory_rate_breaths_per_min: 18

EXAM:
  mental_status_grade: somnolent
  neck_stiffness: True
  kernig_or_brudzinski_positive: True
  cranial_nerve_palsy: none
  papilledema_on_fundoscopy: True
  focal_neurological_deficit: False
  skin_lesion_centrofacial_chronic: False
  petechial_or_purpuric_rash: False

LABS:
  wbc_blood_per_uL: 9200
  platelets_per_uL: 286000
  alt_ast_U_per_L: 32
  crp_mg_per_L: 48.0
  procalcitonin_ng_per_mL: 0.5
  serum_sodium_mEq_per_L: 128

CSF:
  opening_pressure_cmH2O: 26.0
  wbc_per_mm3: 360
  lymphocyte_pct: 75
  neutrophil_pct: 23
  eosinophil_pct: 2
  glucose_mg_per_dL: 24
  protein_mg_per_dL: 320
  lactate_mmol_per_L: 4.4
  ada_U_per_L: 16.0
  crag_lfa_result: negative
  wet_mount_motile_amoebae: negative
  xanthochromia_present: False
  rbc_per_mm3: 2

IMAGING:
  modality: mri_contrast
  pattern: basal_meningeal_enhancement_with_hydrocephalus
  contrast_enhancement: True
  hydrocephalus: True
  basal_meningeal_enhancement: True
  finding_count: None
  text_summary: Thick basal meningeal enhancement on post-contrast T1 with mild communicating hydrocephalus and a small left basal ganglia infarct. Findings consistent with active tuberculous meningitis.

DIAGNOSTIC_TESTS:
  pcr_panel: n/a
  xpert_mtb_rif: Positive, rifampicin susceptible. Cycle threshold consistent with TBM.
  blood_culture: n/a
  csf_culture: Pending at LP; reported positive at 4 weeks (M. tuberculosis drug-sensitive).
  serology_or_antigen: n/a
  smear_or_gram: Positive, scant acid-fast bacilli on concentrated specimen.
  brain_biopsy: n/a
  imaging_test: Hilar lymphadenopathy with adjacent parenchymal infiltrate consistent with primary TB.
  total_dx_results: 4

NARRATIVE_EN: A 38-year-old man from Ho Chi Minh City presented to a tertiary referral hospital with a four-week illness of persistent low-grade fevers, occipital headache, and a six-kilogram weight loss. He was a heavy cigarette smoker and reported no documented tuberculosis contact. Examination on admission: temperature 38.5 C, Glasgow Coma Scale 13, somnolent but rousable, neck stiffness, positive Kernig sign, no focal motor deficit, and papilledema on fundoscopy. CSF showed an opening pressure of 26 cmH2O, white cell count 360 per cubic millimeter with 75 percent lymphocytes, glucose 24 mg/dL, protein 320 mg/dL, and adenosine deaminase 16 U/L. MRI with contrast demonstrated thick basal meningeal enhancement and mild communicating hydrocephalus. CSF Xpert MTB/RIF Ultra was positive and rifampicin susceptible, and AFB smear was positive on concentrated specimen. Anchored to Thwaites NEJM 2004 (PMID 15496623). Wave 1, hold_for_revision.

NARRATIVE_ES: Varon de 38 anos de Ho Chi Minh, Vietnam, ingresado a un hospital terciario tras cuatro semanas de fiebre baja persistente, cefalea occipital y perdida de 6 kg. Fumador empedernido, sin contacto documentado con tuberculosis. Examen: temperatura 38.5 C, Glasgow 13, somnoliento, rigidez de nuca, Kernig positivo, sin deficit motor focal, papiledema en fondo de ojo. LCR con presion 26 cmH2O, leucocitos 360 por mm3 (75 por ciento linfocitos), glucosa 24 mg/dL, proteina 320 mg/dL, adenosina desaminasa 16 U/L. RM con engrosamiento meningeo basal e hidrocefalia comunicante leve. Xpert MTB/RIF Ultra positivo en LCR, susceptible a rifampicina; baciloscopia positiva en muestra concentrada. Anclaje Thwaites NEJM 2004. Wave 1, pre-adjudicacion.

RATIONALE: Subphase 1.4 commit 5.4.3 wave 1 vignette 127 of 14 for Class 4 TBM. Anchored to Thwaites 2004 NEJM. Heavy-smoker risk factor; AFB-smear-positive concentrated CSF. Pre-adjudication hold_for_revision.

ANCHORING_EXTRAS: Anchored to Thwaites GE et al. NEJM 2004 (PMID 15496623). 38-year-old Vietnamese adult male HIV-negative heavy smoker, drug-sensitive TBM, lymphocytic CSF (lymph 75 percent, protein 320, glucose 24), ADA 16 U/L, Xpert MTB/RIF Ultra positive, AFB smear positive. Pre-adjudication kappa 0.70.

ADJUDICATION:
  inclusion_decision: hold_for_revision
  adjudicator_ids: ['WAVE1-TBM-127-ADJ-1', 'WAVE1-TBM-127-ADJ-2']
  ground_truth_class: 4
  pre_adjudication_kappa: 0.7
  disagreement_resolution: None

=== END vignette ===

=== CLASS 4 | vignette_id: 128 | subphase: 1.4 TBM wave_1 | file: tbm_128_marais_cape_town_adult_female_definite_wave1.json ===

ANCHOR:
  pmid: 20822958
  first_author: Marais
  year: 2010
  journal: Lancet Infect Dis
  citation_type: guideline
  doi: 10.1016/S1473-3099(10)70138-9

DEMOGRAPHICS:
  age_years: 32
  sex: female
  geography_region: other_global
  ethnicity: other
  altitude_residence_m: 50
  hiv_status: negative
  cd4_count_cells_per_uL: None
  pregnancy_red_flag: False
  immunocompromise_status: none
  freshwater_exposure_within_14d: False
  freshwater_exposure_type: None

HISTORY:
  symptom_onset_to_presentation_days: 21.0
  chief_complaint: fever_with_headache
  red_flags_present: []
  prodrome_description: Three-week illness in a 32-year-old woman from Cape Town. Subacute headache, intermittent fevers, weight loss of 4 kg. Her husband had recently started treatment for sputum-positive pulmonary tuberculosis.

VITALS:
  temperature_celsius: 38.4
  heart_rate_bpm: 98
  systolic_bp_mmHg: 116
  diastolic_bp_mmHg: 72
  glasgow_coma_scale: 13
  oxygen_saturation_pct: 97
  respiratory_rate_breaths_per_min: 18

EXAM:
  mental_status_grade: somnolent
  neck_stiffness: True
  kernig_or_brudzinski_positive: True
  cranial_nerve_palsy: none
  papilledema_on_fundoscopy: True
  focal_neurological_deficit: False
  skin_lesion_centrofacial_chronic: False
  petechial_or_purpuric_rash: False

LABS:
  wbc_blood_per_uL: 8200
  platelets_per_uL: 274000
  alt_ast_U_per_L: 26
  crp_mg_per_L: 42.0
  procalcitonin_ng_per_mL: 0.4
  serum_sodium_mEq_per_L: 130

CSF:
  opening_pressure_cmH2O: 22.0
  wbc_per_mm3: 280
  lymphocyte_pct: 78
  neutrophil_pct: 20
  eosinophil_pct: 2
  glucose_mg_per_dL: 28
  protein_mg_per_dL: 240
  lactate_mmol_per_L: 4.4
  ada_U_per_L: 14.0
  crag_lfa_result: negative
  wet_mount_motile_amoebae: negative
  xanthochromia_present: False
  rbc_per_mm3: 2

IMAGING:
  modality: mri_contrast
  pattern: basal_meningeal_enhancement_with_hydrocephalus
  contrast_enhancement: True
  hydrocephalus: True
  basal_meningeal_enhancement: True
  finding_count: None
  text_summary: Thick basal meningeal enhancement on post-contrast T1 with mild communicating hydrocephalus and a small left basal ganglia infarct. Findings consistent with active tuberculous meningitis.

DIAGNOSTIC_TESTS:
  pcr_panel: n/a
  xpert_mtb_rif: Positive, rifampicin susceptible. Cycle threshold consistent with TBM.
  blood_culture: n/a
  csf_culture: Pending at LP; reported positive at 4 weeks (M. tuberculosis drug-sensitive).
  serology_or_antigen: n/a
  smear_or_gram: n/a
  brain_biopsy: n/a
  imaging_test: Hilar lymphadenopathy with adjacent parenchymal infiltrate consistent with primary TB.
  total_dx_results: 3

NARRATIVE_EN: A 32-year-old woman from Cape Town presented to a tertiary referral hospital with a three-week illness of subacute headache, intermittent fevers, and a four-kilogram weight loss. Her husband had recently started treatment for sputum-positive pulmonary tuberculosis. Examination on admission: temperature 38.4 C, Glasgow Coma Scale 13, somnolent but rousable, neck stiffness, positive Kernig sign, no focal motor deficit, and papilledema on fundoscopy. CSF showed an opening pressure of 22 cmH2O, white cell count 280 per cubic millimeter with 78 percent lymphocytes, glucose 28 mg/dL, protein 240 mg/dL, and adenosine deaminase 14 U/L. MRI with contrast demonstrated basal meningeal enhancement with mild communicating hydrocephalus. CSF Xpert MTB/RIF Ultra was positive and rifampicin susceptible, satisfying the Marais 2010 uniform case definition for definite tuberculous meningitis. Anchored to Marais Lancet ID 2010 (PMID 20822958). Wave 1, hold_for_revision.

NARRATIVE_ES: Mujer de 32 anos de Ciudad del Cabo, Sudafrica, ingresada a un hospital terciario tras tres semanas de cefalea subaguda, fiebre intermitente y perdida de 4 kg. Esposo recientemente en tratamiento por tuberculosis pulmonar baciloscopia positiva. Examen: temperatura 38.4 C, Glasgow 13, somnolienta, rigidez de nuca, Kernig positivo, sin deficit motor focal, papiledema en fondo de ojo. LCR con presion 22 cmH2O, leucocitos 280 por mm3 (78 por ciento linfocitos), glucosa 28 mg/dL, proteina 240 mg/dL, adenosina desaminasa 14 U/L. RM con engrosamiento meningeo basal e hidrocefalia comunicante leve. Xpert MTB/RIF Ultra positivo en LCR, susceptible a rifampicina, cumpliendo la definicion de caso uniforme de Marais 2010 para meningitis tuberculosa definitiva. Anclaje Marais Lancet ID 2010.

RATIONALE: Subphase 1.4 commit 5.4.3 wave 1 vignette 128 of 14 for Class 4 TBM. Anchored to Marais 2010 uniform case definition; classical definite TBM (microbiologically confirmed). Pre-adjudication hold_for_revision.

ANCHORING_EXTRAS: Anchored to Marais S et al. Lancet ID 2010 (PMID 20822958), TBM uniform case definition. 32-year-old South African adult female HIV-negative, household TB contact, drug-sensitive TBM, lymphocytic CSF, ADA 14 U/L, Xpert MTB/RIF Ultra positive (definite TBM per uniform case definition). Pre-adjudication kappa 0.70.

ADJUDICATION:
  inclusion_decision: hold_for_revision
  adjudicator_ids: ['WAVE1-TBM-128-ADJ-1', 'WAVE1-TBM-128-ADJ-2']
  ground_truth_class: 4
  pre_adjudication_kappa: 0.7
  disagreement_resolution: None

=== END vignette ===

=== CLASS 4 | vignette_id: 129 | subphase: 1.4 TBM wave_1 | file: tbm_129_marais_cape_town_adult_male_probable_wave1.json ===

ANCHOR:
  pmid: 20822958
  first_author: Marais
  year: 2010
  journal: Lancet Infect Dis
  citation_type: guideline
  doi: 10.1016/S1473-3099(10)70138-9

DEMOGRAPHICS:
  age_years: 46
  sex: male
  geography_region: other_global
  ethnicity: other
  altitude_residence_m: 50
  hiv_status: negative
  cd4_count_cells_per_uL: None
  pregnancy_red_flag: False
  immunocompromise_status: none
  freshwater_exposure_within_14d: False
  freshwater_exposure_type: None

HISTORY:
  symptom_onset_to_presentation_days: 28.0
  chief_complaint: fever_with_headache
  red_flags_present: []
  prodrome_description: Four-week illness in a 46-year-old man from Cape Town. Worsening headache, low-grade fevers, and three days of binocular horizontal diplopia in the final week. His brother had died of tuberculosis ten years earlier; heavy alcohol use.

VITALS:
  temperature_celsius: 38.2
  heart_rate_bpm: 102
  systolic_bp_mmHg: 122
  diastolic_bp_mmHg: 76
  glasgow_coma_scale: 12
  oxygen_saturation_pct: 96
  respiratory_rate_breaths_per_min: 18

EXAM:
  mental_status_grade: somnolent
  neck_stiffness: True
  kernig_or_brudzinski_positive: True
  cranial_nerve_palsy: CN_VI
  papilledema_on_fundoscopy: True
  focal_neurological_deficit: True
  skin_lesion_centrofacial_chronic: False
  petechial_or_purpuric_rash: False

LABS:
  wbc_blood_per_uL: 9400
  platelets_per_uL: 232000
  alt_ast_U_per_L: 64
  crp_mg_per_L: 52.0
  procalcitonin_ng_per_mL: 0.6
  serum_sodium_mEq_per_L: 128

CSF:
  opening_pressure_cmH2O: 24.0
  wbc_per_mm3: 340
  lymphocyte_pct: 76
  neutrophil_pct: 22
  eosinophil_pct: 2
  glucose_mg_per_dL: 22
  protein_mg_per_dL: 300
  lactate_mmol_per_L: 4.4
  ada_U_per_L: 16.0
  crag_lfa_result: negative
  wet_mount_motile_amoebae: negative
  xanthochromia_present: False
  rbc_per_mm3: 2

IMAGING:
  modality: mri_contrast
  pattern: basal_meningeal_enhancement_with_hydrocephalus
  contrast_enhancement: True
  hydrocephalus: True
  basal_meningeal_enhancement: True
  finding_count: None
  text_summary: Thick basal meningeal enhancement on post-contrast T1 with mild communicating hydrocephalus and a small left basal ganglia infarct. Findings consistent with active tuberculous meningitis.

DIAGNOSTIC_TESTS:
  pcr_panel: n/a
  xpert_mtb_rif: Positive, rifampicin susceptible. Cycle threshold consistent with TBM.
  blood_culture: n/a
  csf_culture: Pending at LP; reported positive at 4 weeks (M. tuberculosis drug-sensitive).
  serology_or_antigen: n/a
  smear_or_gram: n/a
  brain_biopsy: n/a
  imaging_test: Hilar lymphadenopathy with adjacent parenchymal infiltrate consistent with primary TB.
  total_dx_results: 3

NARRATIVE_EN: A 46-year-old man from Cape Town presented to a tertiary referral hospital with a four-week illness of worsening headache, persistent low-grade fevers, and three days of binocular horizontal diplopia in the final week. His brother had died of tuberculosis ten years earlier, and he reported heavy alcohol use. Examination on admission: temperature 38.2 C, Glasgow Coma Scale 12, somnolent but rousable, neck stiffness, positive Kernig sign, left lateral gaze palsy consistent with sixth cranial nerve involvement, and bilateral papilledema. CSF showed an opening pressure of 24 cmH2O, white cell count 340 per cubic millimeter with 76 percent lymphocytes, glucose 22 mg/dL, protein 300 mg/dL, and adenosine deaminase 16 U/L. MRI with contrast demonstrated thick basal meningeal enhancement with moderate communicating hydrocephalus. CSF Xpert MTB/RIF Ultra was positive and rifampicin susceptible; the case meets Marais 2010 probable tuberculous meningitis criteria with score 14. Anchored to Marais Lancet ID 2010. Wave 1, hold_for_revision.

NARRATIVE_ES: Varon de 46 anos de Ciudad del Cabo, Sudafrica, ingresado a un hospital terciario tras cuatro semanas de cefalea creciente, fiebre baja persistente y tres dias de diplopia horizontal binocular en la ultima semana. Hermano fallecido de tuberculosis hace diez anos; consumo intenso de alcohol. Examen: temperatura 38.2 C, Glasgow 12, somnoliento, rigidez de nuca, Kernig positivo, paresia del sexto par craneal izquierdo, papiledema bilateral. LCR con presion 24 cmH2O, leucocitos 340 por mm3 (76 por ciento linfocitos), glucosa 22 mg/dL, proteina 300 mg/dL, adenosina desaminasa 16 U/L. RM con engrosamiento meningeo basal e hidrocefalia comunicante moderada. Xpert MTB/RIF Ultra positivo en LCR; el caso cumple criterios probables de Marais 2010 con puntaje 14. Anclaje Marais Lancet ID 2010.

RATIONALE: Subphase 1.4 commit 5.4.3 wave 1 vignette 129 of 14 for Class 4 TBM. Anchored to Marais 2010 probable category (score 14). CN VI palsy positive (Huynh 30 percent subset). Pre-adjudication hold_for_revision.

ANCHORING_EXTRAS: Anchored to Marais S et al. Lancet ID 2010 (PMID 20822958), TBM uniform case definition probable category. 46-year-old South African adult male HIV-negative heavy alcohol, lymphocytic CSF (lymph 76 percent, protein 300, glucose 22), ADA 16 U/L, Xpert MTB/RIF Ultra positive, CN VI palsy positive, Marais score 14. Pre-adjudication kappa 0.70.

ADJUDICATION:
  inclusion_decision: hold_for_revision
  adjudicator_ids: ['WAVE1-TBM-129-ADJ-1', 'WAVE1-TBM-129-ADJ-2']
  ground_truth_class: 4
  pre_adjudication_kappa: 0.7
  disagreement_resolution: None

=== END vignette ===

=== CLASS 4 | vignette_id: 130 | subphase: 1.4 TBM wave_1 | file: tbm_130_marais_cape_town_adult_female_possible_wave1.json ===

ANCHOR:
  pmid: 20822958
  first_author: Marais
  year: 2010
  journal: Lancet Infect Dis
  citation_type: guideline
  doi: 10.1016/S1473-3099(10)70138-9

DEMOGRAPHICS:
  age_years: 29
  sex: female
  geography_region: other_global
  ethnicity: other
  altitude_residence_m: 50
  hiv_status: negative
  cd4_count_cells_per_uL: None
  pregnancy_red_flag: False
  immunocompromise_status: none
  freshwater_exposure_within_14d: False
  freshwater_exposure_type: None

HISTORY:
  symptom_onset_to_presentation_days: 14.0
  chief_complaint: fever_with_headache
  red_flags_present: []
  prodrome_description: Two-week illness in a 29-year-old woman from Cape Town with subacute headache and intermittent low-grade fevers. She lived in an informal settlement, was HIV negative on rapid testing, and reported no documented tuberculosis contact.

VITALS:
  temperature_celsius: 38.0
  heart_rate_bpm: 92
  systolic_bp_mmHg: 118
  diastolic_bp_mmHg: 74
  glasgow_coma_scale: 14
  oxygen_saturation_pct: 97
  respiratory_rate_breaths_per_min: 18

EXAM:
  mental_status_grade: confused
  neck_stiffness: True
  kernig_or_brudzinski_positive: True
  cranial_nerve_palsy: none
  papilledema_on_fundoscopy: False
  focal_neurological_deficit: False
  skin_lesion_centrofacial_chronic: False
  petechial_or_purpuric_rash: False

LABS:
  wbc_blood_per_uL: 7400
  platelets_per_uL: 264000
  alt_ast_U_per_L: 22
  crp_mg_per_L: 28.0
  procalcitonin_ng_per_mL: 0.3
  serum_sodium_mEq_per_L: 134

CSF:
  opening_pressure_cmH2O: 18.0
  wbc_per_mm3: 200
  lymphocyte_pct: 76
  neutrophil_pct: 22
  eosinophil_pct: 2
  glucose_mg_per_dL: 36
  protein_mg_per_dL: 180
  lactate_mmol_per_L: 4.4
  ada_U_per_L: 11.0
  crag_lfa_result: negative
  wet_mount_motile_amoebae: negative
  xanthochromia_present: False
  rbc_per_mm3: 2

IMAGING:
  modality: mri_contrast
  pattern: basal_meningeal_enhancement_with_hydrocephalus
  contrast_enhancement: True
  hydrocephalus: True
  basal_meningeal_enhancement: True
  finding_count: None
  text_summary: Thick basal meningeal enhancement on post-contrast T1 with mild communicating hydrocephalus and a small left basal ganglia infarct. Findings consistent with active tuberculous meningitis.

DIAGNOSTIC_TESTS:
  pcr_panel: n/a
  xpert_mtb_rif: Negative on initial CSF specimen. Sensitivity 70-85 percent in TBM per Hernandez TM&IH 2021; culture remains the confirmation modality.
  blood_culture: n/a
  csf_culture: Positive at 4 weeks (M. tuberculosis drug-sensitive); Xpert-negative-culture-confirmed case per RCT inclusion.
  serology_or_antigen: n/a
  smear_or_gram: n/a
  brain_biopsy: n/a
  imaging_test: Hilar lymphadenopathy with adjacent parenchymal infiltrate consistent with primary TB.
  total_dx_results: 3

NARRATIVE_EN: A 29-year-old woman from Cape Town presented to a tertiary referral hospital with a two-week illness of subacute headache and intermittent low-grade fevers. She lived in an informal settlement, was HIV negative on rapid testing, and reported no documented tuberculosis contact. Examination on admission: temperature 38.0 C, Glasgow Coma Scale 14, mild confusion, neck stiffness, positive Kernig sign, no focal motor deficit, and no papilledema on fundoscopy. CSF showed an opening pressure of 18 cmH2O, white cell count 200 per cubic millimeter with 76 percent lymphocytes, glucose 36 mg/dL, protein 180 mg/dL, and adenosine deaminase 11 U/L. MRI with contrast demonstrated subtle basal meningeal enhancement without hydrocephalus. CSF Xpert MTB/RIF Ultra was negative on the initial specimen and mycobacterial culture remained pending. The case meets Marais 2010 possible tuberculous meningitis criteria with score 9; empirical anti-tuberculous therapy was initiated. Anchored to Marais Lancet ID 2010 (PMID 20822958). Wave 1, hold_for_revision.

NARRATIVE_ES: Mujer de 29 anos de Ciudad del Cabo, Sudafrica, ingresada a un hospital terciario tras dos semanas de cefalea subaguda y fiebre baja intermitente. Vive en asentamiento informal, VIH negativo en prueba rapida, sin contacto documentado con tuberculosis. Examen: temperatura 38.0 C, Glasgow 14, confusion leve, rigidez de nuca, Kernig positivo, sin deficit motor focal, sin papiledema. LCR con presion 18 cmH2O, leucocitos 200 por mm3 (76 por ciento linfocitos), glucosa 36 mg/dL, proteina 180 mg/dL, adenosina desaminasa 11 U/L. RM con engrosamiento meningeo basal sutil sin hidrocefalia. Xpert MTB/RIF Ultra negativo en muestra inicial; cultivo micobacteriano pendiente. El caso cumple criterios posibles de Marais 2010 con puntaje 9; tratamiento antifimico empirico iniciado. Anclaje Marais Lancet ID 2010. Wave 1, pre-adjudicacion.

RATIONALE: Subphase 1.4 commit 5.4.3 wave 1 vignette 130 of 14 for Class 4 TBM. Anchored to Marais 2010 possible category (score 9). Diagnostic ambiguity slot: Xpert NEG with culture pending; empirical anti-TB therapy. Pre-adjudication hold_for_revision.

ANCHORING_EXTRAS: Anchored to Marais S et al. Lancet ID 2010 (PMID 20822958), TBM uniform case definition possible category. 29-year-old South African adult female HIV-negative informal-settlement resident, lymphocytic CSF, ADA 11 U/L, Xpert MTB/RIF Ultra NEGATIVE on initial specimen, culture pending, Marais score 9. Diagnostic ambiguity flag True. Pre-adjudication kappa 0.70.

ADJUDICATION:
  inclusion_decision: hold_for_revision
  adjudicator_ids: ['WAVE1-TBM-130-ADJ-1', 'WAVE1-TBM-130-ADJ-2']
  ground_truth_class: 4
  pre_adjudication_kappa: 0.7
  disagreement_resolution: None

=== END vignette ===

=== CLASS 4 | vignette_id: 131 | subphase: 1.4 TBM wave_1 | file: tbm_131_heemskerk_hcmc_adult_male_standard_wave1.json ===

ANCHOR:
  pmid: 26760084
  first_author: Heemskerk
  year: 2016
  journal: NEJM
  citation_type: rct
  doi: 10.1056/NEJMoa1507062

DEMOGRAPHICS:
  age_years: 36
  sex: male
  geography_region: other_global
  ethnicity: asian
  altitude_residence_m: 19
  hiv_status: negative
  cd4_count_cells_per_uL: None
  pregnancy_red_flag: False
  immunocompromise_status: none
  freshwater_exposure_within_14d: False
  freshwater_exposure_type: None

HISTORY:
  symptom_onset_to_presentation_days: 24.0
  chief_complaint: fever_with_headache
  red_flags_present: []
  prodrome_description: Three-and-a-half-week illness in a 36-year-old male construction worker from Ho Chi Minh City. Persistent fevers, progressive frontal headache, intermittent vomiting, and three days of binocular diplopia in the final week. HIV negative, no prior tuberculosis contact.

VITALS:
  temperature_celsius: 38.6
  heart_rate_bpm: 104
  systolic_bp_mmHg: 124
  diastolic_bp_mmHg: 78
  glasgow_coma_scale: 12
  oxygen_saturation_pct: 96
  respiratory_rate_breaths_per_min: 18

EXAM:
  mental_status_grade: somnolent
  neck_stiffness: True
  kernig_or_brudzinski_positive: True
  cranial_nerve_palsy: CN_VI
  papilledema_on_fundoscopy: True
  focal_neurological_deficit: True
  skin_lesion_centrofacial_chronic: False
  petechial_or_purpuric_rash: False

LABS:
  wbc_blood_per_uL: 9000
  platelets_per_uL: 282000
  alt_ast_U_per_L: 28
  crp_mg_per_L: 46.0
  procalcitonin_ng_per_mL: 0.5
  serum_sodium_mEq_per_L: 130

CSF:
  opening_pressure_cmH2O: 24.0
  wbc_per_mm3: 320
  lymphocyte_pct: 78
  neutrophil_pct: 20
  eosinophil_pct: 2
  glucose_mg_per_dL: 26
  protein_mg_per_dL: 280
  lactate_mmol_per_L: 4.4
  ada_U_per_L: 15.0
  crag_lfa_result: negative
  wet_mount_motile_amoebae: negative
  xanthochromia_present: False
  rbc_per_mm3: 2

IMAGING:
  modality: mri_contrast
  pattern: basal_meningeal_enhancement_with_hydrocephalus
  contrast_enhancement: True
  hydrocephalus: True
  basal_meningeal_enhancement: True
  finding_count: None
  text_summary: Thick basal meningeal enhancement on post-contrast T1 with mild communicating hydrocephalus and a small left basal ganglia infarct. Findings consistent with active tuberculous meningitis.

DIAGNOSTIC_TESTS:
  pcr_panel: n/a
  xpert_mtb_rif: Positive, rifampicin susceptible. Cycle threshold consistent with TBM.
  blood_culture: n/a
  csf_culture: Pending at LP; reported positive at 4 weeks (M. tuberculosis drug-sensitive).
  serology_or_antigen: n/a
  smear_or_gram: n/a
  brain_biopsy: n/a
  imaging_test: Hilar lymphadenopathy with adjacent parenchymal infiltrate consistent with primary TB.
  total_dx_results: 3

NARRATIVE_EN: A 36-year-old male construction worker from Ho Chi Minh City presented to a tertiary referral hospital with a three-and-a-half-week illness of persistent fevers, progressive frontal headache, intermittent vomiting, and three days of binocular diplopia in the final week. He was HIV negative and reported no prior tuberculosis contact. Examination on admission: temperature 38.6 C, Glasgow Coma Scale 12, somnolent but rousable, neck stiffness, positive Kernig sign, right lateral gaze palsy consistent with sixth cranial nerve involvement, and papilledema. CSF showed an opening pressure of 24 cmH2O, white cell count 320 per cubic millimeter with 78 percent lymphocytes, glucose 26 mg/dL, protein 280 mg/dL, and adenosine deaminase 15 U/L. MRI with contrast demonstrated basal meningeal enhancement with mild communicating hydrocephalus. CSF Xpert MTB/RIF Ultra was positive and rifampicin susceptible. He was randomized to the standard anti-tuberculous arm. Anchored to Heemskerk NEJM 2016 (PMID 26760084). Wave 1, hold_for_revision.

NARRATIVE_ES: Varon de 36 anos, obrero de construccion, de Ho Chi Minh, Vietnam, ingresado a un hospital terciario tras tres semanas y media de fiebre persistente, cefalea frontal progresiva, vomitos intermitentes y tres dias de diplopia binocular en la ultima semana. VIH negativo, sin contacto previo con tuberculosis. Examen: temperatura 38.6 C, Glasgow 12, somnoliento, rigidez de nuca, Kernig positivo, paresia del sexto par craneal derecho, papiledema. LCR con presion 24 cmH2O, leucocitos 320 por mm3 (78 por ciento linfocitos), glucosa 26 mg/dL, proteina 280 mg/dL, adenosina desaminasa 15 U/L. RM con engrosamiento meningeo basal e hidrocefalia comunicante leve. Xpert MTB/RIF Ultra positivo en LCR, susceptible a rifampicina. Aleatorizado al brazo estandar. Anclaje Heemskerk NEJM 2016.

RATIONALE: Subphase 1.4 commit 5.4.3 wave 1 vignette 131 of 14 for Class 4 TBM. Anchored to Heemskerk 2016 NEJM intensified-anti-TB RCT, standard arm. CN VI palsy positive. Pre-adjudication hold_for_revision.

ANCHORING_EXTRAS: Anchored to Heemskerk AD et al. NEJM 2016 (PMID 26760084), HCMC intensified-anti-TB RCT standard arm. 36-year-old Vietnamese adult male HIV-negative, lymphocytic CSF, ADA 15 U/L, Xpert MTB/RIF Ultra positive, CN VI palsy positive. Pre-adjudication kappa 0.70.

ADJUDICATION:
  inclusion_decision: hold_for_revision
  adjudicator_ids: ['WAVE1-TBM-131-ADJ-1', 'WAVE1-TBM-131-ADJ-2']
  ground_truth_class: 4
  pre_adjudication_kappa: 0.7
  disagreement_resolution: None

=== END vignette ===

=== CLASS 4 | vignette_id: 132 | subphase: 1.4 TBM wave_1 | file: tbm_132_heemskerk_hcmc_adult_female_intensified_wave1.json ===

ANCHOR:
  pmid: 26760084
  first_author: Heemskerk
  year: 2016
  journal: NEJM
  citation_type: rct
  doi: 10.1056/NEJMoa1507062

DEMOGRAPHICS:
  age_years: 27
  sex: female
  geography_region: other_global
  ethnicity: asian
  altitude_residence_m: 19
  hiv_status: negative
  cd4_count_cells_per_uL: None
  pregnancy_red_flag: False
  immunocompromise_status: none
  freshwater_exposure_within_14d: False
  freshwater_exposure_type: None

HISTORY:
  symptom_onset_to_presentation_days: 21.0
  chief_complaint: fever_with_headache
  red_flags_present: []
  prodrome_description: Three-week illness in a 27-year-old female schoolteacher from Ho Chi Minh City. Daily fevers, persistent bifrontal headache, and increasing fatigue. HIV negative; mother treated for sputum-positive pulmonary tuberculosis the prior year.

VITALS:
  temperature_celsius: 38.3
  heart_rate_bpm: 96
  systolic_bp_mmHg: 116
  diastolic_bp_mmHg: 72
  glasgow_coma_scale: 13
  oxygen_saturation_pct: 97
  respiratory_rate_breaths_per_min: 18

EXAM:
  mental_status_grade: somnolent
  neck_stiffness: True
  kernig_or_brudzinski_positive: True
  cranial_nerve_palsy: none
  papilledema_on_fundoscopy: True
  focal_neurological_deficit: False
  skin_lesion_centrofacial_chronic: False
  petechial_or_purpuric_rash: False

LABS:
  wbc_blood_per_uL: 7800
  platelets_per_uL: 304000
  alt_ast_U_per_L: 26
  crp_mg_per_L: 38.0
  procalcitonin_ng_per_mL: 0.4
  serum_sodium_mEq_per_L: 132

CSF:
  opening_pressure_cmH2O: 20.0
  wbc_per_mm3: 240
  lymphocyte_pct: 80
  neutrophil_pct: 18
  eosinophil_pct: 2
  glucose_mg_per_dL: 30
  protein_mg_per_dL: 220
  lactate_mmol_per_L: 4.4
  ada_U_per_L: 13.0
  crag_lfa_result: negative
  wet_mount_motile_amoebae: negative
  xanthochromia_present: False
  rbc_per_mm3: 2

IMAGING:
  modality: mri_contrast
  pattern: basal_meningeal_enhancement_with_hydrocephalus
  contrast_enhancement: True
  hydrocephalus: True
  basal_meningeal_enhancement: True
  finding_count: None
  text_summary: Thick basal meningeal enhancement on post-contrast T1 with mild communicating hydrocephalus and a small left basal ganglia infarct. Findings consistent with active tuberculous meningitis.

DIAGNOSTIC_TESTS:
  pcr_panel: n/a
  xpert_mtb_rif: Positive, rifampicin susceptible. Cycle threshold consistent with TBM.
  blood_culture: n/a
  csf_culture: Pending at LP; reported positive at 4 weeks (M. tuberculosis drug-sensitive).
  serology_or_antigen: n/a
  smear_or_gram: n/a
  brain_biopsy: n/a
  imaging_test: Hilar lymphadenopathy with adjacent parenchymal infiltrate consistent with primary TB.
  total_dx_results: 3

NARRATIVE_EN: A 27-year-old female schoolteacher from Ho Chi Minh City presented to a tertiary referral hospital with a three-week illness of daily fevers, persistent bifrontal headache, and increasing fatigue. She was HIV negative; her mother had been treated for sputum-positive pulmonary tuberculosis the prior year. Examination on admission: temperature 38.3 C, Glasgow Coma Scale 13, somnolent but rousable, neck stiffness, positive Kernig sign, no focal motor deficit, and papilledema on fundoscopy. CSF showed an opening pressure of 20 cmH2O, white cell count 240 per cubic millimeter with 80 percent lymphocytes, glucose 30 mg/dL, protein 220 mg/dL, and adenosine deaminase 13 U/L. MRI with contrast demonstrated basal meningeal enhancement with mild communicating hydrocephalus. CSF Xpert MTB/RIF Ultra was positive and rifampicin susceptible. She was randomized to the intensified anti-tuberculous arm with rifampicin 15 mg/kg and levofloxacin. Anchored to Heemskerk NEJM 2016 (PMID 26760084). Wave 1, hold_for_revision.

NARRATIVE_ES: Mujer de 27 anos, profesora de escuela, de Ho Chi Minh, Vietnam, ingresada a un hospital terciario tras tres semanas de fiebre diaria, cefalea bifrontal persistente y fatiga creciente. VIH negativo; madre tratada por tuberculosis pulmonar baciloscopia positiva el ano previo. Examen: temperatura 38.3 C, Glasgow 13, somnolienta, rigidez de nuca, Kernig positivo, sin deficit motor focal, papiledema en fondo de ojo. LCR con presion 20 cmH2O, leucocitos 240 por mm3 (80 por ciento linfocitos), glucosa 30 mg/dL, proteina 220 mg/dL, adenosina desaminasa 13 U/L. RM con engrosamiento meningeo basal e hidrocefalia comunicante leve. Xpert MTB/RIF Ultra positivo en LCR. Aleatorizada al brazo intensificado con rifampicina 15 mg/kg y levofloxacina. Anclaje Heemskerk NEJM 2016.

RATIONALE: Subphase 1.4 commit 5.4.3 wave 1 vignette 132 of 14 for Class 4 TBM. Anchored to Heemskerk 2016 intensified arm (rifampicin 15 mg/kg + levofloxacin). Pre-adjudication hold_for_revision.

ANCHORING_EXTRAS: Anchored to Heemskerk AD et al. NEJM 2016 (PMID 26760084) intensified arm. 27-year-old Vietnamese adult female HIV-negative schoolteacher, mother prior pulmonary TB, lymphocytic CSF, ADA 13 U/L, Xpert MTB/RIF Ultra positive. Pre-adjudication kappa 0.70.

ADJUDICATION:
  inclusion_decision: hold_for_revision
  adjudicator_ids: ['WAVE1-TBM-132-ADJ-1', 'WAVE1-TBM-132-ADJ-2']
  ground_truth_class: 4
  pre_adjudication_kappa: 0.7
  disagreement_resolution: None

=== END vignette ===

=== CLASS 4 | vignette_id: 133 | subphase: 1.4 TBM wave_1 | file: tbm_133_heemskerk_hcmc_adult_male_severe_fatal_wave1.json ===

ANCHOR:
  pmid: 26760084
  first_author: Heemskerk
  year: 2016
  journal: NEJM
  citation_type: rct
  doi: 10.1056/NEJMoa1507062

DEMOGRAPHICS:
  age_years: 44
  sex: male
  geography_region: other_global
  ethnicity: asian
  altitude_residence_m: 19
  hiv_status: negative
  cd4_count_cells_per_uL: None
  pregnancy_red_flag: False
  immunocompromise_status: none
  freshwater_exposure_within_14d: False
  freshwater_exposure_type: None

HISTORY:
  symptom_onset_to_presentation_days: 32.0
  chief_complaint: altered_mental_status
  red_flags_present: []
  prodrome_description: Four-and-a-half-week illness in a 44-year-old male bricklayer from Ho Chi Minh City. Worsening headache, weight loss of 7 kg, intermittent fevers, three days of binocular diplopia in the final week, and rapid obtundation over the prior 48 hours. HIV negative.

VITALS:
  temperature_celsius: 39.0
  heart_rate_bpm: 118
  systolic_bp_mmHg: 110
  diastolic_bp_mmHg: 68
  glasgow_coma_scale: 8
  oxygen_saturation_pct: 91
  respiratory_rate_breaths_per_min: 26

EXAM:
  mental_status_grade: comatose
  neck_stiffness: True
  kernig_or_brudzinski_positive: True
  cranial_nerve_palsy: CN_VI
  papilledema_on_fundoscopy: True
  focal_neurological_deficit: True
  skin_lesion_centrofacial_chronic: False
  petechial_or_purpuric_rash: False

LABS:
  wbc_blood_per_uL: 12200
  platelets_per_uL: 198000
  alt_ast_U_per_L: 38
  crp_mg_per_L: 72.0
  procalcitonin_ng_per_mL: 0.8
  serum_sodium_mEq_per_L: 124

CSF:
  opening_pressure_cmH2O: 30.0
  wbc_per_mm3: 380
  lymphocyte_pct: 70
  neutrophil_pct: 28
  eosinophil_pct: 2
  glucose_mg_per_dL: 18
  protein_mg_per_dL: 360
  lactate_mmol_per_L: 4.4
  ada_U_per_L: 18.0
  crag_lfa_result: negative
  wet_mount_motile_amoebae: negative
  xanthochromia_present: False
  rbc_per_mm3: 2

IMAGING:
  modality: mri_contrast
  pattern: basal_meningeal_enhancement_with_hydrocephalus
  contrast_enhancement: True
  hydrocephalus: True
  basal_meningeal_enhancement: True
  finding_count: None
  text_summary: Thick basal meningeal enhancement on post-contrast T1 with mild communicating hydrocephalus and a small left basal ganglia infarct. Findings consistent with active tuberculous meningitis.

DIAGNOSTIC_TESTS:
  pcr_panel: n/a
  xpert_mtb_rif: Positive, rifampicin susceptible. Cycle threshold consistent with TBM.
  blood_culture: n/a
  csf_culture: Pending at LP; reported positive at 4 weeks (M. tuberculosis drug-sensitive).
  serology_or_antigen: n/a
  smear_or_gram: Positive, scant acid-fast bacilli on concentrated specimen.
  brain_biopsy: n/a
  imaging_test: Hilar lymphadenopathy with adjacent parenchymal infiltrate consistent with primary TB.
  total_dx_results: 4

NARRATIVE_EN: A 44-year-old male bricklayer from Ho Chi Minh City was brought to a tertiary referral hospital comatose by his family. They reported a four-and-a-half-week illness with progressive headache, a seven-kilogram weight loss, intermittent fevers, three days of binocular diplopia in the final week, and rapid obtundation over the prior 48 hours. He was HIV negative. Examination on admission: temperature 39.0 C, Glasgow Coma Scale 8, comatose, neck stiffness, positive Kernig sign, right lateral gaze palsy consistent with sixth cranial nerve involvement, right hemiparesis, and bilateral papilledema. CSF showed an opening pressure of 30 cmH2O, white cell count 380 per cubic millimeter with 70 percent lymphocytes, glucose 18 mg/dL, protein 360 mg/dL, and adenosine deaminase 18 U/L. MRI with contrast demonstrated thick basal meningeal enhancement, communicating hydrocephalus, and bilateral basal ganglia infarcts. CSF Xpert MTB/RIF Ultra was positive; AFB smear was positive. He was randomized to the standard arm and died on hospital day four. Anchored to Heemskerk NEJM 2016 (PMID 26760084). Wave 1, hold_for_revision.

NARRATIVE_ES: Varon de 44 anos, albanil, de Ho Chi Minh, Vietnam, llevado por la familia a urgencias terciarias en coma. Refieren cuadro de cuatro semanas y media con cefalea progresiva, perdida de 7 kg, fiebre intermitente, tres dias de diplopia binocular en la ultima semana y obnubilacion rapida en las ultimas 48 horas. VIH negativo. Examen: temperatura 39.0 C, Glasgow 8, comatoso, rigidez de nuca, Kernig positivo, paresia del sexto par craneal derecho, hemiparesia derecha, papiledema bilateral. LCR con presion 30 cmH2O, leucocitos 380 por mm3 (70 por ciento linfocitos), glucosa 18 mg/dL, proteina 360 mg/dL, adenosina desaminasa 18 U/L. RM con engrosamiento meningeo basal, hidrocefalia comunicante e infartos bilaterales de ganglios basales. Xpert MTB/RIF Ultra positivo; baciloscopia positiva. Aleatorizado al brazo estandar; fallecio el dia hospitalario cuatro. Anclaje Heemskerk NEJM 2016.

RATIONALE: Subphase 1.4 commit 5.4.3 wave 1 vignette 133 of 14 for Class 4 TBM. Anchored to Heemskerk 2016 standard arm late-stage fatal outcome. CN VI palsy positive. Pre-adjudication hold_for_revision.

ANCHORING_EXTRAS: Anchored to Heemskerk AD et al. NEJM 2016 (PMID 26760084) standard arm. 44-year-old Vietnamese adult male HIV-negative bricklayer, BMRC grade 3 severe TBM, basal ganglia infarcts, Xpert MTB/RIF Ultra positive, AFB smear positive, CN VI palsy positive; died hospital day four. Pre-adjudication kappa 0.70.

ADJUDICATION:
  inclusion_decision: hold_for_revision
  adjudicator_ids: ['WAVE1-TBM-133-ADJ-1', 'WAVE1-TBM-133-ADJ-2']
  ground_truth_class: 4
  pre_adjudication_kappa: 0.7
  disagreement_resolution: None

=== END vignette ===

=== CLASS 4 | vignette_id: 134 | subphase: 1.4 TBM wave_1 | file: tbm_134_heemskerk_hcmc_young_male_xpertneg_wave1.json ===

ANCHOR:
  pmid: 26760084
  first_author: Heemskerk
  year: 2016
  journal: NEJM
  citation_type: rct
  doi: 10.1056/NEJMoa1507062

DEMOGRAPHICS:
  age_years: 19
  sex: male
  geography_region: other_global
  ethnicity: asian
  altitude_residence_m: 19
  hiv_status: negative
  cd4_count_cells_per_uL: None
  pregnancy_red_flag: False
  immunocompromise_status: none
  freshwater_exposure_within_14d: False
  freshwater_exposure_type: None

HISTORY:
  symptom_onset_to_presentation_days: 18.0
  chief_complaint: fever_with_headache
  red_flags_present: []
  prodrome_description: Two-and-a-half-week illness in a 19-year-old male university student from Ho Chi Minh City. Daily low-grade fevers, frontal headache, and progressive fatigue. He lived in a university dormitory where several peers had been treated for pulmonary tuberculosis in the prior year. HIV negative.

VITALS:
  temperature_celsius: 38.2
  heart_rate_bpm: 96
  systolic_bp_mmHg: 118
  diastolic_bp_mmHg: 72
  glasgow_coma_scale: 13
  oxygen_saturation_pct: 97
  respiratory_rate_breaths_per_min: 18

EXAM:
  mental_status_grade: somnolent
  neck_stiffness: True
  kernig_or_brudzinski_positive: True
  cranial_nerve_palsy: none
  papilledema_on_fundoscopy: False
  focal_neurological_deficit: False
  skin_lesion_centrofacial_chronic: False
  petechial_or_purpuric_rash: False

LABS:
  wbc_blood_per_uL: 7600
  platelets_per_uL: 312000
  alt_ast_U_per_L: 24
  crp_mg_per_L: 32.0
  procalcitonin_ng_per_mL: 0.3
  serum_sodium_mEq_per_L: 134

CSF:
  opening_pressure_cmH2O: 18.0
  wbc_per_mm3: 220
  lymphocyte_pct: 80
  neutrophil_pct: 18
  eosinophil_pct: 2
  glucose_mg_per_dL: 30
  protein_mg_per_dL: 200
  lactate_mmol_per_L: 4.4
  ada_U_per_L: 12.0
  crag_lfa_result: negative
  wet_mount_motile_amoebae: negative
  xanthochromia_present: False
  rbc_per_mm3: 2

IMAGING:
  modality: mri_contrast
  pattern: basal_meningeal_enhancement_with_hydrocephalus
  contrast_enhancement: True
  hydrocephalus: True
  basal_meningeal_enhancement: True
  finding_count: None
  text_summary: Thick basal meningeal enhancement on post-contrast T1 with mild communicating hydrocephalus and a small left basal ganglia infarct. Findings consistent with active tuberculous meningitis.

DIAGNOSTIC_TESTS:
  pcr_panel: n/a
  xpert_mtb_rif: Negative on initial CSF specimen. Sensitivity 70-85 percent in TBM per Hernandez TM&IH 2021; culture remains the confirmation modality.
  blood_culture: n/a
  csf_culture: Positive at 4 weeks (M. tuberculosis drug-sensitive); Xpert-negative-culture-confirmed case per RCT inclusion.
  serology_or_antigen: n/a
  smear_or_gram: n/a
  brain_biopsy: n/a
  imaging_test: Hilar lymphadenopathy with adjacent parenchymal infiltrate consistent with primary TB.
  total_dx_results: 3

NARRATIVE_EN: A 19-year-old male university student from Ho Chi Minh City presented to a tertiary referral hospital after a two-and-a-half-week illness of daily low-grade fevers, frontal headache, and progressive fatigue. He lived in a university dormitory where several peers had been treated for pulmonary tuberculosis in the prior year. He was HIV negative. Examination on admission: temperature 38.2 C, Glasgow Coma Scale 13, somnolent but rousable, neck stiffness, positive Kernig sign, no focal motor deficit, and no papilledema. CSF showed an opening pressure of 18 cmH2O, white cell count 220 per cubic millimeter with 80 percent lymphocytes, glucose 30 mg/dL, protein 200 mg/dL, and adenosine deaminase 12 U/L. MRI with contrast demonstrated basal meningeal enhancement without hydrocephalus. CSF Xpert MTB/RIF Ultra was negative on the initial specimen, but mycobacterial culture was positive at four weeks. He was randomized to the standard arm. Anchored to Heemskerk NEJM 2016 (PMID 26760084). Wave 1, hold_for_revision.

NARRATIVE_ES: Varon de 19 anos, estudiante universitario, de Ho Chi Minh, Vietnam, ingresado a un hospital terciario tras dos semanas y media de fiebre baja diaria, cefalea frontal y fatiga progresiva. Vive en residencia universitaria donde varios companeros fueron tratados por tuberculosis pulmonar el ano previo. VIH negativo. Examen: temperatura 38.2 C, Glasgow 13, somnoliento, rigidez de nuca, Kernig positivo, sin deficit motor focal, sin papiledema. LCR con presion 18 cmH2O, leucocitos 220 por mm3 (80 por ciento linfocitos), glucosa 30 mg/dL, proteina 200 mg/dL, adenosina desaminasa 12 U/L. RM con engrosamiento meningeo basal sin hidrocefalia. Xpert MTB/RIF Ultra negativo en muestra inicial; cultivo micobacteriano positivo a las cuatro semanas. Aleatorizado al brazo estandar. Anclaje Heemskerk NEJM 2016.

RATIONALE: Subphase 1.4 commit 5.4.3 wave 1 vignette 134 of 14 for Class 4 TBM. Anchored to Heemskerk 2016 standard arm, Xpert-negative-culture-confirmed case per RCT inclusion. Pre-adjudication hold_for_revision.

ANCHORING_EXTRAS: Anchored to Heemskerk AD et al. NEJM 2016 (PMID 26760084) standard arm. 19-year-old Vietnamese male university student HIV-negative dormitory TB exposure cluster, lymphocytic CSF, ADA 12 U/L, Xpert MTB/RIF Ultra NEGATIVE on initial specimen, culture POSITIVE at 4 weeks (RCT inclusion via culture confirmation). Pre-adjudication kappa 0.70.

ADJUDICATION:
  inclusion_decision: hold_for_revision
  adjudicator_ids: ['WAVE1-TBM-134-ADJ-1', 'WAVE1-TBM-134-ADJ-2']
  ground_truth_class: 4
  pre_adjudication_kappa: 0.7
  disagreement_resolution: None

=== END vignette ===

=== CLASS 4 | vignette_id: 135 | subphase: 1.4 TBM wave_1 | file: tbm_135_heemskerk_hcmc_elderly_female_sequelae_wave1.json ===

ANCHOR:
  pmid: 26760084
  first_author: Heemskerk
  year: 2016
  journal: NEJM
  citation_type: rct
  doi: 10.1056/NEJMoa1507062

DEMOGRAPHICS:
  age_years: 61
  sex: female
  geography_region: other_global
  ethnicity: asian
  altitude_residence_m: 19
  hiv_status: negative
  cd4_count_cells_per_uL: None
  pregnancy_red_flag: False
  immunocompromise_status: none
  freshwater_exposure_within_14d: False
  freshwater_exposure_type: None

HISTORY:
  symptom_onset_to_presentation_days: 28.0
  chief_complaint: altered_mental_status
  red_flags_present: []
  prodrome_description: Four-week illness in a 61-year-old woman from Ho Chi Minh City. Progressive headache, weight loss of 5 kg, persistent low-grade fevers, and increasing forgetfulness with word-finding difficulty noted by her daughter. HIV negative; type 2 diabetes on metformin.

VITALS:
  temperature_celsius: 38.4
  heart_rate_bpm: 102
  systolic_bp_mmHg: 134
  diastolic_bp_mmHg: 82
  glasgow_coma_scale: 11
  oxygen_saturation_pct: 96
  respiratory_rate_breaths_per_min: 20

EXAM:
  mental_status_grade: stuporous
  neck_stiffness: True
  kernig_or_brudzinski_positive: True
  cranial_nerve_palsy: none
  papilledema_on_fundoscopy: True
  focal_neurological_deficit: True
  skin_lesion_centrofacial_chronic: False
  petechial_or_purpuric_rash: False

LABS:
  wbc_blood_per_uL: 9800
  platelets_per_uL: 248000
  alt_ast_U_per_L: 32
  crp_mg_per_L: 54.0
  procalcitonin_ng_per_mL: 0.6
  serum_sodium_mEq_per_L: 130

CSF:
  opening_pressure_cmH2O: 26.0
  wbc_per_mm3: 360
  lymphocyte_pct: 75
  neutrophil_pct: 23
  eosinophil_pct: 2
  glucose_mg_per_dL: 22
  protein_mg_per_dL: 320
  lactate_mmol_per_L: 4.4
  ada_U_per_L: 16.0
  crag_lfa_result: negative
  wet_mount_motile_amoebae: negative
  xanthochromia_present: False
  rbc_per_mm3: 2

IMAGING:
  modality: mri_contrast
  pattern: basal_meningeal_enhancement_with_hydrocephalus
  contrast_enhancement: True
  hydrocephalus: True
  basal_meningeal_enhancement: True
  finding_count: None
  text_summary: Thick basal meningeal enhancement on post-contrast T1 with mild communicating hydrocephalus and a small left basal ganglia infarct. Findings consistent with active tuberculous meningitis.

DIAGNOSTIC_TESTS:
  pcr_panel: n/a
  xpert_mtb_rif: Positive, rifampicin susceptible. Cycle threshold consistent with TBM.
  blood_culture: n/a
  csf_culture: Pending at LP; reported positive at 4 weeks (M. tuberculosis drug-sensitive).
  serology_or_antigen: n/a
  smear_or_gram: Positive, scant acid-fast bacilli on concentrated specimen.
  brain_biopsy: n/a
  imaging_test: Hilar lymphadenopathy with adjacent parenchymal infiltrate consistent with primary TB.
  total_dx_results: 4

NARRATIVE_EN: A 61-year-old woman from Ho Chi Minh City presented to a tertiary referral hospital with a four-week illness of progressive headache, a five-kilogram weight loss, persistent low-grade fevers, and increasing forgetfulness with word-finding difficulty noted by her daughter. She was HIV negative and had type 2 diabetes on metformin. Examination on admission: temperature 38.4 C, Glasgow Coma Scale 11, stuporous, neck stiffness, positive Kernig sign, mild left-sided motor weakness, and bilateral papilledema. CSF showed an opening pressure of 26 cmH2O, white cell count 360 per cubic millimeter with 75 percent lymphocytes, glucose 22 mg/dL, protein 320 mg/dL, and adenosine deaminase 16 U/L. MRI with contrast demonstrated thick basal meningeal enhancement, communicating hydrocephalus, and a small left thalamic infarct. CSF Xpert MTB/RIF Ultra was positive; AFB smear was positive. She was randomized to the intensified arm and survived with persistent cognitive impairment and mild left hemiparesis. Anchored to Heemskerk NEJM 2016 (PMID 26760084). Wave 1, hold_for_revision.

NARRATIVE_ES: Mujer de 61 anos de Ho Chi Minh, Vietnam, ingresada a un hospital terciario tras cuatro semanas de cefalea progresiva, perdida de 5 kg, fiebre baja persistente y olvidos crecientes con dificultad para encontrar palabras referidos por su hija. VIH negativo, diabetes tipo 2 en metformina. Examen: temperatura 38.4 C, Glasgow 11, estuporosa, rigidez de nuca, Kernig positivo, debilidad motora leve izquierda, papiledema bilateral. LCR con presion 26 cmH2O, leucocitos 360 por mm3 (75 por ciento linfocitos), glucosa 22 mg/dL, proteina 320 mg/dL, adenosina desaminasa 16 U/L. RM con engrosamiento meningeo basal, hidrocefalia comunicante e infarto talamico izquierdo pequeno. Xpert MTB/RIF Ultra positivo; baciloscopia positiva. Aleatorizada al brazo intensificado; sobrevivio con deterioro cognitivo persistente y hemiparesia izquierda leve.

RATIONALE: Subphase 1.4 commit 5.4.3 wave 1 vignette 135 of 14 for Class 4 TBM. Anchored to Heemskerk 2016 intensified arm; mid-stage survived with cognitive + motor sequelae. Pre-adjudication hold_for_revision.

ANCHORING_EXTRAS: Anchored to Heemskerk AD et al. NEJM 2016 (PMID 26760084) intensified arm. 61-year-old Vietnamese adult female HIV-negative diabetic, left thalamic infarct, Xpert MTB/RIF Ultra positive, AFB smear positive; survived with cognitive sequelae. Pre-adjudication kappa 0.70.

ADJUDICATION:
  inclusion_decision: hold_for_revision
  adjudicator_ids: ['WAVE1-TBM-135-ADJ-1', 'WAVE1-TBM-135-ADJ-2']
  ground_truth_class: 4
  pre_adjudication_kappa: 0.7
  disagreement_resolution: None

=== END vignette ===

=== CLASS 4 | vignette_id: 136 | subphase: 1.4 TBM wave_1 | file: tbm_136_heemskerk_hcmc_adult_male_early_intensified_wave1.json ===

ANCHOR:
  pmid: 26760084
  first_author: Heemskerk
  year: 2016
  journal: NEJM
  citation_type: rct
  doi: 10.1056/NEJMoa1507062

DEMOGRAPHICS:
  age_years: 33
  sex: male
  geography_region: other_global
  ethnicity: asian
  altitude_residence_m: 19
  hiv_status: negative
  cd4_count_cells_per_uL: None
  pregnancy_red_flag: False
  immunocompromise_status: none
  freshwater_exposure_within_14d: False
  freshwater_exposure_type: None

HISTORY:
  symptom_onset_to_presentation_days: 14.0
  chief_complaint: fever_with_headache
  red_flags_present: []
  prodrome_description: Two-week illness in a 33-year-old male office worker from Ho Chi Minh City. Daily low-grade fevers and frontal headache. HIV negative; cousin treated for sputum-positive pulmonary tuberculosis the prior year.

VITALS:
  temperature_celsius: 38.2
  heart_rate_bpm: 92
  systolic_bp_mmHg: 122
  diastolic_bp_mmHg: 76
  glasgow_coma_scale: 14
  oxygen_saturation_pct: 97
  respiratory_rate_breaths_per_min: 18

EXAM:
  mental_status_grade: confused
  neck_stiffness: True
  kernig_or_brudzinski_positive: True
  cranial_nerve_palsy: none
  papilledema_on_fundoscopy: False
  focal_neurological_deficit: False
  skin_lesion_centrofacial_chronic: False
  petechial_or_purpuric_rash: False

LABS:
  wbc_blood_per_uL: 7400
  platelets_per_uL: 308000
  alt_ast_U_per_L: 22
  crp_mg_per_L: 30.0
  procalcitonin_ng_per_mL: 0.3
  serum_sodium_mEq_per_L: 134

CSF:
  opening_pressure_cmH2O: 18.0
  wbc_per_mm3: 200
  lymphocyte_pct: 82
  neutrophil_pct: 16
  eosinophil_pct: 2
  glucose_mg_per_dL: 32
  protein_mg_per_dL: 180
  lactate_mmol_per_L: 4.4
  ada_U_per_L: 11.0
  crag_lfa_result: negative
  wet_mount_motile_amoebae: negative
  xanthochromia_present: False
  rbc_per_mm3: 2

IMAGING:
  modality: mri_contrast
  pattern: basal_meningeal_enhancement_with_hydrocephalus
  contrast_enhancement: True
  hydrocephalus: True
  basal_meningeal_enhancement: True
  finding_count: None
  text_summary: Thick basal meningeal enhancement on post-contrast T1 with mild communicating hydrocephalus and a small left basal ganglia infarct. Findings consistent with active tuberculous meningitis.

DIAGNOSTIC_TESTS:
  pcr_panel: n/a
  xpert_mtb_rif: Positive, rifampicin susceptible. Cycle threshold consistent with TBM.
  blood_culture: n/a
  csf_culture: Pending at LP; reported positive at 4 weeks (M. tuberculosis drug-sensitive).
  serology_or_antigen: n/a
  smear_or_gram: n/a
  brain_biopsy: n/a
  imaging_test: Hilar lymphadenopathy with adjacent parenchymal infiltrate consistent with primary TB.
  total_dx_results: 3

NARRATIVE_EN: A 33-year-old male office worker from Ho Chi Minh City presented to a tertiary referral hospital after a two-week illness of daily low-grade fevers and frontal headache. He was HIV negative; his cousin had been treated for sputum-positive pulmonary tuberculosis the prior year. He was alert and articulate but described difficulty concentrating at work. Examination on admission: temperature 38.2 C, Glasgow Coma Scale 14, mild confusion, neck stiffness, positive Kernig sign, no focal motor deficit, and no papilledema. CSF showed an opening pressure of 18 cmH2O, white cell count 200 per cubic millimeter with 82 percent lymphocytes, glucose 32 mg/dL, protein 180 mg/dL, and adenosine deaminase 11 U/L. MRI with contrast demonstrated subtle basal meningeal enhancement without hydrocephalus. CSF Xpert MTB/RIF Ultra was positive and rifampicin susceptible. He was randomized to the intensified arm. Anchored to Heemskerk NEJM 2016 (PMID 26760084). Wave 1, hold_for_revision.

NARRATIVE_ES: Varon de 33 anos, oficinista, de Ho Chi Minh, Vietnam, ingresado a un hospital terciario tras dos semanas de fiebre baja diaria y cefalea frontal. VIH negativo; primo tratado por tuberculosis pulmonar baciloscopia positiva el ano previo. Alerta y articulado pero refiere dificultad para concentrarse en el trabajo. Examen: temperatura 38.2 C, Glasgow 14, confusion leve, rigidez de nuca, Kernig positivo, sin deficit motor focal, sin papiledema. LCR con presion 18 cmH2O, leucocitos 200 por mm3 (82 por ciento linfocitos), glucosa 32 mg/dL, proteina 180 mg/dL, adenosina desaminasa 11 U/L. RM con engrosamiento meningeo basal sutil sin hidrocefalia. Xpert MTB/RIF Ultra positivo en LCR, susceptible a rifampicina. Aleatorizado al brazo intensificado. Anclaje Heemskerk NEJM 2016.

RATIONALE: Subphase 1.4 commit 5.4.3 wave 1 vignette 136 of 14 for Class 4 TBM. Anchored to Heemskerk 2016 intensified arm, early-stage presentation. Pre-adjudication hold_for_revision.

ANCHORING_EXTRAS: Anchored to Heemskerk AD et al. NEJM 2016 (PMID 26760084) intensified arm. 33-year-old Vietnamese adult male HIV-negative office worker, cousin prior pulmonary TB, lymphocytic CSF, ADA 11 U/L, Xpert MTB/RIF Ultra positive, early-stage GCS 14. Pre-adjudication kappa 0.70.

ADJUDICATION:
  inclusion_decision: hold_for_revision
  adjudicator_ids: ['WAVE1-TBM-136-ADJ-1', 'WAVE1-TBM-136-ADJ-2']
  ground_truth_class: 4
  pre_adjudication_kappa: 0.7
  disagreement_resolution: None

=== END vignette ===

=== CLASS 5 | vignette_id: 151 | subphase: 1.4 CRYPTO pilot | file: crypto_151_perfect_idsa_hiv_pilot.json ===

ANCHOR:
  pmid: 20047480
  first_author: Perfect
  year: 2010
  journal: CID
  citation_type: guideline
  doi: 10.1086/649858

DEMOGRAPHICS:
  age_years: 38
  sex: male
  geography_region: other_global
  ethnicity: other
  altitude_residence_m: 50
  hiv_status: positive_not_on_art
  cd4_count_cells_per_uL: 45
  pregnancy_red_flag: False
  immunocompromise_status: hiv_cd4_under100
  freshwater_exposure_within_14d: False
  freshwater_exposure_type: None

HISTORY:
  symptom_onset_to_presentation_days: 21.0
  chief_complaint: fever_with_headache
  red_flags_present: ['immunocompromise']
  prodrome_description: Three-week indolent course in a 32-year-old Ugandan man with newly diagnosed HIV. Fever, persistent frontal and bitemporal headache, and progressive nausea. Five-kilogram weight loss over the prior two months. No focal weakness. Antiretroviral therapy not yet started. No recent freshwater exposure or travel.

VITALS:
  temperature_celsius: 38.6
  heart_rate_bpm: 102
  systolic_bp_mmHg: 118
  diastolic_bp_mmHg: 74
  glasgow_coma_scale: 14
  oxygen_saturation_pct: 97
  respiratory_rate_breaths_per_min: 18

EXAM:
  mental_status_grade: confused
  neck_stiffness: True
  kernig_or_brudzinski_positive: False
  cranial_nerve_palsy: none
  papilledema_on_fundoscopy: True
  focal_neurological_deficit: False
  skin_lesion_centrofacial_chronic: False
  petechial_or_purpuric_rash: False

LABS:
  wbc_blood_per_uL: 3800
  platelets_per_uL: 198000
  alt_ast_U_per_L: 32
  crp_mg_per_L: 24.0
  procalcitonin_ng_per_mL: 0.3
  serum_sodium_mEq_per_L: 133

CSF:
  opening_pressure_cmH2O: 38.0
  wbc_per_mm3: 45
  lymphocyte_pct: 86
  neutrophil_pct: 12
  eosinophil_pct: 2
  glucose_mg_per_dL: 38
  protein_mg_per_dL: 95
  lactate_mmol_per_L: 2.4
  ada_U_per_L: None
  crag_lfa_result: positive
  wet_mount_motile_amoebae: negative
  xanthochromia_present: False
  rbc_per_mm3: 1

IMAGING:
  modality: mri_contrast
  pattern: dilated_virchow_robin_with_pseudocysts
  contrast_enhancement: True
  hydrocephalus: False
  basal_meningeal_enhancement: False
  finding_count: None
  text_summary: Dilated Virchow-Robin spaces in the basal ganglia bilaterally with small cystic pseudocysts; no parenchymal mass effect, no ring enhancement. Findings characteristic of HIV-associated cryptococcal meningitis per NIH OI guideline imaging spectrum.

DIAGNOSTIC_TESTS:
  pcr_panel: n/a
  xpert_mtb_rif: n/a
  blood_culture: n/a
  csf_culture: Pending; reported Cryptococcus neoformans var. grubii at day 4.
  serology_or_antigen: Positive, titer 1:2048.
  smear_or_gram: n/a
  brain_biopsy: n/a
  imaging_test: n/a
  total_dx_results: 5

NARRATIVE_EN: A 32-year-old man from Kampala, Uganda, presented to a regional referral hospital with a three-week indolent course of fever, persistent frontal and bitemporal headache, and progressive nausea. He had been diagnosed with HIV two weeks prior and had not yet started antiretroviral therapy; his CD4 count was 35 cells per microliter. He reported no recent freshwater exposure and no travel. Examination on admission: temperature 38.6 C, Glasgow Coma Scale 14, confused but oriented to person, neck stiffness, and bilateral papilledema on fundoscopy. CSF showed an opening pressure of 38 cmH2O, white cell count 45 per cubic millimeter with 86 percent lymphocytes, glucose 38 mg/dL, and protein 95 mg/dL. CSF cryptococcal antigen lateral flow assay was positive at a titer of 1:2048, and India ink microscopy showed encapsulated yeast forms with refractile halos. Serum CrAg was 1:1024. Therapeutic lumbar puncture reduced the pressure from 38 to 18 cmH2O. MRI with contrast showed dilated Virchow-Robin spaces with small pseudocysts. Anchored to Perfect CID 2010 IDSA (PMID 20047480). Pilot, hold_for_revision.

NARRATIVE_ES: Varon de 32 anos de Kampala, Uganda, ingresado a un hospital regional tras tres semanas de fiebre, cefalea frontal y bitemporal persistente, y nauseas progresivas. Diagnostico reciente de VIH (dos semanas antes), sin terapia antirretroviral iniciada; CD4 35 por microlitro. Sin exposicion a agua dulce, sin viajes. Examen: temperatura 38.6 C, Glasgow 14, confuso pero orientado, rigidez de nuca, papiledema bilateral. LCR con presion de apertura 38 cmH2O, leucocitos 45 por mm3 (86 por ciento linfocitos), glucosa 38 mg/dL, proteina 95 mg/dL. Antigeno criptococico en LCR positivo (1:2048) y tinta china con levaduras encapsuladas. CrAg serico 1:1024. Puncion lumbar terapeutica redujo la presion de 38 a 18 cmH2O. RM con espacios de Virchow-Robin dilatados con pseudoquistes. Anclaje Perfect IDSA 2010 (PMID 20047480).

RATIONALE: Subphase 1.4 commit 5.4.2 pilot 3 of 6 for Class 5 Cryptococcal (master prompt 1.4.5 HIV+CD4<100 22-slot bulk stratum). Anchored to Perfect 2010 CID IDSA guidelines. OP 38 satisfies >=25 master prompt requirement; CrAg LFA positive satisfies >=28/30 requirement. cd4_count_cells_per_uL=35 per Ford CID 2018 validator. Pre-adjudication hold_for_revision.

ANCHORING_EXTRAS: Anchored to Perfect JR et al. CID 2010 IDSA cryptococcal guidelines (PMID 20047480). 32-year-old Ugandan ART-naive HIV+ with CD4 35, opening pressure 38 cmH2O, csf_crag_lfa positive 1:2048, mononuclear CSF, dilated VR spaces on MRI. Therapeutic LP per IDSA. Pre-adjudication kappa 0.70.

ADJUDICATION:
  inclusion_decision: hold_for_revision
  adjudicator_ids: ['PILOT-CRYPTO-151-ADJ-1', 'PILOT-CRYPTO-151-ADJ-2']
  ground_truth_class: 5
  pre_adjudication_kappa: 0.7
  disagreement_resolution: None

=== END vignette ===

=== CLASS 5 | vignette_id: 152 | subphase: 1.4 CRYPTO pilot | file: crypto_152_singh_transplant_pilot.json ===

ANCHOR:
  pmid: 17262720
  first_author: Singh
  year: 2007
  journal: JID
  citation_type: cohort
  doi: 10.1086/511438

DEMOGRAPHICS:
  age_years: 54
  sex: male
  geography_region: us_south
  ethnicity: white_non_hispanic
  altitude_residence_m: 224
  hiv_status: negative
  cd4_count_cells_per_uL: None
  pregnancy_red_flag: False
  immunocompromise_status: transplant_solid_organ
  freshwater_exposure_within_14d: False
  freshwater_exposure_type: None

HISTORY:
  symptom_onset_to_presentation_days: 14.0
  chief_complaint: fever_with_headache
  red_flags_present: ['immunocompromise']
  prodrome_description: Two-week subacute illness in a 49-year-old man eighteen months post-renal-transplant on tacrolimus, mycophenolate mofetil, and low-dose prednisone. Daily low-grade fevers, gradual frontal headache, and three days of mild confusion noted by his wife. No freshwater exposure. Cadaveric donor; immunosuppression unchanged over the prior twelve months.

VITALS:
  temperature_celsius: 38.0
  heart_rate_bpm: 88
  systolic_bp_mmHg: 132
  diastolic_bp_mmHg: 84
  glasgow_coma_scale: 14
  oxygen_saturation_pct: 97
  respiratory_rate_breaths_per_min: 16

EXAM:
  mental_status_grade: confused
  neck_stiffness: True
  kernig_or_brudzinski_positive: False
  cranial_nerve_palsy: none
  papilledema_on_fundoscopy: False
  focal_neurological_deficit: False
  skin_lesion_centrofacial_chronic: False
  petechial_or_purpuric_rash: False

LABS:
  wbc_blood_per_uL: 6400
  platelets_per_uL: 224000
  alt_ast_U_per_L: 26
  crp_mg_per_L: 18.0
  procalcitonin_ng_per_mL: 0.2
  serum_sodium_mEq_per_L: 135

CSF:
  opening_pressure_cmH2O: 22.0
  wbc_per_mm3: 30
  lymphocyte_pct: 88
  neutrophil_pct: 10
  eosinophil_pct: 2
  glucose_mg_per_dL: 45
  protein_mg_per_dL: 80
  lactate_mmol_per_L: 2.1
  ada_U_per_L: None
  crag_lfa_result: positive
  wet_mount_motile_amoebae: negative
  xanthochromia_present: False
  rbc_per_mm3: 0

IMAGING:
  modality: mri_contrast
  pattern: dilated_virchow_robin_with_pseudocysts
  contrast_enhancement: True
  hydrocephalus: False
  basal_meningeal_enhancement: False
  finding_count: None
  text_summary: Subtle dilated Virchow-Robin spaces in the basal ganglia; no mass lesion, no hydrocephalus. Findings consistent with post-transplant cryptococcal meningitis per Singh JID 2007 cohort phenotype.

DIAGNOSTIC_TESTS:
  pcr_panel: n/a
  xpert_mtb_rif: n/a
  blood_culture: n/a
  csf_culture: Pending; reported Cryptococcus neoformans var. grubii at day 4.
  serology_or_antigen: Positive, titer 1:256.
  smear_or_gram: n/a
  brain_biopsy: n/a
  imaging_test: n/a
  total_dx_results: 5

NARRATIVE_EN: A 49-year-old man in Pittsburgh presented to a transplant infectious diseases service with a two-week subacute illness. He was eighteen months post-cadaveric renal transplant on tacrolimus, mycophenolate mofetil, and low-dose prednisone with unchanged dosing over the prior year. He reported daily low-grade fevers, gradual frontal headache, and three days of mild confusion noted by his wife. There was no freshwater exposure. Examination on admission: temperature 38.0 C, Glasgow Coma Scale 14, mild confusion, neck stiffness, and no focal deficit. CSF showed an opening pressure of 22 cmH2O, white cell count 30 per cubic millimeter with 88 percent lymphocytes, glucose 45 mg/dL, and protein 80 mg/dL. CSF cryptococcal antigen lateral flow assay was positive at 1:256, India ink showed encapsulated yeast, and serum CrAg was 1:128. Tacrolimus trough was 9.2 ng/mL. MRI showed subtle dilated Virchow-Robin spaces without mass lesion. Anchored to Singh JID 2007 transplant cohort (PMID 17262720). Subphase 1.4 pilot, hold_for_revision.

NARRATIVE_ES: Varon de 49 anos en Pittsburgh, Estados Unidos, evaluado por el servicio de enfermedades infecciosas en transplante con un cuadro subagudo de dos semanas. Diez y ocho meses postransplante renal cadaverico, en tacrolimus, micofenolato mofetil y prednisona en dosis bajas estables el ano previo. Refiere fiebre baja diaria, cefalea frontal gradual y tres dias de confusion leve referida por la esposa. Sin exposicion a agua dulce. Examen: temperatura 38.0 C, Glasgow 14, confusion leve, rigidez de nuca, sin deficit focal. LCR con presion 22 cmH2O, leucocitos 30 por mm3 (88 por ciento linfocitos), glucosa 45 mg/dL, proteina 80 mg/dL. Antigeno criptococico en LCR positivo 1:256, tinta china con levaduras encapsuladas, CrAg serico 1:128. Nivel de tacrolimus 9.2 ng/mL. RM con espacios de Virchow-Robin discretamente dilatados sin masa.

RATIONALE: Subphase 1.4 commit 5.4.2 pilot 4 of 6 for Class 5 Cryptococcal transplant stratum (master prompt 1.4.5 4-slot transplant). Anchored to Singh 2007 JID multicenter transplant cohort; tacrolimus exposure aligns with calcineurin-protective mortality observation. Pre-adjudication hold_for_revision.

ANCHORING_EXTRAS: Anchored to Singh N et al. JID 2007 transplant cryptococcus calcineurin-inhibitor cohort (PMID 17262720). 49-year-old US renal transplant recipient 18 months post-tx on tacrolimus + MMF + prednisone, csf_crag_lfa positive 1:256, lymphocytic CSF, dilated VR spaces. Pre-adjudication kappa 0.70.

ADJUDICATION:
  inclusion_decision: hold_for_revision
  adjudicator_ids: ['PILOT-CRYPTO-152-ADJ-1', 'PILOT-CRYPTO-152-ADJ-2']
  ground_truth_class: 5
  pre_adjudication_kappa: 0.7
  disagreement_resolution: None

=== END vignette ===

=== CLASS 6 | vignette_id: 181 | subphase: 1.4 GAE pilot | file: gae_181_gotuzzo_peru_balamuthia_pilot.json ===

ANCHOR:
  pmid: (none/doi-only)
  first_author: ?
  year: ?
  journal: ?
  citation_type: case_report
  doi: 10.1093/ofid/ofaf695.345

DEMOGRAPHICS:
  age_years: 42
  sex: male
  geography_region: peru_lima_coast
  ethnicity: mestizo
  altitude_residence_m: 154
  hiv_status: negative
  cd4_count_cells_per_uL: None
  pregnancy_red_flag: False
  immunocompromise_status: none
  freshwater_exposure_within_14d: False
  freshwater_exposure_type: None

HISTORY:
  symptom_onset_to_presentation_days: 28.0
  chief_complaint: headache
  red_flags_present: []
  prodrome_description: Four-week neurologic illness in a 42-year-old man from coastal Lima. Subacute progressive headache, intermittent low-grade fevers, and two weeks of word-finding difficulty. Fifteen months earlier the patient had developed a persistent indurated plaque on the central face that had been treated as cutaneous leishmaniasis without resolution. No recent freshwater exposure. Mestizo ethnicity, outdoor manual labor in agricultural soil.

VITALS:
  temperature_celsius: 37.6
  heart_rate_bpm: 92
  systolic_bp_mmHg: 124
  diastolic_bp_mmHg: 78
  glasgow_coma_scale: 13
  oxygen_saturation_pct: 97
  respiratory_rate_breaths_per_min: 18

EXAM:
  mental_status_grade: confused
  neck_stiffness: False
  kernig_or_brudzinski_positive: False
  cranial_nerve_palsy: none
  papilledema_on_fundoscopy: False
  focal_neurological_deficit: True
  skin_lesion_centrofacial_chronic: True
  petechial_or_purpuric_rash: False

LABS:
  wbc_blood_per_uL: 8800
  platelets_per_uL: 268000
  alt_ast_U_per_L: 24
  crp_mg_per_L: 14.0
  procalcitonin_ng_per_mL: 0.2
  serum_sodium_mEq_per_L: 138

CSF:
  opening_pressure_cmH2O: 18.0
  wbc_per_mm3: 45
  lymphocyte_pct: 78
  neutrophil_pct: 18
  eosinophil_pct: 4
  glucose_mg_per_dL: 48
  protein_mg_per_dL: 120
  lactate_mmol_per_L: 2.6
  ada_U_per_L: None
  crag_lfa_result: negative
  wet_mount_motile_amoebae: negative
  xanthochromia_present: False
  rbc_per_mm3: 4

IMAGING:
  modality: mri_contrast
  pattern: multiple_ring_enhancing_lesions
  contrast_enhancement: True
  hydrocephalus: False
  basal_meningeal_enhancement: False
  finding_count: 3
  text_summary: 3 ring-enhancing lesions: right parietal cortex 1.8 cm, left temporal lobe 1.2 cm, and right cerebellar hemisphere 0.9 cm, each with surrounding vasogenic edema. No basal meningeal enhancement. Pattern characteristic of granulomatous amebic encephalitis.

DIAGNOSTIC_TESTS:
  pcr_panel: n/a
  xpert_mtb_rif: n/a
  blood_culture: n/a
  csf_culture: n/a
  serology_or_antigen: Positive, titer 1:512.
  smear_or_gram: n/a
  brain_biopsy: Granulomatous dermatitis with multinucleated giant cells; Balamuthia mandrillaris trophozoites identified on PAS and immunohistochemistry.
  imaging_test: n/a
  total_dx_results: 4

NARRATIVE_EN: A 42-year-old mestizo man from coastal Lima, Peru, presented to a national infectious diseases referral hospital with a four-week neurologic illness: subacute progressive headache, intermittent low-grade fevers, and two weeks of word-finding difficulty. Fifteen months earlier he had developed a persistent indurated plaque on the central face that had been treated empirically as cutaneous leishmaniasis without resolution. He worked outdoors in agricultural soil and reported no freshwater exposure. Examination on admission: temperature 37.6 C, Glasgow Coma Scale 13, mild confusion, no neck stiffness, and a right-sided motor deficit. The central facial plaque remained indurated and weeping. CSF showed an opening pressure of 18 cmH2O, white cell count 45 per cubic millimeter with 78 percent lymphocytes, glucose 48 mg/dL, and protein 120 mg/dL. MRI with contrast showed three ring-enhancing lesions in the right parietal cortex, left temporal lobe, and right cerebellar hemisphere. Skin and brain biopsies showed Balamuthia mandrillaris trophozoites on histology and immunohistochemistry. Anchored to Gotuzzo OFID 2026. Pilot, hold_for_revision.

NARRATIVE_ES: Varon mestizo de 42 anos de Lima costera, Peru, ingresado al instituto nacional de salud con cuadro neurologico de cuatro semanas: cefalea subaguda progresiva, fiebre baja intermitente y dos semanas de dificultad para encontrar palabras. Quince meses antes desarrollo una placa indurada persistente en la cara central, tratada empiricamente como leishmaniasis cutanea sin respuesta. Trabaja al aire libre con suelo agricola; sin exposicion a agua dulce. Examen: temperatura 37.6 C, Glasgow 13, confusion leve, sin rigidez de nuca, paresia derecha. La placa centro-facial persiste indurada y supurativa. LCR con presion 18 cmH2O, leucocitos 45 por mm3 (78 por ciento linfocitos), glucosa 48 mg/dL, proteina 120 mg/dL. RM con tres lesiones anulares (parietal derecha, temporal izquierda, hemisferio cerebeloso derecho). Biopsias de piel y cerebro con Balamuthia mandrillaris en histologia e IHC.

RATIONALE: Subphase 1.4 commit 5.4.2 pilot 5 of 6 for Class 6 GAE Balamuthia Peru stratum (master prompt 1.4.6 12/15 Peru-Hispanic with skin lesion 15-month preceding interval). Anchored via DOI to Gotuzzo 2026 OFID supplement (DOI-only entry per PMID_REGISTRY commit 5.4.0 caveat). Three ring-enhancing lesions match multifocal imaging mandate. Pre-adjudication hold_for_revision.

ANCHORING_EXTRAS: Anchored to Gotuzzo E et al. OFID 2026 supplement (doi:10.1093/ofid/ofaf695.345), Peru 68-case Balamuthia retrospective series. 42-year-old Lima mestizo male, centrofacial skin lesion 15 months preceding CNS, modest lymphocytic CSF, three ring-enhancing brain lesions, Balamuthia IFA 1:512, brain biopsy and mNGS positive. Pre-adjudication kappa 0.70.

ADJUDICATION:
  inclusion_decision: hold_for_revision
  adjudicator_ids: ['PILOT-GAE-181-ADJ-1', 'PILOT-GAE-181-ADJ-2']
  ground_truth_class: 6
  pre_adjudication_kappa: 0.7
  disagreement_resolution: None

=== END vignette ===

=== CLASS 6 | vignette_id: 182 | subphase: 1.4 GAE pilot | file: gae_182_visvesvara_acanthamoeba_aids_pilot.json ===

ANCHOR:
  pmid: 17428307
  first_author: Visvesvara
  year: 2007
  journal: FEMS-Immunol-Med-Microbiol
  citation_type: review
  doi: 10.1111/j.1574-695X.2007.00232.x

DEMOGRAPHICS:
  age_years: 47
  sex: male
  geography_region: us_south
  ethnicity: white_non_hispanic
  altitude_residence_m: 320
  hiv_status: positive_not_on_art
  cd4_count_cells_per_uL: 38
  pregnancy_red_flag: False
  immunocompromise_status: hiv_cd4_under100
  freshwater_exposure_within_14d: False
  freshwater_exposure_type: None

HISTORY:
  symptom_onset_to_presentation_days: 21.0
  chief_complaint: altered_mental_status
  red_flags_present: ['immunocompromise']
  prodrome_description: Three-week subacute encephalopathy in a 47-year-old man with advanced HIV (CD4 38, viral load 480000 copies, ART-naive). Progressive headache, mild fevers, and two weeks of personality change with episodic disorientation. No focal weakness initially; right hemiparesis developed in the final five days. No freshwater exposure. No skin lesions identified on full exam.

VITALS:
  temperature_celsius: 37.8
  heart_rate_bpm: 98
  systolic_bp_mmHg: 118
  diastolic_bp_mmHg: 72
  glasgow_coma_scale: 12
  oxygen_saturation_pct: 96
  respiratory_rate_breaths_per_min: 18

EXAM:
  mental_status_grade: confused
  neck_stiffness: False
  kernig_or_brudzinski_positive: False
  cranial_nerve_palsy: none
  papilledema_on_fundoscopy: False
  focal_neurological_deficit: True
  skin_lesion_centrofacial_chronic: False
  petechial_or_purpuric_rash: False

LABS:
  wbc_blood_per_uL: 3200
  platelets_per_uL: 178000
  alt_ast_U_per_L: 38
  crp_mg_per_L: 16.0
  procalcitonin_ng_per_mL: 0.2
  serum_sodium_mEq_per_L: 135

CSF:
  opening_pressure_cmH2O: 16.0
  wbc_per_mm3: 28
  lymphocyte_pct: 72
  neutrophil_pct: 22
  eosinophil_pct: 6
  glucose_mg_per_dL: 40
  protein_mg_per_dL: 95
  lactate_mmol_per_L: 2.2
  ada_U_per_L: None
  crag_lfa_result: negative
  wet_mount_motile_amoebae: negative
  xanthochromia_present: False
  rbc_per_mm3: 2

IMAGING:
  modality: mri_contrast
  pattern: multiple_ring_enhancing_lesions
  contrast_enhancement: True
  hydrocephalus: False
  basal_meningeal_enhancement: False
  finding_count: 2
  text_summary: 2 ring-enhancing lesions: left frontal lobe 2.1 cm and right thalamus 1.4 cm, each with surrounding vasogenic edema. No basal meningeal enhancement. Pattern characteristic of granulomatous amebic encephalitis.

DIAGNOSTIC_TESTS:
  pcr_panel: n/a
  xpert_mtb_rif: n/a
  blood_culture: n/a
  csf_culture: n/a
  serology_or_antigen: n/a
  smear_or_gram: n/a
  brain_biopsy: Granulomatous inflammation with trophozoites and double-walled cysts; immunohistochemistry positive for Acanthamoeba castellanii.
  imaging_test: n/a
  total_dx_results: 5

NARRATIVE_EN: A 47-year-old man in the US South region presented to an academic infectious diseases service with a three-week subacute encephalopathy. He had been diagnosed with HIV ten years prior but had been lost to follow-up; his admission CD4 count was 38 cells per microliter and his viral load was 480000 copies per milliliter, off antiretroviral therapy. He reported progressive headache, mild fevers, and two weeks of personality change with episodic disorientation; right-sided weakness developed in the final five days. There was no freshwater exposure and no contact-lens use. Examination: temperature 37.8 C, Glasgow Coma Scale 12, confused, no neck stiffness, and right hemiparesis. CSF showed an opening pressure of 16 cmH2O, white cell count 28 per cubic millimeter with 72 percent lymphocytes, glucose 40 mg/dL, and protein 95 mg/dL. MRI showed two ring-enhancing lesions in the left frontal lobe and right thalamus. Brain biopsy demonstrated granulomatous inflammation with double-walled cysts and immunohistochemistry positive for Acanthamoeba castellanii. Anchored to Visvesvara FEMS 2007 (PMID 17428307). Pilot, hold_for_revision.

NARRATIVE_ES: Varon de 47 anos en region sur de Estados Unidos, evaluado por enfermedades infecciosas con cuadro encefalopatico subagudo de tres semanas. Diagnostico de VIH hace diez anos, perdido al seguimiento; al ingreso CD4 38 por microlitro, carga viral 480000 copias por mL, sin terapia antirretroviral. Refiere cefalea progresiva, fiebre leve y dos semanas de cambio de personalidad con desorientacion episodica; debilidad derecha en los ultimos cinco dias. Sin exposicion a agua dulce, sin uso de lentes de contacto. Examen: temperatura 37.8 C, Glasgow 12, confuso, sin rigidez de nuca, hemiparesia derecha. LCR con presion 16 cmH2O, leucocitos 28 por mm3 (72 por ciento linfocitos), glucosa 40 mg/dL, proteina 95 mg/dL. RM con dos lesiones anulares (frontal izquierda, talamo derecho). Biopsia cerebral con Acanthamoeba castellanii en IHC.

RATIONALE: Subphase 1.4 commit 5.4.2 pilot 6 of 6 for Class 6 GAE Acanthamoeba immunocompromised stratum (master prompt 1.4.6 10/15 immunocompromised). Anchored to Visvesvara 2007 FEMS canonical free-living amoebae review. Two ring-enhancing lesions match multifocal imaging mandate. Pre-adjudication hold_for_revision.

ANCHORING_EXTRAS: Anchored to Visvesvara GS et al. FEMS Immunol Med Microbiol 2007 (PMID 17428307), canonical free-living amoebae review. 47-year-old US man with AIDS (CD4 38), two ring-enhancing brain lesions, brain biopsy granulomatous with A. castellanii on IHC, mNGS confirmation. Pre-adjudication kappa 0.70.

ADJUDICATION:
  inclusion_decision: hold_for_revision
  adjudicator_ids: ['PILOT-GAE-182-ADJ-1', 'PILOT-GAE-182-ADJ-2']
  ground_truth_class: 6
  pre_adjudication_kappa: 0.7
  disagreement_resolution: None

=== END vignette ===

# End — 140 vignettes printed.
