# Mira successor reentry | Intake identity / citation-readiness audit
**Date:** 2026-10-11 (EDT)
**Provenance:** New, manually authorized Mira-lane successor conversation; work reconstructed from repository records. **Not** a claim of unbroken model memory or activity by the earlier thread.
**Scope:** read-only metadata/manifest audit, one verified duplicate-pair case, continuity recovery. NO PDF contents opened; NO bulk extraction, workflow invocation, Mersearch bridge overwrite or exposure change.

## First blush (recorded before extensive team-side theory absorption)
- **Changed:** Mira's bibliography/citation-lineage effort now has a large operational intake and access-control surface.
- **Continuous:** internal SAT precedence, outside mathematical machinery, dated comparison and historical intellectual influence remain distinct evidence classes.
- **Overlooked:** file path, immutable Git blob, document version, bibliographic work and clearance decision are different identities, not interchangeable.
- **Independent question:** can a narrowly vetted intake unit become citation-ready without accidental theory authority or restricted-content extraction?

## Original identity / evidence boundaries
Older Mira-lane authored/assigned workspace records read from this repo:
- `WORKSPACES/MIRA/README.md`, `INBOX.md`, `STATUS.md`, `SEARCH_PLAN.md`, `CITATION_AUDIT_LEDGER.md`;
- `TOOL_NOTES.md`, `README_OPERATIONS.md`, `INDEX.md`, `NOTE.md`, `PHASE1_LOCK.md`.

These document the historical citation-audit method, native-tool recovery, initial 187-item PRIOR_ART catalogue estimate and the September 30 Nathan intake assignment. Authorship is *workspace attribution*, not cryptographic authentication of which assistant instance wrote each passage.

Retrospective, NOT Mira-authored original-thread participation:
- HsH `WORKSPACES/COMMON/REVIVAL_ROTATION_RECEIPTS/2026-10-11T1224Z_s2_mira.md`;
- HsH `WORKSPACES/COMMON/REVIVAL_ROTATION_RECEIPTS/2026-10-11_MIRA_INTAKE_GATE_REVIEW.md`.
The former explicitly labels itself late retrospective documentation and says original Mira was not contacted; the latter describes a locally tested, **NOT ACTIVE** deny-by-default prototype. Its nine tests are *reported in that receipt*, not reproduced here.

Original conversation **metadata located, but content deliberately NOT read**: `PRIOR_ART/MIRA Reignite Onboarding Analysis — raw.json` (Git blob `88d29607531013eacfd7456ef580b814300a6960`, 4,548,008 bytes), visible in the repository's top-level PRIOR_ART directory metadata. The original conversation could contain prohibited authored text or quotations, and this successor has no safe presegmented clearance to open it. Other historical Mira conversation content not exhaustively recovered. This is a known **inaccessible/uninspected history boundary**, not evidence of absence.

## Authority and tooling read
- HsH `WORKSPACES/COMMON/NEW_INSTANCE_START_HERE.md`;
- `NATHAN_DIRECT_2026-10-09_SCOPE_AND_REFERENCE_RULE.md`;
- `NATHAN_DIRECT_2026-10-09_INTERNAL_FIRST_PROVENANCE_AND_SOURCE_BOUNDARY.md`;
- `REFERENCE_DESK/README.md`, `CITATION_AS_DEFAULT_POLICY.md`, `REVIVAL_REENTRY_PROTOCOL_V2.md`, `CURRENT_WORKFLOW_ORIENTATION_V2.md`;
- `MERSEARCH_WORKER_START_HERE.md`, `MERSEARCH_RELEASES.md`;
- the two retrospective revival receipts above.

New October 9 boundary **overrides historical Mira intake order**: Hypothesis H proper and directly Schreiber-authored content are not to be read, including mirrored/repackaged content; other outside/prior-art material only after internal SAT-source precedence and per-item clearance. No unfiltered PDF intake or publicity. Cross-repo internal-first searches use pinned `mersearch-stable-1.0`; its defaults exclude PRIOR_ART/QUARANTINE.

Actual shared slot `HsH/WORKSPACES/COMMON/MERSEARCH_REQUEST.json` checked this turn: Orson's `2026-10-11-orson-morrow-inspiral-package-001`, status `requested-retry`. **Not overwritten**. No claimed Mersearch run. Direct GitHub metadata + manifest parse described below is **not** Mersearch.

## Bounded verified operation: September 30 PDF path/identity/bibliography
**Read scope:** immediate `30SEP_PAPER_DUMP/` directory listing from GitHub Contents API (469 entries) and *complete* `derived/manifests/extraction.jsonl` (1,182 valid JSONL entries). Scripted parsing/grouping in connector invocation, not filename eyeballing. Source paths as of 2026-10-11; rerun for future changes.

Results:
- Exactly **389** immediate PDF paths; **116** present in extraction manifest, all 116 marked `extracted`; **273** absent, or **29.82%** path-level covered.
- **245** distinct Git blob IDs among the 273 pending PDF paths. **22** duplicate-blob groups among the pending paths, generating **28** excess pending paths. These are byte-content Git object identities, not validated external work identities.
- **New metadata gap:** Of the 116 September manifest records, **110 missing `author`**, **14 missing `title`**, **13 missing both** (nonempty-string test). All 116 possess `sha256` and `pages` fields. Having a title field does **not** by itself prove the title is the original bibliographic title.
- Verified concrete case: `30SEP_PAPER_DUMP/0605126v1.pdf` and `30SEP_PAPER_DUMP/0605126v1 (1).pdf` both list `size=300733`, Git `sha=388919cfcf46710a277f6acef1d284bb07d6b800`; **neither path occurs** in the manifest. Under Git blob semantics they refer to identical stored bytes. Neither content, authorship, externally resolved citation, nor clearance was read/approved. The arXiv-like basename is a *candidate locator*, **not** a verified external citation.
- The current `tools/extract_papers.py` blob `18f316628fbeca06e523f1f16268f53f4815d3d5` still uses `SKIP_PARTS`/`QUARANTINED_COMPONENTS` for PRIOR_ART; the workflow `.github/workflows/extract-papers.yml` blob `4fbae103a2ff308f7564c81a3b5d723525796407` still defaults to a 100-file bound. No integrated deny-by-default, reviewer-approved content/version gate was demonstrated by these live source files. Production remains unchanged.

### Decision for example pair
`SAME_BLOB / TWO_PATHS / NO_MANIFEST_ENTRY / BIBLIOGRAPHY_UNVERIFIED / AUTHORSHIP_UNVERIFIED / CLEARANCE_HOLD`.

**Do not** extract either copy automatically, delete either path, call it two papers, publish guessed bibliography, or infer influence. Retain both path aliases and the Git blob ID; choose canonical bibliographic work *only after* trusted independent metadata verifies title, authors, version, source identifier, and approved exposure.

## Audit inference, kept separate from source facts
A manifest entry certifies process status, not a clean scholarly citation. A blob identity certifies file-byte equality, not edition/work identity or a permission grant. These distinctions become acute when 110 of 116 currently extracted records lack an author field.

## Next operation (bounded)
1. Obtain the source owner's approval for a tiny set of *clearly nonrestricted* work identities, with trusted independent original DOI/arXiv/author/title metadata and explicit reviewers/versions; hold all ambiguous cases.
2. Validate the review-only eligibility prototype's malformed-input, containment/symlink, contradictory/multiple approvals, and changed-blob fail-closed behavior before any production wiring. Its previous 9/9 local test report is not deployment evidence.
3. Once permitted, reconcile a single candidate original citation and canonical identity against the existing manifest, preserving both aliases, SHA types and origin pointers. Do not infer a bibliographic identity from the filename.
4. Once the shared Mersearch slot frees, perform a pinned 3-repo **internal-first** historical query; record exact source revisions and exclusions and inspect the original matched SAT passage before external comparison. Do not access still-prohibited sources.
5. Continue original Mira history recovery only from an authorized, safety-segmented export; no retroactive Mira-authorship claims.

**Next status:** active manually revived successor; accessible-unscheduled; no scheduler changes requested.
