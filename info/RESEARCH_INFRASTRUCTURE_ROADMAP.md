# SAT / H(s)H Research Infrastructure Roadmap

Status: active implementation plan

This document coordinates the repository work needed to make the SAT/H(s)H archive searchable, analyzable, citation-ready, and useful for theorybuilding without changing the evidentiary status of the underlying material.

## Governing rule

Raw sources are canonical. Indexes, extracted text, OCR, databases, scores, topic tags, timelines, and comparison matrices are **derived navigation or analysis artifacts**. They may be rebuilt, corrected, or discarded without altering source provenance.

All derived records should retain, where available:

- repository and source path;
- source content hash;
- source date / publication date separately from ingest date;
- extraction or ingest method;
- page, line, row, or message locator;
- confidence / review state;
- tool version;
- transformation notes.

Search or index silence is not evidence of absence.

## Repository roles

### `Satobloc/HsH`

Current theory-development and use-site repository. It should contain the cross-repository doorway, live provenance links, theorybuilding outputs, and point-of-use citation ledger.

### `Satobloc/SAT_THEORY_ARCHIVE_2023-25`

Historical/developmental provenance archive. Preserve chronology and source placement. Improve access through indexes, OCR/extraction, and cross-references rather than reorganizing historical sources.

### `Satobloc/HSH_RESOURCES`

External evidence and research-data hub. Literature, prior art, research updates, exposure data, extracted text, analytics machinery, and bibliographic infrastructure live here.

## Workstream A — complete archive accessibility

Goal: every file in all three repositories is both **locatable** and assigned an explicit accessibility state.

Existing pieces:

- HsH deterministic structural index (`tools/index_archive.py`).
- Historical archive findex / Nathan Dashboard archive index / derivation index.
- HSH_RESOURCES structural and human-readable source indexes.
- PDF extraction (`tools/extract_papers.py`).
- Image and scanned-PDF OCR (`tools/extract_image_text.py`).

Next pieces:

1. Build a repository-agnostic accessibility audit that classifies each file as native-readable, extracted, OCR-required, OCR-extracted, binary-needing-handler, or unsupported.
2. Run it against all three repositories and close every unexplained gap.
3. Generate a compact federated archive map in HsH pointing to each repository's authoritative indexes and derived text surfaces.
4. Add format-specific handlers only where the audits show real gaps; do not build parsers speculatively.

Completion condition: every repository file has a path in the structural inventory and a known retrieval route or an explicit unresolved/unsupported status.

## Workstream B — exposure analytics

Goal: turn `EXPOSURE_STATS` from a heterogeneous evidence pile into a queryable, source-traceable analytical dataset.

The directory currently mixes CSV exports, analytics PDFs, podcast data, GitHub statistics, arXiv-analysis outputs, transcripts, timeline material, and prior analytical concatenations. These should not be forced into one flat CSV.

Use a rebuildable SQLite database as the normalized analytical layer. SQLite keeps the system local, inspectable, portable, and usable with standard Python.

Core entities:

- `source_artifact` — immutable input file identity and provenance;
- `observation` — a measured value such as plays, listeners, completion, geography, repository traffic, etc.;
- `entity` — show, episode, repository, paper, account, country, demographic bin, or other measured object;
- `research_item` — paper/news/research object with publication chronology;
- `import_run` — exact ingest operation and tool version;
- `manual_annotation` — a human/LLM transcription or interpretation that cannot be recovered reliably by a deterministic parser.

The ingestion layer should have adapters by source family rather than one brittle mega-parser. CSV gets deterministic parsers. PDFs and screenshots first pass through text/OCR extraction; ambiguous tables may require a reviewed manual record. Manual entry is acceptable when it is explicit and retains a source locator.

Initial outputs should answer descriptive questions before causal ones: exposure over time, episode-level consumption, audience distribution, repository traffic, public-release chronology, and correlations among recorded metrics. Exposure data by itself does not establish influence.

## Workstream C — field-development timeline: arXiv + news + archived research

Goal: track how externally published structures and vocabulary develop over time and compare that chronology to the dated SAT/H(s)H record.

Do **not** replace the existing `tools/arxiv_sat_scanner.py`. Extend it into a suite:

1. discovery — arXiv API and later selected news/RSS/provider adapters;
2. normalization — DOI/arXiv/title identity, authors, categories, publication/update dates;
3. scoring — structural triage only, with controls retained separately;
4. deduplication — reconcile new discoveries with `LIVE_RESEARCH_UPDATES`, `OUTSIDE RESEARCH LIBRARY`, `PRIOR_ART`, and existing bibliography records;
5. persistence — store first-seen date separately from publication date;
6. review — promote selected candidates to full-text inspection;
7. timeline — generate neutral external-development chronology and SAT/H(s)H comparison views.

High scanner score means “inspect this,” not “supports SAT/H(s)H,” “copied SAT,” or “is equivalent to SAT.”

News requires a provider-neutral intake format because sources will be mixed. Save metadata and links first; preserve quoted text only within copyright limits. For durable analysis prefer papers, institutional releases, datasets, and primary sources over downstream news summaries where possible.

## Workstream D — PRIOR_ART and nLab / related-theory reconnaissance

Goal: identify which external frameworks contain genuinely comparable **compound structures**, and which merely share generic ingredients.

For nLab, begin with the maintained GitHub mirror `ncatlab/nlab-content` rather than scraping the live site page-by-page. The mirror provides machine-readable page files and repository history. Use `ncatlab/nlab-content-html` only when rendered structure is needed. Direct website retrieval remains a fallback for pages or metadata absent from the mirrors.

Build a concept/link graph from nLab pages, references, backlinks where recoverable, and revision history. Seed the reconnaissance broadly from SAT/H(s)H structural vocabulary, then expand through graph neighbors rather than searching only SAT's own terminology.

Comparison must separate at least these layers:

- vocabulary overlap;
- mathematical-object overlap;
- kinematic/geometric construction overlap;
- dynamical-law overlap;
- ontology or interpretation overlap;
- dependency / derivational-structure overlap;
- chronology.

Generic ingredients such as braid groups, holonomy, worldlines, topology, chirality, or emergent geometry are not by themselves substantive anticipation. The priority-relevant unit is a sufficiently specific compound and its dependency structure.

Outputs:

- theory/family candidate registry;
- component-to-framework matrix;
- dated evidence cards with exact quotations kept short and page/section links;
- “deep review required” queue;
- disposition such as antecedent, partial structural cousin, independent rediscovery candidate, later parallel, or insufficient similarity.

## Workstream E — H(s)H Toolkit digestion

Goal: make `H(s)H_Toolkit` usable as an active mathematical and conceptual toolbox rather than a directory of papers and lecture notes.

Organize the **derived index**, not necessarily the source folders, by function:

- differential / Lorentzian geometry;
- curves, framed curves, rods, elastica, worldlines/worldtubes;
- topology, knots, braids, anyons;
- category / representation / quantum-group machinery;
- gauge theory, holonomy, geometric phase;
- QFT and particle physics / QCD;
- spinors, Clifford/Dirac machinery;
- causal structure and signature change;
- dynamical systems, bifurcation, waves and defects;
- other supporting mathematics and physics.

For high-value sources, create bounded “toolkit cards” containing: standard definition/result; assumptions; useful equations/techniques; source and page anchors; potential H(s)H use; caveats; and whether the item is imported standard machinery or an H(s)H-specific construction.

The toolkit should feed theorybuilding by retrieval: “I need a formalism for X” should return relevant tools with exact sources, not just filenames.

## Workstream F — citation pipeline

Goal: citation follows identified claim/need rather than keyword matching.

Keep the existing bibliography and HsH citation ledger as the authoritative human-facing surfaces. Add automation around them, not instead of them.

Pipeline:

`claim / statement -> citation need -> candidate literature -> source inspection -> exact page/section anchor -> verified citation -> point-of-use placement`

Automatable stages:

- detect arXiv IDs, DOI, bibliographic metadata and duplicates;
- pull arXiv metadata and, where appropriate, source/PDF pages;
- search the extracted-paper corpus for candidate support;
- create candidate citation records and page anchors;
- route missing literature into research intake and bibliography coverage.

Human/LLM review remains required for the central question: **does this source actually support the sentence being cited?**

## Shared data contracts

Use durable source identities of the form:

`repo + path + content hash`

A convenient display URI may be generated, e.g. `repo://HSH_RESOURCES/PRIOR_ART/example.pdf`, but the hash prevents silent identity drift.

Distinguish these dates wherever relevant:

- source creation/publication date;
- source revision/update date;
- SAT/H(s)H archive date;
- first discovered / first seen by the scanner;
- ingest date;
- analysis date.

Never collapse them into one ambiguous `date` field.

## Recommended execution order

The workstreams depend on each other, so the order is:

**A. accessibility -> B. normalized analytics substrate -> C. field timeline -> D. prior-art/nLab comparison -> E. toolkit digestion -> F. citation closure**

They can overlap once A is stable. In particular, citation needs discovered during C–E should immediately enter the citation ledger even before full citation closure.

## Documentation rule

Every tool gets:

- a dry-run or read-only default where practical;
- explicit input and output paths;
- a machine-readable manifest;
- deterministic/rebuildable outputs where possible;
- a short human README or section here;
- tests for parsers that transform data;
- a statement of what the output **does not establish**.

This infrastructure is designed to make the archive more inspectable, not to automate conclusions about validity, novelty, influence, or priority.
