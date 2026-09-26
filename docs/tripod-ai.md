# TRIPOD+AI reporting checklist, Amoebanator MLP triage classifier

Per Collins GS et al., *TRIPOD+AI statement: updated guidance for reporting
clinical prediction models that use regression or machine learning methods*,
BMJ 2024;385:e078378 (DOI 10.1136/bmj-2023-078378).

This document maps the Amoebanator release to the TRIPOD+AI 2024 reporting
checklist for clinical prediction models that use regression or machine
learning methods. It distinguishes what the current V1.1 release reports, a
calibration / conformal / out-of-distribution / decision-curve
infrastructure exercised on a 30-row synthetic dataset with a 6-row
validation split, from a clinical prediction study that is pre-specified
but not scheduled: a MIMIC-IV bacterial-vs-viral meningitis proxy with
Naegleria fowleri (PAM) held out for out-of-distribution evaluation. The
author holds PhysioNet credentialed access to MIMIC-IV; this repository
contains and uses no MIMIC-IV data.
Items that need a real cohort are marked **Proxy study**, followed by what
that proxy study would do for each. The pre-specified analysis protocol for
that study is `docs/rare_class_design.md`; model and dataset specifics are
in `docs/model_card.md` and `docs/data_card.md` and are not duplicated here.
Performance metrics are not reported (Section 6); the few fitted values
cited below carry their sample size in the same sentence.

---

## 1. Title and abstract

* **Title.** The repository identifies the work as the development of a
  multivariable prediction model, a binary triage
  classifier, for a low-prevalence neurological-infection target (PAM). V1.1
  predicts the High tier of a synthetic `risk_label`; the proxy study, which
  is not scheduled, would operationalize the target through a
  bacterial-vs-viral meningitis proxy. The predicted outcome is stated in
  `model_card.md` Section 2 and the target population, patients presenting
  with an acute meningitis-like syndrome, in `rare_class_design.md`
  Section 1.
* **Abstract.** The V1.1 repository carries no standalone manuscript
  abstract.

## 2. Introduction

* **Background and rationale.** The healthcare context is diagnostic triage.
  `rare_class_design.md` Section 1 states the clinical question: a patient
  presents with an acute meningitis-like syndrome and the clinician must
  decide how aggressively to escalate, where the cost of missing PAM is
  catastrophic and the cost of over-triaging benign meningitis is modest. The
  rationale for the bacterial-vs-viral proxy task is that PAM is too rare to
  train on directly: a 10 percent test split of the 111 to 167 reported U.S.
  cases holds only 11 to 17 positives, too few to separate model behavior
  from sampling noise (`rare_class_design.md` Section 2; CDC 2025; Yoder
  2010). To the author's knowledge, no published calibrated,
  abstention-aware PAM triage model exists; the contribution is the
  surrounding safety stack, not a new diagnostic test.
* **Objectives and intended use.** The objective is to develop and internally
  exercise an abstention-aware triage classifier together with its
  trustworthy-ML safety stack (temperature scaling, split-conformal abstain,
  Mahalanobis and energy OOD gates, decision curve analysis), and to
  pre-specify the real-data proxy study. V1.1 is development plus an
  infrastructure proof on synthetic data; no real-cohort validation of this
  model exists. The proxy study, which is pre-specified but not scheduled,
  would develop and internally validate a separate bacterial-vs-viral
  classifier on a real cohort, not this model (Section 6, Model evaluation
  and updating). Intended users, intended use, and out-of-scope uses are
  enumerated in `model_card.md` Section 2; the model is explicitly not for
  any clinical decision.

## 3. Methods

* **Source of data.** V1.1 uses 30 synthetic rows created for this demo
  (`outputs/diagnosis_log_pro.csv`); they are not a sample of any patient
  population, their age and sex distribution does not match the published
  case series, and their timestamps are synthetic dates within 2025-2026
  (`data_card.md` Sections 1-3). The data were not used in any prior study and
  no blinding applies because there are no real outcomes. **Proxy study:**
  MIMIC-IV (`hosp.labevents`, `hosp.diagnoses_icd`, `hosp.microbiologyevents`),
  a retrospective, de-identified, single-center research database
  (`rare_class_design.md` Section 3); its loader, `ml/mimic_iv_loader.py`, is
  a scaffold tested only on synthetic MIMIC-shaped data.
* **Participants.** V1.1 instances are hypothetical patients; eligibility is
  synthetic presentations spanning the PAM-typical feature region plus
  benign-meningitis controls (`data_card.md` Section 2). No treatments are
  modeled. **Proxy study:** admissions with at least one CSF analyte and at
  least one ICD-10 meningitis code, with G00.x bacterial as the positive
  class, A87.x viral as the negative class, and B60.2 PAM held out for OOD;
  the 60/20/20 split would be stratified by `icd_label`, and because the
  loader returns one row per `subject_id`, no patient would appear in more
  than one partition (`rare_class_design.md` Section 3).
* **Outcome.** V1.1 predicts whether `risk_label`, assigned at row
  authoring, is High (`y = 1`) or not; 11 of 30 rows are High, 16 Low and 3
  Moderate, and Moderate rows count as not High (`data_card.md` Section 2);
  no outcome-assessment blinding applies to synthetic labels. **Proxy
  study:** the bacterial (G00.x) versus viral (A87.x) ICD-10 label, chosen
  because it maps onto the clinically actionable boundary of whether to start
  empiric antibacterial therapy now. The outcome would be taken from coded
  diagnoses (`hosp.diagnoses_icd`), a different table from the predictors
  (`rare_class_design.md` Section 3), but the codes are assigned from the
  hospital-stay record, which can include the CSF results and the CSF Gram
  stain (the `microscopy` predictor), so outcome assessment would not be
  blinded to the predictors.
* **Predictors.** Ten tabular features after one-hot expansion of symptoms:
  `age`, `csf_glucose`, `csf_protein`, `csf_wbc`, `pcr`, `microscopy`,
  `exposure`, `sym_fever`, `sym_headache`, `sym_nuchal_rigidity`, with the
  schema pinned in `outputs/model/features.json` (`model_card.md` Section 1;
  `data_card.md` Section 4). In V1.1 each row is a hypothetical patient
  presentation, so the predictors describe the patient at presentation; in
  the proxy protocol each CSF value is a per-subject median over admissions
  (`rare_class_design.md` Section 3), not a value restricted to presentation.
  `pcr` and `exposure` are PAM-specific signals absent from MIMIC-IV and
  are dropped or held constant zero in the proxy protocol
  (`rare_class_design.md` Section 3). No predictor-assessment blinding
  applies.
* **Sample size.** V1.1 is n = 30 (n_train = 24, n_val = 6). There is no
  formal power calculation; the size is a deliberately small fixture to
  exercise the infrastructure and is the main limitation
  (`model_card.md` Section 9; `data_card.md` Section 5). Section 7
  (Limitations) states what six rows mean for conformal coverage.
  **Proxy study:** the protocol sets no cohort size, and the study has not
  been run.
* **Missing data.** The bundled CSV has no missing cells; the loader
  applies `df.fillna(0)` after one-hot expansion (`data_card.md` Sections 2
  and 4). **Proxy study:** `ml/mimic_iv_loader.assemble_cohort` takes
  per-subject medians for repeated labs, leaves missing CSF analytes as NaN,
  sets `age`, `pcr` and `exposure` to NaN and `symptoms` to an empty string
  (which `ml/infer.py` reads as no symptoms) on every row, and sets
  `microscopy` to 0 for a subject with no CSF Gram stain record; it fills no
  other predictor.
* **Analytical methods.** A two-class multilayer perceptron (PyTorch),
  `Linear(d, 32) -> ReLU -> Linear(32, 16) -> ReLU -> Linear(16, 2)`, trained
  with cross-entropy and class weighting using Adam (lr = 1e-3) for 500
  steps, full-batch, with random seed 42 (`model_card.md` Section 1). Before
  training, the four continuous inputs (`age`, `csf_glucose`, `csf_protein`,
  `csf_wbc`) are z-scored with the 24 training rows' means and population
  standard deviations, which are saved to `outputs/model/scaler.json` and
  applied unchanged at inference; the six binary inputs stay 0/1
  (`ml/scaling.py`). Three calibrated reference baselines run in the
  ablation: logistic regression with Platt scaling, random forest with
  isotonic calibration, and gradient-boosted trees with isotonic calibration;
  on six test rows their metrics are not meaningful (`model_card.md`
  Section 7). Internal validation is a stratified hold-out; the proxy
  protocol also specifies a class-stratified split, 60/20/20 by `icd_label`
  (`rare_class_design.md` Section 3). Hyperparameters are fixed rather than
  tuned given the fixture size, and this is documented as such; the step
  count, 500, is where the loss on the 24 training rows has
  converged (below 0.001) and was set from the training loss alone, not from
  any validation result.
* **Class imbalance.** Addressed with class weighting, clamped to the interval
  [1, 10] so that the small positive count does not produce explosive losses
  (`model_card.md` Sections 1 and 6).
* **Model output.** The model emits a probability of the High tier,
  temperature-scaled by L-BFGS (Guo et al. 2017), and either a
  prediction, Low or High, or an explicit ABSTAIN carrying a reason field:
  when the Mahalanobis or logit-energy gate flags the input, or when the
  conformal prediction set is empty or contains both classes (`model_card.md`
  Sections 4 and 8). The temperature fit on the six validation rows is
  essentially 1.0 (Section 6), so the probability is the model's own softmax
  output. Output is produced at inference time; an input the Mahalanobis
  gate flags is never scored by the model, so its ABSTAIN carries no
  probability.
* **Training.** The model is trained on the 24-row fold, which also fits the
  input scaler and the Mahalanobis gate (on the seven non-symptom inputs,
  before standardization); the calibration temperature (by L-BFGS), the
  conformal qhat and the energy threshold are fit on the six validation rows
  (`model_card.md` Sections 1, 4 and 5). A small-calibration warning fires at
  every conformal fit until n >= 100.
* **Evaluation.** Performance measures are the AUC of the temperature-scaled
  High probability and recall at the decision-curve-chosen threshold, each
  with bootstrap 95% confidence intervals (n_resamples = 2000); conformal
  coverage at alpha in {0.05, 0.10, 0.20} and the ABSTAIN rate at the chosen
  alpha; decision-curve net benefit; and OOD detection AUC for each gate on
  in-distribution versus PAM rows (`model_card.md` Section 4;
  `rare_class_design.md` Section 4).
  In V1.1, out-of-distribution detection is dual-gated: a Mahalanobis
  distance on the seven non-symptom inputs and an energy score on the
  temperature-scaled logits. The proxy protocol (`rare_class_design.md`
  Section 4) specifies all of these measures except decision-curve net
  benefit: it uses the decision curve only to choose the operating
  threshold, by a rule it leaves open, and `model_card.md` Section 4 lists
  net benefit among the measures a real-data evaluation would report. The
  proxy study is not scheduled, and none of these measures is reported for
  the six validation rows (Section 6).
* **Fairness.** Relevant factors are age, sex, and exposure source
  (`model_card.md` Section 3). V1.1 evaluation is unstratified because the
  6-row split cannot support subgroup analysis, so no fairness metric is
  computed (`model_card.md` Sections 3 and 7). The shipped model encodes no
  race, ethnicity, socio-economic, or geographic attributes. **Proxy study:**
  the protocol in `rare_class_design.md` Section 4 specifies no subgroup
  analysis, and its cohort schema has no sex field (`data_card.md`, last
  section); age-band and sex-stratified evaluation would need a real test
  set (`model_card.md` Section 3).
* **Ethical approval.** Not required for V1.1, which uses only synthetic rows
  and no human-subject data (`data_card.md` Section 3). **Proxy study:** the
  MIMIC-IV records are de-identified and would be used under the PhysioNet
  data use agreement (`data_card.md` Section 3); no IRB determination for
  that use is recorded in this repository.

## 4. Open science

* **Funding.** Unfunded single-author research (`data_card.md` Section 1).
  There is no funder and therefore no funder role in design, analysis, or
  reporting.
* **Competing interests.** None declared for this research codebase.
* **Protocol and registration.** Not registered. This is a research-stage
  methods project, not a prospective clinical study. The analysis protocol for
  the proxy study, which is not scheduled, is pre-specified in
  `docs/rare_class_design.md`.
* **Data availability.** The 30-row synthetic dataset ships in the repository
  at `outputs/diagnosis_log_pro.csv`. MIMIC-IV, the source the proxy study
  would use, is not redistributable and is available only to
  PhysioNet-credentialed users under the MIMIC-IV data use agreement
  (`REPRODUCIBILITY.md` Section 6).
* **Code availability.** All code, covering the model, calibration, conformal
  prediction, OOD gates, decision curve analysis, data loaders, and the test
  suite, is in this repository under the license stated in `README.md`.

## 5. Patient and public involvement

There was no patient or public involvement. The V1.1 dataset is synthetic and
the cohort the proxy study would use is a retrospective, de-identified
research database; no patients or members of the public were involved in the
design, conduct, or reporting of this work.

## 6. Results

* **Participants.** V1.1 uses 30 synthetic rows, 11 High and 19 not
  High (16 Low, 3 Moderate), with an 80/20 stratified split (n_train = 24,
  n_val = 6). The rows have a median age of 23.5 years and 16 of 30 are
  male, unlike the Yoder 2010 cohort (median age 12 years, 79.3% male)
  (`data_card.md` Section 2; `model_card.md` Section 3).
  **Proxy study:** a participant-flow diagram, from admissions screened
  through the CSF and ICD filter to the final cohort by class, would
  accompany a real extraction.
* **Model development.** The final model is the state_dict at
  `outputs/model/model.pt`, with the feature schema in `features.json` and
  the input scaler in `scaler.json`; `python -m ml.training_calib_dca`
  regenerates all three and reproduces `model.pt` bit for bit in the
  environment recorded in `REPRODUCIBILITY.md` Section 2; on another device
  the weights can differ (`REPRODUCIBILITY.md` Section 3; `model_card.md`
  Sections 1 and 6). Its calibration temperature, fit by L-BFGS on the 6
  validation rows, is T = 0.999997,
  essentially the starting value of 1.0: the raw logits classify all six
  rows correctly, so the validation loss has no finite minimum in T, the
  temperature is not identifiable, and the probabilities are the model's own
  softmax outputs (`outputs/model/temperature_scale.json`; `model_card.md`
  Section 7).
* **Model performance.** No performance metrics are reported, because on
  six validation rows they would not be meaningful; see `model_card.md`
  Sections 4, 7 and 9. **Proxy study:** the protocol's measures listed in
  Section 3 (Evaluation), on a real cohort (`rare_class_design.md`
  Section 4).
* **Model evaluation and updating.** V1.1 retrains the model with the same
  architecture, seed and split as the V1.0 model, but on standardized
  continuous inputs and for 500 full-batch steps instead of 60, and
  regenerates every downstream artifact from the same 30 rows with
  `scripts/regenerate_all_artifacts.py` (`model_card.md` Section 1). No
  further update is scheduled. The proxy study would not update this model:
  it would train a separate bacterial-vs-viral classifier and compute the
  protocol's measures listed in Section 3 (Evaluation) on a real cohort
  (`rare_class_design.md` Sections 3 and 4).

## 7. Discussion

* **Interpretation.** The V1.1 contribution is a reproducible
  trustworthy-ML pipeline for a low-prevalence, high-asymmetric-cost triage
  problem, not a validated PAM classifier, and it reports no performance
  metrics (Section 6; `model_card.md` Sections 7 and 9;
  `rare_class_design.md` Section 5).
* **Limitations.** The main limitations are the 6-row validation set,
  the 30-row synthetic dataset, the absence of real bacterial, viral,
  and fungal labels (the proxy study, which is not scheduled, would supply
  bacterial and viral labels; its protocol in `rare_class_design.md`
  Section 3 defines no fungal class), and undefined performance on real
  PAM, neonatal or not, since the model has not been evaluated on a real PAM
  case (`model_card.md` Section 9; `data_card.md` Sections 5 and 7). The six
  validation rows that fit the calibration, the conformal threshold and the
  energy gate cap the conformal target at 6/7 coverage (`model_card.md`
  Section 9), and the raw logits separate them perfectly, so the temperature
  is not identifiable (Section 6). How well the two OOD gates detect shifted
  inputs is not established: on the bundled synthetic OOD benchmark
  (`outputs/metrics/synthetic_ood_benchmark.json`) neither separates
  covariate-shifted rows from the bundled rows (AUC 0.561 for the
  Mahalanobis distance, 0.568 for the logit energy), and the logit-energy
  gate also flags 15 of the 30 bundled rows (`model_card.md` Section 9).
  The most important limitation for a must-not-miss triage tool: run
  through the full pipeline, 18 of the 30 bundled rows abstain, including 8
  of the 11 High rows (6 at the logit-energy gate, 2 at the Mahalanobis
  gate), and only 3 High rows get a High label
  (`outputs/metrics/bundled_outcomes.json`; `model_card.md`, top).
* **Usability and future research.** Out-of-scope uses, namely no clinical
  triage, no PAM diagnosis or rule-out, and no EHR or clinical-decision-support
  deployment, are enumerated in `model_card.md` Section 2. The PhysioNet
  MIMIC-IV proxy study in `docs/rare_class_design.md` is a pre-specified
  protocol that is not scheduled, and it specifies no subgroup analysis;
  `model_card.md` Section 3 notes that age-band and sex-stratified
  evaluation would need a real test set. `model_card.md` Section 2 states
  where the abstention architecture prototyped here has been carried; that
  work is separate from this repository.

## Other information

This checklist follows TRIPOD+AI (Collins GS et al., BMJ 2024); the original
TRIPOD statement (Collins GS et al., 2015) is superseded for all prediction
models, whether they use regression or machine learning. The model card, the
data card, and the proxy-task design document together constitute the
supplementary reporting. Full BibTeX entries are in `docs/references.bib`.

## Coverage of the checklist

The current release covers the development and infrastructure items of
TRIPOD+AI on synthetic data. The participant, real-outcome, real-performance,
and fairness items need a real cohort; the proxy study that would supply one
is pre-specified but not scheduled, and these items are marked Proxy study
above. Run as specified, the proxy study would still not complete the
fairness item: its protocol specifies no subgroup analysis, and its cohort
schema has no sex field; see Section 3 (Fairness).

## References

See `docs/references.bib` for full BibTeX entries. Key citations: Collins GS
et al. BMJ 2024 (TRIPOD+AI); Collins GS et al. 2015 (original TRIPOD,
superseded by TRIPOD+AI); Mitchell M et al. FAT\* 2019 (model cards);
Gebru T et al. CACM 2021 (datasheets); Guo C et al. ICML 2017 (temperature
scaling); Vovk V Mach Learn 2013 and Lei J et al. JASA 2018 (split conformal);
Liu W et al. NeurIPS 2020 (energy OOD); Lee K et al. NeurIPS 2018 (Mahalanobis
OOD); Vickers AJ and Elkin EB Med Decis Making 2006 (decision curve analysis);
Yoder JS et al. Epidemiol Infect 2010 and Cope JR and Ali IK Curr Infect Dis
Rep 2016 (PAM epidemiology and clinical review).
