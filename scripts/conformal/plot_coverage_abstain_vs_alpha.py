#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from ml.conformal_advanced import compute_qhat, nonconformity_from_p

METRICS_DIR = Path("outputs/metrics")
VAL_PREDS = METRICS_DIR / "val_preds.csv"
OUT_PNG = METRICS_DIR / "coverage_abstain_vs_alpha.png"


def coverage_abstain_at_alpha(
    y: np.ndarray, p: np.ndarray, alpha: float
) -> tuple[float, float]:
    n = len(y)
    qhat = compute_qhat(nonconformity_from_p(p, y), alpha=alpha)
    include_high = p >= (1.0 - qhat)
    include_low = p <= qhat
    abstained = include_high == include_low
    true_is_high = (y == 1)
    contained = (true_is_high & include_high) | (~true_is_high & include_low)
    coverage = contained.mean() if n else np.nan
    abstain = abstained.mean() if n else np.nan
    return coverage, abstain

def main() -> None:
    if not VAL_PREDS.exists():
        raise SystemExit("Missing outputs/metrics/val_preds.csv")
    df = pd.read_csv(VAL_PREDS)
    y = df["y_true"].astype(int).to_numpy()
    p = df["p_high_cal"].astype(float).to_numpy()

    alphas = np.arange(0.01, 0.201, 0.01)
    covs, absts = [], []
    for a in alphas:
        c, ab = coverage_abstain_at_alpha(y, p, float(a))
        covs.append(c)
        absts.append(ab)

    plt.figure(figsize=(6,4))
    plt.plot(alphas, covs, label="coverage (target = 1-alpha)")
    plt.plot(alphas, absts, label="abstain rate")
    plt.xlabel("alpha (alpha)")
    plt.ylabel("fraction")
    plt.title("Conformal coverage and abstain vs alpha")
    plt.grid(True, alpha=0.3)
    plt.legend()
    METRICS_DIR.mkdir(parents=True, exist_ok=True)
    plt.tight_layout()
    plt.savefig(OUT_PNG, dpi=160)
    print(f"Wrote {OUT_PNG}")

if __name__ == "__main__":
    main()
