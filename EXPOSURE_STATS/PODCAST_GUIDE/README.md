# Central Podcast Episode Guide

**Status:** ACTIVE cross-repo source/index home  
**Scope:** podcast transcripts, episode metadata, analytics/exposure records, and mechanically derived transcript text across `Satobloc/HSH_RESOURCES`, `Satobloc/HsH`, and `Satobloc/SAT_THEORY_ARCHIVE_2023-25`.

## Purpose

This directory is the canonical **combined podcast index layer**. It does not replace or relocate raw sources. Instead it records every located source instance, groups defensibly identical episode material, extracts mechanically searchable text, and links analytics/metadata to episodes while preserving repository/path provenance.

The source-of-truth rule is:

> raw source remains canonical; this directory contains derived discovery/index artifacts.

Podcast material has a special theory-status rule: transcripts primarily establish **what was said publicly** and how SAT/H(s)H was publicly framed. They are not automatically exact canonical theory definitions. Episodes explicitly tasked with finding new insights, reading between the lines, determining convergences, or similar receive an `insight_generation_requested` review flag, but still require source/mathematical review before any theory promotion.

## Known source locations

The builder searches all three repositories rather than relying only on these paths, because historical podcast material has moved and been duplicated.

### `[RESOURCES]` — `Satobloc/HSH_RESOURCES`

Primary current transcript/metadata collection:

- `EXPOSURE_STATS/PODCAST_EPs/`
  - individual and compiled transcript/field-note text;
  - subtitle files including current *The New Physics* episodes;
  - `DAI_Transcripts_TEXT.txt` aggregate corpus;
  - `DebatingA.I.OnScience_EpisodeRankings_all-time.csv` episode metadata/ranking export;
  - existing `CROSS_TRANSCRIPT_*` generated indexes.

Primary current analytics/exposure collection:

- `EXPOSURE_STATS/SAT — PODCAST STATS/`
  - platform analytics CSVs;
  - screenshots and other exposure-stat captures.

### Historical public archive — `Satobloc/SAT_THEORY_ARCHIVE_2023-25`

Known historical analytics collection:

- `SAT PODCAST STATS/`
  - listenership/statistics source text and historical analytics material.

The cross-repo scanner also searches the remainder of the archive for podcast/transcript/episode material and records any additional discovered locations rather than assuming this folder is exhaustive.

### Current public repo — `Satobloc/HsH`

The public project already contains the durable guide design at:

- `WORKSPACES/COMMON/PODCAST_EPISODE_GUIDE_PLAN.md`

The cross-repo scanner searches the full current repository for transcript/episode/analytics source folders as well. This is intentional: current public podcast material should be discovered from the repository state rather than maintained as a second manually typed folder list.

## Generated products

`tools/build_cross_repo_podcast_guide.py` writes:

- `SOURCE_INVENTORY.csv` — one row per located source instance, preserving repo, path, blob/content hash, size, type, and duplicate group;
- `EPISODES.json` — machine-readable logical episode records with all linked source instances;
- `EPISODES.csv` — flat episode table for spreadsheet/filter use;
- `EPISODE_GUIDE.md` — chronological human-readable episode guide;
- `ANALYTICS_INVENTORY.csv` — analytics/exposure sources, kept separate from theory evidence;
- `MANIFEST.json` — input repository commits, builder version, counts, and derived-file hashes;
- `text/` — mechanically cleaned transcript text, one derived file per transcript source instance;
- `cues/` — timestamp-preserving JSONL for SRT/VTT sources.

Existing `CROSS_TRANSCRIPT_*` products remain valid historical/generated artifacts. This guide supersedes them as the **cross-repository episode/source registry**, while retaining them as useful keyword-index inputs until explicitly retired.

## Episode/source model

A logical episode and a source file are different things.

Each `EPISODES.json` record may contain several `source_instances`, for example:

- an SRT subtitle file;
- an older TXT transcript of the same episode;
- an aggregate-corpus occurrence;
- a Spotify/ranking metadata row;
- analytics snapshots from different dates;
- historical archive copies.

Exact duplicate files are detected by SHA-256. Same-title/non-identical files are **not** silently collapsed as exact duplicates. Episode grouping is conservative and records the basis used.

Core episode fields:

```text
episode_id
series
series_aliases
title
published_date
published_date_basis
published_date_confidence
episode_number_if_known
duration
spotify_uri_or_url
source_instances[]
transcript_status
derived_text_paths[]
analytics_sources[]
public_exposure_evidence
interpretive_task_class
rigor_signal
terminology_hazards[]
review_status
notes
```

## Transcript extraction rule

Raw transcript/subtitle files are never rewritten in place.

Derived text is **mechanical only**:

- remove SRT/VTT cue numbers and timestamps;
- retain spoken text in source order;
- remove exact adjacent duplicate caption fragments only where mechanically safe;
- do not paraphrase;
- do not repair scientific terminology;
- do not silently change `field` to geometry, historical boson/fermion vocabulary, or any other theory wording;
- preserve ASR oddities in the extracted text; corrections belong in a separate annotation layer.

For SRT/VTT, the cue JSONL retains timing and raw cue text so searches can return to the public wording at a specific point in an episode.

## Analytics rule

Analytics are **exposure evidence**, not theory authority. An analytics source can establish platform reach, listeners, ranking, geography, date snapshots, or similar metrics when its contents support those claims. It cannot promote a podcast statement to SAT/H(s)H core.

Analytics snapshots from different dates remain separate even if they describe the same episode/show.

## High-value review flags

The index may flag retrieval candidates without deciding their truth/status:

- `insight_generation_requested` — episode explicitly says the production task included deriving additional insights/convergences;
- `rigor_signal` — transcript contains rigor/method/validation vocabulary worth epistemic-method review;
- `terminology_hazard: field` — `field` language may be public-facing shorthand rather than SAT geometric ontology;
- `first_public_mention_candidate` — retrieval lead only, never an absolute FIRST without earlier-source checks.

Current known elevated case: *The New Physics — Majorana Coupling & Coiled Cooper Pairing* should receive `insight_generation_requested` because the episode explicitly describes a secondary mission of reading between the source givens to identify additional convergences.

## Public-first-appearance discipline

Use scoped labels only:

- `EARLIEST-LOCATED-PODCAST-MENTION`
- `EARLIEST-LOCATED-PUBLIC-EXPLANATION`
- `EARLIEST-LOCATED-PUBLIC-EQUATION`
- `EARLIER-PUBLIC-SOURCE-KNOWN`
- `SEARCH-INCOMPLETE`
- `DATE-UNCERTAIN`

Do not use an unqualified `FIRST` field.

## Privacy / quarantine

The full combined index remains in private `HSH_RESOURCES` because it may point to private analytics/source locations. A later public guide can be generated as a sanitized projection containing only explicitly public source instances.

`PRIOR_ART` and any other quarantined root are excluded **before traversal**. They are not podcast discovery inputs.

## Build / refresh

The builder is intended to run with three checkouts available simultaneously, e.g.:

```bash
python tools/build_cross_repo_podcast_guide.py \
  --resources-root . \
  --hsh-root ../HsH \
  --archive-root ../SAT_THEORY_ARCHIVE_2023-25
```

Every build records the exact input commit for each checkout. A later workflow may automate this, but raw-source preservation and current-SHA write safety remain mandatory.
