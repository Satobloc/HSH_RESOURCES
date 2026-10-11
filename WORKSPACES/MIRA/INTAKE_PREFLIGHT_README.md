# Mira intake identity preflight | REVIEW ONLY

**State:** TESTED LOCALLY / NOT DEPLOYED / NOT EXTRACTION AUTHORIZATION
**Scope:** September 30 PDF paths in HSH_RESOURCES, no reads of PDF bytes. Current restrictions forbid Hypothesis H proper and directly Schreiber-authored content, including mirrors. Name/metadata vetoes only deny; they never establish clearance.

Files:
- [intake_preflight_review.py](intake_preflight_review.py): isolated review-only metadata gate.
- [test_intake_preflight_review.py](test_intake_preflight_review.py): synthetic fixture tests.
- [2026-10-11_REVIEW_ONLY_PREFLIGHT_TEST_RECEIPT.md](2026-10-11_REVIEW_ONLY_PREFLIGHT_TEST_RECEIPT.md): pinned evidence and test results.

## Input schema
1. Trusted pinned repository inventory JSON, object with repository="Satobloc/HSH_RESOURCES", commit=<40-hex-repository-commit>, files=[{path,blob_sha,bytes}, ...].
2. Existing derived/manifests/extraction.jsonl, with source_path keys.
3. Approval JSON object: repository="Satobloc/HSH_RESOURCES", schema_version=1, inventory_commit=<same commit>, approvals=[] as the default deny-all baseline.

Each approved path additionally requires path, blob_sha, bytes, reviewed_commit, literal Boolean approved, author_checked, restriction_checked, plus nonblank reviewer, original_citation, canonical_work_id, bibliographic_source, review_record. These represent human review attestations, not independently authenticated truth.

## Local commands

Run from the repository root on a trusted checkout:

    python -m unittest discover -s WORKSPACES/MIRA -p 'test_intake_preflight_review.py' -v
    python WORKSPACES/MIRA/intake_preflight_review.py \
      --inventory /path/to/pinned_directory_inventory.json \
      --manifest derived/manifests/extraction.jsonl \
      --approvals /path/to/reviewed_approvals.json \
      --root . \
      --output /tmp/mira_review_only_report.json

Omitting --root holds all new candidates lacking physical-containment inspection. This program does not generate an extractor allowlist, run OCR, invoke GitHub Actions or publish a bibliography. Pre-existing extraction rows are NOT automatically cleared.

## Production blockers
- Attestation fields cannot verify reviewer authenticity, actual authorship, bibliographic citation accuracy or permission.
- The commit is format-checked, not verified against a live checkout's HEAD/clean tree; actual PDF bytes are not read. A production integration must independently enforce immutable-source identity.
- Physical symlink checks are inspection-time only, not a TOCTOU-resistant PDF-open control. Recheck at use time or use safe file descriptors in any later extractor integration.
- A filename/title/author keyword deny rule cannot identify every forbidden source; source-owner per-item clearance is indispensable.
- The existing production extractor and workflow are unchanged and do NOT use this preflight. An isolated review-only tool does not secure the live extractor.
- Git blob equality establishes same stored bytes, not same intellectual work/edition, author, original citation or source approval. Manifest completion is not bibliographic closure.
- Treat previous extracted/OCR/error rows separately; do not grandfather as safe.

## Next controlled cursor
Have the source owner choose ONE demonstrably nonrestricted candidate and provide authoritative bibliographic identity and a recorded approval pinned to exact Git blob/commit. Then run the gate on a controlled clean checkout before proposing a separate, explicitly reviewed production gate. No unrestricted batch or change to the busy Mersearch shared request slot.
