# DECIDE-AI checklist, Amoebanator V1.0

Per Vasey B et al., *Reporting guideline for the early-stage clinical
evaluation of decision support systems driven by artificial intelligence:
DECIDE-AI*, Nature Medicine 2022;28(5):924–933 (DOI 10.1038/s41591-022-01772-9;
PMID 35585198). 27 items: 10 generic + 17 AI-specific.

The Amoebanator V1.0 sprint targets *infrastructure readiness* for a future
DECIDE-AI study. Several items are intentionally answered "Not yet, research
stage" because no live clinical evaluation has been conducted; those answers
are the honest signal a reviewer should look for in an early-stage report.

---

## Title and abstract

| # | Item | Status | Response |
|---|------|--------|----------|
| 1 | Identification as DECIDE-AI study | Not applicable yet | The current artefact is a methods preprint, not a clinical-evaluation manuscript. When a live study is mounted, the title will include "early-stage clinical evaluation". |
| 2 | Structured summary | Not yet | The forthcoming preprint will carry an objectives / methods / results / conclusions abstract per BMJ structured-abstract guidelines. The methods half is fixed by `docs/SPRINT_LOG.md`; the results half will be populated when MIMIC-IV cohort data is accessible. |

## Introduction

| # | Item | Status | Response |
|---|------|--------|----------|
| 3 | Background and rationale | DONE | PAM is rare (167 cumulative US cases through 2024 per CDC) and near-uniformly fatal (CFR > 97 %). Triage classifiers in this regime fail by overfitting on small case-series and producing miscalibrated probabilities. The motivation for the safety stack is documented in `docs/rare_class_design.md`. |
| 4 | Objectives | DONE | Train a calibrated, abstention-aware triage classifier on a bacterial-vs-viral meningitis proxy task (high-prevalence) and evaluate its OOD-detection behaviour on PAM as the rare held-out class. The intended role of the AI is decision *support*, never replacement; outputs are calibrated probabilities + abstain signals, not diagnoses. |

## Methods

| # | Item | Status | Response |
|---|------|--------|----------|
| 5 | Ethical approval | Pending (USER ASSIGNMENT) | Weber State IRB exemption letter is `docs/USER_ASSIGNMENTS.md` step 2. Synthetic-data training does not require IRB; real-data evaluation does. The IRB gate (`ml/irb_gate.py`) refuses to run training on non-synthetic data without an `approved` or `conditionally_approved` JSON record at `outputs/irb/current_irb.json`. |
| 6 | Study design | Planned | Prospective evaluation is out of scope for V1.0. The future DECIDE-AI study will be a single-site, retrospective MIMIC-IV cohort comparison with the bacterial-vs-viral classifier as exposure and clinician triage as comparator. |
| 7 | Participants, patients | Planned | MIMIC-IV CSF cohort (`hosp.labevents` itemids 51790, 51802, 52286, 52281; ICD-10 G00.x / A87.x / B60.2). Eligibility: ≥ 1 CSF analyte and ≥ 1 meningitis diagnosis code. Setting: Beth Israel Deaconess Medical Center, 2008–2019. Recruitment dates: anonymised by MIMIC-IV. |
| 8 | Participants, users | Planned | The Streamlit live-patient widget targets methods researchers, not clinicians. A clinician-facing study would require usability-evaluation participants under separate IRB. |
| 9 | AI system description | DONE | Inputs: 10 tabular features (age, four CSF labs, three binary clinical findings, three symptom indicators). Outputs: calibrated `p(High)` ∈ [0, 1], conformal prediction set ⊆ {High, Low}, three OOD gate flags, four-tier prediction label. Algorithm: 32-16-2 MLP with cross-entropy + class weighting, L-BFGS temperature scaling. Versioned in `outputs/model/model.pt`. |
| 10 | Human-AI interface | DONE | Single Streamlit form widget at the top of `app.py` (mounted by `ml/ui_live_patient.py`). Renders prediction badge with abstain reason, calibrated probability with progress bar, four safety-stack metrics, conformal prediction set, raw-output JSON expander. Disclaimer banner above the form: "Research and educational use only. Not validated for clinical decisions." |
| 11 | Implementation | DONE | Python 3.12, PyTorch 2.9.1, sklearn 1.8.0, Streamlit. Apple Silicon (MPS) preferred at training; CPU-only inference. Containerised via `Dockerfile` (Phase 9.1). No EHR integration in V1.0. |
| 12 | Safety and error mitigation | DONE | Pre-specified safety machinery: Mahalanobis OOD gate (`ml/ood_simple.py`), logit-energy gate (`ml/robust.py`), neg-energy gate (`ml/ood_energy.py`), conformal abstain (`ml/conformal.py` + `ml/conformal_advanced.py`), DCA-chosen operating threshold (`ml/dca.py`). Every inference output carries an abstain reason field. The audit chain (`ml/audit_hooks.py`) records every training run for tamper-evident provenance. |
| 13 | Outcomes | Planned | Primary AI-performance outcome: AUC with bootstrap 95 % CI on the held-out MIMIC-IV test split. Secondary: empirical conformal coverage at α ∈ {0.05, 0.10, 0.20}, OOD detection AUC vs PAM (B60.2) cases. Clinical and user outcomes: out of scope until DECIDE-AI study runs. |
| 14 | Sample size | DONE (with caveat) | Current validation n = 6 is too small for any real estimate, this is the headline limitation. The Phase 4.1 framework refuses to write a population-level conformal qhat unless n_cal ≥ 100. The future MIMIC-IV cohort is expected to yield ≥ 1000 admissions across the relevant ICD codes. |
| 15 | Data analysis | DONE | Statistical analyses: bootstrap CIs (`ml/metrics/bootstrap.py`, n_resamples=2000, stratified). Missing-data handling: `df.fillna(0)` for tabular features, NaN-tolerant Mahalanobis (median-imputed). Subgroup analyses: not yet (Phase 6+). Performance monitoring: audit chain records every `SESSION_END` event with the metrics dict. |
| 16 | Modifications | DONE | Pre-specified modification plan in the V1.0 → V2.0 roadmap (`docs/AMOEBANATOR_MASTER_PROMPT.md`). Any model architecture or feature-set change requires (a) re-training, (b) re-fitting the conformal threshold, (c) re-fitting both energy gates, (d) re-running the bootstrap CI table, (e) updating the model card. The audit chain provides a tamper-evident record of which artefacts were re-emitted. |

## Results

The Results-section items 17–23 are intentionally not reported in this
checklist because no live clinical evaluation has been conducted. They will
populate when the DECIDE-AI study runs against real-data MIMIC-IV access.

| # | Item | Status |
|---|------|--------|
| 17 | Participant flow | Pending Phase 6 |
| 18 | Baseline characteristics | Pending Phase 6 |
| 19 | Modifications during study | Pending Phase 6 |
| 20 | AI system performance | Partial, `outputs/metrics/ablation_table.{json,csv}` reports four-cell ablation on the bundled n = 6 validation set with the explicit limitation that figures are not population estimates |
| 21 | Human factors | Not yet, no clinician users have interacted with the system |
| 22 | Clinical outcomes | Not yet, no patient outcomes measured |
| 23 | Safety and errors | Partial, every training and inference event is recorded in `outputs/audit/audit.jsonl`. No live-deployment errors to report (no live deployment) |

## Discussion

| # | Item | Status | Response |
|---|------|--------|----------|
| 24 | Interpretation | DONE | The bundled n = 6 result (AUC = 1.0) is an infrastructure proof, not a generalisable performance estimate. The interpretation that matters is qualitative: distinct patient inputs produce distinct calibrated probabilities (regression-tested with a 10-row constant-output sentinel), the safety stack fires correctly on out-of-distribution rows (validated by `scripts/synthetic_ood_benchmark.py`), and the conformal calibration warns at every fit until n ≥ 100. |
| 25 | Generalisability | DONE | Generalisability to PAM specifically is *not claimed* and cannot be claimed from a 30-row synthetic dataset. The roadmap target generalisability is to bacterial-vs-viral meningitis triage on a single-site MIMIC-IV cohort, with PAM as held-out OOD evaluation. Cross-site generalisability is V2.0+. |
| 26 | Implications for next stage | DONE | Next stage is the MIMIC-IV proxy evaluation (Phase 6) once PhysioNet credentialed access lands. Readiness assessment: code infrastructure and safety stack are reviewer-grade today (1221 passing tests, mypy clean, ruff clean); the only blocker is data access. After MIMIC-IV evaluation completes, a comparative Phase II clinician-vs-model study would be the next DECIDE-AI step. |

## Other information

| # | Item | Status | Response |
|---|------|--------|----------|
| 27 | Registration, protocol, funding, conflicts | DONE | Registration: not applicable for a methods preprint. Protocol: this checklist + `docs/SPRINT_LOG.md` + `docs/rare_class_design.md`. Funding: unfunded; single-author research. Conflicts of interest: none declared. Data sharing: code is in this repository; the bundled synthetic dataset ships with the code; real-data access depends on PhysioNet DUA (per-user). |

---

## Status summary

| Section | DONE | Partial / planned | Not yet |
|---------|------|-------------------|---------|
| Title & Abstract | 0 | 0 | 2 |
| Introduction | 2 | 0 | 0 |
| Methods | 5 | 7 | 0 |
| Results | 0 | 2 | 5 |
| Discussion | 3 | 0 | 0 |
| Other information | 1 | 0 | 0 |
| **Total** | **11** | **9** | **7** |

The 7 "Not yet" items are exactly the items DECIDE-AI ties to a live
clinical-evaluation study. Until that study runs, no honest answer is
possible; the appropriate response is to declare that the study has not
been mounted, not to fabricate evidence.
