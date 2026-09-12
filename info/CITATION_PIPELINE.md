# Citation Pipeline

The bibliography answers **what sources are available**. Citation work answers a different question: **what source, exactly, supports this particular sentence or construction?**

The HsH point-of-use citation ledger remains the controlling work surface. This document describes the research-side automation around it.

## Core flow

```text
statement / claim
    ↓
citation need
    ↓
candidate-source retrieval
    ↓
source inspection
    ↓
exact page / section support
    ↓
verified bibliographic identity
    ↓
point-of-use citation
```

Do not skip directly from keyword match to citation.

## Citation-need record

A useful citation-need object should retain:

- stable `CITE-YYYY-NNN` ID;
- HsH file / section / line or conversation locator;
- exact proposition requiring support;
- citation role (`STD`, `EMPIRICAL`, `PRIOR_ART`, `COMPARISON`, `CONSTRAINT`, `DELIBERATE_IMPORT`);
- lifecycle state (`NEEDED`, `PLACED`, `VERIFIED`, `REJECTED`, `SUPERSEDED`);
- search terms / concepts;
- candidate source IDs;
- selected source and page/section anchors;
- reviewer note explaining why the source supports the proposition.

## What can be automated

### Bibliographic identity

Detect and normalize:

- arXiv IDs and versions;
- DOI;
- title/author/year;
- duplicate PDFs;
- journal references.

### Candidate retrieval

Search the extracted HSH_RESOURCES text corpus by concept, phrase, equation token, author, title, or structural vocabulary. Candidate retrieval is recall-oriented; it does not verify support.

### arXiv intake

The arXiv API is well suited to metadata discovery. Full papers are retrieved separately from arXiv's PDF/source endpoints. Once a PDF is archived, `tools/extract_papers.py` creates page-marked text and `tools/extract_image_text.py` handles image-only pages when necessary.

This means automated “pull the relevant pages” should be implemented as a chain rather than pretending the API itself supplies page-level evidence:

```text
arXiv ID / scanner hit
→ metadata
→ PDF/source retrieval
→ archive + hash
→ page-marked extraction/OCR
→ full-text candidate search
→ exact page review
```

### Citation candidate handoff

Automation may propose:

- source identity;
- likely supporting pages;
- short support synopsis;
- Chicago-style bibliographic record;
- ledger handoff ID.

It should never mark a citation `VERIFIED` merely because terms overlap.

## New literature

When citation work reveals a missing source:

1. add it through the research-intake route;
2. preserve original PDF/source and bibliographic identity;
3. run extraction/OCR;
4. update bibliography/index coverage;
5. return to the citation need;
6. verify the exact supporting passage;
7. place the citation.

This keeps the bibliography and citation system synchronized without treating bibliography completeness as permanently closed.

## Page-anchor discipline

For important claims preserve the smallest useful locator:

- PDF page number, preferably both PDF index and printed page if they differ;
- section/equation/figure number where available;
- extracted-text page marker;
- exact archived source path/hash.

For priority comparisons, also preserve the public version/revision date. A later arXiv version may contain language absent from the earlier version.

## Standard literature vs priority literature

A standard citation establishes accepted background or machinery. A prior-art citation establishes that a sufficiently specific construction existed by a particular date. Those are not interchangeable jobs.

For priority work the source must support both:

1. substantive equivalence at the relevant compound/dependency level; and
2. the chronology being asserted.

Generic ingredient citations do not settle priority.

## Planned automation

The next useful citation-side tools are:

- arXiv paper intake/downloader with dry-run and explicit destination;
- extracted-corpus candidate search that emits page candidates;
- citation-need → candidate-source report;
- bibliography/ledger consistency checker;
- page-anchor verifier for archived PDFs/extracts.

The system should optimize the expensive human/LLM step — reading the right pages — rather than automate away the evidentiary judgment.
