# SAT / H(s)H Equation Compendium — machine records

**Snapshot:** 28 November 2026  
**Coverage:** first compilation tranche; not an exhaustive archive harvest.

- `SAT_EQUATION_COMPENDIUM_SEED.json.gz` — gzip-compressed UTF-8 JSON containing 69 equation occurrences, 15 source documents, six sector-document mappings, source paths and blob identities, source equations, assumptions, provenance/maturity fields, and a document index.
- `NATHAN_DIRECT_PROJECTION_ANGLE_SEED.json.gz` — current consolidated machine-readable Nathan Direct sector-commentary compendium (the filename is retained from the initial projection-angle seed). It contains 73 direct user-role message texts from seven source documents. Initial coverage includes core SAT/θ₄ geometry and projection, Blockwave naming/transition, metric/filament/holonomy positioning, and Standard Model recoverability. Pasted code or assessments of unresolved/model-generated authorship are excluded; separable direct instructions are retained. The 24 October 2025 transcript date is approximate from its filename and has no message-level timestamps or IDs. This remains selective, not exhaustive.
- Typeset sector editions in `Satobloc/HsH/PUBLIC_SITE/PAPERS/`:
  - `nathan-direct-geometry-projection` — 43 direct user-role message texts from four conversations, dated 2 June 2025 and 25–28 February 2026.
  - `nathan-direct-gauge-topology` — six direct transcript turns, approximate date 24 October 2025.
  - `nathan-direct-blockwave-metric-sm` — 24 direct user-role message texts from two conversations, dated 13–14 September 2025; includes the SAT→Blockwave naming transition, the offshoot/minimal-ideal lineage statement, metric/holonomy positioning and Standard Model recoverability questions.
  - The first Blockwave transcript filename begins 25.09.12, while raw conversation metadata begins 2025-09-13; the PDF notes the discrepancy and uses raw message timestamps.
  - All three editions cite source paths and Git blob identities. PDF compilation and public-reader verification are separate statuses.

Decompress with `gzip -dk filename.json.gz` and parse the resulting UTF-8 JSON. Public-facing sector PDFs are published separately in `Satobloc/HsH/PUBLIC_SITE/PAPERS/`; their original source citations and links are embedded in the PDFs.
