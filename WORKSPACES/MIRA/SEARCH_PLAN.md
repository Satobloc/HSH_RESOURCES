# Search plan

## Cross-archive native-tool harvest
Search all three active repositories for:
- Mersearch / Mercer_Searcher / Mercer search helpers
- SAT TO STANDARD / STANDARD TO SAT crosswalks
- full-text extractors and normalized corpora
- transcript/podcast indexing
- nLab mirroring, graph traversal, citation-lineage, Hypothesis H
- arXiv scanners and blind/x-ray search tools
- chronology/provenance indexes
- prior-art and citation ledgers

## Query strategy after tool harvest
1. Seed concepts from target-paper claims when available.
2. Expand each seed through SAT↔standard crosswalks.
3. Run exact/phrase/NEAR queries in old SAT archive.
4. Run compound-structure queries over normalized RESOURCES text and PRIOR_ART.
5. Branch through nLab graph/citation neighbors.
6. Search saved live-research/news corpora.
7. Run fresh arXiv/web searches for unresolved gaps.
8. De-duplicate by DOI/arXiv/title/content hash and assign relation class.
9. Close only at point of use in the papers.
