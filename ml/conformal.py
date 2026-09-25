from typing import Tuple

LABELS = ("Low", "High")

def set_from_p_high(p_high: float, qhat: float) -> Tuple[bool, bool]:
    include_high = p_high >= (1.0 - qhat)
    include_low  = p_high <= qhat
    return (include_low, include_high)

def is_abstention(include_low: bool, include_high: bool) -> bool:
    """True when the prediction set is empty or holds both classes; only a one-class set yields a label."""
    return include_low == include_high

def decision_from_p_high(p_high: float, qhat: float) -> str:
    low, high = set_from_p_high(p_high, qhat)
    if is_abstention(low, high):
        return "ABSTAIN"
    return "High" if high else "Low"
