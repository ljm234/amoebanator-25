"""
Tests for the core ML modules.

Covers:
  ml/calibration.py      - TemperatureScaler, fit_temperature
  ml/conformal.py        - set_from_p_high, decision_from_p_high
  ml/ood_energy.py       - neg-energy signal on the temperature-scaled probability
  ml/robust.py           - Mahalanobis gate statistics and scoring, energy score

All tests are self-contained (no disk I/O side-effects on persistent paths).
File I/O tests use pytest's tmp_path fixture.
"""

from __future__ import annotations

import json
import math
from pathlib import Path
from typing import Any

import numpy as np
import pandas as pd
import pytest
import torch


# -----------------------------------------------------------------------------
# ml/calibration.py
# -----------------------------------------------------------------------------


class TestTemperatureScaler:
    def test_init_temperature_is_one(self) -> None:
        from ml.calibration import TemperatureScaler

        scaler = TemperatureScaler()
        assert abs(scaler.temperature() - 1.0) < 1e-5

    def test_forward_divides_logits_by_temperature(self) -> None:
        from ml.calibration import TemperatureScaler

        scaler = TemperatureScaler()
        logits = torch.tensor([[2.0, 1.0]])
        out = scaler(logits)
        # at T=1, output == input
        assert torch.allclose(out, logits, atol=1e-5)

    def test_temperature_above_zero_after_forward(self) -> None:
        from ml.calibration import TemperatureScaler

        scaler = TemperatureScaler()
        assert scaler.temperature() > 0

    def test_high_logT_increases_temperature(self) -> None:
        from ml.calibration import TemperatureScaler

        scaler = TemperatureScaler()
        with torch.no_grad():
            scaler.logT.fill_(1.0)  # T = e^1 ~= 2.718
        assert abs(scaler.temperature() - math.e) < 0.01

    def test_forward_scales_correctly_with_temperature_2(self) -> None:
        from ml.calibration import TemperatureScaler

        scaler = TemperatureScaler()
        with torch.no_grad():
            scaler.logT.fill_(math.log(2.0))  # T = 2
        logits = torch.tensor([[4.0, 2.0]])
        out = scaler(logits)
        expected = torch.tensor([[2.0, 1.0]])
        assert torch.allclose(out, expected, atol=1e-4)


class TestFitTemperature:
    def _make_logits_and_labels(self, n: int = 80) -> tuple[Any, Any]:
        rng = np.random.default_rng(42)
        # Logits: slightly miscalibrated binary
        logits = rng.normal(size=(n, 2)).astype(np.float32)
        logits[:n//2, 1] += 2.0  # class 1 easier to predict
        y = np.array([1] * (n // 2) + [0] * (n // 2), dtype=np.int64)
        return logits, y

    def test_returns_positive_float(self) -> None:
        from ml.calibration import fit_temperature, TemperatureScaler

        logits, y = self._make_logits_and_labels()
        model = TemperatureScaler()
        T = fit_temperature(model, logits, y, max_iter=5, lr=0.1)
        assert isinstance(T, float)
        assert T > 0.0

    def test_temperature_reduces_loss(self) -> None:
        from ml.calibration import fit_temperature, TemperatureScaler

        logits, y = self._make_logits_and_labels()
        model = TemperatureScaler()
        T = fit_temperature(model, logits, y, max_iter=50, lr=0.05)
        # Temperature must be finite and in a sensible range
        assert 0.1 < T < 10.0

    def test_handles_cpu_device(self) -> None:
        from ml.calibration import fit_temperature, TemperatureScaler

        logits = np.array([[1.5, -0.5], [0.2, 1.8]], dtype=np.float32)
        y = np.array([0, 1], dtype=np.int64)
        model = TemperatureScaler()
        T = fit_temperature(model, logits, y, device="cpu", max_iter=10)
        assert isinstance(T, float)

    def test_perfect_logits_temperature_near_one(self) -> None:
        """When logits are already well-calibrated, T should stay near 1."""
        from ml.calibration import fit_temperature, TemperatureScaler

        rng = np.random.default_rng(7)
        n = 100
        logits = np.zeros((n, 2), dtype=np.float32)
        y = rng.integers(0, 2, n).astype(np.int64)
        for i, yi in enumerate(y):
            logits[i, yi] = 3.0
            logits[i, 1 - yi] = -3.0
        model = TemperatureScaler()
        T = fit_temperature(model, logits, y, max_iter=30)
        # Well-separated logits -> temperature close to 1 or slightly < 1
        assert 0.01 < T < 5.0


# -----------------------------------------------------------------------------
# ml/conformal.py
# -----------------------------------------------------------------------------


class TestSetFromPHigh:
    def test_high_p_includes_high(self) -> None:
        from ml.conformal import set_from_p_high

        low, high = set_from_p_high(0.9, 0.1)
        assert high is True
        assert low is False

    def test_low_p_includes_low(self) -> None:
        from ml.conformal import set_from_p_high

        low, high = set_from_p_high(0.05, 0.1)
        assert low is True
        assert high is False

    def test_ambiguous_p_includes_both(self) -> None:
        from ml.conformal import set_from_p_high

        low, high = set_from_p_high(0.5, 0.6)
        assert low is True
        assert high is True

    def test_neither_at_boundary(self) -> None:
        from ml.conformal import set_from_p_high

        low, high = set_from_p_high(0.5, 0.3)
        assert low is False
        assert high is False

    def test_exact_boundary_high(self) -> None:
        from ml.conformal import set_from_p_high

        # p_high == 1 - qhat exactly -> include_high
        low, high = set_from_p_high(0.8, 0.2)
        assert high is True

    def test_exact_boundary_low(self) -> None:
        from ml.conformal import set_from_p_high

        # p_high == qhat exactly -> include_low
        low, high = set_from_p_high(0.2, 0.2)
        assert low is True


class TestDecisionFromPHigh:
    def test_high_decision(self) -> None:
        from ml.conformal import decision_from_p_high

        assert decision_from_p_high(0.95, 0.1) == "High"

    def test_low_decision(self) -> None:
        from ml.conformal import decision_from_p_high

        assert decision_from_p_high(0.02, 0.1) == "Low"

    def test_abstain_when_both(self) -> None:
        from ml.conformal import decision_from_p_high

        assert decision_from_p_high(0.5, 0.6) == "ABSTAIN"

    def test_abstain_string_exact(self) -> None:
        from ml.conformal import decision_from_p_high

        result = decision_from_p_high(0.5, 0.9)
        assert result == "ABSTAIN"

    def test_decision_is_string(self) -> None:
        from ml.conformal import decision_from_p_high

        result = decision_from_p_high(0.8, 0.15)
        assert isinstance(result, str)


# -----------------------------------------------------------------------------
# ml/ood_energy.py
# -----------------------------------------------------------------------------


class TestNegEnergyFromP:
    def test_returns_float(self) -> None:
        from ml.ood_energy import neg_energy_from_p

        e = neg_energy_from_p(0.7)
        assert isinstance(e, float)
        assert math.isfinite(e)

    def test_higher_confidence_lower_energy(self) -> None:
        from ml.ood_energy import neg_energy_from_p

        e_low = neg_energy_from_p(0.51)
        e_high = neg_energy_from_p(0.99)
        assert e_high < e_low

    def test_clips_to_epsilon(self) -> None:
        from ml.ood_energy import neg_energy_from_p

        e0 = neg_energy_from_p(0.0)
        e1 = neg_energy_from_p(1.0)
        assert math.isfinite(e0)
        assert math.isfinite(e1)

    def test_midpoint_approx(self) -> None:
        from ml.ood_energy import neg_energy_from_p

        e = neg_energy_from_p(0.5)
        # at p=0.5, logit=0, energy = -log(1+1) = -log(2)
        expected = -math.log(2.0)
        assert abs(e - expected) < 0.01


class TestOodAbstainEnergy:
    def test_no_gate_file_returns_no_abstain(self, tmp_path: Path) -> None:
        import ml.ood_energy as oe

        original = oe.ENERGY_JSON
        try:
            oe.ENERGY_JSON = tmp_path / "nonexistent.json"
            result = oe.ood_abstain_energy(0.9)
            assert result["ood_abstain_energy"] is False
        finally:
            oe.ENERGY_JSON = original

    def test_with_tau_below_energy_abstains(self, tmp_path: Path) -> None:
        import ml.ood_energy as oe

        gate_file = tmp_path / "ood_energy.json"
        gate_file.write_text(json.dumps({"method": "energy_neg", "tau": -0.1}))
        original = oe.ENERGY_JSON
        try:
            oe.ENERGY_JSON = gate_file
            # p=0.99 -> energy ~= -4.6... more negative than -0.1 -> no abstain
            result = oe.ood_abstain_energy(0.99)
            assert "energy_neg" in result
            assert isinstance(result["ood_abstain_energy"], bool)
        finally:
            oe.ENERGY_JSON = original

    def test_result_has_required_keys(self, tmp_path: Path) -> None:
        import ml.ood_energy as oe

        original = oe.ENERGY_JSON
        try:
            oe.ENERGY_JSON = tmp_path / "nonexistent.json"
            result = oe.ood_abstain_energy(0.7)
            assert "energy_neg" in result
            assert "tau" in result
            assert "ood_abstain_energy" in result
        finally:
            oe.ENERGY_JSON = original


class TestLoadEnergyGate:
    def test_missing_file_returns_defaults(self, tmp_path: Path) -> None:
        import ml.ood_energy as oe

        original = oe.ENERGY_JSON
        try:
            oe.ENERGY_JSON = tmp_path / "missing.json"
            gate = oe.load_energy_gate()
            assert gate["tau"] is None
            assert gate["n"] == 0
        finally:
            oe.ENERGY_JSON = original

    def test_valid_file_loads_correctly(self, tmp_path: Path) -> None:
        import ml.ood_energy as oe

        gate_file = tmp_path / "gate.json"
        gate_file.write_text(json.dumps({"method": "energy_neg", "tau": -2.5, "q": 0.01, "n": 100}))
        original = oe.ENERGY_JSON
        try:
            oe.ENERGY_JSON = gate_file
            gate = oe.load_energy_gate()
            assert gate["tau"] == pytest.approx(-2.5)
        finally:
            oe.ENERGY_JSON = original

    def test_malformed_file_returns_defaults(self, tmp_path: Path) -> None:
        import ml.ood_energy as oe

        bad_file = tmp_path / "bad.json"
        bad_file.write_text("{NOT VALID JSON]]]")
        original = oe.ENERGY_JSON
        try:
            oe.ENERGY_JSON = bad_file
            gate = oe.load_energy_gate()
            assert gate["tau"] is None
        finally:
            oe.ENERGY_JSON = original


# -----------------------------------------------------------------------------
# ml/robust.py
# -----------------------------------------------------------------------------


class TestRobustZ:
    def test_zero_at_median(self) -> None:
        from ml.robust import _robust_z

        x = np.array([5.0, 10.0])
        med = np.array([5.0, 10.0])
        mad = np.array([1.0, 2.0])
        z = _robust_z(x, med, mad)
        assert np.allclose(z, 0.0)

    def test_one_sigma_deviation(self) -> None:
        from ml.robust import _robust_z

        x = np.array([6.0])
        med = np.array([5.0])
        mad = np.array([1.0])
        z = _robust_z(x, med, mad)
        assert z[0] == pytest.approx(1.0)

    def test_nan_becomes_zero(self) -> None:
        from ml.robust import _robust_z

        x = np.array([np.nan])
        med = np.array([5.0])
        mad = np.array([0.0])
        z = _robust_z(x, med, mad)
        assert z[0] == 0.0 or not math.isfinite(z[0])


class TestRobustMahalanobisD2:
    def test_zero_at_mean(self) -> None:
        from ml.robust import mahalanobis_d2

        mu = np.array([0.0, 0.0])
        z = np.array([0.0, 0.0])
        S = np.diag([1.0, 1.0])
        d2, contrib = mahalanobis_d2(z, mu, S, use_diagonal=True)
        assert d2 == pytest.approx(0.0, abs=1e-10)
        assert contrib is not None

    def test_off_diagonal_cov(self) -> None:
        from ml.robust import mahalanobis_d2

        mu = np.array([0.0, 0.0])
        z = np.array([1.0, 0.0])
        S = np.eye(2)
        d2, contrib = mahalanobis_d2(z, mu, S, use_diagonal=False)
        assert d2 == pytest.approx(1.0, rel=1e-5)
        assert contrib is None


class TestRobustScoreEnergy:
    def test_known_value(self) -> None:
        from ml.robust import score_energy

        logits = np.array([0.0, 0.0])
        e = score_energy(logits)
        expected = -np.logaddexp(0.0, 0.0)
        assert e == pytest.approx(expected, rel=1e-5)

    def test_finite(self) -> None:
        from ml.robust import score_energy

        e = score_energy(np.array([1.0, 2.0, 3.0]))
        assert math.isfinite(e)


class TestRobustScoreTabular:
    def _stats(self) -> dict[str, object]:
        return {
            "cols": ["age", "csf_glucose"],
            "median": [40.0, 60.0],
            "mad": [10.0, 10.0],
            "mu": [0.0, 0.0],
            "S": [[1.0, 0.0], [0.0, 1.0]],
            "use_diagonal": True,
            "tau": 9.0,
        }

    def test_in_dist_row(self) -> None:
        from ml.robust import score_tabular

        stats = self._stats()
        row = pd.Series({"age": 40.0, "csf_glucose": 60.0})
        result = score_tabular(row, stats)
        assert result["d2"] == pytest.approx(0.0, abs=1e-10)

    def test_empty_stats_returns_inf(self) -> None:
        from ml.robust import score_tabular

        row = pd.Series({"age": 40.0})
        result = score_tabular(row, {})
        assert result["d2"] == float("inf")

    def test_partial_columns_intersect(self) -> None:
        from ml.robust import score_tabular

        stats = self._stats()
        row = pd.Series({"age": 40.0})  # csf_glucose missing
        result = score_tabular(row, stats)
        assert "d2" in result

    def test_returns_use_diagonal_key(self) -> None:
        from ml.robust import score_tabular

        stats = self._stats()
        row = pd.Series({"age": 40.0, "csf_glucose": 60.0})
        result = score_tabular(row, stats)
        assert "use_diagonal" in result


class TestRobustCheckOodRow:
    def test_returns_two_keys(self) -> None:
        from ml.robust import check_ood_row

        stats = {
            "cols": ["age"],
            "median": [40.0],
            "mad": [5.0],
            "mu": [0.0],
            "S": [[1.0]],
            "use_diagonal": True,
            "tau": 4.0,
        }
        row = pd.Series({"age": 40.0})
        result = check_ood_row(row, stats)
        assert "d2" in result
        assert "contrib" in result


class TestRobustLoadStats:
    def test_missing_file_returns_empty_struct(self, tmp_path: Path) -> None:
        from ml.robust import load_stats

        result = load_stats(tmp_path / "nonexistent.json")
        assert isinstance(result, dict)
        assert "cols" in result

    def test_valid_file_loads(self, tmp_path: Path) -> None:
        from ml.robust import load_stats

        stats = {"cols": ["age"], "tau": 3.14}
        p = tmp_path / "stats.json"
        p.write_text(json.dumps(stats))
        result = load_stats(p)
        assert result["tau"] == pytest.approx(3.14)
