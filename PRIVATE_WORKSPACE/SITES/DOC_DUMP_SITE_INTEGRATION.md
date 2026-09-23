# Doc Dump → Sites Integration — Private Sites Note

Status: active side-channel note.

## Integration gap observed

The first FLC site build reached the source PDFs/page feed but behaved primarily as a PDF viewer. That is consistent with the existing public reconstruction feed: it was strong on page identity, previews and source mapping, but did not yet provide a sufficiently explicit **editorial website contract**.

The fix is now split into three layers:

1. `site-feed.json` — deterministic page/source records;
2. `editorial-overlay.json` — current editorial entities/contents/best-guess structure;
3. `site-bundle.json` — direct Sites build contract: routes, default experience, views, render-now instructions, fallback behavior.

A stable `latest.json` points Sites at the current bundle.

## Consumer rule

For a reconstructed document project, Sites should inspect the stable bundle entry point **before** falling back to PDFs or a page atlas.

When `site-bundle.json` exists and validates:

- use its `default_experience` as the primary presentation;
- build declared routes/entities;
- use PDF/facsimile as source view/fallback;
- preserve unresolved status rather than inventing missing mappings;
- leave feedback in the project comm line when the bundle lacks a needed field.

## FLC current branch

The FLC integration files are on the archive PR branch `codex/flc-reconstruction-feed` under `flc/_RECONSTRUCTION_V1/`.

Current entry point: `latest.json` -> `site-bundle.json`.

The next Sites try should therefore produce a magazine home + issue pages + known contents/bylines + reconstruction status + facsimile access, rather than three primary PDF viewers.

## Generalization

The durable design contract is in `HSH_RESOURCES/MAG_RECON/DOC_DUMP_TO_SITE_INTEGRATION.md`.

As other doc dumps arrive, the reconstruction/editor LLM should emit a site bundle appropriate to the inferred output purpose. Sites should not need to rediscover the source corpus's basic information architecture from raw files each time.
