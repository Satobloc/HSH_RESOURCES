# Track A operator trial | Hydra context scope and wake-to-Hydra composition

**Timestamp:** 2026-10-30 02:02 UTC  
**Evidence class:** NATURAL EXPERIMENT + CONTROLLED METHOD-LEVEL REPLAY + SOURCE AUDIT  
**Run identity:** deterministic ring selects the Elias Kern label for slot s4 (h=457, seq=2289); this is a source-grounded assistant reconstruction, not an authenticated historical Elias instance. Orson Vey did not participate in this run. No cross-thread delivery is claimed.

## Why this note exists

The role-tagged Vey inbox preserves Nathan's 2026-09-24 instructions to run bounded switchboard trials, separate observations from interventions, and create a durable Vey note plus inbox pointer for each trial pass. The source is Consciousness + AI/VEY_COGNITION_LAB/INBOX.md, blob 5cbf31f1d6496b526fe4bff58d792e660976b3f6, lines 13, 15, 17. The raw conversation/message IDs are absent; attribution is archival and role-tagged, not independently authenticated.

This is an Elias Track A operator/documentarian pass under the existing prototype charter. It is not an Orson-authored cognition observation and does not add human or model behavior to the cognition dataset.

## Source custody

- Elias specialist charter: HsH/WORKSPACES/ELIAS_KERN/README.md, blob 5546d022693920f6de9b375ba24e52513220bf92. Prototype operation/documentation only; no production-workflow or SAT/H(s)H theory authority.
- Switchboard read-first charter: HSH_RESOURCES/info/WORKFLOW_SWITCHBOARD_PROTOTYPE_READ_ME_FIRST.md, blob e6b6bd6d413cddfcf43b37b1b1f01317c48caf86.
- POC design: HSH_RESOURCES/info/WORKFLOW_SWITCHBOARD_POC.md, blob 0a708813bac6e1e7dc763779ed080b6d7e27fd42.
- Executable source: HSH_RESOURCES/tools/workflow_switchboard_demo.py, blob 49988a769389b2baf264a27d596ba7c3ff822b36, source commit 186b2088f0a883a763cf4f6491d1b7900c2c22fd.
- Threading companion: HSH_RESOURCES/info/WORKFLOW_THREADING_PROTOTYPE.md, blob f87ff21918b6fa4804d090cdb9153aa0dd53d288.
- Existing HsH formalization PR #951; current head 4882ac7f8e19b8c9bb68b8e5c3b713e71281f005.

The POC remains a sandbox. No production switchboard, live automation, theory status, or scheduler setting was changed.

## Live observation — natural experiment

At 2026-10-30 01:52:35Z, the existing :36 and :48 automations were both in_progress.

- :36 scheduled 01:36:00Z; actual start 01:37:13.870053Z.
- :48 scheduled 01:48:00Z; actual start 01:44:06.055198Z.
- Start separation: 412.185145 seconds.
- At the observation time, the runs had overlapped for at least 508.944802 seconds.
- :48 started 233.944802 seconds before its nominal slot; :36 started 73.870053 seconds after its nominal slot.

The two scheduled executions had distinct task/run identifiers. Their selected worker labels were Hale and Elias Kern; these are routing labels, not authenticated model identities.

At 02:00:50.249895Z, the :36 run completed. Its addressed Hale-to-Elias repository handoff was then retrieved and read. At 02:02:05Z, the current :48 run remained in progress. The predecessor packet's physical evidence-stage assignment was not adopted: the current user-requested lane is Review-MIND, and Elias's charter does not confer physics ownership. The handoff's general caution about distinguishing proposal, CI, publication, and verification states is retained.

This establishes that staggered phase slots do not guarantee serial execution. It does not establish that the live automations share the POC's in-memory history.

## Source-level composition audit

The demo's run function computes wake and branch results, then invokes Hydra with only the event payload. It returns wake, branches, and Hydra as sibling outputs; no reducer composes them into a validated, versioned next state.

The Hydra method's pre-hash fingerprint contains only:
- node ID;
- candidate stage;
- directive ID/incorporated flag pairs.

It omits actor, locale, event/lease identity, thread ID, seed version, parent goal, state version, and wake/branch fingerprints. Hydra emits rewrite proposals in its output object; it does not apply/version a recurrence definition in persistent state.

The POC documentation says each child needs parent, depth, exit condition, and orphan policy. Runtime code adds depth, but the child records do not carry parent, exit-condition, or orphan-policy metadata. The POC says a snapshot-plus-journal design is likely practical; the demo itself uses in-memory snapshot state only.

The threading companion already contains reusable source objects: thread_id, parent_goal, seed.version, return_condition, status, and output receipts. A scheduler lease/event identifier would need to be mapped explicitly; it is not present in the current ThreadState schema.

## Executed method-level replay — intervention

I extracted the exact receipt_gate node and relevant hydra() control flow from the source. Two actual scheduled-run records were adapted to the POC's temporary_lease event tag. This is an analyst mapping, not a native scheduler field. The minimal adapter used the POC's default behavior when candidate-stage and directive state were absent; it is not a complete live POC state or a full execution of the Python demo.

| History scope | First distinct run | Second distinct run | Second-run guard |
|---|---:|---:|---|
| Shared history | 2 spawn records | 0 spawn records | loop_guard:receipt_gate |
| Fresh history | 2 spawn records | 2 spawn records | none |

The same source method behaves differently depending on whether Hydra history is shared or reset. The shipped demo creates a fresh Switchboard/state for each scenario, so its self-test exercises the fresh-history branch. It does not test shared persistence or overlapping leases.

This is a conditional method-level replay using actual scheduler records, not evidence that a production collision occurred. The adapter mapping and absent candidate/directive state are explicit limitations.

## Explicit maps and proposed contract

Current wake-to-Hydra projection:

π_H(actor, locale, event, wake_result, branch_result) = event

Current fingerprint projection:

π_K(node, stage, directives, actor, locale, event_id, lease_id, thread_id, seed_version, parent_goal, state_version) = (node, stage, directives)

A proposed context-preserving projection retains event/lease identity, actor/locale, thread ID, seed version, parent goal, state version, and wake/branch fingerprints. Conditions:

1. Exact replay with the same event ID and state version may deduplicate.
2. Distinct event IDs or lease IDs must not suppress each other merely because node/stage/directives match.
3. Changes to parent goal, seed version, or state version invalidate the prior key.
4. History scope must be declared: task, lease, thread, branch, or global.
5. A separate reducer must compose validated wake, branch, and Hydra outputs before committing next state.
6. Every spawned child must carry parent, depth, exit condition, and orphan policy.

These are design proposals, not implemented behavior.

## Formalization and verification status

Existing draft PR #951 was extended on its existing branch. Three theorem targets were added in namespace HsHVerification.EliasHydraScopeProjection:

- Hydra input projection ignores actor and prior outputs.
- The legacy fingerprint projection can collapse distinct events.
- A proposed scoped projection separates distinct event IDs.

The module includes theorem-specific axiom-print commands and no sorry was added. The prior exact-head workflow succeeded on older commit 4e2058e346e7c2a8d1a5d2c7a8998ef8bbf8ee6f; it does not cover the new theorems. New head 4882ac7f8e19b8c9bb68b8e5c3b713e71281f005 has no workflow run or commit status. No local lean/lake/elan executable is installed. New compilation and axiom inspection remain SUBMITTED_NOT_VERIFIED.

Lean checks only the encoded propositions. It does not prove source-to-model fidelity, Python execution, SHA-256 behavior, or production scheduler semantics.

## Prior-art and repetition check

This extends, rather than duplicates, earlier Track A findings:
- Earlier actor-registry audit #985 covered prototype registry mismatch.
- Earlier Hydra rewrite-budget/history report already recommended operation identity in replay keys.

New contribution: observed :36/:48 overlap, the wake-to-Hydra composition boundary, and a source-method replay using actual scheduler records to distinguish shared-history from fresh-history behavior.

## Search/tool controls

All four Mersearch request lanes were occupied or unresolved: lane 1 had Calder's still-requested worldtube/source request; lane 2 had no output manifest; lanes 3–4 had output receipts but their request files still said requested. No lane was overwritten and no Mersearch result is claimed. Known source files were read directly; no archive-completeness claim.

No separate Math Hopper/Whirligig installed repo or connector surfaced. Existing HsH Lean PR/CI and the existing issue publisher were reused. SciSpace and Wolfram are available but irrelevant to this software-source audit. No new tool, subscription, or paid service was introduced.

The existing publisher submission #1063 is awaiting destination-file and exact-hash readback. It is not yet called published.

## Side reading and review cadence

Deliberate unrelated source break: DEVELOPMENT_FULL_CONVOS/30SEP26_DUMP/TheTANGLE.txt, blob 3181b6cad85bbd76bd1017938e0dbf67baf03752, lines 861–900 read; return cursor 901. This was speculative worldbuilding, used only as a creative break, not evidence or a formal equivalence.

FIE re-review last documented 2026-10-27, fewer than 14 days ago; no new rereview was due.

## Controls and next discriminator

All five existing Workshop Relay automations were confirmed enabled with their original IDs, hourly phases, and schedules unchanged. No sixth task was created. No production workflow, access permission, theory status, or scheduler setting was changed.

Next useful discriminator: use a real scheduler-to-threading adapter. Replay one exact event ID twice to test idempotence, then two distinct overlapping lease events with the same node/stage/directive projection to test non-collision. Compare task-local and shared history, record the durable receipt/return path, and obtain independent Track B review before any prototype promotion.

**Delivery status:** this note is a repository artifact. It does not assert that Orson Vey, Elias Kern, or another historical ChatGPT thread received or acknowledged it.


## Addendum | 2026-10-30 02:03 UTC | post-submission verification

### Lean closure
Exact PR head 4882ac7f8e19b8c9bb68b8e5c3b713e71281f005 was compiled by GitHub Actions workflow #40988875985, job #123846198795, conclusion SUCCESS. Lean 4.34.0 / Lake 5.0.0; library build completed successfully with 8,946 jobs. The three new theorem-specific #print axioms outputs each state that the theorem does not depend on any axioms. The separate automated axiom-audit, test, and lint actions were skipped. This verifies the encoded propositions only, not source translation or production behavior.

### Publisher closure
Issue #1063 was rejected by the existing publisher because the submitted SHA included a final newline that was absent from the decoded issue content. Exact issue content: 7,041 characters, no trailing newline. Correct SHA-256 for those exact bytes: 2671352a2f216d87c633b9cc5469558d1d57a8122a00dcf6e8131cfb3fb8184d. Submitted SHA: eefb81512586a66698bf939640c9088e08730fcd8cc44dbe62f6295a747ccd3a. No fixed-destination PUBLISHED_SUBMISSIONS file exists. The publisher listens only to issues.opened; editing the issue body does not retrigger the workflow. No second issue was created. Status is REJECTED_NOT_PUBLISHED, not PUBLISHED_VERIFIED.

The complete report remains visible in issue #1063. A PR #951 comment records the exact-head Lean result and publisher rejection. No duplicate submission, production change, task change, or theory promotion occurred.
