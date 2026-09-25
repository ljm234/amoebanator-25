"""
docs/REPRODUCIBILITY.md lists the SHA-256 of every artifact that
scripts/regenerate_all_artifacts.py writes. The list must name exactly those
artifacts and match the files in the repository, so the doc cannot drift from
what ships.
"""
from __future__ import annotations

import hashlib
import re

from scripts.regenerate_all_artifacts import PIPELINE, REPO_ROOT

DOC = REPO_ROOT / "docs" / "REPRODUCIBILITY.md"
_ROW = re.compile(r"^\| `([^`]+)` \| `([0-9a-f]{64})` \|$", re.MULTILINE)


def test_checksum_table_matches_the_shipped_artifacts() -> None:
    table = dict(_ROW.findall(DOC.read_text(encoding="utf-8")))
    expected = [artifact for _, _, artifacts in PIPELINE for artifact in artifacts]
    assert sorted(table) == sorted(expected)
    for path, digest in table.items():
        assert hashlib.sha256((REPO_ROOT / path).read_bytes()).hexdigest() == digest, path
