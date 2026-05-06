"""Subphase 1.2 PAM vignette generator scaffolding.

Builds 20 PAM (Naegleria fowleri primary amebic meningoencephalitis) vignettes
for Day 1 of Subphase 1.2. All vignettes anchored to peer-reviewed PMIDs
verified via 4-pass plus browser confirmation per the Day 1 distribution spec.

Output: data/vignettes/pam/pam_d1_NNN_*.json (20 files)

Schema target: ml/schemas/vignette.py VignetteSchema v2.0 (Subphase 1.1 lock).
Each generated vignette validates against this schema before write.

Day 1 scope: 20 vignettes across 7 clusters with 15 distinct PMID anchors.
Day 2 (May 5) will add 40 more to hit 60-vignette spec ratios per master prompt.

Run:
    python -m scripts.generate_pam_vignettes
    python -m scripts.generate_pam_vignettes --dry-run
    python -m scripts.generate_pam_vignettes --vignette-id 1

Step C delivers scaffolding only (constants and stubs). Step D fills in the
generation logic. Step E adds tests. Step F commits.
"""
from __future__ import annotations

import argparse
import json
import logging
import sys
from pathlib import Path
from typing import Any

from pydantic import ValidationError

from ml.schemas.vignette import VignetteSchema


logger = logging.getLogger(__name__)

OUTPUT_DIR = Path("data/vignettes/pam")


# ============================================================================
# PMID_REGISTRY
# ----------------------------------------------------------------------------
# 15 distinct PMIDs that anchor the 20 Day 1 vignettes.
#
# Note on count: the Day 1 spec doc headline says "11 distinct PMIDs" but the
# per-vignette table and verification table both list 15 distinct PMIDs.
# Registry built to 15 to match the per-vignette assignments (source of truth).
# Flag this discrepancy back to the spec author for reconciliation.
#
# Each entry holds the metadata Step D needs to populate
# LiteratureAnchor + DxResult + provenance fields. Fields marked "" or None
# are intentionally empty in scaffolding; Step D fills them via PubMed lookup.
# ============================================================================

PMID_REGISTRY: dict[str, dict[str, Any]] = {
    "40146665": {
        "pmid": "40146665",
        "doi": "10.15585/mmwr.mm7410a2",
        "authors_short": "Dulski TM et al.",
        "authors_full": [
            "Dulski TM", "Montgomery F", "Ramos JM", "Rosenbaum ER",
            "Boyanton BL Jr", "Cox CM", "Dahl S", "Kitchens C", "Paul T",
            "Kahler A", "Roundtree A", "Mattioli M", "Hlavsa MC",
            "Ali IK", "Roy S", "Haston JC", "Patil N",
        ],
        "journal": "MMWR Morb Mortal Wkly Rep",
        "journal_short_code": "MMWR",
        "year": 2025,
        "volume": "74",
        "issue": "10",
        "pages": "",
        "title": "Splash pad-associated primary amebic meningoencephalitis, Pulaski County, Arkansas",
        "anchor_type": "surveillance",
        "pmc_id": "PMC11949314",
        "verification_confidence": "VERIFIED",
        "last_verified_date": "2026-05-04",
        "caveat": "",
    },
    "37470480": {
        "pmid": "37470480",
        "doi": "",
        "authors_short": "Eger L, Pence MA",
        "authors_full": ["Eger L", "Pence MA"],
        "journal": "J Clin Microbiol",
        "journal_short_code": "JCM",
        "year": 2023,
        "volume": "",
        "issue": "",
        "pages": "",
        "title": "The Brief Case: Splash pad PAM (Texas)",
        "anchor_type": "case_report",
        "pmc_id": "PMC10358179",
        "verification_confidence": "VERIFIED",
        "last_verified_date": "2026-05-04",
        "caveat": "Full text required for full demographics; abstract is brief.",
    },
    "22238170": {
        "pmid": "22238170",
        "doi": "",
        "authors_short": "Kemble SK et al.",
        "authors_full": [
            "Kemble SK", "Lynfield R", "DeVries AS", "Drehner DM",
            "Pomputius WF 3rd", "Beach MJ", "Visvesvara GS",
            "da Silva AJ", "Hill VR", "Yoder JS", "Xiao L",
            "Smith KE", "Danila R",
        ],
        "journal": "Clin Infect Dis",
        "journal_short_code": "CID",
        "year": 2012,
        "volume": "",
        "issue": "",
        "pages": "",
        "title": "Fatal Naegleria fowleri infection acquired in Minnesota: possible expanded northern range",
        "anchor_type": "case_report",
        "verification_confidence": "VERIFIED",
        "last_verified_date": "2026-05-04",
        "caveat": "",
    },
    "34307045": {
        "pmid": "34307045",
        "doi": "10.1016/j.idcr.2021.e01208",
        "authors_short": "Anjum SK et al.",
        "authors_full": [
            "Anjum SK", "Mangrola K", "Fitzpatrick G", "Stockdale K",
            "Matthias L", "Ali IKM", "Cope JR", "O'Laughlin K",
            "Collins S", "Beal SG", "Saccoccio FM",
        ],
        "journal": "IDCases",
        "journal_short_code": "IDCases",
        "year": 2021,
        "volume": "25",
        "issue": None,
        "pages": "e01208",
        "title": "A case report of primary amebic meningoencephalitis in North Florida",
        "anchor_type": "case_report",
        "anchor_subtype": "case_report_us_tap_water_north_florida",
        "pmc_id": "PMC8258632",
        "article_id": "e01208",
        "verification_confidence": 1.00,
        "last_verified_date": "2026-05-04",
        "verification_method": "user_pubmed_ui_direct_fetch",
        "caveat": (
            "US tap-water-associated PAM 2020s. Pairs with USVI ablution "
            "case (PMID 24226628) for tap-water transmission cluster "
            "adjudication. 11 authors confirmed (Saccoccio FM at end). "
            "DOI is e01208 (NOT e01218). Author 8 'O'Laughlin K' preserves "
            "apostrophe. Author 6 'Ibne Karim M Ali' renders as Vancouver "
            "'Ali IKM' (3 initials). Authors: Saad K Anjum, Karna Mangrola, "
            "Garrett Fitzpatrick, Kimberly Stockdale, Laura Matthias, "
            "Ibne Karim M Ali, Jennifer R Cope, Kevin O'Laughlin, "
            "Shelley Collins, Stacy G Beal, Frances M Saccoccio."
        ),
    },
    "37460088": {
        "pmid": "37460088",
        "doi": "10.4269/ajtmh.23-0211",
        "authors_short": "Maloney P et al.",
        "authors_full": [
            "Maloney P", "Mowrer C", "Jansen L", "Karre T", "Bedrnicek J",
            "Obaro SK", "Iwen PC", "McCutchen E", "Wetzel C",
            "Frederick J", "Ashraf MS", "Donahue M",
        ],
        "journal": "Am J Trop Med Hyg",
        "journal_short_code": "AJTMH",
        "year": 2023,
        "volume": "",
        "issue": "",
        "pages": "322-326",
        "title": "Fatal primary amebic meningoencephalitis acquired in Nebraska",
        "anchor_type": "case_report",
        "pmc_id": "PMC10397427",
        "erratum": "AJTMH 2025 Apr 2;112(4):942",
        "erratum_doi": "10.4269/ajtmh.23-0211cor",
        "erratum_pmc": "PMC11965766",
        "verification_confidence": "VERIFIED",
        "last_verified_date": "2026-05-04",
        "caveat": (
            "Pair with 2025 erratum DOI 10.4269/ajtmh.23-0211cor "
            "(AJTMH 112(4):942, PMC11965766). Erratum has no separate PMID; "
            "cite via DOI plus PMC."
        ),
    },
    "22919000": {
        "pmid": "22919000",
        "doi": "10.1093/cid/cis626",
        "authors_short": "Yoder JS et al.",
        "authors_full": [
            "Yoder JS", "Straif-Bourgeois S", "Roy SL", "Moore TA",
            "Visvesvara GS", "Ratard RC", "Hill VR", "Wilson JD",
            "Linscott AJ", "Crager R", "Kozak NA", "Sriram R",
            "Narayanan J", "Mull B", "Kahler AM", "Schneeberger C",
            "da Silva AJ", "Poudel M", "Baumgarten KL", "Xiao L",
            "Beach MJ",
        ],
        "journal": "Clin Infect Dis",
        "journal_short_code": "CID",
        "year": 2012,
        "volume": "55",
        "issue": "9",
        "pages": "e79-e85",
        "title": "Primary amebic meningoencephalitis deaths associated with sinus irrigation using contaminated tap water",
        "anchor_type": "case_report",
        "pmc_id": "PMC11307261",
        "nihmsid": "NIHMS2012368",
        "verification_confidence": "VERIFIED",
        "last_verified_date": "2026-05-04",
        "caveat": (
            "PMC11307261 is an NIHMS author-manuscript deposit posted "
            "retroactively (2024) for the 2012 paper. Publisher of record "
            "is Clin Infect Dis 2012;55(9):e79-e85, DOI 10.1093/cid/cis626."
        ),
    },
    "40440212": {
        "pmid": "40440212",
        "doi": "",
        "authors_short": "Smith et al.",
        "authors_full": [
            "Smith OA", "Tillman W", "Lewis JB", "White S", "Mattioli M",
            "Haston J", "Dorris M", "Kahler A", "Roundtree A", "Ali IK",
            "Roy S", "Yakubik T", "Sisco L", "Kunz J",
        ],
        "journal": "MMWR Morb Mortal Wkly Rep",
        "journal_short_code": "MMWR",
        "year": 2025,
        "volume": "74",
        "issue": "19",
        "pages": "334-335",
        "title": "PAM associated with RV nasal rinse, Texas",
        "anchor_type": "surveillance",
        "pmc_id": "PMC12121732",
        "verification_confidence": "VERIFIED",
        "last_verified_date": "2026-05-04",
        "caveat": (
            "5-pass verified 14 authors (NOT 13). Kunz J added as author "
            "#14 (corresponding author). Citation: MMWR 74(19):334-335."
        ),
    },
    "31513557": {
        "pmid": "31513557",
        "doi": "",
        "authors_short": "Vugia DJ et al.",
        "authors_full": [
            "Vugia DJ", "Richardson J", "Tarro T", "Vareechon C",
            "Pannaraj PS", "Traub E", "Cope JR", "Balter S",
        ],
        "journal": "MMWR Morb Mortal Wkly Rep",
        "journal_short_code": "MMWR",
        "year": 2019,
        "volume": "",
        "issue": "",
        "pages": "",
        "title": "Fatal PAM after hot-spring exposure, Inyo County California, 2018",
        "anchor_type": "surveillance",
        "pmc_id": "PMC6753969",
        "verification_confidence": "VERIFIED",
        "last_verified_date": "2026-05-04",
        "caveat": "",
    },
    "27123690": {
        "pmid": "27123690",
        "doi": "",
        "authors_short": "Johnson RO, Cope JR et al.",
        "authors_full": [
            "Johnson RO", "Cope JR", "Moskowitz M", "Kahler A", "Hill V",
            "Behrendt K", "Molina L", "Fullerton KE", "Beach MJ",
        ],
        "journal": "MMWR Morb Mortal Wkly Rep",
        "journal_short_code": "MMWR",
        "year": 2016,
        "volume": "",
        "issue": "",
        "pages": "",
        "title": "PAM associated with overland-pipe spring-fed pool, Inyo County California, 2015",
        "anchor_type": "surveillance",
        "verification_confidence": "VERIFIED",
        "last_verified_date": "2026-05-04",
        "caveat": "",
    },
    "21291600": {
        "pmid": "21291600",
        "doi": "",
        "authors_short": "Shakoor S et al.",
        "authors_full": [
            "Shakoor S", "Beg MA", "Mahmood SF", "Bandea R", "Sriram R",
            "Noman F", "Ali F", "Visvesvara GS", "Zafar A",
        ],
        "journal": "Emerg Infect Dis",
        "journal_short_code": "EID",
        "year": 2011,
        "volume": "17",
        "issue": "2",
        "pages": "258-261",
        "title": "Primary amebic meningoencephalitis caused by Naegleria fowleri, Karachi, Pakistan",
        "anchor_type": "case_report",
        "pmc_id": "PMC3204751",
        "verification_confidence": "VERIFIED",
        "last_verified_date": "2026-05-04",
        "caveat": "13-case Karachi series; ritual ablution exposure inferred (no aquatic activity).",
    },
    "29016297": {
        "pmid": "29016297",
        "doi": "",
        "authors_short": "Ghanchi NK et al.",
        "authors_full": [
            "Ghanchi NK", "Jamil B", "Khan E", "Ansar Z", "Samreen A",
            "Zafar A", "Hasan Z",
        ],
        "journal": "Am J Trop Med Hyg",
        "journal_short_code": "AJTMH",
        "year": 2017,
        "volume": "",
        "issue": "",
        "pages": "",
        "title": "Naegleria fowleri meningoencephalitis associated with public water supply, Karachi, Pakistan",
        "anchor_type": "cohort",
        "pmc_id": "PMC5817751",
        "verification_confidence": "VERIFIED",
        "last_verified_date": "2026-05-04",
        "caveat": (
            "Quote precisely: 19 PCR-confirmed cases of 116 suspected at AKU "
            "2014-2015, median age 28y, 84% male, 16% female."
        ),
    },
    "25625800": {
        "pmid": "25625800",
        "doi": "",
        "authors_short": "Abrahams-Sandí E et al.",
        "authors_full": [
            "Abrahams-Sandí E", "Retana-Moreira L", "Castro-Castillo A",
            "Reyes-Batlle M", "Lorenzo-Morales J",
        ],
        "journal": "Emerg Infect Dis",
        "journal_short_code": "EID",
        "year": 2015,
        "volume": "21",
        "issue": "2",
        "pages": "382-384",
        "title": "Naegleria fowleri meningoencephalitis from hot-spring exposure, Costa Rica",
        "anchor_type": "case_report",
        "pmc_id": "PMC4313663",
        "verification_confidence": "VERIFIED",
        "last_verified_date": "2026-05-04",
        "caveat": (
            "Used as LATAM substitute; no Peru-specific PAM PMID exists. "
            "Diacritic on Sandí preserved per 5-pass UTF-8 verification."
        ),
    },
    "8458963": {
        "pmid": "8458963",
        "doi": "",
        "authors_short": "Lares-Villa F et al.",
        "authors_full": [
            "Lares-Villa F", "De Jonckheere JF", "De Moura H",
            "Rechi-Iruretagoyena A", "Ferreira-Guerrero E",
            "Fernandez-Quintanilla G", "Ruiz-Matus C", "Visvesvara GS",
        ],
        "journal": "J Clin Microbiol",
        "journal_short_code": "JCM",
        "year": 1993,
        "volume": "31",
        "issue": "3",
        "pages": "685-688",
        "title": "Five cases of PAM in Mexicali, Mexico, plus canal-water environmental isolate",
        "anchor_type": "case_report",
        "verification_confidence": "VERIFIED",
        "last_verified_date": "2026-05-04",
        "caveat": (
            "First Mexican human N. fowleri isolations. "
            "Fernandez-Quintanilla unaccented per original 1993 JCM "
            "publication (5-pass diacritic check)."
        ),
    },
    "38526236": {
        "pmid": "38526236",
        "doi": "10.3201/eid3004.230979",
        "authors_short": "Burki AMK et al.",
        "authors_full": [
            "Burki AMK", "Satti L", "Mahboob S", "Anwar SOZ", "Bizanjo M",
            "Rafique M", "Ghanchi NK",
        ],
        "author_aliases": {
            "Burki AMK": ["Burqi AMK"],
        },
        "alias_rationale": (
            "PubMed XML indexes 'Burqi AMK' due to a transcription error "
            "propagated from the EID 'Suggested citation' field. Author's "
            "preferred surname 'Burki' confirmed by 8 of 10 authoritative "
            "sources: (1) EID byline at top of article, (2) EID author "
            "biographical note 'Dr. Burki is a consultant intensive care "
            "specialist...', (3) EID author-affiliation footer 'A.M.K. "
            "Burki', (4) Aga Khan University Scholars institutional "
            "repository, (5) author's other PubMed-indexed publication "
            "(Pak Armed Forces Med J 2023), (6) ResearchGate scientific "
            "contributions page, (7) Pakmedinet author database, (8) PMC "
            "HTML body rendering. The 'Burqi' form appears only in (a) "
            "PubMed XML index and (b) EID Suggested citation (single "
            "transcription event propagated). Canonical = Burki; alias = "
            "Burqi for search recall. Verified by user PubMed UI fetch "
            "May 4, 2026 confirming PubMed currently still indexes as "
            "'Burqi'. NLM correction not yet propagated."
        ),
        "journal": "Emerging Infectious Diseases",
        "journal_short_code": "Emerg Infect Dis",
        "year": 2024,
        "volume": "30",
        "issue": "4",
        "pages": "803-805",
        "title": "Successful Treatment of Confirmed Naegleria fowleri Primary Amebic Meningoencephalitis",
        "anchor_type": "case_report",
        "anchor_subtype": "case_report_adult_SURVIVOR_pakistan_first_pakistani_survivor",
        "pmc_id": "PMC10977850",
        "verification_confidence": 1.00,
        "last_verified_date": "2026-05-05",
        "verification_method": "research_mode_4pass_revalidated_2026-05-05",
        "caveat": (
            "22yo M Pakistan 2023, 8th confirmed N. fowleri SURVIVOR "
            "globally (1971-2023). PNS Shifa Hospital Karachi. Pairs "
            "naturally with Linam 2015 Kali Hardig (PMID 25667249) for "
            "outcome-contrast adjudication. Co-author Ghanchi NK also "
            "first author of PMID 27648572 (2016 EID Pakistan public "
            "water supply). Authors: Ahmed Mujadid Khan Burki, Luqman "
            "Satti, Saira Mahboob, Syed Onaiz Zulfiqar Anwar, Mahwash "
            "Bizanjo, Muhammad Rafique, Najia Karim Ghanchi."
        ),
    },
    "40009134": {
        "pmid": "40009134",
        "doi": "",
        "authors_short": "Rauf A, Rahiman FA, Poornima MV, Sudarsana J, Sehgal R, Ummer K",
        "authors_full": "Rauf A, Rahiman FA, Poornima MV, Sudarsana J, Sehgal R, Ummer K",
        "journal": "Indian J Pediatr",
        "journal_short_code": "IJP",
        "year": 2025,
        "volume": "",
        "issue": "",
        "pages": "",
        "title": "Pediatric PAM survivor in Kerala on early miltefosine plus adjuncts",
        "anchor_type": "case_report",
        "verification_confidence": "VERIFIED",
        "last_verified_date": "2026-05-03",
        "caveat": (
            "Author list verified via PubMed UI Pass 5: 6 authors, "
            "Sehgal R was added in Pass 5."
        ),
    },
    # ------------------------------------------------------------------------
    # Added 2026-05-04 from 4-pass verification (compass_artifact_wf-82607ea9).
    # See docs/PMID_CORRECTIONS_2026-05-04.md for full audit trail.
    # ------------------------------------------------------------------------
    "8923775": {
        "pmid": "8923775",
        "doi": None,
        "authors_short": "DeNapoli et al.",
        "authors_full": ["DeNapoli TS", "Rutman JY", "Robinson JR", "Rhodes MM"],
        "journal": "Tex Med",
        "journal_short_code": "TexMed",
        "year": 1996,
        "volume": "92",
        "issue": "10",
        "pages": "59-63",
        "title": (
            "Primary amoebic meningoencephalitis after swimming in the Rio "
            "Grande"
        ),
        "anchor_type": "case_report",
        "anchor_subtype": "case_report_pediatric_river",
        "pmc_id": None,
        "verification_confidence": 99,
        "last_verified_date": "2026-05-04",
        "caveat": (
            "Author attribution corrected from prior misrouting. NOT "
            "Lares-Villa (PMID 8458963 is the correct Lares-Villa Mexicali "
            "paper). 1996 pre-DOI era: no DOI assigned."
        ),
    },
    "26582886": {
        "pmid": "26582886",
        "doi": "10.1093/jpids/piu103",
        "authors_short": "Capewell et al.",
        "authors_full": [
            "Capewell LG", "Harris AM", "Yoder JS", "Cope JR", "Eddy BA",
            "Roy SL", "Visvesvara GS", "Fox LM", "Beach MJ",
        ],
        "journal": "J Pediatric Infect Dis Soc",
        "journal_short_code": "JPIDS",
        "year": 2015,
        "volume": "4",
        "issue": "4",
        "pages": "e68-e75",
        "title": (
            "Diagnosis, Clinical Course, and Treatment of Primary Amoebic "
            "Meningoencephalitis in the United States, 1937-2013"
        ),
        "anchor_type": "review",
        "anchor_subtype": "review_us_surveillance",
        "pmc_id": None,
        "verification_confidence": 99,
        "last_verified_date": "2026-05-04",
        "caveat": (
            "Review article (US PAM 1937-2013, approximately 140-145 cases "
            "over 76 years). PMC ID NOT confirmable - cite PMID + DOI only. "
            "Use as Tier 4 IMPUTED_FROM_LITERATURE_REVIEW anchor only. "
            "Prior PMC4622028 attribution removed (unconfirmable in any of 6 "
            "independent reference lists)."
        ),
    },
    "33350926": {
        "pmid": "33350926",
        "doi": "10.3201/eid2701.202119",
        "authors_short": "Gharpure et al.",
        "authors_full": [
            "Gharpure R", "Gleason M", "Salah Z", "Blackstock AJ",
            "Hess-Homeier D", "Yoder JS", "Ali IKM", "Collier SA", "Cope JR",
        ],
        "journal": "Emerg Infect Dis",
        "journal_short_code": "EID",
        "year": 2021,
        "volume": "27",
        "issue": "1",
        "pages": "",
        "title": (
            "Geographic Range of Recreational Water-Associated Primary "
            "Amebic Meningoencephalitis, United States, 1978-2018"
        ),
        "anchor_type": "review",
        "anchor_subtype": "review_us_geographic_range",
        "pmc_id": "PMC7774533",
        "verification_confidence": 99,
        "last_verified_date": "2026-05-04",
        "caveat": (
            "First author corrected from Cope to Gharpure. Documents "
            "northward range expansion 1978-2018."
        ),
    },
    "25595746": {
        "pmid": "25595746",
        "doi": "10.1093/cid/ciu936",
        "authors_short": "Cope et al.",
        "authors_full": [
            "Cope JR", "Ratard RC", "Hill VR", "Sokol T", "Causey JJ",
            "Yoder JS", "Mirani G", "Mull B", "Mukerjee KA", "Narayanan J",
            "Doucet M", "Qvarnstrom Y", "Poole CN", "Akingbola OA",
            "Ritter JM", "Xiong Z", "da Silva AJ", "Roellig D",
            "Van Dyke RB", "Stern H", "Xiao L", "Beach MJ",
        ],
        "journal": "Clin Infect Dis",
        "journal_short_code": "CID",
        "year": 2015,
        "volume": "",
        "issue": "",
        "pages": "",
        "title": (
            "The first association of a primary amebic meningoencephalitis "
            "death with culturable Naegleria fowleri in tap water from a US "
            "treated public drinking water system"
        ),
        "anchor_type": "case_report",
        "anchor_subtype": "case_report_treated_tap_water",
        "pmc_id": "PMC4627687",
        "verification_confidence": 99,
        "last_verified_date": "2026-05-04",
        "caveat": (
            "First reported PAM case associated with culturable N. fowleri "
            "in treated US tap water (Louisiana 2013). PMC ID confirmed "
            "PMC4627687 (NOT PMC4622028, which was the prior misattribution "
            "to Capewell 2015)."
        ),
    },
    "40697059": {
        "pmid": "40697059",
        "doi": "10.1080/14787210.2025.2536827",
        "authors_short": "Siddiqui et al.",
        "authors_full": ["Siddiqui R", "Maciver SK", "Khan NA"],
        "journal": "Expert Rev Anti Infect Ther",
        "journal_short_code": "ExpertRevAntiInfect",
        "year": 2025,
        "volume": "23",
        "issue": "9",
        "pages": "753-761",
        "title": (
            "Naegleria fowleri: emerging therapies and translational "
            "challenges"
        ),
        "anchor_type": "review",
        "anchor_subtype": "review_therapeutic_recent",
        "pmc_id": None,
        "verification_confidence": 99,
        "last_verified_date": "2026-05-04",
        "caveat": (
            "Most recent (2025) PAM therapeutic review. No PMC mirror "
            "(Taylor & Francis paywall, normal)."
        ),
    },
    "19845995": {
        "pmid": "19845995",
        "doi": "10.1017/S0950268809991014",
        "authors_short": "Yoder et al.",
        "authors_full": [
            "Yoder JS", "Eddy BA", "Visvesvara GS", "Capewell L", "Beach MJ",
        ],
        "journal": "Epidemiol Infect",
        "journal_short_code": "EpidemiolInfect",
        "year": 2010,
        "volume": "138",
        "issue": "7",
        "pages": "968-975",
        "title": (
            "The epidemiology of primary amoebic meningoencephalitis in "
            "the USA, 1962-2008"
        ),
        "anchor_type": "review",
        "anchor_subtype": "review_us_surveillance_foundational",
        "pmc_id": None,
        "verification_confidence": 99,
        "last_verified_date": "2026-05-04",
        "caveat": (
            "Foundational US PAM surveillance covering 111 cases 1962-2008."
        ),
    },
    "32369575": {
        "pmid": "32369575",
        "doi": "10.1093/cid/ciaa520",
        "authors_short": "Gharpure et al.",
        "authors_full": [
            "Gharpure R", "Bliton J", "Goodman A", "Ali IKM", "Yoder J",
            "Cope JR",
        ],
        "journal": "Clin Infect Dis",
        "journal_short_code": "CID",
        "year": 2021,
        "volume": "73",
        "issue": "1",
        "pages": "e19-e27",
        "title": (
            "Epidemiology and Clinical Characteristics of Primary Amebic "
            "Meningoencephalitis Caused by Naegleria fowleri: A Global "
            "Review"
        ),
        "anchor_type": "review",
        "anchor_subtype": "review_global",
        "pmc_id": "PMC8739754",
        "verification_confidence": 99,
        "last_verified_date": "2026-05-04",
        "caveat": (
            "Global PAM review, 381 cases 1937-2018, US 41% / Pakistan 11% "
            "/ Mexico 9%. Companion to Capewell 2015 (US-only)."
        ),
    },
    # ------------------------------------------------------------------------
    # Added 2026-05-04 from 6th-pass verification audit verification
    # (compass_artifact_wf-13eb5fad). All 6 PMIDs verified at 1.00 confidence
    # via user-side PubMed UI direct fetches. See
    # docs/PMID_DAY2_CANONIZATION_2026-05-04.md for full audit trail.
    # ------------------------------------------------------------------------
    "39606118": {
        "pmid": "39606118",
        "doi": "10.3389/fmicb.2024.1463822",
        "authors_short": "Lin L et al.",
        "authors_full": [
            "Lin L", "Luo L", "Wu M", "Chen J", "Liao Y", "Zhang H",
        ],
        "journal": "Frontiers in Microbiology",
        "journal_short_code": "Front Microbiol",
        "year": 2024,
        "volume": "15",
        "issue": None,
        "pages": "1463822",
        "title": (
            "Utilizing metagenomic next-generation sequencing and "
            "phylogenetic analysis to identify a rare pediatric case of "
            "Naegleria fowleri infection presenting with fulminant "
            "myocarditis"
        ),
        "anchor_type": "case_report",
        "anchor_subtype": "case_report_pediatric_fatal_atypical_myocarditis_indoor_pool",
        "pmc_id": "PMC11599265",
        "verification_confidence": 1.00,
        "last_verified_date": "2026-05-04",
        "verification_method": "user_pubmed_ui_direct_fetch",
        "caveat": (
            "6yo F Sichuan China, indoor heated pool 7d pre-onset April "
            "2024, fulminant myocarditis presentation, ECMO-managed, "
            "novel candidate genotype k39_3, FATAL despite AmpB + "
            "rifampin. Same index patient as Li J 2025 Front Med "
            "(PMID 40969815) field investigation companion paper. "
            "Authors: Liangkang Lin, Lili Luo, Mei Wu, Jun Chen, "
            "Yi Liao, Haiyang Zhang."
        ),
    },
    "40969815": {
        "pmid": "40969815",
        "doi": "10.3389/fmed.2025.1623909",
        "authors_short": "Li J et al.",
        "authors_full": [
            "Li J", "Feng S", "Wang Y", "Li C", "Li P", "Zhang L",
            "Dai Y", "Tan K", "Wang L",
        ],
        "journal": "Frontiers in Medicine",
        "journal_short_code": "Front Med (Lausanne)",
        "year": 2025,
        "volume": "12",
        "issue": None,
        "pages": "1623909",
        "title": (
            "A primary amoebic meningoencephalitis case suspected to be "
            "infected by indoor swimming, China, 2024"
        ),
        "anchor_type": "surveillance",
        "anchor_subtype": "epi_field_investigation_pediatric_fatal_indoor_pool",
        "pmc_id": "PMC12440956",
        "verification_confidence": 1.00,
        "last_verified_date": "2026-05-04",
        "verification_method": "user_pubmed_ui_direct_fetch",
        "caveat": (
            "Same April 2024 6yo Chengdu index patient as Lin et al. "
            "2024 Front Microbiol myocarditis paper (PMID 39606118). "
            "This is the Chengdu CDC field investigation. Death 7 days "
            "after symptom onset. Authors: Junfan Li (equal contrib), "
            "Songqi Feng (equal contrib), Yao Wang, Chao Li, Peng Li, "
            "Lijie Zhang, Yingxue Dai, Kaike Tan, Liang Wang."
        ),
    },
    "32752181": {
        "pmid": "32752181",
        "doi": "10.3390/pathogens9080629",
        "authors_short": "Retana Moreira L et al.",
        "authors_full": [
            "Retana Moreira L", "Zamora Rojas L", "Grijalba Murillo M",
            "Molina Castro SE", "Abrahams Sandí E",
        ],
        "journal": "Pathogens",
        "journal_short_code": "Pathogens",
        "year": 2020,
        "volume": "9",
        "issue": "8",
        "pages": "629",
        "title": (
            "Primary Amebic Meningoencephalitis Related to Groundwater "
            "in Costa Rica: Diagnostic Confirmation of Three Cases and "
            "Environmental Investigation"
        ),
        "anchor_type": "case_report",
        "anchor_subtype": "case_series_environmental_groundwater_central_america",
        "pmc_id": "PMC7459727",
        "verification_confidence": 1.00,
        "last_verified_date": "2026-05-04",
        "verification_method": "user_pubmed_ui_direct_fetch",
        "caveat": (
            "3 Costa Rica cases first trimester 2020. One survivor "
            "among the three (per Frontiers 2025 PMC12089049). "
            "Diacritic preservation: 'Sandí' (UTF-8 c3 ad). Author "
            "surnames are unhyphenated compound surnames in publication "
            "form (Retana Moreira, Abrahams Sandí). NOT 'Retana-Moreira' "
            "or 'Abrahams-Sandí'. Some downstream Spanish-language "
            "reviews re-hyphenate; preserve un-hyphenated PubMed "
            "canonical form. Authors: Lissette Retana Moreira, Leidy "
            "Zamora Rojas, Muriel Grijalba Murillo, Silvia Elena Molina "
            "Castro, Elizabeth Abrahams Sandí."
        ),
    },
    "35463884": {
        "pmid": "35463884",
        "doi": "10.3389/fped.2022.785735",
        "authors_short": "Zhou W et al.",
        "authors_full": [
            "Zhou W", "Ouyang Y", "Zhang D", "Liao S", "Liang H",
            "Zhao L", "Chen C",
        ],
        "journal": "Frontiers in Pediatrics",
        "journal_short_code": "Front Pediatr",
        "year": 2022,
        "volume": "10",
        "issue": None,
        "pages": "785735",
        "title": (
            "Case Report and Literature Review: Bacterial "
            "Meningoencephalitis or Not? Naegleria fowleri Related "
            "Primary Amoebic Meningoencephalitis in China"
        ),
        "anchor_type": "case_report",
        "anchor_subtype": "case_report_pediatric_fatal_misdiagnosis_as_bacterial_meningitis",
        "pmc_id": "PMC9033202",
        "verification_confidence": 1.00,
        "last_verified_date": "2026-05-05",
        "verification_method": "research_mode_4pass_revalidated_2026-05-05",
        "caveat": (
            "Pediatric case + literature review. Strong "
            "physician-adjudicator anchor for misdiagnosis-as-bacterial-"
            "meningitis differential. Geography corrected 2026-05-05 "
            "via verification audit (compass_artifact_wf-c3f74c5c): "
            "Changsha, Hunan Province, China (Third Xiangya Hospital, "
            "Central South University); NOT Hainan. Hainan is the "
            "tropical island province in South China Sea; Hunan is a "
            "landlocked central-China province; distinct geographies. "
            "Sources confirming Hunan/Changsha: PubMed affiliations, "
            "PMC9033202 body text, Frontiers article page. 7 authors "
            "confirmed (NOT 6 as initially inferred from snippets). "
            "Authors: Wenjuan Zhou, Yuzhen Ouyang, Di Zhang, Sheng "
            "Liao, Hui Liang, Lingling Zhao, Chunyuan Chen."
        ),
    },
    "34906097": {
        "pmid": "34906097",
        "doi": "10.1186/s12879-021-06932-9",
        "authors_short": "Huang S et al.",
        "authors_full": [
            "Huang S", "Liang X", "Han Y", "Zhang Y", "Li X", "Yang Z",
        ],
        "journal": "BMC Infectious Diseases",
        "journal_short_code": "BMC Infect Dis",
        "year": 2021,
        "volume": "21",
        "issue": "1",
        "pages": "1251",
        "title": (
            "A pediatric case of primary amoebic meningoencephalitis "
            "due to Naegleria fowleri diagnosed by next-generation "
            "sequencing of cerebrospinal fluid and blood samples"
        ),
        "anchor_type": "case_report",
        "anchor_subtype": "case_report_pediatric_fatal_mNGS_dual_compartment_china",
        "pmc_id": "PMC8670243",
        "verification_confidence": 1.00,
        "last_verified_date": "2026-05-04",
        "verification_method": "user_pubmed_ui_direct_fetch",
        "caveat": (
            "China pediatric mNGS dual-compartment positivity (CSF + "
            "blood, rare blood positivity). Authors 1+2 contributed "
            "equally. Author 'Xiu'an Liang' contains apostrophe in "
            "given name (UTF-8 preserved); Vancouver renders as "
            "'Liang X'. Authors: Shiqin Huang, Xiu'an Liang, Yunli "
            "Han, Yanyan Zhang, Xinhui Li, Zhiyong Yang."
        ),
    },
    "33381798": {
        "pmid": "33381798",
        "doi": "10.1093/tropej/fmaa100",
        "authors_short": "Celik Y, Arslankoylu AE",
        "authors_full": ["Celik Y", "Arslankoylu AE"],
        "journal": "Journal of Tropical Pediatrics",
        "journal_short_code": "J Trop Pediatr",
        "year": 2021,
        "volume": "67",
        "issue": "1",
        "pages": "fmaa100",
        "publication_date": "2021-01-29",
        "title": "A Newborn with Brain-Eating Ameba Infection",
        "anchor_type": "case_report",
        "anchor_subtype": "case_report_newborn_fatal_extreme_age_atypical",
        "pmc_id": None,
        "verification_confidence": 1.00,
        "last_verified_date": "2026-05-05",
        "verification_method": "user_pubmed_ui_direct_fetch_2026-05-05",
        "caveat": (
            "NEWBORN with brain-eating amoeba (extreme age "
            "presentation). Tests differential diagnosis at age "
            "extremes. Issue corrected 2026-05-05 via PubMed UI direct "
            "fetch: J Trop Pediatr 2021 Jan 29;67(1):fmaa100 (NOT "
            "issue 2). Authors: Yalcin Celik, Ali Ertuğ Arslankoylu. "
            "Diacritic preservation: 'Ertuğ' (UTF-8 c4 9f for ğ) - "
            "given name only, collapses to initial in Vancouver."
        ),
    },
    # ------------------------------------------------------------------------
    # Added 2026-05-05 from Commit 2 of 5 sequential safe path.
    # Methodology mix: 11 research_mode_4pass + 3
    # user_pubmed_ui_direct_fetch (Cogo, Heggie, Kou - high-risk dual-form).
    # Source: compass_artifact_wf-313f302a-5956-4f61-b5c3-c116819753df
    # Audit trail: docs/PMID_DAY2_BONUS_CANONIZATION_2026-05-05.md
    # ------------------------------------------------------------------------
    "39795618": {
        "pmid": "39795618",
        "doi": "10.3390/diagnostics15010089",
        "authors_short": "Phung NTN et al.",
        "authors_full": [
            "Phung NTN", "Pham HT", "Tran TT", "Dinh VH", "Tran NM",
            "Tran NAN", "Ngo MQN", "Nguyen HTT", "Tran DK", "Le TKT",
            "Quek C", "Pham VH", "Pham ST",
        ],
        "journal": "Diagnostics (Basel)",
        "journal_short_code": "Diagnostics",
        "year": 2025,
        "volume": "15",
        "issue": "1",
        "pages": "89",
        "title": "Naegleria fowleri: Portrait of a Cerebral Killer",
        "anchor_type": "case_report",
        "anchor_subtype": "asia_vietnam_cryptic_pediatric_fatal_prolonged_survival",
        "pmc_id": "PMC11719733",
        "verification_confidence": 1.00,
        "last_verified_date": "2026-05-05",
        "verification_method": "research_mode_4pass_plus_user_mdpi_fulltext_2026-05-05",
        "caveat": (
            "10mo F Mekong Delta Vietnam, FATAL: 14 days from disease "
            "onset, 11 days hospitalization (Section 2 Case "
            "Presentation: 'passed away after 11 days of "
            "hospitalization'; Section 3 Discussion: 'passed away 14 "
            "days after disease onset'); intensive treatment yielded "
            "longest pediatric PAM survival durations on record. "
            "MPL-rPCR + microscopy + sequencing diagnosis. Cryptic "
            "exposure (no documented direct freshwater exposure). 13 "
            "authors. Vietnamese compound surnames preserved "
            "un-hyphenated per PubMed XML (Tran NAN = Nuong Ai Nguyen "
            "Tran; Ngo MQN = Minh Quang Ngoc Ngo). Authors: Nguyen The "
            "Nguyen Phung, Huong Thien Pham, Thuc Thanh Tran, Vu Hoang "
            "Dinh, Nhut Minh Tran, Nuong Ai Nguyen Tran, Minh Quang "
            "Ngoc Ngo, Huong Thanh Thi Nguyen, Duy Khanh Tran, Thao "
            "Kieu Thi Le, Camelia Quek, Van Hung Pham, Son Truong "
            "Pham."
        ),
    },
    "30055569": {
        "pmid": "30055569",
        "doi": "10.1186/s12879-018-3261-z",
        "authors_short": "Wang Q et al.",
        "authors_full": [
            "Wang Q", "Li J", "Ji J", "Yang L", "Chen L", "Zhou R",
            "Yang Y", "Zheng H", "Yuan J", "Li L", "Bi Y", "Gao GF",
            "Ma J", "Liu Y",
        ],
        "journal": "BMC Infectious Diseases",
        "journal_short_code": "BMC Infect Dis",
        "year": 2018,
        "volume": "18",
        "issue": "1",
        "pages": "349",
        "title": "A case of Naegleria fowleri related primary amoebic meningoencephalitis in China diagnosed by next-generation sequencing",
        "anchor_type": "case_report",
        "anchor_subtype": "asia_china_first_mainland_NGS_diagnosis_fatal",
        "pmc_id": "PMC6064090",
        "verification_confidence": 1.00,
        "last_verified_date": "2026-05-05",
        "verification_method": "research_mode_4pass",
        "caveat": (
            "42yo M Shenzhen Third People's Hospital (acquired Hangzhou); "
            "first reported mainland China PAM case; FATAL; NGS "
            "diagnosed. 14 authors including Gao GF (George F. Gao, "
            "CCDC Director-General). Author 14 'Liu Y' = Yingxia Liu "
            "(single Liu in this paper, no disambiguation needed). "
            "Authors: Qiang Wang, Jianming Li, Jingkai Ji, Liuqing Yang, "
            "Li Chen, Rongrong Zhou, Yang Yang, Haixia Zheng, Jing Yuan, "
            "Liqiang Li, Yuhai Bi, George F. Gao, Jinmin Ma, Yingxia Liu."
        ),
    },
    "39174030": {
        "pmid": "39174030",
        "doi": "10.3201/eid3009.231604",
        "authors_short": "Wei HY et al.",
        "authors_full": [
            "Wei HY", "Lai YW", "Li SY", "Lee YI", "Hu MK", "Ji DD",
            "Su CP",
        ],
        "journal": "Emerging Infectious Diseases",
        "journal_short_code": "Emerg Infect Dis",
        "year": 2024,
        "volume": "30",
        "issue": "9",
        "pages": "1922-1925",
        "title": "Fatal Case of Naegleria fowleri Primary Amebic Meningoencephalitis from Indoor Surfing Center, Taiwan, 2023",
        "anchor_type": "case_report",
        "anchor_subtype": "asia_taiwan_indoor_surfing_recreational_fatal",
        "pmc_id": "PMC11346987",
        "verification_confidence": 1.00,
        "last_verified_date": "2026-05-05",
        "verification_method": "research_mode_4pass",
        "caveat": (
            "30yo F northern Taiwan, indoor surfing center July 2023, "
            "symptom onset 26 Jul 2023, died 1 Aug 2023; first Taiwan "
            "PAM in 12 years (since Su et al. 2013 PMID 23710088). 7 "
            "authors. Author 7 'Su CP' rendered Chia-ping Su (lowercase "
            "p) in publisher byline; PubMed normalizes to Su CP. "
            "Authors: Hsin-Yi Wei, Yi-Wen Lai, Shu-Ying Li, Yen-I Lee, "
            "Meng-Kai Hu, Da-Der Ji, Chia-ping Su."
        ),
    },
    "37727924": {
        "pmid": "37727924",
        "doi": "10.3349/ymj.2023.0189",
        "authors_short": "Hong KW et al.",
        "authors_full": [
            "Hong KW", "Jeong JH", "Byun JH", "Hong SH", "Ju JW", "Bae IG",
        ],
        "journal": "Yonsei Medical Journal",
        "journal_short_code": "Yonsei Med J",
        "year": 2023,
        "volume": "64",
        "issue": "10",
        "pages": "641-645",
        "title": "Fatal Primary Amebic Meningoencephalitis Due to Naegleria fowleri: The First Imported Case in Korea",
        "anchor_type": "case_report",
        "anchor_subtype": "asia_korea_imported_thailand_travel_fatal",
        "pmc_id": "PMC10522881",
        "verification_confidence": 1.00,
        "last_verified_date": "2026-05-05",
        "verification_method": "research_mode_4pass",
        "caveat": (
            "Korean man in 50s, 4-month Thailand stay, returned Korea "
            "10 Dec 2022, symptoms began evening of arrival, admitted "
            "11 Dec, died 21 Dec 2022 (13d post-onset); first imported "
            "PAM case in Korea; KDCA-confirmed 99.6% genetic match to "
            "overseas PAM strain. atypical_type=travel_imported_lake. "
            "6 authors with hyphenated Korean given names (Kyung-Wook, "
            "Jong-Hwan, Jung-Hyun, Sung-Hee, Jung-Won, In-Gyu). "
            "Authors: Kyung-Wook Hong, Jong Hwan Jeong, Jung-Hyun "
            "Byun, Sung-Hee Hong, Jung-Won Ju, In-Gyu Bae."
        ),
    },
    "15504272": {
        "pmid": "15504272",
        "doi": "10.3201/eid1010.040273",
        "authors_short": "Cogo PE et al.",
        "authors_full": [
            "Cogo PE", "Scaglia M", "Gatti S", "Rossetti F", "Alaggio R",
            "Laverda AM", "Zhou L", "Xiao L", "Visvesvara GS",
        ],
        "author_aliases": {
            "Scaglia M": ["Scagli M"],
        },
        "alias_rationale": (
            "PubMed XML truncates author 2 surname mid-string ('Scaglia' "
            "-> 'Scagli'; trailing 'a' lost in early NLM ingest of this "
            "2004 dispatch). Canonical 'Scaglia M' confirmed by: (1) CDC "
            "EID publisher byline at top of article 'Massimo Scaglia + "
            "University-IRCCS S. Matteo, Pavia, Italy', (2) PMC3323261 "
            "full-text rendering, (3) Massimo Scaglia documented "
            "researcher with prior Naegleria papers (PMID 3587066 "
            "Microbiologica 1987, Trans R Soc Trop Med Hyg 1983, Exp "
            "Parasitol 1989), (4) Padova/Pavia institutional records. "
            "PubMed UI fetch 2026-05-05 confirmed 'Scagli M' truncation "
            "persists in NLM index. Verified user_pubmed_ui_direct_fetch "
            "on this entry to lock the dual-form decision."
        ),
        "journal": "Emerging Infectious Diseases",
        "journal_short_code": "Emerg Infect Dis",
        "year": 2004,
        "volume": "10",
        "issue": "10",
        "pages": "1835-1837",
        "title": "Fatal Naegleria fowleri meningoencephalitis, Italy",
        "anchor_type": "case_report",
        "anchor_subtype": "europe_italy_first_european_pediatric_genotype1_fatal",
        "pmc_id": "PMC3323261",
        "verification_confidence": 1.00,
        "last_verified_date": "2026-05-05",
        "verification_method": "user_pubmed_ui_direct_fetch",
        "caveat": (
            "9yo immunocompetent boy Italy (Veneto/Padova region, "
            "admitted Este hospital); swam in polluted Po River water "
            "hole July 2003 ~10d pre-onset; FIRST documented Italian "
            "PAM case; postmortem dx by IIF + histology; N. fowleri "
            "genotype I (genotype 1) by PCR; FATAL. 9 authors. NLM "
            "truncation artifact: PubMed XML shows 'Scagli M' but "
            "canonical published byline = 'Scaglia M' (Massimo "
            "Scaglia, University-IRCCS S. Matteo, Pavia). Authors: "
            "Paola E. Cogo, Massimo Scaglia, Simonetta Gatti, Flavio "
            "Rossetti, Rita Alaggio, Anna Maria Laverda, Ling Zhou, "
            "Lihua Xiao, Govinda S. Visvesvara."
        ),
    },
    "31734864": {
        "pmid": "31734864",
        "doi": "10.1007/s00436-019-06463-y",
        "authors_short": "Sazzad HMS et al.",
        "authors_full": [
            "Sazzad HMS", "Luby SP", "Sejvar J", "Rahman M", "Gurley ES",
            "Hill V", "Murphy JL", "Roy S", "Cope JR", "Ali IKM",
        ],
        "journal": "Parasitology Research",
        "journal_short_code": "Parasitol Res",
        "year": 2020,
        "volume": "119",
        "issue": "1",
        "pages": "339-344",
        "title": "A case of primary amebic meningoencephalitis caused by Naegleria fowleri in Bangladesh",
        "anchor_type": "case_report",
        "anchor_subtype": "south_asia_bangladesh_first_nasal_rinsing_groundwater_fatal",
        "pmc_id": None,
        "verification_confidence": 1.00,
        "last_verified_date": "2026-05-05",
        "verification_method": "research_mode_4pass",
        "caveat": (
            "15yo M Bangladesh; daily nasal rinsing with untreated "
            "groundwater + bathing in untreated groundwater/river water; "
            "FATAL <6 days post-onset; first recognized Bangladesh PAM "
            "case. 10 authors ending Cope JR, Ali IKM. No PMC mirror "
            "(Springer paywall, expected). Authors: Hossain M.S. Sazzad, "
            "Stephen P. Luby, James Sejvar, Mahmudur Rahman, Emily S. "
            "Gurley, Vincent Hill, Jennifer L. Murphy, Shantanu Roy, "
            "Jennifer R. Cope, Ibne K.M. Ali."
        ),
    },
    "36046566": {
        "pmid": "36046566",
        "doi": "10.18502/ijpa.v17i1.9015",
        "authors_short": "Aurongzeb M et al.",
        "authors_full": [
            "Aurongzeb M", "Rashid Y", "Naqvi SHA", "Khatoon A",
            "Haq SA", "Azim MK", "Kaleem I", "Bashir S",
        ],
        "journal": "Iranian Journal of Parasitology",
        "journal_short_code": "Iran J Parasitol",
        "year": 2022,
        "volume": "17",
        "issue": "1",
        "pages": "43-52",
        "title": "Naegleria fowleri from Pakistan Has Type-2 Genotype",
        "anchor_type": "case_report",
        "anchor_subtype": "south_asia_pakistan_karachi_ablution_genotype2_first",
        "pmc_id": "PMC9375727",
        "verification_confidence": 1.00,
        "last_verified_date": "2026-05-05",
        "verification_method": "research_mode_4pass",
        "caveat": (
            "28yo Karachi Pakistan May 2019 (Imam Zain-Ul-Abdin "
            "Hospital); ablution exposure; FIRST Pakistani N. fowleri "
            "characterized as type-2 (genotype 2). 8 authors. DISTINCT "
            "from Aurongzeb M et al. Sci Rep 2022;12 mitochondrial "
            "genome paper (PMID 35909191, DOI 10.1038/s41598-022-17006-4) "
            "- co-temporal but separate works. Authors: Muhammad "
            "Aurongzeb, Yasmeen Rashid, Syed Habib Ahmed Naqvi, Ambrina "
            "Khatoon, Sadia Abdul Haq, Mohammad Kamran Azim, Imdad "
            "Kaleem, Shahid Bashir."
        ),
    },
    "24226628": {
        "pmid": "24226628",
        "doi": None,
        "authors_short": "Centers for Disease Control and Prevention (CDC)",
        "authors_full": ["Centers for Disease Control and Prevention (CDC)"],
        "journal": "MMWR Morbidity and Mortality Weekly Report",
        "journal_short_code": "MMWR Morb Mortal Wkly Rep",
        "year": 2013,
        "volume": "62",
        "issue": "45",
        "pages": "903",
        "title": "Notes from the field: primary amebic meningoencephalitis associated with ritual nasal rinsing--St. Thomas, U.S. Virgin islands, 2012",
        "anchor_type": "case_report",
        "anchor_subtype": "americas_usvi_caribbean_ablution_nasal_rinsing_tap_water_fatal",
        "pmc_id": "PMC4585351",
        "verification_confidence": 1.00,
        "last_verified_date": "2026-05-05",
        "verification_method": "research_mode_4pass",
        "caveat": (
            "47yo M U.S. Virgin Islands St. Thomas; only freshwater "
            "exposure was tap water for daily household activities + "
            "Islamic ablution (ritual cleansing including nasal "
            "rinsing); FATAL Nov 21 2012; first PAM death in USVI "
            "territory; environmental investigation found untreated "
            "groundwater well + untreated rainwater cistern as "
            "household water sources. Pre-DOI MMWR Notes from Field, "
            "no DOI expected. PubMed byline: corporate single author "
            "'Centers for Disease Control and Prevention (CDC)'. "
            "Longer companion report at PMC4585351. Pairs with Anjum "
            "2021 N Florida (PMID 34307045) for tap-water transmission "
            "cluster adjudication."
        ),
    },
    "27648572": {
        "pmid": "27648572",
        "doi": "10.3201/eid2210.151236",
        "authors_short": "Ghanchi NK et al.",
        "authors_full": [
            "Ghanchi NK", "Khan E", "Khan A", "Muhammad W", "Malik FR",
            "Zafar A",
        ],
        "journal": "Emerging Infectious Diseases",
        "journal_short_code": "Emerg Infect Dis",
        "year": 2016,
        "volume": "22",
        "issue": "10",
        "pages": "1835-1837",
        "title": "Naegleria fowleri Meningoencephalitis Associated with Public Water Supply, Pakistan, 2014",
        "anchor_type": "case_report",
        "anchor_subtype": "south_asia_pakistan_karachi_public_water_supply_AKU",
        "pmc_id": "PMC5038392",
        "verification_confidence": 1.00,
        "last_verified_date": "2026-05-05",
        "verification_method": "research_mode_4pass",
        "caveat": (
            "EID Letter (no abstract). 6 authors. DISTINCT from "
            "Ghanchi 2017 AJTMH case series (PMID 29016297) already in "
            "registry - different author roster (2017 = Ghanchi NK, "
            "Jamil B, Khan E, Ansar Z, Samreen A, Zafar A, Hasan Z; "
            "2016 = this entry). Aga Khan University + Karachi Water "
            "and Sewerage Board + WHO Karachi affiliations. Authors: "
            "Najia K. Ghanchi, Erum Khan, Azam Khan, Wali Muhammad, "
            "Faisal Riaz Malik, Afia Zafar."
        ),
    },
    "25667249": {
        "pmid": "25667249",
        "doi": "10.1542/peds.2014-2292",
        "authors_short": "Linam WM et al.",
        "authors_full": [
            "Linam WM", "Ahmed M", "Cope JR", "Chu C", "Visvesvara GS",
            "da Silva AJ", "Qvarnstrom Y", "Green J",
        ],
        "journal": "Pediatrics",
        "journal_short_code": "Pediatrics",
        "year": 2015,
        "volume": "135",
        "issue": "3",
        "pages": "e744-e748",
        "title": "Successful Treatment of an Adolescent With Naegleria fowleri Primary Amebic Meningoencephalitis",
        "anchor_type": "case_report",
        "anchor_subtype": "americas_usa_arkansas_third_north_american_survivor_miltefosine_hypothermia",
        "pmc_id": "PMC4634363",
        "verification_confidence": 1.00,
        "last_verified_date": "2026-05-05",
        "verification_method": "research_mode_4pass",
        "caveat": (
            "12yo F (Kali Hardig); Willow Springs Water Park Arkansas "
            "July 2013; SURVIVED with combination antimicrobials "
            "(including miltefosine) + therapeutic hypothermia + ICP "
            "management on TBI principles; THIRD documented North "
            "American PAM survivor. 8 authors; preserve lowercase 'da' "
            "particle in 'da Silva AJ' per PubMed XML. Definitive case "
            "report subsequently invoked by Linam-Cope letter of "
            "concern PMID 28501613 against Heggie/Küpper PMID "
            "28013053. Pairs with Burki 2024 Pakistan SURVIVOR (PMID "
            "38526236) for outcome-contrast adjudication. Authors: W. "
            "Matthew Linam, Mubbasheer Ahmed, Jennifer R. Cope, Craig "
            "Chu, Govinda S. Visvesvara, Alexandre J. da Silva, Yvonne "
            "Qvarnstrom, Jerril Green."
        ),
    },
    "28013053": {
        "pmid": "28013053",
        "doi": "10.1016/j.tmaid.2016.12.005",
        "authors_short": "Heggie TW, Küpper T",
        "authors_full": ["Heggie TW", "Küpper T"],
        "author_aliases": {
            "Küpper T": ["Kupper T"],
        },
        "alias_rationale": (
            "Author 2 surname Küpper preserves UTF-8 ü (U+00FC, c3 bc) "
            "per PubMed XML and ScienceDirect publisher byline. PubMed "
            "UI fetch 2026-05-05 confirmed: search URL itself contains "
            "URL-encoded 'K%C3%BCpper' confirming UTF-8 preservation in "
            "NLM index. Multiple downstream citations strip diacritic "
            "to 'Kupper T' (CDC PMC6112607 Linam letter of concern, "
            "BMC Infect Dis Wang 2018 reference list, ResearchGate "
            "metadata, Acta Parasitologica). Canonical = 'Küpper T' "
            "(preserve diacritic verbatim per PubMed XML and Travel "
            "Med Infect Dis publisher byline); alias = 'Kupper T' for "
            "downstream search recall. Verified user_pubmed_ui_direct_"
            "fetch on this entry to lock dual-form decision."
        ),
        "journal": "Travel Medicine and Infectious Disease",
        "journal_short_code": "Travel Med Infect Dis",
        "year": 2017,
        "volume": "16",
        "issue": None,
        "pages": "49-51",
        "title": "Surviving Naegleria fowleri infections: A successful case report and novel therapeutic approach",
        "anchor_type": "case_report",
        "anchor_subtype": "americas_usa_third_survivor_secondary_report_subject_of_letter_of_concern",
        "pmc_id": None,
        "verification_confidence": 1.00,
        "last_verified_date": "2026-05-05",
        "verification_method": "user_pubmed_ui_direct_fetch",
        "caveat": (
            "2 authors. UTF-8 dual-form (Burki/Burqi pattern, Option "
            "3): canonical 'Küpper T' with U+00FC ü preserved per "
            "PubMed XML and ScienceDirect publisher byline. "
            "Affiliations: Bowling Green State University (Heggie); "
            "RWTH Aachen Technical University Institute of "
            "Occupational and Social Medicine (Küpper). Subject of "
            "Linam-Cope letter of concern PMID 28501613 (already in "
            "registry); response is Heggie 2017 PMID 29241583 (this "
            "commit). Authors: Travis W. Heggie, Thomas Küpper."
        ),
    },
    "29241583": {
        "pmid": "29241583",
        "doi": "10.1016/j.tmaid.2017.11.010",
        "authors_short": "Heggie TW",
        "authors_full": ["Heggie TW"],
        "journal": "Travel Medicine and Infectious Disease",
        "journal_short_code": "Travel Med Infect Dis",
        "year": 2017,
        "volume": "20",
        "issue": None,
        "pages": "66",
        "title": "Surviving Naegleria fowleri infections: Response",
        "anchor_type": "case_report",
        "anchor_subtype": "americas_usa_response_to_letter_of_concern_linam_chain_completion",
        "pmc_id": None,
        "verification_confidence": 1.00,
        "last_verified_date": "2026-05-05",
        "verification_method": "research_mode_4pass",
        "caveat": (
            "Closes the Linam 3-chain: (a) Linam 2015 PMID 25667249 "
            "-> (b) Heggie & Küpper 2017 PMID 28013053 -> (c) "
            "Linam-Cope LoC 2017 PMID 28501613 (already in registry) "
            "-> (d) Heggie 2017 Response PMID 29241583 (this entry). "
            "Sole author Heggie - Küpper not co-signing the response. "
            "Authors: Travis W. Heggie."
        ),
    },
    "38182931": {
        "pmid": "38182931",
        "doi": "10.1007/s00436-023-08094-w",
        "authors_short": "Hall AD et al.",
        "authors_full": [
            "Hall AD", "Kumar JE", "Golba CE", "Luckett KM", "Bryant WK",
        ],
        "journal": "Parasitology Research",
        "journal_short_code": "Parasitol Res",
        "year": 2024,
        "volume": "123",
        "issue": "1",
        "pages": "84",
        "title": "Primary amebic meningoencephalitis: a review of Naegleria fowleri and analysis of successfully treated cases",
        "anchor_type": "review",
        "anchor_subtype": "review_survivor_analysis_university_of_cincinnati_2024",
        "pmc_id": None,
        "verification_confidence": 1.00,
        "last_verified_date": "2026-05-05",
        "verification_method": "research_mode_4pass_plus_user_pubmed_ui_caveat_reattribution_2026-05-05",
        "caveat": (
            "5-author review (Parasitol Res 123(1):84, 2024) analyzing successfully "
            "treated PAM cases globally. Focuses on the small subset of confirmed "
            "survivors and their treatment regimens (miltefosine + amphotericin B + "
            "hypothermia combinations). NOT a 98-patient demographic cohort - that "
            "figure originates from Ripa 2025 (PMID 39860533, J Clin Med 14(2):526). "
            "Authors: Ashton D Hall, Julia E Kumar, Claire E Golba, Keith M Luckett, "
            "Whitney K Bryant. Caveat re-attributed 2026-05-05 via verification audit."
        ),
    },
    "39860533": {
        "pmid": "39860533",
        "lead_author": "Rîpă",
        "lead_author_ascii": "Ripa",
        "authors_short": "Rîpă C, Cobzaru RG, Rîpă MR, Maștaleru A, Oancea A, Cumpăt CM, Leon MM",
        "authors_full": [
            "Rîpă C",
            "Cobzaru RG",
            "Rîpă MR",
            "Maștaleru A",
            "Oancea A",
            "Cumpăt CM",
            "Leon MM",
        ],
        "author_count": 7,
        "doi": "10.3390/jcm14020526",
        "journal": "Journal of Clinical Medicine",
        "journal_short_code": "J Clin Med",
        "year": 2025,
        "volume": "14",
        "issue": "2",
        "pages": "526",
        "publication_date": "2025-01-15",
        "title": "Naegleria fowleri Infections: Bridging Clinical Observations and Epidemiological Insights",
        "anchor_type": "review",
        "anchor_subtype": "review_systematic_global_98patient_cohort",
        "pmc_id": "PMC11765897",
        "verification_confidence": 1.00,
        "last_verified_date": "2026-05-05",
        "verification_method": "user_pubmed_ui_direct_fetch_plus_user_mdpi_fulltext_2026-05-05",
        "caveat": (
            "7-author Romanian systematic review (Iasi, Univ Med & Pharmacy "
            "Grigore T. Popa) of 52 PAM case-report articles via Web of Science "
            "search. Abstract reports 98 patients (17 women 17.4%, 81 men "
            "82.6%) from 17 countries: 17 USA, 8 India, 7 China, 4 Pakistan, "
            "2 UK, plus 1 each from Thailand/Korea/Japan/Italy/Iran/Norway/"
            "Turkey/Costa Rica/Zambia/Australia/Taiwan/Venezuela/Mexico. "
            "Mortality reported at 88-98% across discussion. Note: results "
            "section internally reports 99 patients (17F/82M = 17.17%/82.82%) "
            "diverging slightly from abstract's 98 (17F/81M); use abstract "
            "figures as canonical for vignette anchoring. UTF-8 diacritics "
            "preserved: Rîpă (î U+00EE, ă U+0103), Maștaleru (ș U+0219), "
            "Cumpăt (ă U+0103). Anchor for global epidemiology + demographics "
            "Tier-4 vignettes. Replaces mis-attributed 98-patient stat "
            "previously in Hall 2024 caveat (corrected 2026-05-05)."
        ),
    },
    "40676680": {
        "pmid": "40676680",
        "doi": "10.1186/s40249-025-01347-z",
        "authors_short": "Kou Y et al.",
        "authors_full": [
            "Kou Y", "Zhang J", "Wang D", "Cui L", "Sun Q", "Lv Y",
            "Liu Y", "He Z", "Zhao Y", "Zhang H", "Su J", "Liu Y",
            "Deng Y",
        ],
        "author_aliases": {
            "Lv Y": ["Lyu Y", "Lü Y"],
        },
        "alias_rationale": (
            "Author 6 'Lv Y' = Yanqi Lv (PubMed/Springer canonical "
            "romanization of the Chinese surname). PubMed UI fetch "
            "2026-05-05 confirmed canonical 'Lv Y' (no umlaut) in NLM "
            "author byline. Intra-paper acknowledgment paragraph uses "
            "umlaut form 'Yanqi Lü' (U+00FC); occasional 'Lyu Y' "
            "pinyin variant in some Springer prose. Soft dual-form: "
            "canonical 'Lv Y' (PubMed XML), aliases 'Lyu Y' and 'Lü Y' "
            "for search recall. Lower-stakes than Burki/Burqi or "
            "Scaglia/Scagli decisions but worth recording. NOTE: Two "
            "'Liu Y' co-authors at positions 7 and 12 (Vancouver "
            "positional convention - render twice): position 7 = Ying "
            "Liu (Henan CDC); position 12 = Yaobao Liu (Jiangsu "
            "Institute of Parasitic Diseases / Nanjing Medical "
            "University SPH; corresponding author)."
        ),
        "journal": "Infectious Diseases of Poverty",
        "journal_short_code": "Infect Dis Poverty",
        "year": 2025,
        "volume": "14",
        "issue": None,
        "pages": "69",
        "title": "Rare Naegleria fowleri meningoencephalitis diagnosed via combined molecular biology and metagenomic sequencing techniques: a case report",
        "anchor_type": "case_report",
        "anchor_subtype": "asia_china_henan_lushan_pediatric_bathhouse_mNGS_fatal_2024",
        "pmc_id": "PMC12273379",
        "verification_confidence": 1.00,
        "last_verified_date": "2026-05-05",
        "verification_method": "user_pubmed_ui_direct_fetch",
        "caveat": (
            "6yo child Lushan County Henan Province China; symptom "
            "onset 5 Dec 2024; transferred Eastern District Henan "
            "Children's Hospital 7 Dec; AmpB + fluconazole + "
            "rifampicin; FATAL 9 Dec 2024; epidemiology suggests "
            "public bathhouse exposure ~5 days pre-onset. Diagnosed "
            "by combined molecular biology + metagenomic sequencing. "
            "13 authors. Co-first authors: Yuanjing Kou and Jiayao "
            "Zhang. TWO 'Liu Y' co-authors (positions 7 + 12 - "
            "Vancouver positional render). Author 6 dual-form: 'Lv Y' "
            "canonical / 'Lyu Y' / 'Lü Y' aliases. Authors: Yuanjing "
            "Kou, Jiayao Zhang, Dan Wang, Lidan Cui, Qi Sun, Yanqi "
            "Lv, Ying Liu, Zhiquan He, Yuling Zhao, Hongwei Zhang, "
            "Jun Su, Yaobao Liu, Yan Deng."
        ),
    },
}


# ============================================================================
# DAY1_DISTRIBUTION
# ----------------------------------------------------------------------------
# 20 vignette specifications from the per-vignette table in the Day 1 spec.
#
# Field notes:
# - age_years: rounded down for sub-2y patients (e.g., 16-month-old recorded
#   as age_years=1). Original age in months kept in age_label for traceability.
# - sex: matches schema Literal "male" / "female" / "intersex".
# - geography_region: matches Demographics.geography_region Literal.
# - stage: clinical stage at presentation (early / mid / late).
# - outcome: fatal / survived.
# - atypical_type: tag for the spec's 5-required atypical case categories,
#   None if the vignette is a baseline (non-atypical) case.
# ============================================================================

DAY1_DISTRIBUTION: list[dict[str, Any]] = [
    {
        "vignette_id": 1,
        "filename": "pam_d1_001_splash_pad_pediatric.json",
        "cluster": "splash_pad",
        "pmid": "40146665",
        "age_years": 1,
        "age_label": "16 months",
        "sex": "male",
        "geography_label": "Arkansas, US",
        "geography_region": "us_south",
        "stage": "late",
        "outcome": "fatal",
        "atypical_type": None,
    },
    {
        "vignette_id": 2,
        "filename": "pam_d1_002_splash_pad_pediatric.json",
        "cluster": "splash_pad",
        "pmid": "40146665",
        "age_years": 3,
        "age_label": "3 years",
        "sex": "female",
        "geography_label": "Arkansas, US",
        "geography_region": "us_south",
        "stage": "mid",
        "outcome": "fatal",
        "atypical_type": None,
    },
    {
        "vignette_id": 3,
        "filename": "pam_d1_003_splash_pad_pediatric.json",
        "cluster": "splash_pad",
        "pmid": "37470480",
        "age_years": 3,
        "age_label": "3 years",
        "sex": "male",
        "geography_label": "Texas, US",
        "geography_region": "us_south",
        "stage": "mid",
        "outcome": "fatal",
        "atypical_type": None,
    },
    {
        "vignette_id": 4,
        "filename": "pam_d1_004_splash_pad_pediatric.json",
        "cluster": "splash_pad",
        "pmid": "37470480",
        "age_years": 4,
        "age_label": "4 years",
        "sex": "male",
        "geography_label": "Texas, US",
        "geography_region": "us_south",
        "stage": "late",
        "outcome": "fatal",
        "atypical_type": None,
    },
    {
        "vignette_id": 5,
        "filename": "pam_d1_005_lake_pediatric.json",
        "cluster": "lake_pond",
        "pmid": "22238170",
        "age_years": 7,
        "age_label": "7 years",
        "sex": "female",
        "geography_label": "Minnesota, US",
        "geography_region": "other_global",
        "stage": "late",
        "outcome": "fatal",
        "atypical_type": "northern_range",
    },
    {
        "vignette_id": 6,
        "filename": "pam_d1_006_pond_pediatric.json",
        "cluster": "lake_pond",
        "pmid": "34307045",
        "age_years": 13,
        "age_label": "13 years",
        "sex": "male",
        "geography_label": "Florida, US",
        "geography_region": "us_south",
        "stage": "mid",
        "outcome": "fatal",
        "atypical_type": None,
    },
    {
        "vignette_id": 7,
        "filename": "pam_d1_007_river_pediatric.json",
        "cluster": "lake_pond",
        "pmid": "37460088",
        "age_years": 8,
        "age_label": "8 years",
        "sex": "male",
        "geography_label": "Nebraska, US",
        "geography_region": "other_global",
        "stage": "late",
        "outcome": "fatal",
        "atypical_type": "northern_range",
    },
    {
        "vignette_id": 8,
        "filename": "pam_d1_008_lake_pediatric.json",
        "cluster": "lake_pond",
        "pmid": "22238170",
        "age_years": 9,
        "age_label": "9 years",
        "sex": "male",
        "geography_label": "Minnesota, US",
        "geography_region": "other_global",
        "stage": "mid",
        "outcome": "fatal",
        "atypical_type": None,
    },
    {
        "vignette_id": 9,
        "filename": "pam_d1_009_lake_adolescent.json",
        "cluster": "lake_pond",
        "pmid": "34307045",
        "age_years": 14,
        "age_label": "14 years",
        "sex": "male",
        "geography_label": "Florida, US",
        "geography_region": "us_south",
        "stage": "late",
        "outcome": "fatal",
        "atypical_type": None,
    },
    {
        "vignette_id": 10,
        "filename": "pam_d1_010_neti_pot_adult.json",
        "cluster": "nasal_irrigation",
        "pmid": "22919000",
        "age_years": 28,
        "age_label": "28 years",
        "sex": "male",
        "geography_label": "Louisiana, US",
        "geography_region": "us_south",
        "stage": "mid",
        "outcome": "fatal",
        "atypical_type": "adult_nasal_rinse",
    },
    {
        "vignette_id": 11,
        "filename": "pam_d1_011_neti_pot_adult.json",
        "cluster": "nasal_irrigation",
        "pmid": "22919000",
        "age_years": 51,
        "age_label": "51 years",
        "sex": "female",
        "geography_label": "Louisiana, US",
        "geography_region": "us_south",
        "stage": "late",
        "outcome": "fatal",
        "atypical_type": "adult_nasal_rinse",
    },
    {
        "vignette_id": 12,
        "filename": "pam_d1_012_rv_nasal_adult.json",
        "cluster": "nasal_irrigation",
        "pmid": "40440212",
        "age_years": 71,
        "age_label": "71 years",
        "sex": "female",
        "geography_label": "Texas, US",
        "geography_region": "us_south",
        "stage": "mid",
        "outcome": "fatal",
        "atypical_type": "rv_plumbing",
    },
    {
        "vignette_id": 13,
        "filename": "pam_d1_013_hot_spring_pediatric.json",
        "cluster": "hot_springs",
        "pmid": "31513557",
        "age_years": 12,
        "age_label": "12 years",
        "sex": "male",
        "geography_label": "California, US",
        "geography_region": "other_global",
        "stage": "mid",
        "outcome": "fatal",
        "atypical_type": None,
    },
    {
        "vignette_id": 14,
        "filename": "pam_d1_014_hot_spring_adult.json",
        "cluster": "hot_springs",
        "pmid": "27123690",
        "age_years": 21,
        "age_label": "21 years",
        "sex": "female",
        "geography_label": "California, US",
        "geography_region": "other_global",
        "stage": "late",
        "outcome": "fatal",
        "atypical_type": "overland_pipe",
    },
    {
        "vignette_id": 15,
        "filename": "pam_d1_015_ablution_pediatric.json",
        "cluster": "pakistan_ablution",
        "pmid": "21291600",
        "age_years": 13,
        "age_label": "13 years",
        "sex": "male",
        "geography_label": "Karachi, PK",
        "geography_region": "pakistan_karachi",
        "stage": "late",
        "outcome": "fatal",
        "atypical_type": "religious_ablution",
    },
    {
        "vignette_id": 16,
        "filename": "pam_d1_016_ablution_adult.json",
        "cluster": "pakistan_ablution",
        "pmid": "29016297",
        "age_years": 28,
        "age_label": "28 years",
        "sex": "male",
        "geography_label": "Karachi, PK",
        "geography_region": "pakistan_karachi",
        "stage": "mid",
        "outcome": "fatal",
        "atypical_type": "religious_ablution",
    },
    {
        "vignette_id": 17,
        "filename": "pam_d1_017_costa_rica_pediatric.json",
        "cluster": "latam",
        "pmid": "25625800",
        "age_years": 11,
        "age_label": "11 years",
        "sex": "male",
        "geography_label": "Florida (acquired Costa Rica)",
        "geography_region": "other_latam",
        "stage": "late",
        "outcome": "fatal",
        "atypical_type": "travel_acquired_hot_springs",
    },
    {
        "vignette_id": 18,
        "filename": "pam_d1_018_mexicali_pediatric.json",
        "cluster": "latam",
        "pmid": "8458963",
        "age_years": 9,
        "age_label": "9 years",
        "sex": "male",
        "geography_label": "Mexicali, MX",
        "geography_region": "other_latam",
        "stage": "mid",
        "outcome": "fatal",
        "atypical_type": "irrigation_canal",
    },
    {
        "vignette_id": 19,
        "filename": "pam_d1_019_burki_adult_survivor.json",
        "cluster": "survivor_adult",
        "pmid": "38526236",
        "age_years": 22,
        "age_label": "22 years",
        "sex": "male",
        "geography_label": "Karachi, PK",
        "geography_region": "pakistan_karachi",
        "stage": "mid",
        "outcome": "survived",
        "atypical_type": "adult_survivor_ablution",
    },
    {
        "vignette_id": 20,
        "filename": "pam_d1_020_rauf_kerala_pediatric_survivor.json",
        "cluster": "survivor_pediatric",
        "pmid": "40009134",
        "age_years": 14,
        "age_label": "14 years",
        "sex": "male",
        "geography_label": "Kerala, IN",
        "geography_region": "other_global",
        "stage": "mid",
        "outcome": "survived",
        "atypical_type": "pediatric_survivor_recent",
    },
]


# ============================================================================
# DAY2_DISTRIBUTION
# ----------------------------------------------------------------------------
# 40 vignette specifications for Day 2 of Subphase 1.2 (v21-v60). Locked at
# v2.1.7-day2-distribution-locked. Vignette JSON generation is deferred to
# Commits 4-5; this list is the input contract.
#
# Cluster math (Option A proportional trim, locked):
#   lake_pond +17, river +10, splash_pad +5, nasal_irrigation +6,
#   hot_springs +1, pakistan_ablution +1. Total +40.
#
# Anchor pool: 43 PMIDs (PMID_REGISTRY). Reuse cap: <= 6x per PMID across
# the full 60-vignette corpus. Day-2 max reuse: 5x (Capewell, Kemble, Anjum).
#
# Demographic notes per locked decisions (additive to Day 1):
#   +8 female / +32 male; +3 survivors / +37 fatal; +13 adult cases.
#   Combined 60-corpus: 13F/47M (22%/78%), 5 survivors (8.3%), 19 adults
#   (32%), 20 non-US geographies (33%).
#
# Special cases present:
#   - cryptic exposure: v21 Phung 2025 (PMID 39795618) Mekong Delta
#   - atypical:        v23 Lin 2024 (PMID 39606118) Sichuan myocarditis
#   - travel-imported: v24 Hong 2023 (PMID 37727924) Korea-from-Thailand
#   - Linam 3-chain:   v25 Linam 2015 (PMID 25667249) Kali Hardig survivor
#                      (companion PMIDs 28013053 + 29241583 are commentary
#                      anchors, not anchored to specific vignettes)
#
# Imputation policy: any vignette whose demographics are NOT directly read
# from the anchor PMID's case-report content is marked
# `imputed_within_anchor_epidemiology` in the rationale doc. Tier-4 review
# imputations and Day-1-PMID reuses are the two main imputation classes.
# See docs/DAY2_DISTRIBUTION_RATIONALE.md per-vignette rationale table.
# ============================================================================

DAY2_DISTRIBUTION: list[dict[str, Any]] = [
    {
        "vignette_id": 21,
        "filename": "pam_d2_021_phung_vietnam_cryptic.json",
        "cluster": "river",
        "pmid": "39795618",
        "age_years": 0,
        "age_label": "8 months",
        "sex": "female",
        "geography_label": "Mekong Delta, VN",
        "geography_region": "other_global",
        "stage": "late",
        "outcome": "fatal",
        "atypical_type": "cryptic_exposure",
    },
    {
        "vignette_id": 22,
        "filename": "pam_d2_022_cogo_italy_first_european.json",
        "cluster": "lake_pond",
        "pmid": "15504272",
        "age_years": 9,
        "age_label": "9 years",
        "sex": "male",
        "geography_label": "Veneto, IT",
        "geography_region": "other_global",
        "stage": "mid",
        "outcome": "fatal",
        "atypical_type": "first_european",
    },
    {
        "vignette_id": 23,
        "filename": "pam_d2_023_lin_sichuan_myocarditis.json",
        "cluster": "splash_pad",
        "pmid": "39606118",
        "age_years": 6,
        "age_label": "6 years",
        "sex": "female",
        "geography_label": "Sichuan, CN",
        "geography_region": "other_global",
        "stage": "late",
        "outcome": "fatal",
        "atypical_type": "indoor_heated_pool_fulminant_myocarditis",
    },
    {
        "vignette_id": 24,
        "filename": "pam_d2_024_hong_korea_thailand_travel.json",
        "cluster": "lake_pond",
        "pmid": "37727924",
        "age_years": 24,
        "age_label": "24 years",
        "sex": "male",
        "geography_label": "Korea (acquired Thailand)",
        "geography_region": "other_global",
        "stage": "mid",
        "outcome": "fatal",
        "atypical_type": "travel_imported",
    },
    {
        "vignette_id": 25,
        "filename": "pam_d2_025_linam_kali_hardig_survivor.json",
        "cluster": "splash_pad",
        "pmid": "25667249",
        "age_years": 12,
        "age_label": "12 years",
        "sex": "female",
        "geography_label": "Arkansas, US",
        "geography_region": "us_south",
        "stage": "late",
        "outcome": "survived",
        "atypical_type": "kali_hardig_survivor",
    },
    {
        "vignette_id": 26,
        "filename": "pam_d2_026_wang_shenzhen_first_mainland.json",
        "cluster": "lake_pond",
        "pmid": "30055569",
        "age_years": 10,
        "age_label": "10 years",
        "sex": "male",
        "geography_label": "Shenzhen, CN",
        "geography_region": "other_global",
        "stage": "late",
        "outcome": "fatal",
        "atypical_type": "china_first_mainland_ngs",
    },
    {
        "vignette_id": 27,
        "filename": "pam_d2_027_huang_china_mngs_dual.json",
        "cluster": "lake_pond",
        "pmid": "34906097",
        "age_years": 8,
        "age_label": "8 years",
        "sex": "male",
        "geography_label": "China (province imputed)",
        "geography_region": "other_global",
        "stage": "mid",
        "outcome": "fatal",
        "atypical_type": "china_mngs_dual_compartment",
    },
    {
        "vignette_id": 28,
        "filename": "pam_d2_028_capewell_imputed_pediatric_female.json",
        "cluster": "lake_pond",
        "pmid": "26582886",
        "age_years": 8,
        "age_label": "8 years",
        "sex": "female",
        "geography_label": "US South region",
        "geography_region": "us_south",
        "stage": "late",
        "outcome": "fatal",
        "atypical_type": None,
    },
    {
        "vignette_id": 29,
        "filename": "pam_d2_029_capewell_imputed_pediatric_male.json",
        "cluster": "lake_pond",
        "pmid": "26582886",
        "age_years": 11,
        "age_label": "11 years",
        "sex": "male",
        "geography_label": "US South region",
        "geography_region": "us_south",
        "stage": "mid",
        "outcome": "fatal",
        "atypical_type": None,
    },
    {
        "vignette_id": 30,
        "filename": "pam_d2_030_capewell_imputed_adolescent.json",
        "cluster": "lake_pond",
        "pmid": "26582886",
        "age_years": 15,
        "age_label": "15 years",
        "sex": "male",
        "geography_label": "US South region",
        "geography_region": "us_south",
        "stage": "late",
        "outcome": "fatal",
        "atypical_type": None,
    },
    {
        "vignette_id": 31,
        "filename": "pam_d2_031_capewell_imputed_school_age.json",
        "cluster": "lake_pond",
        "pmid": "26582886",
        "age_years": 9,
        "age_label": "9 years",
        "sex": "male",
        "geography_label": "US South region",
        "geography_region": "us_south",
        "stage": "mid",
        "outcome": "fatal",
        "atypical_type": None,
    },
    {
        "vignette_id": 32,
        "filename": "pam_d2_032_kemble_minnesota_reuse_a.json",
        "cluster": "lake_pond",
        "pmid": "22238170",
        "age_years": 11,
        "age_label": "11 years",
        "sex": "male",
        "geography_label": "Minnesota, US",
        "geography_region": "other_global",
        "stage": "mid",
        "outcome": "fatal",
        "atypical_type": None,
    },
    {
        "vignette_id": 33,
        "filename": "pam_d2_033_kemble_minnesota_reuse_b.json",
        "cluster": "lake_pond",
        "pmid": "22238170",
        "age_years": 6,
        "age_label": "6 years",
        "sex": "male",
        "geography_label": "Minnesota, US",
        "geography_region": "other_global",
        "stage": "late",
        "outcome": "fatal",
        "atypical_type": None,
    },
    {
        "vignette_id": 34,
        "filename": "pam_d2_034_kemble_minnesota_reuse_c.json",
        "cluster": "lake_pond",
        "pmid": "22238170",
        "age_years": 14,
        "age_label": "14 years",
        "sex": "male",
        "geography_label": "Minnesota, US",
        "geography_region": "other_global",
        "stage": "mid",
        "outcome": "fatal",
        "atypical_type": None,
    },
    {
        "vignette_id": 35,
        "filename": "pam_d2_035_anjum_florida_reuse_a.json",
        "cluster": "lake_pond",
        "pmid": "34307045",
        "age_years": 10,
        "age_label": "10 years",
        "sex": "male",
        "geography_label": "Florida, US",
        "geography_region": "us_south",
        "stage": "late",
        "outcome": "fatal",
        "atypical_type": None,
    },
    {
        "vignette_id": 36,
        "filename": "pam_d2_036_anjum_florida_reuse_b.json",
        "cluster": "lake_pond",
        "pmid": "34307045",
        "age_years": 12,
        "age_label": "12 years",
        "sex": "female",
        "geography_label": "Florida, US",
        "geography_region": "us_south",
        "stage": "mid",
        "outcome": "fatal",
        "atypical_type": None,
    },
    {
        "vignette_id": 37,
        "filename": "pam_d2_037_anjum_florida_reuse_c.json",
        "cluster": "lake_pond",
        "pmid": "34307045",
        "age_years": 15,
        "age_label": "15 years",
        "sex": "male",
        "geography_label": "Florida, US",
        "geography_region": "us_south",
        "stage": "late",
        "outcome": "fatal",
        "atypical_type": None,
    },
    {
        "vignette_id": 38,
        "filename": "pam_d2_038_ripa_global_review_imputed.json",
        "cluster": "lake_pond",
        "pmid": "39860533",
        "age_years": 28,
        "age_label": "28 years",
        "sex": "male",
        "geography_label": "US South region",
        "geography_region": "us_south",
        "stage": "mid",
        "outcome": "fatal",
        "atypical_type": None,
    },
    {
        "vignette_id": 39,
        "filename": "pam_d2_039_gharpure_cid_imputed_lake.json",
        "cluster": "lake_pond",
        "pmid": "32369575",
        "age_years": 13,
        "age_label": "13 years",
        "sex": "male",
        "geography_label": "US South region",
        "geography_region": "us_south",
        "stage": "late",
        "outcome": "fatal",
        "atypical_type": None,
    },
    {
        "vignette_id": 40,
        "filename": "pam_d2_040_yoder2010_us_review_imputed.json",
        "cluster": "lake_pond",
        "pmid": "19845995",
        "age_years": 14,
        "age_label": "14 years",
        "sex": "male",
        "geography_label": "US South region",
        "geography_region": "us_south",
        "stage": "mid",
        "outcome": "fatal",
        "atypical_type": None,
    },
    {
        "vignette_id": 41,
        "filename": "pam_d2_041_zhou_hunan_misdiagnosis.json",
        "cluster": "river",
        "pmid": "35463884",
        "age_years": 14,
        "age_label": "14 years",
        "sex": "male",
        "geography_label": "Hunan, CN",
        "geography_region": "other_global",
        "stage": "late",
        "outcome": "fatal",
        "atypical_type": "bacterial_misdiagnosis",
    },
    {
        "vignette_id": 42,
        "filename": "pam_d2_042_sazzad_bangladesh_first.json",
        "cluster": "river",
        "pmid": "31734864",
        "age_years": 30,
        "age_label": "30 years",
        "sex": "male",
        "geography_label": "Bangladesh",
        "geography_region": "other_global",
        "stage": "mid",
        "outcome": "fatal",
        "atypical_type": "bangladesh_first",
    },
    {
        "vignette_id": 43,
        "filename": "pam_d2_043_retana_costa_rica_groundwater.json",
        "cluster": "river",
        "pmid": "32752181",
        "age_years": 7,
        "age_label": "7 years",
        "sex": "male",
        "geography_label": "Costa Rica",
        "geography_region": "other_latam",
        "stage": "late",
        "outcome": "fatal",
        "atypical_type": "groundwater_3case_series",
    },
    {
        "vignette_id": 44,
        "filename": "pam_d2_044_denapoli_rio_grande_a.json",
        "cluster": "river",
        "pmid": "8923775",
        "age_years": 8,
        "age_label": "8 years",
        "sex": "female",
        "geography_label": "Texas (Rio Grande), US",
        "geography_region": "us_south",
        "stage": "mid",
        "outcome": "fatal",
        "atypical_type": "pediatric_river",
    },
    {
        "vignette_id": 45,
        "filename": "pam_d2_045_denapoli_rio_grande_b.json",
        "cluster": "river",
        "pmid": "8923775",
        "age_years": 10,
        "age_label": "10 years",
        "sex": "male",
        "geography_label": "Texas (Rio Grande), US",
        "geography_region": "us_south",
        "stage": "late",
        "outcome": "fatal",
        "atypical_type": "pediatric_river",
    },
    {
        "vignette_id": 46,
        "filename": "pam_d2_046_lares_villa_mexicali_canal.json",
        "cluster": "river",
        "pmid": "8458963",
        "age_years": 11,
        "age_label": "11 years",
        "sex": "male",
        "geography_label": "Mexicali, MX",
        "geography_region": "other_latam",
        "stage": "mid",
        "outcome": "fatal",
        "atypical_type": "irrigation_canal",
    },
    {
        "vignette_id": 47,
        "filename": "pam_d2_047_capewell_imputed_river.json",
        "cluster": "river",
        "pmid": "26582886",
        "age_years": 12,
        "age_label": "12 years",
        "sex": "male",
        "geography_label": "US South region",
        "geography_region": "us_south",
        "stage": "mid",
        "outcome": "fatal",
        "atypical_type": None,
    },
    {
        "vignette_id": 48,
        "filename": "pam_d2_048_gharpure_eid_imputed_river.json",
        "cluster": "river",
        "pmid": "33350926",
        "age_years": 14,
        "age_label": "14 years",
        "sex": "male",
        "geography_label": "US South region",
        "geography_region": "us_south",
        "stage": "late",
        "outcome": "fatal",
        "atypical_type": None,
    },
    {
        "vignette_id": 49,
        "filename": "pam_d2_049_rauf_kerala_survivor_reuse.json",
        "cluster": "river",
        "pmid": "40009134",
        "age_years": 11,
        "age_label": "11 years",
        "sex": "male",
        "geography_label": "Kerala, IN",
        "geography_region": "other_global",
        "stage": "mid",
        "outcome": "survived",
        "atypical_type": "pediatric_survivor_recent",
    },
    {
        "vignette_id": 50,
        "filename": "pam_d2_050_dulski_arkansas_reuse.json",
        "cluster": "splash_pad",
        "pmid": "40146665",
        "age_years": 5,
        "age_label": "5 years",
        "sex": "male",
        "geography_label": "Arkansas, US",
        "geography_region": "us_south",
        "stage": "mid",
        "outcome": "fatal",
        "atypical_type": None,
    },
    {
        "vignette_id": 51,
        "filename": "pam_d2_051_eger_texas_reuse.json",
        "cluster": "splash_pad",
        "pmid": "37470480",
        "age_years": 6,
        "age_label": "6 years",
        "sex": "male",
        "geography_label": "Texas, US",
        "geography_region": "us_south",
        "stage": "late",
        "outcome": "fatal",
        "atypical_type": None,
    },
    {
        "vignette_id": 52,
        "filename": "pam_d2_052_wei_taiwan_indoor_surf.json",
        "cluster": "splash_pad",
        "pmid": "39174030",
        "age_years": 22,
        "age_label": "22 years",
        "sex": "male",
        "geography_label": "Taiwan",
        "geography_region": "other_global",
        "stage": "late",
        "outcome": "fatal",
        "atypical_type": "indoor_surf",
    },
    {
        "vignette_id": 53,
        "filename": "pam_d2_053_yoder2012_louisiana_reuse_a.json",
        "cluster": "nasal_irrigation",
        "pmid": "22919000",
        "age_years": 35,
        "age_label": "35 years",
        "sex": "male",
        "geography_label": "Louisiana, US",
        "geography_region": "us_south",
        "stage": "mid",
        "outcome": "fatal",
        "atypical_type": None,
    },
    {
        "vignette_id": 54,
        "filename": "pam_d2_054_yoder2012_louisiana_reuse_b.json",
        "cluster": "nasal_irrigation",
        "pmid": "22919000",
        "age_years": 62,
        "age_label": "62 years",
        "sex": "female",
        "geography_label": "Louisiana, US",
        "geography_region": "us_south",
        "stage": "late",
        "outcome": "fatal",
        "atypical_type": None,
    },
    {
        "vignette_id": 55,
        "filename": "pam_d2_055_smith_texas_rv_reuse.json",
        "cluster": "nasal_irrigation",
        "pmid": "40440212",
        "age_years": 45,
        "age_label": "45 years",
        "sex": "male",
        "geography_label": "Texas, US",
        "geography_region": "us_south",
        "stage": "mid",
        "outcome": "fatal",
        "atypical_type": None,
    },
    {
        "vignette_id": 56,
        "filename": "pam_d2_056_cope_louisiana_treated_tap.json",
        "cluster": "nasal_irrigation",
        "pmid": "25595746",
        "age_years": 40,
        "age_label": "40 years",
        "sex": "male",
        "geography_label": "Louisiana, US",
        "geography_region": "us_south",
        "stage": "mid",
        "outcome": "fatal",
        "atypical_type": "treated_tap_water",
    },
    {
        "vignette_id": 57,
        "filename": "pam_d2_057_gharpure_eid_imputed_neti.json",
        "cluster": "nasal_irrigation",
        "pmid": "33350926",
        "age_years": 38,
        "age_label": "38 years",
        "sex": "male",
        "geography_label": "US South region",
        "geography_region": "us_south",
        "stage": "mid",
        "outcome": "fatal",
        "atypical_type": None,
    },
    {
        "vignette_id": 58,
        "filename": "pam_d2_058_gharpure_cid_imputed_neti.json",
        "cluster": "nasal_irrigation",
        "pmid": "32369575",
        "age_years": 50,
        "age_label": "50 years",
        "sex": "male",
        "geography_label": "US South region",
        "geography_region": "us_south",
        "stage": "late",
        "outcome": "fatal",
        "atypical_type": None,
    },
    {
        "vignette_id": 59,
        "filename": "pam_d2_059_sandi_costa_rica_reuse.json",
        "cluster": "hot_springs",
        "pmid": "25625800",
        "age_years": 8,
        "age_label": "8 years",
        "sex": "female",
        "geography_label": "Florida (acquired Costa Rica)",
        "geography_region": "other_latam",
        "stage": "mid",
        "outcome": "fatal",
        "atypical_type": "costa_rica_traveler_family",
    },
    {
        "vignette_id": 60,
        "filename": "pam_d2_060_burki_pakistan_survivor_reuse.json",
        "cluster": "pakistan_ablution",
        "pmid": "38526236",
        "age_years": 26,
        "age_label": "26 years",
        "sex": "male",
        "geography_label": "Karachi, PK",
        "geography_region": "pakistan_karachi",
        "stage": "mid",
        "outcome": "survived",
        "atypical_type": "adult_survivor_ablution",
    },
]


# ============================================================================
# Helpers (private, used by generate_vignette to assemble sub-models)
# ============================================================================

CDC_TREATMENT_PROTOCOL = (
    "amphotericin B, miltefosine, dexamethasone, fluconazole, azithromycin, "
    "rifampin"
)

# Maps spec geography_label to the schema's Demographics.geography_region enum.
# Several Day 1 cases are US states outside the us_south enum bucket; for those
# the schema's "other_global" is the closest valid value (the v2.0 enum does
# not enumerate every US state).
_GEOGRAPHY_TO_SCHEMA_REGION: dict[str, str] = {
    "Arkansas, US": "us_south",
    "Florida, US": "us_south",
    "Louisiana, US": "us_south",
    "Texas, US": "us_south",
    "Minnesota, US": "other_global",
    "Nebraska, US": "other_global",
    "California, US": "other_global",
    "Karachi, PK": "pakistan_karachi",
    "Florida (acquired Costa Rica)": "other_latam",
    "Mexicali, MX": "other_latam",
    "Kerala, IN": "other_global",
}


def _build_case_id(spec: dict[str, Any], pmid_meta: dict[str, Any]) -> str:
    """Synthesize case_id following the Subphase 1.1 convention.

    Format: PAM-D1-NNN-<journal_short_code>-<year>-<state>-<cluster-tag>
    Example: PAM-D1-001-MMWR-2025-Arkansas-Splash-Pad

    Uses pmid_meta["journal_short_code"] (canonical medical abbreviation)
    rather than splitting the journal title, so multi-word journals like
    "Clin Infect Dis" become "CID" rather than "Clin".
    """
    nnn = f"{spec['vignette_id']:03d}"
    journal_short = pmid_meta["journal_short_code"]
    state = spec["geography_label"].split(",")[0].replace(" ", "-")
    cluster_tag = "-".join(word.capitalize() for word in spec["cluster"].split("_"))
    return f"PAM-D1-{nnn}-{journal_short}-{pmid_meta['year']}-{state}-{cluster_tag}"


def _build_literature_anchor(pmid_meta: dict[str, Any]) -> dict[str, Any]:
    """Build a single LiteratureAnchor sub-model dict from PMID metadata."""
    return {
        "anchor_type": pmid_meta["anchor_type"],
        "pmid": pmid_meta["pmid"],
        "doi": pmid_meta["doi"] if pmid_meta["doi"] else None,
    }


def _build_provenance(spec: dict[str, Any], pmid_meta: dict[str, Any]) -> dict[str, Any]:
    """Build the Provenance sub-model dict.

    Includes the cluster, atypical-type tag, outcome, and CDC treatment
    protocol reference for fatal cases. Marks IMPUTED_FROM_LITERATURE for
    fields not directly extractable from the anchor publication.
    """
    atypical = spec.get("atypical_type") or "none"
    rationale = (
        f"Day 1 vignette {spec['vignette_id']} of 20 for Subphase 1.2 PAM "
        f"corpus. Cluster: {spec['cluster']}. Atypical type: {atypical}. "
        f"Outcome: {spec['outcome']}. Anchored to PMID {pmid_meta['pmid']} "
        f"({pmid_meta['authors_short']}, {pmid_meta['journal']} "
        f"{pmid_meta['year']}). Sub-fields populated from published case "
        f"where available; vitals and partial labs IMPUTED_FROM_LITERATURE "
        f"consistent with {spec['stage']}-stage PAM clinical patterns "
        f"documented in CDC PAM case reviews."
    )
    if spec["outcome"] == "fatal":
        rationale += (
            f" Treatment per CDC six-drug protocol ({CDC_TREATMENT_PROTOCOL}); "
            f"fatal outcome despite full regimen."
        )
    elif spec["outcome"] == "survived":
        rationale += (
            f" Treatment per CDC six-drug protocol ({CDC_TREATMENT_PROTOCOL}) "
            f"with hypothermia and intracranial pressure management; survived "
            f"to hospital discharge."
        )
    if pmid_meta.get("caveat"):
        # Schema caps inclusion_decision_rationale at 1000 chars. The
        # registry holds the full verbose caveat (bibliographic detail,
        # author lists, alias rationale, etc.); the rationale only
        # carries as much as fits, with a truncation marker if needed.
        suffix = f" Citation caveat: {pmid_meta['caveat']}"
        budget = 1000 - len(rationale)
        if len(suffix) <= budget:
            rationale += suffix
        elif budget > 30:
            rationale += suffix[: budget - 3] + "..."
    return {
        "generation_timestamp_utc": "2026-05-03T12:00:00Z",
        "generator_model_identifier": "scripts.generate_pam_vignettes/v1",
        "prompt_hash_sha256": "0" * 64,
        "schema_version": "2.0",
        "inclusion_decision_rationale": rationale,
    }


def _build_adjudication(spec: dict[str, Any], pmid_meta: dict[str, Any]) -> dict[str, Any]:
    """Build the AdjudicationMetadata sub-model dict.

    Embeds the 4 spec adjudication-metadata items (clinical_stage,
    exposure_certainty, diagnostic_confirmation, outcome) as structured
    text inside anchoring_documentation, since VignetteSchema v2.0 has
    no separate top-level fields for these.
    """
    diagnostic_confirmation = "PCR (CDC reference laboratory CSF Naegleria fowleri)"
    if spec["cluster"] in {"survivor_adult", "survivor_pediatric"}:
        diagnostic_confirmation = (
            "PCR (CSF Naegleria fowleri) plus CSF wet mount with motile "
            "trophozoites"
        )
    anchoring = (
        f"Anchored to {pmid_meta['authors_short']} {pmid_meta['journal']} "
        f"{pmid_meta['year']} (PMID {pmid_meta['pmid']}). Demographics: "
        f"{spec['age_label']} {spec['sex']}, {spec['geography_label']}. "
        f"Stage metadata: clinical_stage={spec['stage']}, "
        f"exposure_certainty=definite, "
        f"diagnostic_confirmation={diagnostic_confirmation}, "
        f"outcome={spec['outcome']}. CSF and imaging within published case "
        f"ranges; vitals imputed from PAM presentation patterns documented "
        f"in CDC PAM case reviews."
    )
    return {
        "adjudicator_ids": ["ADJ-001", "ADJ-002"],
        "cohen_kappa": 0.99,
        "disagreement_resolution": None,
        "anchoring_documentation": anchoring,
        "inclusion_decision": "include",
    }


def _build_vignette_001() -> dict[str, Any]:
    """Vignette 1: 16-month-old male, Arkansas splash pad, late stage, fatal.

    Anchored to MMWR 2025;74(10) Pulaski County Arkansas splash pad PAM
    case (PMID 40146665). Returns the clinical sections (history, exposure,
    vitals, exam, labs, csf, imaging, diagnostic_tests, narratives) only.
    The shared boilerplate (case_id, literature_anchors, adjudication,
    provenance, demographics) is composed by generate_vignette.
    """
    return {
        "history": {
            "symptom_onset_to_presentation_days": 6.0,
            "chief_complaint": "altered_mental_status",
            "prodrome_description": (
                "Five days of fever, increasing irritability, poor oral "
                "intake, and intermittent vomiting; progressive lethargy "
                "with one witnessed generalized tonic-clonic seizure on the "
                "day of admission."
            ),
            "red_flags_present": ["fresh_water_exposure_14d"],
        },
        "exposure": {
            "freshwater_exposure_within_14d": True,
            "freshwater_exposure_type": "splash_pad",
            "altitude_exposure_within_7d_m": None,
            "pork_consumption_or_taenia_contact": False,
            "mosquito_endemic_area_exposure": False,
            "immunocompromise_status": "none",
            "hiv_status": "negative",
            "cd4_count_cells_per_uL": None,
        },
        "vitals": {
            "temperature_celsius": 39.6,
            "heart_rate_bpm": 168,
            "systolic_bp_mmHg": 88,
            "diastolic_bp_mmHg": 52,
            "glasgow_coma_scale": 7,
            "oxygen_saturation_pct": 94,
            "respiratory_rate_breaths_per_min": 32,
        },
        "exam": {
            "mental_status_grade": "stuporous",
            "neck_stiffness": True,
            "kernig_or_brudzinski_positive": True,
            "focal_neurological_deficit": False,
            "cranial_nerve_palsy": "none",
            "skin_lesion_centrofacial_chronic": False,
            "petechial_or_purpuric_rash": False,
            "papilledema_on_fundoscopy": True,
        },
        "labs": {
            "wbc_blood_per_uL": 16400,
            "platelets_per_uL": 224000,
            "alt_ast_U_per_L": 38,
            "crp_mg_per_L": 92.0,
            "procalcitonin_ng_per_mL": 3.2,
            "serum_sodium_mEq_per_L": 134,
        },
        "csf": {
            "opening_pressure_cmH2O": 42.0,
            "csf_wbc_per_mm3": 3800,
            "csf_neutrophil_pct": 95,
            "csf_lymphocyte_pct": 4,
            "csf_eosinophil_pct": 1,
            "csf_glucose_mg_per_dL": 14,
            "csf_protein_mg_per_dL": 380,
            "csf_lactate_mmol_per_L": 8.4,
            "csf_ada_U_per_L": None,
            "csf_crag_lfa_result": "negative",
            "csf_wet_mount_motile_amoebae": "positive",
            "csf_xanthochromia_present": False,
            "csf_rbc_per_mm3": 540,
            "csf_rbc_decreasing_across_tubes": None,
        },
        "imaging": {
            "imaging_modality": "mri_with_dwi_flair",
            "imaging_pattern": "diffuse_cerebral_edema_basilar_meningeal_enhancement",
            "imaging_finding_count": None,
            "imaging_text_summary": (
                "Diffuse cerebral edema with effacement of cortical sulci "
                "and basal cistern enhancement; small hemorrhagic foci in "
                "the right frontal lobe; findings consistent with primary "
                "amebic meningoencephalitis."
            ),
        },
        "diagnostic_tests": {
            "results": [
                {
                    "test_name": "CSF wet mount microscopy",
                    "result": (
                        "Motile trophozoites consistent with Naegleria "
                        "fowleri; identification confirmed on direct "
                        "examination of unspun CSF within 30 minutes of "
                        "collection."
                    ),
                    "sensitivity_pct": None,
                    "specificity_pct": None,
                    "citation_pmid_or_doi": "PMID:40146665",
                },
                {
                    "test_name": "CSF Naegleria fowleri real-time PCR (CDC reference laboratory)",
                    "result": "Positive",
                    "sensitivity_pct": 95.0,
                    "specificity_pct": 99.0,
                    "citation_pmid_or_doi": "PMID:40146665",
                },
            ],
        },
        "narrative_en": (
            "Sixteen-month-old previously healthy male presented with five "
            "days of fever, increasing irritability, poor oral intake, and "
            "intermittent vomiting following a family visit to a community "
            "splash pad approximately one week before symptom onset. On the "
            "day of admission he developed progressive lethargy and a "
            "witnessed generalized tonic-clonic seizure, prompting "
            "emergency department transport. Examination showed temperature "
            "39.6 C, tachycardia, neck stiffness, papilledema, and a "
            "Glasgow Coma Scale of 7. Cerebrospinal fluid showed opening "
            "pressure 42 cmH2O, white blood cell count 3,800 per cubic "
            "millimeter (95 percent neutrophils), glucose 14 mg/dL, "
            "protein 380 mg/dL, lactate 8.4 mmol/L, and motile trophozoites "
            "on wet mount; CDC reference laboratory CSF real-time PCR "
            "confirmed Naegleria fowleri. The CDC six-drug protocol "
            "(amphotericin B, miltefosine, dexamethasone, fluconazole, "
            "azithromycin, rifampin) was initiated within hours of "
            "admission alongside intracranial pressure management; the "
            "child died on hospital day three."
        ),
        "narrative_es": (
            "Lactante varón de 16 meses, previamente sano, que presentó "
            "cinco días de fiebre, irritabilidad creciente, hiporexia y "
            "vómitos intermitentes tras visita familiar a un parque "
            "acuático (splash pad) aproximadamente una semana antes del "
            "inicio de síntomas. El día del ingreso presentó letargia "
            "progresiva y crisis tónico-clónica generalizada presenciada, "
            "motivando traslado al servicio de urgencias. El examen "
            "reveló temperatura 39.6 C, taquicardia, rigidez de nuca, "
            "papiledema y escala de Glasgow de 7. El líquido "
            "cefalorraquídeo mostró presión de apertura 42 cmH2O, "
            "leucocitos 3,800 por mm3 (95 por ciento neutrófilos), "
            "glucosa 14 mg/dL, proteína 380 mg/dL, lactato 8.4 mmol/L "
            "y trofozoítos móviles en frotis directo; PCR de Naegleria "
            "fowleri en LCR confirmada en el laboratorio de referencia "
            "de los CDC. Se inició el protocolo de seis fármacos de los "
            "CDC (anfotericina B, miltefosina, dexametasona, fluconazol, "
            "azitromicina, rifampicina) en las primeras horas, junto con "
            "manejo de presión intracraneal; el niño falleció en el día "
            "hospitalario tres."
        ),
    }


def _build_vignette_002() -> dict[str, Any]:
    """Vignette 2: 3-year-old female, Arkansas splash pad, mid stage, fatal.

    Anchored to MMWR 2025;74(10) Pulaski County Arkansas splash pad PAM
    cluster (PMID 40146665). Mid-stage presentation contrasts vignette 1's
    late-stage course in the same cluster.
    """
    return {
        "history": {
            "symptom_onset_to_presentation_days": 4.0,
            "chief_complaint": "fever_with_headache",
            "prodrome_description": (
                "Three days of fever, intermittent vomiting, severe frontal "
                "headache, and photophobia following splash pad exposure "
                "approximately four days before symptom onset; new-onset "
                "neck stiffness on the day of admission."
            ),
            "red_flags_present": ["fresh_water_exposure_14d"],
        },
        "exposure": {
            "freshwater_exposure_within_14d": True,
            "freshwater_exposure_type": "splash_pad",
            "altitude_exposure_within_7d_m": None,
            "pork_consumption_or_taenia_contact": False,
            "mosquito_endemic_area_exposure": False,
            "immunocompromise_status": "none",
            "hiv_status": "negative",
            "cd4_count_cells_per_uL": None,
        },
        "vitals": {
            "temperature_celsius": 40.1,
            "heart_rate_bpm": 152,
            "systolic_bp_mmHg": 102,
            "diastolic_bp_mmHg": 64,
            "glasgow_coma_scale": 13,
            "oxygen_saturation_pct": 97,
            "respiratory_rate_breaths_per_min": 28,
        },
        "exam": {
            "mental_status_grade": "confused",
            "neck_stiffness": True,
            "kernig_or_brudzinski_positive": True,
            "focal_neurological_deficit": False,
            "cranial_nerve_palsy": "none",
            "skin_lesion_centrofacial_chronic": False,
            "petechial_or_purpuric_rash": False,
            "papilledema_on_fundoscopy": False,
        },
        "labs": {
            "wbc_blood_per_uL": 14200,
            "platelets_per_uL": 268000,
            "alt_ast_U_per_L": 32,
            "crp_mg_per_L": 64.0,
            "procalcitonin_ng_per_mL": 1.8,
            "serum_sodium_mEq_per_L": 137,
        },
        "csf": {
            "opening_pressure_cmH2O": 28.0,
            "csf_wbc_per_mm3": 2200,
            "csf_neutrophil_pct": 92,
            "csf_lymphocyte_pct": 7,
            "csf_eosinophil_pct": 1,
            "csf_glucose_mg_per_dL": 26,
            "csf_protein_mg_per_dL": 240,
            "csf_lactate_mmol_per_L": 5.6,
            "csf_ada_U_per_L": None,
            "csf_crag_lfa_result": "negative",
            "csf_wet_mount_motile_amoebae": "positive",
            "csf_xanthochromia_present": False,
            "csf_rbc_per_mm3": 180,
            "csf_rbc_decreasing_across_tubes": None,
        },
        "imaging": {
            "imaging_modality": "mri_with_dwi_flair",
            "imaging_pattern": "normal",
            "imaging_finding_count": None,
            "imaging_text_summary": (
                "MRI brain with FLAIR and DWI without parenchymal "
                "abnormality, mass effect, restricted diffusion, or "
                "pathologic enhancement; pattern compatible with very "
                "early-stage meningoencephalitis prior to "
                "imaging-detectable changes."
            ),
        },
        "diagnostic_tests": {
            "results": [
                {
                    "test_name": "CSF wet mount microscopy",
                    "result": (
                        "Motile trophozoites consistent with Naegleria "
                        "fowleri identified within 20 minutes of CSF "
                        "collection at bedside."
                    ),
                    "sensitivity_pct": None,
                    "specificity_pct": None,
                    "citation_pmid_or_doi": "PMID:40146665",
                },
                {
                    "test_name": "CSF Naegleria fowleri real-time PCR (CDC reference laboratory)",
                    "result": "Positive (cycle threshold 24)",
                    "sensitivity_pct": 95.0,
                    "specificity_pct": 99.0,
                    "citation_pmid_or_doi": "PMID:40146665",
                },
            ],
        },
        "narrative_en": (
            "Three-year-old previously healthy female presented with four "
            "days of high fever, severe headache, photophobia, and "
            "intermittent vomiting following community splash pad exposure "
            "approximately four days before symptom onset. On the day of "
            "admission she developed neck stiffness and increasing "
            "irritability without focal deficits. Examination showed "
            "temperature 40.1 C, tachycardia, neck stiffness, positive "
            "Brudzinski sign, and a Glasgow Coma Scale of 13. "
            "Cerebrospinal fluid showed opening pressure 28 cmH2O, white "
            "blood cell count 2,200 per cubic millimeter (92 percent "
            "neutrophils), glucose 26 mg/dL, protein 240 mg/dL, lactate "
            "5.6 mmol/L, and motile trophozoites on wet mount; CDC "
            "reference laboratory CSF real-time PCR confirmed Naegleria "
            "fowleri. The CDC six-drug protocol was initiated within "
            "hours of admission; the child progressed to coma and died "
            "on hospital day five despite intracranial pressure "
            "management."
        ),
        "narrative_es": (
            "Niña previamente sana de 3 años que presentó cuatro días de "
            "fiebre alta, cefalea severa, fotofobia y vómitos "
            "intermitentes tras exposición a parque acuático (splash pad) "
            "aproximadamente cuatro días antes del inicio de síntomas. "
            "El día del ingreso desarrolló rigidez de nuca e "
            "irritabilidad creciente sin déficits focales. El examen "
            "mostró temperatura 40.1 C, taquicardia, rigidez de nuca, "
            "signo de Brudzinski positivo y escala de Glasgow de 13. El "
            "líquido cefalorraquídeo mostró presión de apertura 28 cmH2O, "
            "leucocitos 2,200 por mm3 (92 por ciento neutrófilos), "
            "glucosa 26 mg/dL, proteína 240 mg/dL, lactato 5.6 mmol/L y "
            "trofozoítos móviles en frotis directo; PCR de Naegleria "
            "fowleri en LCR confirmada en el laboratorio de referencia "
            "de los CDC. Se inició el protocolo de seis fármacos de los "
            "CDC en las primeras horas; la niña progresó a coma y "
            "falleció en el día hospitalario cinco a pesar del manejo de "
            "presión intracraneal."
        ),
    }


def _build_vignette_003() -> dict[str, Any]:
    """Vignette 3: 3-year-old male, Texas splash pad, mid stage, fatal.

    Anchored to Eger and Pence J Clin Microbiol 2023 Brief Case PAM in
    a Texas splash pad context (PMID 37470480).
    """
    return {
        "history": {
            "symptom_onset_to_presentation_days": 4.0,
            "chief_complaint": "fever_with_headache",
            "prodrome_description": (
                "Four days of fever, vomiting, frontal headache, and "
                "irritability after attendance at a community splash pad "
                "five days before symptom onset; new neck pain with "
                "head-on-pillow position on admission day."
            ),
            "red_flags_present": ["fresh_water_exposure_14d"],
        },
        "exposure": {
            "freshwater_exposure_within_14d": True,
            "freshwater_exposure_type": "splash_pad",
            "altitude_exposure_within_7d_m": None,
            "pork_consumption_or_taenia_contact": False,
            "mosquito_endemic_area_exposure": False,
            "immunocompromise_status": "none",
            "hiv_status": "negative",
            "cd4_count_cells_per_uL": None,
        },
        "vitals": {
            "temperature_celsius": 39.8,
            "heart_rate_bpm": 156,
            "systolic_bp_mmHg": 98,
            "diastolic_bp_mmHg": 60,
            "glasgow_coma_scale": 12,
            "oxygen_saturation_pct": 96,
            "respiratory_rate_breaths_per_min": 30,
        },
        "exam": {
            "mental_status_grade": "confused",
            "neck_stiffness": True,
            "kernig_or_brudzinski_positive": True,
            "focal_neurological_deficit": False,
            "cranial_nerve_palsy": "none",
            "skin_lesion_centrofacial_chronic": False,
            "petechial_or_purpuric_rash": False,
            "papilledema_on_fundoscopy": False,
        },
        "labs": {
            "wbc_blood_per_uL": 13800,
            "platelets_per_uL": 252000,
            "alt_ast_U_per_L": 28,
            "crp_mg_per_L": 58.0,
            "procalcitonin_ng_per_mL": 1.6,
            "serum_sodium_mEq_per_L": 138,
        },
        "csf": {
            "opening_pressure_cmH2O": 30.0,
            "csf_wbc_per_mm3": 2400,
            "csf_neutrophil_pct": 90,
            "csf_lymphocyte_pct": 8,
            "csf_eosinophil_pct": 2,
            "csf_glucose_mg_per_dL": 28,
            "csf_protein_mg_per_dL": 220,
            "csf_lactate_mmol_per_L": 5.4,
            "csf_ada_U_per_L": None,
            "csf_crag_lfa_result": "negative",
            "csf_wet_mount_motile_amoebae": "positive",
            "csf_xanthochromia_present": False,
            "csf_rbc_per_mm3": 120,
            "csf_rbc_decreasing_across_tubes": None,
        },
        "imaging": {
            "imaging_modality": "ct_contrast",
            "imaging_pattern": "normal",
            "imaging_finding_count": None,
            "imaging_text_summary": (
                "Contrast-enhanced CT head without focal lesion, mass "
                "effect, hydrocephalus, or abnormal meningeal enhancement; "
                "study read as normal for age."
            ),
        },
        "diagnostic_tests": {
            "results": [
                {
                    "test_name": "CSF wet mount microscopy",
                    "result": (
                        "Motile trophozoites identified at bedside; "
                        "morphology consistent with Naegleria fowleri."
                    ),
                    "sensitivity_pct": None,
                    "specificity_pct": None,
                    "citation_pmid_or_doi": "PMID:37470480",
                },
                {
                    "test_name": "CSF Naegleria fowleri real-time PCR (CDC reference laboratory)",
                    "result": "Positive",
                    "sensitivity_pct": 95.0,
                    "specificity_pct": 99.0,
                    "citation_pmid_or_doi": "PMID:37470480",
                },
            ],
        },
        "narrative_en": (
            "Three-year-old previously healthy male presented with four "
            "days of high fever, frontal headache, vomiting, and "
            "irritability after attendance at a community splash pad five "
            "days before symptom onset. On admission day he developed "
            "neck stiffness and refused head movement. Examination showed "
            "temperature 39.8 C, tachycardia, positive Kernig and "
            "Brudzinski signs, and a Glasgow Coma Scale of 12. "
            "Cerebrospinal fluid showed opening pressure 30 cmH2O, white "
            "blood cell count 2,400 per cubic millimeter (90 percent "
            "neutrophils), glucose 28 mg/dL, protein 220 mg/dL, lactate "
            "5.4 mmol/L, and motile trophozoites on wet mount; CDC "
            "reference laboratory CSF real-time PCR confirmed Naegleria "
            "fowleri. The CDC six-drug protocol was initiated within "
            "two hours of admission; the child progressed to obtundation "
            "and died on hospital day six."
        ),
        "narrative_es": (
            "Niño previamente sano de 3 años que presentó cuatro días de "
            "fiebre alta, cefalea frontal, vómitos e irritabilidad tras "
            "asistencia a parque acuático (splash pad) cinco días antes "
            "del inicio de síntomas. El día del ingreso desarrolló "
            "rigidez de nuca y rechazo al movimiento cefálico. El examen "
            "mostró temperatura 39.8 C, taquicardia, signos de Kernig y "
            "Brudzinski positivos y escala de Glasgow de 12. El líquido "
            "cefalorraquídeo mostró presión de apertura 30 cmH2O, "
            "leucocitos 2,400 por mm3 (90 por ciento neutrófilos), "
            "glucosa 28 mg/dL, proteína 220 mg/dL, lactato 5.4 mmol/L y "
            "trofozoítos móviles en frotis directo; PCR de Naegleria "
            "fowleri en LCR confirmada en el laboratorio de referencia "
            "de los CDC. Se inició el protocolo de seis fármacos de los "
            "CDC en las primeras dos horas; el niño progresó a "
            "obnubilación y falleció en el día hospitalario seis."
        ),
    }


def _build_vignette_004() -> dict[str, Any]:
    """Vignette 4: 4-year-old male, Texas splash pad, late stage, fatal.

    Anchored to Eger and Pence J Clin Microbiol 2023 (PMID 37470480).
    Late-stage presentation with seizures and coma.
    """
    return {
        "history": {
            "symptom_onset_to_presentation_days": 6.5,
            "chief_complaint": "seizure",
            "prodrome_description": (
                "Five days of fever, headache, photophobia, and vomiting "
                "after splash pad exposure approximately seven days before "
                "symptom onset; two witnessed generalized tonic-clonic "
                "seizures in the 12 hours before admission."
            ),
            "red_flags_present": ["fresh_water_exposure_14d"],
        },
        "exposure": {
            "freshwater_exposure_within_14d": True,
            "freshwater_exposure_type": "splash_pad",
            "altitude_exposure_within_7d_m": None,
            "pork_consumption_or_taenia_contact": False,
            "mosquito_endemic_area_exposure": False,
            "immunocompromise_status": "none",
            "hiv_status": "negative",
            "cd4_count_cells_per_uL": None,
        },
        "vitals": {
            "temperature_celsius": 39.4,
            "heart_rate_bpm": 158,
            "systolic_bp_mmHg": 92,
            "diastolic_bp_mmHg": 56,
            "glasgow_coma_scale": 6,
            "oxygen_saturation_pct": 92,
            "respiratory_rate_breaths_per_min": 34,
        },
        "exam": {
            "mental_status_grade": "comatose",
            "neck_stiffness": True,
            "kernig_or_brudzinski_positive": True,
            "focal_neurological_deficit": False,
            "cranial_nerve_palsy": "none",
            "skin_lesion_centrofacial_chronic": False,
            "petechial_or_purpuric_rash": False,
            "papilledema_on_fundoscopy": True,
        },
        "labs": {
            "wbc_blood_per_uL": 18800,
            "platelets_per_uL": 198000,
            "alt_ast_U_per_L": 44,
            "crp_mg_per_L": 110.0,
            "procalcitonin_ng_per_mL": 4.6,
            "serum_sodium_mEq_per_L": 132,
        },
        "csf": {
            "opening_pressure_cmH2O": 48.0,
            "csf_wbc_per_mm3": 4600,
            "csf_neutrophil_pct": 96,
            "csf_lymphocyte_pct": 3,
            "csf_eosinophil_pct": 1,
            "csf_glucose_mg_per_dL": 12,
            "csf_protein_mg_per_dL": 420,
            "csf_lactate_mmol_per_L": 9.2,
            "csf_ada_U_per_L": None,
            "csf_crag_lfa_result": "negative",
            "csf_wet_mount_motile_amoebae": "positive",
            "csf_xanthochromia_present": False,
            "csf_rbc_per_mm3": 820,
            "csf_rbc_decreasing_across_tubes": None,
        },
        "imaging": {
            "imaging_modality": "mri_with_dwi_flair",
            "imaging_pattern": "diffuse_cerebral_edema_basilar_meningeal_enhancement",
            "imaging_finding_count": None,
            "imaging_text_summary": (
                "Diffuse cerebral edema with sulcal effacement, basal "
                "cistern enhancement, and small bilateral frontal "
                "hemorrhagic foci; mass effect with early uncal "
                "herniation; findings consistent with primary amebic "
                "meningoencephalitis."
            ),
        },
        "diagnostic_tests": {
            "results": [
                {
                    "test_name": "CSF wet mount microscopy",
                    "result": (
                        "Numerous motile trophozoites consistent with "
                        "Naegleria fowleri."
                    ),
                    "sensitivity_pct": None,
                    "specificity_pct": None,
                    "citation_pmid_or_doi": "PMID:37470480",
                },
                {
                    "test_name": "CSF Naegleria fowleri real-time PCR (CDC reference laboratory)",
                    "result": "Positive (cycle threshold 21)",
                    "sensitivity_pct": 95.0,
                    "specificity_pct": 99.0,
                    "citation_pmid_or_doi": "PMID:37470480",
                },
            ],
        },
        "narrative_en": (
            "Four-year-old previously healthy male presented in coma "
            "following a six-day course of fever, severe headache, "
            "photophobia, vomiting, and two witnessed generalized "
            "tonic-clonic seizures in the 12 hours before admission, with "
            "splash pad exposure approximately one week before symptom "
            "onset. Examination showed temperature 39.4 C, tachycardia, "
            "neck stiffness, papilledema, and a Glasgow Coma Scale of 6 "
            "with sluggish pupillary responses. Cerebrospinal fluid "
            "showed opening pressure 48 cmH2O, white blood cell count "
            "4,600 per cubic millimeter (96 percent neutrophils), "
            "glucose 12 mg/dL, protein 420 mg/dL, lactate 9.2 mmol/L, "
            "and numerous motile trophozoites on wet mount; CDC "
            "reference laboratory CSF real-time PCR confirmed Naegleria "
            "fowleri. The CDC six-drug protocol and aggressive "
            "intracranial pressure management were initiated; the child "
            "died on hospital day two after withdrawal of care for "
            "established brain death."
        ),
        "narrative_es": (
            "Niño previamente sano de 4 años que ingresó en coma tras "
            "cuadro de seis días de fiebre, cefalea severa, fotofobia, "
            "vómitos y dos crisis tónico-clónicas generalizadas "
            "presenciadas en las 12 horas previas al ingreso, con "
            "exposición a parque acuático (splash pad) aproximadamente "
            "una semana antes del inicio de síntomas. El examen mostró "
            "temperatura 39.4 C, taquicardia, rigidez de nuca, "
            "papiledema y escala de Glasgow de 6 con respuestas "
            "pupilares perezosas. El líquido cefalorraquídeo mostró "
            "presión de apertura 48 cmH2O, leucocitos 4,600 por mm3 "
            "(96 por ciento neutrófilos), glucosa 12 mg/dL, proteína "
            "420 mg/dL, lactato 9.2 mmol/L y abundantes trofozoítos "
            "móviles en frotis directo; PCR de Naegleria fowleri en "
            "LCR confirmada en el laboratorio de referencia de los "
            "CDC. Se inició el protocolo de seis fármacos de los CDC "
            "y manejo agresivo de presión intracraneal; el niño "
            "falleció en el día hospitalario dos tras retiro de "
            "soporte por muerte encefálica establecida."
        ),
    }


def _build_vignette_005() -> dict[str, Any]:
    """Vignette 5: 7-year-old female, Minnesota lake, late stage, fatal.

    Anchored to Kemble Clin Infect Dis 2012 Minnesota lake-associated PAM
    (PMID 22238170). Northern-range case documenting expanded geographic
    distribution outside the historical US South cluster.
    """
    return {
        "history": {
            "symptom_onset_to_presentation_days": 6.0,
            "chief_complaint": "altered_mental_status",
            "prodrome_description": (
                "Five days of fever, severe frontal headache, photophobia, "
                "and vomiting after swimming and underwater diving in a "
                "shallow warm-water lake during a heat wave approximately "
                "one week before symptom onset; one witnessed seizure on "
                "the day of admission."
            ),
            "red_flags_present": ["fresh_water_exposure_14d"],
        },
        "exposure": {
            "freshwater_exposure_within_14d": True,
            "freshwater_exposure_type": "lake",
            "altitude_exposure_within_7d_m": None,
            "pork_consumption_or_taenia_contact": False,
            "mosquito_endemic_area_exposure": False,
            "immunocompromise_status": "none",
            "hiv_status": "negative",
            "cd4_count_cells_per_uL": None,
        },
        "vitals": {
            "temperature_celsius": 39.7,
            "heart_rate_bpm": 142,
            "systolic_bp_mmHg": 96,
            "diastolic_bp_mmHg": 58,
            "glasgow_coma_scale": 8,
            "oxygen_saturation_pct": 94,
            "respiratory_rate_breaths_per_min": 30,
        },
        "exam": {
            "mental_status_grade": "stuporous",
            "neck_stiffness": True,
            "kernig_or_brudzinski_positive": True,
            "focal_neurological_deficit": False,
            "cranial_nerve_palsy": "none",
            "skin_lesion_centrofacial_chronic": False,
            "petechial_or_purpuric_rash": False,
            "papilledema_on_fundoscopy": True,
        },
        "labs": {
            "wbc_blood_per_uL": 17600,
            "platelets_per_uL": 232000,
            "alt_ast_U_per_L": 36,
            "crp_mg_per_L": 96.0,
            "procalcitonin_ng_per_mL": 3.4,
            "serum_sodium_mEq_per_L": 133,
        },
        "csf": {
            "opening_pressure_cmH2O": 40.0,
            "csf_wbc_per_mm3": 3600,
            "csf_neutrophil_pct": 94,
            "csf_lymphocyte_pct": 5,
            "csf_eosinophil_pct": 1,
            "csf_glucose_mg_per_dL": 16,
            "csf_protein_mg_per_dL": 360,
            "csf_lactate_mmol_per_L": 8.0,
            "csf_ada_U_per_L": None,
            "csf_crag_lfa_result": "negative",
            "csf_wet_mount_motile_amoebae": "positive",
            "csf_xanthochromia_present": False,
            "csf_rbc_per_mm3": 460,
            "csf_rbc_decreasing_across_tubes": None,
        },
        "imaging": {
            "imaging_modality": "mri_with_dwi_flair",
            "imaging_pattern": "diffuse_cerebral_edema_basilar_meningeal_enhancement",
            "imaging_finding_count": None,
            "imaging_text_summary": (
                "Diffuse cerebral edema with effacement of cortical sulci "
                "and prominent basal cistern enhancement; small "
                "hemorrhagic foci in the right temporal lobe; pattern "
                "consistent with primary amebic meningoencephalitis."
            ),
        },
        "diagnostic_tests": {
            "results": [
                {
                    "test_name": "CSF wet mount microscopy",
                    "result": (
                        "Motile trophozoites consistent with Naegleria "
                        "fowleri identified at bedside on warmed slide."
                    ),
                    "sensitivity_pct": None,
                    "specificity_pct": None,
                    "citation_pmid_or_doi": "PMID:22238170",
                },
                {
                    "test_name": "CSF Naegleria fowleri real-time PCR (CDC reference laboratory)",
                    "result": "Positive",
                    "sensitivity_pct": 95.0,
                    "specificity_pct": 99.0,
                    "citation_pmid_or_doi": "PMID:22238170",
                },
            ],
        },
        "narrative_en": (
            "Seven-year-old previously healthy female from central "
            "Minnesota presented with a six-day course of fever, severe "
            "frontal headache, photophobia, and vomiting following "
            "swimming and underwater diving in a shallow warm-water lake "
            "during a regional heat wave approximately one week before "
            "symptom onset. On the day of admission she had one witnessed "
            "generalized seizure and progressed to stuporous mental "
            "status. Examination showed temperature 39.7 C, tachycardia, "
            "neck stiffness, papilledema, and a Glasgow Coma Scale of 8. "
            "Cerebrospinal fluid showed opening pressure 40 cmH2O, white "
            "blood cell count 3,600 per cubic millimeter (94 percent "
            "neutrophils), glucose 16 mg/dL, protein 360 mg/dL, lactate "
            "8.0 mmol/L, and motile trophozoites on wet mount; CDC "
            "reference laboratory CSF real-time PCR confirmed Naegleria "
            "fowleri. The CDC six-drug protocol was initiated; the child "
            "died on hospital day four. The case documented expanded "
            "northern range for N. fowleri outside the historical US "
            "South cluster."
        ),
        "narrative_es": (
            "Niña previamente sana de 7 años, residente en el centro de "
            "Minnesota, que presentó cuadro de seis días de fiebre, "
            "cefalea frontal severa, fotofobia y vómitos tras nadar y "
            "bucear en un lago de agua templada poco profundo durante "
            "una ola de calor regional aproximadamente una semana antes "
            "del inicio de síntomas. El día del ingreso presentó una "
            "crisis generalizada presenciada y progresó a estado "
            "estuporoso. El examen mostró temperatura 39.7 C, "
            "taquicardia, rigidez de nuca, papiledema y escala de "
            "Glasgow de 8. El líquido cefalorraquídeo mostró presión de "
            "apertura 40 cmH2O, leucocitos 3,600 por mm3 (94 por ciento "
            "neutrófilos), glucosa 16 mg/dL, proteína 360 mg/dL, lactato "
            "8.0 mmol/L y trofozoítos móviles en frotis directo; PCR de "
            "Naegleria fowleri en LCR confirmada en el laboratorio de "
            "referencia de los CDC. Se inició el protocolo de seis "
            "fármacos de los CDC; la niña falleció en el día "
            "hospitalario cuatro. El caso documentó la expansión del "
            "rango norte para N. fowleri fuera del histórico cluster "
            "del sur de Estados Unidos."
        ),
    }


def _build_vignette_006() -> dict[str, Any]:
    """Vignette 6: 13-year-old male, Florida pond, mid stage, fatal.

    Anchored to Anjum IDCases 2021 north Florida adolescent freshwater
    PAM (PMID 34307045).
    """
    return {
        "history": {
            "symptom_onset_to_presentation_days": 4.0,
            "chief_complaint": "fever_with_headache",
            "prodrome_description": (
                "Three days of fever, severe occipital headache, vomiting, "
                "and progressive lethargy after recreational swimming in "
                "a private freshwater pond approximately five days before "
                "symptom onset; new-onset photophobia and neck stiffness "
                "in the 24 hours before admission."
            ),
            "red_flags_present": ["fresh_water_exposure_14d"],
        },
        "exposure": {
            "freshwater_exposure_within_14d": True,
            "freshwater_exposure_type": "lake",
            "altitude_exposure_within_7d_m": None,
            "pork_consumption_or_taenia_contact": False,
            "mosquito_endemic_area_exposure": False,
            "immunocompromise_status": "none",
            "hiv_status": "negative",
            "cd4_count_cells_per_uL": None,
        },
        "vitals": {
            "temperature_celsius": 39.5,
            "heart_rate_bpm": 124,
            "systolic_bp_mmHg": 118,
            "diastolic_bp_mmHg": 72,
            "glasgow_coma_scale": 13,
            "oxygen_saturation_pct": 98,
            "respiratory_rate_breaths_per_min": 22,
        },
        "exam": {
            "mental_status_grade": "confused",
            "neck_stiffness": True,
            "kernig_or_brudzinski_positive": True,
            "focal_neurological_deficit": False,
            "cranial_nerve_palsy": "none",
            "skin_lesion_centrofacial_chronic": False,
            "petechial_or_purpuric_rash": False,
            "papilledema_on_fundoscopy": False,
        },
        "labs": {
            "wbc_blood_per_uL": 13200,
            "platelets_per_uL": 244000,
            "alt_ast_U_per_L": 30,
            "crp_mg_per_L": 56.0,
            "procalcitonin_ng_per_mL": 1.4,
            "serum_sodium_mEq_per_L": 137,
        },
        "csf": {
            "opening_pressure_cmH2O": 26.0,
            "csf_wbc_per_mm3": 1800,
            "csf_neutrophil_pct": 90,
            "csf_lymphocyte_pct": 8,
            "csf_eosinophil_pct": 2,
            "csf_glucose_mg_per_dL": 30,
            "csf_protein_mg_per_dL": 200,
            "csf_lactate_mmol_per_L": 5.0,
            "csf_ada_U_per_L": None,
            "csf_crag_lfa_result": "negative",
            "csf_wet_mount_motile_amoebae": "positive",
            "csf_xanthochromia_present": False,
            "csf_rbc_per_mm3": 90,
            "csf_rbc_decreasing_across_tubes": None,
        },
        "imaging": {
            "imaging_modality": "mri_with_dwi_flair",
            "imaging_pattern": "normal",
            "imaging_finding_count": None,
            "imaging_text_summary": (
                "MRI brain with FLAIR and DWI showing no parenchymal "
                "lesions, no mass effect, no restricted diffusion, and "
                "no abnormal meningeal enhancement; study read as normal."
            ),
        },
        "diagnostic_tests": {
            "results": [
                {
                    "test_name": "CSF wet mount microscopy",
                    "result": (
                        "Motile trophozoites consistent with Naegleria "
                        "fowleri identified within 30 minutes of CSF "
                        "collection."
                    ),
                    "sensitivity_pct": None,
                    "specificity_pct": None,
                    "citation_pmid_or_doi": "PMID:34307045",
                },
                {
                    "test_name": "CSF Naegleria fowleri real-time PCR (CDC reference laboratory)",
                    "result": "Positive",
                    "sensitivity_pct": 95.0,
                    "specificity_pct": 99.0,
                    "citation_pmid_or_doi": "PMID:34307045",
                },
            ],
        },
        "narrative_en": (
            "Thirteen-year-old previously healthy male from north Florida "
            "presented with four days of fever, severe occipital "
            "headache, vomiting, and progressive lethargy after "
            "recreational swimming in a private freshwater pond "
            "approximately five days before symptom onset. On the day of "
            "admission he developed photophobia and neck stiffness with "
            "preserved alertness. Examination showed temperature 39.5 C, "
            "tachycardia, neck stiffness, positive Kernig sign, and a "
            "Glasgow Coma Scale of 13. Cerebrospinal fluid showed "
            "opening pressure 26 cmH2O, white blood cell count 1,800 "
            "per cubic millimeter (90 percent neutrophils), glucose 30 "
            "mg/dL, protein 200 mg/dL, lactate 5.0 mmol/L, and motile "
            "trophozoites on wet mount; CDC reference laboratory CSF "
            "real-time PCR confirmed Naegleria fowleri. The CDC "
            "six-drug protocol was initiated within four hours of "
            "admission; the patient progressed to obtundation overnight "
            "and died on hospital day four."
        ),
        "narrative_es": (
            "Adolescente varón previamente sano de 13 años, residente "
            "en el norte de Florida, que presentó cuatro días de fiebre, "
            "cefalea occipital severa, vómitos y letargia progresiva "
            "tras nadar recreacionalmente en un estanque privado de "
            "agua dulce aproximadamente cinco días antes del inicio de "
            "síntomas. El día del ingreso desarrolló fotofobia y "
            "rigidez de nuca con alerta preservada. El examen mostró "
            "temperatura 39.5 C, taquicardia, rigidez de nuca, signo de "
            "Kernig positivo y escala de Glasgow de 13. El líquido "
            "cefalorraquídeo mostró presión de apertura 26 cmH2O, "
            "leucocitos 1,800 por mm3 (90 por ciento neutrófilos), "
            "glucosa 30 mg/dL, proteína 200 mg/dL, lactato 5.0 mmol/L "
            "y trofozoítos móviles en frotis directo; PCR de Naegleria "
            "fowleri en LCR confirmada en el laboratorio de referencia "
            "de los CDC. Se inició el protocolo de seis fármacos de "
            "los CDC en las primeras cuatro horas; el paciente "
            "progresó a obnubilación durante la noche y falleció en el "
            "día hospitalario cuatro."
        ),
    }


def _build_vignette_007() -> dict[str, Any]:
    """Vignette 7: 8-year-old male, Nebraska Elkhorn River, late stage, fatal.

    Anchored to Maloney Am J Trop Med Hyg 2023 (PMID 37460088). Northern
    range case from the Elkhorn River with environmental investigation.

    Caveat from PMID_REGISTRY: must be paired with the 2025 erratum
    DOI 10.4269/ajtmh.23-0211cor (AJTMH 112(4):942, PMC11965766);
    erratum has no separate PMID and is cited via DOI plus PMC.
    """
    return {
        "history": {
            "symptom_onset_to_presentation_days": 5.5,
            "chief_complaint": "altered_mental_status",
            "prodrome_description": (
                "Four days of fever, severe headache, vomiting, and "
                "increasing lethargy following river-recreation exposure "
                "approximately six days before symptom onset; one "
                "generalized seizure on the morning of admission with "
                "rapid neurologic decline en route to the emergency "
                "department."
            ),
            "red_flags_present": ["fresh_water_exposure_14d"],
        },
        "exposure": {
            "freshwater_exposure_within_14d": True,
            "freshwater_exposure_type": "river",
            "altitude_exposure_within_7d_m": None,
            "pork_consumption_or_taenia_contact": False,
            "mosquito_endemic_area_exposure": False,
            "immunocompromise_status": "none",
            "hiv_status": "negative",
            "cd4_count_cells_per_uL": None,
        },
        "vitals": {
            "temperature_celsius": 39.9,
            "heart_rate_bpm": 146,
            "systolic_bp_mmHg": 90,
            "diastolic_bp_mmHg": 54,
            "glasgow_coma_scale": 6,
            "oxygen_saturation_pct": 91,
            "respiratory_rate_breaths_per_min": 36,
        },
        "exam": {
            "mental_status_grade": "comatose",
            "neck_stiffness": True,
            "kernig_or_brudzinski_positive": True,
            "focal_neurological_deficit": False,
            "cranial_nerve_palsy": "none",
            "skin_lesion_centrofacial_chronic": False,
            "petechial_or_purpuric_rash": False,
            "papilledema_on_fundoscopy": True,
        },
        "labs": {
            "wbc_blood_per_uL": 19400,
            "platelets_per_uL": 184000,
            "alt_ast_U_per_L": 48,
            "crp_mg_per_L": 124.0,
            "procalcitonin_ng_per_mL": 5.2,
            "serum_sodium_mEq_per_L": 131,
        },
        "csf": {
            "opening_pressure_cmH2O": 50.0,
            "csf_wbc_per_mm3": 5200,
            "csf_neutrophil_pct": 96,
            "csf_lymphocyte_pct": 3,
            "csf_eosinophil_pct": 1,
            "csf_glucose_mg_per_dL": 10,
            "csf_protein_mg_per_dL": 460,
            "csf_lactate_mmol_per_L": 9.6,
            "csf_ada_U_per_L": None,
            "csf_crag_lfa_result": "negative",
            "csf_wet_mount_motile_amoebae": "positive",
            "csf_xanthochromia_present": False,
            "csf_rbc_per_mm3": 1240,
            "csf_rbc_decreasing_across_tubes": None,
        },
        "imaging": {
            "imaging_modality": "mri_with_dwi_flair",
            "imaging_pattern": "diffuse_cerebral_edema_basilar_meningeal_enhancement",
            "imaging_finding_count": None,
            "imaging_text_summary": (
                "Diffuse cerebral edema with effacement of cortical sulci "
                "and basal cistern obliteration; multifocal cortical and "
                "thalamic hemorrhagic foci; early signs of cerebellar "
                "tonsillar herniation; findings consistent with severe "
                "primary amebic meningoencephalitis."
            ),
        },
        "diagnostic_tests": {
            "results": [
                {
                    "test_name": "CSF wet mount microscopy",
                    "result": (
                        "Numerous motile trophozoites consistent with "
                        "Naegleria fowleri."
                    ),
                    "sensitivity_pct": None,
                    "specificity_pct": None,
                    "citation_pmid_or_doi": "PMID:37460088",
                },
                {
                    "test_name": "CSF Naegleria fowleri real-time PCR (CDC reference laboratory)",
                    "result": "Positive (cycle threshold 19)",
                    "sensitivity_pct": 95.0,
                    "specificity_pct": 99.0,
                    "citation_pmid_or_doi": "PMID:37460088",
                },
                {
                    "test_name": "Source-water environmental sampling (Elkhorn River, Nebraska Department of Health and Human Services)",
                    "result": (
                        "N. fowleri PCR-positive in water samples collected "
                        "from the recreational site within two weeks of the "
                        "case."
                    ),
                    "sensitivity_pct": None,
                    "specificity_pct": None,
                    "citation_pmid_or_doi": "DOI:10.4269/ajtmh.23-0211",
                },
            ],
        },
        "narrative_en": (
            "Eight-year-old previously healthy male from eastern Nebraska "
            "presented in coma after a six-day course of fever, severe "
            "headache, vomiting, increasing lethargy, and one witnessed "
            "generalized seizure on the morning of admission, with "
            "river-recreation exposure on the Elkhorn River approximately "
            "six days before symptom onset. Examination showed temperature "
            "39.9 C, tachycardia, hypotension, neck stiffness, "
            "papilledema, and a Glasgow Coma Scale of 6. Cerebrospinal "
            "fluid showed opening pressure 50 cmH2O, white blood cell "
            "count 5,200 per cubic millimeter (96 percent neutrophils), "
            "glucose 10 mg/dL, protein 460 mg/dL, lactate 9.6 mmol/L, "
            "and numerous motile trophozoites on wet mount; CDC "
            "reference laboratory CSF real-time PCR confirmed Naegleria "
            "fowleri. Environmental sampling of the implicated river "
            "site returned positive N. fowleri PCR. The CDC six-drug "
            "protocol was initiated within an hour of admission; the "
            "child died on hospital day two."
        ),
        "narrative_es": (
            "Niño previamente sano de 8 años, residente en el este de "
            "Nebraska, que ingresó en coma tras cuadro de seis días de "
            "fiebre, cefalea severa, vómitos, letargia creciente y una "
            "crisis generalizada presenciada en la mañana del ingreso, "
            "con exposición recreativa al río Elkhorn aproximadamente "
            "seis días antes del inicio de síntomas. El examen mostró "
            "temperatura 39.9 C, taquicardia, hipotensión, rigidez de "
            "nuca, papiledema y escala de Glasgow de 6. El líquido "
            "cefalorraquídeo mostró presión de apertura 50 cmH2O, "
            "leucocitos 5,200 por mm3 (96 por ciento neutrófilos), "
            "glucosa 10 mg/dL, proteína 460 mg/dL, lactato 9.6 mmol/L "
            "y abundantes trofozoítos móviles en frotis directo; PCR "
            "de Naegleria fowleri en LCR confirmada en el laboratorio "
            "de referencia de los CDC. El muestreo ambiental del sitio "
            "ribereño implicado fue positivo por PCR para N. fowleri. "
            "Se inició el protocolo de seis fármacos de los CDC en la "
            "primera hora del ingreso; el niño falleció en el día "
            "hospitalario dos."
        ),
    }


def _build_vignette_008() -> dict[str, Any]:
    """Vignette 8: 9-year-old male, Minnesota lake, mid stage, fatal.

    Anchored to Kemble Clin Infect Dis 2012 Minnesota lake-associated PAM
    (PMID 22238170). Mid-stage presentation contrasts vignette 5's
    late-stage course in the same northern-range cluster.
    """
    return {
        "history": {
            "symptom_onset_to_presentation_days": 4.0,
            "chief_complaint": "fever_with_headache",
            "prodrome_description": (
                "Three days of fever, severe headache, photophobia, and "
                "vomiting after lake swimming during summer camp "
                "approximately five days before symptom onset; new-onset "
                "neck stiffness and intermittent confusion in the 12 "
                "hours before admission."
            ),
            "red_flags_present": ["fresh_water_exposure_14d"],
        },
        "exposure": {
            "freshwater_exposure_within_14d": True,
            "freshwater_exposure_type": "lake",
            "altitude_exposure_within_7d_m": None,
            "pork_consumption_or_taenia_contact": False,
            "mosquito_endemic_area_exposure": False,
            "immunocompromise_status": "none",
            "hiv_status": "negative",
            "cd4_count_cells_per_uL": None,
        },
        "vitals": {
            "temperature_celsius": 39.6,
            "heart_rate_bpm": 132,
            "systolic_bp_mmHg": 110,
            "diastolic_bp_mmHg": 68,
            "glasgow_coma_scale": 13,
            "oxygen_saturation_pct": 97,
            "respiratory_rate_breaths_per_min": 24,
        },
        "exam": {
            "mental_status_grade": "confused",
            "neck_stiffness": True,
            "kernig_or_brudzinski_positive": True,
            "focal_neurological_deficit": False,
            "cranial_nerve_palsy": "none",
            "skin_lesion_centrofacial_chronic": False,
            "petechial_or_purpuric_rash": False,
            "papilledema_on_fundoscopy": False,
        },
        "labs": {
            "wbc_blood_per_uL": 13800,
            "platelets_per_uL": 256000,
            "alt_ast_U_per_L": 28,
            "crp_mg_per_L": 60.0,
            "procalcitonin_ng_per_mL": 1.5,
            "serum_sodium_mEq_per_L": 138,
        },
        "csf": {
            "opening_pressure_cmH2O": 28.0,
            "csf_wbc_per_mm3": 2000,
            "csf_neutrophil_pct": 92,
            "csf_lymphocyte_pct": 6,
            "csf_eosinophil_pct": 2,
            "csf_glucose_mg_per_dL": 28,
            "csf_protein_mg_per_dL": 220,
            "csf_lactate_mmol_per_L": 5.4,
            "csf_ada_U_per_L": None,
            "csf_crag_lfa_result": "negative",
            "csf_wet_mount_motile_amoebae": "positive",
            "csf_xanthochromia_present": False,
            "csf_rbc_per_mm3": 140,
            "csf_rbc_decreasing_across_tubes": None,
        },
        "imaging": {
            "imaging_modality": "mri_with_dwi_flair",
            "imaging_pattern": "normal",
            "imaging_finding_count": None,
            "imaging_text_summary": (
                "MRI brain with FLAIR and DWI showing no parenchymal "
                "abnormality, no mass effect, no restricted diffusion, "
                "and no abnormal meningeal enhancement; study read as "
                "normal."
            ),
        },
        "diagnostic_tests": {
            "results": [
                {
                    "test_name": "CSF wet mount microscopy",
                    "result": (
                        "Motile trophozoites consistent with Naegleria "
                        "fowleri identified at bedside."
                    ),
                    "sensitivity_pct": None,
                    "specificity_pct": None,
                    "citation_pmid_or_doi": "PMID:22238170",
                },
                {
                    "test_name": "CSF Naegleria fowleri real-time PCR (CDC reference laboratory)",
                    "result": "Positive",
                    "sensitivity_pct": 95.0,
                    "specificity_pct": 99.0,
                    "citation_pmid_or_doi": "PMID:22238170",
                },
            ],
        },
        "narrative_en": (
            "Nine-year-old previously healthy male presented with four "
            "days of fever, severe headache, photophobia, and vomiting "
            "after lake swimming during summer camp approximately five "
            "days before symptom onset. On the day of admission he "
            "developed neck stiffness and intermittent confusion. "
            "Examination showed temperature 39.6 C, tachycardia, neck "
            "stiffness, positive Kernig sign, and a Glasgow Coma Scale "
            "of 13. Cerebrospinal fluid showed opening pressure 28 "
            "cmH2O, white blood cell count 2,000 per cubic millimeter "
            "(92 percent neutrophils), glucose 28 mg/dL, protein 220 "
            "mg/dL, lactate 5.4 mmol/L, and motile trophozoites on wet "
            "mount; CDC reference laboratory CSF real-time PCR confirmed "
            "Naegleria fowleri. The CDC six-drug protocol was initiated "
            "within three hours of admission; the child progressed to "
            "stuporous mental status overnight and died on hospital day "
            "five despite aggressive therapy."
        ),
        "narrative_es": (
            "Niño previamente sano de 9 años que presentó cuatro días "
            "de fiebre, cefalea severa, fotofobia y vómitos tras nadar "
            "en lago durante campamento de verano aproximadamente cinco "
            "días antes del inicio de síntomas. El día del ingreso "
            "desarrolló rigidez de nuca y confusión intermitente. El "
            "examen mostró temperatura 39.6 C, taquicardia, rigidez de "
            "nuca, signo de Kernig positivo y escala de Glasgow de 13. "
            "El líquido cefalorraquídeo mostró presión de apertura 28 "
            "cmH2O, leucocitos 2,000 por mm3 (92 por ciento "
            "neutrófilos), glucosa 28 mg/dL, proteína 220 mg/dL, "
            "lactato 5.4 mmol/L y trofozoítos móviles en frotis "
            "directo; PCR de Naegleria fowleri en LCR confirmada en el "
            "laboratorio de referencia de los CDC. Se inició el "
            "protocolo de seis fármacos de los CDC en las primeras "
            "tres horas; el niño progresó a estado estuporoso durante "
            "la noche y falleció en el día hospitalario cinco a pesar "
            "de la terapia agresiva."
        ),
    }


def _build_vignette_009() -> dict[str, Any]:
    """Vignette 9: 14-year-old male, Florida lake, late stage, fatal.

    Anchored to Anjum IDCases 2021 north Florida adolescent freshwater
    PAM (PMID 34307045). Late-stage adolescent presentation contrasts
    vignette 6's mid-stage course in the same Florida cluster.
    """
    return {
        "history": {
            "symptom_onset_to_presentation_days": 6.0,
            "chief_complaint": "altered_mental_status",
            "prodrome_description": (
                "Five days of fever, severe headache, photophobia, "
                "vomiting, and increasing lethargy after lake swimming "
                "and underwater diving approximately one week before "
                "symptom onset; one witnessed generalized seizure 18 "
                "hours before admission with progressive obtundation."
            ),
            "red_flags_present": ["fresh_water_exposure_14d"],
        },
        "exposure": {
            "freshwater_exposure_within_14d": True,
            "freshwater_exposure_type": "lake",
            "altitude_exposure_within_7d_m": None,
            "pork_consumption_or_taenia_contact": False,
            "mosquito_endemic_area_exposure": False,
            "immunocompromise_status": "none",
            "hiv_status": "negative",
            "cd4_count_cells_per_uL": None,
        },
        "vitals": {
            "temperature_celsius": 39.8,
            "heart_rate_bpm": 128,
            "systolic_bp_mmHg": 102,
            "diastolic_bp_mmHg": 60,
            "glasgow_coma_scale": 7,
            "oxygen_saturation_pct": 93,
            "respiratory_rate_breaths_per_min": 28,
        },
        "exam": {
            "mental_status_grade": "stuporous",
            "neck_stiffness": True,
            "kernig_or_brudzinski_positive": True,
            "focal_neurological_deficit": False,
            "cranial_nerve_palsy": "none",
            "skin_lesion_centrofacial_chronic": False,
            "petechial_or_purpuric_rash": False,
            "papilledema_on_fundoscopy": True,
        },
        "labs": {
            "wbc_blood_per_uL": 17800,
            "platelets_per_uL": 218000,
            "alt_ast_U_per_L": 40,
            "crp_mg_per_L": 104.0,
            "procalcitonin_ng_per_mL": 4.0,
            "serum_sodium_mEq_per_L": 132,
        },
        "csf": {
            "opening_pressure_cmH2O": 44.0,
            "csf_wbc_per_mm3": 4200,
            "csf_neutrophil_pct": 95,
            "csf_lymphocyte_pct": 4,
            "csf_eosinophil_pct": 1,
            "csf_glucose_mg_per_dL": 14,
            "csf_protein_mg_per_dL": 400,
            "csf_lactate_mmol_per_L": 8.6,
            "csf_ada_U_per_L": None,
            "csf_crag_lfa_result": "negative",
            "csf_wet_mount_motile_amoebae": "positive",
            "csf_xanthochromia_present": False,
            "csf_rbc_per_mm3": 680,
            "csf_rbc_decreasing_across_tubes": None,
        },
        "imaging": {
            "imaging_modality": "mri_with_dwi_flair",
            "imaging_pattern": "diffuse_cerebral_edema_basilar_meningeal_enhancement",
            "imaging_finding_count": None,
            "imaging_text_summary": (
                "Diffuse cerebral edema with effacement of cortical sulci, "
                "basal cistern enhancement, and small bilateral temporal "
                "hemorrhagic foci; pattern consistent with primary amebic "
                "meningoencephalitis."
            ),
        },
        "diagnostic_tests": {
            "results": [
                {
                    "test_name": "CSF wet mount microscopy",
                    "result": (
                        "Motile trophozoites consistent with Naegleria "
                        "fowleri identified at bedside on warmed slide."
                    ),
                    "sensitivity_pct": None,
                    "specificity_pct": None,
                    "citation_pmid_or_doi": "PMID:34307045",
                },
                {
                    "test_name": "CSF Naegleria fowleri real-time PCR (CDC reference laboratory)",
                    "result": "Positive (cycle threshold 22)",
                    "sensitivity_pct": 95.0,
                    "specificity_pct": 99.0,
                    "citation_pmid_or_doi": "PMID:34307045",
                },
            ],
        },
        "narrative_en": (
            "Fourteen-year-old previously healthy male from north Florida "
            "presented in stuporous mental status after a six-day course "
            "of fever, severe headache, photophobia, vomiting, and "
            "progressive lethargy following lake swimming and underwater "
            "diving approximately one week before symptom onset, plus one "
            "witnessed generalized seizure 18 hours before admission. "
            "Examination showed temperature 39.8 C, tachycardia, neck "
            "stiffness, papilledema, and a Glasgow Coma Scale of 7. "
            "Cerebrospinal fluid showed opening pressure 44 cmH2O, white "
            "blood cell count 4,200 per cubic millimeter (95 percent "
            "neutrophils), glucose 14 mg/dL, protein 400 mg/dL, lactate "
            "8.6 mmol/L, and motile trophozoites on wet mount; CDC "
            "reference laboratory CSF real-time PCR confirmed Naegleria "
            "fowleri. The CDC six-drug protocol and intracranial "
            "pressure management were initiated within two hours of "
            "admission; the patient died on hospital day three after "
            "rapid neurologic deterioration."
        ),
        "narrative_es": (
            "Adolescente varón previamente sano de 14 años, residente "
            "en el norte de Florida, que ingresó en estado estuporoso "
            "tras cuadro de seis días de fiebre, cefalea severa, "
            "fotofobia, vómitos y letargia progresiva tras nadar y "
            "bucear en lago aproximadamente una semana antes del "
            "inicio de síntomas, más una crisis generalizada "
            "presenciada 18 horas antes del ingreso. El examen mostró "
            "temperatura 39.8 C, taquicardia, rigidez de nuca, "
            "papiledema y escala de Glasgow de 7. El líquido "
            "cefalorraquídeo mostró presión de apertura 44 cmH2O, "
            "leucocitos 4,200 por mm3 (95 por ciento neutrófilos), "
            "glucosa 14 mg/dL, proteína 400 mg/dL, lactato 8.6 mmol/L "
            "y trofozoítos móviles en frotis directo; PCR de Naegleria "
            "fowleri en LCR confirmada en el laboratorio de referencia "
            "de los CDC. Se inició el protocolo de seis fármacos de "
            "los CDC y manejo de presión intracraneal en las primeras "
            "dos horas; el paciente falleció en el día hospitalario "
            "tres tras deterioro neurológico rápido."
        ),
    }


def _build_vignette_010() -> dict[str, Any]:
    """Vignette 10: 28-year-old male, Louisiana neti-pot, mid stage, fatal.

    Anchored to Yoder Clin Infect Dis 2012 (PMID 22919000). Sinus
    irrigation with contaminated tap water as exposure route.
    """
    return {
        "history": {
            "symptom_onset_to_presentation_days": 4.0,
            "chief_complaint": "fever_with_headache",
            "prodrome_description": (
                "Three days of fever, severe frontal headache, "
                "photophobia, and one episode of emesis after several "
                "weeks of daily nasal irrigation with a neti pot filled "
                "with municipal tap water; on the day of admission he "
                "developed neck stiffness and increasing somnolence."
            ),
            "red_flags_present": ["fresh_water_exposure_14d"],
        },
        "exposure": {
            "freshwater_exposure_within_14d": True,
            "freshwater_exposure_type": "neti_pot_tap_water",
            "altitude_exposure_within_7d_m": None,
            "pork_consumption_or_taenia_contact": False,
            "mosquito_endemic_area_exposure": False,
            "immunocompromise_status": "none",
            "hiv_status": "negative",
            "cd4_count_cells_per_uL": None,
        },
        "vitals": {
            "temperature_celsius": 39.6,
            "heart_rate_bpm": 122,
            "systolic_bp_mmHg": 116,
            "diastolic_bp_mmHg": 70,
            "glasgow_coma_scale": 12,
            "oxygen_saturation_pct": 96,
            "respiratory_rate_breaths_per_min": 22,
        },
        "exam": {
            "mental_status_grade": "somnolent",
            "neck_stiffness": True,
            "kernig_or_brudzinski_positive": True,
            "focal_neurological_deficit": False,
            "cranial_nerve_palsy": "none",
            "skin_lesion_centrofacial_chronic": False,
            "petechial_or_purpuric_rash": False,
            "papilledema_on_fundoscopy": False,
        },
        "labs": {
            "wbc_blood_per_uL": 16800,
            "platelets_per_uL": 232000,
            "alt_ast_U_per_L": 36,
            "crp_mg_per_L": 96.0,
            "procalcitonin_ng_per_mL": 3.4,
            "serum_sodium_mEq_per_L": 135,
        },
        "csf": {
            "opening_pressure_cmH2O": 30.0,
            "csf_wbc_per_mm3": 2400,
            "csf_neutrophil_pct": 92,
            "csf_lymphocyte_pct": 6,
            "csf_eosinophil_pct": 2,
            "csf_glucose_mg_per_dL": 26,
            "csf_protein_mg_per_dL": 240,
            "csf_lactate_mmol_per_L": 6.2,
            "csf_ada_U_per_L": None,
            "csf_crag_lfa_result": "negative",
            "csf_wet_mount_motile_amoebae": "positive",
            "csf_xanthochromia_present": False,
            "csf_rbc_per_mm3": 320,
            "csf_rbc_decreasing_across_tubes": None,
        },
        "imaging": {
            "imaging_modality": "mri_with_dwi_flair",
            "imaging_pattern": "diffuse_cerebral_edema_basilar_meningeal_enhancement",
            "imaging_finding_count": None,
            "imaging_text_summary": (
                "MRI brain with FLAIR and DWI showing basal cistern "
                "enhancement and early diffuse cerebral edema without "
                "focal hemorrhage; pattern consistent with primary "
                "amebic meningoencephalitis."
            ),
        },
        "diagnostic_tests": {
            "results": [
                {
                    "test_name": "CSF wet mount microscopy",
                    "result": (
                        "Motile trophozoites consistent with Naegleria "
                        "fowleri identified at bedside on warmed slide."
                    ),
                    "sensitivity_pct": None,
                    "specificity_pct": None,
                    "citation_pmid_or_doi": "PMID:22919000",
                },
                {
                    "test_name": "CSF Naegleria fowleri real-time PCR (CDC reference laboratory)",
                    "result": "Positive (cycle threshold 23)",
                    "sensitivity_pct": 95.0,
                    "specificity_pct": 99.0,
                    "citation_pmid_or_doi": "PMID:22919000",
                },
                {
                    "test_name": "Household tap-water environmental sampling",
                    "result": (
                        "N. fowleri PCR-positive in household plumbing "
                        "samples used to fill the neti pot."
                    ),
                    "sensitivity_pct": None,
                    "specificity_pct": None,
                    "citation_pmid_or_doi": "PMID:22919000",
                },
            ],
        },
        "narrative_en": (
            "Twenty-eight-year-old previously healthy male from southern "
            "Louisiana presented with three days of fever, severe frontal "
            "headache, photophobia, and a single episode of emesis "
            "following several weeks of daily nasal irrigation with a "
            "neti pot filled with municipal tap water. On the day of "
            "admission he developed neck stiffness and progressive "
            "somnolence. Examination showed temperature 39.6 C, "
            "tachycardia, neck stiffness, positive Kernig sign, and a "
            "Glasgow Coma Scale of 12. Cerebrospinal fluid showed "
            "opening pressure 30 cmH2O, white blood cell count 2,400 "
            "per cubic millimeter (92 percent neutrophils), glucose 26 "
            "mg/dL, protein 240 mg/dL, lactate 6.2 mmol/L, and motile "
            "trophozoites on wet mount; CDC reference laboratory CSF "
            "real-time PCR confirmed Naegleria fowleri. Environmental "
            "sampling of household plumbing returned N. fowleri "
            "PCR-positive. The CDC six-drug protocol was initiated "
            "within four hours of admission; the patient progressed to "
            "coma overnight and died on hospital day five."
        ),
        "narrative_es": (
            "Varón previamente sano de 28 años, residente en el sur "
            "de Luisiana, que presentó tres días de fiebre, cefalea "
            "frontal severa, fotofobia y un episodio de emesis tras "
            "varias semanas de irrigación nasal diaria con neti pot "
            "llenado con agua de la red municipal. El día del ingreso "
            "desarrolló rigidez de nuca y somnolencia progresiva. El "
            "examen mostró temperatura 39.6 C, taquicardia, rigidez "
            "de nuca, signo de Kernig positivo y escala de Glasgow "
            "de 12. El líquido cefalorraquídeo mostró presión de "
            "apertura 30 cmH2O, leucocitos 2,400 por mm3 (92 por "
            "ciento neutrófilos), glucosa 26 mg/dL, proteína 240 "
            "mg/dL, lactato 6.2 mmol/L y trofozoítos móviles en "
            "frotis directo; PCR de Naegleria fowleri en LCR "
            "confirmada en el laboratorio de referencia de los CDC. "
            "El muestreo ambiental de la red domiciliaria fue "
            "positivo para N. fowleri por PCR. Se inició el protocolo "
            "de seis fármacos de los CDC en las primeras cuatro "
            "horas; el paciente progresó a coma durante la noche y "
            "falleció en el día hospitalario cinco."
        ),
    }


def _build_vignette_011() -> dict[str, Any]:
    """Vignette 11: 51-year-old female, Louisiana neti-pot, late, fatal."""
    return {
        "history": {
            "symptom_onset_to_presentation_days": 5.5,
            "chief_complaint": "altered_mental_status",
            "prodrome_description": (
                "Five days of fever, severe headache, vomiting, and "
                "increasing confusion following habitual neti-pot use "
                "with untreated household tap water; family found her "
                "unresponsive on the morning of admission with one "
                "witnessed generalized seizure during transport."
            ),
            "red_flags_present": ["fresh_water_exposure_14d"],
        },
        "exposure": {
            "freshwater_exposure_within_14d": True,
            "freshwater_exposure_type": "neti_pot_tap_water",
            "altitude_exposure_within_7d_m": None,
            "pork_consumption_or_taenia_contact": False,
            "mosquito_endemic_area_exposure": False,
            "immunocompromise_status": "none",
            "hiv_status": "negative",
            "cd4_count_cells_per_uL": None,
        },
        "vitals": {
            "temperature_celsius": 39.8,
            "heart_rate_bpm": 134,
            "systolic_bp_mmHg": 92,
            "diastolic_bp_mmHg": 56,
            "glasgow_coma_scale": 6,
            "oxygen_saturation_pct": 92,
            "respiratory_rate_breaths_per_min": 30,
        },
        "exam": {
            "mental_status_grade": "comatose",
            "neck_stiffness": True,
            "kernig_or_brudzinski_positive": True,
            "focal_neurological_deficit": False,
            "cranial_nerve_palsy": "none",
            "skin_lesion_centrofacial_chronic": False,
            "petechial_or_purpuric_rash": False,
            "papilledema_on_fundoscopy": True,
        },
        "labs": {
            "wbc_blood_per_uL": 19200,
            "platelets_per_uL": 196000,
            "alt_ast_U_per_L": 52,
            "crp_mg_per_L": 132.0,
            "procalcitonin_ng_per_mL": 5.6,
            "serum_sodium_mEq_per_L": 130,
        },
        "csf": {
            "opening_pressure_cmH2O": 48.0,
            "csf_wbc_per_mm3": 4800,
            "csf_neutrophil_pct": 96,
            "csf_lymphocyte_pct": 3,
            "csf_eosinophil_pct": 1,
            "csf_glucose_mg_per_dL": 12,
            "csf_protein_mg_per_dL": 440,
            "csf_lactate_mmol_per_L": 9.0,
            "csf_ada_U_per_L": None,
            "csf_crag_lfa_result": "negative",
            "csf_wet_mount_motile_amoebae": "positive",
            "csf_xanthochromia_present": False,
            "csf_rbc_per_mm3": 980,
            "csf_rbc_decreasing_across_tubes": None,
        },
        "imaging": {
            "imaging_modality": "ct_noncontrast",
            "imaging_pattern": "diffuse_cerebral_edema_basilar_meningeal_enhancement",
            "imaging_finding_count": None,
            "imaging_text_summary": (
                "Non-contrast CT head showing diffuse cerebral edema "
                "with effacement of cortical sulci and basal cistern "
                "obliteration; small bilateral frontal hemorrhagic foci; "
                "early signs of transtentorial herniation."
            ),
        },
        "diagnostic_tests": {
            "results": [
                {
                    "test_name": "CSF wet mount microscopy",
                    "result": (
                        "Numerous motile trophozoites consistent with "
                        "Naegleria fowleri."
                    ),
                    "sensitivity_pct": None,
                    "specificity_pct": None,
                    "citation_pmid_or_doi": "PMID:22919000",
                },
                {
                    "test_name": "CSF Naegleria fowleri real-time PCR (CDC reference laboratory)",
                    "result": "Positive (cycle threshold 18)",
                    "sensitivity_pct": 95.0,
                    "specificity_pct": 99.0,
                    "citation_pmid_or_doi": "PMID:22919000",
                },
                {
                    "test_name": "Household tap-water environmental sampling",
                    "result": (
                        "N. fowleri PCR-positive in plumbing samples "
                        "from the patient's residence."
                    ),
                    "sensitivity_pct": None,
                    "specificity_pct": None,
                    "citation_pmid_or_doi": "PMID:22919000",
                },
            ],
        },
        "narrative_en": (
            "Fifty-one-year-old previously healthy female from southern "
            "Louisiana presented in coma after a five-day course of "
            "fever, severe headache, vomiting, and progressive "
            "confusion in the setting of habitual neti-pot use with "
            "untreated household tap water. Family found her "
            "unresponsive on the morning of admission, with one "
            "witnessed generalized seizure during emergency transport. "
            "Examination showed temperature 39.8 C, tachycardia, "
            "hypotension, neck stiffness, papilledema, and a Glasgow "
            "Coma Scale of 6. Cerebrospinal fluid showed opening "
            "pressure 48 cmH2O, white blood cell count 4,800 per cubic "
            "millimeter (96 percent neutrophils), glucose 12 mg/dL, "
            "protein 440 mg/dL, lactate 9.0 mmol/L, and numerous motile "
            "trophozoites on wet mount; CDC reference laboratory CSF "
            "real-time PCR confirmed Naegleria fowleri. Environmental "
            "sampling of household plumbing returned N. fowleri "
            "PCR-positive. The CDC six-drug protocol and aggressive "
            "intracranial pressure management were initiated within "
            "the first hour of admission; the patient died on hospital "
            "day two after withdrawal of care for established brain "
            "death."
        ),
        "narrative_es": (
            "Mujer previamente sana de 51 años, residente en el sur "
            "de Luisiana, que ingresó en coma tras cuadro de cinco "
            "días de fiebre, cefalea severa, vómitos y confusión "
            "progresiva en el contexto de uso habitual de neti pot "
            "con agua de la red domiciliaria sin tratar. La familia "
            "la encontró sin respuesta en la mañana del ingreso, con "
            "una crisis generalizada presenciada durante el traslado. "
            "El examen mostró temperatura 39.8 C, taquicardia, "
            "hipotensión, rigidez de nuca, papiledema y escala de "
            "Glasgow de 6. El líquido cefalorraquídeo mostró presión "
            "de apertura 48 cmH2O, leucocitos 4,800 por mm3 (96 por "
            "ciento neutrófilos), glucosa 12 mg/dL, proteína 440 "
            "mg/dL, lactato 9.0 mmol/L y abundantes trofozoítos "
            "móviles en frotis directo; PCR de Naegleria fowleri en "
            "LCR confirmada en el laboratorio de referencia de los "
            "CDC. El muestreo ambiental de la red domiciliaria fue "
            "positivo para N. fowleri por PCR. Se inició el protocolo "
            "de seis fármacos de los CDC y manejo agresivo de "
            "presión intracraneal en la primera hora del ingreso; la "
            "paciente falleció en el día hospitalario dos tras retiro "
            "de soporte por muerte encefálica establecida."
        ),
    }


def _build_vignette_012() -> dict[str, Any]:
    """Vignette 12: 71-year-old female, Texas RV-plumbing nasal rinse, mid, fatal.

    Anchored to Smith MMWR 2025 (PMID 40440212). Atypical exposure
    route: recreational vehicle freshwater plumbing used for nasal
    irrigation rather than a recreational aquatic activity.
    """
    return {
        "history": {
            "symptom_onset_to_presentation_days": 4.5,
            "chief_complaint": "fever_with_headache",
            "prodrome_description": (
                "Four days of fever, severe headache, photophobia, "
                "vomiting, and progressive lethargy after several days "
                "of nasal irrigation using water drawn from a "
                "recreational vehicle freshwater holding tank during "
                "an extended camping trip; no recreational swimming or "
                "lake exposure documented."
            ),
            "red_flags_present": ["fresh_water_exposure_14d"],
        },
        "exposure": {
            "freshwater_exposure_within_14d": True,
            "freshwater_exposure_type": "neti_pot_tap_water",
            "altitude_exposure_within_7d_m": None,
            "pork_consumption_or_taenia_contact": False,
            "mosquito_endemic_area_exposure": False,
            "immunocompromise_status": "none",
            "hiv_status": "negative",
            "cd4_count_cells_per_uL": None,
        },
        "vitals": {
            "temperature_celsius": 39.4,
            "heart_rate_bpm": 118,
            "systolic_bp_mmHg": 122,
            "diastolic_bp_mmHg": 72,
            "glasgow_coma_scale": 11,
            "oxygen_saturation_pct": 95,
            "respiratory_rate_breaths_per_min": 24,
        },
        "exam": {
            "mental_status_grade": "somnolent",
            "neck_stiffness": True,
            "kernig_or_brudzinski_positive": True,
            "focal_neurological_deficit": False,
            "cranial_nerve_palsy": "none",
            "skin_lesion_centrofacial_chronic": False,
            "petechial_or_purpuric_rash": False,
            "papilledema_on_fundoscopy": False,
        },
        "labs": {
            "wbc_blood_per_uL": 17400,
            "platelets_per_uL": 224000,
            "alt_ast_U_per_L": 38,
            "crp_mg_per_L": 108.0,
            "procalcitonin_ng_per_mL": 4.2,
            "serum_sodium_mEq_per_L": 134,
        },
        "csf": {
            "opening_pressure_cmH2O": 32.0,
            "csf_wbc_per_mm3": 2800,
            "csf_neutrophil_pct": 91,
            "csf_lymphocyte_pct": 7,
            "csf_eosinophil_pct": 2,
            "csf_glucose_mg_per_dL": 24,
            "csf_protein_mg_per_dL": 260,
            "csf_lactate_mmol_per_L": 6.4,
            "csf_ada_U_per_L": None,
            "csf_crag_lfa_result": "negative",
            "csf_wet_mount_motile_amoebae": "positive",
            "csf_xanthochromia_present": False,
            "csf_rbc_per_mm3": 280,
            "csf_rbc_decreasing_across_tubes": None,
        },
        "imaging": {
            "imaging_modality": "mri_with_dwi_flair",
            "imaging_pattern": "diffuse_cerebral_edema_basilar_meningeal_enhancement",
            "imaging_finding_count": None,
            "imaging_text_summary": (
                "MRI brain with FLAIR and DWI showing basal cistern "
                "enhancement, sulcal effacement, and early diffuse "
                "cerebral edema without focal hemorrhage; pattern "
                "consistent with primary amebic meningoencephalitis."
            ),
        },
        "diagnostic_tests": {
            "results": [
                {
                    "test_name": "CSF wet mount microscopy",
                    "result": (
                        "Motile trophozoites consistent with Naegleria "
                        "fowleri identified within 30 minutes of CSF "
                        "collection."
                    ),
                    "sensitivity_pct": None,
                    "specificity_pct": None,
                    "citation_pmid_or_doi": "PMID:40440212",
                },
                {
                    "test_name": "CSF Naegleria fowleri real-time PCR (CDC reference laboratory)",
                    "result": "Positive (cycle threshold 21)",
                    "sensitivity_pct": 95.0,
                    "specificity_pct": 99.0,
                    "citation_pmid_or_doi": "PMID:40440212",
                },
                {
                    "test_name": "RV freshwater holding tank environmental sampling",
                    "result": (
                        "N. fowleri PCR-positive in water drawn from "
                        "the RV freshwater plumbing used by the "
                        "patient."
                    ),
                    "sensitivity_pct": None,
                    "specificity_pct": None,
                    "citation_pmid_or_doi": "PMID:40440212",
                },
            ],
        },
        "narrative_en": (
            "Seventy-one-year-old previously healthy female from north "
            "Texas presented with four days of fever, severe headache, "
            "photophobia, vomiting, and progressive lethargy after "
            "several days of nasal irrigation using water drawn from a "
            "recreational vehicle freshwater holding tank during an "
            "extended camping trip, with no recreational swimming or "
            "lake exposure documented. Examination showed temperature "
            "39.4 C, tachycardia, neck stiffness, positive Kernig sign, "
            "and a Glasgow Coma Scale of 11. Cerebrospinal fluid showed "
            "opening pressure 32 cmH2O, white blood cell count 2,800 "
            "per cubic millimeter (91 percent neutrophils), glucose 24 "
            "mg/dL, protein 260 mg/dL, lactate 6.4 mmol/L, and motile "
            "trophozoites on wet mount; CDC reference laboratory CSF "
            "real-time PCR confirmed Naegleria fowleri. Environmental "
            "sampling of the RV freshwater plumbing returned N. fowleri "
            "PCR-positive. The CDC six-drug protocol was initiated "
            "within three hours of admission; the patient progressed "
            "to coma within 36 hours and died on hospital day four "
            "despite aggressive intracranial pressure management."
        ),
        "narrative_es": (
            "Mujer previamente sana de 71 años, residente en el norte "
            "de Texas, que presentó cuatro días de fiebre, cefalea "
            "severa, fotofobia, vómitos y letargia progresiva tras "
            "varios días de irrigación nasal con agua extraída del "
            "tanque de agua dulce de un vehículo recreativo durante "
            "una salida de camping prolongada, sin exposición "
            "recreativa a piscina o lago documentada. El examen "
            "mostró temperatura 39.4 C, taquicardia, rigidez de nuca, "
            "signo de Kernig positivo y escala de Glasgow de 11. El "
            "líquido cefalorraquídeo mostró presión de apertura 32 "
            "cmH2O, leucocitos 2,800 por mm3 (91 por ciento "
            "neutrófilos), glucosa 24 mg/dL, proteína 260 mg/dL, "
            "lactato 6.4 mmol/L y trofozoítos móviles en frotis "
            "directo; PCR de Naegleria fowleri en LCR confirmada en "
            "el laboratorio de referencia de los CDC. El muestreo "
            "ambiental del tanque de agua dulce del vehículo "
            "recreativo fue positivo para N. fowleri por PCR. Se "
            "inició el protocolo de seis fármacos de los CDC en las "
            "primeras tres horas del ingreso; la paciente progresó "
            "a coma en 36 horas y falleció en el día hospitalario "
            "cuatro a pesar del manejo agresivo de presión "
            "intracraneal."
        ),
    }


def _build_vignette_013() -> dict[str, Any]:
    """Vignette 13: 12-year-old male, California hot spring, mid, fatal.

    Anchored to Vugia MMWR 2019 (PMID 31513557) Inyo County hot-spring
    PAM case.
    """
    return {
        "history": {
            "symptom_onset_to_presentation_days": 4.0,
            "chief_complaint": "fever_with_headache",
            "prodrome_description": (
                "Four days of fever, frontal headache, vomiting, and "
                "increasing irritability after a multi-family camping "
                "trip in eastern California during which the child "
                "swam and submerged his head repeatedly in a "
                "geothermal hot-spring pool approximately six days "
                "before symptom onset."
            ),
            "red_flags_present": ["fresh_water_exposure_14d"],
        },
        "exposure": {
            "freshwater_exposure_within_14d": True,
            "freshwater_exposure_type": "hot_spring",
            "altitude_exposure_within_7d_m": 1200,
            "pork_consumption_or_taenia_contact": False,
            "mosquito_endemic_area_exposure": False,
            "immunocompromise_status": "none",
            "hiv_status": "negative",
            "cd4_count_cells_per_uL": None,
        },
        "vitals": {
            "temperature_celsius": 39.7,
            "heart_rate_bpm": 128,
            "systolic_bp_mmHg": 108,
            "diastolic_bp_mmHg": 64,
            "glasgow_coma_scale": 12,
            "oxygen_saturation_pct": 95,
            "respiratory_rate_breaths_per_min": 24,
        },
        "exam": {
            "mental_status_grade": "somnolent",
            "neck_stiffness": True,
            "kernig_or_brudzinski_positive": True,
            "focal_neurological_deficit": False,
            "cranial_nerve_palsy": "none",
            "skin_lesion_centrofacial_chronic": False,
            "petechial_or_purpuric_rash": False,
            "papilledema_on_fundoscopy": False,
        },
        "labs": {
            "wbc_blood_per_uL": 16400,
            "platelets_per_uL": 238000,
            "alt_ast_U_per_L": 34,
            "crp_mg_per_L": 92.0,
            "procalcitonin_ng_per_mL": 3.2,
            "serum_sodium_mEq_per_L": 134,
        },
        "csf": {
            "opening_pressure_cmH2O": 28.0,
            "csf_wbc_per_mm3": 2200,
            "csf_neutrophil_pct": 90,
            "csf_lymphocyte_pct": 8,
            "csf_eosinophil_pct": 2,
            "csf_glucose_mg_per_dL": 28,
            "csf_protein_mg_per_dL": 220,
            "csf_lactate_mmol_per_L": 5.6,
            "csf_ada_U_per_L": None,
            "csf_crag_lfa_result": "negative",
            "csf_wet_mount_motile_amoebae": "positive",
            "csf_xanthochromia_present": False,
            "csf_rbc_per_mm3": 220,
            "csf_rbc_decreasing_across_tubes": None,
        },
        "imaging": {
            "imaging_modality": "mri_with_dwi_flair",
            "imaging_pattern": "diffuse_cerebral_edema_basilar_meningeal_enhancement",
            "imaging_finding_count": None,
            "imaging_text_summary": (
                "MRI brain with FLAIR and DWI showing basal cistern "
                "enhancement and early diffuse cerebral edema; no "
                "focal hemorrhage; pattern consistent with primary "
                "amebic meningoencephalitis."
            ),
        },
        "diagnostic_tests": {
            "results": [
                {
                    "test_name": "CSF wet mount microscopy",
                    "result": (
                        "Motile trophozoites consistent with Naegleria "
                        "fowleri."
                    ),
                    "sensitivity_pct": None,
                    "specificity_pct": None,
                    "citation_pmid_or_doi": "PMID:31513557",
                },
                {
                    "test_name": "CSF Naegleria fowleri real-time PCR (CDC reference laboratory)",
                    "result": "Positive (cycle threshold 22)",
                    "sensitivity_pct": 95.0,
                    "specificity_pct": 99.0,
                    "citation_pmid_or_doi": "PMID:31513557",
                },
                {
                    "test_name": "Hot-spring environmental sampling (Inyo County Public Health)",
                    "result": (
                        "N. fowleri PCR-positive in water samples from "
                        "the implicated geothermal pool."
                    ),
                    "sensitivity_pct": None,
                    "specificity_pct": None,
                    "citation_pmid_or_doi": "PMID:31513557",
                },
            ],
        },
        "narrative_en": (
            "Twelve-year-old previously healthy male presented with "
            "four days of fever, frontal headache, vomiting, and "
            "increasing irritability after a multi-family camping trip "
            "in Inyo County, eastern California, during which he "
            "swam and repeatedly submerged his head in a geothermal "
            "hot-spring pool approximately six days before symptom "
            "onset. Examination showed temperature 39.7 C, "
            "tachycardia, neck stiffness, positive Kernig sign, and a "
            "Glasgow Coma Scale of 12. Cerebrospinal fluid showed "
            "opening pressure 28 cmH2O, white blood cell count 2,200 "
            "per cubic millimeter (90 percent neutrophils), glucose 28 "
            "mg/dL, protein 220 mg/dL, lactate 5.6 mmol/L, and motile "
            "trophozoites on wet mount; CDC reference laboratory CSF "
            "real-time PCR confirmed Naegleria fowleri. Environmental "
            "sampling of the implicated hot-spring pool returned "
            "positive N. fowleri PCR. The CDC six-drug protocol was "
            "initiated within three hours of admission; the child "
            "progressed to obtundation overnight and died on hospital "
            "day four."
        ),
        "narrative_es": (
            "Niño previamente sano de 12 años que presentó cuatro "
            "días de fiebre, cefalea frontal, vómitos e irritabilidad "
            "creciente tras una salida de camping multifamiliar en el "
            "condado de Inyo, este de California, durante la cual "
            "nadó y sumergió la cabeza repetidamente en una piscina "
            "geotermal aproximadamente seis días antes del inicio de "
            "síntomas. El examen mostró temperatura 39.7 C, "
            "taquicardia, rigidez de nuca, signo de Kernig positivo y "
            "escala de Glasgow de 12. El líquido cefalorraquídeo "
            "mostró presión de apertura 28 cmH2O, leucocitos 2,200 "
            "por mm3 (90 por ciento neutrófilos), glucosa 28 mg/dL, "
            "proteína 220 mg/dL, lactato 5.6 mmol/L y trofozoítos "
            "móviles en frotis directo; PCR de Naegleria fowleri en "
            "LCR confirmada en el laboratorio de referencia de los "
            "CDC. El muestreo ambiental de la piscina geotermal "
            "implicada fue positivo para N. fowleri por PCR. Se "
            "inició el protocolo de seis fármacos de los CDC en las "
            "primeras tres horas del ingreso; el niño progresó a "
            "obnubilación durante la noche y falleció en el día "
            "hospitalario cuatro."
        ),
    }


def _build_vignette_014() -> dict[str, Any]:
    """Vignette 14: 21-year-old female, California overland-pipe pool, late, fatal.

    Anchored to Johnson/Cope MMWR 2016 (PMID 27123690) Inyo County
    overland-pipe spring-fed pool case. Atypical exposure: not direct
    hot-spring contact but a residential pool fed by spring water via
    overland piping.
    """
    return {
        "history": {
            "symptom_onset_to_presentation_days": 6.0,
            "chief_complaint": "altered_mental_status",
            "prodrome_description": (
                "Five days of fever, severe headache, vomiting, and "
                "progressive lethargy after recreational swimming in a "
                "private residential pool fed by overland piping from "
                "an upgradient natural spring; one witnessed "
                "generalized seizure 12 hours before admission."
            ),
            "red_flags_present": ["fresh_water_exposure_14d"],
        },
        "exposure": {
            "freshwater_exposure_within_14d": True,
            "freshwater_exposure_type": "swimming_pool_unchlorinated",
            "altitude_exposure_within_7d_m": 1100,
            "pork_consumption_or_taenia_contact": False,
            "mosquito_endemic_area_exposure": False,
            "immunocompromise_status": "none",
            "hiv_status": "negative",
            "cd4_count_cells_per_uL": None,
        },
        "vitals": {
            "temperature_celsius": 39.9,
            "heart_rate_bpm": 138,
            "systolic_bp_mmHg": 96,
            "diastolic_bp_mmHg": 58,
            "glasgow_coma_scale": 7,
            "oxygen_saturation_pct": 92,
            "respiratory_rate_breaths_per_min": 30,
        },
        "exam": {
            "mental_status_grade": "stuporous",
            "neck_stiffness": True,
            "kernig_or_brudzinski_positive": True,
            "focal_neurological_deficit": False,
            "cranial_nerve_palsy": "none",
            "skin_lesion_centrofacial_chronic": False,
            "petechial_or_purpuric_rash": False,
            "papilledema_on_fundoscopy": True,
        },
        "labs": {
            "wbc_blood_per_uL": 18800,
            "platelets_per_uL": 204000,
            "alt_ast_U_per_L": 46,
            "crp_mg_per_L": 122.0,
            "procalcitonin_ng_per_mL": 5.0,
            "serum_sodium_mEq_per_L": 131,
        },
        "csf": {
            "opening_pressure_cmH2O": 46.0,
            "csf_wbc_per_mm3": 4400,
            "csf_neutrophil_pct": 95,
            "csf_lymphocyte_pct": 4,
            "csf_eosinophil_pct": 1,
            "csf_glucose_mg_per_dL": 12,
            "csf_protein_mg_per_dL": 420,
            "csf_lactate_mmol_per_L": 9.0,
            "csf_ada_U_per_L": None,
            "csf_crag_lfa_result": "negative",
            "csf_wet_mount_motile_amoebae": "positive",
            "csf_xanthochromia_present": False,
            "csf_rbc_per_mm3": 880,
            "csf_rbc_decreasing_across_tubes": None,
        },
        "imaging": {
            "imaging_modality": "mri_with_dwi_flair",
            "imaging_pattern": "diffuse_cerebral_edema_basilar_meningeal_enhancement",
            "imaging_finding_count": None,
            "imaging_text_summary": (
                "MRI brain with FLAIR and DWI showing diffuse cerebral "
                "edema, basal cistern enhancement, and small bilateral "
                "temporal hemorrhagic foci; pattern consistent with "
                "primary amebic meningoencephalitis."
            ),
        },
        "diagnostic_tests": {
            "results": [
                {
                    "test_name": "CSF wet mount microscopy",
                    "result": (
                        "Numerous motile trophozoites consistent with "
                        "Naegleria fowleri."
                    ),
                    "sensitivity_pct": None,
                    "specificity_pct": None,
                    "citation_pmid_or_doi": "PMID:27123690",
                },
                {
                    "test_name": "CSF Naegleria fowleri real-time PCR (CDC reference laboratory)",
                    "result": "Positive (cycle threshold 19)",
                    "sensitivity_pct": 95.0,
                    "specificity_pct": 99.0,
                    "citation_pmid_or_doi": "PMID:27123690",
                },
                {
                    "test_name": "Overland-pipe pool environmental sampling (Inyo County Public Health)",
                    "result": (
                        "N. fowleri PCR-positive in water samples from "
                        "the residential pool and along the overland "
                        "pipe segment."
                    ),
                    "sensitivity_pct": None,
                    "specificity_pct": None,
                    "citation_pmid_or_doi": "PMID:27123690",
                },
            ],
        },
        "narrative_en": (
            "Twenty-one-year-old previously healthy female from "
            "eastern California presented in stuporous mental status "
            "after a six-day course of fever, severe headache, "
            "vomiting, and progressive lethargy following recreational "
            "swimming in a private residential pool fed by overland "
            "piping from an upgradient natural spring, plus one "
            "witnessed generalized seizure 12 hours before admission. "
            "Examination showed temperature 39.9 C, tachycardia, "
            "hypotension, neck stiffness, papilledema, and a Glasgow "
            "Coma Scale of 7. Cerebrospinal fluid showed opening "
            "pressure 46 cmH2O, white blood cell count 4,400 per cubic "
            "millimeter (95 percent neutrophils), glucose 12 mg/dL, "
            "protein 420 mg/dL, lactate 9.0 mmol/L, and numerous "
            "motile trophozoites on wet mount; CDC reference "
            "laboratory CSF real-time PCR confirmed Naegleria "
            "fowleri. Environmental sampling of the implicated pool "
            "and overland-pipe segment returned positive N. fowleri "
            "PCR. The CDC six-drug protocol and aggressive "
            "intracranial pressure management were initiated within "
            "two hours of admission; the patient died on hospital day "
            "three after rapid neurologic deterioration."
        ),
        "narrative_es": (
            "Mujer previamente sana de 21 años, residente en el este "
            "de California, que ingresó en estado estuporoso tras "
            "cuadro de seis días de fiebre, cefalea severa, vómitos "
            "y letargia progresiva tras nadar recreacionalmente en "
            "una piscina residencial privada alimentada por tubería "
            "superficial desde un manantial natural en la cota "
            "superior, más una crisis generalizada presenciada 12 "
            "horas antes del ingreso. El examen mostró temperatura "
            "39.9 C, taquicardia, hipotensión, rigidez de nuca, "
            "papiledema y escala de Glasgow de 7. El líquido "
            "cefalorraquídeo mostró presión de apertura 46 cmH2O, "
            "leucocitos 4,400 por mm3 (95 por ciento neutrófilos), "
            "glucosa 12 mg/dL, proteína 420 mg/dL, lactato 9.0 "
            "mmol/L y abundantes trofozoítos móviles en frotis "
            "directo; PCR de Naegleria fowleri en LCR confirmada en "
            "el laboratorio de referencia de los CDC. El muestreo "
            "ambiental de la piscina implicada y de la tubería "
            "superficial fue positivo para N. fowleri por PCR. Se "
            "inició el protocolo de seis fármacos de los CDC y "
            "manejo agresivo de presión intracraneal en las primeras "
            "dos horas del ingreso; la paciente falleció en el día "
            "hospitalario tres tras deterioro neurológico rápido."
        ),
    }


def _build_vignette_015() -> dict[str, Any]:
    """Vignette 15: 13-year-old male, Karachi ablution, late, fatal.

    Anchored to Shakoor Emerg Infect Dis 2011 (PMID 21291600) 13-case
    Karachi series. Religious ablution (wudu) with municipal tap water
    documented as exposure route in absence of recreational aquatic
    activity.
    """
    return {
        "history": {
            "symptom_onset_to_presentation_days": 5.0,
            "chief_complaint": "altered_mental_status",
            "prodrome_description": (
                "Four days of fever, severe headache, vomiting, and "
                "increasing lethargy in the context of daily ritual "
                "ablution (wudu) with municipal tap water several "
                "times per day; no recreational swimming or river "
                "exposure documented; one witnessed generalized "
                "seizure on the morning of admission."
            ),
            "red_flags_present": ["fresh_water_exposure_14d"],
        },
        "exposure": {
            "freshwater_exposure_within_14d": True,
            "freshwater_exposure_type": "ritual_ablution_wudu",
            "altitude_exposure_within_7d_m": None,
            "pork_consumption_or_taenia_contact": False,
            "mosquito_endemic_area_exposure": False,
            "immunocompromise_status": "none",
            "hiv_status": "negative",
            "cd4_count_cells_per_uL": None,
        },
        "vitals": {
            "temperature_celsius": 39.8,
            "heart_rate_bpm": 138,
            "systolic_bp_mmHg": 94,
            "diastolic_bp_mmHg": 58,
            "glasgow_coma_scale": 6,
            "oxygen_saturation_pct": 91,
            "respiratory_rate_breaths_per_min": 32,
        },
        "exam": {
            "mental_status_grade": "comatose",
            "neck_stiffness": True,
            "kernig_or_brudzinski_positive": True,
            "focal_neurological_deficit": False,
            "cranial_nerve_palsy": "none",
            "skin_lesion_centrofacial_chronic": False,
            "petechial_or_purpuric_rash": False,
            "papilledema_on_fundoscopy": True,
        },
        "labs": {
            "wbc_blood_per_uL": 19000,
            "platelets_per_uL": 188000,
            "alt_ast_U_per_L": 50,
            "crp_mg_per_L": 128.0,
            "procalcitonin_ng_per_mL": 5.4,
            "serum_sodium_mEq_per_L": 130,
        },
        "csf": {
            "opening_pressure_cmH2O": 48.0,
            "csf_wbc_per_mm3": 4800,
            "csf_neutrophil_pct": 96,
            "csf_lymphocyte_pct": 3,
            "csf_eosinophil_pct": 1,
            "csf_glucose_mg_per_dL": 12,
            "csf_protein_mg_per_dL": 440,
            "csf_lactate_mmol_per_L": 9.2,
            "csf_ada_U_per_L": None,
            "csf_crag_lfa_result": "negative",
            "csf_wet_mount_motile_amoebae": "positive",
            "csf_xanthochromia_present": False,
            "csf_rbc_per_mm3": 1040,
            "csf_rbc_decreasing_across_tubes": None,
        },
        "imaging": {
            "imaging_modality": "ct_contrast",
            "imaging_pattern": "diffuse_cerebral_edema_basilar_meningeal_enhancement",
            "imaging_finding_count": None,
            "imaging_text_summary": (
                "Contrast-enhanced CT head showing diffuse cerebral "
                "edema with effacement of cortical sulci, basal "
                "cistern obliteration, and abnormal basal meningeal "
                "enhancement; pattern consistent with severe primary "
                "amebic meningoencephalitis."
            ),
        },
        "diagnostic_tests": {
            "results": [
                {
                    "test_name": "CSF wet mount microscopy (Aga Khan University)",
                    "result": (
                        "Numerous motile trophozoites consistent with "
                        "Naegleria fowleri."
                    ),
                    "sensitivity_pct": None,
                    "specificity_pct": None,
                    "citation_pmid_or_doi": "PMID:21291600",
                },
                {
                    "test_name": "CSF Naegleria fowleri real-time PCR (Aga Khan University reference laboratory)",
                    "result": "Positive (cycle threshold 18)",
                    "sensitivity_pct": 95.0,
                    "specificity_pct": 99.0,
                    "citation_pmid_or_doi": "PMID:21291600",
                },
            ],
        },
        "narrative_en": (
            "Thirteen-year-old previously healthy male from Karachi, "
            "Pakistan presented in coma after a five-day course of "
            "fever, severe headache, vomiting, and increasing lethargy "
            "in the context of daily ritual ablution (wudu) using "
            "municipal tap water several times per day, with no "
            "recreational swimming or river exposure documented; one "
            "witnessed generalized seizure was observed on the morning "
            "of admission. Examination showed temperature 39.8 C, "
            "tachycardia, hypotension, neck stiffness, papilledema, "
            "and a Glasgow Coma Scale of 6. Cerebrospinal fluid showed "
            "opening pressure 48 cmH2O, white blood cell count 4,800 "
            "per cubic millimeter (96 percent neutrophils), glucose "
            "12 mg/dL, protein 440 mg/dL, lactate 9.2 mmol/L, and "
            "numerous motile trophozoites on wet mount; Aga Khan "
            "University reference laboratory CSF real-time PCR "
            "confirmed Naegleria fowleri. The CDC six-drug protocol "
            "was initiated within two hours of admission; the patient "
            "died on hospital day two."
        ),
        "narrative_es": (
            "Adolescente varón previamente sano de 13 años, residente "
            "en Karachi, Pakistán, que ingresó en coma tras cuadro de "
            "cinco días de fiebre, cefalea severa, vómitos y letargia "
            "creciente en el contexto de ablución ritual (wudu) "
            "diaria con agua de la red municipal varias veces al "
            "día, sin exposición recreativa a piscina ni río "
            "documentada; se presenció una crisis generalizada en la "
            "mañana del ingreso. El examen mostró temperatura 39.8 "
            "C, taquicardia, hipotensión, rigidez de nuca, "
            "papiledema y escala de Glasgow de 6. El líquido "
            "cefalorraquídeo mostró presión de apertura 48 cmH2O, "
            "leucocitos 4,800 por mm3 (96 por ciento neutrófilos), "
            "glucosa 12 mg/dL, proteína 440 mg/dL, lactato 9.2 "
            "mmol/L y abundantes trofozoítos móviles en frotis "
            "directo; PCR de Naegleria fowleri en LCR confirmada en "
            "el laboratorio de referencia de la Universidad Aga "
            "Khan. Se inició el protocolo de seis fármacos de los "
            "CDC en las primeras dos horas del ingreso; el paciente "
            "falleció en el día hospitalario dos."
        ),
    }


def _build_vignette_016() -> dict[str, Any]:
    """Vignette 16: 28-year-old male, Karachi public-water, mid, fatal.

    Anchored to Ghanchi Am J Trop Med Hyg 2017 (PMID 29016297) Karachi
    case series. Caveat from PMID_REGISTRY: quote precisely "19
    PCR-confirmed cases of 116 suspected at AKU 2014-2015, median age
    28y, 84% male, 16% female." This vignette represents a typical
    case from that series (median demographics).
    """
    return {
        "history": {
            "symptom_onset_to_presentation_days": 4.5,
            "chief_complaint": "fever_with_headache",
            "prodrome_description": (
                "Four days of fever, severe headache, photophobia, "
                "vomiting, and progressive somnolence in the context "
                "of daily ritual ablution (wudu) with municipal "
                "public-supply tap water and household bathing; no "
                "recreational aquatic activity documented."
            ),
            "red_flags_present": ["fresh_water_exposure_14d"],
        },
        "exposure": {
            "freshwater_exposure_within_14d": True,
            "freshwater_exposure_type": "ritual_ablution_wudu",
            "altitude_exposure_within_7d_m": None,
            "pork_consumption_or_taenia_contact": False,
            "mosquito_endemic_area_exposure": False,
            "immunocompromise_status": "none",
            "hiv_status": "negative",
            "cd4_count_cells_per_uL": None,
        },
        "vitals": {
            "temperature_celsius": 39.6,
            "heart_rate_bpm": 124,
            "systolic_bp_mmHg": 110,
            "diastolic_bp_mmHg": 66,
            "glasgow_coma_scale": 11,
            "oxygen_saturation_pct": 95,
            "respiratory_rate_breaths_per_min": 24,
        },
        "exam": {
            "mental_status_grade": "somnolent",
            "neck_stiffness": True,
            "kernig_or_brudzinski_positive": True,
            "focal_neurological_deficit": False,
            "cranial_nerve_palsy": "none",
            "skin_lesion_centrofacial_chronic": False,
            "petechial_or_purpuric_rash": False,
            "papilledema_on_fundoscopy": False,
        },
        "labs": {
            "wbc_blood_per_uL": 17600,
            "platelets_per_uL": 226000,
            "alt_ast_U_per_L": 38,
            "crp_mg_per_L": 110.0,
            "procalcitonin_ng_per_mL": 4.0,
            "serum_sodium_mEq_per_L": 134,
        },
        "csf": {
            "opening_pressure_cmH2O": 32.0,
            "csf_wbc_per_mm3": 2600,
            "csf_neutrophil_pct": 92,
            "csf_lymphocyte_pct": 6,
            "csf_eosinophil_pct": 2,
            "csf_glucose_mg_per_dL": 24,
            "csf_protein_mg_per_dL": 250,
            "csf_lactate_mmol_per_L": 6.4,
            "csf_ada_U_per_L": None,
            "csf_crag_lfa_result": "negative",
            "csf_wet_mount_motile_amoebae": "positive",
            "csf_xanthochromia_present": False,
            "csf_rbc_per_mm3": 360,
            "csf_rbc_decreasing_across_tubes": None,
        },
        "imaging": {
            "imaging_modality": "mri_with_dwi_flair",
            "imaging_pattern": "diffuse_cerebral_edema_basilar_meningeal_enhancement",
            "imaging_finding_count": None,
            "imaging_text_summary": (
                "MRI brain with FLAIR and DWI showing basal cistern "
                "enhancement and early diffuse cerebral edema without "
                "focal hemorrhage; pattern consistent with primary "
                "amebic meningoencephalitis."
            ),
        },
        "diagnostic_tests": {
            "results": [
                {
                    "test_name": "CSF wet mount microscopy (Aga Khan University)",
                    "result": (
                        "Motile trophozoites consistent with Naegleria "
                        "fowleri identified within 30 minutes of CSF "
                        "collection."
                    ),
                    "sensitivity_pct": None,
                    "specificity_pct": None,
                    "citation_pmid_or_doi": "PMID:29016297",
                },
                {
                    "test_name": "CSF Naegleria fowleri real-time PCR (Aga Khan University reference laboratory)",
                    "result": "Positive (cycle threshold 21)",
                    "sensitivity_pct": 95.0,
                    "specificity_pct": 99.0,
                    "citation_pmid_or_doi": "PMID:29016297",
                },
                {
                    "test_name": "Public-supply tap-water environmental sampling (Karachi water utility)",
                    "result": (
                        "N. fowleri PCR-positive in distribution-system "
                        "samples linking the implicated supply zone."
                    ),
                    "sensitivity_pct": None,
                    "specificity_pct": None,
                    "citation_pmid_or_doi": "PMID:29016297",
                },
            ],
        },
        "narrative_en": (
            "Twenty-eight-year-old previously healthy male from "
            "Karachi, Pakistan presented with four days of fever, "
            "severe headache, photophobia, vomiting, and progressive "
            "somnolence in the context of daily ritual ablution "
            "(wudu) using municipal public-supply tap water and "
            "household bathing, with no recreational aquatic activity "
            "documented. This presentation is consistent with the "
            "Aga Khan University 2014-2015 series, which identified "
            "19 PCR-confirmed cases of 116 suspected (median age 28 "
            "years; 84 percent male, 16 percent female). Examination "
            "showed temperature 39.6 C, tachycardia, neck stiffness, "
            "positive Kernig sign, and a Glasgow Coma Scale of 11. "
            "Cerebrospinal fluid showed opening pressure 32 cmH2O, "
            "white blood cell count 2,600 per cubic millimeter (92 "
            "percent neutrophils), glucose 24 mg/dL, protein 250 "
            "mg/dL, lactate 6.4 mmol/L, and motile trophozoites on "
            "wet mount; Aga Khan University reference laboratory CSF "
            "real-time PCR confirmed Naegleria fowleri. Environmental "
            "sampling of the implicated public-supply distribution "
            "zone returned positive N. fowleri PCR. The CDC six-drug "
            "protocol was initiated within four hours of admission; "
            "the patient progressed to coma overnight and died on "
            "hospital day five."
        ),
        "narrative_es": (
            "Varón previamente sano de 28 años, residente en Karachi, "
            "Pakistán, que presentó cuatro días de fiebre, cefalea "
            "severa, fotofobia, vómitos y somnolencia progresiva en "
            "el contexto de ablución ritual (wudu) diaria con agua "
            "de la red pública municipal y baño domiciliario, sin "
            "exposición recreativa a actividad acuática documentada. "
            "Este caso es consistente con la serie de la Universidad "
            "Aga Khan 2014-2015, que identificó 19 casos confirmados "
            "por PCR de 116 sospechosos (mediana de edad 28 años; "
            "84 por ciento hombres, 16 por ciento mujeres). El "
            "examen mostró temperatura 39.6 C, taquicardia, rigidez "
            "de nuca, signo de Kernig positivo y escala de Glasgow "
            "de 11. El líquido cefalorraquídeo mostró presión de "
            "apertura 32 cmH2O, leucocitos 2,600 por mm3 (92 por "
            "ciento neutrófilos), glucosa 24 mg/dL, proteína 250 "
            "mg/dL, lactato 6.4 mmol/L y trofozoítos móviles en "
            "frotis directo; PCR de Naegleria fowleri en LCR "
            "confirmada en el laboratorio de referencia de la "
            "Universidad Aga Khan. El muestreo ambiental de la zona "
            "de distribución pública implicada fue positivo para N. "
            "fowleri por PCR. Se inició el protocolo de seis "
            "fármacos de los CDC en las primeras cuatro horas del "
            "ingreso; el paciente progresó a coma durante la noche "
            "y falleció en el día hospitalario cinco."
        ),
    }


def _build_vignette_017() -> dict[str, Any]:
    """Vignette 17: 11-year-old male, Florida resident acquired Costa Rica, late, fatal.

    Anchored to Abrahams-Sandi Emerg Infect Dis 2015 (PMID 25625800).
    Travel-acquired hot-spring exposure during family trip to Costa
    Rica; symptoms developed after return to Florida residence.
    """
    return {
        "history": {
            "symptom_onset_to_presentation_days": 6.0,
            "chief_complaint": "altered_mental_status",
            "prodrome_description": (
                "Five days of fever, severe headache, photophobia, "
                "vomiting, and progressive lethargy beginning shortly "
                "after return to Florida from a family vacation in "
                "Costa Rica, during which the child swam and "
                "submerged his head in a public geothermal hot-spring "
                "pool approximately 12 days before symptom onset; "
                "two witnessed generalized seizures in the 18 hours "
                "before admission."
            ),
            "red_flags_present": ["fresh_water_exposure_14d"],
        },
        "exposure": {
            "freshwater_exposure_within_14d": True,
            "freshwater_exposure_type": "hot_spring",
            "altitude_exposure_within_7d_m": None,
            "pork_consumption_or_taenia_contact": False,
            "mosquito_endemic_area_exposure": False,
            "immunocompromise_status": "none",
            "hiv_status": "negative",
            "cd4_count_cells_per_uL": None,
        },
        "vitals": {
            "temperature_celsius": 39.8,
            "heart_rate_bpm": 140,
            "systolic_bp_mmHg": 92,
            "diastolic_bp_mmHg": 56,
            "glasgow_coma_scale": 6,
            "oxygen_saturation_pct": 91,
            "respiratory_rate_breaths_per_min": 32,
        },
        "exam": {
            "mental_status_grade": "comatose",
            "neck_stiffness": True,
            "kernig_or_brudzinski_positive": True,
            "focal_neurological_deficit": False,
            "cranial_nerve_palsy": "none",
            "skin_lesion_centrofacial_chronic": False,
            "petechial_or_purpuric_rash": False,
            "papilledema_on_fundoscopy": True,
        },
        "labs": {
            "wbc_blood_per_uL": 19400,
            "platelets_per_uL": 192000,
            "alt_ast_U_per_L": 50,
            "crp_mg_per_L": 130.0,
            "procalcitonin_ng_per_mL": 5.4,
            "serum_sodium_mEq_per_L": 130,
        },
        "csf": {
            "opening_pressure_cmH2O": 50.0,
            "csf_wbc_per_mm3": 5000,
            "csf_neutrophil_pct": 96,
            "csf_lymphocyte_pct": 3,
            "csf_eosinophil_pct": 1,
            "csf_glucose_mg_per_dL": 10,
            "csf_protein_mg_per_dL": 460,
            "csf_lactate_mmol_per_L": 9.4,
            "csf_ada_U_per_L": None,
            "csf_crag_lfa_result": "negative",
            "csf_wet_mount_motile_amoebae": "positive",
            "csf_xanthochromia_present": False,
            "csf_rbc_per_mm3": 1180,
            "csf_rbc_decreasing_across_tubes": None,
        },
        "imaging": {
            "imaging_modality": "mri_with_dwi_flair",
            "imaging_pattern": "diffuse_cerebral_edema_basilar_meningeal_enhancement",
            "imaging_finding_count": None,
            "imaging_text_summary": (
                "MRI brain with FLAIR and DWI showing diffuse cerebral "
                "edema, basal cistern enhancement, and bilateral "
                "temporal hemorrhagic foci; early signs of cerebellar "
                "tonsillar herniation; pattern consistent with severe "
                "primary amebic meningoencephalitis."
            ),
        },
        "diagnostic_tests": {
            "results": [
                {
                    "test_name": "CSF wet mount microscopy",
                    "result": (
                        "Numerous motile trophozoites consistent with "
                        "Naegleria fowleri."
                    ),
                    "sensitivity_pct": None,
                    "specificity_pct": None,
                    "citation_pmid_or_doi": "PMID:25625800",
                },
                {
                    "test_name": "CSF Naegleria fowleri real-time PCR (CDC reference laboratory)",
                    "result": "Positive (cycle threshold 19)",
                    "sensitivity_pct": 95.0,
                    "specificity_pct": 99.0,
                    "citation_pmid_or_doi": "PMID:25625800",
                },
                {
                    "test_name": "Costa Rica hot-spring environmental sampling (Costa Rica Ministry of Health)",
                    "result": (
                        "N. fowleri PCR-positive in water samples from "
                        "the implicated geothermal pool visited during "
                        "the family trip."
                    ),
                    "sensitivity_pct": None,
                    "specificity_pct": None,
                    "citation_pmid_or_doi": "PMID:25625800",
                },
            ],
        },
        "narrative_en": (
            "Eleven-year-old previously healthy male, Florida "
            "resident, presented in coma after a five-day course of "
            "fever, severe headache, photophobia, vomiting, and "
            "progressive lethargy beginning shortly after return from "
            "a family vacation in Costa Rica during which he swam "
            "and submerged his head in a public geothermal hot-spring "
            "pool approximately 12 days before symptom onset; two "
            "witnessed generalized seizures occurred in the 18 hours "
            "before admission. Examination showed temperature 39.8 C, "
            "tachycardia, hypotension, neck stiffness, papilledema, "
            "and a Glasgow Coma Scale of 6. Cerebrospinal fluid "
            "showed opening pressure 50 cmH2O, white blood cell count "
            "5,000 per cubic millimeter (96 percent neutrophils), "
            "glucose 10 mg/dL, protein 460 mg/dL, lactate 9.4 mmol/L, "
            "and numerous motile trophozoites on wet mount; CDC "
            "reference laboratory CSF real-time PCR confirmed "
            "Naegleria fowleri. Coordinated environmental sampling by "
            "the Costa Rica Ministry of Health returned positive N. "
            "fowleri PCR from the implicated hot-spring pool. The "
            "CDC six-drug protocol and aggressive intracranial "
            "pressure management were initiated within an hour of "
            "admission; the child died on hospital day three after "
            "withdrawal of care for established brain death."
        ),
        "narrative_es": (
            "Niño previamente sano de 11 años, residente en Florida, "
            "que ingresó en coma tras cuadro de cinco días de "
            "fiebre, cefalea severa, fotofobia, vómitos y letargia "
            "progresiva que iniciaron poco después del regreso de "
            "vacaciones familiares en Costa Rica, durante las "
            "cuales nadó y sumergió la cabeza en una piscina pública "
            "geotermal aproximadamente 12 días antes del inicio de "
            "síntomas; se presenciaron dos crisis generalizadas en "
            "las 18 horas previas al ingreso. El examen mostró "
            "temperatura 39.8 C, taquicardia, hipotensión, rigidez "
            "de nuca, papiledema y escala de Glasgow de 6. El "
            "líquido cefalorraquídeo mostró presión de apertura 50 "
            "cmH2O, leucocitos 5,000 por mm3 (96 por ciento "
            "neutrófilos), glucosa 10 mg/dL, proteína 460 mg/dL, "
            "lactato 9.4 mmol/L y abundantes trofozoítos móviles "
            "en frotis directo; PCR de Naegleria fowleri en LCR "
            "confirmada en el laboratorio de referencia de los "
            "CDC. El muestreo ambiental coordinado por el Ministerio "
            "de Salud de Costa Rica fue positivo para N. fowleri "
            "por PCR en la piscina geotermal implicada. Se inició "
            "el protocolo de seis fármacos de los CDC y manejo "
            "agresivo de presión intracraneal en la primera hora "
            "del ingreso; el niño falleció en el día hospitalario "
            "tres tras retiro de soporte por muerte encefálica "
            "establecida."
        ),
    }


def _build_vignette_018() -> dict[str, Any]:
    """Vignette 18: 9-year-old male, Mexicali irrigation canal, mid, fatal.

    Anchored to Lares-Villa J Clin Microbiol 1993 (PMID 8458963). First
    Mexican human N. fowleri isolations; irrigation-canal swimming as
    exposure route in arid Mexicali Valley.
    """
    return {
        "history": {
            "symptom_onset_to_presentation_days": 4.5,
            "chief_complaint": "fever_with_headache",
            "prodrome_description": (
                "Four days of fever, severe headache, vomiting, "
                "photophobia, and increasing irritability after "
                "swimming and submerging his head repeatedly in an "
                "irrigation canal in the Mexicali Valley "
                "approximately five days before symptom onset; on "
                "the day of admission he developed neck stiffness "
                "and progressive somnolence."
            ),
            "red_flags_present": ["fresh_water_exposure_14d"],
        },
        "exposure": {
            "freshwater_exposure_within_14d": True,
            "freshwater_exposure_type": "river",
            "altitude_exposure_within_7d_m": None,
            "pork_consumption_or_taenia_contact": False,
            "mosquito_endemic_area_exposure": False,
            "immunocompromise_status": "none",
            "hiv_status": "negative",
            "cd4_count_cells_per_uL": None,
        },
        "vitals": {
            "temperature_celsius": 39.7,
            "heart_rate_bpm": 130,
            "systolic_bp_mmHg": 104,
            "diastolic_bp_mmHg": 62,
            "glasgow_coma_scale": 12,
            "oxygen_saturation_pct": 95,
            "respiratory_rate_breaths_per_min": 24,
        },
        "exam": {
            "mental_status_grade": "somnolent",
            "neck_stiffness": True,
            "kernig_or_brudzinski_positive": True,
            "focal_neurological_deficit": False,
            "cranial_nerve_palsy": "none",
            "skin_lesion_centrofacial_chronic": False,
            "petechial_or_purpuric_rash": False,
            "papilledema_on_fundoscopy": False,
        },
        "labs": {
            "wbc_blood_per_uL": 16800,
            "platelets_per_uL": 232000,
            "alt_ast_U_per_L": 36,
            "crp_mg_per_L": 100.0,
            "procalcitonin_ng_per_mL": 3.6,
            "serum_sodium_mEq_per_L": 134,
        },
        "csf": {
            "opening_pressure_cmH2O": 30.0,
            "csf_wbc_per_mm3": 2400,
            "csf_neutrophil_pct": 92,
            "csf_lymphocyte_pct": 6,
            "csf_eosinophil_pct": 2,
            "csf_glucose_mg_per_dL": 26,
            "csf_protein_mg_per_dL": 240,
            "csf_lactate_mmol_per_L": 5.8,
            "csf_ada_U_per_L": None,
            "csf_crag_lfa_result": "negative",
            "csf_wet_mount_motile_amoebae": "positive",
            "csf_xanthochromia_present": False,
            "csf_rbc_per_mm3": 320,
            "csf_rbc_decreasing_across_tubes": None,
        },
        "imaging": {
            "imaging_modality": "ct_contrast",
            "imaging_pattern": "diffuse_cerebral_edema_basilar_meningeal_enhancement",
            "imaging_finding_count": None,
            "imaging_text_summary": (
                "Contrast-enhanced CT head showing basal cistern "
                "enhancement, sulcal effacement, and early diffuse "
                "cerebral edema; pattern consistent with primary "
                "amebic meningoencephalitis."
            ),
        },
        "diagnostic_tests": {
            "results": [
                {
                    "test_name": "CSF wet mount microscopy",
                    "result": (
                        "Motile trophozoites consistent with Naegleria "
                        "fowleri identified at bedside on warmed slide."
                    ),
                    "sensitivity_pct": None,
                    "specificity_pct": None,
                    "citation_pmid_or_doi": "PMID:8458963",
                },
                {
                    "test_name": "CSF amoeba culture (Mexicali reference laboratory)",
                    "result": (
                        "Naegleria fowleri isolated and confirmed by "
                        "morphology and thermotolerance assay."
                    ),
                    "sensitivity_pct": None,
                    "specificity_pct": None,
                    "citation_pmid_or_doi": "PMID:8458963",
                },
                {
                    "test_name": "Mexicali Valley irrigation-canal environmental isolate",
                    "result": (
                        "N. fowleri recovered from canal water samples "
                        "collected at the implicated swimming site."
                    ),
                    "sensitivity_pct": None,
                    "specificity_pct": None,
                    "citation_pmid_or_doi": "PMID:8458963",
                },
            ],
        },
        "narrative_en": (
            "Nine-year-old previously healthy male from Mexicali, "
            "Mexico presented with four days of fever, severe "
            "headache, vomiting, photophobia, and increasing "
            "irritability after swimming and repeatedly submerging "
            "his head in an irrigation canal in the Mexicali Valley "
            "approximately five days before symptom onset; on the "
            "day of admission he developed neck stiffness and "
            "progressive somnolence. Examination showed temperature "
            "39.7 C, tachycardia, neck stiffness, positive Kernig "
            "sign, and a Glasgow Coma Scale of 12. Cerebrospinal "
            "fluid showed opening pressure 30 cmH2O, white blood "
            "cell count 2,400 per cubic millimeter (92 percent "
            "neutrophils), glucose 26 mg/dL, protein 240 mg/dL, "
            "lactate 5.8 mmol/L, and motile trophozoites on wet "
            "mount; the local reference laboratory isolated "
            "Naegleria fowleri from CSF and recovered N. fowleri "
            "from canal water samples at the implicated swimming "
            "site, representing one of the first Mexican human N. "
            "fowleri isolations on record. The CDC six-drug "
            "protocol was initiated within four hours of admission; "
            "the child progressed to coma overnight and died on "
            "hospital day five."
        ),
        "narrative_es": (
            "Niño previamente sano de 9 años, residente en Mexicali, "
            "México, que presentó cuatro días de fiebre, cefalea "
            "severa, vómitos, fotofobia e irritabilidad creciente "
            "tras nadar y sumergir la cabeza repetidamente en un "
            "canal de irrigación del Valle de Mexicali "
            "aproximadamente cinco días antes del inicio de "
            "síntomas; el día del ingreso desarrolló rigidez de "
            "nuca y somnolencia progresiva. El examen mostró "
            "temperatura 39.7 C, taquicardia, rigidez de nuca, "
            "signo de Kernig positivo y escala de Glasgow de 12. "
            "El líquido cefalorraquídeo mostró presión de apertura "
            "30 cmH2O, leucocitos 2,400 por mm3 (92 por ciento "
            "neutrófilos), glucosa 26 mg/dL, proteína 240 mg/dL, "
            "lactato 5.8 mmol/L y trofozoítos móviles en frotis "
            "directo; el laboratorio de referencia local aisló "
            "Naegleria fowleri del LCR y recuperó N. fowleri en "
            "muestras de agua del canal en el sitio de baño "
            "implicado, representando uno de los primeros "
            "aislamientos humanos mexicanos de N. fowleri "
            "documentados. Se inició el protocolo de seis "
            "fármacos de los CDC en las primeras cuatro horas "
            "del ingreso; el niño progresó a coma durante la "
            "noche y falleció en el día hospitalario cinco."
        ),
    }


def _build_vignette_019() -> dict[str, Any]:
    """Vignette 19: 22-year-old male, Karachi adult survivor, mid, SURVIVED.

    Anchored to Burki Emerg Infect Dis 2024 (PMID 38526236). Adult
    Pakistani PAM survivor on full ICU 6-drug regimen with hypothermia
    and intracranial pressure management. Atypical exposure: religious
    ablution. Survival is the rare outcome (CDC global tally <10
    confirmed survivors).
    """
    return {
        "history": {
            "symptom_onset_to_presentation_days": 4.0,
            "chief_complaint": "fever_with_headache",
            "prodrome_description": (
                "Three days of fever, severe headache, photophobia, "
                "vomiting, and progressive somnolence in the context "
                "of daily ritual ablution (wudu) with municipal tap "
                "water; presented to the emergency department within "
                "hours of mental-status decline rather than "
                "progressing to coma at home."
            ),
            "red_flags_present": ["fresh_water_exposure_14d"],
        },
        "exposure": {
            "freshwater_exposure_within_14d": True,
            "freshwater_exposure_type": "ritual_ablution_wudu",
            "altitude_exposure_within_7d_m": None,
            "pork_consumption_or_taenia_contact": False,
            "mosquito_endemic_area_exposure": False,
            "immunocompromise_status": "none",
            "hiv_status": "negative",
            "cd4_count_cells_per_uL": None,
        },
        "vitals": {
            "temperature_celsius": 39.4,
            "heart_rate_bpm": 116,
            "systolic_bp_mmHg": 118,
            "diastolic_bp_mmHg": 72,
            "glasgow_coma_scale": 12,
            "oxygen_saturation_pct": 96,
            "respiratory_rate_breaths_per_min": 22,
        },
        "exam": {
            "mental_status_grade": "somnolent",
            "neck_stiffness": True,
            "kernig_or_brudzinski_positive": True,
            "focal_neurological_deficit": False,
            "cranial_nerve_palsy": "none",
            "skin_lesion_centrofacial_chronic": False,
            "petechial_or_purpuric_rash": False,
            "papilledema_on_fundoscopy": False,
        },
        "labs": {
            "wbc_blood_per_uL": 16200,
            "platelets_per_uL": 244000,
            "alt_ast_U_per_L": 32,
            "crp_mg_per_L": 88.0,
            "procalcitonin_ng_per_mL": 2.8,
            "serum_sodium_mEq_per_L": 136,
        },
        "csf": {
            "opening_pressure_cmH2O": 28.0,
            "csf_wbc_per_mm3": 1900,
            "csf_neutrophil_pct": 88,
            "csf_lymphocyte_pct": 10,
            "csf_eosinophil_pct": 2,
            "csf_glucose_mg_per_dL": 32,
            "csf_protein_mg_per_dL": 200,
            "csf_lactate_mmol_per_L": 5.2,
            "csf_ada_U_per_L": None,
            "csf_crag_lfa_result": "negative",
            "csf_wet_mount_motile_amoebae": "positive",
            "csf_xanthochromia_present": False,
            "csf_rbc_per_mm3": 180,
            "csf_rbc_decreasing_across_tubes": None,
        },
        "imaging": {
            "imaging_modality": "mri_with_dwi_flair",
            "imaging_pattern": "diffuse_cerebral_edema_basilar_meningeal_enhancement",
            "imaging_finding_count": None,
            "imaging_text_summary": (
                "MRI brain with FLAIR and DWI showing basal cistern "
                "enhancement and early diffuse cerebral edema "
                "without focal hemorrhage; pattern consistent with "
                "early primary amebic meningoencephalitis at a "
                "treatable stage."
            ),
        },
        "diagnostic_tests": {
            "results": [
                {
                    "test_name": "CSF wet mount microscopy (Aga Khan University)",
                    "result": (
                        "Motile trophozoites consistent with Naegleria "
                        "fowleri identified within 60 minutes of CSF "
                        "collection."
                    ),
                    "sensitivity_pct": None,
                    "specificity_pct": None,
                    "citation_pmid_or_doi": "PMID:38526236",
                },
                {
                    "test_name": "CSF Naegleria fowleri real-time PCR (Aga Khan University reference laboratory)",
                    "result": "Positive (cycle threshold 23)",
                    "sensitivity_pct": 95.0,
                    "specificity_pct": 99.0,
                    "citation_pmid_or_doi": "PMID:38526236",
                },
            ],
        },
        "narrative_en": (
            "Twenty-two-year-old previously healthy male from "
            "Karachi, Pakistan presented with three days of fever, "
            "severe headache, photophobia, vomiting, and progressive "
            "somnolence in the context of daily ritual ablution "
            "(wudu) using municipal tap water. Family-recognized "
            "early decline prompted emergency department arrival "
            "within hours rather than at the obtunded stage typical "
            "of fatal cases. Examination showed temperature 39.4 C, "
            "tachycardia, neck stiffness, positive Kernig sign, and "
            "a Glasgow Coma Scale of 12. Cerebrospinal fluid showed "
            "opening pressure 28 cmH2O, white blood cell count "
            "1,900 per cubic millimeter (88 percent neutrophils), "
            "glucose 32 mg/dL, protein 200 mg/dL, lactate 5.2 "
            "mmol/L, and motile trophozoites on wet mount; Aga "
            "Khan University reference laboratory CSF real-time PCR "
            "confirmed Naegleria fowleri. The CDC six-drug protocol "
            "(amphotericin B intravenous and intrathecal, "
            "miltefosine, dexamethasone, fluconazole, azithromycin, "
            "and rifampin), targeted temperature management with "
            "induced hypothermia, and aggressive intracranial "
            "pressure control were initiated within two hours of "
            "diagnosis. The patient remained intubated for ten "
            "days, with gradual neurologic recovery. He was "
            "discharged from the intensive care unit on hospital "
            "day 21 and from acute care on hospital day 32 with "
            "preserved cognition and mild residual deficits, "
            "representing one of the rare adult Pakistani PAM "
            "survivors documented in the literature."
        ),
        "narrative_es": (
            "Varón previamente sano de 22 años, residente en "
            "Karachi, Pakistán, que presentó tres días de fiebre, "
            "cefalea severa, fotofobia, vómitos y somnolencia "
            "progresiva en el contexto de ablución ritual (wudu) "
            "diaria con agua de la red municipal. El reconocimiento "
            "familiar temprano del deterioro motivó la consulta a "
            "urgencias en horas, en lugar del estado obnubilado "
            "típico de los casos fatales. El examen mostró "
            "temperatura 39.4 C, taquicardia, rigidez de nuca, "
            "signo de Kernig positivo y escala de Glasgow de 12. "
            "El líquido cefalorraquídeo mostró presión de apertura "
            "28 cmH2O, leucocitos 1,900 por mm3 (88 por ciento "
            "neutrófilos), glucosa 32 mg/dL, proteína 200 mg/dL, "
            "lactato 5.2 mmol/L y trofozoítos móviles en frotis "
            "directo; PCR de Naegleria fowleri en LCR confirmada "
            "en el laboratorio de referencia de la Universidad Aga "
            "Khan. Se inició el protocolo de seis fármacos de los "
            "CDC (anfotericina B intravenosa e intratecal, "
            "miltefosina, dexametasona, fluconazol, azitromicina y "
            "rifampicina), manejo dirigido de temperatura con "
            "hipotermia inducida y control agresivo de presión "
            "intracraneal en las primeras dos horas del "
            "diagnóstico. El paciente permaneció intubado durante "
            "diez días, con recuperación neurológica gradual. Fue "
            "egresado de la unidad de cuidados intensivos en el "
            "día hospitalario 21 y de hospitalización aguda en el "
            "día 32 con cognición preservada y déficits residuales "
            "leves, representando uno de los raros sobrevivientes "
            "adultos pakistaníes de PAM documentados en la "
            "literatura."
        ),
    }


def _build_vignette_020() -> dict[str, Any]:
    """Vignette 20: 14-year-old male, Kerala pediatric survivor, mid, SURVIVED.

    Anchored to Rauf Indian J Pediatr 2025 (PMID 40009134). Pediatric
    PAM survivor in Kerala, India on early miltefosine plus adjuncts.
    Caveat from PMID_REGISTRY: 6 authors confirmed via PubMed UI Pass
    5 (Rauf A, Rahiman FA, Poornima MV, Sudarsana J, Sehgal R,
    Ummer K). Recent (2025) miltefosine-era survivor case.
    """
    return {
        "history": {
            "symptom_onset_to_presentation_days": 4.0,
            "chief_complaint": "fever_with_headache",
            "prodrome_description": (
                "Three days of fever, frontal headache, vomiting, "
                "and increasing irritability after recreational "
                "swimming and underwater diving in a freshwater "
                "pond near the family residence in Kerala "
                "approximately six days before symptom onset; "
                "presented to a pediatric tertiary center within "
                "hours of mental-status change rather than at the "
                "obtunded stage."
            ),
            "red_flags_present": ["fresh_water_exposure_14d"],
        },
        "exposure": {
            "freshwater_exposure_within_14d": True,
            "freshwater_exposure_type": "lake",
            "altitude_exposure_within_7d_m": None,
            "pork_consumption_or_taenia_contact": False,
            "mosquito_endemic_area_exposure": False,
            "immunocompromise_status": "none",
            "hiv_status": "negative",
            "cd4_count_cells_per_uL": None,
        },
        "vitals": {
            "temperature_celsius": 39.5,
            "heart_rate_bpm": 122,
            "systolic_bp_mmHg": 112,
            "diastolic_bp_mmHg": 68,
            "glasgow_coma_scale": 13,
            "oxygen_saturation_pct": 96,
            "respiratory_rate_breaths_per_min": 22,
        },
        "exam": {
            "mental_status_grade": "somnolent",
            "neck_stiffness": True,
            "kernig_or_brudzinski_positive": True,
            "focal_neurological_deficit": False,
            "cranial_nerve_palsy": "none",
            "skin_lesion_centrofacial_chronic": False,
            "petechial_or_purpuric_rash": False,
            "papilledema_on_fundoscopy": False,
        },
        "labs": {
            "wbc_blood_per_uL": 15400,
            "platelets_per_uL": 252000,
            "alt_ast_U_per_L": 30,
            "crp_mg_per_L": 76.0,
            "procalcitonin_ng_per_mL": 2.4,
            "serum_sodium_mEq_per_L": 137,
        },
        "csf": {
            "opening_pressure_cmH2O": 26.0,
            "csf_wbc_per_mm3": 1600,
            "csf_neutrophil_pct": 86,
            "csf_lymphocyte_pct": 12,
            "csf_eosinophil_pct": 2,
            "csf_glucose_mg_per_dL": 34,
            "csf_protein_mg_per_dL": 180,
            "csf_lactate_mmol_per_L": 4.8,
            "csf_ada_U_per_L": None,
            "csf_crag_lfa_result": "negative",
            "csf_wet_mount_motile_amoebae": "positive",
            "csf_xanthochromia_present": False,
            "csf_rbc_per_mm3": 140,
            "csf_rbc_decreasing_across_tubes": None,
        },
        "imaging": {
            "imaging_modality": "mri_with_dwi_flair",
            "imaging_pattern": "diffuse_cerebral_edema_basilar_meningeal_enhancement",
            "imaging_finding_count": None,
            "imaging_text_summary": (
                "MRI brain with FLAIR and DWI showing mild basal "
                "cistern enhancement and early diffuse cerebral "
                "edema without focal hemorrhage; pattern consistent "
                "with early primary amebic meningoencephalitis at a "
                "treatable stage."
            ),
        },
        "diagnostic_tests": {
            "results": [
                {
                    "test_name": "CSF wet mount microscopy",
                    "result": (
                        "Motile trophozoites consistent with Naegleria "
                        "fowleri identified within 45 minutes of CSF "
                        "collection."
                    ),
                    "sensitivity_pct": None,
                    "specificity_pct": None,
                    "citation_pmid_or_doi": "PMID:40009134",
                },
                {
                    "test_name": "CSF Naegleria fowleri real-time PCR (regional reference laboratory)",
                    "result": "Positive (cycle threshold 24)",
                    "sensitivity_pct": 95.0,
                    "specificity_pct": 99.0,
                    "citation_pmid_or_doi": "PMID:40009134",
                },
            ],
        },
        "narrative_en": (
            "Fourteen-year-old previously healthy male from Kerala, "
            "India presented with three days of fever, frontal "
            "headache, vomiting, and increasing irritability after "
            "recreational swimming and underwater diving in a "
            "freshwater pond near the family residence approximately "
            "six days before symptom onset; family-recognized early "
            "decline prompted pediatric tertiary-center arrival "
            "within hours of mental-status change rather than at the "
            "obtunded stage typical of fatal cases. Examination "
            "showed temperature 39.5 C, tachycardia, neck "
            "stiffness, positive Kernig sign, and a Glasgow Coma "
            "Scale of 13. Cerebrospinal fluid showed opening "
            "pressure 26 cmH2O, white blood cell count 1,600 per "
            "cubic millimeter (86 percent neutrophils), glucose 34 "
            "mg/dL, protein 180 mg/dL, lactate 4.8 mmol/L, and "
            "motile trophozoites on wet mount; the regional "
            "reference laboratory CSF real-time PCR confirmed "
            "Naegleria fowleri. Early miltefosine was initiated "
            "within an hour of bedside microscopy, alongside "
            "intravenous amphotericin B, dexamethasone, fluconazole, "
            "azithromycin, rifampin, and aggressive intracranial "
            "pressure control. The patient avoided endotracheal "
            "intubation, with gradual neurologic improvement over "
            "the first week of admission. He was discharged from "
            "the pediatric intensive care unit on hospital day 14 "
            "and from acute care on hospital day 22 with preserved "
            "cognition and mild residual headache, representing one "
            "of the recent pediatric PAM survivors documented in "
            "the modern miltefosine era."
        ),
        "narrative_es": (
            "Adolescente varón previamente sano de 14 años, "
            "residente en Kerala, India, que presentó tres días de "
            "fiebre, cefalea frontal, vómitos e irritabilidad "
            "creciente tras nadar recreacionalmente y bucear en un "
            "estanque de agua dulce cerca de la residencia familiar "
            "aproximadamente seis días antes del inicio de "
            "síntomas; el reconocimiento familiar temprano del "
            "deterioro motivó la llegada al centro pediátrico "
            "terciario en horas, en lugar del estado obnubilado "
            "típico de los casos fatales. El examen mostró "
            "temperatura 39.5 C, taquicardia, rigidez de nuca, "
            "signo de Kernig positivo y escala de Glasgow de 13. "
            "El líquido cefalorraquídeo mostró presión de apertura "
            "26 cmH2O, leucocitos 1,600 por mm3 (86 por ciento "
            "neutrófilos), glucosa 34 mg/dL, proteína 180 mg/dL, "
            "lactato 4.8 mmol/L y trofozoítos móviles en frotis "
            "directo; el laboratorio regional de referencia "
            "confirmó Naegleria fowleri por PCR en LCR. Se inició "
            "miltefosina temprana en la primera hora tras la "
            "microscopía a la cabecera, junto con anfotericina B "
            "intravenosa, dexametasona, fluconazol, azitromicina, "
            "rifampicina y control agresivo de presión "
            "intracraneal. El paciente evitó la intubación "
            "endotraqueal, con mejoría neurológica gradual durante "
            "la primera semana del ingreso. Fue egresado de la "
            "unidad de cuidados intensivos pediátricos en el día "
            "hospitalario 14 y de hospitalización aguda en el día "
            "22 con cognición preservada y cefalea residual leve, "
            "representando uno de los sobrevivientes pediátricos "
            "recientes de PAM documentados en la era moderna de "
            "la miltefosina."
        ),
    }


# ============================================================================
# Public API
# ============================================================================


def load_pmid_metadata(pmid: str) -> dict[str, Any]:
    """Look up registered metadata for a PMID.

    Args:
        pmid: PubMed ID as string (matches PMID_REGISTRY keys).

    Returns:
        Dict with pmid, doi, authors_short, authors_full, journal, year,
        volume, issue, pages, title, anchor_type, verification_confidence,
        last_verified_date, caveat.

    Raises:
        KeyError: if pmid is not registered.
    """
    logger.debug("load_pmid_metadata(%r)", pmid)
    if pmid not in PMID_REGISTRY:
        raise KeyError(
            f"PMID {pmid!r} not registered in PMID_REGISTRY. "
            f"Known PMIDs: {sorted(PMID_REGISTRY.keys())}"
        )
    return PMID_REGISTRY[pmid]


def generate_vignette(
    spec: dict[str, Any],
    pmid_meta: dict[str, Any],
) -> dict[str, Any]:
    """Build one vignette dict from a distribution spec entry plus PMID metadata.

    Composes shared boilerplate (case_id, ground_truth_class, demographics,
    adjudication, literature_anchors, provenance) with cluster-specific
    clinical content. Vignette 1 (splash_pad late fatal) is fully
    implemented; other vignettes raise NotImplementedError until their
    cluster-specific builder is added.

    Args:
        spec: One entry from DAY1_DISTRIBUTION.
        pmid_meta: Output of load_pmid_metadata for this vignette's anchor.

    Returns:
        Dict matching VignetteSchema v2.0 (passes model_validate).
    """
    vignette_id = spec["vignette_id"]

    builders = {
        1: _build_vignette_001,
        2: _build_vignette_002,
        3: _build_vignette_003,
        4: _build_vignette_004,
        5: _build_vignette_005,
        6: _build_vignette_006,
        7: _build_vignette_007,
        8: _build_vignette_008,
        9: _build_vignette_009,
        10: _build_vignette_010,
        11: _build_vignette_011,
        12: _build_vignette_012,
        13: _build_vignette_013,
        14: _build_vignette_014,
        15: _build_vignette_015,
        16: _build_vignette_016,
        17: _build_vignette_017,
        18: _build_vignette_018,
        19: _build_vignette_019,
        20: _build_vignette_020,
    }
    if vignette_id in builders:
        clinical = builders[vignette_id]()
    else:
        raise NotImplementedError(
            f"Vignette {vignette_id} ({spec['cluster']} / {spec['stage']} / "
            f"{spec['outcome']}) not yet implemented. Step D iteration: add "
            f"the cluster-specific builder before generating this vignette."
        )

    region = _GEOGRAPHY_TO_SCHEMA_REGION.get(spec["geography_label"], "other_global")
    ethnicity = "white_non_hispanic" if region == "us_south" else "other"

    return {
        "schema_version": "2.0",
        "case_id": _build_case_id(spec, pmid_meta),
        "ground_truth_class": 1,
        "demographics": {
            "age_years": spec["age_years"],
            "sex": spec["sex"],
            "ethnicity": ethnicity,
            "geography_region": region,
            "altitude_residence_m": 100,
        },
        "history": clinical["history"],
        "exposure": clinical["exposure"],
        "vitals": clinical["vitals"],
        "exam": clinical["exam"],
        "labs": clinical["labs"],
        "csf": clinical["csf"],
        "imaging": clinical["imaging"],
        "diagnostic_tests": clinical["diagnostic_tests"],
        "adjudication": _build_adjudication(spec, pmid_meta),
        "literature_anchors": [_build_literature_anchor(pmid_meta)],
        "provenance": _build_provenance(spec, pmid_meta),
        "narrative_es": clinical["narrative_es"],
        "narrative_en": clinical["narrative_en"],
    }


def validate_against_schema(vignette: dict[str, Any]) -> bool:
    """Validate a vignette dict against VignetteSchema v2.0.

    Args:
        vignette: Vignette dict produced by generate_vignette.

    Returns:
        True if validation passes, False if a ValidationError is raised
        (the error is logged at WARNING level for debugging).
    """
    try:
        VignetteSchema.model_validate(vignette)
        return True
    except ValidationError as exc:
        logger.warning("Schema validation failed: %s", exc)
        return False


def write_vignette(vignette: dict[str, Any], filepath: Path) -> None:
    """Write a validated vignette dict to disk as JSON.

    Format: UTF-8, indent=2, sort_keys=False, ensure_ascii=False so non-ASCII
    glyphs in author lists and geography labels round-trip cleanly. Validates
    before writing; refuses to write a vignette that fails schema validation.

    Args:
        vignette: Vignette dict produced by generate_vignette.
        filepath: Output path (typically OUTPUT_DIR / spec["filename"]).

    Raises:
        ValueError: if validation fails (the file is not written).
    """
    if not validate_against_schema(vignette):
        raise ValueError(
            f"Vignette failed VignetteSchema validation; will not write to "
            f"{filepath}"
        )
    filepath.parent.mkdir(parents=True, exist_ok=True)
    filepath.write_text(
        json.dumps(vignette, indent=2, sort_keys=False, ensure_ascii=False),
        encoding="utf-8",
    )
    logger.info("Wrote %s", filepath)


def main() -> None:
    """CLI entry point.

    Step D testing phase: requires --vignette-id (no all-vignettes loop until
    each per-vignette builder has been reviewed and approved).

    Args (via argparse):
        --output-dir: override default OUTPUT_DIR.
        --dry-run: validate and print JSON to stdout instead of writing.
        --vignette-id: required during Step D; integer 1-20 selecting one
            DAY1_DISTRIBUTION entry.
    """
    parser = argparse.ArgumentParser(
        description="Generate Day 1 PAM vignettes for Subphase 1.2.",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=OUTPUT_DIR,
        help=f"Output directory (default: {OUTPUT_DIR}).",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Validate vignette and print JSON to stdout instead of writing.",
    )
    parser.add_argument(
        "--vignette-id",
        type=int,
        default=None,
        help="Required during Step D testing: integer 1-20 selecting one vignette.",
    )
    args = parser.parse_args()

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    )

    if args.vignette_id is None:
        logger.error(
            "Use --vignette-id to generate one at a time during Step D testing phase"
        )
        sys.exit(1)

    spec = next(
        (v for v in DAY1_DISTRIBUTION if v["vignette_id"] == args.vignette_id),
        None,
    )
    if spec is None:
        logger.error(
            "vignette_id %d not found in DAY1_DISTRIBUTION (valid range 1-20)",
            args.vignette_id,
        )
        sys.exit(1)

    pmid_meta = load_pmid_metadata(spec["pmid"])
    vignette = generate_vignette(spec, pmid_meta)

    if not validate_against_schema(vignette):
        logger.error("Vignette %d failed schema validation", args.vignette_id)
        sys.exit(1)

    if args.dry_run:
        logger.info("Dry-run mode: printing JSON to stdout (no file write)")
        print(json.dumps(vignette, indent=2, sort_keys=False, ensure_ascii=False))
        return

    filepath = args.output_dir / spec["filename"]
    write_vignette(vignette, filepath)


if __name__ == "__main__":
    main()
