# FLC Run 001 — Page Probe Summary

Heuristic visual classes only. These are triage cues, not reviewed page roles.

## flc1_lo.pdf — 48 pages

- `image-heavy`: 1, 6, 23, 41, 48
- `sparse/title/frontmatter`: 2, 24
- `text-heavy`: 3, 4, 8, 9, 12, 13, 14, 15, 16, 17, 18, 19, 21, 22, 25, 27, 28, 29, 30, 31, 32, 36, 38, 40, 43, 46, 47
- `mixed`: 5, 7, 10, 11, 20, 26, 33, 34, 35, 37, 39, 42, 44, 45
- strongest visual-attention candidates: 1, 48, 41, 23, 39, 46, 44, 9, 33, 31
- highest edge/text-density candidates: 14, 15, 8, 47, 18, 30, 36, 38, 19, 27

## flc2_lo.pdf — 41 pages

- `image-heavy`: 1, 4, 25, 28, 39, 40
- `sparse/title/frontmatter`: 41
- `text-heavy`: 2, 5, 6, 7, 10, 12, 14, 17, 19, 20, 21, 22, 23, 24, 26, 30, 36
- `mixed`: 3, 8, 9, 11, 13, 15, 16, 18, 27, 29, 31, 32, 33, 34, 35, 37, 38
- strongest visual-attention candidates: 39, 1, 40, 18, 25, 4, 28, 16, 34, 2
- highest edge/text-density candidates: 40, 18, 39, 1, 28, 10, 6, 24, 27, 22

## flc3_lo.pdf — 49 pages

- `image-heavy`: 1, 3, 19, 20, 21, 39, 41, 44, 45, 46, 48, 49
- `sparse/title/frontmatter`: 2, 40
- `text-heavy`: 7, 8, 9, 11, 12, 14, 16, 17, 18, 29, 30, 31, 32, 33
- `mixed`: 4, 5, 6, 10, 13, 15, 22, 23, 24, 25, 26, 27, 28, 34, 35, 36, 37, 38, 42, 43, 47
- strongest visual-attention candidates: 1, 49, 48, 3, 2, 45, 35, 6, 11, 22
- highest edge/text-density candidates: 49, 7, 32, 35, 14, 17, 1, 12, 9, 18

## Method note

The probe rendered every page and measured Otsu foreground fraction, edge density, color fraction and grayscale contrast. The rough class rules intentionally favor review triage over semantic interpretation. They do **not** distinguish story illustration, advertisement, cover, decorative furniture, pull quote, or photographic scan artifact.

The useful signal from this pass is not the labels themselves; it is the ability to route high-visual, sparse/title-like, and dense-text pages differently during the next reconstruction pass.
