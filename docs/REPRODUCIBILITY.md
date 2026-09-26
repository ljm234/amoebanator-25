# Reproducibility, Amoebanator

This document describes how to reproduce the V1.1 results from a clean
checkout, and states what is and is not reproducible. The model and data
cards (`docs/model_card.md`, `docs/data_card.md`) carry the artifact and
dataset detail; this document is the operational recipe and its limits.

---

## 1. Scope

A clean checkout reproduces every V1.1 synthetic-data result: the trained
model with its input scaler and temperature, and the conformal,
out-of-distribution, and decision-curve artifacts, along with the full test
suite. The results match bit for bit only in the environment recorded in
Section 2. There is no real-data result to reproduce: the MIMIC-IV proxy
study in `docs/rare_class_design.md` is a pre-specified protocol that is not
scheduled and has not been run, and MIMIC-IV data is not redistributable; it
must be obtained from PhysioNet under credentialed access.

## 2. Environment

* **Interpreter.** Python 3.12; continuous integration runs Python 3.12 on
  Linux.
* **Dependencies.** `requirements.txt` pins exact versions of torch
  2.9.1, scikit-learn 1.8.0, numpy 2.2.6, pandas 2.3.3, scipy 1.16.3,
  matplotlib 3.10.6, and streamlit 1.52.0, together with the development tools
  pytest 9.0.2, pytest-cov 7.0.0, hypothesis 6.149.1, ruff 0.14.10, and mypy
  1.19.1; it gives pydantic (used by the vignette schema) and jsonschema only
  lower bounds (`pydantic>=2.5.0`, `jsonschema>=4.20.0`). Install with
  `pip install -r requirements.txt`.
* **Accelerator.** None required. Training uses Apple MPS when it is
  available, then CUDA, then the CPU (`select_device` in
  `ml/training_calib_dca.py`); inference loads the model on the CPU.
  `requirements.txt` notes the CPU-only torch wheel index for Linux, which the
  Dockerfile uses; continuous integration installs the default wheel.
* **Environment of the shipped artifacts.** The files listed in Section 8
  were produced on 2026-09-26 on macOS 26.5 (build 25F71), arm64 (Apple M1
  Max), with Python 3.12.14, torch 2.9.1, numpy 2.2.6, scikit-learn 1.8.0,
  scipy 1.16.3, pandas 2.3.3 and matplotlib 3.10.6. The model was trained
  on MPS.

## 3. Determinism and seeds

`ml/seeds.py` holds the global seed configuration. `set_global_seeds()`
(default seed 42, overridable through the `AMOEBANATOR_SEED` environment
variable) pins Python's `random` module, NumPy, and PyTorch (CPU, plus MPS and
CUDA when present), disables cuDNN benchmark mode, and enables deterministic
algorithms, so that two runs on the same hardware and device produce a
bit-identical `model.pt`. The train and validation split uses
`random_state=42`, and some evaluation scripts fix their own seeds (for
example `np.random.default_rng(42)` in the bootstrap and the coverage sweep);
`AMOEBANATOR_SEED` changes neither. Bit-level reproducibility holds only on
the same hardware, device and library build. A different device can change
the weights well beyond the last bits: on the machine in Section 2, training
the 2026-09-25 model (Section 4) on the CPU instead of MPS gave different
weights, so a CPU run should not be expected to reproduce the shipped
`model.pt`.

## 4. Reproducing the model and metrics

* **Model and calibration.** `python -m ml.training_calib_dca` reads the
  synthetic dataset (`outputs/diagnosis_log_pro.csv`), splits it into 24
  training and 6 validation rows (`random_state=42`, stratified on the High
  label), z-scores the four continuous inputs (age, CSF glucose, CSF
  protein, CSF WBC) with the training rows' means and standard deviations,
  trains the MLP under seed 42 for 500 full-batch Adam steps, fits L-BFGS
  temperature scaling on the validation rows, and writes the model artifacts
  (`outputs/model/`: `model.pt`, `features.json`, `scaler.json`,
  `temperature_scale.json`), `outputs/metrics/metrics.json`, and the
  validation predictions used for the calibration and decision-curve plots.
* **Metrics and figures.** The artifacts under `outputs/metrics/` (calibration
  curve, coverage sweep, decision-curve, abstain Pareto, the conformal and
  OOD JSON, the synthetic OOD benchmark, bootstrap confidence intervals, and
  the ablation table) are produced by the training and evaluation pipeline;
  `outputs/metrics/regeneration_summary.json` records the regeneration. Every
  file under `outputs/model/` and `outputs/metrics/` that the model card
  cites is reproducible from the bundled synthetic CSV. Some values the card
  quotes are not stored in any artifact; for example, the bacterial preset's
  `p_high` and the gate at which it abstains come from running
  `ml.infer.infer_one` on the shipped artifacts, and the
  pipeline does not write the training losses the card quotes.
* **Regenerating every artifact.** One command reruns the pipeline, from
  training through every saved threshold and metrics file:

  ```
  PYTHONPATH=. python scripts/regenerate_all_artifacts.py
  ```

  It runs eleven steps in order, which write the 22 artifacts listed in
  Section 8, and writes `outputs/metrics/regeneration_summary.json` with each
  step's command, exit code, duration, any warnings it printed, and whether
  each artifact the step is expected to write exists afterwards, with its
  size and SHA-256. The conformal fit and ablation steps read the miscoverage
  level from `[conformal] alpha` in `config/amoebanator.toml`. Apart from the
  per-step durations in the summary, two runs on the same machine give
  byte-identical artifacts. The ablation refits the MLP, with its own input
  scaler, and the Mahalanobis gate on its own 18-row training split. Its
  gradient-boosting baseline is scikit-learn's `GradientBoostingClassifier`,
  and `ablation_table.json` records the estimator and calibration method each
  model used.
* **Model history.** The `model.pt` tagged `v1.0.0` and `v1.0.1` (SHA-256
  `f92f540188a869c580365409be65e2eada1bd880a773764a0ca9da18b2409924`,
  temperature 0.2723) did not reproduce in the environment of Section 2.
  Running the training code tagged `v1.0.1` unchanged, with the same data
  and seed, gave a different file (SHA-256
  `419aed386950f0d3a871680b10a5b089dd292c109c196bec9bccd5f3003b2a4b`,
  temperature 0.2662). Both files were trained on MPS; the earlier one was
  recorded as produced under Python 3.12.11 on macOS 14. The retrained file
  replaced it on 2026-09-25, and every artifact
  downstream of it was regenerated from it. V1.1 changes the training
  itself: the continuous inputs are standardized (`ml/scaling.py`, saved as
  `outputs/model/scaler.json`), and the MLP is trained for 500 steps instead
  of 60, a number set from the training loss alone (on the standardized
  inputs, about 0.44 after 60 steps and below 0.001 after 500). The V1.1
  `model.pt` is the one listed in Section 8 (SHA-256
  `d3cbf1d8a4a6fcc408dd60d5a40f4494394002cce1cdb1f67c1a8e8b1bbcb599`); two
  complete regenerations in the environment of Section 2 gave the same file.
  Its fitted temperature is 0.999997. The raw logits already classify all six
  validation rows correctly, so the validation loss has no finite minimum in T
  and the temperature is not identifiable; L-BFGS starts at T = 1.0 and leaves
  it essentially there, because the loss is already near zero at that point.
  Every artifact downstream of the model was regenerated.

## 5. Verifying a reproduction

The reproduction is checked by the test suite. Under Python 3.12 with the
pinned requirements, `pytest` passes with one expected failure,
`tests/test_app_presets.py::test_bacterial_preset_predicts_low`, which records
a known limitation of the synthetic training data: the 30 rows contain no
bacterial meningitis that is not PAM, so the model gives the
bacterial-meningitis preset a High probability (about 0.9994), and the
logit-energy gate then abstains, so the result is ABSTAIN rather than the Low
the test expects. That gate also flags 15 of the 30 bundled rows, so the
abstention is not recognition of bacterial meningitis. Two tests are
skipped: the skeleton in `tests/schemas/test_vignette_migration.py`, whose
migration script has not been written, and the pre-correction diff in
`tests/test_viral_anchor_pmid_corrections.py`, which has nothing to compare
once the corrected PMIDs are committed.
`tests/test_reproducibility_checksums.py` checks that Section 8 matches the
shipped artifacts. `ruff check .` reports no issues, and `mypy` reports no
issues on `ml`, `scripts`, `app`, and `streamlit_app.py`. ruff, mypy, and
pytest run in continuous integration on every push (Python 3.12), with every
tool version pinned in `requirements.txt`.

## 6. Data

The 30-row synthetic dataset ships in the repository at
`outputs/diagnosis_log_pro.csv` and is sufficient to reproduce every V1.1
result. The MIMIC-IV proxy study is a pre-specified protocol that is not
scheduled; its cohort would come from MIMIC-IV, which is not redistributable
and requires PhysioNet credentialing and the MIMIC-IV data use agreement. See
`docs/data_card.md` Sections 3 and 6 and its last section (the MIMIC-IV
cohort schema), and the protocol in `docs/rare_class_design.md`.

## 7. Hardware

No accelerator is required: the model is small enough to train and evaluate
in seconds on a laptop CPU. The shipped artifacts were produced on an Apple
M1 Max with the model trained on MPS (Section 2). Continuous integration runs
on ubuntu-latest, where training would use the CPU, so it should not be
expected to reproduce the shipped `model.pt` (Section 3).

## 8. Artifact checksums

SHA-256 of `model.pt` and of the 21 other artifacts that
`scripts/regenerate_all_artifacts.py` writes, as shipped in V1.1. The same
values are recorded in `outputs/metrics/regeneration_summary.json`, which is
not listed because it also records per-step durations, which change on every
run.

| Artifact | SHA-256 |
|---|---|
| `outputs/model/model.pt` | `d3cbf1d8a4a6fcc408dd60d5a40f4494394002cce1cdb1f67c1a8e8b1bbcb599` |
| `outputs/model/features.json` | `c0f534ebe6cb6201ebdc2a1e5189524c8bb78436b77f90f9d43afdb2c35a59eb` |
| `outputs/model/scaler.json` | `8f1912b8e95cce659729e534157add813e993204d71839b6c915afea7fb2033d` |
| `outputs/model/temperature_scale.json` | `729307c8f794a250cd887fb8e793c5c03e85ed3d2df0ac0026b7a48b07dc58f2` |
| `outputs/metrics/val_preds.csv` | `3eb76d2ff8eab57713512c3b3a3819af369095924d38ba6a4f7e84eeaa5ebc41` |
| `outputs/metrics/metrics.json` | `19742e22eb8d1715b15a46a76693aa914590ea3758f3c3aad55f424f5ae0e8e1` |
| `outputs/metrics/feature_stats.json` | `a12ed84874863b12fd3024f836b812aa93b661f64a3c2fa47fd99d68b9659f0f` |
| `outputs/metrics/feature_stats_train.json` | `a12ed84874863b12fd3024f836b812aa93b661f64a3c2fa47fd99d68b9659f0f` |
| `outputs/metrics/energy_threshold.json` | `b1378d08f990d2d49ac1a491c6caf89551a47c6319cd5126cf6b69f88fe1e6db` |
| `outputs/metrics/ood_energy.json` | `b8b34ad17d5d8ea89854099d23f580457e9dd40a3e18a37db04303a529da3ef6` |
| `outputs/metrics/conformal.json` | `5797c3b2576cb47459a93c0ded549ce8478f750a314995311a71a73e227c3de7` |
| `outputs/metrics/conformal_eval.json` | `2224eff53712f66a56a6acecf446a4723e8c3a03b6d334be3cfa90460fa86b7e` |
| `outputs/metrics/ci.json` | `8617631375196f71fb975402085c0e2b6616e500af0541f29937e3d7a9102955` |
| `outputs/metrics/calibration_curve.png` | `bccfc4c4db31cc85b276b142cc82abffcfdaf3f3d51a091d1b424160f7b998bf` |
| `outputs/metrics/dca_curve.png` | `f3edb6404f403e92f9e484c88376aca9e903a69b13d8e7fe1c3507a69e23cfb6` |
| `outputs/metrics/ablation_table.json` | `2d18bb586d998b580aa683d09f5744faa93198564f226ca5e5bf7c8d3da86202` |
| `outputs/metrics/ablation_table.csv` | `ac4f4bccb01c4ca3fd1e3402c14916b913e2ff6c64f8d65d675f50b91eb0e5a0` |
| `outputs/metrics/coverage_sweep.json` | `47e120db4c41ff8c8e7a79a5733f9803b89ccd8d0456c011afddc039a29e81df` |
| `outputs/metrics/coverage_sweep.png` | `9af67cfb70e7fe57242839ba15f5acca7453385f14e4a9b7d67383835c89dd4d` |
| `outputs/metrics/abstain_pareto.json` | `434d45b7a6b56e456d13f25cb3652458a61d54054a59b50919320275366c0b5e` |
| `outputs/metrics/abstain_pareto.png` | `8cce301b99f340a39aad5ee1f678b628217deb5b94fd2f868fcbfabbf2df5bbe` |
| `outputs/metrics/synthetic_ood_benchmark.json` | `bb89593c4f9ebf429681996283d9ce5dd3e94486e0bcb1aa6b16c92256237fc4` |

## What a reproduction shows

In the environment of Section 2 the synthetic-data results reproduce
deterministically, but what they reproduce is an infrastructure check on a
6-row validation split, not clinical performance. No performance claims are
made: the values in `metrics.json` (AUC 1.0 and recall(High) 1.0 on the six
validation rows) are not meaningful at that size. No real-data evaluation
exists. The MIMIC-IV proxy study in `docs/rare_class_design.md` is a
pre-specified protocol that is not scheduled; it would fit a separate
bacterial-versus-viral classifier on MIMIC-IV and test the calibration,
abstention, and OOD machinery on real data, with PAM rows used only as an OOD
hold-out, so it would not measure the V1.1 model or its performance on PAM.

## References

See `docs/references.bib` and the model and data cards for the methods and
dataset detail. Dependency versions are set in `requirements.txt` (Section
2); the test and lint configuration is in `pyproject.toml`, the type-checking
configuration in `mypy.ini`, and the CI jobs in `.github/workflows/ci.yml`.
