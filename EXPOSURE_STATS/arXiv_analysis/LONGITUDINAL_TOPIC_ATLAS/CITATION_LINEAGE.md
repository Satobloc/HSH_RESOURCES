# Citation Lineage — external literature ancestry / descent map

## Purpose

Build a source-traceable citation graph that shows, as far as the papers themselves document it, which published ideas cite which earlier work. This is an external-literature parallel to the internal SAT/H(s)H development lineage.

This graph does **not** infer intellectual influence from resemblance alone. Its primary edge is explicit citation.

## Preferred accessible source: Semantic Scholar Academic Graph

Semantic Scholar's public Academic Graph API exposes paper metadata plus paginated `references` and `citations` endpoints. It also exposes citation `contexts`, `intents`, and an `isInfluential` flag where available. It accepts common external IDs including arXiv identifiers and DOI-based identifiers.

Documentation:
- https://api.semanticscholar.org/api-docs/
- https://www.semanticscholar.org/product/api

Why it is useful here:
- explicit backward edges: paper → cited paper;
- explicit forward edges: citing paper → paper;
- citation-context text can sometimes show *why* a reference was invoked;
- arXiv and DOI identifiers make it practical to join with our arXiv corpus and research library;
- public unauthenticated access exists, although rate limits are shared and an API key is recommended for sustained harvesting.

## Secondary / corroborating source: Crossref

Crossref's public REST API provides publisher-deposited bibliographic metadata and references when deposited. It requires no sign-up for ordinary use. It is useful for DOI identity resolution, publisher metadata, references, publication dates, and independent verification of bibliographic edges.

Documentation:
- https://www.crossref.org/documentation/retrieve-metadata/rest-api/

Crossref reference coverage is not complete because references depend on what publishers deposited. Missing Crossref edges must not be interpreted as absence of citation.

## Edge classes

- `EXPLICIT-CITATION` — source paper lists target in its bibliography.
- `CITATION-CONTEXT` — text context around the citation is available.
- `CITATION-INTENT` — Semantic Scholar intent label is available.
- `S2-INFLUENTIAL` — Semantic Scholar marks the citation influential.
- `BIBLIOGRAPHIC-MATCH` — identity resolution between arXiv/DOI/S2/Crossref records.
- `REVIEW-ANCESTRY` — a review explicitly identifies earlier lineage; retain as a claim from that review, not automatic historical truth.
- `AUTHOR-PRIOR-WORK` — paper cites earlier work by overlapping authors; descriptive only.

Do not create an influence edge from topic similarity, chronology, common terminology, or embedding similarity. Those belong in separate comparison tables.

## Lineage products

For each comparison concept or paper cluster we should be able to generate:

1. backward citation tree to older work;
2. forward citation descendants;
3. earliest located nodes by publication date;
4. review papers that explicitly narrate the lineage;
5. citation contexts explaining what later authors say they took from earlier papers;
6. discontinuities: similar concepts with no located citation path between them;
7. convergence candidates: structurally related clusters with distinct citation ancestry;
8. joins to the longitudinal arXiv topic atlas, so lineage and field-wide prevalence can be viewed separately.

## Evidentiary wording

Preferred:
- "Paper B explicitly cites Paper A."
- "The available citation context describes A as ..."
- "A is the earliest node located in this citation-descendant subgraph."
- "No citation path was located in the harvested graph."

Avoid unless independently demonstrated:
- "B descends from A" as a statement of actual intellectual causation;
- "A originated the idea";
- "B was influenced by A";
- "independent invention" merely because no citation was found.

## Join keys

Preserve all available identifiers:

`arxiv_id, doi, semantic_scholar_paper_id, corpus_id, crossref_doi, title, year`

Identifier resolution should be stored separately from conceptual interpretation.

## Immediate implementation

`semantic_scholar_lineage.py` accepts arXiv IDs, DOIs, or Semantic Scholar paper IDs and stores paper metadata, direct references, direct citations, contexts/intents where available, and a normalized edge CSV/JSON. Deeper traversal should be depth-limited and cached to avoid unnecessary API load.
