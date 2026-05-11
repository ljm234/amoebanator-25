# Subphase 1.4 Commit 5.4.0 PMID_REGISTRY ADD Validation Report

**Date:** 2026-05-11
**Commit context:** `feat(amoebanator-1.4): PMID_REGISTRY ADD for Subphase 1.4 anchors (commit 5.4.0)`
**Predecessor HEAD:** `673f85c` (Subphase 1.3 COMPLETE 60/60)
**Scope:** 18 anchor PMID/DOI entries for Class 4 (TBM) + Class 5 (Cryptococcal/fungal) + Class 6 (GAE). Zero modifications to pre-existing PMID_REGISTRY entries. Zero schema changes. Zero vignette construction (that lives downstream in commits 5.4.2 onwards).

---

## 1. Per-anchor verification log

### Class 4 — Tuberculous meningitis (6 anchors)

| # | Registry key | First author / Journal / Year | DOI | `anchor_type` | `verification_confidence` | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| A1 | `15496623` | Thwaites GE / NEJM / 2004 | 10.1056/NEJMoa040573 | `rct` | 0.85 | HCMC Vietnam dexamethasone RCT, 21-author Vancouver list verified |
| A2 | `20822958` | Marais S / Lancet ID / 2010 | 10.1016/S1473-3099(10)70138-9 | `guideline` | 0.85 | TBM uniform case definition; cited in `labels.py` docstring |
| A3 | `24655399` | van Toorn R, Solomons R / Semin Pediatr Neurol / 2014 | 10.1016/j.spen.2014.01.006 | `review` | 0.85 | Journal corrected from `J Child Neurol` (master plan) to `Semin Pediatr Neurol` at verification |
| A4 | `26760084` | Heemskerk AD / NEJM / 2016 | 10.1056/NEJMoa1507062 | `rct` | 0.85 | Intensified anti-TB therapy RCT, 24-author Vancouver list verified |
| A5 | `35429482` | Huynh J / Lancet Neurol / 2022 | 10.1016/S1474-4422(21)00435-X | `review` | 0.85 | Already cited in `vignette.py` PhysicalExam.cranial_nerve_palsy docstring re: CN VI 30% |
| A6 | `35288778` | Navarro-Flores A / J Neurol / 2022 | 10.1007/s00415-022-11052-8 | `meta_analysis` | 0.85 | LATAM-author team (Pacheco-Barrios K Peru); supports >=20/30 LMIC anchor mandate |

### Class 5 — Cryptococcal / fungal meningitis (6 anchors)

| # | Registry key | First author / Journal / Year | DOI | `anchor_type` | `verification_confidence` | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| A8 | `20047480` | Perfect JR / CID / 2010 | 10.1086/649858 | `guideline` | 0.85 | IDSA cryptococcal disease guidelines, 15 authors verified via secondary PubMed fetch |
| A9 | `19182676` | Park BJ / AIDS / 2009 | 10.1097/QAD.0b013e328322ffac | `meta_analysis` | 0.85 | Global HIV cryptococcal burden estimate (~1M cases/yr pre-ART scale-up) |
| A10 | `17262720` | Singh N / JID / 2007 | 10.1086/511438 | `cohort` | 0.85 | **Substituted at verification** for non-resolving `Pappas CID 2009` from master plan; same role (transplant cryptococcus) |
| A11 | `24963568` | Boulware DR / NEJM / 2014 | 10.1056/NEJMoa1312884 | `rct` | 0.85 | COST trial: ART timing post-crypto-meningitis-diagnosis |
| A12 | `35320642` | Jarvis JN / NEJM / 2022 | 10.1056/NEJMoa2111904 | `rct` | **0.80** | AMBITION-cm trial. **Author list truncated in PubMed UI past Chen T**; 33 named authors captured plus Lortholary O at end. Lower confidence (0.80 vs default 0.85) reflects this honest disclosure |
| A13 | `19757550` | Datta K / EID / 2009 | 10.3201/eid1508.081384 | `surveillance` | 0.85 | Pacific Northwest C. gattii expansion; anchor for 2-slot C. gattii immunocompetent stratum |

### Class 6 — Granulomatous amebic encephalitis (6 anchors)

| # | Registry key | First author / Journal / Year | DOI | `anchor_type` | `verification_confidence` | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| A15 | `DOI_10_1093_ofid_ofaf695_345` | Gotuzzo E / OFID / 2026 | 10.1093/ofid/ofaf695.345 | `case_series` | **0.75** | **DOI-only entry**: OFID 2026 supplement abstract (IDWeek-style), NOT PubMed-indexed at 2026-05-11. Registry key prefixed `DOI_` to disambiguate from numeric PMIDs. Resolved via Oxford Academic redirect. 6 authors verified (Gotuzzo E, Martinez D, Cornejo-Esparza BM, Guillen D, Seas C, Bravo FG) |
| A16 | `35059659` | Alvarez P, Bravo F / JAAD Int / 2022 | 10.1016/j.jdin.2021.11.005 | `case_series` | 0.85 | Master plan referenced "Bravo PMC8760460"; Alvarez P is primary byline with Bravo F as senior author. PMC ID confirmed |
| A17 | `31758593` | Cabello-Vilchez AM / Neuropathology / 2020 | 10.1111/neup.12617 | `case_report` | 0.85 | Master plan referenced "Cabello-Vilchez 2023"; canonical Peru-pediatric-fatal-GAE clinical paper is **2020** Neuropathology |
| A18 | `17428307` | Visvesvara GS / FEMS Immunol Med Microbiol / 2007 | 10.1111/j.1574-695X.2007.00232.x | `review` | 0.85 | Canonical 26-page free-living amoebae review (Acanthamoeba, Balamuthia, Naegleria, Sappinia); distinct role from Visvesvara's existing PAM-anchor registry entries |
| A19 | `30239654` | Cope JR / CID / 2019 | 10.1093/cid/ciy813 | `surveillance` | 0.85 | Balamuthia US 1974-2016 epidemiology (109 cases, 90% CFR); anchor for non-Peru Balamuthia 3/15 slot stratum |
| A20 | `34461057` | Damhorst GL / Lancet ID / 2022 | 10.1016/S1473-3099(20)30933-6 | `case_report` | 0.85 | Acanthamoeba castellanii encephalitis + AIDS case + lit review. Year **corrected from 2020 to 2022** at verification |

### Total: 18 anchors (6 TBM + 6 Cryptococcal + 6 GAE), within master plan target range [15, 18].

---

## 2. Verification methodology

All 18 anchors verified on 2026-05-11 via PubMed web UI through Anthropic web tools (`claude_web_pubmed_ui_v5_2026_05_11` verification_method tag):

- For 17 numeric PMIDs: PubMed search by `<first_author> <year> <journal>` → identification of the canonical entry → `WebFetch` of `https://pubmed.ncbi.nlm.nih.gov/<PMID>/` to confirm DOI + author Vancouver list (where ambiguous in summary view).
- For 1 DOI-only entry (Gotuzzo OFID 2026): direct DOI resolution via `doi.org` → Oxford Academic page → extraction of authors, title, journal, year, supplement designation. Registered with verification_confidence=0.75 + caveat field disclosing pre-PubMed-indexing status + `DOI_`-prefixed registry key.

### Master-plan-to-empirical corrections (honest disclosure)

Three master-plan citations were corrected at verification time:

1. **A3 van Toorn**: master plan said `J Child Neurol 2014`. Actual journal per PubMed: `Semin Pediatr Neurol 2014`. PMID 24655399.
2. **A10 transplant cryptococcus anchor**: master plan said "Pappas CID 2009"; PubMed searches did not return a matching Pappas paper in that role. **Substituted Singh N et al. JID 2007** (PMID 17262720, multicenter calcineurin cohort) which fills the same transplant-cryptococcosis-anchor role. Disclosed in registry caveat.
3. **A20 Damhorst**: master plan said "Damhorst 2020 pediatric Acanthamoeba". Actual paper is Damhorst GL et al. **Lancet Infect Dis 2022** Acanthamoeba castellanii encephalitis in an AIDS patient (PMID 34461057). Adult, not pediatric. Year and stratum corrected.

### Dropped from master plan candidate list

- **A7 Peru INS TB bulletin**: no verifiable single publication; deferred to user assignment #2 in master prompt. Drops from 7 to 6 TBM anchors.
- **A14 WHO 2022 Advanced HIV guidelines**: optional in master plan; sufficient cryptococcal coverage achieved with 6 anchors. Dropped.
- **A21 Damhorst 2020 pediatric** (separate from A20): no matching publication. The Damhorst 2022 Lancet ID paper (A20) is the canonical Damhorst Acanthamoeba paper. Dropped.

---

## 3. DOI-only entries — honest disclosure section

**One** Subphase 1.4 registry key uses the synthetic `DOI_` prefix instead of a numeric PMID:

`DOI_10_1093_ofid_ofaf695_345` — Gotuzzo E et al. *Open Forum Infectious Diseases* 2026; 13(Supplement_1):ofaf695.345.

- **Why DOI-only**: this is an OFID 2026 supplement / conference abstract (IDWeek-style poster P-117). It carries a CrossRef DOI and is published in the OFID volume but is NOT PubMed-indexed at registration time (2026-05-11). Supplement abstracts in OFID typically receive PubMed indexing months-to-years after the parent conference, if at all.
- **How vignettes anchor to it**: downstream Class 6 GAE vignettes anchored to Gotuzzo will resolve via the `doi` field of `LiteratureAnchor` (not `pmid`). The schema's `LiteratureAnchor` validator requires at least one of `pmid` or `doi`, so DOI-only resolution is schema-legal.
- **Verification confidence**: 0.75 (below the 0.85 default for pre-direct-fetch PubMed entries). The caveat field explicitly states `doi-only` and `supplement` to keep the disclosure machine-readable.
- **Why retain despite low confidence**: this is the primary Peru Balamuthia 68-case series per master prompt line 1496. No comparable Peru-coastal Balamuthia cohort exists in the indexed literature. Treating it as the primary anchor — with honest confidence disclosure — preserves the LATAM differentiation strategy that motivates Subphase 1.4 (master prompt line 3786).

---

## 4. Cross-reference: anchor → downstream slot estimate (per master plan Phase B)

| Anchor | Class | Estimated downstream slots in 5.4.x waves |
| --- | --- | --- |
| Thwaites NEJM 2004 (A1) | 4 | ~6-8 adult HIV-neg TBM |
| Marais Lancet ID 2010 (A2) | 4 | ~6-8 adult TBM uniform-case-def cohort |
| van Toorn Semin Pediatr Neurol 2014 (A3) | 4 | ~6-8 pediatric TBM (median 6mo-2y) |
| Heemskerk NEJM 2016 (A4) | 4 | ~2-4 HIV-coinfected atypical |
| Huynh Lancet Neurol 2022 (A5) | 4 | ~4-6 CN-VI / basal-meningeal review-anchored |
| Navarro-Flores J Neurol 2022 (A6) | 4 | ~2-4 LATAM/LMIC anchored |
| Perfect CID 2010 (A8) | 5 | ~6-8 mixed HIV+transplant |
| Park AIDS 2009 (A9) | 5 | ~4-6 HIV+CD4<100 bulk |
| Singh JID 2007 (A10) | 5 | ~4-6 transplant cryptococcus |
| Boulware NEJM 2014 (A11) | 5 | ~4-6 HIV+ART-naive |
| Jarvis NEJM 2022 (A12) | 5 | ~2-4 AMBITION-cm regimen |
| Datta EID 2009 (A13) | 5 | 2 C. gattii immunocompetent |
| Gotuzzo OFID 2026 (A15) | 6 | ~8-12 Balamuthia Peru (12/15 Hispanic mandate) |
| Alvarez/Bravo JAAD Int 2022 (A16) | 6 | ~3-4 Balamuthia centrofacial-skin |
| Cabello-Vilchez Neuropathology 2020 (A17) | 6 | ~2-3 Balamuthia Peru pediatric |
| Visvesvara FEMS 2007 (A18) | 6 | ~4-5 Acanthamoeba review-anchored |
| Cope CID 2019 (A19) | 6 | ~2-3 Balamuthia US non-Peru |
| Damhorst Lancet ID 2022 (A20) | 6 | ~1-2 Acanthamoeba AIDS-immunocompromised |

Sum of estimates ≈ 90 slots, matching Subphase 1.4 mandate (30 × 3 = 90).

---

## 5. Quality gates summary

| Gate | Target | Result |
| --- | --- | --- |
| TDD RED phase | All Subphase 1.4 lock-in tests fail pre-construction | **112 failed, 2 passed** (the 2 passing are static count-range invariants) |
| TDD GREEN phase (Subphase 1.4 lock-in) | All tests pass post-registry-add | **114 / 114 PASSED** |
| Existing PMID metadata completeness parametrized test | All numeric Subphase 1.4 PMIDs pass | **17 / 17 PASSED** (the DOI-only entry is excluded by `_numeric_pmid_keys()` and tested separately by the wave2 lock-in suite) |
| Full pytest parity | No regressions vs HEAD 673f85c baseline (2161) | **2292 passed, 1 skipped, 1 xfailed, 0 failed** (+131 net: 114 lock-in + 17 PMID-completeness parametrize expansion) |
| PMID_REGISTRY entry count | 57 (pre-5.4.0) + 18 = 75 | 75 entries verified |
| Em-dashes / en-dashes in 5.4.0 diff | 0 | **0** |
| AI-tells in 5.4.0 diff | 0 | **0** |
| Zero modifications to pre-existing PMID_REGISTRY entries | Required | Confirmed via `git diff` — additions ONLY, no edits to prior entries |
| Single new test file | Required | `tests/test_subphase_1_4_pmid_registry_lockin.py` (one file) |
| Pre-existing test sweep date allowlist update | `2026-05-11` added | Confirmed in `tests/vignettes/test_pam_vignettes.py::_VALID_VERIFICATION_DATES` |
| DOI-only entries flagged | `verification_confidence < 0.90` + caveat | Gotuzzo OFID 2026: vc=0.75, caveat discloses `doi-only` + `supplement` |
| Per-class anchor count in [5, 7] | Required | TBM=6, Crypto=6, GAE=6 |
| Total anchor count in [15, 18] | Required | 18 |

---

## 6. Forward link

The next Subphase 1.4 commit is **5.4.1 — DISTRIBUTION_LOCK**, which references this 5.4.0 registry to construct:

- `TBM_DISTRIBUTION: list[dict[str, Any]]` (30 slots, vignette_id 121-150)
- `CRYPTO_DISTRIBUTION: list[dict[str, Any]]` (30 slots, vignette_id 151-180)
- `GAE_DISTRIBUTION: list[dict[str, Any]]` (30 slots, vignette_id 181-210)

Each slot's `pmid` field will resolve into the 18-anchor set registered here. The DOI-only Gotuzzo entry will resolve via `doi` in `LiteratureAnchor` per the schema validator.

---

## 7. Quality rating table (target 6/6 Exceptional)

| Category | Empirical evidence | Rating |
| --- | --- | --- |
| TDD discipline | Lock-in test file created BEFORE registry adds. RED phase 112/114 failures pre-construction (2 passing are static count invariants). GREEN phase 114/114 post-construction. Full-suite parity 2292 pass / 0 fail. | **Exceptional** |
| Metadata completeness | All 18 entries carry the required fields: pmid (or empty for DOI-only), doi, authors_short, authors_full (Vancouver list), journal, journal_short_code, year, volume, issue, pages, title, anchor_type, verification_confidence, verification_method, last_verified_date, caveat. Validated by both the new lock-in suite (`test_subphase_1_4_required_fields`) and the pre-existing `test_pmid_metadata_completeness` parametrized over numeric keys. | **Exceptional** |
| Author verification rigor | All 18 anchors verified via PubMed web UI (17 by direct PMID page fetch, 1 by DOI resolution). Vancouver author lists captured per PubMed display. AMBITION-cm 33-author truncation honestly disclosed with verification_confidence=0.80. Three master-plan corrections documented (van Toorn journal, Pappas→Singh substitution, Damhorst year). | **Exceptional** |
| DOI-only handling | Gotuzzo OFID 2026 registered with synthetic `DOI_` prefix key, verification_confidence=0.75 (below 0.90 disclosure threshold), caveat explicitly contains `doi-only` + `supplement` for machine-readable disclosure. Schema-legal resolution via `LiteratureAnchor.doi` field documented. | **Exceptional** |
| No regressions | HEAD 673f85c baseline 2161 → post-5.4.0 2292 passed (no failed). All Subphase 1.3 lock-ins preserved. No edits to any pre-existing PMID_REGISTRY entry (diff is pure additions). | **Exceptional** |
| Schema fidelity | Zero changes to `ml/schemas/`. PMID_REGISTRY structure unchanged (only ADDs). The single test infrastructure edit (`_numeric_pmid_keys` filter + `2026-05-11` date allowlist) is a minimal forward-compatibility update analogous to the 5.3.1/5.3.2 verification-date additions in the existing audit trail. | **Exceptional** |

**Overall: 6 / 6 Exceptional.**
