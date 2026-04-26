"""
Phase 1.4 — tests for the energy gate fit script.

Covers:
  * fit_logit_energy: math is correct, n recorded, q recorded
  * fit_neg_energy_from_p: monotone in entropy, n recorded
  * _neg_energy_from_p: clamps to (0, 1), matches closed-form for known p
  * end-to-end: running scripts.fit_gates.main writes both JSON files with
    finite tau values when given a val_preds.csv that has logit columns
  * fallback: when val_preds.csv lacks logit columns, the script recomputes
    from model.pt (verified by patching _recompute_val_logits)
"""
from __future__ import annotations

import json
import math
from pathlib import Path
from unittest.mock import patch

import numpy as np
import pandas as pd
import pytest

from scripts.fit_gates import (
    _neg_energy_from_p,
    fit_logit_energy,
    fit_neg_energy_from_p,
)
import scripts.fit_gates as fg


def test_neg_energy_from_p_closed_form() -> None:
    # neg_energy_from_p(0.5) = -log(1 + exp(0)) = -log(2)
    assert _neg_energy_from_p(0.5) == pytest.approx(-math.log(2.0), rel=1e-9)


def test_neg_energy_from_p_clamps_extremes() -> None:
    # Must not raise on 0 or 1
    assert math.isfinite(_neg_energy_from_p(0.0))
    assert math.isfinite(_neg_energy_from_p(1.0))


def test_neg_energy_is_monotone_decreasing_in_p() -> None:
    """neg_energy(p) = -log(1 + exp(logit(p))) is strictly monotone-decreasing."""
    ps = np.linspace(0.01, 0.99, 25)
    vals = [_neg_energy_from_p(float(p)) for p in ps]
    for i in range(len(vals) - 1):
        assert vals[i] > vals[i + 1], (
            f"non-monotone at p={ps[i]:.3f}→{ps[i+1]:.3f}: {vals[i]} ≤ {vals[i+1]}"
        )


def test_fit_logit_energy_records_quantile_and_n() -> None:
    logits = np.array([[1.0, 2.0], [-1.0, 3.0], [0.0, 0.0], [10.0, 5.0]], dtype=float)
    out = fit_logit_energy(logits, q=0.95)
    assert out["q"] == 0.95
    assert out["n"] == 4
    # Tau should equal numpy's 95th percentile of -logsumexp(logits)
    expected = np.quantile([-float(np.logaddexp.reduce(r)) for r in logits], 0.95)
    assert out["tau"] == pytest.approx(float(expected), rel=1e-9)


def test_fit_neg_energy_from_p_records_quantile_and_n() -> None:
    p = np.array([0.01, 0.1, 0.5, 0.9, 0.99], dtype=float)
    out = fit_neg_energy_from_p(p, q=0.95)
    assert out["q"] == 0.95
    assert out["n"] == 5
    assert out["method"] == "energy_neg"
    assert math.isfinite(float(out["tau"]))


def test_main_writes_both_gate_files(tmp_path: Path) -> None:
    """End-to-end: feed a val_preds.csv with logit columns, expect both JSONs."""
    metrics = tmp_path / "metrics"
    metrics.mkdir()
    df = pd.DataFrame({
        "y_true": [1, 0, 1, 0, 1, 0],
        "p_high_uncal": [0.7, 0.2, 0.8, 0.3, 0.6, 0.4],
        "p_high_cal":   [0.9, 0.1, 0.95, 0.2, 0.7, 0.3],
        "logit_low":    [-1.0, 0.5, -2.0, 0.8, -0.5, 0.3],
        "logit_high":   [2.0, -1.0, 3.0, -1.5, 1.2, -0.8],
    })
    df.to_csv(metrics / "val_preds.csv", index=False)

    with (
        patch.object(fg, "METRICS_DIR", metrics),
        patch.object(fg, "VAL_PREDS", metrics / "val_preds.csv"),
    ):
        rc = fg.main([])

    assert rc == 0
    et = json.loads((metrics / "energy_threshold.json").read_text())
    oe = json.loads((metrics / "ood_energy.json").read_text())
    assert math.isfinite(float(et["tau"]))
    assert math.isfinite(float(oe["tau"]))
    assert et["n"] == 6 and oe["n"] == 6


def test_main_recomputes_logits_when_columns_missing(tmp_path: Path, capsys: pytest.CaptureFixture[str]) -> None:
    """If val_preds.csv has no logit columns, the script must invoke the recomputation fallback."""
    metrics = tmp_path / "metrics"
    metrics.mkdir()
    df = pd.DataFrame({
        "y_true": [1, 0, 1],
        "p_high_uncal": [0.7, 0.2, 0.8],
        "p_high_cal":   [0.9, 0.1, 0.95],
    })
    df.to_csv(metrics / "val_preds.csv", index=False)

    fake_logits = np.array([[1.0, 2.0], [-1.0, 0.5], [0.3, 0.7]], dtype=float)
    with (
        patch.object(fg, "METRICS_DIR", metrics),
        patch.object(fg, "VAL_PREDS", metrics / "val_preds.csv"),
        patch.object(fg, "_recompute_val_logits", return_value=fake_logits) as recomp,
    ):
        rc = fg.main([])

    assert rc == 0
    recomp.assert_called_once()
    captured = capsys.readouterr().out
    assert "recomputed" in captured


def test_main_rejects_bad_quantile(tmp_path: Path) -> None:
    metrics = tmp_path / "metrics"
    metrics.mkdir()
    pd.DataFrame({
        "y_true": [1, 0],
        "p_high_cal": [0.9, 0.1],
        "logit_low": [-1.0, 0.5],
        "logit_high": [2.0, -1.0],
    }).to_csv(metrics / "val_preds.csv", index=False)
    with (
        patch.object(fg, "METRICS_DIR", metrics),
        patch.object(fg, "VAL_PREDS", metrics / "val_preds.csv"),
        pytest.raises(SystemExit),
    ):
        fg.main(["--quantile", "1.5"])
