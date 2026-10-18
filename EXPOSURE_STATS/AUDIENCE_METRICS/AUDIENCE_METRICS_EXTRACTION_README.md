# Audience metrics extraction and analysis notes

Date: 2026-10-18  
Repository: `Satobloc/HSH_RESOURCES`  
Source directory: `EXPOSURE_STATS/AUDIENCE_METRICS/`  
Status: Documentation; extraction not yet independently verified end-to-end.

## Purpose

Consolidate every CSV under this directory into one provenance-preserving JSON file for reproducible analysis of *The New Physics* podcast audience, with particular attention to geographic distributions, demographic data, episode consumption, completion, and retention.

## Extractor

Script: `extract_audience_metrics.py` (prepared locally in the October 18, 2026 conversation; it is **not** deployed to this repository merely by creating this README).

The script requires Python 3.9+ and uses the standard library only. It queries the GitHub contents API recursively for CSV files on `main`, retrieves raw CSV content, decodes UTF-8 with BOM handling, and writes `audience_metrics_complete.json`.

Run it from the directory containing the script:

```bash
python extract_audience_metrics.py
```

Or choose a destination:

```bash
python extract_audience_metrics.py /path/to/audience_metrics_complete.json
```

The output includes extraction timestamp, source repository, source paths, original CSV headers and rows, raw CSV text, Git blob SHA, SHA-256, file counts, row totals, and a list of failures. Exit status 1 means at least one file failed, and the JSON marks `complete: false`. Successful completion must be established by checking this field and the source file inventory, not assumed.

## Source inventory at documentation time

85 directory entries were identified, predominantly geographical CSV exports. Several files are numbered `TheNewPhysics_GeoLocationAllPlatforms_all-time (N).csv`; these must **not** be treated as independent samples without checking the geographic hierarchy. Primary files also include age-by-gender, gender, completion, consumption, weekly retention, and recent-window geography.

## Methodological guardrails

- Do not add percentages across geographic hierarchy levels, platforms, or reporting windows.
- Do not infer unique listener counts from percentages without denominators.
- Very small audiences can yield extreme percentages (for example, 100% retention with a denominator of one).
- A city appearance is evidence of platform-reported geolocation, not confirmation of a resident's identity or exact physical whereabouts.
- Geographic outliers require explicit population baselines, sampling uncertainty, and multiple-comparison correction.
- Record whether each statement comes from an observed metric, a calculation, or a hypothesis.
- The geographical connection being examined includes Virginia, Minnesota; Clio, Iowa; and Hagerstown, Maryland. Their presence in a specific export must be verified, not presumed.

## Initial observations (not independently revalidated)

All-time geography reports approximately 94.46% United States. Age 35–44 is approximately 22.94%, and 45–59 approximately 64.18%. These are percentages as provided in source exports, not inferred unique-person statistics. The 2026-09-19 through 2026-10-18 source window is distinct from all-time data.

## Follow-up validation

1. Place the extractor script next to this README, or use the locally provided script.
2. Execute with network access; inspect the command's exit code.
3. Verify `complete == true`, zero failures, and file-count agreement with a fresh directory listing.
4. Recover the full city-level records and build a hierarchy-aware location table.
5. Search for the three target cities and assess repetition and reporting periods before interpreting a pattern.

No analysis in this document is a claim of coordinated listening or causal connection.

## Workflow discovery and execution route (2026-10-18)

A cross-repository review found:

- [RESOURCES] `tools/build_analytics_store.py`: existing source-traceable CSV and JSON ingestion into SQLite, with `--scope`, `--apply`, source SHA-256 and row/schema accounting. The existing `cross-diffusion-data.yml` invokes it but **does not currently include `EXPOSURE_STATS/AUDIENCE_METRICS`** among its explicitly named scopes. Its current trigger covers `EXPOSURE_STATS/**`, so avoid assuming a trigger implies inclusion.
- [RESOURCES] `.github/workflows/extract-papers.yml`: safe automated checkout, Python execution, validation, and commit machinery, but its PDF extractor is not a CSV consolidation tool.
- [[HsH]] `.github/workflows/extract-raw-window.yml`: request-triggered bounded extraction and output publication pattern, scoped to conversation windows.
- [[HsH]] `.github/workflows/issue-publisher.yml`: owner-authored issue intake for bounded Markdown publication to a fixed HsH path, **not** an arbitrary Python execution route or cross-repository writer.
- [[GLASS]] `.github/workflows/full-archive-index.yml`, `build-archive-structure.yml`, and `extract-pdf-text.yml`: historical archive indexing/extraction patterns.

**Preferred local implementation:** Add a narrowly scoped `[RESOURCES]/tools/build_audience_metrics.py` and a workflow under `[RESOURCES]/.github/workflows/` that triggers on changes to the audience CSVs and the script. Run against the checked-out repository (no API calls per CSV), write a deterministic provenance-preserving consolidated JSON, validate file counts/row counts and content hashes, then commit only that generated artifact with a safe fetch/rebase or concurrency-aware retry. Optionally extend `build_analytics_store.py` with the audience-metrics scope as a distinct second layer, avoiding unrelated OCR/PDF work.

**Important:** Reading these tools and recording this route does not mean the consolidator has been deployed or run. Verify workflow run, output integrity and independent repository readback before declaring completion.
