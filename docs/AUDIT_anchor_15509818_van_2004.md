# AUDIT bundle: PMID 15509818 | van 2004

Generated: 2026-05-11
Vignettes in bundle: 5
Build status: NCBI fetched
Bundle type: BIG (n>=5 vignettes single-anchor)

## Anchor: PMID 15509818 | van 2004

### Registry metadata (current state)

```json
{
  "pmid": "15509818",
  "doi": "10.1056/NEJMoa040845",
  "authors_short": "van de Beek D et al.",
  "authors_full": [
    "van de Beek D",
    "de Gans J",
    "Spanjaard L",
    "Weisfelt M",
    "Reitsma JB",
    "Vermeulen M"
  ],
  "journal": "N Engl J Med",
  "journal_short_code": "NEJM",
  "year": 2004,
  "volume": "351",
  "issue": "18",
  "pages": "1849-1859",
  "title": "Clinical features and prognostic factors in adults with bacterial meningitis",
  "anchor_type": "cohort",
  "anchor_subtype": "netherlands_adult_community_bacterial_meningitis_696_episodes",
  "verification_confidence": 0.85,
  "verification_method": "consensus_anchor_subphase_1_3_initial",
  "last_verified_date": "2026-05-06",
  "caveat": "Landmark Netherlands prospective cohort of 696 adult community-acquired bacterial meningitis episodes 1998-2002. Anchor for Class 2 SP-adult and NM-adult vignettes (presentation tetrad: fever, neck stiffness, altered mental status, plus headache). verification_confidence=0.85 indicates consensus anchor without PubMed UI direct fetch in commit 5.3.1; primary-source pull will follow in subsequent Subphase 1.3 commits."
}
```

### NCBI live re-fetch (2026-05-11)

```json
{
  "uid": "15509818",
  "pubdate": "2004 Oct 28",
  "epubdate": "",
  "source": "N Engl J Med",
  "authors": [
    {
      "name": "van de Beek D",
      "authtype": "Author",
      "clusterid": ""
    },
    {
      "name": "de Gans J",
      "authtype": "Author",
      "clusterid": ""
    },
    {
      "name": "Spanjaard L",
      "authtype": "Author",
      "clusterid": ""
    },
    {
      "name": "Weisfelt M",
      "authtype": "Author",
      "clusterid": ""
    },
    {
      "name": "Reitsma JB",
      "authtype": "Author",
      "clusterid": ""
    },
    {
      "name": "Vermeulen M",
      "authtype": "Author",
      "clusterid": ""
    }
  ],
  "lastauthor": "Vermeulen M",
  "title": "Clinical features and prognostic factors in adults with bacterial meningitis.",
  "sorttitle": "clinical features and prognostic factors in adults with bacterial meningitis",
  "volume": "351",
  "issue": "18",
  "pages": "1849-59",
  "lang": [
    "eng"
  ],
  "nlmuniqueid": "0255562",
  "issn": "0028-4793",
  "essn": "1533-4406",
  "pubtype": [
    "Journal Article",
    "Research Support, Non-U.S. Gov't"
  ],
  "recordstatus": "PubMed - indexed for MEDLINE",
  "pubstatus": "4",
  "articleids": [
    {
      "idtype": "pubmed",
      "idtypen": 1,
      "value": "15509818"
    },
    {
      "idtype": "doi",
      "idtypen": 3,
      "value": "10.1056/NEJMoa040845"
    },
    {
      "idtype": "pii",
      "idtypen": 4,
      "value": "351/18/1849"
    }
  ],
  "history": [
    {
      "pubstatus": "pubmed",
      "date": "2004/10/29 09:00"
    },
    {
      "pubstatus": "medline",
      "date": "2004/11/04 09:00"
    },
    {
      "pubstatus": "entrez",
      "date": "2004/10/29 09:00"
    }
  ],
  "references": [
    {
      "refsource": "N Engl J Med. 2005 Mar 3;352(9):950",
      "reftype": "Erratum in",
      "pmid": "",
      "note": ""
    },
    {
      "refsource": "N Engl J Med. 2005 Feb 3;352(5):512-5; author reply 512-5. doi: 10.1056/NEJM200502033520519.",
      "reftype": "Comment in",
      "pmid": 15689595,
      "note": ""
    },
    {
      "refsource": "N Engl J Med. 2005 Feb 3;352(5):512-5; author reply 512-5.",
      "reftype": "Comment in",
      "pmid": 15690600,
      "note": ""
    },
    {
      "refsource": "N Engl J Med. 2005 Feb 3;352(5):512-5; author reply 512-5.",
      "reftype": "Comment in",
      "pmid": 15690602,
      "note": ""
    }
  ],
  "attributes": [
    "Has Abstract"
  ],
  "pmcrefcount": "",
  "fulljournalname": "The New England journal of medicine",
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
  "sortpubdate": "2004/10/28 00:00",
  "sortfirstauthor": "van de Beek D",
  "vernaculartitle": ""
}
```

### Registry-vs-NCBI delta

- **pages**: registry='1849-1859' | ncbi='1849-59'

### Vignettes citing this anchor (5 total)

#### Vignette: vid=062 file=bact_062_sp_netherlands_adult.json class=2 subphase=1.3 BACT

```
ANCHOR:
  pmid: 15509818
  first_author: van
  year: 2004
  journal: NEJM
  citation_type: cohort
  doi: 10.1056/NEJMoa040845

DEMOGRAPHICS:
  age_years: 55  sex: female  region: other_global
  ethnicity: white_non_hispanic  altitude_m: 5
  hiv_status: negative  cd4: None
  pregnancy_red_flag: False
  immunocompromise_status: none
  freshwater_exposure_14d: False (None)

HISTORY:
  symptom_onset_to_presentation_days: 1.0
  chief_complaint: fever_with_headache
  red_flags_present: []
  prodrome_description: 55-year-old female, Netherlands. 24-hour rapid progression: fever 39.2 C, severe headache, neck stiffness, photophobia, nausea. Tertiary ED Amsterdam. No rash. No freshwater. No immunocompromise. Classic triad present (44 percent cohort marker). Outcome: survived with mild cognitive impairment. Antibiotic at hour 1 plus dexamethasone (post-2002 EU guideline).

VITALS:
  T:39.2C HR:112 BP:130/80 GCS:11 SpO2:96% RR:22

EXAM:
  mental_status: somnolent  neck_stiff: True  kernig_brudz: True
  cranial_nerve_palsy: none  papilledema: False  focal_deficit: False
  skin_lesion_centrofacial_chronic: False  rash: False

LABS:
  WBC:18500 Plt:240000 ALT/AST:32 CRP:195.0 PCT:8.5 Na:137

CSF:
  OP:28.0cmH2O  WBC:3200/mm3  lymph%:12 neut%:88 eos%:0
  glucose:22mg/dL protein:195mg/dL lactate:6.4mmol/L ADA:NoneU/L
  crag_lfa:negative  wet_mount:negative  xanthochromia:False  RBC:5

IMAGING:
  modality: ct_noncontrast  pattern: normal
  finding_count: 0
  text_summary: CT head non-contrast: normal at admission, no focal lesion, no hydrocephalus, no mass effect. Initial imaging in adult community-acquired bacterial meningitis is typically normal.

DIAGNOSTIC_TESTS:
  total_results: 3
  pcr_panel: n/a
  xpert_mtb_rif: n/a
  blood_culture: n/a
  csf_culture: n/a
  serology_or_antigen: n/a
  smear_or_gram: n/a
  brain_biopsy: n/a

NARRATIVE_EN: A 55-year-old woman in the Netherlands (Amsterdam) presented to a tertiary emergency department with a 24-hour rapid progression of fever to 39.2 C, severe headache, neck stiffness, photophobia, and nausea. Examination on admission: temperature 39.2 C, Glasgow Coma Scale 11, neck stiffness, positive Kernig sign, no focal deficit, no rash. Classic triad present (this case sits in the 44 percent triad-positive subgroup of the van de Beek 2004 cohort). CSF showed opening pressure 28 cmH2O, white cell count 3,200 per cubic millimeter (88 percent neutrophils), glucose 22 mg/dL, protein 195 mg/dL. Gram stain revealed gram-positive diplococci; culture identified Streptococcus pneumoniae. Primary anchor: PMID 15509818 (van de Beek 2004 NEJM), 696-episode prospective Netherlands community-acquired adult bacterial meningitis cohort 1998-2002 (SP 51 percent, SP mortality 30 percent). Outcome: survived with mild cognitive impairment. Subphase 1.3 commit 5.3.2 pilot 2, pre-adjudication hold_for_revision.

NARRATIVE_ES: Mujer de 55 anos, Paises Bajos (Amsterdam), ingresada a urgencias terciarias con un dia de progresion rapida: fiebre 39.2 C, cefalea intensa, rigidez de nuca, fotofobia, nauseas. Examen: temperatura 39.2 C, escala de Glasgow 11, rigidez de nuca, signo de Kernig positivo, sin deficit focal, sin exantema. Triada clasica presente (subgrupo del 44 por ciento triada-positiva de la cohorte van de Beek 2004). Liquido cefalorraquideo mostro presion de apertura 28 cmH2O, leucocitos 3,200 por mm3 (88 por ciento neutrofilos), glucosa 22 mg/dL, proteina 195 mg/dL. Tincion de Gram con diplococos grampositivos y cultivo Streptococcus pneumoniae. Anclaje primario en cohorte prospectiva neerlandesa (PMID 15509818, van de Beek 2004 NEJM, 696 episodios 1998-2002, SP 51 por ciento, mortalidad SP 30 por ciento). Subphase 1.3 commit 5.3.2 pilot 2.

RATIONALE: Anchored to PMID 15509818 (van de Beek 2004 NEJM), 696-episode prospective Netherlands community-acquired adult bacterial meningitis cohort 1998-2002 (SP 51 percent, classic triad 44 percent, SP mortality 30 percent, unfavorable 34 percent). Demographic anchor (55yo F) within cohort age range. CSF profile bacterial range per Tunkel IDSA 2004 (PMID 15494903). Triad present (44 percent cohort marker). Imputation tiers: tier_1_primary={age, sex, csf_culture, csf_gram_stain, triad}; tier_3_within_cohort={csf_wbc, csf_neutrophil_pct, csf_glucose, csf_protein, gcs}; tier_4_priors={temperature_celsius, symptom_onset_days}. Indeterminate=none. Diagnostic_ambiguity=false. Outcome=survived_mild_cognitive_impairment per 34 percent unfavorable rate. Abx_hours=1. Dexamethasone=true (post-2002 EU guideline). Tier: primary_source_direct. 5.3.2 pilot 2.

ANCHORING_EXTRAS: stage=pre_adjudication; status=pending_external_review; self_review_disposition=hold_for_revision; self_review_notes=pilot vignette anchored to PMID 15509818 (van de Beek 2004 NEJM NL adult); external clinical adjudication pending; classification provisional. adjudicator_ids=PILOT-PRE-ADJ-1, PILOT-PRE-ADJ-2 (sentinel); cohen_kappa=0.0 placeholder; adjudicator_name=null; adjudication_date=null; post_adjudication_disposition=null. Subphase 1.3 commit 5.3.2 (2026-05-07).

ADJUDICATION:
  inclusion_decision: hold_for_revision  ground_truth_class: 2  kappa: 0.0
  adjudicator_ids: ['PILOT-PRE-ADJ-1', 'PILOT-PRE-ADJ-2']
  disagreement_resolution: None
```

#### Vignette: vid=066 file=bact_066_sp_alcoholic_fatal.json class=2 subphase=1.3 BACT

```
ANCHOR:
  pmid: 15509818
  first_author: van
  year: 2004
  journal: NEJM
  citation_type: cohort
  doi: 10.1056/NEJMoa040845

DEMOGRAPHICS:
  age_years: 68  sex: male  region: other_global
  ethnicity: white_non_hispanic  altitude_m: 5
  hiv_status: negative  cd4: None
  pregnancy_red_flag: False
  immunocompromise_status: none
  freshwater_exposure_14d: False (None)

HISTORY:
  symptom_onset_to_presentation_days: 3.0
  chief_complaint: altered_mental_status
  red_flags_present: []
  prodrome_description: 68-year-old male, Netherlands. 3-day course: progressive fever, headache, confusion. Chronic alcohol use 30 years. Tertiary ED Amsterdam. Late presentation; admitted obtunded. No freshwater. Triad present (van de Beek alcoholic stratum). Outcome: fatal hospital day 4. Antibiotic at hour 3 plus dexamethasone.

VITALS:
  T:39.5C HR:124 BP:102/62 GCS:8 SpO2:92% RR:28

EXAM:
  mental_status: stuporous  neck_stiff: True  kernig_brudz: True
  cranial_nerve_palsy: none  papilledema: False  focal_deficit: False
  skin_lesion_centrofacial_chronic: False  rash: False

LABS:
  WBC:19500 Plt:165000 ALT/AST:88 CRP:245.0 PCT:14.5 Na:132

CSF:
  OP:28.0cmH2O  WBC:5400/mm3  lymph%:12 neut%:88 eos%:0
  glucose:22mg/dL protein:220mg/dL lactate:6.8mmol/L ADA:NoneU/L
  crag_lfa:negative  wet_mount:negative  xanthochromia:False  RBC:4

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

NARRATIVE_EN: A 68-year-old man in the Netherlands presented to a tertiary emergency department in Amsterdam after a 3-day course of progressive fever, headache, and confusion. He had a 30-year history of chronic alcohol use. He was obtunded on arrival. Examination on admission: temperature 39.5 C, Glasgow Coma Scale 8, neck stiffness, positive Kernig sign, no focal deficit, no rash. CSF showed opening pressure 28 cmH2O, white cell count 5,400 per cubic millimeter (88 percent neutrophils), glucose 22 mg/dL, protein 220 mg/dL. Gram stain revealed gram-positive diplococci; culture identified Streptococcus pneumoniae. Primary anchor: PMID 15509818 (van de Beek 2004 NEJM), 696-episode prospective Netherlands cohort 1998-2002 (alcoholic stratum mortality elevated). Outcome: fatal hospital day 4. Subphase 1.3 commit 5.3.3 wave 1, pre-adjudication hold_for_revision.

NARRATIVE_ES: Varon de 68 anos en Paises Bajos (Amsterdam), ingresado a urgencias terciarias tras tres dias de fiebre progresiva, cefalea y confusion. Antecedente de consumo cronico de alcohol durante 30 anos. Ingreso obnubilado. Examen: temperatura 39.5 C, escala de Glasgow 8, rigidez de nuca, signo de Kernig positivo, sin deficit focal, sin exantema. Liquido cefalorraquideo mostro presion de apertura 28 cmH2O, leucocitos 5,400 por mm3 (88 por ciento neutrofilos), glucosa 22 mg/dL, proteina 220 mg/dL. Tincion de Gram con diplococos grampositivos y cultivo Streptococcus pneumoniae. Anclaje primario en cohorte prospectiva van de Beek 2004 NEJM (PMID 15509818, 696 episodios 1998-2002, estrato alcoholico con mortalidad elevada). Resultado: fatal en hospital dia 4. Subphase 1.3 commit 5.3.3 wave 1, pre-adjudicacion hold_for_revision.

RATIONALE: Anchored to PMID 15509818 (van de Beek 2004 NEJM), 696-episode prospective Netherlands cohort 1998-2002 (SP 51 percent, SP mortality 30 percent, alcoholic stratum mortality elevated). Demographic anchor (68yo M chronic alcohol) sits in elderly alcoholic stratum. CSF profile bacterial range. Imputation tiers: tier_1_primary={age, sex, csf_culture, csf_gram_stain, alcohol risk}; tier_3_within_cohort={csf_wbc, neutrophil_pct, glucose, protein, gcs}; tier_4_priors={temp, symptom_days}. Indeterminate=none. Diagnostic_ambiguity=false. Outcome=fatal_hospital_day_4. Antibiotic_started_hours=3. Tier: tier_3_imputation_within_cohort_review. 5.3.3 wave1 SP-alcoholic-fatal.

ANCHORING_EXTRAS: stage=pre_adjudication; status=pending_external_review; self_review_disposition=hold_for_revision; self_review_notes=wave 1 vignette anchored to PMID 15509818 (van de Beek 2004 NEJM); external clinical adjudication pending; classification provisional. adjudicator_ids=WAVE1-PRE-ADJ-1, WAVE1-PRE-ADJ-2 (sentinel); cohen_kappa=0.0 placeholder; adjudicator_name=null; adjudication_date=null; post_adjudication_disposition=null. Subphase 1.3 commit 5.3.3 (2026-05-08). anchor=van-de-Beek-NEJM-2004 stratum=alcoholic-elderly.

ADJUDICATION:
  inclusion_decision: hold_for_revision  ground_truth_class: 2  kappa: 0.0
  adjudicator_ids: ['WAVE1-PRE-ADJ-1', 'WAVE1-PRE-ADJ-2']
  disagreement_resolution: None
```

#### Vignette: vid=073 file=bact_073_sp_elderly_fatal.json class=2 subphase=1.3 BACT

```
ANCHOR:
  pmid: 15509818
  first_author: van
  year: 2004
  journal: NEJM
  citation_type: cohort
  doi: 10.1056/NEJMoa040845

DEMOGRAPHICS:
  age_years: 70  sex: female  region: other_global
  ethnicity: white_non_hispanic  altitude_m: 5
  hiv_status: negative  cd4: None
  pregnancy_red_flag: False
  immunocompromise_status: none
  freshwater_exposure_14d: False (None)

HISTORY:
  symptom_onset_to_presentation_days: 4.0
  chief_complaint: altered_mental_status
  red_flags_present: []
  prodrome_description: 70-year-old female, Netherlands. 4-day progressive fever, headache, confusion progressing to obtundation. Tertiary ED Amsterdam. Late presentation. No freshwater. Triad present (van de Beek elderly stratum). Outcome: fatal hospital day 3. Antibiotic at hour 2 plus dexamethasone EU guideline 2002.

VITALS:
  T:38.9C HR:116 BP:105/65 GCS:7 SpO2:91% RR:26

EXAM:
  mental_status: comatose  neck_stiff: True  kernig_brudz: True
  cranial_nerve_palsy: none  papilledema: False  focal_deficit: False
  skin_lesion_centrofacial_chronic: False  rash: False

LABS:
  WBC:18800 Plt:175000 ALT/AST:36 CRP:230.0 PCT:12.5 Na:130

CSF:
  OP:26.0cmH2O  WBC:4100/mm3  lymph%:20 neut%:80 eos%:0
  glucose:25mg/dL protein:195mg/dL lactate:6.0mmol/L ADA:NoneU/L
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

NARRATIVE_EN: A 70-year-old woman in the Netherlands presented to a tertiary emergency department in Amsterdam after a 4-day course of progressive fever, headache, and confusion progressing to obtundation. Examination on admission: temperature 38.9 C, Glasgow Coma Scale 7, neck stiffness, positive Kernig sign, no focal deficit, no rash. CSF showed opening pressure 26 cmH2O, white cell count 4,100 per cubic millimeter (80 percent neutrophils), glucose 25 mg/dL, protein 195 mg/dL. Gram stain revealed gram-positive diplococci; culture identified Streptococcus pneumoniae. Primary anchor: PMID 15509818 (van de Beek 2004 NEJM), elderly stratum mortality 41 percent. Outcome: fatal hospital day 3. Subphase 1.3 commit 5.3.3 wave 1, pre-adjudication hold_for_revision.

NARRATIVE_ES: Mujer de 70 anos en Paises Bajos (Amsterdam), ingresada a urgencias terciarias tras cuatro dias de fiebre progresiva, cefalea y confusion con obnubilacion. Examen: temperatura 38.9 C, escala de Glasgow 7, rigidez de nuca, signo de Kernig positivo, sin deficit focal, sin exantema. Liquido cefalorraquideo mostro presion de apertura 26 cmH2O, leucocitos 4,100 por mm3 (80 por ciento neutrofilos), glucosa 25 mg/dL, proteina 195 mg/dL. Tincion de Gram con diplococos grampositivos y cultivo Streptococcus pneumoniae. Anclaje primario en cohorte prospectiva van de Beek 2004 NEJM (PMID 15509818, 696 episodios 1998-2002, estrato de adultos mayores con mortalidad 41 por ciento a edad >=65). Resultado: fatal en hospital dia 3. Subphase 1.3 commit 5.3.3 wave 1, pre-adjudicacion hold_for_revision.

RATIONALE: Anchored to PMID 15509818 (van de Beek 2004 NEJM), 696-episode prospective Netherlands cohort 1998-2002 (elderly stratum mortality 41 percent at age >=65). Demographic anchor (70yo F) sits in elderly stratum. CSF profile bacterial range. Imputation tiers: tier_1_primary={age, sex, csf_culture, csf_gram_stain}; tier_3_within_cohort={csf_wbc, neutrophil_pct, glucose, protein, gcs}; tier_4_priors={temp, symptom_days}. Indeterminate=none. Diagnostic_ambiguity=false. Outcome=fatal_hospital_day_3. Antibiotic_started_hours=2. Tier: tier_3_imputation_within_cohort_review. 5.3.3 wave1 SP-elderly-fatal.

ANCHORING_EXTRAS: stage=pre_adjudication; status=pending_external_review; self_review_disposition=hold_for_revision; self_review_notes=wave 1 vignette anchored to PMID 15509818 (van de Beek 2004 NEJM); external clinical adjudication pending; classification provisional. adjudicator_ids=WAVE1-PRE-ADJ-1, WAVE1-PRE-ADJ-2 (sentinel); cohen_kappa=0.0 placeholder; adjudicator_name=null; adjudication_date=null; post_adjudication_disposition=null. Subphase 1.3 commit 5.3.3 (2026-05-08). anchor=van-de-Beek-NEJM-2004 stratum=elderly-fatal.

ADJUDICATION:
  inclusion_decision: hold_for_revision  ground_truth_class: 2  kappa: 0.0
  adjudicator_ids: ['WAVE1-PRE-ADJ-1', 'WAVE1-PRE-ADJ-2']
  disagreement_resolution: None
```

#### Vignette: vid=077 file=bact_077_sp_young_adult.json class=2 subphase=1.3 BACT

```
ANCHOR:
  pmid: 15509818
  first_author: van
  year: 2004
  journal: NEJM
  citation_type: cohort
  doi: 10.1056/NEJMoa040845

DEMOGRAPHICS:
  age_years: 18  sex: female  region: other_global
  ethnicity: white_non_hispanic  altitude_m: 5
  hiv_status: negative  cd4: None
  pregnancy_red_flag: False
  immunocompromise_status: none
  freshwater_exposure_14d: False (None)

HISTORY:
  symptom_onset_to_presentation_days: 0.5
  chief_complaint: fever_with_headache
  red_flags_present: []
  prodrome_description: 18-year-old female, Netherlands. Sudden onset fever 39.5 C, severe headache, neck stiffness, photophobia within 12 hours. Tertiary ED Amsterdam. No freshwater. Triad present (van de Beek young-adult subgroup). Outcome: survived no sequelae. Antibiotic at hour 1 plus dexamethasone EU guideline.

VITALS:
  T:39.5C HR:122 BP:115/70 GCS:13 SpO2:97% RR:22

EXAM:
  mental_status: confused  neck_stiff: True  kernig_brudz: True
  cranial_nerve_palsy: none  papilledema: False  focal_deficit: False
  skin_lesion_centrofacial_chronic: False  rash: False

LABS:
  WBC:21500 Plt:285000 ALT/AST:28 CRP:195.0 PCT:8.0 Na:138

CSF:
  OP:28.0cmH2O  WBC:6400/mm3  lymph%:12 neut%:88 eos%:0
  glucose:24mg/dL protein:210mg/dL lactate:6.6mmol/L ADA:NoneU/L
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

NARRATIVE_EN: An 18-year-old woman in the Netherlands presented to a tertiary emergency department in Amsterdam with sudden onset of fever to 39.5 C, severe headache, neck stiffness, and photophobia within 12 hours. Examination on admission: temperature 39.5 C, Glasgow Coma Scale 13, neck stiffness, positive Kernig sign, no focal deficit, no rash. Classic triad present (this case sits in the young-adult subgroup of the van de Beek 2004 cohort). CSF showed opening pressure 28 cmH2O, white cell count 6,400 per cubic millimeter (88 percent neutrophils), glucose 24 mg/dL, protein 210 mg/dL. Gram stain revealed gram-positive diplococci; culture identified Streptococcus pneumoniae. Primary anchor: PMID 15509818 (van de Beek 2004 NEJM), 696-episode prospective Netherlands cohort 1998-2002 (SP 51 percent, classic triad 44 percent). Outcome: survived no sequelae. Subphase 1.3 commit 5.3.3 wave 1, pre-adjudication hold_for_revision.

NARRATIVE_ES: Mujer de 18 anos en Paises Bajos (Amsterdam), ingresada a urgencias terciarias con inicio subito de fiebre 39.5 C, cefalea intensa, rigidez de nuca y fotofobia en 12 horas. Examen: temperatura 39.5 C, escala de Glasgow 13, rigidez de nuca, signo de Kernig positivo, sin deficit focal, sin exantema. Triada clasica presente (subgrupo de adultos jovenes de la cohorte van de Beek 2004). Liquido cefalorraquideo mostro presion de apertura 28 cmH2O, leucocitos 6,400 por mm3 (88 por ciento neutrofilos), glucosa 24 mg/dL, proteina 210 mg/dL. Tincion de Gram con diplococos grampositivos y cultivo Streptococcus pneumoniae. Anclaje primario en cohorte van de Beek 2004 NEJM (PMID 15509818). Subphase 1.3 commit 5.3.3 wave 1.

RATIONALE: Anchored to PMID 15509818 (van de Beek 2004 NEJM), 696-episode prospective Netherlands cohort 1998-2002 (SP 51 percent, classic triad 44 percent). Demographic anchor (18yo F young adult) sits in young-adult subgroup. CSF profile bacterial range. Imputation tiers: tier_1_primary={age, sex, csf_culture, csf_gram_stain, triad}; tier_3_within_cohort={csf_wbc, neutrophil_pct, glucose, protein, gcs}; tier_4_priors={temp, symptom_days}. Indeterminate=none. Diagnostic_ambiguity=false. Outcome=survived. Antibiotic_started_hours=1. Tier: tier_3_imputation_within_cohort_review. 5.3.3 wave1 SP-young-adult.

ANCHORING_EXTRAS: stage=pre_adjudication; status=pending_external_review; self_review_disposition=hold_for_revision; self_review_notes=wave 1 vignette anchored to PMID 15509818 (van de Beek 2004 NEJM); external clinical adjudication pending; classification provisional. adjudicator_ids=WAVE1-PRE-ADJ-1, WAVE1-PRE-ADJ-2 (sentinel); cohen_kappa=0.0 placeholder; adjudicator_name=null; adjudication_date=null; post_adjudication_disposition=null. Subphase 1.3 commit 5.3.3 (2026-05-08). anchor=van-de-Beek-NEJM-2004 stratum=young-adult.

ADJUDICATION:
  inclusion_decision: hold_for_revision  ground_truth_class: 2  kappa: 0.0
  adjudicator_ids: ['WAVE1-PRE-ADJ-1', 'WAVE1-PRE-ADJ-2']
  disagreement_resolution: None
```

#### Vignette: vid=081 file=bact_081_sp_elderly_fatal.json class=2 subphase=1.3 BACT

```
ANCHOR:
  pmid: 15509818
  first_author: van
  year: 2004
  journal: NEJM
  citation_type: cohort
  doi: 10.1056/NEJMoa040845

DEMOGRAPHICS:
  age_years: 79  sex: female  region: other_global
  ethnicity: white_non_hispanic  altitude_m: 5
  hiv_status: negative  cd4: None
  pregnancy_red_flag: False
  immunocompromise_status: none
  freshwater_exposure_14d: False (None)

HISTORY:
  symptom_onset_to_presentation_days: 5.0
  chief_complaint: altered_mental_status
  red_flags_present: []
  prodrome_description: 79-year-old female, Netherlands. 5-day progressive fever, headache, confusion progressing to coma. Tertiary ED Amsterdam. Late presentation, GCS 6 on admission. No freshwater. Triad present (van de Beek elderly subgroup mortality 51 percent at age >=70). Outcome: fatal hospital day 2.

VITALS:
  T:38.7C HR:124 BP:96/56 GCS:6 SpO2:89% RR:30

EXAM:
  mental_status: comatose  neck_stiff: True  kernig_brudz: True
  cranial_nerve_palsy: none  papilledema: False  focal_deficit: False
  skin_lesion_centrofacial_chronic: False  rash: False

LABS:
  WBC:20100 Plt:145000 ALT/AST:42 CRP:245.0 PCT:16.0 Na:128

CSF:
  OP:24.0cmH2O  WBC:3800/mm3  lymph%:22 neut%:78 eos%:0
  glucose:28mg/dL protein:170mg/dL lactate:5.6mmol/L ADA:NoneU/L
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

NARRATIVE_EN: A 79-year-old woman in the Netherlands presented to a tertiary emergency department in Amsterdam after a 5-day course of progressive fever, headache, and confusion progressing to coma. She arrived with Glasgow Coma Scale 6. Examination on admission: temperature 38.7 C, neck stiffness, positive Kernig sign, no focal deficit, no rash. CSF showed opening pressure 24 cmH2O, white cell count 3,800 per cubic millimeter (78 percent neutrophils), glucose 28 mg/dL, protein 170 mg/dL. Gram stain revealed gram-positive diplococci; culture identified Streptococcus pneumoniae. Primary anchor: PMID 15509818 (van de Beek 2004 NEJM), elderly subgroup mortality 51 percent at age 70 years and older. Outcome: fatal hospital day 2. Subphase 1.3 commit 5.3.3 wave 1, pre-adjudication hold_for_revision.

NARRATIVE_ES: Mujer de 79 anos en Paises Bajos (Amsterdam), ingresada a urgencias terciarias tras cinco dias de fiebre progresiva, cefalea y confusion con progresion a coma. Ingreso con escala de Glasgow 6. Examen: temperatura 38.7 C, rigidez de nuca, signo de Kernig positivo, sin deficit focal, sin exantema. Liquido cefalorraquideo mostro presion de apertura 24 cmH2O, leucocitos 3,800 por mm3 (78 por ciento neutrofilos), glucosa 28 mg/dL, proteina 170 mg/dL. Tincion de Gram con diplococos grampositivos y cultivo Streptococcus pneumoniae. Anclaje primario en cohorte prospectiva van de Beek 2004 NEJM (PMID 15509818, 696 episodios 1998-2002, mortalidad estrato adultos mayores 51 por ciento a edad >=70). Resultado: fatal en hospital dia 2. Subphase 1.3 commit 5.3.3 wave 1, pre-adjudicacion hold_for_revision.

RATIONALE: Anchored to PMID 15509818 (van de Beek 2004 NEJM), 696-episode prospective Netherlands cohort 1998-2002 (elderly subgroup mortality 51 percent at age 70 years and older). Demographic anchor (79yo F) sits in eldest stratum. CSF profile bacterial range. Imputation tiers: tier_1_primary={age, sex, csf_culture, csf_gram_stain}; tier_3_within_cohort={csf_wbc, neutrophil_pct, glucose, protein, gcs, hyponatremia}; tier_4_priors={temp, symptom_days, hr}. Indeterminate=none. Diagnostic_ambiguity=false. Outcome=fatal_hospital_day_2. Antibiotic_started_hours=2. Tier: tier_3_imputation_within_cohort_review. 5.3.3 wave1 SP-eldest-fatal.

ANCHORING_EXTRAS: stage=pre_adjudication; status=pending_external_review; self_review_disposition=hold_for_revision; self_review_notes=wave 1 vignette anchored to PMID 15509818 (van de Beek 2004 NEJM); external clinical adjudication pending; classification provisional. adjudicator_ids=WAVE1-PRE-ADJ-1, WAVE1-PRE-ADJ-2 (sentinel); cohen_kappa=0.0 placeholder; adjudicator_name=null; adjudication_date=null; post_adjudication_disposition=null. Subphase 1.3 commit 5.3.3 (2026-05-08). anchor=van-de-Beek-NEJM-2004 stratum=eldest-fatal.

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
