# Image Prompt Harvest — Source Chunks + Editor-Optimized Prompts

Status: seed spec for an optional image-generation support layer.

## Goal

Automatically surface source passages that may be useful as image-generation prompt material, preserving both:

1. the **source chunk as-is**; and
2. an **LLM-editor-optimized prompt draft** that preserves the source's concrete content while making the visual instruction more usable.

The layer should also give the reviewing LLM a smart recommendation about whether it should actually try generating one or two images now, or refrain.

This is an editorial aid, not an instruction to generate images automatically.

## Why keep both raw and optimized forms

The raw chunk preserves provenance, language, accidental specificity, tone and details that an optimized prompt may otherwise flatten.

The optimized form can:
- make subject/action/environment explicit;
- separate visual facts from narrative exposition;
- resolve pronouns only where the source supports it;
- make composition / framing suggestions;
- identify required text or signage carefully;
- note uncertainty rather than inventing missing detail;
- preserve unusual material/design cues;
- avoid importing a style or aesthetic not grounded in the source unless explicitly labeled as an editorial suggestion.

## Candidate record

Each harvested candidate should retain fields like:

```json
{
  "candidate_id": "...",
  "source_id": "...",
  "source_locator": "...",
  "raw_chunk": "...",
  "why_visual": ["strong scene", "distinct object", "layout idea"],
  "editor_prompt": "...",
  "prompt_status": "draft",
  "try_recommendation": "yes-one|yes-two|maybe|no",
  "recommendation_reason": "...",
  "risks_or_missing_details": ["..."],
  "likely_output_use": ["site-illustration", "reconstruction-test"]
}
```

## Candidate discovery

Do not harvest every descriptive sentence. Prefer chunks with one or more of:
- unusually concrete visual scene;
- distinctive object/creature/place/costume/architecture;
- strong spatial relation;
- explicit visual joke;
- image-like narrative beat;
- historical illustration opportunity;
- cover / poster / fake-ad potential;
- visually recoverable layout instruction;
- comparison value for reconstructing damaged/missing visual material;
- high-value site or editorial orientation use.

Candidate detection may use textual cues, page layout, existing illustrations, editor tags, and reviewing-LLM judgment.

## Source chunk selection

The as-is chunk should be:
- source-faithful;
- bounded enough to understand the visual idea;
- long enough to retain decisive details;
- linked to exact source location;
- kept separate from editorial additions.

Do not silently 'clean up' the raw source field.

## LLM-editor-optimized form

The editor may transform the raw chunk into a prompt that is easier for an image model to act on, while preserving evidentiary boundaries.

Useful transformations:
- gather visual details scattered across adjacent sentences;
- remove exposition that does not affect the image;
- make the central subject and setting explicit;
- state visible relationships / scale / posture / orientation;
- convert vague narrative sequence into one chosen visual moment;
- note which details are mandatory versus optional;
- specify whether the target is reconstruction, illustration, cover concept, site graphic, diagram-like artifact, etc.;
- add alternative prompt variants when two compositions are genuinely plausible.

If the source leaves a detail unspecified, the optimized prompt should either leave it open or label an editorial choice explicitly.

## Smart 'should we try this?' recommendation

The layer should advise the reviewing LLM whether generating one or two exploratory images is likely to be editorially useful.

### `yes-one`
Try one image when:
- the source is visually clear;
- the result could immediately improve orientation, reconstruction, or a site page;
- the prompt has one dominant interpretation;
- little is learned from multiple variants.

### `yes-two`
Try two variants when:
- there are two materially different plausible compositions;
- style/composition choice is itself the question;
- comparison would help the editor decide whether image generation is useful;
- the cost of a second attempt is low relative to likely information gained.

### `maybe`
Useful candidate, but hold when:
- key details are unresolved;
- source attribution / permission / role is uncertain;
- the image would mainly be decorative and other reconstruction tasks are more valuable;
- a related original illustration should be inspected first.

### `no`
Do not try now when:
- the prompt would require inventing too much;
- an original image already exists and is the right artifact;
- visual generation risks misleading readers into treating a speculative image as reconstruction;
- the passage is better represented by facsimile/text;
- the image adds little editorial information.

## Recommendation factors

The reviewing LLM should weigh:
- visual specificity;
- source confidence;
- reconstruction value;
- site/public value;
- whether an original visual artifact exists;
- ambiguity;
- risk of misleading historical reconstruction;
- novelty of what would be learned from generation;
- whether one image is enough or comparison is useful.

## Output purpose routing

Likely image-prompt destinations include:
- `site-illustration`
- `site-teaser`
- `cover-concept`
- `visual-reconstruction-test`
- `layout-reconstruction-test`
- `editorial-orientation`
- `voice/scene-example`
- `artifact-fiction-ad/mockup`
- `do-not-generate/use-original`

The reviewing LLM may add project-specific purposes.

## Relation to existing visuals

If a source page already contains an illustration or visual design:
- inspect / index the original first;
- do not generate a replacement by default;
- image generation may still be useful for a clearly labeled alternate interpretation, reconstruction experiment, or site-supporting derivative.

Generated imagery must not silently substitute for the original artifact.

## Editor handoff

At the end of a run, the reviewing LLM should receive a compact list like:

`candidate -> raw source -> optimized prompt -> try? -> why -> likely use -> source`

It should be free to:
- try none;
- try one;
- try two;
- rewrite the prompt;
- merge candidates;
- reject the auto-selected visual idea;
- promote a recurring prompt-extraction pattern into reusable tooling.

## FLC use

FLC is a good benchmark because it contains prose scenes, visual jokes, ads/page furniture, covers, illustrations, and story moments whose source language may itself be valuable prompt material.

For FLC, the default should be conservative where original illustrations exist and more experimental where a passage is visually strong but no original image occupies that role.
