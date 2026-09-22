# FLC Run 001 — Editor-Facing Summary

Status: first whole-batch probe; provisional; reviewing LLM has full editorial control.

## What arrived

Three image-only PDF scans of *The Floating Liars' Club*:

- `flc1_lo.pdf` — 48 pages — manually identified as inaugural / October 2002.
- `flc2_lo.pdf` — 41 pages — manually identified as November 2002.
- `flc3_lo.pdf` — 49 pages — manually identified as January 2003 / issue #3.

Total: 138 pages.

All three PDFs contain zero native PDF text. At this stage the source of record is the page image itself. Any OCR should remain a derived search aid until checked against the scan.

## What it appears to contain

The three files are coherent magazine issues rather than independent story PDFs. Manual reading already establishes issue-level contents, stories by multiple contributors, editorials, contributor material, illustrations, ads/page furniture, pull quotes and cover/back-cover design.

The page object matters. A text-only extraction would lose meaningful structure because editorial framing, illustrations, advertisements, recurring magazine furniture and layout can carry narrative/comic or provenance value.

The current batch probe does **not** assume that PDF order is reader order. That matters: booklet/imposition behavior can separate consecutive printed pages in PDF sequence. The earlier *Gilgamesh Golem* misread is a concrete warning that source-page order must be reconstructed from printed page numbers, titles, continuation cues and visual layout before story-level reading copies are treated as stable.

## Automatic visual probe

A first deterministic pass measured foreground density, edge density, color fraction and contrast, then assigned rough page-attention classes.

- October / `flc1_lo`: 5 image-heavy, 2 sparse/title/frontmatter, 27 text-heavy, 14 mixed.
- November / `flc2_lo`: 6 image-heavy, 1 sparse/title/frontmatter, 17 text-heavy, 17 mixed.
- January / `flc3_lo`: 12 image-heavy, 2 sparse/title/frontmatter, 14 text-heavy, 21 mixed.

These labels are deliberately crude. Their value is triage: January immediately looks like the richest visual/layout review target, while October has the largest automatically identified text-heavy share.

## Strong signals

1. **Issue-level reconstruction is the right first unit.** Each scan contains publication-wide matter as well as stories.
2. **Page-image preservation is mandatory.** The source is not adequately represented by OCR alone.
3. **Printed-page / story-order mapping is the most important immediate manual task.** It unlocks reliable story reading, quotation, excerpting and site navigation.
4. **Visual analysis is worth integrating early.** Covers, title pages, illustrations, ads and recurring furniture are common enough to justify page-level image indexing.
5. **The three issues are already useful before full transcription.** Facsimile browsing, issue contents, contributor navigation and reviewed page/story maps can go live incrementally.

## Weak / ambiguous signals

- The current visual classifier cannot reliably distinguish illustration from ad, title page, decorative page furniture or photo-like scan artifact.
- Text-heavy versus mixed is only a review cue, not a semantic page role.
- No automatic story-boundary inference has yet been trusted.
- No style-based authorship inference should be attempted.
- The current run has not tried exhaustive OCR because direct visual review is more reliable for exact wording and the editorial bottleneck is presently structure/order, not search recall.

## Difficult or unusual material

The main difficulty is not simply low-quality OCR. It is that multiple information channels overlap on the same page: prose, image, pull quote, border text, title/byline, ads and magazine-level furniture. Some elements are part of the story experience; others belong to the publication frame; some may do both.

The second difficulty is imposed-page order. Any generic document pipeline that assumes `PDF page N -> reader page N` will produce plausible but false reconstructions.

## Suggested next review order

1. Recover printed-page numbering and reading sequence for all three issues.
2. Build a reviewed page ledger: issue -> PDF page -> printed page -> page role -> story/section -> continuation links.
3. Confirm contents-page story lists and bylines against the page ledger.
4. Mark illustration / ad / editorial / contributor-bio / cover regions at page level.
5. Only then generate clean story-level reading copies and exact voice excerpts.

## Reconstruction sketch

Working model:

`issue facsimile -> reviewed page map -> story/section entities -> contributor/role links -> visual/layout entities -> reading copies / voice samples / site pages`

The facsimile remains canonical at every stage.

## Purpose routing

### Ready / nearly ready for ChatGPT Sites

- **Issue landing pages:** `site-ready-provisional` now. Use cover, issue date, contents and facsimile navigation, with reconstruction-status banner.
- **Facsimile page browser:** `site-useful-as-facsimile` now.
- **Contributor index:** `site-ready-provisional` once the existing contents/byline list is entered into the reviewed ledger.
- **Visual gallery:** `site-ready-provisional`; begin with covers and manually confirmed illustrations.
- **Story pages:** `hold-for-editor` until story sequence is page-mapped, though selected fully reviewed stories can advance independently.
- **Latest reconstruction updates:** suitable immediately as a live editorial/status surface.

### Other destinations

- **Voice/style corpus:** high value; hold exact excerpt packets until page/order and wording are source-checked.
- **Visual/design corpus:** ready for deeper page-region indexing now.
- **Provenance record:** already useful; preserve production, reading, sales and later-revival context as separately sourced notes rather than embedding them as story metadata.
- **Reconstructed reading edition:** useful, but downstream of the printed-page ledger.

## Capability routing

### Job-specific

- FLC-specific contents/story title map.
- FLC-specific contributor-role corrections.
- Manual fixes for unusual printed-page order and story continuation.

### Maybe repurpose

- Printed-page-number candidate detector for imposed scans.
- Story-continuation detector using title/margin/layout cues.
- Ad-versus-illustration-versus-story-art region classifier.
- Page-furniture role classifier that allows one region to have both publication and narrative function.

### Plug in

- Deterministic page rendering + page hashes.
- Page-level source manifest with exact locators.
- Visual attention metrics for triage.
- Source-linked live-update packets for ChatGPT Sites.
- Review-state separation (`auto-only`, `manual-seen`, `manual-confirmed`, `manual-corrected`, `unresolved`).

## Do not conclude yet

Do not treat PDF order as reading order, OCR as authoritative text, visual similarity as identity, a repeated layout element as automatically non-narrative, or the current page-role guesses as reviewed facts.

The useful result of Run 001 is not a finished reconstruction. It is that the corpus has already exposed the correct next abstraction: **page-order and page-role reconstruction first; transcription, site presentation, voice harvesting and visual analysis can then advance independently but source-linked.**
