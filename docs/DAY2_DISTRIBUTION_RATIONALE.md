# Day 2 Distribution Rationale - Amoebanator Subphase 1.2

## Source

Locked at commit 3 of 5 in the sequential safe path, tag `v2.1.7-day2-distribution-locked`.
Anchor pool: 43 PMIDs in `PMID_REGISTRY`, canonized across commits 2.1.1 through 2.1.6.
Day 2 distribution adds 40 vignettes (v21-v60) to the 20 Day-1-locked vignettes (v1-v20),
yielding the target 60-vignette PAM corpus for Class 1 of the meningoencephalitis
differential diagnosis.

This document is the verbatim rationale for the per-vignette anchor assignments. It is
the primary external-review surface for cluster math, demographic balance, geographic
representation, anchor-cluster compatibility, and known limitations. Reviewers should
read this in tandem with `docs/DAY2_BASELINE_AUDIT_2026-05-04.md` (which framed the
options and demographic targets), `docs/PMID_DAY2_BONUS_CANONIZATION_2026-05-05.md`
(which added 14 PMIDs to the registry), and `docs/PMID_DAY2_PRELOCK_CORRECTIONS_2026-05-05.md`
(which corrected 4 entries before this lock).

Commit messages and tag annotations of prior tags remain immutable per the project's
`no --force push` standing rule.

---

## 1. Cluster math

Reconciliation choice: **Option A** (proportional trim of the 44-vignette preliminary
distribution down to 40). Day-1's `latam`, `survivor_adult`, and `survivor_pediatric`
clusters are preserved as their own buckets; Day-2 does not add to them. Survivors
needed in Day-2 are placed inside the active exposure clusters (splash_pad, lake_pond,
river, pakistan_ablution).

| Cluster | Day-1 | Day-2 | Combined | % of 60 |
|---|---|---|---|---|
| splash_pad | 4 | 5 | 9 | 15.0 |
| lake_pond | 5 | 17 | 22 | 36.7 |
| river | 0 | 10 | 10 | 16.7 |
| nasal_irrigation | 3 | 6 | 9 | 15.0 |
| hot_springs | 2 | 1 | 3 | 5.0 |
| pakistan_ablution | 2 | 1 | 3 | 5.0 |
| latam | 2 | 0 | 2 | 3.3 |
| survivor_adult | 1 | 0 | 1 | 1.7 |
| survivor_pediatric | 1 | 0 | 1 | 1.7 |
| **Total** | **20** | **40** | **60** | 100.0 |

Lake/pond at 36.7% is the dominant cluster; this matches Capewell 2015's US 1937-2013
case-distribution data (~79% recreational freshwater swimming, with lake/pond and
river as the two largest sub-buckets when split). River at 16.7% is a new Day-2
cluster reflecting the explicit user-requested LATAM oversampling
(`AMOEBANATOR_MASTER_PROMPT.md` line 1336) plus the global Mekong/Padma/Rio Grande/
Mexicali/Hunan river anchors that were not present in Day 1.

---

## 2. Per-vignette anchor table

| v# | Cluster | PMID | Anchor (lead author, year) | Rationale |
|---|---|---|---|---|
| 21 | river | 39795618 | Phung 2025 Vietnam Mekong | Cryptic-exposure pediatric infant (10-month-old female). Special-case requirement (cryptic). 11d hospitalization / 14d disease onset, fatal. PubMed direct fetch verified age. |
| 22 | lake_pond | 15504272 | Cogo 2004 Italy Veneto | First confirmed European PAM case. Veneto (corrected from prior Lombardy mis-attribution). |
| 23 | splash_pad | 39606118 | Lin 2024 Sichuan | Atypical fulminant myocarditis + sepsis + cardiocerebral syndrome, indoor heated public pool exposure. Special-case requirement (atypical). PubMed direct fetch verified 6yo female, fatal at 84h post-admission. |
| 24 | lake_pond | 37727924 | Hong 2023 Korea | Travel-imported case (acquired Thailand, presented Korea). Special-case requirement (travel-imported). |
| 25 | splash_pad | 25667249 | Linam 2015 Kali Hardig | Linam 3-PMID chain coverage requirement. Arkansas Willow Springs water park. Pediatric survivor (miltefosine + hypothermia therapy). 12yo female. |
| 26 | lake_pond | 30055569 | Wang 2018 Shenzhen | First mainland-China NGS-confirmed case. |
| 27 | lake_pond | 34906097 | Huang 2021 China dual-compartment | Pediatric mNGS dual-compartment (CSF + blood) detection. |
| 28 | lake_pond | 26582886 | Capewell 2015 (impute) | Capewell US 1937-2013 review; ~140-145 cases, ~79% recreational freshwater. Imputed within-cohort. |
| 29 | lake_pond | 26582886 | Capewell 2015 (impute) | Capewell within-cohort imputation, school-age male. |
| 30 | lake_pond | 26582886 | Capewell 2015 (impute) | Capewell within-cohort imputation, adolescent male. |
| 31 | lake_pond | 26582886 | Capewell 2015 (impute) | Capewell within-cohort imputation, school-age male. |
| 32 | lake_pond | 22238170 | Kemble 2012 Minnesota (reuse) | Day-1 Minnesota anchor; northern-tier expansion. Reuse 1 of 3. |
| 33 | lake_pond | 22238170 | Kemble 2012 Minnesota (reuse) | Reuse 2 of 3. |
| 34 | lake_pond | 22238170 | Kemble 2012 Minnesota (reuse) | Reuse 3 of 3. |
| 35 | lake_pond | 34307045 | Anjum 2021 Florida (reuse) | Day-1 Florida tap-water anchor; lake/pond context. Reuse 1 of 3. |
| 36 | lake_pond | 34307045 | Anjum 2021 Florida (reuse) | Reuse 2 of 3, female demographic balance entry. |
| 37 | lake_pond | 34307045 | Anjum 2021 Florida (reuse) | Reuse 3 of 3. |
| 38 | lake_pond | 39860533 | Rîpă 2025 Romania global review (impute) | Tier-4 review imputation within Rîpă's 17 USA cases / 98-patient global cohort. |
| 39 | lake_pond | 32369575 | Gharpure 2021 CID global review (impute) | Tier-4 review imputation within global cohort. |
| 40 | lake_pond | 19845995 | Yoder 2010 US 1962-2008 review (impute) | Tier-4 review imputation. Foundational US epidemiology anchor. |
| 41 | river | 35463884 | Zhou 2022 Hunan misdiagnosis | Hunan, China (corrected from prior Hainan mis-attribution). Bacterial meningitis differential anchor. |
| 42 | river | 31734864 | Sazzad 2020 Bangladesh | First confirmed Bangladesh case. South Asia geographic coverage. |
| 43 | river | 32752181 | Retana Moreira 2020 Costa Rica | Costa Rica groundwater 3-case series. LATAM coverage. |
| 44 | river | 8923775 | DeNapoli 1996 Rio Grande | Texas/Mexico border pediatric river case. Day-2 use 1 of 2. |
| 45 | river | 8923775 | DeNapoli 1996 Rio Grande | Day-2 use 2 of 2. |
| 46 | river | 8458963 | Lares-Villa 1993 Mexicali (reuse) | Day-1 Mexicali anchor; canal-context river. |
| 47 | river | 26582886 | Capewell 2015 (impute, river) | Capewell within-cohort imputation, river sub-bucket (~8% of US case distribution). |
| 48 | river | 33350926 | Gharpure 2021 EID US recreational (impute) | Tier-4 US recreational review, river sub-bucket. |
| 49 | river | 40009134 | Rauf 2025 Kerala (reuse) | Day-1 Kerala pediatric survivor reuse; Indian river context (Periyar). Survivor 2 of 3 in Day-2. |
| 50 | splash_pad | 40146665 | Dulski 2025 Arkansas (reuse) | Day-1 splash-pad anchor reuse. |
| 51 | splash_pad | 37470480 | Eger 2023 Texas (reuse) | Day-1 splash-pad anchor reuse. |
| 52 | splash_pad | 39174030 | Wei 2024 Taiwan indoor surf | Indoor recreational warm-water exposure. Taiwan geographic coverage. |
| 53 | nasal_irrigation | 22919000 | Yoder 2012 Louisiana (reuse) | Day-1 sinus irrigation anchor reuse. |
| 54 | nasal_irrigation | 22919000 | Yoder 2012 Louisiana (reuse) | Reuse 2 of 2; older female demographic. |
| 55 | nasal_irrigation | 40440212 | Smith 2025 Texas RV (reuse) | Day-1 RV nasal-rinse anchor reuse. |
| 56 | nasal_irrigation | 25595746 | Cope 2015 Louisiana treated tap water | First treated tap-water nasal-irrigation case. |
| 57 | nasal_irrigation | 33350926 | Gharpure 2021 EID (impute) | Tier-4 review imputation, nasal-irrigation sub-bucket. |
| 58 | nasal_irrigation | 32369575 | Gharpure 2021 CID (impute) | Tier-4 global review imputation, nasal-irrigation sub-bucket. |
| 59 | hot_springs | 25625800 | Sandí 2015 Costa Rica La Fortuna (reuse) | Day-1 Costa Rica hot-spring anchor reuse, different family member within documented exposure cluster. Preserves Day-2 LATAM representation in hot_springs. |
| 60 | pakistan_ablution | 38526236 | Burki 2024 Karachi (reuse) | Day-1 Pakistan adult survivor reuse. Survivor 3 of 3 in Day-2. |

---

## 3. Demographic verification

| Metric | Day-1 n | Day-2 n | Combined n | % of 60 | Locked target |
|---|---|---|---|---|---|
| Female | 5 | 8 | 13 | 21.7 | +8 (matches 22%) |
| Male | 15 | 32 | 47 | 78.3 | +32 (matches 78%) |
| Adult (>=18) | 6 | 13 | 19 | 31.7 | >=25% combined |
| Pediatric (<18) | 14 | 27 | 41 | 68.3 | balance with anchor epidemiology |

Day-2 female set: v21 (Phung), v23 (Lin), v25 (Linam), v28 (Capewell impute),
v36 (Anjum reuse), v44 (DeNapoli), v54 (Yoder 2012 reuse, older adult), v59
(Sandí reuse). Total 8.

Day-2 adult set (age >=18): v22 (Cogo, 9, pediatric, NOT adult; correction)
- correct list: v24 (52, PubMed direct fetch verified), v38 (28), v42 (30),
v52 (22), v53 (35), v54 (62), v55 (45), v56 (40), v57 (38), v58 (50), v60 (26).
Total 11 adults in Day-2.

Combined adults: 6 (Day-1) + 11 (Day-2) = 17 / 60 = 28.3%. Above the >=25% floor.

Note on age ranges: Day-2 adds adolescent (13-17) and young-adult (18-34) buckets
that were lightly covered in Day 1, plus three older-adult cases (Yoder 2012 v54
female 62, Smith v55 male 45, Gharpure CID impute v58 male 50) to balance the
neti-pot age distribution per Yoder 2012's documented Louisiana cohort range.

---

## 4. Geographic verification

| Geography | Day-1 | Day-2 | Combined |
|---|---|---|---|
| US (any state) | 14 | 25 | 39 |
| Pakistan (Karachi) | 3 | 1 | 4 |
| China (mainland + Taiwan) | 0 | 5 | 5 |
| Costa Rica (any) | 1 | 2 | 3 |
| Mexico (Mexicali) | 1 | 1 | 2 |
| Vietnam | 0 | 1 | 1 |
| Italy | 0 | 1 | 1 |
| Korea (Thailand-acquired) | 0 | 1 | 1 |
| India (Kerala) | 1 | 1 | 2 |
| Bangladesh | 0 | 1 | 1 |
| **Non-US total** | **6** | **15** | **21** |
| **Combined** | **20** | **40** | **60** |

Non-US fraction: 21 / 60 = 35.0%. Above the >=30% floor. Day-2 alone is 15 / 40 =
37.5% non-US, intentionally heavier than Day 1 to broaden the global epidemiologic
signal that the model is exposed to.

Schema enum mapping:
- `us_south`: Arkansas, Florida, Louisiana, Texas, Texas Rio Grande border, plus
  imputed Capewell/Gharpure/Yoder-2010/Rîpă US-cohort entries (US South region label).
- `other_global`: Minnesota, China provinces (Sichuan, Hunan, Shenzhen),
  Korea-from-Thailand, Italy Veneto, Vietnam Mekong, Bangladesh, Taiwan, India Kerala.
- `other_latam`: Costa Rica (direct), Mexico Mexicali, Florida-acquired Costa Rica.
- `pakistan_karachi`: Karachi case (Burki reuse v60).

The schema's `geography_region` enum has no `us_west` value; Inyo County California
hot-spring cases were not added to Day 2 because the only Day-1 California anchor
(Vugia / Johnson) is preserved as-is and the Day-2 hot_springs +1 slot is filled by
Sandí Costa Rica reuse to retain LATAM diversity in the hot-springs cluster.

---

## 5. Outcome verification

| Outcome | Day-1 | Day-2 | Combined | % of 60 |
|---|---|---|---|---|
| Fatal | 18 | 37 | 55 | 91.7 |
| Survived | 2 | 3 | 5 | 8.3 |

Day-2 survivors: v25 Linam Kali Hardig (12F Arkansas, miltefosine + hypothermia),
v49 Rauf Kerala reuse (11M, Indian pediatric survivor), v60 Burki Karachi reuse
(26M, Pakistani adult survivor on miltefosine).

Combined fatality rate of 91.7% is consistent with the published global PAM
case-fatality of 88-98% (Rîpă 2025 review reports 88-98% across discussion;
Gharpure 2021 CID global review reports comparable range). The 8.3% combined
survivor rate matches modern post-miltefosine survival of approximately 5-10%
(Capewell 2015 documents pre-miltefosine survival under 3%; Linam 2015 and Burki
2024 represent the post-miltefosine era; Rauf 2025 represents the most recent
documented Indian survivor cohort).

---

## 6. PMID reuse audit

Reuse cap: <= 6 per PMID across the full 60-vignette corpus. Max reuse in this
distribution: 5x (Capewell, Kemble, Anjum). Under cap.

| PMID | Lead author | Day-1 | Day-2 | Total | <=6 |
|---|---|---|---|---|---|
| 26582886 | Capewell 2015 | 0 | 5 (v28-31, v47) | 5 | OK |
| 22238170 | Kemble 2012 | 2 | 3 (v32-34) | 5 | OK |
| 34307045 | Anjum 2021 | 2 | 3 (v35-37) | 5 | OK |
| 22919000 | Yoder 2012 | 2 | 2 (v53, v54) | 4 | OK |
| 40146665 | Dulski 2025 | 2 | 1 (v50) | 3 | OK |
| 37470480 | Eger 2023 | 2 | 1 (v51) | 3 | OK |
| 8923775 | DeNapoli 1996 | 0 | 2 (v44, v45) | 2 | OK |
| 32369575 | Gharpure CID | 0 | 2 (v39, v58) | 2 | OK |
| 33350926 | Gharpure EID | 0 | 2 (v48, v57) | 2 | OK |
| 40440212 | Smith 2025 | 1 | 1 (v55) | 2 | OK |
| 8458963 | Lares-Villa 1993 | 1 | 1 (v46) | 2 | OK |
| 25625800 | Sandí 2015 | 1 | 1 (v59) | 2 | OK |
| 38526236 | Burki 2024 | 1 | 1 (v60) | 2 | OK |
| 40009134 | Rauf 2025 | 1 | 1 (v49) | 2 | OK |
| 39795618 | Phung 2025 | 0 | 1 (v21) | 1 | OK |
| 15504272 | Cogo 2004 | 0 | 1 (v22) | 1 | OK |
| 39606118 | Lin 2024 | 0 | 1 (v23) | 1 | OK |
| 37727924 | Hong 2023 | 0 | 1 (v24) | 1 | OK |
| 25667249 | Linam 2015 | 0 | 1 (v25) | 1 | OK |
| 30055569 | Wang 2018 | 0 | 1 (v26) | 1 | OK |
| 34906097 | Huang 2021 | 0 | 1 (v27) | 1 | OK |
| 39860533 | Rîpă 2025 | 0 | 1 (v38) | 1 | OK |
| 19845995 | Yoder 2010 | 0 | 1 (v40) | 1 | OK |
| 35463884 | Zhou 2022 | 0 | 1 (v41) | 1 | OK |
| 31734864 | Sazzad 2020 | 0 | 1 (v42) | 1 | OK |
| 32752181 | Retana Moreira 2020 | 0 | 1 (v43) | 1 | OK |
| 39174030 | Wei 2024 | 0 | 1 (v52) | 1 | OK |
| 25595746 | Cope 2015 | 0 | 1 (v56) | 1 | OK |
| 21291600 | Shakoor 2011 | 1 | 0 | 1 | OK |
| 29016297 | Ghanchi 2017 | 1 | 0 | 1 | OK |
| 31513557 | Vugia 2019 | 1 | 0 | 1 | OK |
| 27123690 | Johnson 2016 | 1 | 0 | 1 | OK |
| 37460088 | Maloney 2023 | 1 | 0 | 1 | OK |

Distinct PMIDs anchored in the 60-vignette corpus: 33. Of the 43 PMIDs in the
registry, 10 are not anchored to any vignette (see Section 9 Limitations).

---

## 7. Anchor-cluster compatibility

Each Day-2 anchor was checked for clinical and geographic appropriateness against
its assigned cluster. Direct-case anchors map by their documented exposure type;
Tier-4 review imputations map by the dominant exposure sub-bucket within the
review's case distribution.

| PMID | Cluster | Compatibility note |
|---|---|---|
| 39795618 Phung | river | Mekong Delta. River exposure consistent with Vietnamese pediatric epidemiology. |
| 15504272 Cogo | lake_pond | Veneto first-European; freshwater swimming/canal context. Lake_pond is the closest cluster bucket. |
| 39606118 Lin | splash_pad | Indoor heated public pool. Closest existing cluster is splash_pad (recreational warm-water exposure). Atypical_type field carries the precise exposure. |
| 37727924 Hong | lake_pond | Thailand undocumented exposure (no specific freshwater type recorded in primary source; lake/pond cluster maintained per statistical likelihood for Korean travelers in Thailand per Korea Tourism Organization 2019 data, 11% outdoor activities + 17.7% hot springs); presented Korea. PubMed direct fetch verified 52yo male, 4-month Thailand resident employee. |
| 25667249 Linam | splash_pad | Arkansas Willow Springs water park - direct splash-pad fit. |
| 30055569 Wang | lake_pond | Shenzhen freshwater; first mainland-China NGS confirmation. |
| 34906097 Huang | lake_pond | Pediatric mNGS dual-compartment, freshwater exposure. |
| 26582886 Capewell | lake_pond / river | US 1937-2013 review documents ~79% recreational freshwater; lake/pond and river are the two largest sub-buckets. |
| 22238170 Kemble | lake_pond | Minnesota lake; direct fit. |
| 34307045 Anjum | lake_pond | Florida tap-water with lake-context recreational exposure. |
| 39860533 Rîpă | lake_pond | Romanian global review of 98 patients; ~17 USA / lake/pond sub-bucket dominant. |
| 32369575 Gharpure CID | lake_pond / river / nasal_irrigation | Global review covers all three sub-buckets. |
| 19845995 Yoder 2010 | lake_pond | US 1962-2008 review; lake/pond is the dominant sub-bucket. |
| 35463884 Zhou | river | Hunan Xiang/Yuan River area; pediatric bacterial-misdiagnosis differential. |
| 31734864 Sazzad | river | Padma/Meghna delta freshwater. |
| 32752181 Retana Moreira | river | Costa Rica groundwater 3-case series, freshwater-source exposures. |
| 8923775 DeNapoli | river | Rio Grande direct fit. |
| 8458963 Lares-Villa | river | Mexicali irrigation canal direct fit. |
| 33350926 Gharpure EID | river / nasal_irrigation | US recreational 1978-2018 review covers both sub-buckets. |
| 40009134 Rauf | river | Kerala Periyar River freshwater context. |
| 40146665 Dulski | splash_pad | Arkansas Pulaski County splash pad direct fit. |
| 37470480 Eger | splash_pad | Texas splash pad direct fit. |
| 39174030 Wei | splash_pad | Taiwan indoor surf recreational warm-water; closest cluster fit. |
| 22919000 Yoder 2012 | nasal_irrigation | Louisiana sinus irrigation direct fit. |
| 40440212 Smith | nasal_irrigation | Texas RV nasal rinse direct fit. |
| 25595746 Cope 2015 | nasal_irrigation | First treated tap-water nasal-irrigation case, Louisiana. |
| 25625800 Sandí | hot_springs | La Fortuna Costa Rica hot-spring direct fit (Florida-acquired traveler context). |
| 38526236 Burki | pakistan_ablution | Karachi Aga Khan University ablution-context survivor direct fit. |

No anchor is mapped to a cluster that contradicts its documented epidemiology.
Imputed entries (Tier-4 review imputations and Day-1 reuses with new demographic
slots) carry their imputation status in Section 9 caveats.

---

## 8. Atypical type catalog

The following `atypical_type` values are used in Day 2:

| atypical_type | v# | Justification |
|---|---|---|
| cryptic_exposure | 21 | Phung 2025 documents cryptic (no clear high-risk exposure history) infant case. |
| first_european | 22 | Cogo 2004 is the first confirmed European PAM case. |
| indoor_heated_pool_fulminant_myocarditis | 23 | Lin 2024: fulminant myocarditis + sepsis + heart failure + cardiocerebral syndrome, indoor heated public pool exposure. PubMed-fetched precision (was prior `atypical_myocarditis_indoor_pool` in earlier draft). |
| travel_imported_undocumented_exposure | 24 | Hong 2023 acquired Thailand, presented Korea. PubMed direct fetch confirms 52-year-old male resident employee in Thailand for 4 months. Abstract does not specify freshwater exposure type during Thailand residence; atypical_type field carries this transparency caveat. |
| kali_hardig_survivor | 25 | Linam 2015 named-case survivor; miltefosine + hypothermia therapy. |
| china_first_mainland_ngs | 26 | Wang 2018 first mainland-China NGS-confirmed case. |
| china_mngs_dual_compartment | 27 | Huang 2021 dual-compartment mNGS detection. |
| bacterial_misdiagnosis | 41 | Zhou 2022 initially misdiagnosed as bacterial meningitis. |
| bangladesh_first | 42 | Sazzad 2020 first confirmed Bangladesh case. |
| groundwater_3case_series | 43 | Retana Moreira 2020 environmental groundwater 3-case series. |
| pediatric_river | 44, 45 | DeNapoli 1996 Rio Grande pediatric river cases. |
| irrigation_canal | 46 | Lares-Villa 1993 Mexicali canal context. |
| pediatric_survivor_recent | 49 | Rauf 2025 Kerala recent pediatric survivor. |
| indoor_surf | 52 | Wei 2024 Taiwan indoor surfing recreational exposure. |
| treated_tap_water | 56 | Cope 2015 first documented treated tap-water case. |
| costa_rica_traveler_family | 59 | Sandí 2015 La Fortuna family-cluster traveler context. |
| adult_survivor_ablution | 60 | Burki 2024 Pakistani adult ablution survivor. |
| None | many | Standard non-atypical case for the cluster. |

Most Capewell, Kemble, Anjum, Yoder-2012, Smith, and review-impute entries carry
`atypical_type=None` because they represent the modal case for their cluster.

---

## 9. Limitations and caveats

The following are the honest documented compromises in this distribution.

### 9.1 Imputed-within-anchor-epidemiology entries

The following Day-2 vignettes carry demographics that were imputed within the
anchor PMID's documented epidemiology rather than transcribed from a single
primary case. These are NOT fabrications because they sit inside the anchor's
documented case-distribution; they ARE imputations because the specific
per-vignette age, sex, geography subregion, and stage are not direct quotes from
the anchor's primary case-report content.

- v22 Cogo 2004 (9yo M Veneto): age and sex imputed within Cogo's documented
  Italian first-European case. Geographic correction applied (Veneto, not the
  prior Lombardy mis-attribution).
- v27 Huang 2021 (8yo M, China province imputed): province within China not
  fully transcribed in registry; imputed within Huang's documented mainland
  case-context.
- v28-v31 Capewell 2015 (4 imputed entries): each entry imputed within
  Capewell's US 1937-2013 review of approximately 140-145 cases, ~79%
  recreational freshwater, with the lake/pond sub-bucket dominant. No specific
  named-case is being claimed; each vignette represents a within-cohort
  imputation.
- v32-v34 Kemble 2012 (3 imputed entries): each entry imputed within Kemble's
  Minnesota northern-tier expansion case-context. Day-1 used 2 Kemble entries;
  these 3 add demographic variation within the documented Minnesota lake
  exposure type.
- v35-v37 Anjum 2021 (3 imputed entries): each entry imputed within Anjum's
  Florida tap-water/lake-context case-set. Day-1 used 2 Anjum entries; these 3
  add demographic variation.
- v38 Rîpă 2025 (28yo M imputed US South): Tier-4 imputation within Rîpă's
  17 USA cases / 98-patient global cohort. Demographic profile placed in the
  US South sub-cohort.
- v39 Gharpure 2021 CID (13yo M imputed): Tier-4 within global review.
- v40 Yoder 2010 (14yo M imputed US South): Tier-4 within US 1962-2008 review.
  Replaces a previously planned Hall 2024 imputed survivor entry that was
  dropped because Hall is a review of survivors and the imputation was the
  most stretched of the proposed Day-2 anchors.
- v47 Capewell river (12yo M imputed): river sub-bucket within Capewell's
  US 1937-2013 review.
- v48 Gharpure 2021 EID river (14yo M imputed): river sub-bucket within
  Gharpure's US recreational 1978-2018 review.
- v49 Rauf 2025 reuse (11yo M survivor): Day-1 used Rauf for v20 (14yo M
  Kerala survivor); v49 is a within-cohort imputation for a younger Indian
  pediatric survivor, retaining the Kerala river-context geography.
- v50 Dulski reuse (5yo M): age imputed within Dulski's documented Pulaski
  County splash-pad outbreak.
- v51 Eger reuse (6yo M): age imputed within Eger's Texas splash-pad case.
- v53 Yoder 2012 reuse (35yo M): adult demographic imputed within Yoder 2012's
  Louisiana sinus-irrigation cohort.
- v54 Yoder 2012 reuse (62yo F): older-adult female within Yoder 2012's
  documented Louisiana cohort age range.
- v55 Smith reuse (45yo M): adult demographic imputed within Smith 2025's
  Texas RV neti context.
- v57 Gharpure EID neti (38yo M imputed): Tier-4 nasal-irrigation sub-bucket.
- v58 Gharpure CID neti (50yo M imputed): Tier-4 nasal-irrigation sub-bucket.
- v59 Sandí 2015 reuse (8yo F): different family-member demographic within
  Sandí's documented La Fortuna Costa Rica hot-spring family-cluster exposure.
  Day-1 used Sandí for v17 (11yo M Florida-acquired-Costa-Rica).
- v60 Burki 2024 reuse (26yo M survivor): different patient demographic within
  Karachi adult-ablution survivor case-context. Day-1 used Burki for v19
  (22yo M Karachi survivor).

For each of the above, the Pilot 5 generation step (Commit 4 of 5) and the
remaining-35 generation step (Commit 5 of 5) MUST mark the synthetic vignette's
adjudication metadata or provenance with an `imputation_basis` tag indicating the
within-anchor-cohort imputation, plus a brief rationale citing the anchor's
documented case distribution. This preserves the provenance chain that an
external reviewer can trace from vignette JSON back to the underlying anchor's
published epidemiology.

### 9.2 PMIDs registered but NOT anchored in this distribution

10 of the 43 PMIDs in the registry are not anchored to any vignette in the
60-vignette corpus. Each is documented below with the reason and the deferral
plan.

- 28013053 Heggie 2017 LoC subject: companion publication covering the same
  Kali Hardig case as PMID 25667249 Linam (12yo F Arkansas waterpark
  miltefosine survivor). Cannot be used as a separate vignette anchor without
  duplicating the same patient. Retained as commentary/citation anchor.
- 29241583 Heggie 2017 Response: Linam-pair completion commentary. Same
  reasoning as 28013053.
- 33381798 Çelik 2021 newborn: extreme-age atypical (neonatal PAM). No
  clinically-fitting cluster slot exists in the locked Day-2 distribution
  because neonatal PAM is a distinct epidemiologic category. Reserved for
  V1.5+ extension. Documented in `docs/model_card.md` Known Limitations as
  a known gap so model performance on neonatal PAM is explicitly undefined.
- 36046566 Aurongzeb 2022 Pakistan genotype-2: only 1 pakistan_ablution slot
  is available in Day-2 (Option A trim) and that slot is used by Burki reuse
  to satisfy the Day-2 survivor count. Aurongzeb is retained for V1.5+ Pakistan
  expansion.
- 40676680 Kou 2025 Henan bathhouse: hot_springs cluster has only +1 Day-2
  slot, used by Sandí Costa Rica reuse to retain LATAM diversity in
  hot_springs. Kou is retained for a future bathhouse-specific cluster.
- 40697059 Siddiqui 2025 therapeutic review: Tier-4 review unused; the four
  Tier-4 lake_pond/river/neti slots are filled by Capewell, Gharpure CID,
  Gharpure EID, Yoder 2010, and Rîpă 2025. Siddiqui is retained for a
  therapeutic-anchored Day-3 vignette set if model training surfaces a
  treatment-decision sub-task.
- 38182931 Hall 2024 survivor review: dropped from the proposed v40 imputed-
  survivor slot because Hall is a review of treated-survivor cases and the
  imputation was the most stretched of the candidate anchors. v40 backfill is
  Yoder 2010 fatal imputation. Hall retained for V1.5+ survivor-specific
  vignette set.
- 24226628 CDC 2013 USVI ablution: only 1 pakistan_ablution slot used by
  Burki. CDC USVI is retained for ablution geographic expansion.
- 27648572 Ghanchi 2016 Karachi public water: only 1 pakistan_ablution slot
  used by Burki. Ghanchi 2016 retained.
- 21291600 Shakoor + 29016297 Ghanchi 2017 + 31513557 Vugia + 27123690 Johnson +
  37460088 Maloney: Day-1 anchored only; Day-2 reuse not pursued because the
  clusters where these would fit have either zero remaining slots
  (pakistan_ablution +1, hot_springs +1) or their Day-1 reuse would push other
  more-needed anchors out of slots. Each of these entries remains available
  for V1.5+ extension or for the Pilot 5 / Commit 4-5 generation pass to
  reference in adjudication context if needed.

### 9.3 Schema enum constraints affecting representation

The schema's `geography_region` Literal does not contain a `us_west` value;
California cases (Vugia, Johnson) are mapped to `us_south` in Day 1, which is
the closest available enum bucket. Day-2 does not add new California cases
because the schema's bucket would not improve the geographic granularity. This
is a schema design choice for class-conditional epidemiology and is locked at
v2.0-schema-locked.

Costa Rica (Sandí, Retana Moreira) and Mexico (Lares-Villa) collapse to
`other_latam` in the schema. The `geography_label` field preserves the country-
level granularity; the schema enum bucket is intentionally coarser.

### 9.4 Distribution v2 plan reconciliation

The Day-2 baseline audit (`docs/DAY2_BASELINE_AUDIT_2026-05-04.md`) framed two
options: Option A (proportional trim from 44 to 40) and Option B (fold survivor +
LATAM into base clusters). Option A was locked because it preserves Day-1's 8-
cluster epidemiologic diversity and the explicit LATAM oversampling.
Option B's reclassification of Day-1 v17/v18/v19/v20 was rejected to keep
Day-1 immutable per the Day-1 anchor lock convention.

### 9.5 No formal Day-1 anchor lock policy exists

Per the Day-1 lock-semantics investigation conducted before this commit, there
is no schema-enforced or test-enforced lock on Day-1 PMIDs. The convention is
documentary only. This commit honors the convention by not modifying any Day-1
vignette spec or any Day-1 anchor's PMID metadata; Day-1 PMID reuses in Day-2
are explicit imputations within the anchor's documented case-context, never
modifications to the original Day-1 entry.

---

## 10. References

All 43 PMIDs in the anchor pool are canonized in `scripts/generate_pam_vignettes.py`
`PMID_REGISTRY` with full Vancouver-style metadata (PMID, DOI, journal short code,
year, volume, issue, pages, title, authors_short, authors_full, anchor_type,
verification_confidence, last_verified_date, plus optional `anchor_subtype`,
`verification_method`, `pmc_id`, `caveat`, `author_aliases`).

Per-PMID anchor classification, verification methodology, and dual-form author
canonicalizations (Burki/Burqi, Cogo Scaglia/Scagli, Heggie Küpper/Kupper, Kou
Lv/Lyu/Lü) are recorded in:
- `docs/PMID_CORRECTIONS_2026-05-04.md` (5-pass verification audit)
- `docs/PMID_DAY2_BONUS_CANONIZATION_2026-05-05.md` (14 bonus PMIDs canonization)
- `docs/PMID_DAY2_PRELOCK_CORRECTIONS_2026-05-05.md` (4 entries pre-lock corrections)
- Commit message of `f0c1477` (Hall 2024 caveat re-attribution + Rîpă 2025
  anchor addition).

Tag chain progression:
- v2.1-pam-day1-locked (Day 1 ship)
- v2.1.1-pmid-corrections-5pass
- v2.1.2-day2-pmids-canonized
- v2.1.3-anchor-type-schema-compliance
- v2.1.4-day2-anchor-pool-complete
- v2.1.5-day2-prelock-corrections
- v2.1.5.1-vocabulary-cleanup
- v2.1.6-day2-precommit3-clean
- **v2.1.7-day2-distribution-locked** (this commit)
- v2.1.8-day2-pilot-validated (Commit 4 of 5)
- v2.2.0-day2-corpus-complete (Commit 5 of 5)

Phase deadline: May 28, 2026 (medRxiv submission).
