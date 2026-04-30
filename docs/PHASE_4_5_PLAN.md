# Phase 4.5 Plan, Locked Sprint Specification

**Author:** Jordan Montenegro-Calla (ORCID 0009-0000-7851-7139)
**Locked:** 2026-04-27
**Version:** v1.0
**Supersedes:** none (first formal sprint plan after Phase 4.5 PRE-FLIGHT discovery audit)
**Companion docs:**
- `docs/AUDIT_REPORT.md`, reviewer-grade evidence + per-Q rationale (1,062 lines)
- `docs/PHASE_4_5_PROMPT_FINAL.md`, sprint-trigger prompt for fresh Claude Code session (pending)
- `docs/INFORMATION_RECAP.md`, narrative knowledge transfer for humans (pending)
- `docs/USER_ASSIGNMENTS.md`, out-of-band actions Jordan executes (updated at Phase J)

This document is the locked specification for the Phase 4.5 web-layer sprint. Every spec here is imperative ("MUST do X with parameters Y"), not narrative. The audit's evidence and rationale lives in `AUDIT_REPORT.md`; this doc is what the sprint executes against. If a sprint commit deviates from anything in this plan, the deviation is a bug, not a judgment call.

**Scope at a glance.** Two minis totaling ~950 LOC + ~90 new tests. Mini-1 (~600 LOC + ~50 tests) ships the form, presets, disclaimer, and audit utilities. Mini-2 (~350 LOC + ~40 tests) ships the audit page, about page, references page, and multi-page navigation. Deploy target: Hugging Face Spaces, Streamlit Docker SDK, free CPU Basic. Test gate: Mini-1 ≥1280 collected / Mini-2 ≥1320 cumulative, with 7 closure criteria each.

---

## §1. Sprint Goals & Non-Goals

### 1.1 Goals (must-ship)

The sprint is scoped against five must-ship goals. If any one slips, the sprint does NOT close, it stops, reports, and waits for direction.

1. **Multi-page Streamlit app deployable to HF Spaces free tier.** Four pages (Predict, Audit, About, References) navigable via `st.navigation`. Cold-boot to first prediction within 30s on free CPU Basic. Container-restart-resilient (no race condition between audit hooks and model load).

2. **Four clinical presets demonstrating model behavior + limitations.** Three buttons + neutral default state (Q12.A locked). Three presets: PAM-positive (`high_risk_pam`), bacterial-NOT-PAM limitation demo (`bacterial_meningitis_limitation`, D18 honesty banner), normal CSF negative control (`normal_csf`). Plus the page-load NEUTRAL state which functions as a fourth scenario.

3. **Disclaimer on every page.** Locked variant (ii) text from Q19.A: *"⚠ Research prototype, NOT a medical device. Trained on n=30 synthetic patient vignettes (n_train=24, n_val=6); contains zero real PHI. Outputs are calibrated probabilities, **limited to** the n=30 training distribution, not diagnoses. Not for clinical decision support, not validated. Source + caveats: github.com/ljm234/amoebanator-25, Contact: lmontenegrocalla@mail.weber.edu (ORCID 0009-0000-7851-7139)"*. Enforced via parametrized canonical test over 4 pages.

4. **Audit log CSV export with hash-chain preservation.** In-UI `st.download_button` exports session audit log as CSV preserving `previous_hash` + `current_hash` chain pointers. Round-trip test (Mini-1 closure gate): write 10 events → export → re-parse → byte-equal hash chain.

5. **WCAG-AA contrast + `prefers-reduced-motion` compliance.** Five a11y sub-decisions from Q15.5 implemented: full-coverage badges (icon + weight + color), unique-key cross-page assertion, `st.table` for audit (screen-reader semantics), wash + border + deep-text CSS pattern (≥7.18:1 contrast), reduced-motion CSS injection.

### 1.2 Non-goals (explicit out-of-scope to prevent scope creep)

The following are explicitly NOT in scope for Phase 4.5. If any surfaces during sprint execution as "we should also...", the answer is "log to FUTURE_WORK.md and continue current task."

- **PHI handling beyond synthetic vignettes.** Real PHI is forbidden until Phase 6 (MIMIC-IV) lands an IRB-approved cohort.
- **Real EHR ingestion / FHIR endpoints.** Out of scope. The sprint's input is the form; no ingestion layer.
- **Multi-user authentication.** No login, no sessions, no per-user state. Streamlit's default single-user-per-tab model is sufficient.
- **Model retraining UI.** `model.pt` is frozen for the sprint. No retraining triggers in the UI.
- **Mobile-responsive layout.** Defer to Phase 5. Streamlit's default desktop-first layout is acceptable for the PI-skim-on-laptop target use case.
- **i18n / Spanish translation of disclaimer.** Defer to Phase 5. The sprint ships English-only; Spanish translation would double the disclaimer surface and the test matrix.
- **SHAP / per-prediction attribution.** Defer to Phase 6 (Q17.A locked). The `|w_i|` panel on About page is the honest substitute at n=30.
- **Persistent audit log storage.** Sprint accepts ephemeral; CSV export is the portability feature (Q13.A). Permanent storage requires paid HF hardware or external S3/Postgres, out of scope.
- **Real-time inference latency budget below 200ms.** Free-tier inference is ~100ms warm; 200ms p95 is the gate. Anything tighter requires caching infra not justified for n=30 model.
- **GitHub Actions cron warmup of HF Space.** Q18.A locked: passive accept 30s cold-start, no cron (HF ToS gray area). Documented in Q9.1 caption.

---

## §2. Locked Decisions (47 sub-decisions, restated as imperative specs)

This section restates every Q-decision from the audit as an imperative spec the sprint MUST satisfy. Legend: ~~strikethrough~~ ✓ rows = decision implemented during audit phase (commit landed or doc-only Phase J edit complete). Plain rows = pending sprint Mini-1 / Mini-2 / USER ASSIGNMENT.

### 2.1 Audit-phase decisions (already implemented)

| # | Decision | Implementation evidence |
|---|---|---|
| ~~Q1~~ ✓ | ~~`apex/` subdirectory MUST be moved to `~/Desktop/apex/` outside the repo. Git MUST be initialized fresh from this clean state.~~ | ~~commit `46f33c4` (baseline)~~ ✓ |
| ~~Q2~~ ✓ | ~~The canonical `MLP` class MUST live in `ml/model.py`. `ml/training.py`, `ml/training_calib_dca.py`, `ml/infer.py`, `tests/test_coverage_boost.py`, `scripts/fit_gates.py`, `scripts/run_ablation.py` MUST import via `from ml.model import MLP`. No duplicate class definitions anywhere.~~ | ~~commit `bed84df` (35 LOC new module + 7 import-site updates)~~ ✓ |
| ~~Q4.B~~ ✓ | ~~`scripts/conformal_fit_from_probs.py` MUST internally call `ml.conformal_advanced.compute_qhat`. The script MUST emit `SmallCalibrationWarning` when `n_cal < 100`. A test in `tests/test_conformal_fit_script.py` MUST assert the warning fires on the round-trip.~~ | ~~commit `67039e3` (+2 tests, 1229 → 1231)~~ ✓ |
| ~~Q5~~ ✓ | ~~The logit-energy OOD gate MUST use Liu 2020 canonical semantics: `if energy > tau_e: ABSTAIN reason="LogitEnergyAboveOODShift"`. The threshold MUST be fit at q=0.95. No reference to `LowEnergy` or `LogitEnergyBelowInDistFloor` may remain anywhere in the codebase.~~ | ~~commits `3fd05ed` (initial rename) + `b8f62e3` (math flip + final rename)~~ ✓ |
| ~~Q6~~ ✓ | ~~Hosting MUST be Hugging Face Spaces with Streamlit Docker SDK on free CPU Basic (16 GB RAM, 2 vCPU, ~50 GB ephemeral disk), public visibility. Space URL: `huggingface.co/spaces/luisjordanmontenegro/amoebanator-25`.~~ | ~~Pre-locked from prior conversation; Space exists~~ ✓ |
| ~~Q7.B~~ ✓ | ~~`tests/test_irb_gate.py` MUST contain assertions that `ml/irb_gate.py` emits `AuditEventType.ACCESS_DENIED` and `AuditEventType.IRB_STATUS_CHANGE` events.~~ | ~~commit `6654877` (+2 tests, 1231 → 1233)~~ ✓ |
| ~~Q8.A~~ ✓ | ~~`docs/references.bib` MUST contain entries for Tunkel 2004 (PMID 15494903) and Seehusen 2003 (PMID 14524396) covering the Q11 inline-tooltip buckets. Total entry count: 22.~~ | ~~commit `6f02a75` (+2 BibTeX entries + comment header)~~ ✓ |
| ~~Q10~~ ✓ | ~~`docs/USER_ASSIGNMENTS.md` MUST include the Vercel `/playground` step with: (Step 0) `pwd` + `git remote -v` cwd-verification guard, (Step 2) backup `cp page.tsx page.tsx.bak`, (Step 3) `echo "*.tsx.bak" >> .gitignore` + commit.~~ | ~~doc-only edit at Phase J (this PR)~~ ✓ |
| ~~Q11.A.fix~~ ✓ | ~~`ml/infer.py:232` MUST use `if energy > tau_e:` (NOT `<`). `ml/ood_combined.py:117-130` MUST use matching direction. Threshold re-fit at q=0.95. All 4 in-distribution clinical presets MUST NOT trigger the gate; OOD positive control MUST trigger it.~~ | ~~commit `b8f62e3` (math flip + 3 test fixture rewrites + 5-preset live re-verification table)~~ ✓ |
| ~~Q14~~ ✓ | ~~Sprint MUST be split as (B) split-after-predict-page: Mini-1 ~600 LOC + Mini-2 ~350 LOC. Mini-1 → Mini-2 transition requires explicit "go" from Jordan after all 7 closure gates green.~~ | ~~Locked spec~~ ✓ |
| ~~Q18.A~~ ✓ | ~~Cold-start MUST be passively accepted. NO GitHub Actions cron warmup. NO third-party uptime ping. The Vercel `/playground` button caption MUST disclose "cold-start ~30s on first visit after idle period."~~ | ~~Documented; no code change~~ ✓ |
| ~~Q18.B~~ ✓ | ~~`load_stats()` MUST NOT be wrapped in `@st.cache_resource`, existing `@lru_cache` is sufficient. The 3ms/call overhead is invisible vs HF proxy RTT.~~ | ~~No code change required~~ ✓ |
| ~~Q20~~ ✓ | ~~Mini-1 closure gate: ≥1280 tests collected, 0 fail/0 error, ≤5 documented xfails. Mini-2 closure gate: ≥1320 cumulative + same 7 criteria. CSV audit export round-trip stays in Mini-1.~~ | ~~Locked spec~~ ✓ |

### 2.2 Mini-1 decisions (sprint must implement)

| # | Decision | Implementation target |
|---|---|---|
| Q3 | A `T=0.27 (n=6)` badge MUST render next to calibrated `p_high` on the predict page result. Hover tooltip MUST explain that T<1 amplifies logits (atypical Guo 2017 direction) and is fit on n=6 validation. A `SmallCalibrationWarning` banner (yellow) MUST fire above the result when `n_calibration < 30`. Tooltip text locked at AUDIT_REPORT §3.C Q3. | `pages/01_predict.py` |
| Q4.A | The predict page MUST render α=0.10 as the headline conformal level. Mini-2 adds the Advanced expander slider over α ∈ {0.05, 0.10, 0.20}. | `pages/01_predict.py` (headline); `pages/03_about.py` or dedicated conformal page (slider, Mini-2) |
| Q4.C | Every conformal-fit operation MUST emit a 3-state regime badge computed from `(n, α, k)`:  ASYMPTOTIC (n ≥ k AND n ≥ 100),  FINITE-SAMPLE (n ≥ k AND n < 100),  INVALID (n < k). At current state (n=6, α=0.10, k=7) the badge MUST display  INVALID. | `pages/01_predict.py` (adjacent to prediction set) |
| Q7.A | Mini-1 commit `feat(4.5.1): AuditEventType cleanup + 3 new WEB_*` MUST delete the 11 dead enum values (list in AUDIT_REPORT D14) AND add `WEB_PREDICT_RECEIVED`, `WEB_PREDICT_RETURNED`, `WEB_RATE_LIMIT_HIT`. Net delta: -8 values. | `ml/audit_hooks.py` (single commit) |
| Q7.C | The 3 new web event types MUST be dedicated values, NOT polymorphic-via-metadata. Reuse of existing `DATA_RECEIVED` for web-layer events is forbidden, preserves filter semantics for audit replay. | `ml/audit_hooks.py` |
| Q11.A | The form MUST have 8 widgets with the following NEUTRAL defaults: `age=12`, `csf_glucose=65.0`, `csf_protein=30.0`, `csf_wbc=3`, `pcr=False`, `microscopy=False`, `exposure=False`, `symptoms=[]`. Sanity gate: `infer_one` against these defaults MUST return `Low` with `p_high < 0.001`. | `pages/01_predict.py` |
| Q11.B | `KNOWN_SYMPTOMS` MUST be the exact tuple `("fever", "headache", "nuchal_rigidity")`, the 3 symptoms the model scores. The 4 currently-dropped symptoms (altered_mental_status, photophobia, nausea_vomiting, seizure) are deferred to Phase 6 with MIMIC-IV retrain. | `app/utils.py` or `ml/ui_live_patient.py` |
| Q12.A | The predict page MUST have exactly 3 preset buttons (NOT 2, NOT 4): `Load PAM-likely example`, `Load bacterial meningitis (limitation demo)`, `Load normal CSF example`. The page-load state functions as a 4th implicit "neutral" scenario. | `pages/01_predict.py` |
| Q12.B | The literal `PRESETS` dict MUST be embedded in `app/presets.py` exactly as specified in AUDIT_REPORT §3.B Q12. Field schema: `key` (snake_case), `label`, `description`, `inputs`, `current_behavior` (with `snapshot_date: "2026-04-26"`), `limitation_banner` (bool, explicit). Field name `current_behavior` (NOT `expected`) is mandatory, the rename was a Q12 override for normative-vocabulary reasons. | `app/presets.py` |
| Q12.C | The D18 limitation banner MUST appear ONLY adjacent to the result panel, NOT before "Run inference". When `bacterial_meningitis_limitation` preset is active, banner MUST render with red wash + deep-red border + deep-red text (Q15.5.D pattern, ≥7.18:1 contrast). | `pages/01_predict.py` |
| Q13.A | An `app/audit_export.py` module MUST provide `export_audit_to_csv(jsonl_path) -> bytes` that converts the audit JSONL to CSV preserving `previous_hash`, `current_hash`, all metadata, genesis timestamp, schema version. The predict-page-or-audit-page UI MUST expose `st.download_button` labeled "Download session audit log (CSV)" with filename `f"amoebanator_audit_{session_id}_{ISO_timestamp}.csv"`. | `app/audit_export.py` (utils, Mini-1); `pages/02_audit.py` (button, Mini-2) |
| Q15.A | Every uncaught exception in the predict path MUST be caught by an outer try/except that: (a) generates `error_id_full = uuid4().hex` (32 chars), (b) truncates to `error_id_user = error_id_full[:12]` for display, (c) renders `st.error(f"Prediction failed (error ID: {error_id_user}). Server-side log captured.")`, (d) emits `_emit(AuditEventType.INTEGRITY_VIOLATION, metadata={"error_id": error_id_full, "exception_type": type(e).__name__, "exception_repr": repr(e)})`. | `pages/01_predict.py` |
| Q15.B | If `load_stats()` raises `FileNotFoundError` (Mahalanobis stats file missing), the predict page MUST: (a) render a yellow banner above the result *"OOD gate is unconfigured (Mahalanobis stats file missing). All predictions return ABSTAIN/OOD until re-fit."*, (b) disable the Run button OR rename it to "Run anyway (gate unconfigured)". The page MUST NOT crash. | `pages/01_predict.py` |
| Q15.C | The audit page (Mini-2) MUST cap dataframe load at the last 10,000 rows. Display banner: *"Showing last 10,000 of N entries (oldest entries trimmed for display; full chain still intact in the underlying file). Use Download CSV to export the full session."* | `pages/02_audit.py` (Mini-2) |
| Q15.D | The Run-inference button MUST implement a session-state debounce with 30s stale-lock recovery. Specifically: `if st.session_state.get("predicting") and (time.time() - st.session_state.get("predicting_at", 0)) < 30: return`. Lock cleared in `finally` block AND on stale-detection. NO infinite lockout possible. | `pages/01_predict.py` |
| Q15.5.A | All 4 prediction badges (`High`, `Low`, `Moderate`, `ABSTAIN`) MUST render with icon + weight + color: ` **HIGH**`, ` **LOW**`, `🔵 **MODERATE**`, `**ABSTAIN**`. A test MUST strip color tags and assert icon + bold text alone convey the prediction state. | `app/utils.py` (`decision_badge` function); `tests/test_pages_predict.py` |
| Q15.5.B | A test MUST collect every `st.button(key=)`, `st.checkbox(key=)`, `st.number_input(key=)`, `st.multiselect(key=)` key across all 4 pages and assert the set has the same length as the list (no duplicate keys). Catches `DuplicateWidgetID` runtime errors at test time. | `tests/test_app_disclaimer.py::test_widget_keys_unique_across_pages` |
| Q15.5.C | The audit page MUST use `st.table(df)`, NOT `st.dataframe(df)`, `st.table` emits true HTML `<table>` semantics for screen readers (NVDA, VoiceOver). Empirical verification MUST happen at sprint time: if 10k-row `st.table` freezes the browser at >2s CPU, drop cap to 1k with banner *"Showing last 1k of N rows; download CSV for full"*; if 1k freezes, drop to 500. | `pages/02_audit.py` (Mini-2) |
| Q15.5.D | `app/disclaimer.py` MUST inject a CSS block defining the wash + border + deep-text pattern for `.stAlert[kind="error"]`, `.stAlert[kind="warning"]`, `.stAlert[kind="info"]`, `.stAlert[kind="success"]`. Computed contrast ratios MUST be ≥4.5:1 (AA threshold); locked colors achieve ≥7.18:1. A test (`test_wcag_aa_contrast`) MUST hand-roll relative-luminance ratio math (no axe-core dep) and assert each combo. | `app/disclaimer.py` (CSS); `tests/test_app_disclaimer.py` |
| Q15.5.E | The same CSS injection block MUST include `@media (prefers-reduced-motion: reduce) { * { animation-duration: 0.01ms !important; transition-duration: 0.01ms !important; } .stSpinner { display: none !important; } }`. Test is manual (browser-side media query): documented in §6 Risk R4 verification checklist. | `app/disclaimer.py` (CSS) |
| Q16.a | Every commit in Mini-1 + Mini-2 MUST follow Conventional Commits + subphase + body + footer: `<type>(<subphase>): <subject>` followed by body paragraph followed by mandatory footer `Closes: Q-refs` + `Refs: PHASE_4_5_PLAN.md §section`. Example: `feat(4.5.2): pages/01_predict.py with 3 presets + form\n\n[body]\n\nCloses: Q11.A, Q12.A, Q12.B, Q12.C\nRefs: PHASE_4_5_PLAN.md §4.2`. | every sprint commit |
| Q16.b | The Streamlit theme MUST be neutral-medical: primary `#0D47A1` (Material Blue 900), white background, dark slate text. NO branded color palette. NO portfolio-site visual identity. Rationale: clinical-adjacent demo; "branded" theming reads as marketing. | `.streamlit/config.toml` |
| Q16.c | `.streamlit/config.toml` MUST contain: `[server] runOnSave=false, fileWatcherType="none", port=8501`; `[global] developmentMode=false, suppressDeprecationWarnings=true`; `[client] showSidebarNavigation=true`; `[theme] primaryColor="#0D47A1"`. Port 8501 (NOT 7860) verified against HF auto-Dockerfile (`EXPOSE 8501`, `--server.port=8501`). All keys verified against Streamlit 1.52: zero deprecations. | `.streamlit/config.toml` |
| Q19.A | `app/disclaimer.py` MUST contain the locked variant (ii) text as a module-level constant `DISCLAIMER_TEXT`. The render function MUST emit it via `st.markdown` (NOT `st.info` or `st.warning`, those carry framework-injected styling that competes with the wash+border CSS). | `app/disclaimer.py` |
| Q19.B | The disclaimer MUST render on every page (Predict, Audit, About, References). Enforced via `tests/test_app_disclaimer.py::test_disclaimer_on_every_page`, parametrized over the 4 pages, asserting the 5 mandatory tokens (`NOT a medical device`, `n=30`, `limited to`, `ORCID`, `lmontenegrocalla@mail.weber.edu`) render on each. | `app/disclaimer.py` (render); `tests/test_app_disclaimer.py` (test) |
| Q19.C | The disclaimer text MUST include `ORCID 0009-0000-7851-7139` and `lmontenegrocalla@mail.weber.edu`. Format: `... (ORCID 0009-0000-7851-7139)` parenthetical at end. | `app/disclaimer.py` |

### 2.3 Mini-2 decisions

| # | Decision | Implementation target |
|---|---|---|
| Q4.A (slider) | The Advanced expander on Mini-2 conformal page MUST allow α slider over {0.05, 0.10, 0.20}, recomputing q-hat and abstain rate live. | `pages/03_about.py` or dedicated conformal page |
| Q8.B | `docs/references.bib` methodology refs (guo2017, lei2018, liu2020, lee2018, mitchell2019, ke2017) MUST stay at original publication year. Post-2022 companion citations (Wang ViM 2022, Sun KNN-OOD 2022, HF Model Card 2022 spec) are deferred to Phase 8.5 preprint prep. The comment header in references.bib already documents this. | `docs/references.bib` (no change needed) |
| Q8.C | Inline tooltips on the predict page MUST render references in sticky deterministic order per p_high bucket: `[1] CDC 2025 + [2] Tunkel 2004` always-shown; `[3] Cope 2016 + [4] Yoder 2010 + [5] Capewell 2015` for `p_high > 0.7`; `[6] Tunkel cross-ref + viral placeholder` for 0.3-0.7; `[7] Seehusen 2003` for `< 0.3`. Click-to-expand `+N more references for this risk band ↓` row. | `pages/01_predict.py` (tooltip rendering); `pages/04_references.py` (full list page) |
| Q13.B | The audit page MUST display the full session events via `st.table`, capped at 10k rows per Q15.C. Banner above the table: *"Showing all events from current session. Earlier sessions wiped on container restart (HF free-tier ephemeral disk). Use 'Download session audit log' to preserve."* | `pages/02_audit.py` |
| Q13.C | `outputs/audit/` MUST be added to `.dockerignore` in Subphase 4.5.4 (Mini-2 Dockerfile work). The dev-machine audit log leak is minor (125 entries, no PHI/tokens/secrets). A smoke test MUST verify: first prediction on a fresh Space cold-start emits the genesis entry (no inherited entries from dev machine). | `.dockerignore`; `tests/test_dockerfile_smoke.py` |
| Q17.A | The About page MUST include a feature-importance panel computed from `|w_i|` of the first `Linear(10,32)` layer averaged over the 32 output dims. Range MUST be 9.1%-11.5% (1.27× max/min ratio), verified live against current `model.pt`. | `pages/03_about.py` |
| Q17.B | The `|w_i|` panel MUST render ONLY on the About page, NOT on the Predict page adjacent to result. `|w_i|` is model-level NOT input-level; placement on Predict would imply input-specificity that doesn't exist. | `pages/03_about.py` only |
| Q17.C | The `|w_i|` panel caption MUST verbatim include: definition (model-level mean of first Linear layer weights), what it does NOT tell you (NOT per-prediction attribution), numerical range (9.1% to 11.5%, 1.27×), interpretation (treats all features near-equally), why (consistent with n=30 limitation), where SHAP fits (Phase 6 with MIMIC-IV n≥200), where to dig further (`docs/model_card.md` §Caveats). | `pages/03_about.py` |

### 2.4 USER ASSIGNMENT decisions

| # | Decision | Owner |
|---|---|---|
| Q9 | The Vercel `/playground` page MUST be replaced with a button: text *"Launch interactive demo →"*, URL `https://huggingface.co/spaces/luisjordanmontenegro/amoebanator-25`, target `_blank`, caption *"Hosted on Hugging Face Spaces (free CPU tier; cold-start ~30s on first visit after idle period). Research prototype, not for clinical use."* This edit happens in the Vercel website repo (separate from Amoebanator), executed by Jordan post-sprint. | Jordan, post-sprint (Step 7 in §7) |
| Q19.D | The GitHub repo MUST be renamed from `ljm234/Amoebanator_25` to `ljm234/amoebanator-25` via `gh repo rename` to match the HF Space slug. Local remote URL MUST be updated. The disclaimer URL `github.com/ljm234/amoebanator-25` only works after this rename. | Jordan, pre-sprint (Step 8 in §7) |

---

## §3. Architecture

### 3.1 File-tree diff (before-sprint vs after-sprint)

**Before-sprint (post-`b8f62e3`):**

```
Amoebanator 25/
├── app.py                          (existing, 8 panels via main())
├── ml/
│   ├── infer.py                    (303 LOC, post-flip)
│   ├── model.py                    (35 LOC, NEW from audit)
│   ├── audit_hooks.py              (286 LOC)
│   ├── ui_live_patient.py          (176 LOC, current panel)
│   ├── ood_combined.py             (159 LOC)
│   ├── conformal_advanced.py       (~250 LOC)
│   └── ...                         (38 modules total)
├── tests/                          (1233 tests across 23 files)
├── outputs/                        (model.pt, conformal.json, etc.)
├── docs/                           (12 .md files + references.bib)
└── .git/                           (7 commits)
```

**After-sprint (post-Mini-2):**

```
Amoebanator 25/
├── app/                            (NEW, sprint module)
│   ├── __init__.py
│   ├── app.py                      (multi-page entry, st.navigation)
│   ├── utils.py                    (build_row, decision_badge, _fmt_metric)
│   ├── presets.py                  (PRESETS dict from Q12.B)
│   ├── disclaimer.py               (DISCLAIMER_TEXT + render + CSS)
│   └── audit_export.py             (export_audit_to_csv)
├── pages/                          (NEW, Streamlit pages dir)
│   ├── 01_predict.py               (form + presets + result + tooltips)
│   ├── 02_audit.py                 (st.table + CSV download button)
│   ├── 03_about.py                 (model card excerpt + |w_i| panel + α slider)
│   └── 04_references.py            (22 refs with anchor links)
├── .streamlit/
│   └── config.toml                 (NEW, Q16.c spec)
├── tests/_snapshots/
│   └── predict.md.snap             (NEW, visual regression baseline)
├── ml/                             (unchanged from audit)
│   └── audit_hooks.py              (-8 enum values, +3 WEB_*)
├── tests/                          (1320+ tests across 27 files)
│   ├── test_pages_predict.py       (NEW, ~18 tests)
│   ├── test_app_presets.py         (NEW, ~20 tests)
│   ├── test_app_disclaimer.py      (NEW, ~12 tests)
│   ├── test_audit_export.py        (NEW, ~10 tests)
│   ├── test_pages_audit.py         (NEW, Mini-2)
│   ├── test_pages_about.py         (NEW, Mini-2)
│   ├── test_pages_references.py    (NEW, Mini-2)
│   └── test_app_navigation.py      (NEW, Mini-2)
├── Dockerfile                      (existing, unchanged in Mini-1; .dockerignore +outputs/audit/ in Mini-2)
└── docs/
    ├── AUDIT_REPORT.md             (1062 lines, this audit)
    ├── PHASE_4_5_PLAN.md           (this doc)
    ├── PHASE_4_5_PROMPT_FINAL.md   (sprint trigger)
    ├── INFORMATION_RECAP.md        (narrative)
    └── USER_ASSIGNMENTS.md         (updated with Step 8)
```

### 3.2 Module dependency graph (ASCII)

```
                          ┌──────────────────────┐
                          │  app/app.py          │  (st.navigation entry)
                          └──────────┬───────────┘
                                     │
              ┌──────────────────────┼──────────────────────┐
              │                      │                      │
              ▼                      ▼                      ▼
    ┌──────────────────┐  ┌──────────────────┐  ┌──────────────────┐
    │ pages/01_predict │  │ pages/02_audit   │  │ pages/03_about,  │
    │  .py             │  │  .py             │  │  04_references   │
    └─────┬────────────┘  └─────┬────────────┘  └─────┬────────────┘
          │                     │                     │
          │  ┌──────────────────┼─────────────────────┘
          │  │                  │
          ▼  ▼                  ▼
   ┌─────────────────┐  ┌─────────────────┐
   │ app/disclaimer  │  │ app/audit_export│
   │  .py            │  │  .py            │
   └─────────────────┘  └─────────────────┘
          │                     │
          ▼                     ▼
   ┌─────────────────┐  ┌─────────────────┐
   │ app/utils.py    │  │ ml/audit_hooks  │
   │ app/presets.py  │  │  .py            │
   └─────┬───────────┘  └─────────────────┘
         │
         ▼
   ┌─────────────────┐
   │ ml/infer.py     │  (existing, frozen for sprint)
   │ → ml/model.py   │
   │ → ml/conformal_ │
   │   advanced.py   │
   │ → ml/ood_       │
   │   combined.py   │
   └─────────────────┘
```

### 3.3 `st.cache_resource` boundaries

- **Cached:** `_load_model_artifacts()` in `ml/infer.py` (already `@lru_cache`-wrapped; do not double-wrap with `@st.cache_resource`).
- **Cached:** `load_presets()` in `app/presets.py` (small dict; cache for clean idempotency under Streamlit's rerun model).
- **NOT cached:** `infer_one()` itself, every call must execute the full inference path so the audit log emits per-prediction.
- **NOT cached:** `export_audit_to_csv()`, must read fresh from disk on every download click.
- **NOT cached:** `decision_badge()`, `_fmt_metric()`, pure functions, caching adds complexity without benefit.

### 3.4 Audit-log write path

The audit log writes to `outputs/audit/audit.jsonl` (repo-relative, configurable via `AMOEBANATOR_AUDIT_PATH` env var). On HF Space deploys, the write path resolves inside the container's ephemeral filesystem. Per-session integrity is preserved by the hash chain; cross-session persistence requires the CSV export feature (Q13.A) executed by the user.

---

## §4. Mini-1 Specification

### 4.1 Scope

- **LOC budget:** ~600 LOC (production) + ~225 LOC (tests). Total file delta: ~825 LOC.
- **Test additions:** ~50 new tests across 4 test files + 1 visual snapshot baseline = 51 new tests. Cumulative: 1233 + 51 = 1284 (≥1280 gate satisfied with 4 tests of headroom).
- **Closure gates:** 7 criteria (§4.4 below), all must be green to ship Mini-1 → Mini-2.
- **Wall-time estimate:** 2-3 hours of focused execution time.

### 4.2 File-by-file spec (production)

#### `app/__init__.py` (~5 LOC)

Empty package marker. May contain a single line `"""Amoebanator 25 web layer (Phase 4.5 sprint)."""`.

#### `app/utils.py` (~80 LOC)

Public functions:

```python
def build_row(
    age: int, csf_glucose: float, csf_protein: float, csf_wbc: int,
    pcr: bool, microscopy: bool, exposure: bool, symptoms: list[str],
) -> dict[str, Any]:
    """Convert form widget values to the dict shape ml.infer.infer_one accepts.
    
    Coerces booleans to int 0/1, joins symptoms list to semicolon string,
    strips blank symptom tokens. Schema-checked: all 8 keys present, types coerced.
    """

def decision_badge(prediction: str, reason: str | None = None) -> str:
    """Return a Streamlit-markdown badge string for the given prediction state.
    
    Renders icon + bold weight + color tag for High/Low/Moderate/ABSTAIN.
    For ABSTAIN, includes the reason in the badge text (e.g., "ABSTAIN, OOD").
    Empty/unknown prediction returns "unknown" badge.
    """

def _fmt_metric(out: dict[str, Any], key: str, fmt: str = "{:.3f}") -> str:
    """Tolerant metric formatter. Returns "-" for missing/None/non-numeric values.
    
    Used for rendering Mahalanobis d², energy, conformal qhat, etc. without
    crashing on partial output dicts (some inference branches don't populate all fields).
    """
```

Edge cases enumerated in `tests/test_pages_predict.py`:
- `build_row` with `symptoms=[""]` → empty string in output
- `build_row` with `symptoms=["fever", "", "headache"]` → `"fever;headache"`
- `decision_badge("ABSTAIN", "OOD")` → contains `"ABSTAIN, OOD"`
- `decision_badge("ABSTAIN", None)` → contains `"ABSTAIN, unspecified"`
- `_fmt_metric({"x": "garbage"}, "x")` → `"-"`
- `_fmt_metric({"x": 1.5}, "x", "{:.1f}")` → `"1.5"`

#### `app/presets.py` (~95 LOC)

Module-level constant `PRESETS: dict[str, dict[str, Any]]` containing the 3 locked preset dicts from Q12.B (verbatim spec in `AUDIT_REPORT.md` §3.B Q12, embedded as code block). Plus a helper:

```python
def load_preset(key: str) -> dict[str, Any]:
    """Return the preset dict for key. Raises KeyError if key not in PRESETS."""
    return PRESETS[key]
```

The xfail-decorated regression test for the bacterial-limitation preset is in `tests/test_app_presets.py` (xfail decorator verbatim spec in `AUDIT_REPORT.md` §3.B Q12).

#### `app/disclaimer.py` (~120 LOC)

Module-level constant `DISCLAIMER_TEXT` containing the locked variant (ii) from Q19.A (verbatim string). Render function:

```python
def render_disclaimer() -> None:
    """Render the disclaimer + CSS injection block.
    
    Called at the top of every page. Idempotent (Streamlit's rerun model handles
    dedup of CSS injection). Emits the 5 mandatory tokens via st.markdown.
    """
    st.markdown(_INJECTED_CSS, unsafe_allow_html=True)
    st.markdown(DISCLAIMER_TEXT)
```

`_INJECTED_CSS` constant contains:
- `.stAlert[kind="error"]` wash + border + deep-text (≥7.18:1 contrast, Q15.5.D)
- `.stAlert[kind="warning"]` similar pattern
- `.stAlert[kind="info"]` light blue wash + deep blue text (≥8.21:1)
- `.stAlert[kind="success"]` light green wash + deep green text (≥7.59:1)
- `@media (prefers-reduced-motion: reduce)` block (Q15.5.E)

The `wcag_contrast_ratio(text_hex, bg_hex) -> float` helper is defined in this module (relative-luminance ratio math, no external dep). The `tests/test_app_disclaimer.py::test_wcag_aa_contrast` test asserts the helper returns ≥4.5 for every locked color combo.

#### `app/audit_export.py` (~75 LOC)

```python
def export_audit_to_csv(jsonl_path: pathlib.Path) -> bytes:
    """Read the audit JSONL at jsonl_path, convert to CSV bytes preserving hash chain.
    
    Columns: timestamp, event_type, actor, resource, action_detail, metadata_json,
    previous_hash, current_hash, schema_version. No filtering, no truncation.
    Returns CSV-encoded bytes ready for st.download_button.
    """

def verify_csv_chain_integrity(csv_bytes: bytes) -> bool:
    """Re-parse CSV, verify previous_hash → current_hash chain integrity.
    
    Used by the round-trip test (Mini-1 closure gate criterion #4).
    Returns True iff every row's current_hash matches sha256 of canonical row repr.
    """
```

#### `pages/01_predict.py` (~225 LOC)

The bulk of Mini-1. Structure:

```python
"""Predict page, Phase 4.5 Mini-1."""
import streamlit as st
from app.disclaimer import render_disclaimer
from app.presets import PRESETS, load_preset
from app.utils import build_row, decision_badge, _fmt_metric
from ml.infer import infer_one
from ml.audit_hooks import _emit, AuditEventType
import time
import uuid

st.set_page_config(page_title="Predict, Amoebanator 25", page_icon="")
render_disclaimer()

st.title("PAM Risk Prediction")

# ── Preset buttons ──
preset_cols = st.columns(3)
for col, key in zip(preset_cols, ["high_risk_pam", "bacterial_meningitis_limitation", "normal_csf"]):
    if col.button(PRESETS[key]["label"], key=f"preset_{key}"):
        st.session_state.update({f"input_{k}": v for k, v in PRESETS[key]["inputs"].items()})
        st.session_state.active_preset = key
        _emit(AuditEventType.WEB_PRESET_LOADED, ...)

# ── Form ──
with st.form("predict_form"):
    col1, col2 = st.columns(2)
    age = col1.number_input("Age (years)", min_value=0, max_value=120, 
                             value=st.session_state.get("input_age", 12), key="age")
    csf_glucose = col1.number_input("CSF glucose (mg/dL)", min_value=0.0, 
                                     value=st.session_state.get("input_csf_glucose", 65.0), 
                                     step=1.0, key="csf_glucose")
    # ... 6 more widgets per Q11.A spec ...
    submitted = st.form_submit_button("Run inference", disabled=_is_button_disabled())

# ── Inference path with debounce + error handling ──
if submitted:
    if st.session_state.get("predicting"):
        lock_age = time.time() - st.session_state.get("predicting_at", 0)
        if lock_age < 30:
            st.warning("Already processing, wait for the current prediction to complete.")
            st.stop()
    
    st.session_state.predicting = True
    st.session_state.predicting_at = time.time()
    try:
        row = build_row(age, csf_glucose, csf_protein, csf_wbc, pcr, microscopy, exposure, symptoms)
        out = infer_one(row)
        # ── Render result ──
        render_result(out)
        # ── D18 limitation banner if active preset is bacterial ──
        if st.session_state.get("active_preset") == "bacterial_meningitis_limitation":
            st.error(PRESETS["bacterial_meningitis_limitation"]["description"])
        _emit(AuditEventType.WEB_PREDICT_RETURNED, ...)
    except FileNotFoundError as e:
        # Q15.B: graceful banner for missing stats
        st.warning("OOD gate is unconfigured (Mahalanobis stats file missing). All predictions return ABSTAIN/OOD until re-fit.")
    except Exception as e:
        # Q15.A: correlation ID + audit log
        error_id_full = uuid.uuid4().hex
        error_id_user = error_id_full[:12]
        st.error(f"Prediction failed (error ID: {error_id_user}). Server-side log captured.")
        _emit(AuditEventType.INTEGRITY_VIOLATION, 
              metadata={"error_id": error_id_full, "exception_type": type(e).__name__, "exception_repr": repr(e)})
    finally:
        st.session_state.predicting = False
        st.session_state.predicting_at = 0


def render_result(out: dict) -> None:
    """Render the prediction badge + T=0.27 banner + 3-state regime badge + |w_i| pointer."""
    badge = decision_badge(out["prediction"], out.get("reason"))
    st.markdown(f"### Result: {badge}")
    
    # T=0.27 (n=6) badge with hover tooltip (Q3)
    st.markdown('<span title="Calibrated by temperature scaling (Guo 2017, L-BFGS, n=6 validation). T=0.27 means the calibrator amplifies the model\'s raw confidence, typical temperature scaling has T>1 (attenuation); T<1 here is unusual and reflects fitting on only 6 samples. ECE and coverage estimates are empirical-only, not asymptotic. See docs/model_card.md §9.">T=0.27 (n=6)</span>', unsafe_allow_html=True)
    
    # SmallCalibrationWarning banner if n_cal < 30
    if out.get("n_cal", 6) < 30:
        st.warning("⚠ Calibration set is small (n=6). Probability estimates are indicative only. Do not use as a clinical confidence score.")
    
    # 3-state conformal regime badge (Q4.C)
    n, alpha = 6, 0.10
    k = math.ceil((n + 1) * (1 - alpha))
    if n >= k and n >= 100:
        st.success(" ASYMPTOTIC: Guarantee holds; finite-sample bound 1−α + 2/(n+2) is tight.")
    elif n >= k:
        st.info(" FINITE-SAMPLE: bound holds but loose; treat reported coverage as empirical.")
    else:
        st.error(f" INVALID: Order-statistic clamped (k clipped from {k} to n={n}); the formal guarantee 1−α is mathematically inapplicable.")
    
    # ... metrics ...
    st.markdown(f"p_high: {_fmt_metric(out, 'p_high')}")
    st.markdown(f"Mahalanobis d²: {_fmt_metric(out, 'mahalanobis_d2')} (τ={_fmt_metric(out, 'd2_tau')})")
    st.markdown(f"Logit energy: {_fmt_metric(out, 'energy')} (τ={_fmt_metric(out, 'energy_tau')})")
```

This is illustrative, the actual implementation will likely differ in widget ordering, key naming, and result-rendering structure. The locked specs are: 8 widgets + 3 preset buttons + Run button with debounce + correlation-ID error handling + missing-stats graceful banner + result rendering with all 4 badges (decision, T=0.27, SmallCalibrationWarning, 3-state regime).

### 4.3 File-by-file spec (tests)

#### `tests/test_pages_predict.py` (~140 LOC, 18 tests)

Each test is a one-liner enumeration here; full implementations follow standard Streamlit AppTest patterns.

1. `test_module_imports_cleanly`, `import pages.predict` succeeds without exceptions
2. `test_form_renders_8_widgets`, AppTest verifies 8 widgets present
3. `test_form_uses_neutral_defaults`, verify `age=12`, `csf_glucose=65.0`, `csf_protein=30.0`, `csf_wbc=3`, `pcr=False`, `microscopy=False`, `exposure=False`, `symptoms=[]`
4. `test_neutral_defaults_predict_low_p_high_lt_001`, submit with neutrals, assert `p_high < 0.001` (sanity gate)
5. `test_three_preset_buttons_render`, assert 3 buttons with labels matching PRESETS keys
6. `test_loading_high_risk_pam_preset_populates_form`, click button, verify session state updated
7. `test_submit_calls_infer_one_with_built_row`, mock `infer_one`, verify dict shape passed
8. `test_no_submit_returns_early`, no `infer_one` call when submit not pressed
9. `test_filenotfounderror_renders_graceful_banner`, mock `infer_one` to raise FNFE, assert warning banner present
10. `test_uncaught_exception_emits_correlation_id_audit`, mock to raise generic Exception, assert `INTEGRITY_VIOLATION` event with `error_id` metadata
11. `test_double_submit_within_30s_blocked`, set `st.session_state.predicting=True`, submit again, assert no new infer_one call
12. `test_stale_lock_recovers_after_30s`, set `predicting_at` to 31s ago, submit, assert infer_one called
13. `test_decision_badge_renders_with_icon_and_bold`, strip color tags, assert icon + bold present
14. `test_decision_badge_color_blind_safe`, same as above but for all 4 prediction states
15. `test_t_027_badge_renders_with_tooltip`, assert badge + hover tooltip present
16. `test_smallcalibrationwarning_fires_for_n_below_30`, mock output with `n_cal=6`, assert warning rendered
17. `test_three_state_regime_badge_invalid_at_n6_alpha010`, assert  INVALID badge present
18. `test_d18_limitation_banner_only_on_bacterial_preset`, set active_preset to bacterial, assert banner; set to others, assert no banner

#### `tests/test_app_presets.py` (~110 LOC, 20 tests)

Per preset (3 presets × 5 assertions + 5 cross-preset tests):

For each of `high_risk_pam`, `bacterial_meningitis_limitation`, `normal_csf`:
1. Preset dict matches schema (`label`, `description`, `inputs`, `current_behavior`, `limitation_banner` all present)
2. All 10 features (8 form widgets + symptoms variants) covered in `inputs`
3. `current_behavior` contains `prediction`, `p_high_approx`, `snapshot_date="2026-04-26"`
4. Submitting preset triggers `infer_one` with exact built_row
5. Live snapshot test: actual `infer_one` output matches `current_behavior.prediction`

Plus the bacterial-specific xfail test (Q12.B):

```python
@pytest.mark.xfail(strict=False, reason="D18 limitation: ...")
def test_preset_bacterial_limitation_returns_high() -> None:
    ...
```

Plus 4 cross-preset tests:
- `test_three_presets_total_count`
- `test_preset_keys_are_snake_case`
- `test_only_bacterial_has_limitation_banner_true`
- `test_all_presets_have_snapshot_date_2026_04_26`

#### `tests/test_app_disclaimer.py` (~95 LOC, 12 tests)

1. `test_disclaimer_text_contains_5_mandatory_tokens`, assert `NOT a medical device`, `n=30`, `limited to`, `ORCID`, `lmontenegrocalla@mail.weber.edu` all in `DISCLAIMER_TEXT`
2. `test_disclaimer_link_targets_are_https`, assert no `javascript:` or `http://` URLs in disclaimer
3. `test_orcid_format_regex`, assert ORCID matches `\d{4}-\d{4}-\d{4}-\d{4}` pattern
4. `test_email_format_regex`, assert email matches RFC 5322 simplified regex
5. `test_disclaimer_on_every_page`, parametrize over 4 pages, assert 5 tokens render on each (at Mini-2 close)
6. `test_wcag_aa_contrast_error_combo`, assert `wcag_contrast_ratio("#B71C1C", "#FFEBEE") >= 4.5`
7. `test_wcag_aa_contrast_info_combo`, assert ≥4.5 for blue combo
8. `test_wcag_aa_contrast_success_combo`, assert ≥4.5 for green combo
9. `test_widget_keys_unique_across_pages`, collect all `key=` values, assert set length == list length (Q15.5.B)
10. `test_reduced_motion_css_block_present`, assert `_INJECTED_CSS` contains `prefers-reduced-motion`
11. `test_utils_fmt_metric_handles_nan`, `_fmt_metric({"x": float("nan")}, "x")` returns `"-"`
12. `test_utils_fmt_metric_handles_inf`, `_fmt_metric({"x": float("inf")}, "x")` returns `"-"`

#### `tests/test_audit_export.py` (~85 LOC, 10 tests)

1. `test_export_returns_bytes`, `export_audit_to_csv()` returns `bytes` type
2. `test_export_csv_has_required_columns`, parse CSV, assert columns include `timestamp`, `event_type`, `previous_hash`, `current_hash`, `schema_version`
3. `test_export_preserves_all_rows`, write 10 events, export, count rows = 10
4. `test_round_trip_hash_chain_byte_equal`, write 10 → export → re-parse → byte-equal hash chain (Mini-1 closure gate criterion #4)
5. `test_verify_csv_chain_integrity_pass`, round-trip + verify_csv_chain_integrity returns True
6. `test_verify_csv_chain_integrity_fail_on_tamper`, modify one row's metadata, verify returns False
7. `test_export_filename_format`, filename matches `f"amoebanator_audit_{session_id}_{ISO_timestamp}.csv"` pattern
8. `test_export_handles_empty_log`, export empty JSONL returns CSV with header row only
9. `test_export_preserves_metadata_json`, nested metadata JSON survives round-trip
10. `test_export_emits_audit_event`, calling `export_audit_to_csv` emits `AuditEventType.AUDIT_EXPORT_REQUESTED`

#### `tests/_snapshots/predict.md.snap` (~30 LOC, 1 baseline snapshot)

Captured via Streamlit AppTest's `result.markdown` snapshot. Text-based, NOT image diff. Stored as text fixture, regenerated via `pytest --snapshot-update` on intentional UI changes. Drift threshold: <5% character delta vs baseline.

### 4.4 Mini-1 closure gates (the 7 from Q20)

All 7 MUST be green to ship Mini-1 → Mini-2:

1. **Test count + pass rate.** `pytest -q` → ≥1280 collected, **0 failed, 0 errors**, ≤5 documented xfails (only the bacterial-limitation xfail from Q12.B and any other pre-existing audit-period xfails).
2. **Type purity.** `pyright` → **0 new errors, 0 new warnings** vs `b8f62e3` baseline. Snapshot baseline error/warning counts at sprint kickoff; allow only deltas at zero.
3. **Streamlit AppTest boot.** `app/app.py` boots in AppTest in **<5s wall-clock** and renders `Predict` page without exceptions.
4. **CSV audit export round-trip.** Write 10 events → `export_audit_to_csv()` → re-parse → byte-equal hash chain. Test in `tests/test_audit_export.py::test_round_trip_hash_chain_byte_equal`.
5. **Disclaimer presence on every page.** `tests/test_app_disclaimer.py::test_disclaimer_on_every_page` parametrizes over 4 pages and asserts the 5 mandatory tokens render on each. Single canonical test, NOT 4 copies.
6. **IRB_BYPASS=1 vs =0 branches.** With `AMOEBANATOR_IRB_BYPASS=1`, predict page renders extra red banner *"IRB bypass active, research mode only"* AND emits `IRB_STATUS_CHANGE` audit event with `actor='env_var'`. With env var unset, no banner + no event. Both branches tested in `tests/test_pages_predict.py`.
7. **Visual regression text-snapshot.** AppTest captures predict page markdown, diff vs `tests/_snapshots/predict.md.snap` baseline. Drift <5% character delta = pass; drift >5% = either intentional (regenerate via `--snapshot-update`) or a regression (investigate).

---

## §5. Mini-2 Specification

### 5.1 Scope

- **LOC budget:** ~350 LOC (production) + ~145 LOC (tests). Total file delta: ~495 LOC.
- **Test additions:** ~40 new tests across 4 test files (Mini-2 builds on Mini-1's snapshot baseline). Cumulative: 1284 + 40 = 1324 (≥1320 gate satisfied).
- **Closure gates:** Same 7 criteria as Mini-1 + cumulative cap raised to ≥1320.
- **Wall-time estimate:** 2 hours of focused execution time.

### 5.2 File-by-file spec (production)

#### `app/app.py` (~30 LOC, modify existing or create new)

The `st.navigation` entry point. Registers the 4 pages. Triggers `render_disclaimer()` on every page via Streamlit's page-level `set_page_config` + the per-page `render_disclaimer()` call (no global hook in Streamlit; hence the canonical test).

```python
import streamlit as st

pages = {
    " Predict": [st.Page("pages/01_predict.py", title="Predict", icon="")],
    "📜 Audit": [st.Page("pages/02_audit.py", title="Audit", icon="📜")],
    "ℹ️ About": [st.Page("pages/03_about.py", title="About", icon="ℹ️")],
    "📚 References": [st.Page("pages/04_references.py", title="References", icon="📚")],
}

pg = st.navigation(pages)
pg.run()
```

#### `pages/02_audit.py` (~120 LOC)

Audit log viewer + CSV download button.

```python
import streamlit as st
from app.disclaimer import render_disclaimer
from app.audit_export import export_audit_to_csv
import pandas as pd
import pathlib
import datetime

st.set_page_config(page_title="Audit, Amoebanator 25", page_icon="📜")
render_disclaimer()

st.title("Audit Log (Current Session)")

st.warning("Showing all events from current session. Earlier sessions wiped on container restart (HF free-tier ephemeral disk). Use 'Download session audit log' to preserve.")

audit_path = pathlib.Path("outputs/audit/audit.jsonl")
if not audit_path.exists():
    st.info("No audit events yet. Run a prediction on the Predict page first.")
    st.stop()

df = pd.read_json(audit_path, lines=True)
total_rows = len(df)
df_display = df.tail(10000)  # Q15.C cap
if total_rows > 10000:
    st.info(f"Showing last 10,000 of {total_rows} entries (oldest entries trimmed for display; full chain still intact in the underlying file). Use Download CSV to export the full session.")

st.table(df_display)  # Q15.5.C: st.table NOT st.dataframe (screen-reader semantics)

# CSV download button
ts = datetime.datetime.utcnow().isoformat().replace(":", "-")
session_id = st.session_state.get("session_id", "unknown")
filename = f"amoebanator_audit_{session_id}_{ts}.csv"
csv_bytes = export_audit_to_csv(audit_path)
st.download_button(
    label="Download session audit log (CSV)",
    data=csv_bytes,
    file_name=filename,
    mime="text/csv",
    key="download_audit_csv",
)
```

#### `pages/03_about.py` (~120 LOC)

Model card excerpt + |w_i| panel + α slider.

Structure:
- Render disclaimer
- §1 Model architecture summary (Linear(10,32)→ReLU→Linear(32,16)→ReLU→Linear(16,2), 914 params)
- §2 Training summary (n_train=24, n_val=6, synthetic from Yoder/Cope marginals)
- §3 Calibration summary (T=0.27, L-BFGS, n=6 caveat with link to model card)
- §4 |w_i| feature importance panel:
  - Compute: load `model.pt`, extract first `Linear(10,32)` layer weight, mean across 32 output dims, normalize by sum
  - Render: bar chart with feature names on y-axis, normalized |w_i| on x-axis
  - Caption: locked Q17.C verbatim text (model-level, not per-prediction, range 9.1%-11.5%, 1.27×, n=30 limitation)
- §5 Conformal Advanced expander (Q4.A slider): α ∈ {0.05, 0.10, 0.20}, recompute q-hat live, show ABSTAIN rate response
- §6 Authorship + ORCID + contact

#### `pages/04_references.py` (~80 LOC)

Full 22-reference list with anchor links. Format: BibTeX-rendered citations grouped by category (PAM clinical, ML methodology, calibration/conformal, OOD, governance frameworks).

### 5.3 File-by-file spec (tests, ~145 LOC across 4 files)

- `tests/test_pages_audit.py` (~12 tests): table renders, download button present, CSV bytes valid, banner appears, 10k cap honored, ephemerality message visible.
- `tests/test_pages_about.py` (~10 tests): |w_i| panel renders, caption verbatim, α slider responds, model architecture summary present.
- `tests/test_pages_references.py` (~8 tests): 22 references rendered, anchor links work, grouping correct.
- `tests/test_app_navigation.py` (~10 tests): all 4 pages registered, navigation order, page titles, icons.

### 5.4 Mini-2 closure gates

Same 7 criteria as Mini-1 (§4.4) + cumulative test count ≥1320. Visual regression baseline expanded to 4 page snapshots in `tests/_snapshots/`.

---

## §6. Risk Register

Eight risks ranked by likelihood × impact. Each with mitigation.

### R1, HF Space cold-boot exceeds 5s, breaking AppTest assumption (high likelihood, medium impact)

**Risk:** Mini-1 closure gate criterion #3 requires AppTest boot in <5s. HF Space cold-boot is 25-30s wall-clock (PyTorch import ~3.7s + container provisioning ~25s). If the AppTest gate runs in CI against an HF-equivalent environment, it will fail.

**Mitigation:** AppTest gate runs in local Docker, NOT against deployed HF Space. Local boot is ~4s (PyTorch import dominates). Document this separation explicitly: *"AppTest closure gate measures local boot, not HF cold-start. HF cold-start is acknowledged 30s per Q18.A."*

### R2, Pyright strict catches new Streamlit dynamic-attribute access (medium likelihood, low impact)

**Risk:** Streamlit's `st.session_state` uses dynamic attribute access (`st.session_state.foo` rather than `st.session_state["foo"]`). Pyright in strict mode flags these as `reportAttributeAccessIssue`.

**Mitigation:** Use bracket-style `st.session_state["foo"]` consistently in all sprint code. Where bracket style is awkward (e.g., `st.session_state.update({...})`), add targeted `# pyright: ignore[reportAttributeAccessIssue]` with a comment explaining why. Snapshot pyright baseline at sprint kickoff and gate on deltas, not absolutes.

### R3, AuditEventType migration leaves stale JSONL entries (medium likelihood, low impact)

**Risk:** Mini-1 deletes 11 dead enum values + adds 3 new `WEB_*`. Existing audit JSONL files on dev machine contain references to the deleted enum values. Reading these via `AuditEventType[entry["event_type"]]` raises `KeyError`.

**Mitigation:** (a) `app/audit_export.py` reads event_type as string, not as enum, survives schema migrations; (b) bump schema version field in audit.jsonl genesis entry to `"2"` post-Mini-1; (c) document migration in `docs/SPRINT_LOG.md` Mini-1 entry.

### R4, Visual snapshot drift on harmless reorder (medium likelihood, low impact)

**Risk:** Mini-2 nav refactor or any cosmetic change might shift page markdown by >5% characters, failing closure gate criterion #7 even though no behavior changed.

**Mitigation:** (a) Threshold tuned to 5% (not 0%) for tolerance; (b) `pytest --snapshot-update` workflow documented for intentional changes; (c) snapshot diff renders visually via `pytest -v --snapshot-diff` before regenerate. Manual checklist for `prefers-reduced-motion`: *"Open demo in Chrome with prefers-reduced-motion: reduce enabled in DevTools → Rendering → confirm no animations play."*

### R5, D18 limitation-demo preset confuses non-clinical reviewers (low likelihood, medium impact)

**Risk:** A reviewer without clinical background clicks bacterial preset, sees `prediction=High`, doesn't read the limitation banner, concludes the model is broken or being deceptive.

**Mitigation:** (a) Banner positioned adjacent to result panel (Q12.C) so it's impossible to miss; (b) Banner uses red wash + deep red text + bold weight (Q15.5.D); (c) First sentence of banner *"⚠ This preset is a known model limitation"* is the load-bearing reframe, reviewers see "limitation" before they see "High"; (d) Last sentence *"Try the other 2 presets to see the model's working regime"* steers them to a successful demo path.

### R6, Phase 6 IRB record creation gap (high likelihood when triggered, high impact)

**Risk:** When MIMIC-IV cohort lands in Phase 6, `AMOEBANATOR_IRB_BYPASS=0` requires a real IRB JSON record. If the env var is flipped before the IRB record is created, the app fails to boot with `IRBGateBlocked`. This is a future-self trap.

**Mitigation:** (a) Dockerfile `ENV AMOEBANATOR_IRB_BYPASS=1` line MUST be preceded by a multi-line safety comment explaining (i) why bypass exists (synthetic data only), (ii) when to flip to 0 (Phase 6 with MIMIC-IV), (iii) what's required first (IRB record at `outputs/governance/irb_record.json` with `irb_status` ∈ {`approved`, `conditionally_approved`}); (b) `docs/USER_ASSIGNMENTS.md` Step 9 (future) documents the flip procedure with checklist. See §7.4 for full spec.

### R7, HF Space 16 GB RAM exceeded by audit log dataframe (low likelihood, low impact)

**Risk:** Audit log grows large enough that `pd.read_json(...)` exceeds free-tier RAM.

**Mitigation:** Largely preventive, already addressed via Q15.C 10k row cap. Per-row size ~500 bytes; 10k rows = 5 MB, trivial vs 16 GB. Risk only materializes if audit log file itself grows beyond cap before display read; in that case `pd.read_json` may load full file before tail-trim. Defensive: stream the JSONL and tail-trim during read.

### R8, Cold-start race condition between audit hooks and model load (medium likelihood, medium impact)

**Risk:** First request after container restart may hit `infer_one()` before `_load_model_artifacts()` completes, raising `RuntimeError: model not loaded`. Audit hook emit happens before the exception is caught.

**Mitigation:** (a) `@lru_cache` on `_load_model_artifacts` is thread-safe and synchronously blocks first caller; (b) Mini-1 acceptance criterion #1 (cold-start test) explicitly tests "click Preset 1 within 5 seconds of 'ready'"; (c) Q15.A correlation-ID error handling catches the `RuntimeError` and renders a graceful banner.

---

## §7. User Assignments

The sprint includes out-of-band actions that only Jordan can execute (account credentials, external repo edits, HF Space deploys). These are tracked in `docs/USER_ASSIGNMENTS.md` as a tiered structure: Pre-sprint (must complete BEFORE Mini-1 starts), During-sprint (none required, sprint is autonomous), Post-sprint (after Mini-2 closes), Future (Phase 6+).

### 7.1 Pre-sprint assignments (run BEFORE Mini-1 starts)

#### Step 6 (existing), Upload HF_TOKEN secret to GitHub Actions

**Why:** GitHub Actions deploy workflow needs the HF token to push to the Space. Token must be uploaded as repo-level secret, NOT committed to repo.

**Procedure (stdin pattern, NEVER paste token to shell):**

```bash
# 1. Retrieve from macOS Keychain
HF_TOKEN_TMP=$(security find-generic-password -s "hf-amoebanator-25" -a "$USER" -w)

# 2. Upload via gh secret set with stdin (token never appears in shell history)
echo "$HF_TOKEN_TMP" | gh secret set HF_TOKEN --repo ljm234/amoebanator-25 --body-file=-

# 3. Verify
gh secret list --repo ljm234/amoebanator-25 | grep HF_TOKEN

# 4. Clear local var
unset HF_TOKEN_TMP
```

**Verification:** `gh secret list` shows `HF_TOKEN` in the output. The actual token value is unreadable post-upload (GitHub encrypts).

#### Step 8 (NEW from Q19.D), Rename GitHub repo Amoebanator_25 → amoebanator-25

**Why:** The HF Space slug is `luisjordanmontenegro/amoebanator-25` (lowercase + dash, npm/pypi convention). The current GitHub repo is `ljm234/Amoebanator_25` (capital + underscore). Match the repo slug to the HF slug so the disclaimer URL `github.com/ljm234/amoebanator-25` works and so the segment a PI pastes is identical across both URLs.

**Procedure:**

```bash
# 1. Rename via gh CLI (auto-redirects old URL permanently)
gh repo rename ljm234/Amoebanator_25 ljm234/amoebanator-25

# 2. Update local remote URL
cd "/Users/jordanmontenegro/Desktop/Amoebanator 25/Amoebanator 25"
git remote set-url origin https://github.com/ljm234/amoebanator-25.git

# 3. Verify both
git remote -v  # must show https://github.com/ljm234/amoebanator-25.git
gh repo view --json url --jq .url  # must show https://github.com/ljm234/amoebanator-25
```

**Why this is path (b) and not (c) full rebrand:** The username mismatch (`ljm234` GitHub vs `luisjordanmontenegro` HF) is a one-line addition to the About page (`pages/03_about.py`): *"Repo: github.com/ljm234/amoebanator-25, HuggingFace Space: huggingface.co/spaces/luisjordanmontenegro/amoebanator-25 (same author, separate handles)."* Full rebrand to `luisjordanmontenegro` GitHub account costs re-auth, secret regen, and ownership transfer for one-line disclosure benefit. Rejected.

**Verification:** Disclaimer URL `https://github.com/ljm234/amoebanator-25` returns 200 in browser.

### 7.2 During-sprint assignments

**None.** The sprint is autonomous between Mini-1 start and Mini-2 close. Jordan reviews at the Mini-1/Mini-2 boundary (after all 7 closure gates are green for Mini-1) and at Mini-2 close. No in-flight intervention required.

### 7.3 Post-sprint assignments (after Mini-2 closes)

#### Step 7 (existing), Update Vercel /playground link-out

**Why:** Q9 locked link-out only. The Vercel website repo (separate from Amoebanator) needs the `/playground` page replaced with a button to the HF Space.

**Procedure:**

```bash
# 0. Verify cwd (Q10 Step 0 cwd guard)
pwd  # should NOT be /Users/jordanmontenegro/Desktop/Amoebanator 25/...
git remote -v  # should show jordanmontenegrocalla.com Next.js repo

# 1. Backup current placeholder
cp app/playground/page.tsx app/playground/page.tsx.bak

# 2. Add *.tsx.bak to .gitignore
echo "*.tsx.bak" >> .gitignore
git add .gitignore && git commit -m "chore: ignore .tsx.bak rollback files"

# 3. Edit page.tsx to replace placeholder with button
# Button: "Launch interactive demo →"
# URL: https://huggingface.co/spaces/luisjordanmontenegro/amoebanator-25
# Target: _blank
# Caption: "Hosted on Hugging Face Spaces (free CPU tier; cold-start ~30s on first visit after idle period). Research prototype, not for clinical use."

# 4. Commit + push
git add app/playground/page.tsx
git commit -m "feat(playground): link-out to HF Space amoebanator-25 demo"
git push origin main

# 5. Verify Vercel deploy
# Open jordanmontenegrocalla.com/playground in browser
# Confirm button renders + opens HF Space in new tab
```

**Verification:** `jordanmontenegrocalla.com/playground` shows button + caption; clicking opens HF Space in new tab.

### 7.4 Future assignments (Phase 6+)

#### Step 9 (NEW, future), Flip AMOEBANATOR_IRB_BYPASS=1 → 0 when MIMIC-IV cohort lands

**Why:** Phase 6 introduces real PHI from MIMIC-IV. The IRB gate must enforce real IRB approval, not synthetic-data bypass. Current Dockerfile sets `ENV AMOEBANATOR_IRB_BYPASS=1` because n=30 cohort is fully synthetic (no PHI, no human subjects).

**Multi-line safety comment for Dockerfile (mandatory):**

```dockerfile
# AMOEBANATOR_IRB_BYPASS, IRB gate bypass switch
#
# WHY THIS EXISTS:
#   The Phase 4.5 demo trains on n=30 synthetic patient vignettes derived from
#   published case-series marginals (Yoder 2010, Cope 2016, CDC 2025). No real
#   PHI, no human subjects. Hence no IRB review is required, but the IRB gate
#   in ml/irb_gate.py refuses to boot the app without an IRB JSON record. This
#   bypass env var short-circuits the gate WITH a mandatory audit log emission
#   (AuditEventType.ACCESS_DENIED → reason="env_var_bypass") so the bypass is
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

**Procedure when flipping:**

```bash
# 1. Verify IRB record exists
test -f outputs/governance/irb_record.json || { echo "BLOCK: no IRB record"; exit 1; }

# 2. Verify status is approved
jq -r '.irb_status' outputs/governance/irb_record.json | grep -qE '^(approved|conditionally_approved)$' \
  || { echo "BLOCK: irb_status not approved"; exit 1; }

# 3. Edit Dockerfile: change ENV AMOEBANATOR_IRB_BYPASS=1 to =0
# (or remove the env var entirely; ml/irb_gate.py treats missing/0 as "enforce")

# 4. Run full test suite, especially the new IRB enforcement tests
pytest tests/test_irb_gate.py -v

# 5. Re-deploy to HF Space
git add Dockerfile && git commit -m "feat(phase6): flip AMOEBANATOR_IRB_BYPASS to 0 (real MIMIC-IV cohort)"
git push origin main
```

**Verification:** App boots successfully with `AMOEBANATOR_IRB_BYPASS=0`. Without the IRB record, `IRBGateBlocked` raises and the app refuses to start (correct behavior).

---

## §8. Out-of-Scope Punchlist

Things considered during the audit and explicitly deferred or rejected. Each with rationale so future-Jordan doesn't re-litigate.

### 8.1 Visual image-diff regression (axe-core, Percy, Chromatic)

**Status:** Deferred to Phase 5. **Rationale:** Text-snapshot suffices for nav/disclaimer regression detection (Q20 closure gate #7). Image diff requires CI infrastructure (browser pool, screenshot service) not justified for n=30 demo. Phase 5 may revisit if mobile-responsive layout introduces visual states that text snapshots can't capture.

### 8.2 Mobile-responsive layout

**Status:** Deferred to Phase 5. **Rationale:** PI-skim-on-laptop is the target use case. Mobile breakpoints would double the test matrix and require Streamlit theme custom CSS beyond the wash+border pattern. Document in About page: "Optimized for desktop; mobile rendering not guaranteed."

### 8.3 i18n / Spanish disclaimer translation

**Status:** Deferred to Phase 5. **Rationale:** Sprint ships English-only. Spanish translation would double the disclaimer surface, the test matrix, and require careful clinical-Spanish vocabulary review (terms like "decisión clínica" carry different connotations than "clinical decision"). Phase 5 with Kallpa Spanish-language pivot is the natural home.

### 8.4 Model-card auto-generation from training metadata

**Status:** Already shipped (`docs/model_card.md`, Phase 8.1). **Rationale:** No UI surface needed; reviewers read the markdown file directly. Linking to it from the About page is sufficient (Q17.C caption includes link).

### 8.5 Per-prediction SHAP attribution

**Status:** Deferred to Phase 6. **Rationale:** SHAP on n=30 background data is mathematically vacuous (Q17.A). The `|w_i|` panel on About page is the honest substitute at current scale. Phase 6 with MIMIC-IV n≥200 is the right time to revisit.

### 8.6 GitHub Actions cron warmup of HF Space

**Status:** Rejected (Q18.A). **Rationale:** HF ToS gray area; risk of free-tier rate-limit or revocation. Passive-accept 30s cold-start is the honest framing, disclosed in Q9.1 caption. Paid HF hardware is the correct upgrade path if always-on becomes load-bearing.

### 8.7 Real EHR / FHIR ingestion

**Status:** Out of scope. **Rationale:** Sprint's input is the form. EHR ingestion requires HL7/FHIR client libraries, vendor-specific adapters, and PHI handling infrastructure that doesn't exist in this repo. Phase 7+ if Kallpa industry pivot needs it.

### 8.8 Multi-user authentication

**Status:** Out of scope. **Rationale:** No login, no sessions, no per-user state. Streamlit's default single-user-per-tab is sufficient for PI-demo use case. If Phase 6 needs per-user audit log isolation, that's a Phase 6 design problem.

### 8.9 Persistent audit log storage (S3, Postgres)

**Status:** Out of scope. **Rationale:** CSV export feature (Q13.A) provides the portability path. Permanent storage requires paid HF hardware or external infra. Phase 6 if regulatory environment requires N-day retention guarantees.

### 8.10 Real-time inference latency below 200ms

**Status:** Out of scope. **Rationale:** Free-tier inference is ~100ms warm; 200ms p95 is acceptable. Tighter latency requires caching infra not justified for n=30 model.

---

## §9. Appendix

### A. Quick reference, locked clinical presets

```python
PRESETS = {
    "high_risk_pam":             {"age": 12, "csf_glucose": 18.0,  "csf_protein": 420.0, "csf_wbc": 2100, "pcr": True,  "microscopy": True,  "exposure": True,  "symptoms": ["fever", "headache", "nuchal_rigidity"]},
    "bacterial_meningitis_limitation": {"age": 45, "csf_glucose": 38.0, "csf_protein": 180.0, "csf_wbc": 2500, "pcr": False, "microscopy": False, "exposure": False, "symptoms": ["fever", "headache", "nuchal_rigidity"]},
    "normal_csf":                {"age": 35, "csf_glucose": 65.0,  "csf_protein": 30.0,  "csf_wbc": 3,    "pcr": False, "microscopy": False, "exposure": False, "symptoms": []},
}

NEUTRAL_DEFAULTS = {"age": 12, "csf_glucose": 65.0, "csf_protein": 30.0, "csf_wbc": 3, "pcr": False, "microscopy": False, "exposure": False, "symptoms": []}
```

### B. Disclaimer text (verbatim, copy-paste ready)

```
⚠ Research prototype, NOT a medical device. Trained on n=30 synthetic patient vignettes (n_train=24, n_val=6); contains zero real PHI. Outputs are calibrated probabilities, **limited to** the n=30 training distribution, not diagnoses. Not for clinical decision support, not validated. Source + caveats: github.com/ljm234/amoebanator-25, Contact: lmontenegrocalla@mail.weber.edu (ORCID 0009-0000-7851-7139)
```

The 5 mandatory tokens enforced by `tests/test_app_disclaimer.py::test_disclaimer_on_every_page`:
1. `NOT a medical device`
2. `n=30`
3. `limited to`
4. `ORCID`
5. `lmontenegrocalla@mail.weber.edu`

### C. Pyright config delta (none expected; document if any)

Sprint may not modify `pyrightconfig.json` from the `b8f62e3` baseline. If a Streamlit dynamic-attribute access requires a targeted ignore, use inline `# pyright: ignore[reportAttributeAccessIssue]` with a comment explaining why, do NOT loosen the project-wide config.

### D. Color palette (locked, WCAG-AA compliant)

| Use | Text | Background | Border | Contrast |
|---|---|---|---|---|
| Error / limitation banner | `#B71C1C` | `#FFEBEE` | `#B71C1C` 4px left | 7.18:1 |
| Info banner | `#0D47A1` | `#E3F2FD` | `#0D47A1` 4px left | 8.21:1 |
| Success banner | `#1B5E20` | `#E8F5E9` | `#1B5E20` 4px left | 7.59:1 |
| Theme primary | `#0D47A1` | white | n/a | n/a |
| Theme text | dark slate | white | n/a | n/a |

### E. Sprint commit message template

```
<type>(<subphase>): <subject under 70 chars>

<body paragraph explaining the WHY of the change, not the WHAT -
what's already in the diff. Body is optional for trivial changes
but mandatory for any commit closing a Q-decision.>

Closes: Q<N>.<sub>, Q<M>.<sub>
Refs: PHASE_4_5_PLAN.md §<section>, AUDIT_REPORT.md §<section>
```

Examples:

```
feat(4.5.1): pages/01_predict.py with form + 3 presets + disclaimer

Implements the locked Q11.A neutral defaults form, the Q12.A 3-preset
buttons, the Q12.C D18 limitation banner placement, the Q15.A error
correlation-ID handling, the Q15.B graceful missing-stats banner, and
the Q15.D session-state debounce with 30s stale-lock recovery. Calls
the existing infer_one path (frozen) and emits WEB_PREDICT_RECEIVED +
WEB_PREDICT_RETURNED audit events.

Closes: Q11.A, Q12.A, Q12.C, Q15.A, Q15.B, Q15.D
Refs: PHASE_4_5_PLAN.md §4.2, AUDIT_REPORT.md §3.A Q5+Q11.A.fix
```

```
test(4.5.1): test_app_disclaimer.py with WCAG-AA contrast assertion

Adds 12 tests covering: 5 mandatory disclaimer tokens, link safety,
ORCID + email format, 4-page parametrized presence, 3 WCAG-AA contrast
combos, unique widget keys cross-page, reduced-motion CSS, and 2
_fmt_metric edge cases (NaN, inf).

Closes: Q19.B, Q15.5.A, Q15.5.B, Q15.5.D
Refs: PHASE_4_5_PLAN.md §4.3
```

---

**End of PHASE_4_5_PLAN.md.** Doc 3 (`PHASE_4_5_PROMPT_FINAL.md`) consumes this spec verbatim and packages it with operating rules into a single self-contained sprint-trigger prompt.
