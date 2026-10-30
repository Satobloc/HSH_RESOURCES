# VEY-016 — Human–LLM peer groups: direct evidence, replication unit, and reusable experiment platform

**Date:** 2026-10-30  
**Status:** COMPLETE-AS-STAGE — full-text literature review, source/code/data audit, conditional Lean formalization in HsH PR #1115; no new model trial or human-subject experiment.  
**Evidence class:** LITERATURE RESULT + SOURCE AUDIT + INTERPRETATION.  
**Owner lane:** Vey Cognition Lab / Review-MIND. This note is a source-grounded reconstruction, not an authenticated Orson Vay ChatGPT instance or thread.

## Question

What empirical evidence exists for real human groups interacting repeatedly with multiple LLM agents as peers, and what does the design actually permit us to infer? What existing platform can support a better-replicated VEY-004 experiment without building a new group-chat system?

## Executive result

A direct peer-agent study was missed by the earlier Review-MIND evidence map:

- Lin Chen, Ziyi Liu, Xia Hu, and Yong Li (2026), **“AI agents reshape consensus formation in human groups,”** arXiv:2609.02122, first posted 2026-09-02.
- The study places multiple LLM agents in 24-member mixed human–AI populations. Participants and agents repeatedly describe the same tangram and are randomly paired for 40 rounds. They see the partner's description and a similarity-score payoff before the next round.
- This is a direct counterexample to any broad statement that mixed human groups with multiple LLM peer participants have not been studied.

It does **not** close the more demanding gap identified in the earlier map. The paper does not provide independently replicated group sessions per treatment, independent source/context ancestry, or independent semantic adjudication of the primary consensus outcome. The strongest remaining gap is therefore narrower: **replicated human–multi-LLM peer groups with auditable agent-state/source provenance and independently adjudicated outcomes.**

## 1. Direct peer-agent study: Chen et al. (2026)

**Primary source:** https://arxiv.org/abs/2609.02122  
**Version:** v1, 2026-09-02. Preprint; peer-review status not established in this review.

### 1.1 What was actually done

The supplement reports 127 human participants, randomly assigned to eight conditions. Each experimental session contains 24 total participants, mixing humans and LLM agents. Participants complete 40 rounds of random pairwise communication. Each pair independently describes the same abstract tangram; after submission, each sees the partner's description and a similarity score. Pairings change each round under a homogeneous-mixing protocol.

The main agent model is Qwen2.5-VL-32B-Instruct. A weaker Qwen2.5-VL-7B-Instruct condition is used in Study C. All agents receive the game rules; neutral, high-adoption, and high-persistence prompts are compared. This is a structured repeated dyadic convention-formation task, not an unrestricted group-chat deliberation task.

### 1.2 Source-transcribed group composition

| Study / condition | Humans | LLM agents | Total seats |
|---|---:|---:|---:|
| A: 0% agents | 24 | 0 | 24 |
| A: 12.5% agents | 21 | 3 | 24 |
| A: 33.3% agents | 16 | 8 | 24 |
| A: 50% agents | 12 | 12 | 24 |
| A: 75% agents | 6 | 18 | 24 |
| B: high adoption | 16 | 8 | 24 |
| B: high persistence | 16 | 8 | 24 |
| C: weaker base model | 16 | 8 | 24 |
| **Total** | **127** | **65** | **192** |

The eight reported human counts sum exactly to 127; the complementary agent counts sum to 65. Combined with the stated 24-member session size, this is consistent with **one 24-member session per condition**. The paper does not separately report a multi-session replication count. Treat one session per condition as a strong source-level inference, not a Lean-proven fact.

### 1.3 Reproducibility cross-check

The public repository https://github.com/tsinghua-fib-lab/human-ai-consensus contains figure-reproduction scripts and processed data, not the complete live experiment-serving platform or per-request model traces.

The A2–A5 personalized-question CSVs contain 108, 144, 189, and 54 rows respectively. The supplement says each human participant is shown nine sampled interaction rounds. Dividing each CSV count by nine gives 12, 16, 21, and 6 humans, matching the corresponding 50%, 33.3%, 12.5%, and 75% conditions. Across these four files, 495 rows = 55 humans × 9 sampled rounds. This exactly matches the supplement's M5 regression N=495.

The analysis code's M5 OLS uses heteroskedasticity-consistent HC3 standard errors. HC3 does not account for repeated observations nested within the same person or for the group/session as the treatment-assignment unit. The code loads one tracker per A2–A5 experiment and does not supply session-clustered standard errors. This is not evidence of fabricated data; it is a dependence/uncertainty limitation.

### 1.4 Main inferential limitation: no group-level replication per condition

The manipulated agent proportion and agent-trait/model conditions are group/session-level conditions. The source counts imply one 24-member session per condition. Thus each treatment arm has one independent group, while participants and 40 rounds are nested/repeated observations inside that group.

The primary consensus curves and within-session error bars cannot substitute for independent group replication. Session-specific effects are inseparable from condition effects when there is only one session per condition. For the adoption-willingness regression, N=495 is not 495 independent people or 495 independent groups: it is 55 humans contributing nine sampled-round responses each across four agent-proportion sessions.

A group-level treatment effect requires multiple independently randomized sessions per condition and analysis at the group/session level. With one session per arm, between-session variance cannot be estimated. The published descriptive pattern remains an observed result in this particular set of sessions; broad causal generalization across groups is not established.

### 1.5 Measurement and generalization limits

- The same all-MiniLM-L6-v2 embedding model computes the similarity feedback/payoff participants receive and the embedding-based consensus outcomes. The primary outcome is therefore aligned to the task's reward signal; it is not independent semantic truth or decision accuracy.
- A separate LLM-as-judge annotation is used for analogical, holistic, and event-framing properties, with reported robustness across Qwen2.5-72B, DeepSeek-V3, and Kimi-K2. This is useful secondary checking, not independent adjudication of the primary consensus measure.
- One tangram figure is used across sessions. The authors justify this as stimulus control, but generalization to other tasks remains open.
- The main peer agents come from one model family at two sizes. This is multiple agent participation, not cross-family model replication.
- Pairings use homogeneous random mixing. Structured networks, persistent dyads, and naturalistic group conversation are not tested.
- “Semantic attractor” is an explanatory label for observed embedding-space convergence, not a directly measured physical or cognitive force. The paper's account of a shared linguistic prior is an interpretation of the observed initial similarity and behavior, not direct access to model internals.

### 1.6 Claim status

| Claim | Status |
|---|---|
| Multiple human participants and multiple LLM agents occupy the same experimental group | VERIFIED AS REPORTED |
| Repeated human–agent and agent–agent interaction occurs | VERIFIED AS REPORTED through randomized pairings |
| Agent proportion is associated with different convergence regimes in this task | REPORTED; descriptive within these sessions |
| Agent proportion has a replicated group-level causal effect | NOT ESTABLISHED; one session per condition is implied |
| Independent source/context ancestry is auditable | NOT REPORTED in the released figure-reproduction package |
| Primary semantic consensus is independently adjudicated | NO; primary measure uses the same embedding model as the payoff |
| Cross-family model replication | NO; one family at two sizes |
| Naturalistic group-chat dynamics | NO; structured pairwise rounds |

## 2. Replicated facilitator comparator: Alsobay et al. (2026)

**Primary source:** https://arxiv.org/abs/2508.08242  
**Published version:** Proceedings of the ACM on Human-Computer Interaction, 10(6), article CSCW059 (2026), DOI 10.1145/3816907.

This study used 1,475 participants in 281 five-person groups, with 70 groups per condition (one additional group in the message condition). It compared no facilitator, a human facilitator, an LLM facilitator, and an LLM facilitator with a message treatment. The LLM facilitator used GPT-4o. The experiment was preregistered and the group was the randomized experimental unit.

The LLM facilitator increased the amount of unique factual information shared, but did not significantly improve the final rate of optimal group decisions. This is a stronger example of group-level replication than the single-session-per-condition peer-agent study, but it uses one shared facilitator, not multiple LLM peer participants.

## 3. Existing platform: GRAIL

**Repository:** https://github.com/microsoft/group_ai_lab  
**License:** MIT. Current repository page showed three forks; a targeted search did not surface a fork implementing multiple peer agents. Fork-level coverage is not exhaustive.

GRAIL already supplies much of the infrastructure needed for VEY-004:

- synchronous multi-human sessions and treatment assignment;
- private participant stimuli and hidden-profile tasks;
- consent/onboarding and exit surveys;
- shared chat UI and group coordination;
- full LLM request payload/response logging, model label, timestamps, and trigger metadata;
- server-side timestamp correction guidance.

The current implementation is **one shared LLM facilitator**, not multiple peer agents. The server callbacks have one openaiModel, one getLLMResponse function, one facilitator prompt, and one chat sender identity (ai / Facilitator). The treatment factor is facilitation = none | human | LLM. It does not currently instantiate several independently stateful LLM players.

A multi-peer extension would require per-agent identities, independent conversation state/context, model/prompt configuration per agent, explicit turn scheduling and visibility rules, agent-agent/human exposure logging, and per-agent request lineage. Reusing GRAIL is preferable to building a new group-chat platform from scratch, but this is a bounded code adaptation, not a configuration-only change.

The repository uses Empirica v1.12.0 and requires a user-supplied LLM endpoint/API key and a deployed server. The platform itself has no software-license cost. It does not provide model access, participant recruitment, or hosting. A dollar estimate is not credible until the number of groups, agents per group, turns, context lengths, provider/model, and recruitment/compensation plan are fixed. IRB approval and informed consent are required; the default consent form is a placeholder, and the project warns that it is not security-hardened or production-ready.

## 4. Formalization

HsH draft PR #1115, branch review/human-ai-group-unit-identifiability-20261030t1848z, adds FORMAL_VERIFICATION/HsHVerification/HumanAIGroupsSessionConfounding.lean to the existing Lean 4/Mathlib project.

The module transcribes the eight reported human/agent counts and proves their arithmetic totals. It also proves a conditional identifiability result: if a treatment level occurs in exactly one group/session, its treatment indicator equals that group's indicator; shifting a nonzero amount between the group intercept and treatment coefficient leaves all fitted values unchanged. This is the algebraic reason a one-group-per-treatment design cannot separate treatment from session-specific effects.

**Important boundary:** Lean proves only the encoded conditional statement and arithmetic. It does not prove the source interpretation that there was exactly one session per condition, validate the paper's data, or adjudicate the statistical model. Exact-head CI and theorem-specific axiom inspection are required before this formalization is marked verified.

## 5. Revised VEY-004 direction

The broad “no mixed human–multi-LLM peer-group experiment exists” claim is no longer tenable. The narrower research opportunity remains:

1. multiple independent groups per condition, with group/session as the randomization and primary analysis unit;
2. at least two independently stateful LLM peer agents in each relevant group;
3. explicit shared-source versus disjoint-source evidence packets;
4. agent-agent communication on/off as a separate factor;
5. exact model/version, prompts, source ancestry, per-agent context, and every message logged;
6. blinded semantic adjudication independent of the model used for feedback/reward;
7. multiple model families or a deliberately limited single-family scope;
8. preregistered group-level outcomes and cluster-aware inference;
9. consent, privacy controls, and IRB approval before any human-subject session.

Do not choose a sample size by intuition. Power analysis requires a pilot estimate of between-group variance and the planned primary outcome. GRAIL can provide the group coordination and logging substrate, but its facilitator callback must be extended for multiple peer agents.

## 6. Limits and next action

- This is a full-text and public-code audit, not an independent replication.
- The live experiment-serving code and raw model request logs for Chen et al. were not recovered from the public figure-reproduction repository.
- No new model calls, human participants, or private instance experiments were used.
- No paid API, hosting, recruitment, or IRB activity occurred.
- VEY-004 remains QUEUED. This literature review does not complete it.
- Orson's ConsistencyBench P1 remains separate and protected; this note does not alter the Nov 9 minor-paper gate, the Nov 30 major-paper gate, or the Dec 14 full-theory gate.
- HSH_RESOURCES remains a research shelf, not H(s)H theory bedrock.


### Operational independence caveat

The paper treats the LLMs as separate participant slots and describes their repeated pairwise interactions, so the study is a direct multi-agent group experiment at the task-design level. However, the released repository is a figure-reproduction package; it does not expose the live serving/orchestration code, per-agent request IDs, or separate context histories. Therefore, independent model-session/state isolation is **reported but not independently auditable** from the public artifacts. Do not silently upgrade “multiple LLM agent participants” into “verified independent model instances.”


### Reported quantitative pattern (not independently re-estimated)

The paper reports a pure-human final consensus mean of 0.695; the 12.5% agent condition is reported as 8.0% above that baseline (z = 3.282, p = 0.001), the 33.3% condition 23.1% below baseline (z = -12.326, p < 0.001), and the 75% condition at 0.725. At fixed 33.3% agent proportion, the high-persistence prompt is reported to reduce consensus by 9.6% relative to neutral agents (z = -3.289, p = 0.001); high adoption is not significant (p = 0.2684). These are the authors' reported statistics, not an independent reanalysis. Given the one-session-per-condition inference, they should be read as within-study descriptive contrasts rather than replicated group-level treatment estimates.


## Verification and source-correction addendum | 2026-10-30 19:37Z

### Exact-head Lean verification
- Draft PR #1115 branch: `review/human-ai-group-unit-identifiability-20261030t1848z`.
- Exact head: `c029318b96a07fc433ed16a9082cb2e7b29002ea`.
- GitHub Actions run #41115603417, job #124268909008: **SUCCESS**. Lean 4.34.0, Lake 5.0.0, 8,973 build jobs.
- The theorem-specific `#print axioms` outputs contain no `sorryAx`. The conditional identifiability theorems use standard dependencies `propext`, `Classical.choice`, and `Quot.sound`; arithmetic checks emit `propext`. The `nanoda` and automated `axiom-audit` steps were skipped.
- Status: `LEAN_COMPILE_SUCCESS / THEOREM_AXIOMS_INSPECTED / AUTOMATED_AXIOM_AUDIT_NOT_RUN`.
- Lean verifies only the formalized conditional statement. It does not prove the source-level inference that there was exactly one group/session per condition, validate the paper's data, or establish the paper's causal interpretation.

### Independent arithmetic and design-matrix check
- Reported human counts: `[24,21,16,12,6,16,16,16]`; reported LLM-agent slots: `[0,3,8,12,18,8,8,8]`.
- Sums: 127 humans, 65 agent slots, 192 total seats. The supplement says 24 total participants per session; the eight compositions therefore strongly imply eight 24-seat sessions, one per condition. The paper does not separately state a session-replication count.
- Conditional on that one-session-per-condition inference, the 8 group-indicator columns and 8 treatment-indicator columns are identical. A Python check of the 8x16 matrix `[I8 | I8]` gives rank 8 and nullity 8. This is a structural calculation, not a fit to participant-level observations.
- With 24 participants paired once per round over 40 rounds, there are 12 dyads per round and 480 pairings per session. Across eight sessions that would be 3,840 pairings, conditional on the session-count inference. The actual pairing schedule is not released, so no actual network connectivity or agent-agent edge count is claimed.

### Public data/code correction
- The public repository stores `A2.pkl` through `A5.pkl` in `processed_data/`; these are pickle files, not CSVs. The earlier wording “A2–A5 questionnaire CSVs” was inaccurate and is corrected here.
- The current analysis script reads the `.pkl` files and fits OLS with `cov_type="HC3"`. HC3 is heteroskedasticity-robust; it does not cluster repeated observations by participant or session.
- The earlier audit's per-file row counts (108, 144, 189, 54) were not re-extracted from the pickle files in this pass. The arithmetic `495 = 55 x 9` is consistent with the paper's M5 N and nine sampled interactions, but the row-count extraction remains a prior-pass result.
- The primary consensus outcome is cosine similarity under `all-MiniLM-L6-v2`, also used for the payoff feedback. It measures embedding convergence, not truth or independent task quality.
- The study is an arXiv preprint (2609.02122, submitted 2026-09-02). Its public repository contains processed data and figure-reproduction scripts, not the live experiment runtime or per-agent request/context traces. Multi-human/multi-LLM peer interaction is verified as reported; independent per-agent state isolation is not independently auditable from the released artifacts.

### GRAIL source-status correction
- The current indexed GRAIL repository page shows five forks, not the three recorded in the first note. No exhaustive fork-by-fork code audit was performed; targeted search did not surface a fork implementing multiple peer agents.
- The current main implementation has one `openaiModel`, one `getLLMResponse` path, one `Facilitator` sender, and a shared `llmLog`. It is a single-facilitator platform, not a multi-peer-agent platform out of the box.
- The GRAIL README's companion-paper citation lists PACM HCI 10(6), 31 October 2026, one day after this run. The ACM DOI page returned 403 in this check. As of 30 October, journal publication status is therefore not independently confirmed; use the accessible arXiv:2508.08242 preprint as the source.
- Reuse/adapt GRAIL rather than build a new platform. No new tool, paid API call, hosting deployment, participant recruitment, or human-subject session was initiated.

### Scope and provenance
- This source corrects the earlier Review-MIND gap statement: a direct multi-human/multi-LLM peer-interaction study exists as reported. The group-level replication and per-agent provenance limitations remain.
- The original Oct 9 local / Oct 10 UTC Nathan instruction assigned Orson primarily to LLM cognition. The Oct 26 Nathan Direct reinforcement adds the four-of-five substantive-turn target and the Nov 9 P1 paper gate. The exact original conversation/message UUID was not recovered in this pass; do not attribute the Oct 26 reinforcement to the original role reset.
- The OV-49–OV-53 answer-keyed cognition test bank remains unrecovered. OV-55/56 and OV-100 are analytical/synthetic artifacts, not administered human trials.
- The Nov 9 minor paper remains separate from the Nov 30 major and Dec 14 full-theory gates. No manuscript, PDF, reader, or gate status changed.
- Last recorded FIE reread: 2026-10-27, so the 14-day re-review threshold is not due.


### Publication verification
- Existing issue #1116 remains the sole publisher submission for this note. Publisher receipt comment #6531798863 recorded commit `78873863192bf06b90aff915aa2cc9277f20efef`; artifact `WORKSPACES/COMMON/PUBLISHED_SUBMISSIONS/reviewmind-human-ai-peer-group-replication-audit-20261030t1848z-s4-001.md` was read back and matched the issue payload exactly. Independent SHA-256: `38d9738ebb7aed17933815ce3d40d94fadf3600e389f0035e980bd9f03527888`. Additive correction comment #6532231836 was added; no second submission was created.
