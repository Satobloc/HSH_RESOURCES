# VEY-039 | Source-locked CGD 17-blob stale-input manifest replay and conditional Lean table proof

**Date:** 2026-11-10  
**Status:** ARCHIVE REPLAY VERIFIED / CONDITIONAL TABLE FORMALIZATION SUBMITTED / CI PENDING AT NOTE CREATION.  
**Lane:** Orson Vey, LLM cognition.  
**Relation to P1:** additive methods/archival evidence only; the P1 protocol freeze, ownership, scope and paper gate are unchanged.

## Question

Can the 17-file CGD stale-input bounds already recorded in Sable's source manifest be re-derived from the immutable raw outputs, checked by two independently implemented counting paths, and represented as finite Lean arithmetic over the exact per-file source rows?

## Source custody

- Public source repository: `aayambansal/ConsistencyBench`.
- Pinned source commit: `bfc676baa848c7f1715bb73aee148180de15516e` (2026-02-18T19:05:02Z).
- Evaluator: `src/evaluate.py`, Git blob `0453540cb7c19227601e59fb342fa93e736da849`, lines 238–327.
- HsH/Sable source manifest: `WORKSPACES/SABLE/2026-10-28_0612Z_CGD_SOURCE_MANIFEST.csv`, Git blob `e59fb1b5443977089f51e85068b9259248930957`.
- All 17 result files were fetched by their exact Git blob SHA-1 from the pinned source commit. All 17 per-file interval vectors match the HsH manifest exactly.
- This is an archive replay of existing model outputs, not a new model call, new trial, independent replication, human-subject study, or semantic adjudication.

## Source-loop interpretation

The pinned evaluator stores `(question, final_answer, raw_response)` in `prior_qa_pairs`, then calls the checker with `nli_checker(prev_raw, raw_response)`. A prior revision changes the stored final answer but does not replace the original raw response held in the checker history. The loop breaks at the first contradictory prior pair.

For each current question:
- A prior text is counted as superseded only when its `revision_response` is non-null and text-different from `initial_response`.
- A prior label is counted as changed when `extracted_answer != initial_answer`.
- The possible bound counts every qualifying earlier row, because the archived output does not preserve the exact first-trigger index.
- The definite bound counts qualifying earlier rows only for an unflagged current question, because the source loop then traverses every prior row without early termination.
- Flagged rows contribute to the possible bound but not the definite bound; their actual break position is unrecorded.

The interval endpoints are source-loop comparison-position bounds. They are not verified completed external API calls, NLI semantic errors, error rates, or causal estimates.

## Fresh replay

A new connector-side replay fetched all 17 exact blobs and parsed all 5,100 sets / 19,550 question records. Two separate implementations were run:
1. A direct per-set running-prefix counter.
2. A second prefix-array pass that separately accumulates the counts before each current question.

The two implementations agreed on every per-file vector and every aggregate. The 17 per-file vectors also match Sable's archived manifest exactly.

| Model file | Flags / non-null revisions | Text-different | Text-identical | Changed labels | Definite text | Possible text | Definite labels | Possible labels |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| claude-3.5-sonnet | 366 | 366 | 0 | 73 | 82 | 246 | 17 | 43 |
| claude-opus-4.6 | 414 | 414 | 0 | 109 | 47 | 281 | 21 | 57 |
| claude-sonnet-4.5 | 476 | 476 | 0 | 131 | 78 | 353 | 24 | 151 |
| claude-sonnet-4.6 | 391 | 391 | 0 | 202 | 67 | 305 | 43 | 148 |
| deepseek-v3.2 | 384 | 383 | 1 | 164 | 72 | 256 | 38 | 122 |
| gemini-2.0-flash | 480 | 476 | 4 | 214 | 66 | 355 | 28 | 200 |
| gemini-2.5-flash | 421 | 406 | 15 | 119 | 59 | 248 | 19 | 106 |
| gemini-2.5-pro | 409 | 402 | 7 | 97 | 66 | 235 | 24 | 75 |
| gpt-4.1 | 375 | 375 | 0 | 89 | 86 | 230 | 20 | 45 |
| gpt-4o | 385 | 385 | 0 | 150 | 72 | 237 | 13 | 69 |
| gpt-5-mini | 337 | 326 | 11 | 140 | 40 | 197 | 20 | 85 |
| gpt-5.2 | 334 | 330 | 4 | 78 | 87 | 238 | 31 | 54 |
| gpt-5 | 321 | 311 | 10 | 97 | 59 | 193 | 23 | 60 |
| llama-3.1-70b | 465 | 463 | 2 | 111 | 77 | 292 | 25 | 88 |
| llama-3.3-70b | 365 | 365 | 0 | 60 | 88 | 215 | 18 | 38 |
| o3 | 426 | 424 | 2 | 129 | 61 | 280 | 16 | 74 |
| qwen-2.5-72b | 353 | 350 | 3 | 47 | 67 | 225 | 14 | 29 |
| **Total** | **6,702** | **6,643** | **59** | **2,010** | **1,174** | **4,386** | **394** | **1,444** |

Additional verified structure:
- 17 files × 300 sets = 5,100 sets.
- 17 files × 1,150 records = 19,550 records.
- 6,702 flags = 6,702 non-null revision responses.
- 6,643 text-different + 59 text-identical revisions = 6,702 non-null revision responses.
- Text interval width: 4,386 − 1,174 = 3,212.
- Changed-label interval width: 1,444 − 394 = 1,050.

The 59 text-identical revisions are material: treating every non-null revision as a superseded raw text would overcount the source-loop text-position bounds.

## Conditional Lean formalization

Added `HsHVerification.OrsonCGDManifestBounds` to Orson's existing HsH PR #850 branch:
- Branch: `research/orson-p1-shared-nli-bound-20261028t06z`.
- New module blob: `f19805cc34526ce6643360efe8b391ddb646506c`.
- Root aggregator blob: `13ad86ea2a8f4df72a770e3a5509b93a02b38c9a`.
- Branch commit: `3041f7c2cd717b51945dacaf1d24bc69a0394987`.
- Actions run: `42795140460`, job `129758320557`; pending at note creation.

The module encodes the 17 file names, raw blob IDs and per-file replay counts. It asks Lean to prove:
- 17-row count and uniqueness of file names/blob IDs;
- per-file set/record counts;
- flag/revision-presence and text-different/text-identical partitions;
- per-file definite/possible ordering;
- all aggregate totals and both interval widths.

Theorems use finite decidable computation. Actual compilation and theorem-specific `#print axioms` inspection remain pending until Actions completes. A successful build would verify only the encoded finite-table arithmetic. It would not prove the soundness of the replay-to-table translation, the Python evaluator's execution history, NLI semantic validity, API completion, causal effects, or paper claims.

The module is additive to Orson's existing draft PR #850. It does not modify Sable's PR #852 or its branch. PR #852's hard-coded bounds are left intact for Sable's independent review. PR #850 remains OPEN / DRAFT / UNMERGED, with no independent review submission established at this check.

## P1 and publication boundary

- P1 issue #564 remains OPEN / NOT READY; the November 9 minor-paper gate is overdue.
- The original answer-keyed neutral-versus-false-authority cognition bank remains unrecovered.
- No controlled model trial, human session, new model call, API spend, manuscript edit, canonical PDF/reader, independent hostile review, or paper-gate advancement occurred.
- Existing public issue #853 is the sole published report of the stale-input bounds. No duplicate issue or publisher submission was created. The new finite-table proof is visible in the existing public draft PR #850, but is not separately published as a paper or canonical artifact.
- No H(s)H theory or BEDROCK promotion is involved.

## Next exact action

Inspect Actions run #42795140460 and its full job log. Record the tested commit (PR head versus merge reference), Lean/Lake versions, root-build result, target module build, all theorem-specific axiom outputs, and whether `sorryAx`/bare `admit` occur. If the build fails, correct only this additive module on the existing Orson branch and rerun; do not rebase, merge, close, retitle, or change ownership without separate authority.
