"""
Advanced split-conformal predictor: marginal + label-conditional + coverage tools.

Builds on ml/conformal.py (which only exposes the
threshold-band decision rule) by adding:

  * compute_qhat             - finite-sample-corrected split conformal threshold
  * finite_sample_rank       - exact rank k = ceil((n+1)(1-alpha)) of that threshold
  * label_conditional_qhats  - per-class threshold dictionary
  * empirical_coverage       - joint and per-class coverage on a held-out set
  * coverage_sweep           - coverage / abstain-rate across multiple alphas
  * qhat_to_json             - JSON-safe form of a threshold that may be infinite
  * SmallCalibrationWarning  - issued when n_cal is below the recommended floor
  * InfiniteThresholdWarning - issued when no finite threshold reaches 1 - alpha

References:
  - Vovk V, Gammerman A, Shafer G. Algorithmic Learning in a Random World.
    Springer, 2005. (split conformal coverage E[cov] >= 1 - alpha)
  - Lei J, G'Sell M, Rinaldo A, Tibshirani RJ, Wasserman L. "Distribution-Free
    Predictive Inference for Regression." JASA 2018. (E[cov] <= 1 - alpha + 1/(n+1)
    when the scores have no ties)
  - Vovk V. "Conditional Validity of Inductive Conformal Predictors."
    Mach Learn 2013;92:349-376. (label-conditional / Mondrian conformal)
"""
from __future__ import annotations

import math
import warnings
from fractions import Fraction
from typing import TypedDict

import numpy as np

from ml.config import parse_alpha

SMALL_CAL_FLOOR: int = 100  # below this, the finite-sample correction matters in practice


class SmallCalibrationWarning(UserWarning):
    """Emitted when a conformal calibration set is below SMALL_CAL_FLOOR, where realized coverage varies widely."""


class InfiniteThresholdWarning(UserWarning):
    """Emitted when ceil((n+1)(1-alpha)) > n, so the valid threshold is infinite."""


class CoverageResult(TypedDict):
    alpha: float
    qhat: float
    coverage: float
    abstain_rate: float
    n: int


def _check_alpha(alpha: float | Fraction) -> None:
    if not (0 < alpha < 1):
        raise ValueError(f"alpha must lie in (0, 1); got {alpha!r}.")


def finite_sample_rank(n: int, alpha: float | Fraction) -> int:
    """
    Rank k = ceil((n+1)(1-alpha)) of the split-conformal threshold, in exact
    arithmetic after ml.config.parse_alpha, so 1/7 computed in floating point
    gives k = n for n = 6 while 0.1428571 (just below 1/7) gives k = n + 1.
    """
    return math.ceil((n + 1) * (1 - parse_alpha(alpha)))


def _check_calibration_size(n: int) -> None:
    if n < 1:
        raise ValueError(f"calibration set must be non-empty; got n={n}.")
    if n < SMALL_CAL_FLOOR:
        warnings.warn(
            f"Conformal calibration set size n={n} is below the recommended "
            f"floor of {SMALL_CAL_FLOOR}. Split conformal coverage still holds on "
            f"average under exchangeability, but with n = {n} the realized "
            f"coverage varies widely, and a valid threshold cannot target more "
            f"than {n}/{n + 1} coverage, about {100 * n / (n + 1):.0f} percent, "
            f"without abstaining on every input.",
            SmallCalibrationWarning,
            stacklevel=3,
        )


def compute_qhat(
    nonconformity_scores: np.ndarray,
    alpha: float | Fraction,
    finite_sample_correction: bool = True,
    stacklevel: int = 2,
) -> float:
    """
    Split-conformal qhat from nonconformity scores at miscoverage level alpha.

    With the finite-sample correction (default), the threshold is the
    k-th smallest score with k = ceil((n+1)(1-alpha)). When k > n no finite
    threshold reaches 1 - alpha coverage: the function returns +inf, so every
    prediction set holds both classes and every input abstains, and it issues
    InfiniteThresholdWarning. Without the correction it falls back to the
    (1-alpha) sample quantile.

    Issues SmallCalibrationWarning when n < SMALL_CAL_FLOOR.
    """
    _check_alpha(alpha)
    scores = np.asarray(nonconformity_scores, dtype=float).ravel()
    n = len(scores)
    _check_calibration_size(n)
    if finite_sample_correction:
        k = max(finite_sample_rank(n, alpha), 1)
        if k > n:
            warnings.warn(
                f"alpha = {parse_alpha(alpha)} needs rank k = {k}, but there are "
                f"only n = {n} calibration scores, so no finite threshold "
                f"guarantees {1.0 - float(alpha):.4f} coverage. The threshold is "
                f"+inf; a marginal band then holds both classes, so every input "
                f"abstains. With n = {n} the highest coverage a finite threshold "
                f"guarantees is {n}/{n + 1} (alpha = 1/{n + 1}).",
                InfiniteThresholdWarning,
                stacklevel=stacklevel,
            )
            return math.inf
        return float(np.partition(scores, k - 1)[k - 1])
    return float(np.quantile(scores, 1.0 - float(alpha)))


def label_conditional_qhats(
    nonconformity_scores: np.ndarray,
    labels: np.ndarray,
    alpha: float | Fraction,
    finite_sample_correction: bool = True,
) -> dict[int, float]:
    """
    Vovk 2013 label-conditional (Mondrian) conformal: a separate qhat per class.

    Returns {class_label: qhat}. Per-class coverage holds at 1-alpha conditional on
    each class label, which is what you want for low-prevalence triage where
    the marginal positive rate would otherwise dominate the threshold.
    """
    _check_alpha(alpha)
    scores = np.asarray(nonconformity_scores, dtype=float).ravel()
    labs = np.asarray(labels).ravel()
    if scores.shape != labs.shape:
        raise ValueError(
            f"scores shape {scores.shape} != labels shape {labs.shape}"
        )
    out: dict[int, float] = {}
    for cls in np.unique(labs):
        mask = labs == cls
        cls_scores = scores[mask]
        if len(cls_scores) == 0:
            continue
        out[int(cls)] = compute_qhat(cls_scores, alpha, finite_sample_correction, stacklevel=3)
    return out


def empirical_coverage(
    p_high: np.ndarray,
    y_true: np.ndarray,
    qhat: float,
) -> CoverageResult:
    """
    Empirical (joint) coverage and abstain rate of the conformal band on
    held-out data. A row abstains unless its prediction set holds exactly one
    class, so both an empty set and a two-class set count as abstentions.
    Returns alpha-style summary so callers can compare to target.
    """
    p = np.asarray(p_high, dtype=float).ravel()
    y = np.asarray(y_true).ravel()
    if p.shape != y.shape:
        raise ValueError(f"p_high shape {p.shape} != y_true shape {y.shape}")
    n = len(p)
    if n == 0:
        return {
            "alpha": float("nan"), "qhat": float(qhat),
            "coverage": float("nan"), "abstain_rate": float("nan"), "n": 0,
        }
    include_high = p >= (1.0 - qhat)
    include_low = p <= qhat
    abstain = include_high == include_low
    is_high = (y == 1)
    contained = (is_high & include_high) | (~is_high & include_low)
    coverage = float(contained.mean())
    abstain_rate = float(abstain.mean())
    return {
        "alpha": float(1.0 - coverage),
        "qhat": float(qhat),
        "coverage": coverage,
        "abstain_rate": abstain_rate,
        "n": int(n),
    }


def coverage_sweep(
    cal_scores: np.ndarray,
    test_p_high: np.ndarray,
    test_y: np.ndarray,
    alphas: tuple[float, ...] = (0.05, 0.10, 0.20),
    finite_sample_correction: bool = True,
) -> list[CoverageResult]:
    """
    Fit qhat on `cal_scores` for each alpha, then evaluate empirical coverage
    + abstain rate on (`test_p_high`, `test_y`). Returns one CoverageResult
    per alpha, in the same order as `alphas`.
    """
    out: list[CoverageResult] = []
    for a in alphas:
        qhat = compute_qhat(cal_scores, a, finite_sample_correction, stacklevel=3)
        result = empirical_coverage(test_p_high, test_y, qhat)
        result["alpha"] = float(a)
        out.append(result)
    return out


def qhat_to_json(qhat: float) -> float | str:
    """A threshold as JSON: finite values as numbers, +inf as the string "inf"."""
    return float(qhat) if math.isfinite(qhat) else "inf"


def nonconformity_from_p(p_high: np.ndarray, y_true: np.ndarray) -> np.ndarray:
    """
    Standard nonconformity score for binary classification with calibrated
    probabilities: 1 - probability assigned to the true class.
    """
    p = np.asarray(p_high, dtype=float).ravel()
    y = np.asarray(y_true).ravel()
    if p.shape != y.shape:
        raise ValueError(f"shape mismatch: {p.shape} vs {y.shape}")
    p_true = np.where(y == 1, p, 1.0 - p)
    return 1.0 - p_true
