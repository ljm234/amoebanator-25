# PMID Day 2 Pre-Distribution-Lock Corrections Audit Trail
## Amoebanator Subphase 1.2 - Commit 2.5 of 5
## Date: May 5, 2026

## Source
Verification audit research mode audit:
compass_artifact_wf-c3f74c5c-0e6d-4116-8cdf-4c03dc486879

Plus user-side PubMed UI verification for 2 high-priority items
(Celik 2021 issue number, Phung 2025 outcome confirmation).

## Errors Caught Before Distribution Lock

### BLOCKING errors (2)

#### 1. PMID 38526236 Burki 2024 Pakistan SURVIVOR - page numbers
- Registry pre-fix: EID 30(4):788-791
- CORRECT: EID 30(4):803-805
- Sources confirming 803-805:
  - PubMed primary record
  - PMC10977850
  - CDC EID journal page (wwwnc.cdc.gov/eid/article/30/4/23-0979_article)
  - Aga Khan University institutional page
- Verification method: research_mode_4pass_revalidated_2026-05-05

#### 2. PMID 35463884 Zhou 2022 China - geography precision
- Registry pre-fix: caveat said only "China pediatric case" without province
- CORRECT: Changsha, Hunan Province, China (Third Xiangya Hospital, Central South University)
- Critical: A separate audit reference flagged "Hainan" as the prior wrong-province assumption that was being carried in adjudicator-facing notes. Hainan is the tropical island province in South China Sea; Hunan is a landlocked central-China province; distinct geographies entirely.
- Sources confirming Hunan:
  - PubMed affiliations
  - PMC9033202 body text
  - Frontiers article page
- Verification method: research_mode_4pass_revalidated_2026-05-05
- Caveat now contains explicit negation ("NOT Hainan") for adjudicator clarity.

### HIGH-PRIORITY items (2)

#### 3. PMID 33381798 Celik 2021 Newborn - issue number
- Registry pre-fix: J Trop Pediatr 67(2):fmaa100
- CORRECT: J Trop Pediatr 2021 Jan 29;67(1):fmaa100
- Source confirming 67(1): PubMed UI direct fetch on 2026-05-05
  - Citation block: "J Trop Pediatr. 2021 Jan 29;67(1):fmaa100"
- Added new field: `publication_date: "2021-01-29"`
- Verification method: user_pubmed_ui_direct_fetch_2026-05-05

#### 4. PMID 39795618 Phung 2025 Vietnam - outcome precision
- Registry pre-fix outcome: FATAL with 14-day prolonged survival
- CONFIRMED CORRECT outcome: FATAL (no change to classification)
- Caveat refinement: Add temporal precision
  - Section 2 Case Presentation states: "passed away after 11 days of hospitalization"
  - Section 3 Discussion states: "passed away 14 days after disease onset"
  - Both numbers are accurate, measure different things (hospitalization vs onset-to-death)
- Verification method: research_mode_4pass_plus_user_mdpi_fulltext_2026-05-05

## Bookkeeping Check
- PMID 39174030 (Wei Taiwan) uniqueness verified: 1 occurrence (correct, no duplicate)
- No duplicate entries detected in registry

## Total Registry State After This Commit
- Pre-commit count: 42 PMIDs
- Post-commit count: 42 PMIDs (no entries added/removed)
- Modified entries: 4
- author_aliases coverage: 4/42 (Burki, Cogo, Heggie, Kou) - PRESERVED
- verification_method coverage: 22/42 - 4 entries updated to reflect re-verification

## Methodology Mix Update
- research_mode_4pass_revalidated_2026-05-05: 2 entries (Burki, Zhou)
- user_pubmed_ui_direct_fetch_2026-05-05: 1 entry (Celik)
- research_mode_4pass_plus_user_mdpi_fulltext_2026-05-05: 1 entry (Phung)

## Hainan/Hunan literal count rationale (audit-trail design choice)
The Zhou caveat now contains 2 occurrences of "Hainan" as explanatory negations
("NOT Hainan" and "Hainan is the tropical island province in South China Sea").
This is a deliberate audit-trail design choice: an adjudicator reading the
caveat sees the disambiguation in context rather than only seeing the corrected
"Hunan" without knowing what the prior-state confusion was. Hunan literal count
is 3 (canonical mention + "Hunan is a landlocked central-China province" +
caveat header).

## Tag Chain Progression
- v2.1-pam-day1-locked
- v2.1.1-pmid-corrections-5pass
- v2.1.2-day2-pmids-canonized
- v2.1.3-anchor-type-schema-compliance
- v2.1.4-day2-anchor-pool-complete
- v2.1.5-day2-prelock-corrections        <-- THIS COMMIT
- v2.1.6-day2-distribution-locked        (next, Commit 3)
- v2.1.7-day2-pilot-validated            (Commit 4)
- v2.2.0-day2-corpus-complete            (Commit 5, final)

## Verification

| Gate | Result |
|---|---|
| AST parse | OK |
| Tests | 75 passed, 1 skipped (no regression) |
| Em-dashes | 0 |
| AI-tells | 0 |
| Sandi UTF-8 (c3 ad) | 175 (preserved) |
| Kupper UTF-8 (c3 bc) | 17 (preserved) |
| Ertug UTF-8 (c4 9f) | 3 (preserved) |
| Hunan literal | 3 (NEW - Zhou correction context) |
| Hainan literal | 2 (deliberate negation in caveat for audit clarity) |

## Next Steps
1. Push origin + hf
2. Tag v2.1.5-day2-prelock-corrections
3. Commit 3 of 5: Lock Day 2 distribution plan (40 vignettes v21-v60)
   using Option C anchor-driven hybrid distribution

Phase deadline: May 28, 2026 (medRxiv submission)
