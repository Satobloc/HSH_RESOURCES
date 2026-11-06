# Fourth-Dimension History Harvester

**Version:** 0.2.0  
**Repository:** `Satobloc/HSH_RESOURCES`  
**Tool location:** `tools/fourth_dimension_history_harvester/`  
**Only write target:** `HISTORICAL/FOURTH_DIMENSION_HISTORY/harvested/`

A reproducible, bounded source-acquisition tool for the history of physical/spatial higher-dimensional thought, the Zöllner–Slade affair, spiritualism stigma, scientific boundary-setting, and possible academic career consequences.

The harvester is a **source collector**, not a historical adjudicator. A search hit is a lead, not evidence that a proposition is true. It retains query provenance, source identifiers, publication dates, source URLs, rights metadata, provider fields, snippets where available, and content hashes for downloaded objects.

## Current provider adapters

| Provider | Operation | Retained material | Limitations |
|---|---|---|---|
| **Deutsches Zeitungsportal (DDB)** | Page-level OCR search in `newspaper-issues` Solr collection | Page identifiers, newspaper title/date/place/provider, page number, highlighted OCR snippets, hit totals, viewer links | Requires a DDB API key. The general Search API is officially documented; the newspaper-specific collection/field layout is not fully specified in the public docs and is schema-checked at run time. Results are relevance-ranked, not chronological. |
| **ANNO / Austrian National Library** | Search newspaper/periodical issues; optional page snippets | Issue identifiers, title, date/year, place/language, matching-hit counts, optional page-level snippets and page links | Uses the currently observed AnnoSearch web-app backend, which ANNO does not publish as an official API. Explicit opt-in required; may drift. Do not assume a failed IIIF request means OCR text is absent. |
| **Library of Congress, Chronicling America** | Current loc.gov JSON API | U.S. newspaper metadata and OCR text returned in the record | U.S. coverage; not a European archive substitute. |
| **Internet Archive** | Advanced Search and item metadata | Catalogue metadata, rights/license fields, candidate PDF links | Search result paging bounded; automatic downloads need explicit license evidence. |
| **Crossref** | Works metadata search | DOI, title, authors, journal, date, abstract, publisher, links | Bibliographic metadata, not a full-text newspaper or journal search. |
| **OpenAlex** | Works metadata search | DOI, title, authors, year, venue, OA status, abstract and OA link | Full-text availability varies. OA status alone does not authorize downloading. |
| **Generic OAI-PMH** | Bounded `ListRecords` | Dublin Core metadata and repository identifiers | Supply endpoint. Number of batches is capped and recorded. |
| **Saved HTML** | Import a locally saved, already-rendered portal result page | Link labels, canonical URL, source page title, local source path | JavaScript-only pages may not preserve results in saved HTML. |
| **Local seed files** | Register explicit local PDFs, text, HTML, XML, or JSON | SHA-256, byte size, page count and available metadata | Source file is not copied into the repository by the registration step. |

See `HISTORICAL/FOURTH_DIMENSION_HISTORY/source_registry.json` for endpoint details, authentication, status, and manual archival targets.

## Install

Python 3.10+ is sufficient for searching and metadata harvesting. The repository already includes `pypdf` in `requirements-tools.txt` for optional PDF metadata extraction.

```bash
python -m pip install -r requirements-tools.txt
```

## Run it

From a local checkout of `Satobloc/HSH_RESOURCES`:

```bash
# Preview only. Makes network requests but writes no repository files.
python tools/fourth_dimension_history_harvester/harvest.py \
  --repo-root . --query-group core --limit 10

# Save records and a run manifest in a new, immutable run folder.
python tools/fourth_dimension_history_harvester/harvest.py \
  --repo-root . --query-group stigma --start-year 1876 --end-year 1938 \
  --limit 20 --apply

# Save a local source file's hash and metadata, without copying the source binary.
python tools/fourth_dimension_history_harvester/harvest.py \
  --repo-root . --providers '' --query-group manual \
  --import-file /path/to/ONB_nwg_19241121.pdf \
  --import-file-url 'https://anno.onb.ac.at/' --apply

# Import a saved browser capture from DDB, ANNO, Kalliope, or another archive.
python tools/fourth_dimension_history_harvester/harvest.py \
  --repo-root . --providers '' --query-group manual \
  --import-html /path/to/saved-results.html --apply
```

Use `--query` to append one-off searches and `--config` to point to a revised copy of `queries.json`. The `manual` query group is intentionally empty so a one-off query can be run without inheriting the default `core` set.

### DDB full-text newspaper search

The official DDB API documentation requires a registered user and API key. Create a DDB account, generate an API key in the account's *My DDB* area, and set it in the environment. Do not place the key in the repository, configuration, or run manifest.

```bash
export DDB_API_KEY='your-key'
python tools/fourth_dimension_history_harvester/harvest.py \
  --repo-root . --providers ddb --query-group manual \
  --query '"vierte dimension"' \
  --start-year 1870 --end-year 1945 \
  --limit 1000 --ddb-max-pages 10 --apply
```

DDB returns individual newspaper pages with highlighted OCR snippets. The portal search capture supplied on 2026-11-05 reported 42,708 matches for the literal phrase `vierte dimension`; that number is a **portal-reported search count**, not a number of relevant articles. The API query syntax, date filtering, and index can produce a different count. Each page result records the reported count, page sweep, and whether the configured page ceiling was reached.

The `--ddb-max-pages` default is 5, at up to 100 results per page. To sweep more deeply, deliberately raise both `--limit` and `--ddb-max-pages`. Do not launch a 40,000-result sweep casually: at the default 1.25-second per-host delay it is a long-running corpus job. Prefer date-windowed batches, inspect result quality, and retain each batch as its own run. Search results are relevance-ranked; the tool does not relabel that order as chronology.

### ANNO newspaper and periodical search

ANNO exposes linked-data metadata and IIIF documentation, but the currently observed full-text search route is an undocumented backend of its AnnoSearch web application. It is disabled unless explicitly enabled:

```bash
python tools/fourth_dimension_history_harvester/harvest.py \
  --repo-root . --providers anno --query-group manual \
  --query '"vierte Dimension"' \
  --start-year 1870 --end-year 1945 \
  --allow-undocumented-anno-api --anno-medium all \
  --anno-snippets 5 --limit 100 --anno-max-pages 10 --apply
```

`--anno-medium` may be `all`, `newspaper`, or `periodical`. ANNO's own filter vocabulary uses `journal` for newspapers and `periodical` for periodicals; the adapter translates the operator-facing choices. The adapter checks the expected JSON response shape and fails loudly if the site begins returning its HTML application shell or otherwise changes its interface. It is a convenience route, not an institutional API guarantee.

### Other options

```bash
# Metadata search via the scholarly registries.
python tools/fourth_dimension_history_harvester/harvest.py \
  --repo-root . --providers crossref,openalex,ia --query-group people \
  --limit 50 --apply

# Optional, bounded OAI-PMH ListRecords search.
python tools/fourth_dimension_history_harvester/harvest.py \
  --repo-root . --providers oai --query-group manual \
  --query 'Zöllner' --oai-endpoint 'https://example.org/oai' \
  --oai-max-batches 5 --apply

# Download only sources carrying an explicit open-license/public-domain signal.
python tools/fourth_dimension_history_harvester/harvest.py \
  --repo-root . --query-group core --limit 10 --download --apply
```

Set `OPENALEX_MAILTO` to a contact address if you want to identify the polite-pool requester. DDB credentials are read from `DDB_API_KEY`. No credentials are written to run manifests.

## Output layout

```text
HISTORICAL/FOURTH_DIMENSION_HISTORY/
  README.md
  source_registry.json
  seed_file_register.json
  research_questions.md
  seed_inputs/
    ddb_vierte_dimension_results_2026-11-05.txt
  harvested/
    runs/<run_id>/records.jsonl
    runs/<run_id>/run.json
    objects/<first-two-sha-chars>/<sha256>.<extension>
```

Each run is isolated by a unique ID. Existing run artifacts are never replaced. Downloads are named by SHA-256; an existing object is verified before reuse. Run manifests record the repository commit and branch where available, query/provider scope, limits, and errors.

## Search policy and safety

- Dry-run is the default; `--apply` is required to write.
- The only write root is `HISTORICAL/FOURTH_DIMENSION_HISTORY/harvested/`.
- Original sources are never altered. No writes to `PRIOR_ART`, `PRIVATE_WORKSPACE`, quarantine, sandbox, source indexes, or existing historical source folders.
- Temporary files are isolated and finalized without clobbering an existing run artifact.
- Requests are sequential, default 1.25 seconds per host; transient failures receive bounded retries. Access denials are not bypassed.
- API result counts and page limits are explicit. A capped sweep is not described as exhaustive.
- PDF downloading is separately opt-in, size-bounded, and requires explicit open-license evidence. Paywalls and login walls are not bypassed.
- No global relevance score is applied. False positives and OCR errors remain inspectable.
- Near-duplicates are not automatically merged; `dedup_key` flags probable identity matches while preserving separate provenance records.

## Evidence discipline

A record may establish that a source was discovered at a location and what its metadata/snippet says. It does not establish that the source was read, that OCR is accurate, that the source is reliable, that a person held a specific belief, or that a career outcome was caused by stigma.

For career consequences, collect appointment/promotion records, university or academy minutes, correspondence, diaries, editorial decisions, obituaries, memoirs, and independent contemporary coverage. Keep explicit statements, documented events of unknown cause, temporal associations, and later interpretations separate. See `HISTORICAL/FOURTH_DIMENSION_HISTORY/research_questions.md`.

## Validation

Run the standard-library test suite and dry-run smoke test from the repository root:

```bash
python -m unittest discover -s tests -p 'test_fourth_dimension_history_harvester.py' -v
python tools/fourth_dimension_history_harvester/harvest.py \
  --repo-root . --providers '' --query-group core
```

The tests require no network. Live archive queries have not been run from the development environment; run a small `--limit 5` preview first on a machine with network access and a DDB API key.
