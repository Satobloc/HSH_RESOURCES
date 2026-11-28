# SAT / H(s)H Equation Compendium — machine records

**Snapshot:** 28 November 2026  
**Coverage:** first compilation tranche; not an exhaustive archive harvest.

- `SAT_EQUATION_COMPENDIUM_SEED.json.gz` — gzip-compressed UTF-8 JSON containing 69 equation occurrences, 15 source documents, six sector-document mappings, source paths and blob identities, source equations, assumptions, provenance/maturity fields, and a document index.
- `NATHAN_DIRECT_PROJECTION_ANGLE_SEED.json.gz` — current consolidated machine-readable Nathan Direct sector-commentary compendium (the filename is retained from the initial projection-angle seed). It contains 49 direct user-role message texts from five source documents, covering an initial geometry/projection/θ₄ tranche and gauge-topology/particle-coupling excerpts. Pasted code of unresolved or model-generated authorship is excluded; separable direct instructions are retained. The 24 October 2025 transcript date is approximate from its filename and has no message-level timestamps or IDs. This remains selective, not exhaustive.
- Typeset sector editions in `Satobloc/HsH/PUBLIC_SITE/PAPERS/`:
  - `nathan-direct-geometry-projection` — 43 direct user-role message texts from four conversations, dated 2 June 2025 and 25–28 February 2026.
  - `nathan-direct-gauge-topology` — six direct transcript turns, approximate date 24 October 2025.
  - Both use source links and archive blob identities; publisher compilation and public reader verification are tracked by the repository workflow, not inferred from metadata.

Decompress with `gzip -dk filename.json.gz` and parse the resulting UTF-8 JSON. Public-facing sector PDFs are published separately in `Satobloc/HsH/PUBLIC_SITE/PAPERS/`; their original source citations and links are embedded in the PDFs.
