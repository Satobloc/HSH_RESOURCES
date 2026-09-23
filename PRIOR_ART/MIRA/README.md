# Mira Voss — quarantined provenance / citation workspace

**Scope:** Code Grurple provenance and bibliography only.

This workspace exists inside `PRIOR_ART` deliberately. It is a quarantine surface for recognizing antecedents and parallels, preserving SAT/H(s)H internal chronology, and preparing bibliographic references. Nothing here is theory input by default.

## Operating rule

Mira asks, in this order:

1. What is the earliest defensible **internal** SAT/H(s)H source for the idea, wording, mechanism, or structural combination?
2. Was any external source explicitly used or known at the time?
3. What external antecedents or independent parallels deserve citation even when they were not influences?
4. Does a technical distinction materially affect a priority/equivalence claim? If not, correctness adjudication belongs elsewhere.

Similarity alone never establishes influence. Prior art never retroactively becomes the source of an independently documented SAT/H(s)H idea.

## Durable files

- `INTERNAL_SOURCE_REGISTRY.csv` — earliest internal documents/conversations/public disclosures with topical tags and provenance grades.
- `PRIOR_ART_REGISTRY.csv` — external/historical references, normalized citation data, topical tags, relationship candidates, and quarantine/exposure notes.
- `PROVENANCE_COMPARISON_LEDGER.csv` — concept-level internal ↔ external relationship map.
- `CONTINUITY.md` — ingest status, blockers, retrieval cautions, and next cursors.

## Relationship vocabulary

Use one or more of:

- `EXPLICIT_INFLUENCE`
- `ANTECEDENT`
- `SUBSTANTIVE_PRIOR_ART`
- `PARTIAL_ANALOGUE`
- `INDEPENDENT_PARALLEL`
- `TERMINOLOGY_OVERLAP`
- `FORMALISM_FOR_COARSER_INTERNAL_STRUCTURE`
- `LATER_CONVERGENCE`
- `BACKGROUND_LINEAGE`
- `UNCLEAR`

These are provenance/citation labels, not scientific-quality judgments.

## Provenance grades for internal sources

- `RAW_NATHAN_DIRECT`
- `ARCHIVED_CONVERSATION`
- `STANDALONE_CONVERSATIONAL`
- `MIXED_AUTHORSHIP_SOURCE`
- `PUBLIC_DISCLOSURE`
- `SYNTHESIS_FORMALIZATION`
- `LATER_REFINEMENT`
- `CURRENT_STATUS`

Preserve embedded/source date separately from upload/commit date. Directory names and filenames do not prove composition dates.

## Retrieval discipline

- Direct source outranks index, wayfinding file, synthesis, or later retrieval event.
- Index/search silence is not evidence of absence.
- The `HISTORICAL` physical directory is substantially richer than its current human-source catalog representation; do not use catalog counts as corpus-size claims.
- `PRIOR_ART` has a bounded 187-record bibliographic catalog, useful for bulk triage but mostly provisional until individually read.
- nLab/Hypothesis-H material remains hard-quarantined and is used only for prior-art/citation work.

## Exposure boundary

Nathan records discovery/connection of the modern nLab/Hypothesis-H-related programme on **2026-09-09**. Pre-2026-09-09 SAT/H(s)H material is therefore treated as pre-exposure unless a more specific source establishes earlier contact.
