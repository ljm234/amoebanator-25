"""
Threshold, abstention and energy-gate checks for the conformal and OOD steps.

Covers the finite-sample rank at n = 6, the demo target of 6/7 coverage read
from config/amoebanator.toml, abstention on empty and two-class prediction
sets, and an energy threshold fit on the same temperature-scaled logits that
ml/infer.py scores.
"""
from __future__ import annotations

import json
import math
import warnings
from collections.abc import Iterator
from fractions import Fraction
from pathlib import Path
from typing import Any

import numpy as np
import pytest

import ml.infer as infer
from ml.config import conformal_alpha, parse_alpha
from ml.conformal import decision_from_p_high
from ml.conformal_advanced import (
    InfiniteThresholdWarning,
    SmallCalibrationWarning,
    compute_qhat,
    empirical_coverage,
    finite_sample_rank,
)
from ml.robust import score_energy
from scripts.ood.fit_gates import fit_logit_energy

# Nonconformity scores of the six-row fixture in tests/test_conformal_fit_script.py;
# n = 6 matches the bundled validation split.
SCORES = np.array([0.08, 0.05, 0.12, 0.10, 0.29, 0.35])

# An in-distribution row that passes the Mahalanobis and energy gates.
_BENIGN: dict[str, Any] = {
    "age": 45, "csf_glucose": 70.0, "csf_protein": 0.4, "csf_wbc": 3,
    "pcr": 0, "microscopy": 0, "exposure": 0, "symptoms": "", "risk_score": 5,
}


@pytest.fixture(autouse=True)
def _quiet_small_calibration() -> Iterator[None]:
    with warnings.catch_warnings():
        warnings.simplefilter("ignore", SmallCalibrationWarning)
        yield


def test_alpha_0_10_with_six_points_gives_infinite_threshold_and_warning() -> None:
    with pytest.warns(InfiniteThresholdWarning, match="no finite threshold"):
        qhat = compute_qhat(SCORES, alpha=0.10)
    assert math.isinf(qhat) and qhat > 0


@pytest.mark.parametrize("alpha", [Fraction(1, 7), 1 / 7, "1/7"])
def test_alpha_one_seventh_gives_largest_calibration_score(alpha: Any) -> None:
    with warnings.catch_warnings():
        warnings.simplefilter("error", InfiniteThresholdWarning)
        qhat = compute_qhat(SCORES, alpha=parse_alpha(alpha))
    assert qhat == SCORES.max()


def test_config_sets_demo_target_to_six_sevenths() -> None:
    assert conformal_alpha() == Fraction(1, 7)
    assert finite_sample_rank(6, conformal_alpha()) == 6
    assert finite_sample_rank(6, 0.10) == 7


def test_float_alpha_near_one_seventh_keeps_its_exact_value() -> None:
    assert parse_alpha(1 / 7) == Fraction(1, 7)
    assert parse_alpha(0.1) == Fraction(1, 10)
    # 0.1428571 is below 1/7, so six points cannot support it.
    assert finite_sample_rank(6, 0.1428571) == 7
    with pytest.raises(ValueError):
        parse_alpha("1/0")


def test_decision_rule_abstains_on_empty_and_two_class_sets() -> None:
    assert decision_from_p_high(0.5, qhat=0.10) == "ABSTAIN"  # neither class
    assert decision_from_p_high(0.5, qhat=0.60) == "ABSTAIN"  # both classes
    assert decision_from_p_high(0.97, qhat=0.10) == "High"
    assert decision_from_p_high(0.02, qhat=0.10) == "Low"


def test_coverage_report_counts_empty_and_two_class_sets_as_abstentions() -> None:
    p = np.array([0.5, 0.97, 0.02])
    y = np.array([1, 1, 0])
    # qhat 0.10: the p = 0.5 row gets an empty set; the other two are single-class.
    assert empirical_coverage(p, y, qhat=0.10)["abstain_rate"] == pytest.approx(1 / 3)
    # qhat 0.60: the p = 0.5 row gets both classes; the other two are single-class.
    assert empirical_coverage(p, y, qhat=0.60)["abstain_rate"] == pytest.approx(1 / 3)
    # An infinite threshold puts both classes in every set.
    assert empirical_coverage(p, y, qhat=math.inf)["abstain_rate"] == pytest.approx(1.0)


@pytest.mark.parametrize(
    ("qhat", "reason"),
    [(0.10, "ConformalEmptySet"), (0.60, "ConformalAmbiguity")],
)
def test_infer_one_abstains_on_empty_and_two_class_sets(
    monkeypatch: pytest.MonkeyPatch, qhat: float, reason: str
) -> None:
    # Equal logits give p_high = 0.5 and energy -5.69, below the shipped gate,
    # so the row reaches the conformal step.
    monkeypatch.setattr(infer, "_real_logits", lambda _row: (5.0, 5.0))
    monkeypatch.setattr(infer, "_choose_qhat", lambda _age: (qhat, 1 / 7, "global"))
    out = infer.infer_one(_BENIGN)
    assert out["prediction"] == "ABSTAIN"
    assert out["reason"] == reason
    assert out["include_low"] == out["include_high"]


def test_energy_gate_flags_about_five_percent_at_95th_percentile() -> None:
    rng = np.random.default_rng(0)
    logits = rng.normal(0.0, 3.0, size=(4000, 2))
    T = 0.27
    gate = fit_logit_energy(logits, q=0.95, T=T)
    assert gate["logits"] == "temperature_scaled"
    # ml/infer.py scores energy on the temperature-scaled logits it gets from
    # _real_logits, so the gate is applied on the same scale it was fit on.
    energies = np.array([score_energy(row / T) for row in logits])
    flagged = float((energies > gate["tau"]).mean())
    assert flagged == pytest.approx(0.05, abs=0.01)


def test_shipped_energy_threshold_matches_the_model_temperature() -> None:
    gate = json.loads(Path(infer.ENERGY_JSON).read_text())
    T = json.loads(infer.TEMPERATURE_JSON.read_text())["T"]
    assert gate["logits"] == "temperature_scaled"
    assert gate["T"] == pytest.approx(T, rel=1e-9)


def test_infer_rejects_an_energy_threshold_fit_on_another_scale(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    raw_gate = tmp_path / "energy_threshold.json"
    raw_gate.write_text(json.dumps({"tau": -0.99, "q": 0.95, "n": 6}))
    monkeypatch.setattr(infer, "ENERGY_JSON", raw_gate)
    with pytest.raises(ValueError, match="not fit on logits scaled"):
        infer.infer_one(_BENIGN)
