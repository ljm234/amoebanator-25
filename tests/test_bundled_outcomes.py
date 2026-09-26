"""
outputs/metrics/bundled_outcomes.json records what the shipped pipeline does
with each of the 30 bundled rows. It must match a fresh run, its summary must
match its rows, and the abstention figures the docs quote must match it.
"""
from __future__ import annotations

import json
import re
from pathlib import Path

import pandas as pd

import scripts.inference.bundled_outcomes as bo
from ml.infer import infer_one

REPO = Path(__file__).resolve().parent.parent
ARTIFACT = REPO / "outputs" / "metrics" / "bundled_outcomes.json"


def _payload() -> dict:
    return json.loads(ARTIFACT.read_text())


def test_artifact_matches_a_fresh_run() -> None:
    df = pd.read_csv(bo.LOG_CSV)
    rows = _payload()["rows"]
    assert len(rows) == len(df) == 30
    for (_, r), rec in zip(df.iterrows(), rows):
        out = infer_one(r[bo.INPUT_COLS])
        assert rec["case_id"] == str(r["case_id"])
        assert rec["outcome"] == bo.outcome(out)


def test_summary_matches_rows() -> None:
    payload = _payload()
    assert payload["summary"] == bo.summarize(payload["rows"])


def test_docs_quote_the_artifact_counts() -> None:
    s = _payload()["summary"]
    high = s["by_label"]["High"]
    n_high = sum(high.values())
    n_high_abstain = sum(v for k, v in high.items() if k.startswith("ABSTAIN"))
    for doc in ("README.md", "docs/model_card.md", "docs/tripod-ai.md"):
        text = re.sub(r"\s+", " ", (REPO / doc).read_text(encoding="utf-8").replace(">", " "))
        assert f"{s['n_abstain']} of the {s['n_rows']} bundled rows abstain" in text, doc
        assert f"{n_high_abstain} of the {n_high} High rows" in text, doc
        assert "outputs/metrics/bundled_outcomes.json" in text, doc
