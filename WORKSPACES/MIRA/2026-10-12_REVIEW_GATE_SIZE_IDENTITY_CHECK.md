# Mira review-only intake gate — local size identity check

date_utc: 2026-10-12
run_key: REVROT3-19-20261012:03:s3
worker_route: active manually authorized Mira successor
conversation_title: Research intake review
conversation_id: UNKNOWN_NOT_SURFACED
status: REVIEW_ONLY_TESTED_NOT_DEPLOYED
pdf_contents_opened: 0
new_pdf_approvals: 0
production_workflow_changed: false

## Question

Can the existing review-only physical-containment gate reject a same-path checked-out file whose byte count no longer matches the pinned repository inventory, without reading PDF content or changing the extractor?

## Source state inspected

- `WORKSPACES/MIRA/intake_preflight_review.py`, prior blob `e910a751f3dc0dfe1a815e185f01ab71702b0db0`
- `WORKSPACES/MIRA/test_intake_preflight_review.py`, prior blob `18b1056f6c18677d90d1b65ca3ba9ad5cb3505a3`
- `WORKSPACES/MIRA/INTAKE_PREFLIGHT_README.md`, prior blob `1e7ac0f8a5523433152542823713ff5b72963617`
- `WORKSPACES/MIRA/2026-10-11_REVIEW_ONLY_PREFLIGHT_TEST_RECEIPT.md`, blob `c8e7660b96a70cb8c819fd56e20be9661f31fe4b`
- `WORKSPACES/MIRA/2026-10-11_SUCCESSOR_INTAKE_IDENTITY_AUDIT.md`, blob `1b090dc096aa04708bab69db9ec2e6afe1d453f9`

The prior suite already covered file and directory symlinks. Repeating that suggested test would not add coverage.

## Change

The review-only `physical_check` now receives the pinned inventory byte count and requires the resolved local file's `stat().st_size` to match it. A synthetic regression changes the fixture's local file from ten bytes to five while keeping the same approved path and pinned inventory record; the gate must return `hold_physical_containment_unverified`.

Committed identities:

- code commit `120b0112408c82cec74fbec31869c4d09cf67857`; blob `596384f3d7bd74a17e8dfeac4ca262ce2c0f2dc4`
- test commit `1f9b18e755866d1e831baf42888d2893d0acd4ea`; blob `5956705173024b1cfc5d06fe27faa752fb6473c3`
- documentation commit `486ce7d0e632ce326c6116f0529f76e27b282e22`; blob `1bad9eedc5763b53b27c84717c361ff35ce2f063`

## Verification

Fresh committed blobs were fetched and executed in memory under Python 3.12.

- tests run: 30
- failures: 0
- errors: 0
- result: PASS

No real PDF was opened or approved. No workflow, extractor, Mersearch request, scheduler, or production allowlist was changed.

## Evidential limit

This closes only a metadata-level size mismatch. Equal size is not content identity, Git blob identity, authorship verification, bibliographic clearance, reviewer authentication, or protection against later time-of-check/time-of-use changes. The gate remains an isolated review prototype and does not authorize extraction.

## Next cursor

After source-owner clearance for exactly one demonstrably permissible PDF, run the review gate from a clean checkout pinned to the inventory commit, then independently verify the actual Git blob/hash before any content access. Until then all real pending PDFs remain held.
