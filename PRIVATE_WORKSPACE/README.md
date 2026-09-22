# HSH_RESOURCES Private Workspace

Status: active discretionary workspace home.

This repository is private. This directory is the default **working home for provisional, editor-facing, experimental, cross-project, or not-yet-public material** when HSH_RESOURCES is the most natural host.

## Governing rule

Material here is **workspace state, not publication state**.

Nothing in `PRIVATE_WORKSPACE/` should be treated as ready for Sites, public documentation, canonical archive summaries, or external citation merely because it exists here. Promotion outward should be explicit.

## What belongs here

Good candidates include:

- editor scratch and working syntheses;
- Sites / output-surface feedback and reply notes;
- experimental reconstruction versions;
- provisional image-prompt harvests;
- source-linked prompt experiments and results notes;
- one-off or maybe-reusable helper modules under evaluation;
- review queues and ambiguity cards;
- temporary cross-archive maps;
- private editorial commentary that should not ride with a public-facing artifact;
- project-specific configuration not yet mature enough for the general tool layer.

## What does not belong here by default

- raw historical sources that already have a canonical archive location;
- reviewed outputs intended to be durable public/navigation surfaces;
- general reusable tools that have clearly graduated into the shared tooling layer;
- current H(s)H theory-development material that belongs more naturally in `Satobloc/HsH/INTERNAL` or another explicit HsH workspace;
- historical SAT source material that should remain in `SAT_THEORY_ARCHIVE_2023-25`.

## Discretionary repository routing

Use judgment rather than forcing every private workspace into this repository.

### Prefer `HSH_RESOURCES/PRIVATE_WORKSPACE`
When the work centers on:
- external resources;
- document reconstruction / digitization;
- archive analysis tooling;
- voice/style corpora;
- Sites-facing source preparation;
- image/prompt/editorial support;
- cross-project reusable infrastructure under evaluation.

### Prefer `HsH/INTERNAL` or HsH project workspace
When the work is tightly coupled to current theorybuilding, formalization, solver work, unpublished papers, or internal H(s)H decisions.

### Prefer a project-local private area elsewhere
When locality materially improves provenance or avoids creating a misleading cross-repo dependency.

### Avoid writing current workspace state into the historical SAT archive
unless the item is itself historical/provenance material or the archive explicitly calls for it.

## Suggested project shape

A project may create:

```text
PRIVATE_WORKSPACE/<PROJECT>/
  README.md
  NOTES/
  INBOX/
  EXPERIMENTS/
  SITE_FEEDBACK/
  PROMPT_HARVEST/
  MODULE_CANDIDATES/
  REVIEW_QUEUE/
```

Create only the subfolders actually needed; do not manufacture empty bureaucracy.

## Promotion routes

Workspace material may graduate to:

- project documentation;
- public/Sites-ready packets;
- canonical indexes/manifests;
- a reusable tool/module;
- reviewed voice corpus;
- provenance record;
- another repository better suited to the mature artifact.

When promoting, preserve source links and note what editorial/review step changed the status.

## Cross-project rule

Projects may point here without copying the workspace contents into their public-facing areas. A pointer means “working material may live here,” not “publish everything here.”
