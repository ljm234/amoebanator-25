"""Tests for ml.seeds."""
from __future__ import annotations

import os
import random
from pathlib import Path
from unittest.mock import patch

import numpy as np
import pytest
import torch

from ml.seeds import DEFAULT_SEED, SEED_ENV, SeedReport, set_global_seeds


def test_default_seed_is_42() -> None:
    assert DEFAULT_SEED == 42


def test_set_global_seeds_returns_report() -> None:
    report = set_global_seeds(7)
    assert isinstance(report, SeedReport)
    assert report.seed == 7
    assert report.python_random is True
    assert report.numpy is True
    assert report.torch_cpu is True


def test_two_seeds_produce_same_random_sequence() -> None:
    set_global_seeds(42)
    a_py = [random.random() for _ in range(5)]
    a_np = np.random.rand(5)
    a_torch = torch.rand(5).tolist()
    set_global_seeds(42)
    b_py = [random.random() for _ in range(5)]
    b_np = np.random.rand(5)
    b_torch = torch.rand(5).tolist()
    assert a_py == b_py
    np.testing.assert_array_equal(a_np, b_np)
    assert a_torch == b_torch


def test_different_seeds_produce_different_sequences() -> None:
    set_global_seeds(1)
    a = torch.rand(20)
    set_global_seeds(2)
    b = torch.rand(20)
    assert not torch.equal(a, b)


def test_env_var_overrides_default() -> None:
    with patch.dict(os.environ, {SEED_ENV: "99"}):
        report = set_global_seeds()
    assert report.seed == 99


def test_explicit_seed_beats_env_var() -> None:
    with patch.dict(os.environ, {SEED_ENV: "99"}):
        report = set_global_seeds(7)
    assert report.seed == 7


def test_invalid_env_var_raises() -> None:
    with patch.dict(os.environ, {SEED_ENV: "not-an-int"}), pytest.raises(ValueError, match="integer"):
        set_global_seeds()


def test_training_is_deterministic_under_pinned_seed(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    """Two runs of the pipeline's trainer write bit-identical model.pt files."""
    from ml.training_calib_dca import main as train

    # Write to temporary paths so the test never replaces the shipped model
    # or appends to the repository's audit log.
    monkeypatch.setenv("AMOEBANATOR_AUDIT_PATH", str(tmp_path / "audit.jsonl"))
    out_a = train(model_dir=str(tmp_path / "a"), metrics_dir=str(tmp_path / "a_metrics"))
    out_b = train(model_dir=str(tmp_path / "b"), metrics_dir=str(tmp_path / "b_metrics"))
    assert (tmp_path / "a" / "model.pt").read_bytes() == (tmp_path / "b" / "model.pt").read_bytes()
    assert out_a["T"] == out_b["T"]
