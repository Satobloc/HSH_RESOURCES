# flc — backend → Sites refresh probe 001

Status: pushed; awaiting visible consumer response.

## Branding correction

Public styling is:

- `flc`
- `floating liars’ club`

Do not title-case the publication name in ordinary site chrome unless reproducing a source artifact that does so.

## Probe

Backend branch: `Satobloc/SAT_THEORY_ARCHIVE_2023-25`, `codex/flc-reconstruction-feed`.

Requested revision: `2026-09-23.1`.

Updated:
- `editorial-overlay.json`
- `site-bundle.json`
- `latest.json`
- added `site-refresh.json`

The bundle/refresh nonce explicitly requests an editorial-first rebuild rather than the existing primary PDF-viewer experience.

## Expected visible smoke test

A successful seamless update should make at least one of these visible without Nathan manually rebuilding the site:

1. site branding changes to `flc` / `floating liars’ club`;
2. collection-home presentation appears;
3. issue cards + known contents/bylines appear;
4. PDF/facsimile becomes a secondary/source view rather than the primary page.

## Diagnostic interpretation

If a reload still shows the old PDF-viewer-first experience, the backend half of the tunnel is working but the current published Sites consumer is not watching/reconciling `latest.json` / `site-bundle.json`. One consumer-side rebuild/watcher hookup is then required. After that hookup, later backend bundle/nonce changes should be able to drive live revisions without another conceptual rebuild.

Do not treat failure of this first probe as a reconstruction-data failure: the editorial bundle exists and is source-linked; the test is specifically whether the published Sites runtime consumes backend revision signals automatically.
