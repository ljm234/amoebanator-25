"""
Fit the Mahalanobis OOD gate on the training split only.

Fitting the gate on all 30 rows would let the validation rows shape it. This
script rederives the training indices the same way ml/training_calib_dca.py
does (random_state=42, test_size=0.2, stratify=y) and fits the gate
statistics only on those rows.

Output: outputs/metrics/feature_stats_train.json, same schema as
feature_stats.json; --replace also copies it to feature_stats.json, the file
inference reads.

Usage:
  PYTHONPATH=. python scripts/ood/refit_mahalanobis_train.py
  PYTHONPATH=. python scripts/ood/refit_mahalanobis_train.py --quantile 0.99 --replace
"""
from __future__ import annotations

import argparse
import json
import shutil
import sys
from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

REPO_ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(REPO_ROOT))

from ml.robust import NUMERIC_COLS, fit_gate_stats  # noqa: E402

LOG_CSV = REPO_ROOT / "outputs" / "diagnosis_log_pro.csv"
OUT_JSON = REPO_ROOT / "outputs" / "metrics" / "feature_stats_train.json"
PROD_JSON = REPO_ROOT / "outputs" / "metrics" / "feature_stats.json"


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--quantile", type=float, default=0.999)
    parser.add_argument("--use-diagonal", action="store_true", default=True)
    parser.add_argument("--replace", action="store_true",
                        help="Overwrite feature_stats.json with the train-only fit.")
    args = parser.parse_args(argv)

    if not LOG_CSV.exists():
        raise SystemExit(f"missing {LOG_CSV}")
    df = pd.read_csv(LOG_CSV)
    if df.empty:
        raise SystemExit(f"{LOG_CSV} is empty")
    for c in NUMERIC_COLS:
        if c in df.columns:
            df[c] = pd.to_numeric(df[c], errors="coerce")

    if "risk_label" not in df.columns:
        raise SystemExit("diagnosis_log_pro.csv missing risk_label column")
    y = (df["risk_label"].astype(str).str.lower() == "high").astype(int).to_numpy()
    idx = np.arange(len(df))
    train_idx, _ = train_test_split(idx, test_size=0.2, stratify=y, random_state=42)

    df_train = df.iloc[train_idx]
    cols = [c for c in NUMERIC_COLS if c in df_train.columns]
    out = fit_gate_stats(df_train[cols].to_numpy(dtype=float), cols, args.quantile, args.use_diagonal)
    out.update({
        "n_train": int(len(train_idx)),
        "n_total": int(len(df)),
        "provenance": "fit on train split only (random_state=42, test_size=0.2, stratify=risk_label==High)",
    })
    tau = out["tau"]
    OUT_JSON.parent.mkdir(parents=True, exist_ok=True)
    OUT_JSON.write_text(json.dumps(out, indent=2))
    print(json.dumps({"wrote": str(OUT_JSON), "tau": tau, "n_train": len(train_idx), "cols": cols}, indent=2))

    if args.replace:
        shutil.copyfile(OUT_JSON, PROD_JSON)
        print(json.dumps({"replaced": str(PROD_JSON)}, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
