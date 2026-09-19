# Episode Guide

**Seed state:** 2026-09-18 ET  
**Canonical role:** cross-repository podcast/public-exposure guide  
**Source rule:** raw transcripts remain canonical; this guide is derived discovery/index state.

Podcast transcripts primarily document **what was said publicly**. They are not automatically exact SAT/H(s)H core definitions. Episodes explicitly tasked with deriving additional insights receive elevated review, but still require source and mathematical validation.

## Verified source clusters

| Repository | Location | Material | Status |
|---|---|---|---|
| `Satobloc/HSH_RESOURCES` | `EXPOSURE_STATS/PODCAST_EPs/` | individual/compiled transcript text, SRT subtitles, episode ranking metadata, older transcript keyword indexes | current primary transcript collection |
| `Satobloc/HSH_RESOURCES` | `EXPOSURE_STATS/DEBATING AI DATA/` | Spotify-for-Creators analytics PDFs/CSVs and related show analytics | exposure/analytics evidence |
| `Satobloc/HSH_RESOURCES` | `EXPOSURE_STATS/SAT — PODCAST STATS/` | historical/current platform analytics CSVs, captures/screenshots | exposure/analytics evidence |
| `Satobloc/SAT_THEORY_ARCHIVE_2023-25` | `SAT PODCAST STATS/` | historical listenership/statistics text and analytics material | historical exposure evidence |
| `Satobloc/HsH` | `WORKSPACES/COMMON/PODCAST_EPISODE_GUIDE_PLAN.md` | existing public episode-guide design/schema | infrastructure/design, not an episode |

The cross-repository builder searches all three repositories for additional podcast/episode/show-specific paths; this table is not used as an exhaustive hard-coded whitelist.

## Seed episode/transcript catalog

This table is seeded from the established `CROSS_TRANSCRIPT_CATALOG.csv` plus the newly uploaded subtitle episode. It will be replaced/refreshed by `tools/build_cross_repo_podcast_guide.py` when the cross-repository build publishes.

| Date | Episode / transcript title | Source | Review note |
|---|---|---|---|
| 2025-02-02 | FIRST PUBLIC MENTION SAT DAI — WHAT IS THOUGHT MADE OF | `PODCAST_EPs/FIRST PUBLIC MENTION SAT DAI -- WHAT IS THOUGHT MADE OF.txt` | first-public-mention **candidate**; scoped verification required |
| 2025-12-21 | Scalar-Angular Theory Field Notes — Lithium-7: The First Dark Matter Horizon | `PODCAST_EPs/FULL_Scalar-Angular Theory_ Field Notes - Lithium-7_ The First Dark Matter Horizon_.txt` | public exposition |
| 2025-12-24 | Scalar-Angular Theory Field Notes — Proof GR & QM Are Compatible | `PODCAST_EPs/Scalar-Angular Theory_ Field Notes - Proof GR & QM Are Compatible.txt` | **P1 GR↔QM proof-recovery priority**; title wording is not itself proof certification |
| 2026-01-16 | Scalar-Angular Theory Field Notes — Post-Closure Experimental Predictions | `PODCAST_EPs/FULL_Scalar-Angular Theory_ Field Notes - Post-Closure Experimental Predictions.txt` | predictions/public-exposure record |
| 2026-01-19 | Scalar-Angular Theory Field Notes — Timelike Twist in the Accelerator | `PODCAST_EPs/FULL_Scalar-Angular Theory_ Field Notes - Timelike Twist in the Accelerator .txt` | public exposition |
| 2026-02-24 | Scalar-Angular Theory Field Notes — The 0.239 rad Constant | `PODCAST_EPs/FULL_Scalar-Angular Theory_ Field Notes - The 0.239 rad Constant.txt` | constants/symbol-history priority |
| 2026-02-25 | Scalar-Angular Theory Field Notes — SAT’s Derivations | `PODCAST_EPs/FULL_Scalar-Angular Theory_ Field Notes - SAT’s Derivations.txt` | derivation/method review priority |
| undated in current catalog | Scalar-Angular Theory Field Notes — Prior Model Prediction Drop 3.1.26 | `PODCAST_EPs/FULL_Scalar-Angular Theory_ Field Notes - Prior Model Prediction Drop 3.1.26.txt` | date/title reconciliation required |
| 2026-03-07 | Scalar-Angular Theory Field Notes — Method for QM-GR Unification | `PODCAST_EPs/FULL_Scalar-Angular Theory_ Field Notes - Method for QM-GR Unification.txt` | **P1 GR↔QM reconstruction priority** |
| 2026-03-16 | Scalar-Angular Theory Field Notes — A Lab Testable TOE | `PODCAST_EPs/FULL_Scalar-Angular Theory_ Field Notes - A Lab Testable TOE.txt` | test/methodology review priority |
| 2026-05-08 | Scalar-Angular Theory Field Notes — The 17mK He3 λ Anomaly | `PODCAST_EPs/FULL_Scalar-Angular Theory_ Field Notes - The 17mK He3 λ Anomaly.txt` | **P3 He-3 anchor priority** |
| 2026-05-09 | Scalar-Angular Theory Field Notes — Full Unification GR-QM-ST | `PODCAST_EPs/FULL_Scalar-Angular Theory_ Field Notes - Full Unification GR-QM-ST.txt` | **P1 GR↔QM reconstruction priority** |
| undated in current catalog | Scalar-Angular Theory Field Notes — Neutrino-Photon Identity, Quantum Tunneling, and Chondrules(..!) | `PODCAST_EPs/FULL_Scalar-Angular Theory_ Field Notes - Neutrino-Photon Identity, Quantum Tunneling, and Chondrules(..!).txt` | traveling-excitation/history priority |
| 2026-09-06 | The New Physics — Majorana Coupling & Coiled Cooper Pairing | `PODCAST_EPs/The New Physics - Majorana Coupling & Coiled Cooper Pairing.srt` | `insight_generation_requested`; He-3/Majorana/Cooper/parafermion candidate insights |

## Generated index/extraction format

The cross-repository builder writes:

- `SOURCE_INVENTORY.csv` — every located source instance with repo/path/hash/type and exact-duplicate grouping;
- `ANALYTICS_INVENTORY.csv` — analytics/metadata/capture sources separated from transcript authority;
- `EPISODES.json` — logical episode records with all linked source instances;
- `EPISODES.csv` — flat filterable episode index;
- `MANIFEST.json` — exact input repo commits and build counts;
- `text/*.txt` — mechanically derived transcript text with provenance header;
- `cues/*.jsonl` — timestamp-preserving subtitle cues for SRT/VTT sources.

Raw SRT/VTT/TXT is never rewritten. Derived text removes subtitle timing/sequence markup only; it does **not** paraphrase, fix ASR language, normalize SAT terminology, change `field` wording, or silently update historical theory language.

## Retrieval/review flags

High-value automatic retrieval signals include:

- `insight_generation_requested`
- `rigor_signal`
- `terminology_hazard_field`
- exact duplicate/source-copy groups
- transcript date/title disagreement
- first-public-mention **candidate** status

A retrieval flag is not a theory-status judgment.
