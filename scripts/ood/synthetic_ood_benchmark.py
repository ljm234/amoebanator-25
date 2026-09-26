"""
Synthetic OOD shift benchmarks.

Generates two random synthetic shifts of the bundled simulated data and
reports how well each score separates the shifted rows: the two OOD gates
(Mahalanobis, logit-energy) and the secondary neg-energy signal, which never
abstains:

  * covariate_shift - multiply CSF lab values by random factors in [0.5, 2.0]
                      and add Gaussian noise; keep labels as-is.
  * label_shift     - flip risk_label with probability 0.5. Neither the model
                      nor any gate reads the label, so every shifted row
                      scores exactly like its bundled row and every AUC is 0.5
                      by construction; this is a sanity check, not a
                      detectable shift.

The in-distribution rows are the 30 bundled rows. For each shift type and
score we report the AUC of the continuous score as an OOD discriminator,
and, at its fitted threshold, the detection rate (share of shifted rows
flagged) and the false-alarm rate (share of bundled rows flagged). Each score
is used the way ml/infer.py flags it: above its threshold. For the two gates
a higher score is more OOD, and a flag means abstention. The neg-energy
score is log(1 - p_high), so a higher value means only a smaller p_high (a
more confident Low prediction); its flag never causes an abstention.

Output: outputs/metrics/synthetic_ood_benchmark.json
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.metrics import roc_auc_score

REPO_ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(REPO_ROOT))

from ml.infer import NEG_ENERGY_JSON, _real_logits, _softmax_high  # noqa: E402
from ml.ood_energy import neg_energy_from_p  # noqa: E402
from ml.robust import ENERGY_JSON, load_stats, score_energy, score_tabular  # noqa: E402

LOG_CSV = REPO_ROOT / "outputs" / "diagnosis_log_pro.csv"
OUT_JSON = REPO_ROOT / "outputs" / "metrics" / "synthetic_ood_benchmark.json"

NUMERIC_FEATURES = ["age", "csf_glucose", "csf_protein", "csf_wbc", "pcr", "microscopy", "exposure"]


def _row_signals(row: pd.Series, stats: dict) -> dict[str, float]:
    """Return the Mahalanobis, logit-energy and neg-energy scores for a single row."""
    ood = score_tabular(row=row, stats=stats)
    d2 = float(ood["d2"])
    try:
        lo, hi = _real_logits(row)
        e_logit = float(score_energy(np.array([lo, hi], dtype=float)))
        p_high = _softmax_high(lo, hi)
        e_neg = float(neg_energy_from_p(p_high))
    except Exception:
        e_logit, e_neg = float("nan"), float("nan")
    return {"mahalanobis_d2": d2, "logit_energy": e_logit, "neg_energy": e_neg}


def _gather(df: pd.DataFrame, stats: dict, label: int) -> list[dict[str, float]]:
    out = []
    for _, row in df.iterrows():
        sig = _row_signals(row, stats)
        sig["is_ood"] = float(label)
        out.append(sig)
    return out


def covariate_shift(df: pd.DataFrame, seed: int = 0) -> pd.DataFrame:
    """Multiply numeric labs by random scale in [0.5, 2.0] and add Gaussian noise."""
    rng = np.random.default_rng(seed)
    shifted = df.copy()
    for c in ["csf_glucose", "csf_protein", "csf_wbc"]:
        if c in shifted.columns:
            scale = rng.uniform(0.5, 2.0, size=len(shifted))
            noise = rng.normal(0.0, 0.1, size=len(shifted)) * shifted[c].astype(float).abs()
            shifted[c] = (shifted[c].astype(float) * scale + noise).clip(lower=0.0)
    return shifted


def label_shift(df: pd.DataFrame, seed: int = 1) -> pd.DataFrame:
    """Randomly flip risk_label with probability 0.5 (High becomes Low; Low and
    Moderate become High). Only the label changes; the input features, and so
    every gate score, are identical to the input rows'."""
    rng = np.random.default_rng(seed)
    shifted = df.copy()
    if "risk_label" in shifted.columns:
        flip = rng.random(size=len(shifted)) < 0.5
        new_labels = shifted["risk_label"].astype(str).copy()
        new_labels[flip] = np.where(
            shifted.loc[flip, "risk_label"].astype(str).str.lower() == "high",
            "Low", "High"
        )
        shifted["risk_label"] = new_labels
    return shifted


def gate_thresholds(stats: dict) -> dict[str, float]:
    """
    The threshold each score is flagged above, as inference applies it: the
    Mahalanobis tau from feature_stats.json, and the energy taus from
    energy_threshold.json and ood_energy.json (ml/infer.py abstains when
    d2 > tau and when the logit energy > tau, and flags a neg energy > tau
    without abstaining).
    """
    return {
        "mahalanobis_d2": float(stats.get("tau", float("inf"))),
        "logit_energy": float(json.loads(Path(ENERGY_JSON).read_text())["tau"]),
        "neg_energy": float(json.loads(Path(NEG_ENERGY_JSON).read_text())["tau"]),
    }


def evaluate(
    rows_in: list[dict[str, float]],
    rows_out: list[dict[str, float]],
    taus: dict[str, float],
) -> dict[str, dict[str, float]]:
    df = pd.DataFrame(rows_in + rows_out)
    if "is_ood" not in df.columns:
        raise RuntimeError("rows missing is_ood")
    y = df["is_ood"].astype(int).to_numpy()
    out: dict[str, dict[str, float]] = {}
    for gate in ("mahalanobis_d2", "logit_energy", "neg_energy"):
        s = df[gate].astype(float).to_numpy()
        mask = np.isfinite(s)
        if mask.sum() < 2 or len(np.unique(y[mask])) < 2:
            out[gate] = {"auc": float("nan"), "n_finite": int(mask.sum())}
            continue
        # ml/infer.py flags each score above its threshold, so the score is
        # used as is (for neg-energy, higher only means a smaller p_high).
        flagged = s > taus[gate]
        out[gate] = {
            "auc": float(roc_auc_score(y[mask], s[mask])),
            "n_finite": int(mask.sum()),
            "tau": taus[gate],
            "detection_rate": float(flagged[mask & (y == 1)].mean()),
            "false_alarm_rate": float(flagged[mask & (y == 0)].mean()),
            "median_in_dist": float(np.median(s[mask & (y == 0)])),
            "median_ood": float(np.median(s[mask & (y == 1)])),
        }
    return out


def main() -> int:
    if not LOG_CSV.exists():
        raise SystemExit(f"missing {LOG_CSV}")
    df = pd.read_csv(LOG_CSV)
    for c in NUMERIC_FEATURES:
        if c in df.columns:
            df[c] = pd.to_numeric(df[c], errors="coerce")
    stats = load_stats()
    taus = gate_thresholds(stats)

    in_rows = _gather(df, stats, label=0)
    cov_rows = _gather(covariate_shift(df), stats, label=1)
    lab_rows = _gather(label_shift(df), stats, label=1)

    payload = {
        "n_in_dist": len(in_rows),
        "n_covariate_shift": len(cov_rows),
        "n_label_shift": len(lab_rows),
        "covariate_shift": evaluate(in_rows, cov_rows, taus),
        "label_shift": evaluate(in_rows, lab_rows, taus),
    }
    OUT_JSON.parent.mkdir(parents=True, exist_ok=True)
    OUT_JSON.write_text(json.dumps(payload, indent=2, default=float))
    print(json.dumps(payload, indent=2, default=float))
    return 0


if __name__ == "__main__":
    sys.exit(main())
