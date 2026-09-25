from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np
import numpy.typing as npt

from ml.config import conformal_alpha, parse_alpha
from ml.conformal_advanced import compute_qhat, qhat_to_json

MET = Path("outputs/metrics")
MOD = Path("outputs/model")


def _load_T() -> float:
    for p in [MOD/"temperature_scale.json", MET/"temperature_scale.json"]:
        if p.exists():
            return float(json.loads(p.read_text())["T"])
    raise FileNotFoundError("temperature_scale.json not found in outputs/model or outputs/metrics")


def _softmax(z: npt.NDArray[np.floating[object]]) -> npt.NDArray[np.floating[object]]:  # type: ignore[type-var]
    z = z - z.max(axis=1, keepdims=True)
    ez = np.exp(z)
    return ez / ez.sum(axis=1, keepdims=True)  # type: ignore[no-any-return]


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--alpha", type=parse_alpha, default=None)
    args = ap.parse_args()
    alpha = args.alpha if args.alpha is not None else conformal_alpha()

    logits_p = MET / "val_logits.npy"
    y_p      = MET / "val_y.npy"
    if not (logits_p.exists() and y_p.exists()):
        raise FileNotFoundError("Missing outputs/metrics/val_logits.npy or val_y.npy. Re-run your calib script to export them.")

    T = _load_T()
    logits = np.load(logits_p)
    y = np.load(y_p).astype(int)
    p = _softmax(logits / T)

    s = 1.0 - p[np.arange(len(y)), y]  # nonconformity
    n = len(s)
    qhat = compute_qhat(s, alpha=alpha)

    out = {"alpha": float(alpha), "qhat": qhat_to_json(qhat), "n_calib": int(n)}
    (MET / "conformal.json").write_text(json.dumps(out, indent=2))
    print(json.dumps(out, indent=2))

if __name__ == "__main__":
    main()
