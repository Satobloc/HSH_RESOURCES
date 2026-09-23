# Tool notes — live

Initial finding: generic GitHub metadata/code search is not sufficient for HSH_RESOURCES archive coverage. Prefer repository tree traversal plus maintained human/derived indexes and native scripts.

Known useful HSH_RESOURCES surfaces:
- `indexes/HUMAN_BIBLIOGRAPHY.md`
- `indexes/human_source_index/`
- `derived/`
- `tools/`
- `.github/workflows/extract-papers.yml`
- `.github/workflows/arxiv-longitudinal-topic-atlas-pilot.yml`
- `.github/workflows/prepare-arxiv-blind-xray.yml`
- `.github/workflows/source-inventory.yml`
- `.github/workflows/cross-podcast-transcript-index.yml`

Known archive facts from current index pass:
- `PRIOR_ART`: 187 source records in two bounded catalog shards.
- `HISTORICAL`: large mixed text/PDF corpus; PDF-only bibliography materially undercounts it.

Next tool pass: discover and compare native search/index/digestion utilities in all three repos; locate Mersearch/Mercer_Searcher and SAT↔standard crosswalks; identify reusable full-text/extraction corpora before writing additional indexing code.
