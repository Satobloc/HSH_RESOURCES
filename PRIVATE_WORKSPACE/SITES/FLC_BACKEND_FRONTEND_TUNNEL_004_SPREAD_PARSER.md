# flc backend → frontend tunnel 004 — spread-aware text

Status: active parser upgrade / Sites handoff

## Publication lockup

Render the publication lockup as:

*flc -- floating liars' club*

Rules:
- lowercase;
- italic;
- preferably Times / Times New Roman / serif fallback;
- do not title-case or all-cap the lockup unless reproducing source typography.

## Parsing correction

The surviving FLC PDFs are photographed/scanned **open spreads**. One physical PDF page therefore contains two logical printed pages.

Whole-spread OCR is the wrong primitive for readable story text: it can merge/interleave the left and right printed pages before story association even begins.

The new parser at:

`Satobloc/SAT_THEORY_ARCHIVE_2023-25/tools/parse_flc_spreads.py`

changes the order of operations:

`physical spread -> Tesseract TSV geometry -> left/right logical pages -> printed-page number detection/inference -> printed-page ordering -> title-anchor story spans -> provisional story text`

This is the first parser layer that directly attacks the observed failure mode rather than trying to clean up an already-interleaved text dump.

## Derived outputs

Per issue, the parser writes under:

`flc/_PARSED_TEXT/<issue-stem>/`

including:
- `manifest.json`
- `logical-pages.jsonl`
- `logical_pages/*.txt`
- `story-anchors.json`
- `story-text-index.json`
- `stories/<slug>.json`
- `stories/<slug>.txt`
- `spread-diagnostics.json`
- `PARSE_REPORT.md`

These are derived/rebuildable surfaces. The source scan remains authoritative.

## Feed preference

`tools/build_flc_story_text_feed.py` now prefers spread-aware parsed story text when available and falls back to the older whole-spread OCR only when necessary.

Frontend-visible `text_source_kind` distinguishes:
- `spread-aware-logical-page-ocr`
- `legacy-whole-spread-ocr`

Sites should prefer the former and can expose the distinction on reconstruction-status without making the public reading interface noisy.

## Frontend contract remains stable

Story routes remain:

`/stories/<slug>/`

A text-ready story still exposes `text_url`, `facsimile_route`, `reading_order_basis`, and `display_text`. The backend can therefore improve text quality and page ordering without requiring route churn in the website.

## Review boundary

The spread parser improves structure, not authority. Automatic page numbers, inferred facing-page numbers, story anchors, paragraph reflow, and OCR wording remain provisional until checked against the facsimile.

The most useful next QA comparison is:

1. pick a story whose source spread is known visually;
2. compare old whole-spread `display_text` with new spread-aware `display_text`;
3. inspect logical page order;
4. record systematic OCR/reflow errors;
5. turn only recurring fixes into parser rules.
