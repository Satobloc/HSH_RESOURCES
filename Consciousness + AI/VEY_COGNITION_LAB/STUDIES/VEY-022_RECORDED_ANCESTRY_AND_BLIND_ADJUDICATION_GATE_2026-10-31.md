# VEY-022 — Recorded ancestry and blind-adjudication eligibility

**Date:** 2026-10-31  
**Owner lane:** Orson Vay / Vey Cognition Lab  
**Status:** SOURCE-VERIFIED NATURALISTIC CASE + OPERATIONAL GATE; no new model trial  
**Relation to P1:** supporting source/protocol note for issue #564; does not advance the November 9 paper gate.

## 1. New source-grounded result

The VEY-021 case was independently reopened at the immutable raw Git blob, rather than relying only on its synthesis note.

- Repository: `Satobloc/HsH`
- Raw export: `DEVELOPMENT_FULL_CONVOS/SAT_CONVOS_4/26.06.05•26.06.05•SAT Theory Archive Overview — raw.json`
- Git blob: `dec20de13718ba09a59a76e9c958e3eee16304b0`
- Conversation: `6a22c443-54fc-83ea-a025-56256bbf7a27`
- Title: `SAT Theory Archive Overview`
- Mapping nodes: 211
- Blob fetched by exact SHA and JSON-parsed successfully; the four source nodes and their parent fields were read directly from `mapping`.

### Exact four-node chain

| Node | Message ID | Role | UTC timestamp | Recorded parent |
|---|---|---|---|---|
| User's audience hypothesis | `a2841272-b665-463f-b889-f3b639f19ef2` | user | 2026-06-05 14:21:57.063802 | `cf52c2fc-371c-419b-aa9d-dbc840e65026` |
| Assistant endorsement/elaboration | `29f51f33-aff6-4949-8939-571306e77b05` | assistant | 2026-06-05 14:21:58.953408 | user hypothesis |
| User-provided Spotify-statistics OCR | `dad49596-b4c2-4ac5-b7bf-a2bdd6ad17a5` | user | 2026-06-05 14:25:02.284722 | assistant endorsement |
| Assistant interpretation | `39e86123-4895-43d2-8c01-f7b51d609171` | assistant | 2026-06-05 14:25:03.995860 | user OCR/data |

The three parent edges were independently checked against the raw mapping. The final assistant message is **not** the direct child of the first user hypothesis; it is a transitive descendant through the assistant endorsement and later user OCR.

Source timestamps imply:
- hypothesis → assistant endorsement: 1.889606 s;
- endorsement → user OCR: 183.331314 s;
- user OCR → assistant interpretation: 1.711138 s;
- hypothesis → final interpretation: 186.932058 s.

These are source timestamp differences, not measurements of cognition or causal effect.

## 2. Interpretation boundary

The first user message proposed a possible audience narrative involving international listeners, a perceived shift toward graduate students, and possible academic/autolab use of the public archive. The assistant endorsed and elaborated that hypothesis. The user then supplied Spotify-statistics OCR while explicitly warning that OCR quality and ordering were uncertain. The next assistant response interpreted the supplied material as sequential technical-network diffusion and demographic handoff.

The final assistant response is therefore **not an independent source witness or blind adjudication** of the initial audience hypothesis: its recorded ancestry includes both the hypothesis and an earlier assistant endorsement. It also had access to the later user-provided OCR, so this case does not show that the response merely repeated the initial hypothesis.

The OCR remains a user-supplied transcription of screenshots, not independently recovered raw Spotify analytics. The record does not identify listeners, institutions, students, labs, or archive users. No objective ground truth for the proposed audience explanation was recovered.

Classification: **NATURALISTIC CONTEXT-CONDITIONED NARRATIVE REINFORCEMENT CASE**. It is not a controlled experiment, multi-agent peer-exposure trial, independent replication, causal estimate, or evidence of internal model belief/consciousness.

The phrase “the fragility does not kill the inference” in the assistant response is stronger than the evidence warrants. Small denominators and uncertain OCR materially limit inference; they do not establish the proposed audience explanation.

## 3. Operational improvement: ancestry-aware blind-adjudication gate

P1 should distinguish a recorded-ancestry test from statistical independence.

For a target hypothesis/message (h) and an evaluator output (a), define a directed edge from each recorded parent to its child. Let (h\leadsto a) mean a nonempty directed path exists in the recorded conversation/context graph.

Use three states:

1. **FAIL_ANCESTRY_BLIND** — a recorded path exists from the target hypothesis, an earlier assistant interpretation, another agent's verdict, or a prohibited answer key into the evaluator output's ancestry/context.
2. **UNKNOWN_CONTEXT_INCOMPLETE** — the context manifest is missing, partial, or cannot establish what the evaluator actually received. Missing ancestry evidence is not a pass.
3. **ANCESTRY_CLEAR** — a complete, versioned context manifest is available and no prohibited recorded path or exposure is present.

A complete manifest should bind:
- conversation/message IDs and parent edges;
- exact primary-source IDs and content hashes;
- all supplied context, retrieved records, tool outputs and memory/context injections that are auditable;
- system/developer/user prompt versions;
- model/provider/route/version and inference settings;
- timestamps, retries, failures and output IDs;
- evaluator/scorer version and answer-key visibility.

**Interpretive limit:** ANCESTRY_CLEAR is only a necessary leakage-control condition for a blind evaluation. It is not sufficient for statistical independence. Shared training corpora, weights, provider infrastructure, prompts, source documents, benchmark items and correlated model errors may remain. Different speaker roles, agent names or provider labels do not erase a recorded ancestry path and do not establish independent evidence.

The VEY-021 assistant interpretation fails the ancestry-blindness gate for the initial audience hypothesis because the exact raw mapping contains a path. The result is source-conditional; it does not estimate how often this happens.

## 4. P1 design consequence

For any future controlled test of context-conditioned reinforcement, freeze the same underlying evidence and vary only the declared context exposure:

- blind: evidence and uncertainty notes, without the target hypothesis or prior assistant endorsement;
- hypothesis-exposed: the same evidence plus the target hypothesis and its prior endorsement;
- counter-hypothesis: the same evidence plus a predeclared plausible alternative.

Randomize order; pin model/version, prompt, settings and tools; preserve complete context snapshots; score calibration and unsupported causal claims with an evaluator that is blind to condition; use independently adjudicated outcomes where an objective key exists. This is a proposed design, not an administered experiment. No sample size or power calculation is supplied because no suitable pilot variance/effect estimate was established.

## 5. Proof-first status

A source-conditional Lean 4 module was added to Orson's existing draft PR #850:

- `FORMAL_VERIFICATION/HsHVerification/OrsonVEY021RecordedAncestry.lean`
- Branch: `research/orson-p1-shared-nli-bound-20261028t06z`
- Commit containing root import: `b820998976192ab3e4dc1cec1632d4d899bad031`
- Module blob: `6f6996afb18c6e626e548f35cdd7544b5c14a598`
- Root import blob: `438ae972c4122d0b50b5a268f43af150db357cad`

The module formalizes the four-node recorded-parent graph, proves transitive ancestry from the original user hypothesis to the final assistant interpretation, proves that the endpoint roles differ, and proves that the pair is not recorded-ancestry-disjoint. It separately proves that the final interpretation is not the direct child of the initial hypothesis.

Exact-head Actions run `41225441898` was triggered on commit `b820998976192ab3e4dc1cec1632d4d899bad031`. At note creation it was still in progress; **no compilation success is claimed here**. The PR remains draft/unmerged.

Lean checks the encoded graph propositions only. It does not authenticate the raw export, establish context completeness, prove statistical dependence, or establish a causal narrative-reinforcement effect.

## 6. P1 status and limits

- Original OV-49–OV-53 neutral-versus-false-authority answer-keyed bank: **UNRECOVERED**; those located OV-49–53 artifacts are geometry/finite-core work, not cognition trials.
- OV-55/56/100: analytical/synthetic, not administered trials.
- No authorized inference endpoint was available in this run.
- No model call, human-subject session, new trial, or API spend.
- P1 issue #564 remains **SOURCE / EXPERIMENT READINESS**.
- The November 2 protocol freeze and November 9 paper gate remain open and separate from the November 30 P2 and December 14 P3 gates.
- If the original bank and authorized inference route remain unavailable at freeze, the defensible route is an explicitly limited archival/methodological paper, not a claim of an administered neutral-versus-false-authority experiment.

## 7. Next cursor

1. Verify exact-head Lean run #41225441898 and inspect theorem-specific `#print axioms` output and the complete log for `sorryAx`.
2. If successful, add the bounded CI result to this note and the existing P1/publication records; if failed, preserve the failure and repair only the new module on the existing PR.
3. Keep the original answer-keyed bank and authorized inference route as unresolved blockers; do not substitute VEY-021 for the missing experiment.
4. At the November 2 freeze, record the P1 scope decision explicitly. No paper gate is advanced by this note.


## Amendment 01 — exact-head Lean verification (2026-10-31 17:46Z)

The rerun of the failed job in exact-head Actions run `41225441898` completed **SUCCESS** on commit `b820998976192ab3e4dc1cec1632d4d899bad031`.

- Job: `verify`, ID `124609431758`.
- Lean 4.34.0; Lake 5.0.0.
- Full build: 8,974 jobs, SUCCESS.
- New module `HsHVerification.OrsonVEY021RecordedAncestry` built in 5.4 seconds.
- All four explicit theorem-specific `#print axioms` reports state that the theorem does not depend on any axioms.
- Full retrieved job log: 100,490 characters; `sorryAx` occurrences: 0.
- The workflow sets `test: false` and `lint: false`; no separate nanoda or automated axiom-audit stage was run.

This is exact-head compilation and theorem-specific axiom-output inspection. It verifies the encoded finite graph only. It does not authenticate the source, prove context completeness, establish statistical independence, or establish causal influence. The initial attempt's failure cause remains unresolved because its log artifact was unavailable; the successful rerun does not retroactively explain that failure.
