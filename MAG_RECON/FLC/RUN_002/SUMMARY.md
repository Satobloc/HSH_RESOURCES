# FLC Run 002 — Full Geometric Auto-Recon

All 138 pages were processed. This run concentrates on the part that is fast, deterministic, and useful before OCR: page identity, source hashes, visual density, rough page role, and page-wise column/gutter guesses.

- **October 2002 — inaugural issue** (`flc1_lo.pdf`): 48 pages; 12 pages received a confident two-column gutter candidate.
- **November 2002** (`flc2_lo.pdf`): 41 pages; 5 pages received a confident two-column gutter candidate.
- **January 2003 — issue #3** (`flc3_lo.pdf`): 49 pages; 16 pages received a confident two-column gutter candidate.

## Immediate use

- Sites can build from issue identity, contents, facsimile/source links, and the version-switch reader contract immediately.
- Any page marked two-column is a candidate for a reversible derived split-column version, not an instruction to overwrite the page.
- The next reconstruction pass should target printed-page order / continuation anchors, then selective OCR/transcription where it changes editorial output.
- Two attempts to OCR the entire 138-page batch synchronously exceeded the execution window. That is itself a workflow result: OCR should be staged/incremental and content-hash cached rather than tied to one foreground run.

## QA finding from this pass

The first coarse `image-heavy/text-heavy/mixed` color-density heuristic was too sensitive to the tinted/aged scan background and overclassified pages as image-heavy. Do **not** route those coarse class labels to public output. Keep the geometry and gutter candidates; revise the visual classifier separately.

## Candidate two-column pages

- October PDF pages: 2, 6, 8, 12, 16, 22, 24, 38, 40, 41, 44, 47
- November PDF pages: 2, 3, 10, 24, 28
- January PDF pages: 10, 20, 21, 23, 24, 30, 31, 32, 34, 35, 36, 37, 38, 40, 42, 47

These are auto-only candidates for the next split-column experiment.

## Editorial state

Source scans remain canonical. Run 001's reviewed/manual orientation remains the stronger semantic layer; Run 002 adds a full-batch geometric layer and an immediate Sites packet.
