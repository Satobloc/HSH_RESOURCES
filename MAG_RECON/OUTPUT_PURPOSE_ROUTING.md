# Output Purpose Routing — Open-Ended Document Reconstruction

Status: seed categories. These are editorial destinations, not fixed document types.

## Principle

A useful reconstruction pipeline should ask not only **what is this material?** but **what can this material usefully become next?**

The system may make smart, provisional guesses about likely output purposes from the sources, current editorial state, existing project surfaces, and the work already completed. The reviewing LLM has final editorial control and may add, remove, merge, split, or reprioritize destinations.

Purpose guesses should carry:
- purpose category;
- confidence;
- evidence / reason;
- source dependencies;
- readiness state;
- blockers;
- whether the output can update incrementally as editorial review progresses.

A source or derived object may serve multiple purposes simultaneously.

## Purpose 1 — Ready for ChatGPT Sites build / live update

This is the first explicit destination category.

The pipeline should recognize material that is ready, or nearly ready, to feed a ChatGPT Sites build and should prepare a **source-linked live editorial surface** rather than waiting for a final reconstructed edition.

Possible outputs include:
- issue landing pages;
- story / article pages;
- contributor pages;
- visual galleries;
- facsimile-page browsers;
- editorial / contents / contributor-material sections;
- provenance notes;
- reconstruction-status notes;
- related-context cards;
- searchable indexes;
- "latest reconstructed / reviewed" updates.

### Live-update behavior

As editorial review progresses, site-ready outputs may update incrementally from reviewed source records.

Examples:
- a provisional story boundary becomes reviewed and the site page updates;
- a corrected byline replaces an OCR guess;
- a reviewed illustration attribution appears without rebuilding unrelated pages;
- a new story-level transcript becomes available while the facsimile remains canonical;
- an editor adds context and the site gains a source-linked note;
- a weak reconstruction remains visibly tentative rather than being withheld or silently hardened into fact.

### Site-readiness states

Use states such as:
- `site-ready-reviewed`
- `site-ready-provisional`
- `site-useful-as-facsimile`
- `site-useful-with-warning`
- `not-site-ready`
- `hold-for-editor`

A provisional item may still be site-useful if its tentative status is explicit and its source can be inspected.

### Site handoff packet

Where useful, emit a compact site-build packet containing:
- stable item id;
- preferred display title;
- item type / page intent;
- source and exact locator;
- reviewed transcription / excerpt where available;
- facsimile or image relationship;
- contributor / role data and confidence;
- editorial summary or deck;
- tags / cross-links;
- reconstruction status;
- display warnings;
- suggested navigation parent / sibling relationships;
- last source/editorial update basis.

The reviewing LLM may write or reshape these packets directly for the site rather than preserving machine-generated prose.

## Purpose 2 — Editor workbench / next-pass handoff

Material whose immediate purpose is to help another LLM or human editor continue the reconstruction.

Typical outputs:
- editor-facing orientation;
- unresolved-question queue;
- page/story boundary map;
- ambiguity cards;
- targeted re-read list;
- proposed corrections with source locators.

## Purpose 3 — Canonical archive/navigation aid

Derived material whose value is durable retrieval rather than public presentation.

Typical outputs:
- source inventory;
- hashes;
- page manifests;
- OCR/transcription maps;
- exact locators;
- duplicate/version relationships;
- cross-archive indexes.

These remain subordinate to the original sources.

## Purpose 4 — Reconstructed reading edition

Material suitable for a clean reading path separated from, but linked back to, the facsimile.

Typical outputs:
- story-level reading copies;
- issue-level reading order;
- restored page sequence;
- reviewed headings/bylines;
- unobtrusive notes for unresolved text or structure.

Do not normalize away meaningful layout or artifact-fiction behavior when it carries part of the work.

## Purpose 5 — Research / provenance record

Material useful for documenting who made what, when, in what setting, and with what later recollections or external traces.

Typical outputs:
- provenance notes;
- contributor-role records;
- venue / reading / sales context;
- chronology candidates;
- external witness/source links;
- distinctions between source evidence, later recollection, and inference.

## Purpose 6 — Voice / style corpus

Material suitable for author-voice packets or stylistic study.

Typical outputs:
- exact source-linked excerpts;
- humor mechanism samples;
- narrative / explanatory / exploratory voice samples;
- context envelopes;
- edited-versus-spontaneous distinction;
- performance-dependence notes where known.

Do not infer authorship from style merely because a passage resembles a known voice.

## Purpose 7 — Visual / design corpus

Material useful for image, layout, typography, illustration, ad, cover, or recurring-design analysis.

Typical outputs:
- visual-page index;
- image crops linked to source pages;
- recurring motif/furniture clusters;
- layout-feature records;
- palette / density / region measurements;
- reviewed design-role notes.

## Purpose 8 — Public excerpt / showcase / teaser

Material that may support a compact public-facing sample without requiring the entire work to be reconstructed first.

Typical outputs:
- short excerpts;
- image + caption pairs;
- issue teasers;
- contributor spotlights;
- "from the archive" cards.

Copyright / authorship / permission state must remain explicit where relevant.

## Purpose 9 — Tooling / reusable capability input

A document problem that is itself useful as a test case for improving the reconstruction system.

Route discoveries through:
- `job-specific`;
- `maybe-repurpose`;
- `plug-in`.

The source corpus can therefore produce not only reconstructed content but improved general machinery.

## Purpose 10 — Hold / unresolved / do not publish yet

Some material should be deliberately routed away from publication or normalization when:
- authorship is unclear;
- OCR is too poor;
- chronology is misleadingly uncertain;
- privacy / permission status needs review;
- reconstruction alternatives materially change meaning;
- a likely correction has not been checked against the source.

A hold is a useful editorial output, not pipeline failure.

## Smart purpose guessing

The initial pass may nominate purposes using source-grounded cues.

Examples:
- clear title + byline + contiguous pages + readable text -> likely reading-edition and site-page candidate;
- visually strong cover / illustration with uncertain text -> likely facsimile/gallery/site visual candidate before transcription is ready;
- contributor bio page -> contributor-page / provenance candidate;
- repeated fake ad or page-furniture element -> visual/design corpus and possibly story-context/site annotation candidate;
- exact Nathan-authored passage -> possible voice-corpus candidate, subject to provenance check;
- unresolved page boundary -> editor-workbench purpose first, public purpose later.

Purpose inference should be liberal enough to surface opportunities but conservative about readiness.

## Editorial routing summary

At the end of a run, the reviewing LLM should be able to produce a compact table or narrative equivalent:

`object -> likely purpose(s) -> readiness -> confidence -> next action -> source`

The editor may then directly advance outputs. In particular, **ChatGPT Sites-ready work should be allowed to flow live from reviewed source records as editorial reconstruction progresses**, rather than waiting for the entire corpus to reach a fictional "finished" state.
