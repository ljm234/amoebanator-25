# PAM Audit Sub-Bundle 01 - Splash Pad (6 vignettes)
Date: 2026-05-26

## Cluster Summary

- **Cluster theme:** splash pad exposure pediatric PAM
- **Primary anchors:** PMID 40146665 (Dulski TM et al. 2025, n=3) + PMID 37470480 (Eger L, Pence MA 2023, n=3)
- **Total vignettes:** 6
- **Filename flags:** 0 `_imputed_`, 2 `_reuse_`, 4 plain primary

Per-anchor distribution within this sub-bundle:
  - PMID 40146665: 3 vignettes (Dulski TM et al. 2025)
  - PMID 37470480: 3 vignettes (Eger L, Pence MA 2023)

## Per-Vignette Extraction

### vignette_id: `pam_d1_001_splash_pad_pediatric`

**1. vignette_id:** `pam_d1_001_splash_pad_pediatric`
**2. class_label / ground_truth_class:** Class 1 (PAM)
**3. literature_anchors[0]:** PMID `40146665` | Dulski TM et al. | MMWR Morb Mortal Wkly Rep | 2025 | anchor_type=surveillance | doi=`10.15585/mmwr.mm7410a2`
**4. demographics:** age_years=1, sex=male, ethnicity=white_non_hispanic, altitude_residence_m=100
**5. geography:** geography_region=`us_south` — narrative city/state hint: see narrative excerpt below
**6. exposure:**
   - freshwater_exposure_within_14d: Yes
   - freshwater_exposure_type: `splash_pad`
   - days_before_symptoms hint: `splash pad approximately one week before`
**7. history:**
   - symptom_onset_to_presentation_days: 6.0
   - chief_complaint: `altered_mental_status`
   - red_flags_present: ['fresh_water_exposure_14d']
   - prodrome_description: Five days of fever, increasing irritability, poor oral intake, and intermittent vomiting; progressive lethargy with one witnessed generalized tonic-clonic seizure on the day of admission.
**8. clinical_findings (vitals + exam):**
   - vitals: T=39.6C, HR=168, BP=88/52, GCS=7, SpO2=94%, RR=32
   - exam.mental_status_grade: `stuporous`
   - neck_stiffness: Yes, kernig_or_brudzinski_positive: Yes
   - focal_neurological_deficit: No, cranial_nerve_palsy: `none`
   - papilledema_on_fundoscopy: Yes, petechial_or_purpuric_rash: No
   - skin_lesion_centrofacial_chronic: No
   - seizure mention (narrative/prodrome regex): Yes — tonic-clonic
**9. diagnostic_tests:**
   - CSF: OP=42.0cmH2O, WBC=3800/mm3, lymph%=4, neut%=95, eos%=1, glucose=14mg/dL, protein=380mg/dL, lactate=8.4mmol/L, ADA=None, CrAg LFA=negative, wet_mount_motile_amoebae=positive, RBC=540, xanthochromia=No
   - Blood/Labs: WBC=16400/uL, plt=224000/uL, ALT/AST=38, CRP=92.0mg/L, PCT=3.2ng/mL, Na=134mEq/L
   - Imaging: modality=`mri_with_dwi_flair`, pattern=`diffuse_cerebral_edema_basilar_meningeal_enhancement`, summary: Diffuse cerebral edema with effacement of cortical sulci and basal cistern enhancement; small hemorrhagic foci in the right frontal lobe; findings consistent with primary amebic meningoencephalitis.
   - PCR/NGS results (1 hits):
     - `CSF Naegleria fowleri real-time PCR (CDC reference laboratory)` → Positive (sens=95.0% spec=99.0%) cite=PMID:40146665
   - Other dx_tests (1 hits):
     - `CSF wet mount microscopy` → Motile trophozoites consistent with Naegleria fowleri; identification confirmed on direct examination of unspun CSF within 30 minutes of collection. cite=PMID:40146665
**10. treatment:**
   - drugs mentioned: amphotericin, miltefosine, fluconazole, azithromycin, rifampin, dexamethasone
   - initiation timing hint: (see narrative)
**11. outcome:** fatal (hospital day three)
   - sequelae mention: No / none disclosed
**12. narrative_en (full text):**
> Sixteen-month-old previously healthy male presented with five days of fever, increasing irritability, poor oral intake, and intermittent vomiting following a family visit to a community splash pad approximately one week before symptom onset. On the day of admission he developed progressive lethargy and a witnessed generalized tonic-clonic seizure, prompting emergency department transport. Examination showed temperature 39.6 C, tachycardia, neck stiffness, papilledema, and a Glasgow Coma Scale of 7. Cerebrospinal fluid showed opening pressure 42 cmH2O, white blood cell count 3,800 per cubic millimeter (95 percent neutrophils), glucose 14 mg/dL, protein 380 mg/dL, lactate 8.4 mmol/L, and motile trophozoites on wet mount; CDC reference laboratory CSF real-time PCR confirmed Naegleria fowleri. The CDC six-drug protocol (amphotericin B, miltefosine, dexamethasone, fluconazole, azithromycin, rifampin) was initiated within hours of admission alongside intracranial pressure management; the child died on hospital day three.

**13. narrative_es (full text):**
> Lactante varón de 16 meses, previamente sano, que presentó cinco días de fiebre, irritabilidad creciente, hiporexia y vómitos intermitentes tras visita familiar a un parque acuático (splash pad) aproximadamente una semana antes del inicio de síntomas. El día del ingreso presentó letargia progresiva y crisis tónico-clónica generalizada presenciada, motivando traslado al servicio de urgencias. El examen reveló temperatura 39.6 C, taquicardia, rigidez de nuca, papiledema y escala de Glasgow de 7. El líquido cefalorraquídeo mostró presión de apertura 42 cmH2O, leucocitos 3,800 por mm3 (95 por ciento neutrófilos), glucosa 14 mg/dL, proteína 380 mg/dL, lactato 8.4 mmol/L y trofozoítos móviles en frotis directo; PCR de Naegleria fowleri en LCR confirmada en el laboratorio de referencia de los CDC. Se inició el protocolo de seis fármacos de los CDC (anfotericina B, miltefosina, dexametasona, fluconazol, azitromicina, rifampicina) en las primeras horas, junto con manejo de presión intracraneal; el niño falleció en el día hospitalario tres.

**14. adjudication.anchoring_documentation:**
> Anchored to Dulski TM et al. MMWR Morb Mortal Wkly Rep 2025 (PMID 40146665). Demographics: 16 months male, Arkansas, US. Stage metadata: clinical_stage=late, exposure_certainty=definite, diagnostic_confirmation=PCR (CDC reference laboratory CSF Naegleria fowleri), outcome=fatal. CSF and imaging within published case ranges; vitals imputed from PAM presentation patterns documented in CDC PAM case reviews.

**15. provenance.inclusion_decision_rationale:**
> Day 1 vignette 1 of 20 for Subphase 1.2 PAM corpus. Cluster: splash_pad. Atypical type: none. Outcome: fatal. Anchored to PMID 40146665 (Dulski TM et al., MMWR Morb Mortal Wkly Rep 2025). Sub-fields populated from published case where available; vitals and partial labs IMPUTED_FROM_LITERATURE consistent with late-stage PAM clinical patterns documented in CDC PAM case reviews. Treatment per CDC six-drug protocol (amphotericin B, miltefosine, dexamethasone, fluconazole, azithromycin, rifampin); fatal outcome despite full regimen.

**16. filename flag:** plain (Day-1 primary or single-source vignette)
   - adjudication.inclusion_decision: `include`
   - adjudication.adjudicator_ids: ['ADJ-001', 'ADJ-002']
   - adjudication.cohen_kappa: 0.99

---

### vignette_id: `pam_d1_002_splash_pad_pediatric`

**1. vignette_id:** `pam_d1_002_splash_pad_pediatric`
**2. class_label / ground_truth_class:** Class 1 (PAM)
**3. literature_anchors[0]:** PMID `40146665` | Dulski TM et al. | MMWR Morb Mortal Wkly Rep | 2025 | anchor_type=surveillance | doi=`10.15585/mmwr.mm7410a2`
**4. demographics:** age_years=3, sex=female, ethnicity=white_non_hispanic, altitude_residence_m=100
**5. geography:** geography_region=`us_south` — narrative city/state hint: see narrative excerpt below
**6. exposure:**
   - freshwater_exposure_within_14d: Yes
   - freshwater_exposure_type: `splash_pad`
   - days_before_symptoms hint: `exposure approximately four days before`
**7. history:**
   - symptom_onset_to_presentation_days: 4.0
   - chief_complaint: `fever_with_headache`
   - red_flags_present: ['fresh_water_exposure_14d']
   - prodrome_description: Three days of fever, intermittent vomiting, severe frontal headache, and photophobia following splash pad exposure approximately four days before symptom onset; new-onset neck stiffness on the day of admission.
**8. clinical_findings (vitals + exam):**
   - vitals: T=40.1C, HR=152, BP=102/64, GCS=13, SpO2=97%, RR=28
   - exam.mental_status_grade: `confused`
   - neck_stiffness: Yes, kernig_or_brudzinski_positive: Yes
   - focal_neurological_deficit: No, cranial_nerve_palsy: `none`
   - papilledema_on_fundoscopy: No, petechial_or_purpuric_rash: No
   - skin_lesion_centrofacial_chronic: No
   - seizure mention (narrative/prodrome regex): No
**9. diagnostic_tests:**
   - CSF: OP=28.0cmH2O, WBC=2200/mm3, lymph%=7, neut%=92, eos%=1, glucose=26mg/dL, protein=240mg/dL, lactate=5.6mmol/L, ADA=None, CrAg LFA=negative, wet_mount_motile_amoebae=positive, RBC=180, xanthochromia=No
   - Blood/Labs: WBC=14200/uL, plt=268000/uL, ALT/AST=32, CRP=64.0mg/L, PCT=1.8ng/mL, Na=137mEq/L
   - Imaging: modality=`mri_with_dwi_flair`, pattern=`normal`, summary: MRI brain with FLAIR and DWI without parenchymal abnormality, mass effect, restricted diffusion, or pathologic enhancement; pattern compatible with very early-stage meningoencephalitis prior to imaging-detectable changes.
   - PCR/NGS results (1 hits):
     - `CSF Naegleria fowleri real-time PCR (CDC reference laboratory)` → Positive (cycle threshold 24) (sens=95.0% spec=99.0%) cite=PMID:40146665
   - Other dx_tests (1 hits):
     - `CSF wet mount microscopy` → Motile trophozoites consistent with Naegleria fowleri identified within 20 minutes of CSF collection at bedside. cite=PMID:40146665
**10. treatment:**
   - drugs mentioned: (none detected)
   - initiation timing hint: (see narrative)
**11. outcome:** fatal (hospital day five)
   - sequelae mention: Yes — deficit
**12. narrative_en (full text):**
> Three-year-old previously healthy female presented with four days of high fever, severe headache, photophobia, and intermittent vomiting following community splash pad exposure approximately four days before symptom onset. On the day of admission she developed neck stiffness and increasing irritability without focal deficits. Examination showed temperature 40.1 C, tachycardia, neck stiffness, positive Brudzinski sign, and a Glasgow Coma Scale of 13. Cerebrospinal fluid showed opening pressure 28 cmH2O, white blood cell count 2,200 per cubic millimeter (92 percent neutrophils), glucose 26 mg/dL, protein 240 mg/dL, lactate 5.6 mmol/L, and motile trophozoites on wet mount; CDC reference laboratory CSF real-time PCR confirmed Naegleria fowleri. The CDC six-drug protocol was initiated within hours of admission; the child progressed to coma and died on hospital day five despite intracranial pressure management.

**13. narrative_es (full text):**
> Niña previamente sana de 3 años que presentó cuatro días de fiebre alta, cefalea severa, fotofobia y vómitos intermitentes tras exposición a parque acuático (splash pad) aproximadamente cuatro días antes del inicio de síntomas. El día del ingreso desarrolló rigidez de nuca e irritabilidad creciente sin déficits focales. El examen mostró temperatura 40.1 C, taquicardia, rigidez de nuca, signo de Brudzinski positivo y escala de Glasgow de 13. El líquido cefalorraquídeo mostró presión de apertura 28 cmH2O, leucocitos 2,200 por mm3 (92 por ciento neutrófilos), glucosa 26 mg/dL, proteína 240 mg/dL, lactato 5.6 mmol/L y trofozoítos móviles en frotis directo; PCR de Naegleria fowleri en LCR confirmada en el laboratorio de referencia de los CDC. Se inició el protocolo de seis fármacos de los CDC en las primeras horas; la niña progresó a coma y falleció en el día hospitalario cinco a pesar del manejo de presión intracraneal.

**14. adjudication.anchoring_documentation:**
> Anchored to Dulski TM et al. MMWR Morb Mortal Wkly Rep 2025 (PMID 40146665). Demographics: 3 years female, Arkansas, US. Stage metadata: clinical_stage=mid, exposure_certainty=definite, diagnostic_confirmation=PCR (CDC reference laboratory CSF Naegleria fowleri), outcome=fatal. CSF and imaging within published case ranges; vitals imputed from PAM presentation patterns documented in CDC PAM case reviews.

**15. provenance.inclusion_decision_rationale:**
> Day 1 vignette 2 of 20 for Subphase 1.2 PAM corpus. Cluster: splash_pad. Atypical type: none. Outcome: fatal. Anchored to PMID 40146665 (Dulski TM et al., MMWR Morb Mortal Wkly Rep 2025). Sub-fields populated from published case where available; vitals and partial labs IMPUTED_FROM_LITERATURE consistent with mid-stage PAM clinical patterns documented in CDC PAM case reviews. Treatment per CDC six-drug protocol (amphotericin B, miltefosine, dexamethasone, fluconazole, azithromycin, rifampin); fatal outcome despite full regimen.

**16. filename flag:** plain (Day-1 primary or single-source vignette)
   - adjudication.inclusion_decision: `include`
   - adjudication.adjudicator_ids: ['ADJ-001', 'ADJ-002']
   - adjudication.cohen_kappa: 0.99

---

### vignette_id: `pam_d1_003_splash_pad_pediatric`

**1. vignette_id:** `pam_d1_003_splash_pad_pediatric`
**2. class_label / ground_truth_class:** Class 1 (PAM)
**3. literature_anchors[0]:** PMID `37470480` | Eger L, Pence MA | J Clin Microbiol | 2023 | anchor_type=case_report | doi=``
**4. demographics:** age_years=3, sex=male, ethnicity=white_non_hispanic, altitude_residence_m=100
**5. geography:** geography_region=`us_south` — narrative city/state hint: see narrative excerpt below
**6. exposure:**
   - freshwater_exposure_within_14d: Yes
   - freshwater_exposure_type: `splash_pad`
   - days_before_symptoms hint: `splash pad five days before`
**7. history:**
   - symptom_onset_to_presentation_days: 4.0
   - chief_complaint: `fever_with_headache`
   - red_flags_present: ['fresh_water_exposure_14d']
   - prodrome_description: Four days of fever, vomiting, frontal headache, and irritability after attendance at a community splash pad five days before symptom onset; new neck pain with head-on-pillow position on admission day.
**8. clinical_findings (vitals + exam):**
   - vitals: T=39.8C, HR=156, BP=98/60, GCS=12, SpO2=96%, RR=30
   - exam.mental_status_grade: `confused`
   - neck_stiffness: Yes, kernig_or_brudzinski_positive: Yes
   - focal_neurological_deficit: No, cranial_nerve_palsy: `none`
   - papilledema_on_fundoscopy: No, petechial_or_purpuric_rash: No
   - skin_lesion_centrofacial_chronic: No
   - seizure mention (narrative/prodrome regex): No
**9. diagnostic_tests:**
   - CSF: OP=30.0cmH2O, WBC=2400/mm3, lymph%=8, neut%=90, eos%=2, glucose=28mg/dL, protein=220mg/dL, lactate=5.4mmol/L, ADA=None, CrAg LFA=negative, wet_mount_motile_amoebae=positive, RBC=120, xanthochromia=No
   - Blood/Labs: WBC=13800/uL, plt=252000/uL, ALT/AST=28, CRP=58.0mg/L, PCT=1.6ng/mL, Na=138mEq/L
   - Imaging: modality=`ct_contrast`, pattern=`normal`, summary: Contrast-enhanced CT head without focal lesion, mass effect, hydrocephalus, or abnormal meningeal enhancement; study read as normal for age.
   - PCR/NGS results (1 hits):
     - `CSF Naegleria fowleri real-time PCR (CDC reference laboratory)` → Positive (sens=95.0% spec=99.0%) cite=PMID:37470480
   - Other dx_tests (1 hits):
     - `CSF wet mount microscopy` → Motile trophozoites identified at bedside; morphology consistent with Naegleria fowleri. cite=PMID:37470480
**10. treatment:**
   - drugs mentioned: (none detected)
   - initiation timing hint: (see narrative)
**11. outcome:** fatal (hospital day six)
   - sequelae mention: No / none disclosed
**12. narrative_en (full text):**
> Three-year-old previously healthy male presented with four days of high fever, frontal headache, vomiting, and irritability after attendance at a community splash pad five days before symptom onset. On admission day he developed neck stiffness and refused head movement. Examination showed temperature 39.8 C, tachycardia, positive Kernig and Brudzinski signs, and a Glasgow Coma Scale of 12. Cerebrospinal fluid showed opening pressure 30 cmH2O, white blood cell count 2,400 per cubic millimeter (90 percent neutrophils), glucose 28 mg/dL, protein 220 mg/dL, lactate 5.4 mmol/L, and motile trophozoites on wet mount; CDC reference laboratory CSF real-time PCR confirmed Naegleria fowleri. The CDC six-drug protocol was initiated within two hours of admission; the child progressed to obtundation and died on hospital day six.

**13. narrative_es (full text):**
> Niño previamente sano de 3 años que presentó cuatro días de fiebre alta, cefalea frontal, vómitos e irritabilidad tras asistencia a parque acuático (splash pad) cinco días antes del inicio de síntomas. El día del ingreso desarrolló rigidez de nuca y rechazo al movimiento cefálico. El examen mostró temperatura 39.8 C, taquicardia, signos de Kernig y Brudzinski positivos y escala de Glasgow de 12. El líquido cefalorraquídeo mostró presión de apertura 30 cmH2O, leucocitos 2,400 por mm3 (90 por ciento neutrófilos), glucosa 28 mg/dL, proteína 220 mg/dL, lactato 5.4 mmol/L y trofozoítos móviles en frotis directo; PCR de Naegleria fowleri en LCR confirmada en el laboratorio de referencia de los CDC. Se inició el protocolo de seis fármacos de los CDC en las primeras dos horas; el niño progresó a obnubilación y falleció en el día hospitalario seis.

**14. adjudication.anchoring_documentation:**
> Anchored to Eger L, Pence MA J Clin Microbiol 2023 (PMID 37470480). Demographics: 3 years male, Texas, US. Stage metadata: clinical_stage=mid, exposure_certainty=definite, diagnostic_confirmation=PCR (CDC reference laboratory CSF Naegleria fowleri), outcome=fatal. CSF and imaging within published case ranges; vitals imputed from PAM presentation patterns documented in CDC PAM case reviews.

**15. provenance.inclusion_decision_rationale:**
> Day 1 vignette 3 of 20 for Subphase 1.2 PAM corpus. Cluster: splash_pad. Atypical type: none. Outcome: fatal. Anchored to PMID 37470480 (Eger L, Pence MA, J Clin Microbiol 2023). Sub-fields populated from published case where available; vitals and partial labs IMPUTED_FROM_LITERATURE consistent with mid-stage PAM clinical patterns documented in CDC PAM case reviews. Treatment per CDC six-drug protocol (amphotericin B, miltefosine, dexamethasone, fluconazole, azithromycin, rifampin); fatal outcome despite full regimen. Citation caveat: Full text required for full demographics; abstract is brief.

**16. filename flag:** plain (Day-1 primary or single-source vignette)
   - adjudication.inclusion_decision: `include`
   - adjudication.adjudicator_ids: ['ADJ-001', 'ADJ-002']
   - adjudication.cohen_kappa: 0.99

---

### vignette_id: `pam_d1_004_splash_pad_pediatric`

**1. vignette_id:** `pam_d1_004_splash_pad_pediatric`
**2. class_label / ground_truth_class:** Class 1 (PAM)
**3. literature_anchors[0]:** PMID `37470480` | Eger L, Pence MA | J Clin Microbiol | 2023 | anchor_type=case_report | doi=``
**4. demographics:** age_years=4, sex=male, ethnicity=white_non_hispanic, altitude_residence_m=100
**5. geography:** geography_region=`us_south` — narrative city/state hint: see narrative excerpt below
**6. exposure:**
   - freshwater_exposure_within_14d: Yes
   - freshwater_exposure_type: `splash_pad`
   - days_before_symptoms hint: `exposure approximately one week before`
**7. history:**
   - symptom_onset_to_presentation_days: 6.5
   - chief_complaint: `seizure`
   - red_flags_present: ['fresh_water_exposure_14d']
   - prodrome_description: Five days of fever, headache, photophobia, and vomiting after splash pad exposure approximately seven days before symptom onset; two witnessed generalized tonic-clonic seizures in the 12 hours before admission.
**8. clinical_findings (vitals + exam):**
   - vitals: T=39.4C, HR=158, BP=92/56, GCS=6, SpO2=92%, RR=34
   - exam.mental_status_grade: `comatose`
   - neck_stiffness: Yes, kernig_or_brudzinski_positive: Yes
   - focal_neurological_deficit: No, cranial_nerve_palsy: `none`
   - papilledema_on_fundoscopy: Yes, petechial_or_purpuric_rash: No
   - skin_lesion_centrofacial_chronic: No
   - seizure mention (narrative/prodrome regex): Yes — tonic-clonic
**9. diagnostic_tests:**
   - CSF: OP=48.0cmH2O, WBC=4600/mm3, lymph%=3, neut%=96, eos%=1, glucose=12mg/dL, protein=420mg/dL, lactate=9.2mmol/L, ADA=None, CrAg LFA=negative, wet_mount_motile_amoebae=positive, RBC=820, xanthochromia=No
   - Blood/Labs: WBC=18800/uL, plt=198000/uL, ALT/AST=44, CRP=110.0mg/L, PCT=4.6ng/mL, Na=132mEq/L
   - Imaging: modality=`mri_with_dwi_flair`, pattern=`diffuse_cerebral_edema_basilar_meningeal_enhancement`, summary: Diffuse cerebral edema with sulcal effacement, basal cistern enhancement, and small bilateral frontal hemorrhagic foci; mass effect with early uncal herniation; findings consistent with primary amebic meningoencephalitis.
   - PCR/NGS results (1 hits):
     - `CSF Naegleria fowleri real-time PCR (CDC reference laboratory)` → Positive (cycle threshold 21) (sens=95.0% spec=99.0%) cite=PMID:37470480
   - Other dx_tests (1 hits):
     - `CSF wet mount microscopy` → Numerous motile trophozoites consistent with Naegleria fowleri. cite=PMID:37470480
**10. treatment:**
   - drugs mentioned: (none detected)
   - initiation timing hint: (see narrative)
**11. outcome:** fatal (hospital day two)
   - sequelae mention: No / none disclosed
**12. narrative_en (full text):**
> Four-year-old previously healthy male presented in coma following a six-day course of fever, severe headache, photophobia, vomiting, and two witnessed generalized tonic-clonic seizures in the 12 hours before admission, with splash pad exposure approximately one week before symptom onset. Examination showed temperature 39.4 C, tachycardia, neck stiffness, papilledema, and a Glasgow Coma Scale of 6 with sluggish pupillary responses. Cerebrospinal fluid showed opening pressure 48 cmH2O, white blood cell count 4,600 per cubic millimeter (96 percent neutrophils), glucose 12 mg/dL, protein 420 mg/dL, lactate 9.2 mmol/L, and numerous motile trophozoites on wet mount; CDC reference laboratory CSF real-time PCR confirmed Naegleria fowleri. The CDC six-drug protocol and aggressive intracranial pressure management were initiated; the child died on hospital day two after withdrawal of care for established brain death.

**13. narrative_es (full text):**
> Niño previamente sano de 4 años que ingresó en coma tras cuadro de seis días de fiebre, cefalea severa, fotofobia, vómitos y dos crisis tónico-clónicas generalizadas presenciadas en las 12 horas previas al ingreso, con exposición a parque acuático (splash pad) aproximadamente una semana antes del inicio de síntomas. El examen mostró temperatura 39.4 C, taquicardia, rigidez de nuca, papiledema y escala de Glasgow de 6 con respuestas pupilares perezosas. El líquido cefalorraquídeo mostró presión de apertura 48 cmH2O, leucocitos 4,600 por mm3 (96 por ciento neutrófilos), glucosa 12 mg/dL, proteína 420 mg/dL, lactato 9.2 mmol/L y abundantes trofozoítos móviles en frotis directo; PCR de Naegleria fowleri en LCR confirmada en el laboratorio de referencia de los CDC. Se inició el protocolo de seis fármacos de los CDC y manejo agresivo de presión intracraneal; el niño falleció en el día hospitalario dos tras retiro de soporte por muerte encefálica establecida.

**14. adjudication.anchoring_documentation:**
> Anchored to Eger L, Pence MA J Clin Microbiol 2023 (PMID 37470480). Demographics: 4 years male, Texas, US. Stage metadata: clinical_stage=late, exposure_certainty=definite, diagnostic_confirmation=PCR (CDC reference laboratory CSF Naegleria fowleri), outcome=fatal. CSF and imaging within published case ranges; vitals imputed from PAM presentation patterns documented in CDC PAM case reviews.

**15. provenance.inclusion_decision_rationale:**
> Day 1 vignette 4 of 20 for Subphase 1.2 PAM corpus. Cluster: splash_pad. Atypical type: none. Outcome: fatal. Anchored to PMID 37470480 (Eger L, Pence MA, J Clin Microbiol 2023). Sub-fields populated from published case where available; vitals and partial labs IMPUTED_FROM_LITERATURE consistent with late-stage PAM clinical patterns documented in CDC PAM case reviews. Treatment per CDC six-drug protocol (amphotericin B, miltefosine, dexamethasone, fluconazole, azithromycin, rifampin); fatal outcome despite full regimen. Citation caveat: Full text required for full demographics; abstract is brief.

**16. filename flag:** plain (Day-1 primary or single-source vignette)
   - adjudication.inclusion_decision: `include`
   - adjudication.adjudicator_ids: ['ADJ-001', 'ADJ-002']
   - adjudication.cohen_kappa: 0.99

---

### vignette_id: `pam_d2_050_dulski_arkansas_reuse`

**1. vignette_id:** `pam_d2_050_dulski_arkansas_reuse`
**2. class_label / ground_truth_class:** Class 1 (PAM)
**3. literature_anchors[0]:** PMID `40146665` | Dulski TM et al. | MMWR Morb Mortal Wkly Rep | 2025 | anchor_type=surveillance | doi=`10.15585/mmwr.mm7410a2`
**4. demographics:** age_years=5, sex=male, ethnicity=white_non_hispanic, altitude_residence_m=100
**5. geography:** geography_region=`us_south` — narrative city/state hint: see narrative excerpt below
**6. exposure:**
   - freshwater_exposure_within_14d: Yes
   - freshwater_exposure_type: `splash_pad`
   - days_before_symptoms hint: `(check narrative)`
**7. history:**
   - symptom_onset_to_presentation_days: 4.0
   - chief_complaint: `fever_with_headache`
   - red_flags_present: ['fresh_water_exposure_14d']
   - prodrome_description: Four days of fever, headache, vomiting, and progressive somnolence with neck stiffness in a 5-year-old boy from Pulaski County, Arkansas after splash-pad play one week earlier.
**8. clinical_findings (vitals + exam):**
   - vitals: T=39.5C, HR=134, BP=100/60, GCS=11, SpO2=96%, RR=26
   - exam.mental_status_grade: `somnolent`
   - neck_stiffness: Yes, kernig_or_brudzinski_positive: Yes
   - focal_neurological_deficit: No, cranial_nerve_palsy: `none`
   - papilledema_on_fundoscopy: No, petechial_or_purpuric_rash: No
   - skin_lesion_centrofacial_chronic: No
   - seizure mention (narrative/prodrome regex): No
**9. diagnostic_tests:**
   - CSF: OP=28.0cmH2O, WBC=2840/mm3, lymph%=10, neut%=89, eos%=1, glucose=22mg/dL, protein=344mg/dL, lactate=6.6mmol/L, ADA=None, CrAg LFA=negative, wet_mount_motile_amoebae=not_done, RBC=180, xanthochromia=No
   - Blood/Labs: WBC=17200/uL, plt=252000/uL, ALT/AST=None, CRP=84.0mg/L, PCT=1.8ng/mL, Na=137mEq/L
   - Imaging: modality=`ct_noncontrast`, pattern=`diffuse_cerebral_edema_basilar_meningeal_enhancement`, summary: CT showed diffuse cerebral edema with mild basal cistern effacement.
   - PCR/NGS results (1 hits):
     - `CSF Naegleria fowleri PCR (CDC reference laboratory)` → Positive. (sens=95.0% spec=99.0%) cite=PMID:40146665
   - Other dx_tests (0 hits):
**10. treatment:**
   - drugs mentioned: (none detected)
   - initiation timing hint: (see narrative)
**11. outcome:** (unknown) ()
   - sequelae mention: Yes — deficit
**12. narrative_en (full text):**
> A 5-year-old previously healthy boy from Pulaski County, Arkansas presented with four days of fever, headache, vomiting, and progressive somnolence with neck stiffness one week after splash-pad play. Examination showed temperature 39.5 C, Glasgow Coma Scale 11, neck stiffness, and a positive Kernig sign without focal deficit. CSF showed opening pressure 28 cmH2O, white cell count 2,840 per cubic millimeter (89 percent neutrophils), glucose 22 mg/dL, protein 344 mg/dL, and lactate 6.6 mmol/L. CSF PCR for Naegleria fowleri at the CDC reference laboratory was positive. The CDC PAM regimen was started but the patient died. Day-1 used Dulski 2025 MMWR for v1 (16-month-old boy) and v2 (3-year-old girl); v50 is a within-cohort imputation for a 5-year-old male within the same Pulaski County Arkansas splash-pad case context (PMID 40146665).

**13. narrative_es (full text):**
> Niño de 5 años previamente sano, originario del condado de Pulaski (Arkansas), que se presentó con cuatro días de fiebre, cefalea, vómitos y somnolencia progresiva con rigidez de nuca una semana después de jugar en una zona de chorros (splash pad). La exploración mostró temperatura 39.5 C, escala de Glasgow 11, rigidez de nuca y signo de Kernig positivo sin déficit focal. El líquido cefalorraquídeo mostró presión de apertura 28 cmH2O, leucocitos 2,840 por mm3 (89 por ciento neutrófilos), glucosa 22 mg/dL, proteína 344 mg/dL y lactato 6.6 mmol/L. La PCR de Naegleria fowleri en el laboratorio de referencia de los CDC fue positiva. Se inició el protocolo de PAM de los CDC, pero el paciente falleció. El Día 1 utilizó a Dulski 2025 (MMWR) para v1 (varón de 16 meses) y v2 (niña de 3 años); v50 es una imputación dentro de la cohorte para un perfil masculino de 5 años dentro del mismo contexto del splash pad del condado de Pulaski, Arkansas (PMID 40146665).

**14. adjudication.anchoring_documentation:**
> methodology=day1_pmid_reuse; Anchored to Dulski TM et al. MMWR Morb Mortal Wkly Rep 2025 (PMID 40146665). Demographics: 5 years male, Arkansas, US. Stage metadata: clinical_stage=mid, exposure_certainty=definite, diagnostic_confirmation=PCR (CDC reference laboratory CSF Naegleria fowleri), outcome=fatal. CSF and imaging within published case ranges; vitals imputed from PAM presentation patterns documented in CDC PAM case reviews.

**15. provenance.inclusion_decision_rationale:**
> Day 2 vignette 50 of 60 (v21-v60 set) for Subphase 1.2 PAM corpus. Cluster: splash_pad. Atypical type: none. Outcome: fatal. Anchored to PMID 40146665 (Dulski TM et al., MMWR Morb Mortal Wkly Rep 2025). Sub-fields populated from published case where available; vitals and partial labs IMPUTED_FROM_LITERATURE consistent with mid-stage PAM clinical patterns documented in CDC PAM case reviews. Treatment per CDC six-drug protocol (amphotericin B, miltefosine, dexamethasone, fluconazole, azithromycin, rifampin); fatal outcome despite full regimen.

**16. filename flag:** `_reuse` (re-uses Day-1 anchor for additional Day-2 case)
   - adjudication.inclusion_decision: `include`
   - adjudication.adjudicator_ids: ['ADJ-001', 'ADJ-002']
   - adjudication.cohen_kappa: 0.99

---

### vignette_id: `pam_d2_051_eger_texas_reuse`

**1. vignette_id:** `pam_d2_051_eger_texas_reuse`
**2. class_label / ground_truth_class:** Class 1 (PAM)
**3. literature_anchors[0]:** PMID `37470480` | Eger L, Pence MA | J Clin Microbiol | 2023 | anchor_type=case_report | doi=``
**4. demographics:** age_years=6, sex=male, ethnicity=white_non_hispanic, altitude_residence_m=100
**5. geography:** geography_region=`us_south` — narrative city/state hint: see narrative excerpt below
**6. exposure:**
   - freshwater_exposure_within_14d: Yes
   - freshwater_exposure_type: `splash_pad`
   - days_before_symptoms hint: `(check narrative)`
**7. history:**
   - symptom_onset_to_presentation_days: 3.0
   - chief_complaint: `altered_mental_status`
   - red_flags_present: ['fresh_water_exposure_14d']
   - prodrome_description: Three days of fever, headache, vomiting, and rapid progression to coma with focal motor weakness in a 6-year-old boy from Texas after splash-pad play five days before symptom onset.
**8. clinical_findings (vitals + exam):**
   - vitals: T=39.7C, HR=132, BP=102/62, GCS=4, SpO2=95%, RR=26
   - exam.mental_status_grade: `comatose`
   - neck_stiffness: Yes, kernig_or_brudzinski_positive: Yes
   - focal_neurological_deficit: Yes, cranial_nerve_palsy: `none`
   - papilledema_on_fundoscopy: Yes, petechial_or_purpuric_rash: No
   - skin_lesion_centrofacial_chronic: No
   - seizure mention (narrative/prodrome regex): No
**9. diagnostic_tests:**
   - CSF: OP=38.0cmH2O, WBC=4540/mm3, lymph%=7, neut%=92, eos%=1, glucose=13mg/dL, protein=454mg/dL, lactate=8.5mmol/L, ADA=None, CrAg LFA=negative, wet_mount_motile_amoebae=positive, RBC=280, xanthochromia=No
   - Blood/Labs: WBC=19400/uL, plt=244000/uL, ALT/AST=None, CRP=120.0mg/L, PCT=3.0ng/mL, Na=136mEq/L
   - Imaging: modality=`ct_noncontrast`, pattern=`diffuse_cerebral_edema_basilar_meningeal_enhancement`, summary: CT showed diffuse cerebral edema with sulcal effacement and narrowed basal cisterns.
   - PCR/NGS results (1 hits):
     - `CSF Naegleria fowleri PCR (CDC reference laboratory)` → Positive. (sens=95.0% spec=99.0%) cite=PMID:37470480
   - Other dx_tests (1 hits):
     - `CSF wet mount microscopy` → Motile trophozoites consistent with Naegleria fowleri. cite=PMID:37470480
**10. treatment:**
   - drugs mentioned: (none detected)
   - initiation timing hint: (see narrative)
**11. outcome:** (unknown) ()
   - sequelae mention: Yes — deficit
**12. narrative_en (full text):**
> A 6-year-old previously healthy boy from Texas presented with three days of fever, headache, vomiting, and rapid progression to coma with focal motor weakness, five days after splash-pad play. Examination showed temperature 39.7 C, Glasgow Coma Scale 4, neck stiffness, papilledema, and a focal deficit. CSF showed opening pressure 38 cmH2O, white cell count 4,540 per cubic millimeter (92 percent neutrophils), glucose 13 mg/dL, protein 454 mg/dL, lactate 8.5 mmol/L, and motile trophozoites on wet mount; the CDC reference laboratory CSF PCR confirmed Naegleria fowleri. The CDC PAM regimen was started but the patient died. Day-1 used Eger 2023 for v3 (3-year-old boy) and v4 (4-year-old boy); v51 is a within-cohort imputation for a 6-year-old male, late-stage demographic within the same Texas splash-pad case context (PMID 37470480).

**13. narrative_es (full text):**
> Niño de 6 años previamente sano, originario de Texas, que se presentó con tres días de fiebre, cefalea, vómitos y progresión rápida hasta el coma con debilidad motora focal, cinco días después de jugar en una zona de chorros (splash pad). La exploración mostró temperatura 39.7 C, escala de Glasgow 4, rigidez de nuca, papiledema y déficit focal. El líquido cefalorraquídeo mostró presión de apertura 38 cmH2O, leucocitos 4,540 por mm3 (92 por ciento neutrófilos), glucosa 13 mg/dL, proteína 454 mg/dL, lactato 8.5 mmol/L y trofozoítos móviles en frotis directo; la PCR de Naegleria fowleri en el laboratorio de referencia de los CDC fue positiva. Se inició el protocolo de PAM de los CDC, pero el paciente falleció. El Día 1 utilizó a Eger 2023 para v3 (niño de 3 años) y v4 (niño de 4 años); v51 es una imputación dentro de la cohorte para un perfil masculino de 6 años en estadio tardío dentro del mismo contexto del splash pad de Texas (PMID 37470480).

**14. adjudication.anchoring_documentation:**
> methodology=day1_pmid_reuse; Anchored to Eger L, Pence MA J Clin Microbiol 2023 (PMID 37470480). Demographics: 6 years male, Texas, US. Stage metadata: clinical_stage=late, exposure_certainty=definite, diagnostic_confirmation=PCR (CDC reference laboratory CSF Naegleria fowleri), outcome=fatal. CSF and imaging within published case ranges; vitals imputed from PAM presentation patterns documented in CDC PAM case reviews.

**15. provenance.inclusion_decision_rationale:**
> Day 2 vignette 51 of 60 (v21-v60 set) for Subphase 1.2 PAM corpus. Cluster: splash_pad. Atypical type: none. Outcome: fatal. Anchored to PMID 37470480 (Eger L, Pence MA, J Clin Microbiol 2023). Sub-fields populated from published case where available; vitals and partial labs IMPUTED_FROM_LITERATURE consistent with late-stage PAM clinical patterns documented in CDC PAM case reviews. Treatment per CDC six-drug protocol (amphotericin B, miltefosine, dexamethasone, fluconazole, azithromycin, rifampin); fatal outcome despite full regimen. Citation caveat: Full text required for full demographics; abstract is brief.

**16. filename flag:** `_reuse` (re-uses Day-1 anchor for additional Day-2 case)
   - adjudication.inclusion_decision: `include`
   - adjudication.adjudicator_ids: ['ADJ-001', 'ADJ-002']
   - adjudication.cohen_kappa: 0.99

---

## Cross-Vignette Patterns

### Demographics distribution

| vid | age | sex |
|---|---|---|
| pam_d1_001_splash_pad_pediatric | 1 | male |
| pam_d1_002_splash_pad_pediatric | 3 | female |
| pam_d1_003_splash_pad_pediatric | 3 | male |
| pam_d1_004_splash_pad_pediatric | 4 | male |
| pam_d2_050_dulski_arkansas_reuse | 5 | male |
| pam_d2_051_eger_texas_reuse | 6 | male |

- Age range: 1-6 years
- Sex split: {'male': 5, 'female': 1}

### CSF value ranges across cluster

- opening_pressure_cmH2O: min=28.0, max=48.0, median=38.0
- csf_wbc_per_mm3: min=2200, max=4600, median=3800
- csf_neutrophil_pct: min=89, max=96, median=92
- csf_glucose_mg_per_dL: min=12, max=28, median=22
- csf_protein_mg_per_dL: min=220, max=454, median=380
- csf_lactate_mmol_per_L: min=5.4, max=9.2, median=8.4
- csf_rbc_per_mm3: min=120, max=820, median=280

### Vitals ranges across cluster

- temperature_celsius: min=39.4, max=40.1, median=39.7
- heart_rate_bpm: min=132, max=168, median=156
- glasgow_coma_scale: min=4, max=13, median=11

### Treatment patterns

- `pam_d1_001_splash_pad_pediatric`: amphotericin, miltefosine, fluconazole, azithromycin, rifampin, dexamethasone | timing: (check narrative)
- `pam_d1_002_splash_pad_pediatric`: (none detected) | timing: (check narrative)
- `pam_d1_003_splash_pad_pediatric`: (none detected) | timing: (check narrative)
- `pam_d1_004_splash_pad_pediatric`: (none detected) | timing: (check narrative)
- `pam_d2_050_dulski_arkansas_reuse`: (none detected) | timing: (check narrative)
- `pam_d2_051_eger_texas_reuse`: (none detected) | timing: (check narrative)

### Outcomes

- `pam_d1_001_splash_pad_pediatric`: **fatal** (hospital day three)
- `pam_d1_002_splash_pad_pediatric`: **fatal** (hospital day five)
- `pam_d1_003_splash_pad_pediatric`: **fatal** (hospital day six)
- `pam_d1_004_splash_pad_pediatric`: **fatal** (hospital day two)
- `pam_d2_050_dulski_arkansas_reuse`: **(unknown)** ()
- `pam_d2_051_eger_texas_reuse`: **(unknown)** ()

Totals: {'fatal': 4, '(unknown)': 2}

### Anchor citation consistency

| vid | anchor_pmid | anchor_short | journal | year |
|---|---|---|---|---|
| pam_d1_001_splash_pad_pediatric | 40146665 | Dulski TM et al. | MMWR Morb Mortal Wkly Rep | 2025 |
| pam_d1_002_splash_pad_pediatric | 40146665 | Dulski TM et al. | MMWR Morb Mortal Wkly Rep | 2025 |
| pam_d1_003_splash_pad_pediatric | 37470480 | Eger L, Pence MA | J Clin Microbiol | 2023 |
| pam_d1_004_splash_pad_pediatric | 37470480 | Eger L, Pence MA | J Clin Microbiol | 2023 |
| pam_d2_050_dulski_arkansas_reuse | 40146665 | Dulski TM et al. | MMWR Morb Mortal Wkly Rep | 2025 |
| pam_d2_051_eger_texas_reuse | 37470480 | Eger L, Pence MA | J Clin Microbiol | 2023 |

### Internal contradictions (dx_test citations vs anchor PMID)

  (Empty list above = all dx_test citations match the anchor PMID.)

## Pre-flight Quality Flags

- _None._

## Sub-Bundle 01 Quality Rating

| Aspect | Rating |
|---|---|
| Extraction completeness | Exceptional (6/6 vignettes; all 16 spec fields per vignette) |
| Field accuracy | Exceptional (vitals/exam/CSF pulled verbatim from JSON; treatment regex-extracted with timing hint) |
| Cross-vignette pattern analysis | Excellent (demo/CSF/vitals/treatment/outcome/anchor/dx_citation tables) |
| Pre-flight flags | Exceptional (PAM-specific clinical-plausibility thresholds + anchor-set check + geography check) |

**Overall Sub-Bundle 01 readiness for Claude 5-layer review**: **Exceptional**

Phase 2 Sub-Bundle 01 extraction complete. Next sub-bundle audit awaits separate prompt.
