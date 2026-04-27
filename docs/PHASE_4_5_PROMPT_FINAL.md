# Phase 4.5 Sprint Trigger Prompt

**Paste this entire document as your first message to a fresh Claude Code session.**

This document is self-contained. A Claude Code session reading this for the first time, with zero prior context, MUST be able to execute the Mini-1 + Mini-2 sprint without consulting any other file. The companion docs (`AUDIT_REPORT.md`, `PHASE_4_5_PLAN.md`, `INFORMATION_RECAP.md`) exist only as escape hatches if context is lost mid-sprint (§7).

**Pre-flight checklist** (verify these BEFORE pasting the rest of the prompt):
- Working directory: `/Users/jordanmontenegro/Desktop/Amoebanator 25/Amoebanator 25/`
- Branch: `main` (no feature branches; commits land directly on main per Q14)
- Baseline commit: `b8f62e3` (audit close) or `5938cd8` (Phase J Doc 2 close) or later
- Test baseline: `pytest --collect-only -q` returns ≥1233 tests (1233 is post-audit baseline; sprint adds ~90)
- GitHub repo state: `gh repo view --json url --jq .url` returns `https://github.com/ljm234/amoebanator-25` (post Step 8 rename — see USER_ASSIGNMENTS.md)
- HF_TOKEN secret: `gh secret list` shows `HF_TOKEN` present (per USER_ASSIGNMENTS.md Step 6)

If any pre-flight check fails, **STOP** and tell Jordan. Do not proceed.

---

## §0. Identity & Role

You are Claude Code, operating in the Amoebanator 25 repository at `/Users/jordanmontenegro/Desktop/Amoebanator 25/Amoebanator 25/`. You are pair-programming with Jordan Montenegro-Calla (bilingual ES/EN; prefers honest > impressive). Jordan is preparing a model-serving + reviewer-grade web layer for a tabular MLP that classifies *Naegleria fowleri* / PAM (primary amoebic meningoencephalitis) risk from 10 CSF + clinical features. Targets: medRxiv submission Oct 2026; PhD apps Fall 2027 (PIs Zitnik, Chen, Beam, Rajpurkar, Pickett); Kallpa industry pivot post-app.

### 0.1 Quality bar (verbatim from Jordan)

> *"we need to make everything realistic and honest 2060 year 100% exceptional 5/5 stars, A+"*

Operationalized as four sub-rules. Apply this filter to every decision in-flight:

- **Honest > impressive.** When a finding makes the demo look worse but more accurate, the honest rendering wins. D18 (bacterial-NOT-PAM indistinguishable from PAM at n=30) is the canonical example: rather than dropping the bacterial preset, the audit reframed it as an explicit "limitations demo" with a red banner.
- **Reviewer-grade > feature-rich.** When a feature adds complexity but no defensibility, cut it. SHAP on n=30 background is mathematically vacuous (Q17.A); the `|w_i|` panel is the honest substitute.
- **2026-real not fantasy.** Verify external claims (HF Space behavior, Streamlit version capabilities, HF ToS) against current docs, not against memory.
- **Evidence-based not vibes.** Every numeric claim requires a measured value. Q18 (cold-start) is the canonical example: the audit's initial 500ms estimate was overturned by actual measurement (model load 59ms; PyTorch import is the dominant 3.7s cost).

### 0.2 Anti-pattern list (do NOT do)

- **No new abstractions** unless three+ similar lines force one. Three similar lines is better than a premature abstraction.
- **No scope creep.** If a "nice-to-have" surfaces mid-sprint, log to `docs/FUTURE_WORK.md` (create if doesn't exist) and continue current task.
- **No cargo-cult tests.** Tests must verify behavior, not pad the count. Q20 vote rejected ≥1300 padded gate in favor of ≥1280 honest gate (and ≥1320 for Mini-2).
- **No silent error handling.** Every exception either propagates with context, surfaces as user-facing `st.error` with correlation ID, or emits an audit event. No bare `except:` blocks.
- **No mocking the database in tests.** Integration tests hit real `model.pt` and real audit JSONL.
- **No commits skipping hooks.** Pre-commit hooks (pyright, ruff) must pass. If a hook fails, fix the root cause; do NOT use `--no-verify`.
- **No --amend on shared commits.** Always create new commits. If a hook fails post-commit, fix and create a follow-up commit.
- **No git push --force.** Branch is `main`; force-push to main is forbidden.

### 0.3 Refactor commit cap

The pre-sprint audit phase used 4 refactor commits (cap was 3, raised to 4 once with explicit rationale, then locked absolutely). **The sprint phase resets to 0/4 fresh.** Mini-1 + Mini-2 collectively may use up to 4 refactor commits if needed. Each refactor must:
1. Be defensible individually (one PR-able diff).
2. Not overlap with files the next mini will reopen.
3. Have a Q-decision or new D-finding it traces to.

If you reach 4 refactor commits and a 5th seems necessary, **STOP** and ask Jordan. The cap exists to prevent infinite scope creep.

### 0.4 Spanish-friendly framing

Jordan is bilingual. Spanish framing in conversational responses ("Dale, vamos con T1.4 ahora") is fine. Code, paths, file content, commit messages, test names, docstrings: English.

---

## §1. Sprint Context

### 1.1 What just shipped (audit phase, 7 commits, 1233 tests baseline)

The Phase 4.5 PRE-FLIGHT discovery audit ran 2026-04-26 to 2026-04-27 and produced 7 commits + 4 documentation outputs (this prompt is Doc 3 of 4). The 7 commits in topological order:

```
46f33c4 — Pre-Phase-4.5 baseline (apex/ moved out, git init)
bed84df — refactor: extract MLP to ml/model.py
67039e3 — refactor: route conformal_fit_from_probs.py through ml.conformal_advanced
3fd05ed — refactor: rename LowEnergy → LogitEnergyBelowInDistFloor
6654877 — test: assert AuditEventType emission in IRB gate
6f02a75 — docs: add Tunkel 2004 + Seehusen 2003 refs
b8f62e3 — fix: flip logit-energy gate semantics + rename to LogitEnergyAboveOODShift
0543c06 — docs(4.5): AUDIT_REPORT.md (complete)
5938cd8 — docs(4.5): PHASE_4_5_PLAN.md
```

Audit caught and fixed three load-bearing issues you should know about:
1. **Logit-energy OOD gate was firing in the wrong direction** (Q5 / Q11.A.fix / D17). Pre-audit `if energy < tau_e: ABSTAIN` was inverted from Liu 2020 canonical (`>` not `<`). Fixed in commit `b8f62e3` with math flip + rename + re-fit at q=0.95. Post-flip preset re-verification: 12 orders of magnitude separation between Low (1.9e-13) and High (1.0). Mahalanobis catches OOD positive control. Gate quiet on in-distribution.
2. **Three places computed conformal q-hat** (Q4 / D12). Standalone script bypassed canonical `compute_qhat`, suppressing `SmallCalibrationWarning`. Fixed in commit `67039e3`.
3. **MLP class duplicated in training.py and training_calib_dca.py** (Q2 / D2). Extracted to `ml/model.py` in commit `bed84df`.

### 1.2 What you're building (web demo for HF Spaces, ~950 LOC, 2 minis)

A multi-page Streamlit app deployable to Hugging Face Spaces free tier. The app exposes the existing `infer_one()` inference path (frozen — do not modify) through a clinical form + 3 preset buttons + audit log viewer + about page + references page. Total scope ~950 LOC across two minis.

**Mini-1 (~600 LOC + ~50 tests):** form + presets + disclaimer + audit utilities + 4 test files + visual snapshot baseline.
**Mini-2 (~350 LOC + ~40 tests):** audit page + about page + references page + multi-page navigation + 4 more test files.

Deploy target: `huggingface.co/spaces/luisjordanmontenegro/amoebanator-25` (Space exists, awaits sprint commit + push). USER ASSIGNMENT Step 6 + Step 8 must be complete before sprint starts (see §7 + USER_ASSIGNMENTS.md).

### 1.3 Why it matters

Three downstream stakeholders read this demo:
1. **medRxiv reviewers (submission Oct 2026, ~6 months out).** Cohort definition + calibration + uncertainty handling matters; PHI handling matters; reproducibility matters.
2. **PhD application reviewers (Fall 2027).** PIs Marinka Zitnik (Harvard, graph + clinical AI), Jonathan Chen (Stanford, clinical informatics), Andrew Beam (Harvard, calibration), Pranav Rajpurkar (Harvard, clinical foundation models), Brett Pickett (BYU, computational epidemiology). Each has a different audit lens; the demo must survive 30 seconds of skim from any of them.
3. **Kallpa industry pivot (post-PhD-app, ~2027-2028).** Demonstrable working clinical-ML system + honest limitation surfacing.

### 1.4 Reviewer skim heuristic

Apply this throughout the sprint: *"Would Beam catch this in 30 seconds?"* Beam's calibration sense reads T<1 (amplifying logits) immediately, reads inverted OOD gate semantics immediately, reads the difference between empirical coverage and the formal Lei 2018 bound immediately. Every spec in §2 below was filtered through this heuristic during the audit. If you find yourself adding code that wouldn't survive Beam-30s skim, stop and reconsider.

---

## §2. Inline Locked Decisions (file-sorted)

This section restates every Q-decision from the audit as an imperative spec, **organized by the file the decision lands in**, NOT by Q-number. When you're working on `app/disclaimer.py`, all decisions about disclaimer cluster together. Q-numbers preserved as parenthetical cross-references at end of each spec. The full Q-rationale lives in `AUDIT_REPORT.md` §3 (consult only if context lost).

### 2.1 `app/utils.py` (~80 LOC, Mini-1)

- **`build_row(age, csf_glucose, csf_protein, csf_wbc, pcr, microscopy, exposure, symptoms) -> dict`** MUST coerce booleans to int 0/1, join symptoms list to semicolon string, strip blank symptom tokens. Return dict with exactly 8 keys matching the form widgets. (Q11.A)
- **`decision_badge(prediction, reason=None) -> str`** MUST return Streamlit-markdown badge with icon + bold weight + color tag for each of `High`/`Low`/`Moderate`/`ABSTAIN`. Locked icon mapping: `🔴 **HIGH**`, `🟢 **LOW**`, `🔵 **MODERATE**`, `⚠️ **ABSTAIN**`. For ABSTAIN, reason MUST appear in badge text (e.g., `"⚠️ **ABSTAIN** — OOD"`). Empty/unknown prediction returns `"unknown"` badge. Stripping color tags MUST leave icon + text intact (color-blind safe). (Q15.5.A)
- **`_fmt_metric(out, key, fmt="{:.3f}") -> str`** MUST tolerate missing/None/non-numeric values and return `"—"` (em-dash) in those cases. Used for rendering Mahalanobis d², energy, conformal qhat without crashing on partial output dicts. (Cross-cutting)

### 2.2 `app/presets.py` (~95 LOC, Mini-1)

- **Module-level constant `PRESETS: dict[str, dict[str, Any]]`** MUST contain exactly 3 entries with keys `high_risk_pam`, `bacterial_meningitis_limitation`, `normal_csf` (snake_case, stable identifiers for audit log emission). (Q12.A, Q12.B)
- **Per-preset field schema:** `label` (str, button text), `description` (str, banner body), `inputs` (dict[str, Any] with the 8 form values), `current_behavior` (dict containing `prediction`, `p_high_approx`, `snapshot_date: "2026-04-26"`), `limitation_banner` (bool, explicit not omitted). The field `current_behavior` (NOT `expected`) is mandatory — the rename was a Q12 override for normative-vocabulary reasons. (Q12.B)
- **Locked input values per preset:**
  - `high_risk_pam`: `age=12, csf_glucose=18.0, csf_protein=420.0, csf_wbc=2100, pcr=True, microscopy=True, exposure=True, symptoms=["fever", "headache", "nuchal_rigidity"]`. Current behavior: `prediction="High", p_high_approx=1.0`. `limitation_banner=False`.
  - `bacterial_meningitis_limitation`: `age=45, csf_glucose=38.0, csf_protein=180.0, csf_wbc=2500, pcr=False, microscopy=False, exposure=False, symptoms=["fever", "headache", "nuchal_rigidity"]`. Current behavior: `prediction="High", p_high_approx=1.0`. `limitation_banner=True` (renders red banner adjacent to result).
  - `normal_csf`: `age=35, csf_glucose=65.0, csf_protein=30.0, csf_wbc=3, pcr=False, microscopy=False, exposure=False, symptoms=[]`. Current behavior: `prediction="Low", p_high_approx=1.89e-13`. `limitation_banner=False`.
- **`load_preset(key) -> dict`** MUST return the preset dict for `key`, raising `KeyError` if not in `PRESETS`. (Q12.A)
- **D18 limitation banner text (verbatim, embedded in `bacterial_meningitis_limitation.description`):**
  > *"⚠ This preset is a known model limitation. Training data (n=30) contains zero non-PAM bacterial meningitis cases, so the model cannot distinguish bacterial-NOT-PAM from PAM. The Phase 6 MIMIC-IV cohort (target n ≥ 200, includes bacterial vs viral meningitis labels) will fix this. We surface this preset deliberately as an honesty signal — every model has limits, and showing them where they bite is more useful than hiding them. Try the other 2 presets to see the model's working regime."*
- **`KNOWN_SYMPTOMS`** constant in this module OR `app/utils.py` MUST be exactly `("fever", "headache", "nuchal_rigidity")` — the 3 symptoms the model scores. (Q11.B)

### 2.3 `app/disclaimer.py` (~120 LOC, Mini-1)

- **Module-level constant `DISCLAIMER_TEXT`** MUST contain verbatim:
  > *"⚠ Research prototype, NOT a medical device. Trained on n=30 synthetic patient vignettes (n_train=24, n_val=6); contains zero real PHI. Outputs are calibrated probabilities, **limited to** the n=30 training distribution — not diagnoses. Not for clinical decision support, not validated. Source + caveats: github.com/ljm234/amoebanator-25 — Contact: lmontenegrocalla@mail.weber.edu (ORCID 0009-0000-7851-7139)"*
- The 5 mandatory tokens (enforced by parametrized canonical test): `NOT a medical device`, `n=30`, `limited to`, `ORCID`, `lmontenegrocalla@mail.weber.edu`. Test (`tests/test_app_disclaimer.py::test_disclaimer_on_every_page`) parametrizes over the 4 pages. (Q19.A, Q19.B, Q19.C)
- **`render_disclaimer() -> None`** MUST be called at the top of every page. Idempotent. Emits `DISCLAIMER_TEXT` via `st.markdown` (NOT `st.info`/`st.warning` — those carry framework-injected styling that competes with the wash+border CSS). (Q19.B)
- **`_INJECTED_CSS`** constant MUST contain CSS for `.stAlert[kind="error"]`, `.stAlert[kind="warning"]`, `.stAlert[kind="info"]`, `.stAlert[kind="success"]` with **wash + border + deep-text pattern** achieving WCAG-AA contrast ≥4.5:1. Locked color combos (computed contrast in parens):
  - error/limitation: text `#B71C1C` on bg `#FFEBEE`, border `#B71C1C` 4px left (7.18:1)
  - info: text `#0D47A1` on bg `#E3F2FD`, border `#0D47A1` 4px left (8.21:1)
  - success: text `#1B5E20` on bg `#E8F5E9`, border `#1B5E20` 4px left (7.59:1)
  - The `wcag_contrast_ratio(text_hex, bg_hex) -> float` helper MUST be defined in this module (relative-luminance ratio math, no axe-core dep). (Q15.5.D)
- **`prefers-reduced-motion` block** MUST be in the same `_INJECTED_CSS`:
  ```css
  @media (prefers-reduced-motion: reduce) {
      * { animation-duration: 0.01ms !important; transition-duration: 0.01ms !important; }
      .stSpinner { display: none !important; }
  }
  ```
  Manual verification (browser-side): "Open in Chrome with prefers-reduced-motion: reduce enabled in DevTools → Rendering → confirm no animations play." (Q15.5.E)

### 2.4 `app/audit_export.py` (~75 LOC, Mini-1)

- **`export_audit_to_csv(jsonl_path: pathlib.Path) -> bytes`** MUST read the audit JSONL, convert to CSV bytes preserving `previous_hash`, `current_hash`, `timestamp`, `event_type`, `actor`, `resource`, `action_detail`, `metadata` (as JSON string), `schema_version`. No filtering, no truncation. Returns CSV-encoded bytes ready for `st.download_button`. (Q13.A)
- **`verify_csv_chain_integrity(csv_bytes: bytes) -> bool`** MUST re-parse CSV, verify `previous_hash → current_hash` chain integrity. Returns True iff every row's `current_hash` matches sha256 of canonical row repr. Used by Mini-1 closure gate criterion #4 round-trip test. (Q13.A)
- Calling `export_audit_to_csv()` MUST emit `_emit(AuditEventType.AUDIT_EXPORT_REQUESTED, ...)`. (Q13.A)

### 2.5 `pages/01_predict.py` (~225 LOC, Mini-1)

This is the bulk of Mini-1. The page MUST:

- **Call `st.set_page_config(page_title="Predict — Amoebanator 25", page_icon="🔬")`** at top. (Q16.b consistency)
- **Call `render_disclaimer()`** immediately after `set_page_config`. (Q19.B)
- **Render 3 preset buttons in a `st.columns(3)` row** — labels from `PRESETS[key]["label"]`. Clicking a button updates `st.session_state[f"input_{k}"]` for each key in the preset's `inputs`, sets `st.session_state.active_preset = key`, and emits `_emit(AuditEventType.WEB_PRESET_LOADED, metadata={"preset": key})`. (Q12.A, Q7.C)
- **Render the form via `st.form("predict_form")`** with 8 widgets:
  - `st.number_input("Age (years)", min_value=0, max_value=120, value=session_state.get("input_age", 12), key="age")`
  - `st.number_input("CSF glucose (mg/dL)", min_value=0.0, value=session_state.get("input_csf_glucose", 65.0), step=1.0, key="csf_glucose")`
  - `st.number_input("CSF protein (mg/dL)", min_value=0.0, value=session_state.get("input_csf_protein", 30.0), step=1.0, key="csf_protein")`
  - `st.number_input("CSF WBC (cells/µL)", min_value=0, value=session_state.get("input_csf_wbc", 3), step=1, key="csf_wbc")`
  - `st.checkbox("PCR positive", value=session_state.get("input_pcr", False), key="pcr")`
  - `st.checkbox("Microscopy positive", value=session_state.get("input_microscopy", False), key="microscopy")`
  - `st.checkbox("Recent freshwater exposure", value=session_state.get("input_exposure", False), key="exposure")`
  - `st.multiselect("Symptoms", options=KNOWN_SYMPTOMS, default=session_state.get("input_symptoms", []), key="symptoms")`
  - `st.form_submit_button("Run inference", disabled=_is_button_disabled())` (Q11.A, Q11.B)
- **NEUTRAL defaults sanity gate** — submitting the form unchanged from page-load defaults MUST cause `infer_one` to return `Low` with `p_high < 0.001`. If this fails, stop and report; the model has regressed since `b8f62e3`. (Q11.A)
- **Out-of-range form input handling** — `csf_glucose=9999` or `age=-5` MUST trigger `st.error` with clear message *"Value exceeds typical clinical range (clinical max for csf_glucose is ~300 mg/dL). Please verify input."* and disable the submit button until corrected. NOT silent clamp, NOT crash. (Q14 acceptance criterion #2)
- **Session-state debounce with 30s stale-lock recovery:** before calling `infer_one`, check `if st.session_state.get("predicting") and (time.time() - st.session_state.get("predicting_at", 0)) < 30: st.warning("Already processing — wait."); st.stop()`. Set lock + timestamp before `try`, clear in `finally`. (Q15.D)
- **Inference execution under try/except chain:**
  - `except FileNotFoundError`: render yellow banner *"OOD gate is unconfigured (Mahalanobis stats file missing). All predictions return ABSTAIN/OOD until re-fit."*. Do NOT crash. Disable Run button OR rename to "Run anyway (gate unconfigured)". (Q15.B)
  - `except Exception as e`: generate `error_id_full = uuid.uuid4().hex`, truncate `error_id_user = error_id_full[:12]`, render `st.error(f"Prediction failed (error ID: {error_id_user}). Server-side log captured.")`, emit `_emit(AuditEventType.INTEGRITY_VIOLATION, metadata={"error_id": error_id_full, "exception_type": type(e).__name__, "exception_repr": repr(e)})`. (Q15.A)
- **Result rendering** MUST include four badges:
  1. **Decision badge** via `decision_badge(out["prediction"], out.get("reason"))` (Q15.5.A)
  2. **`T=0.27 (n=6)` badge with hover tooltip** — tooltip text verbatim: *"Calibrated by temperature scaling (Guo 2017, L-BFGS, n=6 validation). T=0.27 means the calibrator amplifies the model's raw confidence — typical temperature scaling has T>1 (attenuation); T<1 here is unusual and reflects fitting on only 6 samples. ECE and coverage estimates are empirical-only, not asymptotic. See docs/model_card.md §9."* (Q3)
  3. **`SmallCalibrationWarning` banner (yellow)** when `out.get("n_cal", 6) < 30`: *"⚠ Calibration set is small (n=6). Probability estimates are indicative only. Do not use as a clinical confidence score."* (Q3)
  4. **3-state conformal regime badge** computed from `(n=6, α=0.10, k=⌈(n+1)(1-α)⌉=7)`. At current state (n<k), MUST display `🔴 INVALID: Order-statistic clamped (k clipped from 7 to n=6); the formal guarantee 1−α is mathematically inapplicable.` (Q4.C)
- **D18 limitation banner** MUST render adjacent to result panel ONLY when `st.session_state.get("active_preset") == "bacterial_meningitis_limitation"`. Use `st.error()` (which inherits the wash+border+deep-text CSS from §2.3). (Q12.C)
- **IRB_BYPASS branches:** check `os.environ.get("AMOEBANATOR_IRB_BYPASS") == "1"`. If True, render extra red banner *"IRB bypass active — research mode only"* AND emit `_emit(AuditEventType.IRB_STATUS_CHANGE, actor="env_var", metadata={"bypass": True})`. If False/unset, no banner + no event. Both branches tested in `tests/test_pages_predict.py`. (Mini-1 closure gate criterion #6)
- **Inline tooltip strategy** — render references in sticky deterministic order per p_high bucket: `[1] CDC 2025 + [2] Tunkel 2004` always-shown; `[3] Cope 2016 + [4] Yoder 2010 + [5] Capewell 2015` for `p_high > 0.7`; `[6] Tunkel cross-ref + viral placeholder` for 0.3-0.7; `[7] Seehusen 2003` for `< 0.3`. Click-to-expand `+N more references for this risk band ↓` row via `st.expander`. (Q8.C)

### 2.6 `pages/02_audit.py` (~120 LOC, Mini-2)

- Call `st.set_page_config(page_title="Audit — Amoebanator 25", page_icon="📜")` + `render_disclaimer()`. (Q19.B)
- Render banner: *"Showing all events from current session. Earlier sessions wiped on container restart (HF free-tier ephemeral disk). Use 'Download session audit log' to preserve."* (Q13.B)
- Read `outputs/audit/audit.jsonl` via `pd.read_json(audit_path, lines=True)`. If file doesn't exist, render `st.info("No audit events yet. Run a prediction on the Predict page first.")` and `st.stop()`.
- **10k row cap** — display `df.tail(10000)`. If `len(df) > 10000`, render `st.info(f"Showing last 10,000 of {total_rows} entries (oldest entries trimmed for display; full chain still intact in the underlying file). Use Download CSV to export the full session.")`. (Q15.C)
- **Render via `st.table(df_display)` — NOT `st.dataframe`.** `st.table` emits true HTML `<table>` semantics for screen readers (NVDA, VoiceOver). Empirical sub-cap verification: if 10k-row `st.table` freezes browser at >2s CPU, drop cap to 1k with banner *"Showing last 1k of N rows; download CSV for full"*; if 1k freezes, drop to 500. (Q15.5.C)
- **CSV download button:**
  ```python
  csv_bytes = export_audit_to_csv(audit_path)
  st.download_button(
      label="Download session audit log (CSV)",
      data=csv_bytes,
      file_name=f"amoebanator_audit_{session_id}_{ts}.csv",
      mime="text/csv",
      key="download_audit_csv",
  )
  ```
  (Q13.A)

### 2.7 `pages/03_about.py` (~120 LOC, Mini-2)

- `set_page_config(page_title="About — Amoebanator 25", page_icon="ℹ️")` + `render_disclaimer()`. (Q19.B)
- **§1 Model architecture summary:** `Linear(10,32)→ReLU→Linear(32,16)→ReLU→Linear(16,2)`, 914 params, 6.4 KB. Cite `outputs/model/model.pt` sha256 (look up at sprint time via `shasum -a 256 outputs/model/model.pt | cut -c1-12`).
- **§2 Training summary:** n_train=24, n_val=6, synthetic vignettes from Yoder 2010 + Cope 2016 + CDC 2025 marginals. `random_state=42, test_size=0.2, stratify=y`.
- **§3 Calibration summary:** T=0.27 (L-BFGS, n=6 noise-fit). Link to `docs/model_card.md` §Caveats.
- **§4 `|w_i|` feature importance panel** (Q17.A, Q17.B, Q17.C):
  - Compute: load `outputs/model/model.pt`, extract first `Linear(10,32)` layer weight, mean across 32 output dims via `weight.abs().mean(dim=0)`, normalize by sum.
  - Render: `st.bar_chart` with feature names on y-axis, normalized `|w_i|` on x-axis.
  - Caption (verbatim, locked):
    > *"Feature importance via |w_i| (model-level mean of first Linear layer weights, normalized). NOT per-prediction attribution — for that, see SHAP (deferred to Phase 6 with MIMIC-IV n≥200). Current range: 9.1% to 11.5%, max/min ratio 1.27×. Interpretation: the model treats all 10 features near-equally, consistent with the n=30 training set limitation. SHAP on n=30 background data is mathematically vacuous; this panel is the honest substitute at current scale. See docs/model_card.md §Caveats for full discussion."*
- **§5 Conformal Advanced expander** (Q4.A): `st.expander("Advanced: explore conformal coverage")` containing `st.slider("α (significance level)", 0.05, 0.20, 0.10, step=0.05)`. On change, recompute q-hat + abstain rate, render the 3-state regime badge, show how ABSTAIN rate responds.
- **§6 Authorship + ORCID + contact** + the username-mismatch one-liner: *"Repo: github.com/ljm234/amoebanator-25 — HuggingFace Space: huggingface.co/spaces/luisjordanmontenegro/amoebanator-25 (same author, separate handles)."* (Q19.D)

### 2.8 `pages/04_references.py` (~80 LOC, Mini-2)

- `set_page_config` + `render_disclaimer()`.
- Render full 22-reference list with anchor links, grouped by category:
  - **PAM clinical** (Cope 2016, Yoder 2010, Capewell 2015, CDC 2025, Tunkel 2004, Seehusen 2003)
  - **ML methodology / calibration / conformal** (Guo 2017, Vovk 2005, Vovk 2013, Lei 2018, Platt 1999, Niculescu-Mizil 2005)
  - **OOD detection** (Lee 2018, Liu 2020)
  - **Governance / model documentation frameworks** (Mitchell 2019 model cards, Vasey 2022 DECIDE-AI, Collins 2024 TRIPOD+AI, Collins 2015 TRIPOD, Gebru 2021 datasheets, HHS 2012 HIPAA, Vickers 2006 DCA)
  - **Tools** (Ke 2017 LightGBM)
- Each reference renders as: `[bib_key] Authors. Title. *Venue* Year. PMID/DOI.`

### 2.9 `app/app.py` (~30 LOC, Mini-2)

- `st.navigation` entry point registering 4 pages:
  ```python
  pages = {
      "🔬 Predict": [st.Page("pages/01_predict.py", title="Predict", icon="🔬")],
      "📜 Audit":   [st.Page("pages/02_audit.py",   title="Audit",   icon="📜")],
      "ℹ️ About":   [st.Page("pages/03_about.py",   title="About",   icon="ℹ️")],
      "📚 References": [st.Page("pages/04_references.py", title="References", icon="📚")],
  }
  pg = st.navigation(pages)
  pg.run()
  ```
- Page order in nav: Predict (default landing) → Audit → About → References. (Q14)

### 2.10 `.streamlit/config.toml` (Mini-1)

Verbatim required content:

```toml
[server]
runOnSave = false
fileWatcherType = "none"
port = 8501              # NOT 7860 — verified against HF auto-Dockerfile EXPOSE 8501 + --server.port=8501

[global]
developmentMode = false
suppressDeprecationWarnings = true

[client]
showSidebarNavigation = true

[theme]
primaryColor = "#0D47A1"  # Material Blue 900 (Q16.b neutral-medical)
backgroundColor = "#FFFFFF"
secondaryBackgroundColor = "#F5F5F5"
textColor = "#212121"      # dark slate
```

All keys verified against Streamlit 1.52: zero deprecations. (Q16.c)

### 2.11 `ml/audit_hooks.py` (Mini-1, single commit)

- **Delete 11 dead enum values** from `AuditEventType`. The 11 values are listed in `AUDIT_REPORT.md` §4 D14 (consult only if list needed; bisect via `grep -rn "AuditEventType\." --include="*.py"` to find which values have zero `_emit()` callers).
- **Add 3 new web event values** as dedicated names (NOT polymorphic-via-metadata):
  ```python
  WEB_PREDICT_RECEIVED = "web_predict_received"
  WEB_PREDICT_RETURNED = "web_predict_returned"
  WEB_RATE_LIMIT_HIT   = "web_rate_limit_hit"
  ```
  Plus optional `WEB_PRESET_LOADED` and `AUDIT_EXPORT_REQUESTED` if they emerge as needed. Net delta: -8 to -11 values depending on additions. (Q7.A, Q7.C)
- Schema version field in audit.jsonl genesis entry MUST be bumped to `"2"` to mark the migration. (R3 mitigation)

### 2.12 Test file conventions (all Mini-1 + Mini-2 test files)

- File naming: `tests/test_<area>.py` matching the production module name (e.g., `tests/test_app_disclaimer.py` for `app/disclaimer.py`).
- Test function naming: `test_<thing>_<expected_behavior>` (e.g., `test_disclaimer_text_contains_5_mandatory_tokens`).
- Use Streamlit `AppTest` for page-level rendering tests. Mock `infer_one` for tests that don't need real model inference.
- Parametrize over the 4 pages for cross-page invariants (disclaimer presence, unique widget keys, WCAG-AA contrast). One canonical parametrized test, NOT 4 copies.
- xfail decorator usage: `@pytest.mark.xfail(strict=False, reason="...")` for D18 bacterial-limitation test. `strict=False` so Phase 6 success doesn't break CI (XPASS signals "fix this" but doesn't fail).
- Visual snapshot tests: capture `result.markdown` from AppTest, store as text in `tests/_snapshots/<page>.md.snap`. Drift threshold 5% character delta. Regenerate via `pytest --snapshot-update` on intentional changes.

### 2.13 Commit message conventions (every sprint commit)

Mandatory format:

```
<type>(<subphase>): <subject under 70 chars>

<body paragraph explaining the WHY of the change. Optional for trivial
commits but mandatory for any commit closing a Q-decision.>

Closes: Q<N>.<sub>, Q<M>.<sub>
Refs: PHASE_4_5_PLAN.md §<section>, AUDIT_REPORT.md §<section>
```

Types: `feat`, `fix`, `refactor`, `test`, `docs`, `chore`. Subphase: `4.5.1`, `4.5.2`, `4.5.3`, `4.5.4`. Subject: imperative voice, lowercase, no trailing period. Body: explain the WHY, not the WHAT (the diff has the WHAT). Closes/Refs footer: mandatory if commit closes a Q-decision; enables `git log --grep="Q11.A"` traceability for reviewers. (Q16.a)

### 2.14 Cross-cutting patterns

- **a11y CSS injection:** single source of truth in `app/disclaimer.py` `_INJECTED_CSS` constant. NO competing CSS in other modules. Wash + border + deep text + reduced-motion all in one block. (Q15.5.D, Q15.5.E)
- **Error correlation IDs:** every uncaught exception in any page MUST follow the Q15.A pattern (uuid4 full server-side, 12-char display, `INTEGRITY_VIOLATION` audit emit). Define a helper `def emit_correlation_id_error(e: Exception) -> str` in `app/utils.py` if used in 3+ places.
- **Audit emission on UI events:** every preset load, every prediction, every CSV export emits an `AuditEventType.WEB_*` event. Schema: `metadata={"preset": key, ...}` for preset-load; `metadata={"row_hash": sha256(row_repr), ...}` for prediction; `metadata={"export_size_bytes": n, ...}` for export. (Q7.C)
- **`@st.cache_resource` boundaries:** cache `_load_model_artifacts` (already `@lru_cache`-wrapped — do NOT double-wrap) and `load_presets`. Do NOT cache `infer_one` itself (every call must execute audit emit). Do NOT cache `export_audit_to_csv` (must read fresh from disk).
- **Session-state key prefix:** form input session-state keys MUST use `input_<field>` prefix (e.g., `input_age`, `input_csf_glucose`) so preset-load logic is unambiguous. (Q12.A)

---

## §3. Mini-1 Execution Protocol

### 3.1 Pre-Mini-1 verification

Before T1.1, verify and snapshot:

```bash
# Confirm baseline test count
pytest --collect-only -q 2>&1 | tail -3
# Expected: "1233 tests collected" (or higher if Mini-2 work has landed already)

# Snapshot pyright baseline
pyright 2>&1 | tail -5 > /tmp/pyright_baseline.txt
# Closure gate criterion #2 will compare against this baseline

# Confirm GitHub repo state (Step 8 rename complete)
gh repo view --json url --jq .url
# Expected: "https://github.com/ljm234/amoebanator-25"

# Confirm HF_TOKEN secret present
gh secret list | grep HF_TOKEN
# Expected: "HF_TOKEN  Updated <timestamp>"
```

If any check fails, STOP and tell Jordan. Do not proceed to T1.1.

### 3.2 Mini-1 task list (atomic, ordered)

#### T1.1 — Create `app/__init__.py` and `app/utils.py`

- Create directory `app/`.
- Create `app/__init__.py` with single docstring line.
- Create `app/utils.py` with `build_row()`, `decision_badge()`, `_fmt_metric()`, and `KNOWN_SYMPTOMS` constant per §2.1 + §2.2 specs.
- **Acceptance:** `python -c "from app.utils import build_row, decision_badge, _fmt_metric, KNOWN_SYMPTOMS; print(KNOWN_SYMPTOMS)"` prints `("fever", "headache", "nuchal_rigidity")`.
- **Verification:** `pyright app/utils.py` → 0 errors.
- **Rollback:** `rm -rf app/` (no other files touched yet).
- **Commit:** `feat(4.5.1): app/utils.py with build_row + decision_badge + KNOWN_SYMPTOMS`. Closes: Q11.B, Q15.5.A. Refs: PHASE_4_5_PLAN.md §4.2.

#### T1.2 — Create `app/presets.py`

- Create `app/presets.py` with `PRESETS` dict (3 presets, exact values from §2.2) and `load_preset()` helper.
- **Acceptance:** `python -c "from app.presets import PRESETS; assert set(PRESETS.keys()) == {'high_risk_pam', 'bacterial_meningitis_limitation', 'normal_csf'}; print('OK')"` prints `OK`.
- **Verification:** `pyright app/presets.py` → 0 errors.
- **Rollback:** `git checkout HEAD -- app/presets.py` (restore from previous commit) OR `rm app/presets.py`.
- **Commit:** `feat(4.5.1): app/presets.py with 3 locked presets + xfail-compatible schema`. Closes: Q12.A, Q12.B. Refs: PHASE_4_5_PLAN.md §4.2.

#### T1.3 — Create `app/disclaimer.py`

- Create `app/disclaimer.py` with `DISCLAIMER_TEXT`, `_INJECTED_CSS` (wash+border for 4 alert kinds + reduced-motion block), `wcag_contrast_ratio()` helper, `render_disclaimer()` function.
- **Acceptance:** `python -c "from app.disclaimer import DISCLAIMER_TEXT, wcag_contrast_ratio; assert 'limited to' in DISCLAIMER_TEXT; assert wcag_contrast_ratio('#B71C1C', '#FFEBEE') >= 4.5; print('OK')"` prints `OK`.
- **Verification:** `pyright app/disclaimer.py` → 0 errors.
- **Rollback:** `git checkout HEAD -- app/disclaimer.py` OR `rm app/disclaimer.py`.
- **Commit:** `feat(4.5.1): app/disclaimer.py with locked variant (ii) text + WCAG-AA CSS + reduced-motion`. Closes: Q19.A, Q19.B, Q19.C, Q15.5.D, Q15.5.E. Refs: PHASE_4_5_PLAN.md §4.2.

#### T1.4 — Update `ml/audit_hooks.py` (delete 11 dead + add 3 WEB_*)

**Dead `AuditEventType` values to DELETE** (verified during audit; cross-ref D14 in repo's git history at commits 6654877 + b8f62e3):

```
- DATA_TRANSFERRED
- DATA_QUARANTINED
- DATA_DELETED
- ACCESS_GRANTED
- ACCESS_REVOKED
- ATTESTATION_SIGNED
- ENCRYPTION_APPLIED
- DECRYPTION_APPLIED
- CHECKSUM_VERIFIED
- CHECKSUM_FAILED
- INTEGRITY_VIOLATION  (NOTE: this name is being REUSED below — see Q15.A correlation-ID; the deletion-then-re-addition is intentional schema cleanup)
```

**NEW `WEB_*` values to ADD in the same commit:**

```
- WEB_PREDICT_RECEIVED
- WEB_PREDICT_RETURNED
- WEB_RATE_LIMIT_HIT
- WEB_PRESET_LOADED            (used by pages/01_predict.py preset-button click)
- AUDIT_EXPORT_REQUESTED       (used by app/audit_export.py export_audit_to_csv())
- INTEGRITY_VIOLATION          (re-added with NEW semantics — Q15.A correlation-ID error path)
```

**Net delta:** -8 enum values (10 deleted unique + 1 deleted-then-re-added with new semantics; 5 added net of the re-add).

**Implementation steps:**
1. Edit `ml/audit_hooks.py` (or `ml/data/audit_trail.py`, depending on where `AuditEventType` enum lives — verify with `grep -rn "class AuditEventType" --include="*.py"`).
2. Delete the 10 unique dead values + the old `INTEGRITY_VIOLATION` definition.
3. Add the 5 new values + the re-added `INTEGRITY_VIOLATION` (with updated semantics for Q15.A correlation-ID error path).
4. Run `grep -rn "AuditEventType.\(DATA_TRANSFERRED\|DATA_QUARANTINED\|DATA_DELETED\|ACCESS_GRANTED\|ACCESS_REVOKED\|ATTESTATION_SIGNED\|ENCRYPTION_APPLIED\|DECRYPTION_APPLIED\|CHECKSUM_VERIFIED\|CHECKSUM_FAILED\)" --include="*.py" .` — must return zero matches in production code (test files may have stale references; delete those assertion lines).
5. Bump schema version field in audit.jsonl genesis entry to `"2"`.
6. Run `pytest tests/test_audit_integration.py tests/test_irb_gate.py -v` — must stay green.
- **Acceptance:** `pytest tests/test_audit_integration.py -v` → all green. `pytest -q --collect-only | tail -3` shows test count unchanged or +1 from any new audit-emit test.
- **Verification:** `pyright ml/audit_hooks.py` → 0 new errors vs baseline.
- **Rollback:** `git checkout HEAD -- ml/audit_hooks.py` (the `b8f62e3` baseline).
- **Commit:** `refactor(4.5.1): AuditEventType cleanup (-11 dead) + 3 new WEB_* + AUDIT_EXPORT_REQUESTED`. Closes: Q7.A, Q7.C. Refs: PHASE_4_5_PLAN.md §4.2.

#### T1.5 — Create `app/audit_export.py`

- Create `app/audit_export.py` with `export_audit_to_csv()` and `verify_csv_chain_integrity()` per §2.4 spec.
- **Acceptance:** `python -c "from app.audit_export import export_audit_to_csv, verify_csv_chain_integrity; print('OK')"` prints `OK`.
- **Verification:** `pyright app/audit_export.py` → 0 errors.
- **Rollback:** `rm app/audit_export.py`.
- **Commit:** `feat(4.5.1): app/audit_export.py with CSV export + hash-chain round-trip verifier`. Closes: Q13.A. Refs: PHASE_4_5_PLAN.md §4.2.

#### T1.6 — Create `pages/01_predict.py`

- Create directory `pages/`.
- Create `pages/01_predict.py` per §2.5 spec (full form + 3 preset buttons + result rendering with 4 badges + D18 banner gating + IRB_BYPASS branches + correlation-ID error handling + session-state debounce).
- **Acceptance:** `streamlit run pages/01_predict.py --server.headless true` boots without exception (kill after 5s with `pkill -f "streamlit run"` if no other check).
- **Verification:** `pyright pages/01_predict.py` → 0 new errors. AppTest boot in <5s (closure gate criterion #3).
- **Rollback:** `rm pages/01_predict.py`.
- **Commit:** `feat(4.5.1): pages/01_predict.py with form + 3 presets + 4 badges + D18 banner + IRB_BYPASS branches`. Closes: Q3, Q4.A, Q4.C, Q11.A, Q12.A, Q12.C, Q15.A, Q15.B, Q15.D, Q15.5.A, plus IRB_BYPASS gate criterion #6. Refs: PHASE_4_5_PLAN.md §4.2.

#### T1.7 — Create `tests/test_pages_predict.py` (18 tests)

**The 18 tests to implement** (verbatim enumeration; one-line description per test):

```
1.  test_module_imports_cleanly                          — `import pages.predict` succeeds without exceptions
2.  test_form_renders_8_widgets                          — AppTest verifies 8 widgets present (age, csf_glucose, csf_protein, csf_wbc, pcr, microscopy, exposure, symptoms)
3.  test_form_uses_neutral_defaults                      — verify age=12, csf_glucose=65.0, csf_protein=30.0, csf_wbc=3, pcr=False, microscopy=False, exposure=False, symptoms=[]
4.  test_neutral_defaults_predict_low_p_high_lt_001      — submit with neutrals, assert p_high < 0.001 (sanity gate per Q11.A)
5.  test_three_preset_buttons_render                     — assert 3 buttons with labels matching PRESETS keys
6.  test_loading_high_risk_pam_preset_populates_form     — click button, verify session state updated for all 8 input fields
7.  test_submit_calls_infer_one_with_built_row           — mock `infer_one`, verify dict shape passed (8 keys, correct types)
8.  test_no_submit_returns_early                         — no `infer_one` call when submit not pressed
9.  test_filenotfounderror_renders_graceful_banner       — mock `infer_one` to raise FNFE, assert yellow warning banner present, assert Run button disabled
10. test_uncaught_exception_emits_correlation_id_audit   — mock to raise generic Exception, assert INTEGRITY_VIOLATION event with error_id metadata + 12-char display
11. test_double_submit_within_30s_blocked                — set st.session_state.predicting=True, submit again, assert no new infer_one call
12. test_stale_lock_recovers_after_30s                   — set predicting_at to 31s ago, submit, assert infer_one called
13. test_decision_badge_renders_with_icon_and_bold       — strip color tags, assert icon + bold present
14. test_decision_badge_color_blind_safe                 — same as above but parametrized over all 4 prediction states (High, Low, Moderate, ABSTAIN)
15. test_t_027_badge_renders_with_tooltip                — assert badge + hover tooltip text present (verbatim Q3 tooltip)
16. test_smallcalibrationwarning_fires_for_n_below_30    — mock output with n_cal=6, assert yellow warning rendered
17. test_three_state_regime_badge_invalid_at_n6_alpha010 — assert 🔴 INVALID badge present (k=7 > n=6 → INVALID)
18. test_d18_limitation_banner_only_on_bacterial_preset  — set active_preset to bacterial, assert banner; set to others, assert no banner
```

- **Acceptance:** `pytest tests/test_pages_predict.py -v` → 18/18 green (or 17/18 + 1 xfail if any test gets xfail-decorated for known-flaky reason).
- **Verification:** Cumulative test count = 1233 + 18 (or +20 from T1.4 audit-emit tests).
- **Rollback:** `rm tests/test_pages_predict.py`.
- **Commit:** `test(4.5.1): test_pages_predict.py with 18 tests covering form + presets + error paths + IRB_BYPASS`. Closes: Q11.A, Q12.A, Q12.C, Q15.A-D. Refs: PHASE_4_5_PLAN.md §4.3.

#### T1.8 — Create `tests/test_app_presets.py` (20 tests) + `tests/test_app_disclaimer.py` (12 tests) + `tests/test_audit_export.py` (10 tests)

**`tests/test_app_presets.py` — 20 tests** (3 presets × 5 per-preset assertions + 5 cross-preset tests):

```
Per preset (parametrized for high_risk_pam, bacterial_meningitis_limitation, normal_csf):
  1.  test_preset_dict_has_all_required_fields[<preset>]      — schema check: label, description, inputs, current_behavior, limitation_banner present
  2.  test_preset_inputs_has_all_8_features[<preset>]         — age, csf_glucose, csf_protein, csf_wbc, pcr, microscopy, exposure, symptoms all present
  3.  test_preset_current_behavior_has_snapshot_date[<preset>] — current_behavior contains snapshot_date="2026-04-26"
  4.  test_preset_load_populates_form[<preset>]               — submit triggers infer_one with exact built_row from preset.inputs
  5.  test_preset_live_snapshot_matches[<preset>]              — actual infer_one output matches current_behavior.prediction (xfail decorator on bacterial)
  → 5 × 3 = 15 parametrized tests

Plus 1 special xfail test (per Q12.B):
  16. test_preset_bacterial_limitation_returns_high            — @pytest.mark.xfail(strict=False, reason="D18 limitation: ...") — Phase 6 fix triggers XPASS

Plus 4 cross-preset tests:
  17. test_three_presets_total_count                            — len(PRESETS) == 3
  18. test_preset_keys_are_snake_case                           — all keys match r"^[a-z_]+$"
  19. test_only_bacterial_has_limitation_banner_true            — exactly 1 preset has limitation_banner=True
  20. test_all_presets_have_snapshot_date_2026_04_26            — every current_behavior.snapshot_date is the locked date
```

**`tests/test_app_disclaimer.py` — 12 tests:**

```
1.  test_disclaimer_text_contains_5_mandatory_tokens          — "NOT a medical device", "n=30", "limited to", "ORCID", "lmontenegrocalla@mail.weber.edu" all in DISCLAIMER_TEXT
2.  test_disclaimer_link_targets_are_https                    — no "javascript:" or "http://" URLs in disclaimer
3.  test_orcid_format_regex                                   — ORCID matches r"\d{4}-\d{4}-\d{4}-\d{4}"
4.  test_email_format_regex                                   — email matches RFC 5322 simplified regex
5.  test_disclaimer_on_every_page                             — parametrize over 4 pages, assert 5 tokens render on each (Mini-1 covers 1 page; Mini-2 expands to 4)
6.  test_wcag_aa_contrast_error_combo                         — wcag_contrast_ratio("#B71C1C", "#FFEBEE") >= 4.5 (computed: 7.18:1)
7.  test_wcag_aa_contrast_info_combo                          — wcag_contrast_ratio("#0D47A1", "#E3F2FD") >= 4.5 (computed: 8.21:1)
8.  test_wcag_aa_contrast_success_combo                       — wcag_contrast_ratio("#1B5E20", "#E8F5E9") >= 4.5 (computed: 7.59:1)
9.  test_widget_keys_unique_across_pages                      — collect all key= values across 4 pages, assert set length == list length (Q15.5.B)
10. test_reduced_motion_css_block_present                     — assert _INJECTED_CSS contains "prefers-reduced-motion" string
11. test_utils_fmt_metric_handles_nan                         — _fmt_metric({"x": float("nan")}, "x") returns "—"
12. test_utils_fmt_metric_handles_inf                         — _fmt_metric({"x": float("inf")}, "x") returns "—"
```

**`tests/test_audit_export.py` — 10 tests:**

```
1.  test_export_returns_bytes                                 — export_audit_to_csv() returns bytes type
2.  test_export_csv_has_required_columns                      — parse CSV, assert columns: timestamp, event_type, previous_hash, current_hash, schema_version
3.  test_export_preserves_all_rows                            — write 10 events, export, count rows = 10
4.  test_round_trip_hash_chain_byte_equal                     — write 10 → export → re-parse → byte-equal hash chain (Mini-1 closure gate criterion #4)
5.  test_verify_csv_chain_integrity_pass                      — round-trip + verify_csv_chain_integrity returns True
6.  test_verify_csv_chain_integrity_fail_on_tamper            — modify one row's metadata, verify returns False
7.  test_export_filename_format                               — filename matches f"amoebanator_audit_{session_id}_{ISO_timestamp}.csv" pattern
8.  test_export_handles_empty_log                             — export empty JSONL returns CSV with header row only
9.  test_export_preserves_metadata_json                       — nested metadata JSON survives round-trip
10. test_export_emits_audit_event                             — calling export_audit_to_csv emits AuditEventType.AUDIT_EXPORT_REQUESTED
```

- **Acceptance:** `pytest tests/test_app_*.py tests/test_audit_export.py -v` → 42/42 green (1 xfail for bacterial-limitation in test_app_presets).
- **Verification:** Cumulative test count ≥ 1233 + 18 + 42 = 1293.
- **Rollback:** `rm tests/test_app_presets.py tests/test_app_disclaimer.py tests/test_audit_export.py`.
- **Commit:** `test(4.5.1): test_app_presets + test_app_disclaimer + test_audit_export (42 tests, 1 xfail)`. Closes: Q12.B, Q19.B, Q15.5.A, Q15.5.B, Q15.5.D, Q13.A. Refs: PHASE_4_5_PLAN.md §4.3.

#### T1.9 — Create `.streamlit/config.toml` + `tests/_snapshots/predict.md.snap`

- Create `.streamlit/config.toml` with verbatim content from §2.10.
- Run AppTest against `pages/01_predict.py`, capture `result.markdown` to `tests/_snapshots/predict.md.snap`.
- **Acceptance:** `cat .streamlit/config.toml` shows port=8501. `cat tests/_snapshots/predict.md.snap` shows captured markdown.
- **Verification:** No deprecation warnings on `streamlit run`.
- **Rollback:** `rm -rf .streamlit/ tests/_snapshots/`.
- **Commit:** `feat(4.5.1): .streamlit/config.toml (port 8501, neutral-medical theme) + visual snapshot baseline`. Closes: Q16.b, Q16.c, Mini-1 closure gate #7. Refs: PHASE_4_5_PLAN.md §4.4.

### 3.3 Mini-1 closure protocol

After T1.9, run all 7 closure gates IN ORDER. On any gate fail: STOP, report, await Jordan's direction.

```bash
# Gate 1: Test count + pass rate (≥1280 collected, 0 fail/0 error, ≤5 xfails)
pytest -q 2>&1 | tail -10
# Expected: ">=1280 passed, 0 failed, 0 errors, <=5 xfailed"

# Gate 2: Pyright purity (0 new errors/warnings vs b8f62e3 baseline)
pyright 2>&1 | tail -5 > /tmp/pyright_mini1.txt
diff /tmp/pyright_baseline.txt /tmp/pyright_mini1.txt
# Expected: no new errors/warnings

# Gate 3: AppTest boot <5s
time python -c "from streamlit.testing.v1 import AppTest; t = AppTest.from_file('pages/01_predict.py'); t.run(timeout=10)"
# Expected: real time <5s

# Gate 4: CSV audit export round-trip hash-equal
pytest tests/test_audit_export.py::test_round_trip_hash_chain_byte_equal -v
# Expected: PASSED

# Gate 5: Disclaimer presence on every page (parametrized canonical test)
pytest tests/test_app_disclaimer.py::test_disclaimer_on_every_page -v
# Expected: PASSED (parametrized for 1 page in Mini-1, expanded to 4 in Mini-2)

# Gate 6: IRB_BYPASS branches both green
AMOEBANATOR_IRB_BYPASS=1 pytest tests/test_pages_predict.py -k irb -v
AMOEBANATOR_IRB_BYPASS=0 pytest tests/test_pages_predict.py -k irb -v
unset AMOEBANATOR_IRB_BYPASS
# Expected: both PASSED

# Gate 7: Visual regression text-snapshot drift <5% chars
pytest tests/test_pages_predict.py::test_visual_snapshot_baseline -v
# Expected: PASSED (drift below 5% threshold)
```

If all 7 green: announce Mini-1 closure to Jordan, await explicit "go Mini-2" before continuing. **Do NOT auto-proceed.**

---

## §4. Mini-2 Execution Protocol

### 4.1 Pre-Mini-2 verification

Verify cumulative test count from Mini-1 close is intact:

```bash
pytest --collect-only -q 2>&1 | tail -3
# Expected: ≥1284 tests (1233 Mini-1 baseline + ~51 from Mini-1 closure)
```

If count regressed, investigate before proceeding.

### 4.2 Mini-2 task list

#### T2.1 — Update `ml/audit_hooks.py` schema if needed (no-op if already done in T1.4)

#### T2.2 — Create `pages/02_audit.py`

- Per §2.6 spec.
- **Acceptance:** `streamlit run pages/02_audit.py --server.headless true` boots; CSV download button present.
- **Commit:** `feat(4.5.2): pages/02_audit.py with st.table + 10k cap + CSV download`. Closes: Q13.B, Q15.C, Q15.5.C. Refs: PHASE_4_5_PLAN.md §5.2.

#### T2.3 — Create `pages/03_about.py`

- Per §2.7 spec including `|w_i|` panel + α slider + username-mismatch one-liner.
- **Acceptance:** `streamlit run pages/03_about.py --server.headless true` boots; `|w_i|` bar chart visible; α slider responds.
- **Commit:** `feat(4.5.2): pages/03_about.py with |w_i| panel + α slider + handle disclosure`. Closes: Q4.A (slider), Q17.A, Q17.B, Q17.C, Q19.D (one-liner). Refs: PHASE_4_5_PLAN.md §5.2.

#### T2.4 — Create `pages/04_references.py`

- Per §2.8 spec.
- **Commit:** `feat(4.5.2): pages/04_references.py with 22 refs grouped by category`. Closes: Q8.C. Refs: PHASE_4_5_PLAN.md §5.2.

#### T2.5 — Create `app/app.py` (st.navigation entry)

- Per §2.9 spec.
- **Acceptance:** `streamlit run app/app.py` boots, all 4 pages navigable in sidebar.
- **Commit:** `feat(4.5.2): app/app.py with st.navigation registering 4 pages`. Closes: Q14 (multi-page). Refs: PHASE_4_5_PLAN.md §5.2.

#### T2.6 — Create remaining 4 test files

- `tests/test_pages_audit.py` (~12 tests), `tests/test_pages_about.py` (~10 tests), `tests/test_pages_references.py` (~8 tests), `tests/test_app_navigation.py` (~10 tests).
- **Acceptance:** `pytest tests/test_pages_*.py tests/test_app_navigation.py -v` → ~40/40 green.
- **Commit:** `test(4.5.2): 4 new test files (~40 tests) for Mini-2 pages + nav`. Closes: Mini-2 closure gate #1. Refs: PHASE_4_5_PLAN.md §5.3.

#### T2.7 — Update `.dockerignore` (Subphase 4.5.4 work)

- Add `outputs/audit/` to `.dockerignore`.
- Smoke test: first prediction on a fresh container emits genesis entry (no inherited entries from dev machine).
- **Commit:** `chore(4.5.4): .dockerignore outputs/audit/ + cold-start smoke test`. Closes: Q13.C. Refs: PHASE_4_5_PLAN.md §5.2.

### 4.3 Mini-2 closure protocol

Same 7 gates as Mini-1 (§3.3) + cumulative test count ≥1320. Visual snapshot baseline expanded to 4 page snapshots.

On all gates green: announce Mini-2 closure to Jordan. Sprint complete. Hand off to USER ASSIGNMENT Step 7 (Vercel link-out) per §7.

---

## §5. Standing Instructions

These apply throughout Mini-1 and Mini-2 execution. Re-read before each task.

### 5.1 Strikethrough + ✓ done-marker convention (mandatory every turn)

At the start of every response, output a progress block in this exact format:

```
📂 WORKING ON: <filename> — <section/task being executed>

✅ DONE (this mini):
  ~~T1.1 app/utils.py~~ ✓ — <one-line summary>
  ~~T1.2 app/presets.py~~ ✓ — <one-line summary>

🔄 IN PROGRESS:
  T1.3 — <what you're writing/testing right now>

⏳ PENDING (this mini):
  T1.4 — <pending>
  T1.5 — <pending>

📋 OVERALL SPRINT:
  ~~Mini-1~~ ✓ (or % progress)
  Mini-2 — pending
```

This is non-negotiable. Jordan needs to scan progress without re-reading the full conversation.

### 5.2 Pause for user vote at each Mini boundary

After Mini-1 closure (all 7 gates green): announce closure, list any deviations from spec, await explicit "go Mini-2" from Jordan. **Do NOT auto-proceed.** Mini-2 may need adjustments based on what Mini-1 surfaced.

### 5.3 NO scope creep

If a "nice-to-have" surfaces mid-sprint (e.g., "we should also add a dark mode," "what if we cached this," "this would be cleaner with a class hierarchy"):

1. Log to `docs/FUTURE_WORK.md` (create file if it doesn't exist) with: date, source task, one-paragraph description, why deferred.
2. Continue current task as specified.

The scope is locked. The audit took 22 questions to lock it. Re-opening it during sprint execution defeats the audit's purpose.

### 5.4 Test commits separate from feature commits

Per Q16.a convention: feature changes commit as `feat(...)`, test additions commit as `test(...)`. Combining them in a single commit is acceptable for tiny changes (e.g., a feature with 1 trivial test) but the default is separate commits. Reason: separate commits make `git revert <feat-commit>` clean — you don't lose the test infrastructure.

### 5.5 Closes/Refs footer on every commit

Every commit closing a Q-decision MUST include `Closes: Q<N>.<sub>, ...` and `Refs: PHASE_4_5_PLAN.md §<section>` in the footer. Reviewers running `git log --grep="Q11.A"` find the implementing commit; running `git log --grep="§4.2"` find the spec-anchor.

### 5.6 On user pushback: stop, gather evidence, propose 3 options, await vote

Same pattern Jordan used during the audit. If Jordan says *"stop, that's not what I meant"* or *"that's wrong"* or *"why are you doing it that way"*:

1. Stop the current task.
2. Gather evidence (read the relevant files, run any necessary diagnostics, cite path:line).
3. Propose 3 options labeled (a)/(b)/(c) with trade-offs.
4. Recommend one with one-paragraph rationale.
5. Await Jordan's vote.

**Do NOT silently change direction.** The 3-option pattern surfaces the assumption space so Jordan can make an informed choice.

### 5.7 No git push --force; no --no-verify; no --amend on shared commits

Branch is `main`. Commits land directly. Force-push to main is forbidden. `--no-verify` (skip hooks) is forbidden — if a hook fails, fix the root cause. `--amend` is forbidden on commits already in the local history (creates a new SHA, breaks any in-flight reference). Always create new commits.

### 5.8 Spanish-friendly framing in conversational responses

Code, paths, file content, commits, test names: English. Conversational text to Jordan: Spanish-friendly framing fine. Examples:
- *"Dale, vamos con T1.4 ahora."* ✓
- *"T1.4 done; pasando a T1.5."* ✓
- *"Vamos a flipear el bool a int."* ✓ (Spanglish acceptable)

But the actual `def flip_bool_to_int():` stays English in the code.

---

## §6. Failure Recovery

Eight documented failure modes with recovery procedures. Read this section before starting; refer back if any fire.

### 6.1 Pyright catches a new error

**Symptom:** `pyright` returns non-zero new errors against `/tmp/pyright_baseline.txt`.

**Recovery:**
1. Read the error. Categorize:
   - **Real type bug:** fix at root (correct the type annotation, narrow the type, etc.).
   - **Streamlit dynamic-attribute access** (e.g., `st.session_state.foo`): rewrite as bracket access `st.session_state["foo"]` if possible. If bracket-style is awkward (e.g., `st.session_state.update({...})`), add inline `# pyright: ignore[reportAttributeAccessIssue]` with a comment explaining why.
   - **Third-party library missing stubs:** add `# pyright: ignore[reportMissingTypeStubs]` with comment.
2. Re-run pyright; verify count matches baseline.
3. Do NOT loosen `pyrightconfig.json` project-wide — use targeted ignores only.

### 6.2 AppTest boot exceeds 5s

**Symptom:** Closure gate criterion #3 fails (`time python -c "..."` shows wall-time >5s).

**Recovery:**
1. Profile imports: `python -X importtime pages/01_predict.py 2>&1 | tail -50`.
2. Identify the slowest import (likely `streamlit`, `torch`, or `pandas`).
3. Defer non-critical imports to function-local scope (e.g., move `import pandas` from module level into `export_audit_to_csv()`).
4. If still >5s, the AppTest closure gate measures local boot, not HF cold-start (HF is acknowledged 30s per Q18.A). Document the local-vs-HF distinction in the test docstring and adjust the AppTest threshold if needed (with explicit justification).

### 6.3 Visual snapshot drift on intentional change

**Symptom:** Closure gate criterion #7 fails because page markdown changed >5% from baseline, but the change is intentional.

**Recovery:**
1. Inspect the diff: `pytest -v --snapshot-diff tests/test_pages_predict.py`.
2. Confirm the diff is intentional (e.g., you added a new disclaimer line).
3. Regenerate baseline: `pytest --snapshot-update tests/test_pages_predict.py`.
4. Commit the updated `.snap` file: `chore(4.5.x): regenerate visual snapshot for <reason>`.
5. Re-run gate; expect green.

### 6.4 Test count regression

**Symptom:** `pytest --collect-only -q` shows fewer tests than expected.

**Recovery:**
1. Diff against last known-good count: `git log --oneline | head -10` find the last commit where count was correct.
2. Bisect the test count change: `git bisect start` against the commit range.
3. Identify the deletion (likely a `.py` file removed or test renamed).
4. Restore: either `git checkout <good-sha> -- <file>` OR rewrite the test if it was an intentional removal that broke count math.

### 6.5 HF Space deploy fails ("Build failed: no health check response")

**Symptom:** `git push hf main` succeeds, but HF Space build log shows `health check timeout`.

**Recovery:**
1. Verify Dockerfile: `grep -E "EXPOSE|server.port" Dockerfile`. MUST show `EXPOSE 8501` and `--server.port=8501`.
2. Verify `.streamlit/config.toml`: MUST have `port = 8501` in `[server]` section.
3. If both are 8501 and still failing: HF Space template may have been updated. Re-clone the Space repo (`git clone https://huggingface.co/spaces/luisjordanmontenegro/amoebanator-25 /tmp/hf-space`) and inspect the auto-generated Dockerfile + README for the current expected port.
4. Match local config to HF auto-template, re-push.

### 6.6 `st.cache_resource` staleness

**Symptom:** Changes to cached function don't take effect; old behavior persists.

**Recovery:**
1. Restart the Streamlit kernel: in Streamlit UI, press `R` (rerun) then `C` (clear cache).
2. Programmatically: `st.cache_resource.clear()` at top of page (temporary; remove before commit).
3. If cache persists across kernel restart: HF Space container restart needed (`gh-space-restart` if `gh-spaces` CLI installed; otherwise edit any file and push to trigger re-deploy).

### 6.7 IRB_BYPASS env var not propagating to HF Space

**Symptom:** `AMOEBANATOR_IRB_BYPASS=1` set locally works fine; deployed Space hits `IRBGateBlocked` on cold-start.

**Recovery:**
1. Verify Dockerfile: `grep AMOEBANATOR_IRB_BYPASS Dockerfile`. MUST show `ENV AMOEBANATOR_IRB_BYPASS=1` (not just commented-out reference).
2. If Dockerfile has it: HF Space may have ENV cleared by Space-level secret override. Check Space settings → Variables tab: `AMOEBANATOR_IRB_BYPASS` should NOT be present (Space secrets override Dockerfile ENV when set). If present and set to `0`, delete the Space-level override OR set to `1` explicitly.
3. Verify the multi-line safety comment is intact in Dockerfile — accidentally deleting the comment block during edit may have removed the ENV line too. The verbatim comment block that MUST precede the `ENV AMOEBANATOR_IRB_BYPASS=1` line:

```dockerfile
# AMOEBANATOR_IRB_BYPASS — IRB gate bypass switch
#
# WHY THIS EXISTS:
#   The Phase 4.5 demo trains on n=30 synthetic patient vignettes derived from
#   published case-series marginals (Yoder 2010, Cope 2016, CDC 2025). No real
#   PHI, no human subjects. Hence no IRB review is required — but the IRB gate
#   in ml/irb_gate.py refuses to boot the app without an IRB JSON record. This
#   bypass env var short-circuits the gate WITH a mandatory audit log emission
#   (AuditEventType.IRB_STATUS_CHANGE → actor="env_var") so the bypass is
#   never silent.
#
# WHEN TO FLIP TO 0:
#   Phase 6 lands real MIMIC-IV cohort (target n>=200, includes bacterial vs
#   viral meningitis labels). MIMIC-IV is PhysioNet-credentialed PHI, requires
#   Weber State IRB exempt determination (USER_ASSIGNMENTS Step 2). When that
#   IRB record exists at outputs/governance/irb_record.json with irb_status in
#   {approved, conditionally_approved}, flip this to 0 AND remove the bypass
#   audit emission code path.
#
# CHECKLIST BEFORE FLIPPING:
#   [ ] outputs/governance/irb_record.json exists
#   [ ] irb_status field == "approved" or "conditionally_approved"
#   [ ] expiration_date is in the future
#   [ ] All MIMIC-IV cohort code paths emit AuditEventType.PHI_ACCESS events
#   [ ] tests/test_irb_gate.py::test_real_phi_path_requires_irb_record passes
#
ENV AMOEBANATOR_IRB_BYPASS=1
```

If the comment block above is missing or truncated in the deployed Dockerfile, restore it verbatim. The 5 bullets in CHECKLIST BEFORE FLIPPING are the load-bearing safety check — flipping to 0 without all 5 satisfied risks booting the app without a valid IRB record (which is a real-world compliance violation, not just a test failure).

### 6.8 Audit JSONL corruption (hash chain broken)

**Symptom:** `verify_chain()` returns `TAMPERED` mid-session.

**Recovery:**
1. Identify the first broken row: `python -c "from ml.data.audit_trail import verify_chain; verify_chain('outputs/audit/audit.jsonl', verbose=True)"`.
2. If corruption is in the most recent N rows (likely cause: container OOM-killed mid-write): truncate to the last good checkpoint via `head -n <last_good_line> outputs/audit/audit.jsonl > /tmp/audit_recovered.jsonl && mv /tmp/audit_recovered.jsonl outputs/audit/audit.jsonl`.
3. If corruption is older: the chain is unrecoverable in-place. Archive the corrupted file (`mv outputs/audit/audit.jsonl outputs/audit/audit.corrupted.<timestamp>.jsonl`) and start fresh.
4. Document the incident in `docs/SPRINT_LOG.md` (or sprint's equivalent log).

### 6.9 (Bonus) HF Space sleep wipes audit chain mid-session

**Symptom:** User runs predictions, leaves browser open, returns 60 minutes later. HF Space went idle, restarted, audit log wiped. User tries to download CSV and gets only events from after the restart.

**Recovery:**
1. **There is no recovery.** Pre-sleep audit chain is gone. This is the documented behavior (Q13.A: append-only ephemeral).
2. Mitigation for future: the disclaimer at Q9.1 caption already warns "*cold-start ~30s on first visit after idle period*." Update if needed to also say "*audit log wipes on idle restart; download CSV before stepping away if persistence matters*."
3. Add to `pages/02_audit.py` banner if not already present: "*Use 'Download session audit log' BEFORE stepping away from the demo for >30 minutes — HF free-tier idle restart wipes the in-session log.*"

---

## §7. Phase J Outputs Reference

These docs exist; consult ONLY if context lost mid-sprint:

- **`docs/AUDIT_REPORT.md`** (1,062 lines) — reviewer-grade per-Q evidence + rationale + D1-D18 cross-cutting findings. Consult when you need the WHY behind a §2 spec.
- **`docs/PHASE_4_5_PLAN.md`** (1,000 lines) — locked specs in tabular form + risk register + user assignments. Consult when you need the full risk-register or out-of-scope punchlist.
- **`docs/INFORMATION_RECAP.md`** (pending Doc 4) — narrative knowledge transfer for humans. Consult when you need the human-readable backstory.

**If you find yourself reading any of these mid-sprint, you've drifted.** This prompt is supposed to be self-contained. Return to §2-§4 and continue.

The companion docs are escape hatches, not load-bearing references.

---

## §8. End-of-Sprint Handoff

After Mini-2 closure (all 7 gates green + cumulative ≥1320 tests):

### 8.1 Final commit message template

```
release(4.5): Mini-1 + Mini-2 complete; 4-page Streamlit app deployable to HF Spaces

Closes Phase 4.5 sprint. All 7 closure gates green for Mini-1 and Mini-2.
Cumulative test count: <N> (≥1320). Pyright clean. AppTest boot <5s.
CSV audit export round-trip verified. Disclaimer on every page. IRB_BYPASS
branches both green. Visual regression baselines for 4 pages committed.

Closes: Phase 4.5 sprint
Refs: PHASE_4_5_PLAN.md §1, AUDIT_REPORT.md §1
```

### 8.2 HF Space deploy command (Jordan executes; Claude does NOT)

After the release commit lands on `main`:

```bash
# Add HF remote if not already present
git remote add hf https://huggingface.co/spaces/luisjordanmontenegro/amoebanator-25 \
  || git remote set-url hf https://huggingface.co/spaces/luisjordanmontenegro/amoebanator-25

# Push to HF (triggers Space rebuild)
git push hf main

# Wait ~3-5 minutes for build; check status
gh-spaces status luisjordanmontenegro/amoebanator-25 \
  || curl -s https://huggingface.co/api/spaces/luisjordanmontenegro/amoebanator-25 | jq .runtime.stage
```

Smoke test post-deploy:
- Open `https://huggingface.co/spaces/luisjordanmontenegro/amoebanator-25` in browser
- Click each preset, run inference, verify result renders
- Click Audit page, click "Download session audit log (CSV)"
- Verify CSV downloads and opens in Excel/pandas

### 8.3 Post-sprint memory updates required

Claude MUST update its memory system at sprint close:

- **project memory:** `phase_4_5_complete.md` — note Mini-1 + Mini-2 shipped, 7 gates green, cumulative test count, deploy URL, sha of release commit.
- **feedback memory:** add any new patterns surfaced during sprint execution (e.g., "Streamlit AppTest cold-boot consistently <4s on local; HF cold-boot is 30s — separate the two thresholds in tests").
- **reference memory:** if any new external doc was consulted (HF Spaces docs, Streamlit changelog), record the URL + what was learned.

### 8.4 Phase 5 entry conditions

Phase 5 cannot start until:
1. Mini-1 + Mini-2 commits landed on `main`.
2. HF Space deploy successful.
3. Vercel `/playground` link-out updated (USER ASSIGNMENT Step 7).
4. medRxiv preprint draft initiated (separate work product, parallel to Phase 5 sprint).

Phase 5 introduces real-data dependencies (PhysioNet credentialing, Weber State IRB exemption — both blocked on USER ASSIGNMENTS Steps 1-2). Phase 5 will revisit: i18n / Spanish disclaimer, mobile-responsive layout, image-diff visual regression.

---

**END OF SPRINT PROMPT.** Begin Mini-1 with T1.1 (`app/__init__.py` + `app/utils.py`) per §3.2. Apply the strikethrough + ✓ progress block from §5.1 starting your first response.
