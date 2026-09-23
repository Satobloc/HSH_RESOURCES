# flc backend → frontend tunnel 003

Status: backend story-text path is now live on the public archive; frontend consumption is the next seam.

## Public backend entry point

`latest.json`

https://raw.githubusercontent.com/Satobloc/SAT_THEORY_ARCHIVE_2023-25/main/flc/_SITE_FEED/latest.json

The frontend should fetch this first with cache disabled / a cache-busting query, then follow its **absolute** `story_index_url` and per-story `text_url` values. Do not resolve feed-relative paths against the `chatgpt.site` origin.

## Current backend state

As of backend build `2026-09-23T12:19:11+00:00`:

- 22 known stories in the catalog;
- 7 stories currently have machine-derived text records;
- those 7 are the October 2002 inaugural issue;
- November 2002 and January 2003 still await their text-source pass;
- contents/index page 7 is now excluded from story-body matching because it names many stories;
- every text-ready story exposes an absolute `text_url`, stable route, source/facsimile route, text state, and reading-order basis.

Current public index:

https://raw.githubusercontent.com/Satobloc/SAT_THEORY_ARCHIVE_2023-25/main/flc/_SITE_FEED/story-index.json

Example story record:

https://raw.githubusercontent.com/Satobloc/SAT_THEORY_ARCHIVE_2023-25/main/flc/_SITE_FEED/stories/eye-of-the-angry-god.json

Important: the current text extraction is **provisional and potentially partial**. It finds pages where title/running-title evidence is visible. It is enough to prove the backend→story-reader tunnel and expose useful text, but it does not yet establish complete story membership or correct printed reading order.

## Frontend behavior requested

1. On page load, fetch backend `latest.json` fresh.
2. Fetch `latest.story_index_url`.
3. Merge backend story state into existing issue/contents cards by stable slug/id.
4. If `text_url` is non-null, make story title/byline clickable to `route`.
5. `/stories/:slug/` fetches that story's `text_url` and renders `display_text`.
6. Keep `facsimile_route` beside the text as the source view.
7. Display the text state compactly (`OCR text — provisional` or equivalent).
8. `/reconstruction-status/` should show:
   - whether live backend fetch succeeded;
   - `latest.built_utc`;
   - story count and text-ready count;
   - actual backend URL fetched;
   - whether the site is displaying live data or a packaged fallback.
9. If live backend fetch fails, preserve current packaged behavior but say so; do not silently look current.

## Reference consumer

A small framework-agnostic reference implementation is public here:

https://github.com/Satobloc/SAT_THEORY_ARCHIVE_2023-25/blob/main/flc/_SITE_FEED/frontend-consumer-reference.js

It implements `loadFlcBackend()`, `loadStory(slug)`, and `backendStatus()` against the absolute endpoints.

## Immediate smoke test

The first visible success criterion is deliberately small:

- October issue contents show seven active story links;
- clicking one opens a text-reader route instead of only the PDF viewer;
- source/facsimile remains available;
- reconstruction-status reports 22 stories / 7 machine-text stories and a non-null backend build time.

Once that works, improve story completeness/order and run the text-source pass for issues 02 and 03 without changing the frontend contract.
