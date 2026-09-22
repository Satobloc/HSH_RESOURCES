# Magazine Auto-Reconstruction — Seed Spec

Status: design note only. No large implementation pass yet.

## Aim

Build a magazine-specific derived pipeline that makes the scans easier to navigate, inspect, compare and reconstruct while preserving the scan as canonical evidence.

The pipeline should be conservative: emit measurements and candidates; leave interpretive decisions to review.

## Proposed derived surfaces

### 1. `issue_manifest.jsonl`
One record per issue:
- issue id / date;
- source file identity and hash;
- page count;
- scan dimensions / orientation summary;
- extraction states;
- reviewed/unreviewed page-ledger status.

### 2. `page_manifest.jsonl`
One record per page:
- issue id;
- PDF page index;
- printed page candidate;
- rendered-page hash;
- OCR text path;
- text/image coverage estimates;
- visual feature summary;
- repeated-element matches;
- title/byline/page-role candidates;
- manual review state;
- exact source locator.

### 3. `regions.jsonl`
Optional later layer for detected page regions:
- bounding box;
- region class candidate (`body-text`, `title`, `byline`, `pull-quote`, `illustration`, `ad`, `page-number`, `unknown`);
- OCR snippet where applicable;
- confidence;
- manual override.

### 4. `cross_archive_hits.jsonl`
Federated contextual retrieval results from the three repositories, retaining:
- query;
- repository/path;
- source hash where available;
- locator;
- excerpt;
- linked magazine entity candidate (`issue`, `story`, `person`, `venue`, `date`, etc.);
- review state.

## Reused machinery / contracts

### Structural identity
Borrow the deterministic source inventory / duplicate discipline from `HsH/tools/index_archive.py`.

### Text retrieval
Use the record/locator philosophy of Mercer_Searcher (`HsH/tools/search_archive_content.py`). For magazine pages, add page-level records rather than trying to force page layout into conversation-message semantics.

### Incremental rebuild
Borrow the Mersearch generation pattern:
- content hashes decide reuse;
- unchanged source pages are not reparsed unnecessarily;
- generated state is rebuildable;
- publication of an index generation is atomic where practical.

### OCR
Reuse `HSH_RESOURCES/tools/extract_image_text.py` behavior and manifest discipline. For magazine work, OCR should remain explicitly distinguishable from reviewed transcription.

### Derived analytical store
If/when the page manifest becomes unwieldy, use SQLite as a query layer, following `build_analytics_store.py`: source artifacts remain canonical; database rows point back to exact source identity and locators.

## Magazine-specific adapters to add gradually

Do not begin with a monolithic vision model. Add small adapters whose failure modes are inspectable.

### Adapter A — page renderer
Rasterize each PDF page at a stable DPI and retain deterministic page-image hashes.

### Adapter B — OCR bridge
Run existing OCR machinery per page and expose text with preserved page identity.

### Adapter C — basic visual metrics
Compute simple reproducible page features:
- dimensions / aspect ratio;
- grayscale and color summary;
- foreground/text-like density;
- large connected image-region share;
- whitespace share;
- edge density;
- rough column count candidates.

These are descriptors, not aesthetic judgments.

### Adapter D — repeated furniture detector
Use exact/perceptual hashes and image-region similarity to surface repeated:
- masthead pieces;
- page furniture;
- recurring ads;
- decorative elements;
- reused illustrations / motifs.

### Adapter E — transition-cue detector
Use OCR + layout cues to nominate likely beginnings/endings:
- large title text;
- `by` / author-name patterns;
- strong whitespace or illustration/title compositions;
- recurring margin story-title behavior;
- contributor / contents / editorial markers.

Output candidates only.

### Adapter F — cross-archive context search
Generate bounded searches across HsH, SAT archive and HSH_RESOURCES for:
- exact story titles;
- issue dates;
- contributor names;
- `Floating Liars` variants;
- Victorian's / Larry's;
- phrases selected during manual review.

Prefer exact phrase and NEAR searches before broad semantic guessing.

## Manual steering file

The auto pipeline should consume a small reviewed configuration rather than bury project knowledge in source code. Proposed later file: `MAG_RECON/project_rules.yaml`.

Likely contents:
- known issue ids/dates;
- known contributor names and spelling variants;
- known story titles;
- page-role vocabulary;
- known recurring design elements;
- explicit corrections / exclusions;
- terms worth federated archive search;
- current manual priorities.

This file should express project knowledge, not model-generated conclusions.

## Review states

Use a small explicit vocabulary:
- `auto-only`
- `manual-seen`
- `manual-confirmed`
- `manual-corrected`
- `unresolved`

Keep confidence separate from review state. A high-confidence automatic classification is still `auto-only` until reviewed.

## First implementation bite

Do only these pieces first:

1. issue + page manifest skeleton;
2. deterministic page rasterization/hashing;
3. hook existing OCR output to page records;
4. basic text/image/whitespace metrics;
5. produce a compact human-readable page table for one issue.

Then compare the automatic page table to the manual reading already done. The mismatches should determine the next adapter.

## Success criterion for phase 1

A reviewer should be able to open one generated page table and quickly answer:

- what each page probably contains;
- where the likely story boundaries are;
- which pages need visual/manual attention;
- where OCR is weak;
- what repeats visually;
- how to jump back to the exact source page.

If the first implementation does not make manual review faster, it is not yet useful enough to expand.
