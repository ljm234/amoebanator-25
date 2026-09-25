"""
Calibrated baselines for ablation comparisons against the Amoebanator MLP.

Every baseline exposes the same interface so the ablation runner treats them
uniformly:

    fit(X_train, y_train) -> self          # calibrated by internal cross-validation
    predict_proba_high(X) -> np.ndarray    # calibrated P(High), shape (n,)
    uncalibrated() -> unfitted scikit-learn estimator with the same settings

Baselines:
  * logistic.LogisticPlatt     - sklearn LogisticRegression + Platt scaling
  * random_forest.RFCalibrated - sklearn RandomForestClassifier + isotonic
  * gbm.GBMIsotonic            - sklearn GradientBoostingClassifier + isotonic

Isotonic calibration falls back to sigmoid when a class has fewer than five
training rows. `build_all_baselines()` returns (name, class) pairs.
"""
from ml.baselines.gbm import GBMIsotonic
from ml.baselines.logistic import LogisticPlatt
from ml.baselines.random_forest import RFCalibrated

__all__ = [
    "LogisticPlatt",
    "RFCalibrated",
    "GBMIsotonic",
    "build_all_baselines",
]


def build_all_baselines() -> list[tuple[str, type]]:
    return [
        ("logistic_platt", LogisticPlatt),
        ("rf_calibrated", RFCalibrated),
        ("gbm_isotonic", GBMIsotonic),
    ]
