# HSH_RESOURCES — Human-Readable Source Index

> **Start here for people.** This is a compact router; the catalog itself is split into bounded documents rather than one giant file.

No record-bearing catalog document contains more than **100 records**.

## Browse the archive

| View | Use it for |
|---|---|
| [Folder / subfolder](indexes/human_source_index/BY_FOLDER.md) | Follow the actual repository hierarchy down to the containing directory. |
| [Subject](indexes/human_source_index/BY_SUBJECT.md) | Browse broad machine-assigned subject tags; records may appear in more than one subject. |
| [Author](indexes/human_source_index/BY_AUTHOR.md) | Alphabetical first-author browsing. |
| [Date](indexes/human_source_index/BY_DATE.md) | Browse by recoverable bibliographic year, newest first. |

## Research infrastructure

- [Integrated research-infrastructure roadmap](info/RESEARCH_INFRASTRUCTURE_ROADMAP.md)
- [Image / scanned-PDF OCR workflow](info/IMAGE_TEXT_EXTRACTION.md)
- [Research and exposure analytics engine](info/ANALYTICS_ENGINE.md)
- `tools/extract_papers.py` — embedded PDF-text extraction
- `tools/extract_image_text.py` — second-stage OCR for images and scanned PDFs
- `tools/audit_accessibility.py` — repository-wide retrieval/accessibility audit
- `tools/build_analytics_store.py` — rebuildable normalized SQLite analytical layer
- `tools/arxiv_sat_scanner.py` — arXiv structural-discovery scanner

Derived tools and indexes are navigation/analysis aids; raw repository sources remain canonical.

## Coverage at this build

- PDF paths in structural index: **1211**
- Unique PDF content groups: **1136**
- Reviewed unique-content groups: **70**
- Provisionally machine-indexed unique-content groups: **1065**
- Total bibliographically indexed unique-content groups: **1135**
- Explicitly excluded non-bibliographic unique-content groups: **1**
- Total accounted unique-content groups: **1136**
- Remaining unresolved unique-content groups: **0**

Human-facing catalog records: **1135** (69 reviewed, 1065 provisional, 1 explicit non-source exclusions).

### Status and tag discipline

`reviewed` means bibliographic identity received human/LLM review. `provisional` means identity/navigation came from extraction metadata and first-page heuristics and still needs individual review. `excluded` means the preserved artifact is not itself a literature/source item.

Subject tags are navigation aids, not theory claims. They are machine-assigned until individually reviewed and may be corrected without changing source provenance.

For citation decisions use `indexes/HUMAN_BIBLIOGRAPHY.md` and the HsH point-of-use citation ledger. For exact machine coverage use `indexes/BIBLIOGRAPHY_COVERAGE.md` and `indexes/RESOURCE_INDEX.md`.
