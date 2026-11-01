# Mira intake identity preflight | REVIEW ONLY

**State:** TESTED LOCALLY / NOT DEPLOYED / NOT EXTRACTION AUTHORIZATION
**Scope:** September 30 PDF paths in HSH_RESOURCES; no reads of PDF bytes.

**Current research-access policy (2026-10-24 Nathan Direct; confirmed 2026-10-27):** The earlier October 9 blanket research-access prohibition for Hypothesis H proper and directly Schreiber-authored sources is superseded for research reading/comparison after internal SAT/H(s)H provenance is recovered. This does not authorize public indexing, redistribution of private material, publication without review, or importation of external assumptions as SAT premises. Mira remains outside the active internal review corpus; only cleared operational answers may cross that exposure boundary.

**Local gate remains stricter by design:** This review-only program still applies its `DENY_NAME`, path-component and metadata vetoes as fail-closed holds. Those vetoes are a local safety control, not current project-wide research-access policy. Do not remove them or treat their presence as proof that a source is globally prohibited; do not treat their absence as clearance. No PDF bytes are opened or extraction authorized by this README. Any later intake still requires source-owner per-item clearance, exact pinned source identity, and a separately reviewed production workflow.

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
- The commit is format-checked, not verified against a live checkout's HEAD/clean tree. Physical inspection now requires the local file size to match the pinned inventory, but actual PDF bytes and Git blob content are not read; equal size is not immutable-source identity. A production integration must enforce the full blob/hash identity independently.
- Physical symlink checks are inspection-time only, not a TOCTOU-resistant PDF-open control. Recheck at use time or use safe file descriptors in any later extractor integration.
- A filename/title/author keyword deny rule cannot identify every forbidden source; source-owner per-item clearance is indispensable.
- The existing production extractor and workflow are unchanged and do NOT use this preflight. An isolated review-only tool does not secure the live extractor.
- Git blob equality establishes same stored bytes, not same intellectual work/edition, author, original citation or source approval. Manifest completion is not bibliographic closure.
- Treat previous extracted/OCR/error rows separately; do not grandfather as safe.

## Next controlled cursor
Have the source owner choose ONE demonstrably nonrestricted candidate and provide authoritative bibliographic identity and a recorded approval pinned to exact Git blob/commit. Then run the gate on a controlled clean checkout before proposing a separate, explicitly reviewed production gate. No unrestricted batch or change to the busy Mersearch shared request slot.
