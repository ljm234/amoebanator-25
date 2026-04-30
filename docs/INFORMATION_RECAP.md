# Information Recap, Phase 4.5 PRE-FLIGHT Discovery

**Author:** Jordan Montenegro-Calla (ORCID 0009-0000-7851-7139)
**Audit window:** 2026-04-26 to 2026-04-27
**Doc version:** v1.0 (locked 2026-04-27)
**Read this first if you're returning after a long gap.**

This is the human-readable narrative companion to the three formal Phase 4.5 outputs. It tells the story of what we found, what we changed, what's next, and what we're deliberately not hiding. If you're a future-Jordan returning after weeks away, or a reviewer wanting the backstory before diving into the audit report, start here.

The other three docs are formal artifacts:
- `docs/AUDIT_REPORT.md`, reviewer-grade evidence with path:line cites
- `docs/PHASE_4_5_PLAN.md`, locked specs in tabular form
- `docs/PHASE_4_5_PROMPT_FINAL.md`, sprint trigger prompt for fresh Claude Code session

This doc is the prose. Read it once, then refer to the others.

---

## §1. Where We Are

### 1.1 Project status (one paragraph)

Amoebanator 25 is a clinical-AI triage prototype that classifies *Naegleria fowleri* / PAM (primary amoebic meningoencephalitis) risk from 10 CSF + clinical features. The model is a small tabular MLP (914 params, 6.4 KB), trained on n=30 synthetic patient vignettes derived from published case-series marginals (Yoder 2010, Cope 2016, CDC 2025). Phases 1-9 shipped over the prior weeks: inference path wired, calibration via temperature scaling (Guo 2017, L-BFGS), conformal prediction with Vovk small-sample correction, three-gate OOD detection (Mahalanobis + Liu 2020 logit-energy + neg-energy), governance layer (audit hooks + de-identification + IRB gate), reviewer-grade documentation (Mitchell model card + DECIDE-AI + TRIPOD+AI + Gebru data card), Dockerfile + CI workflows + reproducibility guarantees. Total test count post-Phase-9: 1229. The Phase 4.5 PRE-FLIGHT discovery audit (2026-04-26 to 2026-04-27) was the gate between Phase 9 and the Phase 4.5 web-layer sprint that puts the demo on Hugging Face Spaces for medRxiv-reviewer-grade public viewing.

### 1.2 Since-last-recap delta (what changed in the last 48 hours)

The audit ran 22 questions over ~30 hours of asynchronous interview between Jordan and Claude Code (Opus 4.7). Outcome: 47 sub-decisions locked, 7 commits landed (4 refactors + 1 docs + 1 test + 1 baseline), test count went 1229 → 1233, all 7 closure gates for the audit phase satisfied. The discovery prompt explicitly forbade scope creep into sprint execution; only refactors directly motivated by audit findings were permitted, capped at 3 then deliberately overridden to 4 once the gate-inversion bug surfaced. That cap is now absolute. Phase 4.5 sprint executes against the locked specs in `PHASE_4_5_PLAN.md` via the trigger prompt in `PHASE_4_5_PROMPT_FINAL.md`.

### 1.3 The 7 audit commits in plain English

In topological order, oldest first:

1. **Pre-Phase-4.5 baseline (`46f33c4`).** The repo wasn't under git when the audit started; Jordan had also accumulated an unrelated `apex/` subdirectory (cryptography/post-quantum experiments unrelated to PAM). The audit moved `apex/` to a sister directory `~/Desktop/apex/` and initialized a fresh git repo. This baseline commit is the "Phase 4.5 starts here" anchor.

2. **MLP class extraction (`bed84df`).** The `MLP` class definition was duplicated across `ml/training.py` and `ml/training_calib_dca.py`, and `ml/infer.py` imported the model from the training module, meaning inference depended on training-module imports. The audit extracted `MLP` to a new `ml/model.py`, decoupled inference from training, and updated 7 import sites. Pyright caught 4 stragglers beyond the obvious 3.

3. **Conformal math de-duplication (`67039e3`).** The conformal q-hat calibration math (`compute_qhat` with finite-sample correction) was duplicated across three call sites, and the standalone reproducibility script (`scripts/conformal_fit_from_probs.py`) was bypassing the canonical implementation, silently suppressing `SmallCalibrationWarning` when n < 100. The audit routed the standalone script through `ml.conformal_advanced.compute_qhat` and added a round-trip warning-emission test.

4. **Logit-energy gate rename (`3fd05ed`).** The OOD gate used the comparison `if energy < tau_e: ABSTAIN reason="LowEnergy"`. The audit initially treated this as a naming clarity issue and renamed the abstain reason to `LogitEnergyBelowInDistFloor` to make the (unusual) confidence-floor semantics explicit. Math left unchanged. Subsequently superseded by commit 7.

5. **IRB gate emission tests (`6654877`).** The IRB gate (`ml/irb_gate.py`) emitted `AuditEventType.ACCESS_DENIED` and `AuditEventType.IRB_STATUS_CHANGE` events but no test asserted on those emissions. The audit added two tests verifying the emissions. Test-only commit, didn't count against the refactor cap (same precedent as commit 3).

6. **References bib additions (`6f02a75`).** The Q11 inline-tooltip strategy needed clinical references for the "always-shown" and "p_high < 0.3 (normal CSF)" buckets. Added Tunkel 2004 IDSA bacterial meningitis guidelines (PMID 15494903) and Seehusen 2003 AFP CSF analysis (PMID 14524396). Total references: 20 → 22. Comment header added explaining ML methodology refresh deferral to Phase 8.5 preprint prep.

7. **Logit-energy gate semantics flip (`b8f62e3`).** The audit's biggest catch. When the four locked clinical presets were run through `infer_one` for live verification, the gate fired on **all four**, including unambiguously in-distribution cases. Root cause: the comparison direction was inverted from Liu 2020 canonical semantics. The Liu 2020 framing is *"abstain when energy > tau (above the in-distribution shift, i.e., OOD)"*, not *"abstain when energy < tau (below the in-distribution floor)"*. The fix flipped the math (`<` → `>`), re-fit the threshold at q=0.95 (the correct Liu 2020 percentile), and renamed the abstain reason to `LogitEnergyAboveOODShift`. Three test fixtures had to be rewritten with tau values flipped. The cap was raised from 3 to 4 with explicit rationale and locked absolutely. Post-flip preset re-verification: 12 orders of magnitude separation between Low (1.9e-13) and High (1.0); Mahalanobis catches OOD positive control; gate quiet on in-distribution.

Plus four documentation commits for Phase J outputs: `0543c06` AUDIT_REPORT.md, `5938cd8` PHASE_4_5_PLAN.md, `82f0d85` PHASE_4_5_PROMPT_FINAL.md, `442541c` self-containment fix.

---

## §2. What We Found That Surprised Us

The audit caught seven things that would have shipped to medRxiv reviewers if the audit hadn't run. These are stories told in plain English; the formal evidence is in `AUDIT_REPORT.md` §3 + §4.

### 2.1 The OOD gate was firing in the wrong direction

The single most consequential finding. The logit-energy OOD gate at `ml/infer.py:232` used `if energy < tau_e: ABSTAIN`, with the threshold `tau_e = -0.99` fit at the 5th percentile of in-distribution validation logits. The original framing was *"low logit-energy means the model is uncertain, so abstain."* This sounds plausible but is **the opposite of Liu 2020**, which is the canonical citation for energy-based OOD detection in the literature. Liu 2020 frames it as *"high logit-energy means the input lives above the in-distribution shift, hence is OOD, hence abstain."* The audit caught the inversion not by reading Liu 2020 carefully but by running the four locked clinical presets through `infer_one` and observing the gate fired on all four, including the NEUTRAL DEFAULTS preset which is unambiguously in-distribution. An OOD gate that fires on every input is a constant-true predicate, not an OOD gate. The fix flipped the comparison, re-fit at q=0.95, renamed the abstain reason, and updated three test fixtures. Beam (calibration sense) would have caught this in 30 seconds; we caught it before he had to.

### 2.2 Temperature scaling at T=0.27 is amplifying logits, not attenuating them

The calibrated temperature is `T = 0.2723`. Standard Guo 2017 temperature scaling has T > 1, the calibrator divides logits by T to *attenuate* overconfident predictions. But T = 0.27 means dividing by 0.27 ≈ multiplying by 3.7×. The calibrator is *amplifying* the model's raw confidence, which is the opposite of typical temperature-scaling behavior. This isn't a bug in the calibration code, it's what L-BFGS optimization on n=6 validation samples produces when the loss landscape has insufficient curvature to constrain T meaningfully. The fit is essentially a noise-optimized point estimate. The audit's response is *not* to "fix" the T value (any other T at n=6 would be equally arbitrary). Instead, the predict page surfaces a `T=0.27 (n=6)` badge with a hover tooltip explaining the amplification, plus a yellow `SmallCalibrationWarning` banner. Beam reads "T<1" and immediately knows what's happening. The honest surfacing is the entire response.

### 2.3 The model can't tell bacterial-NOT-PAM from PAM yet

When the four clinical presets were run for live verification, the bacterial-meningitis-but-NOT-PAM preset returned `prediction=High` with `p_high = 1.0`, identical to the actual PAM preset. The model can't distinguish them. Root cause: the n=30 training set contains zero non-PAM bacterial meningitis cases. The model has never seen the contrastive case it would need to learn the distinction. The audit's response was *not* to drop the bacterial preset from the demo (that would hide the limitation). It was to keep the preset, rename it `bacterial_meningitis_limitation`, and render a red banner adjacent to the result explaining: *"⚠ This preset is a known model limitation. Training data (n=30) contains zero non-PAM bacterial meningitis cases, so the model cannot distinguish bacterial-NOT-PAM from PAM. The Phase 6 MIMIC-IV cohort (target n ≥ 200, includes bacterial vs viral meningitis labels) will fix this. We surface this preset deliberately as an honesty signal, every model has limits, and showing them where they bite is more useful than hiding them."* Plus an xfail-decorated regression test with `strict=False` so when Phase 6 fixes the limitation, the test transitions to XPASS as a "fix this" signal rather than breaking CI. Beam, Chen, Zitnik all reward demos that volunteer limitations rather than letting reviewers dig for them.

### 2.4 Three places computing conformal q-hat

The conformal calibration math (`compute_qhat` with Vovk finite-sample correction) was duplicated across three call sites: the canonical `ml/conformal_advanced.compute_qhat` with `SmallCalibrationWarning`, an inline copy in `scripts/conformal_fit_from_probs.py`, and another inline copy in `scripts/refit_conformal_held_out.py`. The standalone `conformal_fit_from_probs.py` script bypassed the canonical implementation entirely, which meant the `SmallCalibrationWarning` (fires when n_cal < 100) was silent in that path. This is the bug class where one copy gets updated and the others diverge silently. The audit routed the standalone script through `ml.conformal_advanced.compute_qhat`, eliminating one duplicate and restoring the warning emission. The held-out script's inline copy was left intact (it's a different reproducibility entry point with different semantics, not a bug-class duplicate). Two duplicates collapsed; one preserved with rationale.

### 2.5 Eleven audit event types defined but never emitted

The `AuditEventType` enum in `ml/audit_hooks.py` (or `ml/data/audit_trail.py`, depending on layout) declared 11 values that no `_emit()` call in the runtime path ever reached and no test asserted on. These are the "audit fantasy" analogue of dead code: features that exist in nominal docs but not in observed behavior. A reviewer auditing the governance layer would find the 11 declarations and reasonably ask "where do these emit from?", and the honest answer would be "they don't." The audit's resolution is to delete all 11 dead values inside the Mini-1 sprint as part of the same commit that adds the three new web-only event types (`WEB_PREDICT_RECEIVED`, `WEB_PREDICT_RETURNED`, `WEB_RATE_LIMIT_HIT`). Same file, same commit, net delta -8 values. The cleanup happens in-sprint rather than pre-sprint because the cap was already at 4 refactors when this finding surfaced.

### 2.6 PyTorch import dominates 3.7s boot, model load is 59 milliseconds

The audit initially estimated cold-start budget as "model load ~500ms" (a guess, not a measurement). When the actual cold-start was profiled with `python -X importtime`, the result overturned the estimate: `import torch` took 3.7 seconds, `_load_model_artifacts()` took 59 milliseconds. The model isn't slow to load; PyTorch is slow to import. This matters for two reasons. First, it kills the optimization story: there's no `@st.cache_resource` change that would meaningfully reduce cold-start, because the dominant cost is library import and `@lru_cache` is already wrapping `_load_model_artifacts()`. Second, it overturned the audit's prior framing of cold-start as "model loading." HF Spaces free-tier cold-start (~30s) is dominated by container provisioning (~25s) plus PyTorch import (~3.7s) plus everything else (~1.3s). Passive accept is the only honest response; the disclaimer caption already discloses the 30s expectation.

### 2.7 HF Space repo template defaults to port 8501, not 7860

When drafting the `.streamlit/config.toml` spec, the audit's initial proposal had `port = 7860` (the Gradio default port, which is what the audit assumed Streamlit on HF Spaces would use). Before locking the spec, the audit cloned the actual HF Space repo (`huggingface.co/spaces/luisjordanmontenegro/amoebanator-25`) and inspected the auto-generated Dockerfile. It said `EXPOSE 8501` and `--server.port=8501`, Streamlit's default, not Gradio's. If the locked `config.toml` had shipped with port 7860, the deployed Space would have failed health checks on cold-boot with a confusing error (build succeeds, runtime fails). This catch was a 5-minute side trip that prevented a 2-hour debug session post-deploy. It's also a representative example of the audit's "2026-real not fantasy" rule: external claims must be verified against current docs, not against memory.

---

## §3. What's Next

### 3.1 Mini-1 in plain English (one paragraph)

Mini-1 ships the form, the three preset buttons, the disclaimer, and the audit-export utilities. About 600 lines of production code across four new modules in `app/` (utils, presets, disclaimer, audit_export) plus one new page (`pages/01_predict.py`). Plus four test files totaling ~50 tests, plus a visual snapshot baseline. The form opens with NEUTRAL defaults (csf_glucose=65 normal, csf_protein=30 normal, csf_wbc=3 normal, all toggles off, no symptoms checked) so a PI clicking the demo sees the model say "Low" before doing any work, the discrimination story is in clicking presets, not in pre-rigged form values. The three preset buttons load the high-risk PAM scenario, the bacterial-NOT-PAM limitation demo, and the normal CSF negative control. The result panel renders four badges: decision, T=0.27 calibration warning, small-calibration banner, and the 3-state conformal regime badge (currently  INVALID at n=6, α=0.10, k=7). Errors get caught by an outer try/except that generates a uuid4 correlation ID, shows a 12-char ID to the user, and emits an `INTEGRITY_VIOLATION` audit event with the full ID for server-side debugging. Mini-1 takes about 2-3 hours of focused execution.

### 3.2 Mini-2 in plain English (one paragraph)

Mini-2 ships the audit page, the about page, the references page, and the multi-page navigation. About 350 lines across three new pages plus a small `app/app.py` for `st.navigation` registration. Plus four more test files totaling ~40 tests. The audit page renders the session's audit log via `st.table` (true HTML table semantics for screen readers, not `st.dataframe`'s virtualized React grid), capped at the last 10,000 rows with a banner explaining the cap, plus a "Download session audit log (CSV)" button that exports the full session including hash chain pointers. The about page has the model architecture summary, the calibration summary with link to the model card, the `|w_i|` feature-importance bar chart with locked caption explaining it's model-level (not per-prediction attribution), the conformal advanced expander with α slider, and the authorship + ORCID + handle-disclosure one-liner. The references page lists all 22 BibTeX entries grouped by category. Mini-2 takes about 2 hours of focused execution.

### 3.3 Sprint duration estimate, calendar dates, blocking dependencies

Mini-1: ~2-3 hours. Mini-2: ~2 hours. Realistic calendar dates (assuming Jordan is the bottleneck for the Mini-1 → Mini-2 transition vote): start Mini-1 the same day USER ASSIGNMENT Steps 6 (HF_TOKEN) and 8 (gh repo rename) complete; finish Mini-2 within 24-48 hours including review windows. Total wall-clock: 2-3 days conservative, 1 day optimistic. The two USER ASSIGNMENT steps are the blocking pre-sprint dependencies. Step 7 (Vercel /playground link-out edit) is post-sprint and doesn't block sprint kickoff.

### 3.4 What success looks like (qualitative)

A reviewer (Beam, Zitnik, Chen) opens the HF Space link, the app boots in ~30 seconds (cold-start, disclosed), the disclaimer is the first thing they read. They click the high-risk PAM preset, see `prediction=High` with `p_high=1.0`, see the  INVALID conformal regime badge explaining why the formal guarantee doesn't apply at n=6, see the T=0.27 calibration badge explaining the amplification, see the Mahalanobis d² and logit-energy values gate-quiet for in-distribution. They click the bacterial preset, see `prediction=High` again, then immediately see the red limitation banner explaining why this is a known model failure mode and what Phase 6 will fix. They click the normal CSF preset, see `prediction=Low` with `p_high=1.9e-13`, see the discrimination story (12 orders of magnitude). They click the audit page, see the JSONL chain with hash pointers, click download CSV, get a verifiable audit trail they can run `verify_chain()` against from a cloned repo. They click the about page, see the `|w_i|` panel with caption explicitly disclaiming "this is NOT per-prediction attribution; model-level only; range 9.1%-11.5% confirms n=30 near-equal weighting." They close the tab having spent 5 minutes and learned more about the model's honest limits than they would from reading 50 pages of preprint methodology. That's the success state.

### 3.5 What failure looks like (early-warning signals)

Three failure modes to watch for during Mini-1 + Mini-2:

1. **Test count regression.** If `pytest --collect-only -q` ever shows fewer tests than the cumulative target (1280 after Mini-1, 1320 after Mini-2), something got deleted accidentally. Bisect to find the deletion.
2. **Pyright errors creep up against b8f62e3 baseline.** If the diff between current pyright output and the baseline shows new errors, fix at root or add targeted ignores with comments. Do NOT loosen project-wide config.
3. **Visual snapshot drift exceeds 5% character delta on harmless changes.** If the snapshot fails on a refactor that didn't change behavior, the snapshot is over-tight. Either regenerate via `pytest --snapshot-update` (intentional) or investigate (regression).

If any of these fire and the cause isn't immediately obvious, stop and tell Jordan. Don't paper over.

---

## §4. Honest Limitations We're Not Hiding

Five permanent caveats the demo will not bury. Each is disclosed in the UI, the disclaimer, the model card, and the about page, the same caveat appears in multiple places by design.

### 4.1 The n=30 cohort is the load-bearing limitation

Every uncertainty caveat traces back to `n_train=24, n_val=6`. T=0.27 is a noise-fit on n=6. The conformal guarantee is mathematically inapplicable because k=7 > n=6. The model can't distinguish bacterial-NOT-PAM from PAM because the training set has zero non-PAM bacterial cases. None of these are bugs in the methodology code; they are sample-size artifacts. The model card and the disclaimer both lead with the n=30 number. The Phase 6 MIMIC-IV cohort (target n ≥ 200) is the next phase that will produce externally-grounded calibration.

### 4.2 Synthetic vignettes have no real-world calibration

The n=30 training data is synthetic patient vignettes drawn to match published case-series marginals (Yoder 2010, Cope 2016, CDC 2025). This is reproducibility-friendly (any future researcher can re-derive the same training set from the same marginals + seed), but it's not externally validated. The model has never seen a real patient. The Phase 6 MIMIC-IV cohort will be the first contact with real-world clinical data.

### 4.3 L-BFGS calibration is a noise-optimized point estimate

The `T = 0.2723` value was found by running L-BFGS optimization on n=6 validation samples. The loss landscape at that sample size has insufficient curvature to constrain T meaningfully. Different random subsets of n=6 would produce different T values in the range 0.1-2.0. The reported T should be treated as a sample-specific point estimate, not as evidence of structural under-confidence or over-confidence. The UI surfaces this directly via the `T=0.27 (n=6)` badge and hover tooltip.

### 4.4 HF Space ephemeral filesystem

Audit log persistence is per-session only. The chain integrity is preserved within a session and can be exported as CSV for permanent verification, but cross-session persistence (audit log surviving a container restart) requires paid HF hardware or external storage (S3, Postgres), both out of scope. The disclaimer in the audit page explains this; the CSV download button is the user's path to permanent retention.

### 4.5 Single-author audit, no peer code review

The audit was conducted by one human (Jordan) with one LLM (Claude Code Opus 4.7). No second pair of human eyes reviewed the audit's findings or the 7 commits before the formal output docs were written. Reviewer-grade defensibility relies on three things: the verbatim-prompt evidence trail in `AUDIT_REPORT.md` §9 Appendix A (proves the discovery process was real, not retconned), the per-commit Q-traceability via the Closes/Refs footer convention (any reviewer can `git log --grep="Q11.A"` to find the implementing commit), and the post-flip preset re-verification table being independently re-runnable from the committed `outputs/model/model.pt` (sha256 in `AUDIT_REPORT.md` §1).

---

## §5. Why This Matters

### 5.1 Stakeholder ladder

Three downstream stakeholders read this demo. Each has a different audit lens:

1. **medRxiv reviewers (submission Oct 2026, ~6 months from now).** They want to know: is the cohort definition honest? Is the calibration well-disclosed? Is uncertainty handled rigorously? Is reproducibility real? The demo is a supplementary artifact for the preprint, demonstrating that the pipeline actually works end-to-end on the cohort the paper describes.
2. **PhD application reviewers (Fall 2027, ~12 months from now).** PIs Marinka Zitnik (Harvard, graph + clinical AI), Jonathan Chen (Stanford, clinical informatics), Andrew Beam (Harvard, calibration + uncertainty), Pranav Rajpurkar (Harvard, clinical foundation models), Brett Pickett (BYU, computational epidemiology). Each has a different audit reflex; the demo must survive 30 seconds of skim from any of them. The audit's Beam-30s heuristic was concrete: would Beam catch this in 30 seconds? If yes, fix it before he has to.
3. **Kallpa industry pivot (post-PhD-app, ~2027-2028).** Demonstrable working clinical-ML system + honest limitation surfacing + reproducibility hygiene. The Kallpa pivot uses the demo as evidence of operational competence, not just methodology competence.

### 5.2 What each stakeholder will see

- **medRxiv reviewer:** clicks the link in the supplementary materials, sees the disclaimer, runs a preset, reads the calibration regime badge, downloads the audit log, verifies the chain, closes the tab. Time investment: 5 minutes.
- **PhD app reviewer:** clicks the link in the application portfolio, sees the demo, recognizes the regime classification (Beam) or the limitation banner (Chen) or the model-card link (Zitnik) as familiar reviewer-grade signals. Time investment: 2 minutes.
- **Kallpa team member:** clones the repo, runs the test suite, reads the model card and the audit report, looks for the operational seams (Dockerfile, config, deploy workflow). Time investment: 30 minutes if interested.

### 5.3 What we're NOT promising

The demo is not a clinical decision support tool. It is not validated for patient care. It does not generate diagnoses; it generates calibrated probabilities under the n=30 training distribution. The disclaimer says this on every page. The "limited to the n=30 training distribution" wording (locked in Q19 after explicit micro-correction by Jordan) makes the scope of validity explicit. A reviewer who reads the disclaimer cannot reasonably claim they were misled.

---

## §6. Glossary

Plain-English definitions for the 18 terms a future reader (or non-CS reviewer) might need.

- **ABSTAIN.** Model output indicating "I shouldn't predict on this input" rather than "Low" or "High." Triggered by OOD detection or conformal ambiguity. Includes a reason field (e.g., `OOD`, `LogitEnergyAboveOODShift`, `ConformalAmbiguity`).
- **AppTest.** Streamlit's testing framework for headlessly running a page and asserting on its rendered output. Used in this sprint for closure gate criterion #3 (boot in <5s).
- **AUC.** Area Under the (ROC) Curve. A metric for classifier discrimination quality. Reported as `1.0` in the model card with explicit "infrastructure proof, not generalisable" caveat, n=6 validation set is too small for AUC to be meaningful.
- **Conformal q-hat.** The threshold value computed during conformal calibration that determines prediction set width. At α=0.10 and n=6, q-hat is currently 0.0162.
- **IRB_BYPASS.** An environment variable that short-circuits the IRB gate to allow boot on synthetic-data deployments. Set to `1` in the Dockerfile because the n=30 cohort is fully synthetic (no real PHI). Must flip to `0` when Phase 6 lands real MIMIC-IV cohort.
- **L-BFGS.** Limited-memory BFGS optimizer. Used by Guo 2017 temperature scaling to fit the calibration parameter T. At n=6 the optimization landscape lacks curvature, so T = 0.27 is a noise-optimized point estimate.
- **Liu 2020 energy gate.** OOD detection method based on the logit energy `−logsumexp(logits)`. Inputs with high energy live above the in-distribution shift, hence are likely OOD, hence trigger abstain. Originally inverted in this codebase; flipped to canonical semantics in commit `b8f62e3`.
- **Mahalanobis distance.** OOD detection method based on the squared distance from a feature vector to the training distribution mean, scaled by the covariance matrix. At threshold τ=24.86, the OOD positive control fires at d²=42104 (well above τ).
- **PAM.** Primary Amoebic Meningoencephalitis. A rare CNS infection caused by *Naegleria fowleri* (the "brain-eating amoeba"). 167 cumulative US cases per CDC 2025; 4 survivors; ~97% case-fatality rate.
- **PHI.** Protected Health Information. Patient data covered by HIPAA. The Phase 4.5 demo handles zero PHI (training data is synthetic vignettes); Phase 6 introduces real PHI from MIMIC-IV.
- **prefers-reduced-motion.** A CSS media query that user browsers expose when the user has enabled the OS-level "reduce motion" accessibility preference. The audit's CSS injection block honors this preference by disabling animations and transitions.
- **`st.cache_resource`.** Streamlit's caching decorator for expensive resources like ML models. Cached across reruns within a session. Used for `_load_model_artifacts()` (already `@lru_cache`-wrapped, so don't double-wrap) and `load_presets()`.
- **st.table vs st.dataframe.** Streamlit has two table-rendering primitives. `st.table` emits a true HTML `<table>` element with `<thead>`/`<tbody>` semantics that screen readers (NVDA, VoiceOver) can navigate row-by-row. `st.dataframe` emits a virtualized React grid that screen readers can't navigate. The audit page uses `st.table` for accessibility.
- **T (temperature).** The single learnable parameter in temperature scaling (Guo 2017). Standard behavior: T > 1 attenuates overconfidence. This codebase's T = 0.2723 means the calibrator is amplifying logits, the opposite direction, an artifact of n=6 noise-fit.
- **Visual regression text-snapshot.** A test that captures the markdown output of a Streamlit page and asserts it hasn't drifted >5% character delta from a committed baseline. Catches nav/disclaimer regressions that unit tests miss. Lives at `tests/_snapshots/<page>.md.snap`.
- **WCAG-AA.** Web Content Accessibility Guidelines, Level AA. The audit uses the contrast ratio requirement: text/background contrast ≥4.5:1 for normal text. The locked color combos achieve ≥7.18:1 (well above threshold).
- **xfail (with strict=False).** Pytest decorator marking a test as "expected to fail." With `strict=False`, the test passes CI when it fails (xfailed) AND when it succeeds (xpassed). The bacterial-limitation regression test uses this so when Phase 6 fixes the limitation, the test transitions to XPASS as a "fix this" signal rather than breaking CI.
- **|w_i| feature importance.** Model-level feature importance computed as the mean absolute weight of the first `Linear(10,32)` layer averaged across the 32 output dimensions, normalized by sum. Range 9.1%-11.5% (max/min ratio 1.27×) confirms the n=30 model treats all 10 features near-equally. Honest substitute for SHAP at this sample size.

---

## §7. Pointers

- **Specs lock:** `docs/PHASE_4_5_PLAN.md` (1,000 lines), locked sprint specification with all 47 sub-decisions, file-by-file Mini-1/Mini-2 specs, 8-risk register, tiered user assignments.
- **Sprint trigger:** `docs/PHASE_4_5_PROMPT_FINAL.md` (913 lines, post self-containment fix), paste this entire document as the first message to a fresh Claude Code session to execute Mini-1 + Mini-2.
- **Reviewer-defensible audit trail:** `docs/AUDIT_REPORT.md` (1,062 lines), per-Q evidence, D1-D18 cross-cutting findings, 22-reference index, verbatim-prompt appendix pointer.
- **Audit transcript (raw):** `/Users/jordanmontenegro/.claude/projects/-Users-jordanmontenegro-Desktop-Amoebanator-25/a62ae6d8-9c41-48c4-aa08-f855fdc6cfb5.jsonl` (6.2 MB, 1,836 lines), full Claude Code session jsonl. The single canonical source.
- **Code:** `https://github.com/ljm234/amoebanator-25` (after USER ASSIGNMENT Step 8 rename from `Amoebanator_25`).
- **Demo (post-deploy):** `https://huggingface.co/spaces/luisjordanmontenegro/amoebanator-25` (Streamlit Docker SDK, free CPU Basic).
- **Pre-sprint user assignments:** `docs/USER_ASSIGNMENTS.md` Steps 6 (HF_TOKEN secret) and 8 (gh repo rename) must complete before sprint kickoff.

If you're returning to this project after weeks away, read this doc end-to-end first, then open `PHASE_4_5_PROMPT_FINAL.md` if executing the sprint or `AUDIT_REPORT.md` if reviewing the audit's findings.

---

**End of INFORMATION_RECAP.md.** Phase 4.5 PRE-FLIGHT discovery audit complete. Ready for sprint kickoff.
