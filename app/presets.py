"""Clinical presets for the predict page.

Three presets cover the demo's discrimination story:

1. ``high_risk_pam``                    - positive control (PAM-likely
                                          pediatric patient).
2. ``bacterial_meningitis_limitation``  - known limitation (see its
                                          description). The UI shows a
                                          red banner next to the result.
3. ``normal_csf``                       - negative control (adult, no
                                          PAM risk factors).

The page-load NEUTRAL state functions as a fourth implicit scenario.

The field is named ``current_behavior``, not ``expected``: it records
what ``infer_one`` returned on ``snapshot_date``, and a model trained on
a real cohort should change the bacterial preset's result.
tests/test_app_presets.py checks the recorded prediction against a live
``infer_one`` call.

The ``limitation_banner`` flag is set on every preset. The predict page
shows a preset's description as a red banner next to the result when the
flag is True and the preset's inputs are submitted unchanged.
"""
from __future__ import annotations

from typing import Any


# Snapshot date for current_behavior values: the model regenerated with
# standardized inputs and 500 training steps.
_SNAPSHOT_DATE: str = "2026-09-26"


PRESETS: dict[str, dict[str, Any]] = {
    # -- Preset 1: positive control (PAM-likely) -------------------------
    "high_risk_pam": {
        "label": "Load PAM-likely example",
        "description": (
            "Pediatric patient with classic PAM presentation: low CSF "
            "glucose, high protein, high WBC, recent freshwater exposure, "
            "positive PCR and microscopy, full symptom triad. Expected: "
            "High risk prediction."
        ),
        "inputs": {
            "age": 12,
            "csf_glucose": 18.0,
            "csf_protein": 420.0,
            "csf_wbc": 2100,
            "pcr": True,
            "microscopy": True,
            "exposure": True,
            "symptoms": ["fever", "headache", "nuchal_rigidity"],
        },
        "current_behavior": {
            "prediction": "High",
            # p_high returned by infer_one on the snapshot date.
            "p_high_approx": 0.999999,
            "snapshot_date": _SNAPSHOT_DATE,
        },
        "limitation_banner": False,
    },

    # -- Preset 2: known limitation (bacterial meningitis, not PAM) -----
    # The model gives this preset a High probability of 0.9994, and the
    # logit-energy gate then abstains on it (reason LogitEnergyAboveOODShift);
    # the description below says why. test_preset_live_snapshot_matches in
    # tests/test_app_presets.py pins the ABSTAIN. test_bacterial_preset_predicts_low
    # is marked xfail(strict=False): a model that predicts Low shows up there
    # as XPASS, while test_preset_live_snapshot_matches fails until
    # current_behavior is updated.
    "bacterial_meningitis_limitation": {
        "label": "Load bacterial meningitis (limitation demo)",
        "description": (
            "This preset shows a known model limitation. The 30 synthetic "
            "rows (24 training, 6 validation) contain no bacterial "
            "meningitis that is not PAM, so the model cannot tell bacterial "
            "meningitis from PAM: it gives this input a High probability of "
            "0.9994. The result is ABSTAIN only because the logit-energy "
            "gate flags the input, and that gate, fit on six validation "
            "rows, also flags 15 of the 30 bundled rows, so it does not "
            "recognize bacterial meningitis. Telling the two apart needs "
            "real data in which bacterial meningitis and PAM carry different "
            "labels. Try the other 2 presets to see a High and a Low "
            "prediction."
        ),
        "inputs": {
            "age": 45,
            "csf_glucose": 38.0,
            "csf_protein": 180.0,
            "csf_wbc": 2500,
            "pcr": False,
            "microscopy": False,
            "exposure": False,
            "symptoms": ["fever", "headache", "nuchal_rigidity"],
        },
        "current_behavior": {
            "prediction": "ABSTAIN",
            "reason": "LogitEnergyAboveOODShift",
            # p_high returned by infer_one on the snapshot date.
            "p_high_approx": 0.9994,
            "snapshot_date": _SNAPSHOT_DATE,
        },
        # The UI shows the description as a red banner next to the
        # result, after inference, not before.
        "limitation_banner": True,
    },

    # -- Preset 3: negative control (normal CSF) -------------------------
    "normal_csf": {
        "label": "Load normal CSF example",
        "description": (
            "Adult patient with normal CSF profile and no PAM risk "
            "factors. Expected: Low risk prediction."
        ),
        "inputs": {
            "age": 35,
            "csf_glucose": 65.0,
            "csf_protein": 30.0,
            "csf_wbc": 3,
            "pcr": False,
            "microscopy": False,
            "exposure": False,
            "symptoms": [],
        },
        "current_behavior": {
            "prediction": "Low",
            # p_high returned by infer_one on the snapshot date.
            "p_high_approx": 3.44e-06,
            "snapshot_date": _SNAPSHOT_DATE,
        },
        "limitation_banner": False,
    },
}


def load_preset(key: str) -> dict[str, Any]:
    """Return the preset dict for ``key``.

    Raises ``KeyError`` if ``key`` not in :data:`PRESETS` - fail-loud
    over silent default so an upstream typo surfaces immediately rather
    than rendering an empty form.
    """
    return PRESETS[key]
