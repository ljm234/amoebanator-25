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

import streamlit as st


pages = {
    "🔬 Predict": [
        st.Page("pages/01_predict.py", title="Predict", icon="🔬"),
    ],
    "📜 Audit": [
        st.Page("pages/02_audit.py", title="Audit", icon="📜"),
    ],
    "ℹ️ About": [
        st.Page("pages/03_about.py", title="About", icon="ℹ️"),
    ],
    "📚 References": [
        st.Page("pages/04_references.py", title="References", icon="📚"),
    ],
}

pg = st.navigation(pages)
pg.run()
