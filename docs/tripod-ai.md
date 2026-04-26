# TRIPOD+AI checklist — Amoebanator V1.0

Per Collins GS et al., *TRIPOD+AI statement: updated guidance for reporting
clinical prediction models that use regression or machine learning methods*,
BMJ 2024;385:e078378 (DOI 10.1136/bmj-2023-078378; PMID 38626948).
27 items spanning model development, evaluation, fairness, open science,
and patient/public involvement.

---

## Title and abstract

| # | Item | Status | Response |
|---|------|--------|----------|
| 1 | Identification | DONE | This work develops a multivariable prediction model for high-risk meningitis triage; the target population is patients with acute meningitis-like presentations; the outcome is a "high-risk" tier proxy operationalised via bacterial-meningitis ICD-10 codes; ML methods are used (PyTorch MLP + temperature scaling). |
| 2 | Structured summary | Pending preprint | A TRIPOD+AI-for-Abstracts–conformant abstract will accompany the medRxiv submission. The methods + open-science halves are fixed by this checklist; the results half is gated on Phase 6 real-data access. |

## Introduction

| # | Item | Status | Response |
|---|------|--------|----------|
| 3 | Background | DONE | PAM is rare and near-uniformly fatal. Existing prediction models for meningitis triage do not surface a calibrated abstain signal at clinically meaningful low prevalence. Background discussion in `README.md` and `docs/rare_class_design.md`. |
| 4 | Objectives | DONE | (a) Develop a calibrated MLP triage classifier on a bacterial-vs-viral meningitis proxy. (b) Evaluate its safety-stack behaviour (Mahalanobis OOD, logit-energy gate, neg-energy gate, split conformal) under realistic distribution shift. (c) Provide reviewer-grade documentation, audit trail, and reproducibility infrastructure. |

## Methods

| # | Item | Status | Response |
|---|------|--------|----------|
| 5 | Data sources | Partial | Current: bundled `outputs/diagnosis_log_pro.csv` (30 simulated rows). Planned: MIMIC-IV `hosp.labevents` + `hosp.diagnoses_icd` + `hosp.microbiologyevents` filtered on CSF analytes and meningitis ICD codes (loader `ml/mimic_iv_loader.py`). |
| 6 | Participants | Partial | Current: synthetic vignettes. Planned: MIMIC-IV admissions with ≥ 1 CSF lab and ≥ 1 of G00.x, A87.x, or B60.2; subject-disjoint splits to prevent ICU-stay leakage. |
| 7 | Data preparation | DONE | Pipeline: `pd.read_csv` → Safe Harbor scrub (`ml/data_loader.deidentify_dataframe`) → one-hot symptom expansion → `df.fillna(0)` → stratified split (`ml/splits.stratified_split`). Median-impute used inside Mahalanobis. Linkage: subject_id only, no cross-table linkage in V1.0. |
| 8 | Outcome | DONE | Binary outcome: `risk_label == "High"` (mapped from bacterial / amebic ICD codes in the planned MIMIC-IV cohort; encoded as `risk_label` in the bundled CSV). Assessed at row time. No blinding (retrospective records). |
| 9 | Predictors | DONE | Ten predictors: `age`, four CSF labs (glucose, protein, WBC/Total Nucleated Cells, polys%), three binary clinical findings (PCR, microscopy, exposure), three symptom indicators (fever, headache, nuchal rigidity). Pre-selected by domain knowledge per Cope 2016 / Yoder 2010; no automated feature selection. |
| 10 | Sample size | DONE (with caveat) | Current: n_train = 24, n_val = 6 — flagged in every report. Phase 4.1 framework refuses to ship conformal qhats fit on n_cal < 100. Planned MIMIC-IV cohort is expected to exceed 1000 admissions. |
| 11 | Missing data | DONE | Tabular missingness handled via `df.fillna(0)` in the trainer (matches the per-row `_build_feature_vector` behaviour at inference time). Mahalanobis tolerates per-feature NaN by median-imputing before the Z-transform. |
| 12 | Analytical methods | DONE | Architecture: 32-16-2 MLP (PyTorch). Loss: cross-entropy with class weight clamped to [1, 10]. Optimiser: Adam (lr=1e-3, 60 epochs, full-batch). Calibration: L-BFGS temperature scaling on validation logits (Guo 2017). Hyperparameters fixed (no tuning sweep at n = 24). Software: Python 3.12, PyTorch 2.9.1, sklearn 1.8.0; pinned in `requirements.txt`. |
| 13 | Class imbalance | DONE | Class-weighted cross-entropy with the positive-class weight `w_pos = max(1, neg/pos)` clamped to [1, 10]. The clamp prevents the small-fold instability that produced exploding losses without the bound. |
| 14 | Model output | DONE | Output is calibrated `p(High)` ∈ [0, 1] (softmax over the two logit head, post temperature scaling). Operating threshold `0.05` chosen by argmax net-benefit DCA sweep within [0.05, 0.30]. Conformal abstain band defined by qhat from validation nonconformity scores. |
| 15 | Training-evaluation split | DONE | Stratified 80/20 (`random_state = 42`) at training time. Phase 2.5 introduced `ml.splits.stratified_split` with optional group-disjoint constraint (no subject ever appears in more than one partition). Conformal calibration uses a separate held-out half of the validation set per `scripts/eval_coverage_sweep.py`. Data leakage prevention: train-only Mahalanobis fit (`scripts/refit_mahalanobis_train.py`) so per-feature stats never see val/test rows. |
| 16 | Performance measures | DONE | Discrimination: AUC. Calibration: temperature scaling + reliability curve (`outputs/metrics/calibration_curve.png`). Clinical utility: decision curve analysis (`ml/dca.py`, `outputs/metrics/dca_curve.png`). Conformal coverage at α ∈ {0.05, 0.10, 0.20} (`scripts/eval_coverage_sweep.py`). Bootstrap 95 % CI on every metric (`ml/metrics/bootstrap.py`, n_resamples = 2000). |
| 17 | Model updating | DONE | Re-training fully reproduces `outputs/model/model.pt` from `outputs/diagnosis_log_pro.csv` via `python -m ml.training_calib_dca`. Per-event audit log records every re-train. No incremental updating in V1.0. |
| 18 | Fairness | Partial | Current: no subgroup analysis (n = 6 cannot support it). Planned: per-age-band and per-sex AUC + recall + abstain-rate on the MIMIC-IV cohort, with bootstrap CIs. Encoded in the Phase 6 protocol. |

## Open science and patient/public involvement

| # | Item | Status | Response |
|---|------|--------|----------|
| 19 | Funding, COI, protocol, registration, data/code | DONE | Funding: unfunded. COI: none declared. Protocol: this document + `docs/SPRINT_LOG.md` + `docs/rare_class_design.md`. Pre-registration: not applicable for a methods-only release; the future MIMIC-IV evaluation will be pre-registered on OSF prior to running. Code: this repository. Data: bundled synthetic CSV; real-data access via PhysioNet DUA. |
| 20 | Patient and public involvement | Not yet | No PPI in V1.0 (single-author methods preprint). The future DECIDE-AI study will incorporate clinician-user feedback under IRB. |

## Results

| # | Item | Status |
|---|------|--------|
| 21 | Participants | Bundled-data only: n_train = 24, n_val = 6, n_test = 6 per `ml.splits.stratified_split` defaults (60/20/20). Real-data flow pending Phase 6. |
| 22 | Model development | DONE — final model spec in `outputs/model/model.pt` + `outputs/model/features.json` + `outputs/model/temperature_scale.json`. Predictor-importance analysis pending real-data evaluation. |
| 23 | Model performance | Partial — `outputs/metrics/metrics.json` reports AUC = 1.0 / recall = 1.0 on n = 6 with the standing caveat. Bootstrap CI table at `outputs/metrics/ablation_table.{json,csv}`. Subgroup / fairness results pending Phase 6. |
| 24 | Model updating | Not applicable — no recalibration in V1.0 (single training pass per re-run). |

## Discussion

| # | Item | Status | Response |
|---|------|--------|----------|
| 25 | Interpretation | DONE | Bundled-data results are an infrastructure proof. The model responds to its inputs (regression-tested with a 10-row constant-output sentinel), produces a calibrated probability that matches softmax-over-logits-divided-by-T, surfaces three independent OOD signals, and refuses to ship a conformal qhat fitted on n < 100 unless explicitly forced. |
| 26 | Limitations | DONE | (1) n = 6 validation. (2) Synthetic training data. (3) No real subgroup analysis. (4) Single architecture, no hyperparameter sweep. (5) No external validation. (6) PAM-specific deployment claim *explicitly disclaimed* in the model card and README. |
| 27 | Usability and implications | DONE | The methods preprint is intended to demonstrate that calibration / conformal / OOD machinery survives end-to-end wiring on a small but honest dataset. Clinical implications require the future MIMIC-IV evaluation. Monitoring: audit chain at `outputs/audit/audit.jsonl` provides tamper-evident provenance for every training run. |

---

## Differences from TRIPOD 2015 surfaced here

This checklist exposes the five places TRIPOD+AI is more demanding than the
original 2015 statement, and how Amoebanator V1.0 responds:

1. **Item 13 (class imbalance) — new in 2024.** Amoebanator: clamped class
   weight, documented in the model card.
2. **Item 18 (fairness) — new in 2024.** Amoebanator: not yet, deferred to
   Phase 6 with the protocol pre-specified.
3. **Item 19 (open science) — elevated to standalone item in 2024.**
   Amoebanator: full code + audit chain + reproducibility instructions in
   `docs/REPRODUCIBILITY.md` (Phase 9.5).
4. **Item 20 (PPI) — new in 2024.** Amoebanator: not yet, planned for the
   DECIDE-AI study.
5. **Item 12 (computational reproducibility) — expanded in 2024.**
   Amoebanator: pinned `requirements.txt`, Dockerfile, GitHub Actions CI,
   pinned random seeds — see Phase 9 deliverables.

## Status summary

| Status | Count |
|--------|-------|
| DONE | 17 |
| Partial / planned | 7 |
| Not yet | 2 |
| Not applicable | 1 |
| **Total** | **27** |

Every "Not yet" item ties to a live clinical study or a real-data cohort
that has not been accessed; honesty about absence is the appropriate
response, not fabricated evidence.
