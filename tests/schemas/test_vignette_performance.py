"""Performance benchmark for VignetteSchema validation.

Asserts P99 < 5ms per validation on canonical fixture.
Critical for production: ML training loops validate thousands of vignettes per epoch.
"""
from __future__ import annotations

import json
import time
from pathlib import Path

from ml.schemas.vignette import VignetteSchema

FIXTURE = Path(__file__).parent / "fixtures" / "valid_pam_fixture.json"
N_ITERATIONS = 1000
P99_THRESHOLD_MS = 5.0


def test_validation_p99_under_5ms() -> None:
    """Validate 1000 times; assert P99 < 5ms."""
    raw = json.loads(FIXTURE.read_text())
    times_ns: list[int] = []
    for _ in range(N_ITERATIONS):
        t0 = time.perf_counter_ns()
        VignetteSchema.model_validate(raw)
        times_ns.append(time.perf_counter_ns() - t0)

    times_ms = [t / 1_000_000 for t in times_ns]
    times_ms.sort()
    p50 = times_ms[N_ITERATIONS // 2]
    p95 = times_ms[int(N_ITERATIONS * 0.95)]
    p99 = times_ms[int(N_ITERATIONS * 0.99)]

    print(f"\nValidation latency over {N_ITERATIONS} iterations:")
    print(f"  P50: {p50:.4f} ms")
    print(f"  P95: {p95:.4f} ms")
    print(f"  P99: {p99:.4f} ms")
    print(f"  Threshold: {P99_THRESHOLD_MS} ms")

    assert p99 < P99_THRESHOLD_MS, (
        f"P99 {p99:.4f} ms exceeds threshold {P99_THRESHOLD_MS} ms"
    )
