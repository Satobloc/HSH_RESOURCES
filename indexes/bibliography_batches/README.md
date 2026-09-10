# Reviewed bibliography batches

This directory extends the human bibliography layer without turning `indexes/HUMAN_BIBLIOGRAPHY.md` into one enormous file.

Each `BATCH_*.md` file contains a bounded set of unique-content lineages that received human/LLM-reviewed bibliographic treatment. The current working batch size is 10 entries. Duplicate repository copies are recorded under the same entry rather than indexed as separate works.

The master `indexes/HUMAN_BIBLIOGRAPHY.md` remains the policy, prior-art, provenance, and citation-handoff surface. These batch files carry incremental general-resource indexing.

Automatic bibliography coverage and intake treat the master plus all `BATCH_*.md` files as one human bibliography corpus. A source disappears from the intake queue once any path in its byte-identical lineage is represented in that corpus.

Batch indexing establishes bibliographic identity and a neutral source description. It does **not** by itself establish H(s)H relevance, citation need, prior art, independent rediscovery, novelty displacement, or scientific validity. Those judgments belong to later comparison passes.

## Batch protocol

1. Take the next bounded set of unique-content lineages from `indexes/BIBLIOGRAPHY_INTAKE.md`.
2. Verify title, authorship, identifier, date/publication, and source type against the source or a primary bibliographic record when available.
3. Preserve every known repository path for duplicate copies.
4. State the actual read level. Do not imply a full-paper read from metadata/abstract verification.
5. Commit the reviewed batch. The bibliography-maintenance workflow then regenerates coverage and advances the intake queue.
6. Resolve extraction/OCR/orphan stragglers separately; they do not block ordinary bibliography batches.
