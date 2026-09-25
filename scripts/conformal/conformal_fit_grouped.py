# scripts/conformal/conformal_fit_grouped.py
from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path

import numpy as np
import pandas as pd

from ml.config import conformal_alpha
from ml.conformal_advanced import compute_qhat, nonconformity_from_p, qhat_to_json

VAL = Path("outputs/metrics/val_preds.csv")
OUT = Path("outputs/metrics/conformal_grouped.json")

def qhat_from_probs(y_true: np.ndarray, p_high: np.ndarray, alpha: float | Fraction) -> float:
    return compute_qhat(nonconformity_from_p(p_high, y_true), alpha=alpha)

def main() -> None:
    if not VAL.exists():
        print("missing val_preds.csv")
        return
    df = pd.read_csv(VAL)
    if not {"y_true","p_high_cal"}.issubset(df.columns):
        print("missing columns")
        return
    alpha = conformal_alpha()
    if "age" not in df.columns:
        OUT.parent.mkdir(parents=True, exist_ok=True)
        OUT.write_text(json.dumps({"alpha": float(alpha), "groups": {}}, indent=2))
        print("no age in val_preds; saved empty groups")
        return
    child = df[df["age"] < 18]
    adult = df[df["age"] >= 18]
    groups = {}
    for name, part in [("child", child), ("adult", adult)]:
        if len(part) >= 1:
            qh = qhat_from_probs(part["y_true"].to_numpy(int), part["p_high_cal"].to_numpy(float), alpha)
            groups[name] = {"n": int(len(part)), "qhat": qhat_to_json(qh)}
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps({"alpha": float(alpha), "groups": groups}, indent=2))
    print("saved conformal_grouped.json")

if __name__ == "__main__":
    main()
