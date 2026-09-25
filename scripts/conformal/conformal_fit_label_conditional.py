# scripts/conformal/conformal_fit_label_conditional.py
from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np
import pandas as pd

from ml.config import conformal_alpha, parse_alpha
from ml.conformal_advanced import compute_qhat, qhat_to_json

METRICS_DIR = Path("outputs/metrics")
VAL_PREDS = METRICS_DIR / "val_preds.csv"
OUT = METRICS_DIR / "conformal_label_conditional.json"


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--alpha", type=parse_alpha, default=None)
    args = ap.parse_args()
    alpha = args.alpha if args.alpha is not None else conformal_alpha()

    df = pd.read_csv(VAL_PREDS)
    y = df["y_true"].astype(int).to_numpy()
    p = df["p_high_cal"].astype(float).to_numpy()

    # class-conditional nonconformity scores
    s_pos = 1.0 - p[y == 1]   # want high p on positives
    s_neg = p[y == 0]         # want low p on negatives

    def qhat_of(scores: np.ndarray) -> float:
        if len(scores) == 0:
            return float("nan")
        return compute_qhat(scores, alpha=alpha)

    q_pos = qhat_of(s_pos)
    q_neg = qhat_of(s_neg)

    out = {
        "alpha": float(alpha),
        "qhat_pos": qhat_to_json(q_pos),   # threshold for including "High"
        "qhat_neg": qhat_to_json(q_neg),   # threshold for including "Low"
        "n_pos": int((y==1).sum()),
        "n_neg": int((y==0).sum()),
        "source": "val_preds.csv",
        "method": "label-conditional split conformal"
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    with open(OUT, "w") as f:
        json.dump(out, f, indent=2)
    print(json.dumps(out, indent=2))

if __name__ == "__main__":
    main()
