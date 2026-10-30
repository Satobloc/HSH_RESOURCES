# Vey Cognition Lab — Purpose-Driven Source Index

This index is intentionally narrower than the repository-wide bibliography. It tracks sources useful to the Vey research programs and records *why* they matter. Inclusion is not endorsement.

Review states used here: **LOCATED**, **TRIAGED**, **REVIEWED**, **EXTRACTED**, **SUPERSEDED/CONTEXTUAL**.

## Internal archive anchors

### HSH_RESOURCES human index — AI, Cognition & Consciousness

- **State:** TRIAGED
- **Path:** `indexes/human_source_index/subject__ai-cognition-consciousness-408c51__001.md`
- **Current coverage:** 32 catalog records tagged `AI, Cognition & Consciousness`.
- **Use:** Baseline external/internal literature shelf. Many entries remain provisional and require claim-level review before use.

### `Consciousness + AI/`

- **State:** LOCATED
- **Use:** Existing archive-native papers, conversations and compilations directly relevant to AI consciousness, panagnosticism, model behavior, and Nathan–AI work.
- **Notable already-indexed items:**
  - *A Meaningless Argument About a Meaningless Argument: The Gnome, the God, and the GPU* — Nathan McKnight; archive-native satirical/formal epistemology manuscript.
  - *A Formal Epistemic Proof of Panagnosticism* / related versions — archive-native formal epistemology.
  - `TRANSCENDER.txt`, `A CHAT.txt`, `Wacky 4D*.txt` and other long-form human–AI artifacts — potential behavioral corpus material; provenance/role analysis required before cognitive claims.

### Conversation / instance corpus

- **State:** LOCATED AS RESEARCH FAMILY; path census pending VEY-001
- **Priority topics already known from prior work:**
  - memory-isolated, SAT-naïve and SAT-exposed instances used as epistemic controls;
  - NotebookLM role/persona carryover from uploaded ChatGPT-oriented documents;
  - recursive ChatGPT ↔ NotebookLM ↔ artifact workflows;
  - Overseer / Integrator / Auditor / specialist role systems and later Tern-managed execution leases;
  - constructed-personality, revival and role-conflict experiments;
  - observed constraint leak, mirror drift, loop fatigue, literalization and backmapping;
  - cases where model self-report exceeded what could be supported by model knowledge or supplied evidence.

These materials are not assumed to be controlled experiments. Many are naturalistic observations whose value depends on recoverable context and exposure history.

## High-priority outside literature / product documentation

### Google — current NotebookLM / Gemini Notebook product behavior

1. **Google (2026-07-16), “NotebookLM is now Gemini Notebook.”**
   - URL: https://blog.google/innovation-and-ai/products/gemini-notebook/notebooklm-gemini-notebook/
   - **State:** TRIAGED
   - **Why it matters:** Current product identity and architecture context. Google states that NotebookLM was renamed **Gemini Notebook** while remaining a standalone research product, with newer integrations and a secure cloud computer/code execution rollout. Historical archive references should remain `NotebookLM`; current-system tests should record the current product/version surface.

2. **Google Gemini Notebook Help — source grounding differences across products.**
   - URL: https://support.google.com/gemininotebook/answer/17513891?hl=en
   - **State:** TRIAGED
   - **Why it matters:** Official documentation states that Gemini Notebook chat grounds responses exclusively in notebook sources, while related Gemini/Search surfaces may also use web search and other tools. This is directly relevant to interpreting Nathan's cross-system persona/backmapping observations and to designing source-isolation tests.

3. **Google (2026-06-08; updated 2026-07-16), “Do better research with NotebookLM.”**
   - URL: https://blog.google/innovation-and-ai/products/notebooklm/better-research-notebooklm/
   - **State:** TRIAGED
   - **Why it matters:** Product changes can invalidate comparisons across years. Current NotebookLM/Gemini Notebook runs should not be assumed behaviorally equivalent to 2024–2025 runs.

### Persona / role effects

4. **Hu, Zizhao; Mohammad Rostami; Jesse Thomason (2026), “Expert Personas Improve LLM Alignment but Damage Accuracy: Bootstrapping Intent-Based Persona Routing with PRISM.”**
   - arXiv: https://arxiv.org/abs/2603.18507
   - **State:** TRIAGED
   - **Why it matters:** Direct comparison point for archive observations in which role/persona conditioning changed behavior. The paper reports that persona effectiveness depends on task/model/prompt conditions and can improve some preference/alignment outcomes while harming accuracy on other tasks. Useful warning against treating a vivid persona as a uniformly beneficial cognitive scaffold.

### Reasoning, chain-of-thought and self-report

5. **Wang, Wenshuo (2026), “LLM Reasoning Is Latent, Not the Chain of Thought.”**
   - arXiv: https://arxiv.org/abs/2604.15726
   - **State:** TRIAGED; a copy is already represented in HSH_RESOURCES.
   - **Why it matters:** Strongly relevant to Vey's rule that generated reasoning narratives are not automatically faithful descriptions of internal mechanism. Position-paper status must be kept distinct from direct empirical demonstration.

6. **David, Joey (2025), “Temporal Predictors of Outcome in Reasoning Language Models.”**
   - arXiv: https://arxiv.org/abs/2511.14773
   - **State:** TRIAGED
   - **Why it matters:** Hidden-state work suggesting eventual correctness can become predictable early in a reasoning trace. Relevant to distinguishing latent computation from surface explanation and to potential early-warning/error-prediction designs.

### Multi-agent context / independence

7. **Helmi, Tooraj (2025), “Modeling Response Consistency in Multi-Agent LLM Systems: A Comparative Analysis of Shared and Separate Context Approaches.”**
   - arXiv: https://arxiv.org/abs/2504.07303
   - **State:** TRIAGED
   - **Why it matters:** Directly relevant to VEY-004. Shared versus separate context affects consistency, noise and interdependence; useful literature comparator for the project's concern that nominally separate instances may not supply independent corroboration.

8. **Hossain, Elias; Niloofar Yousefi; Ser-Nam Lim (2026), “Agreement Overstates Evidence: Error Dependence in LLM Judge Consensus.”**
   - arXiv:2609.22512
   - **State:** TRIAGED (abstract read; full-text review open)
   - **Why it matters:** Reports correlated judge errors and reduced effective independent-judge information. Direct caution for interpreting panel agreement as independent evidence; not the same dataset or intervention as VEY-011.

9. **Hu, Yibo; Jiaming Qu (2026), “Social Pressure Breaks Majority Voting in LLM Safety Panels.”**
   - arXiv:2608.04415
   - **State:** TRIAGED (abstract read; full-text review open)
   - **Why it matters:** Controlled two-round peer-label exposure design. Important comparator for a future causal VEY-004 test; unlike VEY-011, this study actually shows peer labels to models and manipulates the cue.


### Longitudinal human–LLM collaboration

8. **Du, Lingxiao (2026), “Human Reinforcement Learning from AI Feedback: Feedback Mechanisms, Meta-Collaborative Monitoring, and Identity Positioning in Long-Term Human-AI Collaboration.”**
   - SSRN: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6928698
   - **State:** HIGH-PRIORITY TRIAGE
   - **Why it matters:** Exceptionally relevant comparator. It uses a longitudinal self-case-study corpus of 1,611 conversation windows / 25,859 messages and reports shifts toward structure, archiving, collaboration governance, risk reminders and reality checks. Nathan's corpus is different in scale, structure and multi-instance organization, but any claim about unusual long-term human–AI co-adaptation must compare against this work rather than assume novelty.

9. **Farach et al. / Microsoft Research (2026), “Scaffolding Human-AI Collaboration: A Field Experiment on Behavioral Protocols and Cognitive Reframing.”**
   - URL: https://www.microsoft.com/en-us/research/publication/human-ai-collaboration-field-experiment/
   - **State:** TRIAGED
   - **Why it matters:** Controlled evidence that collaboration scaffolds can help, harm, or interact with design confounds. Relevant to evaluating Nathan's elaborate workflow scaffolds without assuming that additional structure is automatically beneficial.

10. **“Human-AI collaboration or obedient and often clueless AI in instruct, serve, repeat dynamics?” (2026), The Internet and Higher Education 70:101087.**
    - DOI landing page: https://doi.org/10.1016/j.iheduc.2026.101087
    - **State:** TRIAGED
    - **Why it matters:** Interaction-sequence study reporting dominant instructive rather than collaborative patterns in a student task corpus. Useful contrast class: Nathan's collaboration is explicitly recursive, corrective, role-structured and meta-governed rather than simple prompt→answer use.

11. **“Cognitive offloading in student–AI collaboration: A longitudinal analysis of prompting strategies” (2026), Computers in Human Behavior Reports 22:101130.**
    - Article landing page: https://www.sciencedirect.com/science/article/pii/S2451958826002046
    - **State:** TRIAGED
    - **Why it matters:** Comparator for cognitive offloading, prompt evolution and low-effort convergence. Nathan's archive may allow a materially different question: under intensive expert-like use, when does offloading become *reallocation* into critique, orchestration and verification rather than simple disengagement?

## Immediate review priorities

1. Du 2026 longitudinal self-case study — closest obvious precedent for a Nathan–LLM paper.
2. Persona-effect literature, beginning with PRISM — relevant to Alberr/Alice/Enheduanna/revival and NotebookLM role adoption.
3. Shared/separate-context and correlated-error multi-agent literature — needed before making claims about instance independence.
4. Reasoning/self-report literature — establish what can and cannot be inferred from model explanations of themselves.
5. Current Gemini Notebook documentation — build a versioned product timeline so old NotebookLM observations are not silently generalized to the current system.

## Acquisition policy

Where licensing and repository policy permit, preserve a local paper or text extract. Otherwise preserve a bibliographic record, stable URL/DOI/arXiv identifier, review notes and any legally reusable excerpts needed for research. Do not duplicate material merely to create volume; the purpose-driven index should remain smaller and more heavily reviewed than the general resource library.


## P1 multi-agent dependence — full-text review addendum (2026-10-30)

- **Hossain, Yousefi & Lim (2026), “Agreement Overstates Evidence: Error Dependence in LLM Judge Consensus,” arXiv:2609.22512.**
  - State: FULL-TEXT REVIEWED 2026-10-30.
  - Scope: passive correlated judge-error analysis. It does not manipulate shared evidence-source exposure or show peer answers to the judges.
  - URL: https://arxiv.org/abs/2609.22512

- **Kohli et al. (2026), “Nine Judges, Two Effective Votes,” arXiv:2605.29800.**
  - State: FULL-TEXT REVIEWED 2026-10-30.
  - Scope: judge-panel error dependence against human annotations. It is not a source-sharing intervention.
  - URL: https://arxiv.org/abs/2605.29800

- **Hu & Qu (2026), “Most LLM Conformity Needs No Speaker: Source-Free Conformity as a Baseline and Attribution Increment,” arXiv:2607.05545.**
  - State: FULL-TEXT REVIEWED 2026-10-30.
  - Scope: repeated answer content without an explicit speaker still changes responses; source/authority attribution adds an increment. The “source-free” arm still contains repeated content and is not a no-information control.
  - URL: https://arxiv.org/abs/2607.05545

- **Hu & Qu (2026), “Social Pressure Breaks Majority Voting in LLM Safety Panels,” arXiv:2608.04415.**
  - State: FULL-TEXT REVIEWED 2026-10-30.
  - Scope: peer-label exposure intervention; not an isolated content-only baseline.
  - URL: https://arxiv.org/abs/2608.04415

- **Qu et al. (2026), “Easier to Mislead Than to Correct,” arXiv:2606.01637.**
  - State: FULL-TEXT REVIEWED in VEY-012.
  - Scope: peer-majority and authority cues; related research group to the Hu & Qu studies, not an independent replication.
  - URL: https://arxiv.org/abs/2606.01637

Do not compare their error-correlation coefficients directly with VEY-013's pair-specific key-disagreement phi. Dataset, ground truth, missingness, item-difficulty conditioning, and intervention differ.


## P1 implementation provenance: ConsistencyBench CGD evaluator

- Repository: `aayambansal/ConsistencyBench`
- Path: `src/evaluate.py`
- Exact Git blob: `0453540cb7c19227601e59fb342fa93e736da849`
- Read extent: 327 lines; exact blob fetched 2026-10-30.
- Relevant regions: repair prompt lines 82-95; model-input/output handling lines 181-209; CGD loop and stored result fields lines 238-289; `NLIContradictionChecker` lines 296-327.
- Finding: the common hard-coded `openrouter/openai/gpt-4o-mini` checker compares two same-model raw responses without the question or premise. The revision prompt receives question/premise context. The checker response is reduced to a Boolean flag in the archived result. The model does not receive other models' answers; panel majority is post-hoc.
- Interpretation boundary: common evaluator and common benchmark are documented; common evidence-source exposure and causal peer influence are not identified.
- Full source/pipeline analysis: `STUDIES/VEY-014_SOURCE_PIPELINE_AND_P1_SCOPE_AUDIT_2026-10-30.md`.


## P1 key-semantics / finite-pattern source set (2026-10-30, VEY-015)

### Original ConsistencyBench source
- Repository: `aayambansal/ConsistencyBench`.
- Full bank: `data/consistency_bench.json`, blob `3171d2899fd1eb4292794df5952514666b0e2f43`; read as parsed source data, 493 sets / 1,930 question positions.
- Sample bank: `data/consistency_bench_sample.json`, blob `10eb2da27c84c706d8e9e2325afca864fcae6a0d`; read as parsed source data, 300 sets / 1,150 question positions / 268 unique premise strings.
- Upstream evaluator: `src/evaluate.py`, blob `0453540cb7c19227601e59fb342fa93e736da849`; read relevant system-prompt, extract-answer, repair-prompt, CGD-loop and checker regions. The upstream `extract_answer` parser is distinct from the expected-key scorer used in the P1 replay.

### P1 analysis scorer and archived model outputs
- Orson replay script: `WORKSPACES/ORSON_VAY/CODE/2026_10_28_cgd_revision_balance_replay.py`, blob `2e10ed2510b8ce14e716780a887c0fe23c3067b9`; local `norm` function maps free-text expected keys and archived output labels.
- The 17 vanilla and 17 CGD output blobs were independently re-fetched by immutable Git blob IDs from the existing Orson/Calder manifest. The exact 34-blob manifest is retained in the existing Calder full-17 PCR/sensitivity report and the Orson replay script; no new model calls were made.
- Source-fidelity/sensitivity report: `STUDIES/VEY-015_P1_KEY_SEMANTICS_AND_FINITE_PATTERN_IDENTIFIABILITY_2026-10-30.md`.
- Static key-row extraction: `STUDIES/VEY-015_P1_NEGATIVE_INFERENCE_KEY_ROWS_2026-10-30.csv`, 578 rows; 350 sample members. This is not a human-adjudicated key.

### Interpretation boundary
The 1,677/1,700 result is sensitivity to the P1 analysis scorer's alternate treatment of one expected-answer phrase. It is not an upstream benchmark score, corrected key, human adjudication, or causal effect. The OV-55/56 shared-gate and latent-difficulty mechanisms remain assistant-authored analytic models, not administered trials or measured LLM mechanisms.


## Human–multi-LLM peer groups and reusable group-experiment platform (2026-10-30; VEY-016)

- **Chen, Liu, Hu & Li (2026), “AI agents reshape consensus formation in human groups,” arXiv:2609.02122.**
  - State: FULL-TEXT REVIEWED 2026-10-30; public code and processed questionnaire data cross-checked.
  - Scope: direct mixed human–LLM peer participation as reported, 24-member sessions, 40 rounds of randomized pairwise interaction, eight conditions. Public artifacts do not expose per-agent request IDs or separate context histories, so independent model-session/state isolation is not independently auditable.
  - Critical design note: reported human counts plus 24 total seats/session imply one session per condition; group-level treatment replication is not reported. M5 N=495 is 55 humans × 9 sampled interactions, not 495 independent people or groups. HC3 does not cluster by participant/session.
  - Limits: one model family at two sizes, one tangram stimulus, homogeneous random mixing; same MiniLM embedding model used for payoff and primary consensus outcome.
  - URL: https://arxiv.org/abs/2609.02122
  - Code/data: https://github.com/tsinghua-fib-lab/human-ai-consensus

- **Alsobay et al. (2026), “Bringing Everyone to the Table: An Experimental Study of LLM-Facilitated Group Decision Making,” PACM HCI 10(6), CSCW059.**
  - State: FULL-TEXT REVIEWED 2026-10-30.
  - Scope: 1,475 participants in 281 five-person groups; 70 groups per condition; preregistered group-level experiment; GPT-4o facilitator.
  - Interpretation: strong replicated human–LLM facilitator comparator, not a multi-LLM peer-group study. More unique factual information was shared, but optimal decision rate did not significantly improve.
  - DOI: 10.1145/3816907
  - URL: https://arxiv.org/abs/2508.08242

- **Microsoft Research Group-AI Interaction Laboratory (GRAIL), repository microsoft/group_ai_lab.**
  - State: REPOSITORY AND CORE SERVER CALLBACKS REVIEWED 2026-10-30.
  - Scope: open-source MIT platform for synchronous human groups, treatment assignment, consent/surveys, shared chat, LLM facilitator, request/response logging and server-side timestamps.
  - Limit: current implementation is one shared LLM facilitator, not multiple independently stateful peer agents. Adaptation requires per-agent state, identity, prompt/model configuration, turn scheduling and provenance logging.
  - URL: https://github.com/microsoft/group_ai_lab

Full source/method note: STUDIES/VEY-016_HUMAN_MULTI_LLM_GROUP_INTERACTION_REPLICATION_AUDIT_2026-10-30.md.



## 2026-10-30 source-status corrections
- Chen et al., arXiv:2609.02122 is a 2026 preprint providing a direct human-group/multiple-LLM-peer study as reported. The one-session-per-condition inference is strongly implied by the reported 24-seat composition totals, but is not separately stated as a session count.
- Public A2-A5 processed-data artifacts in the Chen et al. repository are `.pkl` files, not CSVs. The earlier VEY-016 wording was inaccurate; the public analysis script reads pickle files and uses OLS HC3 covariance.
- GRAIL's indexed repository page currently shows five forks, not three; fork implementations were not exhaustively reviewed. Main-branch code remains a single shared facilitator.
- GRAIL README cites PACM HCI 10(6) with date 31 October 2026. Since this index update is 30 October and the ACM DOI page returned 403, classify the journal publication status as `NOT INDEPENDENTLY VERIFIED AS OF 2026-10-30`; use arXiv:2508.08242 as the accessible source.
