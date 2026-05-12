# AUDIT bundle: PMID 15494903 | Tunkel 2004

Generated: 2026-05-11
Vignettes in bundle: 10
Build status: NCBI fetched
Bundle type: BIG (n>=5 vignettes single-anchor)

## Anchor: PMID 15494903 | Tunkel 2004

### Registry metadata (current state)

```json
{
  "pmid": "15494903",
  "doi": "10.1086/425368",
  "authors_short": "Tunkel AR et al.",
  "authors_full": [
    "Tunkel AR",
    "Hartman BJ",
    "Kaplan SL",
    "Kaufman BA",
    "Roos KL",
    "Scheld WM",
    "Whitley RJ"
  ],
  "journal": "Clin Infect Dis",
  "journal_short_code": "CID",
  "year": 2004,
  "volume": "39",
  "issue": "9",
  "pages": "1267-1284",
  "title": "Practice guidelines for the management of bacterial meningitis",
  "anchor_type": "guideline",
  "anchor_subtype": "idsa_bacterial_meningitis_guidelines_2004",
  "verification_confidence": 0.85,
  "verification_method": "consensus_anchor_subphase_1_3_initial",
  "last_verified_date": "2026-05-06",
  "caveat": "IDSA bacterial meningitis management guidelines (Tunkel 2004). Canonical reference for empiric therapy decisions, CSF profile thresholds, and prognostic indicators in Class 2 vignettes. Anchor for guideline-imputed Class 2 entries where exact case demographic is sampled from IDSA recommended-empiric-therapy patient profiles. verification_confidence=0.85 pre-direct-fetch."
}
```

### NCBI live re-fetch (2026-05-11)

```json
{
  "uid": "15494903",
  "pubdate": "2004 Nov 1",
  "epubdate": "2004 Oct 6",
  "source": "Clin Infect Dis",
  "authors": [
    {
      "name": "Tunkel AR",
      "authtype": "Author",
      "clusterid": ""
    },
    {
      "name": "Hartman BJ",
      "authtype": "Author",
      "clusterid": ""
    },
    {
      "name": "Kaplan SL",
      "authtype": "Author",
      "clusterid": ""
    },
    {
      "name": "Kaufman BA",
      "authtype": "Author",
      "clusterid": ""
    },
    {
      "name": "Roos KL",
      "authtype": "Author",
      "clusterid": ""
    },
    {
      "name": "Scheld WM",
      "authtype": "Author",
      "clusterid": ""
    },
    {
      "name": "Whitley RJ",
      "authtype": "Author",
      "clusterid": ""
    }
  ],
  "lastauthor": "Whitley RJ",
  "title": "Practice guidelines for the management of bacterial meningitis.",
  "sorttitle": "practice guidelines for the management of bacterial meningitis",
  "volume": "39",
  "issue": "9",
  "pages": "1267-84",
  "lang": [
    "eng"
  ],
  "nlmuniqueid": "9203213",
  "issn": "1058-4838",
  "essn": "1537-6591",
  "pubtype": [
    "Journal Article",
    "Practice Guideline",
    "Research Support, Non-U.S. Gov't"
  ],
  "recordstatus": "PubMed - indexed for MEDLINE",
  "pubstatus": "256",
  "articleids": [
    {
      "idtype": "pubmed",
      "idtypen": 1,
      "value": "15494903"
    },
    {
      "idtype": "doi",
      "idtypen": 3,
      "value": "10.1086/425368"
    },
    {
      "idtype": "pii",
      "idtypen": 4,
      "value": "CID34796"
    }
  ],
  "history": [
    {
      "pubstatus": "received",
      "date": "2004/08/20 00:00"
    },
    {
      "pubstatus": "accepted",
      "date": "2004/08/25 00:00"
    },
    {
      "pubstatus": "pubmed",
      "date": "2004/10/21 09:00"
    },
    {
      "pubstatus": "medline",
      "date": "2006/10/13 09:00"
    },
    {
      "pubstatus": "entrez",
      "date": "2004/10/21 09:00"
    }
  ],
  "references": [
    {
      "refsource": "Clin Infect Dis. 2005 Apr 1;40(7):1061-2; author reply 1062-3. doi: 10.1086/428670.",
      "reftype": "Comment in",
      "pmid": 15825003,
      "note": ""
    },
    {
      "refsource": "Clin Infect Dis. 2005 Apr 1;40(7):1061; author reply 1062-3. doi: 10.1086/428668.",
      "reftype": "Comment in",
      "pmid": 15825004,
      "note": ""
    }
  ],
  "attributes": [],
  "pmcrefcount": "",
  "fulljournalname": "Clinical infectious diseases : an official publication of the Infectious Diseases Society of America",
  "elocationid": "",
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
  "sortpubdate": "2004/11/01 00:00",
  "sortfirstauthor": "Tunkel AR",
  "vernaculartitle": ""
}
```

### Registry-vs-NCBI delta

- **pages**: registry='1267-1284' | ncbi='1267-84'

### Vignettes citing this anchor (10 total)

#### Vignette: vid=065 file=bact_065_sp_asplenia.json class=2 subphase=1.3 BACT

```
ANCHOR:
  pmid: 15494903
  first_author: Tunkel
  year: 2004
  journal: CID
  citation_type: guideline
  doi: 10.1086/425368

DEMOGRAPHICS:
  age_years: 28  sex: male  region: us_south
  ethnicity: white_non_hispanic  altitude_m: 100
  hiv_status: negative  cd4: None
  pregnancy_red_flag: False
  immunocompromise_status: none
  freshwater_exposure_14d: False (None)

HISTORY:
  symptom_onset_to_presentation_days: 1.5
  chief_complaint: fever_with_headache
  red_flags_present: []
  prodrome_description: 28-year-old male, US South region, post-traumatic splenectomy 6 years prior. 36-hour rapid progression: fever 39.4 C, severe headache, neck stiffness, vomiting. Tertiary ED. No freshwater. Asplenia raises encapsulated-organism risk per IDSA. Outcome: survived no sequelae. Antibiotic at hour 1 plus dexamethasone.

VITALS:
  T:39.4C HR:118 BP:122/76 GCS:12 SpO2:96% RR:22

EXAM:
  mental_status: somnolent  neck_stiff: True  kernig_brudz: True
  cranial_nerve_palsy: none  papilledema: False  focal_deficit: False
  skin_lesion_centrofacial_chronic: False  rash: False

LABS:
  WBC:22000 Plt:280000 ALT/AST:30 CRP:195.0 PCT:9.2 Na:137

CSF:
  OP:32.0cmH2O  WBC:6800/mm3  lymph%:8 neut%:92 eos%:0
  glucose:18mg/dL protein:250mg/dL lactate:7.4mmol/L ADA:NoneU/L
  crag_lfa:negative  wet_mount:negative  xanthochromia:False  RBC:6

IMAGING:
  modality: ct_noncontrast  pattern: normal
  finding_count: 0
  text_summary: CT head non-contrast: normal at admission. No focal lesion, no hydrocephalus, no midline shift, no mass effect. Pattern consistent with early-stage adult community-acquired bacterial meningitis.

DIAGNOSTIC_TESTS:
  total_results: 3
  pcr_panel: n/a
  xpert_mtb_rif: n/a
  blood_culture: n/a
  csf_culture: n/a
  serology_or_antigen: n/a
  smear_or_gram: n/a
  brain_biopsy: n/a

NARRATIVE_EN: A 28-year-old man in the US South region presented to a tertiary emergency department with a 36-hour rapid progression of fever to 39.4 C, severe headache, neck stiffness, and vomiting. He was post-splenectomy six years prior following a motor vehicle accident. Examination on admission: temperature 39.4 C, Glasgow Coma Scale 12, neck stiffness, positive Kernig sign, no focal deficit, no rash. CSF showed opening pressure 32 cmH2O, white cell count 6,800 per cubic millimeter (92 percent neutrophils), glucose 18 mg/dL, protein 250 mg/dL. Gram stain revealed gram-positive diplococci; culture identified Streptococcus pneumoniae. Anchored to Tunkel IDSA 2004 (PMID 15494903) recommendations for suspected pneumococcal meningitis with asplenia risk factor. Outcome: survived no sequelae. Subphase 1.3 commit 5.3.3 wave 1, pre-adjudication hold_for_revision.

NARRATIVE_ES: Varon de 28 anos en region sur de Estados Unidos, ingresado a urgencias terciarias con 36 horas de progresion rapida: fiebre 39.4 C, cefalea intensa, rigidez de nuca, vomitos. Esplenectomia traumatica seis anos antes (accidente vial). Examen: temperatura 39.4 C, escala de Glasgow 12, rigidez de nuca, signo de Kernig positivo, sin deficit focal, sin exantema. Liquido cefalorraquideo mostro presion de apertura 32 cmH2O, leucocitos 6,800 por mm3 (92 por ciento neutrofilos), glucosa 18 mg/dL, proteina 250 mg/dL. Tincion de Gram con diplococos grampositivos y cultivo Streptococcus pneumoniae. Anclaje en guia IDSA Tunkel 2004 (PMID 15494903) para meningitis neumococica con asplenia. Subphase 1.3 commit 5.3.3 wave 1.

RATIONALE: Anchored to PMID 15494903 (Tunkel IDSA 2004 CID guideline). Demographic anchor (28yo M asplenic) reflects the encapsulated-organism risk stratum referenced by Tunkel as a covered indication for empiric vancomycin plus ceftriaxone. CSF profile bacterial range per guideline cutoffs. Imputation tiers: tier_1_primary={csf_culture, csf_gram_stain, age, sex, asplenia risk factor}; tier_3_within_cohort={csf_wbc, neutrophil_pct, glucose, protein}; tier_4_priors={temp, gcs, symptom_days}. Indeterminate=none. Diagnostic_ambiguity=false. Outcome=survived_no_sequelae. Antibiotic_started_hours=1. Tier: tier_4_imputation_idsa_guideline_anchored. 5.3.3 wave1 SP-asplenia.

ANCHORING_EXTRAS: stage=pre_adjudication; status=pending_external_review; self_review_disposition=hold_for_revision; self_review_notes=wave 1 vignette anchored to PMID 15494903 (Tunkel IDSA 2004); external clinical adjudication pending; classification provisional. adjudicator_ids=WAVE1-PRE-ADJ-1, WAVE1-PRE-ADJ-2 (sentinel); cohen_kappa=0.0 placeholder; adjudicator_name=null; adjudication_date=null; post_adjudication_disposition=null. Subphase 1.3 commit 5.3.3 (2026-05-08). anchor=Tunkel-IDSA-2004 risk_factor=asplenia.

ADJUDICATION:
  inclusion_decision: hold_for_revision  ground_truth_class: 2  kappa: 0.0
  adjudicator_ids: ['WAVE1-PRE-ADJ-1', 'WAVE1-PRE-ADJ-2']
  disagreement_resolution: None
```

#### Vignette: vid=067 file=bact_067_sp_pediatric.json class=2 subphase=1.3 BACT

```
ANCHOR:
  pmid: 15494903
  first_author: Tunkel
  year: 2004
  journal: CID
  citation_type: guideline
  doi: 10.1086/425368

DEMOGRAPHICS:
  age_years: 3  sex: male  region: us_south
  ethnicity: white_non_hispanic  altitude_m: 100
  hiv_status: negative  cd4: None
  pregnancy_red_flag: False
  immunocompromise_status: none
  freshwater_exposure_14d: False (None)

HISTORY:
  symptom_onset_to_presentation_days: 1.5
  chief_complaint: altered_mental_status
  red_flags_present: []
  prodrome_description: Three-year-old male, US South region. 36-hour fever 39.6 C, vomiting, irritability progressing to lethargy. Recent otitis media. Tertiary pediatric ED. No freshwater. Outcome: survived with mild hearing loss. Antibiotic at hour 1.5 plus dexamethasone per IDSA pediatric protocol.

VITALS:
  T:39.6C HR:148 BP:100/60 GCS:12 SpO2:95% RR:30

EXAM:
  mental_status: confused  neck_stiff: True  kernig_brudz: True
  cranial_nerve_palsy: none  papilledema: None  focal_deficit: False
  skin_lesion_centrofacial_chronic: False  rash: False

LABS:
  WBC:23500 Plt:295000 ALT/AST:26 CRP:185.0 PCT:8.8 Na:136

CSF:
  OP:30.0cmH2O  WBC:7200/mm3  lymph%:10 neut%:90 eos%:0
  glucose:20mg/dL protein:240mg/dL lactate:7.2mmol/L ADA:NoneU/L
  crag_lfa:negative  wet_mount:negative  xanthochromia:False  RBC:4

IMAGING:
  modality: ct_noncontrast  pattern: normal
  finding_count: 0
  text_summary: CT head non-contrast: normal at admission. No focal lesion, no hydrocephalus, no midline shift, no mass effect. Pattern consistent with early-stage adult community-acquired bacterial meningitis.

DIAGNOSTIC_TESTS:
  total_results: 3
  pcr_panel: n/a
  xpert_mtb_rif: n/a
  blood_culture: n/a
  csf_culture: n/a
  serology_or_antigen: n/a
  smear_or_gram: n/a
  brain_biopsy: n/a

NARRATIVE_EN: A three-year-old boy in the US South region presented to a tertiary pediatric emergency department with a 36-hour history of fever to 39.6 C, vomiting, irritability, and decreasing responsiveness. He had been treated for otitis media in the preceding week. Examination on admission: temperature 39.6 C, Glasgow Coma Scale 12, neck stiffness, positive Kernig sign, no focal deficit, no rash. CSF showed opening pressure 30 cmH2O, white cell count 7,200 per cubic millimeter (90 percent neutrophils), glucose 20 mg/dL, protein 240 mg/dL. Gram stain revealed gram-positive diplococci; culture identified Streptococcus pneumoniae. Anchored to Tunkel IDSA 2004 (PMID 15494903) pediatric pneumococcal meningitis recommendations. Outcome: survived with mild hearing loss. Subphase 1.3 commit 5.3.3 wave 1, pre-adjudication hold_for_revision.

NARRATIVE_ES: Varon de tres anos en region sur de Estados Unidos, ingresado a urgencias pediatricas terciarias con 36 horas de fiebre 39.6 C, vomitos, irritabilidad y respuesta disminuida. Tratamiento previo para otitis media en la semana anterior. Examen: temperatura 39.6 C, escala de Glasgow 12, rigidez de nuca, signo de Kernig positivo, sin deficit focal, sin exantema. Liquido cefalorraquideo mostro presion de apertura 30 cmH2O, leucocitos 7,200 por mm3 (90 por ciento neutrofilos), glucosa 20 mg/dL, proteina 240 mg/dL. Tincion de Gram con diplococos grampositivos y cultivo Streptococcus pneumoniae. Anclaje en guia IDSA Tunkel 2004 (PMID 15494903), recomendaciones pediatricas. Subphase 1.3 commit 5.3.3 wave 1.

RATIONALE: Anchored to PMID 15494903 (Tunkel IDSA 2004 CID guideline) for pediatric pneumococcal meningitis empiric coverage. Demographic anchor (3yo M post-otitis-media) sits in the high-risk pediatric stratum referenced by Tunkel. CSF profile bacterial range per guideline cutoffs. Imputation tiers: tier_1_primary={age, sex, csf_culture, csf_gram_stain}; tier_3_within_cohort={csf_wbc, neutrophil_pct, glucose, protein}; tier_4_priors={temp, gcs, symptom_days, hr}. Indeterminate=papilledema. Diagnostic_ambiguity=false. Outcome=survived_mild_hearing_loss. Antibiotic_started_hours=1.5. Tier: tier_4_imputation_idsa_guideline_anchored. 5.3.3 wave1 SP-pediatric.

ANCHORING_EXTRAS: stage=pre_adjudication; status=pending_external_review; self_review_disposition=hold_for_revision; self_review_notes=wave 1 vignette anchored to PMID 15494903 (Tunkel IDSA 2004); external clinical adjudication pending; classification provisional. adjudicator_ids=WAVE1-PRE-ADJ-1, WAVE1-PRE-ADJ-2 (sentinel); cohen_kappa=0.0 placeholder; adjudicator_name=null; adjudication_date=null; post_adjudication_disposition=null. Subphase 1.3 commit 5.3.3 (2026-05-08). anchor=Tunkel-IDSA-2004 stratum=pediatric.

ADJUDICATION:
  inclusion_decision: hold_for_revision  ground_truth_class: 2  kappa: 0.0
  adjudicator_ids: ['WAVE1-PRE-ADJ-1', 'WAVE1-PRE-ADJ-2']
  disagreement_resolution: None
```

#### Vignette: vid=069 file=bact_069_sp_recurrent_csf_leak.json class=2 subphase=1.3 BACT

```
ANCHOR:
  pmid: 15494903
  first_author: Tunkel
  year: 2004
  journal: CID
  citation_type: guideline
  doi: 10.1086/425368

DEMOGRAPHICS:
  age_years: 19  sex: male  region: us_south
  ethnicity: white_non_hispanic  altitude_m: 100
  hiv_status: negative  cd4: None
  pregnancy_red_flag: False
  immunocompromise_status: none
  freshwater_exposure_14d: False (None)

HISTORY:
  symptom_onset_to_presentation_days: 2.0
  chief_complaint: fever_with_headache
  red_flags_present: []
  prodrome_description: 19-year-old male, US South region. Skull-base fracture with CSF rhinorrhea 3 years prior (motor vehicle accident); not surgically corrected. Second meningitis episode: 2-day fever 39.2 C, headache, neck stiffness. Tertiary ED. No freshwater. Outcome: survived. Antibiotic at hour 2 plus dexamethasone.

VITALS:
  T:39.2C HR:110 BP:124/74 GCS:13 SpO2:96% RR:22

EXAM:
  mental_status: confused  neck_stiff: True  kernig_brudz: True
  cranial_nerve_palsy: none  papilledema: False  focal_deficit: False
  skin_lesion_centrofacial_chronic: False  rash: False

LABS:
  WBC:17500 Plt:250000 ALT/AST:28 CRP:145.0 PCT:5.5 Na:137

CSF:
  OP:26.0cmH2O  WBC:4200/mm3  lymph%:15 neut%:85 eos%:0
  glucose:25mg/dL protein:180mg/dL lactate:5.5mmol/L ADA:NoneU/L
  crag_lfa:negative  wet_mount:negative  xanthochromia:False  RBC:6

IMAGING:
  modality: ct_noncontrast  pattern: normal
  finding_count: 0
  text_summary: CT head non-contrast: normal at admission. No focal lesion, no hydrocephalus, no midline shift, no mass effect. Pattern consistent with early-stage adult community-acquired bacterial meningitis.

DIAGNOSTIC_TESTS:
  total_results: 3
  pcr_panel: n/a
  xpert_mtb_rif: n/a
  blood_culture: n/a
  csf_culture: n/a
  serology_or_antigen: n/a
  smear_or_gram: n/a
  brain_biopsy: n/a

NARRATIVE_EN: A 19-year-old man in the US South region presented to a tertiary emergency department with a 2-day history of fever to 39.2 C, headache, and neck stiffness. He had a skull-base fracture with CSF rhinorrhea three years prior following a motor vehicle accident that had not been surgically corrected; this was his second episode of bacterial meningitis. Examination on admission: temperature 39.2 C, Glasgow Coma Scale 13, neck stiffness, positive Kernig sign, no focal deficit, no rash. CSF showed opening pressure 26 cmH2O, white cell count 4,200 per cubic millimeter (85 percent neutrophils), glucose 25 mg/dL, protein 180 mg/dL. Gram stain revealed gram-positive diplococci; culture identified Streptococcus pneumoniae. Anchored to Tunkel IDSA 2004 (PMID 15494903) recurrent SP meningitis recommendations. Outcome: survived. Subphase 1.3 commit 5.3.3 wave 1, pre-adjudication hold_for_revision.

NARRATIVE_ES: Varon de 19 anos en region sur de Estados Unidos, ingresado a urgencias terciarias con dos dias de fiebre 39.2 C, cefalea y rigidez de nuca. Antecedente de fractura de base de craneo con rinorrea de liquido cefalorraquideo tres anos antes (no corregida quirurgicamente); segundo episodio de meningitis bacteriana. Examen: temperatura 39.2 C, escala de Glasgow 13, rigidez de nuca, signo de Kernig positivo, sin deficit focal, sin exantema. Liquido cefalorraquideo mostro presion de apertura 26 cmH2O, leucocitos 4,200 por mm3 (85 por ciento neutrofilos), glucosa 25 mg/dL, proteina 180 mg/dL. Tincion de Gram con diplococos grampositivos y cultivo Streptococcus pneumoniae. Anclaje en guia IDSA Tunkel 2004 (PMID 15494903). Subphase 1.3 commit 5.3.3 wave 1.

RATIONALE: Anchored to PMID 15494903 (Tunkel IDSA 2004 CID guideline) recurrent SP meningitis recommendations. Anatomic CSF rhinorrhea raises recurrent-SP risk per guideline. Demographic anchor (19yo M with anatomic CSF leak) reflects the recurrent-meningitis stratum. CSF profile bacterial range. Imputation tiers: tier_1_primary={age, sex, csf_culture, csf_gram_stain, anatomic_leak history}; tier_3_within_cohort={csf_wbc, neutrophil_pct, glucose, protein}; tier_4_priors={temp, gcs, symptom_days}. Indeterminate=none. Diagnostic_ambiguity=false. Outcome=survived. Antibiotic_started_hours=2. Tier: tier_4_imputation_idsa_guideline_anchored. 5.3.3 wave1 SP-recurrent-CSF-leak.

ANCHORING_EXTRAS: stage=pre_adjudication; status=pending_external_review; self_review_disposition=hold_for_revision; self_review_notes=wave 1 vignette anchored to PMID 15494903 (Tunkel IDSA 2004); external clinical adjudication pending; classification provisional. adjudicator_ids=WAVE1-PRE-ADJ-1, WAVE1-PRE-ADJ-2 (sentinel); cohen_kappa=0.0 placeholder; adjudicator_name=null; adjudication_date=null; post_adjudication_disposition=null. Subphase 1.3 commit 5.3.3 (2026-05-08). anchor=Tunkel-IDSA-2004 risk_factor=anatomic-CSF-leak.

ADJUDICATION:
  inclusion_decision: hold_for_revision  ground_truth_class: 2  kappa: 0.0
  adjudicator_ids: ['WAVE1-PRE-ADJ-1', 'WAVE1-PRE-ADJ-2']
  disagreement_resolution: None
```

#### Vignette: vid=071 file=bact_071_sp_lima_adult.json class=2 subphase=1.3 BACT

```
ANCHOR:
  pmid: 15494903
  first_author: Tunkel
  year: 2004
  journal: CID
  citation_type: guideline
  doi: 10.1086/425368

DEMOGRAPHICS:
  age_years: 38  sex: female  region: peru_lima_coast
  ethnicity: mestizo  altitude_m: 154
  hiv_status: negative  cd4: None
  pregnancy_red_flag: False
  immunocompromise_status: none
  freshwater_exposure_14d: False (None)

HISTORY:
  symptom_onset_to_presentation_days: 2.0
  chief_complaint: fever_with_headache
  red_flags_present: []
  prodrome_description: 38-year-old female, Lima Peru, presented to tertiary urban ED with 2-day fever 39.0 C, severe headache, neck stiffness, photophobia. No freshwater exposure. No rash. Empiric ceftriaxone-vancomycin started hour 1 plus dexamethasone per IDSA SP protocol. Outcome: survived no sequelae.

VITALS:
  T:39.0C HR:108 BP:120/72 GCS:13 SpO2:97% RR:20

EXAM:
  mental_status: confused  neck_stiff: True  kernig_brudz: True
  cranial_nerve_palsy: none  papilledema: False  focal_deficit: False
  skin_lesion_centrofacial_chronic: False  rash: False

LABS:
  WBC:19200 Plt:245000 ALT/AST:32 CRP:165.0 PCT:6.3 Na:136

CSF:
  OP:28.0cmH2O  WBC:5800/mm3  lymph%:12 neut%:88 eos%:0
  glucose:22mg/dL protein:200mg/dL lactate:6.4mmol/L ADA:NoneU/L
  crag_lfa:negative  wet_mount:negative  xanthochromia:False  RBC:5

IMAGING:
  modality: ct_noncontrast  pattern: normal
  finding_count: 0
  text_summary: CT head non-contrast: normal at admission. No focal lesion, no hydrocephalus, no midline shift, no mass effect. Pattern consistent with early-stage adult community-acquired bacterial meningitis.

DIAGNOSTIC_TESTS:
  total_results: 3
  pcr_panel: n/a
  xpert_mtb_rif: n/a
  blood_culture: n/a
  csf_culture: n/a
  serology_or_antigen: n/a
  smear_or_gram: n/a
  brain_biopsy: n/a

NARRATIVE_EN: A 38-year-old woman in Lima, Peru presented to a tertiary urban emergency department with a 2-day history of fever to 39.0 C, severe headache, neck stiffness, and photophobia. Examination on admission: temperature 39.0 C, Glasgow Coma Scale 13, neck stiffness, positive Kernig sign, no focal deficit, no rash. CSF showed opening pressure 28 cmH2O, white cell count 5,800 per cubic millimeter (88 percent neutrophils), glucose 22 mg/dL, protein 200 mg/dL. Gram stain revealed gram-positive diplococci; culture identified Streptococcus pneumoniae. Anchored to Tunkel IDSA 2004 (PMID 15494903) for empiric ceftriaxone-vancomycin coverage of adult community-acquired pneumococcal meningitis. Outcome: survived no sequelae. Subphase 1.3 commit 5.3.3 wave 1, pre-adjudication hold_for_revision.

NARRATIVE_ES: Mujer de 38 anos en Lima, Peru, ingresada a urgencias terciarias con dos dias de fiebre 39.0 C, cefalea intensa, rigidez de nuca y fotofobia. Examen: temperatura 39.0 C, escala de Glasgow 13, rigidez de nuca, signo de Kernig positivo, sin deficit focal, sin exantema. Liquido cefalorraquideo mostro presion de apertura 28 cmH2O, leucocitos 5,800 por mm3 (88 por ciento neutrofilos), glucosa 22 mg/dL, proteina 200 mg/dL. Tincion de Gram con diplococos grampositivos y cultivo Streptococcus pneumoniae. Anclaje en guia IDSA Tunkel 2004 (PMID 15494903) para cobertura empirica con ceftriaxona-vancomicina mas dexametasona en meningitis neumococica del adulto adquirida en la comunidad. Geografia anclada a Peru (5/30 escenarios bacterianos de la distribucion 5.3.1 asignados a Peru). Resultado: sobrevivio sin secuelas. Subphase 1.3 commit 5.3.3 wave 1, pre-adjudicacion hold_for_revision.

RATIONALE: Anchored to PMID 15494903 (Tunkel IDSA 2004 CID guideline) for adult community-acquired pneumococcal meningitis empiric coverage. Peru-anchored geography (5/30 BACT slots assigned to Peru per 5.3.1 distribution lock). Demographic anchor (38yo F adult) sits in standard adult community stratum. CSF profile bacterial range. Imputation tiers: tier_1_primary={age, sex, region, csf_culture, csf_gram_stain}; tier_3_within_cohort={csf_wbc, neutrophil_pct, glucose, protein}; tier_4_priors={temp, gcs, symptom_days}. Indeterminate=none. Diagnostic_ambiguity=false. Outcome=survived. Antibiotic_started_hours=1. Tier: tier_4_imputation_idsa_guideline_anchored. 5.3.3 wave1 SP-Lima-adult.

ANCHORING_EXTRAS: stage=pre_adjudication; status=pending_external_review; self_review_disposition=hold_for_revision; self_review_notes=wave 1 vignette anchored to PMID 15494903 (Tunkel IDSA 2004); external clinical adjudication pending; classification provisional. adjudicator_ids=WAVE1-PRE-ADJ-1, WAVE1-PRE-ADJ-2 (sentinel); cohen_kappa=0.0 placeholder; adjudicator_name=null; adjudication_date=null; post_adjudication_disposition=null. Subphase 1.3 commit 5.3.3 (2026-05-08). anchor=Tunkel-IDSA-2004 region=Lima-Peru.

ADJUDICATION:
  inclusion_decision: hold_for_revision  ground_truth_class: 2  kappa: 0.0
  adjudicator_ids: ['WAVE1-PRE-ADJ-1', 'WAVE1-PRE-ADJ-2']
  disagreement_resolution: None
```

#### Vignette: vid=075 file=bact_075_sp_partial_treatment_ambiguity.json class=2 subphase=1.3 BACT

```
ANCHOR:
  pmid: 15494903
  first_author: Tunkel
  year: 2004
  journal: CID
  citation_type: guideline
  doi: 10.1086/425368

DEMOGRAPHICS:
  age_years: 25  sex: female  region: us_south
  ethnicity: white_non_hispanic  altitude_m: 100
  hiv_status: negative  cd4: None
  pregnancy_red_flag: False
  immunocompromise_status: none
  freshwater_exposure_14d: False (None)

HISTORY:
  symptom_onset_to_presentation_days: 1.5
  chief_complaint: fever_with_headache
  red_flags_present: []
  prodrome_description: 25-year-old female, US South region. Outpatient amoxicillin started 24 hours prior for sinusitis. Subsequent fever 39.0 C, headache, neck stiffness within 12 hours of pretreatment. Tertiary ED. No freshwater. Diagnostic_ambiguity=true; type=partial_antibiotic_pretreatment. Outcome: survived. IDSA pretreated-suspected protocol.

VITALS:
  T:39.0C HR:105 BP:116/72 GCS:14 SpO2:98% RR:20

EXAM:
  mental_status: somnolent  neck_stiff: True  kernig_brudz: True
  cranial_nerve_palsy: none  papilledema: False  focal_deficit: False
  skin_lesion_centrofacial_chronic: False  rash: False

LABS:
  WBC:14200 Plt:260000 ALT/AST:26 CRP:95.0 PCT:2.8 Na:138

CSF:
  OP:22.0cmH2O  WBC:1850/mm3  lymph%:35 neut%:65 eos%:0
  glucose:30mg/dL protein:165mg/dL lactate:4.2mmol/L ADA:NoneU/L
  crag_lfa:negative  wet_mount:negative  xanthochromia:False  RBC:4

IMAGING:
  modality: ct_noncontrast  pattern: normal
  finding_count: 0
  text_summary: CT head non-contrast: normal at admission. No focal lesion, no hydrocephalus, no midline shift, no mass effect. Pattern consistent with early-stage adult community-acquired bacterial meningitis.

DIAGNOSTIC_TESTS:
  total_results: 4
  pcr_panel: n/a
  xpert_mtb_rif: n/a
  blood_culture: n/a
  csf_culture: n/a
  serology_or_antigen: streptococcus_pneumoniae_positive
  smear_or_gram: n/a
  brain_biopsy: n/a

NARRATIVE_EN: A 25-year-old woman in the US South region presented to a tertiary emergency department with fever to 39.0 C, headache, and neck stiffness developing 12 hours after starting outpatient amoxicillin for presumed sinusitis (24 hours of pretreatment). Examination on admission: temperature 39.0 C, Glasgow Coma Scale 14, neck stiffness, positive Kernig sign, no focal deficit, no rash. CSF showed opening pressure 22 cmH2O, white cell count 1,850 per cubic millimeter (65 percent neutrophils), glucose 30 mg/dL, protein 165 mg/dL. Gram stain unrevealing; CSF and blood cultures sterile after partial antibiotic pretreatment; CSF pneumococcal antigen positive. Diagnostic_ambiguity=true; type=partial_antibiotic_pretreatment_sterile_cultures. Anchored to Tunkel IDSA 2004 (PMID 15494903) pretreated-meningitis recommendations. Outcome: survived no sequelae. Subphase 1.3 commit 5.3.3 wave 1, pre-adjudication hold_for_revision.

NARRATIVE_ES: Mujer de 25 anos en region sur de Estados Unidos, ingresada a urgencias terciarias con fiebre 39.0 C, cefalea y rigidez de nuca 12 horas despues de iniciar amoxicilina ambulatoria por sinusitis presunta (24 horas de pretratamiento). Examen: temperatura 39.0 C, escala de Glasgow 14, rigidez de nuca, signo de Kernig positivo, sin deficit focal, sin exantema. Liquido cefalorraquideo mostro presion de apertura 22 cmH2O, leucocitos 1,850 por mm3 (65 por ciento neutrofilos), glucosa 30 mg/dL, proteina 165 mg/dL. Tincion de Gram sin organismos; cultivos de liquido y sangre esteriles tras pretratamiento antibiotico parcial; antigeno neumococico en liquido positivo. Ambiguedad diagnostica por pretratamiento parcial. Anclaje en guia IDSA Tunkel 2004 (PMID 15494903). Subphase 1.3 commit 5.3.3 wave 1.

RATIONALE: Anchored to PMID 15494903 (Tunkel IDSA 2004 CID guideline) pretreated-suspected meningitis recommendations. Diagnostic_ambiguity=true; type=partial_antibiotic_pretreatment_sterile_cultures. Demographic anchor (25yo F outpatient pretreated) reflects ambiguity stratum. CSF profile attenuated (WBC 1850, neutrophil 65 percent) consistent with partial treatment. Antigen confirms organism. Imputation tiers: tier_1_primary={age, sex, csf_pneumococcal_antigen, pretreatment_history}; tier_3_within_cohort={csf_wbc, neutrophil_pct, glucose, protein attenuation}; tier_4_priors={temp, gcs, symptom_days}. Indeterminate=culture-based-organism-confirmation. Outcome=survived. Antibiotic_started_hours=1. Tier: tier_4_imputation_idsa_guideline_anchored. 5.3.3 wave1 SP-pretreated-ambiguity.

ANCHORING_EXTRAS: stage=pre_adjudication; status=pending_external_review; self_review_disposition=hold_for_revision; self_review_notes=wave 1 vignette anchored to PMID 15494903 (Tunkel IDSA 2004); external clinical adjudication pending; classification provisional. adjudicator_ids=WAVE1-PRE-ADJ-1, WAVE1-PRE-ADJ-2 (sentinel); cohen_kappa=0.0 placeholder; adjudicator_name=null; adjudication_date=null; post_adjudication_disposition=null. Subphase 1.3 commit 5.3.3 (2026-05-08). anchor=Tunkel-IDSA-2004 type=partial_antibiotic_pretreatment.

ADJUDICATION:
  inclusion_decision: hold_for_revision  ground_truth_class: 2  kappa: 0.0
  adjudicator_ids: ['WAVE1-PRE-ADJ-1', 'WAVE1-PRE-ADJ-2']
  disagreement_resolution: None
```

#### Vignette: vid=076 file=bact_076_sp_partial_treatment_ambiguity.json class=2 subphase=1.3 BACT

```
ANCHOR:
  pmid: 15494903
  first_author: Tunkel
  year: 2004
  journal: CID
  citation_type: guideline
  doi: 10.1086/425368

DEMOGRAPHICS:
  age_years: 60  sex: male  region: other_global
  ethnicity: white_non_hispanic  altitude_m: 5
  hiv_status: negative  cd4: None
  pregnancy_red_flag: False
  immunocompromise_status: none
  freshwater_exposure_14d: False (None)

HISTORY:
  symptom_onset_to_presentation_days: 2.0
  chief_complaint: fever_with_headache
  red_flags_present: []
  prodrome_description: 60-year-old male, Netherlands. Outpatient amoxicillin 48 hours for productive cough; symptom recrudescence with fever 38.7 C, headache, neck stiffness. Tertiary ED. No freshwater. Diagnostic_ambiguity=true; type=partial_antibiotic_pretreatment. Outcome: survived. Ceftriaxone-vancomycin-dexamethasone IDSA.

VITALS:
  T:38.7C HR:102 BP:130/78 GCS:14 SpO2:96% RR:20

EXAM:
  mental_status: somnolent  neck_stiff: True  kernig_brudz: True
  cranial_nerve_palsy: none  papilledema: False  focal_deficit: False
  skin_lesion_centrofacial_chronic: False  rash: False

LABS:
  WBC:13500 Plt:240000 ALT/AST:32 CRP:78.0 PCT:1.9 Na:137

CSF:
  OP:24.0cmH2O  WBC:2400/mm3  lymph%:30 neut%:70 eos%:0
  glucose:26mg/dL protein:180mg/dL lactate:4.6mmol/L ADA:NoneU/L
  crag_lfa:negative  wet_mount:negative  xanthochromia:False  RBC:3

IMAGING:
  modality: ct_noncontrast  pattern: normal
  finding_count: 0
  text_summary: CT head non-contrast: normal at admission. No focal lesion, no hydrocephalus, no midline shift, no mass effect. Pattern consistent with early-stage adult community-acquired bacterial meningitis.

DIAGNOSTIC_TESTS:
  total_results: 4
  pcr_panel: n/a
  xpert_mtb_rif: n/a
  blood_culture: n/a
  csf_culture: n/a
  serology_or_antigen: streptococcus_pneumoniae_positive
  smear_or_gram: n/a
  brain_biopsy: n/a

NARRATIVE_EN: A 60-year-old man in the Netherlands presented to a tertiary emergency department after 48 hours of outpatient amoxicillin for a productive cough, with recrudescence of symptoms (fever 38.7 C, headache, neck stiffness). Examination on admission: temperature 38.7 C, Glasgow Coma Scale 14, neck stiffness, positive Kernig sign, no focal deficit, no rash. CSF showed opening pressure 24 cmH2O, white cell count 2,400 per cubic millimeter (70 percent neutrophils), glucose 26 mg/dL, protein 180 mg/dL. Gram stain unrevealing; cultures sterile after partial antibiotic pretreatment; CSF pneumococcal antigen positive. Diagnostic_ambiguity=true; type=partial_antibiotic_pretreatment_sterile_cultures. Anchored to Tunkel IDSA 2004 (PMID 15494903). Outcome: survived. Subphase 1.3 commit 5.3.3 wave 1, pre-adjudication hold_for_revision.

NARRATIVE_ES: Varon de 60 anos en Paises Bajos, ingresado a urgencias terciarias tras 48 horas de amoxicilina ambulatoria por tos productiva, con recrudescencia de sintomas (fiebre 38.7 C, cefalea, rigidez de nuca). Examen: temperatura 38.7 C, escala de Glasgow 14, rigidez de nuca, signo de Kernig positivo, sin deficit focal, sin exantema. Liquido cefalorraquideo mostro presion de apertura 24 cmH2O, leucocitos 2,400 por mm3 (70 por ciento neutrofilos), glucosa 26 mg/dL, proteina 180 mg/dL. Cultivos esteriles tras pretratamiento antibiotico parcial; antigeno neumococico en liquido positivo. Ambiguedad diagnostica por pretratamiento parcial. Anclaje en guia IDSA Tunkel 2004 (PMID 15494903). Subphase 1.3 commit 5.3.3 wave 1.

RATIONALE: Anchored to PMID 15494903 (Tunkel IDSA 2004 CID guideline) pretreated-suspected meningitis recommendations. Diagnostic_ambiguity=true; type=partial_antibiotic_pretreatment_sterile_cultures. Demographic anchor (60yo M outpatient pretreated). CSF profile attenuated (WBC 2400, neutrophil 70 percent). Antigen confirms organism. Imputation tiers: tier_1_primary={age, sex, csf_pneumococcal_antigen, pretreatment_history}; tier_3_within_cohort={csf_wbc, neutrophil_pct, glucose, protein attenuation}; tier_4_priors={temp, gcs, symptom_days}. Indeterminate=culture-based-organism-confirmation. Outcome=survived. Tier: tier_4_imputation_idsa_guideline_anchored. 5.3.3 wave1 SP-pretreated-ambiguity NL.

ANCHORING_EXTRAS: stage=pre_adjudication; status=pending_external_review; self_review_disposition=hold_for_revision; self_review_notes=wave 1 vignette anchored to PMID 15494903 (Tunkel IDSA 2004); external clinical adjudication pending; classification provisional. adjudicator_ids=WAVE1-PRE-ADJ-1, WAVE1-PRE-ADJ-2 (sentinel); cohen_kappa=0.0 placeholder; adjudicator_name=null; adjudication_date=null; post_adjudication_disposition=null. Subphase 1.3 commit 5.3.3 (2026-05-08). anchor=Tunkel-IDSA-2004 type=partial_antibiotic_pretreatment.

ADJUDICATION:
  inclusion_decision: hold_for_revision  ground_truth_class: 2  kappa: 0.0
  adjudicator_ids: ['WAVE1-PRE-ADJ-1', 'WAVE1-PRE-ADJ-2']
  disagreement_resolution: None
```

#### Vignette: vid=078 file=bact_078_sp_hiv_immunocompromised.json class=2 subphase=1.3 BACT

```
ANCHOR:
  pmid: 15494903
  first_author: Tunkel
  year: 2004
  journal: CID
  citation_type: guideline
  doi: 10.1086/425368

DEMOGRAPHICS:
  age_years: 50  sex: male  region: us_south
  ethnicity: white_non_hispanic  altitude_m: 100
  hiv_status: positive_on_art  cd4: 285
  pregnancy_red_flag: False
  immunocompromise_status: hiv_cd4_over200
  freshwater_exposure_14d: False (None)

HISTORY:
  symptom_onset_to_presentation_days: 2.0
  chief_complaint: fever_with_headache
  red_flags_present: ['immunocompromise']
  prodrome_description: 50-year-old male, US South region. HIV-positive 8 years on antiretroviral therapy (CD4 285). 2-day fever 39.2 C, severe headache, neck stiffness. Tertiary ED. No freshwater. Encapsulated-organism risk per HIV. Outcome: survived. Ceftriaxone-vancomycin-dexamethasone IDSA HIV-specific.

VITALS:
  T:39.2C HR:112 BP:118/72 GCS:13 SpO2:97% RR:22

EXAM:
  mental_status: confused  neck_stiff: True  kernig_brudz: True
  cranial_nerve_palsy: none  papilledema: False  focal_deficit: False
  skin_lesion_centrofacial_chronic: False  rash: False

LABS:
  WBC:18200 Plt:235000 ALT/AST:30 CRP:175.0 PCT:7.0 Na:137

CSF:
  OP:27.0cmH2O  WBC:5200/mm3  lymph%:15 neut%:85 eos%:0
  glucose:22mg/dL protein:195mg/dL lactate:6.0mmol/L ADA:NoneU/L
  crag_lfa:negative  wet_mount:negative  xanthochromia:False  RBC:5

IMAGING:
  modality: ct_noncontrast  pattern: normal
  finding_count: 0
  text_summary: CT head non-contrast: normal at admission. No focal lesion, no hydrocephalus, no midline shift, no mass effect. Pattern consistent with early-stage adult community-acquired bacterial meningitis.

DIAGNOSTIC_TESTS:
  total_results: 3
  pcr_panel: n/a
  xpert_mtb_rif: n/a
  blood_culture: n/a
  csf_culture: n/a
  serology_or_antigen: n/a
  smear_or_gram: n/a
  brain_biopsy: n/a

NARRATIVE_EN: A 50-year-old man in the US South region with HIV (eight years on antiretroviral therapy, CD4 count 285 cells per microliter) presented to a tertiary emergency department with a 2-day history of fever to 39.2 C, severe headache, and neck stiffness. Examination on admission: temperature 39.2 C, Glasgow Coma Scale 13, neck stiffness, positive Kernig sign, no focal deficit, no rash. CSF showed opening pressure 27 cmH2O, white cell count 5,200 per cubic millimeter (85 percent neutrophils), glucose 22 mg/dL, protein 195 mg/dL; CSF cryptococcal antigen negative. Gram stain revealed gram-positive diplococci; culture identified Streptococcus pneumoniae. Anchored to Tunkel IDSA 2004 (PMID 15494903) HIV-specific empiric coverage recommendations. Outcome: survived. Subphase 1.3 commit 5.3.3 wave 1, pre-adjudication hold_for_revision.

NARRATIVE_ES: Varon de 50 anos en region sur de Estados Unidos con infeccion por VIH (ocho anos de terapia antirretroviral, CD4 285 celulas por microlitro), ingresado a urgencias terciarias con dos dias de fiebre 39.2 C, cefalea intensa y rigidez de nuca. Examen: temperatura 39.2 C, escala de Glasgow 13, rigidez de nuca, signo de Kernig positivo, sin deficit focal, sin exantema. Liquido cefalorraquideo mostro presion de apertura 27 cmH2O, leucocitos 5,200 por mm3 (85 por ciento neutrofilos), glucosa 22 mg/dL, proteina 195 mg/dL; antigeno criptococico en liquido negativo. Tincion de Gram con diplococos grampositivos y cultivo Streptococcus pneumoniae. Anclaje en guia IDSA Tunkel 2004 (PMID 15494903) recomendaciones VIH-especificas. Subphase 1.3 commit 5.3.3 wave 1.

RATIONALE: Anchored to PMID 15494903 (Tunkel IDSA 2004 CID guideline) HIV-specific empiric coverage recommendations. Demographic anchor (50yo M HIV+ ART CD4 285) reflects HIV-on-ART stratum covered by Tunkel for SP empiric vancomycin plus ceftriaxone. CrAg negative excludes co-incident cryptococcal infection. CSF profile bacterial range. Imputation tiers: tier_1_primary={age, sex, csf_culture, csf_gram_stain, hiv_status, cd4}; tier_3_within_cohort={csf_wbc, neutrophil_pct, glucose, protein}; tier_4_priors={temp, gcs, symptom_days}. Indeterminate=none. Diagnostic_ambiguity=false. Outcome=survived. Antibiotic_started_hours=1. Tier: tier_4_imputation_idsa_guideline_anchored. 5.3.3 wave1 SP-HIV-on-ART.

ANCHORING_EXTRAS: stage=pre_adjudication; status=pending_external_review; self_review_disposition=hold_for_revision; self_review_notes=wave 1 vignette anchored to PMID 15494903 (Tunkel IDSA 2004); external clinical adjudication pending; classification provisional. adjudicator_ids=WAVE1-PRE-ADJ-1, WAVE1-PRE-ADJ-2 (sentinel); cohen_kappa=0.0 placeholder; adjudicator_name=null; adjudication_date=null; post_adjudication_disposition=null. Subphase 1.3 commit 5.3.3 (2026-05-08). anchor=Tunkel-IDSA-2004 stratum=HIV-on-ART.

ADJUDICATION:
  inclusion_decision: hold_for_revision  ground_truth_class: 2  kappa: 0.0
  adjudicator_ids: ['WAVE1-PRE-ADJ-1', 'WAVE1-PRE-ADJ-2']
  disagreement_resolution: None
```

#### Vignette: vid=079 file=bact_079_sp_partial_treatment_ambiguity.json class=2 subphase=1.3 BACT

```
ANCHOR:
  pmid: 15494903
  first_author: Tunkel
  year: 2004
  journal: CID
  citation_type: guideline
  doi: 10.1086/425368

DEMOGRAPHICS:
  age_years: 45  sex: female  region: us_south
  ethnicity: white_non_hispanic  altitude_m: 100
  hiv_status: negative  cd4: None
  pregnancy_red_flag: False
  immunocompromise_status: none
  freshwater_exposure_14d: False (None)

HISTORY:
  symptom_onset_to_presentation_days: 1.5
  chief_complaint: fever_with_headache
  red_flags_present: []
  prodrome_description: 45-year-old female, US South region. Outpatient cefuroxime 36 hours for bronchitis. Recrudescence: fever 38.8 C, headache, neck stiffness. Tertiary ED. No freshwater. Diagnostic_ambiguity=true; type=partial_antibiotic_pretreatment. Outcome: survived. IDSA pretreated-suspected protocol followed.

VITALS:
  T:38.8C HR:100 BP:120/74 GCS:14 SpO2:98% RR:18

EXAM:
  mental_status: somnolent  neck_stiff: True  kernig_brudz: True
  cranial_nerve_palsy: none  papilledema: False  focal_deficit: False
  skin_lesion_centrofacial_chronic: False  rash: False

LABS:
  WBC:12800 Plt:245000 ALT/AST:28 CRP:70.0 PCT:1.5 Na:138

CSF:
  OP:20.0cmH2O  WBC:1600/mm3  lymph%:40 neut%:60 eos%:0
  glucose:32mg/dL protein:155mg/dL lactate:3.8mmol/L ADA:NoneU/L
  crag_lfa:negative  wet_mount:negative  xanthochromia:False  RBC:3

IMAGING:
  modality: ct_noncontrast  pattern: normal
  finding_count: 0
  text_summary: CT head non-contrast: normal at admission. No focal lesion, no hydrocephalus, no midline shift, no mass effect. Pattern consistent with early-stage adult community-acquired bacterial meningitis.

DIAGNOSTIC_TESTS:
  total_results: 4
  pcr_panel: n/a
  xpert_mtb_rif: n/a
  blood_culture: n/a
  csf_culture: n/a
  serology_or_antigen: streptococcus_pneumoniae_positive
  smear_or_gram: n/a
  brain_biopsy: n/a

NARRATIVE_EN: A 45-year-old woman in the US South region presented to a tertiary emergency department after 36 hours of outpatient cefuroxime for presumed bronchitis, with recrudescence of fever to 38.8 C, headache, and neck stiffness. Examination on admission: temperature 38.8 C, Glasgow Coma Scale 14, neck stiffness, positive Kernig sign, no focal deficit, no rash. CSF showed opening pressure 20 cmH2O, white cell count 1,600 per cubic millimeter (60 percent neutrophils), glucose 32 mg/dL, protein 155 mg/dL. Gram stain unrevealing; CSF and blood cultures sterile after partial antibiotic pretreatment; CSF pneumococcal antigen positive. Diagnostic_ambiguity=true; type=partial_antibiotic_pretreatment_sterile_cultures. Anchored to Tunkel IDSA 2004 (PMID 15494903) pretreated-meningitis recommendations. Outcome: survived. Subphase 1.3 commit 5.3.3 wave 1, pre-adjudication hold_for_revision.

NARRATIVE_ES: Mujer de 45 anos en region sur de Estados Unidos, ingresada a urgencias terciarias tras 36 horas de cefuroxima ambulatoria por bronquitis presunta, con recrudescencia de fiebre 38.8 C, cefalea y rigidez de nuca. Examen: temperatura 38.8 C, escala de Glasgow 14, rigidez de nuca, signo de Kernig positivo, sin deficit focal, sin exantema. Liquido cefalorraquideo mostro presion de apertura 20 cmH2O, leucocitos 1,600 por mm3 (60 por ciento neutrofilos), glucosa 32 mg/dL, proteina 155 mg/dL. Cultivos esteriles tras pretratamiento antibiotico parcial; antigeno neumococico en liquido positivo. Ambiguedad diagnostica por pretratamiento parcial. Anclaje en guia IDSA Tunkel 2004 (PMID 15494903). Subphase 1.3 commit 5.3.3 wave 1.

RATIONALE: Anchored to PMID 15494903 (Tunkel IDSA 2004 CID guideline) pretreated-suspected meningitis recommendations. Diagnostic_ambiguity=true; type=partial_antibiotic_pretreatment_sterile_cultures. Demographic anchor (45yo F outpatient pretreated). CSF profile attenuated (WBC 1600, neutrophil 60 percent, glucose 32). Antigen confirms organism. Imputation tiers: tier_1_primary={age, sex, csf_pneumococcal_antigen, pretreatment_history}; tier_3_within_cohort={csf_wbc, neutrophil_pct, glucose, protein attenuation}; tier_4_priors={temp, gcs, symptom_days}. Indeterminate=culture-based-organism-confirmation. Outcome=survived. Tier: tier_4_imputation_idsa_guideline_anchored. 5.3.3 wave1 SP-pretreated-ambiguity-2.

ANCHORING_EXTRAS: stage=pre_adjudication; status=pending_external_review; self_review_disposition=hold_for_revision; self_review_notes=wave 1 vignette anchored to PMID 15494903 (Tunkel IDSA 2004); external clinical adjudication pending; classification provisional. adjudicator_ids=WAVE1-PRE-ADJ-1, WAVE1-PRE-ADJ-2 (sentinel); cohen_kappa=0.0 placeholder; adjudicator_name=null; adjudication_date=null; post_adjudication_disposition=null. Subphase 1.3 commit 5.3.3 (2026-05-08). anchor=Tunkel-IDSA-2004 type=partial_antibiotic_pretreatment.

ADJUDICATION:
  inclusion_decision: hold_for_revision  ground_truth_class: 2  kappa: 0.0
  adjudicator_ids: ['WAVE1-PRE-ADJ-1', 'WAVE1-PRE-ADJ-2']
  disagreement_resolution: None
```

#### Vignette: vid=080 file=bact_080_sp_partial_treatment_ambiguity.json class=2 subphase=1.3 BACT

```
ANCHOR:
  pmid: 15494903
  first_author: Tunkel
  year: 2004
  journal: CID
  citation_type: guideline
  doi: 10.1086/425368

DEMOGRAPHICS:
  age_years: 33  sex: male  region: other_global
  ethnicity: white_non_hispanic  altitude_m: 5
  hiv_status: negative  cd4: None
  pregnancy_red_flag: False
  immunocompromise_status: none
  freshwater_exposure_14d: False (None)

HISTORY:
  symptom_onset_to_presentation_days: 1.5
  chief_complaint: fever_with_headache
  red_flags_present: []
  prodrome_description: 33-year-old male, Netherlands. Outpatient amoxicillin 30 hours for sinus pain. Recrudescence fever 38.9 C, headache, neck stiffness, vomiting. Tertiary ED. No freshwater. Diagnostic_ambiguity=true; type=partial_antibiotic_pretreatment. Outcome: survived. IDSA pretreated-suspected protocol.

VITALS:
  T:38.9C HR:108 BP:122/76 GCS:14 SpO2:97% RR:20

EXAM:
  mental_status: somnolent  neck_stiff: True  kernig_brudz: True
  cranial_nerve_palsy: none  papilledema: False  focal_deficit: False
  skin_lesion_centrofacial_chronic: False  rash: False

LABS:
  WBC:14500 Plt:255000 ALT/AST:30 CRP:85.0 PCT:2.3 Na:137

CSF:
  OP:23.0cmH2O  WBC:2900/mm3  lymph%:32 neut%:68 eos%:0
  glucose:28mg/dL protein:175mg/dL lactate:4.4mmol/L ADA:NoneU/L
  crag_lfa:negative  wet_mount:negative  xanthochromia:False  RBC:4

IMAGING:
  modality: ct_noncontrast  pattern: normal
  finding_count: 0
  text_summary: CT head non-contrast: normal at admission. No focal lesion, no hydrocephalus, no midline shift, no mass effect. Pattern consistent with early-stage adult community-acquired bacterial meningitis.

DIAGNOSTIC_TESTS:
  total_results: 4
  pcr_panel: n/a
  xpert_mtb_rif: n/a
  blood_culture: n/a
  csf_culture: n/a
  serology_or_antigen: streptococcus_pneumoniae_positive
  smear_or_gram: n/a
  brain_biopsy: n/a

NARRATIVE_EN: A 33-year-old man in the Netherlands presented to a tertiary emergency department after 30 hours of outpatient amoxicillin for sinus pain, with recrudescence of fever to 38.9 C, headache, neck stiffness, and vomiting. Examination on admission: temperature 38.9 C, Glasgow Coma Scale 14, neck stiffness, positive Kernig sign, no focal deficit, no rash. CSF showed opening pressure 23 cmH2O, white cell count 2,900 per cubic millimeter (68 percent neutrophils), glucose 28 mg/dL, protein 175 mg/dL. Gram stain unrevealing; cultures sterile after partial antibiotic pretreatment; CSF pneumococcal antigen positive. Diagnostic_ambiguity=true; type=partial_antibiotic_pretreatment_sterile_cultures. Anchored to Tunkel IDSA 2004 (PMID 15494903) pretreated-meningitis recommendations. Outcome: survived. Subphase 1.3 commit 5.3.3 wave 1, pre-adjudication hold_for_revision.

NARRATIVE_ES: Varon de 33 anos en Paises Bajos, ingresado a urgencias terciarias tras 30 horas de amoxicilina ambulatoria por dolor sinusal, con recrudescencia de fiebre 38.9 C, cefalea, rigidez de nuca y vomitos. Examen: temperatura 38.9 C, escala de Glasgow 14, rigidez de nuca, signo de Kernig positivo, sin deficit focal, sin exantema. Liquido cefalorraquideo mostro presion de apertura 23 cmH2O, leucocitos 2,900 por mm3 (68 por ciento neutrofilos), glucosa 28 mg/dL, proteina 175 mg/dL. Cultivos esteriles tras pretratamiento antibiotico parcial; antigeno neumococico en liquido positivo. Ambiguedad diagnostica por pretratamiento parcial. Anclaje en guia IDSA Tunkel 2004 (PMID 15494903). Subphase 1.3 commit 5.3.3 wave 1.

RATIONALE: Anchored to PMID 15494903 (Tunkel IDSA 2004 CID guideline) pretreated-suspected meningitis recommendations. Diagnostic_ambiguity=true; type=partial_antibiotic_pretreatment_sterile_cultures. Demographic anchor (33yo M outpatient pretreated NL). CSF profile attenuated (WBC 2900, neutrophil 68 percent, glucose 28). Antigen confirms organism. Imputation tiers: tier_1_primary={age, sex, csf_pneumococcal_antigen, pretreatment_history}; tier_3_within_cohort={csf_wbc, neutrophil_pct, glucose, protein attenuation}; tier_4_priors={temp, gcs, symptom_days}. Indeterminate=culture-based-organism-confirmation. Outcome=survived. Tier: tier_4_imputation_idsa_guideline_anchored. 5.3.3 wave1 SP-pretreated-ambiguity NL-2.

ANCHORING_EXTRAS: stage=pre_adjudication; status=pending_external_review; self_review_disposition=hold_for_revision; self_review_notes=wave 1 vignette anchored to PMID 15494903 (Tunkel IDSA 2004); external clinical adjudication pending; classification provisional. adjudicator_ids=WAVE1-PRE-ADJ-1, WAVE1-PRE-ADJ-2 (sentinel); cohen_kappa=0.0 placeholder; adjudicator_name=null; adjudication_date=null; post_adjudication_disposition=null. Subphase 1.3 commit 5.3.3 (2026-05-08). anchor=Tunkel-IDSA-2004 type=partial_antibiotic_pretreatment.

ADJUDICATION:
  inclusion_decision: hold_for_revision  ground_truth_class: 2  kappa: 0.0
  adjudicator_ids: ['WAVE1-PRE-ADJ-1', 'WAVE1-PRE-ADJ-2']
  disagreement_resolution: None
```

#### Vignette: vid=090 file=bact_090_gn_post_neurosurgical_fatal.json class=2 subphase=1.3 BACT

```
ANCHOR:
  pmid: 15494903
  first_author: Tunkel
  year: 2004
  journal: CID
  citation_type: guideline
  doi: 10.1086/425368

DEMOGRAPHICS:
  age_years: 55  sex: male  region: us_south
  ethnicity: white_non_hispanic  altitude_m: 100
  hiv_status: negative  cd4: None
  pregnancy_red_flag: False
  immunocompromise_status: none
  freshwater_exposure_14d: False (None)

HISTORY:
  symptom_onset_to_presentation_days: 1.5
  chief_complaint: altered_mental_status
  red_flags_present: ['recent_neurosurgery']
  prodrome_description: 55-year-old male, US South region. Glioma resection 9 days prior; postoperative course complicated by CSF leak from surgical site, then fever 39.0 C, headache, declining mental status over 36 hours, progressive obtundation. Tertiary ED. No freshwater. Healthcare-associated gram-negative bacterial meningitis. Outcome: fatal hospital day 4.

VITALS:
  T:39.0C HR:118 BP:100/60 GCS:8 SpO2:92% RR:24

EXAM:
  mental_status: stuporous  neck_stiff: True  kernig_brudz: True
  cranial_nerve_palsy: none  papilledema: False  focal_deficit: True
  skin_lesion_centrofacial_chronic: False  rash: False

LABS:
  WBC:19500 Plt:165000 ALT/AST:42 CRP:215.0 PCT:11.5 Na:135

CSF:
  OP:30.0cmH2O  WBC:4500/mm3  lymph%:14 neut%:86 eos%:0
  glucose:16mg/dL protein:290mg/dL lactate:8.2mmol/L ADA:NoneU/L
  crag_lfa:negative  wet_mount:negative  xanthochromia:False  RBC:8

IMAGING:
  modality: ct_noncontrast  pattern: diffuse_cerebral_edema_basilar_meningeal_enhancement
  finding_count: 1
  text_summary: CT head non-contrast: diffuse cerebral edema with effacement of sulci, basilar meningeal enhancement on contrast-equivalent regions, no focal lesion, no midline shift. Pattern consistent with severe late-stage bacterial meningitis.

DIAGNOSTIC_TESTS:
  total_results: 3
  pcr_panel: n/a
  xpert_mtb_rif: n/a
  blood_culture: n/a
  csf_culture: n/a
  serology_or_antigen: n/a
  smear_or_gram: n/a
  brain_biopsy: n/a

NARRATIVE_EN: A 55-year-old man in the US South region presented to a tertiary emergency department 9 days after glioma resection. The postoperative course had been complicated by a CSF leak at the surgical site. Over 36 hours he developed fever to 39.0 C, headache, and declining mental status with progressive obtundation. Examination on admission: temperature 39.0 C, Glasgow Coma Scale 8, neck stiffness, positive Kernig sign, focal deficit (right hemiparesis), no rash. CSF showed opening pressure 30 cmH2O, white cell count 4,500 per cubic millimeter (86 percent neutrophils), glucose 16 mg/dL, protein 290 mg/dL. Gram stain revealed gram-negative rods; culture identified Pseudomonas aeruginosa. Anchored to Tunkel IDSA 2004 (PMID 15494903) healthcare-associated meningitis recommendations (empiric meropenem coverage of gram-negative rods including Pseudomonas in post-neurosurgical context). Outcome: fatal hospital day 4. Subphase 1.3 commit 5.3.3 wave 1, pre-adjudication hold_for_revision.

NARRATIVE_ES: Varon de 55 anos en region sur de Estados Unidos, ingresado a urgencias terciarias nueve dias despues de reseccion de glioma. El curso postoperatorio se complico con fuga de liquido cefalorraquideo en el sitio quirurgico. En 36 horas desarrollo fiebre 39.0 C, cefalea y deterioro del estado mental con obnubilacion progresiva. Examen: temperatura 39.0 C, escala de Glasgow 8, rigidez de nuca, signo de Kernig positivo, deficit focal (hemiparesia derecha), sin exantema. Liquido cefalorraquideo mostro presion de apertura 30 cmH2O, leucocitos 4,500 por mm3 (86 por ciento neutrofilos), glucosa 16 mg/dL, proteina 290 mg/dL. Tincion de Gram con bacilos gramnegativos y cultivo Pseudomonas aeruginosa. Anclaje en guia IDSA Tunkel 2004 (PMID 15494903), recomendaciones para meningitis asociada a atencion sanitaria. Subphase 1.3 commit 5.3.3 wave 1.

RATIONALE: Anchored to PMID 15494903 (Tunkel IDSA 2004 CID guideline) healthcare-associated meningitis recommendations. Demographic anchor (55yo M post-neurosurgical glioma resection day 9 with CSF leak) reflects post-neurosurgical gram-negative stratum covered by Tunkel for empiric meropenem-vancomycin coverage. CSF profile bacterial range; gram-negative rods on Gram stain with Pseudomonas culture. Imputation tiers: tier_1_primary={age, sex, csf_culture, csf_gram_stain, neurosurgery_history, csf_leak}; tier_3_within_cohort={csf_wbc, neutrophil_pct, glucose, protein, lactate, gcs}; tier_4_priors={temp, symptom_days, hr}. Indeterminate=none. Diagnostic_ambiguity=false. Outcome=fatal_hospital_day_4. Antibiotic_started_hours=2. Tier: tier_4_imputation_idsa_guideline_anchored. 5.3.3 wave1 GN-post-neurosurgical-fatal.

ANCHORING_EXTRAS: stage=pre_adjudication; status=pending_external_review; self_review_disposition=hold_for_revision; self_review_notes=wave 1 vignette anchored to PMID 15494903 (Tunkel IDSA 2004); external clinical adjudication pending; classification provisional. adjudicator_ids=WAVE1-PRE-ADJ-1, WAVE1-PRE-ADJ-2 (sentinel); cohen_kappa=0.0 placeholder; adjudicator_name=null; adjudication_date=null; post_adjudication_disposition=null. Subphase 1.3 commit 5.3.3 (2026-05-08). anchor=Tunkel-IDSA-2004 stratum=post-neurosurgical-GN.

ADJUDICATION:
  inclusion_decision: hold_for_revision  ground_truth_class: 2  kappa: 0.0
  adjudicator_ids: ['WAVE1-PRE-ADJ-1', 'WAVE1-PRE-ADJ-2']
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
