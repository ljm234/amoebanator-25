"""Multi-page Streamlit entry point.

Registers the four pages with ``st.navigation`` (Streamlit 1.36+).

Run via:

    streamlit run streamlit_app.py

This entry lives at the repo root (HF Spaces docker-app convention).
An earlier layout placed it at ``app/app.py``, but that made Python register
"app" as the script module name when Streamlit booted, shadowing the
``app/`` package directory and breaking ``from app.disclaimer import ...``
on the Hugging Face Space. The legacy single-file entry lives at
``legacy_app.py``; this is the canonical entry point.
"""
from __future__ import annotations

from pathlib import Path

import streamlit as st


# st.Page resolves paths relative to the entry script's directory.
# This entry lives at the repo root, so the pages/ directory is a
# direct sibling. Resolve absolute paths so nav works regardless of
# cwd at `streamlit run` time.
_REPO_ROOT = Path(__file__).resolve().parent
_PAGES_DIR = _REPO_ROOT / "pages"


pages = [
    st.Page(_PAGES_DIR / "01_predict.py", title="Predict"),
    st.Page(_PAGES_DIR / "02_audit.py", title="Audit"),
    st.Page(_PAGES_DIR / "03_about.py", title="About"),
    st.Page(_PAGES_DIR / "04_references.py", title="References"),
]

pg = st.navigation(pages)
pg.run()
