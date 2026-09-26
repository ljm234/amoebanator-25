# Rare-class triage as a low-prevalence proxy task

This document defines the supervised task, explains why PAM is operationalized
through a proxy, and pre-specifies the evaluation protocol for a MIMIC-IV
proxy study. The study is not scheduled and has not been run: the V1.1 model
is built from the 30 bundled synthetic rows in `outputs/diagnosis_log_pro.csv`,
and `ml/mimic_iv_loader.py` is a scaffold tested only on synthetic
MIMIC-shaped data. The loader leaves `age` empty (it does not read the
patients table), sets `microscopy` to 1 for any CSF Gram stain whatever its
result, and does not require the CSF lab and the diagnosis code to share an
admission. It also keeps B60.2 rows in the cohort with `risk_label = "High"`,
the label of the G00.x positive class; only `icd_label = "amebic"` marks them
for the OOD hold-out, so they must be filtered out before training on
`risk_label`. The protocol also leaves open the MIMIC-IV version, the models
and their hyperparameters, the rule for choosing the operating threshold from
the decision curve, and the alpha at which the ABSTAIN rate is reported.
Sections 3 to 5 describe the study as designed, with notes on what the loader
and the V1.1 model actually do; none of it is a result of the study.

---

## 1. The clinical question

A patient presents with acute meningitis-like syndrome (fever, headache,
nuchal rigidity, altered mental status). The clinician must decide, in the
first minutes of the workup, how aggressively to escalate. The worst
outcome, Primary Amebic Meningoencephalitis (PAM), is functionally
untreatable once intracranial pressure rises, so the cost of *missing* a PAM
case is catastrophic. The cost of *over-triaging* a benign meningitis is a
few hours of additional workup and one extra dose of broad-spectrum empiric
therapy.

This is a textbook low-prevalence, high-asymmetric-cost decision problem.

## 2. Why a proxy task

PAM is too rare to train on directly. The CDC reports 167 cumulative U.S.
cases between 1962 and 2024 (CDC, *Naegleria fowleri Infections*,
2025). Yoder et al. 2010 (Epidemiol Infect 138(7):968-975) document 111
cases over a 47-year window with a case-fatality rate of 99.1%. A standard
80/10/10 split of these 111 to 167 cases yields a test set of only 11 to 17
positives, too few to distinguish model behavior from sampling noise.

The proxy task substitutes a *related* high-prevalence supervised problem
that exercises the same triage decision and the same calibration / OOD
machinery, then evaluates the trained model on the rare class as an OOD
held-out set.

## 3. The proxy task

**Source cohort:** MIMIC-IV (`hosp.labevents`, `hosp.diagnoses_icd`,
`hosp.microbiologyevents`) filtered to admissions with at least one CSF
analyte and at least one ICD-10 code in the meningitis ranges:

  * **G00.x**, Bacterial meningitis (positive class, "High")
  * **A87.x**, Viral meningitis (negative class, "Low")
  * **B60.2**, Naegleriasis / PAM (held-out OOD class)

The labeling rule treats bacterial meningitis as the positive class because
the clinical decision the model supports, *should the patient receive
empiric antibacterial therapy now?*, maps onto bacterial-vs-viral
discrimination at exactly the clinically actionable boundary. PAM (B60.2)
sits outside the training distribution and is reserved for OOD evaluation;
`ml/mimic_iv_loader.py` maps only B60.2 to the amebic class, so other B60.x
codes (for example B60.1x, acanthamebiasis) are not treated as OOD.

**Features (extracted from MIMIC-IV per subject):**

| Feature | Source | Notes |
|---------|--------|-------|
| `csf_glucose` | labevents itemid 51790 | median over admissions |
| `csf_protein` | labevents itemid 51802 | median |
| `csf_wbc`     | labevents itemid 52286 | "Total Nucleated Cells, CSF", closest available; MIMIC-IV does not carry a "WBC, CSF" item |
| `csf_polys_pct` | labevents itemid 52281 | neutrophil predominance proxy |
| `microscopy` | microbiologyevents | 1 if any positive CSF Gram stain |
| `age` | patients table | computed at admission |
| `pcr`, `exposure` | not in MIMIC-IV | the loader sets them to NaN; dropped or held at constant zero for the proxy |

`pcr` and `exposure` are PAM-specific signals not represented in MIMIC. The
proxy classifier is fit without them (or with them as constant zero) to
match the available column set. The app's Predict page runs the V1.1 model,
not the proxy classifier, and still takes both as inputs because the V1.1
model uses them. Clinically they are the dominant signals for actual PAM
cases, but the V1.1 model, trained on 24 of the 30 synthetic rows, does not
respond to them that way: with the page's other inputs at their defaults,
checking both gives p_high = 8.6e-05, and the logit-energy gate abstains.

**Splits:** 60/20/20 train/val/test, stratified by `icd_label`. The loader
returns one row per `subject_id`, so the class-stratified split in
`ml/splits.py` (`stratified_split` without `groups`) already keeps each
patient in exactly one partition. Called with `groups`, the same function
makes a group-disjoint split instead; that mode cannot also stratify and only
warns when a partition's positive rate drifts more than 5 percentage points
from the overall rate.

## 4. Evaluation protocol

For each combination of model and ablation cell the protocol calls for:

  * **AUC (calibrated probability)** with bootstrap 95% CI (n_resamples=2000,
    stratified, alpha=0.05) via `ml.metrics.bootstrap.bootstrap_ci`.
  * **Recall at the operating threshold** (the DCA-chosen threshold) with
    the same CI protocol.
  * **Conformal coverage at alpha = 0.05, 0.10, 0.20** on the test split,
    with the conformal threshold (qhat) fit on the held-out validation split,
    which serves as the calibration split.
  * **ABSTAIN rate** at the chosen alpha.
  * **OOD detection AUC** for each of the two gates, Mahalanobis distance
    in feature space and the energy score on the logits, evaluated on
    (in-distribution = bacterial+viral test rows) vs. (OOD = PAM rows from
    B60.2). This is the only experiment that uses the PAM rows.

The target coverage is 1 - alpha. The marginal coverage, the probability
over calibration and test draws that the conformal prediction set contains
the true label, lies between 1 - alpha and 1 - alpha + 1 / (n+1) for n
calibration rows per the Lei et al. 2018 bound (the upper bound assumes no
ties among the scores). The PAM OOD AUC target is >= 0.85, well above
chance, distinctly below the perfect 1.0 that would suggest data leakage.

## 5. Safeguards in the design

* **No PAM-specific training.** The PAM rows are only ever seen at OOD
  evaluation time; the supervised loss never touches them. The headline
  classifier discriminates bacterial vs viral, which is a real, learnable,
  high-prevalence task.
* **No synthetic rows presented as real.** Every row of the proxy study
  comes from MIMIC-IV. `ml/mimic_iv_loader.py` sets `source="mimic_iv"` on
  every row it assembles, including the synthetic MIMIC-shaped rows its
  tests use, so `source` alone does not mark those rows as synthetic (the
  rows `synthesize_mimic_shaped_csvs` writes have subject IDs from
  9,000,000). The 30 bundled demo rows are `source="simulated"`, and rows
  from `ml/case_series.synthesize_yoder_cohort` are
  `source="synthetic_from_yoder2010"`, so those can be filtered out of any
  real-data quoted metric by `source`.
* **No claim that the proxy = PAM.** The bacterial-vs-viral classifier is a
  *proxy for the calibration and OOD machinery*; any PAM-specific deployment
  claim would require prospective validation.

## 6. Dependencies

* PhysioNet credentialed access (CITI training + DUA): obtained; required
  for all real-data evaluation.
* An IRB record: none is recorded in the repository. `ml/irb_gate.py`
  treats MIMIC-IV rows (`source="mimic_iv"`) as real data, not synthetic:
  outside research mode (`AMOEBANATOR_RESEARCH_MODE`), `check_irb_or_raise`
  passes such a cohort only when an approved or conditionally approved IRB
  record is present, like any real dataset. No training entry point calls the
  gate; it runs only in `tests/test_irb_gate.py`.
* Optional: Capewell LG et al., *J Pediatric Infect Dis Soc* 2015;4(4):e68-e75
  (PMID 26582886) for numeric CSF summaries of U.S. PAM cases (median and
  range of WBC, glucose and protein). Cope 2016 reports the patterns
  qualitatively only.

---

**References:**

* Yoder JS, Eddy BA, Visvesvara GS, Capewell L, Beach MJ. *Epidemiol Infect*
  2010;138(7):968-975. PMID 19845995.
* Cope JR, Ali IK. *Curr Infect Dis Rep* 2016;18(10):31. PMID 27614893.
* CDC. *Naegleria fowleri Infections.* 2025.
  https://www.cdc.gov/naegleria/about/index.html
* Lei J, G'Sell M, Rinaldo A, Tibshirani RJ, Wasserman L. *J Am Stat Assoc*
  2018;113(523):1094-1111.
* Vovk V. *Mach Learn* 2013;92(2-3):349-376. (Mondrian / label-conditional
  conformal.)
