# Future Work, Phase 4.5 sprint backlog

Items deferred during sprint execution that were either out of scope, would have caused scope creep mid-task, or surfaced as documentation drift to be cleaned up at a natural seam (typically Mini-2 or post-sprint).

Each entry: source task / discovery → action → owner → trigger.

---

## Mini-2 cleanup items

### HF Space entrypoint namespace collision (`app/` package vs. root entry)

**Source:** Spec-gap #10 (post-Mini-2 push, surfaced by HF Space build crash on commit `447c493`).

**Issue:** HF Space's default Streamlit discovery expects an entrypoint file at the repo root (`app.py` or `streamlit_app.py`). The Mini-2 layout placed the navigation entry at `app/app.py`, but the `app/` package directory at the same level shadowed the resolution and the Space build crashed before Streamlit started. Hot-fixed by renaming `app/app.py` → `streamlit_app.py` (commit `e3a26d0`), with `Dockerfile` `CMD` and `tests/test_app_navigation.py` import path updated to match.

**Action:** Two forward items:
- Add an "HF Space build smoke-test" gate to the closure protocol (either `docker build .` locally with the Space's expected layout, or a CI job that runs `streamlit run streamlit_app.py --server.headless true` and checks for clean boot).
- Document the entrypoint convention (`streamlit_app.py` at root, `app/` package for modules only) in `docs/REPRODUCIBILITY.md` so the collision can't be reintroduced by future renames.

**Owner:** Phase 5 sprint kickoff (closure-gate addition); Mini-2 cleanup or Phase 5 entry (docs update).

**Trigger:** Convenient, does not block current work, but should land before any future entrypoint reshuffling.

---

### Closure-gate parameterization to mirror CI workflow exactly

**Source:** Spec-gap #9 (post-Mini-2 push, surfaced by CI failure on commit `079d2a8`).

**Issue:** Mini-1 + Mini-2 closure protocols ran 7 gates (test count, pyright, AppTest boot, CSV roundtrip, disclaimer parametrized, IRB_BYPASS, visual snapshot) but did NOT include `ruff check ...` matching the CI workflow. Result: 6 ruff violations (1× `E741` ambiguous `l`, 5× `F541` unused f-string prefixes) shipped to GitHub and broke CI on the first push of the Mini-1+Mini-2 commits. Hot-fixed in the post-push cleanup commit; underlying gap is that the closure protocol should mirror CI commands exactly.

**Action:** Next sprint kickoff (Phase 5 or successor): add `ruff check <paths>` and `mypy <wired modules>` to the closure-gate list. The closure-gate spec in `PHASE_4_5_PROMPT_FINAL.md` §3.3 should be regenerated for the next sprint with these gates included.

**Owner:** Phase 5 sprint kickoff.

**Trigger:** Convenient, does not block any current work.

---

### Documentation drift: `streamlit run app.py` references

**Source:** Mini-1 spec-gap #8 (T1.x legacy_app.py rename). **Status:** PARTIALLY DONE, `.github/workflows/test.yml` ruff path updated post-Mini-2 (commit hot-fix). README/SPRINT_LOG/REPRODUCIBILITY.md still pending.

**Issue:** Phase 4.5 Mini-1 renamed top-level `app.py` → `legacy_app.py` to unblock the `app/` package shadowing collision. Multiple docs still reference `streamlit run app.py` as the entry point:

- `README.md:61`, `streamlit run app.py`
- `README.md:82`, Streamlit dashboard table mentions `app.py`
- `README.md:138`, file-tree comment for `app.py`
- `docs/SPRINT_LOG.md:10, 24, 84, 342, 345, 538`, Phase 1.3 sprint log mentions
- `docs/REPRODUCIBILITY.md:150`, `ruff check ml/ scripts/ tests/ app.py`
- `docs/decide-ai.md:38`, DECIDE-AI table mentions
- `docs/AMOEBANATOR_MASTER_PROMPT.md:366`, Phase 1.3 Streamlit app mention

**Action:** Update each reference:
- README.md `streamlit run app.py` → `streamlit run app/app.py` (the new st.navigation entry created in Mini-2 T2.5).
- SPRINT_LOG.md mentions can either stay (historical record of Phase 1.3) or get a footnote pointing forward.
- REPRODUCIBILITY.md `ruff check` line: `app.py` → `legacy_app.py app/`.
- DECIDE-AI / MASTER_PROMPT mentions: cross-reference to the new entry point.

**Owner:** Mini-2 cleanup commit.

**Trigger:** After T2.5 (`app/app.py` st.navigation entry) lands and is verified green via Mini-2 closure gates.

**Why deferred to Mini-2 (not patched mid-Mini-1):** `app/app.py` doesn't exist yet. Updating README to point at a non-existent entry point now would create new drift; Mini-2 is when the new entry actually exists.

---

### Pyright baseline reduction

**Source:** Mini-1 closure report spec-gap #2.

**Issue:** Pyright project-wide baseline at `b8f62e3` is 6 errors (in `ml/training.py`, `ml/training_calib_dca.py`, `scripts/bootstrap_metrics.py`). Mini-1 closure gate criterion #2 is delta-vs-baseline (not absolute zero). The 6 are pre-existing and Mini-1 did not touch these files.

**Action:** Triage the 6 errors:
- `ml/training.py:48-49`, `bool.sum` attribute access (likely a numpy boolean array vs Python bool confusion)
- `ml/training_calib_dca.py:79-80, 132`, same pattern + `list[Unknown].astype` issue
- `scripts/bootstrap_metrics.py:37`, `floating[Any]` not assignable to `float`

Fix at root or add targeted `# pyright: ignore` with comment per the standing instruction. One-shot post-Mini-2 cleanup commit.

**Owner:** Post-sprint cleanup or Phase 5 entry.

**Trigger:** Convenient, does not block Mini-2 or sprint deploy.

---

### `schema_version` field on JSONL audit entries

**Source:** Mini-1 closure report spec-gap #4.

**Issue:** `app/audit_export.py` uses a static `CSV_SCHEMA_VERSION = "1"` constant for the CSV column. The underlying JSONL audit entries (`ml/data/audit_trail.AuditEntry`) have no `schema_version` field. The audit-time spec said to "bump schema version field in audit.jsonl genesis entry to '2'" but the field doesn't exist yet to bump.

**Action:** Add `schema_version: int = 1` field to `AuditEntry` NamedTuple, threaded through `_compute_entry_hash` (changes the hash so old logs become incompatible, needs migration plan), or introduce a separate `audit_schema.json` metadata file that records the format version of the JSONL log alongside it.

**Owner:** Phase 5 or Phase 6 (when MIMIC-IV ingestion warrants real schema evolution).

**Trigger:** When the JSONL format changes shape (e.g., new field, renamed field, format break), until then the static CSV constant suffices.

---

### `_fmt_metric` NaN/inf handling

**Source:** Mini-1 T1.8 `tests/test_app_disclaimer.py` test-utils edge cases.

**Issue:** Current `_fmt_metric` in `app/utils.py` returns the literal string `"nan"` or `"inf"` for NaN/inf inputs (because they're valid floats and pass the `try: float(value)` block). The test allows either `"-"` or the pass-through, defensive but arguably the spec intent was "non-numeric gets em-dash."

**Action:** Decide: special-case NaN/inf with `math.isnan` / `math.isinf` and return `"-"`, OR document the pass-through as intended ("inference output is honest about what it computed; em-dash only for missing keys"). Update test to assert the chosen behavior, not accept both.

**Owner:** Post-Mini-2 cleanup.

**Trigger:** Convenient, defensive tests don't block.

---

## Watch list (no action yet)

### Pyright transient `audit_hooks unknown import` diagnostic

`from ml import audit_hooks as ah` triggers a transient pyright diagnostic that doesn't appear in `pyright tests/test_audit_export.py` or `pyright` project-wide. Suspected pyright import-resolution timing issue. Reappears occasionally; project-wide error count unchanged. Not blocking; not actioning unless it becomes load-bearing.
