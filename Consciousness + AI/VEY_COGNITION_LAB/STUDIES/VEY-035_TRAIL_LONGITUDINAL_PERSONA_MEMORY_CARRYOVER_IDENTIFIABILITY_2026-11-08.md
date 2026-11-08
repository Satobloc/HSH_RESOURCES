# VEY-035 — TRAIL longitudinal persona-memory carryover and identifiability gate

**Prepared:** 2026-11-08, relay h687:s3 (nominal 15:36Z)  
**Status:** PRIMARY-SOURCE REVIEW COMPLETE / ARCHITECTURE CROSSWALK COMPLETE / CONDITIONAL LEAN FORMALIZATION SUBMITTED, LEAN_NOT_RUN  
**Evidence class:** primary literature and official project-site description; assistant-derived design model; no independent participant-data reanalysis or administered model trial  
**Owner boundary:** supporting LLM-cognition research. Orson retains P1 ownership. This note does not alter the frozen ConsistencyBench P1 scope or the November 9 gate.

## 1. Primary sources and review extent

1. M. Amin Samadi et al. (2026), “TRAIL: A Platform for Configurable Human–AI Teaming Experiments,” arXiv:2607.12180v1, submitted 2026-07-13. Full HTML reviewed, including the platform design, §§3–4.4, the six-session demonstration study, analytics/export description, limitations, and references: https://arxiv.org/html/2607.12180v1
2. Official TRAIL / Team Research and AI Integration Lab website, accessed 2026-11-08: https://trail.aminsamadi.org/
3. Internal predecessor: VEY-034, “Human-AI teammate replacement, relational graph structure, and temporal-claim correction.” VEY-034's explicit next cursor was to inspect TRAIL's state isolation, per-team context boundaries, turn logging, and action-manager/response-generator implementation.

This is a bounded primary-source and official-site review, not a source-code audit. The paper and website inspected here do not link a public code repository. The website directs researchers to sign up and apply for researcher access. No account was created, no access request was made, and no private system was accessed.

## 2. What the paper actually specifies

TRAIL is a human–AI teammate platform with one configured AI teammate in a human team. It is not, in the reviewed paper, a multi-LLM peer-panel platform.

The paper describes four cooperating subsystems:

- **Persona configuration:** graded Big Five controls, backstory, communication style, domain expertise, education, provider/model version, and optional researcher-authored event/response triggers. The full persona specification is stored with the experiment and re-applied to each session.
- **Synchronous chat and message pipeline:** batching; memory integration; a participation decision that may abstain; persona-aligned generation. All stages write to a shared data store.
- **Dual memory:** short-term recent conversational context plus periodic natural-language reflective summaries describing team progress and dynamics. The stated design target is persona coherence across a full experimental session.
- **Experiment chaining and analytics:** ordered sessions with persistent teams and stable participant/AI identities; timestamped chat exports; participant identifiers; condition labels; persona specifications; pre/post-survey responses; per-message decision traces with context and rationale; retrieval queries and retrieved passages.

The paper therefore provides meaningful instrumentation for message-level and team-level analysis. It does **not**, in the reviewed description, specify:

- whether reflective long-term memory is reset, copied, or carried across session boundaries;
- a memory-snapshot identifier/hash and parent-snapshot lineage for each session;
- a complete reset/clone/carryover event log;
- the exact per-team/per-agent state-isolation or database-partitioning contract;
- per-model-request identifiers and retry/error lineage for every generated turn;
- a multi-agent-per-team message-visibility graph.

These are **not specified in the paper**, not proven absent from the implementation. The statement that all pipeline stages write to a shared data store does not establish either cross-team leakage or per-team isolation.

### Important distinction

**Persistent identity is not proof of persistent state.**

The paper explicitly describes stable participant and AI identities across chained sessions, while its dual-memory description frames the memory mechanism as sustaining coherence across a session. Those are different claims. Stable identity alone cannot establish that one session's reflective memory is supplied to the next.

The correct present status is:

- AI_IDENTITY_CONTINUITY = SOURCE_REPORTED
- WITHIN_SESSION_DUAL_MEMORY = SOURCE_REPORTED
- CROSS_SESSION_MEMORY_CARRYOVER = NOT_SPECIFIED
- RESET_OR_CLONE_SEMANTICS = NOT_SPECIFIED
- PER_TEAM_MEMORY_ISOLATION = NOT_INDEPENDENTLY_VERIFIED

## 3. Study-version lineage: do not merge the two descriptions

The paper's demonstration study is described as:

- six weekly sessions;
- about 51 students, with 52 present from session six onward;
- two configured personas: cognitive-scaffolding and socially-supportive;
- a persistent roster and recurring team formation;
- 99 team-sessions and 4,495 messages in the six-session chain.

The official website separately describes **Study 3, “Temporal HAT,” as ongoing**:

- 17 teams followed across five sessions;
- half with a verbose AI persona and half with a terse persona.

The public website also says that each study replaces one human seat with one AI teammate. That confirms the single-AI-teammate evidence regime, not a multi-LLM peer panel.

The paper's six-session demonstration and the website's current five-session verbose/terse study have different session counts and different persona labels. Their relationship is **UNRESOLVED**. They may be different study stages, cohorts, or descriptions; do not treat their counts, conditions, participants, or outputs as one dataset without an author/source crosswalk.

The website's headline statistics are public project claims, not independently reanalysed results. The ongoing Study 3 description is not a results paper.

## 4. New architecture finding: persona effects and memory history can become aliased

A longitudinal AI teammate has at least two conceptually distinct state inputs:

1. current persona configuration, P;
2. memory/history state presented to the model, H.

For a saturated two-factor mean model:

\[
Y_{p,h}=\alpha+\beta_P p+\beta_H h+\beta_{PH}ph,
\qquad p,h\in\{0,1\}.
\]

If the observed design contains only the diagonal cells (0,0) and (1,1), then the observed contrast combines the persona, history, and interaction effects. For every nonzero \(\delta\), the coefficient transformation

\[
(\beta_P,\beta_H,\beta_{PH})
\mapsto
(\beta_P+\delta,\beta_H-\delta,\beta_{PH})
\]

leaves both diagonal cell means unchanged. The distinct persona and history main effects therefore cannot be separated from those observations alone.

If all four cells (0,0),(1,0),(0,1),(1,1) are observed, equality of the four saturated-model cell means forces equality of the intercept, persona effect, history effect, and interaction coefficient. This is algebraic parameter identifiability under the stated model, not by itself causal identification.

### Interpretation boundary

This is a **conditional design theorem**, not a finding that TRAIL's published demonstration was confounded. The paper does not say that persona was switched within teams, and it does not specify cross-session memory carryover. If memory is reset each session, the proposed cross-session carryover concern does not apply. If memory persists, its role depends on the estimand:

- For the **total effect of a stable persona across a longitudinal collaboration**, persona-conditioned accumulated history may be part of the treatment package or a mediator. It should not automatically be adjusted away.
- For a **direct persona effect holding memory history fixed**, the memory state must be reset, standardized, cloned, or independently manipulated and logged.
- If persona and memory history vary together without independent support, direct persona and history effects are not separately identified by the saturated model.

## 5. Proposed experiment and state-lineage contract

A minimal direct-effect design is a team-randomized 2×2 factorial:

| Current persona | Memory mode | Purpose |
|---|---|---|
| A | Fresh | Persona A under reset state |
| B | Fresh | Persona B under reset state |
| A | Standardized carryover | Persona A under a common frozen history snapshot |
| B | Standardized carryover | Persona B under the same frozen history snapshot |

The carried snapshot should be identical across persona conditions if the target is the effect of current persona conditional on a common history. If the research question instead concerns **who generated the history**, add an explicit history-origin factor (for example, A-generated, B-generated, and fresh) and counterbalance or clone the state. Do not silently equate “carryover present” with “history generated by the current persona.”

Randomize at the team level, analyze repeated sessions as clustered within teams, preregister the session sequence and carryover policy, and do not count turns or team-sessions as independent teams.

### Required state and exposure records

For each team, agent, and session, retain:

- team ID and agent-instance ID;
- provider, model/version, decoding configuration, system/prompt hash, persona-config hash, and participation-policy hash;
- pre-session and post-session memory snapshot IDs/hashes;
- parent snapshot ID, prior-session ID, and explicit RESET, CLONE, or CARRY_FORWARD event;
- short-term context window definition and long-term reflective-summary version;
- retrieval-index version, query IDs, and retrieved-document IDs;
- message IDs, sender, recipient/visibility set, timestamps, ordering, truncation, and context-injection record;
- model request ID, output/abstention, retries, provider errors, and decision trace;
- assignment condition, randomization seed, sequence/order, and team-level outcome provenance.

For a future **multi-LLM peer** extension, each agent requires separately versioned memory plus an explicit directed message-visibility/exposure graph. The reviewed TRAIL paper and site do not establish that the current platform implements multiple AI peers within one team.

## 6. Formalization status

A conditional Lean 4/Mathlib module was added to Orson's existing draft PR #1115, which already contains group/session confounding and prior-visibility formalizations:

- PR: https://github.com/Satobloc/HsH/pull/1115
- Branch: review/human-ai-group-unit-identifiability-20261030t1848z
- New module: FORMAL_VERIFICATION/HsHVerification/HumanAIMemoryCarryover.lean
- Module commit: 2c91ae5e72ec5503b070bcf446b78ae1fa83319f
- Root-import commit: 7e3b3e5e1ac9933cd6a7c0f5c42879b469f34c7e

The module states the diagonal-cell aliasing theorem and the four-cell saturated-model identification theorem. It includes theorem-specific #print axioms commands and no intentional sorry or admit placeholders.

**Verification: LEAN_NOT_RUN.** The required local lean, lake, and elan executables are absent; a bounded attempt to reach GitHub to install the pinned toolchain failed DNS resolution. No Lean Actions run is associated with the new PR head. The branch's push produced a separate conversation-json-content-ci failure before any job record was exposed; that is not a Lean result and its cause is not established. The existing successful Lean run for PR #1480 does not include this module and cannot be borrowed as verification.

The module remains an unverified draft. Do not call the theorem compiled or verified, and do not merge the PR on this evidence. The existing project workflow specifies Lean 4.34.0 / Mathlib v4.34.0; a future successful run must identify the exact checked commit and theorem-specific axiom output. Exact-head verification remains separate from any merge-reference build.

## 7. Evidence and limits

- The TRAIL paper is a primary preprint; its platform and demonstration claims are attributed to its authors.
- The official site is a current project description, not independent replication or a peer-reviewed results paper.
- No participant-level data, raw team transcripts, memory snapshots, platform schema, source code, or model request logs were accessed.
- No model trial, human session, API call, participant contact, or API spend occurred.
- No memory carryover is asserted as an observed TRAIL behavior.
- No consciousness, subjective experience, or human-equivalent cognition claim is made.
- No P1 manuscript, frozen ConsistencyBench scope, November 9 gate, P2 November 30 gate, or P3 December 14 gate was changed.
- No SAT-O/Blockwave equation, physical model, H(s)H prediction, BEDROCK claim, or theory status was changed.
- No new tool, plugin, fork, paid service, or automation was created.

## 8. Exact next cursor

1. Obtain a source-authorized schema, code inspection, or researcher-accessible export sufficient to establish team-scoped state isolation and memory reset/carryover semantics. No access request or account creation is implied by this note.
2. Resolve whether the paper's six-session demonstration and the website's ongoing five-session Temporal HAT study are the same cohort/study stage; require an author/source crosswalk before combining them.
3. Run the new module with the pinned Lean 4.34.0 / Mathlib v4.34.0 workflow on the exact PR head; inspect theorem-specific axioms and retain the failure state if compilation does not pass.
4. Keep the ConsistencyBench P1 source/experiment and manuscript-readiness gates separate.

**Disposition:** VEY-035 primary-source review complete; conditional design theorem formalized but LEAN_NOT_RUN; no empirical reanalysis or administered trial; no P1 or theory advancement.
