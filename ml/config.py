"""Project settings read from config/amoebanator.toml."""
from __future__ import annotations

import tomllib
from fractions import Fraction
from functools import lru_cache
from pathlib import Path
from typing import Any

CONFIG_PATH: Path = Path(__file__).resolve().parent.parent / "config" / "amoebanator.toml"

# Largest denominator tried when reading a float as a simple fraction.
_MAX_DENOMINATOR: int = 10**6


def parse_alpha(value: str | float | Fraction) -> Fraction:
    """
    Parse a miscoverage level into an exact fraction in (0, 1).

    Strings such as "1/7" or "0.1" are parsed exactly. A float counts as a
    simple fraction only when it is the nearest double to that fraction, so
    1/7 computed in floating point is exactly 1/7; any other float keeps its
    exact binary value, and rounding never moves it across a rank boundary.
    """
    try:
        if isinstance(value, Fraction):
            alpha = value
        elif isinstance(value, str):
            alpha = Fraction(value.strip())
        else:
            x = float(value)
            exact = Fraction(x)
            snapped = exact.limit_denominator(_MAX_DENOMINATOR)
            alpha = snapped if float(snapped) == x else exact
    except (ValueError, ZeroDivisionError, OverflowError) as e:
        raise ValueError(f"alpha must be a number or a fraction such as 1/7; got {value!r}.") from e
    if not (0 < alpha < 1):
        raise ValueError(f"alpha must lie in (0, 1); got {value!r}.")
    return alpha


@lru_cache(maxsize=1)
def _load() -> dict[str, Any]:
    return tomllib.loads(CONFIG_PATH.read_text())


def conformal_alpha() -> Fraction:
    """The demo's split-conformal miscoverage level, from [conformal] alpha."""
    section = _load().get("conformal", {})
    if "alpha" not in section:
        raise KeyError(f"{CONFIG_PATH} has no [conformal] alpha setting.")
    return parse_alpha(section["alpha"])
