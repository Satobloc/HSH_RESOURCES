# flc text parse pass 004 — backend reconstruction note

Status: active experiment / Sites-facing backend work.

Public styling lock: *flc -- floating liars' club* — lowercase; italic Times/Times New Roman preferred.

## What failed in the previous dump

Two distinct failures were present and should not be conflated:

1. **Reading-order failure.** Whole-page OCR sometimes braided the left and right prose columns together, especially around illustrations and irregular blocks.
2. **Parser corruption.** The first coordinate-reflow implementation parsed Tesseract TSV with standard CSV quote semantics. An unmatched OCR double quote could cause the remainder of a TSV file to be consumed as one `text` field, which is why literal Tesseract metadata rows such as coordinates/confidences appeared inside story prose.

The second problem is not bad OCR; it is a deterministic parser bug.

## Current repair

The new pass is:

`source scan -> initial page/folio probe -> literal-TSV block discovery -> independent crop OCR -> conservative printed-page solver -> source-reviewed story ranges -> story feed -> Sites`

### Text reflow

`tools/reflow_flc_pages_v2.py`

- parses TSV by physical line and literal tabs, not CSV quoting;
- identifies dense text blocks geometrically;
- crops those regions from the page image;
- OCRs each crop independently;
- orders left-column blocks top-to-bottom, then right-column blocks top-to-bottom;
- keeps full-width/centre blocks as supplemental material rather than injecting them arbitrarily into prose;
- changes derived `clean_text` only.

### Printed-page solver

`tools/solve_flc_page_order.py`

Evidence priority:

1. source-reviewed manual page anchors;
2. compatible visible-margin folio OCR;
3. exact bracketed +/-1 sequences;
4. source-reviewed story ranges from the magazine contents;
5. exact singleton or local-run completion inside a story range.

It is allowed to clear a machine page-number assignment when a strong unique story identity makes that number impossible. Ambiguity remains unresolved instead of being filled heuristically.

### January source anchors currently encoded

The visually reviewed January mappings now include:

- A Buried Mystery: PDF 8->printed 4; 7->5; 6->6; 5->7.
- The Gilgamesh Golem: PDF 4->printed 8; 9->9; 14->10; 13->11; 12->12; 11->13; 10->14.

These anchors are source evidence and are kept distinct from solver deductions.

## QA added

`tools/audit_flc_story_feed.py` checks for:

- story pages outside reviewed story ranges;
- duplicate printed pages within a story;
- manual-anchor drift;
- leaked Tesseract TSV metadata / numeric parser garbage;
- impossible complete-status claims.

A focused folio candidate pass (`tools/refine_flc_folios.py`) has also been staged for the next iteration if page-number coverage remains sparse. It OCRs narrow page margins rather than asking whole-page OCR to notice small folios amid body text.

## Current run

The active build is GitHub Actions run 35908401055 in `Satobloc/SAT_THEORY_ARCHIVE_2023-25`.

Success criteria for this pass:

- no literal TSV coordinate/confidence rows in public story text;
- *A Buried Mystery* does not absorb *The Gilgamesh Golem* or *Strange Forms of the Surfacing Dead* pages;
- *The Gilgamesh Golem* is assembled in reviewed printed order 8 through 14;
- column prose is materially less braided;
- source/manual anchors survive automatic solving unchanged;
- missing/ambiguous pages remain explicitly missing rather than guessed.

Sites should continue consuming the stable `_SITE_FEED` story routes. Text quality can improve behind those ids without changing frontend routes.
