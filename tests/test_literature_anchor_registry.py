"""Every literature anchor in the vignette corpus must match PMID_REGISTRY.

For each literature_anchors entry of every vignette JSON under data/vignettes/,
the PMID must be a PMID_REGISTRY key, and a non-null DOI must equal the
registry DOI for that PMID (compared case-insensitively, since DOIs are
case-insensitive). A null DOI is allowed: some anchors do not carry the DOI
the registry records.

The test runs offline; it compares the committed data with the registry only.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import pytest

_REPO_ROOT = Path(__file__).resolve().parent.parent
if str(_REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(_REPO_ROOT))

from scripts.vignettes.generate_pam_vignettes import PMID_REGISTRY  # noqa: E402

_VIGNETTE_ROOT = _REPO_ROOT / "data" / "vignettes"


def _vignette_paths() -> list[Path]:
    paths = []
    for path in sorted(_VIGNETTE_ROOT.rglob("*.json")):
        data = json.loads(path.read_text(encoding="utf-8"))
        if isinstance(data, dict) and "literature_anchors" in data:
            paths.append(path)
    return paths


VIGNETTE_PATHS = _vignette_paths()


def test_corpus_has_vignettes_with_anchors() -> None:
    assert len(VIGNETTE_PATHS) >= 138, len(VIGNETTE_PATHS)


@pytest.mark.parametrize(
    "path", VIGNETTE_PATHS, ids=[p.name for p in VIGNETTE_PATHS]
)
def test_anchor_pmid_and_doi_match_registry(path: Path) -> None:
    data = json.loads(path.read_text(encoding="utf-8"))
    anchors = data["literature_anchors"]
    assert anchors, f"{path.name}: no literature anchors"
    for anchor in anchors:
        pmid = anchor["pmid"]
        assert pmid in PMID_REGISTRY, f"{path.name}: PMID {pmid} is not in PMID_REGISTRY"
        doi = anchor["doi"]
        if doi is None:
            continue
        registry_doi = PMID_REGISTRY[pmid]["doi"]
        assert registry_doi is not None and doi.lower() == registry_doi.lower(), (
            f"{path.name}: PMID {pmid} DOI {doi!r} does not match the registry DOI "
            f"{registry_doi!r}"
        )
