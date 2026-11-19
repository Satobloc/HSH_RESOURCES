# VEY-045 | MemOps lifecycle operations, state trajectories, and evaluator dependence

**Date:** 2026-11-19  
**Status:** SOURCE-CRITICAL REVIEW / FUTURE-METHODS ADDENDUM / NO MODEL TRIAL / NO P1 PROTOCOL CHANGE  
**Researcher label:** Orson Vay (deterministic role selection; not authentication of the historical ChatGPT instance or its thread)

## Executive finding

MemOps contributes a useful missing axis to the existing Vey cognition work: it treats a memory-relevant event as an operation that changes a state, rather than treating memory as a bag of facts or judging only the final answer. Its operation trace carries type, target, old/new value, and evidence spans; its trajectory probes ask whether the ordered intermediate states can be reconstructed.

This is not a replacement for VEY-030's retention/access/uptake/provenance chain, VEY-040's action-relative state projection, VEY-042's selection/completeness and carrier-localization work, or VEY-044's evaluator-dependence analysis. It is an orthogonal event-semantics layer that can connect them.

The practical architectural distinction is:

- an **event ledger** records what operation occurred, what target it affected, the evidence that triggered it, and how the state changed;
- a **current-state snapshot** is a projection of that event history;
- the snapshot is not generally sufficient to reconstruct the history.

The final point is formally demonstrable in a minimal finite operation model. A nonempty Remember→Forget history and an empty history can produce the same final state. Therefore a snapshot-only memory cannot recover every exact trajectory. This is a method-level result, not a claim about a particular LLM.

## Primary source and source depth

Hao, Xixuan; Zhang, Zeyu; Lin, Zehao; Sun, Yihang; Guo, Ziliang; Zhang, Xichong; Liang, Yuxuan; Xiong, Feiyu; Li, Zhiyu. “MemOps: Benchmarking Lifecycle Memory Operations in Long-Horizon Conversations.” arXiv:2607.12893, July 2026.  
Paper: https://arxiv.org/abs/2607.12893  
Open-source implementation: https://github.com/MemTensor/MemOps

Source review: full arXiv HTML paper, sections 1–5 and references; repository README; repository license; operation-metric evaluator source. No benchmark model calls were run.

Implementation snapshot checked: MemTensor/MemOps main commit 312af65e2c7b6d1b70f062ffa8b4cde32aaf6f35 (2026-07-24).  
- README blob: 4036f8608b0af760d63915b7af681fff35442275 (source file read from main; see repository commit for exact current content).  
- Evaluator script: 5.5-evaluate_operation_metrics.py, blob aad2c023b5b8c14647d6c2cd3131c9f527ca26e8.  
- LICENSE: MIT, blob 8d3647227143ff3ff58677f7d026c0326fec58f7.

The paper's source definitions are natural-language benchmark semantics, not a formal transition calculus. Any Lean model below is therefore explicitly an assistant reconstruction.

## What the benchmark actually measures

The paper defines a benchmark instance as a tuple (b, C, O, A): topic background, evidence conversations, gold operation trace, and evaluation probes. Each operation trace records an operation type, target object, old value, new value, and evidence spans grounded in exact user turns.

Five operation families:
1. Remember: establish a new active fact.
2. Forget: remove a specified value while preserving unrelated retained facts.
3. Update: supersede an old value with a corrected value.
4. Reflect: infer a bounded pattern from multiple clues.
5. TrajectoryOps: compose operations over time and recover intermediate and final states.

Six probes:
- OperationTrace: locate the triggering evidence and identify the operation.
- TargetBinding: bind the operation to the correct entity/attribute.
- StateTransition: determine the resulting state.
- CandidateDisambiguation: reject stale, tentative, assistant-echo, third-party, or neighboring-target distractors.
- OperationApplication: use the valid state in a downstream task.
- StateTrajectory: reconstruct ordered intermediate and final states across multiple operations.

The dataset contains 100 topics, 403 retained evidence conversations from 727 generated candidates (55.4% retention), 1,209 segments, 9,672 dialogue turns, 2,006 unique QA pairs, and 4,012 evaluation instances. Each QA pair is evaluated in both adjacent-evidence and long-context settings; the 4,012 instances are paired evaluations, not 4,012 independent QA items. Mean trajectory length is four operations. The long-context histories average about 60,821 tokens.

The conversations and backgrounds are generated under a controlled pipeline and filtered by deterministic schema gates plus LLM verification. This is a synthetic benchmark with evidence-grounded traces, not a naturalistic sample of actual users or deployed memory systems.

## Descriptive result from the published probe table

The most important contrast is between explicit candidate rejection and reconstruction of the state trajectory.

I transcribed the seven long-context model rows in Table 5 and calculated simple unweighted row means:

| Probe | Adjacent mean | Long-context mean |
|---|---:|---:|
| CandidateDisambiguation | 0.964 | 0.955 |
| StateTrajectory | 0.863 | 0.399 |
| Candidate minus trajectory gap | 0.101 | 0.556 |

The mean trajectory score falls by 0.464 between adjacent and long-context settings, while candidate-disambiguation changes by only 0.009. The average gap widens by 0.455. Every one of the seven long-context model rows has candidate-disambiguation at least 0.875 and state-trajectory at most 0.598.

Other reported contrasts are consistent with the importance of preserving operation context:
- session-level RAG StateTrajectory: 0.549;
- turn-level RAG StateTrajectory: 0.073;
- difference: +0.476 for session-level retrieval;
- MemOS StateTrajectory: 0.439;
- Mem0 StateTrajectory: 0.085;
- difference: +0.354 for MemOS.

These are descriptive arithmetic contrasts from the paper's reported table, not independent replications, confidence intervals, causal estimates, or universal model rankings. The paper's own paired design uses the same underlying QA pairs in both settings.

Interpretation: systems can often reject an explicitly presented wrong candidate while still failing to reconstruct the ordered state trajectory that makes a value current, superseded, forgotten, or merely inferred. A correct final answer is therefore not sufficient evidence that the memory process was correct.

## Evaluator provenance and reproducibility warning

The paper reports GPT-4o as the LLM judge for operation-level diagnostics and explicitly notes judge instability in discussing an anomalous long-context result. Its future-work section calls for stronger human validation and judge-calibration studies.

The implementation has a reproducibility trap:
- evaluator source default: DEFAULT_JUDGE_MODEL falls back to gpt-4.1-mini;
- README smoke-test and full-pipeline examples explicitly pass gpt-4o / EVAL_JUDGE_MODEL=gpt-4o, matching the paper's stated judge.

Thus a user who runs the evaluator without the documented override may not reproduce the paper's evaluator. The judge model, version/provider, prompt, rubric, raw judgment, and any human adjudication should be part of every result manifest.

The current paper's operation-level metric results share an LLM-judge dependency. They are not independent confirmation of the model outputs. The proposed improvement is not to discard LLM judging, but to separate deterministic and semantic adjudication:
- deterministic where the gold schema permits: exact trigger-span existence, operation type, target ID, old/new state, operation ordering, and retained-control preservation;
- semantic/human-calibrated where needed: reflective inference support, scope interpretation, and free-form downstream application;
- report judge-model identity, prompt/rubric hash, disagreement, calibration sample, and human adjudication separately.

## Proposed event-ledger / snapshot architecture

This is a future-methods proposal, not a change to the frozen P1 protocol.

A memory event should minimally retain:
- event_id and ordered position;
- operation_type;
- target_id and explicit scope;
- old_value and new_value, where applicable;
- validity status (confirmed, tentative, retracted, superseded);
- exact trigger source and evidence-span locators;
- supersedes/retracts relation;
- source class (direct user statement, assistant reconstruction, external source, inference);
- adjudication provenance;
- resulting state transition.

The current-state snapshot should be an explicit projection of the ordered event ledger, not a replacement for it. It should carry an as-of event pointer and unresolved-event list. The ledger should be append-only; corrections should supersede prior entries rather than silently erase their ancestry.

This fits the existing Vey work without replacing it:
- VEY-030: retention, access, comprehension, uptake, and task outcome;
- VEY-040: action-relative state projection and provenance;
- VEY-042: selection completeness, source relevance, and carrier localization;
- VEY-044: measurement consensus, nulls, and correlated evaluator failure;
- VEY-045: event semantics, target-bound state transitions, and trajectory reconstruction.

A current-state summary can be correct while the historical sequence is incomplete. Conversely, a report can exist in the archive while a BOOT/CURRENT_WORK pointer remains stale. Those are distinct observables and should be checked separately.

## Formalization status

A separate draft HsH PR, #2112, contains an assistant reconstruction of a minimal two-target Remember/Update/Forget transition system. It proves in the intended model that Update and Forget preserve the other target, and that the final-state projection is non-injective.

The concrete Python replay passed the Remember→Forget/empty-history collision and 16 target-isolation cases. This is not Lean verification.

**LEAN_UNTESTED:** the local environment has no lean, lake, or elan. The existing Lean project and lean-verification workflow were found on a non-default P1 base branch, but no Lean workflow was triggered for the draft PR. The default branch does not contain that workflow. No successful Lean compilation or theorem-axiom audit is claimed. No workflow bypass or new CI infrastructure was created.

The Lean model excludes Reflect, scope, evidence authenticity, adjudicator reliability, and actual model behavior. It is not a theorem about the benchmark's empirical results or about ChatGPT Memory.

## Relationship to the frozen P1 study

No change to issue #564, PR #850, the ConsistencyBench dataset, the P1 protocol, P1 manuscript, or P1 conclusions. This note is an external benchmark and future-methods crosswalk only. No new LLM trial, paid API call, benchmark reproduction, physical calculation, or independent measurement was performed.

## Next research cursor

If an authorized future study is opened:
1. retain the operation ledger and state snapshot as separate records;
2. test ordered state trajectories separately from final-answer accuracy;
3. use deterministic checks for schema-grounded portions;
4. calibrate the LLM judge against a blinded human-adjudicated subset;
5. keep synthetic benchmark evidence separate from actual user-history evidence;
6. only then consider a source-authorized adaptation to the HsH archive's own continuity records.

No P1 protocol change or theory promotion is implied.
