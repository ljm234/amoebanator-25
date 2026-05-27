# AUDIT bundle: PMID 26652862 | Bijlsma 2016

Generated: 2026-05-11
Vignettes in bundle: 6
Build status: NCBI fetched
Bundle type: BIG (n>=5 vignettes single-anchor)

## Anchor: PMID 26652862 | Bijlsma 2016

### Registry metadata (current state)

```json
{
  "pmid": "26652862",
  "doi": "10.1016/S1473-3099(15)00430-2",
  "authors_short": "Bijlsma MW et al.",
  "authors_full": [
    "Bijlsma MW",
    "Brouwer MC",
    "Kasanmoentalib ES",
    "Kloek AT",
    "Lucas MJ",
    "Tanck MW",
    "van der Ende A",
    "van de Beek D"
  ],
  "journal": "Lancet Infect Dis",
  "journal_short_code": "Lancet Infect Dis",
  "year": 2016,
  "volume": "16",
  "issue": "3",
  "pages": "339-347",
  "title": "Community-acquired bacterial meningitis in adults in the Netherlands, 2006-14: a prospective cohort study",
  "anchor_type": "cohort",
  "anchor_subtype": "netherlands_pneumococcal_2006_2014_1412_cases",
  "verification_confidence": 0.85,
  "verification_method": "consensus_anchor_subphase_1_3_initial",
  "last_verified_date": "2026-05-06",
  "caveat": "Netherlands prospective adult community-acquired bacterial meningitis cohort 2006-2014, 1412 cases (72% pneumococcal). Anchor for SP-adult Class 2 vignettes with mortality 17%, unfavorable outcome 39%. Pairs with van de Beek 2004 (PMID 15509818) for two-decade Netherlands continuity. verification_confidence=0.85 pre-direct-fetch."
}
```

### NCBI live re-fetch (2026-05-11)

```json
{
  "uid": "26652862",
  "pubdate": "2016 Mar",
  "epubdate": "2015 Dec 1",
  "source": "Lancet Infect Dis",
  "authors": [
    {
      "name": "Bijlsma MW",
      "authtype": "Author",
      "clusterid": ""
    },
    {
      "name": "Brouwer MC",
      "authtype": "Author",
      "clusterid": ""
    },
    {
      "name": "Kasanmoentalib ES",
      "authtype": "Author",
      "clusterid": ""
    },
    {
      "name": "Kloek AT",
      "authtype": "Author",
      "clusterid": ""
    },
    {
      "name": "Lucas MJ",
      "authtype": "Author",
      "clusterid": ""
    },
    {
      "name": "Tanck MW",
      "authtype": "Author",
      "clusterid": ""
    },
    {
      "name": "van der Ende A",
      "authtype": "Author",
      "clusterid": ""
    },
    {
      "name": "van de Beek D",
      "authtype": "Author",
      "clusterid": ""
    }
  ],
  "lastauthor": "van de Beek D",
  "title": "Community-acquired bacterial meningitis in adults in the Netherlands, 2006-14: a prospective cohort study.",
  "sorttitle": "community acquired bacterial meningitis in adults in the netherlands 2006 14 a prospective cohort study",
  "volume": "16",
  "issue": "3",
  "pages": "339-47",
  "lang": [
    "eng"
  ],
  "nlmuniqueid": "101130150",
  "issn": "1473-3099",
  "essn": "1474-4457",
  "pubtype": [
    "Journal Article",
    "Research Support, Non-U.S. Gov't"
  ],
  "recordstatus": "PubMed - indexed for MEDLINE",
  "pubstatus": "256",
  "articleids": [
    {
      "idtype": "pubmed",
      "idtypen": 1,
      "value": "26652862"
    },
    {
      "idtype": "doi",
      "idtypen": 3,
      "value": "10.1016/S1473-3099(15)00430-2"
    },
    {
      "idtype": "pii",
      "idtypen": 4,
      "value": "S1473-3099(15)00430-2"
    }
  ],
  "history": [
    {
      "pubstatus": "received",
      "date": "2015/09/02 00:00"
    },
    {
      "pubstatus": "revised",
      "date": "2015/10/28 00:00"
    },
    {
      "pubstatus": "accepted",
      "date": "2015/10/29 00:00"
    },
    {
      "pubstatus": "entrez",
      "date": "2015/12/15 06:00"
    },
    {
      "pubstatus": "pubmed",
      "date": "2015/12/15 06:00"
    },
    {
      "pubstatus": "medline",
      "date": "2016/07/30 06:00"
    }
  ],
  "references": [
    {
      "refsource": "Lancet Infect Dis. 2016 Mar;16(3):271-2. doi: 10.1016/S1473-3099(15)00462-4.",
      "reftype": "Comment in",
      "pmid": 26652863,
      "note": ""
    }
  ],
  "attributes": [
    "Has Abstract"
  ],
  "pmcrefcount": "",
  "fulljournalname": "The Lancet. Infectious diseases",
  "elocationid": "doi: 10.1016/S1473-3099(15)00430-2",
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
  "sortpubdate": "2016/03/01 00:00",
  "sortfirstauthor": "Bijlsma MW",
  "vernaculartitle": ""
}
```

### Registry-vs-NCBI delta

- **pages**: registry='339-347' | ncbi='339-47'

### Vignettes citing this anchor (6 total)

#### Vignette: vid=061 file=bact_061_sp_netherlands_adult.json class=2 subphase=1.3 BACT

```
ANCHOR:
  pmid: 26652862
  first_author: Bijlsma
  year: 2016
  journal: Lancet Infect Dis
  citation_type: cohort
  doi: 10.1016/S1473-3099(15)00430-2

DEMOGRAPHICS:
  age_years: 35  sex: male  region: other_global
  ethnicity: white_non_hispanic  altitude_m: 5
  hiv_status: negative  cd4: None
  pregnancy_red_flag: False
  immunocompromise_status: none
  freshwater_exposure_14d: False (None)

HISTORY:
  symptom_onset_to_presentation_days: 1.5
  chief_complaint: fever_with_headache
  red_flags_present: []
  prodrome_description: 35-year-old male, Netherlands. 36-hour rapid progression: fever 39.0 C, severe headache, neck stiffness, photophobia. Tertiary ED Amsterdam. No freshwater. Triad present (Bijlsma 2016 cohort 47 percent triad subgroup). Outcome: survived. Antibiotic at hour 1 plus dexamethasone EU guideline.

VITALS:
  T:39.0C HR:110 BP:124/76 GCS:13 SpO2:96% RR:20

EXAM:
  mental_status: confused  neck_stiff: True  kernig_brudz: True
  cranial_nerve_palsy: none  papilledema: False  focal_deficit: False
  skin_lesion_centrofacial_chronic: False  rash: False

LABS:
  WBC:18500 Plt:240000 ALT/AST:30 CRP:175.0 PCT:7.5 Na:137

CSF:
  OP:27.0cmH2O  WBC:5200/mm3  lymph%:12 neut%:88 eos%:0
  glucose:22mg/dL protein:200mg/dL lactate:6.4mmol/L ADA:NoneU/L
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

NARRATIVE_EN: A 35-year-old man in the Netherlands presented to a tertiary emergency department in Amsterdam with a 36-hour rapid progression of fever to 39.0 C, severe headache, neck stiffness, and photophobia. Examination on admission: temperature 39.0 C, Glasgow Coma Scale 13, neck stiffness, positive Kernig sign, no focal deficit, no rash. CSF showed opening pressure 27 cmH2O, white cell count 5,200 per cubic millimeter (88 percent neutrophils), glucose 22 mg/dL, protein 200 mg/dL. Gram stain revealed gram-positive diplococci; culture identified Streptococcus pneumoniae. Primary anchor: PMID 26652862 (Bijlsma 2016 Lancet Infect Dis), 1,412-episode prospective Netherlands community-acquired adult bacterial meningitis cohort 2006-2014 (SP 70 percent, classic triad 47 percent). Outcome: survived. Subphase 1.3 commit 5.3.4 wave 2, pre-adjudication hold_for_revision.

NARRATIVE_ES: Varon de 35 anos en Paises Bajos (Amsterdam), ingresado a urgencias terciarias con 36 horas de progresion rapida: fiebre 39.0 C, cefalea intensa, rigidez de nuca, fotofobia. Examen: temperatura 39.0 C, escala de Glasgow 13, rigidez de nuca, signo de Kernig positivo, sin deficit focal, sin exantema. Triada clasica presente (subgrupo del 47 por ciento triada-positiva de la cohorte Bijlsma 2016). Liquido cefalorraquideo mostro presion de apertura 27 cmH2O, leucocitos 5,200 por mm3 (88 por ciento neutrofilos), glucosa 22 mg/dL, proteina 200 mg/dL. Tincion de Gram con diplococos grampositivos y cultivo Streptococcus pneumoniae. Anclaje primario en cohorte prospectiva neerlandesa Bijlsma 2016 Lancet ID (PMID 26652862, 1,412 episodios 2006-2014, SP 70 por ciento, triada 47 por ciento). Subphase 1.3 commit 5.3.4 wave 2.

RATIONALE: Anchored to PMID 26652862 (Bijlsma 2016 Lancet Infect Dis), 1,412-episode prospective Netherlands community-acquired adult bacterial meningitis cohort 2006-2014 (SP 70 percent, classic triad 47 percent, mortality 17 percent). Demographic anchor (35yo M adult community SP) sits in dominant cohort stratum. CSF profile bacterial range. Imputation tiers: tier_1_primary={age, sex, csf_culture, csf_gram_stain, triad}; tier_3_within_cohort={csf_wbc, neutrophil_pct, glucose, protein, gcs}; tier_4_priors={temp, symptom_days}. Indeterminate=none. Diagnostic_ambiguity=false. Outcome=survived. Antibiotic_started_hours=1. Tier: tier_3_imputation_within_cohort_review. 5.3.4 wave2 SP-NL-adult.

ANCHORING_EXTRAS: stage=pre_adjudication; status=pending_external_review; self_review_disposition=hold_for_revision; self_review_notes=wave 2 vignette anchored to PMID 26652862 (Bijlsma 2016 Lancet ID); external clinical adjudication pending; classification provisional. adjudicator_ids=WAVE2-PRE-ADJ-1, WAVE2-PRE-ADJ-2 (sentinel); cohen_kappa=0.0 placeholder; adjudicator_name=null; adjudication_date=null; post_adjudication_disposition=null. Subphase 1.3 commit 5.3.4 (2026-05-08). anchor=Bijlsma-Lancet-ID-2016 stratum=adult-community.

ADJUDICATION:
  inclusion_decision: hold_for_revision  ground_truth_class: 2  kappa: 0.0
  adjudicator_ids: ['WAVE2-PRE-ADJ-1', 'WAVE2-PRE-ADJ-2']
  disagreement_resolution: None
```

#### Vignette: vid=063 file=bact_063_sp_elderly_fatal.json class=2 subphase=1.3 BACT

```
ANCHOR:
  pmid: 26652862
  first_author: Bijlsma
  year: 2016
  journal: Lancet Infect Dis
  citation_type: cohort
  doi: 10.1016/S1473-3099(15)00430-2

DEMOGRAPHICS:
  age_years: 72  sex: female  region: other_global
  ethnicity: white_non_hispanic  altitude_m: 5
  hiv_status: negative  cd4: None
  pregnancy_red_flag: False
  immunocompromise_status: none
  freshwater_exposure_14d: False (None)

HISTORY:
  symptom_onset_to_presentation_days: 3.0
  chief_complaint: altered_mental_status
  red_flags_present: []
  prodrome_description: 72-year-old female, Netherlands. 3-day course: progressive fever, headache, confusion progressing to obtundation. Tertiary ED Amsterdam. Late presentation. No freshwater. Triad present (Bijlsma elderly stratum mortality elevated). Outcome: fatal hospital day 3. Antibiotic at hour 2 plus dexamethasone EU guideline.

VITALS:
  T:39.1C HR:118 BP:102/62 GCS:7 SpO2:91% RR:28

EXAM:
  mental_status: comatose  neck_stiff: True  kernig_brudz: True
  cranial_nerve_palsy: none  papilledema: False  focal_deficit: False
  skin_lesion_centrofacial_chronic: False  rash: False

LABS:
  WBC:19200 Plt:168000 ALT/AST:38 CRP:235.0 PCT:13.5 Na:130

CSF:
  OP:27.0cmH2O  WBC:4400/mm3  lymph%:18 neut%:82 eos%:0
  glucose:24mg/dL protein:195mg/dL lactate:6.2mmol/L ADA:NoneU/L
  crag_lfa:negative  wet_mount:negative  xanthochromia:False  RBC:5

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

NARRATIVE_EN: A 72-year-old woman in the Netherlands presented to a tertiary emergency department in Amsterdam after a 3-day course of progressive fever, headache, and confusion progressing to obtundation. Examination on admission: temperature 39.1 C, Glasgow Coma Scale 7, neck stiffness, positive Kernig sign, no focal deficit, no rash. CSF showed opening pressure 27 cmH2O, white cell count 4,400 per cubic millimeter (82 percent neutrophils), glucose 24 mg/dL, protein 195 mg/dL. Gram stain revealed gram-positive diplococci; culture identified Streptococcus pneumoniae. Primary anchor: PMID 26652862 (Bijlsma 2016 Lancet Infect Dis), elderly stratum mortality elevated above the 17 percent cohort-overall rate. Outcome: fatal hospital day 3. Subphase 1.3 commit 5.3.4 wave 2, pre-adjudication hold_for_revision.

NARRATIVE_ES: Mujer de 72 anos en Paises Bajos (Amsterdam), ingresada a urgencias terciarias tras tres dias de fiebre progresiva, cefalea y confusion con obnubilacion. Examen: temperatura 39.1 C, escala de Glasgow 7, rigidez de nuca, signo de Kernig positivo, sin deficit focal, sin exantema. Liquido cefalorraquideo mostro presion de apertura 27 cmH2O, leucocitos 4,400 por mm3 (82 por ciento neutrofilos), glucosa 24 mg/dL, proteina 195 mg/dL. Tincion de Gram con diplococos grampositivos y cultivo Streptococcus pneumoniae. Anclaje primario en cohorte prospectiva Bijlsma 2016 Lancet ID (PMID 26652862, 1,412 episodios 2006-2014, estrato de adultos mayores con mortalidad elevada por encima del 17 por ciento global de la cohorte). Resultado: fatal en hospital dia 3. Subphase 1.3 commit 5.3.4 wave 2.

RATIONALE: Anchored to PMID 26652862 (Bijlsma 2016 Lancet Infect Dis), 1,412-episode prospective Netherlands cohort 2006-2014 (SP 70 percent, mortality 17 percent overall, elderly stratum elevated). Demographic anchor (72yo F elderly) sits in elderly stratum. CSF profile bacterial range. Imputation tiers: tier_1_primary={age, sex, csf_culture, csf_gram_stain}; tier_3_within_cohort={csf_wbc, neutrophil_pct, glucose, protein, gcs, hyponatremia}; tier_4_priors={temp, symptom_days, hr}. Indeterminate=none. Diagnostic_ambiguity=false. Outcome=fatal_hospital_day_3. Antibiotic_started_hours=2. Tier: tier_3_imputation_within_cohort_review. 5.3.4 wave2 SP-NL-elderly-fatal.

ANCHORING_EXTRAS: stage=pre_adjudication; status=pending_external_review; self_review_disposition=hold_for_revision; self_review_notes=wave 2 vignette anchored to PMID 26652862 (Bijlsma 2016 Lancet ID); external clinical adjudication pending; classification provisional. adjudicator_ids=WAVE2-PRE-ADJ-1, WAVE2-PRE-ADJ-2 (sentinel); cohen_kappa=0.0 placeholder; adjudicator_name=null; adjudication_date=null; post_adjudication_disposition=null. Subphase 1.3 commit 5.3.4 (2026-05-08). anchor=Bijlsma-Lancet-ID-2016 stratum=elderly-fatal.

ADJUDICATION:
  inclusion_decision: hold_for_revision  ground_truth_class: 2  kappa: 0.0
  adjudicator_ids: ['WAVE2-PRE-ADJ-1', 'WAVE2-PRE-ADJ-2']
  disagreement_resolution: None
```

#### Vignette: vid=068 file=bact_068_sp_adult_female.json class=2 subphase=1.3 BACT

```
ANCHOR:
  pmid: 26652862
  first_author: Bijlsma
  year: 2016
  journal: Lancet Infect Dis
  citation_type: cohort
  doi: 10.1016/S1473-3099(15)00430-2

DEMOGRAPHICS:
  age_years: 51  sex: female  region: other_global
  ethnicity: white_non_hispanic  altitude_m: 5
  hiv_status: negative  cd4: None
  pregnancy_red_flag: False
  immunocompromise_status: none
  freshwater_exposure_14d: False (None)

HISTORY:
  symptom_onset_to_presentation_days: 2.0
  chief_complaint: fever_with_headache
  red_flags_present: []
  prodrome_description: 51-year-old female, Netherlands. 2-day fever 39.2 C, severe headache, neck stiffness. Recent otitis media one week prior. Tertiary ED Amsterdam. No freshwater. Triad present (Bijlsma 2016 adult community stratum). Outcome: survived no sequelae. Antibiotic at hour 1 plus dexamethasone EU guideline.

VITALS:
  T:39.2C HR:112 BP:124/78 GCS:13 SpO2:96% RR:22

EXAM:
  mental_status: confused  neck_stiff: True  kernig_brudz: True
  cranial_nerve_palsy: none  papilledema: False  focal_deficit: False
  skin_lesion_centrofacial_chronic: False  rash: False

LABS:
  WBC:19800 Plt:260000 ALT/AST:28 CRP:185.0 PCT:7.8 Na:136

CSF:
  OP:28.0cmH2O  WBC:5800/mm3  lymph%:10 neut%:90 eos%:0
  glucose:22mg/dL protein:210mg/dL lactate:6.6mmol/L ADA:NoneU/L
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

NARRATIVE_EN: A 51-year-old woman in the Netherlands presented to a tertiary emergency department in Amsterdam with a 2-day history of fever to 39.2 C, severe headache, and neck stiffness. She had been treated for otitis media one week prior. Examination on admission: temperature 39.2 C, Glasgow Coma Scale 13, neck stiffness, positive Kernig sign, no focal deficit, no rash. CSF showed opening pressure 28 cmH2O, white cell count 5,800 per cubic millimeter (90 percent neutrophils), glucose 22 mg/dL, protein 210 mg/dL. Gram stain revealed gram-positive diplococci; culture identified Streptococcus pneumoniae. Primary anchor: PMID 26652862 (Bijlsma 2016 Lancet Infect Dis), 1,412-episode prospective Netherlands cohort 2006-2014. Outcome: survived no sequelae. Subphase 1.3 commit 5.3.4 wave 2, pre-adjudication hold_for_revision.

NARRATIVE_ES: Mujer de 51 anos en Paises Bajos (Amsterdam), ingresada a urgencias terciarias con dos dias de fiebre 39.2 C, cefalea intensa y rigidez de nuca. Antecedente de otitis media tratada una semana antes. Examen: temperatura 39.2 C, escala de Glasgow 13, rigidez de nuca, signo de Kernig positivo, sin deficit focal, sin exantema. Liquido cefalorraquideo mostro presion de apertura 28 cmH2O, leucocitos 5,800 por mm3 (90 por ciento neutrofilos), glucosa 22 mg/dL, proteina 210 mg/dL. Tincion de Gram con diplococos grampositivos y cultivo Streptococcus pneumoniae. Anclaje primario en cohorte prospectiva Bijlsma 2016 Lancet ID (PMID 26652862, 1,412 episodios 2006-2014, SP 70 por ciento, triada 47 por ciento). Resultado: sobrevivio sin secuelas. Subphase 1.3 commit 5.3.4 wave 2, pre-adjudicacion hold_for_revision.

RATIONALE: Anchored to PMID 26652862 (Bijlsma 2016 Lancet ID), 1,412-episode prospective Netherlands cohort 2006-2014 (SP 70 percent, classic triad 47 percent). Demographic anchor (51yo F adult with otitis media antecedent) sits in adult community stratum. CSF profile bacterial range. Imputation tiers: tier_1_primary={age, sex, csf_culture, csf_gram_stain, otitis_media history}; tier_3_within_cohort={csf_wbc, neutrophil_pct, glucose, protein}; tier_4_priors={temp, gcs, symptom_days}. Indeterminate=none. Diagnostic_ambiguity=false. Outcome=survived_no_sequelae. Tier: tier_3_imputation_within_cohort_review. 5.3.4 wave2 SP-NL-adult-female.

ANCHORING_EXTRAS: stage=pre_adjudication; status=pending_external_review; self_review_disposition=hold_for_revision; self_review_notes=wave 2 vignette anchored to PMID 26652862 (Bijlsma 2016 Lancet ID); external clinical adjudication pending; classification provisional. adjudicator_ids=WAVE2-PRE-ADJ-1, WAVE2-PRE-ADJ-2 (sentinel); cohen_kappa=0.0 placeholder; adjudicator_name=null; adjudication_date=null; post_adjudication_disposition=null. Subphase 1.3 commit 5.3.4 (2026-05-08). anchor=Bijlsma-Lancet-ID-2016 stratum=adult-community-female.

ADJUDICATION:
  inclusion_decision: hold_for_revision  ground_truth_class: 2  kappa: 0.0
  adjudicator_ids: ['WAVE2-PRE-ADJ-1', 'WAVE2-PRE-ADJ-2']
  disagreement_resolution: None
```

#### Vignette: vid=070 file=bact_070_sp_elderly_sequelae.json class=2 subphase=1.3 BACT

```
ANCHOR:
  pmid: 26652862
  first_author: Bijlsma
  year: 2016
  journal: Lancet Infect Dis
  citation_type: cohort
  doi: 10.1016/S1473-3099(15)00430-2

DEMOGRAPHICS:
  age_years: 65  sex: male  region: other_global
  ethnicity: white_non_hispanic  altitude_m: 5
  hiv_status: negative  cd4: None
  pregnancy_red_flag: False
  immunocompromise_status: none
  freshwater_exposure_14d: False (None)

HISTORY:
  symptom_onset_to_presentation_days: 2.5
  chief_complaint: fever_with_headache
  red_flags_present: []
  prodrome_description: 65-year-old male, Netherlands. 2.5-day fever 39.0 C, headache, neck stiffness, mild confusion. Tertiary ED Amsterdam. No freshwater. Triad present (Bijlsma elderly stratum, sequelae rate 24 percent in survivors). Outcome: survived with mild hearing loss. Antibiotic at hour 1.5 plus dexamethasone EU.

VITALS:
  T:39.0C HR:108 BP:134/80 GCS:12 SpO2:96% RR:22

EXAM:
  mental_status: confused  neck_stiff: True  kernig_brudz: True
  cranial_nerve_palsy: none  papilledema: False  focal_deficit: False
  skin_lesion_centrofacial_chronic: False  rash: False

LABS:
  WBC:18200 Plt:225000 ALT/AST:32 CRP:168.0 PCT:6.8 Na:135

CSF:
  OP:26.0cmH2O  WBC:4800/mm3  lymph%:16 neut%:84 eos%:0
  glucose:25mg/dL protein:195mg/dL lactate:6.0mmol/L ADA:NoneU/L
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

NARRATIVE_EN: A 65-year-old man in the Netherlands presented to a tertiary emergency department in Amsterdam with a 2.5-day history of fever to 39.0 C, headache, neck stiffness, and mild confusion. Examination on admission: temperature 39.0 C, Glasgow Coma Scale 12, neck stiffness, positive Kernig sign, no focal deficit, no rash. CSF showed opening pressure 26 cmH2O, white cell count 4,800 per cubic millimeter (84 percent neutrophils), glucose 25 mg/dL, protein 195 mg/dL. Gram stain revealed gram-positive diplococci; culture identified Streptococcus pneumoniae. Primary anchor: PMID 26652862 (Bijlsma 2016 Lancet Infect Dis), 1,412-episode prospective Netherlands cohort 2006-2014; elderly stratum sequelae rate 24 percent in survivors. Outcome: survived with mild hearing loss. Subphase 1.3 commit 5.3.4 wave 2, pre-adjudication hold_for_revision.

NARRATIVE_ES: Varon de 65 anos en Paises Bajos (Amsterdam), ingresado a urgencias terciarias con 2.5 dias de fiebre 39.0 C, cefalea, rigidez de nuca y confusion leve. Examen: temperatura 39.0 C, escala de Glasgow 12, rigidez de nuca, signo de Kernig positivo, sin deficit focal, sin exantema. Liquido cefalorraquideo mostro presion de apertura 26 cmH2O, leucocitos 4,800 por mm3 (84 por ciento neutrofilos), glucosa 25 mg/dL, proteina 195 mg/dL. Tincion de Gram con diplococos grampositivos y cultivo Streptococcus pneumoniae. Anclaje primario en cohorte Bijlsma 2016 Lancet ID (PMID 26652862, estrato adulto mayor, secuelas 24 por ciento en sobrevivientes). Resultado: sobrevivio con perdida auditiva leve. Subphase 1.3 commit 5.3.4 wave 2.

RATIONALE: Anchored to PMID 26652862 (Bijlsma 2016 Lancet ID), 1,412-episode prospective Netherlands cohort 2006-2014 (SP 70 percent, sequelae rate 24 percent in survivors at age >=60). Demographic anchor (65yo M elderly survived) sits in elderly-survived-with-sequelae stratum. CSF profile bacterial range. Imputation tiers: tier_1_primary={age, sex, csf_culture, csf_gram_stain}; tier_3_within_cohort={csf_wbc, neutrophil_pct, glucose, protein, gcs}; tier_4_priors={temp, symptom_days}. Indeterminate=none. Diagnostic_ambiguity=false. Outcome=survived_with_mild_hearing_loss. Tier: tier_3_imputation_within_cohort_review. 5.3.4 wave2 SP-NL-elderly-sequelae.

ANCHORING_EXTRAS: stage=pre_adjudication; status=pending_external_review; self_review_disposition=hold_for_revision; self_review_notes=wave 2 vignette anchored to PMID 26652862 (Bijlsma 2016 Lancet ID); external clinical adjudication pending; classification provisional. adjudicator_ids=WAVE2-PRE-ADJ-1, WAVE2-PRE-ADJ-2 (sentinel); cohen_kappa=0.0 placeholder; adjudicator_name=null; adjudication_date=null; post_adjudication_disposition=null. Subphase 1.3 commit 5.3.4 (2026-05-08). anchor=Bijlsma-Lancet-ID-2016 stratum=elderly-survived-sequelae.

ADJUDICATION:
  inclusion_decision: hold_for_revision  ground_truth_class: 2  kappa: 0.0
  adjudicator_ids: ['WAVE2-PRE-ADJ-1', 'WAVE2-PRE-ADJ-2']
  disagreement_resolution: None
```

#### Vignette: vid=072 file=bact_072_sp_adult.json class=2 subphase=1.3 BACT

```
ANCHOR:
  pmid: 26652862
  first_author: Bijlsma
  year: 2016
  journal: Lancet Infect Dis
  citation_type: cohort
  doi: 10.1016/S1473-3099(15)00430-2

DEMOGRAPHICS:
  age_years: 55  sex: male  region: other_global
  ethnicity: white_non_hispanic  altitude_m: 5
  hiv_status: negative  cd4: None
  pregnancy_red_flag: False
  immunocompromise_status: none
  freshwater_exposure_14d: False (None)

HISTORY:
  symptom_onset_to_presentation_days: 2.0
  chief_complaint: fever_with_headache
  red_flags_present: []
  prodrome_description: 55-year-old male, Netherlands. 48-hour fever 39.3 C, severe headache, neck stiffness. Tertiary ED Amsterdam. No freshwater. Triad present (Bijlsma adult community stratum). Outcome: survived no sequelae. Antibiotic at hour 1 plus dexamethasone EU guideline 2002.

VITALS:
  T:39.3C HR:110 BP:128/78 GCS:13 SpO2:96% RR:22

EXAM:
  mental_status: confused  neck_stiff: True  kernig_brudz: True
  cranial_nerve_palsy: none  papilledema: False  focal_deficit: False
  skin_lesion_centrofacial_chronic: False  rash: False

LABS:
  WBC:19400 Plt:250000 ALT/AST:30 CRP:178.0 PCT:7.2 Na:136

CSF:
  OP:27.0cmH2O  WBC:5600/mm3  lymph%:12 neut%:88 eos%:0
  glucose:23mg/dL protein:205mg/dL lactate:6.4mmol/L ADA:NoneU/L
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

NARRATIVE_EN: A 55-year-old man in the Netherlands presented to a tertiary emergency department in Amsterdam with a 48-hour history of fever to 39.3 C, severe headache, and neck stiffness. Examination on admission: temperature 39.3 C, Glasgow Coma Scale 13, neck stiffness, positive Kernig sign, no focal deficit, no rash. CSF showed opening pressure 27 cmH2O, white cell count 5,600 per cubic millimeter (88 percent neutrophils), glucose 23 mg/dL, protein 205 mg/dL. Gram stain revealed gram-positive diplococci; culture identified Streptococcus pneumoniae. Primary anchor: PMID 26652862 (Bijlsma 2016 Lancet Infect Dis), 1,412-episode prospective Netherlands community-acquired adult cohort 2006-2014 (SP 70 percent, classic triad 47 percent, mortality 17 percent). Outcome: survived no sequelae. Subphase 1.3 commit 5.3.4 wave 2, pre-adjudication hold_for_revision.

NARRATIVE_ES: Varon de 55 anos en Paises Bajos (Amsterdam), ingresado a urgencias terciarias con 48 horas de fiebre 39.3 C, cefalea intensa y rigidez de nuca. Examen: temperatura 39.3 C, escala de Glasgow 13, rigidez de nuca, signo de Kernig positivo, sin deficit focal, sin exantema. Liquido cefalorraquideo mostro presion de apertura 27 cmH2O, leucocitos 5,600 por mm3 (88 por ciento neutrofilos), glucosa 23 mg/dL, proteina 205 mg/dL. Tincion de Gram con diplococos grampositivos y cultivo Streptococcus pneumoniae. Anclaje primario en cohorte prospectiva Bijlsma 2016 Lancet ID (PMID 26652862, 1,412 episodios 2006-2014, estrato adulto comunitario). Subphase 1.3 commit 5.3.4 wave 2, pre-adjudicacion hold_for_revision.

RATIONALE: Anchored to PMID 26652862 (Bijlsma 2016 Lancet ID), 1,412-episode prospective Netherlands cohort 2006-2014 (SP 70 percent, classic triad 47 percent). Demographic anchor (55yo M adult community) sits in dominant adult-community stratum. CSF profile bacterial range. Imputation tiers: tier_1_primary={age, sex, csf_culture, csf_gram_stain}; tier_3_within_cohort={csf_wbc, neutrophil_pct, glucose, protein}; tier_4_priors={temp, gcs, symptom_days}. Indeterminate=none. Diagnostic_ambiguity=false. Outcome=survived. Tier: tier_3_imputation_within_cohort_review. 5.3.4 wave2 SP-NL-adult-community.

ANCHORING_EXTRAS: stage=pre_adjudication; status=pending_external_review; self_review_disposition=hold_for_revision; self_review_notes=wave 2 vignette anchored to PMID 26652862 (Bijlsma 2016 Lancet ID); external clinical adjudication pending; classification provisional. adjudicator_ids=WAVE2-PRE-ADJ-1, WAVE2-PRE-ADJ-2 (sentinel); cohen_kappa=0.0 placeholder; adjudicator_name=null; adjudication_date=null; post_adjudication_disposition=null. Subphase 1.3 commit 5.3.4 (2026-05-08). anchor=Bijlsma-Lancet-ID-2016 stratum=adult-community-male.

ADJUDICATION:
  inclusion_decision: hold_for_revision  ground_truth_class: 2  kappa: 0.0
  adjudicator_ids: ['WAVE2-PRE-ADJ-1', 'WAVE2-PRE-ADJ-2']
  disagreement_resolution: None
```

#### Vignette: vid=074 file=bact_074_sp_adult_female.json class=2 subphase=1.3 BACT

```
ANCHOR:
  pmid: 26652862
  first_author: Bijlsma
  year: 2016
  journal: Lancet Infect Dis
  citation_type: cohort
  doi: 10.1016/S1473-3099(15)00430-2

DEMOGRAPHICS:
  age_years: 42  sex: female  region: other_global
  ethnicity: white_non_hispanic  altitude_m: 5
  hiv_status: negative  cd4: None
  pregnancy_red_flag: False
  immunocompromise_status: none
  freshwater_exposure_14d: False (None)

HISTORY:
  symptom_onset_to_presentation_days: 1.5
  chief_complaint: fever_with_headache
  red_flags_present: []
  prodrome_description: 42-year-old female, Netherlands. 36-hour fever 39.1 C, severe headache, neck stiffness, photophobia. Tertiary ED Amsterdam. No freshwater. Triad present (Bijlsma adult community stratum, women cohort proportion 46 percent). Outcome: survived no sequelae. Antibiotic at hour 1 plus dexamethasone.

VITALS:
  T:39.1C HR:108 BP:122/74 GCS:13 SpO2:97% RR:20

EXAM:
  mental_status: confused  neck_stiff: True  kernig_brudz: True
  cranial_nerve_palsy: none  papilledema: False  focal_deficit: False
  skin_lesion_centrofacial_chronic: False  rash: False

LABS:
  WBC:18800 Plt:245000 ALT/AST:28 CRP:165.0 PCT:6.5 Na:137

CSF:
  OP:26.0cmH2O  WBC:5400/mm3  lymph%:14 neut%:86 eos%:0
  glucose:24mg/dL protein:200mg/dL lactate:6.2mmol/L ADA:NoneU/L
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

NARRATIVE_EN: A 42-year-old woman in the Netherlands presented to a tertiary emergency department in Amsterdam with a 36-hour history of fever to 39.1 C, severe headache, neck stiffness, and photophobia. Examination on admission: temperature 39.1 C, Glasgow Coma Scale 13, neck stiffness, positive Kernig sign, no focal deficit, no rash. CSF showed opening pressure 26 cmH2O, white cell count 5,400 per cubic millimeter (86 percent neutrophils), glucose 24 mg/dL, protein 200 mg/dL. Gram stain revealed gram-positive diplococci; culture identified Streptococcus pneumoniae. Primary anchor: PMID 26652862 (Bijlsma 2016 Lancet Infect Dis), 1,412-episode prospective Netherlands cohort 2006-2014 (women cohort proportion 46 percent). Outcome: survived no sequelae. Subphase 1.3 commit 5.3.4 wave 2, pre-adjudication hold_for_revision.

NARRATIVE_ES: Mujer de 42 anos en Paises Bajos (Amsterdam), ingresada a urgencias terciarias con 36 horas de fiebre 39.1 C, cefalea intensa, rigidez de nuca y fotofobia. Examen: temperatura 39.1 C, escala de Glasgow 13, rigidez de nuca, signo de Kernig positivo, sin deficit focal, sin exantema. Liquido cefalorraquideo mostro presion de apertura 26 cmH2O, leucocitos 5,400 por mm3 (86 por ciento neutrofilos), glucosa 24 mg/dL, proteina 200 mg/dL. Tincion de Gram con diplococos grampositivos y cultivo Streptococcus pneumoniae. Anclaje primario en cohorte prospectiva Bijlsma 2016 Lancet ID (PMID 26652862, 1,412 episodios 2006-2014, proporcion de mujeres 46 por ciento). Subphase 1.3 commit 5.3.4 wave 2, pre-adjudicacion hold_for_revision.

RATIONALE: Anchored to PMID 26652862 (Bijlsma 2016 Lancet ID), 1,412-episode prospective Netherlands cohort 2006-2014. Demographic anchor (42yo F adult community) sits in adult-community stratum. CSF profile bacterial range. Imputation tiers: tier_1_primary={age, sex, csf_culture, csf_gram_stain}; tier_3_within_cohort={csf_wbc, neutrophil_pct, glucose, protein}; tier_4_priors={temp, gcs, symptom_days}. Indeterminate=none. Diagnostic_ambiguity=false. Outcome=survived_no_sequelae. Tier: tier_3_imputation_within_cohort_review. 5.3.4 wave2 SP-NL-adult-female-2.

ANCHORING_EXTRAS: stage=pre_adjudication; status=pending_external_review; self_review_disposition=hold_for_revision; self_review_notes=wave 2 vignette anchored to PMID 26652862 (Bijlsma 2016 Lancet ID); external clinical adjudication pending; classification provisional. adjudicator_ids=WAVE2-PRE-ADJ-1, WAVE2-PRE-ADJ-2 (sentinel); cohen_kappa=0.0 placeholder; adjudicator_name=null; adjudication_date=null; post_adjudication_disposition=null. Subphase 1.3 commit 5.3.4 (2026-05-08). anchor=Bijlsma-Lancet-ID-2016 stratum=adult-community-female-2.

ADJUDICATION:
  inclusion_decision: hold_for_revision  ground_truth_class: 2  kappa: 0.0
  adjudicator_ids: ['WAVE2-PRE-ADJ-1', 'WAVE2-PRE-ADJ-2']
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
