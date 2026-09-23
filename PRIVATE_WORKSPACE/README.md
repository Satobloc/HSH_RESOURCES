# HSH_RESOURCES Private LLM Workspaces

Status: active umbrella workspace home.

This repository is private. `PRIVATE_WORKSPACE/` is the umbrella home for **private LLM workspaces**: provisional, editor-facing, experimental, or not-yet-public working areas that should remain separate from their public/canonical project surfaces.

## Governing rule

Each private LLM workspace should normally live as a sibling beneath this directory:

```text
PRIVATE_WORKSPACE/
  SITES/
  MAG_RECON/
  <FUTURE_PRIVATE_LLM_WORKSPACE>/
```

Create a new sibling workspace when a distinct private LLM role/workstream needs its own durable working context. Do not turn this root into one giant shared scratchpad.

Material here is **workspace state, not publication state**. Presence here does not make anything public-ready, canonical, or approved.

## Current workspaces

### `SITES/`
Private Sites workshop only.

It is an adjunct to, **not a replacement for**, the main Sites workspace in the Glass Sausage Factory. Use it for private handoffs, source-sensitive notes, experiments, alternate implementations, private editorial questions, and feedback that should not live in the main Sites workspace yet.

### `MAG_RECON/`
Private LLM workspace for magazine/document reconstruction: experimental reconstructions, editor scratch, prompt/image work, ambiguity handling, module candidates, and source-linked notes behind the durable `MAG_RECON/` layer.

## Future private LLM workspaces

Other private LLM workspaces should be created here when appropriate, for example:

```text
PRIVATE_WORKSPACE/<WORKSPACE_NAME>/
  README.md
  INBOX/
  NOTES/
  EXPERIMENTS/
  REVIEW_QUEUE/
```

Only create the subfolders a workspace actually needs.

## What belongs here

Good candidates include:

- LLM-to-LLM handoff state;
- private editorial scratch and working syntheses;
- experimental versions / alternate reconstructions;
- source-sensitive notes that should not appear publicly yet;
- provisional image-prompt harvests and generation experiments;
- one-off or maybe-reusable helper modules under evaluation;
- review queues and ambiguity cards;
- temporary cross-archive maps;
- project/workspace configuration under active development.

## What does not belong here by default

- raw historical sources that already have a canonical archive location;
- reviewed outputs intended to be durable public/navigation surfaces;
- clearly graduated general-purpose tools;
- material whose natural private home is a more specific repo-local workspace;
- public/current Sites planning that belongs in the main Glass Sausage Factory Sites workspace.

## Promotion / routing

A private workspace artifact may later move or be promoted to:

- its project's durable documentation;
- a public/Sites-ready packet;
- a canonical index/manifest;
- a shared reusable tool/module;
- a reviewed corpus;
- another repository better suited to the mature artifact.

Preserve source links and review status when promoting.
