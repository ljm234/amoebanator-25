"""Audit log viewer.

Renders the shared audit chain (not filtered to the current session) via ``st.table`` (HTML <table> semantics for screen readers, NOT
``st.dataframe``'s virtualised React grid). Capped at 10,000 rows;
full chain stays intact in the underlying JSONL file.

The CSV behind the download button is rebuilt on every page run (each
run appends an audit_export_requested event, clicked or not),
preserving every row + the hash chain pointers, so reviewers
can check the chain links post-download against a cloned repo.

The download matters because the Hugging Face Space's filesystem is
ephemeral: the audit log is wiped when the container restarts, so the
page asks the user to download a copy before leaving.
"""
from __future__ import annotations

import datetime
from pathlib import Path

import pandas as pd
import streamlit as st

from app.audit_export import export_audit_to_csv
from app.disclaimer import render_disclaimer
from ml.audit_hooks import default_audit_path


_ROW_CAP = 10_000


st.set_page_config(page_title="Audit - Amoebanator 25")
render_disclaimer()

st.title("Audit Log")

# Ephemerality banner above the table.
st.warning(
    "Showing the shared audit log file: events from all visitors, not "
    "just this session (entries carry no session ID). "
    "On the Space the file is wiped "
    "on container restart (HF free-tier ephemeral disk). "
    "Use 'Download audit log (CSV)' to keep a copy before leaving the "
    "demo."
)

audit_path: Path = default_audit_path()

if not audit_path.exists() or audit_path.stat().st_size == 0:
    st.info(
        "No audit events yet. Run a prediction on the Predict page first, "
        "then return here to view the chain."
    )
    st.stop()


def _load_audit_df(path: Path) -> pd.DataFrame:
    """Load JSONL audit log into a flat DataFrame.

    Each line in the JSONL is a single AuditEntry. Type and date inference
    are off, so every field is shown as stored: without that, pandas reads
    the all-zero genesis previous_hash as the integer 0 and reformats the
    timestamps.
    """
    return pd.read_json(path, lines=True, dtype=False, convert_dates=False)


df = _load_audit_df(audit_path)
total_rows = len(df)

if total_rows > _ROW_CAP:
    df_display = df.tail(_ROW_CAP)
    st.info(
        f"Showing last {_ROW_CAP:,} of {total_rows:,} entries (oldest "
        "entries trimmed for display; full chain still intact in the "
        "underlying file). Use 'Download audit log (CSV)' to export the full log."
    )
else:
    df_display = df

# st.table - true HTML <table> semantics for screen readers.
st.table(df_display)


# CSV download button. The file name carries the export time; the log has
# no session ID to put in it.
ts = (
    datetime.datetime.now(datetime.timezone.utc)
    .isoformat()
    .replace(":", "-")
)
filename = f"amoebanator_audit_{ts}.csv"
csv_bytes = export_audit_to_csv(audit_path)
st.download_button(
    label="Download audit log (CSV)",
    data=csv_bytes,
    file_name=filename,
    mime="text/csv",
    key="download_audit_csv",
)

# Small footer surfacing the schema version + chain integrity contract
# so a reviewer reading the downloaded CSV knows what to verify.
st.caption(
    "Exported under CSV schema version 1. To verify chain integrity, "
    "run `app.audit_export.verify_csv_chain_integrity(<bytes>)` on the "
    "downloaded file from a cloned repo. Each row includes "
    "`previous_hash` + `entry_hash` columns; the verifier recomputes "
    "each row's hash and checks each link to the prior row. It catches "
    "a row edited in place, but not rows removed from the start or end "
    "of the file or a chain rewritten with recomputed (unkeyed) hashes."
)
