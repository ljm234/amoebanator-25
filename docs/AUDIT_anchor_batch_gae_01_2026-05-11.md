# AUDIT batch: class=gae batch=1/1

Generated: 2026-05-11
Vignettes in bundle: 2
Anchors in bundle: 2
Build status: NCBI fetched (mixed)
Bundle type: CLASS-LOCKED-BATCH (class gae, small clusters packed)

## Anchors in this batch

- doi:10.1093/ofid/ofaf695.345 (? ?, n=1)
- pmid:17428307 (Visvesvara 2007, n=1)

## Anchor: DOI 10.1093/ofid/ofaf695.345 | ? ?

### Registry metadata (current state)

```json
{}
```

### NCBI live re-fetch (2026-05-11)

```json
{
  "_doi_only": true
}
```

### Registry-vs-NCBI delta

- **__doi_only__**: registry='n/a' | ncbi='n/a'

### Vignettes citing this anchor (1 total)

#### Vignette: vid=181 file=gae_181_gotuzzo_peru_balamuthia_pilot.json class=6 subphase=1.4 GAE pilot

```
ANCHOR:
  pmid: (none/doi-only)
  first_author: ?
  year: ?
  journal: ?
  citation_type: case_report
  doi: 10.1093/ofid/ofaf695.345

DEMOGRAPHICS:
  age_years: 42  sex: male  region: peru_lima_coast
  ethnicity: mestizo  altitude_m: 154
  hiv_status: negative  cd4: None
  pregnancy_red_flag: False
  immunocompromise_status: none
  freshwater_exposure_14d: False (None)

HISTORY:
  symptom_onset_to_presentation_days: 28.0
  chief_complaint: headache
  red_flags_present: []
  prodrome_description: Four-week neurologic illness in a 42-year-old man from coastal Lima. Subacute progressive headache, intermittent low-grade fevers, and two weeks of word-finding difficulty. Fifteen months earlier the patient had developed a persistent indurated plaque on the central face that had been treated as cutaneous leishmaniasis without resolution. No recent freshwater exposure. Mestizo ethnicity, outdoor manual labor in agricultural soil.

VITALS:
  T:37.6C HR:92 BP:124/78 GCS:13 SpO2:97% RR:18

EXAM:
  mental_status: confused  neck_stiff: False  kernig_brudz: False
  cranial_nerve_palsy: none  papilledema: False  focal_deficit: True
  skin_lesion_centrofacial_chronic: True  rash: False

LABS:
  WBC:8800 Plt:268000 ALT/AST:24 CRP:14.0 PCT:0.2 Na:138

CSF:
  OP:18.0cmH2O  WBC:45/mm3  lymph%:78 neut%:18 eos%:4
  glucose:48mg/dL protein:120mg/dL lactate:2.6mmol/L ADA:NoneU/L
  crag_lfa:negative  wet_mount:negative  xanthochromia:False  RBC:4

IMAGING:
  modality: mri_contrast  pattern: multiple_ring_enhancing_lesions
  finding_count: 3
  text_summary: 3 ring-enhancing lesions: right parietal cortex 1.8 cm, left temporal lobe 1.2 cm, and right cerebellar hemisphere 0.9 cm, each with surrounding vasogenic edema. No basal meningeal enhancement. Pattern characteristic of granulomatous amebic encephalitis.

DIAGNOSTIC_TESTS:
  total_results: 4
  pcr_panel: n/a
  xpert_mtb_rif: n/a
  blood_culture: n/a
  csf_culture: n/a
  serology_or_antigen: Positive, titer 1:512.
  smear_or_gram: n/a
  brain_biopsy: Granulomatous dermatitis with multinucleated giant cells; Balamuthia mandrillaris trophozoites identified on PAS and immunohistochemistry.

NARRATIVE_EN: A 42-year-old mestizo man from coastal Lima, Peru, presented to a national infectious diseases referral hospital with a four-week neurologic illness: subacute progressive headache, intermittent low-grade fevers, and two weeks of word-finding difficulty. Fifteen months earlier he had developed a persistent indurated plaque on the central face that had been treated empirically as cutaneous leishmaniasis without resolution. He worked outdoors in agricultural soil and reported no freshwater exposure. Examination on admission: temperature 37.6 C, Glasgow Coma Scale 13, mild confusion, no neck stiffness, and a right-sided motor deficit. The central facial plaque remained indurated and weeping. CSF showed an opening pressure of 18 cmH2O, white cell count 45 per cubic millimeter with 78 percent lymphocytes, glucose 48 mg/dL, and protein 120 mg/dL. MRI with contrast showed three ring-enhancing lesions in the right parietal cortex, left temporal lobe, and right cerebellar hemisphere. Skin and brain biopsies showed Balamuthia mandrillaris trophozoites on histology and immunohistochemistry. Anchored to Gotuzzo OFID 2026. Pilot, hold_for_revision.

NARRATIVE_ES: Varon mestizo de 42 anos de Lima costera, Peru, ingresado al instituto nacional de salud con cuadro neurologico de cuatro semanas: cefalea subaguda progresiva, fiebre baja intermitente y dos semanas de dificultad para encontrar palabras. Quince meses antes desarrollo una placa indurada persistente en la cara central, tratada empiricamente como leishmaniasis cutanea sin respuesta. Trabaja al aire libre con suelo agricola; sin exposicion a agua dulce. Examen: temperatura 37.6 C, Glasgow 13, confusion leve, sin rigidez de nuca, paresia derecha. La placa centro-facial persiste indurada y supurativa. LCR con presion 18 cmH2O, leucocitos 45 por mm3 (78 por ciento linfocitos), glucosa 48 mg/dL, proteina 120 mg/dL. RM con tres lesiones anulares (parietal derecha, temporal izquierda, hemisferio cerebeloso derecho). Biopsias de piel y cerebro con Balamuthia mandrillaris en histologia e IHC.

RATIONALE: Subphase 1.4 commit 5.4.2 pilot 5 of 6 for Class 6 GAE Balamuthia Peru stratum (master prompt 1.4.6 12/15 Peru-Hispanic with skin lesion 15-month preceding interval). Anchored via DOI to Gotuzzo 2026 OFID supplement (DOI-only entry per PMID_REGISTRY commit 5.4.0 caveat). Three ring-enhancing lesions match multifocal imaging mandate. Pre-adjudication hold_for_revision.

ANCHORING_EXTRAS: Anchored to Gotuzzo E et al. OFID 2026 supplement (doi:10.1093/ofid/ofaf695.345), Peru 68-case Balamuthia retrospective series. 42-year-old Lima mestizo male, centrofacial skin lesion 15 months preceding CNS, modest lymphocytic CSF, three ring-enhancing brain lesions, Balamuthia IFA 1:512, brain biopsy and mNGS positive. Pre-adjudication kappa 0.70.

ADJUDICATION:
  inclusion_decision: hold_for_revision  ground_truth_class: 6  kappa: 0.7
  adjudicator_ids: ['PILOT-GAE-181-ADJ-1', 'PILOT-GAE-181-ADJ-2']
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

## Anchor: PMID 17428307 | Visvesvara 2007

### Registry metadata (current state)

```json
{
  "pmid": "17428307",
  "doi": "10.1111/j.1574-695X.2007.00232.x",
  "authors_short": "Visvesvara GS, Moura H, Schuster FL",
  "authors_full": [
    "Visvesvara GS",
    "Moura H",
    "Schuster FL"
  ],
  "journal": "FEMS Immunol Med Microbiol",
  "journal_short_code": "FEMS-Immunol-Med-Microbiol",
  "year": 2007,
  "volume": "50",
  "issue": "1",
  "pages": "1-26",
  "title": "Pathogenic and opportunistic free-living amoebae: Acanthamoeba spp., Balamuthia mandrillaris, Naegleria fowleri, and Sappinia diploidea",
  "anchor_type": "review",
  "anchor_subtype": "visvesvara_2007_free_living_amoebae_review",
  "verification_confidence": 0.85,
  "verification_method": "claude_web_pubmed_ui_v5_2026_05_11",
  "last_verified_date": "2026-05-11",
  "caveat": "Subphase 1.4 commit 5.4.0 anchor for Class 6 GAE. Canonical Visvesvara 2007 FEMS Immunology review of free-living amoebae (Acanthamoeba spp., B. mandrillaris, N. fowleri, S. diploidea); 26-page comprehensive clinical and epidemiologic phenotype review. Anchor for Acanthamoeba GAE majority stratum. Visvesvara GS is a co-author on multiple existing Subphase 1.1/1.2 PAM registry entries (Naegleria role); this anchor is the Acanthamoeba/Balamuthia role distinct from those. verification_confidence=0.85 pre-direct-fetch."
}
```

### NCBI live re-fetch (2026-05-11)

```json
{
  "uid": "17428307",
  "pubdate": "2007 Jun",
  "epubdate": "2007 Apr 11",
  "source": "FEMS Immunol Med Microbiol",
  "authors": [
    {
      "name": "Visvesvara GS",
      "authtype": "Author",
      "clusterid": ""
    },
    {
      "name": "Moura H",
      "authtype": "Author",
      "clusterid": ""
    },
    {
      "name": "Schuster FL",
      "authtype": "Author",
      "clusterid": ""
    }
  ],
  "lastauthor": "Schuster FL",
  "title": "Pathogenic and opportunistic free-living amoebae: Acanthamoeba spp., Balamuthia mandrillaris, Naegleria fowleri, and Sappinia diploidea.",
  "sorttitle": "pathogenic and opportunistic free living amoebae acanthamoeba spp balamuthia mandrillaris naegleria fowleri and sappinia diploidea",
  "volume": "50",
  "issue": "1",
  "pages": "1-26",
  "lang": [
    "eng"
  ],
  "nlmuniqueid": "9315554",
  "issn": "0928-8244",
  "essn": "",
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
      "value": "17428307"
    },
    {
      "idtype": "doi",
      "idtypen": 3,
      "value": "10.1111/j.1574-695X.2007.00232.x"
    },
    {
      "idtype": "pii",
      "idtypen": 4,
      "value": "FIM232"
    }
  ],
  "history": [
    {
      "pubstatus": "pubmed",
      "date": "2007/04/13 09:00"
    },
    {
      "pubstatus": "medline",
      "date": "2007/10/05 09:00"
    },
    {
      "pubstatus": "entrez",
      "date": "2007/04/13 09:00"
    }
  ],
  "references": [],
  "attributes": [
    "Has Abstract"
  ],
  "pmcrefcount": "",
  "fulljournalname": "FEMS immunology and medical microbiology",
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
  "sortpubdate": "2007/06/01 00:00",
  "sortfirstauthor": "Visvesvara GS",
  "vernaculartitle": ""
}
```

### Registry-vs-NCBI delta

- ALL FIELDS MATCH ✓

### Vignettes citing this anchor (1 total)

#### Vignette: vid=182 file=gae_182_visvesvara_acanthamoeba_aids_pilot.json class=6 subphase=1.4 GAE pilot

```
ANCHOR:
  pmid: 17428307
  first_author: Visvesvara
  year: 2007
  journal: FEMS-Immunol-Med-Microbiol
  citation_type: review
  doi: 10.1111/j.1574-695X.2007.00232.x

DEMOGRAPHICS:
  age_years: 47  sex: male  region: us_south
  ethnicity: white_non_hispanic  altitude_m: 320
  hiv_status: positive_not_on_art  cd4: 38
  pregnancy_red_flag: False
  immunocompromise_status: hiv_cd4_under100
  freshwater_exposure_14d: False (None)

HISTORY:
  symptom_onset_to_presentation_days: 21.0
  chief_complaint: altered_mental_status
  red_flags_present: ['immunocompromise']
  prodrome_description: Three-week subacute encephalopathy in a 47-year-old man with advanced HIV (CD4 38, viral load 480000 copies, ART-naive). Progressive headache, mild fevers, and two weeks of personality change with episodic disorientation. No focal weakness initially; right hemiparesis developed in the final five days. No freshwater exposure. No skin lesions identified on full exam.

VITALS:
  T:37.8C HR:98 BP:118/72 GCS:12 SpO2:96% RR:18

EXAM:
  mental_status: confused  neck_stiff: False  kernig_brudz: False
  cranial_nerve_palsy: none  papilledema: False  focal_deficit: True
  skin_lesion_centrofacial_chronic: False  rash: False

LABS:
  WBC:3200 Plt:178000 ALT/AST:38 CRP:16.0 PCT:0.2 Na:135

CSF:
  OP:16.0cmH2O  WBC:28/mm3  lymph%:72 neut%:22 eos%:6
  glucose:40mg/dL protein:95mg/dL lactate:2.2mmol/L ADA:NoneU/L
  crag_lfa:negative  wet_mount:negative  xanthochromia:False  RBC:2

IMAGING:
  modality: mri_contrast  pattern: multiple_ring_enhancing_lesions
  finding_count: 2
  text_summary: 2 ring-enhancing lesions: left frontal lobe 2.1 cm and right thalamus 1.4 cm, each with surrounding vasogenic edema. No basal meningeal enhancement. Pattern characteristic of granulomatous amebic encephalitis.

DIAGNOSTIC_TESTS:
  total_results: 5
  pcr_panel: n/a
  xpert_mtb_rif: n/a
  blood_culture: n/a
  csf_culture: n/a
  serology_or_antigen: n/a
  smear_or_gram: n/a
  brain_biopsy: Granulomatous inflammation with trophozoites and double-walled cysts; immunohistochemistry positive for Acanthamoeba castellanii.

NARRATIVE_EN: A 47-year-old man in the US South region presented to an academic infectious diseases service with a three-week subacute encephalopathy. He had been diagnosed with HIV ten years prior but had been lost to follow-up; his admission CD4 count was 38 cells per microliter and his viral load was 480000 copies per milliliter, off antiretroviral therapy. He reported progressive headache, mild fevers, and two weeks of personality change with episodic disorientation; right-sided weakness developed in the final five days. There was no freshwater exposure and no contact-lens use. Examination: temperature 37.8 C, Glasgow Coma Scale 12, confused, no neck stiffness, and right hemiparesis. CSF showed an opening pressure of 16 cmH2O, white cell count 28 per cubic millimeter with 72 percent lymphocytes, glucose 40 mg/dL, and protein 95 mg/dL. MRI showed two ring-enhancing lesions in the left frontal lobe and right thalamus. Brain biopsy demonstrated granulomatous inflammation with double-walled cysts and immunohistochemistry positive for Acanthamoeba castellanii. Anchored to Visvesvara FEMS 2007 (PMID 17428307). Pilot, hold_for_revision.

NARRATIVE_ES: Varon de 47 anos en region sur de Estados Unidos, evaluado por enfermedades infecciosas con cuadro encefalopatico subagudo de tres semanas. Diagnostico de VIH hace diez anos, perdido al seguimiento; al ingreso CD4 38 por microlitro, carga viral 480000 copias por mL, sin terapia antirretroviral. Refiere cefalea progresiva, fiebre leve y dos semanas de cambio de personalidad con desorientacion episodica; debilidad derecha en los ultimos cinco dias. Sin exposicion a agua dulce, sin uso de lentes de contacto. Examen: temperatura 37.8 C, Glasgow 12, confuso, sin rigidez de nuca, hemiparesia derecha. LCR con presion 16 cmH2O, leucocitos 28 por mm3 (72 por ciento linfocitos), glucosa 40 mg/dL, proteina 95 mg/dL. RM con dos lesiones anulares (frontal izquierda, talamo derecho). Biopsia cerebral con Acanthamoeba castellanii en IHC.

RATIONALE: Subphase 1.4 commit 5.4.2 pilot 6 of 6 for Class 6 GAE Acanthamoeba immunocompromised stratum (master prompt 1.4.6 10/15 immunocompromised). Anchored to Visvesvara 2007 FEMS canonical free-living amoebae review. Two ring-enhancing lesions match multifocal imaging mandate. Pre-adjudication hold_for_revision.

ANCHORING_EXTRAS: Anchored to Visvesvara GS et al. FEMS Immunol Med Microbiol 2007 (PMID 17428307), canonical free-living amoebae review. 47-year-old US man with AIDS (CD4 38), two ring-enhancing brain lesions, brain biopsy granulomatous with A. castellanii on IHC, mNGS confirmation. Pre-adjudication kappa 0.70.

ADJUDICATION:
  inclusion_decision: hold_for_revision  ground_truth_class: 6  kappa: 0.7
  adjudicator_ids: ['PILOT-GAE-182-ADJ-1', 'PILOT-GAE-182-ADJ-2']
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
