# HSH Resources — Orphan / Misfile Ledger

Status: provisional / append-oriented / provenance-first

Purpose: record files whose current path, filename, labeling, chronology, or linkage does not adequately expose their relationship to the SAT/H(s)H developmental record. Historical source files should normally remain in place; resolution should be by breadcrumbs, duplicate-lineage notes, and provenance crosswalks rather than moving source artifacts.

Confidence vocabulary: exact duplicate/content match; strong textual/chronological match; thematic relation; unresolved suspicion.

## O-001 — `PDF_SPECS/PERFECT v2.txt`

- Repository/path: `Satobloc/HSH_RESOURCES/PDF_SPECS/PERFECT v2.txt`
- Artifact type: substantive SAT manuscript draft, plain text
- Current folder label: `PDF_SPECS`
- Detected date evidence: uploaded to HSH_RESOURCES in commit `87c75232132bd5b79334e0c7617b0e65be82b1a3` on 2026-09-10; this is repository-ingest evidence, not composition date.
- Why orphaned/misfiled: contents are theory material rather than PDF/LaTeX formatting specifications. The document is titled `LEAN-4 VERIFIED GEOMETRIC CONSTRAINT YIELDS CHARGE-DEPENDENT MASS SPECTRUM` and includes a covariant action discussion, emergent Einstein equation, momentum-balance equation, topological mass formula `m_Ψ=(Tℓ_f/c²)(1/Q)`, a claimed `Q ≤ 3` UV Finiteness Lock, and proposed Q=2/Q=3 mass states.
- Main-archive duplicate/source lineage: exact-title/content matches are present at `SAT_THEORY_ARCHIVE_2023-25/MISC/PERFECT v2.txt`, `SAT_THEORY_ARCHIVE_2023-25/A_Theory_of_Everything/PERFECT v2.txt`, and `SAT_THEORY_ARCHIVE_2023-25/10-31-2025 SAT FULL THEORY/PERFECT v2.txt`. The `10-31-2025 SAT FULL THEORY` copy first appears in repository history in commit `e17b73aaab4bcb7bca22f94ff037d4e6cebe6aaa` on 2026-05-31; folder naming alone is not being treated as sufficient composition-date evidence.
- Related archive lineage: `UV Finiteness Lock` / `Q ≤ 3` language also occurs in `SATOBLOC/SATOBLOCK_inputs.txt`, `leanchecks/SATOBLOCK_FULLTHEORY_leancheck.txt`, `FORMALIZATION DEVELOPMENTS/SATOBLOCK_FULLTHEORY_leancheck.txt`, `SATOBLOC/SATO-BLOCK-INT.txt`, `SATOBLOC/SATOBLOCK-LIVE.txt`, and related SATOBLOC development files. This establishes a broader internal SAT/Blockwave lineage but does not yet identify the originating FULL_CONVO.
- Candidate source conversation(s): unresolved. No exact `UV Finiteness Lock` hit was recovered from the currently searchable HsH repository in this pass; absence from GitHub code search is not evidence of absence from deep/raw conversation exports.
- Candidate downstream document(s): `MISC/SUBMISSION_SUPPLEMENTAL.txt`, `A_Theory_of_Everything/SUBMISSION_SUPPLEMENTAL.txt`, and `10-31-2025 SAT FULL THEORY/SUBMISSION_SUPPLEMENTAL.txt` explicitly cite/reference the manuscript title in discussion of the momentum-balance equation and formal-verification layer.
- Duplicate/lineage relationship: strong exact-title/content lineage across three main-archive locations plus the HSH_RESOURCES copy; byte identity has not yet been independently hashed across all four copies in this audit pass.
- Confidence: high that the HSH_RESOURCES placement is a misfile; high for document-family identity; unresolved for originating conversation and true composition date.
- Read status: partial direct content inspection plus repository-wide exact-phrase search.
- Resolution status: OPEN — retain file in place; add bibliography/index breadcrumb rather than move. Next provenance task is to locate the earliest dated conversation/export containing the Q≤3/UV-lock construction and distinguish derivation, assertion, and later Lean encoding.

## Coverage limits

This ledger is not an exhaustive orphan scan. It currently records only candidates encountered during bibliography/provenance work. Deep miscellaneous/old/unsorted folders in all three repositories remain incompletely sampled; search-index silence must not be interpreted as absence.
