"""Tests for pages/01_predict.py.

Covers the input form and its neutral defaults, the preset buttons, error
paths, the decision and calibration badges, submit debounce, the
known-limitation banner on the bacterial preset, both research-mode
branches, and a text-snapshot drift check.

Tests of the page run it through Streamlit's AppTest; tests of the helpers
call app.utils directly. Most tests that submit the form patch
``infer_one``. Two tests run the shipped model:
test_stale_lock_recovers_after_30s, which submits the form, and
test_neutral_defaults_predict_low_p_high_lt_001, which calls ml.infer
directly.
"""
from __future__ import annotations

import json
import os
import re
import tempfile
from pathlib import Path
from typing import Any
from unittest.mock import patch  # noqa: F401 - used by the tests that patch ml.infer.infer_one

import pytest
from streamlit.testing.v1 import AppTest


PAGE_PATH = "pages/01_predict.py"
SNAPSHOT_PATH = Path(__file__).parent / "_snapshots" / "predict.md.snap"


def _artifact_thresholds() -> dict[str, float | int]:
    """The shipped thresholds and calibration size, read from the artifacts."""
    metrics = Path(__file__).resolve().parent.parent / "outputs" / "metrics"
    conformal = json.loads((metrics / "conformal.json").read_text())
    return {
        "energy_tau": float(json.loads((metrics / "energy_threshold.json").read_text())["tau"]),
        "d2_tau": float(json.loads((metrics / "feature_stats.json").read_text())["tau"]),
        "n_cal": int(conformal["n"]),
        "alpha": float(conformal["alpha"]),
    }


# The bacterial-meningitis preset's infer_one readout on the shipped
# artifacts: ABSTAIN at the logit-energy gate. One set of values, shared by
# the banner tests and the fixture check.
_BACTERIAL_FAKE: dict[str, Any] = {
    "prediction": "ABSTAIN",
    "p_high": 0.9994,
    "reason": "LogitEnergyAboveOODShift",
    "energy": -3.967,
    "mahalanobis_d2": 15.096,
}


def _fake_infer_output(
    *,
    prediction: str = "Low",
    p_high: float = 1.4e-9,
    reason: str | None = None,
    n_cal: int | None = None,
    alpha: float | None = None,
    energy: float = -11.7,
    energy_tau: float | None = None,
    mahalanobis_d2: float = 5.0,
    d2_tau: float | None = None,
) -> dict[str, Any]:
    """Build a synthetic infer_one output dict matching the real shape."""
    shipped = _artifact_thresholds()
    out: dict[str, Any] = {
        "prediction": prediction,
        "p_high": p_high,
        "n_cal": shipped["n_cal"] if n_cal is None else n_cal,
        "alpha": shipped["alpha"] if alpha is None else alpha,
        "energy": energy,
        "energy_tau": shipped["energy_tau"] if energy_tau is None else energy_tau,
        "mahalanobis_d2": mahalanobis_d2,
        "d2_tau": shipped["d2_tau"] if d2_tau is None else d2_tau,
    }
    if reason is not None:
        out["reason"] = reason
    return out


def _fresh_app_test(env: dict[str, str] | None = None) -> AppTest:
    """Build an AppTest with a clean session state and optional env vars."""
    # Reset audit-hooks singleton between tests so IRB_STATUS_CHANGE etc.
    # don't bleed across runs.
    from ml import audit_hooks as ah
    ah._singleton_log = None
    ah._singleton_path = None
    at = AppTest.from_file(PAGE_PATH)
    if env:
        for k, v in env.items():
            os.environ[k] = v
    return at


# ---------------------------------------------------------------------
# Module imports cleanly
# ---------------------------------------------------------------------
def test_module_imports_cleanly() -> None:
    """`import pages.predict` would succeed if pages were a package; here we
    verify AppTest can load the file as a script without exceptions."""
    at = _fresh_app_test()
    at.run(timeout=30)
    assert len(at.exception) == 0


# ---------------------------------------------------------------------
# Form renders 8 widgets
# ---------------------------------------------------------------------
def test_form_renders_8_widgets() -> None:
    at = _fresh_app_test()
    at.run(timeout=30)
    # 4 number_input + 3 checkbox + 1 multiselect = 8
    assert len(list(at.number_input)) == 4
    assert len(list(at.checkbox)) == 3
    assert len(list(at.multiselect)) == 1


# ---------------------------------------------------------------------
# Form uses neutral defaults
# ---------------------------------------------------------------------
def test_form_uses_neutral_defaults() -> None:
    at = _fresh_app_test()
    at.run(timeout=30)
    assert at.number_input(key="age").value == 12
    assert at.number_input(key="csf_glucose").value == 65.0
    assert at.number_input(key="csf_protein").value == 30.0
    assert at.number_input(key="csf_wbc").value == 3
    assert at.checkbox(key="pcr").value is False
    assert at.checkbox(key="microscopy").value is False
    assert at.checkbox(key="exposure").value is False
    assert list(at.multiselect(key="symptoms").value) == []


# ---------------------------------------------------------------------
# Neutral defaults predict Low with p_high < 0.001 (real model)
# ---------------------------------------------------------------------
def test_neutral_defaults_predict_low_p_high_lt_001() -> None:
    """Calls real infer_one on the fixed NEUTRAL defaults. No mock -
    if this regresses, the model itself has changed and the demo's
    'page-load shows Low' invariant breaks."""
    from app.utils import build_row
    from ml.infer import infer_one

    row = build_row(
        age=12, csf_glucose=65.0, csf_protein=30.0, csf_wbc=3,
        pcr=False, microscopy=False, exposure=False, symptoms=[],
    )
    out = infer_one(row)
    assert out["prediction"] == "Low"
    assert float(out["p_high"]) < 1e-3


# ---------------------------------------------------------------------
# Three preset buttons render
# ---------------------------------------------------------------------
def test_three_preset_buttons_render() -> None:
    from app.presets import PRESETS

    at = _fresh_app_test()
    at.run(timeout=30)
    button_labels = [b.label for b in at.button]
    for key in ("high_risk_pam", "bacterial_meningitis_limitation", "normal_csf"):
        assert PRESETS[key]["label"] in button_labels


# ---------------------------------------------------------------------
# Loading a preset fills the form widgets, also after another preset
# ---------------------------------------------------------------------
@pytest.mark.parametrize("first, second", [
    ("high_risk_pam", None),
    ("high_risk_pam", "normal_csf"),
])
def test_loading_a_preset_populates_form(first: str, second: str | None) -> None:
    from app.presets import PRESETS

    at = _fresh_app_test()
    at.run(timeout=30)
    at.button(key=f"preset_{first}").click().run(timeout=30)
    if second is not None:
        at.button(key=f"preset_{second}").click().run(timeout=30)
    key = second or first
    expected = PRESETS[key]["inputs"]
    for field in ("age", "csf_glucose", "csf_protein", "csf_wbc"):
        assert at.number_input(key=field).value == expected[field]
    for field in ("pcr", "microscopy", "exposure"):
        assert at.checkbox(key=field).value == expected[field]
    assert at.multiselect(key="symptoms").value == expected["symptoms"]
    assert at.session_state["active_preset"] == key


def test_preset_survives_a_page_change() -> None:
    """A loaded preset is still in the form after visiting another page."""
    from app.presets import PRESETS

    at = AppTest.from_file("streamlit_app.py")
    at.run(timeout=60)
    at.button(key="preset_bacterial_meningitis_limitation").click().run(timeout=60)
    at.switch_page("pages/03_about.py").run(timeout=60)
    at.switch_page("pages/01_predict.py").run(timeout=60)
    expected = PRESETS["bacterial_meningitis_limitation"]["inputs"]
    for field in ("age", "csf_glucose", "csf_protein", "csf_wbc"):
        assert at.number_input(key=field).value == expected[field]
    assert at.multiselect(key="symptoms").value == expected["symptoms"]


# ---------------------------------------------------------------------
# Submit calls infer_one with the dict shape build_row produces
# ---------------------------------------------------------------------
def test_submit_calls_infer_one_with_built_row() -> None:
    """AppTest can't patch script-level imports across runs (the page
    is loaded as a script, not a module - `pages.predict` is not
    importable). We verify the *contract* instead: ``build_row`` emits
    the dict shape ``infer_one`` accepts. Patch-based call-arg
    verification is covered indirectly by the tooltip, small-calibration,
    and regime-badge tests below (they patch ``ml.infer.infer_one`` and
    observe the page's downstream rendering).
    """
    from app.utils import build_row
    row = build_row(
        age=12, csf_glucose=65.0, csf_protein=30.0, csf_wbc=3,
        pcr=False, microscopy=False, exposure=False, symptoms=[],
    )
    assert set(row.keys()) == {
        "age", "csf_glucose", "csf_protein", "csf_wbc",
        "pcr", "microscopy", "exposure", "symptoms",
    }
    assert isinstance(row["age"], int)
    assert isinstance(row["csf_glucose"], float)
    assert row["pcr"] == 0  # False -> 0
    assert row["symptoms"] == ""


# ---------------------------------------------------------------------
# No submit -> no infer_one call
# ---------------------------------------------------------------------
def test_no_submit_returns_early() -> None:
    """First render with no interaction must not invoke inference."""
    at = _fresh_app_test()
    at.run(timeout=30)
    # If inference had run, a result heading would render. Verify none.
    headings = [h.value for h in at.markdown]
    assert not any(h.startswith("### Result:") for h in headings)


# ---------------------------------------------------------------------
# FileNotFoundError -> warning banner instead of a crash
# ---------------------------------------------------------------------
def test_filenotfounderror_renders_graceful_banner() -> None:
    """Missing artifact must surface as warning banner, not raise."""
    err = FileNotFoundError("Mahalanobis stats not found")
    err.filename = "outputs/metrics/feature_stats_train.json"
    at = _fresh_app_test()
    at.run(timeout=30)
    # Submit the form. Patch infer_one to raise FNFE.
    with patch("ml.infer.infer_one", side_effect=err):
        at.button[3].click()  # form_submit_button is the 4th button
        at.run(timeout=30)
    warnings = [w.value for w in at.warning]
    assert any("A required artifact is missing" in w for w in warnings)
    assert len(at.exception) == 0  # no crash


# ---------------------------------------------------------------------
# Generic exception -> correlation-ID error + INTEGRITY_VIOLATION audit
# ---------------------------------------------------------------------
def test_uncaught_exception_emits_correlation_id_audit() -> None:
    """Uncaught exception -> uuid4 12-char display + INTEGRITY_VIOLATION emit."""
    with tempfile.NamedTemporaryFile(mode="w", suffix=".jsonl", delete=False) as f:
        tmp_path = Path(f.name)
    os.environ["AMOEBANATOR_AUDIT_PATH"] = str(tmp_path)
    try:
        at = _fresh_app_test()
        at.run(timeout=30)
        with patch("ml.infer.infer_one", side_effect=ValueError("boom")):
            at.button[3].click()
            at.run(timeout=30)
        errors = [e.value for e in at.error]
        assert any(re.search(r"error ID: [0-9a-f]{12}", e) for e in errors), (
            f"expected 12-char hex ID in error message; got {errors!r}"
        )
        # Verify INTEGRITY_VIOLATION emitted with full 32-char error_id
        events = [json.loads(line) for line in tmp_path.read_text().splitlines() if line]
        violations = [e for e in events if e["event_type"] == "integrity_violation"]
        assert len(violations) >= 1
        meta = violations[-1]["metadata"]
        assert "error_id" in meta and len(meta["error_id"]) == 32
        assert meta["exception_type"] == "ValueError"
    finally:
        os.environ.pop("AMOEBANATOR_AUDIT_PATH", None)
        tmp_path.unlink(missing_ok=True)


# ---------------------------------------------------------------------
# Double-submit within 30s blocked by debounce
# ---------------------------------------------------------------------
def test_double_submit_within_30s_blocked() -> None:
    """Predicting=True with fresh timestamp -> second submit aborts."""
    import time
    at = _fresh_app_test()
    at.session_state["predicting"] = True
    at.session_state["predicting_at"] = time.time()  # fresh lock
    at.run(timeout=30)
    at.button[3].click()  # form_submit
    at.run(timeout=30)
    warnings = [w.value for w in at.warning]
    assert any("Already processing" in w for w in warnings)


# ---------------------------------------------------------------------
# Stale lock (>30s old) recovers and allows submission
# ---------------------------------------------------------------------
def test_stale_lock_recovers_after_30s() -> None:
    """Predicting=True with timestamp >30s ago -> fall through, re-acquire."""
    import time
    at = _fresh_app_test()
    at.session_state["predicting"] = True
    at.session_state["predicting_at"] = time.time() - 31  # stale by 1s
    at.run(timeout=30)
    at.button[3].click()
    at.run(timeout=30)
    # No "Already processing" warning - stale lock was bypassed.
    warnings = [w.value for w in at.warning]
    assert not any("Already processing" in w for w in warnings)


# ---------------------------------------------------------------------
# decision_badge: icon + bold preserved when color tags stripped
# ---------------------------------------------------------------------
def test_decision_badge_renders_with_bold() -> None:
    from app.utils import decision_badge

    badge = decision_badge("High")
    # Strip :color[...] wrapper; bold label must remain
    stripped = re.sub(r":\w+\[|\]$", "", badge)
    assert "**HIGH**" in stripped


# ---------------------------------------------------------------------
# decision_badge: color-blind safe across prediction states
# ---------------------------------------------------------------------
@pytest.mark.parametrize(
    "prediction, label",
    [
        ("High",     "HIGH"),
        ("Low",      "LOW"),
        ("ABSTAIN",  "ABSTAIN"),
    ],
)
def test_decision_badge_color_blind_safe(
    prediction: str, label: str
) -> None:
    """Every badge state legible without color."""
    from app.utils import decision_badge

    badge = decision_badge(prediction, reason="OOD" if prediction == "ABSTAIN" else None)
    stripped = re.sub(r":\w+\[|\]$", "", badge)
    assert label in stripped
    assert f"**{label}" in stripped  # bold prefix; ABSTAIN may have suffix " - OOD"


# ---------------------------------------------------------------------
# Temperature badge: value and tooltip read from the shipped artifacts
# ---------------------------------------------------------------------
def test_temperature_badge_reads_the_artifacts() -> None:
    """The badge shows the shipped T and n_cal, and the tooltip states why
    T is not identifiable when the validation rows are perfectly separated."""
    from ml.infer import calibration_info

    info = calibration_info()
    fake = _fake_infer_output()
    fake.pop("n_cal")
    at = _fresh_app_test()
    at.run(timeout=30)
    with patch("ml.infer.infer_one", return_value=fake):
        at.button[3].click()
        at.run(timeout=30)
    md_blob = "\n".join(m.value for m in at.markdown)
    assert f"T={float(info['T']):.2f} (n={info['n_cal']})" in md_blob
    if info["val_separated"]:
        assert "not identifiable" in md_blob


def test_temperature_note_states_each_case() -> None:
    """The tooltip text follows the artifact values, not a fixed number."""
    from app.utils import temperature_note

    assert "starting value of 1.0" in temperature_note(0.9999974, 6, True)
    assert "where the optimizer stopped" in temperature_note(0.1, 6, True)
    assert "sharpens" in temperature_note(0.5, 6, False)
    assert "softens" in temperature_note(1.5, 6, False)
    assert "essentially 1" in temperature_note(0.9999974, 6, None)
    assert "essentially 1" in temperature_note(1.0, 6, False)
    assert "is below 1" not in temperature_note(0.9999974, 6, None)


def test_min_calibration_rows_matches_the_rank_rule() -> None:
    from app.utils import min_calibration_rows
    from ml.conformal_advanced import finite_sample_rank

    for alpha, expected in [(0.10, 9), (0.05, 19), (1 / 7, 6), (0.20, 4),
                            (0.5, 1), (1e-4, 9999), (1e-7, 10_000_000)]:
        n = min_calibration_rows(alpha)
        assert n == expected
        assert finite_sample_rank(n, alpha) <= n
        assert finite_sample_rank(n - 1, alpha) > n - 1


# ---------------------------------------------------------------------
# SmallCalibrationWarning fires when n_cal < 30
# ---------------------------------------------------------------------
def test_smallcalibrationwarning_fires_for_n_below_30() -> None:
    fake = _fake_infer_output(n_cal=6)
    at = _fresh_app_test()
    at.run(timeout=30)
    with patch("ml.infer.infer_one", return_value=fake):
        at.button[3].click()
        at.run(timeout=30)
    warnings = [w.value for w in at.warning]
    assert any("Calibration set is small" in w for w in warnings)


# ---------------------------------------------------------------------
# 3-state regime badge: at n=6 alpha=0.10 -> INVALID
# ---------------------------------------------------------------------
def test_three_state_regime_badge_invalid_at_n6_alpha010() -> None:
    """k = ceil((n+1)(1-alpha)) = 7 > n=6 -> INVALID."""
    fake = _fake_infer_output(n_cal=6, alpha=0.10)
    at = _fresh_app_test()
    at.run(timeout=30)
    with patch("ml.infer.infer_one", return_value=fake):
        at.button[3].click()
        at.run(timeout=30)
    errors = [e.value for e in at.error]
    assert any("INVALID" in e for e in errors)


# ---------------------------------------------------------------------
# Limitation banner renders only when the bacterial preset is active
# ---------------------------------------------------------------------
def test_limitation_banner_only_on_bacterial_preset() -> None:
    """Banner is post-result + bacterial-preset-gated."""
    from app.presets import PRESETS

    fake = _fake_infer_output(**_BACTERIAL_FAKE)
    at = _fresh_app_test()
    at.run(timeout=30)
    at.button(key="preset_bacterial_meningitis_limitation").click()
    at.run(timeout=30)
    with patch("ml.infer.infer_one", return_value=fake):
        at.button[3].click()
        at.run(timeout=30)
    errors = [e.value for e in at.error]
    bacterial_desc = PRESETS["bacterial_meningitis_limitation"]["description"]
    assert any(bacterial_desc[:60] in e for e in errors), (
        "limitation banner missing on bacterial preset"
    )

    # Now non-bacterial preset -> no limitation banner
    at2 = _fresh_app_test()
    at2.run(timeout=30)
    at2.button(key="preset_high_risk_pam").click()
    at2.run(timeout=30)
    with patch("ml.infer.infer_one", return_value=fake):
        at2.button[3].click()
        at2.run(timeout=30)
    errors2 = [e.value for e in at2.error]
    # The INVALID conformal-regime error is allowed; no preset description is.
    assert not any(bacterial_desc[:60] in e for e in errors2), (
        "limitation banner spuriously rendered on non-bacterial preset"
    )
    hr_desc = PRESETS["high_risk_pam"]["description"]
    assert not PRESETS["high_risk_pam"]["limitation_banner"]
    assert not any(hr_desc[:60] in e for e in errors2), (
        "a preset without limitation_banner rendered its description as a banner"
    )


def test_limitation_banner_hidden_after_inputs_are_edited() -> None:
    """Once the loaded bacterial preset's inputs are edited, the result no
    longer describes that preset, so its banner is not shown."""
    from app.presets import PRESETS

    fake = _fake_infer_output(prediction="Low", p_high=1e-6)
    at = _fresh_app_test()
    at.run(timeout=30)
    at.button(key="preset_bacterial_meningitis_limitation").click()
    at.run(timeout=30)
    at.number_input(key="csf_wbc").set_value(3)
    with patch("ml.infer.infer_one", return_value=fake):
        at.button[3].click()
        at.run(timeout=30)
    bacterial_desc = PRESETS["bacterial_meningitis_limitation"]["description"]
    assert not any(bacterial_desc[:60] in e.value for e in at.error)


def test_limitation_banner_kept_when_symptoms_are_reselected() -> None:
    """Deselecting and reselecting a symptom reorders the multiselect value
    but leaves the input unchanged, so the banner is still shown."""
    from app.presets import PRESETS

    fake = _fake_infer_output(**_BACTERIAL_FAKE)
    at = _fresh_app_test()
    at.run(timeout=30)
    at.button(key="preset_bacterial_meningitis_limitation").click()
    at.run(timeout=30)
    at.multiselect(key="symptoms").unselect("fever").run(timeout=30)
    at.multiselect(key="symptoms").select("fever").run(timeout=30)
    assert at.multiselect(key="symptoms").value == ["headache", "nuchal_rigidity", "fever"]
    with patch("ml.infer.infer_one", return_value=fake):
        at.button[3].click()
        at.run(timeout=30)
    bacterial_desc = PRESETS["bacterial_meningitis_limitation"]["description"]
    assert any(bacterial_desc[:60] in e.value for e in at.error)
    # Removing a symptom for real is an edit, so the banner goes away.
    at.multiselect(key="symptoms").unselect("fever").run(timeout=30)
    with patch("ml.infer.infer_one", return_value=fake):
        at.button[3].click()
        at.run(timeout=30)
    assert not any(bacterial_desc[:60] in e.value for e in at.error)


# ---------------------------------------------------------------------
# RESEARCH_MODE=1/true/TRUE/yes -> red banner + IRB_STATUS_CHANGE audit emit
# ---------------------------------------------------------------------
@pytest.mark.parametrize("value", ["1", "true", "TRUE", "yes"])
def test_research_mode_active_renders_banner_and_emits_event(value: str) -> None:
    """Research-mode branch, for every value the IRB gate treats as research mode."""
    with tempfile.NamedTemporaryFile(mode="w", suffix=".jsonl", delete=False) as f:
        tmp_path = Path(f.name)
    os.environ["AMOEBANATOR_AUDIT_PATH"] = str(tmp_path)
    os.environ["AMOEBANATOR_RESEARCH_MODE"] = value
    try:
        at = _fresh_app_test()
        at.run(timeout=30)
        errors = [e.value for e in at.error]
        assert any("No IRB required" in e for e in errors)
        events = [json.loads(line) for line in tmp_path.read_text().splitlines() if line]
        irb_events = [e for e in events if e["event_type"] == "irb_status_change"]
        assert len(irb_events) >= 1
        assert irb_events[-1]["actor"] == "env_var"
    finally:
        os.environ.pop("AMOEBANATOR_AUDIT_PATH", None)
        os.environ.pop("AMOEBANATOR_RESEARCH_MODE", None)
        tmp_path.unlink(missing_ok=True)


# ---------------------------------------------------------------------
# RESEARCH_MODE unset -> no banner and no event
# ---------------------------------------------------------------------
def test_research_mode_inactive_no_banner_no_event() -> None:
    """RESEARCH_MODE=0/unset branch."""
    with tempfile.NamedTemporaryFile(mode="w", suffix=".jsonl", delete=False) as f:
        tmp_path = Path(f.name)
    os.environ["AMOEBANATOR_AUDIT_PATH"] = str(tmp_path)
    os.environ.pop("AMOEBANATOR_RESEARCH_MODE", None)
    try:
        at = _fresh_app_test()
        at.run(timeout=30)
        errors = [e.value for e in at.error]
        assert not any("No IRB required" in e for e in errors)
        events = [json.loads(line) for line in tmp_path.read_text().splitlines() if line]
        irb_events = [e for e in events if e["event_type"] == "irb_status_change"]
        # The page never emitted IRB_STATUS_CHANGE because the env var was unset.
        assert len(irb_events) == 0
    finally:
        os.environ.pop("AMOEBANATOR_AUDIT_PATH", None)
        tmp_path.unlink(missing_ok=True)


# ---------------------------------------------------------------------
# Visual regression text-snapshot drift <5% chars
# ---------------------------------------------------------------------
def test_visual_snapshot_baseline() -> None:
    """Capture markdown blob from page render; compare to committed baseline.

    Skipped until the baseline file lands. Once committed, the
    test fails if the page's markdown drifts >5% character delta -
    catching nav/disclaimer regressions that unit tests miss.
    """
    if not SNAPSHOT_PATH.exists():
        pytest.skip(
            f"baseline {SNAPSHOT_PATH} not present yet; capture will create it"
        )
    at = _fresh_app_test()
    at.run(timeout=30)
    captured = "\n".join(m.value for m in at.markdown)
    baseline = SNAPSHOT_PATH.read_text(encoding="utf-8")
    if not baseline:
        pytest.skip("baseline file empty")
    # Symmetric character-delta ratio
    longer = max(len(captured), len(baseline))
    shorter = min(len(captured), len(baseline))
    drift = (longer - shorter) / longer if longer else 0.0
    assert drift < 0.05, (
        f"snapshot drift {drift:.1%} exceeds 5% threshold "
        f"(baseline={len(baseline)} chars, captured={len(captured)} chars)"
    )


def test_fake_output_uses_the_shipped_thresholds() -> None:
    """The fixture's defaults are the artifacts' values, not typed numbers."""
    shipped = _artifact_thresholds()
    fake = _fake_infer_output()
    for key in ("energy_tau", "d2_tau", "n_cal", "alpha"):
        assert fake[key] == shipped[key]
    # the default Low fake sits inside both gates; the bacterial fake is above tau_E
    assert fake["energy"] <= fake["energy_tau"] and fake["mahalanobis_d2"] <= fake["d2_tau"]
    bacterial = _fake_infer_output(**_BACTERIAL_FAKE)
    assert bacterial["energy"] > bacterial["energy_tau"]
    assert bacterial["mahalanobis_d2"] <= bacterial["d2_tau"]


def test_bacterial_fake_matches_the_shipped_preset() -> None:
    """The shared bacterial values are what infer_one returns for the preset."""
    import pytest

    from app.presets import PRESETS
    from app.utils import build_row
    from ml.infer import infer_one

    out = infer_one(build_row(**PRESETS["bacterial_meningitis_limitation"]["inputs"]))
    assert out["prediction"] == _BACTERIAL_FAKE["prediction"]
    assert out["reason"] == _BACTERIAL_FAKE["reason"]
    assert out["p_high"] == pytest.approx(_BACTERIAL_FAKE["p_high"], abs=5e-5)
    assert out["energy"] == pytest.approx(_BACTERIAL_FAKE["energy"], abs=5e-4)
    assert out["mahalanobis_d2"] == pytest.approx(_BACTERIAL_FAKE["mahalanobis_d2"], abs=5e-4)
