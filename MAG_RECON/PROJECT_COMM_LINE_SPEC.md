# Per-Project Comm Line — Sites / Editor / Reconstruction Loop

Status: seed spec; optional per project.

## Goal

Keep a live two-way communication line between reconstruction/editorial work and the chosen output surface (for example ChatGPT Sites) whenever that is useful for the project.

The communication line is itself one possible **best-guess output strategy**: rather than waiting for a final edition, allow the output surface to build from current reviewed state, leave implementation/editorial notes, and feed those notes back into reconstruction.

## Loop

`source/recon state -> editor review -> output-surface build -> site/output notes -> reconstruction/editor response -> updated source-linked build`

The output surface is not authoritative over the source. Its notes are design/editorial feedback that may reveal:
- missing metadata;
- awkward reconstruction structure;
- needed navigation relationships;
- unhelpful granularity;
- image/display needs;
- unclear status labels;
- reusable UI/data-contract opportunities.

## Per-project choice

Projects may choose one of these modes:
- `off` — no live output-surface communication;
- `notes-only` — output surface leaves notes, editor decides whether to act;
- `live-review` — notes are part of the normal editorial loop;
- `live-build` — reviewed source changes may flow directly into the output surface;
- `experimental` — output surface may try provisional views/versions for evaluation.

The reviewing LLM may change mode as the project matures.

## Best-guess output role

The output surface may be treated as a live **best-guess presentation layer**:
- current best reconstruction shown by default;
- alternate versions available where useful;
- provisional status visible;
- source/facsimile one gesture away;
- changes versioned rather than silently overwriting interpretation history.

## Notes channel

Site/output notes should be stored in a source-linked, project-local location and should distinguish:
- display/UI request;
- missing-data request;
- editorial question;
- reconstruction conflict;
- reusable capability suggestion;
- bug / parser mismatch;
- ready-to-promote pattern.

Each note should, where possible, include the affected entity/page/story/source and current reconstruction version.

## Routing site/output notes

The reviewing LLM decides whether each note becomes:
- local editorial change;
- local project config;
- `maybe-repurpose` module;
- `plug-in` capability;
- no action / rejected suggestion;
- unresolved question.

## Output contract

A per-project live build should expose enough metadata for the editor to understand what the site is displaying:
- entity id;
- version id;
- default/best-guess status;
- source locator;
- review state;
- last editorial update;
- output-surface notes pending/closed;
- available alternate views.

## FLC default

For FLC, use `live-review` immediately and allow `experimental` views for page/story presentation, column reconstruction, image placement, facsimile comparison and version switching.

If the Sites build proves stable and source-linked, individual reviewed items may graduate to `live-build` without waiting for the full corpus.
