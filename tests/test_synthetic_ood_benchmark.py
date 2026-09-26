"""
The synthetic OOD benchmark must score each gate and the neg-energy signal
the way inference applies them: a row is flagged when its score is above the
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
    # Asymmetric counts, plus one in-distribution row exactly at tau, which
    # inference does not flag (d2 <= tau is in-distribution; the energy gates
    # flag only a score > tau).
    rows_in = _rows(
        [(1.0, -8.0, -2.0), (2.0, -7.0, -1.5), (3.0, -6.0, -1.0), (5.0, -3.0, -0.5), (6.0, -2.0, -0.1)], 0
    )
    rows_out = _rows([(9.0, -1.0, -0.1), (8.0, -2.0, -0.2), (4.0, -4.0, -1.0)], 1)
    out = bench.evaluate(rows_in, rows_out, _TAUS)
    for gate in ("mahalanobis_d2", "logit_energy", "neg_energy"):
        # s > tau flags 2 of 3 shifted rows and 1 of 5 bundled rows; s >= tau
        # would give a false-alarm rate of 0.4, s < tau 1/3 and 0.6.
        assert out[gate]["detection_rate"] == pytest.approx(2 / 3), gate
        assert out[gate]["false_alarm_rate"] == pytest.approx(0.2), gate
        assert out[gate]["tau"] == _TAUS[gate]
