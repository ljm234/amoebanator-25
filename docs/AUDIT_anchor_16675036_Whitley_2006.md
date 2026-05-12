# AUDIT bundle: PMID 16675036 | Whitley 2006

Generated: 2026-05-11
Vignettes in bundle: 6
Build status: NCBI fetched
Bundle type: BIG (n>=5 vignettes single-anchor)

## Anchor: PMID 16675036 | Whitley 2006

### Registry metadata (current state)

```json
{
  "pmid": "16675036",
  "doi": "10.1016/j.antiviral.2006.04.002",
  "authors_short": "Whitley RJ",
  "authors_full": [
    "Whitley RJ"
  ],
  "journal": "Antiviral Res",
  "journal_short_code": "Antiviral Res",
  "year": 2006,
  "volume": "71",
  "issue": "2-3",
  "pages": "141-148",
  "title": "Herpes simplex encephalitis: adolescents and adults",
  "anchor_type": "review",
  "anchor_subtype": "hsv_encephalitis_adolescents_adults_review_acyclovir_protocol",
  "verification_confidence": 0.95,
  "verification_method": "claude_web_pubmed_ui_v4_2026_05_07",
  "last_verified_date": "2026-05-07",
  "caveat": "Comprehensive HSE review for adolescents and adults. Acyclovir 10 mg/kg every 8 hours for 21 days protocol. Even with early acyclovir, approximately two-thirds of survivors have significant residual neurologic deficits. Untreated mortality 70 percent. PCR is gold standard for diagnosis; false negatives can occur early after disease onset. MRI demonstrates temporal lobe edema and hemorrhage. EEG shows spike-and-slow-wave activity over temporal lobes. Anchor for Class 3 HSV-1 adult primary-source vignettes (Subphase 1.3 commit 5.3.2). Errata 5.4.3.1 (2026-05-11): the previously-registered companion PMID 16517432 was removed; NCBI E-utilities verification showed 16517432 is a J Asthma 2006 Danish skin-test reactivity paper, not a Whitley HSV review. The 6 vignettes that anchored to 16517432 now anchor to this entry (16675036)."
}
```

### NCBI live re-fetch (2026-05-11)

```json
{
  "uid": "16675036",
  "pubdate": "2006 Sep",
  "epubdate": "2006 Apr 25",
  "source": "Antiviral Res",
  "authors": [
    {
      "name": "Whitley RJ",
      "authtype": "Author",
      "clusterid": ""
    }
  ],
  "lastauthor": "Whitley RJ",
  "title": "Herpes simplex encephalitis: adolescents and adults.",
  "sorttitle": "herpes simplex encephalitis adolescents and adults",
  "volume": "71",
  "issue": "2-3",
  "pages": "141-8",
  "lang": [
    "eng"
  ],
  "nlmuniqueid": "8109699",
  "issn": "0166-3542",
  "essn": "",
  "pubtype": [
    "Journal Article",
    "Research Support, N.I.H., Extramural",
    "Research Support, Non-U.S. Gov't",
    "Review"
  ],
  "recordstatus": "PubMed - indexed for MEDLINE",
  "pubstatus": "256",
  "articleids": [
    {
      "idtype": "pubmed",
      "idtypen": 1,
      "value": "16675036"
    },
    {
      "idtype": "doi",
      "idtypen": 3,
      "value": "10.1016/j.antiviral.2006.04.002"
    },
    {
      "idtype": "pii",
      "idtypen": 4,
      "value": "S0166-3542(06)00110-0"
    }
  ],
  "history": [
    {
      "pubstatus": "received",
      "date": "2006/02/21 00:00"
    },
    {
      "pubstatus": "revised",
      "date": "2006/03/30 00:00"
    },
    {
      "pubstatus": "accepted",
      "date": "2006/04/03 00:00"
    },
    {
      "pubstatus": "pubmed",
      "date": "2006/05/06 09:00"
    },
    {
      "pubstatus": "medline",
      "date": "2006/11/11 09:00"
    },
    {
      "pubstatus": "entrez",
      "date": "2006/05/06 09:00"
    }
  ],
  "references": [],
  "attributes": [
    "Has Abstract"
  ],
  "pmcrefcount": "",
  "fulljournalname": "Antiviral research",
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
  "sortpubdate": "2006/09/01 00:00",
  "sortfirstauthor": "Whitley RJ",
  "vernaculartitle": ""
}
```

### Registry-vs-NCBI delta

- **pages**: registry='141-148' | ncbi='141-8'

### Vignettes citing this anchor (6 total)

#### Vignette: vid=091 file=vir_091_hsv1_pediatric_sequelae.json class=3 subphase=1.3 VIRAL

```
ANCHOR:
  pmid: 16675036
  first_author: Whitley
  year: 2006
  journal: Antiviral Res
  citation_type: review
  doi: 10.1016/S1473-3099(06)70414-6

DEMOGRAPHICS:
  age_years: 8  sex: female  region: us_south
  ethnicity: white_non_hispanic  altitude_m: 100
  hiv_status: negative  cd4: None
  pregnancy_red_flag: False
  immunocompromise_status: none
  freshwater_exposure_14d: False (None)

HISTORY:
  symptom_onset_to_presentation_days: 6.0
  chief_complaint: altered_mental_status
  red_flags_present: []
  prodrome_description: 8-year-old female, US South region. 6-day course: low-grade fever 38.4 C, headache, then progressive behavioral change day 3, expressive aphasia day 4, complex partial seizures day 5, obtundation day 6 prompting tertiary pediatric ED. No neck stiffness. No freshwater. Acyclovir hour 4. Outcome: survived with moderate cognitive sequelae per Whitley HSE pediatric-residual-deficit pattern.

VITALS:
  T:38.4C HR:122 BP:100/60 GCS:9 SpO2:96% RR:22

EXAM:
  mental_status: stuporous  neck_stiff: False  kernig_brudz: False
  cranial_nerve_palsy: none  papilledema: False  focal_deficit: True
  skin_lesion_centrofacial_chronic: False  rash: False

LABS:
  WBC:9200 Plt:285000 ALT/AST:24 CRP:22.0 PCT:0.4 Na:137

CSF:
  OP:24.0cmH2O  WBC:240/mm3  lymph%:75 neut%:25 eos%:0
  glucose:52mg/dL protein:130mg/dL lactate:2.6mmol/L ADA:NoneU/L
  crag_lfa:negative  wet_mount:negative  xanthochromia:True  RBC:38

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

NARRATIVE_EN: An 8-year-old girl in the US South region presented to a tertiary pediatric emergency department with a 6-day course: low-grade fever to 38.4 C, headache, progressive behavioral change on day 3, expressive aphasia on day 4, complex partial seizures on day 5, and obtundation on day 6. She had no neck stiffness on examination and no antecedent freshwater exposure. Examination on admission: temperature 38.4 C, Glasgow Coma Scale 9, focal deficit (expressive aphasia), no rash. CSF showed opening pressure 24 cmH2O, white cell count 240 per cubic millimeter (75 percent lymphocytes), glucose 52 mg/dL, protein 130 mg/dL, RBC 38 with xanthochromia (canonical hemorrhagic component). CSF HSV-1 PCR positive. Brain MRI with DWI/FLAIR showed mesial temporal T2/FLAIR hyperintensity asymmetric. Acyclovir initiated within four hours. Anchored to Whitley 2006 Lancet Infect Dis HSE pathogenesis review (PMID 16675036). Outcome: survived with moderate cognitive sequelae. Subphase 1.3 commit 5.3.6 wave 2, pre-adjudication hold_for_revision.

NARRATIVE_ES: Nina de 8 anos en region sur de Estados Unidos, ingresada a urgencias pediatricas terciarias con curso de seis dias: febricula 38.4 C, cefalea, cambio conductual progresivo al tercer dia, afasia expresiva al cuarto dia, crisis parciales complejas al quinto y obnubilacion al sexto. Sin rigidez de nuca al examen. Sin exposicion a agua dulce. Examen: temperatura 38.4 C, escala de Glasgow 9, deficit focal (afasia expresiva), sin exantema. Liquido cefalorraquideo mostro presion de apertura 24 cmH2O, leucocitos 240 por mm3 (75 por ciento linfocitos), glucosa 52 mg/dL, proteina 130 mg/dL, eritrocitos 38 con xantocromia. PCR de HSV-1 positiva. RM cerebral con hiperintensidad temporal mesial T2/FLAIR. Aciclovir en cuatro horas. Anclaje en revision Whitley 2006 Lancet ID HSE (PMID 16675036). Subphase 1.3 commit 5.3.6 wave 2, pre-adjudicacion hold_for_revision.

RATIONALE: Anchored to PMID 16675036 (Whitley 2006 Lancet ID HSE pathogenesis review). Pediatric HSE phenotype with classic limbic-frontal extension and late-presentation obtundation. Demographic anchor (8yo F US South pediatric HSE) sits in Whitley's pediatric-HSE-residual-deficit stratum. CSF lymphocytic with hemorrhagic component (RBC 38, xanthochromia). MRI mesial temporal pattern. Imputation tiers: tier_1_primary={age, sex, hsv1_pcr, imaging_pattern, focal_aphasia, behavioral_change}; tier_3_within_review={csf_wbc, neutrophil_pct, glucose, protein, rbc, xanthochromia, gcs}; tier_4_priors={temp, symptom_days}. Indeterminate=none. Diagnostic_ambiguity=false. Outcome=survived_moderate_cognitive_sequelae. Acyclovir_hours=4. Tier: tier_3_imputation_within_review. 5.3.6 wave2 HSV1-Whitley-pediatric-sequelae.

ANCHORING_EXTRAS: stage=pre_adjudication; status=pending_external_review; self_review_disposition=hold_for_revision; self_review_notes=wave 5.3.6 VIRAL vignette anchored to PMID 16675036 (Whitley 2006 Lancet ID HSE pathogenesis review); external clinical adjudication pending; classification provisional. adjudicator_ids=VIRAL-WAVE2-PRE-ADJ-1, VIRAL-WAVE2-PRE-ADJ-2 (sentinel); cohen_kappa=0.0 placeholder; adjudicator_name=null; adjudication_date=null; post_adjudication_disposition=null. Subphase 1.3 commit 5.3.6 (2026-05-08, FINAL Subphase 1.3 wave). anchor=Whitley-Lancet-ID-2006 stratum=pediatric-HSE-sequelae.

ADJUDICATION:
  inclusion_decision: hold_for_revision  ground_truth_class: 3  kappa: 0.0
  adjudicator_ids: ['VIRAL-WAVE2-PRE-ADJ-1', 'VIRAL-WAVE2-PRE-ADJ-2']
  disagreement_resolution: None
```

#### Vignette: vid=092 file=vir_092_hsv1_adult.json class=3 subphase=1.3 VIRAL

```
ANCHOR:
  pmid: 16675036
  first_author: Whitley
  year: 2006
  journal: Antiviral Res
  citation_type: review
  doi: 10.1016/j.antiviral.2006.04.002

DEMOGRAPHICS:
  age_years: 42  sex: male  region: other_global
  ethnicity: white_non_hispanic  altitude_m: 50
  hiv_status: negative  cd4: None
  pregnancy_red_flag: False
  immunocompromise_status: none
  freshwater_exposure_14d: False (None)

HISTORY:
  symptom_onset_to_presentation_days: 5.0
  chief_complaint: seizure
  red_flags_present: []
  prodrome_description: 42-year-old male, US tertiary ED. 5-day progressive course: fever 38.8 C, severe headache, behavioral change with personality alteration day 3, expressive aphasia day 4, focal seizure day 5 prompting ED. No neck stiffness. No freshwater exposure. Medial temporal and limbic predilection canonical for HSE. Outcome: survived with mild memory deficit. Acyclovir hour 6.

VITALS:
  T:38.8C HR:102 BP:132/82 GCS:12 SpO2:97% RR:18

EXAM:
  mental_status: confused  neck_stiff: False  kernig_brudz: False
  cranial_nerve_palsy: none  papilledema: False  focal_deficit: True
  skin_lesion_centrofacial_chronic: False  rash: False

LABS:
  WBC:9800 Plt:240000 ALT/AST:28 CRP:22.0 PCT:0.4 Na:138

CSF:
  OP:22.0cmH2O  WBC:180/mm3  lymph%:75 neut%:25 eos%:0
  glucose:58mg/dL protein:95mg/dL lactate:2.6mmol/L ADA:NoneU/L
  crag_lfa:negative  wet_mount:negative  xanthochromia:True  RBC:45

IMAGING:
  modality: mri_with_dwi_flair  pattern: mesial_temporal_t2_flair_hyperintensity
  finding_count: 1
  text_summary: MRI brain with DWI/FLAIR: mesial temporal T2/FLAIR hyperintensity left greater than right asymmetric with basal ganglia sparing. Canonical HSE imaging signature.

DIAGNOSTIC_TESTS:
  total_results: 3
  pcr_panel: positive
  xpert_mtb_rif: n/a
  blood_culture: n/a
  csf_culture: n/a
  serology_or_antigen: n/a
  smear_or_gram: n/a
  brain_biopsy: n/a

NARRATIVE_EN: A 42-year-old man in the United States presented to a tertiary emergency department with a five-day progressive course: low-grade fever 38.8 C, severe headache, behavioral change with personality alteration noted by family on day 3, expressive aphasia on day 4, and focal seizure on day 5 prompting ED presentation. No neck stiffness on examination. No antecedent freshwater exposure. Examination on admission: Glasgow Coma Scale 12, focal neurological deficit (expressive aphasia). CSF showed opening pressure 22 cmH2O, white cell count 180 per cubic millimeter (75 percent lymphocytes), glucose 58 mg/dL, protein 95 mg/dL, RBC 45 with mild xanthochromia (canonical hemorrhagic component). CSF HSV-1 PCR positive. Brain MRI with DWI/FLAIR showed mesial temporal T2/FLAIR hyperintensity left greater than right asymmetric with basal ganglia sparing (canonical HSE imaging signature). Acyclovir initiated within six hours. Primary anchor: PMID 16675036 (Whitley 2006 Antiviral Res), HSE adolescents and adults review. Outcome: survived with mild memory deficit (per Whitley two-thirds of survivors have residual deficits even with early treatment). Subphase 1.3 commit 5.3.2 pilot 4, pre-adjudication hold_for_revision.

NARRATIVE_ES: Varon de 42 anos, Estados Unidos, ingresado a urgencias terciarias con curso progresivo de cinco dias: fiebre baja 38.8 C, cefalea intensa, cambio conductual con alteracion de personalidad notada por la familia al tercer dia, afasia expresiva al cuarto dia, crisis focal al quinto dia que motivo consulta. Sin rigidez de nuca al examen. Sin exposicion a agua dulce. Examen: escala de Glasgow 12, deficit focal (afasia expresiva). Liquido cefalorraquideo mostro presion de apertura 22 cmH2O, leucocitos 180 por mm3 (75 por ciento linfocitos), glucosa 58 mg/dL, proteina 95 mg/dL, eritrocitos 45 con xantocromia leve. PCR de HSV-1 positiva. RM cerebral mostro hiperintensidad temporal mesial T2/FLAIR izquierda mayor que derecha, asimetrica, con preservacion de ganglios basales. Inicio de aciclovir en seis horas. Anclaje primario en revision de HSE en adolescentes y adultos (PMID 16675036, Whitley 2006 Antiviral Res). Subphase 1.3 commit 5.3.2 pilot 4.

RATIONALE: Anchored to PMID 16675036 (Whitley 2006 Antiviral Res), HSE adolescents/adults review. Phenotype (fever + AMS + expressive aphasia + focal seizure, 42yo M) prototypical adult HSE. CSF (WBC 180 lymphocytic, RBC 45 hemorrhagic component, mild xanthochromia) canonical. MRI mesial temporal T2/FLAIR hyperintensity asymmetric L>R per master prompt 1.3 mandate. Acyclovir hour 6 yielded survival with mild memory deficit per Whitley two-thirds residual deficits even with early Rx. Imputation tiers: tier_1_primary={age, sex, hsv1_pcr, imaging_pattern}; tier_3_within_cohort={csf_wbc, neutrophil_pct, glucose, protein, csf_rbc, xanthochromia, imaging_laterality}; tier_4_priors={temp, gcs, symptom_days}. Indeterminate=none. Diagnostic_ambiguity=false. Outcome=survived_mild_memory_deficit. Acyclovir_hours=6. Tier: primary_source_direct. 5.3.2 pilot 4.

ANCHORING_EXTRAS: stage=pre_adjudication; status=pending_external_review; self_review_disposition=hold_for_revision; self_review_notes=pilot vignette anchored to PMID 16675036 (Whitley 2006 Antiviral Res HSE adult); external clinical adjudication pending; classification provisional. adjudicator_ids=PILOT-PRE-ADJ-1, PILOT-PRE-ADJ-2 (sentinel); cohen_kappa=0.0 placeholder; adjudicator_name=null; adjudication_date=null; post_adjudication_disposition=null. Subphase 1.3 commit 5.3.2 (2026-05-07).

ADJUDICATION:
  inclusion_decision: hold_for_revision  ground_truth_class: 3  kappa: 0.0
  adjudicator_ids: ['PILOT-PRE-ADJ-1', 'PILOT-PRE-ADJ-2']
  disagreement_resolution: None
```

#### Vignette: vid=093 file=vir_093_hsv1_elderly_fatal.json class=3 subphase=1.3 VIRAL

```
ANCHOR:
  pmid: 16675036
  first_author: Whitley
  year: 2006
  journal: Antiviral Res
  citation_type: review
  doi: 10.1016/S1473-3099(06)70414-6

DEMOGRAPHICS:
  age_years: 67  sex: female  region: other_global
  ethnicity: white_non_hispanic  altitude_m: 5
  hiv_status: negative  cd4: None
  pregnancy_red_flag: False
  immunocompromise_status: none
  freshwater_exposure_14d: False (None)

HISTORY:
  symptom_onset_to_presentation_days: 7.0
  chief_complaint: altered_mental_status
  red_flags_present: []
  prodrome_description: 67-year-old female, Netherlands. 7-day course: low-grade fever 38.3 C, headache, behavioral change with confusion day 2, anomic aphasia day 4, focal seizures day 5, progressive obtundation day 6, coma day 7. Tertiary ED Amsterdam. No freshwater. Acyclovir hour 12 (delayed by atypical presentation). Outcome: fatal hospital day 5 per Whitley HSE elderly-mortality data.

VITALS:
  T:38.3C HR:110 BP:102/64 GCS:5 SpO2:88% RR:26

EXAM:
  mental_status: comatose  neck_stiff: False  kernig_brudz: False
  cranial_nerve_palsy: none  papilledema: False  focal_deficit: True
  skin_lesion_centrofacial_chronic: False  rash: False

LABS:
  WBC:8800 Plt:215000 ALT/AST:32 CRP:28.0 PCT:0.5 Na:132

CSF:
  OP:26.0cmH2O  WBC:280/mm3  lymph%:72 neut%:28 eos%:0
  glucose:50mg/dL protein:145mg/dL lactate:2.8mmol/L ADA:NoneU/L
  crag_lfa:negative  wet_mount:negative  xanthochromia:True  RBC:50

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

NARRATIVE_EN: A 67-year-old woman in the Netherlands presented to a tertiary emergency department in Amsterdam after a 7-day course: low-grade fever to 38.3 C, headache, behavioral change on day 2, anomic aphasia on day 4, focal seizures on day 5, and progressive obtundation to coma by day 7. Examination on admission: temperature 38.3 C, Glasgow Coma Scale 5, comatose, focal deficit (anomic aphasia, residual right-sided posturing), no rash. CSF showed opening pressure 26 cmH2O, white cell count 280 per cubic millimeter (72 percent lymphocytes), glucose 50 mg/dL, protein 145 mg/dL, RBC 50 with xanthochromia (canonical hemorrhagic component). CSF HSV-1 PCR positive. Brain MRI with DWI/FLAIR showed mesial temporal T2/FLAIR hyperintensity bilateral. Acyclovir initiated at hour 12 (delayed by atypical presentation). Anchored to Whitley 2006 Lancet Infect Dis HSE pathogenesis review (PMID 16675036). Outcome: fatal hospital day 5 per Whitley HSE elderly-mortality data. Subphase 1.3 commit 5.3.6 wave 2, pre-adjudication hold_for_revision.

NARRATIVE_ES: Mujer de 67 anos en Paises Bajos (Amsterdam), ingresada a urgencias terciarias tras curso de siete dias: febricula 38.3 C, cefalea, cambio conductual al segundo dia, afasia anomica al cuarto, crisis focales al quinto, obnubilacion progresiva con coma al septimo. Examen: temperatura 38.3 C, escala de Glasgow 5, comatosa, deficit focal (afasia anomica, postura derecha residual), sin exantema. Liquido cefalorraquideo mostro presion de apertura 26 cmH2O, leucocitos 280 por mm3 (72 por ciento linfocitos), glucosa 50 mg/dL, proteina 145 mg/dL, eritrocitos 50 con xantocromia. PCR de HSV-1 positiva. RM cerebral con hiperintensidad temporal mesial T2/FLAIR bilateral. Aciclovir en hora 12 (retraso por presentacion atipica). Anclaje en revision Whitley 2006 Lancet ID HSE (PMID 16675036). Subphase 1.3 commit 5.3.6 wave 2.

RATIONALE: Anchored to PMID 16675036 (Whitley 2006 Lancet ID HSE pathogenesis review). Elderly HSE with delayed-acyclovir fatal outcome per Whitley elderly-mortality stratum. Demographic anchor (67yo F NL elderly HSE delayed-treatment) sits in elderly-fatal-HSE stratum. CSF lymphocytic with prominent hemorrhagic component (RBC 50, xanthochromia). MRI bilateral mesial temporal. Imputation tiers: tier_1_primary={age, sex, hsv1_pcr, imaging_pattern, focal_aphasia, delayed_acyclovir}; tier_3_within_review={csf_wbc, neutrophil_pct, glucose, protein, rbc, xanthochromia, gcs}; tier_4_priors={temp, symptom_days, hyponatremia}. Indeterminate=none. Diagnostic_ambiguity=false. Outcome=fatal_hospital_day_5. Acyclovir_hours=12. Tier: tier_3_imputation_within_review. 5.3.6 wave2 HSV1-Whitley-elderly-fatal.

ANCHORING_EXTRAS: stage=pre_adjudication; status=pending_external_review; self_review_disposition=hold_for_revision; self_review_notes=wave 5.3.6 VIRAL vignette anchored to PMID 16675036 (Whitley 2006 Lancet ID HSE pathogenesis review); external clinical adjudication pending; classification provisional. adjudicator_ids=VIRAL-WAVE2-PRE-ADJ-1, VIRAL-WAVE2-PRE-ADJ-2 (sentinel); cohen_kappa=0.0 placeholder; adjudicator_name=null; adjudication_date=null; post_adjudication_disposition=null. Subphase 1.3 commit 5.3.6 (2026-05-08, FINAL Subphase 1.3 wave). anchor=Whitley-Lancet-ID-2006 stratum=elderly-fatal-delayed-treatment.

ADJUDICATION:
  inclusion_decision: hold_for_revision  ground_truth_class: 3  kappa: 0.0
  adjudicator_ids: ['VIRAL-WAVE2-PRE-ADJ-1', 'VIRAL-WAVE2-PRE-ADJ-2']
  disagreement_resolution: None
```

#### Vignette: vid=095 file=vir_095_hsv1_adolescent.json class=3 subphase=1.3 VIRAL

```
ANCHOR:
  pmid: 16675036
  first_author: Whitley
  year: 2006
  journal: Antiviral Res
  citation_type: review
  doi: 10.1016/S1473-3099(06)70414-6

DEMOGRAPHICS:
  age_years: 14  sex: male  region: us_south
  ethnicity: white_non_hispanic  altitude_m: 100
  hiv_status: negative  cd4: None
  pregnancy_red_flag: False
  immunocompromise_status: none
  freshwater_exposure_14d: False (None)

HISTORY:
  symptom_onset_to_presentation_days: 4.0
  chief_complaint: behavioral_change
  red_flags_present: []
  prodrome_description: 14-year-old male, US South region. 4-day course: fever 38.5 C, headache, then progressive behavioral change with personality alteration day 2, anomic aphasia day 3, complex partial seizure day 4 prompting tertiary pediatric ED. No neck stiffness. No freshwater. Acyclovir hour 5. Outcome: survived with mild memory deficit.

VITALS:
  T:38.5C HR:96 BP:118/72 GCS:12 SpO2:97% RR:18

EXAM:
  mental_status: confused  neck_stiff: False  kernig_brudz: False
  cranial_nerve_palsy: none  papilledema: False  focal_deficit: True
  skin_lesion_centrofacial_chronic: False  rash: False

LABS:
  WBC:8800 Plt:270000 ALT/AST:24 CRP:18.0 PCT:0.4 Na:138

CSF:
  OP:22.0cmH2O  WBC:195/mm3  lymph%:78 neut%:22 eos%:0
  glucose:55mg/dL protein:105mg/dL lactate:2.4mmol/L ADA:NoneU/L
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

NARRATIVE_EN: A 14-year-old boy in the US South region presented to a tertiary pediatric emergency department with a 4-day course: fever to 38.5 C, headache, then progressive behavioral change with personality alteration on day 2, anomic aphasia on day 3, and a complex partial seizure on day 4. He had no neck stiffness and no antecedent freshwater exposure. Examination on admission: temperature 38.5 C, Glasgow Coma Scale 12, focal deficit (anomic aphasia), no rash. CSF showed opening pressure 22 cmH2O, white cell count 195 per cubic millimeter (78 percent lymphocytes), glucose 55 mg/dL, protein 105 mg/dL, RBC 28 with xanthochromia. CSF HSV-1 PCR positive. Brain MRI with DWI/FLAIR showed mesial temporal T2/FLAIR hyperintensity asymmetric. Acyclovir initiated within five hours. Anchored to Whitley 2006 Lancet Infect Dis HSE pathogenesis review (PMID 16675036), adolescent-HSE stratum. Outcome: survived with mild memory deficit. Subphase 1.3 commit 5.3.6 wave 2, pre-adjudication hold_for_revision.

NARRATIVE_ES: Varon de 14 anos en region sur de Estados Unidos, ingresado a urgencias pediatricas terciarias con curso de cuatro dias: fiebre 38.5 C, cefalea, cambio conductual con alteracion de personalidad al segundo dia, afasia anomica al tercer dia y crisis parcial compleja al cuarto. Sin rigidez de nuca. Sin exposicion a agua dulce. Examen: temperatura 38.5 C, escala de Glasgow 12, deficit focal (afasia anomica), sin exantema. Liquido cefalorraquideo mostro presion de apertura 22 cmH2O, leucocitos 195 por mm3 (78 por ciento linfocitos), glucosa 55 mg/dL, proteina 105 mg/dL, eritrocitos 28 con xantocromia. PCR de HSV-1 positiva. RM cerebral con hiperintensidad temporal mesial T2/FLAIR. Aciclovir en cinco horas. Anclaje en revision Whitley 2006 Lancet ID HSE (PMID 16675036). Subphase 1.3 commit 5.3.6 wave 2.

RATIONALE: Anchored to PMID 16675036 (Whitley 2006 Lancet ID HSE pathogenesis review). Adolescent HSE phenotype with classic limbic-frontal pattern. Demographic anchor (14yo M US South adolescent HSE) sits in Whitley adolescent-HSE stratum. CSF lymphocytic with hemorrhagic component. MRI mesial temporal. Imputation tiers: tier_1_primary={age, sex, hsv1_pcr, imaging_pattern, focal_aphasia, behavioral_change}; tier_3_within_review={csf_wbc, neutrophil_pct, glucose, protein, rbc, xanthochromia, gcs}; tier_4_priors={temp, symptom_days}. Indeterminate=none. Diagnostic_ambiguity=false. Outcome=survived_mild_memory_deficit. Acyclovir_hours=5. Tier: tier_3_imputation_within_review. 5.3.6 wave2 HSV1-Whitley-adolescent.

ANCHORING_EXTRAS: stage=pre_adjudication; status=pending_external_review; self_review_disposition=hold_for_revision; self_review_notes=wave 5.3.6 VIRAL vignette anchored to PMID 16675036 (Whitley 2006 Lancet ID HSE pathogenesis review); external clinical adjudication pending; classification provisional. adjudicator_ids=VIRAL-WAVE2-PRE-ADJ-1, VIRAL-WAVE2-PRE-ADJ-2 (sentinel); cohen_kappa=0.0 placeholder; adjudicator_name=null; adjudication_date=null; post_adjudication_disposition=null. Subphase 1.3 commit 5.3.6 (2026-05-08, FINAL Subphase 1.3 wave). anchor=Whitley-Lancet-ID-2006 stratum=adolescent-HSE.

ADJUDICATION:
  inclusion_decision: hold_for_revision  ground_truth_class: 3  kappa: 0.0
  adjudicator_ids: ['VIRAL-WAVE2-PRE-ADJ-1', 'VIRAL-WAVE2-PRE-ADJ-2']
  disagreement_resolution: None
```

#### Vignette: vid=098 file=vir_098_hsv1_pediatric.json class=3 subphase=1.3 VIRAL

```
ANCHOR:
  pmid: 16675036
  first_author: Whitley
  year: 2006
  journal: Antiviral Res
  citation_type: review
  doi: 10.1016/S1473-3099(06)70414-6

DEMOGRAPHICS:
  age_years: 9  sex: female  region: us_south
  ethnicity: white_non_hispanic  altitude_m: 100
  hiv_status: negative  cd4: None
  pregnancy_red_flag: False
  immunocompromise_status: none
  freshwater_exposure_14d: False (None)

HISTORY:
  symptom_onset_to_presentation_days: 4.0
  chief_complaint: altered_mental_status
  red_flags_present: []
  prodrome_description: 9-year-old female, US South region. 4-day course: fever 38.6 C, headache, then irritability and behavioral change day 2, expressive aphasia day 3, complex partial seizure day 4 prompting tertiary pediatric ED. No neck stiffness. No freshwater. Acyclovir hour 4. Outcome: survived with mild cognitive sequelae per Whitley pediatric-HSE pattern.

VITALS:
  T:38.6C HR:110 BP:102/64 GCS:12 SpO2:97% RR:22

EXAM:
  mental_status: confused  neck_stiff: False  kernig_brudz: False
  cranial_nerve_palsy: none  papilledema: False  focal_deficit: True
  skin_lesion_centrofacial_chronic: False  rash: False

LABS:
  WBC:8600 Plt:295000 ALT/AST:24 CRP:16.0 PCT:0.3 Na:138

CSF:
  OP:22.0cmH2O  WBC:210/mm3  lymph%:78 neut%:22 eos%:0
  glucose:56mg/dL protein:105mg/dL lactate:2.4mmol/L ADA:NoneU/L
  crag_lfa:negative  wet_mount:negative  xanthochromia:True  RBC:30

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

NARRATIVE_EN: A 9-year-old girl in the US South region presented to a tertiary pediatric emergency department with a 4-day course: fever to 38.6 C, headache, then irritability and behavioral change on day 2, expressive aphasia on day 3, and a complex partial seizure on day 4. She had no neck stiffness and no antecedent freshwater exposure. Examination on admission: temperature 38.6 C, Glasgow Coma Scale 12, focal deficit (expressive aphasia), no rash. CSF showed opening pressure 22 cmH2O, white cell count 210 per cubic millimeter (78 percent lymphocytes), glucose 56 mg/dL, protein 105 mg/dL, RBC 30 with xanthochromia. CSF HSV-1 PCR positive. Brain MRI with DWI/FLAIR showed mesial temporal T2/FLAIR hyperintensity asymmetric. Acyclovir initiated within four hours. Anchored to Whitley 2006 Lancet Infect Dis HSE pathogenesis review (PMID 16675036), pediatric-HSE stratum. Outcome: survived with mild cognitive sequelae. Subphase 1.3 commit 5.3.6 wave 2, pre-adjudication hold_for_revision.

NARRATIVE_ES: Nina de 9 anos en region sur de Estados Unidos, ingresada a urgencias pediatricas terciarias con curso de cuatro dias: fiebre 38.6 C, cefalea, irritabilidad y cambio conductual al segundo dia, afasia expresiva al tercer dia y crisis parcial compleja al cuarto. Sin rigidez de nuca. Sin exposicion a agua dulce. Examen: temperatura 38.6 C, escala de Glasgow 12, deficit focal (afasia expresiva), sin exantema. Liquido cefalorraquideo mostro presion de apertura 22 cmH2O, leucocitos 210 por mm3 (78 por ciento linfocitos), glucosa 56 mg/dL, proteina 105 mg/dL, eritrocitos 30 con xantocromia. PCR de HSV-1 positiva. RM cerebral con hiperintensidad temporal mesial T2/FLAIR. Aciclovir en cuatro horas. Anclaje en revision Whitley 2006 Lancet ID HSE (PMID 16675036). Subphase 1.3 commit 5.3.6 wave 2, pre-adjudicacion hold_for_revision.

RATIONALE: Anchored to PMID 16675036 (Whitley 2006 Lancet ID HSE pathogenesis review). Pediatric HSE with classic limbic phenotype. Demographic anchor (9yo F US South pediatric HSE) sits in Whitley pediatric-HSE stratum. CSF lymphocytic with hemorrhagic component. MRI mesial temporal. Imputation tiers: tier_1_primary={age, sex, hsv1_pcr, imaging_pattern, focal_aphasia, behavioral_change}; tier_3_within_review={csf_wbc, neutrophil_pct, glucose, protein, rbc, xanthochromia, gcs}; tier_4_priors={temp, symptom_days, hr}. Indeterminate=none. Diagnostic_ambiguity=false. Outcome=survived_mild_cognitive_sequelae. Acyclovir_hours=4. Tier: tier_3_imputation_within_review. 5.3.6 wave2 HSV1-Whitley-pediatric.

ANCHORING_EXTRAS: stage=pre_adjudication; status=pending_external_review; self_review_disposition=hold_for_revision; self_review_notes=wave 5.3.6 VIRAL vignette anchored to PMID 16675036 (Whitley 2006 Lancet ID HSE pathogenesis review); external clinical adjudication pending; classification provisional. adjudicator_ids=VIRAL-WAVE2-PRE-ADJ-1, VIRAL-WAVE2-PRE-ADJ-2 (sentinel); cohen_kappa=0.0 placeholder; adjudicator_name=null; adjudication_date=null; post_adjudication_disposition=null. Subphase 1.3 commit 5.3.6 (2026-05-08, FINAL Subphase 1.3 wave). anchor=Whitley-Lancet-ID-2006 stratum=pediatric-HSE.

ADJUDICATION:
  inclusion_decision: hold_for_revision  ground_truth_class: 3  kappa: 0.0
  adjudicator_ids: ['VIRAL-WAVE2-PRE-ADJ-1', 'VIRAL-WAVE2-PRE-ADJ-2']
  disagreement_resolution: None
```

#### Vignette: vid=101 file=vir_101_hsv1_adolescent.json class=3 subphase=1.3 VIRAL

```
ANCHOR:
  pmid: 16675036
  first_author: Whitley
  year: 2006
  journal: Antiviral Res
  citation_type: review
  doi: 10.1016/S1473-3099(06)70414-6

DEMOGRAPHICS:
  age_years: 17  sex: male  region: us_south
  ethnicity: white_non_hispanic  altitude_m: 100
  hiv_status: negative  cd4: None
  pregnancy_red_flag: False
  immunocompromise_status: none
  freshwater_exposure_14d: False (None)

HISTORY:
  symptom_onset_to_presentation_days: 4.0
  chief_complaint: behavioral_change
  red_flags_present: []
  prodrome_description: 17-year-old male, US South region. 4-day course: fever 38.5 C, headache, behavioral change with personality alteration day 2, anomic aphasia day 3, complex partial seizure day 4 prompting tertiary ED. No neck stiffness. No freshwater. Acyclovir hour 4. Outcome: survived with mild memory deficit per Whitley adolescent-HSE pattern.

VITALS:
  T:38.5C HR:92 BP:124/74 GCS:13 SpO2:98% RR:18

EXAM:
  mental_status: confused  neck_stiff: False  kernig_brudz: False
  cranial_nerve_palsy: none  papilledema: False  focal_deficit: True
  skin_lesion_centrofacial_chronic: False  rash: False

LABS:
  WBC:9200 Plt:265000 ALT/AST:26 CRP:18.0 PCT:0.3 Na:138

CSF:
  OP:22.0cmH2O  WBC:200/mm3  lymph%:78 neut%:22 eos%:0
  glucose:56mg/dL protein:110mg/dL lactate:2.4mmol/L ADA:NoneU/L
  crag_lfa:negative  wet_mount:negative  xanthochromia:True  RBC:30

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

NARRATIVE_EN: A 17-year-old man in the US South region presented to a tertiary emergency department with a 4-day course: fever to 38.5 C, headache, behavioral change with personality alteration on day 2, anomic aphasia on day 3, and a complex partial seizure on day 4. He had no neck stiffness and no antecedent freshwater exposure. Examination on admission: temperature 38.5 C, Glasgow Coma Scale 13, focal deficit (anomic aphasia), no rash. CSF showed opening pressure 22 cmH2O, white cell count 200 per cubic millimeter (78 percent lymphocytes), glucose 56 mg/dL, protein 110 mg/dL, RBC 30 with xanthochromia. CSF HSV-1 PCR positive. Brain MRI with DWI/FLAIR showed mesial temporal T2/FLAIR hyperintensity asymmetric. Acyclovir initiated within four hours. Anchored to Whitley 2006 Lancet Infect Dis HSE pathogenesis review (PMID 16675036), older-adolescent-HSE stratum. Outcome: survived with mild memory deficit. Subphase 1.3 commit 5.3.6 wave 2, pre-adjudication hold_for_revision.

NARRATIVE_ES: Varon de 17 anos en region sur de Estados Unidos, ingresado a urgencias terciarias con curso de cuatro dias: fiebre 38.5 C, cefalea, cambio conductual con alteracion de personalidad al segundo dia, afasia anomica al tercer dia y crisis parcial compleja al cuarto. Sin rigidez de nuca. Sin exposicion a agua dulce. Examen: temperatura 38.5 C, escala de Glasgow 13, deficit focal (afasia anomica), sin exantema. Liquido cefalorraquideo mostro presion de apertura 22 cmH2O, leucocitos 200 por mm3 (78 por ciento linfocitos), glucosa 56 mg/dL, proteina 110 mg/dL, eritrocitos 30 con xantocromia. PCR de HSV-1 positiva. RM cerebral con hiperintensidad temporal mesial T2/FLAIR. Aciclovir en cuatro horas. Anclaje en revision Whitley 2006 Lancet ID HSE (PMID 16675036). Subphase 1.3 commit 5.3.6 wave 2, pre-adjudicacion hold_for_revision.

RATIONALE: Anchored to PMID 16675036 (Whitley 2006 Lancet ID HSE pathogenesis review). Older-adolescent HSE phenotype. Demographic anchor (17yo M US South older-adolescent HSE) sits in Whitley adolescent-HSE stratum. CSF lymphocytic with hemorrhagic component. MRI mesial temporal. Imputation tiers: tier_1_primary={age, sex, hsv1_pcr, imaging_pattern, focal_aphasia, behavioral_change}; tier_3_within_review={csf_wbc, neutrophil_pct, glucose, protein, rbc, xanthochromia, gcs}; tier_4_priors={temp, symptom_days}. Indeterminate=none. Diagnostic_ambiguity=false. Outcome=survived_mild_memory_deficit. Acyclovir_hours=4. Tier: tier_3_imputation_within_review. 5.3.6 wave2 HSV1-Whitley-older-adolescent.

ANCHORING_EXTRAS: stage=pre_adjudication; status=pending_external_review; self_review_disposition=hold_for_revision; self_review_notes=wave 5.3.6 VIRAL vignette anchored to PMID 16675036 (Whitley 2006 Lancet ID HSE pathogenesis review); external clinical adjudication pending; classification provisional. adjudicator_ids=VIRAL-WAVE2-PRE-ADJ-1, VIRAL-WAVE2-PRE-ADJ-2 (sentinel); cohen_kappa=0.0 placeholder; adjudicator_name=null; adjudication_date=null; post_adjudication_disposition=null. Subphase 1.3 commit 5.3.6 (2026-05-08, FINAL Subphase 1.3 wave). anchor=Whitley-Lancet-ID-2006 stratum=older-adolescent-HSE.

ADJUDICATION:
  inclusion_decision: hold_for_revision  ground_truth_class: 3  kappa: 0.0
  adjudicator_ids: ['VIRAL-WAVE2-PRE-ADJ-1', 'VIRAL-WAVE2-PRE-ADJ-2']
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
