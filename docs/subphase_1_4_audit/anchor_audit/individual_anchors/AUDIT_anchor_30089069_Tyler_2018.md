# AUDIT bundle: PMID 30089069 | Tyler 2018

Generated: 2026-05-11
Vignettes in bundle: 13
Build status: NCBI fetched
Bundle type: BIG (n>=5 vignettes single-anchor)

## Anchor: PMID 30089069 | Tyler 2018

### Registry metadata (current state)

```json
{
  "pmid": "30089069",
  "doi": "10.1056/NEJMra1708714",
  "authors_short": "Tyler KL",
  "authors_full": [
    "Tyler KL"
  ],
  "journal": "N Engl J Med",
  "journal_short_code": "NEJM",
  "year": 2018,
  "volume": "379",
  "issue": "6",
  "pages": "557-566",
  "title": "Acute Viral Encephalitis",
  "anchor_type": "review",
  "anchor_subtype": "viral_encephalitis_clinical_review",
  "verification_confidence": 0.95,
  "verification_method": "claude_web_pubmed_ncbi_esummary_2026_05_11",
  "last_verified_date": "2026-05-11",
  "caveat": "NEJM clinical review of acute viral encephalitis. Anchor for Class 3 enterovirus + arboviral + HSV-2/VZV vignettes; documents pathogen-specific imaging and CSF profiles. Errata 5.4.3.1: PMID corrected from 29490180 (a NEJM Letter on breast cancer recurrence) to 30089069 per NCBI E-utilities verification 2026-05-11. Volume/issue/pages corrected to 379(6):557-566 (NEJM 2018-08-09 issue)."
}
```

### NCBI live re-fetch (2026-05-11)

```json
{
  "uid": "30089069",
  "pubdate": "2018 Aug 9",
  "epubdate": "",
  "source": "N Engl J Med",
  "authors": [
    {
      "name": "Tyler KL",
      "authtype": "Author",
      "clusterid": ""
    }
  ],
  "lastauthor": "Tyler KL",
  "title": "Acute Viral Encephalitis.",
  "sorttitle": "acute viral encephalitis",
  "volume": "379",
  "issue": "6",
  "pages": "557-566",
  "lang": [
    "eng"
  ],
  "nlmuniqueid": "0255562",
  "issn": "0028-4793",
  "essn": "1533-4406",
  "pubtype": [
    "Journal Article",
    "Review"
  ],
  "recordstatus": "PubMed - indexed for MEDLINE",
  "pubstatus": "4",
  "articleids": [
    {
      "idtype": "pubmed",
      "idtypen": 1,
      "value": "30089069"
    },
    {
      "idtype": "doi",
      "idtypen": 3,
      "value": "10.1056/NEJMra1708714"
    }
  ],
  "history": [
    {
      "pubstatus": "entrez",
      "date": "2018/08/09 06:00"
    },
    {
      "pubstatus": "pubmed",
      "date": "2018/08/09 06:00"
    },
    {
      "pubstatus": "medline",
      "date": "2018/08/17 06:00"
    }
  ],
  "references": [],
  "attributes": [],
  "pmcrefcount": "",
  "fulljournalname": "The New England journal of medicine",
  "elocationid": "doi: 10.1056/NEJMra1708714",
  "doctype": "citation",
  "srccontriblist": [],
  "booktitle": "",
  "medium": "",
  "edition": "",
  "publisherlocation": "",
  "publishername": "",
  "srcdate": "",
  "reportnumber": "",
  "availablefromurl": "",
  "locationlabel": "",
  "doccontriblist": [],
  "docdate": "",
  "bookname": "",
  "chapter": "",
  "sortpubdate": "2018/08/09 00:00",
  "sortfirstauthor": "Tyler KL",
  "vernaculartitle": ""
}
```

### Registry-vs-NCBI delta

- ALL FIELDS MATCH ✓

### Vignettes citing this anchor (13 total)

#### Vignette: vid=096 file=vir_096_hsv1_adult.json class=3 subphase=1.3 VIRAL

```
ANCHOR:
  pmid: 30089069
  first_author: Tyler
  year: 2018
  journal: NEJM
  citation_type: review
  doi: 10.1056/NEJMra1708714

DEMOGRAPHICS:
  age_years: 45  sex: female  region: other_global
  ethnicity: white_non_hispanic  altitude_m: 5
  hiv_status: negative  cd4: None
  pregnancy_red_flag: False
  immunocompromise_status: none
  freshwater_exposure_14d: False (None)

HISTORY:
  symptom_onset_to_presentation_days: 4.0
  chief_complaint: altered_mental_status
  red_flags_present: []
  prodrome_description: 45-year-old female, Netherlands. 4-day progressive course: fever 38.7 C, severe headache, behavioral change with personality alteration day 2, expressive aphasia day 3, right-sided focal seizure day 4 prompting tertiary ED Amsterdam. No neck stiffness. No freshwater. Acyclovir hour 5. Outcome: survived with mild memory deficit per Tyler review HSE residual-deficit rate.

VITALS:
  T:38.7C HR:96 BP:128/78 GCS:12 SpO2:97% RR:18

EXAM:
  mental_status: confused  neck_stiff: False  kernig_brudz: False
  cranial_nerve_palsy: none  papilledema: False  focal_deficit: True
  skin_lesion_centrofacial_chronic: False  rash: False

LABS:
  WBC:8200 Plt:245000 ALT/AST:26 CRP:18.0 PCT:0.3 Na:138

CSF:
  OP:22.0cmH2O  WBC:220/mm3  lymph%:75 neut%:25 eos%:0
  glucose:55mg/dL protein:120mg/dL lactate:2.6mmol/L ADA:NoneU/L
  crag_lfa:negative  wet_mount:negative  xanthochromia:True  RBC:35

IMAGING:
  modality: mri_with_dwi_flair  pattern: mesial_temporal_t2_flair_hyperintensity
  finding_count: 1
  text_summary: MRI brain with DWI/FLAIR: mesial temporal T2/FLAIR hyperintensity asymmetric with basal ganglia sparing. Canonical HSE imaging signature per Tyler 2018 NEJM viral encephalitis review.

DIAGNOSTIC_TESTS:
  total_results: 3
  pcr_panel: positive
  xpert_mtb_rif: n/a
  blood_culture: n/a
  csf_culture: n/a
  serology_or_antigen: n/a
  smear_or_gram: n/a
  brain_biopsy: n/a

NARRATIVE_EN: A 45-year-old woman in the Netherlands presented to a tertiary emergency department in Amsterdam with a 4-day progressive course: fever to 38.7 C, severe headache, behavioral change with personality alteration on day 2, expressive aphasia on day 3, and a right-sided focal seizure on day 4 prompting ED presentation. She had no neck stiffness on examination and no antecedent freshwater exposure. Examination on admission: Glasgow Coma Scale 12, focal neurological deficit (expressive aphasia). CSF showed opening pressure 22 cmH2O, white cell count 220 per cubic millimeter (75 percent lymphocytes), glucose 55 mg/dL, protein 120 mg/dL, RBC 35 with mild xanthochromia (canonical hemorrhagic component). CSF HSV-1 PCR positive. Brain MRI with DWI/FLAIR showed mesial temporal T2/FLAIR hyperintensity asymmetric with basal ganglia sparing. Acyclovir initiated within five hours. Anchored to Tyler 2018 NEJM viral encephalitis review (PMID 30089069). Outcome: survived with mild memory deficit. Subphase 1.3 commit 5.3.5 wave 1, pre-adjudication hold_for_revision.

NARRATIVE_ES: Mujer de 45 anos en Paises Bajos (Amsterdam), ingresada a urgencias terciarias con curso progresivo de cuatro dias: fiebre 38.7 C, cefalea intensa, cambio conductual con alteracion de personalidad al segundo dia, afasia expresiva al tercer dia, crisis focal derecha al cuarto dia que motivo consulta. Sin rigidez de nuca al examen. Sin exposicion a agua dulce. Examen: escala de Glasgow 12, deficit focal (afasia expresiva). Liquido cefalorraquideo mostro presion de apertura 22 cmH2O, leucocitos 220 por mm3 (75 por ciento linfocitos), glucosa 55 mg/dL, proteina 120 mg/dL, eritrocitos 35 con xantocromia leve. PCR de HSV-1 positiva. RM cerebral mostro hiperintensidad temporal mesial T2/FLAIR asimetrica con preservacion de ganglios basales. Anclaje en revision Tyler 2018 NEJM encefalitis viral aguda (PMID 30089069). Subphase 1.3 commit 5.3.5 wave 1.

RATIONALE: Anchored to PMID 30089069 (Tyler KL 2018 NEJM clinical review of acute viral encephalitis), HSV1 mesial-temporal-encephalitis phenotype. Demographic anchor (45yo F adult HSE) sits in adult-HSE stratum (HSE bimodal age, peaks at adulthood). CSF lymphocytic (220 WBC, 75 percent lymphocytes), normal glucose 55, mildly elevated protein 120, RBC 35 with xanthochromia (hemorrhagic temporal necrosis component). MRI mesial temporal T2/FLAIR hyperintensity per master prompt 1.3.4 mandate. Imputation tiers: tier_1_primary={age, sex, hsv1_pcr, imaging_pattern, focal_aphasia}; tier_3_within_review={csf_wbc, neutrophil_pct, glucose, protein, rbc, xanthochromia, gcs}; tier_4_priors={temp, symptom_days}. Indeterminate=none. Diagnostic_ambiguity=false. Outcome=survived_mild_memory_deficit. Acyclovir_hours=5. Tier: tier_3_imputation_within_review. 5.3.5 wave1 HSV1-NL-adult-female.

ANCHORING_EXTRAS: stage=pre_adjudication; status=pending_external_review; self_review_disposition=hold_for_revision; self_review_notes=wave 5.3.5 VIRAL vignette anchored to PMID 30089069 (Tyler 2018 NEJM viral encephalitis review); external clinical adjudication pending; classification provisional. adjudicator_ids=VIRAL-WAVE1-PRE-ADJ-1, VIRAL-WAVE1-PRE-ADJ-2 (sentinel); cohen_kappa=0.0 placeholder; adjudicator_name=null; adjudication_date=null; post_adjudication_disposition=null. Subphase 1.3 commit 5.3.5 (2026-05-08). anchor=Tyler-NEJM-2018 stratum=HSV1-adult-HSE.

ADJUDICATION:
  inclusion_decision: hold_for_revision  ground_truth_class: 3  kappa: 0.0
  adjudicator_ids: ['VIRAL-WAVE1-PRE-ADJ-1', 'VIRAL-WAVE1-PRE-ADJ-2']
  disagreement_resolution: None
```

#### Vignette: vid=099 file=vir_099_hsv1_lima_adult.json class=3 subphase=1.3 VIRAL

```
ANCHOR:
  pmid: 30089069
  first_author: Tyler
  year: 2018
  journal: NEJM
  citation_type: review
  doi: 10.1056/NEJMra1708714

DEMOGRAPHICS:
  age_years: 38  sex: male  region: peru_lima_coast
  ethnicity: mestizo  altitude_m: 154
  hiv_status: negative  cd4: None
  pregnancy_red_flag: False
  immunocompromise_status: none
  freshwater_exposure_14d: False (None)

HISTORY:
  symptom_onset_to_presentation_days: 5.0
  chief_complaint: seizure
  red_flags_present: []
  prodrome_description: 38-year-old male in Lima, Peru. 5-day course: low-grade fever 38.5 C, severe headache, then new-onset olfactory hallucinations day 3, expressive aphasia day 4, complex partial seizure day 5 prompting tertiary urban ED. No neck stiffness. No freshwater. Acyclovir hour 8. Outcome: survived with mild memory deficit.

VITALS:
  T:38.5C HR:92 BP:124/76 GCS:13 SpO2:97% RR:18

EXAM:
  mental_status: confused  neck_stiff: False  kernig_brudz: False
  cranial_nerve_palsy: none  papilledema: False  focal_deficit: True
  skin_lesion_centrofacial_chronic: False  rash: False

LABS:
  WBC:9100 Plt:250000 ALT/AST:30 CRP:22.0 PCT:0.4 Na:138

CSF:
  OP:21.0cmH2O  WBC:180/mm3  lymph%:78 neut%:22 eos%:0
  glucose:58mg/dL protein:105mg/dL lactate:2.4mmol/L ADA:NoneU/L
  crag_lfa:negative  wet_mount:negative  xanthochromia:True  RBC:28

IMAGING:
  modality: mri_with_dwi_flair  pattern: mesial_temporal_t2_flair_hyperintensity
  finding_count: 1
  text_summary: MRI brain with DWI/FLAIR: mesial temporal T2/FLAIR hyperintensity asymmetric with basal ganglia sparing. Canonical HSE imaging signature per Tyler 2018 NEJM viral encephalitis review.

DIAGNOSTIC_TESTS:
  total_results: 3
  pcr_panel: positive
  xpert_mtb_rif: n/a
  blood_culture: n/a
  csf_culture: n/a
  serology_or_antigen: n/a
  smear_or_gram: n/a
  brain_biopsy: n/a

NARRATIVE_EN: A 38-year-old man in Lima, Peru presented to a tertiary urban emergency department with a 5-day course: low-grade fever to 38.5 C, severe headache, then new-onset olfactory hallucinations on day 3, expressive aphasia on day 4, and a complex partial seizure on day 5 prompting ED presentation. He had no neck stiffness on examination and no antecedent freshwater exposure. Examination on admission: Glasgow Coma Scale 13, focal neurological deficit (expressive aphasia and olfactory hallucinations). CSF showed opening pressure 21 cmH2O, white cell count 180 per cubic millimeter (78 percent lymphocytes), glucose 58 mg/dL, protein 105 mg/dL, RBC 28 with mild xanthochromia. CSF HSV-1 PCR positive. Brain MRI with DWI/FLAIR showed mesial temporal T2/FLAIR hyperintensity asymmetric with basal ganglia sparing. Acyclovir initiated within eight hours. Anchored to Tyler 2018 NEJM viral encephalitis review (PMID 30089069), Peru-Lima coastal stratum. Outcome: survived with mild memory deficit. Subphase 1.3 commit 5.3.5 wave 1, pre-adjudication hold_for_revision.

NARRATIVE_ES: Varon de 38 anos en Lima, Peru, ingresado a urgencias urbanas terciarias con curso de cinco dias: febricula 38.5 C, cefalea intensa, alucinaciones olfativas de novo al tercer dia, afasia expresiva al cuarto dia y crisis parcial compleja al quinto dia que motivo consulta. Sin rigidez de nuca al examen. Sin exposicion a agua dulce. Examen: escala de Glasgow 13, deficit focal (afasia expresiva, alucinaciones olfativas). Liquido cefalorraquideo mostro presion de apertura 21 cmH2O, leucocitos 180 por mm3 (78 por ciento linfocitos), glucosa 58 mg/dL, proteina 105 mg/dL, eritrocitos 28 con xantocromia leve. PCR de HSV-1 positiva. RM cerebral mostro hiperintensidad temporal mesial T2/FLAIR asimetrica. Anclaje en revision Tyler 2018 NEJM (PMID 30089069), estrato Lima coastal. Subphase 1.3 commit 5.3.5 wave 1.

RATIONALE: Anchored to PMID 30089069 (Tyler 2018 NEJM viral encephalitis review). HSV1 mesial-temporal-encephalitis phenotype with olfactory hallucinations + aphasia + partial seizure (classic limbic-dominant signature). Demographic anchor (38yo M Lima) sits in adult-HSE stratum + Peru-coastal-tertiary-care stratum. CSF lymphocytic with hemorrhagic component. MRI mesial temporal pattern. Imputation tiers: tier_1_primary={age, sex, region, hsv1_pcr, imaging_pattern, olfactory_hallucinations, aphasia}; tier_3_within_review={csf_wbc, neutrophil_pct, glucose, protein, rbc, xanthochromia, gcs}; tier_4_priors={temp, symptom_days}. Indeterminate=none. Diagnostic_ambiguity=false. Outcome=survived_mild_memory_deficit. Acyclovir_hours=8. Tier: tier_3_imputation_within_review. 5.3.5 wave1 HSV1-Lima-adult-male.

ANCHORING_EXTRAS: stage=pre_adjudication; status=pending_external_review; self_review_disposition=hold_for_revision; self_review_notes=wave 5.3.5 VIRAL vignette anchored to PMID 30089069 (Tyler 2018 NEJM viral encephalitis review); external clinical adjudication pending; classification provisional. adjudicator_ids=VIRAL-WAVE1-PRE-ADJ-1, VIRAL-WAVE1-PRE-ADJ-2 (sentinel); cohen_kappa=0.0 placeholder; adjudicator_name=null; adjudication_date=null; post_adjudication_disposition=null. Subphase 1.3 commit 5.3.5 (2026-05-08). anchor=Tyler-NEJM-2018 region=Lima-Peru.

ADJUDICATION:
  inclusion_decision: hold_for_revision  ground_truth_class: 3  kappa: 0.0
  adjudicator_ids: ['VIRAL-WAVE1-PRE-ADJ-1', 'VIRAL-WAVE1-PRE-ADJ-2']
  disagreement_resolution: None
```

#### Vignette: vid=102 file=vir_102_hsv1_adult.json class=3 subphase=1.3 VIRAL

```
ANCHOR:
  pmid: 30089069
  first_author: Tyler
  year: 2018
  journal: NEJM
  citation_type: review
  doi: 10.1056/NEJMra1708714

DEMOGRAPHICS:
  age_years: 50  sex: male  region: other_global
  ethnicity: white_non_hispanic  altitude_m: 5
  hiv_status: negative  cd4: None
  pregnancy_red_flag: False
  immunocompromise_status: none
  freshwater_exposure_14d: False (None)

HISTORY:
  symptom_onset_to_presentation_days: 6.0
  chief_complaint: behavioral_change
  red_flags_present: []
  prodrome_description: 50-year-old male, Netherlands. 6-day course: low-grade fever 38.4 C, headache, then progressive behavioral change with disinhibition day 3, anomic aphasia day 4, left-sided focal seizure day 6 prompting tertiary ED Amsterdam. No neck stiffness. No freshwater. Acyclovir hour 4. Outcome: survived with moderate memory deficit.

VITALS:
  T:38.4C HR:88 BP:132/80 GCS:11 SpO2:96% RR:18

EXAM:
  mental_status: somnolent  neck_stiff: False  kernig_brudz: False
  cranial_nerve_palsy: none  papilledema: False  focal_deficit: True
  skin_lesion_centrofacial_chronic: False  rash: False

LABS:
  WBC:9600 Plt:235000 ALT/AST:28 CRP:24.0 PCT:0.4 Na:137

CSF:
  OP:24.0cmH2O  WBC:250/mm3  lymph%:72 neut%:28 eos%:0
  glucose:52mg/dL protein:135mg/dL lactate:2.8mmol/L ADA:NoneU/L
  crag_lfa:negative  wet_mount:negative  xanthochromia:True  RBC:40

IMAGING:
  modality: mri_with_dwi_flair  pattern: mesial_temporal_t2_flair_hyperintensity
  finding_count: 1
  text_summary: MRI brain with DWI/FLAIR: mesial temporal T2/FLAIR hyperintensity asymmetric with basal ganglia sparing. Canonical HSE imaging signature per Tyler 2018 NEJM viral encephalitis review.

DIAGNOSTIC_TESTS:
  total_results: 3
  pcr_panel: positive
  xpert_mtb_rif: n/a
  blood_culture: n/a
  csf_culture: n/a
  serology_or_antigen: n/a
  smear_or_gram: n/a
  brain_biopsy: n/a

NARRATIVE_EN: A 50-year-old man in the Netherlands presented to a tertiary emergency department in Amsterdam with a 6-day course: low-grade fever to 38.4 C, headache, then progressive behavioral change with disinhibition on day 3, anomic aphasia on day 4, and a left-sided focal seizure on day 6 prompting ED presentation. He had no neck stiffness on examination and no antecedent freshwater exposure. Examination on admission: Glasgow Coma Scale 11, focal neurological deficit (anomic aphasia and disinhibition). CSF showed opening pressure 24 cmH2O, white cell count 250 per cubic millimeter (72 percent lymphocytes), glucose 52 mg/dL, protein 135 mg/dL, RBC 40 with xanthochromia. CSF HSV-1 PCR positive. Brain MRI with DWI/FLAIR showed mesial temporal T2/FLAIR hyperintensity asymmetric with bilateral but left-dominant involvement and basal ganglia sparing. Acyclovir initiated within four hours. Anchored to Tyler 2018 NEJM viral encephalitis review (PMID 30089069). Outcome: survived with moderate memory deficit. Subphase 1.3 commit 5.3.5 wave 1, pre-adjudication hold_for_revision.

NARRATIVE_ES: Varon de 50 anos en Paises Bajos (Amsterdam), ingresado a urgencias terciarias con curso de seis dias: febricula 38.4 C, cefalea, luego cambio conductual progresivo con desinhibicion al tercer dia, afasia anomica al cuarto dia y crisis focal izquierda al sexto dia que motivo consulta. Sin rigidez de nuca al examen. Sin exposicion a agua dulce. Examen: escala de Glasgow 11, deficit focal (afasia anomica, desinhibicion). Liquido cefalorraquideo mostro presion de apertura 24 cmH2O, leucocitos 250 por mm3 (72 por ciento linfocitos), glucosa 52 mg/dL, proteina 135 mg/dL, eritrocitos 40 con xantocromia. PCR de HSV-1 positiva. RM cerebral mostro hiperintensidad temporal mesial T2/FLAIR bilateral con dominancia izquierda. Anclaje en revision Tyler 2018 NEJM (PMID 30089069). Subphase 1.3 commit 5.3.5 wave 1, pre-adjudicacion hold_for_revision.

RATIONALE: Anchored to PMID 30089069 (Tyler 2018 NEJM viral encephalitis review). HSV1 mesial-temporal-encephalitis phenotype with frontal-disinhibition + anomic aphasia (limbic + frontal extension). Demographic anchor (50yo M adult HSE) sits in adult-HSE stratum. CSF lymphocytic with hemorrhagic component. MRI mesial temporal pattern with bilateral but asymmetric involvement. Imputation tiers: tier_1_primary={age, sex, hsv1_pcr, imaging_pattern, focal_aphasia, behavioral_change}; tier_3_within_review={csf_wbc, neutrophil_pct, glucose, protein, rbc, xanthochromia, gcs}; tier_4_priors={temp, symptom_days}. Indeterminate=none. Diagnostic_ambiguity=false. Outcome=survived_moderate_memory_deficit. Acyclovir_hours=4. Tier: tier_3_imputation_within_review. 5.3.5 wave1 HSV1-NL-adult-male-bilateral.

ANCHORING_EXTRAS: stage=pre_adjudication; status=pending_external_review; self_review_disposition=hold_for_revision; self_review_notes=wave 5.3.5 VIRAL vignette anchored to PMID 30089069 (Tyler 2018 NEJM viral encephalitis review); external clinical adjudication pending; classification provisional. adjudicator_ids=VIRAL-WAVE1-PRE-ADJ-1, VIRAL-WAVE1-PRE-ADJ-2 (sentinel); cohen_kappa=0.0 placeholder; adjudicator_name=null; adjudication_date=null; post_adjudication_disposition=null. Subphase 1.3 commit 5.3.5 (2026-05-08). anchor=Tyler-NEJM-2018 stratum=HSV1-adult-bilateral.

ADJUDICATION:
  inclusion_decision: hold_for_revision  ground_truth_class: 3  kappa: 0.0
  adjudicator_ids: ['VIRAL-WAVE1-PRE-ADJ-1', 'VIRAL-WAVE1-PRE-ADJ-2']
  disagreement_resolution: None
```

#### Vignette: vid=106 file=vir_106_enterovirus_pediatric.json class=3 subphase=1.3 VIRAL

```
ANCHOR:
  pmid: 30089069
  first_author: Tyler
  year: 2018
  journal: NEJM
  citation_type: review
  doi: 10.1056/NEJMra1708714

DEMOGRAPHICS:
  age_years: 7  sex: female  region: us_south
  ethnicity: white_non_hispanic  altitude_m: 100
  hiv_status: negative  cd4: None
  pregnancy_red_flag: False
  immunocompromise_status: none
  freshwater_exposure_14d: False (None)

HISTORY:
  symptom_onset_to_presentation_days: 1.0
  chief_complaint: fever_with_headache
  red_flags_present: []
  prodrome_description: 7-year-old female, US South region. 24-hour course: fever 38.4 C, headache, neck stiffness, photophobia, nausea, summer late-July presentation. Pediatric tertiary ED. No freshwater. No focal deficit. Outcome: survived with full recovery in 5 days. Supportive care; no antibiotics after enterovirus PCR positive.

VITALS:
  T:38.4C HR:108 BP:100/64 GCS:15 SpO2:98% RR:22

EXAM:
  mental_status: alert  neck_stiff: True  kernig_brudz: True
  cranial_nerve_palsy: none  papilledema: False  focal_deficit: False
  skin_lesion_centrofacial_chronic: False  rash: False

LABS:
  WBC:10800 Plt:295000 ALT/AST:22 CRP:16.0 PCT:0.3 Na:138

CSF:
  OP:18.0cmH2O  WBC:95/mm3  lymph%:80 neut%:20 eos%:0
  glucose:60mg/dL protein:50mg/dL lactate:2.0mmol/L ADA:NoneU/L
  crag_lfa:negative  wet_mount:negative  xanthochromia:False  RBC:3

IMAGING:
  modality: none  pattern: (none)
  finding_count: None
  text_summary: No imaging performed (uncomplicated enteroviral meningitis presentation with normal mental status; Tyler 2018 NEJM review supports deferring imaging in benign aseptic pattern).

DIAGNOSTIC_TESTS:
  total_results: 3
  pcr_panel: positive
  xpert_mtb_rif: n/a
  blood_culture: n/a
  csf_culture: n/a
  serology_or_antigen: n/a
  smear_or_gram: n/a
  brain_biopsy: n/a

NARRATIVE_EN: A 7-year-old girl in the US South region presented to a tertiary pediatric emergency department in late July with a 24-hour course of fever to 38.4 C, headache, neck stiffness, photophobia, and nausea. Examination on admission: temperature 38.4 C, Glasgow Coma Scale 15, alert, neck stiffness, positive Kernig sign, no focal deficit, no rash. CSF showed opening pressure 18 cmH2O, white cell count 95 per cubic millimeter (80 percent lymphocytes), glucose 60 mg/dL, protein 50 mg/dL. CSF enterovirus PCR positive. Gram stain and culture negative. No imaging performed (uncomplicated viral meningitis presentation in a child with normal mental status). Anchored to Tyler 2018 NEJM viral encephalitis review (PMID 30089069), summer enteroviral peak stratum. Outcome: survived with full recovery in five days. Subphase 1.3 commit 5.3.5 wave 1, pre-adjudication hold_for_revision.

NARRATIVE_ES: Nina de 7 anos en region sur de Estados Unidos, ingresada a urgencias pediatricas terciarias en julio con 24 horas de fiebre 38.4 C, cefalea, rigidez de nuca, fotofobia y nauseas. Examen: temperatura 38.4 C, escala de Glasgow 15, alerta, rigidez de nuca, signo de Kernig positivo, sin deficit focal, sin exantema. Liquido cefalorraquideo mostro presion de apertura 18 cmH2O, leucocitos 95 por mm3 (80 por ciento linfocitos), glucosa 60 mg/dL, proteina 50 mg/dL. PCR de enterovirus en liquido cefalorraquideo positiva. Tincion de Gram y cultivo negativos. Sin imagenes (presentacion no complicada). Anclaje en revision Tyler 2018 NEJM (PMID 30089069), estrato pico estival enteroviral. Subphase 1.3 commit 5.3.5 wave 1, pre-adjudicacion hold_for_revision.

RATIONALE: Anchored to PMID 30089069 (Tyler 2018 NEJM viral encephalitis review). Enteroviral aseptic meningitis with classic summer pediatric presentation. Demographic anchor (7yo F US South summer) sits in pediatric-aseptic-meningitis-summer-peak stratum. CSF lymphocytic (95 WBC, 80 percent lymphocytes), normal glucose 60, modestly elevated protein 50 - textbook viral pattern per Tyler review. EV PCR positive. Imputation tiers: tier_1_primary={age, sex, ev_pcr, season}; tier_3_within_review={csf_wbc, neutrophil_pct, glucose, protein}; tier_4_priors={temp, gcs, symptom_days}. Indeterminate=none. Diagnostic_ambiguity=false. Outcome=survived_full_recovery. Tier: tier_3_imputation_within_review. 5.3.5 wave1 EV-US-pediatric-summer.

ANCHORING_EXTRAS: stage=pre_adjudication; status=pending_external_review; self_review_disposition=hold_for_revision; self_review_notes=wave 5.3.5 VIRAL vignette anchored to PMID 30089069 (Tyler 2018 NEJM viral encephalitis review); external clinical adjudication pending; classification provisional. adjudicator_ids=VIRAL-WAVE1-PRE-ADJ-1, VIRAL-WAVE1-PRE-ADJ-2 (sentinel); cohen_kappa=0.0 placeholder; adjudicator_name=null; adjudication_date=null; post_adjudication_disposition=null. Subphase 1.3 commit 5.3.5 (2026-05-08). anchor=Tyler-NEJM-2018 stratum=EV-pediatric-summer.

ADJUDICATION:
  inclusion_decision: hold_for_revision  ground_truth_class: 3  kappa: 0.0
  adjudicator_ids: ['VIRAL-WAVE1-PRE-ADJ-1', 'VIRAL-WAVE1-PRE-ADJ-2']
  disagreement_resolution: None
```

#### Vignette: vid=107 file=vir_107_enterovirus_young_adult.json class=3 subphase=1.3 VIRAL

```
ANCHOR:
  pmid: 30089069
  first_author: Tyler
  year: 2018
  journal: NEJM
  citation_type: review
  doi: 10.1056/NEJMra1708714

DEMOGRAPHICS:
  age_years: 22  sex: female  region: other_global
  ethnicity: white_non_hispanic  altitude_m: 5
  hiv_status: negative  cd4: None
  pregnancy_red_flag: False
  immunocompromise_status: none
  freshwater_exposure_14d: False (None)

HISTORY:
  symptom_onset_to_presentation_days: 2.0
  chief_complaint: fever_with_headache
  red_flags_present: []
  prodrome_description: 22-year-old female, Netherlands. 2-day course: fever 38.6 C, severe headache, neck stiffness, photophobia, myalgia, summer August presentation. University setting. Tertiary ED Amsterdam. No freshwater. No focal deficit. Outcome: survived with full recovery in 7 days. Supportive care; no antiviral or antibiotics after EV PCR positive.

VITALS:
  T:38.6C HR:102 BP:116/70 GCS:15 SpO2:98% RR:18

EXAM:
  mental_status: alert  neck_stiff: True  kernig_brudz: True
  cranial_nerve_palsy: none  papilledema: False  focal_deficit: False
  skin_lesion_centrofacial_chronic: False  rash: False

LABS:
  WBC:11500 Plt:275000 ALT/AST:24 CRP:18.0 PCT:0.3 Na:138

CSF:
  OP:19.0cmH2O  WBC:220/mm3  lymph%:78 neut%:22 eos%:0
  glucose:55mg/dL protein:65mg/dL lactate:2.2mmol/L ADA:NoneU/L
  crag_lfa:negative  wet_mount:negative  xanthochromia:False  RBC:3

IMAGING:
  modality: none  pattern: (none)
  finding_count: None
  text_summary: No imaging performed (uncomplicated enteroviral meningitis presentation with normal mental status; Tyler 2018 NEJM review supports deferring imaging in benign aseptic pattern).

DIAGNOSTIC_TESTS:
  total_results: 3
  pcr_panel: positive
  xpert_mtb_rif: n/a
  blood_culture: n/a
  csf_culture: n/a
  serology_or_antigen: n/a
  smear_or_gram: n/a
  brain_biopsy: n/a

NARRATIVE_EN: A 22-year-old woman in the Netherlands presented to a tertiary emergency department in Amsterdam in late August with a 2-day course of fever to 38.6 C, severe headache, neck stiffness, photophobia, and myalgia. She lived in a university setting. Examination on admission: temperature 38.6 C, Glasgow Coma Scale 15, alert, neck stiffness, positive Kernig sign, no focal deficit, no rash. CSF showed opening pressure 19 cmH2O, white cell count 220 per cubic millimeter (78 percent lymphocytes), glucose 55 mg/dL, protein 65 mg/dL. CSF enterovirus PCR positive. Gram stain and culture negative. No imaging performed (uncomplicated presentation). Anchored to Tyler 2018 NEJM viral encephalitis review (PMID 30089069), young-adult enteroviral summer-peak stratum. Outcome: survived with full recovery in seven days. Subphase 1.3 commit 5.3.5 wave 1, pre-adjudication hold_for_revision.

NARRATIVE_ES: Mujer de 22 anos en Paises Bajos (Amsterdam), ingresada a urgencias terciarias en agosto con dos dias de fiebre 38.6 C, cefalea intensa, rigidez de nuca, fotofobia y mialgia. Entorno universitario. Examen: temperatura 38.6 C, escala de Glasgow 15, alerta, rigidez de nuca, signo de Kernig positivo, sin deficit focal, sin exantema. Liquido cefalorraquideo mostro presion de apertura 19 cmH2O, leucocitos 220 por mm3 (78 por ciento linfocitos), glucosa 55 mg/dL, proteina 65 mg/dL. PCR de enterovirus en LCR positiva. Tincion de Gram y cultivo negativos. Sin imagenes. Anclaje en revision Tyler 2018 NEJM (PMID 30089069), estrato adulto joven pico estival enteroviral. Subphase 1.3 commit 5.3.5 wave 1, pre-adjudicacion hold_for_revision.

RATIONALE: Anchored to PMID 30089069 (Tyler 2018 NEJM viral encephalitis review). Enteroviral aseptic meningitis young-adult pattern. Demographic anchor (22yo F NL university summer) sits in young-adult-aseptic-meningitis-summer stratum. CSF lymphocytic (220 WBC, 78 percent lymphocytes), normal glucose 55, mildly elevated protein 65 - textbook viral pattern. EV PCR positive. Imputation tiers: tier_1_primary={age, sex, ev_pcr, season}; tier_3_within_review={csf_wbc, neutrophil_pct, glucose, protein}; tier_4_priors={temp, gcs, symptom_days}. Indeterminate=none. Diagnostic_ambiguity=false. Outcome=survived_full_recovery. Tier: tier_3_imputation_within_review. 5.3.5 wave1 EV-NL-young-adult.

ANCHORING_EXTRAS: stage=pre_adjudication; status=pending_external_review; self_review_disposition=hold_for_revision; self_review_notes=wave 5.3.5 VIRAL vignette anchored to PMID 30089069 (Tyler 2018 NEJM viral encephalitis review); external clinical adjudication pending; classification provisional. adjudicator_ids=VIRAL-WAVE1-PRE-ADJ-1, VIRAL-WAVE1-PRE-ADJ-2 (sentinel); cohen_kappa=0.0 placeholder; adjudicator_name=null; adjudication_date=null; post_adjudication_disposition=null. Subphase 1.3 commit 5.3.5 (2026-05-08). anchor=Tyler-NEJM-2018 stratum=EV-young-adult-summer.

ADJUDICATION:
  inclusion_decision: hold_for_revision  ground_truth_class: 3  kappa: 0.0
  adjudicator_ids: ['VIRAL-WAVE1-PRE-ADJ-1', 'VIRAL-WAVE1-PRE-ADJ-2']
  disagreement_resolution: None
```

#### Vignette: vid=108 file=vir_108_enterovirus_school_outbreak.json class=3 subphase=1.3 VIRAL

```
ANCHOR:
  pmid: 30089069
  first_author: Tyler
  year: 2018
  journal: NEJM
  citation_type: review
  doi: 10.1056/NEJMra1708714

DEMOGRAPHICS:
  age_years: 11  sex: male  region: us_south
  ethnicity: white_non_hispanic  altitude_m: 100
  hiv_status: negative  cd4: None
  pregnancy_red_flag: False
  immunocompromise_status: none
  freshwater_exposure_14d: False (None)

HISTORY:
  symptom_onset_to_presentation_days: 2.0
  chief_complaint: fever_with_headache
  red_flags_present: []
  prodrome_description: 11-year-old male, US South region. School outbreak with multiple peers symptomatic. 2-day course: fever 38.7 C, headache, neck stiffness, photophobia, vomiting, summer early-September presentation. Pediatric tertiary ED. No freshwater. No focal. Outcome: survived with full recovery in 6 days.

VITALS:
  T:38.7C HR:100 BP:110/68 GCS:15 SpO2:98% RR:20

EXAM:
  mental_status: alert  neck_stiff: True  kernig_brudz: True
  cranial_nerve_palsy: none  papilledema: False  focal_deficit: False
  skin_lesion_centrofacial_chronic: False  rash: False

LABS:
  WBC:10200 Plt:285000 ALT/AST:23 CRP:14.0 PCT:0.3 Na:138

CSF:
  OP:18.0cmH2O  WBC:180/mm3  lymph%:82 neut%:18 eos%:0
  glucose:58mg/dL protein:60mg/dL lactate:2.0mmol/L ADA:NoneU/L
  crag_lfa:negative  wet_mount:negative  xanthochromia:False  RBC:2

IMAGING:
  modality: none  pattern: (none)
  finding_count: None
  text_summary: No imaging performed (uncomplicated enteroviral meningitis presentation with normal mental status; Tyler 2018 NEJM review supports deferring imaging in benign aseptic pattern).

DIAGNOSTIC_TESTS:
  total_results: 3
  pcr_panel: positive
  xpert_mtb_rif: n/a
  blood_culture: n/a
  csf_culture: n/a
  serology_or_antigen: n/a
  smear_or_gram: n/a
  brain_biopsy: n/a

NARRATIVE_EN: An 11-year-old boy in the US South region presented to a tertiary pediatric emergency department in early September with a 2-day course of fever to 38.7 C, headache, neck stiffness, photophobia, and vomiting. He attended a school with several peers reporting similar symptoms in the same week (suspected school enteroviral outbreak). Examination on admission: temperature 38.7 C, Glasgow Coma Scale 15, alert, neck stiffness, positive Kernig sign, no focal deficit, no rash. CSF showed opening pressure 18 cmH2O, white cell count 180 per cubic millimeter (82 percent lymphocytes), glucose 58 mg/dL, protein 60 mg/dL. CSF enterovirus PCR positive. Gram stain and culture negative. No imaging performed. Anchored to Tyler 2018 NEJM viral encephalitis review (PMID 30089069), school-outbreak enteroviral stratum. Outcome: survived with full recovery in six days. Subphase 1.3 commit 5.3.5 wave 1, pre-adjudication hold_for_revision.

NARRATIVE_ES: Varon de 11 anos en region sur de Estados Unidos, ingresado a urgencias pediatricas terciarias a principios de septiembre con dos dias de fiebre 38.7 C, cefalea, rigidez de nuca, fotofobia y vomitos. Asistio a colegio con varios companeros con sintomas similares la misma semana (brote escolar de enterovirus sospechado). Examen: temperatura 38.7 C, escala de Glasgow 15, alerta, rigidez de nuca, signo de Kernig positivo, sin deficit focal, sin exantema. Liquido cefalorraquideo mostro presion de apertura 18 cmH2O, leucocitos 180 por mm3 (82 por ciento linfocitos), glucosa 58 mg/dL, proteina 60 mg/dL. PCR de enterovirus en LCR positiva. Anclaje en revision Tyler 2018 NEJM (PMID 30089069), estrato brote escolar. Subphase 1.3 commit 5.3.5 wave 1.

RATIONALE: Anchored to PMID 30089069 (Tyler 2018 NEJM viral encephalitis review). Enteroviral aseptic meningitis with school-outbreak epidemiology. Demographic anchor (11yo M US school outbreak September) sits in school-outbreak-pediatric stratum. CSF lymphocytic (180 WBC, 82 percent lymphocytes), normal glucose 58, mildly elevated protein 60 - textbook viral pattern. EV PCR positive. Imputation tiers: tier_1_primary={age, sex, ev_pcr, school_outbreak_context, season}; tier_3_within_review={csf_wbc, neutrophil_pct, glucose, protein}; tier_4_priors={temp, gcs, symptom_days}. Indeterminate=none. Diagnostic_ambiguity=false. Outcome=survived_full_recovery. Tier: tier_3_imputation_within_review. 5.3.5 wave1 EV-school-outbreak-pediatric.

ANCHORING_EXTRAS: stage=pre_adjudication; status=pending_external_review; self_review_disposition=hold_for_revision; self_review_notes=wave 5.3.5 VIRAL vignette anchored to PMID 30089069 (Tyler 2018 NEJM viral encephalitis review); external clinical adjudication pending; classification provisional. adjudicator_ids=VIRAL-WAVE1-PRE-ADJ-1, VIRAL-WAVE1-PRE-ADJ-2 (sentinel); cohen_kappa=0.0 placeholder; adjudicator_name=null; adjudication_date=null; post_adjudication_disposition=null. Subphase 1.3 commit 5.3.5 (2026-05-08). anchor=Tyler-NEJM-2018 stratum=EV-school-outbreak.

ADJUDICATION:
  inclusion_decision: hold_for_revision  ground_truth_class: 3  kappa: 0.0
  adjudicator_ids: ['VIRAL-WAVE1-PRE-ADJ-1', 'VIRAL-WAVE1-PRE-ADJ-2']
  disagreement_resolution: None
```

#### Vignette: vid=109 file=vir_109_enterovirus_infant.json class=3 subphase=1.3 VIRAL

```
ANCHOR:
  pmid: 30089069
  first_author: Tyler
  year: 2018
  journal: NEJM
  citation_type: review
  doi: 10.1056/NEJMra1708714

DEMOGRAPHICS:
  age_years: 3  sex: female  region: other_global
  ethnicity: white_non_hispanic  altitude_m: 5
  hiv_status: negative  cd4: None
  pregnancy_red_flag: False
  immunocompromise_status: none
  freshwater_exposure_14d: False (None)

HISTORY:
  symptom_onset_to_presentation_days: 2.0
  chief_complaint: fever_with_headache
  red_flags_present: []
  prodrome_description: 3-year-old female, Netherlands. 2-day course: fever 38.5 C, irritability, decreased oral intake, vomiting, bulging fontanelle remnant, neck stiffness on exam, summer July presentation. Pediatric tertiary ED Amsterdam. No freshwater. No focal deficit. Outcome: survived with full recovery in 5 days.

VITALS:
  T:38.5C HR:130 BP:96/60 GCS:15 SpO2:98% RR:26

EXAM:
  mental_status: alert  neck_stiff: True  kernig_brudz: True
  cranial_nerve_palsy: none  papilledema: False  focal_deficit: False
  skin_lesion_centrofacial_chronic: False  rash: False

LABS:
  WBC:9800 Plt:305000 ALT/AST:22 CRP:12.0 PCT:0.3 Na:138

CSF:
  OP:17.0cmH2O  WBC:145/mm3  lymph%:85 neut%:15 eos%:0
  glucose:56mg/dL protein:55mg/dL lactate:2.0mmol/L ADA:NoneU/L
  crag_lfa:negative  wet_mount:negative  xanthochromia:False  RBC:2

IMAGING:
  modality: none  pattern: (none)
  finding_count: None
  text_summary: No imaging performed (uncomplicated enteroviral meningitis presentation with normal mental status; Tyler 2018 NEJM review supports deferring imaging in benign aseptic pattern).

DIAGNOSTIC_TESTS:
  total_results: 3
  pcr_panel: positive
  xpert_mtb_rif: n/a
  blood_culture: n/a
  csf_culture: n/a
  serology_or_antigen: n/a
  smear_or_gram: n/a
  brain_biopsy: n/a

NARRATIVE_EN: A 3-year-old girl in the Netherlands presented to a tertiary pediatric emergency department in Amsterdam in July with a 2-day course of fever to 38.5 C, irritability, decreased oral intake, vomiting, and neck stiffness on examination. Examination on admission: temperature 38.5 C, Glasgow Coma Scale 15, alert, neck stiffness, positive Kernig sign, no focal deficit, no rash. CSF showed opening pressure 17 cmH2O, white cell count 145 per cubic millimeter (85 percent lymphocytes), glucose 56 mg/dL, protein 55 mg/dL. CSF enterovirus PCR positive. Gram stain and culture negative. No imaging performed. Anchored to Tyler 2018 NEJM viral encephalitis review (PMID 30089069), early-childhood enteroviral summer stratum. Outcome: survived with full recovery in five days. Subphase 1.3 commit 5.3.5 wave 1, pre-adjudication hold_for_revision.

NARRATIVE_ES: Nina de 3 anos en Paises Bajos (Amsterdam), ingresada a urgencias pediatricas terciarias en julio con dos dias de fiebre 38.5 C, irritabilidad, disminucion de ingesta oral, vomitos y rigidez de nuca al examen. Examen: temperatura 38.5 C, escala de Glasgow 15, alerta, rigidez de nuca, signo de Kernig positivo, sin deficit focal, sin exantema. Liquido cefalorraquideo mostro presion de apertura 17 cmH2O, leucocitos 145 por mm3 (85 por ciento linfocitos), glucosa 56 mg/dL, proteina 55 mg/dL. PCR de enterovirus en LCR positiva. Tincion de Gram y cultivo negativos. Sin imagenes. Anclaje en revision Tyler 2018 NEJM (PMID 30089069), estrato infancia temprana pico estival enteroviral. Subphase 1.3 commit 5.3.5 wave 1, pre-adjudicacion hold_for_revision.

RATIONALE: Anchored to PMID 30089069 (Tyler 2018 NEJM viral encephalitis review). Enteroviral aseptic meningitis early-childhood summer pattern. Demographic anchor (3yo F NL summer) sits in early-childhood-EV-summer stratum. CSF lymphocytic (145 WBC, 85 percent lymphocytes), normal glucose 56, mildly elevated protein 55. EV PCR positive. Imputation tiers: tier_1_primary={age, sex, ev_pcr, season, irritability}; tier_3_within_review={csf_wbc, neutrophil_pct, glucose, protein}; tier_4_priors={temp, gcs, hr, symptom_days}. Indeterminate=none. Diagnostic_ambiguity=false. Outcome=survived_full_recovery. Tier: tier_3_imputation_within_review. 5.3.5 wave1 EV-NL-infant-summer.

ANCHORING_EXTRAS: stage=pre_adjudication; status=pending_external_review; self_review_disposition=hold_for_revision; self_review_notes=wave 5.3.5 VIRAL vignette anchored to PMID 30089069 (Tyler 2018 NEJM viral encephalitis review); external clinical adjudication pending; classification provisional. adjudicator_ids=VIRAL-WAVE1-PRE-ADJ-1, VIRAL-WAVE1-PRE-ADJ-2 (sentinel); cohen_kappa=0.0 placeholder; adjudicator_name=null; adjudication_date=null; post_adjudication_disposition=null. Subphase 1.3 commit 5.3.5 (2026-05-08). anchor=Tyler-NEJM-2018 stratum=EV-early-childhood-summer.

ADJUDICATION:
  inclusion_decision: hold_for_revision  ground_truth_class: 3  kappa: 0.0
  adjudicator_ids: ['VIRAL-WAVE1-PRE-ADJ-1', 'VIRAL-WAVE1-PRE-ADJ-2']
  disagreement_resolution: None
```

#### Vignette: vid=111 file=vir_111_enterovirus_pediatric.json class=3 subphase=1.3 VIRAL

```
ANCHOR:
  pmid: 30089069
  first_author: Tyler
  year: 2018
  journal: NEJM
  citation_type: review
  doi: 10.1056/NEJMra1708714

DEMOGRAPHICS:
  age_years: 5  sex: male  region: us_south
  ethnicity: white_non_hispanic  altitude_m: 100
  hiv_status: negative  cd4: None
  pregnancy_red_flag: False
  immunocompromise_status: none
  freshwater_exposure_14d: False (None)

HISTORY:
  symptom_onset_to_presentation_days: 2.0
  chief_complaint: fever_with_headache
  red_flags_present: []
  prodrome_description: 5-year-old male, US South region. 2-day course: fever 38.6 C, headache, neck stiffness, photophobia, summer August presentation. Pediatric tertiary ED. No freshwater. No focal. Outcome: survived with full recovery in 6 days. Supportive care; antibiotics discontinued after EV PCR positive.

VITALS:
  T:38.6C HR:110 BP:100/64 GCS:15 SpO2:98% RR:22

EXAM:
  mental_status: alert  neck_stiff: True  kernig_brudz: True
  cranial_nerve_palsy: none  papilledema: False  focal_deficit: False
  skin_lesion_centrofacial_chronic: False  rash: False

LABS:
  WBC:10500 Plt:290000 ALT/AST:22 CRP:15.0 PCT:0.3 Na:138

CSF:
  OP:18.0cmH2O  WBC:165/mm3  lymph%:80 neut%:20 eos%:0
  glucose:55mg/dL protein:58mg/dL lactate:2.1mmol/L ADA:NoneU/L
  crag_lfa:negative  wet_mount:negative  xanthochromia:False  RBC:3

IMAGING:
  modality: none  pattern: (none)
  finding_count: None
  text_summary: No imaging performed (uncomplicated enteroviral meningitis presentation with normal mental status; Tyler 2018 NEJM review supports deferring imaging in benign aseptic pattern).

DIAGNOSTIC_TESTS:
  total_results: 3
  pcr_panel: positive
  xpert_mtb_rif: n/a
  blood_culture: n/a
  csf_culture: n/a
  serology_or_antigen: n/a
  smear_or_gram: n/a
  brain_biopsy: n/a

NARRATIVE_EN: A 5-year-old boy in the US South region presented to a tertiary pediatric emergency department in August with a 2-day course of fever to 38.6 C, headache, neck stiffness, and photophobia. Examination on admission: temperature 38.6 C, Glasgow Coma Scale 15, alert, neck stiffness, positive Kernig sign, no focal deficit, no rash. CSF showed opening pressure 18 cmH2O, white cell count 165 per cubic millimeter (80 percent lymphocytes), glucose 55 mg/dL, protein 58 mg/dL. CSF enterovirus PCR positive. Gram stain and culture negative. No imaging performed (uncomplicated viral meningitis presentation in a child with normal mental status). Anchored to Tyler 2018 NEJM viral encephalitis review (PMID 30089069), pediatric enteroviral summer-peak stratum. Outcome: survived with full recovery in six days. Subphase 1.3 commit 5.3.5 wave 1, pre-adjudication hold_for_revision.

NARRATIVE_ES: Varon de 5 anos en region sur de Estados Unidos, ingresado a urgencias pediatricas terciarias en agosto con dos dias de fiebre 38.6 C, cefalea, rigidez de nuca y fotofobia. Examen: temperatura 38.6 C, escala de Glasgow 15, alerta, rigidez de nuca, signo de Kernig positivo, sin deficit focal, sin exantema. Liquido cefalorraquideo mostro presion de apertura 18 cmH2O, leucocitos 165 por mm3 (80 por ciento linfocitos), glucosa 55 mg/dL, proteina 58 mg/dL. PCR de enterovirus en LCR positiva. Tincion de Gram y cultivo negativos. Sin imagenes. Anclaje en revision Tyler 2018 NEJM (PMID 30089069), estrato pediatrico pico estival enteroviral. Subphase 1.3 commit 5.3.5 wave 1, pre-adjudicacion hold_for_revision.

RATIONALE: Anchored to PMID 30089069 (Tyler 2018 NEJM viral encephalitis review). Enteroviral aseptic meningitis pediatric summer pattern. Demographic anchor (5yo M US South August) sits in pediatric-EV-summer stratum. CSF lymphocytic (165 WBC, 80 percent lymphocytes), normal glucose 55, mildly elevated protein 58. EV PCR positive. Imputation tiers: tier_1_primary={age, sex, ev_pcr, season}; tier_3_within_review={csf_wbc, neutrophil_pct, glucose, protein}; tier_4_priors={temp, gcs, symptom_days}. Indeterminate=none. Diagnostic_ambiguity=false. Outcome=survived_full_recovery. Tier: tier_3_imputation_within_review. 5.3.5 wave1 EV-US-pediatric-summer-2.

ANCHORING_EXTRAS: stage=pre_adjudication; status=pending_external_review; self_review_disposition=hold_for_revision; self_review_notes=wave 5.3.5 VIRAL vignette anchored to PMID 30089069 (Tyler 2018 NEJM viral encephalitis review); external clinical adjudication pending; classification provisional. adjudicator_ids=VIRAL-WAVE1-PRE-ADJ-1, VIRAL-WAVE1-PRE-ADJ-2 (sentinel); cohen_kappa=0.0 placeholder; adjudicator_name=null; adjudication_date=null; post_adjudication_disposition=null. Subphase 1.3 commit 5.3.5 (2026-05-08). anchor=Tyler-NEJM-2018 stratum=EV-pediatric-summer-2.

ADJUDICATION:
  inclusion_decision: hold_for_revision  ground_truth_class: 3  kappa: 0.0
  adjudicator_ids: ['VIRAL-WAVE1-PRE-ADJ-1', 'VIRAL-WAVE1-PRE-ADJ-2']
  disagreement_resolution: None
```

#### Vignette: vid=113 file=vir_113_hsv2_mollaret_recurrent_ambiguity.json class=3 subphase=1.3 VIRAL

```
ANCHOR:
  pmid: 30089069
  first_author: Tyler
  year: 2018
  journal: NEJM
  citation_type: review
  doi: 10.1056/NEJMra1708714

DEMOGRAPHICS:
  age_years: 28  sex: female  region: other_global
  ethnicity: white_non_hispanic  altitude_m: 5
  hiv_status: negative  cd4: None
  pregnancy_red_flag: False
  immunocompromise_status: none
  freshwater_exposure_14d: False (None)

HISTORY:
  symptom_onset_to_presentation_days: 2.0
  chief_complaint: fever_with_headache
  red_flags_present: []
  prodrome_description: 28-year-old female, Netherlands. First-episode HSV2 lymphocytic meningitis with prominent meningismus 2 weeks after primary genital herpes outbreak. 2-day course: fever 38.6 C, severe headache, prominent neck stiffness, photophobia. Tertiary ED Amsterdam. No freshwater. Diagnostic_ambiguity=true; type=hsv2_first_episode_with_prominent_meningismus_bacterial_ddx. Outcome: survived with full recovery.

VITALS:
  T:38.6C HR:102 BP:116/70 GCS:14 SpO2:97% RR:18

EXAM:
  mental_status: alert  neck_stiff: True  kernig_brudz: True
  cranial_nerve_palsy: none  papilledema: False  focal_deficit: False
  skin_lesion_centrofacial_chronic: False  rash: False

LABS:
  WBC:12500 Plt:245000 ALT/AST:24 CRP:32.0 PCT:0.5 Na:138

CSF:
  OP:24.0cmH2O  WBC:350/mm3  lymph%:65 neut%:35 eos%:0
  glucose:48mg/dL protein:105mg/dL lactate:2.8mmol/L ADA:NoneU/L
  crag_lfa:negative  wet_mount:negative  xanthochromia:False  RBC:4

IMAGING:
  modality: mri_with_dwi_flair  pattern: normal
  finding_count: 0
  text_summary: MRI brain with DWI/FLAIR: normal. No focal lesion. Mollaret and HSV2 first-episode lymphocytic meningitis typically demonstrate normal imaging per Tyler review.

DIAGNOSTIC_TESTS:
  total_results: 3
  pcr_panel: positive
  xpert_mtb_rif: n/a
  blood_culture: n/a
  csf_culture: n/a
  serology_or_antigen: n/a
  smear_or_gram: n/a
  brain_biopsy: n/a

NARRATIVE_EN: A 28-year-old woman in the Netherlands presented to a tertiary emergency department in Amsterdam with a 2-day course of fever to 38.6 C, severe headache, prominent neck stiffness, and photophobia, two weeks after a primary genital herpes outbreak. Examination on admission: temperature 38.6 C, Glasgow Coma Scale 14, alert, prominent neck stiffness, positive Kernig sign, no focal deficit, no rash. CSF showed opening pressure 24 cmH2O, white cell count 350 per cubic millimeter (65 percent lymphocytes, 35 percent neutrophils), glucose 48 mg/dL, protein 105 mg/dL. CSF HSV-2 PCR positive. Gram stain and culture negative. MRI brain with DWI/FLAIR normal. Diagnostic_ambiguity=true; type=hsv2_first_episode_with_prominent_meningismus_bacterial_ddx. The prominent meningismus and CSF pleocytosis at 350 WBC with 35 percent neutrophils raised initial bacterial-meningitis differential; HSV2 PCR confirmed organism. Anchored to Tyler 2018 NEJM viral encephalitis review (PMID 30089069). Outcome: survived with full recovery. Subphase 1.3 commit 5.3.5 wave 1, pre-adjudication hold_for_revision.

NARRATIVE_ES: Mujer de 28 anos en Paises Bajos (Amsterdam), ingresada a urgencias terciarias con dos dias de fiebre 38.6 C, cefalea intensa, rigidez de nuca prominente y fotofobia, dos semanas tras brote primario de herpes genital. Examen: temperatura 38.6 C, escala de Glasgow 14, alerta, rigidez de nuca prominente, signo de Kernig positivo, sin deficit focal, sin exantema. Liquido cefalorraquideo mostro presion de apertura 24 cmH2O, leucocitos 350 por mm3 (65 por ciento linfocitos, 35 por ciento neutrofilos), glucosa 48 mg/dL, proteina 105 mg/dL. PCR de HSV-2 en LCR positiva. RM cerebral normal. Ambiguedad diagnostica por meningismo prominente con DDx bacteriana inicial. Anclaje en revision Tyler 2018 NEJM (PMID 30089069). Subphase 1.3 commit 5.3.5 wave 1, pre-adjudicacion hold_for_revision.

RATIONALE: Anchored to PMID 30089069 (Tyler 2018 NEJM viral encephalitis review). HSV2 first-episode lymphocytic meningitis with prominent meningismus that mimics bacterial DDx. Diagnostic_ambiguity=true; type=hsv2_first_episode_with_prominent_meningismus_bacterial_ddx (verbatim from spec). Demographic anchor (28yo F NL post-genital-herpes) sits in HSV2-first-episode stratum. CSF prominent (WBC 350) with 35 percent neutrophils approaching bacterial threshold but lymphocyte-dominant; protein elevated 105; glucose mildly low 48 - borderline-bacterial-DDx pattern raising initial empiric-ceftriaxone consideration. HSV2 PCR confirms organism. Imputation tiers: tier_1_primary={age, sex, hsv2_pcr, primary_genital_herpes_history, prominent_meningismus}; tier_3_within_review={csf_wbc, neutrophil_pct, glucose, protein}; tier_4_priors={temp, gcs, symptom_days}. Indeterminate=initial-bacterial-DDx-resolved-by-PCR. Outcome=survived_full_recovery. Tier: tier_3_imputation_within_review. 5.3.5 wave1 HSV2-firs...

ANCHORING_EXTRAS: stage=pre_adjudication; status=pending_external_review; self_review_disposition=hold_for_revision; self_review_notes=wave 5.3.5 VIRAL vignette anchored to PMID 30089069 (Tyler 2018 NEJM viral encephalitis review); external clinical adjudication pending; classification provisional. adjudicator_ids=VIRAL-WAVE1-PRE-ADJ-1, VIRAL-WAVE1-PRE-ADJ-2 (sentinel); cohen_kappa=0.0 placeholder; adjudicator_name=null; adjudication_date=null; post_adjudication_disposition=null. Subphase 1.3 commit 5.3.5 (2026-05-08). anchor=Tyler-NEJM-2018 type=hsv2_first_episode_with_prominent_meningismus_bacterial_ddx.

ADJUDICATION:
  inclusion_decision: hold_for_revision  ground_truth_class: 3  kappa: 0.0
  adjudicator_ids: ['VIRAL-WAVE1-PRE-ADJ-1', 'VIRAL-WAVE1-PRE-ADJ-2']
  disagreement_resolution: None
```

#### Vignette: vid=114 file=vir_114_hsv2_first_episode.json class=3 subphase=1.3 VIRAL

```
ANCHOR:
  pmid: 30089069
  first_author: Tyler
  year: 2018
  journal: NEJM
  citation_type: review
  doi: 10.1056/NEJMra1708714

DEMOGRAPHICS:
  age_years: 35  sex: male  region: us_south
  ethnicity: white_non_hispanic  altitude_m: 100
  hiv_status: negative  cd4: None
  pregnancy_red_flag: False
  immunocompromise_status: none
  freshwater_exposure_14d: False (None)

HISTORY:
  symptom_onset_to_presentation_days: 2.0
  chief_complaint: fever_with_headache
  red_flags_present: []
  prodrome_description: 35-year-old male, US South region. 2-day course: fever 38.4 C, severe headache, neck stiffness, photophobia, 10 days after primary genital herpes outbreak. Tertiary ED. No freshwater. No focal deficit. Outcome: survived with full recovery in 6 days. Acyclovir IV initiated empirically.

VITALS:
  T:38.4C HR:92 BP:124/76 GCS:15 SpO2:98% RR:18

EXAM:
  mental_status: alert  neck_stiff: True  kernig_brudz: True
  cranial_nerve_palsy: none  papilledema: False  focal_deficit: False
  skin_lesion_centrofacial_chronic: False  rash: False

LABS:
  WBC:10800 Plt:250000 ALT/AST:24 CRP:22.0 PCT:0.4 Na:138

CSF:
  OP:22.0cmH2O  WBC:280/mm3  lymph%:78 neut%:22 eos%:0
  glucose:55mg/dL protein:80mg/dL lactate:2.4mmol/L ADA:NoneU/L
  crag_lfa:negative  wet_mount:negative  xanthochromia:False  RBC:3

IMAGING:
  modality: mri_with_dwi_flair  pattern: normal
  finding_count: 0
  text_summary: MRI brain with DWI/FLAIR: normal. No focal lesion. Mollaret and HSV2 first-episode lymphocytic meningitis typically demonstrate normal imaging per Tyler review.

DIAGNOSTIC_TESTS:
  total_results: 3
  pcr_panel: positive
  xpert_mtb_rif: n/a
  blood_culture: n/a
  csf_culture: n/a
  serology_or_antigen: n/a
  smear_or_gram: n/a
  brain_biopsy: n/a

NARRATIVE_EN: A 35-year-old man in the US South region presented to a tertiary emergency department with a 2-day course of fever to 38.4 C, severe headache, neck stiffness, and photophobia, ten days after a primary genital herpes outbreak. Examination on admission: temperature 38.4 C, Glasgow Coma Scale 15, alert, neck stiffness, positive Kernig sign, no focal deficit, no rash. CSF showed opening pressure 22 cmH2O, white cell count 280 per cubic millimeter (78 percent lymphocytes), glucose 55 mg/dL, protein 80 mg/dL. CSF HSV-2 PCR positive. Gram stain and culture negative. MRI brain with DWI/FLAIR normal. Empiric IV acyclovir initiated. Anchored to Tyler 2018 NEJM viral encephalitis review (PMID 30089069), HSV2 first-episode lymphocytic meningitis stratum. Outcome: survived with full recovery in six days. Subphase 1.3 commit 5.3.5 wave 1, pre-adjudication hold_for_revision.

NARRATIVE_ES: Varon de 35 anos en region sur de Estados Unidos, ingresado a urgencias terciarias con dos dias de fiebre 38.4 C, cefalea intensa, rigidez de nuca y fotofobia, diez dias tras brote primario de herpes genital. Examen: temperatura 38.4 C, escala de Glasgow 15, alerta, rigidez de nuca, signo de Kernig positivo, sin deficit focal, sin exantema. Liquido cefalorraquideo mostro presion de apertura 22 cmH2O, leucocitos 280 por mm3 (78 por ciento linfocitos), glucosa 55 mg/dL, proteina 80 mg/dL. PCR de HSV-2 en LCR positiva. Tincion de Gram y cultivo negativos. RM cerebral normal. Aciclovir IV empirico iniciado. Anclaje en revision Tyler 2018 NEJM (PMID 30089069), estrato HSV2 primer episodio. Subphase 1.3 commit 5.3.5 wave 1, pre-adjudicacion hold_for_revision.

RATIONALE: Anchored to PMID 30089069 (Tyler 2018 NEJM viral encephalitis review). HSV2 first-episode lymphocytic meningitis. Demographic anchor (35yo M US post-genital-herpes) sits in HSV2-first-episode-male stratum. CSF lymphocytic (280 WBC, 78 percent lymphocytes), normal glucose 55, mildly elevated protein 80. HSV2 PCR positive. Imputation tiers: tier_1_primary={age, sex, hsv2_pcr, primary_genital_herpes_history}; tier_3_within_review={csf_wbc, neutrophil_pct, glucose, protein}; tier_4_priors={temp, gcs, symptom_days}. Indeterminate=none. Diagnostic_ambiguity=false. Outcome=survived_full_recovery. Tier: tier_3_imputation_within_review. 5.3.5 wave1 HSV2-first-episode-male.

ANCHORING_EXTRAS: stage=pre_adjudication; status=pending_external_review; self_review_disposition=hold_for_revision; self_review_notes=wave 5.3.5 VIRAL vignette anchored to PMID 30089069 (Tyler 2018 NEJM viral encephalitis review); external clinical adjudication pending; classification provisional. adjudicator_ids=VIRAL-WAVE1-PRE-ADJ-1, VIRAL-WAVE1-PRE-ADJ-2 (sentinel); cohen_kappa=0.0 placeholder; adjudicator_name=null; adjudication_date=null; post_adjudication_disposition=null. Subphase 1.3 commit 5.3.5 (2026-05-08). anchor=Tyler-NEJM-2018 stratum=HSV2-first-episode-male.

ADJUDICATION:
  inclusion_decision: hold_for_revision  ground_truth_class: 3  kappa: 0.0
  adjudicator_ids: ['VIRAL-WAVE1-PRE-ADJ-1', 'VIRAL-WAVE1-PRE-ADJ-2']
  disagreement_resolution: None
```

#### Vignette: vid=117 file=vir_117_dengue_lima_ambiguity.json class=3 subphase=1.3 VIRAL

```
ANCHOR:
  pmid: 30089069
  first_author: Tyler
  year: 2018
  journal: NEJM
  citation_type: review
  doi: 10.1056/NEJMra1708714

DEMOGRAPHICS:
  age_years: 32  sex: female  region: peru_lima_coast
  ethnicity: mestizo  altitude_m: 154
  hiv_status: negative  cd4: None
  pregnancy_red_flag: False
  immunocompromise_status: none
  freshwater_exposure_14d: False (None)

HISTORY:
  symptom_onset_to_presentation_days: 4.0
  chief_complaint: fever_with_headache
  red_flags_present: []
  prodrome_description: 32-year-old female in Lima, Peru. 4-day febrile illness during Peru 2024 dengue outbreak: fever 39.4 C, retro-orbital pain, severe myalgia, severe headache, encephalopathic mental status by day 3 with prominent CNS features raising arboviral DDx. No neck stiffness. Tertiary urban ED. Diagnostic_ambiguity=true; type=dengue_with_prominent_cns_arbo_encephalitis_overlap. Outcome: survived with full recovery.

VITALS:
  T:39.4C HR:112 BP:112/72 GCS:12 SpO2:96% RR:22

EXAM:
  mental_status: confused  neck_stiff: False  kernig_brudz: False
  cranial_nerve_palsy: none  papilledema: False  focal_deficit: False
  skin_lesion_centrofacial_chronic: False  rash: False

LABS:
  WBC:4500 Plt:75000 ALT/AST:138 CRP:28.0 PCT:0.5 Na:134

CSF:
  OP:19.0cmH2O  WBC:110/mm3  lymph%:70 neut%:30 eos%:0
  glucose:58mg/dL protein:80mg/dL lactate:2.4mmol/L ADA:NoneU/L
  crag_lfa:negative  wet_mount:negative  xanthochromia:False  RBC:4

IMAGING:
  modality: mri_with_dwi_flair  pattern: normal
  finding_count: 0
  text_summary: MRI brain with DWI/FLAIR: normal. No focal lesion, no edema. Dengue encephalopathy is typically metabolic or cytokine-mediated rather than direct viral invasion per Tyler review.

DIAGNOSTIC_TESTS:
  total_results: 4
  pcr_panel: DENV_2_serotype_positive
  xpert_mtb_rif: n/a
  blood_culture: n/a
  csf_culture: n/a
  serology_or_antigen: positive
  smear_or_gram: n/a
  brain_biopsy: n/a

NARRATIVE_EN: A 32-year-old woman in Lima, Peru presented to a tertiary urban emergency department during the Peru 2024 dengue outbreak with a 4-day febrile illness: fever to 39.4 C, retro-orbital pain, severe myalgia, severe headache, and encephalopathic mental status by day 3. The prominent CNS features raised initial differential for other arboviral encephalitides (EEE, JE, WNV). No neck stiffness on examination. Examination on admission: temperature 39.4 C, Glasgow Coma Scale 12, confused, no neck stiffness, no focal deficit, no rash. Platelets 75,000 per cubic millimeter (WHO 2009 dengue with warning signs threshold below 150,000 satisfied). CSF showed opening pressure 19 cmH2O, white cell count 110 per cubic millimeter (70 percent lymphocytes), glucose 58 mg/dL, protein 80 mg/dL. DENV NS1 antigen positive and DENV-2 PCR positive. Brain MRI normal. Diagnostic_ambiguity=true; type=dengue_with_prominent_cns_arbo_encephalitis_overlap. Anchored to Tyler 2018 NEJM viral encephalitis review (PMID 30089069). Outcome: survived. Subphase 1.3 commit 5.3.5 wave 1, pre-adjudication hold_for_revision.

NARRATIVE_ES: Mujer de 32 anos en Lima, Peru, ingresada a urgencias urbanas terciarias durante el brote de dengue de Peru 2024: cuatro dias de fiebre 39.4 C, dolor retro-orbitario, mialgia severa, cefalea intensa y estado mental encefalopatico al tercer dia. Las manifestaciones CNS prominentes elevaron el diagnostico diferencial inicial con otras encefalitides arbovirales. Sin rigidez de nuca al examen. Examen: temperatura 39.4 C, escala de Glasgow 12, confusa. Plaquetas 75,000 por mm3 (umbral signos de alarma OMS 2009 menor de 150,000). Liquido cefalorraquideo mostro presion de apertura 19 cmH2O, leucocitos 110 por mm3 (70 por ciento linfocitos), glucosa 58 mg/dL, proteina 80 mg/dL. NS1 antigeno DENV positivo y PCR DENV-2 positiva. RM cerebral normal. Ambiguedad diagnostica por superposicion CNS arbo-encefalitis. Anclaje en revision Tyler 2018 NEJM (PMID 30089069). Subphase 1.3 commit 5.3.5 wave 1.

RATIONALE: Anchored to PMID 30089069 (Tyler 2018 NEJM viral encephalitis review) with prominent CNS-arbo-encephalitis-overlap phenotype. Diagnostic_ambiguity=true; type=dengue_with_prominent_cns_arbo_encephalitis_overlap (verbatim from spec). Demographic anchor (32yo F Lima during 2024 outbreak) sits in dengue-with-CNS stratum that overlaps with EEE/JE/WNV DDx. Platelets 75k satisfies thrombocytopenia-warning-signs threshold. CSF lymphocytic (110 WBC, 70 percent lymphocytes), normal glucose 58, mildly elevated protein 80. NS1 + DENV-2 PCR confirm organism. Imputation tiers: tier_1_primary={age, sex, region, denv_pcr, ns1, platelets, outbreak_context}; tier_3_within_review={csf_wbc, neutrophil_pct, glucose, protein}; tier_4_priors={temp, gcs, symptom_days}. Indeterminate=initial-arbo-DDx-resolved-by-DENV-PCR. Outcome=survived. Tier: tier_4_imputation_peru_dengue_2024_anchored. 5.3.5 wave1 dengue-Lima-arbo-overlap.

ANCHORING_EXTRAS: stage=pre_adjudication; status=pending_external_review; self_review_disposition=hold_for_revision; self_review_notes=wave 5.3.5 VIRAL vignette anchored to PMID 30089069 (Tyler 2018 NEJM viral encephalitis review); external clinical adjudication pending; classification provisional. adjudicator_ids=VIRAL-WAVE1-PRE-ADJ-1, VIRAL-WAVE1-PRE-ADJ-2 (sentinel); cohen_kappa=0.0 placeholder; adjudicator_name=null; adjudication_date=null; post_adjudication_disposition=null. Subphase 1.3 commit 5.3.5 (2026-05-08). anchor=Tyler-NEJM-2018 type=dengue_with_prominent_cns_arbo_encephalitis_overlap region=Lima-Peru.

ADJUDICATION:
  inclusion_decision: hold_for_revision  ground_truth_class: 3  kappa: 0.0
  adjudicator_ids: ['VIRAL-WAVE1-PRE-ADJ-1', 'VIRAL-WAVE1-PRE-ADJ-2']
  disagreement_resolution: None
```

#### Vignette: vid=119 file=vir_119_dengue_tumbes.json class=3 subphase=1.3 VIRAL

```
ANCHOR:
  pmid: 30089069
  first_author: Tyler
  year: 2018
  journal: NEJM
  citation_type: review
  doi: 10.1056/NEJMra1708714

DEMOGRAPHICS:
  age_years: 41  sex: male  region: peru_tumbes
  ethnicity: mestizo  altitude_m: 6
  hiv_status: negative  cd4: None
  pregnancy_red_flag: False
  immunocompromise_status: none
  freshwater_exposure_14d: False (None)

HISTORY:
  symptom_onset_to_presentation_days: 4.0
  chief_complaint: fever_with_headache
  red_flags_present: []
  prodrome_description: 41-year-old male in Tumbes, Peru coastal community. 4-day febrile illness during regional dengue activity: fever 39.2 C, retro-orbital pain, severe myalgia, severe headache, transient encephalopathy day 3. No neck stiffness. Regional hospital. Outcome: survived with full recovery.

VITALS:
  T:39.2C HR:108 BP:116/72 GCS:13 SpO2:96% RR:22

EXAM:
  mental_status: confused  neck_stiff: False  kernig_brudz: False
  cranial_nerve_palsy: none  papilledema: False  focal_deficit: False
  skin_lesion_centrofacial_chronic: False  rash: False

LABS:
  WBC:4800 Plt:85000 ALT/AST:124 CRP:26.0 PCT:0.5 Na:135

CSF:
  OP:18.0cmH2O  WBC:95/mm3  lymph%:72 neut%:28 eos%:0
  glucose:60mg/dL protein:75mg/dL lactate:2.4mmol/L ADA:NoneU/L
  crag_lfa:negative  wet_mount:negative  xanthochromia:False  RBC:4

IMAGING:
  modality: mri_with_dwi_flair  pattern: normal
  finding_count: 0
  text_summary: MRI brain with DWI/FLAIR: normal. No focal lesion, no edema. Dengue encephalopathy is typically metabolic or cytokine-mediated rather than direct viral invasion per Tyler review.

DIAGNOSTIC_TESTS:
  total_results: 4
  pcr_panel: DENV_2_serotype_positive
  xpert_mtb_rif: n/a
  blood_culture: n/a
  csf_culture: n/a
  serology_or_antigen: positive
  smear_or_gram: n/a
  brain_biopsy: n/a

NARRATIVE_EN: A 41-year-old man in Tumbes, Peru coastal community presented to a regional hospital during regional dengue activity with a 4-day febrile illness: fever to 39.2 C, retro-orbital pain, severe myalgia, severe headache, and transient encephalopathy on day 3. He had no neck stiffness on examination. Examination on admission: temperature 39.2 C, Glasgow Coma Scale 13, confused, no neck stiffness, no focal deficit, no rash. Platelets 85,000 per cubic millimeter (WHO 2009 dengue with warning signs threshold below 150,000). CSF showed opening pressure 18 cmH2O, white cell count 95 per cubic millimeter (72 percent lymphocytes), glucose 60 mg/dL, protein 75 mg/dL. DENV NS1 antigen positive and DENV-2 PCR positive. Brain MRI normal (metabolic / cytokine-mediated encephalopathy). Anchored to Tyler 2018 NEJM viral encephalitis review (PMID 30089069), Peru-coastal-Tumbes dengue stratum. Outcome: survived with full recovery. Subphase 1.3 commit 5.3.5 wave 1, pre-adjudication hold_for_revision.

NARRATIVE_ES: Varon de 41 anos en comunidad costera de Tumbes, Peru, ingresado a hospital regional durante actividad regional de dengue: cuatro dias de fiebre 39.2 C, dolor retro-orbitario, mialgia severa, cefalea intensa y encefalopatia transitoria al tercer dia. Sin rigidez de nuca al examen. Examen: temperatura 39.2 C, escala de Glasgow 13, confuso. Plaquetas 85,000 por mm3 (umbral OMS 2009 menor de 150,000). Liquido cefalorraquideo mostro presion de apertura 18 cmH2O, leucocitos 95 por mm3 (72 por ciento linfocitos), glucosa 60 mg/dL, proteina 75 mg/dL. NS1 antigeno DENV positivo y PCR DENV-2 positiva. RM cerebral normal. Anclaje en revision Tyler 2018 NEJM (PMID 30089069), estrato Tumbes-coastal dengue. Subphase 1.3 commit 5.3.5 wave 1, pre-adjudicacion hold_for_revision.

RATIONALE: Anchored to PMID 30089069 (Tyler 2018 NEJM viral encephalitis review). Dengue with transient encephalopathy in Peru-coastal-Tumbes stratum. Demographic anchor (41yo M Tumbes) sits in Peru-coastal-dengue stratum. Platelets 85k satisfies thrombocytopenia-warning-signs threshold. CSF lymphocytic (95 WBC, 72 percent lymphocytes), normal glucose 60, mildly elevated protein 75. NS1 + DENV-2 PCR confirm organism. MRI normal (metabolic / cytokine encephalopathy not direct viral invasion). Imputation tiers: tier_1_primary={age, sex, region, denv_pcr, ns1, platelets}; tier_3_within_review={csf_wbc, neutrophil_pct, glucose, protein}; tier_4_priors={temp, gcs, symptom_days}. Indeterminate=none. Diagnostic_ambiguity=false. Outcome=survived_full_recovery. Tier: tier_4_imputation_peru_dengue_2024_anchored. 5.3.5 wave1 dengue-Tumbes-coastal.

ANCHORING_EXTRAS: stage=pre_adjudication; status=pending_external_review; self_review_disposition=hold_for_revision; self_review_notes=wave 5.3.5 VIRAL vignette anchored to PMID 30089069 (Tyler 2018 NEJM viral encephalitis review); external clinical adjudication pending; classification provisional. adjudicator_ids=VIRAL-WAVE1-PRE-ADJ-1, VIRAL-WAVE1-PRE-ADJ-2 (sentinel); cohen_kappa=0.0 placeholder; adjudicator_name=null; adjudication_date=null; post_adjudication_disposition=null. Subphase 1.3 commit 5.3.5 (2026-05-08). anchor=Tyler-NEJM-2018 region=Tumbes-Peru.

ADJUDICATION:
  inclusion_decision: hold_for_revision  ground_truth_class: 3  kappa: 0.0
  adjudicator_ids: ['VIRAL-WAVE1-PRE-ADJ-1', 'VIRAL-WAVE1-PRE-ADJ-2']
  disagreement_resolution: None
```

#### Vignette: vid=120 file=vir_120_eee_northeast_us_fatal.json class=3 subphase=1.3 VIRAL

```
ANCHOR:
  pmid: 30089069
  first_author: Tyler
  year: 2018
  journal: NEJM
  citation_type: review
  doi: 10.1056/NEJMra1708714

DEMOGRAPHICS:
  age_years: 58  sex: male  region: us_south
  ethnicity: white_non_hispanic  altitude_m: 100
  hiv_status: negative  cd4: None
  pregnancy_red_flag: False
  immunocompromise_status: none
  freshwater_exposure_14d: False (None)

HISTORY:
  symptom_onset_to_presentation_days: 5.0
  chief_complaint: altered_mental_status
  red_flags_present: []
  prodrome_description: 58-year-old male, US South region. 5-day course: fever 39.0 C, severe headache, neck stiffness, then progressive encephalopathy with stupor day 4 and coma day 5. Recent outdoor activity in mosquito-endemic wooded area. Tertiary ED. Outcome: fatal hospital day 4. EEE per Tyler review case fatality approximately 30 percent.

VITALS:
  T:39.0C HR:124 BP:102/64 GCS:6 SpO2:90% RR:28

EXAM:
  mental_status: comatose  neck_stiff: True  kernig_brudz: True
  cranial_nerve_palsy: none  papilledema: False  focal_deficit: True
  skin_lesion_centrofacial_chronic: False  rash: False

LABS:
  WBC:13500 Plt:175000 ALT/AST:38 CRP:65.0 PCT:1.2 Na:132

CSF:
  OP:28.0cmH2O  WBC:350/mm3  lymph%:60 neut%:35 eos%:5
  glucose:48mg/dL protein:145mg/dL lactate:3.4mmol/L ADA:NoneU/L
  crag_lfa:negative  wet_mount:negative  xanthochromia:False  RBC:5

IMAGING:
  modality: mri_with_dwi_flair  pattern: diffuse_cerebral_edema_basilar_meningeal_enhancement
  finding_count: 1
  text_summary: MRI brain with DWI/FLAIR: diffuse cerebral edema with basal ganglia and thalamic involvement, sulcal effacement. EEE predilection for basal ganglia and thalamus per Tyler 2018 NEJM review (case fatality approximately 30 percent; permanent neurologic sequelae in 50 percent of survivors).

DIAGNOSTIC_TESTS:
  total_results: 4
  pcr_panel: positive
  xpert_mtb_rif: n/a
  blood_culture: n/a
  csf_culture: n/a
  serology_or_antigen: positive
  smear_or_gram: n/a
  brain_biopsy: n/a

NARRATIVE_EN: A 58-year-old man in the US South region presented to a tertiary emergency department with a 5-day course of fever to 39.0 C, severe headache, neck stiffness, then progressive encephalopathy with stupor on day 4 and coma on day 5. He reported recent outdoor activity in a mosquito-endemic wooded area. Examination on admission: temperature 39.0 C, Glasgow Coma Scale 6, comatose, neck stiffness, positive Kernig sign, focal deficit (left-sided weakness), no rash. CSF showed opening pressure 28 cmH2O, white cell count 350 per cubic millimeter (60 percent lymphocytes, 35 percent neutrophils, 5 percent eosinophils), glucose 48 mg/dL, protein 145 mg/dL. CSF EEE IgM serology positive and CSF EEE PCR positive. Brain MRI with DWI/FLAIR showed diffuse cerebral edema with basal ganglia and thalamic involvement (EEE predilection per Tyler review). Anchored to Tyler 2018 NEJM viral encephalitis review (PMID 30089069), EEE high-mortality older-adult stratum (case fatality approximately 30 percent, permanent sequelae in 50 percent of survivors). Outcome: fatal hospital day 4. Subphase 1.3 commit 5.3.5 wave 1, pre-adjudication hold_for_revision.

NARRATIVE_ES: Varon de 58 anos en region sur de Estados Unidos, ingresado a urgencias terciarias con curso de cinco dias: fiebre 39.0 C, cefalea intensa, rigidez de nuca, luego encefalopatia progresiva con estupor al cuarto dia y coma al quinto. Actividad reciente al aire libre en area boscosa endemica de mosquitos. Examen: temperatura 39.0 C, escala de Glasgow 6, comatoso, rigidez de nuca, signo de Kernig positivo, deficit focal (debilidad izquierda), sin exantema. Liquido cefalorraquideo mostro presion de apertura 28 cmH2O, leucocitos 350 por mm3 (60 por ciento linfocitos, 35 por ciento neutrofilos), glucosa 48 mg/dL, proteina 145 mg/dL. IgM y PCR de EEE en LCR positivas. RM cerebral con edema cerebral difuso con compromiso de ganglios basales y talamo. Anclaje en revision Tyler 2018 NEJM (PMID 30089069), estrato EEE alta mortalidad. Subphase 1.3 commit 5.3.5 wave 1.

RATIONALE: Anchored to PMID 30089069 (Tyler 2018 NEJM viral encephalitis review). EEE high-mortality older-adult phenotype (case fatality approximately 30 percent, permanent neurologic sequelae in 50 percent of survivors per Tyler review). Demographic anchor (58yo M US South mosquito-endemic woods) sits in EEE-older-adult stratum. CSF mixed-cellularity leaning lymphocytic (350 WBC, 60 percent lymphocytes, 35 percent neutrophils, 5 percent eosinophils), glucose 48 (near master prompt 1.3.4 floor), elevated protein 145. EEE IgM + PCR positive. MRI diffuse cerebral edema with basal ganglia and thalamic involvement. Imputation tiers: tier_1_primary={age, sex, eee_igm, eee_pcr, mosquito_endemic_area, imaging_pattern}; tier_3_within_review={csf_wbc, neutrophil_pct, glucose, protein, gcs}; tier_4_priors={temp, symptom_days, hr}. Indeterminate=none. Diagnostic_ambiguity=false. Outcome=fatal_hospital_day_4. Tier: tier_3_imputation_within_review. 5.3.5 wave1 EEE-older-adult-fatal.

ANCHORING_EXTRAS: stage=pre_adjudication; status=pending_external_review; self_review_disposition=hold_for_revision; self_review_notes=wave 5.3.5 VIRAL vignette anchored to PMID 30089069 (Tyler 2018 NEJM viral encephalitis review); external clinical adjudication pending; classification provisional. adjudicator_ids=VIRAL-WAVE1-PRE-ADJ-1, VIRAL-WAVE1-PRE-ADJ-2 (sentinel); cohen_kappa=0.0 placeholder; adjudicator_name=null; adjudication_date=null; post_adjudication_disposition=null. Subphase 1.3 commit 5.3.5 (2026-05-08). anchor=Tyler-NEJM-2018 stratum=EEE-older-adult-fatal mosquito_endemic=true.

ADJUDICATION:
  inclusion_decision: hold_for_revision  ground_truth_class: 3  kappa: 0.0
  adjudicator_ids: ['VIRAL-WAVE1-PRE-ADJ-1', 'VIRAL-WAVE1-PRE-ADJ-2']
  disagreement_resolution: None
```

### REVIEWER PROMPT (Claude chat fills below)

For each vignette above, the reviewer (Claude chat) must answer:
1. Does the vignette's clinical content match the anchor paper's actual claims?
2. Are demographics, CSF, vitals, imaging plausible per the paper?
3. Does the narrative reference the anchor accurately (year, author, claim)?
4. Would this vignette anchor better to a different paper in the registry? (specify which if yes)
5. Severity if issues found: [Catastrophic / Needs Errata / Minor / Clean]

### REVIEWER NOTES (Claude chat YYYY-MM-DD)

_(empty; to be filled during chat verification)_
