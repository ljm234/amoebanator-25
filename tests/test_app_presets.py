"""Tests for app/presets.py.

20 tests: 5 parametrized x 3 presets + 1 xfail-decorated bacterial
regression + 4 cross-preset invariants. The xfail decorator uses
``strict=False`` so a future MIMIC-IV cohort success -> XPASS as a
"fix this" signal rather than CI breakage.
"""
from __future__ import annotations

import re

import pytest

from app.presets import PRESETS, load_preset
from app.utils import build_row


_PRESET_KEYS: tuple[str, ...] = (
    "high_risk_pam",
    "bacterial_meningitis_limitation",
    "normal_csf",
)


# --- Per-preset parametrized (5 x 3 = 15 tests) ----------------------

@pytest.mark.parametrize("preset_key", _PRESET_KEYS)
def test_preset_dict_has_all_required_fields(preset_key: str) -> None:
    """Pinned schema."""
    p = PRESETS[preset_key]
    required = {"label", "description", "inputs", "current_behavior", "limitation_banner"}
    assert required.issubset(p.keys()), (
        f"{preset_key} missing fields: {required - p.keys()}"
    )


@pytest.mark.parametrize("preset_key", _PRESET_KEYS)
def test_preset_inputs_has_all_8_features(preset_key: str) -> None:
    expected = {
        "age", "csf_glucose", "csf_protein", "csf_wbc",
        "pcr", "microscopy", "exposure", "symptoms",
    }
    inputs = PRESETS[preset_key]["inputs"]
    assert set(inputs.keys()) == expected


@pytest.mark.parametrize("preset_key", _PRESET_KEYS)
def test_preset_current_behavior_has_snapshot_date(preset_key: str) -> None:
    """Field rename: current_behavior (NOT expected) +
    snapshot_date pinned to 2026-04-26."""
    cb = PRESETS[preset_key]["current_behavior"]
    assert cb["snapshot_date"] == "2026-04-26"
    assert "prediction" in cb
    assert "p_high_approx" in cb


@pytest.mark.parametrize("preset_key", _PRESET_KEYS)
def test_preset_load_populates_form(preset_key: str) -> None:
    """``load_preset`` returns the dict; verify build_row accepts inputs."""
    p = load_preset(preset_key)
    inputs = p["inputs"]
    row = build_row(
        age=inputs["age"],
        csf_glucose=inputs["csf_glucose"],
        csf_protein=inputs["csf_protein"],
        csf_wbc=inputs["csf_wbc"],
        pcr=inputs["pcr"],
        microscopy=inputs["microscopy"],
        exposure=inputs["exposure"],
        symptoms=inputs["symptoms"],
    )
    assert isinstance(row, dict)
    assert row["age"] == inputs["age"]


@pytest.mark.parametrize("preset_key", _PRESET_KEYS)
def test_preset_live_snapshot_matches(preset_key: str) -> None:
    """Live snapshot: actual infer_one output matches current_behavior.

    For ``bacterial_meningitis_limitation`` this currently passes
    because the model returns 'High' (the known limitation). A model
    that returns 'Low' for it fails this test, and the xfail-decorated
    test below then reports XPASS.
    """
    from ml.infer import infer_one
    p = PRESETS[preset_key]
    inputs = p["inputs"]
    row = build_row(
        age=inputs["age"],
        csf_glucose=inputs["csf_glucose"],
        csf_protein=inputs["csf_protein"],
        csf_wbc=inputs["csf_wbc"],
        pcr=inputs["pcr"],
        microscopy=inputs["microscopy"],
        exposure=inputs["exposure"],
        symptoms=inputs["symptoms"],
    )
    out = infer_one(row)
    assert out["prediction"] == p["current_behavior"]["prediction"]


# --- Special xfail bacterial regression (1 test) ---------------------

@pytest.mark.xfail(
    strict=False,
    reason=(
        "Known limitation: the bacterial_meningitis_limitation preset is "
        "predicted 'High' because the 30-row synthetic dataset contains no "
        "bacterial meningitis that is not PAM. A model trained on a real "
        "cohort should predict 'Low' here; the test then reports XPASS, and "
        "the xfail marker and the preset's current_behavior should be updated."
    ),
)
def test_bacterial_preset_predicts_low() -> None:
    """The limitation above, as a test. strict=False, so a model that
    predicts 'Low' shows up as XPASS without failing CI."""
    from ml.infer import infer_one
    p = PRESETS["bacterial_meningitis_limitation"]
    inputs = p["inputs"]
    row = build_row(
        age=inputs["age"],
        csf_glucose=inputs["csf_glucose"],
        csf_protein=inputs["csf_protein"],
        csf_wbc=inputs["csf_wbc"],
        pcr=inputs["pcr"],
        microscopy=inputs["microscopy"],
        exposure=inputs["exposure"],
        symptoms=inputs["symptoms"],
    )
    out = infer_one(row)
    # The current model predicts 'High' for this preset; see the xfail reason.
    assert out["prediction"] == "Low"


# --- Cross-preset invariants (4 tests) -------------------------------

def test_three_presets_total_count() -> None:
    assert len(PRESETS) == 3


def test_preset_keys_are_snake_case() -> None:
    pattern = re.compile(r"^[a-z][a-z0-9_]*$")
    for k in PRESETS:
        assert pattern.match(k), f"key {k!r} not snake_case"


def test_only_bacterial_has_limitation_banner_true() -> None:
    """The limitation_banner is True for exactly the bacterial preset."""
    flagged = [k for k, p in PRESETS.items() if p["limitation_banner"]]
    assert flagged == ["bacterial_meningitis_limitation"]


def test_all_presets_have_snapshot_date_2026_04_26() -> None:
    for key, p in PRESETS.items():
        assert p["current_behavior"]["snapshot_date"] == "2026-04-26", (
            f"{key} snapshot_date drifted"
        )
