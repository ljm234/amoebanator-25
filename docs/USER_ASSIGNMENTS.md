# User Assignments — work that requires Jordan, not Claude Code

**Last refreshed:** 2026-04-27 (Phase 4.5 PRE-FLIGHT audit close)
**Companion docs:** `PHASE_4_5_PLAN.md` §7, `PHASE_4_5_PROMPT_FINAL.md` §7

This is the single source of truth for everything the Amoebanator pipeline needs from a human. Each entry is self-contained: why it matters, what to do, how long it realistically takes, and the verification command that proves it succeeded.

The structure follows a 4-tier timeline:
- **§1 Pre-sprint** — must be done BEFORE Phase 4.5 sprint kickoff
- **§2 During-sprint** — touchpoints between Mini-1 and Mini-2 (autonomous; no user action required)
- **§3 Post-sprint** — after Mini-2 closure
- **§4 Future Phase 6+** — deferred until MIMIC-IV cohort lands

Completed Phase 1-9 historical assignments are listed at the bottom (§5) with strikethrough markers for traceability.

---

## §1. Pre-sprint assignments (must complete BEFORE Mini-1 kickoff)

### Step 1 — Verify backup tar.gz exists

**Why:** Cheap insurance before sprint commits land. If anything in Mini-1 / Mini-2 goes catastrophically wrong, the backup is the unconditional rollback path.

**Command:**

```bash
ls -lh ~/amoebanator-pre-4.5-sprint.tar.gz 2>&1 | head -2
```

**Expected:** File exists, ~50-100 MB. If missing, create it now:

```bash
tar -czf ~/amoebanator-pre-4.5-sprint.tar.gz \
  -C "$HOME/Desktop" "Amoebanator 25" \
  --exclude="*/__pycache__/*" \
  --exclude="*/_wip/*" \
  --exclude="*/.pytest_cache/*"
ls -lh ~/amoebanator-pre-4.5-sprint.tar.gz  # verify
```

**Realistic timeline:** 30 seconds.

---

### Step 2 — Verify HF Space exists

**Why:** Sprint deploys to an existing HF Space. Creating it mid-sprint adds friction and changes the deploy URL.

**Command:**

```bash
curl -s -o /dev/null -w "%{http_code}\n" \
  https://huggingface.co/spaces/luisjordanmontenegro/amoebanator-25
```

**Expected:** `200`.

If `404`, the Space needs to be created via the HF Hub UI (https://huggingface.co/new-space) with: Owner=`luisjordanmontenegro`, Space name=`amoebanator-25`, SDK=Docker (not Streamlit native — Docker SDK is required for the locked Dockerfile + `.streamlit/config.toml` setup), Visibility=Public, Hardware=CPU Basic (free tier).

**Realistic timeline:** 30 seconds verify; 5 minutes create if missing.

---

### Step 3 — Verify HF token in macOS Keychain

**Why:** GitHub Actions deploy workflow reads the HF token from Keychain (via the wrapper script that resolves Keychain → env var). Token must be in Keychain BEFORE Step 4 uploads it to GitHub.

**Command (metadata-only check, does NOT print the token value):**

```bash
security find-generic-password -s "hf-amoebanator-25" -a "$USER" 2>&1 | head -5
```

**Expected:** Returns metadata block with `class:`, `attributes:`, `service:`. Does NOT print the password value (that requires `-w` flag).

If missing, add via interactive prompt (NEVER paste the token to shell history):

```bash
security add-generic-password -a "$USER" -s "hf-amoebanator-25" -w
# Terminal will prompt for password — paste the hf_... token there.
# It is NOT stored in shell history because no -W argument was used.
```

**Realistic timeline:** 30 seconds verify; 1 minute add if missing.

---

### Step 4 — Verify GitHub auth + HF_TOKEN secret uploaded

**Why:** GitHub Actions workflow (`.github/workflows/deploy_hf.yml` if exists, or future addition) needs `HF_TOKEN` as a repo-level secret to push to the HF Space.

**Verification commands:**

```bash
# 1. Confirm authenticated as ljm234
gh auth status 2>&1 | grep "Logged in"
# Expected: "✓ Logged in to github.com account ljm234"

# 2. Confirm HF_TOKEN secret present
gh secret list --repo ljm234/amoebanator-25 2>&1 | grep HF_TOKEN
# Expected: "HF_TOKEN  Updated <timestamp>"
```

If `HF_TOKEN` is missing, upload via stdin pattern (token NEVER appears in shell history or process listing):

```bash
# 1. Retrieve from Keychain into temp variable
HF_TOKEN_TMP=$(security find-generic-password -s "hf-amoebanator-25" -a "$USER" -w)

# 2. Upload via gh secret set with --body-file=- (reads stdin)
echo "$HF_TOKEN_TMP" | gh secret set HF_TOKEN --repo ljm234/amoebanator-25 --body-file=-

# 3. Verify upload succeeded
gh secret list --repo ljm234/amoebanator-25 | grep HF_TOKEN

# 4. Clear local temp variable (do NOT leave the token in shell env)
unset HF_TOKEN_TMP
```

**Why stdin pattern, not `--body "$HF_TOKEN_TMP"`:** Command-line arguments are visible to other processes via `ps -ef`. Stdin is not. The stdin pattern is the only safe upload path.

**Realistic timeline:** 1 minute.

---

### Step 5 — PhysioNet credentialed-access form (already submitted)

**Status:** Submitted 2026-04-25. Awaiting review confirmation.

**Background:** Required for downloading MIMIC-IV CSVs (Phase 6 dependency). Phase 4.5 sprint does NOT depend on this — the sprint uses synthetic n=30 data only. This step is listed here because Phase 6 will need the CSVs, but it does not block Phase 4.5 kickoff.

**Reviewer of record:** Abdias Valdiviezo (PhysioNet credentialing).

**No action needed unless rejected** — if rejection email arrives, re-submit with reference contact (Dr. Brett Pickett at BYU as suggested in original Phase 1-9 form).

---

### Step 6 — NEW — `gh repo rename` Amoebanator_25 → amoebanator-25

**Why:** The HF Space slug is `luisjordanmontenegro/amoebanator-25` (lowercase + dash, npm/pypi convention). The current GitHub repo is `ljm234/Amoebanator_25` (capital + underscore). The locked Phase 4.5 disclaimer URL is `github.com/ljm234/amoebanator-25` — that URL only resolves after the rename. Match the repo slug to the HF slug so the segment a PI pastes is identical across both URLs (citation hygiene).

**Procedure:**

```bash
# 1. Rename the repo on GitHub (auto-creates a permanent redirect from old name)
gh repo rename ljm234/Amoebanator_25 ljm234/amoebanator-25

# 2. Update the local remote URL
cd "/Users/jordanmontenegro/Desktop/Amoebanator 25/Amoebanator 25"
git remote set-url origin https://github.com/ljm234/amoebanator-25.git

# 3. Verify both
git remote -v
# Expected: "origin  https://github.com/ljm234/amoebanator-25.git (fetch)"
#           "origin  https://github.com/ljm234/amoebanator-25.git (push)"

gh repo view --json url --jq .url
# Expected: "https://github.com/ljm234/amoebanator-25"
```

**Why path (b) rename and NOT path (c) full rebrand to luisjordanmontenegro GitHub account:** Per Q19.D vote, full rebrand costs re-auth + secret regen + ownership transfer for one-line disclosure benefit. The username mismatch (`ljm234` GitHub vs `luisjordanmontenegro` HF) is handled by a one-line addition to the About page (`pages/03_about.py`): *"Repo: github.com/ljm234/amoebanator-25 — HuggingFace Space: huggingface.co/spaces/luisjordanmontenegro/amoebanator-25 (same author, separate handles)."*

**Realistic timeline:** 2 minutes.

**Verification (after rename):** Open `https://github.com/ljm234/amoebanator-25` in browser → returns 200. Open the old `https://github.com/ljm234/Amoebanator_25` → auto-redirects to the new URL (GitHub handles the redirect permanently).

---

## §2. During-sprint touchpoints

**No user action required.** The sprint is autonomous between Mini-1 kickoff and Mini-2 close.

The Mini-1 → Mini-2 transition is a Claude Code pause for explicit user vote (per `PHASE_4_5_PROMPT_FINAL.md` §5.2 standing instruction): after all 7 Mini-1 closure gates green, Claude waits for "go Mini-2" from Jordan before continuing. This is a verification + approval touchpoint, not a coding action.

If Mini-1 reports any closure gate fail, Claude stops and reports — Jordan decides whether to fix-and-retry, redirect, or pause.

---

## §3. Post-sprint assignments (after Mini-2 closure)

### Step 7 — Update `jordanmontenegrocalla.com/playground` link-out (Vercel Next.js repo)

**Why:** Q9 locked link-out only — the Vercel `/playground` page replaces its placeholder content with a button to the HF Space. This edit happens in the **Vercel website repo** (separate from Amoebanator), executed by Jordan post-sprint.

**Procedure (executed in the Next.js repo, NOT the Amoebanator repo):**

```bash
# Step 0: Verify cwd is the Next.js repo (NOT Amoebanator)
pwd
# Expected: NOT containing "Amoebanator"
git remote -v
# Expected: shows the jordanmontenegrocalla.com Next.js repo URL

# Step 1: Backup the current placeholder
cp app/playground/page.tsx app/playground/page.tsx.bak

# Step 2: Add *.tsx.bak to .gitignore (one-time, idempotent)
grep -q "*.tsx.bak" .gitignore || echo "*.tsx.bak" >> .gitignore
git add .gitignore
git diff --cached --quiet || git commit -m "chore: ignore .tsx.bak rollback files"

# Step 3: Edit app/playground/page.tsx with the link-out button
# Locked button content (per Q9.1 caption):
#   Button text: "Launch interactive demo →"
#   Button URL:  https://huggingface.co/spaces/luisjordanmontenegro/amoebanator-25
#   Target:      _blank (open in new tab)
#   Caption (under button, smaller font):
#     "Hosted on Hugging Face Spaces (free CPU tier; cold-start ~30s
#      on first visit after idle period). Research prototype — not
#      for clinical use."

# Step 4: Commit + push
git add app/playground/page.tsx
git commit -m "feat(playground): link-out to HF Space amoebanator-25 demo"
git push origin main

# Step 5: Verify Vercel auto-deploy (~2 min build)
# Open https://jordanmontenegrocalla.com/playground in incognito browser
# Expected: button renders, clicking opens HF Space in new tab
```

**Why backup-with-cwd-guard:** Jordan has multiple repos open in different terminals. A one-line `pwd` guard prevents accidentally backing up the wrong placeholder. The `.bak` extension is parsed-cleanly-as-non-tsx by Next.js dev hot-reload (unlike `.bak.tsx` which throws warnings).

**Realistic timeline:** 10 minutes (button edit + Vercel deploy + smoke test).

**Verification:** `https://jordanmontenegrocalla.com/playground` shows button + caption; clicking opens HF Space in new tab; old placeholder content gone.

---

## §4. Future Phase 6+ assignments (deferred — when MIMIC-IV cohort lands)

### Step 8 — Download MIMIC-IV CSVs after PhysioNet approval

**Trigger:** PhysioNet approval email arrives (~1-3 weeks after Step 5 form submission).

**Procedure:**

```bash
# 1. Sign the MIMIC-IV Data Use Agreement
# Visit https://physionet.org/content/mimiciv/3.1/ → "Files" tab → click DUA agree.

# 2. Download the four CSV files the loader needs (from hosp/ directory)
mkdir -p "/Users/jordanmontenegro/Desktop/Amoebanator 25/Amoebanator 25/data/raw/mimiciv"
cd "/Users/jordanmontenegro/Desktop/Amoebanator 25/Amoebanator 25/data/raw/mimiciv"

# Use wget with PhysioNet basic auth (after credentialing):
wget --user="<physionet-username>" --ask-password \
  https://physionet.org/files/mimiciv/3.1/hosp/labevents.csv.gz \
  https://physionet.org/files/mimiciv/3.1/hosp/d_labitems.csv.gz \
  https://physionet.org/files/mimiciv/3.1/hosp/diagnoses_icd.csv.gz \
  https://physionet.org/files/mimiciv/3.1/hosp/microbiologyevents.csv.gz

# 3. Decompress (or let the loader's compression='gzip' path handle it)
gunzip *.gz

# 4. Smoke-test the loader
cd "/Users/jordanmontenegro/Desktop/Amoebanator 25/Amoebanator 25"
PYTHONPATH=. python -c "
from pathlib import Path
from ml.mimic_iv_loader import load_cohort_from_csvs, task_balance
base = Path('data/raw/mimiciv')
cohort = load_cohort_from_csvs(
    base/'labevents.csv', base/'diagnoses_icd.csv', base/'microbiologyevents.csv'
)
print(f'cohort rows={len(cohort)}, balance={task_balance(cohort)}')
"
# Expected: several thousand rows, roughly balanced bacterial/viral, small amebic count
```

**Realistic timeline:** Download ~30 min depending on connection (~3 GB total). Smoke test ~5 min.

---

### Step 9 — Create real IRB record + flip `AMOEBANATOR_IRB_BYPASS=0`

**Trigger:** Phase 6 Mini-X is ready to integrate real PHI from MIMIC-IV.

**Background:** Independent researcher status applies for Phase 4.5 (synthetic data only, no PHI). Phase 6 introduces real PHI from MIMIC-IV; an IRB record becomes load-bearing for the audit gate.

**Procedure:**

```bash
# 1. Create the IRB record (independent researcher justification + DUA reference)
mkdir -p outputs/governance
cat > outputs/governance/irb_record.json <<EOF
{
  "irb_status": "approved",
  "approval_date": "<YYYY-MM-DD>",
  "expiration_date": "<YYYY-MM-DD>",
  "approving_body": "Independent researcher — MIMIC-IV DUA",
  "data_use_agreement": "MIMIC-IV PhysioNet DUA (signed <YYYY-MM-DD>)",
  "justification": "Independent research on de-identified MIMIC-IV cohort (Beth Israel Deaconess). PhysioNet credentialing approved per Step 5. No new PHI generated; analysis on existing de-identified records under 45 CFR §46.104(d)(4)."
}
EOF

# 2. CHECKLIST BEFORE FLIPPING (all 5 must be ✓):
#   [ ] outputs/governance/irb_record.json exists
#   [ ] irb_status field == "approved" or "conditionally_approved"
#   [ ] expiration_date is in the future
#   [ ] All MIMIC-IV cohort code paths emit AuditEventType.PHI_ACCESS events
#   [ ] tests/test_irb_gate.py::test_real_phi_path_requires_irb_record passes

# 3. Edit Dockerfile: change ENV AMOEBANATOR_IRB_BYPASS=1 to =0
# (or remove the env var entirely — ml/irb_gate.py treats missing/0 as "enforce")
# Reference the verbatim 5-bullet safety comment block in PHASE_4_5_PROMPT_FINAL.md §6.7

# 4. Run full test suite, especially the new IRB enforcement tests
pytest tests/test_irb_gate.py -v

# 5. Re-deploy to HF Space
git add Dockerfile outputs/governance/irb_record.json
git commit -m "fix(safety): IRB_BYPASS=0 with real PHI cohort (Phase 6 — MIMIC-IV)"
git push origin main
git push hf main  # trigger HF Space rebuild
```

**Verification:** App boots successfully with `AMOEBANATOR_IRB_BYPASS=0`. Without the IRB record, `IRBGateBlocked` raises and the app refuses to start (correct behavior — fail-loud over fail-silent).

**Realistic timeline:** 30 minutes (record creation + checklist verification + Dockerfile edit + test run + deploy).

---

## §5. Historical / Completed assignments

These are Phase 1-9 era items, retained for traceability. All completed before the Phase 4.5 PRE-FLIGHT audit (2026-04-26).

### ~~Phase 1-9 §1. PhysioNet credentialed-access submission~~ ✓ DONE 2026-04-25

CITI training completed. PhysioNet form submitted with reference contact + 1-paragraph research description. Awaiting review confirmation. (See current §1 Step 5 for status; downstream MIMIC-IV download deferred to §4 Step 8.)

### ~~Phase 1-9 §2. Weber State IRB exemption letter~~ — REMOVED

**Original status:** REQUIRED for medRxiv preprint submission.

**Status as of 2026-04-27:** REMOVED from this assignments doc. Per project memory: independent researcher status applies; no Weber State IRB exemption required for the synthetic-data-only Phase 4.5 demo. When Phase 6 integrates real MIMIC-IV PHI, the IRB record path moves to §4 Step 9 (independent researcher justification + DUA reference). Weber State institutional path is not the relevant one for this project's structure.

### ~~Phase 1-9 §3. LightGBM install~~ ✓ DONE 2026-04-25

`lightgbm==4.6.0` installed. `GBMIsotonic.backend_ = "lightgbm"` verified end-to-end. Ablation table at `outputs/metrics/ablation_table.json` uses LightGBM for the GBM cell.

### ~~Phase 1-9 §4. (Optional) Capewell 2015 PDF extraction~~ — STILL OPTIONAL

Optional enrichment for `ml/case_series.synthesize_yoder_cohort` to sample from empirical PAM CSF distribution rather than broader bacterial-meningitis-pattern range. Defer to Phase 6 with MIMIC-IV (real CSF distributions will supersede the published-case-series synthesis approach).

### ~~Phase 1-9 §5. Real OOD evaluation cohort~~ ✓ UNBLOCKED 2026-04-25 by §1

No standalone user action required. Loader handles the fungal/parasitic OOD held-out extension by adding `B45.x` codes to `MimicCohortConfig.amebic_codes`. Will run automatically as part of Phase 6 real-data evaluation against the MIMIC-IV CSVs from §4 Step 8.

---

## Status snapshot (as of 2026-04-27)

| Tier | # | Assignment | Status |
|---|---|---|---|
| §1 Pre-sprint | 1 | Verify backup tar.gz | **REQUIRED before sprint** |
| §1 Pre-sprint | 2 | Verify HF Space exists | **REQUIRED before sprint** |
| §1 Pre-sprint | 3 | Verify HF token in Keychain | **REQUIRED before sprint** |
| §1 Pre-sprint | 4 | Verify GitHub HF_TOKEN secret | **REQUIRED before sprint** |
| §1 Pre-sprint | 5 | PhysioNet form (submitted, awaiting) | ✅ submitted 2026-04-25 |
| §1 Pre-sprint | 6 | gh repo rename Amoebanator_25 → amoebanator-25 | **REQUIRED before sprint** |
| §2 During-sprint | — | (none) | autonomous |
| §3 Post-sprint | 7 | Vercel /playground link-out | scheduled post-sprint |
| §4 Future | 8 | MIMIC-IV CSV download | deferred until PhysioNet approval |
| §4 Future | 9 | IRB_BYPASS flip + irb_record.json | deferred until Phase 6 Mini-X |
| §5 Historical | — | Phase 1-9 completed items | reference only |

**Sprint kickoff blocker:** Steps 1, 2, 3, 4, 6 in §1 must all be ✓ before pasting `PHASE_4_5_PROMPT_FINAL.md` into a fresh Claude Code session. Step 5 is informational (does not block Phase 4.5; blocks Phase 6).

Update this file as each step completes. The Phase 6 verification scripts (Step 9 onward) will read it implicitly to determine which gates are open.
