# scripts/calibration/bootstrap_metrics.py
from __future__ import annotations

import json
import os
from collections.abc import Callable

import numpy as np
import pandas as pd
from sklearn.metrics import recall_score, roc_auc_score

SRC = "outputs/metrics/val_preds.csv"
OUT = "outputs/metrics/ci.json"
N_BOOT = 2000


def boot_ci(
    stat_fn: Callable[[np.ndarray, np.ndarray], float],
    y: np.ndarray,
    p: np.ndarray,
    rng: np.random.Generator,
    defined: Callable[[np.ndarray], bool],
) -> dict[str, float | int | None]:
    """
    Percentile bootstrap over N_BOOT resamples of the rows. A resample for
    which the metric is undefined (``defined(yy)`` is False) is skipped and
    counted, not scored, so it cannot pull the interval toward a
    placeholder value such as recall = 0 when a resample has no High row.
    When every resample is skipped, lo, hi and mean are None.
    """
    stats = []
    skipped = 0
    n = len(y)
    for _ in range(N_BOOT):
        idx = rng.integers(0, n, size=n)
        yy, pp = y[idx], p[idx]
        if not defined(yy):
            skipped += 1
            continue
        stats.append(stat_fn(yy, pp))
    if not stats:
        # The metric is undefined in every resample (for example, no High
        # row at all): report the interval as undefined with the skip count.
        return {"lo": None, "hi": None, "mean": None, "n_resamples": N_BOOT, "n_skipped": skipped}
    arr = np.array(stats, dtype=float)
    return {
        "lo": float(np.percentile(arr, 2.5)),
        "hi": float(np.percentile(arr, 97.5)),
        "mean": float(np.mean(arr)),
        "n_resamples": N_BOOT,
        "n_skipped": skipped,
    }


def _has_both_classes(yy: np.ndarray) -> bool:
    return len(np.unique(yy)) == 2


def _has_high_row(yy: np.ndarray) -> bool:
    return bool((yy == 1).any())


def main() -> None:
    if not os.path.exists(SRC):
        raise FileNotFoundError(f"Missing {SRC}. Run python -m ml.training_calib_dca first.")

    df = pd.read_csv(SRC)
    y = df["y_true"].astype(int).to_numpy()
    p = df["p_high_cal"].astype(float).to_numpy()  # temperature-scaled probabilities
    rng = np.random.default_rng(42)

    # AUC needs both classes in a resample; recall needs at least one High row.
    auc_ci = boot_ci(lambda yy, pp: roc_auc_score(yy, pp), y, p, rng, _has_both_classes)
    rec_ci = boot_ci(
        lambda yy, pp: recall_score(yy, (pp >= 0.5).astype(int), pos_label=1),
        y, p, rng, _has_high_row,
    )

    os.makedirs("outputs/metrics", exist_ok=True)
    with open(OUT, "w") as f:
        json.dump({
            "auc_calibrated_CI95": auc_ci,
            "recall_high@0.5_CI95": rec_ci,
        }, f, indent=2)

    print(f"Saved {OUT}")


if __name__ == "__main__":
    main()
