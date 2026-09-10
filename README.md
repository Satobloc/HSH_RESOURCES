# HSH Resources
THE CONTENTS OF THIS REPO ARE STRICTLY FOR INFORMATION AND PRIOR ART CITATIONS AS NEEDED.
NOTHING IN THIS ARCHIVE BINDS SAT/H(S)H HUMAN OR LLM THEORISTS TO THEIR FINDINGS AND ACCURACY SHOULD NOT BE ASSUMED.

Private source repository for scientific papers, raw datasets, and their derived
navigation artifacts used during the H(s)H reconstruction.

This repository is evidence storage, not the public synthesis. A paper's presence
here does not endorse it, make it relevant, or establish an H(s)H claim. Public
synthesis statements belong in [`Satobloc/HsH`](https://github.com/Satobloc/HsH)
and should cite the exact resource record used.

## Theorybuilding boundary

SAT/H(s)H research and development is reconstructed from the project's own
Fundamental Intuitions and internal SAT → SAT-O → 4DHH → Blockwave/Satobloc →
H(s)H development. External literature is stored here for bibliographic credit,
standard mathematical/physical context, empirical evidence and constraints,
prior-art comparison, and explicitly provenance-labeled imports. Related outside
theories are not silently treated as the generative basis of H(s)H.

The source-side citation and handoff surface is:

- `indexes/HUMAN_BIBLIOGRAPHY.md`

The receiving point-of-use ledger in the public theory repository is:

- `Satobloc/HsH/ledgers/CITATION_LEDGER.md`

When a workflow, reviewer, or synthesis pass identifies an actual citation need,
record the same stable `CITE-YYYY-NNN` handoff ID on both sides with the exact
HSH_RESOURCES source path and exact HsH destination path/claim.

## Repository layers

- `HAUL */` and other source folders — uploaded source material; preserve files as received.
- `tools/` — deterministic extraction, indexing, and coverage utilities.
- `indexes/RESOURCE_INDEX.md` — generated structural catalog.
- `indexes/index-state.json` — machine-readable structural scan state.
- `indexes/HUMAN_BIBLIOGRAPHY.md` — human/LLM-reviewed bibliography and source-side citation handoffs.
- `indexes/BIBLIOGRAPHY_COVERAGE.md` — generated accounting of indexed PDF content not yet represented in the human bibliography.
- `derived/text/` — page-marked text extraction keyed by source-content SHA-256; not a source inventory.
- `derived/manifests/` — authoritative extraction mapping/results, errors, and OCR-needed status.
- `derived/README.md` — wayfinding for the derived layer and large-directory/truncation warning.

### Large derived-text directory warning

Do not use the GitHub web listing of `derived/text/` as a completeness check.
GitHub truncates large directory views at 1,000 entries. The extracted-text file
count also need not equal the source-PDF count because byte-identical source PDFs
share one content-addressed `<sha256>.txt` extraction while retaining separate
source-path records.

For complete extraction coverage, use `derived/manifests/extraction.jsonl` as the
authoritative `source_path → sha256 → text_path` mapping. The bibliography intake
workflow reads that manifest and the corresponding text files from a full checkout;
it does not depend on GitHub's truncated directory rendering. Extraction workflow
logs also report manifest records, unique text paths, actual derived-text files,
and any missing manifest targets.

Do not silently rename, deduplicate, repair, or replace source files. Duplicate
paths are recorded in the index and can remain as provenance evidence.

## Install tools

Python 3.10 or later is recommended. Text extraction prefers `pypdf`; if it is
unavailable, the extractor can use Poppler's `pdftotext` executable.

```bash
python -m pip install -r requirements-tools.txt
```

## Build the structural index

Preview first:

```bash
python tools/index_papers.py --root .
```

Write the generated index and state:

```bash
python tools/index_papers.py --root . --apply
```

## Extract PDF text

Extraction is dry-run by default. The following previews up to ten pending PDFs:

```bash
python tools/extract_papers.py --root . --max-files 10
```

To perform extraction:

```bash
python tools/extract_papers.py --root . --max-files 10 --apply
```

Each extracted page receives an explicit page marker. Empty or nearly empty
results are marked `needs_ocr`; OCR is not silently substituted because it has a
different error profile and should be separately auditable.

## Automated extraction and indexing

The `Extract and index papers` workflow runs after PDF uploads and can also be
started manually from the repository's Actions tab. It installs the pinned tool
requirements, runs the tests, extracts only new or changed PDFs, refreshes the
structural index, and commits the derived text and extraction manifest back to
this private repository. Workflow-generated text is force-added intentionally;
it remains ignored during ordinary local work to prevent accidental bulk adds.

Manual runs accept a `max_files` batch size. `0` means all pending PDFs. Bounded
runs select pending files after excluding current manifest entries, so repeated
runs advance through the corpus.

## Automated bibliography coverage

`Maintain bibliography coverage` runs whenever the structural state, human
bibliography, or coverage tool changes. It regenerates
`indexes/BIBLIOGRAPHY_COVERAGE.md` using `tools/update_bibliography_coverage.py`.

That generated report has a deliberately narrow job: it says which unique indexed
PDF content groups are or are not represented in the human bibliography. It treats
byte-identical copies as one backlog item. It does **not** infer relevance, reading
status, citation need, prior-art status, novelty, or theoretical authority.

This preserves a hard boundary between automatic coverage and human/LLM-reviewed
bibliographic judgment.

## Date conversation exports

The [conversation date utility](tools/date_conversation_exports.py) prefixes
ChatGPT exports with their first and last message dates in Eastern time. It is
dry-run by default, follows the active conversation branch, emits an audit
manifest, replaces its own prior prefix, and refuses filename collisions.

Display its options:

```bash
python tools/date_conversation_exports.py --help
```

Only use it on a deliberately added conversation-export directory. Do not run it
against paper, dataset, haul, extracted-text, or other evidence-source folders.

## Evidence discipline

Keep these judgments separate:

1. the file is present;
2. text was extracted successfully;
3. bibliographic metadata was identified;
4. the source was read;
5. a result is relevant to an H(s)H dependency;
6. an actual citation is needed at a specific HsH point of use;
7. the result supports, conflicts with, constrains, predates, or merely resembles a model construction.
