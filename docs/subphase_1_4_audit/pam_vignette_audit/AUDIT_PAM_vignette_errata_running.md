# PAM Vignette-Level Errata Log (Running)
Created: 2026-05-26
Status: ACCUMULATING - will be processed in Errata 5.4.3.3 phase

## Methodology
- Audit READ-ONLY in Subphase 1.4
- Errors logged here for batch fix in Errata 5.4.3.3
- Each error format: ERR-NNN with vignette_id, anchor, type, vignette claim, paper truth, severity, fix proposal

## Errors Confirmed (2026-05-26)

### Demographic-level (Sub-Bundles 01-02 + prior catalog)
ERR-001: pam_d2_026 Wang 2018 (PMID 30055569) | AGE | vignette 10/M vs paper 42/M Shenzhen | CRITICAL
ERR-002: pam_d2_041 Zhou 2022 (PMID 35463884) | AGE | vignette 14/M vs paper 9/M Changsha | CRITICAL
ERR-003: pam_d2_042 Sazzad 2020 (PMID 31734864) | AGE | vignette 30/M vs paper 15/M Bangladesh | CRITICAL
ERR-004: pam_d2_052 Wei 2024 (PMID 39174030) | AGE+SEX | vignette 22/M vs paper 30/F Taiwan | CRITICAL
ERR-005: pam_d2_043 Retana 2020 (PMID 32752181) | FRANKENSTEIN | vignette 7/M groundwater survivor matches no actual case (real: 15M hot springs fatal, 5F hot springs survivor, 1mo groundwater fatal) | CRITICAL
ERR-006: pam_d2_044 DeNapoli 1996 (PMID 8923775) | AGE+SEX | vignette 8/F vs paper 13/M | CRITICAL (no _imputed_ flag)
ERR-007: pam_d2_045 DeNapoli 1996 (PMID 8923775) | AGE | vignette 10/M vs paper 13/M | CRITICAL (no _imputed_ flag)
ERR-008: pam_d1_002 Dulski 2025 (PMID 40146665) | AGE+SEX | vignette 3/F Arkansas vs paper 16mo sex-unspecified | CRITICAL (no _imputed_ flag)
ERR-009: pam_d1_004 Eger 2023 (PMID 37470480) | AGE | vignette 4/M Texas vs paper 3/M | CRITICAL (no _imputed_ flag)
ERR-010: pam_d2_040 Yoder 2010 (PMID 19845995) | OUTCOME | vignette survivor vs paper review states "nearly always fatal" | MEDIUM
ERR-012: pam_d1_008 Kemble 2012 (PMID 22238170) | AGE+SEX | vignette 9/M Minnesota lake summer camp vs paper Annie Bahneman 7/F Lily Lake Stillwater | CRITICAL (likely Jack Ariola-Erenberg 2012 case mis-anchored to Kemble Annie 2010 case)
ERR-013: pam_d1_009 Anjum 2021 (PMID 34307045) | AGE | vignette 14/M N Florida vs paper 13/M Caucasian Madison County FL | CRITICAL (no _imputed_ flag)

### Clinical content fabrication (Sub-Bundles 01-02)
ERR-011: pam_d1_001, 002, 003, 004, d2_050, d2_051 (6 splash pad vignettes Dulski + Eger) | CSF FABRICATION | WBC 10x off Dulski/2.4x off Eger; RBC 10x off Dulski/16x off Eger; protein/glucose off; dates off; sex assumed for Dulski sex-unspecified paper | HIGH
ERR-014: pam_d1_006 Anjum 2021 (PMID 34307045) | CLINICAL CONTENT FABRICATION | demo matches (13/M N Florida) but CSF Opening pressure 26 vs 36 cmH2O, WBC 1800 vs 670, protein 200 vs 389; MRI "normal" vs paper "leptomeningeal enhancement"; exposure "private pond" vs "campground water park untreated lake"; treatment timing "4h from admission" vs "62h after symptom onset" | HIGH

### Minor (location detail)
ERR-015: pam_d1_005 Kemble 2012 (PMID 22238170) | LOCATION DETAIL | vignette "central Minnesota" vs paper Lily Lake Stillwater Washington County (eastern Minnesota) | LOW

### Sub-Bundle 03 river/canal additions (2026-05-27)
ERR-016: pam_d2_041 Zhou 2022 (PMID 35463884) | EXPOSURE TYPE WRONG | vignette says rural river swimming vs paper says "public swimming POOL choked" + CSF protein 438 vs paper 2606 (6x off) | CRITICAL
ERR-017: pam_d1_007 Maloney 2023 (PMID 37460088) | CSF VALUES OFF | demo matches (8/M Nebraska Elkhorn) but CSF WBC 5200 vs paper 6574; neut 96% vs 91%; protein 460 vs >600 mg/dL | MEDIUM
ERR-018: pam_d2_049 Rauf 2025 (PMID 40009134) | AGE + CSF FABRICATION | vignette 11/M vs paper 14/M; vignette CSF WBC 1820 (87% neut) vs paper CSF WBC 43 (20% neut, 80% LYMPHOCYTIC - atypical case); paper is FIRST CONFIRMED India PAM survivor | CRITICAL
ERR-019: pam_d1_018 Lares-Villa 1993 (PMID 8458963) | UNVERIFIABLE | vignette 9/M Mexicali canal vs paper "5 cases" with no individual demographics in abstract; full text paywall | UNVERIFIABLE
ERR-020: pam_d2_046 Lares-Villa 1993 (PMID 8458963) | UNVERIFIABLE _reuse | vignette 11/M Mexicali canal _reuse_ from 5-case Lares paper; demographics unverifiable | UNVERIFIABLE

## Status
- Total errors: 20 (was 15)
- Total vignettes affected: 23 unique files (was 18)
- Sub-Bundles deep-audited: 3/12 PAM (25%)
- Vignettes demo-audited: 87/270 (32%)
- CSF cross-check for Kemble vignettes: PENDING (no full text access)

## Pattern Detected
- Day-1 "plain" filename vignettes that don't match anchor demographics = systematic undisclosed imputations
- Even demographic-matching vignettes have fabricated CSF/clinical content
- _reuse_ flag is consistently applied to disclosed imputations (Day-2 set)
- NEW PATTERN: Even demographic-matching vignettes have CSF values fabricated with "PAM-classic" templates that don't match atypical real cases (Rauf Kerala best example: real case low WBC + lymphocytic vs vignette high WBC + neutrophilic)

End of file.
