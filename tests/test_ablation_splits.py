"""
The ablation must measure what its cells claim. Every model and gate it
reports is fit only on the ablation's own training or calibration split, never
on rows it is evaluated on, and the base cell is the uncalibrated probability,
not the calibrated one.
"""
from __future__ import annotations

import json
from collections.abc import Iterator
from typing import Any

import numpy as np
import pytest

import scripts.experiments.run_ablation as ra
from ml.robust import NUMERIC_COLS
from ml.splits import stratified_split
from ml.training_calib_dca import load_tabular


@pytest.fixture(scope="module")
def ablation_run(tmp_path_factory: pytest.TempPathFactory) -> Iterator[dict[str, Any]]:
    tmp = tmp_path_factory.mktemp("ablation")
    seen: dict[str, Any] = {"cells": {}}
    real_train = ra.train_mlp
    real_temperature = ra.fit_clamped_temperature
    real_gate = ra.fit_gate_stats
    real_cells = ra._evaluate_cells

    def spy_train(Xtr: np.ndarray, ytr: np.ndarray, device: str) -> Any:
        seen["mlp_train"] = Xtr.copy()
        return real_train(Xtr, ytr, device)

    def spy_temperature(model: Any, logits: np.ndarray, yva: np.ndarray) -> float:
        seen["temperature_labels"] = yva.copy()
        return real_temperature(model, logits, yva)

    def spy_gate(X: np.ndarray, cols: list[str], *args: Any, **kwargs: Any) -> dict[str, Any]:
        seen["gate_rows"] = X.copy()
        seen["gate_cols"] = list(cols)
        return real_gate(X, cols, *args, **kwargs)

    def spy_cells(name: str, p_base: np.ndarray, p_cal: np.ndarray, *args: Any, **kwargs: Any) -> Any:
        seen["cells"][name] = (p_base.copy(), p_cal.copy())
        return real_cells(name, p_base, p_cal, *args, **kwargs)

    def no_shipped_model(*_args: Any, **_kwargs: Any) -> Any:
        raise AssertionError("the ablation must not load the shipped model.pt")

    with pytest.MonkeyPatch.context() as mp:
        mp.setattr(ra, "train_mlp", spy_train)
        mp.setattr(ra, "fit_clamped_temperature", spy_temperature)
        mp.setattr(ra, "fit_gate_stats", spy_gate)
        mp.setattr(ra, "_evaluate_cells", spy_cells)
        mp.setattr(ra.torch, "load", no_shipped_model)
        mp.setattr(ra, "_ci", lambda *_a, **_k: None)
        mp.setattr(ra, "OUT_JSON", tmp / "ablation_table.json")
        mp.setattr(ra, "OUT_CSV", tmp / "ablation_table.csv")
        mp.setenv("AMOEBANATOR_AUDIT_PATH", str(tmp / "audit.jsonl"))
        assert ra.main() == 0
    seen["payload"] = json.loads((tmp / "ablation_table.json").read_text())
    yield seen


@pytest.fixture(scope="module")
def data() -> tuple[np.ndarray, np.ndarray, list[str], dict[str, np.ndarray]]:
    X, y, feats = load_tabular()
    splits = stratified_split(y, train_frac=0.6, val_frac=0.2, test_frac=0.2, seed=42)
    return X, y, feats, splits


def test_splits_are_disjoint(data: Any) -> None:
    _, _, _, splits = data
    train_idx = set(splits["train"].tolist())
    assert train_idx.isdisjoint(splits["val"].tolist())
    assert train_idx.isdisjoint(splits["test"].tolist())
    assert set(splits["val"].tolist()).isdisjoint(splits["test"].tolist())


def test_mlp_is_fit_only_on_the_training_split(ablation_run: dict[str, Any], data: Any) -> None:
    X, y, _, splits = data
    assert np.array_equal(ablation_run["mlp_train"], X[splits["train"]])
    assert np.array_equal(ablation_run["temperature_labels"], y[splits["val"]])


def test_ood_gate_is_fit_only_on_the_training_split(ablation_run: dict[str, Any], data: Any) -> None:
    X, _, feats, splits = data
    cols = [c for c in NUMERIC_COLS if c in feats]
    assert ablation_run["gate_cols"] == cols
    idx = [feats.index(c) for c in cols]
    assert np.array_equal(ablation_run["gate_rows"], X[splits["train"]][:, idx])


def test_base_cell_is_uncalibrated(ablation_run: dict[str, Any]) -> None:
    cells = ablation_run["cells"]
    assert set(cells) == {"logistic_platt", "rf_calibrated", "gbm_isotonic", "amoebanator_mlp"}
    for name, (p_base, p_cal) in cells.items():
        assert not np.allclose(p_base, p_cal), name


def test_table_records_what_ran(ablation_run: dict[str, Any]) -> None:
    payload = ablation_run["payload"]
    assert payload["models"] == {
        "logistic_platt": {"estimator": "LogisticRegression", "calibration": "sigmoid"},
        "rf_calibrated": {"estimator": "RandomForestClassifier", "calibration": "isotonic"},
        "gbm_isotonic": {"estimator": "GradientBoostingClassifier", "calibration": "isotonic"},
        "amoebanator_mlp": {"estimator": "MLP", "calibration": "temperature"},
    }
