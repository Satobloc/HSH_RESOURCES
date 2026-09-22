# Floating Liars' Club Magazine Reconstruction

Status: seed project manual. Keep early passes small, reversible, and source-faithful.

## Purpose

Reconstruct the *Floating Liars' Club* magazines as complete literary/visual objects, not merely as OCR containers for story text.

The project should recover, where possible:

- complete issue/page sequence;
- story boundaries, titles, bylines, illustrations, pull quotes, ads, editorial matter, contributor bios, covers and back covers;
- layout relationships among those elements;
- authorship / design / illustration provenance;
- live-reading and sales context when independently recoverable;
- clean story-level reading copies without losing the original facsimile context;
- Nathan voice samples and other author-specific samples with precise source locators;
- visual/layout patterns that can be indexed and compared across issues.

The raw scan remains the source of record. OCR, page labels, story segmentation, image crops, inferred boundaries, tags, transcriptions and reconstructions are derived aids.

## Project principle: manual recon steers auto recon

Do not build automation first and then force the magazines into whatever the tool happens to recognize.

Manual reading establishes the ontology of the magazine: what counts as a story page, continuation page, illustration, fake ad, editorial note, pull quote, contributor bio, design furniture, etc. Automation should then help find, cluster, measure, and cross-link those things at scale.

Likewise, auto recon should generate useful surprises and review queues for manual inspection. The loop is:

`manual read -> define useful distinctions -> automate bounded detection -> inspect misses/false positives -> refine distinctions -> rebuild derived index`

## Two reconstruction tracks

### A. Manual reconstruction

For each issue, preserve a reviewed page ledger with at least:

- issue and PDF-page number;
- printed page number where visible;
- page role(s);
- story / section title if applicable;
- author / illustrator / designer where actually supported;
- continuation-from / continuation-to links;
- notable layout features;
- notable image/art content;
- exact text corrections where OCR is unreliable;
- confidence / unresolved notes.

Manual review has authority over interpretive labels such as story boundaries, joke function, artifact-fiction status, or whether a page element belongs to the story versus the magazine frame.

### B. Automatic reconstruction

Automation should initially concentrate on high-confidence, reversible outputs:

1. source inventory and hashes;
2. page rendering and page-image identity;
3. OCR with page boundaries retained;
4. title/byline/date/page-number candidate extraction;
5. repeated-header/footer and recurring-layout detection;
6. image-region / text-region segmentation;
7. perceptual similarity / duplicate or reused-art detection;
8. simple visual descriptors such as dominant palette, text density, whitespace, image coverage and orientation;
9. story-boundary candidates based on title/byline/layout/OCR cues;
10. cross-archive retrieval for names, titles, venues, dates, issue references and later recollections.

Anything interpretive should be emitted as a candidate with confidence and evidence, not silently promoted to reviewed fact.

## Reuse existing archive machinery

Do not create a separate search/index philosophy for the magazine project if an existing pattern already works.

Useful existing machinery includes:

- `HsH/tools/index_archive.py` — deterministic structural inventory and duplicate detection;
- `HsH/tools/search_archive_content.py` / Mercer_Searcher — read-only multi-format Boolean / NEAR retrieval with locators and source hashes;
- `HsH/tools/build_mersearch_index.py` — incremental content-hash-based SQLite/FTS indexing;
- `HSH_RESOURCES/tools/extract_image_text.py` — content-addressed OCR for images and image-only PDFs with a separate manifest;
- `HSH_RESOURCES/tools/build_human_readable_index.py` — pattern for generated human navigation;
- `HSH_RESOURCES/tools/build_cross_repo_podcast_guide.py` — pattern for a federated cross-repository guide;
- `HSH_RESOURCES/tools/build_analytics_store.py` — pattern for a derived SQLite layer that preserves source-artifact identity and records unsupported/ambiguous inputs rather than guessing.

The project should use those contracts where sensible rather than copying code blindly.

## Three-archive search surface

Magazine reconstruction may query all three project repositories for contextual traces:

- `Satobloc/HsH`
- `Satobloc/SAT_THEORY_ARCHIVE_2023-25`
- `Satobloc/HSH_RESOURCES`

Search targets include exact story titles, `Floating Liars`, `Victorian's Midnight Cafe`, Larry's, contributor names, issue dates, quotations, uploaded scans, later recollections, and prior voice-analysis notes.

Cross-archive hits are context/provenance candidates. They do not override the magazines themselves.

## First manual goals

Start with the three currently read issues and build only enough reviewed structure to support later automation:

1. issue-level identity;
2. ordered page ledger;
3. story / editorial / ad / art / bio boundaries;
4. contributor-role notes;
5. Nathan-authored pages and layout-created elements;
6. unresolved page-order / attribution questions.

Do not over-transcribe yet. A good page map is more valuable at this stage than a giant noisy OCR dump.

## First automatic goals

The first auto pass should answer descriptive questions only:

- What pages exist?
- Which pages are mostly text, mostly image, or mixed?
- Which visual elements recur?
- Which OCR terms strongly indicate title/byline/section transitions?
- Which pages are likely continuations of the same item?
- Where does OCR confidence look poor enough to require manual reading?
- Which names/titles from the magazines appear elsewhere in the three archives?

## Non-goals for the seed phase

Do not yet attempt to:

- infer literary quality;
- automatically identify humor or voice;
- decide authorship from style;
- reconstruct missing wording by language-model completion;
- replace page facsimiles with normalized text;
- treat OCR as authoritative quotation text;
- rewrite the historical magazine into a modernized edition.

## Provenance contract

Every derived record should retain when available:

- source repository / attachment identity;
- exact source path or file identity;
- source content hash;
- issue;
- PDF page and printed-page locator;
- extraction / detection method;
- tool / rule version;
- confidence and review state;
- manual correction / annotation history.

Use `unknown` or `unresolved` rather than filling gaps by inference.
