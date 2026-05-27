# AUDIT bundle: PMID 32935747 | Soeters 2020

Generated: 2026-05-11
Vignettes in bundle: 5
Build status: NCBI fetched
Bundle type: BIG (n>=5 vignettes single-anchor)

## Anchor: PMID 32935747 | Soeters 2020

### Registry metadata (current state)

```json
{
  "pmid": "32935747",
  "doi": "10.15585/mmwr.mm6936a3",
  "authors_short": "Soeters HM et al.",
  "authors_full": [
    "Soeters HM",
    "McNamara LA",
    "Whaley M",
    "Wang X",
    "Alexander-Scott N",
    "Kanadanian KV",
    "Kelleher CM",
    "King M",
    "Lawrence GL",
    "MacNeil JR"
  ],
  "journal": "MMWR Morb Mortal Wkly Rep",
  "journal_short_code": "MMWR",
  "year": 2020,
  "volume": "69",
  "issue": "37",
  "pages": "1245-1249",
  "title": "Active Bacterial Core Surveillance for invasive bacterial diseases",
  "anchor_type": "surveillance",
  "anchor_subtype": "cdc_abcs_hib_nm_surveillance_2008_2019",
  "verification_confidence": 0.85,
  "verification_method": "consensus_anchor_subphase_1_3_initial",
  "last_verified_date": "2026-05-06",
  "caveat": "CDC Active Bacterial Core surveillance: H. influenzae and N. meningitidis incidence and serogroup distribution, US 2008-2019. Anchor for Class 2 Hib (pediatric unimmunized) and NM serogroup distribution vignettes. verification_confidence=0.85 pre-direct-fetch."
}
```

### NCBI live re-fetch (2026-05-11)

```json
{
  "uid": "32935747",
  "pubdate": "2020 Jul-Sep",
  "epubdate": "",
  "source": "Arq Gastroenterol",
  "authors": [
    {
      "name": "Mattar R",
      "authtype": "Author",
      "clusterid": ""
    },
    {
      "name": "Marques SB",
      "authtype": "Author",
      "clusterid": ""
    },
    {
      "name": "Minata MK",
      "authtype": "Author",
      "clusterid": ""
    },
    {
      "name": "Silva-Etto JMKD",
      "authtype": "Author",
      "clusterid": ""
    },
    {
      "name": "Sakai P",
      "authtype": "Author",
      "clusterid": ""
    },
    {
      "name": "DE Moura EGH",
      "authtype": "Author",
      "clusterid": ""
    }
  ],
  "lastauthor": "DE Moura EGH",
  "title": "DIAGNOSTIC ACCURACY OF ONE SAMPLE OR TWO SAMPLES QUANTITATIVE FECAL IMMUNOCHEMICAL TESTS FOR INTESTINAL NEOPLASIA DETECTION.",
  "sorttitle": "diagnostic accuracy of one sample or two samples quantitative fecal immunochemical tests for intestinal neoplasia detection",
  "volume": "57",
  "issue": "3",
  "pages": "316-322",
  "lang": [
    "eng"
  ],
  "nlmuniqueid": "15310600R",
  "issn": "0004-2803",
  "essn": "1678-4219",
  "pubtype": [
    "Journal Article",
    "Randomized Controlled Trial"
  ],
  "recordstatus": "PubMed - indexed for MEDLINE",
  "pubstatus": "4",
  "articleids": [
    {
      "idtype": "pubmed",
      "idtypen": 1,
      "value": "32935747"
    },
    {
      "idtype": "doi",
      "idtypen": 3,
      "value": "10.1590/S0004-2803.202000000-58"
    },
    {
      "idtype": "pii",
      "idtypen": 4,
      "value": "S0004-28032020005008207"
    }
  ],
  "history": [
    {
      "pubstatus": "received",
      "date": "2020/05/08 00:00"
    },
    {
      "pubstatus": "accepted",
      "date": "2020/06/05 00:00"
    },
    {
      "pubstatus": "pubmed",
      "date": "2020/09/17 06:00"
    },
    {
      "pubstatus": "medline",
      "date": "2021/01/16 06:00"
    },
    {
      "pubstatus": "entrez",
      "date": "2020/09/16 08:40"
    }
  ],
  "references": [],
  "attributes": [
    "Has Abstract"
  ],
  "pmcrefcount": "",
  "fulljournalname": "Arquivos de gastroenterologia",
  "elocationid": "doi: 10.1590/S0004-2803.202000000-58",
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
  "sortpubdate": "2020/07/01 00:00",
  "sortfirstauthor": "Mattar R",
  "vernaculartitle": ""
}
```

### Registry-vs-NCBI delta

- **first_author_surname**: registry='Soeters' | ncbi='Mattar R'
- **journal**: registry='MMWR Morb Mortal Wkly Rep' | ncbi='Arq Gastroenterol'
- **volume**: registry='69' | ncbi='57'
- **issue**: registry='37' | ncbi='3'
- **pages**: registry='1245-1249' | ncbi='316-322'
- **doi**: registry='10.15585/mmwr.mm6936a3' | ncbi='10.1590/s0004-2803.202000000-58'

### Vignettes citing this anchor (5 total)

#### Vignette: vid=083 file=bact_083_nm_adolescent_fatal.json class=2 subphase=1.3 BACT

```
ANCHOR:
  pmid: 32935747
  first_author: Soeters
  year: 2020
  journal: MMWR
  citation_type: surveillance
  doi: 10.15585/mmwr.mm6936a3

DEMOGRAPHICS:
  age_years: 17  sex: female  region: us_south
  ethnicity: white_non_hispanic  altitude_m: 100
  hiv_status: negative  cd4: None
  pregnancy_red_flag: False
  immunocompromise_status: none
  freshwater_exposure_14d: False (None)

HISTORY:
  symptom_onset_to_presentation_days: 1.5
  chief_complaint: altered_mental_status
  red_flags_present: []
  prodrome_description: 17-year-old female, US South region. 36-hour rapid progression: fever 39.6 C, severe headache, neck stiffness, petechial rash extremities and trunk evolving to purpura within 12 hours. Tertiary ED. No freshwater. Outcome: fatal hospital day 2 with disseminated intravascular coagulation.

VITALS:
  T:39.6C HR:132 BP:92/54 GCS:8 SpO2:90% RR:30

EXAM:
  mental_status: stuporous  neck_stiff: True  kernig_brudz: True
  cranial_nerve_palsy: none  papilledema: False  focal_deficit: False
  skin_lesion_centrofacial_chronic: False  rash: True

LABS:
  WBC:22000 Plt:78000 ALT/AST:56 CRP:245.0 PCT:18.0 Na:132

CSF:
  OP:30.0cmH2O  WBC:4500/mm3  lymph%:12 neut%:88 eos%:0
  glucose:18mg/dL protein:240mg/dL lactate:7.6mmol/L ADA:NoneU/L
  crag_lfa:negative  wet_mount:negative  xanthochromia:False  RBC:6

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

NARRATIVE_EN: A 17-year-old woman in the US South region presented to a tertiary emergency department with a 36-hour rapid progression of fever to 39.6 C, severe headache, neck stiffness, and a petechial rash on her extremities and trunk that evolved to purpura within 12 hours. Examination on admission: temperature 39.6 C, Glasgow Coma Scale 8, neck stiffness, positive Kernig sign, petechial rash, no focal deficit. Platelets 78,000 with evolving disseminated intravascular coagulation. CSF showed opening pressure 30 cmH2O, white cell count 4,500 per cubic millimeter (88 percent neutrophils), glucose 18 mg/dL, protein 240 mg/dL. Gram stain revealed gram-negative diplococci; culture identified Neisseria meningitidis serogroup B. Anchored to Soeters 2020 MMWR CDC ABCs (PMID 32935747, US adolescent NM surveillance, mortality 12 percent). Outcome: fatal hospital day 2. Subphase 1.3 commit 5.3.4 wave 2, pre-adjudication hold_for_revision.

NARRATIVE_ES: Mujer de 17 anos en region sur de Estados Unidos, ingresada a urgencias terciarias con 36 horas de progresion rapida: fiebre 39.6 C, cefalea intensa, rigidez de nuca y exantema petequial en extremidades y tronco con evolucion a purpura en 12 horas. Examen: temperatura 39.6 C, escala de Glasgow 8, rigidez de nuca, signo de Kernig positivo, exantema petequial, sin deficit focal. Plaquetas 78,000 con coagulacion intravascular diseminada evolutiva. Liquido cefalorraquideo mostro presion de apertura 30 cmH2O, leucocitos 4,500 por mm3 (88 por ciento neutrofilos), glucosa 18 mg/dL, proteina 240 mg/dL. Tincion de Gram con diplococos gramnegativos y cultivo Neisseria meningitidis serogrupo B. Anclaje en Soeters 2020 MMWR ABCs CDC (PMID 32935747, vigilancia adolescente). Subphase 1.3 commit 5.3.4 wave 2.

RATIONALE: Anchored to PMID 32935747 (Soeters 2020 MMWR CDC ABCs surveillance) covering US adolescent and young adult NM epidemiology with approximately 12 percent overall NM case-fatality and elevated fulminant-purpura subgroup mortality. Demographic anchor (17yo F adolescent) sits in target surveillance stratum. CSF bacterial range; petechial-to-purpuric evolution + DIC consistent with fulminant meningococcemia. Imputation tiers: tier_1_primary={age, sex, csf_culture, csf_gram_stain, petechial_rash, DIC platelets}; tier_3_within_cohort={csf_wbc, neutrophil_pct, glucose, protein}; tier_4_priors={temp, gcs, symptom_days}. Indeterminate=none. Diagnostic_ambiguity=false. Outcome=fatal_hospital_day_2. Tier: tier_4_imputation_cdc_abcs_anchored. 5.3.4 wave2 NM-adolescent-fulminant-fatal.

ANCHORING_EXTRAS: stage=pre_adjudication; status=pending_external_review; self_review_disposition=hold_for_revision; self_review_notes=wave 2 vignette anchored to PMID 32935747 (Soeters 2020 MMWR CDC ABCs); external clinical adjudication pending; classification provisional. adjudicator_ids=WAVE2-PRE-ADJ-1, WAVE2-PRE-ADJ-2 (sentinel); cohen_kappa=0.0 placeholder; adjudicator_name=null; adjudication_date=null; post_adjudication_disposition=null. Subphase 1.3 commit 5.3.4 (2026-05-08). anchor=Soeters-MMWR-CDC-ABCs-2020 stratum=adolescent-fulminant.

ADJUDICATION:
  inclusion_decision: hold_for_revision  ground_truth_class: 2  kappa: 0.0
  adjudicator_ids: ['WAVE2-PRE-ADJ-1', 'WAVE2-PRE-ADJ-2']
  disagreement_resolution: None
```

#### Vignette: vid=084 file=bact_084_nm_loreto_infant_partial_treatment_ambiguity.json class=2 subphase=1.3 BACT

```
ANCHOR:
  pmid: 32935747
  first_author: Soeters
  year: 2020
  journal: MMWR
  citation_type: surveillance
  doi: 10.15585/mmwr.mm6936a3

DEMOGRAPHICS:
  age_years: 1  sex: male  region: peru_loreto_amazon
  ethnicity: mestizo  altitude_m: 100
  hiv_status: negative  cd4: None
  pregnancy_red_flag: False
  immunocompromise_status: none
  freshwater_exposure_14d: False (None)

HISTORY:
  symptom_onset_to_presentation_days: 2.0
  chief_complaint: altered_mental_status
  red_flags_present: []
  prodrome_description: 14-month-old male, Loreto Peru Amazon community. Outpatient amoxicillin 24 hours via riverine health post for febrile illness. Subsequent decline: fever 39.4 C, irritability, lethargy, bulging fontanelle, petechiae trunk. Air-evac to Iquitos tertiary ED. Diagnostic_ambiguity=true; type=partial_antibiotic_pretreatment_sterile_cultures. Outcome: fatal.

VITALS:
  T:39.4C HR:168 BP:78/46 GCS:8 SpO2:90% RR:38

EXAM:
  mental_status: stuporous  neck_stiff: True  kernig_brudz: True
  cranial_nerve_palsy: none  papilledema: None  focal_deficit: False
  skin_lesion_centrofacial_chronic: False  rash: True

LABS:
  WBC:16500 Plt:95000 ALT/AST:48 CRP:132.0 PCT:6.5 Na:134

CSF:
  OP:24.0cmH2O  WBC:1800/mm3  lymph%:40 neut%:60 eos%:0
  glucose:28mg/dL protein:165mg/dL lactate:4.6mmol/L ADA:NoneU/L
  crag_lfa:negative  wet_mount:negative  xanthochromia:False  RBC:5

IMAGING:
  modality: ct_noncontrast  pattern: diffuse_cerebral_edema_basilar_meningeal_enhancement
  finding_count: 1
  text_summary: CT head non-contrast: diffuse cerebral edema with effacement of sulci, basilar meningeal enhancement on contrast-equivalent regions, no focal lesion, no midline shift. Pattern consistent with severe late-stage bacterial meningitis.

DIAGNOSTIC_TESTS:
  total_results: 4
  pcr_panel: neisseria_meningitidis_positive_serogroup_C
  xpert_mtb_rif: n/a
  blood_culture: n/a
  csf_culture: n/a
  serology_or_antigen: n/a
  smear_or_gram: n/a
  brain_biopsy: n/a

NARRATIVE_EN: A 14-month-old boy from a Loreto Amazon community in Peru received outpatient amoxicillin for 24 hours via a riverine health post for an undifferentiated febrile illness, then deteriorated with fever to 39.4 C, irritability, lethargy, a bulging anterior fontanelle, and petechiae on the trunk. He was air-evacuated to a tertiary emergency department in Iquitos. Examination on admission: temperature 39.4 C, Glasgow Coma Scale 8, neck stiffness, positive Kernig sign, petechiae. CSF showed opening pressure 24 cmH2O, white cell count 1,800 per cubic millimeter (60 percent neutrophils), glucose 28 mg/dL, protein 165 mg/dL. Gram stain unrevealing; CSF + blood cultures sterile after partial-antibiotic pretreatment and remote specimen handling delay; CSF meningococcal PCR positive for serogroup C. Diagnostic_ambiguity=true; type=partial_antibiotic_pretreatment_sterile_cultures. Anchored to Soeters 2020 MMWR CDC ABCs (PMID 32935747, NM surveillance overlaid with Peru-Amazon care-access context). Outcome: fatal. Subphase 1.3 commit 5.3.4 wave 2, pre-adjudication hold_for_revision.

NARRATIVE_ES: Lactante varon de 14 meses originario de comunidad ribereña en Loreto Peru, recibio amoxicilina ambulatoria 24 horas en posta de salud rural por enfermedad febril, con posterior deterioro: fiebre 39.4 C, irritabilidad, letargo, fontanela anterior abombada, petequias en tronco. Evacuacion aerea a urgencias terciarias en Iquitos. Examen: temperatura 39.4 C, escala de Glasgow 8, rigidez de nuca, signo de Kernig positivo, petequias. Liquido cefalorraquideo mostro presion de apertura 24 cmH2O, leucocitos 1,800 por mm3 (60 por ciento neutrofilos), glucosa 28 mg/dL, proteina 165 mg/dL. Tincion de Gram sin organismos; cultivos de liquido y sangre esteriles tras pretratamiento antibiotico parcial y demora en manejo de muestras; PCR meningococica en liquido positiva para serogrupo C. Ambiguedad diagnostica por pretratamiento parcial. Subphase 1.3 commit 5.3.4 wave 2.

RATIONALE: Anchored to PMID 32935747 (Soeters 2020 MMWR CDC ABCs) surveillance with overlaid Peru-Amazon care-access context. Diagnostic_ambiguity=true; type=partial_antibiotic_pretreatment_sterile_cultures with secondary remote-specimen-handling-delay compounding feature. Demographic anchor (14mo M Loreto pediatric outpatient pretreated then air-evac) sits in ambiguity stratum. CSF profile attenuated (WBC 1800, neutrophil 60 percent). PCR confirms organism (serogroup C). Imputation tiers: tier_1_primary={age, sex, csf_meningococcal_pcr, pretreatment_history, petechial_rash}; tier_3_within_cohort={csf_wbc, neutrophil_pct, glucose, protein attenuation}; tier_4_priors={temp, gcs, hr}. Indeterminate=culture-based-organism-confirmation. Outcome=fatal. Tier: tier_4_imputation_cdc_abcs_anchored. 5.3.4 wave2 NM-Loreto-infant-ambiguity.

ANCHORING_EXTRAS: stage=pre_adjudication; status=pending_external_review; self_review_disposition=hold_for_revision; self_review_notes=wave 2 vignette anchored to PMID 32935747 (Soeters 2020 MMWR CDC ABCs); external clinical adjudication pending; classification provisional. adjudicator_ids=WAVE2-PRE-ADJ-1, WAVE2-PRE-ADJ-2 (sentinel); cohen_kappa=0.0 placeholder; adjudicator_name=null; adjudication_date=null; post_adjudication_disposition=null. Subphase 1.3 commit 5.3.4 (2026-05-08). anchor=Soeters-MMWR-CDC-ABCs-2020 type=partial_antibiotic_pretreatment region=peru-loreto-amazon.

ADJUDICATION:
  inclusion_decision: hold_for_revision  ground_truth_class: 2  kappa: 0.0
  adjudicator_ids: ['WAVE2-PRE-ADJ-1', 'WAVE2-PRE-ADJ-2']
  disagreement_resolution: None
```

#### Vignette: vid=085 file=bact_085_nm_military.json class=2 subphase=1.3 BACT

```
ANCHOR:
  pmid: 32935747
  first_author: Soeters
  year: 2020
  journal: MMWR
  citation_type: surveillance
  doi: 10.15585/mmwr.mm6936a3

DEMOGRAPHICS:
  age_years: 22  sex: female  region: us_south
  ethnicity: white_non_hispanic  altitude_m: 100
  hiv_status: negative  cd4: None
  pregnancy_red_flag: False
  immunocompromise_status: none
  freshwater_exposure_14d: False (None)

HISTORY:
  symptom_onset_to_presentation_days: 1.0
  chief_complaint: fever_with_headache
  red_flags_present: []
  prodrome_description: 22-year-old female, US South region. Active-duty military barracks setting. 24-hour fever 39.4 C, severe headache, neck stiffness, petechial rash extremities. Tertiary ED. No freshwater. Outcome: survived no sequelae. Antibiotic at hour 1 plus dexamethasone IDSA young adult NM.

VITALS:
  T:39.4C HR:122 BP:112/70 GCS:13 SpO2:96% RR:22

EXAM:
  mental_status: confused  neck_stiff: True  kernig_brudz: True
  cranial_nerve_palsy: none  papilledema: False  focal_deficit: False
  skin_lesion_centrofacial_chronic: False  rash: True

LABS:
  WBC:18800 Plt:195000 ALT/AST:38 CRP:188.0 PCT:8.2 Na:136

CSF:
  OP:26.0cmH2O  WBC:5200/mm3  lymph%:10 neut%:90 eos%:0
  glucose:22mg/dL protein:200mg/dL lactate:6.8mmol/L ADA:NoneU/L
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

NARRATIVE_EN: A 22-year-old woman in the US South region in an active-duty military barracks setting presented to a tertiary emergency department with a 24-hour history of fever to 39.4 C, severe headache, neck stiffness, and petechial rash on her extremities. Examination on admission: temperature 39.4 C, Glasgow Coma Scale 13, neck stiffness, positive Kernig sign, petechial rash, no focal deficit. CSF showed opening pressure 26 cmH2O, white cell count 5,200 per cubic millimeter (90 percent neutrophils), glucose 22 mg/dL, protein 200 mg/dL. Gram stain revealed gram-negative diplococci; culture identified Neisseria meningitidis serogroup B. Anchored to Soeters 2020 MMWR CDC ABCs (PMID 32935747, US young-adult NM surveillance; military barracks an established outbreak setting). Outcome: survived no sequelae. Subphase 1.3 commit 5.3.4 wave 2, pre-adjudication hold_for_revision.

NARRATIVE_ES: Mujer de 22 anos en region sur de Estados Unidos, en cuartel militar en servicio activo, ingresada a urgencias terciarias con 24 horas de fiebre 39.4 C, cefalea intensa, rigidez de nuca y exantema petequial en extremidades. Examen: temperatura 39.4 C, escala de Glasgow 13, rigidez de nuca, signo de Kernig positivo, exantema petequial, sin deficit focal. Liquido cefalorraquideo mostro presion de apertura 26 cmH2O, leucocitos 5,200 por mm3 (90 por ciento neutrofilos), glucosa 22 mg/dL, proteina 200 mg/dL. Tincion de Gram con diplococos gramnegativos y cultivo Neisseria meningitidis serogrupo B. Anclaje en Soeters 2020 MMWR ABCs CDC (PMID 32935747, vigilancia adulto joven; cuartel militar como entorno de brote establecido). Subphase 1.3 commit 5.3.4 wave 2.

RATIONALE: Anchored to PMID 32935747 (Soeters 2020 MMWR CDC ABCs surveillance). Demographic anchor (22yo F young adult military barracks) sits in CDC-documented outbreak-setting stratum. CSF profile bacterial range; petechial rash + classic NM serogroup B. Imputation tiers: tier_1_primary={age, sex, csf_culture, csf_gram_stain, petechial_rash, military_barracks_setting}; tier_3_within_cohort={csf_wbc, neutrophil_pct, glucose, protein}; tier_4_priors={temp, gcs, symptom_days}. Indeterminate=none. Diagnostic_ambiguity=false. Outcome=survived_no_sequelae. Tier: tier_4_imputation_cdc_abcs_anchored. 5.3.4 wave2 NM-young-adult-military.

ANCHORING_EXTRAS: stage=pre_adjudication; status=pending_external_review; self_review_disposition=hold_for_revision; self_review_notes=wave 2 vignette anchored to PMID 32935747 (Soeters 2020 MMWR CDC ABCs); external clinical adjudication pending; classification provisional. adjudicator_ids=WAVE2-PRE-ADJ-1, WAVE2-PRE-ADJ-2 (sentinel); cohen_kappa=0.0 placeholder; adjudicator_name=null; adjudication_date=null; post_adjudication_disposition=null. Subphase 1.3 commit 5.3.4 (2026-05-08). anchor=Soeters-MMWR-CDC-ABCs-2020 stratum=young-adult-military.

ADJUDICATION:
  inclusion_decision: hold_for_revision  ground_truth_class: 2  kappa: 0.0
  adjudicator_ids: ['WAVE2-PRE-ADJ-1', 'WAVE2-PRE-ADJ-2']
  disagreement_resolution: None
```

#### Vignette: vid=086 file=bact_086_hib_cusco_pediatric.json class=2 subphase=1.3 BACT

```
ANCHOR:
  pmid: 32935747
  first_author: Soeters
  year: 2020
  journal: MMWR
  citation_type: surveillance
  doi: 10.15585/mmwr.mm6936a3

DEMOGRAPHICS:
  age_years: 3  sex: male  region: peru_cusco_altitude
  ethnicity: mestizo  altitude_m: 3399
  hiv_status: negative  cd4: None
  pregnancy_red_flag: False
  immunocompromise_status: none
  freshwater_exposure_14d: False (None)

HISTORY:
  symptom_onset_to_presentation_days: 2.5
  chief_complaint: altered_mental_status
  red_flags_present: []
  prodrome_description: 3-year-old male, Cusco Peru highlands (3,399 m). 60-hour gradual progression: fever 39.0 C, vomiting, decreasing responsiveness, neck stiffness. Recent otitis media. No freshwater. Vaccination history incomplete (Hib coverage not yet achieved). Outcome: survived no sequelae. Antibiotic at hour 2 plus dexamethasone.

VITALS:
  T:39.0C HR:142 BP:100/60 GCS:12 SpO2:92% RR:30

EXAM:
  mental_status: confused  neck_stiff: True  kernig_brudz: True
  cranial_nerve_palsy: none  papilledema: None  focal_deficit: False
  skin_lesion_centrofacial_chronic: False  rash: False

LABS:
  WBC:21500 Plt:285000 ALT/AST:26 CRP:195.0 PCT:7.5 Na:136

CSF:
  OP:28.0cmH2O  WBC:4800/mm3  lymph%:12 neut%:88 eos%:0
  glucose:22mg/dL protein:210mg/dL lactate:6.8mmol/L ADA:NoneU/L
  crag_lfa:negative  wet_mount:negative  xanthochromia:False  RBC:5

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
  serology_or_antigen: haemophilus_influenzae_type_b_positive
  smear_or_gram: n/a
  brain_biopsy: n/a

NARRATIVE_EN: A three-year-old boy from Cusco, Peru in the Andean highlands (3,399 m altitude residence) presented to a tertiary pediatric emergency department with a 60-hour gradual progression of fever to 39.0 C, vomiting, decreasing responsiveness, and neck stiffness. He had been treated for otitis media in the preceding week; vaccination history showed incomplete Hib coverage. Examination on admission: temperature 39.0 C, Glasgow Coma Scale 12, neck stiffness, positive Kernig sign, no focal deficit, no rash. CSF showed opening pressure 28 cmH2O, white cell count 4,800 per cubic millimeter (88 percent neutrophils), glucose 22 mg/dL, protein 210 mg/dL. Gram stain revealed gram-negative coccobacilli; culture identified Haemophilus influenzae type b; CSF Hib capsular antigen positive. Anchored to Soeters 2020 MMWR CDC ABCs (PMID 32935747) Hib surveillance overlaid with incomplete-vaccination-coverage Andean stratum. Outcome: survived no sequelae. Subphase 1.3 commit 5.3.4 wave 2, pre-adjudication hold_for_revision.

NARRATIVE_ES: Varon de tres anos de Cusco Peru en sierra andina (3,399 m), ingresado a urgencias pediatricas terciarias con 60 horas de progresion gradual: fiebre 39.0 C, vomitos, respuesta disminuida y rigidez de nuca. Tratamiento previo para otitis media en la semana anterior; cobertura vacunal Hib incompleta. Examen: temperatura 39.0 C, escala de Glasgow 12, rigidez de nuca, signo de Kernig positivo, sin deficit focal, sin exantema. Liquido cefalorraquideo mostro presion de apertura 28 cmH2O, leucocitos 4,800 por mm3 (88 por ciento neutrofilos), glucosa 22 mg/dL, proteina 210 mg/dL. Tincion de Gram con cocobacilos gramnegativos y cultivo Haemophilus influenzae tipo b; antigeno Hib en liquido positivo. Anclaje en Soeters 2020 MMWR ABCs CDC (PMID 32935747). Subphase 1.3 commit 5.3.4 wave 2.

RATIONALE: Anchored to PMID 32935747 (Soeters 2020 MMWR CDC ABCs) surveillance overlaid with Andean-pediatric incomplete-Hib-coverage stratum (Cusco altitude region 3,399m). Demographic anchor (3yo M Cusco pediatric undervaccinated post-otitis-media) sits in surveillance gap stratum. CSF bacterial range; Gram stain + culture + antigen all confirm Hib. Imputation tiers: tier_1_primary={age, sex, region, csf_culture, csf_gram_stain, csf_hib_antigen, otitis_media}; tier_3_within_cohort={csf_wbc, neutrophil_pct, glucose, protein}; tier_4_priors={temp, gcs, symptom_days}. Indeterminate=papilledema_on_fundoscopy. Diagnostic_ambiguity=false. Outcome=survived. Tier: tier_4_imputation_cdc_abcs_anchored. 5.3.4 wave2 Hib-Cusco-pediatric.

ANCHORING_EXTRAS: stage=pre_adjudication; status=pending_external_review; self_review_disposition=hold_for_revision; self_review_notes=wave 2 vignette anchored to PMID 32935747 (Soeters 2020 MMWR CDC ABCs); external clinical adjudication pending; classification provisional. adjudicator_ids=WAVE2-PRE-ADJ-1, WAVE2-PRE-ADJ-2 (sentinel); cohen_kappa=0.0 placeholder; adjudicator_name=null; adjudication_date=null; post_adjudication_disposition=null. Subphase 1.3 commit 5.3.4 (2026-05-08). anchor=Soeters-MMWR-CDC-ABCs-2020 stratum=pediatric-Cusco-altitude.

ADJUDICATION:
  inclusion_decision: hold_for_revision  ground_truth_class: 2  kappa: 0.0
  adjudicator_ids: ['WAVE2-PRE-ADJ-1', 'WAVE2-PRE-ADJ-2']
  disagreement_resolution: None
```

#### Vignette: vid=087 file=bact_087_hib_unimmunized_infant.json class=2 subphase=1.3 BACT

```
ANCHOR:
  pmid: 32935747
  first_author: Soeters
  year: 2020
  journal: MMWR
  citation_type: surveillance
  doi: 10.15585/mmwr.mm6936a3

DEMOGRAPHICS:
  age_years: 1  sex: male  region: us_south
  ethnicity: white_non_hispanic  altitude_m: 100
  hiv_status: negative  cd4: None
  pregnancy_red_flag: False
  immunocompromise_status: none
  freshwater_exposure_14d: False (None)

HISTORY:
  symptom_onset_to_presentation_days: 2.0
  chief_complaint: altered_mental_status
  red_flags_present: []
  prodrome_description: 18-month-old male, US South region. Parents declined vaccinations; no Hib coverage. 48-hour fever 39.2 C, vomiting, irritability progressing to lethargy, bulging fontanelle. Tertiary pediatric ED. No freshwater. Outcome: survived no sequelae. Antibiotic at hour 1.5 plus dexamethasone IDSA pediatric protocol.

VITALS:
  T:39.2C HR:156 BP:92/56 GCS:12 SpO2:95% RR:32

EXAM:
  mental_status: confused  neck_stiff: True  kernig_brudz: True
  cranial_nerve_palsy: none  papilledema: None  focal_deficit: False
  skin_lesion_centrofacial_chronic: False  rash: False

LABS:
  WBC:24500 Plt:295000 ALT/AST:28 CRP:215.0 PCT:9.8 Na:135

CSF:
  OP:30.0cmH2O  WBC:6200/mm3  lymph%:10 neut%:90 eos%:0
  glucose:20mg/dL protein:230mg/dL lactate:7.4mmol/L ADA:NoneU/L
  crag_lfa:negative  wet_mount:negative  xanthochromia:False  RBC:6

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
  serology_or_antigen: haemophilus_influenzae_type_b_positive
  smear_or_gram: n/a
  brain_biopsy: n/a

NARRATIVE_EN: An 18-month-old boy in the US South region whose parents had declined vaccinations, including the Hib series, presented to a tertiary pediatric emergency department with a 48-hour history of fever to 39.2 C, vomiting, irritability progressing to lethargy, and a bulging anterior fontanelle. Examination on admission: temperature 39.2 C, Glasgow Coma Scale 12, neck stiffness, positive Kernig sign, no focal deficit, no rash. CSF showed opening pressure 30 cmH2O, white cell count 6,200 per cubic millimeter (90 percent neutrophils), glucose 20 mg/dL, protein 230 mg/dL. Gram stain revealed gram-negative coccobacilli; culture identified Haemophilus influenzae type b; CSF Hib capsular antigen positive. Anchored to Soeters 2020 MMWR CDC ABCs (PMID 32935747) Hib surveillance, undervaccinated-infant resurgence stratum. Outcome: survived no sequelae. Subphase 1.3 commit 5.3.4 wave 2, pre-adjudication hold_for_revision.

NARRATIVE_ES: Lactante varon de 18 meses en region sur de Estados Unidos, cuyos padres habian declinado las vacunas (incluida la serie Hib), ingresado a urgencias pediatricas terciarias con 48 horas de fiebre 39.2 C, vomitos, irritabilidad con progresion a letargo y fontanela anterior abombada. Examen: temperatura 39.2 C, escala de Glasgow 12, rigidez de nuca, signo de Kernig positivo, sin deficit focal, sin exantema. Liquido cefalorraquideo mostro presion de apertura 30 cmH2O, leucocitos 6,200 por mm3 (90 por ciento neutrofilos), glucosa 20 mg/dL, proteina 230 mg/dL. Tincion de Gram con cocobacilos gramnegativos y cultivo Haemophilus influenzae tipo b; antigeno Hib positivo. Anclaje en Soeters 2020 MMWR ABCs CDC (PMID 32935747, estrato lactante no vacunado). Subphase 1.3 commit 5.3.4 wave 2.

RATIONALE: Anchored to PMID 32935747 (Soeters 2020 MMWR CDC ABCs) Hib surveillance with undervaccinated-infant resurgence stratum. Demographic anchor (18mo M unimmunized Hib) sits in post-vaccine-era resurgence stratum documented by ABCs. CSF bacterial range; Gram + culture + antigen all confirm Hib. Imputation tiers: tier_1_primary={age, sex, csf_culture, csf_gram_stain, csf_hib_antigen, vaccine_decline}; tier_3_within_cohort={csf_wbc, neutrophil_pct, glucose, protein}; tier_4_priors={temp, gcs, hr, symptom_days}. Indeterminate=papilledema_on_fundoscopy. Diagnostic_ambiguity=false. Outcome=survived. Tier: tier_4_imputation_cdc_abcs_anchored. 5.3.4 wave2 Hib-unimmunized-infant.

ANCHORING_EXTRAS: stage=pre_adjudication; status=pending_external_review; self_review_disposition=hold_for_revision; self_review_notes=wave 2 vignette anchored to PMID 32935747 (Soeters 2020 MMWR CDC ABCs); external clinical adjudication pending; classification provisional. adjudicator_ids=WAVE2-PRE-ADJ-1, WAVE2-PRE-ADJ-2 (sentinel); cohen_kappa=0.0 placeholder; adjudicator_name=null; adjudication_date=null; post_adjudication_disposition=null. Subphase 1.3 commit 5.3.4 (2026-05-08). anchor=Soeters-MMWR-CDC-ABCs-2020 stratum=undervaccinated-infant.

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
