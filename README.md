# HSH Resources

Private source repository for scientific papers, raw datasets, and their derived
navigation artifacts used during the H(s)H reconstruction.

This repository is evidence storage, not the public synthesis. A paper's presence
here does not endorse it, make it relevant, or establish an H(s)H claim. Public
synthesis statements belong in [`Satobloc/HsH`](https://github.com/Satobloc/HsH)
and should cite the exact resource record used.

## Repository layers

- `HAUL */` — uploaded source material; preserve files as received.
- `tools/` — deterministic extraction and indexing utilities.
- `indexes/` — generated structural catalogs and scan state.
- `derived/text/` — page-marked text extraction keyed by source content hash.
- `derived/manifests/` — extraction results, errors, and OCR-needed status.

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

## Automated extraction

The `Extract and index papers` workflow runs after PDF uploads and can also be
started manually from the repository's Actions tab. It installs the pinned tool
requirements, runs the tests, extracts only new or changed PDFs, refreshes the
structural index, and commits the derived text and extraction manifest back to
this private repository. Workflow-generated text is force-added intentionally;
it remains ignored during ordinary local work to prevent accidental bulk adds.

Manual runs accept a `max_files` batch size. `0` means all pending PDFs. Bounded
runs select pending files after excluding current manifest entries, so repeated
runs advance through the corpus.

## Evidence discipline

Keep these judgments separate:

1. the file is present;
2. text was extracted successfully;
3. bibliographic metadata was identified;
4. the source was read;
5. a result is relevant to an H(s)H dependency;
6. the result supports, conflicts with, or merely resembles a model construction.
