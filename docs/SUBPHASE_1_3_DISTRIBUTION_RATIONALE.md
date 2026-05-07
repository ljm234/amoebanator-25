# Subphase 1.3 Distribution Rationale

Pre-vignette-generation lock for Class 2 (Bacterial meningitis) and Class 3
(Viral meningoencephalitis), 60 vignettes total. This document accompanies
`BACTERIAL_DISTRIBUTION` and `VIRAL_DISTRIBUTION` in
`scripts/generate_pam_vignettes.py` and the two `marginals.json` artifacts at
`data/vignettes/v2/class_02_bacterial/` and `data/vignettes/v2/class_03_viral/`.

Tagged at `v2.3.0-subphase1.3-distribution-locked` (commit 5.3.1 of 5).

---

## 1. Master prompt mandate (verbatim)

From `docs/AMOEBANATOR_MASTER_PROMPT.md` Subphase 1.3 (L1403-1420):

> Construct 60 physician-adjudicated synthetic vignettes for the two
> highest-stakes early PAM confounders - Class 2 (acute bacterial meningitis,
> n=30) and Class 3 (acute viral meningoencephalitis, n=30) - covering the
> diseases most likely to be confused with PAM in the first 24-48 hours.

Per L1413 (Class 2) and L1414 (Class 3) the pathogen mandates are:

- Class 2: 21 S. pneumoniae / 4 N. meningitidis / 2 H. influenzae /
  2 Listeria / 1 gram-negative.
- Class 3: 12 HSV-1 / 8 enterovirus / 4 HSV-2 plus VZV / 4 arboviral
  (3 dengue Peru-relevant + 1 EEE) / 2 HSV-PCR-negative-at-72h.

Sanity gate from master prompt 1.3.10: every Class 2 and Class 3 vignette
must have `freshwater_exposure_within_14d=False`. This commit's
`BACTERIAL_DISTRIBUTION` and `VIRAL_DISTRIBUTION` set the field to `False`
on every spec; subsequent commits 5.3.2-5.3.4 will preserve that setting in
the generated JSON files.

## 2. Bacterial pathogen distribution rationale

The 21/4/2/2/1 pathogen mix maps directly to the published epidemiology of
adult community-acquired bacterial meningitis in the Netherlands (van de
Beek 2004 NEJM, PMID 15509818; Bijlsma 2016 Lancet Infect Dis,
PMID 26652862) and to CDC ABCs surveillance for invasive Hib and N.
meningitidis (Soeters 2020 MMWR, PMID 32935747). The Listeria share at 6%
(2/30) reflects Mylonakis 2002 Medicine PMID 11873028 (pregnancy and
elderly skew) plus the IDSA Tunkel 2004 guideline indication for
ampicillin coverage when host factors are present.

Within S. pneumoniae the cohort split is:

- Adult community (Netherlands cohort) baseline: 13 cases (v61, v62, v68,
  v72, v74, v77 and others), reflecting median-presentation patients in
  the 18-50y range.
- Elderly (>= 65y) high-mortality skew: 5 cases (v63, v66, v70, v73, v81)
  including the alcoholic-elderly comorbid risk pattern.
- Pediatric (< 5y): 2 cases (v64 Lima, v67 US South), reflecting global
  surveillance of post-pneumococcal-conjugate-vaccine breakthrough.
- Risk-factor-specific: 1 asplenia (v65), 1 HIV (v78), 1 recurrent CSF
  leak (v69).

N. meningitidis 4 cases cover college outbreak (v82), adolescent
Waterhouse-Friderichsen fatal (v83), Loreto pediatric Peru (v84), and US
military barracks (v85) per Heckenberg 2008 Medicine and CDC ABCs
serogroup distribution.

H. influenzae 2 cases are unimmunized infants (v86 Cusco, v87 US South).
Listeria 2 cases are pregnancy at 30 weeks (v88 Tumbes) and elderly with
sequelae (v89 Netherlands). Gram-negative single case is post-
neurosurgical fatal (v90) per IDSA Tunkel 2004 nosocomial coverage.

## 3. Viral pathogen distribution rationale

The 12/8/4/4/2 mix follows the published etiology of acute viral
encephalitis (Tyler 2018 NEJM PMID 29490180; Granerod 2010 Lancet Infect
Dis PMID 21088000 England population-based study; Whitley 2006 Lancet
Infect Dis PMID 16517432) and IDSA Tunkel 2008 encephalitis guidelines
(PMID 19886816). HSV-1 dominance at 40% (12/30) reflects the etiology
mix in untreated acute-encephalitis cohorts; mesial-temporal T2/FLAIR
hyperintensity is the single most-cited imaging finding and is mandated
for all 12 HSV-1 cases per master prompt test 1.3.4.

Enterovirus 8 cases (27%) follow the most common viral meningitis
agent in pediatric and young-adult populations; pediatric skew is
preserved (5 cases under 18). HSV-2 (2 Mollaret-pattern cases) and VZV
(2 elderly with zoster sequelae) cover the recurrent and reactivation
phenotypes.

Arboviral 4 cases use 3 dengue Peru-anchored (Lima v117, Loreto v118,
Tumbes v119) per master prompt's Peru-relevant mandate plus the 2024 Peru
dengue outbreak (MMWR surveillance), with mandatory thrombocytopenia
(platelets < 150,000 / uL) per master prompt test "test_dengue_vignette
_thrombocytopenia". A single EEE case (v120, US Northeast adult fatal)
provides the high-mortality NA arboviral comparator.

The 2 HSV-PCR-negative-at-72h cases (v103, v104) are the diagnostic-
ambiguity subset for Class 3 - clinical encephalitis phenotype with PCR
negativity that pushes the model toward INVALID-badge or low-confidence
abstention behavior. They are encoded with their own pathogen value
`HSV_PCR_negative_72h` so master-prompt test_hsv1_vignette_mri_temporal
_lobe receives exactly 12 HSV1 cases.

## 4. Geography rationale

Master prompt's Peru anchoring is dictated for arboviral (3 dengue
Peru-relevant, master prompt L1408 + L1414) and is encouraged for
broader LATAM signal in Class 2.

Class 2 Peru anchors (5/30):

- v64: 4-year-old Lima SP (Peruvian pediatric pneumococcal post-PCV
  breakthrough)
- v71: 38-year-old Lima SP (adult community)
- v84: 14-month-old Loreto NM (pediatric meningococcal Amazonia)
- v86: 3-year-old Cusco Hib (highland pediatric Hib unimmunized)
- v88: 28-year-old Tumbes Listeria pregnancy (coastal pregnancy
  surveillance gap)

Class 3 Peru anchors (4/30, dengue 3 mandated + 1 HSV-1 bonus):

- v99: 38-year-old Lima HSV-1 adult (LATAM signal bonus, not mandated)
- v117: 32-year-old Lima dengue with CNS (mandated)
- v118: 28-year-old Loreto dengue (mandated)
- v119: 41-year-old Tumbes dengue (mandated)

Master-prompt test alignment:

- `test_dengue_vignette_thrombocytopenia`: 3/3 dengue have
  `platelet_mandate_below_per_uL = 150000`.
- `test_class_2_3_no_freshwater_exposure`: 60/60 entries have
  `freshwater_exposure_within_14d = False`.

## 5. Diagnostic ambiguity rationale

Master prompt 1.3.5 requires 5 ambiguity cases per class.

Class 2 ambiguity (5 cases, all `partial_antibiotic_pretreatment_
sterile_cultures`):

- v75: 25-year-old female SP partially treated outpatient with
  pre-tap amoxicillin
- v76: 60-year-old male SP partially treated at outside facility
- v79: 45-year-old female SP partially treated
- v80: 33-year-old male SP partially treated
- v84: 14-month-old Loreto NM (Peru) partially treated by community
  health post

These cases test the model's honest uncertainty in the bacterial-meningitis
classification: they have bacterial-typical CSF profile attenuated by prior
beta-lactam exposure, sterile cultures, and a higher-than-baseline
nonconformity score. Subphase 1.4 calibration will check whether the
INVALID badge fires appropriately on these cases.

Class 3 ambiguity (5 cases):

- v103, v104: HSV clinical phenotype with PCR negative at 72h (the
  master-prompt-named ambiguity subset)
- v107: 22-year-old enterovirus with initial neutrophilic CSF mimicking
  bacterial meningitis (early-viral CSF lag pattern)
- v117: Lima dengue with prominent CNS overlap with arbo-encephalitis
  classification
- v113: 28-year-old HSV-2 first episode with prominent meningismus
  raising bacterial differential

## 6. Methodology classifications

Each spec carries an explicit `methodology` field with one of four
canonical values, extending the Subphase 1.2 classification convention:

- `tier_3_imputation_within_cohort_review`: case demographic sampled
  within a published large-cohort review (van de Beek 2004,
  Bijlsma 2016, Mylonakis 2002, Heckenberg 2008, Tyler 2018,
  Granerod 2010, Whitley 2006). 47/60 entries.
- `tier_4_imputation_idsa_guideline_anchored`: case anchored to IDSA
  Tunkel 2004 / 2008 guideline patient-profile recommendations rather
  than a specific cohort. 8/60 entries (Class 2).
- `tier_4_imputation_cdc_abcs_anchored`: case anchored to CDC ABCs
  surveillance distributions (Soeters 2020). 4/60 entries (Class 2 NM
  + Hib).
- `tier_4_imputation_peru_dengue_2024_anchored`: 3 dengue cases anchored
  to Peru 2024 dengue outbreak surveillance.
- `tier_4_imputation_within_review_ambiguity`: 2 HSV-PCR-neg ambiguity
  cases anchored within Granerod 2010 etiology cohort PCR-negative subset.

No `primary_source_direct` entries in 5.3.1 because the distribution lock
commit does not generate per-vignette JSONs - those will be added in
5.3.2 (pilot 6 cases) where primary-source verbatim values are pulled
via PubMed UI direct fetch and the methodology classification is
upgraded accordingly.

## 7. Adjudication disclosure

Master prompt 1.3.7 requires kappa >= 0.7 documented per vignette via
Dr. Garcia's network. Subphase 1.3 commit 5.3.1 ships the distribution
lock without adjudication metadata populated; subsequent commits 5.3.2-
5.3.4 will set `adjudication.cohen_kappa = 0.0`, `adjudication.
disagreement_resolution = None`, and `adjudication.inclusion_decision =
"hold_for_revision"` on every Class 2 / Class 3 vignette JSON, with the
explicit `adjudication.anchoring_documentation` prefix
`adjudication_state=pre_adjudication; ` to make the state empirically
auditable.

The medRxiv preprint Methods section will document the rolling Garcia-
network adjudication and report corpus state at submission. Honest
disclosure preserves the camino largo Subphase 1.2 pattern of marking
imputed and pre-adjudicated entries clearly rather than fabricating
review status.

## 8. HSV-1 imaging mandate and dengue platelet mandate

Per master prompt tests 4 and 5:

- All 12 HSV-1 vignettes (v91-v102) carry `imaging_mandate =
  "mesial_temporal_t2_flair_hyperintensity"` in the spec dict. The
  builders 91-102 in subsequent commits MUST encode
  `imaging.imaging_pattern = "mesial_temporal_t2_flair_hyperintensity"`
  (already a schema enum value).
- All 3 dengue vignettes (v117-v119) carry
  `platelet_mandate_below_per_uL = 150000` in the spec dict. The
  builders 117-119 MUST encode `labs.platelets_per_uL` strictly below
  150,000.

Lock-in tests in this commit assert both mandates at the spec level;
runtime-encoding tests will fire in 5.3.4 when the JSONs ship.

## 9. Per-vignette imputation honesty

Every Class 2 and Class 3 vignette will be a within-cohort or guideline-
anchored imputation, not a direct primary-source case-report. There is no
single PAM-style v25-Linam-Kali-Hardig per-case-report verbatim primary
in this batch (the literature reviews dominate). Each vignette
narrative in subsequent commits will explicitly disclose:

- The methodology tag in `adjudication.anchoring_documentation`
- The cohort/guideline anchor in the EN+ES narrative closing
- The pre-adjudication state
- The diagnostic-ambiguity flag where applicable

This is the same forensic-audit-clean disclosure pattern that closed
Subphase 1.2 commit 5.2.2 at 11/11 Exceptional. Applied proactively,
not retrospectively.

---

**Refs:** Subphase 1.3 commit 5.3.1 of 5. Tag
v2.3.0-subphase1.3-distribution-locked. Next: 5.3.2 pilot 6 vignettes
(3 Bacterial + 3 Viral) with primary-source-direct verification.

medRxiv submission target: 2026-05-28.
