"""Clinical presets for the predict page.

Three presets cover the demo's discrimination story:

1. ``high_risk_pam``                    - positive control (PAM-likely
                                          pediatric patient).
2. ``bacterial_meningitis_limitation``  - known limitation: the model
                                          cannot tell bacterial
                                          meningitis from PAM at n=30.
                                          The UI shows a red banner next
                                          to the result.
3. ``normal_csf``                       - negative control (adult, no
                                          PAM risk factors).

The page-load NEUTRAL state functions as a fourth implicit scenario.

The field is named ``current_behavior``, not ``expected``: it records
what ``infer_one`` returned on ``snapshot_date``, and a model trained on
a real cohort should change the bacterial preset's result.

The ``limitation_banner`` flag is explicit (not omitted) on every
preset so the UI's render logic doesn't have to handle missing-key
cases.
"""
from __future__ import annotations

from typing import Any


# Snapshot date for current_behavior values.
_SNAPSHOT_DATE: str = "2026-04-26"


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
            "p_high_approx": 1.0,
            "snapshot_date": _SNAPSHOT_DATE,
        },
        "limitation_banner": False,
    },

    # -- Preset 2: known limitation (bacterial meningitis, not PAM) -----
    # The model returns prediction="High" because the 30 synthetic rows
    # contain no bacterial meningitis that is not PAM. The matching test in
    # tests/test_app_presets.py is marked xfail(strict=False), so a model
    # that predicts Low shows up as XPASS without failing CI.
    "bacterial_meningitis_limitation": {
        "label": "Load bacterial meningitis (limitation demo)",
        "description": (
            "This preset shows a known model limitation. The 30 synthetic "
            "training rows contain no bacterial meningitis that is not "
            "PAM, so the model cannot tell bacterial meningitis from PAM "
            "and predicts High. Fixing this needs a real cohort with "
            "bacterial and viral meningitis labels, such as the planned "
            "MIMIC-IV study (target n >= 200). Try the other 2 presets to "
            "see where the model works."
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
            "prediction": "High",
            "p_high_approx": 1.0,
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
            "p_high_approx": 1.89e-13,
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
