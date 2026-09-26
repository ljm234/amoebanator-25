"""
Fit a split-conformal qhat from the temperature-scaled probabilities
(p_high_cal) in val_preds.csv.

The conformal math is `ml.conformal_advanced.compute_qhat` and
`nonconformity_from_p`, so running this script on a small calibration set
emits the `SmallCalibrationWarning` to stderr, as the module does.

The default alpha comes from [conformal] alpha in config/amoebanator.toml.

Usage:
  PYTHONPATH=. python scripts/conformal/conformal_fit_from_probs.py
  PYTHONPATH=. python scripts/conformal/conformal_fit_from_probs.py --alpha 1/5
  PYTHONPATH=. python scripts/conformal/conformal_fit_from_probs.py --out /tmp/c.json
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

import pandas as pd

from ml.config import conformal_alpha, parse_alpha
from ml.conformal_advanced import compute_qhat, nonconformity_from_p, qhat_to_json

MET = Path("outputs/metrics")
DEFAULT_OUT = MET / "conformal.json"


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--alpha", type=parse_alpha, default=None,
                    help="miscoverage level, e.g. 1/7 or 0.2 (default: config)")
    ap.add_argument("--val_preds", type=str, default=str(MET / "val_preds.csv"))
    ap.add_argument("--out", type=Path, default=DEFAULT_OUT)
    args = ap.parse_args(argv)
    alpha = args.alpha if args.alpha is not None else conformal_alpha()

    df = pd.read_csv(args.val_preds)
    if not {"y_true", "p_high_cal"}.issubset(df.columns):
        raise ValueError("val_preds.csv must have columns: y_true, p_high_cal")

    y = df["y_true"].astype(int).to_numpy()
    p_high = df["p_high_cal"].astype(float).to_numpy()

    scores = nonconformity_from_p(p_high, y)
    qhat = compute_qhat(scores, alpha=alpha)

    out = {
        "alpha": float(alpha),
        "alpha_fraction": str(alpha),
        "qhat": qhat_to_json(qhat),
        "n": int(len(scores)),
        "source": Path(args.val_preds).name,
    }
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(out, indent=2, allow_nan=False))
    print(json.dumps(out, indent=2, allow_nan=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())
