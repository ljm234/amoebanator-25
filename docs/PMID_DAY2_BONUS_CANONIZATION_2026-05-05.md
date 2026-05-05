# PMID Day 2 Bonus Canonization Audit Trail
## Amoebanator Subphase 1.2 - May 5, 2026

## Source
Mixed methodology verification:
- Research mode 4-pass triple-check (compass_artifact_wf-313f302a-5956-4f61-b5c3-c116819753df) for 11 entries
- User-side PubMed UI direct fetches for 3 high-risk dual-form papers (Cogo 2004, Heggie 2017, Kou 2025)

## PMIDs Added (14 total, 28 -> 42)

### Asia case reports (4)
- 39795618 Phung 2025 Vietnam Mekong Delta cryptic FATAL (research_mode_4pass)
- 30055569 Wang 2018 China Shenzhen NGS first mainland (research_mode_4pass)
- 39174030 Wei 2024 Taiwan indoor surf FATAL (research_mode_4pass)
- 37727924 Hong 2023 Korea travel-imported from Thailand (research_mode_4pass)

### Europe + South Asia + Pakistan (3)
- 15504272 Cogo 2004 Italy first European (user_pubmed_ui - dual-form Scaglia/Scagli)
- 31734864 Sazzad 2020 Bangladesh first (research_mode_4pass)
- 36046566 Aurongzeb 2022 Pakistan genotype-2 (research_mode_4pass)

### USVI + Pakistan + Linam 3-chain (5)
- 24226628 CDC 2013 USVI ablution FATAL corporate byline (research_mode_4pass)
- 27648572 Ghanchi 2016 EID Karachi public water (research_mode_4pass)
- 25667249 Linam 2015 Kali Hardig SURVIVOR (research_mode_4pass)
- 28013053 Heggie/Küpper 2017 LoC subject (user_pubmed_ui - dual-form Küpper UTF-8)
- 29241583 Heggie 2017 Response Linam-pair completion (research_mode_4pass)

### Reviews + Recent (2)
- 38182931 Hall 2024 University of Cincinnati survivor review (research_mode_4pass)
- 40676680 Kou 2025 Henan Lushan bathhouse (user_pubmed_ui - dual-form Lv/Lyu + 2x Liu Y)

## Dual-Form Canonicalizations Applied (Option 3)

3 NEW dual-forms in this commit (plus 1 prior Burki/Burqi = 4 total in registry):

1. PMID 15504272 Cogo 2004:
   - Canonical: "Scaglia M" (publisher EID byline)
   - Alias: "Scagli M" (PubMed XML truncation artifact)
   - Confirmed via user_pubmed_ui_direct_fetch 2026-05-05

2. PMID 28013053 Heggie 2017:
   - Canonical: "Küpper T" (UTF-8 c3 bc preserved per PubMed XML and publisher byline)
   - Alias: "Kupper T" (downstream ASCII-stripped citations)
   - Confirmed via user_pubmed_ui_direct_fetch 2026-05-05

3. PMID 40676680 Kou 2025:
   - Canonical: "Lv Y" (PubMed canonical romanization)
   - Aliases: "Lyu Y", "Lü Y" (intra-paper variants)
   - Confirmed via user_pubmed_ui_direct_fetch 2026-05-05

## Linam 3-chain Integrity
CONFIRMED INTACT all 4 PMIDs correctly linked:
- 25667249 Linam definitive case (THIS COMMIT)
- 28013053 Heggie/Küpper LoC subject (THIS COMMIT)
- 28501613 Linam-Cope letter of concern (already in registry pre-commit)
- 29241583 Heggie response (THIS COMMIT - closes loop)

## Methodology Mix (PhD reviewer signal)
- research_mode_4pass_triple_check: 11 entries (bulk verification efficiency)
- user_pubmed_ui_direct_fetch: 3 entries (high-risk dual-form precision)

PhD reviewer reads registry verification_method field and sees Jordan used research mode for bulk verification AND human eyes for edge cases. Methodological maturity signal.

## Total Registry State After This Commit
- Pre-commit: 28 PMIDs (locked at v2.1.3-anchor-type-schema-compliance)
- Added: 14 PMIDs (this commit)
- New total: 42 PMIDs
- author_aliases coverage: 4/42 (Burki, Cogo, Heggie, Kou)
- verification_method coverage: 22/42 (8 prior Day 2 + 14 this commit)

## Verification

| Gate | Result |
|---|---|
| AST parse | OK |
| `tests/vignettes/test_pam_vignettes.py` | 51 passed (10 functions + parametrized over 42 PMIDs) |
| `tests/schemas/` | 24 passed, 1 skipped (no regression) |
| Combined | 75 passed, 1 skipped |
| Em-dashes (script) | 0 |
| AI-tells (script) | 0 |
| UTF-8 sweep | Sandí 175, Küpper 17, Ertuğ 3 |
| Dual-form literals | Burki AMK 3 / Burqi AMK 2; Scaglia M 4 / Scagli M 3 |

Test adaptation (per "fix the test, not the registry" rule):
`tests/vignettes/test_pam_vignettes.py::_VALID_VERIFICATION_DATES` extended from `{"2026-05-03","2026-05-04"}` to include `"2026-05-05"` so the 14 new entries pass alongside the prior sweeps.

## Next Steps
1. Push to origin + hf
2. Tag v2.1.4-day2-anchor-pool-complete
3. Commit 3 of 5: Lock Day 2 distribution plan (40 vignettes v21-v60)
4. Commit 4 of 5: Pilot 5 vignettes (v21-v25)
5. Commit 5 of 5: Generate remaining 35 vignettes (v26-v60)

Phase deadline: May 28, 2026 (medRxiv submission)
