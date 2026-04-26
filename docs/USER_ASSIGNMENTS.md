# User assignments — work that requires Jordan, not Claude Code

This is the single source of truth for everything the Amoebanator pipeline
needs from a human. Each entry is self-contained: why it matters, what to
do, how long it realistically takes, and the verification command that
proves it succeeded.

Phases that depend on each assignment are listed so you can plan the order.

---

## 1. PhysioNet credentialed access for MIMIC-IV  ✅ **DONE 2026-04-25**

**Status:** Approved. Phases 2.2, 3 (real-data), 5.5, and 6 (real DCA) are
unblocked from this side. Remaining work is the data **download** + drop
into `data/raw/mimiciv/` (see "Next steps after approval" below).

**Why:** MIMIC-IV is the only practical source of large-n bacterial /
viral / fungal meningitis CSF data with linked diagnoses. Without access
the Phase 2 proxy task and the real-data Phase 3 / 5.5 evaluations cannot
run; the pipeline still works on simulated data, but no headline metric in
the preprint can quote real numbers.

**Steps (in order):**

1. **Create a PhysioNet account** with your **institutional email** (Weber
   State address is required — a personal Gmail will not be approved).
   https://physionet.org/register/
2. **Create a CITI Program account** at https://about.citiprogram.org/
   Affiliate with your home institution. Complete the
   **"Data or Specimens Only Research"** course (and the
   **"Conflicts of Interest"** module if prompted). Self-paced, ~4–8 hours.
3. **Download the CITI Completion Report** (not the certificate) from
   "Records → View-Print-Share." Save the PDF.
4. **PhysioNet → profile → Credentialing:** submit the credentialing form
   with reference contact (suggested: Dr. Brett Pickett at BYU or your
   Weber State research advisor) and a 1-paragraph research description
   ("Calibrated, abstention-aware triage signal for low-prevalence
   meningoencephalitis using MIMIC-IV CSF labs as the proxy training
   distribution.").
5. **PhysioNet → profile → Training:** upload the CITI Completion Report PDF.
6. **Sign the MIMIC-IV Data Use Agreement** at the project page,
   currently https://physionet.org/content/mimiciv/3.1/ → "Files" tab.

**Realistic timeline:** CITI course ≈ 4–8 hours; PhysioNet review
typically 1–3 weeks (community-reported, not an official SLA). Plan
**2–4 weeks end-to-end**.

**Verification:** Once approved, downloading any file from
`https://physionet.org/content/mimiciv/3.1/hosp/` should succeed without
prompting for login. Run:
```bash
PYTHONPATH=. python -c "from ml.mimic_iv_loader import load_cohort_from_csvs; print('schema OK')"
```
to confirm the loader is callable on whatever CSVs you place under
`data/raw/mimiciv/`.

### Next steps after approval (small, mechanical)

1. **Download the four CSV files** the loader needs. From the MIMIC-IV
   project page (`https://physionet.org/content/mimiciv/3.1/`) under
   `hosp/`, grab:
   - `labevents.csv.gz`     (~ 2.5 GB compressed)
   - `d_labitems.csv.gz`    (~ 30 KB)
   - `diagnoses_icd.csv.gz` (~ 30 MB)
   - `microbiologyevents.csv.gz` (~ 100 MB)
2. **Place them** under `data/raw/mimiciv/` (gunzip first, or use the
   loader's `pd.read_csv(..., compression='gzip')` path).
3. **Smoke-test the loader** on the real CSVs:
   ```bash
   PYTHONPATH=. python -c "
   from pathlib import Path
   from ml.mimic_iv_loader import load_cohort_from_csvs, task_balance
   base = Path('data/raw/mimiciv')
   cohort = load_cohort_from_csvs(
       base/'labevents.csv', base/'diagnoses_icd.csv', base/'microbiologyevents.csv'
   )
   print(f'cohort rows={len(cohort)}, balance={task_balance(cohort)}')
   "
   ```
   Expected: a cohort with several thousand rows and a roughly balanced
   bacterial / viral count plus a small amebic count.
4. **Run the real-data pipeline:** the next sprint will replace the
   bundled CSV in `outputs/diagnosis_log_pro.csv` with the MIMIC-IV cohort
   and re-emit every artefact via `scripts/regenerate_all_artifacts.py`.

---

## 2. IRB exemption letter from Weber State  *(BLOCKS preprint submission, NOT Phase 2-5 code)*

**Why:** medRxiv requires an explicit IRB statement for any human-subjects
research, even for retrospective use of fully de-identified public data.
Most institutions issue an **exempt determination** for MIMIC-IV use under
45 CFR §46.104(d)(4) (research on existing, de-identified data).

**Steps:**

1. Submit an IRB exemption request at Weber State's IRB portal. The
   description should reference: (a) MIMIC-IV (de-identified, Beth Israel
   Deaconess), (b) the Yoder 2010 / Cope 2016 published case-series
   (already in the public domain), and (c) the simulated bundle in
   `outputs/diagnosis_log_pro.csv` (no real patients).
2. Cite the exemption category 4 ("research involving the collection or
   study of existing data, documents, records ... if the information is
   recorded ... so that subjects cannot be identified").

**Realistic timeline:** typically 2–4 weeks for an exempt determination.

**Verification:** PDF of the exempt-determination letter saved to
`docs/irb/weber_state_exemption.pdf` (untracked; do not commit).

---

## 3. Install LightGBM for Phase 3.3 baseline  ✅ **DONE 2026-04-25**

**Status:** `lightgbm==4.6.0` installed; `GBMIsotonic.backend_ = "lightgbm"`
verified end-to-end. The ablation table at `outputs/metrics/ablation_table.json`
now uses LightGBM for the GBM cell instead of the sklearn fallback.

**Verified with:**
```bash
python -c "from ml.baselines.gbm import lightgbm_available; print(lightgbm_available())"
# True
```

---

## 4. *(Optional)* Capewell 2015 case-series PDF for richer PAM CSF priors

**Why:** Cope JR, Ali IK 2016 (the PAM "what we've learned" review)
describes CSF abnormalities qualitatively only — no numeric tables.
Capewell LG et al., *J Pediatric Infect Dis Soc* 2015;4(4):e68–e75
(PMID 26582886) tabulates per-case CSF values for U.S. pediatric PAM cases.
With those numbers, `ml/case_series.synthesize_yoder_cohort` can sample
from an empirical PAM CSF distribution rather than from the broader
bacterial-meningitis-pattern range it currently uses.

**Steps:** Download the PDF (PubMed open access:
https://pubmed.ncbi.nlm.nih.gov/26582886/), extract the Table 1 / Table 2
CSF values, and add them to `ml/case_series.py` under a new
`Capewell2015CSF` dataclass. Code stub welcome — Claude can do the
encoding once the numbers are extracted.

**Verification:**
```bash
python -c "from ml.case_series import published_constants; print('capewell2015' in published_constants())"
```

---

## 5. Real OOD evaluation cohort: bacterial vs viral vs fungal/parasitic  ✅ **UNBLOCKED 2026-04-25**

**Status:** No standalone user action required. With PhysioNet access
approved (Step 1) the loader handles the fungal/parasitic OOD held-out
extension by adding `B45.x` codes to `MimicCohortConfig.amebic_codes`.
This will run automatically as part of the next sprint's Phase 5.5
real-data evaluation, against the same MIMIC-IV CSVs you drop under
`data/raw/mimiciv/`.

---

## Status snapshot

| # | Assignment | Blocks | Status |
|---|------------|--------|--------|
| 1 | PhysioNet credentialed access | 2.2 real, 3 real, 5.5, 6 (DCA) | ✅ **DONE 2026-04-25** |
| 2 | Weber State IRB exemption | preprint submission | **REQUIRED** |
| 3 | LightGBM install | Phase 3.3 (LightGBM-specific) | ✅ **DONE 2026-04-25** |
| 4 | Capewell 2015 PDF extract | richer Phase 2.3 priors | optional |
| 5 | Real OOD cohort | Phase 5.5 real eval | ✅ unblocked by #1 |

**Remaining required:** only #2 (Weber State IRB exemption letter).
Without it the medRxiv preprint cannot be submitted, but every code path
of Phase 6 / 5.5 / real-data 3 can run today.

**Mechanical follow-on to #1 (small):** download the four MIMIC-IV CSVs
under `data/raw/mimiciv/` (see Step 1's "Next steps after approval"
section) and run the loader smoke command.

Update this file as each step completes; the Phase 2 → 5 verification
scripts will read it implicitly (they raise SystemExit with a pointer
back to the relevant section number when the data they need is missing).
