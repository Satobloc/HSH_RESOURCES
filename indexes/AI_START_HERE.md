# HSH_RESOURCES — AI / LLM Start Here

> # **CRITICAL: MYSEARCH / MERSEARCH ARE ARCHIVE-RESIDENT SYSTEMS, NOT STANDALONE TOOLS**
>
> **THERE IS NO SEPARATE “TOOL EXPOSURE” FOR EITHER ONE.** Do not look for, request, or expect standalone Mysearch/Mersearch connector tools. Their implementations and operating interfaces live in the archives. Use them **through the connected archive connector**, whose repository read/write, workflow/Actions, and artifact operations provide access to the archived search systems. For archive-search tasks, use Mysearch/Mersearch **instead of the connector's generic search functions** wherever the documented bespoke route supports the task. Generic GitHub/code search is fallback only when that route genuinely cannot be operated; disclose the blocker and never mislabel fallback results.
>
> Start with the archive-resident instructions and request/workflow interfaces. Mersearch's connector route includes request lanes and an Actions bridge; inspect lane occupancy before writing and verify the request-specific manifest/receipt afterward. A compact receipt is not an exhaustive hit inventory. Check Mysearch's current operational status in its archive records.

> Compact routing contract for Janus and other H(s)H agents. Use this before scanning the repository broadly.

## Priority corridors

### 1. PRIOR_ART

Use [`ai_source_index/PRIOR_ART.md`](ai_source_index/PRIOR_ART.md) first.

This corridor is for external antecedents, comparison literature, chronology, citation credit, and deliberately provenance-labeled imports. Presence in `PRIOR_ART/` is **not** evidence that a source influenced SAT/H(s)H or that it contains the same result.

Read [`../PRIOR_ART/README_FROM_NATHAN.md`](../PRIOR_ART/README_FROM_NATHAN.md) before drawing genealogy or influence conclusions.

### 2. H(s)H_Toolkit

Use [`ai_source_index/HSH_TOOLKIT.md`](ai_source_index/HSH_TOOLKIT.md) first.

This corridor is a technical reference library: mathematics, geometry/topology, GR, QFT, strings/higher dimensions, variational methods, and related tools. Treat it as reference material, not as the generative basis of H(s)H.

## Machine layers

- [`RESOURCE_INDEX.md`](RESOURCE_INDEX.md) — complete structural catalog of repository files. It records presence, file identity, duplicate-content groups, and identifier hints. It is **not** a bibliography or relevance judgment.
- [`index-state.json`](index-state.json) — machine-readable structural state backing the resource index.
- [`../derived/manifests/extraction.jsonl`](../derived/manifests/extraction.jsonl) — authoritative `source_path → sha256 → text_path` mapping, with extraction status, page count, metadata, OCR-needed state, and errors.
- [`../derived/README.md`](../derived/README.md) — extraction-layer rules and the GitHub 1,000-entry truncation warning.
- [`../!_HSH_RESOURCES_INDEX.md`](../!_HSH_RESOURCES_INDEX.md) — compact human-facing router by folder/subfolder, subject, author, and date.

## Retrieval protocol for agents

1. Start from the relevant priority corridor rather than the full repository tree.
2. Use the bounded catalog shards to identify the exact repository source path and bibliographic identity.
3. For full-text work, locate that exact `source_path` in `derived/manifests/extraction.jsonl` and follow its `text_path` into `derived/text/`.
4. If the manifest status is `needs_ocr` or `error`, record that limitation; do not infer that the source is absent or unreadable in principle.
5. Preserve exact repository paths and duplicate lineage. Byte-identical copies may share one extracted-text object.
6. Distinguish source presence, successful extraction, bibliographic identity, actual reading, relevance, citation need, and priority/novelty conclusions.
7. Do not use GitHub directory-listing silence as evidence of absence. Large directories may be visually truncated.

## Theorybuilding boundary

External literature may provide credit, standard results, empirical constraints, prior-art comparison, or an explicitly labeled import. It should not silently become an H(s)H premise. Internal SAT/H(s)H provenance and external citation are separate questions.

For actual point-of-use citation obligations, use `indexes/HUMAN_BIBLIOGRAPHY.md` on this source side and `Satobloc/HsH/ledgers/CITATION_LEDGER.md` on the theory side.