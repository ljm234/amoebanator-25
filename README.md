# Amoebanator

Research codebase for a calibrated, abstention-aware triage signal for Primary Amebic
Meningoencephalitis (PAM), the rare, near-uniformly fatal CNS infection caused by
*Naegleria fowleri*. The goal of the repository is a defensible preprint that
describes a small but honest classifier surrounded by reviewer-grade safety
machinery: temperature scaling, split conformal prediction with explicit
abstention, two complementary energy-based OOD signals, and decision curve
analysis at clinically realistic prevalences.

> **Research / educational use only.** This is not a cleared medical device,
> not a substitute for clinical judgment, and not validated for unsupervised
> use. Any deployment requires prospective evaluation, site-level threshold
> tuning, and human oversight.

---

## Why PAM

PAM is rare and near-uniformly fatal. The CDC's *About Primary Amebic
Meningoencephalitis* page (last verified 2026-04-24) reports **167 cumulative
US cases between 1962 and 2024 with 4 survivors** — a case-fatality rate of
163 / 167 ≈ **97.6 %** — and notes that "typically, fewer than 10 people a
year in the United States get PAM." See also Cope JR & Ali IK, *Curr Infect
Dis Rep* 2016;18(10):31 (PMID 27614893) for clinical context, and Yoder JS et
al., *Epidemiol Infect* 2010;138(7):968–975 (PMID 19845995) for the
1962–2008 US epidemiology (n = 111 cases, CFR = 110 / 111 ≈ 99.1 %, median
age 12 years, 79.3 % male, 73.6 % freshwater-exposure source). Full citation
records in `docs/references.bib`.

Triage classifiers in this regime fail in two interesting ways: they overfit
on small case-series, and they produce miscalibrated probabilities that are
clinically unreadable. The point of this repository is to make those two
failure modes the explicit subject of the work, not a footnote.

---

## Quickstart

These commands are the canonical happy-path. Each one writes deterministic
artifacts under `outputs/`.

```bash
# 1. Train the MLP, fit temperature scaling, and write val_preds.csv
PYTHONPATH=. python -m ml.training_calib_dca

# 2. Fit the conformal threshold from calibrated probabilities
PYTHONPATH=. python scripts/conformal_fit_from_probs.py

# 3. Fit both energy gates (logit-energy + neg-energy on probability)
PYTHONPATH=. python scripts/fit_gates.py

# 4. Single-case inference from the CLI
PYTHONPATH=. python scripts/infer_cli.py --json '{
  "age": 12, "csf_glucose": 18, "csf_protein": 420, "csf_wbc": 2100,
  "pcr": 1, "microscopy": 1, "exposure": 1,
  "symptoms": "fever;headache;nuchal_rigidity"
}'

# 5. Launch the Streamlit dashboard (live patient widget at the top)
streamlit run app.py
```

The previous quickstart pointed at `scripts/conformal_fit.py`, which crashes on
a missing `val_logits.npy`. The script above (`conformal_fit_from_probs.py`)
is the one that actually works against the artifacts produced by step 1.

---

## What is wired end-to-end

| Layer | Module | Status |
|-------|--------|--------|
| Tabular MLP (PyTorch) | `ml/training.py`, `ml/training_calib_dca.py` | Trained on the bundled CSV, weights in `outputs/model/model.pt` |
| Temperature scaling | `ml/calibration.py` | L-BFGS fit; saved to `outputs/model/temperature_scale.json` |
| Inference + safety stack | `ml/infer.py` | Loads model.pt, applies T, runs OOD → energy → conformal pipeline |
| Split conformal | `ml/conformal.py` | Implemented; calibration set is currently small (see Limitations) |
| Mahalanobis OOD | `ml/ood_simple.py`, `ml/robust.py` | Fit per-feature stats; `outputs/metrics/feature_stats.json` |
| Logit-energy OOD gate | `ml/robust.py`, `scripts/fit_gates.py` | Fit; `outputs/metrics/energy_threshold.json` |
| Neg-energy gate (probability) | `ml/ood_energy.py`, `scripts/fit_gates.py` | Fit; `outputs/metrics/ood_energy.json` |
| Decision curve analysis | `ml/dca.py` | Net-benefit sweep; `outputs/metrics/threshold_pick.json` |
| Streamlit dashboard | `app.py`, `ml/ui_*.py` | Live patient widget + per-phase panels |

A single-row prediction now responds to its inputs (audit bug #1 fixed in
`ml/infer.py`, regression-tested in `tests/test_infer_integration.py` with
a 10-row constant-output sentinel sweep).

---

## What is *not* wired

Several modules under `ml/data/` are scaffolding for future phases of the
roadmap. They have no test coverage in this repo and should be treated as
drafts, not validated components:

```
ml/data/who_database.py         ml/data/dvc_versioning.py
ml/data/synthetic.py            ml/data/versioning.py
ml/data/literature.py           ml/data/quality_assurance.py
ml/data/pathology_atlas.py      ml/data/negative_collection.py
ml/data/labeling.py             ml/data/annotation_protocol.py
```

Six sibling modules (`acquisition.py`, `audit_trail.py`, `clinical.py`,
`compliance.py`, `deidentification.py`, `microscopy.py`) are real and
covered by their respective `tests/test_phase1_1_*.py` suites; they are
not yet wired into the training pipeline (Phase 7 of the roadmap).

---

## Limitations (read this before quoting any number)

* **Dataset size.** Training uses 30 simulated rows (`outputs/diagnosis_log_pro.csv`).
  After an 80/20 stratified split that leaves roughly 24 train / 6 validation
  rows. Headline AUC = 1.0 on n = 6 is statistically meaningless; it appears
  in `metrics.json` because the metric is mathematically defined, not because
  the model has clinical accuracy.
* **Conformal coverage.** Split conformal's coverage guarantee approaches
  `1 − α` only as the calibration set grows. The currently shipped fit uses
  the same 6-row validation split, so the guarantee should be read as
  empirical coverage on a tiny held-out set, not the population-level
  marginal guarantee. Replacing this with a proper held-out calibration set
  of n ≥ 200 is roadmap Phase 4.1.
* **Provenance.** Every row carries `source = "simulated"` and
  `physician = "demo"`. None of the cases came from a clinical record.
* **OOD gates.** Both energy thresholds were fit on the same 6-row
  validation set. They produce a real τ rather than a placeholder, but
  they share the small-sample weakness of the conformal step.
* **Not a diagnostic.** The model is trained to discriminate "high vs not
  high" risk on a synthetic feature distribution. It must not be used to
  rule PAM in or out of any real clinical workflow.

---

## Repository layout

```
app.py                       # Streamlit entry point (live-patient widget on top)
ml/
  infer.py                   # End-to-end inference: model.pt → safety stack → label
  training.py                # Training entry point used in tests
  training_calib_dca.py      # Full pipeline: train + temperature + val_preds + DCA
  calibration.py             # L-BFGS temperature scaling
  conformal.py               # Split conformal + ABSTAIN logic
  dca.py                     # Decision curve analysis sweep
  ood_simple.py, ood.py      # Mahalanobis + entropy gates
  ood_energy.py              # Neg-energy-from-probability gate
  robust.py                  # Tabular robustness + logit-energy gate
  ui_live_patient.py         # Phase 1.3 single-case form
  ui_phase2.py, ui_phase3.py # Per-phase dashboards
  data/                      # Mixed: 6 wired modules + 10 WIP scaffolds
scripts/
  fit_gates.py               # Phase 1.4: fit energy_threshold.json + ood_energy.json
  conformal_fit_from_probs.py
  infer_cli.py
  ...
outputs/
  model/                     # model.pt, features.json, temperature_scale.json
  metrics/                   # All fitted artifacts: conformal, energy, DCA, val_preds
docs/
  AMOEBANATOR_MASTER_PROMPT.md
  model_card.md              # Currently a stub; full Mitchell-et-al. model card is Phase 8.1
tests/                       # 1100+ unit + integration tests
```

---

## Methods, with citations

* **Temperature scaling.** Guo C, Pleiss G, Sun Y, Weinberger KQ. "On Calibration
  of Modern Neural Networks." ICML 2017.
* **Split conformal prediction.** Vovk V, Gammerman A, Shafer G. *Algorithmic
  Learning in a Random World.* Springer, 2005. Lei J et al. "Distribution-Free
  Predictive Inference for Regression." JASA 2018.
* **Energy-based OOD detection.** Liu W, Wang X, Owens J, Li Y. "Energy-based
  Out-of-distribution Detection." NeurIPS 2020.
* **Mahalanobis OOD.** Lee K, Lee K, Lee H, Shin J. "A Simple Unified Framework
  for Detecting Out-of-Distribution Samples and Adversarial Attacks." NeurIPS 2018.
* **Decision curve analysis.** Vickers AJ, Elkin EB. "Decision Curve Analysis:
  A Novel Method for Evaluating Prediction Models." Med Decis Making 2006;26(6):565–574.
* **Model card structure.** Mitchell M et al. "Model Cards for Model Reporting."
  FAccT 2019.
* **PAM clinical baseline.** Cope JR, Ali IK. "Primary Amebic Meningoencephalitis:
  What Have We Learned in the Last 5 Years?" Curr Infect Dis Rep 2016;18(10):31.
  CDC. *Parasites — Naegleria fowleri / Primary Amebic Meningoencephalitis (PAM).*

---

## Tests, lint, type checking

```bash
PYTHONPATH=. python -m pytest tests/ -q          # unit + integration suite
PYTHONPATH=. ruff check .                         # lint
PYTHONPATH=. mypy ml/infer.py                     # strict type check (per file)
```

---

## License and disclaimer

The code is provided for research and educational purposes. It is not a
medical device. The maintainers make no representation regarding fitness
for any clinical, diagnostic, or operational use. Any clinical interpretation
of model output is the responsibility of a licensed clinician operating
within an appropriate regulatory framework.
