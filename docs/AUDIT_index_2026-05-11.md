# AUDIT index — per-anchor verification bundles 2026-05-11

## Build summary

- **Total bundles built**: 21
- **Total vignettes covered**: 140 / 140
- **Total unique anchors**: 53
- **Big anchors (>=5 vignettes)**: 12
- **Class-locked batches**: 9
- **NCBI fetch success**: 53 / 53
- **NCBI failures**: 0
- **Registry-vs-NCBI deltas detected**: 23
- **Build date**: 2026-05-11

## Big-anchor bundles (priority review)

| Anchor | Author Year | Vignettes | Filename |
|---|---|---|---|
| pmid | Tyler 2018 | 13 | `AUDIT_anchor_30089069_Tyler_2018.md` |
| pmid | Tunkel 2004 | 10 | `AUDIT_anchor_15494903_Tunkel_2004.md` |
| pmid | Granerod 2010 | 9 | `AUDIT_anchor_20952256_Granerod_2010.md` |
| pmid | Bijlsma 2016 | 6 | `AUDIT_anchor_26652862_Bijlsma_2016.md` |
| pmid | Whitley 2006 | 6 | `AUDIT_anchor_16675036_Whitley_2006.md` |
| pmid | Thwaites 2004 | 6 | `AUDIT_anchor_15496623_Thwaites_2004.md` |
| pmid | Heemskerk 2016 | 6 | `AUDIT_anchor_26760084_Heemskerk_2016.md` |
| pmid | Kemble 2012 | 5 | `AUDIT_anchor_22238170_Kemble_2012.md` |
| pmid | Anjum 2021 | 5 | `AUDIT_anchor_34307045_Anjum_2021.md` |
| pmid | Capewell 2015 | 5 | `AUDIT_anchor_26582886_Capewell_2015.md` |
| pmid | van 2004 | 5 | `AUDIT_anchor_15509818_van_2004.md` |
| pmid | Soeters 2020 | 5 | `AUDIT_anchor_32935747_Soeters_2020.md` |

## Class-locked batch bundles

| Class | Batch label | Vignettes | Filename |
|---|---|---|---|
| bact | class=bact batch 1 | 4 | `AUDIT_anchor_batch_bact_01_2026-05-11.md` |
| fungal | class=fungal batch 1 | 2 | `AUDIT_anchor_batch_fungal_01_2026-05-11.md` |
| gae | class=gae batch 1 | 2 | `AUDIT_anchor_batch_gae_01_2026-05-11.md` |
| pam | class=pam batch 1 | 14 | `AUDIT_anchor_batch_pam_01_2026-05-11.md` |
| pam | class=pam batch 2 | 12 | `AUDIT_anchor_batch_pam_02_2026-05-11.md` |
| pam | class=pam batch 3 | 11 | `AUDIT_anchor_batch_pam_03_2026-05-11.md` |
| pam | class=pam batch 4 | 8 | `AUDIT_anchor_batch_pam_04_2026-05-11.md` |
| tb | class=tb batch 1 | 4 | `AUDIT_anchor_batch_tb_01_2026-05-11.md` |
| viral | class=viral batch 1 | 2 | `AUDIT_anchor_batch_viral_01_2026-05-11.md` |

## NCBI fetch failures

_None._

## Registry-vs-NCBI deltas detected

These deltas are surfaced inside each bundle's `### Registry-vs-NCBI delta` section and require Claude chat review.

| PMID | Author | Year | n_deltas | fields |
|---|---|---|---|---|
| 32935747 | Soeters | 2020 | 6 | first_author_surname, journal, volume, issue, pages, doi |
| 11873028 | Mylonakis | 2002 | 6 | first_author_surname, journal, volume, issue, pages, doi |
| 26582886 | Capewell | 2015 | 1 | pages |
| 26652862 | Bijlsma | 2016 | 1 | pages |
| 15509818 | van | 2004 | 1 | pages |
| 15494903 | Tunkel | 2004 | 1 | pages |
| 16675036 | Whitley | 2006 | 1 | pages |
| 20952256 | Granerod | 2010 | 1 | pages |
| 15496623 | Thwaites | 2004 | 1 | pages |
| 26760084 | Heemskerk | 2016 | 1 | pages |
| 22919000 | Yoder | 2012 | 1 | pages |
| 21291600 | Shakoor | 2011 | 1 | pages |
| 25625800 | Abrahams-Sandí | 2015 | 1 | pages |
| 8458963 | Lares-Villa | 1993 | 1 | pages |
| 38526236 | Burki | 2024 | 1 | first_author_surname |
| 15504272 | Cogo | 2004 | 1 | pages |
| 25667249 | Linam | 2015 | 1 | pages |
| 19845995 | Yoder | 2010 | 1 | pages |
| 25595746 | Cope | 2015 | 1 | doi |
| 27831604 | Davalos | 2016 | 1 | doi |
| 24655399 | van | 2014 | 1 | pages |
| 20822958 | Marais | 2010 | 1 | pages |
| 17262720 | Singh | 2007 | 1 | pages |

## User Assignment

1. **Upload to Claude chat** (drag & drop), in priority order:
   - Big anchors first: `AUDIT_anchor_<pmid>_<author>_<year>.md`
   - Then class-locked batches per class: `AUDIT_anchor_batch_<class>_<n>_*.md`
2. **Claude chat fills `REVIEWER NOTES` section** per vignette via research mode (PubMed lookup of anchor paper, compare to vignette content).
3. **After all bundles reviewed**, Claude chat consolidates findings into `docs/AUDIT_findings_consolidated_2026-05-11.md`.
4. **Errata 5.4.3.2 (bundled)** generated FROM the consolidated findings.

## Bundle output size

- Total bundle files: 21
- Total size: ~983 KB
- Total ~tokens (chars/4): ~251K
