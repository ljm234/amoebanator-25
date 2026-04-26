"""
ml/data/_wip/ — work-in-progress data pipeline scaffolds.

Intentionally NOT exposed at the ml.data package level. These modules were
moved here in Phase 7.4 of the V1.0 sprint because they are scaffolding
without unit-test coverage and not currently wired into any production code
path. Importing them by their previous names (e.g. `from ml.data.synthetic
import GenerationPipeline`) is a deliberate breaking change so reviewers
cannot accidentally believe these modules ship.

To use one explicitly during research:
    from ml.data._wip import synthetic
    pipeline = synthetic.GenerationPipeline(...)

See _wip/README.md for the per-module status and roadmap target version.
"""
