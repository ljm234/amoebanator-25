# Data card, Amoebanator bundled dataset

Per Gebru T et al., *Datasheets for Datasets*, Communications of the ACM
2021;64(12):86-92 (DOI 10.1145/3458723; arXiv:1803.09010).

This card documents `outputs/diagnosis_log_pro.csv`, the only dataset the
V1.1 model is trained and evaluated on. It is **30 simulated patient
vignettes**, not real patient data. The literature-anchored vignette registry
under `data/vignettes/` (138 vignettes across six diagnostic classes) also
ships with the repository; no model code reads it, and this card does not
cover it. The card also documents, in its last section, the MIMIC-IV cohort
that the proxy-study protocol in `docs/rare_class_design.md` would use. That
protocol is pre-specified but not scheduled; the cohort is described here so
that the data lineage of any future figure is traceable.

---

## 1. Motivation

* **For what purpose was the dataset created?** To demonstrate the
  Amoebanator calibration / conformal / OOD / DCA pipeline end-to-end on a
  tractable synthetic problem. The dataset exists to prove that the
  *infrastructure* runs. No performance metrics are reported, because on six
  validation rows they would not be meaningful. No real clinical cohort
  replaces it: the MIMIC-IV proxy study in `docs/rare_class_design.md` is a
  pre-specified protocol that is not scheduled (Section 7).
* **Who created the dataset?** Luis Jordan Montenegro-Calla (single-author
  research). No institutional dataset commission.
* **Funding.** Unfunded.
* **Other comments.** The 30 rows are synthetic rows created for this demo.
  They are *not* drawn from any patient population, and their age and sex
  distribution does not match the published PAM case series (Yoder JS et
  al., *Epidemiol Infect* 2010;138:968-975).

## 2. Composition

* **What do the instances represent?** Each row is a hypothetical patient
  presentation with: demographic features (`age`, `sex`), CSF lab values
  (`csf_glucose`, `csf_protein`, `csf_wbc`), three binary clinical findings
  (`pcr`, `microscopy`, `exposure`), a semicolon-separated symptom string
  (`symptoms`), an integer `risk_score`, and a risk-tier label
  (`risk_label` in {"Low", "Moderate", "High"}). Provenance metadata (`case_id`,
  `source`, `physician`, `timestamp_tz`, `comments`) is also included; the
  audit chain does not read it. When the trainer loads the CSV, the chain
  records only the file path and the row and feature counts.
* **How many instances?** **30 rows.** Stratified 80/20 train/val split
  yields **n_train = 24**, **n_val = 6**.
* **Is the dataset a sample of a larger set?** No, every row was generated
  synthetically. The dataset is not a sample of a clinical population.
* **What does each instance consist of?** 16 columns in total: nine raw
  feature columns (`age`, `sex`, `csf_glucose`, `csf_protein`, `csf_wbc`,
  `symptoms`, `pcr`, `microscopy`, `exposure`; the model uses all but `sex`,
  Section 4), two label columns (`risk_label`, `risk_score`) and five
  provenance fields (`case_id`, `source`, `physician`, `timestamp_tz`,
  `comments`).
* **Is there a label/target?** Yes, `risk_label` in {"Low", "Moderate",
  "High"}. The trainer makes it binary: `y = 1` for High, `y = 0` otherwise.
  The bundled CSV has 11 High, 16 Low and 3 Moderate rows. In every row
  the label follows `risk_score` (High for scores 7 to 16, Moderate for 6,
  Low for 1 to 4), so the target is a score-based risk tier, not a confirmed
  diagnosis or clinical outcome; `risk_score` itself is not a model feature.
* **Is any information missing?** Every row is complete (no missing cells in
  the bundled CSV).
* **Are relationships between instances explicit?** No. Each row is
  independent.
* **Recommended splits.** Stratified 80/20 train/val at `random_state = 42`
  per `ml.training_calib_dca`. The `ml.splits.stratified_split` helper
  supports a 60/20/20 train/val/test split for downstream evaluation.
* **Errors / noise / redundancies.** No deliberate noise injection. Cases
  are drawn to span the PAM-typical feature region; some rows represent
  benign-meningitis controls. The free-text `comments` (not a model input)
  do not always match the structured fields. For example, one row (age 37,
  hot springs) lists `fever` in `symptoms` while its comment says "no
  fever"; one Low row (age 48) whose comment says "protein low" has a CSF
  protein of 90 mg/dL, above the normal range; and five Low rows whose
  comments call the CSF near normal, normal-ish, reassuring or benign have a
  CSF WBC of 150 to 450 cells/uL (normal CSF has at most 5).
* **Self-contained?** Self-contained. No external dependencies.
* **Confidential data?** None. Synthetic.
* **Offensive / sensitive content?** None.
* **Data relate to people?** Hypothetical people only. No real individuals.
* **Identifies subpopulations?** The bundled rows are 16 male and 14
  female, so they do not reproduce the 79.3 % male PAM cohort of Yoder 2010.
  Other demographics (race, ethnicity, geography) are not encoded.
* **Possible to identify individuals?** No. There are no real individuals
  in the dataset.
* **Sensitive attributes?** None.

## 3. Collection process

* **How was the data acquired?** Not acquired from any source; see Section
  1.
* **Mechanisms / procedures.** Not applicable to the bundled rows. The
  separate `ml.case_series.synthesize_yoder_cohort` function draws sex and
  exposure source with the Yoder 2010 frequencies and age from a log-normal
  around the Yoder 2010 median of 12 years (spread chosen in the module),
  clipped to the published range. Its CSF values and PCR and microscopy
  rates are the module's own choices, not published values, and it sets
  `exposure = 1`, the same three symptoms and `risk_score = 14` on every
  row. Rows it produces carry `source = "synthetic_from_yoder2010"` and are
  not part of the bundled 30-row CSV.
* **Sampling strategy.** Not applicable (no underlying population).
* **Who was involved?** Single author. No crowdworkers, contractors, or
  annotators.
* **Timeframe.** 2025-2026 (the `timestamp_tz` field carries plausible but
  synthetic dates within this window).
* **Ethical review.** Not required; no human subjects. The MIMIC-IV proxy
  study (a pre-specified protocol that is not scheduled) would use
  de-identified records under the signed PhysioNet DUA; no IRB determination
  for it is recorded in this repository. `ml/irb_gate.py` does not count a
  cohort with `source = "mimic_iv"` (the value `ml/mimic_iv_loader.py`
  sets) as synthetic, so outside research mode (`AMOEBANATOR_RESEARCH_MODE`)
  its check requires an IRB record for such a cohort, as for any real
  dataset; no training entry point calls that check.
* **Data relate to people?** No real people.
* **Notification / consent / impact analysis.** Not applicable.

## 4. Preprocessing / cleaning / labeling

* **Preprocessing applied?** The trainer
  (`ml.training_calib_dca.load_tabular`) applies two transformations at load
  time:
  1. **One-hot symptom expansion**: `symptoms` string -> `sym_<token>`
     binary indicators.
  2. **Vectorization**: `feats = ["age", "csf_glucose", "csf_protein",
     "csf_wbc", "pcr", "microscopy", "exposure", "sym_*"]` ->
     `df[feats].fillna(0).astype(float).values`.

  After the stratified split, `ml.training_calib_dca.main`
  **standardizes** the four continuous inputs (`age`, `csf_glucose`,
  `csf_protein`, `csf_wbc`) with `ml/scaling.py`: each is z-scored with the
  mean and population standard deviation (ddof 0) of the 24 training rows
  only. The binary inputs (`pcr`, `microscopy`, `exposure`, `sym_*`) stay
  0/1. The fitted means and standard deviations are saved to
  `outputs/model/scaler.json`, and inference applies exactly those values.

  `ml/data_loader.load_tabular_safe_harbor` runs the same two load-time
  steps after a partial **Safe Harbor-style scrub** (modeled on HIPAA 45 CFR
  164.514(b)(2), not a complete implementation): ages > 89 capped to 89,
  `physician` field blanked, dates generalized to year, free-text > 20 chars
  passed through the `SafeHarborProcessor` regex scrubber (phone numbers,
  SSNs, email addresses and slash-format dates). Columns that hold direct
  identifiers, such as `name`, `mrn` or `ssn`, pass through unchanged, so it
  does not de-identify a real-data CSV on its own; the trainer does not call
  it.
* **Raw data preserved?** Yes, `outputs/diagnosis_log_pro.csv` is the raw
  form. The preprocessed `(X, y)` is computed in-memory and not persisted
  as a separate artifact; the feature list and the scaler's values are
  saved to `outputs/model/features.json` and `outputs/model/scaler.json`.
* **Preprocessing software.** The trainer's steps are in
  `ml/training_calib_dca.py` and `ml/scaling.py`. The scrubbing loader,
  which the trainer does not call, is in `ml/data_loader.py`; it calls the
  `SafeHarborProcessor` regex scrubber in `ml/data/deidentification.py`.
  Open-sourced as part of this repository.

## 5. Uses

* **Used for any tasks already?** Yes, the bundled MLP in
  `outputs/model/model.pt` and its input scaler
  (`outputs/model/scaler.json`) were fit on this dataset. Calibration,
  conformal qhat, energy thresholds, the Mahalanobis gate statistics,
  decision curves, ablation table, coverage sweep and synthetic OOD
  benchmark all derive from it. Every figure under `outputs/metrics/` is
  downstream of the bundled CSV.
* **Repository linking to papers / systems using the dataset.** This
  repository is the only known consumer.
* **What other tasks could the dataset be used for?** Synthetic-data
  benchmarking of small-sample calibration and conformal prediction
  techniques. Pedagogical examples of decision curve analysis on a very
  small sample (11 of 30 rows are High, so the prevalence is not low).
* **Composition / collection issues that impact future use?** The most
  important issue: **n = 30 is too small to fit anything reliably.** Any
  quoted metric must be paired with the n caveat. The dataset is not
  intended as a benchmark for model performance; it is a fixture for
  testing the surrounding safety machinery.
* **Tasks for which the dataset should not be used.**
  - Quoting AUC / recall / sensitivity / specificity as if they were
    population estimates.
  - Training a model intended for any clinical use.
  - Benchmarking against published meningitis-triage classifiers.

## 6. Distribution

* **Distributed to third parties?** Yes, bundled with the open-source
  Amoebanator code release.
* **How will it be distributed?** Same channel as the code (Git
  repository).
* **When?** Now, included in the V1.1 release; the CSV has shipped
  unchanged since the `v1.0.0` tag.
* **License.** Released under the same MIT License as the code (see
  `LICENSE`). The dataset is provided for research and education and is not
  intended or validated for clinical or commercial use (see `README.md`,
  License and disclaimer section).
* **Third-party IP restrictions.** None; all rows are synthetic. MIMIC-IV
  data, which the pre-specified proxy study would use, is not
  redistributable: it is available only to PhysioNet-credentialed users
  under the MIMIC-IV data use agreement, and none ships with this
  repository.
* **Export / regulatory restrictions.** None applicable to synthetic data.

## 7. Maintenance

* **Who maintains the dataset?** Luis Jordan Montenegro-Calla.
* **How to contact the maintainer.** Contact the maintainer through the
  repository.
* **Errata?** The CSV is unchanged since the `v1.0.0` tag. This card has
  been corrected since then. Among other things, as tagged `v1.0.0` and
  `v1.0.1` it called secondary analysis of MIMIC-IV data IRB-exempt,
  although no IRB determination is recorded (Section 3); described HIPAA
  Safe Harbor de-identification (`ml/data_loader.load_tabular_safe_harbor`)
  as a load-time step of training, although no training entry point calls
  that loader and its scrub is only partial (Section 4); listed only the Low
  and High labels, although the CSV also has 3 Moderate rows; and said the
  rows' feature distributions mimic published PAM presentations and are
  male-biased like Yoder 2010, although their age and sex distribution does
  not match that series and they are 16 male and 14 female (Sections 1
  and 2). The model and every artifact fitted on this dataset have also
  been regenerated since those tags, most recently for V1.1, which
  standardizes the continuous inputs (Section 4) and trains for 500 steps
  instead of 60.
  Every correction since `v1.0.1` is listed in the `v1.1.0` release notes:
  https://github.com/ljm234/amoebanator-25/releases/tag/v1.1.0
* **Will the dataset be updated?** No update is scheduled. The MIMIC-IV
  bacterial-vs-viral meningitis proxy study (`docs/rare_class_design.md`;
  cohort schema in the last section of this card) is a pre-specified
  protocol that is not scheduled; the author has PhysioNet credentialed
  access to MIMIC-IV.
* **Retention limits?** Not applicable (synthetic).
* **Older versions supported?** Yes. The V1.0 release is tagged `v1.0.0`
  and `v1.0.1`, and V1.1 is tagged `v1.1.0`; the CSV is the same at every
  tag and remains accessible through the repository history.
* **Mechanism for contributions.** Pull requests via the project
  repository. Adding new synthetic rows requires (a) explicit
  `source = "synthetic_*"` provenance, (b) re-running the audit chain to
  record the addition, (c) re-fitting the input scaler, the model and all
  downstream metrics (`scripts/regenerate_all_artifacts.py` re-runs the
  whole pipeline) so the model card stays synchronized.

---

## Pre-specified dataset (de-identified MIMIC-IV, not scheduled)

The proxy-study protocol in `docs/rare_class_design.md` is pre-specified but
not scheduled. If it is run, it would use a MIMIC-IV cohort with the schema
below. No MIMIC-IV data ships with this repository.

| Field | Source | Notes |
|-------|--------|-------|
| `subject_id` | `hosp.patients.subject_id` | Surrogate ID; never a real MRN |
| `csf_glucose` | `hosp.labevents` itemid 51790 | mg/dL; median per subject |
| `csf_protein` | `hosp.labevents` itemid 51802 | mg/dL; median per subject |
| `csf_wbc` | `hosp.labevents` itemid 52286 | "Total Nucleated Cells, CSF", closest available; MIMIC-IV does not carry "WBC, CSF" |
| `csf_polys_pct` | `hosp.labevents` itemid 52281 | neutrophil % proxy |
| `microscopy` | `hosp.microbiologyevents` | 1 if any positive Gram stain on `spec_type_desc == 'CSF;SPINAL FLUID'` |
| `risk_label` | `hosp.diagnoses_icd` | High = G00.x bacterial; Low = A87.x viral; OOD held-out = B60.2 PAM |
| `pcr`, `exposure` | not in MIMIC-IV | PAM-specific; the proxy model would be fit without them or with them held at 0 |
| `age` | `hosp.patients` | computed at admission |

Loader: `ml/mimic_iv_loader.assemble_cohort`, a scaffold that does not
implement every row above: it does not read `hosp.patients` and leaves `age`,
`pcr` and `exposure` as NaN, sets `microscopy` to 1 for any CSF Gram stain
record whatever its result, and labels B60.2 rows `risk_label = "High"`
(`icd_label = "amebic"` keeps them identifiable for the hold-out).
Smoke-tested end-to-end against synthetic MIMIC-shaped CSVs in
`tests/test_mimic_iv_loader.py`; it has not been run on MIMIC-IV data.
