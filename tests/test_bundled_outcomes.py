"""
outputs/metrics/bundled_outcomes.json records what the shipped pipeline does
with each of the 30 bundled rows. Every stored field must match a fresh run,
its summary must match its rows, and every copy of every count the docs and
the app quote from it (overall and per label, per gate) must match it.
"""
from __future__ import annotations

import json
import re
from pathlib import Path

import pandas as pd
import pytest

import scripts.inference.bundled_outcomes as bo
from app.presets import PRESETS
from ml.infer import infer_one

REPO = Path(__file__).resolve().parent.parent
ARTIFACT = REPO / "outputs" / "metrics" / "bundled_outcomes.json"
ENERGY = "ABSTAIN:LogitEnergyAboveOODShift"
OOD = "ABSTAIN:OOD"


def _payload() -> dict:
    return json.loads(ARTIFACT.read_text())


def _flat(path: str) -> str:
    """Doc text with blockquote markers removed and whitespace collapsed."""
    return re.sub(r"\s+", " ", (REPO / path).read_text(encoding="utf-8").replace(">", " "))


def _all_equal(pattern: str, text: str, expected: tuple[str, ...]) -> None:
    """Every occurrence of the quote in the text carries the artifact's numbers."""
    hits = re.findall(pattern, text, re.IGNORECASE)
    assert hits, pattern
    for h in hits:
        assert (h if isinstance(h, tuple) else (h,)) == expected, (pattern, h)


def test_artifact_matches_a_fresh_run() -> None:
    df = pd.read_csv(bo.LOG_CSV)
    rows = _payload()["rows"]
    assert len(rows) == len(df) == 30
    for (_, r), rec in zip(df.iterrows(), rows):
        out = infer_one(r[bo.INPUT_COLS])
        assert rec["case_id"] == str(r["case_id"])
        assert rec["risk_label"] == str(r["risk_label"])
        assert rec["prediction"] == str(out["prediction"])
        assert rec["reason"] == out.get("reason")
        assert rec["outcome"] == bo.outcome(out)
        if out.get("p_high") is None:
            assert rec["p_high"] is None
        else:
            # p_high comes from float32 logits; CI (Linux x86) and the machine that wrote the
            # artifact (macOS arm64) can differ by an ulp, i.e. ~1e-6 relative for tiny p_high.
            assert rec["p_high"] == pytest.approx(float(out["p_high"]), rel=1e-4, abs=1e-12)


def test_summary_matches_rows() -> None:
    payload = _payload()
    assert payload["summary"] == bo.summarize(payload["rows"])


def _counts() -> dict[str, int]:
    s = _payload()["summary"]
    high = s["by_label"]["High"]
    return {
        "n_rows": s["n_rows"],
        "n_abstain": s["n_abstain"],
        "n_energy": s["overall"].get(ENERGY, 0),
        "n_ood": s["overall"].get(OOD, 0),
        "n_high": sum(high.values()),
        "high_abstain": sum(v for k, v in high.items() if k.startswith("ABSTAIN")),
        "high_energy": high.get(ENERGY, 0),
        "high_ood": high.get(OOD, 0),
        "high_high": high.get("High", 0),
        "high_low": high.get("Low", 0),
    }


@pytest.mark.parametrize("doc", ["README.md", "docs/model_card.md", "docs/tripod-ai.md"])
def test_docs_quote_the_high_row_counts(doc: str) -> None:
    c = _counts()
    text = _flat(doc)
    assert f"{c['n_abstain']} of the {c['n_rows']} bundled rows abstain" in text
    assert f"{c['high_abstain']} of the {c['n_high']} High rows" in text
    assert f"{c['high_energy']} at the logit-energy gate" in text
    assert f"{c['high_ood']} at the Mahalanobis gate" in text
    assert re.search(rf"only {c['high_high']} High rows get a High label", text, re.IGNORECASE)
    assert "outputs/metrics/bundled_outcomes.json" in text
    _all_equal(r"(\d+) of the (\d+) bundled rows abstain", text, (str(c["n_abstain"]), str(c["n_rows"])))
    _all_equal(r"(\d+) of the (\d+) High rows", text, (str(c["high_abstain"]), str(c["n_high"])))
    _all_equal(r"only (\d+) High rows (?:get a High label|are labeled High)", text, (str(c["high_high"]),))
    splits = {(str(c["n_energy"]), str(c["n_ood"])), (str(c["high_energy"]), str(c["high_ood"]))}
    for split in re.findall(r"(\d+) at the logit-energy gate,? (?:and )?(\d+) at the Mahalanobis gate", text):
        assert split in splits, split
    if doc != "docs/tripod-ai.md":  # README and model card also say no High row is labeled Low
        assert c["high_low"] == 0
        assert "none gets a Low label" in text


def test_model_card_quotes_the_overall_gate_split() -> None:
    c = _counts()
    text = _flat("docs/model_card.md")
    assert (
        f"({c['n_energy']} at the logit-energy gate, {c['n_ood']} at the Mahalanobis gate)"
        in text
    )


@pytest.mark.parametrize(
    "doc", ["docs/model_card.md", "docs/tripod-ai.md", "docs/REPRODUCIBILITY.md"]
)
def test_docs_quote_the_energy_gate_count(doc: str) -> None:
    c = _counts()
    text = _flat(doc)
    assert f"flags {c['n_energy']} of the {c['n_rows']} bundled rows" in text
    assert "outputs/metrics/bundled_outcomes.json" in text
    _all_equal(r"flags (\d+) of the (\d+) bundled rows", text, (str(c["n_energy"]), str(c["n_rows"])))


def test_banner_quotes_the_energy_gate_count() -> None:
    """The bacterial preset's red banner quotes the same count as the artifact."""
    c = _counts()
    banner = PRESETS["bacterial_meningitis_limitation"]["description"]
    assert f"flags {c['n_energy']} of the {c['n_rows']} bundled rows" in banner
    _all_equal(r"flags (\d+) of the (\d+) bundled rows", banner, (str(c["n_energy"]), str(c["n_rows"])))
