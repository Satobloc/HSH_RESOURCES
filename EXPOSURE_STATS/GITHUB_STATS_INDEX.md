# GitHub Statistics Source Index (working)

**Purpose:** A lightweight, in-folder finding aid for GitHub repository statistics and related evidence located across the three SAT / H(s)H repositories. This is an additive index only. It does not reorganize, rename, deduplicate, reinterpret, or move source files.

**Index location:** `HSH_RESOURCES/EXPOSURE_STATS/GITHUB_STATS_INDEX.md`  
**Coverage status:** Initial discovery pass, not exhaustive. Search results and known folder inventories were used; absence from this index is not evidence that a source does not exist.

## Repository map

| Repository | Role in this index | Primary locations |
|---|---|---|
| `Satobloc/HSH_RESOURCES` | Main exposure-statistics collection and working source register | `EXPOSURE_STATS/`, especially `_SAT  Satobloc GitHubStats/` |
| `Satobloc/SAT_THEORY_ARCHIVE_2023-25` | Earlier SAT-era captures and historical GitHub snapshots | `2026/SAT  Satobloc GitHubStats/`, root snapshots, `PRE_HSH_ROUNDUP/` |
| `Satobloc/HsH` | HsH-era captures, OCR/text dumps, clone-forensics and workflow-attribution material | `DEVELOPMENT_FULL_CONVOS/`, `WORKSPACES/COMMON/` |

## 1. HSH_RESOURCES — primary collection

### Main GitHubStats folder

[Open folder: EXPOSURE_STATS/_SAT Satobloc GitHubStats](https://github.com/Satobloc/HSH_RESOURCES/tree/main/EXPOSURE_STATS/_SAT%20%20Satobloc%20GitHubStats)

Key identified files:

- [58k.JPG](https://github.com/Satobloc/HSH_RESOURCES/blob/main/EXPOSURE_STATS/_SAT%20%20Satobloc%20GitHubStats/58k.JPG) — screenshot capture; OCR text is also indexed below.
- [30k.txt](https://github.com/Satobloc/HSH_RESOURCES/blob/main/EXPOSURE_STATS/_SAT%20%20Satobloc%20GitHubStats/30k.txt) — text snapshot.
- [HSH_54k.txt](https://github.com/Satobloc/HSH_RESOURCES/blob/main/EXPOSURE_STATS/_SAT%20%20Satobloc%20GitHubStats/HSH_54k.txt) — text snapshot.
- [9.8.26 -- GITSTATS.txt](https://github.com/Satobloc/HSH_RESOURCES/blob/main/EXPOSURE_STATS/_SAT%20%20Satobloc%20GitHubStats/9.8.26%20--%20GITSTATS.txt) — dated snapshot.
- [HSH_TRAFFIC_23SEP26.txt](https://github.com/Satobloc/HSH_RESOURCES/blob/main/EXPOSURE_STATS/_SAT%20%20Satobloc%20GitHubStats/HSH_TRAFFIC_23SEP26.txt) — HsH traffic capture.
- [SAT_TRAFFIC_23SEP26.txt](https://github.com/Satobloc/HSH_RESOURCES/blob/main/EXPOSURE_STATS/_SAT%20%20Satobloc%20GitHubStats/SAT_TRAFFIC_23SEP26.txt) — SAT traffic capture.
- [HSH_gitclones.txt](https://github.com/Satobloc/HSH_RESOURCES/blob/main/EXPOSURE_STATS/_SAT%20%20Satobloc%20GitHubStats/HSH_gitclones.txt) — clone-related record.
- [HSH_repo_stats.txt](https://github.com/Satobloc/HSH_RESOURCES/blob/main/EXPOSURE_STATS/_SAT%20%20Satobloc%20GitHubStats/HSH_repo_stats.txt) — repository statistics record.
- [HSH_commits.txt](https://github.com/Satobloc/HSH_RESOURCES/blob/main/EXPOSURE_STATS/_SAT%20%20Satobloc%20GitHubStats/HSH_commits.txt) and [MAIN_ARCHIVE_COMMITS.txt](https://github.com/Satobloc/HSH_RESOURCES/blob/main/EXPOSURE_STATS/_SAT%20%20Satobloc%20GitHubStats/MAIN_ARCHIVE_COMMITS.txt) — commit records.
- [GITHUB_INSIGHTS.txt](https://github.com/Satobloc/HSH_RESOURCES/blob/main/EXPOSURE_STATS/_SAT%20%20Satobloc%20GitHubStats/GITHUB_INSIGHTS.txt) — analysis / interpretation material; not an independent telemetry capture.
- [GITHUB_ASSISTANT_CONVO.txt](https://github.com/Satobloc/HSH_RESOURCES/blob/main/EXPOSURE_STATS/_SAT%20%20Satobloc%20GitHubStats/GITHUB_ASSISTANT_CONVO.txt) — discussion/context record; not an independent telemetry capture.
- [SAT_GIT_JUN10.txt](https://github.com/Satobloc/HSH_RESOURCES/blob/main/EXPOSURE_STATS/_SAT%20%20Satobloc%20GitHubStats/SAT_GIT_JUN10.txt) — earlier SAT-era record.
- [CONTROLS folder](https://github.com/Satobloc/HSH_RESOURCES/tree/main/EXPOSURE_STATS/_SAT%20%20Satobloc%20GitHubStats/CONTROLS) — control-repository material; classify each file by its explicit repository and capture identity before comparison.

The folder also contains multiple CSV exports for clones, unique cloners, views, unique visitors, commits, and code frequency, including numbered copies and renamed copies. Some have identical Git blob SHAs despite different filenames. Treat identical SHAs as duplicate file content, not independent observations. Examples include the SAT GIT-prefixed and unprefixed exports for clone, view, unique-cloner, unique-visitor, and commit series.

### Other useful files in EXPOSURE_STATS

- [github_traffic_readme.txt](https://github.com/Satobloc/HSH_RESOURCES/blob/main/EXPOSURE_STATS/github_traffic_readme.txt) — traffic metric/context notes.
- [CROSS_DIFFUSION_SOURCE_MANIFEST.csv](https://github.com/Satobloc/HSH_RESOURCES/blob/main/EXPOSURE_STATS/CROSS_DIFFUSION_SOURCE_MANIFEST.csv) — broad source-artifact manifest; useful for discovering additional traffic records.
- [CROSS_MASTER_CHRONOLOGY.md](https://github.com/Satobloc/HSH_RESOURCES/blob/main/EXPOSURE_STATS/CROSS_MASTER_CHRONOLOGY.md) — chronology/correlation surface, where present.
- [CROSS_IMAGE_TEXT_INDEX.md](https://github.com/Satobloc/HSH_RESOURCES/blob/main/EXPOSURE_STATS/CROSS_IMAGE_TEXT_INDEX.md) — image inventory and OCR-extract pointers.
- `derived/image_text/` — content-addressed OCR extracts; inspect the index and source image together.
- `EXP_ANALYSIS/CONCAT_FULL_GIT_STATS.txt` — concatenated Git-stat material, if present in the current tree.

### Screenshot/OCR lead

- [58k.JPG](https://github.com/Satobloc/HSH_RESOURCES/blob/main/EXPOSURE_STATS/_SAT%20%20Satobloc%20GitHubStats/58k.JPG) has a corresponding OCR extract under `derived/image_text/` (source-image SHA-256: `f4ea6e908c4a6efc6f5548ea6a604dcb9e6e79e1bbf51342cede60883775d2c0`). The OCR explicitly identifies `Satobloc/HsH` and reports 58,677 clones and 5,897 unique cloners in the last 14 days, with 1 unique visitor. Capture date still needs independent establishment.
- `Total views in last 14 days.png` has a corresponding OCR extract (source-image SHA-256: `0c4d76e2d2e2de7400ed865cad70c4bb3d094d855ee9a174a7bb41090c71c0a0`); OCR reports 1,022 views for the chart window Aug 30–Sep 12. Repository identity should be correlated against contemporaneous captures rather than inferred from the filename alone.

## 2. SAT_THEORY_ARCHIVE_2023-25 — historical SAT records

### Dedicated statistics folder

[Open folder: 2026/SAT Satobloc GitHubStats](https://github.com/Satobloc/SAT_THEORY_ARCHIVE_2023-25/tree/main/2026/SAT%20%20Satobloc%20GitHubStats)

Identified CSV series:

- `Clones in last 14 days.csv`
- `Commits over time.csv`
- `Satobloc's Commits.csv`
- `Total views in last 14 days.csv`
- `Unique cloners in last 14 days.csv`
- `Unique visitors in last 14 days.csv`

The two commit CSVs currently identified have the same Git blob SHA, so they are duplicate content rather than independent series.

### Other historical snapshots

- [GITHUB_8-26_STATS.txt](https://github.com/Satobloc/SAT_THEORY_ARCHIVE_2023-25/blob/main/GITHUB_8-26_STATS.txt) — historical GitHub traffic / insights snapshot.
- [PRE_HSH_ROUNDUP/github rep.txt](https://github.com/Satobloc/SAT_THEORY_ARCHIVE_2023-25/blob/main/PRE_HSH_ROUNDUP/github%20rep.txt) — earlier repository referral/traffic capture.
- [PREDICTIONS/SAT PREDICTION — METRICS + OTHER SAT's.txt](https://github.com/Satobloc/SAT_THEORY_ARCHIVE_2023-25/blob/main/PREDICTIONS/SAT%20PREDICTION%20%E2%80%94%20METRICS%20%2B%20OTHER%20SAT's.txt) — contains a historical discussion and embedded GitHub-stat material; treat as contextual evidence unless the underlying capture is independently located.

## 3. HsH — current-era captures and clone forensics

### Traffic and stats text exports

- [DEVELOPMENT_FULL_CONVOS/30SEP26_DUMP/CONCAT_FULL_GIT_STATS.txt](https://github.com/Satobloc/HsH/blob/main/DEVELOPMENT_FULL_CONVOS/30SEP26_DUMP/CONCAT_FULL_GIT_STATS.txt) — concatenated Git-stat capture material.
- [DEVELOPMENT_FULL_CONVOS/30SEP26_DUMP/gtss.txt](https://github.com/Satobloc/HsH/blob/main/DEVELOPMENT_FULL_CONVOS/30SEP26_DUMP/gtss.txt) — clone / unique-cloner traffic capture.
- [DEVELOPMENT_FULL_CONVOS/30SEP26_DUMP/gt.txt](https://github.com/Satobloc/HsH/blob/main/DEVELOPMENT_FULL_CONVOS/30SEP26_DUMP/gt.txt) — related traffic capture.
- [DEVELOPMENT_FULL_CONVOS/30SEP26_DUMP/HSH_commits.txt](https://github.com/Satobloc/HsH/blob/main/DEVELOPMENT_FULL_CONVOS/30SEP26_DUMP/HSH_commits.txt) — commit-related capture.
- [DEVELOPMENT_FULL_CONVOS/30SEP26_DUMP/HSH ACTIVITY.txt](https://github.com/Satobloc/HsH/blob/main/DEVELOPMENT_FULL_CONVOS/30SEP26_DUMP/HSH%20ACTIVITY.txt) — activity capture.
- [DEVELOPMENT_FULL_CONVOS/30SEP26_DUMP/CONTROLS.txt](https://github.com/Satobloc/HsH/blob/main/DEVELOPMENT_FULL_CONVOS/30SEP26_DUMP/CONTROLS.txt) — control material; identify repository and date from contents before assigning.
- [DEVELOPMENT_FULL_CONVOS/30SEP26_DUMP/JOINT STATS.txt](https://github.com/Satobloc/HsH/blob/main/DEVELOPMENT_FULL_CONVOS/30SEP26_DUMP/JOINT%20STATS.txt) — joint-stat capture; preserve its scope and repository attribution.
- [DEVELOPMENT_FULL_CONVOS/30SEP26_DUMP/23swp42.txt](https://github.com/Satobloc/HsH/blob/main/DEVELOPMENT_FULL_CONVOS/30SEP26_DUMP/23swp42.txt) — includes referring-site data.

Related search-discovered copies / additional captures:

- `DEVELOPMENT_FULL_CONVOS/MOSTLY_EARLY_NLM/gtss.txt`
- `DEVELOPMENT_FULL_CONVOS/MOSTLY_EARLY_NLM/factory_fresh.txt`
- `DEVELOPMENT_FULL_CONVOS/SAT_CONVOS_19/SAT_ACTIV.txt`
- `DEVELOPMENT_FULL_CONVOS/SAT_CONVOS_20/SAT_ACTIV.txt`
- `DEVELOPMENT_FULL_CONVOS/SAT_CONVOS_21/JOINT STATS.txt`

Some of these appear in more than one dump or folder. Compare content hashes before counting them as separate captures.

### Attribution / clone-forensics records

- [CLONE_FOOTPRINT_WORKER_CHECKINS_2026-11-03.md](https://github.com/Satobloc/HsH/blob/main/WORKSPACES/COMMON/CLONE_FOOTPRINT_WORKER_CHECKINS_2026-11-03.md) — worker-side clone-mechanism classification.
- [2026-11-05 clone census handoff](https://github.com/Satobloc/HsH/blob/main/WORKSPACES/COMMON/REVIVAL_ROTATION_HANDOFFS/2026-11-05T1058Z_from_s2_to_s2_tern_rook_clone_census.md) — clone census questions, workflow checkout attribution, and low/central/high internal-clone estimation instructions.
- [PHASE_STEERING_2026-10-26.md](https://github.com/Satobloc/HsH/blob/main/WORKSPACES/COMMON/PHASE_STEERING_2026-10-26.md) — identifies the cross-repository exposure/analytics workstream and the need to separate users, bots, workflows, and causal influence.

## 4. Working rules for using this index

1. **Keep source identity explicit.** Record repository, exact path, capture date/window, metric, and source type separately.
2. **Do not add overlapping rolling windows.** GitHub traffic exports commonly represent rolling 14-day windows; they are snapshots, not additive periods.
3. **Deduplicate by content identity.** Prefer Git blob SHA or SHA-256 over filename. Renamed copies are not independent evidence.
4. **Treat screenshots and OCR as paired evidence.** Record the image and OCR extract; OCR is a finding aid, and the original image remains authoritative for visual interpretation.
5. **Separate telemetry from interpretation.** CSVs, screenshots, and raw traffic dumps are capture evidence. Analysis documents and conversation transcripts are context, not independent telemetry.
6. **Preserve uncertainty in repository attribution.** Use explicit repository labels first. Where missing, apply the working chronology heuristic only as a provisional assignment: HsH first, SAT/Satobloc second, then other repositories; a lone pre-spring-2026 capture is provisionally SAT-era. Mark inferred assignments as inferred.
7. **Do not equate clones or unique cloners with people, readership, influence, or scientific uptake.** Investigate internal workflows and automation separately.
8. **Do not treat this index as an exhaustive census.** Continue adding confirmed candidates from nested folders, root-level records, OCR extracts, manifests, and conversation dumps as they are found.

## 5. Next-pass candidates

- Enumerate every item in `EXPOSURE_STATS/` and its nested folders whose filename, extracted text, or OCR mentions GitHub, traffic, clones, cloners, views, visitors, referrers, popular content, commits, or repository insights.
- Search all three repositories for screenshots and their generated OCR extracts, including images whose filenames do not mention GitHub.
- Correlate capture windows and totals across text, CSV, JSON, and screenshot records.
- Record content hashes and duplicate families before constructing a chronological ledger.
- Keep website, podcast, and general web-exposure statistics separate from GitHub repository telemetry, even when they appear in the same source bundle.

---
*Initial index prepared from a targeted cross-repository discovery pass. Update additively as additional source paths are verified.*
