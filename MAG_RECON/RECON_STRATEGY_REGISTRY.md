# Reconstruction Strategy Registry

Status: seed registry for auto-recon stumbling blocks and candidate solitons / solutions.

## Principle

When the initial auto-reconstruction layer encounters a stumbling block, do not jump directly to a large general model. First ask whether the obstacle has a stupidly simple deterministic fix, a known classical document-layout strategy, or a small page-wise algorithm that converts the hard problem into an easier one.

The registry should capture:
- obstacle;
- cheapest plausible strategy;
- stronger fallback strategy;
- whether it is job-specific / maybe-repurpose / plug-in;
- whether the strategy modifies source or produces a reversible derived artifact;
- validation / failure cues.

The source scan remains canonical. Split/cropped/deskewed/reordered PDFs are derived reconstruction aids.

## 1. Multi-column pages

### Stumbling block
OCR or reading order interleaves columns, pull quotes, sidebars or ads.

### Stupidly simple soliton
Detect the vertical whitespace gutter and split the rendered page at the gutter into left/right derived pages or regions. Then OCR/read each region independently.

Possible output:
`source page -> crop A -> crop B -> reading-order relation`

This can be emitted either as image crops or as a new derived PDF with one logical column per page.

### Slightly cleverer
Use a vertical projection profile of foreground pixels / connected components to find persistent low-density bands. Prefer the widest stable gutter near the middle, but allow asymmetric columns.

### Classical stronger strategies
- recursive X-Y cut / whitespace partitioning;
- connected-component clustering;
- OCR bounding-box clustering into columns;
- learned document-layout segmentation when classical geometry fails.

### Validation cues
- text lines should rarely cross the proposed split;
- OCR word order should improve after split;
- detected column widths should be plausible across neighboring pages;
- the strategy must not split a full-width title, illustration or pull quote without retaining the original page relation.

Routing: `plug-in` if implemented generically; FLC can be the first benchmark.

## 2. Booklet / imposed PDF order

### Stumbling block
PDF scan sequence is not reader sequence. Consecutive printed pages may be far apart in the PDF.

### Simple strategies
- detect printed page numbers and sort by them when confidence is high;
- use visible story-title running heads / margins as continuity cues;
- treat cover, contents, editorial and contributor pages as anchors;
- build an adjacency graph rather than assuming PDF-next-page.

### Cleverer strategy
Score candidate page-to-page continuations using several weak signals:
- printed page number progression;
- same story title / running header;
- sentence continuation / punctuation compatibility;
- matching margin furniture;
- typography / column structure;
- issue contents order;
- manual anchor pages.

Find the highest-consistency path through pages, but retain alternatives where scores are close.

Routing: `maybe-repurpose` initially; likely broadly reusable for scanned zines, pamphlets, signatures and booklets.

## 3. Page rotation / skew

### Stumbling block
OCR and layout detection fail because the scan is rotated or slightly crooked.

### Existing simple strategy
Use orientation detection and deskew before layout analysis. Keep corrected pages as derived outputs only.

Routing: `plug-in`; this is standard preprocessing.

## 4. Pull quotes / sidebars interrupting body text

### Stumbling block
Large decorative text is mistaken for the next body-text line.

### Simple strategy
Detect text blocks by size / bounding box / alignment and treat outlier-sized blocks as separate regions. Reconstruct body reading order without them, while preserving a relation such as `pull-quote-from page/story`.

### Stronger strategy
Compare OCR snippets against nearby body text; repeated or near-repeated text is likely a pull quote rather than new narrative content.

Routing: `maybe-repurpose` -> `plug-in` if robust.

## 5. Ads / page furniture / illustrations mixed with prose

### Stumbling block
A generic text extractor cannot tell publication frame from story content, and the distinction may itself be editorially meaningful.

### Simple strategy
Region segmentation first; semantic classification later. Preserve `unknown-region` rather than forcing a class.

### Cleverer strategy
Cluster recurring visual regions across issues. Repeated elements in similar positions are likely magazine furniture; one-off large image regions near story starts may be illustrations; repeated boxed designs may be ads. These remain candidates until reviewed.

Routing: region segmentation `plug-in`; semantic role classifier `maybe-repurpose`.

## 6. Full-width title over multi-column body

### Stumbling block
Naive gutter splitting cuts the title or misorders it.

### Simple strategy
Detect horizontal bands first. If the upper band spans most page width and contains sparse/large text, preserve it as a full-width title region, then column-split only the body below.

This suggests a page-wise hierarchical strategy:
`horizontal zoning -> local column detection -> reading-order graph`

Routing: `plug-in` candidate.

## 7. Mixed one-column / two-column / image pages

### Stumbling block
A single issue changes layout from page to page.

### Simple strategy
Do not infer one issue-wide column count. Detect layout per page and optionally smooth only with neighboring-page evidence.

Possible page states:
- one-column;
- two-column;
- three-or-more;
- full-page image;
- mixed / hierarchical;
- unresolved.

Routing: `plug-in`.

## 8. OCR-poor but visually obvious structure

### Stumbling block
Exact text recognition is weak, but title blocks, columns and image regions are visually clear.

### Strategy
Separate layout reconstruction from transcription. Use geometry first; OCR only where useful. A page can be structurally reconstructed while its text remains `manual-review-required`.

Routing: governing principle / `plug-in`.

## 9. Story boundary detection

### Stumbling block
Stories begin/end without reliable OCR headings or span imposed pages.

### Simple signals
- title/byline block;
- large whitespace break;
- illustration + title composition;
- running header change;
- page number / contents alignment;
- author-name change.

### Cleverer strategy
Use a weighted boundary score from independent signals. Avoid requiring any one cue to be present.

Routing: `maybe-repurpose`.

## 10. Create a derived reconstruction PDF

A useful pattern for many obstacles is to transform a difficult scan into a reversible editor-friendly derivative:

- split spreads into single logical pages;
- split columns into sequential logical pages;
- deskew / rotate;
- reorder imposed pages;
- crop large margins;
- optionally create region-only PDFs for OCR.

Every derived page should retain a mapping back to:
`source file + source PDF page + crop rectangle + transform + reconstruction order`.

Never replace the source scan.

## Strategy escalation rule

For each obstacle, try in this order where appropriate:

1. **geometry / metadata trick** — simplest deterministic operation;
2. **classical document-layout algorithm** — projection profiles, connected components, X-Y cut, whitespace analysis;
3. **OCR-box reasoning** — use word/line boxes as layout evidence;
4. **learned layout model** — only where simpler methods fail materially;
5. **reviewing LLM / human visual judgment** — resolve ambiguity and decide whether a new reusable module is warranted.

The purpose is not to avoid sophisticated methods. It is to avoid spending sophistication where one clean crop or page-wise rule solves the actual problem.

## FLC immediate experiment

The next useful FLC auto-recon experiment should test column strategy on a bounded set of pages:

1. choose obvious one-column, two-column, title-plus-columns, image-heavy and mixed pages;
2. detect candidate gutters from rendered-page geometry;
3. create reversible crop regions / split-PDF derivative;
4. compare OCR/read-order quality before vs after;
5. record failures by page type;
6. promote only the successful general part into the reusable pipeline.

The key question is not "can we detect columns?" but "does the detected layout lead to a materially better reconstruction strategy for the next editor?"
