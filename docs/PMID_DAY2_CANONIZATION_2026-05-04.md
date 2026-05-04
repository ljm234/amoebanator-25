# PMID Day 2 Canonization Audit Trail
## Amoebanator Subphase 1.2 - May 4, 2026

## Source
6th-pass independent triple-check verification (compass_artifact_wf-13eb5fad)
+ user-side PubMed UI direct fetches for all 8 PMIDs.

## PMIDs Applied (8 entries; 6 new + 2 update-in-place)

The 8-entry spec contained 2 PMIDs already present in `PMID_REGISTRY` from prior passes (38526236 Burki, 34307045 Anjum); these were updated in place rather than duplicated. The remaining 6 are new additions. Net registry growth: 22 -> 28.

### Resolved from prior 6th-pass flags (3 new)
- PMID 39606118 - Lin L et al. 2024 Front Microbiol (Sichuan myocarditis, atypical pediatric pool exposure)
- PMID 40969815 - Li J et al. 2025 Front Med (Chengdu CDC field investigation, same index patient as Lin 2024)
- PMID 32752181 - Retana Moreira L et al. 2020 Pathogens (Costa Rica groundwater, 3-case series with 1 survivor)

### Bonus high-value additions (3 new + 2 updates)
- PMID 35463884 - Zhou W et al. 2022 Front Pediatr (China pediatric, misdiagnosis-as-bacterial-meningitis anchor, 7 authors)
- PMID 34906097 - Huang S et al. 2021 BMC Infect Dis (China pediatric mNGS dual-compartment CSF + blood)
- PMID 33381798 - Celik Y, Arslankoylu AE 2021 J Trop Pediatr (NEWBORN extreme-age presentation, 2-author paper)
- PMID 38526236 - Burki AMK et al. 2024 EID (Pakistan adult SURVIVOR; updated with full Vancouver metadata + Option-3 dual-form alias structure)
- PMID 34307045 - Anjum SK et al. 2021 IDCases (N Florida tap water; updated with full volume/issue/pages metadata + verbose author list)

## Burki/Burqi Dual-Form Canonicalization (Option 3)

PMID 38526236 implements modern bibliographic best practice with both forms stored:
- Canonical (`authors_full[0]`): `"Burki AMK"`
- Alias (`author_aliases` dict): `{"Burki AMK": ["Burqi AMK"]}`
- `alias_rationale` field documents 8 of 10 authoritative sources confirming "Burki"
- PubMed XML "Burqi" preserved as alias for search recall
- Aligns with NLM/ORCID/Crossref/OpenAlex/FAIR data principles
- Replaces the prior `aliases.first_author` schema with the canonical-first dict structure

## Verification Methodology

All 8 entries verified via direct PubMed UI fetch by user (Jordan Montenegro)
on May 4, 2026. User pasted PubMed UI output verbatim into research session.
Author lists, PMIDs, DOIs, PMC IDs all extracted from user-paste, NOT inferred
or hallucinated. `verification_method` field set to `"user_pubmed_ui_direct_fetch"`
on all 8 entries to distinguish from search-snippet-inferred entries.

## Diacritic Preservation Audit (UTF-8)

All UTF-8 diacritics preserved verbatim from PubMed UI:
- "Sandí" (Costa Rica): UTF-8 c3 ad for í
- "Ertuğ" (Turkish given name): UTF-8 c4 9f for ğ - in caveat documentary text only (Vancouver-style author list collapses to initial "AE")
- "Xiu'an" (Chinese given name): standard ASCII apostrophe in caveat
- "O'Laughlin" (Irish surname): standard ASCII apostrophe in caveat
- All compound Spanish surnames preserved un-hyphenated per publication form
  (Retana Moreira, NOT Retana-Moreira; Abrahams Sandí, NOT Abrahams-Sandí)

## Schema-Compliance Adaptations

Two adaptations were required to keep the 8 entries valid against the LOCKED `VignetteSchema` while preserving all user-supplied data:

### 1. `anchor_type` schema-compliance + `anchor_subtype` for descriptive metadata

The schema's `LiteratureAnchor.anchor_type` is a strict Literal of base types: `case_report | guideline | review | surveillance | meta_analysis | cohort | rct | prospective_observational`. The user's spec used long descriptive forms like `case_report_us_tap_water_north_florida`. These were preserved as-is in a new `anchor_subtype` registry field; `anchor_type` was set to the schema-compliant base type for each entry:

| PMID | `anchor_type` (schema-bound) | `anchor_subtype` (descriptive) |
|---|---|---|
| 39606118 Lin | `case_report` | `case_report_pediatric_fatal_atypical_myocarditis_indoor_pool` |
| 40969815 Li | `surveillance` | `epi_field_investigation_pediatric_fatal_indoor_pool` |
| 32752181 Retana Moreira | `case_report` | `case_series_environmental_groundwater_central_america` |
| 38526236 Burki | `case_report` | `case_report_adult_SURVIVOR_pakistan_first_pakistani_survivor` |
| 35463884 Zhou | `case_report` | `case_report_pediatric_fatal_misdiagnosis_as_bacterial_meningitis` |
| 34906097 Huang | `case_report` | `case_report_pediatric_fatal_mNGS_dual_compartment_china` |
| 33381798 Celik | `case_report` | `case_report_newborn_fatal_extreme_age_atypical` |
| 34307045 Anjum | `case_report` | `case_report_us_tap_water_north_florida` |

### 2. `inclusion_decision_rationale` length cap in `_build_provenance`

Several updated entries (Burki, Anjum) carry verbose author-list caveats that, when concatenated into `provenance.inclusion_decision_rationale` via `_build_provenance`, exceeded the schema's `max_length=1000`. The helper now budget-caps the appended caveat suffix and adds a `...` truncation marker if the full caveat would overflow. The registry caveat itself is preserved verbatim; only the propagation into the rationale is bounded.

## Test Adaptation (per "fix the test, not the registry" standing rule)

`tests/vignettes/test_pam_vignettes.py::_CASE_ID_RE` and `_ALLOWED_JOURNAL_CODES`:
- Regex relaxed from `[A-Za-z]+` to `.+?` (non-greedy) for the journal portion, to accept Vancouver-style abbreviations like `Emerg Infect Dis` that contain spaces.
- Allowed-journal set extended with the new Vancouver codes: `Emerg Infect Dis`, `Front Microbiol`, `Front Med (Lausanne)`, `Pathogens`, `Front Pediatr`, `BMC Infect Dis`, `J Trop Pediatr`, plus prior round's `TexMed`, `JPIDS`, `EpidemiolInfect`, `ExpertRevAntiInfect`.

Result: vignette 19 (Burki) case_id is now `PAM-D1-019-Emerg Infect Dis-2024-Karachi-Survivor-Adult` (contains spaces, was `PAM-D1-019-EID-2024-Karachi-Survivor-Adult`).

## Total Registry State After This Commit

- Previous count: 22 PMIDs (locked at v2.1.1-pmid-corrections-5pass tag)
- Net additions this commit: 6 new PMIDs
- Updated in place: 2 PMIDs (Burki, Anjum)
- New total: 28 PMIDs

## Verification

| Gate | Result |
|---|---|
| AST parse | OK |
| `tests/vignettes/test_pam_vignettes.py` | 37 passed (10 functions + parametrized over 28 PMIDs) |
| `tests/schemas/` | 24 passed, 1 skipped (no regression) |
| Schema 20/20 dry-run | 20 PASS / 0 FAIL |
| AI-tells | 0 / 0 |
| Em-dashes | 0 / 0 |
| UTF-8 diacritics | Sandí (c3 ad) preserved; Ertuğ (c4 9f) preserved in caveat documentary text |

## Next Steps

1. Push to origin + hf (await user GO)
2. Tag v2.1.2-day2-pmids-canonized (await user GO)
3. Day 2 vignette generation v21-v60 (40 new vignettes; await user GO)
4. Phase deadline May 28, 2026 (medRxiv submission)
