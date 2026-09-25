#!/usr/bin/env bash
# Amoebanator V1.0 - end-to-end pipeline runner.
#
# Runs scripts/regenerate_all_artifacts.py, which holds the single list of
# pipeline steps and checks that every expected artefact lands on disk.
#
# Usage:
#   PYTHONPATH=. bash scripts/run_full_pipeline.sh
#
# Exit code 0 means every step succeeded and every artefact was produced.

set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$REPO_ROOT"

export PYTHONPATH="${PYTHONPATH:-$REPO_ROOT}"

exec python scripts/regenerate_all_artifacts.py "$@"
