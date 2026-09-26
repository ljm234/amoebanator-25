"""
The synthetic OOD benchmark must score each gate the way inference applies
it: a higher score is more OOD, and the gate flags a score above its
threshold. A sign flip here would report an inverted AUC.
"""
from __future__ import annotations

import pytest

import scripts.ood.synthetic_ood_benchmark as bench

_TAUS = {"mahalanobis_d2": 5.0, "logit_energy": -3.0, "neg_energy": -0.5}


def _rows(values: list[tuple[float, float, float]], is_ood: int) -> list[dict[str, float]]:
    return [
        {"mahalanobis_d2": d2, "logit_energy": e, "neg_energy": ne, "is_ood": float(is_ood)}
        for d2, e, ne in values
    ]


def test_higher_scores_on_shifted_rows_give_auc_one() -> None:
    rows_in = _rows([(1.0, -8.0, -2.0), (2.0, -7.0, -1.5)], 0)
    rows_out = _rows([(9.0, -1.0, -0.1), (8.0, -2.0, -0.2)], 1)
    out = bench.evaluate(rows_in, rows_out, _TAUS)
    for gate in ("mahalanobis_d2", "logit_energy", "neg_energy"):
        assert out[gate]["auc"] == pytest.approx(1.0), gate


def test_rates_are_taken_at_the_gate_threshold() -> None:
    rows_in = _rows([(1.0, -8.0, -2.0), (6.0, -2.0, -0.1)], 0)
    rows_out = _rows([(9.0, -1.0, -0.1), (4.0, -4.0, -1.0)], 1)
    out = bench.evaluate(rows_in, rows_out, _TAUS)
    for gate in ("mahalanobis_d2", "logit_energy", "neg_energy"):
        assert out[gate]["detection_rate"] == pytest.approx(0.5), gate
        assert out[gate]["false_alarm_rate"] == pytest.approx(0.5), gate
        assert out[gate]["tau"] == _TAUS[gate]
