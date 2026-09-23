# Document Dump → Website Integration Contract

Status: active design contract for reconstruction-to-Sites handoff.

## Problem this solves

A document-reconstruction pipeline can successfully inventory PDFs, render pages, hash sources, and produce previews while still handing Sites something that behaves like **a PDF shelf** rather than a website.

The missing layer is a site-facing editorial bundle: a small, predictable object that tells a Sites worker not merely *where the documents are*, but **what the current best editorial presentation is, which entities exist, what can be rendered now, what remains unresolved, and how source/facsimile views map back to it**.

## Core pipeline

`doc dump -> recon/source feed -> editorial overlay -> site bundle -> Sites renderer -> feedback -> editorial/recon update`

The source/reconstruction feed and the editorial overlay remain distinct.

- **Recon/source feed**: deterministic facts and derived artifacts: files, pages, hashes, thumbnails, OCR, geometry, candidate structure.
- **Editorial overlay**: reviewed or provisional interpretive structure: titles, issue/story entities, order, display copy, route intent, best-guess defaults, warnings, purpose decisions.
- **Site bundle**: merged, compact, build-facing contract. It should be sufficient for Sites to construct a useful first website without rediscovering the archive from scratch.

## Standing consumer rule

When a valid site bundle exists, **do not make the PDF viewer the primary experience unless the bundle explicitly requests that**.

The PDF/facsimile viewer is a source view and fallback. The normal first render should use the bundle's editorial entities and route plan.

## Well-known files

A project may expose these files beneath its reconstruction/output root:

```text
site-feed.json            # deterministic/source-side recon feed
editorial-overlay.json    # LLM/human editorial state
site-bundle.json          # Sites-ready merged contract
site-feedback.md          # or project-specific private comm-line pointer
```

`site-bundle.json` is the default entry point for a Sites worker.

If the project supports live rebuilds, a lightweight `latest.json` may point to the current versioned bundle.

## Minimum `site-bundle.json` contract

The bundle should carry, at minimum:

```json
{
  "schema_version": 1,
  "project_id": "...",
  "bundle_status": "provisional|reviewed|mixed",
  "default_experience": "editorial",
  "source_feed": "relative/or/stable/path",
  "site": {
    "title": "...",
    "slug_hint": "...",
    "headline": "...",
    "dek": "..."
  },
  "routes": [],
  "entities": [],
  "views": [],
  "build_instructions": [],
  "feedback": {}
}
```

The exact schema may grow, but these concepts should remain recognizable.

## Site-ready entities

Sites should receive actual editorial objects, not only pages.

Common entity types:

- `collection`
- `issue`
- `piece`
- `contributor`
- `page`
- `image`
- `editorial-note`
- `timeline-entry`
- `source`

An entity can exist before all source spans are fully mapped. For example, a contents page may establish that a story exists even while its exact continuation pages remain unresolved.

Useful entity fields:

- stable id;
- type;
- display title;
- author/contributor where supported;
- parent/container;
- route intent;
- source mapping;
- review state;
- available views;
- display status;
- optional teaser/dek;
- unresolved fields.

## Route intent

The bundle should tell Sites what it can build *now*.

Examples:

```json
{
  "path": "/",
  "entity_id": "flc",
  "template": "collection-home",
  "readiness": "site-ready-provisional"
}
```

```json
{
  "path": "/issues/october-2002",
  "entity_id": "flc-issue-01",
  "template": "issue",
  "readiness": "site-ready-provisional"
}
```

A story whose page mapping is unresolved can still appear as a card/table-of-contents entry while its dedicated reading route remains `hold-for-editor`.

## Views

The bundle should expose the current best guess while retaining source alternatives.

Typical views:

- `editorial` / `best-guess`
- `facsimile`
- `raw-pdf-order`
- `printed-order-reconstruction`
- `layout-reconstruction`
- `ocr-raw`
- `reviewed-text`
- named alternate reconstructions

Each view should declare its status and source basis.

## Progressive enhancement

The website should become richer as editorial reconstruction advances **without requiring a redesign**.

A first bundle may support:

- collection landing page;
- issue cards;
- issue contents;
- facsimile/page atlas;
- reconstruction status.

Later overlays can add:

- exact story page spans;
- reviewed reading text;
- contributor pages;
- image galleries;
- alternate page orders;
- annotations;
- prompt/generated-image experiments;
- provenance/context pages.

The route/entity ids should remain stable where possible so Sites can update rather than rebuild conceptually from zero.

## Editorial copy

The bundle may include short site-ready copy where the reviewing LLM has enough evidence to write it responsibly.

Sites may rewrite for fit and presentation, but it should not need to invent the basic information architecture or re-derive the collection from PDFs.

Prefer:

`source evidence -> editorial summary -> website copy`

not:

`PDF filename -> generic viewer`

## Smart defaulting

The reviewing LLM should make a best guess about the most useful first website experience.

Examples:

- literary magazine -> collection home + issue shelf + contents + facsimile;
- research-paper dump -> browse/search + paper cards + abstracts/status + reader;
- notebook/archive dump -> timeline/topic clusters + source viewer;
- image-heavy ephemera -> gallery/atlas + metadata + source context.

These are defaults, not hard taxonomies.

## Build instructions

The bundle may contain explicit instructions such as:

- `Do not use PDF viewer as homepage when editorial entities are present.`
- `Render unresolved pieces in contents but do not fabricate story text.`
- `Keep facsimile one gesture away.`
- `Show provisional status compactly.`
- `Preserve stable source links.`
- `Do not surface auto-only OCR as quotation text.`

This allows project-specific editorial judgment to travel with the data.

## Feedback loop

Every bundle should provide a return path for Sites/editorial notes.

Useful feedback classes:

- missing field;
- awkward entity boundary;
- route/template mismatch;
- source mapping problem;
- desired image derivative;
- reconstruction ambiguity;
- reusable module suggestion;
- site-only display preference.

The reviewing LLM decides whether feedback is job-specific, maybe-reusable, or a general plug-in capability.

## Live update behavior

Where the site builder can re-read the source repository, the integration should prefer a stable bundle path and versioned content behind it.

Where live repository access is unavailable, Sites may bake the current bundle into the build, but should record the bundle/version/source it used so the next build can update cleanly.

## FLC benchmark

For FLC, a correct first integration should produce more than three PDF viewers even before complete story segmentation.

At minimum it should be able to render:

- a magazine home/collection page;
- three issue cards;
- issue dates/labels;
- each issue's known contents and bylines;
- reconstruction status;
- page atlas/facsimile access;
- best-guess/source view controls;
- disabled/provisional story routes where page spans remain unresolved.

If Sites receives this bundle and still only displays PDFs, that is a consumer/integration failure rather than an absence of editorial structure.
