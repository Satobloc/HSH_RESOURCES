# Magazine Reconstruction — Private Workspace

Status: active project workspace.

This is the private working home for magazine/document reconstruction material that should not yet sit in the durable/public-facing `MAG_RECON/` layer.

## Current intended uses

- Sites feedback / implementation notes;
- replies and editorial decisions arising from that feedback;
- experimental reader versions;
- alternate page/story reconstructions;
- prompt-harvest candidates before promotion;
- image-generation experiments and evaluation notes;
- reconstruction heuristics under test;
- one-off adapters / scripts;
- `maybe-repurpose` module candidates;
- unresolved ambiguity cards;
- editor scratch that helps the next LLM pick up the project quickly.

## Relationship to `MAG_RECON/`

`MAG_RECON/` contains the durable project specs, reviewed reconstruction outputs, reusable contracts, and explicit source-linked run artifacts.

`PRIVATE_WORKSPACE/MAG_RECON/` contains the editable working layer behind them.

Useful working loop:

`source -> auto probe -> private workspace -> reviewing LLM -> Sites/output experiment -> feedback -> private workspace -> promote reviewed result to MAG_RECON / tools / site packet`

## FLC

Use `FLC/` beneath this workspace for project-specific experimentation when needed. Durable run outputs already live under `MAG_RECON/FLC/`.

The private FLC layer may hold:
- Sites notes;
- page-order alternatives;
- column-split experiments;
- prompt candidates;
- visual-generation comparisons;
- temporary page maps;
- editorial scratch.

Do not move the canonical scans here merely to make the workspace self-contained; point back to the sources.

## Promotion test

Before moving a workspace artifact outward, ask:

1. Is the source/provenance mapping intact?
2. Is its status clear?
3. Is this now useful beyond the current editor's scratch context?
4. Does it belong in `MAG_RECON/`, `tools/`, Sites-ready output, a voice corpus, or another repo instead?

If not, leave it here.
