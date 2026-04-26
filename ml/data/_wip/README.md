# ml/data/_wip/

**Status:** Work-in-progress data-pipeline scaffolds, NOT shipping in V1.0.

The ten modules in this directory were moved out of `ml/data/` in Phase 7.4
of the V1.0 sprint (April 2026) because they share three properties:

1. They have **zero unit-test coverage** in `tests/`.
2. They are **not imported** by any production code path (training,
   inference, dashboard, fit scripts, or the ml/data wired modules).
3. They contain **placeholder logic** in their core functions — for
   example, `who_database.py` returns `np.random` data with a
   `# Simulated API call` comment instead of issuing a real WHO GHO
   request; `synthetic.py` returns prompt strings without invoking any
   image-generation backend.

Until each module has (a) a real backend integration, (b) unit tests
covering the public API, and (c) at least one integration call from a
production script, it should not be re-imported at the `ml.data` package
level.

## Roadmap target

| Module                  | LOC   | Backend that needs to land first                    | Earliest target |
|-------------------------|-------|-----------------------------------------------------|-----------------|
| `who_database.py`       | 2097  | WHO Global Health Observatory API integration       | V2.0            |
| `synthetic.py`          | 2324  | Diffusion-model backend (Stable Diffusion XL or alt)| V2.0            |
| `literature.py`         | 2427  | NCBI Entrez (PubMed) API + figure OCR pipeline      | V1.2            |
| `pathology_atlas.py`    | 2722  | Licensed atlas API + tile cache                     | V2.0            |
| `labeling.py`           | 2944  | Label Studio backend + annotator registry           | V2.0            |
| `dvc_versioning.py`     | 2058  | DVC + remote storage (S3 / GCS) configured          | V1.1            |
| `versioning.py`         |  ?    | Snapshot store + lineage graph backend              | V1.2            |
| `quality_assurance.py`  | 1500+ | QC rule engine + alerting integration               | V1.2            |
| `negative_collection.py`| 2500+ | Hard-negative mining pipeline + similarity search   | V2.0            |
| `annotation_protocol.py`| 2944  | Expert registry + calibration tracking              | V2.0            |

## Roadmap unblock checklist (per module)

A module is ready to graduate out of `_wip/` when:

- [ ] Backend integration (real API / library) replaces every `# Simulated`,
      `np.random`, or stub return.
- [ ] At least one production script imports a function from the module.
- [ ] `tests/test_<module>.py` exists and exercises the public API at
      ≥ 70% line coverage.
- [ ] `mypy --strict` passes on the module.
- [ ] The module's symbols are added back to `ml/data/__init__.py` `__all__`.
- [ ] An entry in the V1.x → V2.0 changelog documents the move.

## Why move rather than delete

These modules are real research artefacts — they encode a design surface for
the data pipeline that the project will need eventually. Deleting them would
lose that design work. Keeping them under `_wip/` makes them grep-able for
future contributors while preventing accidental import from production code.
