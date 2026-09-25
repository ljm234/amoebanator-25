# Reproducibility, Amoebanator

This document describes how to reproduce the V1.0 results from a clean
checkout, and states plainly what is and is not reproducible. The model and
data cards (`docs/model_card.md`, `docs/data_card.md`) carry the artifact and
dataset detail; this document is the operational recipe and its honest
limits.

---

## 1. Scope

A clean checkout reproduces every V1.0 synthetic-data result: the trained
model, its calibration, and the conformal, out-of-distribution, and
decision-curve artifacts, along with the full test suite. The results match
bit for bit only in the environment recorded in Section 2. The planned
MIMIC-IV proxy study is not reproducible from this repository, because that
data is not redistributable and must be obtained from PhysioNet under
credentialed access; its pre-specified protocol is in
`docs/rare_class_design.md`.

## 2. Environment

* **Interpreter.** Python 3.12; continuous integration runs Python 3.12 on
  Linux.
* **Dependencies.** All versions are pinned in `requirements.txt`: torch
  2.9.1, scikit-learn 1.8.0, numpy 2.2.6, pandas 2.3.3, scipy 1.16.3,
  matplotlib 3.10.6, and streamlit 1.52.0, together with the development tools
  pytest 9.0.2, pytest-cov 7.0.0, hypothesis 6.149.1, ruff 0.14.10, and mypy
  1.19.1, plus pydantic and jsonschema for the vignette schema. Install with
  `pip install -r requirements.txt`.
* **Accelerator.** None required. Training uses Apple MPS when it is
  available, then CUDA, then the CPU (`select_device` in
  `ml/training_calib_dca.py`); inference loads the model on the CPU. A CPU
  wheel index for Linux CI is noted in `requirements.txt`.
* **Environment of the shipped artifacts.** The files listed in Section 8
  were produced on 2026-09-25 on macOS 26.5 (build 25F71), arm64 (Apple M1
  Max), with Python 3.12.14, torch 2.9.1, numpy 2.2.6, scikit-learn 1.8.0,
  scipy 1.16.3, pandas 2.3.3 and matplotlib 3.10.6. The model was trained
  on MPS.

## 3. Determinism and seeds

`ml/seeds.py` is the single source of seed configuration. `set_global_seeds()`
(default seed 42, overridable through the `AMOEBANATOR_SEED` environment
variable) pins Python's `random` module, NumPy, and PyTorch (CPU, plus MPS and
CUDA when present), disables cuDNN benchmark mode, and enables deterministic
algorithms, so that two runs on the same hardware and device produce a
bit-identical `model.pt`. The train and validation split uses
`random_state=42`. Bit-level reproducibility holds only on the same hardware,
device and library build. A different device can change the weights well
beyond the last bits: on the machine in Section 2, training on the CPU
instead of MPS changes some weights by up to 0.025.

## 4. Reproducing the model and metrics

* **Model and calibration.** `python -m ml.training_calib_dca` reads the
  synthetic dataset (`outputs/diagnosis_log_pro.csv`), trains the MLP under
  seed 42, fits L-BFGS temperature scaling, and writes the model artifacts
  (`outputs/model/`: `model.pt`, `features.json`, `temperature_scale.json`)
  and the validation predictions used for the calibration and decision-curve
  plots.
* **Metrics and figures.** The artifacts under `outputs/metrics/` (calibration
  curve, coverage sweep, decision-curve, abstain Pareto, the conformal and
  OOD JSON, bootstrap confidence intervals, and the ablation table) are
  produced by the training and evaluation pipeline;
  `outputs/metrics/regeneration_summary.json` records the regeneration. Every
  figure cited in the model card traces to a file in `outputs/metrics/` and is
  reproducible from the bundled synthetic CSV.
* **Regenerating every artifact.** One command reruns the pipeline, from
  training through every saved threshold and metrics file:

  ```
  PYTHONPATH=. python scripts/regenerate_all_artifacts.py
  ```

  It runs thirteen steps in order and writes
  `outputs/metrics/regeneration_summary.json` with each step's command, exit
  code, duration, any warnings it printed, and whether each artifact the step
  is expected to write exists afterwards. The conformal fit, grouped fit, and
  ablation steps read the miscoverage level from `[conformal] alpha` in
  `config/amoebanator.toml`. Apart from the per-step durations in the summary,
  two runs on the same machine give byte-identical artifacts. The ablation's
  gradient-boosting baseline is scikit-learn's `GradientBoostingClassifier`,
  and `ablation_table.json` records the estimator and calibration method
  each model used. `threshold_pick.json` and `threshold_sweep.csv` are not
  produced by this command.
* **The previous model did not reproduce.** The `model.pt` shipped before
  this release (SHA-256
  `f92f540188a869c580365409be65e2eada1bd880a773764a0ca9da18b2409924`,
  temperature 0.2723) did not reproduce in the environment of Section 2.
  Running the training code tagged `v1.0.1` unchanged, with the same data
  and seed, gives the `model.pt` listed in Section 8 (temperature 0.2662).
  Both files were trained on MPS; the earlier one was recorded as produced
  under Python 3.12.11 on macOS 14. The shipped model and every artifact
  downstream of it were regenerated from the new file.

## 5. Verifying a reproduction

The reproduction is checked by the test suite. Under Python 3.12 with the
pinned requirements, `pytest` passes with one expected failure,
`tests/test_app_presets.py::test_bacterial_preset_predicts_low`, which records
a known limitation of the synthetic training data: the bacterial-meningitis
preset is predicted High. `tests/test_reproducibility_checksums.py` checks
that Section 8 matches the shipped artifacts. `ruff check .` reports no
issues, and `mypy` reports no issues on `ml`, `scripts`, `app`,
`streamlit_app.py` and `outputs/model`. ruff, mypy, and pytest run in
continuous integration on every push (Python 3.12), with every tool version
pinned in `requirements.txt`.

## 6. Data

The 30-row synthetic dataset ships in the repository at
`outputs/diagnosis_log_pro.csv` and is sufficient to reproduce every V1.0
result. The planned MIMIC-IV proxy cohort is not redistributable and requires
PhysioNet credentialing and the MIMIC-IV data use agreement; see
`docs/data_card.md` Section 6 and the protocol in
`docs/rare_class_design.md`.

## 7. Hardware

No accelerator is required: the model is small enough to train and evaluate
in seconds on a laptop CPU. The shipped artifacts were produced on an Apple
M1 Max with the model trained on MPS (Section 2). Continuous integration runs
on ubuntu-latest, where training would use the CPU and so would not
reproduce the shipped `model.pt` (Section 3).

## 8. Artifact checksums

SHA-256 of `model.pt` and of every other artifact that
`scripts/regenerate_all_artifacts.py` writes, as shipped. The same values are
recorded in `outputs/metrics/regeneration_summary.json`, which is not listed
because it also records per-step durations, which change on every run.

| Artifact | SHA-256 |
|---|---|
| `outputs/model/model.pt` | `419aed386950f0d3a871680b10a5b089dd292c109c196bec9bccd5f3003b2a4b` |
| `outputs/model/features.json` | `c0f534ebe6cb6201ebdc2a1e5189524c8bb78436b77f90f9d43afdb2c35a59eb` |
| `outputs/model/temperature_scale.json` | `a0bf462471044adee47b8f66a38e5d545b1a10ec688c9761543d56e44dab07b9` |
| `outputs/metrics/val_preds.csv` | `1fbf18c5e66b27e3c75768fe85f457d1d32492fc813f0a9d3ff7e43b00627986` |
| `outputs/metrics/metrics.json` | `7884941b0d62e9df7dec35deeb926fb40a23e434d320b38100894024648f931b` |
| `outputs/metrics/feature_stats.json` | `ed4c8c3d6fc1bab69aa1eb31d2259a8dbef0dffdba9561481e8f8b85ad9fe703` |
| `outputs/metrics/feature_stats_train.json` | `ed4c8c3d6fc1bab69aa1eb31d2259a8dbef0dffdba9561481e8f8b85ad9fe703` |
| `outputs/metrics/energy_threshold.json` | `b7d856f0dcdb2dabe202d6bf5ff02d33b89ee3bb8885a7648ed8eb87ba74dd66` |
| `outputs/metrics/ood_energy.json` | `cff3bda4ae968a95c7e7e245e1bd2c4a37a8bf653cd263a9f2ffe5e9366dd0a2` |
| `outputs/metrics/conformal.json` | `76ae94eab684e23729d2900320c4dbdfb0ca6f5d12c19114d1f4bba4b247a7f2` |
| `outputs/metrics/conformal_grouped.json` | `1f0f0f6cf8afe7549d2d421b68c48efc8b39fd0407279b98ef6417646063a8d7` |
| `outputs/metrics/conformal_eval.json` | `2224eff53712f66a56a6acecf446a4723e8c3a03b6d334be3cfa90460fa86b7e` |
| `outputs/metrics/ood_gate.json` | `b96805eb1f05820f7e6d139e75246787fa73f44c5291055d91e3781b832330d7` |
| `outputs/metrics/ci.json` | `8617631375196f71fb975402085c0e2b6616e500af0541f29937e3d7a9102955` |
| `outputs/metrics/calibration_curve.png` | `fcc4fe0d46af0c28d2d3e75189ce070ab46c6d763c92024c2610bf559915b42a` |
| `outputs/metrics/dca_curve.png` | `c3d15537768348ccbd87977dbd570018bd05a7bcaa8899081d9b5da433b6adba` |
| `outputs/metrics/ablation_table.json` | `3cbee434fac81b9acdab18a33a7c8888913d9602e953238c5da546d2db967b81` |
| `outputs/metrics/ablation_table.csv` | `3257e5bf0dfec0555a75ce157c3412aa71d75f79460ce48bd4b57bcadebab9a5` |
| `outputs/metrics/coverage_sweep.json` | `47e120db4c41ff8c8e7a79a5733f9803b89ccd8d0456c011afddc039a29e81df` |
| `outputs/metrics/coverage_sweep.png` | `9af67cfb70e7fe57242839ba15f5acca7453385f14e4a9b7d67383835c89dd4d` |
| `outputs/metrics/abstain_pareto.json` | `68bc4cac792a219dfa4df227248f3d4df0fba736fd61c140ca6352a078c339dc` |
| `outputs/metrics/abstain_pareto.png` | `ade187ba83b73e02b3137e47ffe295811f38101a65d6df963135440426b3bd79` |
| `outputs/metrics/synthetic_ood_benchmark.json` | `c83177a9a0f4a8476493e7ad5ff6bc76200d21f2dafddb348013079be2ea271f` |

## Honesty signal

The synthetic-data results are fully and deterministically reproducible, but
reproducing them reproduces an infrastructure proof on a 6-row validation
split, not clinical performance. No performance metrics are reported, because
on six validation rows they would not be meaningful; the real-data study that
would produce clinically meaningful numbers is the planned MIMIC-IV proxy
study, not yet run. Reproducibility here means the pipeline is honest and
re-runnable, not that the numbers are clinically validated.

## References

See `docs/references.bib` and the model and data cards for the methods and
dataset detail. Dependency versions are pinned in `requirements.txt`; the
test, lint, and type configuration is in `pyproject.toml` and
`.github/workflows/ci.yml`.
