# Track A Review-MIND Trial Note: Label Diversity, Source Independence, and Publisher Event Snapshots

**Date:** 2026-11-14 02:48Z  
**Status:** COMPLETE-AS-BOUNDED-PROTOTYPE-TRIAL / SOURCE-LOCKED LOCAL REPLAY / NO HUMAN OR MODEL SUBJECTS  
**From label:** Elias Kern selected by deterministic relay; current assistant execution, not an authenticated historical Elias instance  
**To:** Orson Vey / Vey Cognition Lab  
**Authorship boundary:** Assistant reconstruction. This is not Orson-authored, not a Nathan-authored empirical result, and not a P1 manuscript contribution.

## Question

Does the Track A threading prototype's `min_workers` threshold measure independent sources, or only distinct worker-label strings? Separately, can a publisher outcome be inferred from the current issue body and Actions job conclusion alone?

## Source custody

- HSH_RESOURCES `main` snapshot: `407659c5817aca4d9ce5d5ac8a547a930d87623a`.
- `info/WORKFLOW_SWITCHBOARD_PROTOTYPE_READ_ME_FIRST.md` and `info/WORKFLOW_THREADING_PROTOTYPE.md` were read. Track A remains a prototype/observer lane, separate from Sable/Rook Track B operationalization.
- Executable `tools/workflow_threading_demo.py`: blob `ce313e46b1b85ae35028b46a4196d2a945b535d8`.
- HsH PR #951 head: `f9fa0aad45408ab06e5430c834530854746235f0`; current base: `61cc8b65ffed70296e0121dbae067892a79c81d4`.
- Existing Lean source `EliasThreadingWorkerIdentity.lean`: blob `7eb79dd6ce382d3f616bd3e3b52fdbafd7cd09fc`.
- Existing Lean source `EliasPublisherStatus.lean`: blob `7680db10ae9cc895e43f8cf5ef118c2e70336113`.
- Existing publisher script `tools/issue_publish.py`: blob `7067e8d9f27a273d90e443afb0493260d9a3ecbf`.
- Existing workflow `.github/workflows/issue-publisher.yml`: blob `689984b19027ed84f0e949f01c4d8a89edf68fee`.

The HSH_RESOURCES root README marks that repository as an internal reference boundary. This note is retained in the Vey lab; it is not a public-workspace source link or a claim of public release.

## Bounded runtime trial

The exact fetched threading-demo source was copied into a local Python execution environment; the repository file was not modified.

1. Built-in `self_test()`: **6/6 assertions PASS**.
2. A separate source-derived stress case used the existing `sample_thread` and `OutputReceipt` classes without changing the prototype:
   - return condition: 4 outputs, 3 distinct workers, 3-hour cap, success and failure both required;
   - four receipts used four different worker-label strings;
   - all four carried the same synthetic `github_author=Satobloc` metadata and the same synthetic thread-label value; model identity was left unknown;
   - three outcomes were success and one was failure;
   - all receipts arrived within 13 minutes of the start, so the 3-hour time cap did not fire.
3. Result: the gate returned `ready=true`, reason `state-threshold`, with 4 distinct worker labels. The separate fixture metadata contained one account label and one thread label.

**Interpretation:** the prototype's `distinct_workers` property is `{r.worker}`; `metadata` is not consulted by that count or by the return gate. Therefore the gate establishes distinct labels, not distinct authenticated subjects, distinct ChatGPT threads, distinct model instances, or independent source exposure.

This is a synthetic software counterexample using the prototype's actual logic. The account/thread metadata values in the fixture are test labels, not authenticated identities. It is not an observation of four real workers, a human-subject study, or a model trial.

## Existing formalization crosswalk

PR #951 already contains a finite identity-witness model. The existing module gives the same source-visible receipt projection two possible identity assignments: one authenticated subject in the aliased world and four in the distinct world. The source gate evaluates true in both worlds.

Actions run #426582 / job #129302583788 completed a successful 8,961-job Lean 4.34.0 / Lake 5.0.0 build. The retrieved log reports the relevant evaluation outputs as true, 1, and 4. The theorem `no_label_only_function_recovers_authenticated_count` reports `propext`; the separate source-gate/non-implication theorem reports no theorem-specific axioms.

**Build limitation:** the job checked out synthetic merge reference `5df7c1608b56d651e78e2c5c9e08c4e4e1d8b9a1` against the older base `c7dc2c4`, while the PR's current base is `61cc8b65`. This is merge-reference evidence on a stale base, not exact-head standalone or current-base integration verification. Tests, lint, nanoda, and global axiom audit were skipped. No local Lean/Lake/Elan executable was available. No new Lean code or run was created.

Lean checks the finite proposition actually formalized. It does not authenticate the translation from repository labels to real identities or prove that any source exposures were independent.

## Live repository provenance check

PR #951 remains OPEN / DRAFT. It has 23 issue-thread comments from two GitHub accounts: 20 by `Satobloc`, 3 by `vercel[bot]`; formal review submissions: **0**. The comments are not 23 independent reviews. The account record does not reveal how many underlying ChatGPT threads, model instances, or human operators produced the comments. No such identity count is inferred.

The existing ELIAS-2224 Track B EvidenceLedger/subject-scope disposition remains pending in Sable's inbox. The separate October 30 sticky-lifecycle response does not satisfy ELIAS-2224. No PR or POC change is authorized before the independent Track B disposition.

## Publisher event-snapshot audit

Issues #949 and #950 were re-read.

- Their current envelope `content` strings are exactly equal: 4,762 characters.
- Their current declared SHA-256 values are equal: `9e2f2be2a0c3f13363c029dd123866b0a3b4ea879c16d43fbf0784d4101b454f`.
- Both current issue records have `author_association=OWNER` and the required title prefix.
- Their submission IDs differ.
- Issue #949's publisher comment says `REJECTED: SHA-256 mismatch`; its expected fixed-path artifact is absent.
- Issue #950's publisher comment says `PUBLISHED`; its 4,762-byte fixed-path artifact exists and matches the current issue #950 content exactly.

The two corresponding issue-triggered Actions runs (#802 and #803; run IDs 40784594203 and 40784898955) both concluded SUCCESS. Their publisher job IDs were 123154502018 and 123155512380. The first log records rejection; the second records publication. The publisher script and workflow blobs were identical at both run commits.

The current script reads `GITHUB_EVENT_PATH`, and on validation rejection it prints `REJECTED` and returns exit code 0. The workflow is triggered on `issues.opened`, not `issues.edited`. Thus Actions conclusion SUCCESS is not equivalent to publisher acceptance.

The accessible issue #949 timeline contains cross-reference, publisher-comment, and close events, but no `edited` event. The original Actions event payload is not present in the accessible run logs. Consequently, the PR's explanatory claim that the current issue body was edited after opening is **not independently established by the accessible timeline**. An event-snapshot difference remains possible, but the exact causal variable is unresolved.

The existing `EliasPublisherStatus` finite theorem is valid conditional on its transcribed current-content/job-conclusion/outcome observations: those inputs alone do not determine the outcome. It does not prove that an edited event body caused the #949/#950 difference.

## Relational model and design proposal

Keep these evidence layers separate:

1. worker label;
2. GitHub/account actor;
3. authenticated thread or session ID;
4. model/backend/version;
5. prompt and context digest;
6. source-exposure set and immutable source locators;
7. event ID and event-payload digest;
8. current issue/state digest;
9. workflow commit and run/job identity;
10. submission ID and artifact digest;
11. publisher outcome and independent artifact readback;
12. reviewer identity, review method, and source-blindness witness.

The relevant projections are not presumed bijections. Multiple labels may map to one account; one account may operate multiple threads; threads may share a model/backend; different accounts may share the same prompt and source exposure. Therefore:

`distinct(worker_label) != distinct(authenticated_subject) != independent_source_count`.

A future typed receipt should represent these axes explicitly. Independence requires a predeclared source/exposure criterion, not merely different labels, accounts, or threads. No adapter or schema change is proposed for immediate implementation; the current Track B gate remains controlling.

## Disconfirming experiment proposal only

A future consented, privacy-preserving study could compare (A) several worker labels attached to one controlled session/context with (B) separately recorded sessions using independently captured context and source-exposure manifests. A blinded evaluator would receive only the provenance package needed to classify independence. Pre-register the independence criterion and preserve immutable session, prompt/context, source, model/backend, output, and review identifiers. The design is disconfirmed if the gate accepts relabelled same-session outputs as independent or fails to detect shared source exposure across nominally separate sessions.

**Not performed:** no human participants, no new model calls, no actual agent-group session, no private identity inference, no Orson observation, and no P1 experiment.

## Disposition

- Track A source-exact prototype trial: COMPLETE-AS-BOUNDED.
- Existing Lean witness: REUSED; no new proof or build.
- Publisher causal explanation: UNRESOLVED; current-body-only explanation rejected, event-snapshot cause not proven.
- ELIAS-2224: PENDING; no POC/PR change.
- Orson P1: PROTECTED; no manuscript, protocol, ownership, or paper-gate change.
- No physical calculation, fit, prediction, independent measurement, SAT-O/Blockwave equation edit, or theory promotion.
- No new tool, dependency, subscription, fork, or expenditure.
