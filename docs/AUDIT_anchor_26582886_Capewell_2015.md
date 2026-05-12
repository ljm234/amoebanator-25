# AUDIT bundle: PMID 26582886 | Capewell 2015

Generated: 2026-05-11
Vignettes in bundle: 5
Build status: NCBI fetched
Bundle type: BIG (n>=5 vignettes single-anchor)

## Anchor: PMID 26582886 | Capewell 2015

### Registry metadata (current state)

```json
{
  "pmid": "26582886",
  "doi": "10.1093/jpids/piu103",
  "authors_short": "Capewell et al.",
  "authors_full": [
    "Capewell LG",
    "Harris AM",
    "Yoder JS",
    "Cope JR",
    "Eddy BA",
    "Roy SL",
    "Visvesvara GS",
    "Fox LM",
    "Beach MJ"
  ],
  "journal": "J Pediatric Infect Dis Soc",
  "journal_short_code": "JPIDS",
  "year": 2015,
  "volume": "4",
  "issue": "4",
  "pages": "e68-e75",
  "title": "Diagnosis, Clinical Course, and Treatment of Primary Amoebic Meningoencephalitis in the United States, 1937-2013",
  "anchor_type": "review",
  "anchor_subtype": "review_us_surveillance",
  "pmc_id": null,
  "verification_confidence": 99,
  "last_verified_date": "2026-05-04",
  "caveat": "Review article (US PAM 1937-2013, approximately 140-145 cases over 76 years). PMC ID NOT confirmable - cite PMID + DOI only. Use as Tier 4 IMPUTED_FROM_LITERATURE_REVIEW anchor only. Prior PMC4622028 attribution removed (unconfirmable in any of 6 independent reference lists)."
}
```

### NCBI live re-fetch (2026-05-11)

```json
{
  "uid": "26582886",
  "pubdate": "2015 Dec",
  "epubdate": "2014 Oct 23",
  "source": "J Pediatric Infect Dis Soc",
  "authors": [
    {
      "name": "Capewell LG",
      "authtype": "Author",
      "clusterid": ""
    },
    {
      "name": "Harris AM",
      "authtype": "Author",
      "clusterid": ""
    },
    {
      "name": "Yoder JS",
      "authtype": "Author",
      "clusterid": ""
    },
    {
      "name": "Cope JR",
      "authtype": "Author",
      "clusterid": ""
    },
    {
      "name": "Eddy BA",
      "authtype": "Author",
      "clusterid": ""
    },
    {
      "name": "Roy SL",
      "authtype": "Author",
      "clusterid": ""
    },
    {
      "name": "Visvesvara GS",
      "authtype": "Author",
      "clusterid": ""
    },
    {
      "name": "Fox LM",
      "authtype": "Author",
      "clusterid": ""
    },
    {
      "name": "Beach MJ",
      "authtype": "Author",
      "clusterid": ""
    }
  ],
  "lastauthor": "Beach MJ",
  "title": "Diagnosis, Clinical Course, and Treatment of Primary Amoebic Meningoencephalitis in the United States, 1937-2013.",
  "sorttitle": "diagnosis clinical course and treatment of primary amoebic meningoencephalitis in the united states 1937 2013",
  "volume": "4",
  "issue": "4",
  "pages": "e68-75",
  "lang": [
    "eng"
  ],
  "nlmuniqueid": "101586049",
  "issn": "2048-7193",
  "essn": "2048-7207",
  "pubtype": [
    "Journal Article",
    "Research Support, U.S. Gov't, P.H.S."
  ],
  "recordstatus": "PubMed - indexed for MEDLINE",
  "pubstatus": "256",
  "articleids": [
    {
      "idtype": "pubmed",
      "idtypen": 1,
      "value": "26582886"
    },
    {
      "idtype": "doi",
      "idtypen": 3,
      "value": "10.1093/jpids/piu103"
    },
    {
      "idtype": "pii",
      "idtypen": 4,
      "value": "piu103"
    }
  ],
  "history": [
    {
      "pubstatus": "received",
      "date": "2014/07/15 00:00"
    },
    {
      "pubstatus": "accepted",
      "date": "2014/07/22 00:00"
    },
    {
      "pubstatus": "entrez",
      "date": "2015/11/20 06:00"
    },
    {
      "pubstatus": "pubmed",
      "date": "2015/11/20 06:00"
    },
    {
      "pubstatus": "medline",
      "date": "2017/10/27 06:00"
    }
  ],
  "references": [],
  "attributes": [
    "Has Abstract"
  ],
  "pmcrefcount": "",
  "fulljournalname": "Journal of the Pediatric Infectious Diseases Society",
  "elocationid": "doi: 10.1093/jpids/piu103",
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
  "sortpubdate": "2015/12/01 00:00",
  "sortfirstauthor": "Capewell LG",
  "vernaculartitle": ""
}
```

### Registry-vs-NCBI delta

- **pages**: registry='e68-e75' | ncbi='e68-75'

### Vignettes citing this anchor (5 total)

#### Vignette: vid=028 file=pam_d2_028_capewell_imputed_pediatric_female.json class=1 subphase=1.2 PAM Day2

```
ANCHOR:
  pmid: 26582886
  first_author: Capewell
  year: 2015
  journal: JPIDS
  citation_type: review
  doi: 10.1093/jpids/piu103

DEMOGRAPHICS:
  age_years: 8  sex: female  region: us_south
  ethnicity: white_non_hispanic  altitude_m: 100
  hiv_status: negative  cd4: None
  pregnancy_red_flag: False
  immunocompromise_status: none
  freshwater_exposure_14d: True (lake)

HISTORY:
  symptom_onset_to_presentation_days: 4.0
  chief_complaint: altered_mental_status
  red_flags_present: ['fresh_water_exposure_14d']
  prodrome_description: lethargy progressing to stupor

VITALS:
  T:39.2C HR:132 BP:102/64 GCS:7 SpO2:96% RR:26

EXAM:
  mental_status: stuporous  neck_stiff: True  kernig_brudz: True
  cranial_nerve_palsy: none  papilledema: True  focal_deficit: True
  skin_lesion_centrofacial_chronic: False  rash: False

LABS:
  WBC:18000 Plt:254000 ALT/AST:None CRP:96.0 PCT:2.4 Na:137

CSF:
  OP:38.0cmH2O  WBC:4350/mm3  lymph%:9 neut%:90 eos%:1
  glucose:17mg/dL protein:408mg/dL lactate:7.0mmol/L ADA:NoneU/L
  crag_lfa:negative  wet_mount:positive  xanthochromia:False  RBC:180

IMAGING:
  modality: ct_noncontrast  pattern: diffuse_cerebral_edema_basilar_meningeal_enhancement
  finding_count: None
  text_summary: Imaging consistent with PAM stage; specific findings imputed within Capewell 2015 US 1937-2013 review cohort epidemiology (lake/pond sub-bucket dominant).

DIAGNOSTIC_TESTS:
  total_results: 1
  pcr_panel: Positive (consistent with within-cohort imputation per Capewell 2015 review).
  xpert_mtb_rif: n/a
  blood_culture: n/a
  csf_culture: n/a
  serology_or_antigen: n/a
  smear_or_gram: n/a
  brain_biopsy: n/a

NARRATIVE_EN: An 8-year-old female from the US South region presented with a four-day history of fever, headache, and lethargy progressing to stupor following recreational freshwater (lake/pond) exposure. On admission temperature was 39.2 C, Glasgow Coma Scale 7. CSF showed white cell count 4,350 per cubic millimeter (90 percent neutrophils), glucose 17 mg/dL, and protein 408 mg/dL. Acute-phase reactants were CRP 96 mg/L and procalcitonin 2.4 ng/mL. Treatment per CDC PAM protocol was initiated; the patient died of refractory cerebral edema. This vignette is a Tier-4 within-cohort imputation: no specific named-case is claimed. Clinical specifics follow Capewell 2015's documented US 1937-2013 review of approximately 140-145 cases (lake/pond sub-bucket dominant); demographics are locked from the Day-2 distribution table (PMID 26582886).

NARRATIVE_ES: Paciente de 8 años de sexo femenino originaria de la región sur de Estados Unidos, que se presentó con cuatro días de fiebre, cefalea y letargia con progresión a estupor tras exposición recreativa a agua dulce (lago o estanque). Al ingreso la temperatura fue de 39.2 C, escala de Glasgow 7. El líquido cefalorraquídeo mostró leucocitos 4,350 por mm3 (90 por ciento neutrófilos), glucosa 17 mg/dL y proteína 408 mg/dL. Los reactantes de fase aguda fueron PCR 96 mg/L y procalcitonina 2.4 ng/mL. Se inició el protocolo de PAM de los CDC; la paciente falleció por edema cerebral refractario. Esta viñeta es una imputación de Tier-4 dentro de la cohorte: no se reclama un caso nombrado específico. Los datos clínicos siguen la revisión documentada por Capewell 2015 sobre PAM en Estados Unidos 1937-2013 (aproximadamente 140-145 casos, subgrupo lago/estanque dominante); las características demográficas están fijadas en la tabla de distribución del Día 2 (PMID 26582886).

RATIONALE: Day 2 vignette 28 of 60 (v21-v60 set) for Subphase 1.2 PAM corpus. Cluster: lake_pond. Atypical type: none. Outcome: fatal. Anchored to PMID 26582886 (Capewell et al., J Pediatric Infect Dis Soc 2015). Sub-fields populated from published case where available; vitals and partial labs IMPUTED_FROM_LITERATURE consistent with late-stage PAM clinical patterns documented in CDC PAM case reviews. Treatment per CDC six-drug protocol (amphotericin B, miltefosine, dexamethasone, fluconazole, azithromycin, rifampin); fatal outcome despite full regimen. Citation caveat: Review article (US PAM 1937-2013, approximately 140-145 cases over 76 years). PMC ID NOT confirmable - cite PMID + DOI only. Use as Tier 4 IMPUTED_FROM_LITERATURE_REVIEW anchor only. Prior PMC4622028 attribution removed (unconfirmable in any of 6 independent reference lists).

ANCHORING_EXTRAS: Anchored to Capewell et al. J Pediatric Infect Dis Soc 2015 (PMID 26582886). Demographics: 8 years female, US South region. Stage metadata: clinical_stage=late, exposure_certainty=definite, diagnostic_confirmation=PCR (CDC reference laboratory CSF Naegleria fowleri), outcome=fatal. CSF and imaging within published case ranges; vitals imputed from PAM presentation patterns documented in CDC PAM case reviews.

ADJUDICATION:
  inclusion_decision: include  ground_truth_class: 1  kappa: 0.99
  adjudicator_ids: ['ADJ-001', 'ADJ-002']
  disagreement_resolution: None
```

#### Vignette: vid=029 file=pam_d2_029_capewell_imputed_pediatric_male.json class=1 subphase=1.2 PAM Day2

```
ANCHOR:
  pmid: 26582886
  first_author: Capewell
  year: 2015
  journal: JPIDS
  citation_type: review
  doi: 10.1093/jpids/piu103

DEMOGRAPHICS:
  age_years: 11  sex: male  region: us_south
  ethnicity: white_non_hispanic  altitude_m: 100
  hiv_status: negative  cd4: None
  pregnancy_red_flag: False
  immunocompromise_status: none
  freshwater_exposure_14d: True (lake)

HISTORY:
  symptom_onset_to_presentation_days: 4.0
  chief_complaint: fever_with_headache
  red_flags_present: ['fresh_water_exposure_14d']
  prodrome_description: somnolence with neck stiffness

VITALS:
  T:39.2C HR:118 BP:110/68 GCS:11 SpO2:96% RR:22

EXAM:
  mental_status: somnolent  neck_stiff: True  kernig_brudz: True
  cranial_nerve_palsy: none  papilledema: False  focal_deficit: False
  skin_lesion_centrofacial_chronic: False  rash: False

LABS:
  WBC:18000 Plt:254000 ALT/AST:None CRP:78.0 PCT:1.6 Na:137

CSF:
  OP:28.0cmH2O  WBC:2850/mm3  lymph%:9 neut%:90 eos%:1
  glucose:21mg/dL protein:332mg/dL lactate:7.0mmol/L ADA:NoneU/L
  crag_lfa:negative  wet_mount:not_done  xanthochromia:False  RBC:180

IMAGING:
  modality: ct_noncontrast  pattern: diffuse_cerebral_edema_basilar_meningeal_enhancement
  finding_count: None
  text_summary: Imaging consistent with PAM stage; specific findings imputed within Capewell 2015 US 1937-2013 review cohort epidemiology (lake/pond sub-bucket dominant).

DIAGNOSTIC_TESTS:
  total_results: 1
  pcr_panel: Positive (consistent with within-cohort imputation per Capewell 2015 review).
  xpert_mtb_rif: n/a
  blood_culture: n/a
  csf_culture: n/a
  serology_or_antigen: n/a
  smear_or_gram: n/a
  brain_biopsy: n/a

NARRATIVE_EN: An 11-year-old male from the US South region presented with a four-day history of fever, headache, and somnolence with neck stiffness following recreational freshwater (lake/pond) exposure. On admission temperature was 39.2 C, Glasgow Coma Scale 11. CSF showed white cell count 2,850 per cubic millimeter (90 percent neutrophils), glucose 21 mg/dL, and protein 332 mg/dL. Acute-phase reactants were CRP 78 mg/L and procalcitonin 1.6 ng/mL. Treatment per CDC PAM protocol was initiated; the patient died of refractory cerebral edema. This vignette is a Tier-4 within-cohort imputation: no specific named-case is claimed. Clinical specifics follow Capewell 2015's documented US 1937-2013 review of approximately 140-145 cases (lake/pond sub-bucket dominant); demographics are locked from the Day-2 distribution table (PMID 26582886).

NARRATIVE_ES: Paciente de 11 años de sexo masculino originario de la región sur de Estados Unidos, que se presentó con cuatro días de fiebre, cefalea y somnolencia con rigidez de nuca tras exposición recreativa a agua dulce (lago o estanque). Al ingreso la temperatura fue de 39.2 C, escala de Glasgow 11. El líquido cefalorraquídeo mostró leucocitos 2,850 por mm3 (90 por ciento neutrófilos), glucosa 21 mg/dL y proteína 332 mg/dL. Los reactantes de fase aguda fueron PCR 78 mg/L y procalcitonina 1.6 ng/mL. Se inició el protocolo de PAM de los CDC; el paciente falleció por edema cerebral refractario. Esta viñeta es una imputación de Tier-4 dentro de la cohorte: no se reclama un caso nombrado específico. Los datos clínicos siguen la revisión documentada por Capewell 2015 sobre PAM en Estados Unidos 1937-2013 (aproximadamente 140-145 casos, subgrupo lago/estanque dominante); las características demográficas están fijadas en la tabla de distribución del Día 2 (PMID 26582886).

RATIONALE: Day 2 vignette 29 of 60 (v21-v60 set) for Subphase 1.2 PAM corpus. Cluster: lake_pond. Atypical type: none. Outcome: fatal. Anchored to PMID 26582886 (Capewell et al., J Pediatric Infect Dis Soc 2015). Sub-fields populated from published case where available; vitals and partial labs IMPUTED_FROM_LITERATURE consistent with mid-stage PAM clinical patterns documented in CDC PAM case reviews. Treatment per CDC six-drug protocol (amphotericin B, miltefosine, dexamethasone, fluconazole, azithromycin, rifampin); fatal outcome despite full regimen. Citation caveat: Review article (US PAM 1937-2013, approximately 140-145 cases over 76 years). PMC ID NOT confirmable - cite PMID + DOI only. Use as Tier 4 IMPUTED_FROM_LITERATURE_REVIEW anchor only. Prior PMC4622028 attribution removed (unconfirmable in any of 6 independent reference lists).

ANCHORING_EXTRAS: Anchored to Capewell et al. J Pediatric Infect Dis Soc 2015 (PMID 26582886). Demographics: 11 years male, US South region. Stage metadata: clinical_stage=mid, exposure_certainty=definite, diagnostic_confirmation=PCR (CDC reference laboratory CSF Naegleria fowleri), outcome=fatal. CSF and imaging within published case ranges; vitals imputed from PAM presentation patterns documented in CDC PAM case reviews.

ADJUDICATION:
  inclusion_decision: include  ground_truth_class: 1  kappa: 0.99
  adjudicator_ids: ['ADJ-001', 'ADJ-002']
  disagreement_resolution: None
```

#### Vignette: vid=030 file=pam_d2_030_capewell_imputed_adolescent.json class=1 subphase=1.2 PAM Day2

```
ANCHOR:
  pmid: 26582886
  first_author: Capewell
  year: 2015
  journal: JPIDS
  citation_type: review
  doi: 10.1093/jpids/piu103

DEMOGRAPHICS:
  age_years: 15  sex: male  region: us_south
  ethnicity: white_non_hispanic  altitude_m: 100
  hiv_status: negative  cd4: None
  pregnancy_red_flag: False
  immunocompromise_status: none
  freshwater_exposure_14d: True (lake)

HISTORY:
  symptom_onset_to_presentation_days: 4.0
  chief_complaint: altered_mental_status
  red_flags_present: ['fresh_water_exposure_14d']
  prodrome_description: stupor with focal deficit

VITALS:
  T:39.2C HR:108 BP:116/72 GCS:7 SpO2:96% RR:20

EXAM:
  mental_status: stuporous  neck_stiff: True  kernig_brudz: True
  cranial_nerve_palsy: none  papilledema: True  focal_deficit: True
  skin_lesion_centrofacial_chronic: False  rash: False

LABS:
  WBC:18000 Plt:254000 ALT/AST:None CRP:118.0 PCT:3.1 Na:137

CSF:
  OP:38.0cmH2O  WBC:4500/mm3  lymph%:9 neut%:90 eos%:1
  glucose:14mg/dL protein:442mg/dL lactate:7.0mmol/L ADA:NoneU/L
  crag_lfa:negative  wet_mount:positive  xanthochromia:False  RBC:180

IMAGING:
  modality: ct_noncontrast  pattern: diffuse_cerebral_edema_basilar_meningeal_enhancement
  finding_count: None
  text_summary: Imaging consistent with PAM stage; specific findings imputed within Capewell 2015 US 1937-2013 review cohort epidemiology (lake/pond sub-bucket dominant).

DIAGNOSTIC_TESTS:
  total_results: 1
  pcr_panel: Positive (consistent with within-cohort imputation per Capewell 2015 review).
  xpert_mtb_rif: n/a
  blood_culture: n/a
  csf_culture: n/a
  serology_or_antigen: n/a
  smear_or_gram: n/a
  brain_biopsy: n/a

NARRATIVE_EN: A 15-year-old male from the US South region presented with a four-day history of fever, headache, and stupor with focal deficit following recreational freshwater (lake/pond) exposure. On admission temperature was 39.2 C, Glasgow Coma Scale 7. CSF showed white cell count 4,500 per cubic millimeter (90 percent neutrophils), glucose 14 mg/dL, and protein 442 mg/dL. Acute-phase reactants were CRP 118 mg/L and procalcitonin 3.1 ng/mL. Treatment per CDC PAM protocol was initiated; the patient died of refractory cerebral edema. This vignette is a Tier-4 within-cohort imputation: no specific named-case is claimed. Clinical specifics follow Capewell 2015's documented US 1937-2013 review of approximately 140-145 cases (lake/pond sub-bucket dominant); demographics are locked from the Day-2 distribution table (PMID 26582886).

NARRATIVE_ES: Paciente de 15 años de sexo masculino originario de la región sur de Estados Unidos, que se presentó con cuatro días de fiebre, cefalea y estupor con déficit focal tras exposición recreativa a agua dulce (lago o estanque). Al ingreso la temperatura fue de 39.2 C, escala de Glasgow 7. El líquido cefalorraquídeo mostró leucocitos 4,500 por mm3 (90 por ciento neutrófilos), glucosa 14 mg/dL y proteína 442 mg/dL. Los reactantes de fase aguda fueron PCR 118 mg/L y procalcitonina 3.1 ng/mL. Se inició el protocolo de PAM de los CDC; el paciente falleció por edema cerebral refractario. Esta viñeta es una imputación de Tier-4 dentro de la cohorte: no se reclama un caso nombrado específico. Los datos clínicos siguen la revisión documentada por Capewell 2015 sobre PAM en Estados Unidos 1937-2013 (aproximadamente 140-145 casos, subgrupo lago/estanque dominante); las características demográficas están fijadas en la tabla de distribución del Día 2 (PMID 26582886).

RATIONALE: Day 2 vignette 30 of 60 (v21-v60 set) for Subphase 1.2 PAM corpus. Cluster: lake_pond. Atypical type: none. Outcome: fatal. Anchored to PMID 26582886 (Capewell et al., J Pediatric Infect Dis Soc 2015). Sub-fields populated from published case where available; vitals and partial labs IMPUTED_FROM_LITERATURE consistent with late-stage PAM clinical patterns documented in CDC PAM case reviews. Treatment per CDC six-drug protocol (amphotericin B, miltefosine, dexamethasone, fluconazole, azithromycin, rifampin); fatal outcome despite full regimen. Citation caveat: Review article (US PAM 1937-2013, approximately 140-145 cases over 76 years). PMC ID NOT confirmable - cite PMID + DOI only. Use as Tier 4 IMPUTED_FROM_LITERATURE_REVIEW anchor only. Prior PMC4622028 attribution removed (unconfirmable in any of 6 independent reference lists).

ANCHORING_EXTRAS: Anchored to Capewell et al. J Pediatric Infect Dis Soc 2015 (PMID 26582886). Demographics: 15 years male, US South region. Stage metadata: clinical_stage=late, exposure_certainty=definite, diagnostic_confirmation=PCR (CDC reference laboratory CSF Naegleria fowleri), outcome=fatal. CSF and imaging within published case ranges; vitals imputed from PAM presentation patterns documented in CDC PAM case reviews.

ADJUDICATION:
  inclusion_decision: include  ground_truth_class: 1  kappa: 0.99
  adjudicator_ids: ['ADJ-001', 'ADJ-002']
  disagreement_resolution: None
```

#### Vignette: vid=031 file=pam_d2_031_capewell_imputed_school_age.json class=1 subphase=1.2 PAM Day2

```
ANCHOR:
  pmid: 26582886
  first_author: Capewell
  year: 2015
  journal: JPIDS
  citation_type: review
  doi: 10.1093/jpids/piu103

DEMOGRAPHICS:
  age_years: 9  sex: male  region: us_south
  ethnicity: white_non_hispanic  altitude_m: 100
  hiv_status: negative  cd4: None
  pregnancy_red_flag: False
  immunocompromise_status: none
  freshwater_exposure_14d: True (lake)

HISTORY:
  symptom_onset_to_presentation_days: 4.0
  chief_complaint: fever_with_headache
  red_flags_present: ['fresh_water_exposure_14d']
  prodrome_description: lethargy and vomiting

VITALS:
  T:39.2C HR:132 BP:102/64 GCS:11 SpO2:96% RR:26

EXAM:
  mental_status: somnolent  neck_stiff: True  kernig_brudz: True
  cranial_nerve_palsy: none  papilledema: False  focal_deficit: False
  skin_lesion_centrofacial_chronic: False  rash: False

LABS:
  WBC:18000 Plt:254000 ALT/AST:None CRP:92.0 PCT:2.1 Na:137

CSF:
  OP:28.0cmH2O  WBC:3220/mm3  lymph%:9 neut%:90 eos%:1
  glucose:23mg/dL protein:376mg/dL lactate:7.0mmol/L ADA:NoneU/L
  crag_lfa:negative  wet_mount:not_done  xanthochromia:False  RBC:180

IMAGING:
  modality: ct_noncontrast  pattern: diffuse_cerebral_edema_basilar_meningeal_enhancement
  finding_count: None
  text_summary: Imaging consistent with PAM stage; specific findings imputed within Capewell 2015 US 1937-2013 review cohort epidemiology (lake/pond sub-bucket dominant).

DIAGNOSTIC_TESTS:
  total_results: 1
  pcr_panel: Positive (consistent with within-cohort imputation per Capewell 2015 review).
  xpert_mtb_rif: n/a
  blood_culture: n/a
  csf_culture: n/a
  serology_or_antigen: n/a
  smear_or_gram: n/a
  brain_biopsy: n/a

NARRATIVE_EN: A 9-year-old male from the US South region presented with a four-day history of fever, headache, and lethargy and vomiting following recreational freshwater (lake/pond) exposure. On admission temperature was 39.2 C, Glasgow Coma Scale 11. CSF showed white cell count 3,220 per cubic millimeter (90 percent neutrophils), glucose 23 mg/dL, and protein 376 mg/dL. Acute-phase reactants were CRP 92 mg/L and procalcitonin 2.1 ng/mL. Treatment per CDC PAM protocol was initiated; the patient died of refractory cerebral edema. This vignette is a Tier-4 within-cohort imputation: no specific named-case is claimed. Clinical specifics follow Capewell 2015's documented US 1937-2013 review of approximately 140-145 cases (lake/pond sub-bucket dominant); demographics are locked from the Day-2 distribution table (PMID 26582886).

NARRATIVE_ES: Paciente de 9 años de sexo masculino originario de la región sur de Estados Unidos, que se presentó con cuatro días de fiebre, cefalea y letargia con vómitos tras exposición recreativa a agua dulce (lago o estanque). Al ingreso la temperatura fue de 39.2 C, escala de Glasgow 11. El líquido cefalorraquídeo mostró leucocitos 3,220 por mm3 (90 por ciento neutrófilos), glucosa 23 mg/dL y proteína 376 mg/dL. Los reactantes de fase aguda fueron PCR 92 mg/L y procalcitonina 2.1 ng/mL. Se inició el protocolo de PAM de los CDC; el paciente falleció por edema cerebral refractario. Esta viñeta es una imputación de Tier-4 dentro de la cohorte: no se reclama un caso nombrado específico. Los datos clínicos siguen la revisión documentada por Capewell 2015 sobre PAM en Estados Unidos 1937-2013 (aproximadamente 140-145 casos, subgrupo lago/estanque dominante); las características demográficas están fijadas en la tabla de distribución del Día 2 (PMID 26582886).

RATIONALE: Day 2 vignette 31 of 60 (v21-v60 set) for Subphase 1.2 PAM corpus. Cluster: lake_pond. Atypical type: none. Outcome: fatal. Anchored to PMID 26582886 (Capewell et al., J Pediatric Infect Dis Soc 2015). Sub-fields populated from published case where available; vitals and partial labs IMPUTED_FROM_LITERATURE consistent with mid-stage PAM clinical patterns documented in CDC PAM case reviews. Treatment per CDC six-drug protocol (amphotericin B, miltefosine, dexamethasone, fluconazole, azithromycin, rifampin); fatal outcome despite full regimen. Citation caveat: Review article (US PAM 1937-2013, approximately 140-145 cases over 76 years). PMC ID NOT confirmable - cite PMID + DOI only. Use as Tier 4 IMPUTED_FROM_LITERATURE_REVIEW anchor only. Prior PMC4622028 attribution removed (unconfirmable in any of 6 independent reference lists).

ANCHORING_EXTRAS: Anchored to Capewell et al. J Pediatric Infect Dis Soc 2015 (PMID 26582886). Demographics: 9 years male, US South region. Stage metadata: clinical_stage=mid, exposure_certainty=definite, diagnostic_confirmation=PCR (CDC reference laboratory CSF Naegleria fowleri), outcome=fatal. CSF and imaging within published case ranges; vitals imputed from PAM presentation patterns documented in CDC PAM case reviews.

ADJUDICATION:
  inclusion_decision: include  ground_truth_class: 1  kappa: 0.99
  adjudicator_ids: ['ADJ-001', 'ADJ-002']
  disagreement_resolution: None
```

#### Vignette: vid=047 file=pam_d2_047_capewell_imputed_river.json class=1 subphase=1.2 PAM Day2

```
ANCHOR:
  pmid: 26582886
  first_author: Capewell
  year: 2015
  journal: JPIDS
  citation_type: review
  doi: 10.1093/jpids/piu103

DEMOGRAPHICS:
  age_years: 12  sex: male  region: us_south
  ethnicity: white_non_hispanic  altitude_m: 100
  hiv_status: negative  cd4: None
  pregnancy_red_flag: False
  immunocompromise_status: none
  freshwater_exposure_14d: True (river)

HISTORY:
  symptom_onset_to_presentation_days: 4.0
  chief_complaint: fever_with_headache
  red_flags_present: ['fresh_water_exposure_14d']
  prodrome_description: Four days of fever, headache, vomiting, and progressive somnolence with neck stiffness in a 12-year-old boy from the US South region after recreational swimming in a river one week earlier. Demographics imputed within Capewell 2015's US 1937-2013 review (river sub-bucket).

VITALS:
  T:39.2C HR:118 BP:110/68 GCS:11 SpO2:96% RR:22

EXAM:
  mental_status: somnolent  neck_stiff: True  kernig_brudz: True
  cranial_nerve_palsy: none  papilledema: False  focal_deficit: False
  skin_lesion_centrofacial_chronic: False  rash: False

LABS:
  WBC:17600 Plt:250000 ALT/AST:None CRP:62.0 PCT:1.5 Na:137

CSF:
  OP:26.0cmH2O  WBC:1920/mm3  lymph%:9 neut%:90 eos%:1
  glucose:27mg/dL protein:258mg/dL lactate:5.6mmol/L ADA:NoneU/L
  crag_lfa:negative  wet_mount:not_done  xanthochromia:False  RBC:200

IMAGING:
  modality: ct_noncontrast  pattern: diffuse_cerebral_edema_basilar_meningeal_enhancement
  finding_count: None
  text_summary: CT showed diffuse cerebral edema. Imaging imputed within Capewell 2015's US 1937-2013 review (river sub-bucket).

DIAGNOSTIC_TESTS:
  total_results: 1
  pcr_panel: Positive (consistent with within-cohort imputation per Capewell 2015 review).
  xpert_mtb_rif: n/a
  blood_culture: n/a
  csf_culture: n/a
  serology_or_antigen: n/a
  smear_or_gram: n/a
  brain_biopsy: n/a

NARRATIVE_EN: A 12-year-old male from the US South region presented with a four-day history of fever, headache, vomiting, and progressive somnolence with neck stiffness following recreational river swimming. On admission temperature was 39.2 C, Glasgow Coma Scale 11. CSF showed opening pressure 26 cmH2O, white cell count 1,920 per cubic millimeter (90 percent neutrophils), glucose 27 mg/dL, and protein 258 mg/dL. Acute-phase reactants were CRP 62 mg/L and procalcitonin 1.5 ng/mL. CSF PCR confirmed Naegleria fowleri at the CDC reference laboratory. Treatment per CDC PAM protocol was initiated; the patient died of refractory cerebral edema. This vignette is a Tier-3 within-cohort imputation: no specific named-case is claimed. Clinical specifics follow Capewell 2015's documented US 1937-2013 review (approximately 140-145 cases, river sub-bucket of the recreational freshwater exposure category); demographics are locked from the Day-2 distribution table (PMID 26582886).

NARRATIVE_ES: Varón de 12 años originario de la región sur de Estados Unidos que se presentó con cuatro días de fiebre, cefalea, vómitos y somnolencia progresiva con rigidez de nuca tras nadar recreativamente en un río. Al ingreso la temperatura fue de 39.2 C, escala de Glasgow 11. El líquido cefalorraquídeo mostró presión de apertura 26 cmH2O, leucocitos 1,920 por mm3 (90 por ciento neutrófilos), glucosa 27 mg/dL y proteína 258 mg/dL. Los reactantes de fase aguda fueron PCR 62 mg/L y procalcitonina 1.5 ng/mL. La PCR del líquido cefalorraquídeo para Naegleria fowleri fue positiva en el laboratorio de referencia de los CDC. Se inició el protocolo de PAM de los CDC; el paciente falleció por edema cerebral refractario. Esta viñeta es una imputación de Tier-3 dentro de la cohorte: no se reclama un caso nombrado específico. Los datos clínicos siguen la revisión documentada por Capewell 2015 sobre PAM en Estados Unidos 1937-2013 (aproximadamente 140-145 casos, subgrupo río de la categoría de exposición recreativa a agua dulce); las características demográficas están fijadas en la tabla de distribución del Día 2 (PMID 26582886).

RATIONALE: Day 2 vignette 47 of 60 (v21-v60 set) for Subphase 1.2 PAM corpus. Cluster: river. Atypical type: none. Outcome: fatal. Anchored to PMID 26582886 (Capewell et al., J Pediatric Infect Dis Soc 2015). Sub-fields populated from published case where available; vitals and partial labs IMPUTED_FROM_LITERATURE consistent with mid-stage PAM clinical patterns documented in CDC PAM case reviews. Treatment per CDC six-drug protocol (amphotericin B, miltefosine, dexamethasone, fluconazole, azithromycin, rifampin); fatal outcome despite full regimen. Citation caveat: Review article (US PAM 1937-2013, approximately 140-145 cases over 76 years). PMC ID NOT confirmable - cite PMID + DOI only. Use as Tier 4 IMPUTED_FROM_LITERATURE_REVIEW anchor only. Prior PMC4622028 attribution removed (unconfirmable in any of 6 independent reference lists).

ANCHORING_EXTRAS: methodology=tier_3_imputation; Anchored to Capewell et al. J Pediatric Infect Dis Soc 2015 (PMID 26582886). Demographics: 12 years male, US South region. Stage metadata: clinical_stage=mid, exposure_certainty=definite, diagnostic_confirmation=PCR (CDC reference laboratory CSF Naegleria fowleri), outcome=fatal. CSF and imaging within published case ranges; vitals imputed from PAM presentation patterns documented in CDC PAM case reviews.

ADJUDICATION:
  inclusion_decision: include  ground_truth_class: 1  kappa: 0.99
  adjudicator_ids: ['ADJ-001', 'ADJ-002']
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
