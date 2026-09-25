# ml/robust.py  - Tabular out-of-distribution detection utilities
from __future__ import annotations
import json
from pathlib import Path
import numpy as np
import pandas as pd

# Numeric features we try to use if present
NUMERIC_COLS = [
    "age", "csf_glucose", "csf_protein", "csf_wbc",
    "pcr", "microscopy", "exposure", "risk_score",
]

METRICS_DIR = Path("outputs/metrics")
STATS_JSON = METRICS_DIR / "feature_stats.json"
ENERGY_JSON = METRICS_DIR / "energy_threshold.json"

def _robust_z(x: np.ndarray, median: np.ndarray, mad: np.ndarray) -> np.ndarray:
    z = (x - median) / mad
    z = np.where(np.isfinite(z), z, 0.0)
    return z

def mahalanobis_d2(z: np.ndarray, mu: np.ndarray, S: np.ndarray, use_diagonal: bool = True) -> tuple[float, object]:
    d = z - mu
    if use_diagonal:
        invd = 1.0 / (np.diag(S) + 1e-12)
        contrib = d * d * invd
        return float(contrib.sum()), contrib
    inv = np.linalg.inv(S + 1e-6 * np.eye(S.shape[0]))
    return float(d @ inv @ d), None

def fit_gate_stats(
    X: np.ndarray,
    cols: list[str],
    quantile: float = 0.999,
    use_diagonal: bool = True,
) -> dict:
    """
    Fit the Mahalanobis gate on the rows of X, whose columns are named by cols:
    robust z-scores (median and MAD), their mean and covariance (diagonal by
    default), and tau, the given quantile of the fitted rows' own distances.
    """
    X = np.where(np.isfinite(X), X, np.nan)

    col_median = np.nanmedian(X, axis=0)
    col_mad = np.nanmedian(np.abs(X - col_median), axis=0)
    col_mad = np.where(col_mad > 0, col_mad, 1.0)

    X_filled = np.where(np.isnan(X), col_median, X)
    Z = _robust_z(X_filled, col_median, col_mad)

    mu = Z.mean(axis=0)
    S: np.ndarray = np.cov(Z, rowvar=False)
    if use_diagonal:
        S = np.diag(np.clip(np.diag(S), 1e-6, None))

    d2 = []
    for i in range(Z.shape[0]):
        val, _ = mahalanobis_d2(Z[i], mu, S, use_diagonal)
        d2.append(val)
    tau = float(np.quantile(d2, quantile))

    return {
        "cols": cols,
        "median": col_median.tolist(),
        "mad": col_mad.tolist(),
        "mu": mu.tolist(),
        "S": S.tolist(),
        "use_diagonal": bool(use_diagonal),
        "tau": tau,
        "quantile": float(quantile),
    }

def score_energy(logits: np.ndarray) -> float:
    # Energy = -logsumexp(logits)
    return -float(np.logaddexp.reduce(logits))

def load_stats(path: Path = STATS_JSON) -> dict:
    # Minimal loader used by ml.infer
    p = Path(path)
    if p.exists():
        return json.loads(p.read_text())
    return {
        "cols": [],
        "median": [],
        "mad": [],
        "mu": [],
        "S": [],
        "use_diagonal": True,
        "tau": float("inf"),
    }

def score_tabular(row: pd.Series, stats: dict) -> dict:
    """
    Returns dict: {d2, tau, contrib, use_diagonal}
    Tolerant to missing columns (intersects what the row has).
    """
    all_cols = stats.get("cols", [])
    if not all_cols:
        return {"d2": float("inf"), "tau": float("inf"), "in_dist": False, "contrib": None, "use_diagonal": True}

    present = [c for c in all_cols if c in row.index]
    if not present:
        return {"d2": float("inf"), "tau": float("inf"), "in_dist": False, "contrib": None, "use_diagonal": True}

    idx = [all_cols.index(c) for c in present]

    med = np.array(stats["median"], dtype=float)[idx]
    mad = np.array(stats["mad"], dtype=float)[idx]
    mu  = np.array(stats["mu"], dtype=float)[idx]
    S   = np.array(stats["S"], dtype=float)
    S   = S[np.ix_(idx, idx)]

    x: np.ndarray = row[present].to_numpy(dtype=float)
    x = np.where(np.isfinite(x), x, np.nan)
    z = _robust_z(np.where(np.isnan(x), med, x), med, mad)

    d2, contrib = mahalanobis_d2(z, mu, S, bool(stats.get("use_diagonal", True)))
    tau = float(stats.get("tau", float("inf")))
    return {
        "d2": float(d2),
        "tau": tau,
        "in_dist": bool(d2 <= tau),
        "contrib": (contrib.tolist() if contrib is not None else None),  # type: ignore[attr-defined]
        "use_diagonal": bool(stats.get("use_diagonal", True)),
    }

def check_ood_row(row: pd.Series, stats: dict) -> dict:
    out = score_tabular(row, stats)
    return {"d2": out["d2"], "contrib": out["contrib"]}
