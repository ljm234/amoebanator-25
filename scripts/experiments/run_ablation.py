"""
Four-cell ablation across baselines and the Amoebanator MLP.

Every model is fit on the training split and evaluated on the held-out test
split; the report gives AUC + recall@operating-point with bootstrap 95% CIs.
The four cells are:

    base       - the model's own probability, uncalibrated: the scikit-learn
                 estimator fit without its calibration step, or the MLP's
                 softmax at T = 1
    +cal       - the calibrated probability: Platt scaling (logistic
                 regression) or isotonic regression (random forest, gradient
                 boosting), fit by internal cross-validation on the training
                 split, or temperature scaling fit on the calibration split (MLP)
    +conformal - +cal with the split conformal abstain rule, threshold fit on
                 the calibration split
    +ood       - +conformal, also abstaining when a Mahalanobis gate fit on the
                 training split flags the input

Models compared:
  * logistic_platt   (scikit-learn LogisticRegression + Platt scaling)
  * rf_calibrated    (scikit-learn RandomForestClassifier + isotonic)
  * gbm_isotonic     (scikit-learn GradientBoostingClassifier + isotonic)
  * amoebanator_mlp  (the Amoebanator MLP, refit on the ablation's training split with
                      the pipeline's training settings; temperature fit on the
                      calibration split)

Output: outputs/metrics/ablation_table.json with one row per (model, cell)
plus a CSV mirror at outputs/metrics/ablation_table.csv. The JSON also records
the estimator and calibration method each model actually used.

This script runs to completion on the bundled simulated data so the wiring is
proven. The split is 18 training, 6 calibration and 6 test rows, so the
metrics are not meaningful; real metrics need a real cohort.
"""
from __future__ import annotations

import json
import sys
import warnings
from fractions import Fraction
from pathlib import Path
from typing import Any

import numpy as np
import pandas as pd
import torch
from sklearn.metrics import recall_score, roc_auc_score

REPO_ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(REPO_ROOT))

from ml.baselines import GBMIsotonic, LogisticPlatt, RFCalibrated  # noqa: E402
from ml.config import conformal_alpha  # noqa: E402
from ml.conformal_advanced import (  # noqa: E402
    qhat_to_json,
    SmallCalibrationWarning,
    compute_qhat,
    nonconformity_from_p,
)
from ml.metrics.bootstrap import bootstrap_ci  # noqa: E402
from ml.robust import NUMERIC_COLS, fit_gate_stats, score_tabular  # noqa: E402
from ml.splits import split_summary, stratified_split  # noqa: E402
from ml.model import MLP  # noqa: E402
from ml.seeds import set_global_seeds  # noqa: E402
from ml.training_calib_dca import (  # noqa: E402
    fit_clamped_temperature,
    load_tabular,
    select_device,
    train_mlp,
)

OUT_JSON = REPO_ROOT / "outputs" / "metrics" / "ablation_table.json"
OUT_CSV = REPO_ROOT / "outputs" / "metrics" / "ablation_table.csv"
OPERATING_POINT = 0.5


def _safe_auc(y: np.ndarray, p: np.ndarray) -> float:
    if len(np.unique(y)) < 2:
        return float("nan")
    return float(roc_auc_score(y, p))


def _safe_recall(y: np.ndarray, p: np.ndarray, t: float = OPERATING_POINT) -> float:
    if len(np.unique(y)) < 2:
        return float("nan")
    return float(recall_score(y, (p >= t).astype(int), pos_label=1, zero_division=0.0))  # type: ignore[arg-type]


def _ci(metric_fn: Any, y: np.ndarray, p: np.ndarray) -> dict[str, float] | None:
    try:
        if len(np.unique(y)) < 2:
            return None
        return dict(bootstrap_ci(metric_fn, y, p, n_resamples=2000, alpha=0.05, seed=0))  # type: ignore[arg-type]
    except Exception as e:
        warnings.warn(f"bootstrap CI failed: {type(e).__name__}: {e}", stacklevel=2)
        return None


def _mlp_logits(model: MLP, X: np.ndarray) -> np.ndarray:
    device = next(model.parameters()).device
    with torch.no_grad():
        return model(torch.tensor(X, dtype=torch.float32, device=device)).cpu().numpy()


def _amoebanator_proba(model: MLP, T: float, X: np.ndarray) -> np.ndarray:
    """Temperature-scaled High-class probability from the MLP."""
    raw = _mlp_logits(model, X) / T
    z = raw - raw.max(axis=1, keepdims=True)
    e = np.exp(z)
    return (e / e.sum(axis=1, keepdims=True))[:, 1].astype(float)


def _fit_amoebanator_mlp(
    Xtr: np.ndarray, ytr: np.ndarray, Xca: np.ndarray, yca: np.ndarray
) -> tuple[MLP, float]:
    """
    Refit the MLP on the ablation's training split, like the baselines, so no
    calibration or test row was seen in training. The shipped model.pt was
    trained on a different split of the same 30 rows and would leak here.
    """
    set_global_seeds()
    model = train_mlp(Xtr, ytr, select_device())
    T = fit_clamped_temperature(model, _mlp_logits(model, Xca), yca)
    return model, T


def _fit_ood_gate(Xtr: np.ndarray, feature_names: list[str]) -> dict[str, Any]:
    """
    Fit the Mahalanobis gate on the ablation's training split, over the gate's
    columns that the ablation's features include. The shipped
    feature_stats.json was fit on a different split of the same 30 rows and
    would leak here.
    """
    cols = [c for c in NUMERIC_COLS if c in feature_names]
    idx = [feature_names.index(c) for c in cols]
    return fit_gate_stats(Xtr[:, idx], cols)


def _ood_mask(X: np.ndarray, feature_names: list[str], stats: dict[str, Any]) -> np.ndarray:
    """Boolean mask of rows the Mahalanobis OOD gate would abstain on."""
    abstain = np.zeros(len(X), dtype=bool)
    for i, row_arr in enumerate(X):
        row = pd.Series({c: row_arr[feature_names.index(c)] for c in feature_names})
        ood = score_tabular(row=row, stats=stats)
        abstain[i] = not ood["in_dist"]
    return abstain


def _evaluate_cells(
    name: str,
    p_base: np.ndarray,
    p_cal: np.ndarray,
    cal_scores: np.ndarray,
    y_test: np.ndarray,
    ood_mask: np.ndarray,
    alpha: float | Fraction | None = None,
) -> list[dict[str, Any]]:
    if alpha is None:
        alpha = conformal_alpha()
    rows: list[dict[str, Any]] = []
    for cell, p in [("base", p_base), ("+cal", p_cal)]:
        rows.append({
            "model": name, "cell": cell,
            "n": int(len(y_test)), "n_pos": int(y_test.sum()),
            "auc": _safe_auc(y_test, p),
            "auc_ci": _ci(_safe_auc, y_test, p),
            "recall_high@0.5": _safe_recall(y_test, p),
            "recall_ci": _ci(_safe_recall, y_test, p),
            "abstain_rate": 0.0,
        })
    qhat = compute_qhat(cal_scores, alpha=alpha)
    include_high = p_cal >= (1.0 - qhat)
    include_low = p_cal <= qhat
    abstain_conformal = include_high == include_low  # empty or two-class set
    keep = ~abstain_conformal
    rows.append({
        "model": name, "cell": "+conformal",
        "n": int(keep.sum()), "n_pos": int(y_test[keep].sum()),
        "auc": _safe_auc(y_test[keep], p_cal[keep]) if keep.sum() else float("nan"),
        "auc_ci": _ci(_safe_auc, y_test[keep], p_cal[keep]) if keep.sum() else None,
        "recall_high@0.5": _safe_recall(y_test[keep], p_cal[keep]) if keep.sum() else float("nan"),
        "recall_ci": _ci(_safe_recall, y_test[keep], p_cal[keep]) if keep.sum() else None,
        "abstain_rate": float(abstain_conformal.mean()),
        "qhat": qhat_to_json(qhat), "alpha": float(alpha),
    })
    abstain_combined = abstain_conformal | ood_mask
    keep_c = ~abstain_combined
    rows.append({
        "model": name, "cell": "+ood",
        "n": int(keep_c.sum()), "n_pos": int(y_test[keep_c].sum()),
        "auc": _safe_auc(y_test[keep_c], p_cal[keep_c]) if keep_c.sum() else float("nan"),
        "auc_ci": _ci(_safe_auc, y_test[keep_c], p_cal[keep_c]) if keep_c.sum() else None,
        "recall_high@0.5": _safe_recall(y_test[keep_c], p_cal[keep_c]) if keep_c.sum() else float("nan"),
        "recall_ci": _ci(_safe_recall, y_test[keep_c], p_cal[keep_c]) if keep_c.sum() else None,
        "abstain_rate": float(abstain_combined.mean()),
        "ood_abstain_rate": float(ood_mask.mean()),
        "qhat": qhat_to_json(qhat), "alpha": float(alpha),
    })
    return rows


def main() -> int:
    X, y, feats = load_tabular()
    splits = stratified_split(y, train_frac=0.6, val_frac=0.2, test_frac=0.2, seed=42)
    summary = split_summary(y, splits)

    Xtr, ytr = X[splits["train"]], y[splits["train"]]
    Xca, yca = X[splits["val"]], y[splits["val"]]
    Xte, yte = X[splits["test"]], y[splits["test"]]

    ood_mask_test = _ood_mask(Xte, feats, _fit_ood_gate(Xtr, feats))
    rows: list[dict[str, Any]] = []
    models: dict[str, dict[str, str]] = {}

    with warnings.catch_warnings():
        warnings.simplefilter("default", category=SmallCalibrationWarning)

        for name, factory in [
            ("logistic_platt", LogisticPlatt),
            ("rf_calibrated", RFCalibrated),
            ("gbm_isotonic", GBMIsotonic),
        ]:
            try:
                clf = factory()
                clf.fit(Xtr, ytr)
                raw = clf.uncalibrated().fit(Xtr, ytr)
            except Exception as e:
                warnings.warn(f"{name}: fit failed: {type(e).__name__}: {e}", stacklevel=2)
                continue
            assert clf.model_ is not None
            models[name] = {
                "estimator": type(clf.model_.estimator).__name__,
                "calibration": str(clf.model_.method),
            }
            p_base = raw.predict_proba(Xte)[:, 1]
            p_cal = clf.predict_proba_high(Xte)
            cal_scores = nonconformity_from_p(clf.predict_proba_high(Xca), yca)
            rows.extend(_evaluate_cells(name, p_base, p_cal, cal_scores, yte, ood_mask_test))

        try:
            mlp, T = _fit_amoebanator_mlp(Xtr, ytr, Xca, yca)
            models["amoebanator_mlp"] = {"estimator": "MLP", "calibration": "temperature"}
            p_base = _amoebanator_proba(mlp, 1.0, Xte)
            p_te = _amoebanator_proba(mlp, T, Xte)
            p_ca = _amoebanator_proba(mlp, T, Xca)
            cal_scores = nonconformity_from_p(p_ca, yca)
            rows.extend(_evaluate_cells("amoebanator_mlp", p_base, p_te, cal_scores, yte, ood_mask_test))
        except Exception as e:
            warnings.warn(f"amoebanator_mlp evaluation failed: {type(e).__name__}: {e}", stacklevel=2)

    OUT_JSON.parent.mkdir(parents=True, exist_ok=True)
    payload = {
        "models": models,
        "splits": summary,
        "operating_point": OPERATING_POINT,
        "rows": rows,
    }
    OUT_JSON.write_text(json.dumps(payload, indent=2, default=float))
    pd.DataFrame(rows).to_csv(OUT_CSV, index=False)
    print(json.dumps({"n_rows": len(rows), "wrote": [str(OUT_JSON), str(OUT_CSV)]}, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
