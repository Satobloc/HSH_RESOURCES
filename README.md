# HSH Resources

> **Human-facing catalog:** [`!_HSH_RESOURCES_INDEX.md`](!%5FHSH%5FRESOURCES%5FINDEX.md)

THE CONTENTS OF THIS REPO ARE STRICTLY FOR INFORMATION AND PRIOR ART CITATIONS AS NEEDED.
NOTHING IN THIS ARCHIVE BINDS SAT/H(S)H HUMAN OR LLM THEORISTS TO THEIR FINDINGS AND ACCURACY SHOULD NOT BE ASSUMED.

Private source repository for scientific papers, raw datasets, and their derived navigation artifacts used during the H(s)H reconstruction.

This repository is evidence storage, not the public synthesis. A paper's presence here does not endorse it, make it relevant, or establish an H(s)H claim. Public synthesis statements belong in [`Satobloc/HsH`](https://github.com/Satobloc/HsH) and should cite the exact resource record used.

## Start here

For people browsing the repository, use [`!_HSH_RESOURCES_INDEX.md`](!%5FHSH%5FRESOURCES%5FINDEX.md). It consolidates reviewed and provisional source records into one navigable catalog with title, author/metadata, identifier/date, source type, review/read status, exact repository path, and a concise description or identity note.

Supporting layers remain separate:

- `indexes/HUMAN_BIBLIOGRAPHY.md` — reviewed bibliography policy, PRIOR_ART notes, and citation handoffs.
- `indexes/bibliography_batches/` — bounded human/LLM-reviewed bibliography batches.
- `indexes/bibliography_provisional/` — bounded machine-generated identity/navigation batches for successfully extracted sources.
- `indexes/BIBLIOGRAPHY_COVERAGE.md` — machine coverage accounting.
- `indexes/BIBLIOGRAPHY_STRAGGLERS.md` — unresolved extraction/indexing exceptions.
- `indexes/RESOURCE_INDEX.md` and `indexes/index-state.json` — structural machine inventory.

## Theorybuilding boundary

SAT/H(s)H research and development is reconstructed from the project's own Fundamental Intuitions and internal SAT → SAT-O → 4DHH → Blockwave/Satobloc → H(s)H development. External literature is stored here for bibliographic credit, standard mathematical/physical context, empirical evidence and constraints, prior-art comparison, and explicitly provenance-labeled imports. Related outside theories are not silently treated as the generative basis of H(s)H.

The source-side citation and handoff surface is `indexes/HUMAN_BIBLIOGRAPHY.md`. The receiving point-of-use ledger in the public theory repository is `Satobloc/HsH/ledgers/CITATION_LEDGER.md`. When an actual citation need is identified, record the same stable `CITE-YYYY-NNN` handoff ID on both sides with the exact source and theory destination.

## Repository layers

- `HAUL */` and other source folders — uploaded source material; preserve files as received.
- `tools/` — deterministic extraction, indexing, bibliography, and coverage utilities.
- `indexes/RESOURCE_INDEX.md` — generated structural catalog.
- `indexes/index-state.json` — machine-readable structural scan state.
- `indexes/HUMAN_BIBLIOGRAPHY.md` — reviewed bibliography and source-side citation handoffs.
- `indexes/BIBLIOGRAPHY_COVERAGE.md` — generated reviewed/provisional/exclusion accounting.
- `derived/text/` — page-marked text extraction keyed by source-content SHA-256; not a source inventory.
- `derived/manifests/` — authoritative extraction mapping/results, errors, and OCR-needed status.
- `derived/README.md` — wayfinding for the derived layer and large-directory/truncation warning.

## Large derived-text directory warning

Do not use the GitHub web listing of `derived/text/` as a completeness check. GitHub truncates large directory views at 1,000 entries. The extracted-text count also need not equal the source-PDF count because byte-identical source PDFs share one content-addressed `<sha256>.txt` extraction while retaining separate source-path records.

For complete extraction coverage, use `derived/manifests/extraction.jsonl` as the authoritative `source_path → sha256 → text_path` mapping. The bibliography workflow reads that manifest and corresponding text files from a full checkout; it does not depend on GitHub's truncated directory rendering.

Do not silently rename, deduplicate, repair, or replace source files. Duplicate paths are recorded in the index and can remain as provenance evidence.

## Automated maintenance

The `Extract and index papers` workflow handles new or changed PDFs, extraction, and structural indexing. The `Maintain bibliography coverage` workflow builds provisional bibliography batches, coverage accounting, the human-review intake queue, straggler accounting, and the root human-readable source index.

The presentation layers never promote machine metadata to reviewed status and never infer H(s)H relevance, citation need, prior art, novelty, theoretical authority, or scientific validity.

## Evidence discipline

Keep these judgments separate:

1. the file is present;
2. text was extracted successfully;
3. bibliographic metadata was identified;
4. the source was read;
5. a result is relevant to an H(s)H dependency;
6. an actual citation is needed at a specific HsH point of use;
7. the result supports, conflicts with, constrains, predates, or merely resembles a model construction.
