# Research / Exposure Analytics Engine

Current implementation: `tools/build_analytics_store.py`

The analytics layer is deliberately **derived**. Raw files in `EXPOSURE_STATS`, `LIVE_RESEARCH_UPDATES`, `OUTSIDE RESEARCH LIBRARY`, and `PRIOR_ART` remain the evidence of record.

## Why SQLite

The source material is heterogeneous: CSV tables, PDFs, screenshots, scanner JSON, transcripts, GitHub statistics, and manually assembled historical material. A single giant CSV would either lose structure or become full of one-off columns.

SQLite gives us a local, inspectable relational layer that can be rebuilt from the repository and queried from Python, command-line SQLite, notebooks, or later UI tools.

Default database:

```text
derived/analytics/research_analytics.sqlite
```

The database should not be committed as if it were primary evidence. It can always be regenerated.

## Version 0.1 behavior

The builder currently:

1. inventories the selected source areas;
2. hashes each source artifact with SHA-256;
3. records file path, size, extension, source family and media type;
4. records the schema and row count of CSV files;
5. normalizes Spotify-style episode tables when they contain `Episode title`, `Publish date`, and `Episode URI`;
6. normalizes numeric matrix tables such as geography percentages or age-by-gender percentages;
7. ingests JSON output produced by `tools/arxiv_sat_scanner.py` into research-item and scan-match tables;
8. records unhandled/needs-adapter artifacts rather than silently discarding them.

The generic numeric-matrix adapter treats the first column as a dimension and numeric later columns as metrics. This is appropriate for tables such as `Age, Total percentage, Male percentage, ...` and `Geo, Percentage`; it is only used when the sampled later cells are actually numeric.

## Safe use

Dry-run is default:

```text
py tools/build_analytics_store.py
```

Build the database:

```text
py tools/build_analytics_store.py --apply
```

Test a bounded prefix while developing adapters:

```text
py tools/build_analytics_store.py --max-files 50 --apply
```

Override or add source scopes:

```text
py tools/build_analytics_store.py --scope EXPOSURE_STATS --scope LIVE_RESEARCH_UPDATES --apply
```

Include `H(s)H_Toolkit` in the artifact inventory when useful:

```text
py tools/build_analytics_store.py --include-toolkit --apply
```

## Core tables

### `source_artifact`

One row per input file. Holds the durable path/hash identity and adapter state.

### `csv_schema`

Headers, row count, and delimiter for every ingested CSV whether or not a full semantic adapter exists. This makes unsupported CSV families visible and lets us prioritize adapters by actual need.

### `entity`

Measured objects such as podcast episodes. External identifiers such as Spotify episode URIs are retained when present.

### `observation`

Normalized measured values. Examples: episode consumption hours, completion percentage, geographic percentage, demographic percentage. Each observation points back to its exact source artifact and row locator.

### `research_item`

Deduplicated research-paper identity. arXiv IDs are version-normalized for identity while the latest observed version remains in the record. DOI is used where available; normalized title hash is fallback identity.

### `research_match`

A paper's appearance in a particular SAT/H(s)H arXiv scan: structural score, tier, matched sectors/features/terms, controls, contrast, and scan timestamp. Keeping scan observations separate from paper identity lets us analyze scanner evolution over time.

### `import_note`

Parser warnings/errors or other import facts. Ambiguity is recorded instead of silently guessed away.

## Adapter philosophy

Do not build a parser that tries to infer everything from filenames. Add adapters for recurring source families with stable schemas.

Recommended next adapters, after inventorying the actual unsupported CSV schemas:

- Spotify aggregate show-level metrics;
- GitHub traffic/referrer/clone/view data;
- episode discovery/source-of-play data;
- public-release / transcript chronology;
- existing `EXP_ANALYSIS` timeline datasets;
- manual-entry bridge for values available only in PDFs/screenshots.

PDF/screenshot values should first pass through ordinary extraction/OCR. If a table cannot be recovered deterministically, a manual record is acceptable **only** when it preserves source path, page/image locator, transcription author/method, and review state.

## Descriptive before causal

The first analytics products should be descriptive:

- exposure over time;
- episode-level consumption and completion;
- audience geography/demographics;
- repository traffic;
- release/publication chronology;
- field-literature feature prevalence;
- external research-item chronology.

Correlations can then be explored, but public exposure, a later external publication, or changing vocabulary does not by itself demonstrate influence or copying. Influence/priority analysis needs independent chronological and substantive evidence.

## Relationship to the arXiv scanner

`tools/arxiv_sat_scanner.py` remains the discovery/scoring tool. The analytics store is the persistence and comparison layer.

A useful long-term cycle is:

```text
scan -> normalize -> deduplicate -> persist -> review -> retrieve full text -> compare -> timeline -> citation intake
```

The scanner's structural score is triage. It is never converted automatically into an equivalence or novelty judgment.

## Planned manual-review bridge

Some archive evidence is intrinsically mixed or historical. A later schema revision should add reviewed manual observations/annotations with fields for source artifact, locator, value/assertion, reviewer, confidence, and notes. This is preferable to embedding one-off guesses in source-specific parsing code.

## Query examples

Once built, ordinary SQL can ask questions such as:

```sql
SELECT label, value_numeric
FROM observation
JOIN entity ON entity.id = observation.entity_id
WHERE metric = 'Consumption time (hours)'
ORDER BY value_numeric DESC;
```

or:

```sql
SELECT title, published, score, sectors_json
FROM research_item
JOIN research_match ON research_match.research_item_id = research_item.id
WHERE score >= 10
ORDER BY published, score DESC;
```

The query result is an analytical view. Any important factual or priority conclusion should still be traced through `source_artifact` to the underlying file/paper.
