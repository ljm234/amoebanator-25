# Governance integration, Amoebanator

This document describes the governance controls built into the Amoebanator
codebase and how they connect end to end: data governance, research
governance, audit governance, model governance, and runtime safety
governance. It is a map of what is enforced in code, not a claim of
clinical-deployment readiness. The model and data cards
(`docs/model_card.md`, `docs/data_card.md`) and the proxy-task design
(`docs/rare_class_design.md`) carry the per-control detail; this document
shows how the controls fit together and states, plainly, what posture they
hold at the current research stage.

---

## 1. Scope and posture

* **Posture.** Research stage, synthetic data, no clinical deployment. The
  controls below are implemented and tested so that the lineage to the
  planned real-data study is governed from the first commit, not so that the
  system can be called governed for any clinical use. On the bundled
  synthetic dataset several controls (de-identification, the IRB gate) are
  no-op safeguards; they become load-bearing only when real data arrives.
* **Frameworks.** No formal external AI-governance or quality-management
  framework (for example, a regulatory software-as-a-medical-device system)
  is adopted. The data-privacy controls map to the HIPAA Privacy Rule
  de-identification standard (45 CFR 164.514(b)(1) Expert Determination and
  (b)(2) Safe Harbor); the audit and access controls follow standard
  tamper-evident-log and gating practice. The out-of-scope uses that bound
  the whole project are enumerated in `model_card.md` Section 2.

## 2. Data governance: de-identification and provenance

* **De-identification pipeline.** `ml/data/deidentification.py` implements a
  layered pipeline. The base layer is HIPAA Safe Harbor (45 CFR
  164.514(b)(2)): removal of the eighteen identifier categories, age capping
  at 89 and above, ZIP truncation to three digits, and generalisation of
  dates to the year (`SafeHarborConfig`, `SafeHarborProcessor`). Statistical
  layers above it provide k-anonymity (every equivalence class at least size
  k), l-diversity, and t-closeness for quasi-identifier risk; an
  expert-determination path (45 CFR 164.514(b)(1)) is also represented.
* **On the bundled data.** The shipped 30-row dataset is synthetic and
  carries no identifiers, so the de-identification pass is a no-op safeguard
  today. It is load-bearing for any future MIMIC-IV-shaped CSV, where the age
  cap, date generalisation, and identifier removal do real work
  (`data_card.md` Section 4).
* **Provenance.** Every row carries `source`, `physician`, `timestamp_tz`,
  and a `case_id`. Synthetic rows are tagged with a `source` value such as
  `simulated` or `synthetic_from_yoder2010` so they can be filtered out of
  any real-data metric, and per-row provenance is recorded in the audit chain
  (`model_card.md` Sections 6 and 9).

## 3. Research governance: the IRB gate

* **The gate.** `ml/irb_gate.py` sits at the training entry point. If the
  dataset is synthetic-only, detected when every `source` value matches a
  known prefix (`simulated`, `synthetic`, `bridge`, `mimic_iv`), the gate is
  a no-op, because synthetic data does not require IRB approval. Otherwise the
  gate reads `outputs/irb/current_irb.json` and permits training only when
  the record's status is approved or conditionally approved; any other
  status, including a missing file or malformed JSON, raises `IRBGateBlocked`
  with an actionable remediation message.
* **Bypass is visible.** An `AMOEBANATOR_IRB_BYPASS` environment variable
  skips the check for continuous integration and smoke tests, and every
  bypass is written to the audit log so it is never invisible.
* **Real-data path.** The planned MIMIC-IV extension is additionally gated by
  PhysioNet credentialing and the MIMIC-IV data use agreement, outside the
  repository (`data_card.md` Sections 3 and 6).

## 4. Audit governance: the tamper-evident trail

* **Hash chain.** `ml/data/audit_trail.py` maintains a tamper-evident log.
  Each entry is linked to the previous one through a SHA-256 hash chain (the
  entry hash is computed over the entry fields together with the previous
  hash), and periodic Merkle-tree checkpoints summarise the chain. Any
  modification to a past entry breaks the chain, surfaced as an integrity
  status of valid, tampered, incomplete, or unknown.
* **Event coverage.** Logged event types span the data lifecycle (received,
  verified, released), access decisions (access denied), compliance
  (compliance check, IRB status change), integrity violations, session and
  configuration changes, and the web layer (prediction received and returned,
  rate-limit hit, preset loaded, audit export requested).
* **Wiring and access.** The log path is configurable through
  `AMOEBANATOR_AUDIT_PATH`. Controls emit into the chain through
  `ml/audit_hooks`, and the Streamlit dashboard exposes a read-only audit
  export (`app/audit_export.py`, `pages/02_audit.py`).

## 5. Model governance: versioning and change control

* **Versioning.** The model is V1.0. Its state_dict is regenerable from a
  pinned random seed via the documented training entry point, and a git tag
  marks the release commit so the V1.0 artefacts remain retrievable from
  history (`model_card.md` Section 1; `data_card.md` Section 7).
* **Change control.** Re-fitting the model requires re-running the audit
  chain and re-fitting every downstream metric so that the model card stays
  synchronised with the artefacts it describes. Adding synthetic rows
  requires explicit `source` provenance, an audit re-run to record the
  addition, and a downstream re-fit (`data_card.md` Section 7;
  `model_card.md` Section 9).

## 6. Runtime safety governance

* **Intended-use enforcement.** The Streamlit application renders a research
  prototype disclaimer above every prediction surface. The banner states that
  the system is not a medical device, that it was trained on thirty synthetic
  vignettes containing no real protected health information, that the outputs
  are calibrated probabilities limited to that training distribution rather
  than diagnoses, and that it is not for clinical decision support and not
  validated; it also carries the source link and the maintainer contact. A
  set of mandatory tokens in that banner, including the sample size and the
  not-for-clinical-use language, is asserted by the test suite
  (`app/disclaimer.py`; `tests/test_app_disclaimer.py`). The full set of
  out-of-scope uses is in `model_card.md` Section 2.
* **The safety stack.** Three gates fire on every inference call: a
  Mahalanobis out-of-distribution gate, a logit-energy gate, and a
  split-conformal abstain. Each returns an explicit ABSTAIN with a reason
  field when triggered, and the dashboard shows the raw safety-signal
  breakdown beneath each prediction (`model_card.md` Section 8). The web
  layer additionally enforces a rate limit, logged as an audit event.

## 7. Accountability

This is a single-author research project. The maintainer is reachable through
the repository, errata are tracked in the release notes, and the governance
code, covering de-identification, the audit trail, the IRB gate, and the
safety stack, is open-sourced under the license stated in `README.md`
(`model_card.md` Section 1; `data_card.md` Section 7).

## Honesty signal

These controls are real and tested, but their posture is research governance,
not deployment governance. On synthetic data the de-identification pass and
the IRB gate are mostly no-op safeguards, and the audit chain governs a
pipeline that has never processed a real patient. They exist so that the
transition to the planned real-data study is governed from the first commit,
not to assert that the system is cleared for any clinical setting. Naming that
posture plainly is the point.

## References

The data-privacy controls draw on the HIPAA Privacy Rule de-identification
standard: 45 CFR 164.514(b)(1) Expert Determination and (b)(2) Safe Harbor,
with the HHS Office for Civil Rights de-identification guidance recorded in
`docs/references.bib` and pinned in `docs/data_card.md` Section 4. The methods
citations for the runtime safety stack (temperature scaling, split conformal,
energy and Mahalanobis OOD, decision curve analysis) are listed in
`docs/model_card.md` and `docs/references.bib`.
