# Derived extraction layer

This directory contains generated navigation/extraction artifacts, not source evidence.

## Authoritative inventory

Do **not** use the GitHub web listing of `derived/text/` as a completeness check. GitHub truncates large directory views at 1,000 entries. The extracted-text directory is also content-addressed, so its file count is not supposed to equal the number of source PDF paths.

Use these instead:

- `manifests/extraction.jsonl` — authoritative source-path → SHA-256 → extracted-text-path mapping, including extraction status, pages, metadata, OCR-needed state, and errors.
- `../indexes/BIBLIOGRAPHY_INTAKE.md` — generated human/LLM intake queue built from that manifest and the extracted text in a full repository checkout.
- `../indexes/RESOURCE_INDEX.md` / `../indexes/index-state.json` — structural inventory of source files; `derived/text/` is intentionally excluded from source-file counts.

## Why counts differ

`derived/text/<sha256>.txt` is keyed by the source PDF's SHA-256. Byte-identical PDF copies therefore share a single extracted-text file while retaining separate source-path records in the extraction manifest. This preserves provenance without duplicating derived text.

For audit purposes, distinguish at least:

1. source PDF paths;
2. source manifest records;
3. unique PDF contents / SHA-256 values;
4. unique extracted-text files;
5. extraction status (`extracted`, `needs_ocr`, `error`);
6. human bibliography coverage.

A truncated GitHub directory view is never evidence that an extracted record is absent.
