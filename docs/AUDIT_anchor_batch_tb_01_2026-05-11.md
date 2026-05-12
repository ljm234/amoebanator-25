# AUDIT batch: class=tb batch=1/1

Generated: 2026-05-11
Vignettes in bundle: 4
Anchors in bundle: 2
Build status: NCBI fetched (mixed)
Bundle type: CLASS-LOCKED-BATCH (class tb, small clusters packed)

## Anchors in this batch

- pmid:24655399 (van 2014, n=1)
- pmid:20822958 (Marais 2010, n=3)

## Anchor: PMID 24655399 | van 2014

### Registry metadata (current state)

```json
{
  "pmid": "24655399",
  "doi": "10.1016/j.spen.2014.01.006",
  "authors_short": "van Toorn R, Solomons R",
  "authors_full": [
    "van Toorn R",
    "Solomons R"
  ],
  "journal": "Semin Pediatr Neurol",
  "journal_short_code": "Semin-Pediatr-Neurol",
  "year": 2014,
  "volume": "21",
  "issue": "1",
  "pages": "12-18",
  "title": "Update on the diagnosis and management of tuberculous meningitis in children",
  "anchor_type": "review",
  "anchor_subtype": "pediatric_tbm_review_diagnosis_management",
  "verification_confidence": 0.85,
  "verification_method": "claude_web_pubmed_ui_v5_2026_05_11",
  "last_verified_date": "2026-05-11",
  "caveat": "Subphase 1.4 commit 5.4.0 anchor for Class 4 pediatric TBM stratum (8 slots median 6mo-2y per master prompt 1.4.4). Master plan referenced J Child Neurol; actual journal is Semin Pediatr Neurol per PubMed. Corrected at registration. verification_confidence=0.85 pre-direct-fetch."
}
```

### NCBI live re-fetch (2026-05-11)

```json
{
  "uid": "24655399",
  "pubdate": "2014 Mar",
  "epubdate": "2014 Feb 2",
  "source": "Semin Pediatr Neurol",
  "authors": [
    {
      "name": "van Toorn R",
      "authtype": "Author",
      "clusterid": ""
    },
    {
      "name": "Solomons R",
      "authtype": "Author",
      "clusterid": ""
    }
  ],
  "lastauthor": "Solomons R",
  "title": "Update on the diagnosis and management of tuberculous meningitis in children.",
  "sorttitle": "update on the diagnosis and management of tuberculous meningitis in children",
  "volume": "21",
  "issue": "1",
  "pages": "12-8",
  "lang": [
    "eng"
  ],
  "nlmuniqueid": "9441351",
  "issn": "1071-9091",
  "essn": "1558-0776",
  "pubtype": [
    "Journal Article",
    "Review"
  ],
  "recordstatus": "PubMed - indexed for MEDLINE",
  "pubstatus": "256",
  "articleids": [
    {
      "idtype": "pubmed",
      "idtypen": 1,
      "value": "24655399"
    },
    {
      "idtype": "doi",
      "idtypen": 3,
      "value": "10.1016/j.spen.2014.01.006"
    },
    {
      "idtype": "pii",
      "idtypen": 4,
      "value": "S1071-9091(14)00007-2"
    }
  ],
  "history": [
    {
      "pubstatus": "entrez",
      "date": "2014/03/25 06:00"
    },
    {
      "pubstatus": "pubmed",
      "date": "2014/03/25 06:00"
    },
    {
      "pubstatus": "medline",
      "date": "2014/11/14 06:00"
    }
  ],
  "references": [],
  "attributes": [
    "Has Abstract"
  ],
  "pmcrefcount": "",
  "fulljournalname": "Seminars in pediatric neurology",
  "elocationid": "doi: 10.1016/j.spen.2014.01.006",
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
  "sortpubdate": "2014/03/01 00:00",
  "sortfirstauthor": "van Toorn R",
  "vernaculartitle": ""
}
```

### Registry-vs-NCBI delta

- **pages**: registry='12-18' | ncbi='12-8'

### Vignettes citing this anchor (1 total)

#### Vignette: vid=122 file=tbm_122_vantoorn_cape_town_pediatric_pilot.json class=4 subphase=1.4 TBM pilot

```
ANCHOR:
  pmid: 24655399
  first_author: van
  year: 2014
  journal: Semin-Pediatr-Neurol
  citation_type: review
  doi: 10.1016/j.spen.2014.01.006

DEMOGRAPHICS:
  age_years: 1  sex: female  region: other_global
  ethnicity: other  altitude_m: 50
  hiv_status: negative  cd4: None
  pregnancy_red_flag: False
  immunocompromise_status: none
  freshwater_exposure_14d: False (None)

HISTORY:
  symptom_onset_to_presentation_days: 21.0
  chief_complaint: altered_mental_status
  red_flags_present: []
  prodrome_description: Eighteen-month-old girl from Cape Town with three weeks of intermittent fever, poor feeding, weight failure, and increasing irritability. The grandmother was treated for sputum-positive pulmonary tuberculosis four months earlier. BCG vaccinated at birth. Progressive lethargy in the final five days with one focal seizure.

VITALS:
  T:38.1C HR:142 BP:95/58 GCS:11 SpO2:95% RR:32

EXAM:
  mental_status: somnolent  neck_stiff: True  kernig_brudz: True
  cranial_nerve_palsy: none  papilledema: True  focal_deficit: True
  skin_lesion_centrofacial_chronic: False  rash: False

LABS:
  WBC:11200 Plt:286000 ALT/AST:22 CRP:26.0 PCT:0.3 Na:124

CSF:
  OP:28.0cmH2O  WBC:220/mm3  lymph%:80 neut%:18 eos%:2
  glucose:22mg/dL protein:220mg/dL lactate:4.4mmol/L ADA:12.0U/L
  crag_lfa:negative  wet_mount:negative  xanthochromia:False  RBC:2

IMAGING:
  modality: mri_contrast  pattern: basal_meningeal_enhancement_with_hydrocephalus
  finding_count: None
  text_summary: Marked basal meningeal enhancement with communicating hydrocephalus requiring ventriculoperitoneal shunt placement. Multiple small basal ganglia infarcts. Findings highly characteristic of pediatric tuberculous meningitis per van Toorn pediatric TBM phenotype.

DIAGNOSTIC_TESTS:
  total_results: 5
  pcr_panel: n/a
  xpert_mtb_rif: Positive, rifampicin susceptible. Cycle threshold consistent with TBM.
  blood_culture: n/a
  csf_culture: Pending at LP; reported positive at 4 weeks (M. tuberculosis drug-sensitive).
  serology_or_antigen: n/a
  smear_or_gram: n/a
  brain_biopsy: n/a

NARRATIVE_EN: An 18-month-old girl from Cape Town presented to a pediatric tertiary hospital with three weeks of intermittent fever, poor feeding, failure to thrive, and increasing irritability. Her grandmother had been treated for sputum-positive pulmonary tuberculosis four months earlier. The child had received BCG vaccination at birth. Over the final five days she became progressively lethargic with one focal seizure on the day of admission. Examination: temperature 38.1 C, Glasgow Coma Scale 11, somnolent, neck stiffness, positive Kernig sign, right-sided motor weakness, and papilledema on fundoscopy. CSF showed opening pressure 28 cmH2O, white cell count 220 per cubic millimeter with 80 percent lymphocytes, glucose 22 mg/dL, protein 220 mg/dL, and adenosine deaminase 12 U/L. Serum sodium was 124 mEq/L consistent with SIADH. MRI showed marked basal meningeal enhancement with communicating hydrocephalus that required ventriculoperitoneal shunt placement. CSF Xpert MTB/RIF Ultra was positive. Anchored to van Toorn Semin Pediatr Neurol 2014 (PMID 24655399). Pilot, hold_for_revision.

NARRATIVE_ES: Nina de 18 meses de Ciudad del Cabo, Sudafrica, ingresada a un hospital pediatrico terciario tras tres semanas de fiebre intermitente, mala alimentacion, fallo en el crecimiento e irritabilidad creciente. Abuela tratada por tuberculosis pulmonar baciloscopia positiva cuatro meses antes. Vacunada con BCG al nacer. En los ultimos cinco dias progreso a letargia con una crisis focal el dia del ingreso. Examen: temperatura 38.1 C, Glasgow 11, somnolienta, rigidez de nuca, Kernig positivo, hemiparesia derecha, papiledema. LCR con presion 28 cmH2O, leucocitos 220 por mm3 (80 por ciento linfocitos), glucosa 22 mg/dL, proteina 220 mg/dL, adenosina desaminasa 12 U/L. Sodio serico 124 (SIADH). RM con engrosamiento meningeo basal e hidrocefalia comunicante, manejada con derivacion ventriculo-peritoneal. Xpert positivo. Anclaje van Toorn 2014.

RATIONALE: Subphase 1.4 commit 5.4.2 pilot 2 of 6 for Class 4 TBM pediatric (master prompt 1.4.4 pediatric median 6mo-2y stratum). Anchored to van Toorn 2014 Semin Pediatr Neurol pediatric TBM review. Hydrocephalus requiring VP shunt is van Toorn signature; hyponatremia 124 reflects SIADH common in pediatric TBM. Pre-adjudication hold_for_revision.

ANCHORING_EXTRAS: Anchored to van Toorn R, Solomons R, Semin Pediatr Neurol 2014 (PMID 24655399), pediatric TBM review. 18-month-old Cape Town girl, BCG vaccinated, household TB contact, lymphocytic CSF with ADA 12, Xpert MTB/RIF Ultra positive, communicating hydrocephalus on MRI requiring VP shunt. Pre-adjudication kappa 0.70.

ADJUDICATION:
  inclusion_decision: hold_for_revision  ground_truth_class: 4  kappa: 0.7
  adjudicator_ids: ['PILOT-TBM-122-ADJ-1', 'PILOT-TBM-122-ADJ-2']
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

## Anchor: PMID 20822958 | Marais 2010

### Registry metadata (current state)

```json
{
  "pmid": "20822958",
  "doi": "10.1016/S1473-3099(10)70138-9",
  "authors_short": "Marais S et al.",
  "authors_full": [
    "Marais S",
    "Thwaites G",
    "Schoeman JF",
    "Torok ME",
    "Misra UK",
    "Prasad K",
    "Donald PR",
    "Wilkinson RJ",
    "Marais BJ"
  ],
  "journal": "Lancet Infect Dis",
  "journal_short_code": "Lancet Infect Dis",
  "year": 2010,
  "volume": "10",
  "issue": "11",
  "pages": "803-812",
  "title": "Tuberculous meningitis: a uniform case definition for use in clinical research",
  "anchor_type": "guideline",
  "anchor_subtype": "tbm_uniform_case_definition_clinical_research",
  "verification_confidence": 0.85,
  "verification_method": "claude_web_pubmed_ui_v5_2026_05_11",
  "last_verified_date": "2026-05-11",
  "caveat": "Subphase 1.4 commit 5.4.0 anchor for Class 4 TBM. Marais 2010 uniform case definition is the canonical clinical research framework cited in ml/schemas/labels.py docstring. Torok ME diacritic O-with-umlaut rendered as plain O for ASCII safety; original is Torok with diacritic. verification_confidence=0.85 pre-direct-fetch."
}
```

### NCBI live re-fetch (2026-05-11)

```json
{
  "uid": "20822958",
  "pubdate": "2010 Nov",
  "epubdate": "2010 Sep 6",
  "source": "Lancet Infect Dis",
  "authors": [
    {
      "name": "Marais S",
      "authtype": "Author",
      "clusterid": ""
    },
    {
      "name": "Thwaites G",
      "authtype": "Author",
      "clusterid": ""
    },
    {
      "name": "Schoeman JF",
      "authtype": "Author",
      "clusterid": ""
    },
    {
      "name": "Török ME",
      "authtype": "Author",
      "clusterid": ""
    },
    {
      "name": "Misra UK",
      "authtype": "Author",
      "clusterid": ""
    },
    {
      "name": "Prasad K",
      "authtype": "Author",
      "clusterid": ""
    },
    {
      "name": "Donald PR",
      "authtype": "Author",
      "clusterid": ""
    },
    {
      "name": "Wilkinson RJ",
      "authtype": "Author",
      "clusterid": ""
    },
    {
      "name": "Marais BJ",
      "authtype": "Author",
      "clusterid": ""
    }
  ],
  "lastauthor": "Marais BJ",
  "title": "Tuberculous meningitis: a uniform case definition for use in clinical research.",
  "sorttitle": "tuberculous meningitis a uniform case definition for use in clinical research",
  "volume": "10",
  "issue": "11",
  "pages": "803-12",
  "lang": [
    "eng"
  ],
  "nlmuniqueid": "101130150",
  "issn": "1473-3099",
  "essn": "1474-4457",
  "pubtype": [
    "Consensus Statement",
    "Journal Article",
    "Research Support, Non-U.S. Gov't",
    "Research Support, U.S. Gov't, Non-P.H.S."
  ],
  "recordstatus": "PubMed - indexed for MEDLINE",
  "pubstatus": "256",
  "articleids": [
    {
      "idtype": "pubmed",
      "idtypen": 1,
      "value": "20822958"
    },
    {
      "idtype": "doi",
      "idtypen": 3,
      "value": "10.1016/S1473-3099(10)70138-9"
    },
    {
      "idtype": "pii",
      "idtypen": 4,
      "value": "S1473-3099(10)70138-9"
    }
  ],
  "history": [
    {
      "pubstatus": "entrez",
      "date": "2010/09/09 06:00"
    },
    {
      "pubstatus": "pubmed",
      "date": "2010/09/09 06:00"
    },
    {
      "pubstatus": "medline",
      "date": "2010/11/16 06:00"
    }
  ],
  "references": [],
  "attributes": [
    "Has Abstract"
  ],
  "pmcrefcount": "",
  "fulljournalname": "The Lancet. Infectious diseases",
  "elocationid": "doi: 10.1016/S1473-3099(10)70138-9",
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
  "sortpubdate": "2010/11/01 00:00",
  "sortfirstauthor": "Marais S",
  "vernaculartitle": ""
}
```

### Registry-vs-NCBI delta

- **pages**: registry='803-812' | ncbi='803-12'

### Vignettes citing this anchor (3 total)

#### Vignette: vid=128 file=tbm_128_marais_cape_town_adult_female_definite_wave1.json class=4 subphase=1.4 TBM wave_1

```
ANCHOR:
  pmid: 20822958
  first_author: Marais
  year: 2010
  journal: Lancet Infect Dis
  citation_type: guideline
  doi: 10.1016/S1473-3099(10)70138-9

DEMOGRAPHICS:
  age_years: 32  sex: female  region: other_global
  ethnicity: other  altitude_m: 50
  hiv_status: negative  cd4: None
  pregnancy_red_flag: False
  immunocompromise_status: none
  freshwater_exposure_14d: False (None)

HISTORY:
  symptom_onset_to_presentation_days: 21.0
  chief_complaint: fever_with_headache
  red_flags_present: []
  prodrome_description: Three-week illness in a 32-year-old woman from Cape Town. Subacute headache, intermittent fevers, weight loss of 4 kg. Her husband had recently started treatment for sputum-positive pulmonary tuberculosis.

VITALS:
  T:38.4C HR:98 BP:116/72 GCS:13 SpO2:97% RR:18

EXAM:
  mental_status: somnolent  neck_stiff: True  kernig_brudz: True
  cranial_nerve_palsy: none  papilledema: True  focal_deficit: False
  skin_lesion_centrofacial_chronic: False  rash: False

LABS:
  WBC:8200 Plt:274000 ALT/AST:26 CRP:42.0 PCT:0.4 Na:130

CSF:
  OP:22.0cmH2O  WBC:280/mm3  lymph%:78 neut%:20 eos%:2
  glucose:28mg/dL protein:240mg/dL lactate:4.4mmol/L ADA:14.0U/L
  crag_lfa:negative  wet_mount:negative  xanthochromia:False  RBC:2

IMAGING:
  modality: mri_contrast  pattern: basal_meningeal_enhancement_with_hydrocephalus
  finding_count: None
  text_summary: Thick basal meningeal enhancement on post-contrast T1 with mild communicating hydrocephalus and a small left basal ganglia infarct. Findings consistent with active tuberculous meningitis.

DIAGNOSTIC_TESTS:
  total_results: 3
  pcr_panel: n/a
  xpert_mtb_rif: Positive, rifampicin susceptible. Cycle threshold consistent with TBM.
  blood_culture: n/a
  csf_culture: Pending at LP; reported positive at 4 weeks (M. tuberculosis drug-sensitive).
  serology_or_antigen: n/a
  smear_or_gram: n/a
  brain_biopsy: n/a

NARRATIVE_EN: A 32-year-old woman from Cape Town presented to a tertiary referral hospital with a three-week illness of subacute headache, intermittent fevers, and a four-kilogram weight loss. Her husband had recently started treatment for sputum-positive pulmonary tuberculosis. Examination on admission: temperature 38.4 C, Glasgow Coma Scale 13, somnolent but rousable, neck stiffness, positive Kernig sign, no focal motor deficit, and papilledema on fundoscopy. CSF showed an opening pressure of 22 cmH2O, white cell count 280 per cubic millimeter with 78 percent lymphocytes, glucose 28 mg/dL, protein 240 mg/dL, and adenosine deaminase 14 U/L. MRI with contrast demonstrated basal meningeal enhancement with mild communicating hydrocephalus. CSF Xpert MTB/RIF Ultra was positive and rifampicin susceptible, satisfying the Marais 2010 uniform case definition for definite tuberculous meningitis. Anchored to Marais Lancet ID 2010 (PMID 20822958). Wave 1, hold_for_revision.

NARRATIVE_ES: Mujer de 32 anos de Ciudad del Cabo, Sudafrica, ingresada a un hospital terciario tras tres semanas de cefalea subaguda, fiebre intermitente y perdida de 4 kg. Esposo recientemente en tratamiento por tuberculosis pulmonar baciloscopia positiva. Examen: temperatura 38.4 C, Glasgow 13, somnolienta, rigidez de nuca, Kernig positivo, sin deficit motor focal, papiledema en fondo de ojo. LCR con presion 22 cmH2O, leucocitos 280 por mm3 (78 por ciento linfocitos), glucosa 28 mg/dL, proteina 240 mg/dL, adenosina desaminasa 14 U/L. RM con engrosamiento meningeo basal e hidrocefalia comunicante leve. Xpert MTB/RIF Ultra positivo en LCR, susceptible a rifampicina, cumpliendo la definicion de caso uniforme de Marais 2010 para meningitis tuberculosa definitiva. Anclaje Marais Lancet ID 2010.

RATIONALE: Subphase 1.4 commit 5.4.3 wave 1 vignette 128 of 14 for Class 4 TBM. Anchored to Marais 2010 uniform case definition; classical definite TBM (microbiologically confirmed). Pre-adjudication hold_for_revision.

ANCHORING_EXTRAS: Anchored to Marais S et al. Lancet ID 2010 (PMID 20822958), TBM uniform case definition. 32-year-old South African adult female HIV-negative, household TB contact, drug-sensitive TBM, lymphocytic CSF, ADA 14 U/L, Xpert MTB/RIF Ultra positive (definite TBM per uniform case definition). Pre-adjudication kappa 0.70.

ADJUDICATION:
  inclusion_decision: hold_for_revision  ground_truth_class: 4  kappa: 0.7
  adjudicator_ids: ['WAVE1-TBM-128-ADJ-1', 'WAVE1-TBM-128-ADJ-2']
  disagreement_resolution: None
```

#### Vignette: vid=129 file=tbm_129_marais_cape_town_adult_male_probable_wave1.json class=4 subphase=1.4 TBM wave_1

```
ANCHOR:
  pmid: 20822958
  first_author: Marais
  year: 2010
  journal: Lancet Infect Dis
  citation_type: guideline
  doi: 10.1016/S1473-3099(10)70138-9

DEMOGRAPHICS:
  age_years: 46  sex: male  region: other_global
  ethnicity: other  altitude_m: 50
  hiv_status: negative  cd4: None
  pregnancy_red_flag: False
  immunocompromise_status: none
  freshwater_exposure_14d: False (None)

HISTORY:
  symptom_onset_to_presentation_days: 28.0
  chief_complaint: fever_with_headache
  red_flags_present: []
  prodrome_description: Four-week illness in a 46-year-old man from Cape Town. Worsening headache, low-grade fevers, and three days of binocular horizontal diplopia in the final week. His brother had died of tuberculosis ten years earlier; heavy alcohol use.

VITALS:
  T:38.2C HR:102 BP:122/76 GCS:12 SpO2:96% RR:18

EXAM:
  mental_status: somnolent  neck_stiff: True  kernig_brudz: True
  cranial_nerve_palsy: CN_VI  papilledema: True  focal_deficit: True
  skin_lesion_centrofacial_chronic: False  rash: False

LABS:
  WBC:9400 Plt:232000 ALT/AST:64 CRP:52.0 PCT:0.6 Na:128

CSF:
  OP:24.0cmH2O  WBC:340/mm3  lymph%:76 neut%:22 eos%:2
  glucose:22mg/dL protein:300mg/dL lactate:4.4mmol/L ADA:16.0U/L
  crag_lfa:negative  wet_mount:negative  xanthochromia:False  RBC:2

IMAGING:
  modality: mri_contrast  pattern: basal_meningeal_enhancement_with_hydrocephalus
  finding_count: None
  text_summary: Thick basal meningeal enhancement on post-contrast T1 with mild communicating hydrocephalus and a small left basal ganglia infarct. Findings consistent with active tuberculous meningitis.

DIAGNOSTIC_TESTS:
  total_results: 3
  pcr_panel: n/a
  xpert_mtb_rif: Positive, rifampicin susceptible. Cycle threshold consistent with TBM.
  blood_culture: n/a
  csf_culture: Pending at LP; reported positive at 4 weeks (M. tuberculosis drug-sensitive).
  serology_or_antigen: n/a
  smear_or_gram: n/a
  brain_biopsy: n/a

NARRATIVE_EN: A 46-year-old man from Cape Town presented to a tertiary referral hospital with a four-week illness of worsening headache, persistent low-grade fevers, and three days of binocular horizontal diplopia in the final week. His brother had died of tuberculosis ten years earlier, and he reported heavy alcohol use. Examination on admission: temperature 38.2 C, Glasgow Coma Scale 12, somnolent but rousable, neck stiffness, positive Kernig sign, left lateral gaze palsy consistent with sixth cranial nerve involvement, and bilateral papilledema. CSF showed an opening pressure of 24 cmH2O, white cell count 340 per cubic millimeter with 76 percent lymphocytes, glucose 22 mg/dL, protein 300 mg/dL, and adenosine deaminase 16 U/L. MRI with contrast demonstrated thick basal meningeal enhancement with moderate communicating hydrocephalus. CSF Xpert MTB/RIF Ultra was positive and rifampicin susceptible; the case meets Marais 2010 probable tuberculous meningitis criteria with score 14. Anchored to Marais Lancet ID 2010. Wave 1, hold_for_revision.

NARRATIVE_ES: Varon de 46 anos de Ciudad del Cabo, Sudafrica, ingresado a un hospital terciario tras cuatro semanas de cefalea creciente, fiebre baja persistente y tres dias de diplopia horizontal binocular en la ultima semana. Hermano fallecido de tuberculosis hace diez anos; consumo intenso de alcohol. Examen: temperatura 38.2 C, Glasgow 12, somnoliento, rigidez de nuca, Kernig positivo, paresia del sexto par craneal izquierdo, papiledema bilateral. LCR con presion 24 cmH2O, leucocitos 340 por mm3 (76 por ciento linfocitos), glucosa 22 mg/dL, proteina 300 mg/dL, adenosina desaminasa 16 U/L. RM con engrosamiento meningeo basal e hidrocefalia comunicante moderada. Xpert MTB/RIF Ultra positivo en LCR; el caso cumple criterios probables de Marais 2010 con puntaje 14. Anclaje Marais Lancet ID 2010.

RATIONALE: Subphase 1.4 commit 5.4.3 wave 1 vignette 129 of 14 for Class 4 TBM. Anchored to Marais 2010 probable category (score 14). CN VI palsy positive (Huynh 30 percent subset). Pre-adjudication hold_for_revision.

ANCHORING_EXTRAS: Anchored to Marais S et al. Lancet ID 2010 (PMID 20822958), TBM uniform case definition probable category. 46-year-old South African adult male HIV-negative heavy alcohol, lymphocytic CSF (lymph 76 percent, protein 300, glucose 22), ADA 16 U/L, Xpert MTB/RIF Ultra positive, CN VI palsy positive, Marais score 14. Pre-adjudication kappa 0.70.

ADJUDICATION:
  inclusion_decision: hold_for_revision  ground_truth_class: 4  kappa: 0.7
  adjudicator_ids: ['WAVE1-TBM-129-ADJ-1', 'WAVE1-TBM-129-ADJ-2']
  disagreement_resolution: None
```

#### Vignette: vid=130 file=tbm_130_marais_cape_town_adult_female_possible_wave1.json class=4 subphase=1.4 TBM wave_1

```
ANCHOR:
  pmid: 20822958
  first_author: Marais
  year: 2010
  journal: Lancet Infect Dis
  citation_type: guideline
  doi: 10.1016/S1473-3099(10)70138-9

DEMOGRAPHICS:
  age_years: 29  sex: female  region: other_global
  ethnicity: other  altitude_m: 50
  hiv_status: negative  cd4: None
  pregnancy_red_flag: False
  immunocompromise_status: none
  freshwater_exposure_14d: False (None)

HISTORY:
  symptom_onset_to_presentation_days: 14.0
  chief_complaint: fever_with_headache
  red_flags_present: []
  prodrome_description: Two-week illness in a 29-year-old woman from Cape Town with subacute headache and intermittent low-grade fevers. She lived in an informal settlement, was HIV negative on rapid testing, and reported no documented tuberculosis contact.

VITALS:
  T:38.0C HR:92 BP:118/74 GCS:14 SpO2:97% RR:18

EXAM:
  mental_status: confused  neck_stiff: True  kernig_brudz: True
  cranial_nerve_palsy: none  papilledema: False  focal_deficit: False
  skin_lesion_centrofacial_chronic: False  rash: False

LABS:
  WBC:7400 Plt:264000 ALT/AST:22 CRP:28.0 PCT:0.3 Na:134

CSF:
  OP:18.0cmH2O  WBC:200/mm3  lymph%:76 neut%:22 eos%:2
  glucose:36mg/dL protein:180mg/dL lactate:4.4mmol/L ADA:11.0U/L
  crag_lfa:negative  wet_mount:negative  xanthochromia:False  RBC:2

IMAGING:
  modality: mri_contrast  pattern: basal_meningeal_enhancement_with_hydrocephalus
  finding_count: None
  text_summary: Thick basal meningeal enhancement on post-contrast T1 with mild communicating hydrocephalus and a small left basal ganglia infarct. Findings consistent with active tuberculous meningitis.

DIAGNOSTIC_TESTS:
  total_results: 3
  pcr_panel: n/a
  xpert_mtb_rif: Negative on initial CSF specimen. Sensitivity 70-85 percent in TBM per Hernandez TM&IH 2021; culture remains the confirmation modality.
  blood_culture: n/a
  csf_culture: Positive at 4 weeks (M. tuberculosis drug-sensitive); Xpert-negative-culture-confirmed case per RCT inclusion.
  serology_or_antigen: n/a
  smear_or_gram: n/a
  brain_biopsy: n/a

NARRATIVE_EN: A 29-year-old woman from Cape Town presented to a tertiary referral hospital with a two-week illness of subacute headache and intermittent low-grade fevers. She lived in an informal settlement, was HIV negative on rapid testing, and reported no documented tuberculosis contact. Examination on admission: temperature 38.0 C, Glasgow Coma Scale 14, mild confusion, neck stiffness, positive Kernig sign, no focal motor deficit, and no papilledema on fundoscopy. CSF showed an opening pressure of 18 cmH2O, white cell count 200 per cubic millimeter with 76 percent lymphocytes, glucose 36 mg/dL, protein 180 mg/dL, and adenosine deaminase 11 U/L. MRI with contrast demonstrated subtle basal meningeal enhancement without hydrocephalus. CSF Xpert MTB/RIF Ultra was negative on the initial specimen and mycobacterial culture remained pending. The case meets Marais 2010 possible tuberculous meningitis criteria with score 9; empirical anti-tuberculous therapy was initiated. Anchored to Marais Lancet ID 2010 (PMID 20822958). Wave 1, hold_for_revision.

NARRATIVE_ES: Mujer de 29 anos de Ciudad del Cabo, Sudafrica, ingresada a un hospital terciario tras dos semanas de cefalea subaguda y fiebre baja intermitente. Vive en asentamiento informal, VIH negativo en prueba rapida, sin contacto documentado con tuberculosis. Examen: temperatura 38.0 C, Glasgow 14, confusion leve, rigidez de nuca, Kernig positivo, sin deficit motor focal, sin papiledema. LCR con presion 18 cmH2O, leucocitos 200 por mm3 (76 por ciento linfocitos), glucosa 36 mg/dL, proteina 180 mg/dL, adenosina desaminasa 11 U/L. RM con engrosamiento meningeo basal sutil sin hidrocefalia. Xpert MTB/RIF Ultra negativo en muestra inicial; cultivo micobacteriano pendiente. El caso cumple criterios posibles de Marais 2010 con puntaje 9; tratamiento antifimico empirico iniciado. Anclaje Marais Lancet ID 2010. Wave 1, pre-adjudicacion.

RATIONALE: Subphase 1.4 commit 5.4.3 wave 1 vignette 130 of 14 for Class 4 TBM. Anchored to Marais 2010 possible category (score 9). Diagnostic ambiguity slot: Xpert NEG with culture pending; empirical anti-TB therapy. Pre-adjudication hold_for_revision.

ANCHORING_EXTRAS: Anchored to Marais S et al. Lancet ID 2010 (PMID 20822958), TBM uniform case definition possible category. 29-year-old South African adult female HIV-negative informal-settlement resident, lymphocytic CSF, ADA 11 U/L, Xpert MTB/RIF Ultra NEGATIVE on initial specimen, culture pending, Marais score 9. Diagnostic ambiguity flag True. Pre-adjudication kappa 0.70.

ADJUDICATION:
  inclusion_decision: hold_for_revision  ground_truth_class: 4  kappa: 0.7
  adjudicator_ids: ['WAVE1-TBM-130-ADJ-1', 'WAVE1-TBM-130-ADJ-2']
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
