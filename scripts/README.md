# scripts/

Utility and pipeline scripts for the model, organized into functional
subpackages. Run everything from the repository root with `PYTHONPATH=.` set.
Each subdirectory is a Python package, so modules are imported as
`from scripts.<group>.<module> import ...`.

## Subpackages

- **`conformal/`** - Split-conformal prediction: fitting the threshold (global,
  age-grouped, and from precomputed probabilities), set statistics on the
  validation rows, the coverage sweep, and the abstention/accuracy trade-off.
- **`ood/`** - Out-of-distribution detection: fitting the Mahalanobis and
  energy gates, and a synthetic OOD benchmark.
- **`calibration/`** - Bootstrap confidence intervals and the calibration and
  decision-curve plots.
- **`inference/`** - Command-line inference entry point.
- **`vignettes/`** - Clinical vignette and test-fixture generation.
- **`experiments/`** - The four-cell ablation.

## Top-level scripts

- **`regenerate_all_artifacts.py`** - Retrains the model and regenerates every
  threshold, metrics file and figure the pipeline ships
  (`PYTHONPATH=. python scripts/regenerate_all_artifacts.py`); `--dry-run`
  only checks that the artifacts exist.
- **`check_dua.py`** - Data guard run in continuous integration.
