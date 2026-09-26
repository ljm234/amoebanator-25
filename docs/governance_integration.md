# Governance integration, Amoebanator

This document describes the governance controls built into the Amoebanator
codebase and how they connect end to end: data governance, research
governance, audit governance, model governance, and runtime safety
governance. It is a map of what the code implements and which parts of it
run, not a claim of clinical-deployment readiness. The model and data cards
(`docs/model_card.md`, `docs/data_card.md`) and the proxy-task design
(`docs/rare_class_design.md`) carry the per-control detail; this document
shows how the controls fit together and states what posture they hold at
the current research stage.

---

## 1. Scope and posture

* **Posture.** Research stage, synthetic data, no clinical deployment. The
  controls below are implemented and tested so that the lineage to any
  real-data study would be governed from the first commit, not so that the
  system can be called governed for any clinical use. On the bundled
  synthetic dataset two controls (de-identification, the IRB gate) would be
  no-op safeguards for the model, and no training entry point calls either
  (Sections 2 and 3).
* **Frameworks.** No formal external AI-governance or quality-management
  framework (for example, a regulatory software-as-a-medical-device system)
  is adopted. The data-privacy controls map to the HIPAA Privacy Rule
  de-identification standard: the Safe Harbor method (45 CFR 164.514(b)(2)),
  which the code implements in part, and the Expert Determination method
  (45 CFR 164.514(b)(1)), for which it offers risk estimates but no
  determination workflow (Section 2); the audit trail is an unkeyed SHA-256
  hash chain with the limits stated in Section 4, and the IRB gate, the one
  control that would block training on a dataset, is called by no entry
  point (Section 3). The out-of-scope uses that bound the whole project are
  enumerated in `model_card.md` Section 2.

## 2. Data governance: de-identification and provenance

* **De-identification pipeline.** `ml/data/deidentification.py` implements a
  layered pipeline. The base layer is HIPAA Safe Harbor (45 CFR
  164.514(b)(2)): removal of fields named on a fixed list of 24 names
  spanning the eighteen identifier categories (the same identifier under
  another column name, such as `patient_name`, passes through), age capping
  at 89 and above, truncation to three ZIP digits and generalization to the
  year in other fields whose names contain `zip`, `postal` or `date`, and a
  pattern scrub of phone numbers, SSNs, e-mail addresses and slash-format
  dates in string values over 20 characters (`SafeHarborConfig`,
  `SafeHarborProcessor`). Statistical layers above it provide k-anonymity
  (every equivalence class at least size k) and Laplace noise on numeric
  fields, and separate helpers enforce l-diversity and check t-closeness for
  quasi-identifier risk; for the expert-determination method (45 CFR
  164.514(b)(1)) the module offers re-identification risk estimates
  (`ReidentificationRiskEstimator`) but no determination workflow.
* **On the bundled data.** The shipped 30-row dataset is synthetic and
  carries no identifiers. The loader that wraps the Safe Harbor layer,
  `ml/data_loader.load_tabular_safe_harbor`, would be a no-op for the model
  today (on the 30 rows it would only blank `physician` and cut
  `timestamp_tz` to the year, and neither is a model feature), and the
  trainer does not call it. That loader is a partial scrub:
  `SafeHarborProcessor` drops columns named on its list, but the loader
  copies back only the columns the processor returns and keeps its own copy
  of the rest, so identifier columns such as `name`, `mrn`, `ssn` or
  `zip_code` pass through it unchanged (the list's date columns, such as
  `date_of_birth`, are cut to the year by the loader's own date step), and
  it would not de-identify a real-data CSV on its own (`data_card.md`
  Section 4).
* **Provenance.** Every row of the bundled CSV carries `source`,
  `physician`, `timestamp_tz`, and a `case_id`. The bundled rows are tagged
  `source = "simulated"`, and rows from
  `ml/case_series.synthesize_yoder_cohort` are tagged
  `synthetic_from_yoder2010`, so both can be filtered out of any real-data
  metric by `source`; the synthetic MIMIC-shaped rows the loader tests use
  are tagged `mimic_iv`, like real MIMIC-IV rows, so `source` alone does not
  mark them as synthetic (`rare_class_design.md` Section 5). The per-row
  provenance lives in the CSV's own columns, and the data-load event that
  each training run writes to the audit chain records only the dataset path
  and its row and feature counts (`data_card.md` Section 2; `model_card.md`
  Sections 6 and 9).

## 3. Research governance: the IRB gate

* **The gate.** `ml/irb_gate.py` implements the gate
  (`check_irb_or_raise`), but no training entry point calls it; it runs only
  in `tests/test_irb_gate.py`. If every `source` value matches a synthetic
  prefix (`simulated`, `synthetic`, `bridge`), the gate treats the dataset
  as synthetic and permits it without an IRB record, logging a compliance
  check, because synthetic data does not require IRB approval. The gate
  does not treat rows tagged `mimic_iv` as synthetic
  (`ml/mimic_iv_loader.assemble_cohort` sets that tag on every row it
  assembles, which for a real cohort would be de-identified MIMIC-IV patient
  data), so outside research mode (next item) a MIMIC-IV cohort needs an IRB
  record like any real dataset. For any dataset that is not synthetic the
  gate reads `outputs/irb/current_irb.json` (or the path in
  `AMOEBANATOR_IRB_PATH`) and permits training only when the record's status
  is approved or conditionally approved; any other status, including a
  missing file or malformed JSON, raises `IRBGateBlocked` with a message
  naming the record path and the reason.
* **Research mode is visible.** An `AMOEBANATOR_RESEARCH_MODE` environment
  variable makes the gate skip the record check for any dataset, a MIMIC-IV
  cohort included, so it is appropriate only while the data are synthetic.
  The Docker image that the Hugging Face Space runs sets it (continuous
  integration does not); the gate, when it is called, logs each skip to the
  audit log, and the predict page shows a research-mode banner and logs an
  IRB status change event once per session, so research mode is never
  invisible.
* **Real-data path.** The MIMIC-IV proxy study in `docs/rare_class_design.md`
  is a pre-specified protocol that is not scheduled, and
  `ml/mimic_iv_loader.py` is a scaffold tested only on synthetic
  MIMIC-shaped data. Outside research mode a MIMIC-IV cohort would need an
  IRB record at this gate, and access to MIMIC-IV is additionally gated by
  PhysioNet credentialing and the MIMIC-IV data use agreement, outside the
  repository (`data_card.md` Sections 3 and 7).

## 4. Audit governance: the tamper-evident trail

* **Hash chain.** `ml/data/audit_trail.py` maintains a tamper-evident log.
  Each entry is linked to the previous one through a SHA-256 hash chain (the
  entry hash is computed over the entry fields together with the previous
  hash), and every 100 entries an in-memory Merkle-tree checkpoint
  summarizes the entries recorded since the previous checkpoint; the
  checkpoints are not written to the JSONL file.
  Editing a past entry without recomputing its hash and every later one
  breaks the chain, and `verify_chain` reports it as tampered (otherwise
  valid). The hashes are unkeyed and the latest hash is not anchored outside
  the log, so a rewrite that recomputes the hashes from the edited entry
  onward, or a truncated tail, still verifies as valid.
* **Event coverage.** The event types defined in `ml/data/audit_trail.py`
  span the data lifecycle (received, verified, released), access decisions
  (access denied), compliance (compliance check, IRB status change),
  integrity violations, session and configuration changes, and the web layer
  (prediction received and returned, rate-limit hit, preset loaded, audit
  export requested). Not all are emitted: the trainer writes data received,
  session start and end, configuration change and data released; the
  predict page writes the prediction and preset events, an IRB status change
  in research mode, and prediction errors under integrity violation; the
  audit page writes audit export requested. Data verified, access denied and
  compliance check come only from the Safe Harbor loader
  (`ml/data_loader.load_tabular_safe_harbor`) and the IRB gate, which no
  entry point calls, and nothing emits rate-limit hit.
* **Wiring and access.** The log path is configurable through
  `AMOEBANATOR_AUDIT_PATH`. Controls emit into the chain through
  `ml/audit_hooks`. The Streamlit Audit Log page (`pages/02_audit.py`)
  shows the shared log file read-only, with the events of all visitors
  (entries carry no session ID), and offers the whole chain as a CSV
  download (`app/audit_export.py`); building that CSV on each page run
  writes an audit export requested event. On the Space the log file is
  wiped when the container restarts, so the download is the way to keep a
  copy.

## 5. Model governance: versioning and change control

* **Versioning.** The model is V1.1. Its state_dict is regenerable from a
  pinned random seed via the documented training entry point, bit for bit in
  the environment recorded in `docs/REPRODUCIBILITY.md`; two full
  regenerations there produced the same `model.pt`. The tags `v1.0.0` and
  `v1.0.1` mark the earlier releases; their `model.pt` did not reproduce in
  that environment, so the model was retrained, and V1.1 retrains it again
  on standardized inputs (`outputs/model/scaler.json`) for 500 full-batch
  steps. The tagged artifacts remain retrievable from history
  (`model_card.md` Section 1; `data_card.md` Section 7).
* **Change control.** Re-fitting the model requires re-running the audit
  chain and re-fitting every downstream metric so that the model card stays
  synchronized with the artifacts it describes. Adding synthetic rows
  requires explicit `source` provenance, an audit re-run to record the
  addition, and a downstream re-fit (`data_card.md` Section 7;
  `model_card.md` Section 9).

## 6. Runtime safety governance

* **Intended-use enforcement.** The Streamlit application renders a research
  prototype disclaimer above every prediction surface. The banner states that
  the system is not a medical device, that it was trained on thirty synthetic
  vignettes containing no real protected health information, that the outputs
  are temperature-scaled probabilities (the temperature fit on six
  validation rows) limited to that training distribution rather than
  diagnoses, and that it is not for clinical decision support and not
  validated; it also carries the source link and the maintainer contact. A
  set of mandatory tokens in that banner, including the not-a-medical-device
  statement and the sample size, is asserted by the test suite
  (`app/disclaimer.py`; `tests/test_app_disclaimer.py`). The full set of
  out-of-scope uses is in `model_card.md` Section 2.
* **The safety stack.** Out-of-distribution detection is dual-gated:
  Mahalanobis distance on the seven non-symptom inputs and an energy score
  on the temperature-scaled logits. A split-conformal step follows. Each
  returns an explicit ABSTAIN with a reason field when triggered, and the
  dashboard shows the raw safety-signal breakdown beneath each prediction
  (`model_card.md` Section 8). How well the two gates detect shifted inputs
  is not established: on the bundled synthetic OOD benchmark neither
  separates covariate-shifted rows from the bundled rows (AUC 0.561 for the
  Mahalanobis distance, 0.568 for the logit energy; `model_card.md`
  Section 9). The predict page ignores a new submission while one is still
  running, with a lock that expires after 30 seconds; the web layer has no
  rate limit (`ml/data/audit_trail.py` has only an anomaly
  detector, `AuditAnomalyDetector`, that flags high event rates, bursts and
  off-hours events without limiting them, and the web layer does not use
  it).

## 7. Accountability

This is a single-author research project. The maintainer is reachable through
the repository, the corrections since `v1.0.1` are listed in the `v1.1.0`
release notes (https://github.com/ljm234/amoebanator-25/releases/tag/v1.1.0),
and the governance code, covering de-identification, the audit trail, the
IRB gate, and the safety stack, is open-sourced under the license stated in
`README.md` (`model_card.md` Section 1; `data_card.md` Section 7).

## Limits of these controls

These controls are real and tested, but their posture is research governance,
not deployment governance. On synthetic data the de-identification pass and
the IRB gate would be no-op safeguards for the model, and no training entry
point calls either (Sections 2 and 3); the audit chain governs a pipeline
that has never processed a real patient. They exist so that any
transition to real data would be governed from the first commit, not to
assert that the system is cleared for any clinical setting.

## References

The data-privacy controls draw on the HIPAA Privacy Rule de-identification
standard: 45 CFR 164.514(b)(1) Expert Determination and (b)(2) Safe Harbor,
with the HHS Office for Civil Rights de-identification guidance recorded in
`docs/references.bib` as `hipaa2012deident`; `docs/data_card.md` Section 4
cites the Safe Harbor standard (45 CFR 164.514(b)(2)). The methods
citations for the runtime safety stack (temperature scaling, split conformal,
energy and Mahalanobis OOD, decision curve analysis) are listed in
`docs/model_card.md` and `docs/references.bib`.
