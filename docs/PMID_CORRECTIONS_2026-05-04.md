# PMID Corrections Applied 2026-05-04

## Source
4-pass verification audit verification (compass_artifact_wf-82607ea9-54e4-4560-8928-59f91005997a)

Applied to `scripts/generate_pam_vignettes.py` `PMID_REGISTRY` before Day 2 vignette generation. All 24/24 existing tests still pass (no schema modifications, no Day 1 vignette regeneration changes).

---

## Critical Corrections

### PMID 8923775 - Author Attribution Fixed
- **Before:** Lares-Villa (incorrect attribution noted in prior research artifacts; this PMID was not yet in the registry)
- **After:** DeNapoli TS, Rutman JY, Robinson JR, Rhodes MM
- **Source:** Tex Med 1996;92(10):59-63
- **Note:** Lares-Villa 1993 Mexicali is a separate paper, PMID 8458963 (already in registry, correctly attributed)
- **Status:** Added fresh to registry as DeNapoli for Day 2 v44 (Rio Grande pediatric river case)
- **DOI:** none (1996 pre-DOI era)

### PMID 31441589 - REMOVED FROM CORPUS
- **Issue:** Megalencephaly genetics paper (Dobyns/Mirzaa 2019), NO Naegleria content
- **Replacement plan:** Vareechon OFID 2019 ofz349 (PMID needs PubMed UI confirmation, see pending list)
- **Same patient covered by:** PMID 31513557 (Vugia/Vareechon MMWR, already in registry)
- **Status:** PMID 31441589 was never added to `PMID_REGISTRY`; documenting here so it stays out

### PMID 26582886 - Capewell 2015 - PMC ID Removed
- **Before:** PMC4622028 (unconfirmable in any of 6 independent reference lists)
- **After:** No PMC ID (cite by PMID + DOI only)
- **Reason:** No corroboration found across 6 independent reference lists
- **Status:** Added to registry with `pmc_id: null` and explicit caveat
- **Anchor type:** `review_us_surveillance` (Tier 4 IMPUTED_FROM_LITERATURE_REVIEW only)

### PMID 33350926 - Author Attribution Fixed
- **Before:** Cope 2020 epidemiology (incorrect attribution)
- **After:** Gharpure R, Gleason M, Salah Z, Blackstock AJ, Hess-Homeier D, Yoder JS, Ali IKM, Collier SA, Cope JR (2021 EID Geographic Range)
- **PMC:** PMC7774533
- **Status:** Added to registry as Gharpure 2021 EID Geographic Range

### PMID 25595746 - Cope 2015 Louisiana - PMC ID Confirmed
- **Before:** Prior PMC4622028 misattribution (which was the unconfirmable Capewell 2015 candidate)
- **After:** PMC4627687 (confirmed exact)
- **Status:** Added to registry with confirmed PMC4627687

### PMID 23621053 - Author Attribution Fixed
- **Before:** Sifuentes (incorrect attribution noted in prior research artifacts)
- **After:** Budge PJ et al. (Florida case + epidemiology review)
- **Note:** Sifuentes 2014 (PMID 24967566) is environmental Arizona surveillance, a separate paper
- **Status:** PMID 23621053 not yet in registry; documented here so it gets the correct attribution if/when added in Day 2

### PMID 37460088 - Maloney 2023 Nebraska - Erratum Fields Structured
- Added structured fields to existing entry:
 - `pmc_id`: `PMC10397427`
 - `erratum`: `AJTMH 2025 Apr 2;112(4):942`
 - `erratum_doi`: `10.4269/ajtmh.23-0211cor`
 - `erratum_pmc`: `PMC11965766`
- Existing free-text caveat retained (used by `_build_provenance` for downstream rationale)
- `last_verified_date` updated 2026-05-03 → 2026-05-04

---

## Demographic Claim Softening (preemptive for Day 2)

Applied to PMIDs not yet in `PMID_REGISTRY`. When these PMIDs are added during Day 2 generation, the entries must use the softened language below until full-text verification is completed:

- **Stowe 2017 PMID 28389055:** use *"two fatal pediatric cases"* (not "ages 4 and 14")
- **Wei 2024 PMID 39174030:** use *"fatal after hospital admission"* (not "died 3 days after admission")
- **Lin 2024 PMID 39606118:** use *"rapidly fatal despite ECMO"* (not "died <72 hours")
- **Capewell 2015 PMID 26582886:** caveat already softened to *"approximately 140-145 cases over 76 years (1937-2013)"*

---

## New PMIDs Added (Tier 4 supporting reviews)

These three reviews are reference anchors for Tier 4 IMPUTED_FROM_LITERATURE_REVIEW corpus entries; they do not anchor case-level vignettes directly but provide global/historical context for downstream review-anchored cases.

- **PMID 40697059** Siddiqui 2025 - most recent therapeutic review (Expert Rev Anti Infect Ther 23(9):753-761; DOI 10.1080/14787210.2025.2536827; no PMC mirror, T&F paywall)
- **PMID 19845995** Yoder 2010 - foundational US surveillance, 111 cases 1962-2008 (Epidemiol Infect 138(7):968-975; DOI 10.1017/S0950268809991014)
- **PMID 32369575** Gharpure 2021 CID - global review, 381 cases 1937-2018 (Clin Infect Dis 73(1):e19-e27; DOI 10.1093/cid/ciaa520; PMC8739754); companion to Capewell 2015 (US-only)

---

## Pending User-Side PubMed UI Verifications

The following items are flagged for confirmation against the PubMed UI before Day 2 generation begins:

1. **Vareechon OFID 2019 ofz349** - find correct PMID (replacement for PMID 31441589 misattribution)
2. **Budge 2013 PMID 23621053** - verify journal name and volume/issue/pages
3. **Stowe 2017 PMID 28389055** - confirm specific ages (4 and 14) via full-text
4. **Wei 2024 PMID 39174030** - confirm exact death timing via full-text
5. **Lin 2024 PMID 39606118** - confirm <72h timing and ECMO detail via full-text
6. **Capewell 2015 PMID 26582886** - confirm exact case count via full-text (currently softened to "approximately 140-145")

---

## Registry State After Corrections

| Group | Count | PMIDs |
|-------|-------|-------|
| Day 1 case anchors (existing) | 15 | 40146665, 37470480, 22238170, 34307045, 37460088, 22919000, 40440212, 31513557, 27123690, 21291600, 29016297, 25625800, 8458963, 38526236, 40009134 |
| Day 2 case anchors (new) | 4 | 8923775 (DeNapoli), 26582886 (Capewell), 33350926 (Gharpure EID), 25595746 (Cope Louisiana) |
| Tier 4 review anchors (new) | 3 | 40697059 (Siddiqui), 19845995 (Yoder 2010), 32369575 (Gharpure CID) |
| **Total** | **22** | |

Maloney 2023 (PMID 37460088) updated in place with structured erratum fields; remains the same entry, not double-counted.

---

## Author List Audit (2026-05-04)

Audited all 22 `PMID_REGISTRY` entries for truncated `authors_full` lists. Methodology: any entry whose `authors_short` contains "et al." MUST have at least 2 named authors in `authors_full`; single-author papers should have exactly 1.

### Findings

**Confirmed truncation (fixed in this commit):**
- **PMID 25595746 Cope 2015:** had 1 author (`["Cope JR"]`), corrected to 22 authors verified via 4-pass verification (Cope JR, Ratard RC, Hill VR, Sokol T, Causey JJ, Yoder JS, Mirani G, Mull B, Mukerjee KA, Narayanan J, Doucet M, Qvarnstrom Y, Poole CN, Akingbola OA, Ritter JM, Xiong Z, da Silva AJ, Roellig D, Van Dyke RB, Stern H, Xiao L, Beach MJ).

**Empty `authors_full` (not truncated mid-list - never populated; flagged for user research-verification before Day 2):**

These 14 Day 1 originals were created with `authors_full: ""` because the original Day 1 sweep populated only `authors_short`. They are **not** mid-list truncations; the field was simply not filled. No author names will be guessed from memory; these require PubMed UI verification before Day 2 generation.

| PMID | Year | Journal | authors_short | Action |
|---|---|---|---|---|
| 8458963 | 1993 | JCM | Lares-Villa F et al. | Pending UI verification |
| 21291600 | 2011 | EID | Shakoor S et al. | Pending UI verification |
| 22238170 | 2012 | CID | Kemble SK et al. | Pending UI verification |
| 22919000 | 2012 | CID | Yoder JS et al. | Pending UI verification |
| 25625800 | 2015 | EID | Abrahams-Sandi E et al. | Pending UI verification |
| 27123690 | 2016 | MMWR | Johnson RO, Cope JR et al. | Pending UI verification |
| 29016297 | 2017 | AJTMH | Ghanchi NK et al. | Pending UI verification |
| 31513557 | 2019 | MMWR | Vugia DJ et al. | Pending UI verification |
| 34307045 | 2021 | IDCases | Anjum SK et al. | Pending UI verification |
| 37460088 | 2023 | AJTMH | Maloney P et al. | Pending UI verification |
| 37470480 | 2023 | JCM | Eger L, Pence MA | 2 authors implied by short, needs UI confirmation |
| 38526236 | 2024 | EID | Burki et al. | Pending UI verification |
| 40146665 | 2025 | MMWR | Dulski TM et al. | Pending UI verification |
| 40440212 | 2025 | MMWR | Smith et al. | Pending UI verification |

**Intact (verified populated):**

| PMID | Year | Author count | Source |
|---|---|---|---|
| 8923775 | 1996 | 4 | Day 2 prep (this sweep) |
| 19845995 | 2010 | 5 | Day 2 prep (this sweep) |
| 26582886 | 2015 | 9 | Day 2 prep (this sweep) |
| 32369575 | 2021 | 6 | Day 2 prep (this sweep) |
| 33350926 | 2021 | 9 | Day 2 prep (this sweep) |
| 25595746 | 2015 | 22 | Day 2 prep (CORRECTED in this amend) |
| 40009134 | 2025 | 6 | Day 1 (string-format authors_short with full list) |
| 40697059 | 2025 | 3 | Day 2 prep (this sweep) |

**Day 2 generation precondition:** the 14 empty `authors_full` entries should be backfilled by user-side PubMed UI research before any Day 2 vignette is generated, so that downstream provenance metadata (citation completeness for Tier 3 anchoring) is consistent across the corpus. This does not affect the current Day 1 vignettes (the generator never reads `authors_full`; only `authors_short` is rendered into adjudication anchoring text).

## Verification

- AST parse: clean
- `tests/vignettes/test_pam_vignettes.py`: 31 passed (10 functions, parametrized over 22 PMIDs)
- `tests/schemas/`: 24 passed, 1 skipped (no regression)
- All 20 Day 1 vignettes still validate against `VignetteSchema`
- 0 em-dashes in script and corrections doc
- 0 AI-tells in script and corrections doc

The vignette test count grew from 24 to 31 because `test_pmid_metadata_completeness` is parametrized over all `PMID_REGISTRY` keys; adding 7 new entries automatically expanded coverage. `last_verified_date` check was relaxed from strict equality to set membership `{"2026-05-03", "2026-05-04"}`.

---

## 5-Pass Independent Verification (2026-05-04, second sweep)

Source: compass_artifact_wf-edd469f0-53d2-4871-b7b1-1c59cf60c3c5

All 14 PMIDs author lists verified to 99%+ confidence via independent sources beyond original 4-pass. The 14 empty `authors_full` entries flagged in the prior audit have been backfilled with verified lists. Registry now has 0 empty `authors_full` entries; all 22 PMIDs are populated.

### Resolutions

**Burki vs Burqi (PMID 38526236):** RESOLVED 8-2 in favor of "Burki AMK" canonical, "Burqi AMK" alias.
Evidence: Burki appears in EID HTML byline, EID affiliation footer, EID bio note, AKU institutional repo, author's other PubMed publication (Pak Armed Forces Med J 2023), ResearchGate, Pakmedinet, PMC body text (8 sources). Burqi appears only in PubMed XML index and EID "Suggested citation" field (2 sources, both downstream of single transcription event). Stored in registry under `aliases.first_author` with `alias_rationale` field.

**Diacritics:**
- KEEP_DIACRITIC: Abrahams-Sandí E (UTF-8 verified in PubMed XML, not just HTML)
- STRIP_DIACRITIC: Fernandez-Quintanilla G (original 1993 JCM publication unaccented)

### New finding (5-pass)
- PMID 40440212 has 14 authors NOT 13. Kunz J added as author #14 (corresponding author).

### Metadata corrections confirmed (5-pass)
- PMID 34307045 DOI: `10.1016/j.idcr.2021.e01208` (article id `e01208`, not `e01218`); `article_id` field added.
- PMID 37460088 pages: `322-326` (not `322-325`).
- PMID 22919000 PMC: `PMC11307261` NIHMSID `NIHMS2012368` (NIH author-manuscript retroactive deposit). Volume/issue/pages added: `55(9):e79-e85`. DOI added: `10.1093/cid/cis626`.
- PMID 40440212 cite: `MMWR 74(19):334-335` (volume, issue, pages added).

### PMC IDs added across the registry (5-pass sweep)

| PMID | New `pmc_id` |
|---|---|
| 21291600 Shakoor 2011 | PMC3204751 |
| 22919000 Yoder 2012 | PMC11307261 (+ NIHMS2012368) |
| 25625800 Abrahams-Sandí 2015 | PMC4313663 |
| 29016297 Ghanchi 2017 | PMC5817751 |
| 31513557 Vugia 2019 | PMC6753969 |
| 34307045 Anjum 2021 | PMC8258632 |
| 37470480 Eger Pence 2023 | PMC10358179 |
| 38526236 Burki 2024 | PMC10977850 |
| 40146665 Dulski 2025 | PMC11949314 |
| 40440212 Smith 2025 | PMC12121732 |

### Initial-form differences clarified
- PMID 40146665 Dulski uses `Ali IK` (this paper bylines "Ibne K. Ali")
- PMID 34307045 Anjum uses `Ali IKM` (this paper bylines "Ibne Karim M Ali")
- Both are correct for their respective papers; do NOT normalize across corpus.

### Post-fix author count summary

All 22 `PMID_REGISTRY` entries now have populated `authors_full` lists:

| PMID | # authors | First author |
|---|---|---|
| 8458963 | 8 | Lares-Villa F |
| 8923775 | 4 | DeNapoli TS |
| 19845995 | 5 | Yoder JS |
| 21291600 | 9 | Shakoor S |
| 22238170 | 13 | Kemble SK |
| 22919000 | 21 | Yoder JS |
| 25595746 | 22 | Cope JR |
| 25625800 | 5 | Abrahams-Sandí E |
| 26582886 | 9 | Capewell LG |
| 27123690 | 9 | Johnson RO |
| 29016297 | 7 | Ghanchi NK |
| 31513557 | 8 | Vugia DJ |
| 32369575 | 6 | Gharpure R |
| 33350926 | 9 | Gharpure R |
| 34307045 | 11 | Anjum SK |
| 37460088 | 12 | Maloney P |
| 37470480 | 2 | Eger L |
| 38526236 | 7 | Burki AMK |
| 40009134 | 6 | Rauf A |
| 40146665 | 17 | Dulski TM |
| 40440212 | 14 | Smith OA |
| 40697059 | 3 | Siddiqui R |

Zero empty entries.

---

## Tag Re-annotation + authors_short Consistency Fix (2026-05-04)

Within minutes of creating tag v2.1.1-pmid-corrections-5pass, detected two related diacritic preservation issues:

1. The tag's human-readable annotation message was created via shell heredoc, which stripped the í diacritic from "Abrahams-Sandí" rendering it as "Abrahams-Sandi" in the annotation text only. Re-annotated using `git tag -F` with a UTF-8 file-sourced message to preserve the diacritic. The commit hash 3fb40b3 was unchanged; only the tag's annotation text was corrected.

2. The PMID_REGISTRY entry for PMID 25625800 had `authors_short` rendered as 'Abrahams-Sandi E et al.' (without diacritic) while `authors_full[0]` correctly preserved 'Abrahams-Sandí E' with diacritic. Since `authors_short` is rendered into adjudication anchoring text by `_build_adjudication`, this inconsistency would have surfaced in physician-facing review output. Updated `authors_short` to 'Abrahams-Sandí E et al.' for consistency with `authors_full`.

Both fixes preserve the U+00ED diacritic byte-pattern (UTF-8 c3 ad). The registry source data was already correct in `authors_full`; only the human-readable surfaces (tag annotation, authors_short rendering) needed alignment. Standard git hygiene applied within the tag's first hour of life.

### Verification
- Tag annotation hex inspection confirms c3 ad UTF-8 sequence present (2 instances in body text)
- `PMID_REGISTRY['25625800']['authors_short']` and `['authors_full'][0]` both contain U+00ED
- Both remotes (origin, hf) updated with new tag SHA pointing to commit 3fb40b3
- Tests still pass (55 passed, 1 skipped)
- Tag SHA chain: e3c561d (broken-form) -> 50f194e (UTF-8 corrected); both deref to commit 3fb40b3

### Reversibility
The original tag annotation was backed up to /tmp/original_tag_v2.1.1_message_BACKUP.txt before deletion; the backup was retained until verification of the new tag completed, then cleaned up alongside the new tag message file in Phase 4.

---

## Day 2 Corrections (2026-05-07)

**Document appended:** 2026-05-08 (scoped exclusion-only commit; 8 author corrections deferred per Decision 1, see "Deferred items" below).

### Source
Manual PMC document triangulation. 6 PMC full-text documents were independently verified by Jordan against committee 2060 corrections on 2026-05-07. 9 of 9 author attributions confirmed as committee-suggested. The verification surfaced one critical exclusion (PMID 29462145, off-topic urology paper) and 8 author corrections for downstream PMIDs.

### Critical Finding: PMID 29462145 EXCLUDED

- **Original committee hint:** VIRAL_W1_07 companion = Mehta R Zika systematic review.
- **Actual PMID 29462145 content:** "Videourodynamic findings of lower urinary tract dysfunctions in men with persistent storage lower urinary tract symptoms after medical treatment" (Jiang YH, Wang CC, Kuo HC. PLoS One 2018;13(2):e0190704).
- **Topic:** Urology - benign prostatic hyperplasia / bladder outlet obstruction in men. ZERO meningitis / encephalitis / Zika content.
- **Resolution:** EXCLUDED from corpus. Future Class 3 Zika neurological vignette slots (if added in subsequent commits) will be anchored solely to Brito Ferreira ML 2017 (PMID 29140242) without a companion. Note: PMID 29140242 is also NOT currently in PMID_REGISTRY; that addition is deferred along with the 8 author corrections per Decision 1.
- **Lesson:** Camino largo extremo manual verification justified retroactively. Bulk acceptance of committee corrections (Option B at decision point) would have contaminated VIRAL_W1_07 with off-topic urology paper.

### Artifact Applied in this Commit (scoped)

- **PMID_REGISTRY EXCLUDED comment block** added at the end of `scripts/generate_pam_vignettes.py` PMID_REGISTRY, documenting PMID 29462145 exclusion + cross-reference to this section.
- **Lock-in test** `test_pmid_29462145_excluded_from_registry` added to `tests/vignettes/test_pam_vignettes.py`. Asserts PMID 29462145 is not present in PMID_REGISTRY; assertion holds permanently regardless of future ADDs.
- **Schema unmodified.** PMID_REGISTRY entry count unchanged at 57 (29462145 was never present; the exclusion is a documentation + test guard, not a removal).

### Closed Items: 8 PMIDs Not Needed (resolved 2026-05-08)

The 8 author corrections originally proposed for this commit cycle target PMIDs that are NOT currently in PMID_REGISTRY (verified 2026-05-08 via empirical key lookup):

| Slot | PMID | Target First Author | Status |
|------|------|---------------------|--------|
| BACT_W1_06 | 21067624 | Amaya-Villar R | CLOSED - NOT NEEDED |
| BACT_W1_08 | 30815433 | Xu M | CLOSED - NOT NEEDED |
| BACT_W1_11 | 23823579 | Azevedo LCP | CLOSED - NOT NEEDED |
| VIRAL_W1_01 | 34840888 | Montalvo M | CLOSED - NOT NEEDED |
| VIRAL_W1_06 | 37797296 | Petersen PT | CLOSED - NOT NEEDED |
| VIRAL_W1_07 | 29140242 | Brito Ferreira ML | CLOSED - NOT NEEDED |
| VIRAL_W1_11 | 25324865 | Ryu JU | CLOSED - NOT NEEDED |
| VIRAL_W1_12 | 38744070 | Pham TS | CLOSED - NOT NEEDED |

#### Resolution (read-only audit 2026-05-08)

A read-only audit on 2026-05-08 cross-referenced the 8 deferred PMIDs against current `BACTERIAL_DISTRIBUTION` (vignette_id 61-90) and `VIRAL_DISTRIBUTION` (vignette_id 91-120) anchors after Commit 5.3.2 pilot ship.

Verdict: 8/8 NOT NEEDED for current corpus structure.

- All 60 BACT + VIRAL slots in the locked distributions already have PMIDs assigned
- Zero overlap between the 8 deferred PMIDs and the 14 distinct slot-anchor PMIDs in current lock
- The 8 deferred PMIDs were artifacts of a superseded "Wave 1" planning attempt (slot IDs `BACT_W1_xx` / `VIRAL_W1_xx`) that does not match the current `vignette_id` 61-120 architecture from Commit 5.3.1

Action: All 8 PMIDs DISCARDED from active backlog. Forensic trail preserved above for audit completeness. No PMID_REGISTRY ADDs performed.

If Subphase 1.4 (TBM + Cryptococcal + GAE) or Subphase 1.5 (NCC + Tropical + Non-infectious) introduces additional Class 2 or Class 3 slots beyond the locked 30+30, a fresh anchor selection process will run; retrofitting these specific 8 PMIDs is not authorized.

#### Subphase 1.3.x Errata (resolved 2026-05-08)

Audit also surfaced a broken anchor reference unrelated to the 8 deferred PMIDs: slot v83 in `BACTERIAL_DISTRIBUTION` referenced PMID 18626302 (typo PMID removed from `PMID_REGISTRY` in Commit 5.3.2). Existing parametrized test `test_day2_pmids_in_registry` covers PAM corpus IDs 21-60 only and missed the leak.

Resolution applied in this commit (Subphase 1.3.x):

- Slot v83 anchor changed: PMID 18626302 to PMID 32935747 (Soeters HM CDC ABCs surveillance, demographically appropriate for adolescent NM case)
- Slot v83 methodology field updated from `tier_3_imputation_within_cohort_review` to `tier_4_imputation_cdc_abcs_anchored` to match the new anchor
- New lock-in test `test_bacterial_viral_distribution_pmids_in_registry` parametrizes over all 60 BACT + VIRAL slots; permanent guard against future regression
- Test was written FIRST (TDD), confirmed FAILING on v83 18626302 with assertion message `[(83, '18626302')]`, then v83 fixed and confirmed PASSING

This commit is the formal closure of Subphase 1.2.x metadata lock work plus the v83 errata caught by the read-only audit.

A subsequent commit (planned: scoped ADD with full Vancouver metadata) will introduce these 8 PMIDs as new PMID_REGISTRY entries and apply the canonical first authors verbatim. The ADD requires:

1. Full Vancouver `authors_full` lists per PMID (not provided in current Day 2 audit).
2. `journal`, `journal_short_code`, `year`, `volume`, `issue`, `pages`, `title`, `doi`, `pmc_id` per PMID.
3. Decision on `first_author` schema field (currently registry uses `authors_short`; new field requires schema-extension decision).
4. Slot-ID mapping (`BACT_W1_xx` / `VIRAL_W1_xx` to current `vignette_id` integers in BACTERIAL_DISTRIBUTION / VIRAL_DISTRIBUTION).
5. PMID 34840888 metadata refinements: `pages = "e714-e721"` (not e640-e647); `anchor_type = "case_series_with_review"` (PMID_REGISTRY developer-facing field only; LiteratureAnchor schema enum is locked and does not include this value, so vignette JSON `literature_anchors[].anchor_type` must remain within the locked enum).
6. PMID 37797296 `article_number = "e16081"` (not e16125). New field; addition decision deferred.

### Verification Method

Manual PMC full-text document review for each PMID. Author bylines compared character-by-character against committee corrections. Publication type and pagination cross-checked against journal landing page metadata. PMID 29462145's off-topic urology content was confirmed in PMC document on 2026-05-07.

### Confidence Level

PMID 29462145 exclusion: 100% (off-topic content empirically confirmed in PMC document). 8 author corrections: 100% pending entry creation (will be applied verbatim once ADD scope is authorized).
