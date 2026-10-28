# Mira | 2026-10-28 07:12Z | Live September intake and structural-index drift

**Type:** read-only, source-grounded metadata and provenance audit. Current assistant operating under Mira's citation/Resources remit; **not** authenticated historical Mira participation. No PDF opened, extracted, approved, copied, indexed publicly, or attributed to Nathan. No Mersearch bridge overwritten. No physical calculation or H(s)H theory promotion.

## Immutable source snapshot

- Repository: `Satobloc/HSH_RESOURCES`, **main commit** `51e81fb5ea2ee145bce653eb6685b579a6c9130c`.
- `30SEP_PAPER_DUMP/` directory **tree** `9c0c7d56ba0a4d5fbb7aea21b411d0fc72a1f2fa`.
- `derived/manifests/extraction.jsonl` **blob** `511a5760c82aa2a09faf80f773c0bea089f27c04`.
- `indexes/index-state.json` **blob** `3978f885e212b34373b6c7c7c5251b919a56a85b`.
- Production extractor `tools/extract_papers.py` blob `18f316628fbeca06e523f1f16268f53f4815d3d5`; workflow `.github/workflows/extract-papers.yml` blob `4fbae103a2ff308f7564c81a3b5d723525796407`.
- Source roles: Git tree=path/byte identity; extraction manifest=process state; structural index=dated inventory snapshot; none proves original bibliography, copyright/license clearance, influence or scientific truth.

## Executed audit (connector-side JavaScript on actual source responses)

Parsed the entire pinned directory listing and every nonempty JSONL manifest row. Selected immediate PDF paths by filename extension, matched the exact `source_path` field, grouped *unmanifested* paths by Git blob SHA, and asserted all 116 manifest-covered September PDF paths exist in the pinned listing.

| Measure | Actual observed |
|---|---:|
| Immediate directory entries | 469 |
| Immediate PDF paths | 389 |
| September PDF paths in manifest | 116 (all `extracted`) |
| September PDF paths absent from manifest | **273** |
| Distinct Git blobs among those 273 paths | **245** |
| Duplicate-blob groups among pending | 22 |
| Excess pending aliases over unique blobs | 28 |
| Covered September records lacking author metadata | **110 / 116** |
| Covered September records lacking title metadata | **14 / 116** |
| Entire manifest records, all source folders | 1,183 |
| Entire manifest statuses | 1,166 extracted; 9 error; 8 needs_ocr |
| Latest manifest `processed_at` | 2026-10-19T10:52:19Z (outside September intake) |

The September coverage is **116/389 = 29.82% of paths**, with **70.18% absent**. Duplicate path aliases are not additional distinct content or additional papers. These counts reproduce the October 11 Mira coverage finding at a fresh, independently pinned October 28 repository commit; the new observation is **no progress in September path coverage despite subsequent manifest changes elsewhere**.

## Separate newly observed index-age defect

The live `indexes/index-state.json` is dated `scanned_at=2026-09-30T17:58:40Z` and records **123** entries under `counts_by_top_level["30SEP_PAPER_DUMP"]`. The pinned current directory listing contains **469** entries. Thus the structural index cannot serve as the current directory inventory. The numerical difference **346 entries** is a *snapshot discrepancy*, not a count of missing or unextracted PDFs.

The manifest has been updated since September 30, most recently October 19, while the structural index file has not (its latest path-specific commit is 2026-09-30T17:58:41Z). The `extract-papers.yml` workflow is triggered by PDF/tool changes, has a 100-file-per-pass bound and calls `extract_papers.py --apply`; source inspection found `PRIOR_ART` path pruning but **no per-document source-owner approval gate** integrated into that production path. A review-only Mira preflight exists separately and is **not** proof of production enforcement.

## Decision and next cursor

**Classification:** `SOURCE-METADATA VERIFIED / INTAKE BACKLOG CONFIRMED / STRUCTURAL INDEX STALE / APPROVAL GATE NOT INTEGRATED / EXTRACTION ON HOLD`.

1. Do not trigger bulk extraction or update the index by running production workflow before the Resources owner reviews scope and exposure. The Oct 24 change lifting research-access prohibitions does **not** itself approve public derivative extraction.
2. Request source-owner-reviewed, explicit clearance of one small, identified PDF and verify original citation/title/author/edition from an independent primary bibliographic source. Preserve every filename alias and Git blob identity.
3. For production repair, separate a **read-only, current-tree inventory refresh** from PDF content extraction. Review the existing `tools/index_papers.py` and preflight rather than building a new indexing engine. Add a fail-closed review gate to the actual extractor before unattended intake, with actual regression tests.
4. Source-critical bibliography recommendations for P1/P2/P3 require point-of-use manuscript claims and reviewed source identities, not mere filename matches.
5. Do not infer authenticated historical Mira-thread access or cross-chat delivery from this report.

**Lean triage:** Counting and duplicate-source identity are mathematical, but no physical law is asserted. A minimal source-conditional Finset/injectivity and observed-count consistency proof is appropriate; do not claim compiled until actual Lean 4/Mathlib CI succeeds. No data-free physics fixtures were used.

**Mersearch:** inspected active four-lane request state, all marked `requested` for existing archive topics. This is a **GitHub metadata audit, not a Mersearch run**. FIE rereview is not due (<14 days since Mira's October 27 review).
