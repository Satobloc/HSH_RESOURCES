# Mira | Review-only intake gate verification | 2026-10-11 EDT

**Disposition:** isolated prototype PASS for synthetic fixtures, NOT LIVE, NOT approved for production extraction.

## Exact tested code identity
- WORKSPACES/MIRA/intake_preflight_review.py: Git blob e910a751f3dc0dfe1a815e185f01ab71702b0db0; SHA-256 63b1eb1a6de06fd5bd88c68e9c896598c30ca6f31aeaaafa2bc0b96cd4b68be9; 8,844 bytes.
- WORKSPACES/MIRA/test_intake_preflight_review.py: Git blob 18b1056f6c18677d90d1b65ca3ba9ad5cb3505a3; SHA-256 d4d87ed5d2e522d0cdca3c901a94e7715c1e146213fbc50673702f3d1751af7e; 7,594 bytes.
- Local test copies returned the SAME Git object hashes as GitHub committed blobs (verified by git hash-object).
- Local Python unittest final rerun: **29 / 29 PASS**. Cases include explicit approval, default hold, missing citation, stale version, path traversal, folder/file symlink, restricted-name/metadata veto, contradicting approvals, duplicate blobs/manifest/inventory entries, missing filesystem and malformed approval envelope structures. Synthetic PDF bytes only.
- Additional CLI smoke: a synthetic approved fixture within a local checkout yielded provisional_review_pass_not_extraction_permission: 1. Malformed JSON approval file exited 2 with NO report file written.

## Live metadata recheck, at a PINNED commit
Exact Git revision: 1611d55db3a0590d05290b840ca51eda3b425d2e.
Two independent fetched surfaces: GitHub immediate directory listing for 30SEP_PAPER_DUMP/; complete derived/manifests/extraction.jsonl.

- **389** PDF paths; **116** path-level manifest entries; **273** unmanifested PDF paths.
- 273 unmanifested paths map to **245** distinct Git blob hashes; **22** duplicate-blob groups and **28** excess path aliases.
- **1** unmanifested PDF path triggers a restricted-name heuristic; filename and contents not reproduced. It is held, not entered in any approval list.
- No actual per-source owner approvals were supplied or issued; **0 newly authorized PDFs**. All 273 missing-record paths remain held.
- Earlier manifest metadata audit also found 110/116 extracted September records missing author and 14/116 missing title. This is NOT repaired by an eligibility script.

## Scope and limits
This is static approval classification from supplied metadata. A pass does not prove external citations, reviewer authority, actual source safety, that local files match Git blob identity, or later filesystem race safety.

Current production files reread:
- tools/extract_papers.py blob 18f316628fbeca06e523f1f16268f53f4815d3d5
- .github/workflows/extract-papers.yml blob 4fbae103a2ff308f7564c81a3b5d723525796407

The production job still lacks deny-by-default per-item clearance. No workflows launched, no live source PDFs opened, no production files edited, no scheduled-task changes. Mersearch slot remained Orson's request 2026-10-11-orson-morrow-inspiral-package-001, status requested-retry; no overwrite.

**Next:** source-owner-reviewed one-item bibliography/clearance and stronger runtime clean-checkout/TOCTOU design before production wiring.
