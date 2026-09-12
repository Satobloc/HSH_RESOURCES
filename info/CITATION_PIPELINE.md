# Citation Pipeline

The bibliography answers **what sources are available**. Citation work answers a different question: **what source, exactly, supports this particular sentence or construction?**

The HsH point-of-use citation ledger remains the controlling work surface. This document describes the research-side automation around it.

## Public/private boundary

`HSH_RESOURCES` is a private reference warehouse. Its repository paths and URLs are useful for internal recovery and verification, but they are **not the public citation surface**.

The public project-record cross-link is:

**`Satobloc/HsH` ↔ `Satobloc/SAT_THEORY_ARCHIVE_2023-25`**

When evidence from HSH_RESOURCES is used in either public repository, the public-facing result should normally contain one or more of:

- a **Chicago-style citation to the original external source**;
- an attributed **quotation/extract** with page or location information;
- a sourced **summary/paraphrase** with enough provenance to identify the original source;
- for private/raw project data, a **public-safe extract or summary** describing what was analyzed and its provenance.

The private-side citation handoff may additionally preserve the exact HSH_RESOURCES path, content hash, extraction path, and review notes. Those internal locators are for reproducibility/recovery, not substitutes for the public citation.

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
public-usable citation / quotation / sourced summary
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
- selected original source identity and page/section anchors;
- private archived-copy path/hash when useful for recovery;
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
→ private archive + hash
→ page-marked extraction/OCR
→ full-text candidate search
→ exact page review
→ original-source citation / public-safe extract
```

### Citation candidate handoff

Automation may propose:

- original source identity;
- likely supporting pages;
- short support synopsis;
- Chicago-style bibliographic record;
- ledger handoff ID;
- private archived-copy locator/hash for internal recovery.

It should never mark a citation `VERIFIED` merely because terms overlap.

## New literature

When citation work reveals a missing source:

1. add it through the research-intake route;
2. preserve original PDF/source and bibliographic identity;
3. run extraction/OCR;
4. update bibliography/index coverage;
5. return to the citation need;
6. verify the exact supporting passage;
7. place the public-usable citation/quotation/summary at the point of use.

This keeps the bibliography and citation system synchronized without treating bibliography completeness as permanently closed.

## Page-anchor discipline

For important claims preserve the smallest useful locator:

- PDF page number, preferably both PDF index and printed page if they differ;
- section/equation/figure number where available;
- extracted-text page marker;
- exact private archived source path/hash for recovery;
- original public source identifier/URL/DOI/arXiv record for citation.

For priority comparisons, also preserve the public version/revision date. A later arXiv version may contain language absent from the earlier version.

## Standard literature vs priority literature

A standard citation establishes accepted background or machinery. A prior-art citation establishes that a sufficiently specific construction existed by a particular date. Those are not interchangeable jobs.

For priority work the source must support both:

1. substantive equivalence at the relevant compound/dependency level; and
2. the chronology being asserted.

Generic ingredient citations do not settle priority.

## Planned automation

The next useful citation-side tools are:

- arXiv paper intake/downloader with dry-run and explicit private destination;
- extracted-corpus candidate search that emits page candidates;
- citation-need → candidate-source report;
- bibliography/ledger consistency checker;
- page-anchor verifier for archived PDFs/extracts;
- public-output checker that flags HSH_RESOURCES private links where a normal citation/quotation/summary is required.

The system should optimize the expensive human/LLM step — reading the right pages — rather than automate away the evidentiary judgment.
