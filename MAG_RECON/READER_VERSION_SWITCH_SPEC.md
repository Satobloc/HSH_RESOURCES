# Reader Version Switch — Best Guess + Reader Choice

Status: seed UI/editorial spec.

## Goal

For reconstructed documents, display the current editorial **best guess** by default while allowing the reader to switch among alternate source/reconstruction views at will.

This is especially useful when the editorial state is still evolving and the source admits more than one defensible presentation.

## Core rule

Default view:

`BEST GUESS`

But the reader can switch to any available version without losing place.

Possible versions:
- `Best guess` — current editor-selected reconstruction.
- `Facsimile` — original source page/image.
- `PDF order` — raw scan sequence.
- `Printed order` — reconstructed reader order.
- `OCR raw` — uncorrected machine text.
- `Reviewed text` — manually/LLM-reviewed transcription.
- `Alternate reconstruction A/B/...` — competing plausible orders/boundaries.
- `Layout reconstruction` — split columns / reordered regions / cleaned derived page.
- `Source + reconstruction` — side-by-side or overlay comparison.

Not every item needs every version.

## Editorial status display

Every switchable item should expose a compact status indicator, e.g.:
- `reviewed`
- `provisional`
- `alternate`
- `raw source`
- `OCR`
- `manual correction`
- `unresolved`

The purpose is transparency, not warning clutter.

## Switching behavior

The reader should preserve context when changing versions:
- same issue;
- same logical page/story position;
- same anchor if possible;
- same scroll vicinity where mapping exists.

If two versions do not map cleanly, show the nearest corresponding source locator and state that the mapping is approximate.

## Best-guess selection

The reviewing LLM/editor chooses the default best-guess version.

That choice should be stored separately from the underlying candidates so changing the default does not destroy earlier reconstructions.

Suggested record:

```json
{
  "entity_id": "...",
  "default_version": "recon-v3",
  "available_versions": ["facsimile", "raw-pdf-order", "recon-v2", "recon-v3"],
  "editorial_basis": "reviewed printed page numbers + contents + continuation cues",
  "status": "provisional"
}
```

## Live editorial update

This design works naturally with ChatGPT Sites live-update behavior.

As editorial work advances:
- new reconstruction versions can be added;
- the default best guess can move from v1 -> v2 -> v3;
- the old versions remain available for comparison;
- reviewed transcription can replace OCR as the default text layer;
- facsimile remains permanently accessible;
- alternate interpretations can stay visible rather than being deleted.

## Suggested page UI

Minimal control near the reader header:

`View: [ Best guess v3 ▾ ]`

Dropdown examples:
- Best guess v3 — provisional
- Facsimile
- Raw PDF order
- Printed-order reconstruction v2
- OCR raw
- Reviewed text
- Alternate ordering A

Optional secondary toggle:

`Compare with source`

which opens split or overlay mode.

## Why this matters for FLC

FLC has several situations where a single hard-published reconstruction would be premature:
- PDF/imposition order vs printed reading order;
- column splitting;
- story boundary reconstruction;
- layout/page-furniture interpretation;
- raw OCR vs reviewed text;
- future corrected readings.

A version-switching reader turns uncertainty into a useful feature instead of forcing the editor to wait for total certainty.

## Sites handoff requirement

When generating a ChatGPT Sites-ready packet, include:
- available versions;
- default best-guess version;
- status for each version;
- source/reconstruction mapping;
- editor note/basis if useful;
- update timestamp / source basis;
- whether comparison mode is supported.

## Reader principle

**Best guess should be easy; source and alternatives should be one gesture away.**

Do not make the reader choose among raw technical versions before reading, but do not hide the uncertainty or the source history either.
