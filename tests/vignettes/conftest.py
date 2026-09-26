"""Pytest config for the PAM vignette generator tests.

Registers the ``pam_vignettes`` marker, ensures the project root is on
``sys.path`` so ``scripts.vignettes.generate_pam_vignettes`` is importable, and
exposes session-scoped fixtures for the 20 generated vignettes so the
generator runs once instead of once per test.
"""
from __future__ import annotations

import sys
from pathlib import Path
from typing import Any

import pytest

_REPO_ROOT = Path(__file__).resolve().parents[2]
if str(_REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(_REPO_ROOT))

from scripts.vignettes.generate_pam_vignettes import (  # noqa: E402
    PAM_DISTRIBUTION_1_20,
    PAM_DISTRIBUTION_21_60,
    PMID_REGISTRY,
    generate_vignette,
    load_pmid_metadata,
)


def pytest_configure(config: pytest.Config) -> None:
    config.addinivalue_line(
        "markers",
        "pam_vignettes: tests for the PAM vignette generator and vignette distributions",
    )


@pytest.fixture(scope="session")
def distribution() -> list[dict[str, Any]]:
    return PAM_DISTRIBUTION_1_20


@pytest.fixture(scope="session")
def distribution_21_60() -> list[dict[str, Any]]:
    return PAM_DISTRIBUTION_21_60


@pytest.fixture(scope="session")
def pmid_registry() -> dict[str, dict[str, Any]]:
    return PMID_REGISTRY


@pytest.fixture(scope="session")
def generated_vignettes() -> list[dict[str, Any]]:
    """Generate all 20 vignettes once per session."""
    out: list[dict[str, Any]] = []
    for spec in PAM_DISTRIBUTION_1_20:
        pmid_meta = load_pmid_metadata(spec["pmid"])
        out.append(generate_vignette(spec, pmid_meta))
    return out
