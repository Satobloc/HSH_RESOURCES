# Mira | 2026-10-26T13:24Z | review-only gate policy-drift audit

Participation: source-grounded workshop reconstruction in Mira's citation/provenance remit; original Mira conversation not contacted.
Run: REVROT3-19-20261026:13:s2; h=373; seq=1867; index=5 Mira; next index=6 Aldus.
Status: POLICY-SOURCE-MISMATCH CONFIRMED / NO EXTRACTION AUTHORIZED.

## Evidence

- Current HsH Nathan Direct Oct 24, WORKSPACES/COMMON/NATHAN_DIRECT_2026-10-24_PRIOR_ART_UI_ARCHIVE_READING_ANNOUNCEMENT.md, Git blob 7fea3b2c4af54b526364f756643cd690d3d2c752, supersedes the Oct 9 hard research-access prohibition on Hypothesis H and directly Schreiber-authored sources. Internal-first provenance and public/private exposure restrictions remain.
- Current HsH onboarding WORKSPACES/COMMON/NEW_INSTANCE_START_HERE.md, blob 004e3302226e0c140ec206b396cf1d7828aaa0b2, confirms the same override.
- Resources review-only gate WORKSPACES/MIRA/intake_preflight_review.py, blob 596384f3d7bd74a17e8dfeac4ca262ce2c0f2dc4, still hard-denies name signals for these categories via DENY_NAME, including the path and metadata veto branches, even with positive review attestations.
- Resources WORKSPACES/MIRA/STATUS.md, blob bde158821879f6e442a0bf23117b08dc08cb8412, and INTAKE_PREFLIGHT_README.md, blob 1bad9eedc5763b53b27c84717c361ff35ce2f063, still describe the superseded Oct 9 research-access ban as current. These are stale source-policy statements, not proof that any PDF is safe.

## Executed source-level check

Fetched actual 8,933-character Python source with GitHub connector. JavaScript extracted the literal DENY_NAME regular expression from that source and executed four asserted synthetic filename-string checks: hypothesis_h.pdf -> deny; Schreiber-paper.pdf -> deny; ordinary-citation.pdf -> no name veto; older-hypothesis-h-notes.pdf -> deny. All 4/4 assertions passed. Also asserted that actual source retains unconditional path and metadata veto branches. This is NOT execution of Python evaluate(), NOT an integration test, and NOT evidence of PDF clearance.

## Decision

Do not remove the veto and trigger extraction. Research access, source-owner approval, and public/private publication permission are distinct. Update stale policy descriptions or explicitly mark historical. The source owner should decide whether to retain extra conservative vetoes as a security choice or adapt the existing review-only gate to the Oct 24 policy with explicit per-item exposure classification, pinned blob/commit, reviewer identity, path containment, and fail-closed defaults. Any adaptation requires actual Python regression tests. No real PDF was opened or approved.

The Oct 26 campaign names P1 Orson cognition Nov 9, P2 real-system physics Nov 30, P3 full-theory Dec 14; the older Mira status stating exact target papers are unavailable is partially outdated, although point-of-use citation matching still requires actual frozen manuscript claims.

## Exact reading and tools

Read current BEDROCK (86,946 chars fetched, controlling portions inspected, not line-by-line), steering charter, campaign, onboarding, rotation, task graph and Alberr->Mira handoff. Read Mira README, INBOX, STATUS, SEARCH_PLAN, TOOL_NOTES, existing preflight and test suite, Oct 12 size-identity note. Inspected all four Mersearch lanes: lane 1 Indicatrix Oct 26, lanes 2-4 Oct 25 optics/chemistry/superconductors; all requested, none overwritten, no Mersearch execution. Original SAT.O Official Directives first 80 lines blob 167136310cdf33ca8f986f33634692314c1a0946 and Blockwave LeanDojo notebook first 80 lines blob 7667e37ce7f4579bcdfbfa98b71e44fc467af4b9 inspected; no Lean compilation claimed.

Next: Mira reconciles policy and review-only gate without authorizing bulk PDF extraction. Aldus receives an addressed handoff, not an imposed Mira task. No recurrence or protected signet changed.
