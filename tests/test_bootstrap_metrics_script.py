"""
scripts/calibration/bootstrap_metrics.py must skip, and count, resamples for
which a metric is undefined, instead of scoring them as 0. A resample with no
High row has no defined recall; scoring it 0 would widen the interval.
"""
from __future__ import annotations

import numpy as np
import pytest
from sklearn.metrics import recall_score

import scripts.calibration.bootstrap_metrics as bm


def _recall(yy: np.ndarray, pp: np.ndarray) -> float:
    return float(recall_score(yy, (pp >= 0.5).astype(int), pos_label=1))


def test_resamples_without_a_high_row_are_skipped_and_counted() -> None:
    # Every row classified correctly: wherever recall is defined it is 1.0.
    y = np.array([0, 1, 0, 0, 1, 0])
    p = np.array([0.1, 0.9, 0.2, 0.1, 0.8, 0.3])
    out = bm.boot_ci(_recall, y, p, np.random.default_rng(0), bm._has_high_row)
    assert out["n_resamples"] == bm.N_BOOT
    assert 0 < out["n_skipped"] < bm.N_BOOT
    assert out["lo"] == pytest.approx(1.0)
    assert out["mean"] == pytest.approx(1.0)


def test_skip_count_matches_resamples_with_no_high_row() -> None:
    y = np.array([0, 1, 0, 0, 1, 0])
    p = np.full(6, 0.5)
    rng_a, rng_b = np.random.default_rng(7), np.random.default_rng(7)
    out = bm.boot_ci(_recall, y, p, rng_a, bm._has_high_row)
    expected = sum(
        not (y[rng_b.integers(0, len(y), size=len(y))] == 1).any() for _ in range(bm.N_BOOT)
    )
    assert out["n_skipped"] == expected


def test_auc_needs_both_classes() -> None:
    assert bm._has_both_classes(np.array([0, 1]))
    assert not bm._has_both_classes(np.array([1, 1]))
    assert not bm._has_high_row(np.array([0, 0]))


def test_interval_is_undefined_when_every_resample_is_skipped() -> None:
    y = np.zeros(6, dtype=int)  # no High row anywhere
    out = bm.boot_ci(_recall, y, np.zeros(6), np.random.default_rng(0), bm._has_high_row)
    assert out == {"lo": None, "hi": None, "mean": None, "n_resamples": bm.N_BOOT, "n_skipped": bm.N_BOOT}
