"""
Standardization of the model's continuous inputs.

The continuous inputs (age and the three CSF values) are z-scored with the
means and standard deviations of the training split; the binary inputs (PCR,
microscopy, exposure and the symptom indicators) stay 0/1. Without this step
CSF WBC, which runs into the thousands, would dominate the first layer.

The trainer fits the scaler on the training rows only and writes it to
outputs/model/scaler.json next to model.pt. Inference and every script that
runs the saved model load that file and apply exactly the stored values.
"""
from __future__ import annotations

import json
import math
from pathlib import Path
from typing import Any

import numpy as np

CONTINUOUS_FEATURES: tuple[str, ...] = ("age", "csf_glucose", "csf_protein", "csf_wbc")
SCALER_FILENAME = "scaler.json"


def fit_scaler(X_train: np.ndarray, feats: list[str] | tuple[str, ...]) -> dict[str, Any]:
    """
    Means and population standard deviations (ddof=0) of the continuous
    columns of X_train. A column with zero spread keeps a standard deviation
    of 1, so it is only centered.
    """
    names = [f for f in CONTINUOUS_FEATURES if f in feats]
    if not names:
        raise ValueError(f"none of {CONTINUOUS_FEATURES} are in the feature list {list(feats)}")
    idx = [list(feats).index(f) for f in names]
    cols = np.asarray(X_train, dtype=float)[:, idx]
    mean = cols.mean(axis=0)
    std = cols.std(axis=0)
    std = np.where(std > 0, std, 1.0)
    return {
        "features": names,
        "mean": [float(v) for v in mean],
        "std": [float(v) for v in std],
        "n_fit": int(cols.shape[0]),
    }


def validate_scaler(scaler: dict[str, Any], feats: list[str] | tuple[str, ...]) -> None:
    """Raise ValueError unless the scaler is well formed and matches feats."""
    names = scaler.get("features")
    mean = scaler.get("mean")
    std = scaler.get("std")
    if not isinstance(names, list) or not isinstance(mean, list) or not isinstance(std, list):
        raise ValueError("scaler must hold 'features', 'mean' and 'std' lists")
    if not (len(names) == len(mean) == len(std)) or not names:
        raise ValueError("scaler 'features', 'mean' and 'std' must be non-empty and the same length")
    missing = [n for n in names if n not in feats]
    if missing:
        raise ValueError(f"scaler features {missing} are not in the model's feature list")
    for m, s in zip(mean, std):
        if not (isinstance(m, (int, float)) and math.isfinite(m)):
            raise ValueError(f"scaler mean must be finite; got {m!r}")
        if not (isinstance(s, (int, float)) and math.isfinite(s) and s > 0):
            raise ValueError(f"scaler std must be finite and positive; got {s!r}")


def apply_scaler(
    X: np.ndarray, feats: list[str] | tuple[str, ...], scaler: dict[str, Any]
) -> np.ndarray:
    """Return a float32 copy of X (2-D, or 1-D for one row) with the continuous columns z-scored."""
    validate_scaler(scaler, feats)
    out = np.array(X, dtype=np.float32, copy=True)
    for name, m, s in zip(scaler["features"], scaler["mean"], scaler["std"]):
        j = list(feats).index(name)
        if out.ndim == 1:
            out[j] = (out[j] - m) / s
        else:
            out[:, j] = (out[:, j] - m) / s
    return out


def save_scaler(scaler: dict[str, Any], model_dir: str | Path) -> Path:
    path = Path(model_dir) / SCALER_FILENAME
    path.write_text(json.dumps(scaler, indent=2))
    return path


def load_scaler(path: str | Path, feats: list[str] | tuple[str, ...]) -> dict[str, Any]:
    """Load and validate a scaler saved by save_scaler."""
    scaler = json.loads(Path(path).read_text())
    if not isinstance(scaler, dict):
        raise ValueError(f"{path} must hold a JSON object")
    validate_scaler(scaler, feats)
    return scaler
