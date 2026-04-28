"""Phase 4.5 multi-page Streamlit entry — Mini-2 T2.4.

Registers the 4 sprint pages with ``st.navigation`` (Streamlit 1.36+).
Page order matches the demo's intended UX flow: Predict (landing) →
Audit (chain viewer + CSV download) → About (model card + |w_i| panel)
→ References (22 refs grouped).

Run via:

    streamlit run app/app.py

(After Mini-1 spec-gap #8 fix, the legacy single-file entry lives at
``legacy_app.py``; this is the canonical Phase 4.5 entry.)
"""
from __future__ import annotations

from pathlib import Path

import streamlit as st


# st.Page resolves paths relative to the entry script's directory.
# Since this entry lives at app/app.py but the pages live at the
# repo root pages/ directory, we resolve absolute paths here so the
# nav works regardless of cwd at `streamlit run` time.
_REPO_ROOT = Path(__file__).resolve().parent.parent
_PAGES_DIR = _REPO_ROOT / "pages"


pages = {
    "🔬 Predict": [
        st.Page(_PAGES_DIR / "01_predict.py", title="Predict", icon="🔬"),
    ],
    "📜 Audit": [
        st.Page(_PAGES_DIR / "02_audit.py", title="Audit", icon="📜"),
    ],
    "ℹ️ About": [
        st.Page(_PAGES_DIR / "03_about.py", title="About", icon="ℹ️"),
    ],
    "📚 References": [
        st.Page(_PAGES_DIR / "04_references.py", title="References", icon="📚"),
    ],
}

pg = st.navigation(pages)
pg.run()
