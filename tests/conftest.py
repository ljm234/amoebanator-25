"""Setup shared by the whole test suite."""
from __future__ import annotations

from collections.abc import Iterator
from pathlib import Path

import pytest

from ml.audit_hooks import AUDIT_PATH_ENV, reset_audit_log


@pytest.fixture(autouse=True)
def _isolated_audit_log(
    tmp_path_factory: pytest.TempPathFactory, monkeypatch: pytest.MonkeyPatch
) -> Iterator[Path]:
    """Point the audit log at a fresh temporary file for every test.

    Without this, a test that runs the app or the trainer without setting
    AMOEBANATOR_AUDIT_PATH appends to outputs/audit/audit.jsonl in the
    repository, and the cached log carries over from one test to the next.
    """
    path = tmp_path_factory.mktemp("audit") / "audit.jsonl"
    monkeypatch.setenv(AUDIT_PATH_ENV, str(path))
    reset_audit_log()
    yield path
    reset_audit_log()
