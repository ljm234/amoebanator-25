"""
Gradient boosted trees + isotonic calibration baseline.

scikit-learn's GradientBoostingClassifier, wrapped in CalibratedClassifierCV
with isotonic regression (sigmoid when a class has fewer than five training
rows). Boosted trees tend to be miscalibrated, so the probabilities are
recalibrated post hoc.

References:
  Friedman JH. "Greedy Function Approximation: A Gradient Boosting Machine."
  Annals of Statistics 2001.
"""
from __future__ import annotations

import numpy as np
from sklearn.calibration import CalibratedClassifierCV
from sklearn.ensemble import GradientBoostingClassifier


class GBMIsotonic:
    name: str = "gbm_isotonic"

    def __init__(
        self,
        n_estimators: int = 200,
        learning_rate: float = 0.05,
        max_depth: int = 4,
        random_state: int = 42,
    ) -> None:
        self.n_estimators = n_estimators
        self.learning_rate = learning_rate
        self.max_depth = max_depth
        self.random_state = random_state
        self.model_: CalibratedClassifierCV | None = None

    def uncalibrated(self) -> GradientBoostingClassifier:
        """The unfitted classifier, with the same settings and no calibration."""
        return GradientBoostingClassifier(
            n_estimators=self.n_estimators,
            learning_rate=self.learning_rate,
            max_depth=self.max_depth,
            random_state=self.random_state,
        )

    def fit(self, X_train: np.ndarray, y_train: np.ndarray) -> "GBMIsotonic":
        n_per_class_min = int(min(np.bincount(y_train)))
        cv = max(2, min(5, n_per_class_min))
        method = "isotonic" if n_per_class_min >= 5 else "sigmoid"
        self.model_ = CalibratedClassifierCV(self.uncalibrated(), method=method, cv=cv)
        self.model_.fit(X_train, y_train)
        return self

    def predict_proba_high(self, X: np.ndarray) -> np.ndarray:
        if self.model_ is None:
            raise RuntimeError(f"{type(self).__name__}: call fit() before predict_proba_high().")
        return self.model_.predict_proba(X)[:, 1]
