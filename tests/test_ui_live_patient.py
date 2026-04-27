"""
Phase 1.3 — tests for the live-patient widget.

Covers:
  * build_row: schema correctness, type coercion, symptom joining
  * decision_badge: badge per prediction class (incl. ABSTAIN with reason)
  * _fmt_metric: missing/None/garbage tolerance
  * render_live_patient_panel: module imports cleanly with Streamlit mocked,
    form path returns without calling infer_one when not submitted, and
    successful submission path passes the row through to infer_one.
"""
from __future__ import annotations

import sys
from typing import Any
from unittest.mock import MagicMock, patch

import pytest


def _import_module() -> Any:
    sys.modules.pop("ml.ui_live_patient", None)
    import ml.ui_live_patient as mod
    return mod


def test_module_imports_cleanly() -> None:
    mod = _import_module()
    assert hasattr(mod, "render_live_patient_panel")
    assert callable(mod.render_live_patient_panel)
    assert hasattr(mod, "build_row")
    assert hasattr(mod, "decision_badge")


def test_build_row_schema_and_types() -> None:
    mod = _import_module()
    row = mod.build_row(
        age=12, csf_glucose=18.0, csf_protein=420.0, csf_wbc=2100,
        pcr=True, microscopy=True, exposure=True,
        symptoms=["fever", "headache", "nuchal_rigidity"],
    )
    assert row["age"] == 12 and isinstance(row["age"], int)
    assert row["csf_glucose"] == 18.0 and isinstance(row["csf_glucose"], float)
    assert row["csf_protein"] == 420.0 and isinstance(row["csf_protein"], float)
    assert row["csf_wbc"] == 2100 and isinstance(row["csf_wbc"], int)
    assert row["pcr"] == 1 and row["microscopy"] == 1 and row["exposure"] == 1
    assert row["symptoms"] == "fever;headache;nuchal_rigidity"


def test_build_row_handles_empty_symptoms() -> None:
    mod = _import_module()
    row = mod.build_row(45, 70, 0.4, 3, False, False, False, [])
    assert row["symptoms"] == ""
    assert row["pcr"] == 0


def test_build_row_strips_blank_symptom_tokens() -> None:
    mod = _import_module()
    row = mod.build_row(20, 50, 1.0, 10, False, False, False, ["fever", "", "headache"])
    assert row["symptoms"] == "fever;headache"


@pytest.mark.parametrize(
    "prediction, reason, expected_substr",
    [
        ("High", None, "HIGH"),
        ("Low", None, "LOW"),
        ("Moderate", None, "MODERATE"),
        ("ABSTAIN", "OOD", "ABSTAIN — OOD"),
        ("ABSTAIN", "LogitEnergyAboveOODShift", "ABSTAIN — LogitEnergyAboveOODShift"),
        ("ABSTAIN", "ConformalAmbiguity", "ABSTAIN — ConformalAmbiguity"),
        ("ABSTAIN", None, "ABSTAIN — unspecified"),
        ("", None, "unknown"),
    ],
)
def test_decision_badge_covers_all_paths(
    prediction: str, reason: str | None, expected_substr: str
) -> None:
    mod = _import_module()
    badge = mod.decision_badge(prediction, reason)
    assert expected_substr in badge


def test_fmt_metric_handles_missing_and_garbage() -> None:
    mod = _import_module()
    out = {"a": 1.5, "b": None, "c": "xyz"}
    assert mod._fmt_metric(out, "a") == "1.500"
    assert mod._fmt_metric(out, "b") == "—"
    assert mod._fmt_metric(out, "c") == "—"
    assert mod._fmt_metric(out, "missing") == "—"
    assert mod._fmt_metric(out, "a", "{:.1f}") == "1.5"


def _streamlit_stub(submitted: bool = False) -> MagicMock:
    """Build a MagicMock that emulates the Streamlit API surface used by the panel."""
    st = MagicMock()
    # st.expander, st.form, and st.columns return context managers
    st.expander.return_value.__enter__.return_value = st
    st.expander.return_value.__exit__.return_value = False
    st.form.return_value.__enter__.return_value = st
    st.form.return_value.__exit__.return_value = False
    # st.columns(N) returns a list of N column-context-managers
    def _columns(n: int) -> list[MagicMock]:
        cols: list[MagicMock] = []
        for _ in range(n):
            col = MagicMock()
            col.__enter__.return_value = col
            col.__exit__.return_value = False
            cols.append(col)
        return cols
    st.columns.side_effect = _columns
    # number_input / checkbox / multiselect return their default-like values
    st.number_input.side_effect = [12, 18.0, 420.0, 2100]
    st.checkbox.side_effect = [True, True, True]
    st.multiselect.return_value = ["fever", "headache", "nuchal_rigidity"]
    st.form_submit_button.return_value = submitted
    return st


def test_render_returns_early_when_form_not_submitted() -> None:
    mod = _import_module()
    st = _streamlit_stub(submitted=False)
    with (
        patch.object(mod, "st", st),
        patch.object(mod, "infer_one") as mocked_infer,
    ):
        mod.render_live_patient_panel()
    mocked_infer.assert_not_called()


def test_render_calls_infer_one_with_built_row_on_submit() -> None:
    mod = _import_module()
    st = _streamlit_stub(submitted=True)
    fake_out = {
        "prediction": "High",
        "p_high": 0.97,
        "mahalanobis_d2": 19.0, "d2_tau": 26.7,
        "energy": 363.6, "energy_tau": 86.2,
        "energy_neg": -3.4, "energy_neg_tau": -1e-8,
        "ood_abstain_energy_neg": False,
        "qhat": 0.025, "alpha": 0.10,
        "include_high": True, "include_low": False,
        "group": "child",
    }
    with (
        patch.object(mod, "st", st),
        patch.object(mod, "infer_one", return_value=fake_out) as mocked_infer,
    ):
        mod.render_live_patient_panel()
    mocked_infer.assert_called_once()
    sent_row = mocked_infer.call_args[0][0]
    assert sent_row["age"] == 12
    assert sent_row["csf_glucose"] == 18.0
    assert sent_row["csf_protein"] == 420.0
    assert sent_row["csf_wbc"] == 2100
    assert sent_row["pcr"] == 1
    assert sent_row["microscopy"] == 1
    assert sent_row["exposure"] == 1
    assert sent_row["symptoms"] == "fever;headache;nuchal_rigidity"


def test_render_handles_missing_model_gracefully() -> None:
    mod = _import_module()
    st = _streamlit_stub(submitted=True)
    err = FileNotFoundError("Required model weights not found at /nope/model.pt.")
    with (
        patch.object(mod, "st", st),
        patch.object(mod, "infer_one", side_effect=err),
    ):
        mod.render_live_patient_panel()
    st.error.assert_called()
    st.info.assert_called()  # remediation hint shown
