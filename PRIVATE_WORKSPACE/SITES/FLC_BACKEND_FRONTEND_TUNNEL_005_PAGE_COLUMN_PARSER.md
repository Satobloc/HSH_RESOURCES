# flc backend → frontend tunnel 005 — page/column parser

Status: active Sites handoff / geometry correction

## Publication lockup

Render as:

*flc -- floating liars' club*

Lowercase, italic, preferably Times / Times New Roman / serif fallback.

## Correct geometry

Direct image QA corrected the previous model.

Each source PDF image is ordinarily **one photographed printed magazine page**, not a two-page spread. Many prose pages contain two text columns. The source PDF page sequence is also not reliably the magazine's printed reading sequence.

A representative checked page is source PDF page 15 of the October issue: it is printed page `-19-`, with a left prose column, right prose column, and vertical outer-margin story/byline furniture. Source PDF page 17 is printed page `-17-`. Thus two independent problems have to be solved:

1. read columns in the correct within-page order;
2. reorder photographed pages by their printed page numbers before assembling a story.

## Active pipeline

`PDF image page -> Tesseract page-layout OCR -> column-aware body text -> separate outer-margin page-number detection -> conservative local page-number interpolation -> printed-page ordering -> source-reviewed contents-table story ranges -> provisional story text`

Parser:

`Satobloc/SAT_THEORY_ARCHIVE_2023-25/tools/parse_flc_pages.py`

Story-range assembler:

`Satobloc/SAT_THEORY_ARCHIVE_2023-25/tools/apply_flc_story_ranges.py`

Public feed builder:

`Satobloc/SAT_THEORY_ARCHIVE_2023-25/tools/build_flc_story_text_feed.py`

## Source-reviewed structural anchors

The printed contents pages now provide the story start pages rather than asking fuzzy OCR title matching to invent boundaries.

October 2002 starts: 4, 6, 12, 21, 24, 33, 39.

November 2002 starts: 4, 9, 13, 18, 25, 29, 35, 37.

January 2003 starts: 4, 8, 15, 22, 29, 36, 39.

Those values are encoded in `flc/_SITE_FEED/story_catalog.json` with `contents_page_review_state: source-reviewed`.

## Text completeness is explicit

A story record may report:
- `page-range-complete / text-unreviewed`
- `page-range-partial / text-unreviewed`
- `open-ended-range / text-unreviewed`
- `unresolved`

Unnumbered pages are not silently shoved into prose. They are exposed as unplaced candidates when their running-title OCR suggests a story association.

## Frontend behavior

Routes remain stable at `/stories/<slug>/`. The frontend does not need route churn as parser quality improves.

Prefer `text_source_kind: page-aware-column-ocr` over the legacy layout-text fallback. If `text_completeness` is partial, show a compact warning and keep the facsimile control visible.

`/reconstruction-status/` should expose live backend state plus counts of page-aware stories and complete recovered page ranges.

## Review boundary

The contents-table story starts are source-reviewed structural facts. Recovered printed page numbers, column reading order, paragraphing, and OCR wording are still machine-derived and provisional until checked against the facsimile.
