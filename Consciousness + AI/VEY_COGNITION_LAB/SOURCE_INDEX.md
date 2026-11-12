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
   - **State:** FULL-TEXT REVIEWED 2026-10-30; see P1 multi-agent dependence addendum below.
   - **Why it matters:** Reports correlated judge errors and reduced effective independent-judge information. Direct caution for interpreting panel agreement as independent evidence; not the same dataset or intervention as VEY-011.

9. **Awuni et al. (2026), “Who Judges Matters: Measuring Family-Conditioned Preference in LLM-as-Judge Panels,” arXiv:2609.17857v1.**
   - **State:** FULL-TEXT REVIEWED 2026-11-04 (arXiv HTML §§1–11 and Appendices A–D).
   - **Why it matters:** Fully crossed judge-family × candidate-family panel; demonstrates why the naive row-wise same-family contrast confounds candidate-family strength and gives a column-wise estimator under balanced/double-centered assumptions. Separates family-conditioned preference from exact self-evaluation, likelihood familiarity, and order instability.
   - **Boundary:** Preprint; no raw archive independently retrieved in this pass. No peer exposure or cross-model deliberation is tested. Not a P1 replication.
   - **URL:** https://arxiv.org/abs/2609.17857
   - **Public HsH artifact:** issue #1334 (PUBLISHED_VERIFIED).

10. **Hu, Yibo; Jiaming Qu (2026), “Social Pressure Breaks Majority Voting in LLM Safety Panels.”**
   - arXiv:2608.04415
   - **State:** FULL-TEXT REVIEWED 2026-10-30; see the source-status corrections below.
   - **Why it matters:** Controlled two-round peer-label exposure design. Important comparator for a future causal VEY-004 test; unlike VEY-011, this study actually shows peer labels to models and manipulates the cue.


### Longitudinal human–LLM collaboration

8. **Du, Lingxiao (2026), “Human Reinforcement Learning from AI Feedback: Feedback Mechanisms, Meta-Collaborative Monitoring, and Identity Positioning in Long-Term Human-AI Collaboration.”**
   - SSRN: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6928698
   - **State:** HIGH-PRIORITY TRIAGE
   - **Why it matters:** Exceptionally relevant comparator. It uses a longitudinal self-case-study corpus of 1,611 conversation windows / 25,859 messages and reports shifts toward structure, archiving, collaboration governance, risk reminders and reality checks. Nathan's corpus is different in scale, structure and multi-instance organization, but any claim about unusual long-term human–AI co-adaptation must compare against this work rather than assume novelty.

9. **Farach et al. / Microsoft Research (2026), “Scaffolding Human-AI Collaboration: A Field Experiment on Behavioral Protocols and Cognitive Reframing.”**
   - URL: https://www.microsoft.com/en-us/research/publication/human-ai-collaboration-field-experiment/
   - **State:** FULL-TEXT REVIEWED 2026-11-08 / WORKING PAPER PREPRINT; peer review not established.
   - **Review note:** `STUDIES/VEY-036_FARACH_SCAFFOLDING_FIELD_EXPERIMENT_UNIT_OF_ANALYSIS_AND_ATTRITION_2026-11-08.md`.
   - **Source-fidelity correction:** `STUDIES/VEY-036_FARACH_SCAFFOLDING_FIELD_EXPERIMENT_UNIT_OF_ANALYSIS_AND_ATTRITION_2026-11-08_AMENDMENT_01_SOURCE_UNIT_CORRECTION_2026-11-12.md` (2026-11-12); the earlier note's participant/pair attribution is corrected there.
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


## 2026-10-30 publication readback
- VEY-016 publisher issue #1116 is the only submission. Artifact readback matched the issue payload exactly; independently recomputed SHA-256 `38d9738ebb7aed17933815ce3d40d94fadf3600e389f0035e980bd9f03527888`. Correction comment #6532231836 is additive; no duplicate submission.


## 2026-10-31 | VEY-018 source cluster

- Shao, Tengfei (2026), “Language-model groups overstate consensus when replaying human deliberation on a reasoning task,” arXiv:2609.20543v1. Primary record: https://arxiv.org/abs/2609.20543. OSF preregistration cited by paper: https://osf.io/5jp7s. Zenodo code/data DOI cited by paper: https://doi.org/10.5281/zenodo.21318346. Full-text mirror inspected: https://www.conceptio.app/document/978469/language-model-groups-overstate-consensus-when-replaying-human-deliber. Preregistration and Zenodo bytes not independently retrieved.
- Zhu, Xiaochen et al. (2026), “DeliChess: A Multi-party Dialogue Dataset for Deliberation in Chess Puzzle Solving,” arXiv:2606.04987v1. Paper: https://arxiv.org/abs/2606.04987. Dataset: https://huggingface.co/datasets/SpaceHunterInf/DeliChess. Usage guide: https://huggingface.co/datasets/SpaceHunterInf/DeliChess/blob/main/USAGE.md. Dataset bytes/checksum not retrieved.
- Karadzhov, Georgi; Tom Stafford; Andreas Vlachos (2023), DeliData, PACM HCI 7(CSCW2), Article 265. DOI: https://doi.org/10.1145/3610056. Repository copy: https://eprints.whiterose.ac.uk/id/eprint/207765/.
- Kohli, Guneet (2026), “Nine Judges, Two Effective Votes: Correlated Errors Undermine LLM Evaluation Panels,” arXiv:2605.29800v1. Primary record: https://arxiv.org/abs/2605.29800. Full HTML: https://arxiv.org/html/2605.29800v1. Kish formula is conditional on exchangeability; eigenvalue n_eff is a separate non-exchangeable diagnostic.
- SciSpace-only leads not counted as evidence: “Effective Sample Size Under Peer Exposure in Multi-LLM Deliberation” (OSF DOI 10.17605/osf.io/aw9vf) and “DelibSim: Procedural Parity, Outcome Mismatch.” Primary records/full texts not retrieved.


## 2026-10-31 | VEY-019 five-regime consensus measurement audit

- Full synthesis: STUDIES/VEY-019_FIVE_EVIDENCE_REGIMES_AND_CONSENSUS_MEASUREMENT_AUDIT_2026-10-31.md.
- Evidence regimes: Kohli (correlated judge errors), Shao (LLM replay of human deliberation), Chen et al. (mixed human–LLM peer population), DeliChess (human-only deliberation with Stockfish outcome), Alsobay et al. (human groups with one LLM facilitator), plus passive ConsistencyBench.
- Main correction: convergence is not correctness; error dependence is not peer influence; facilitator studies are not multi-peer studies; nested turns/utterances/agent slots are not independent groups.
- P1 source status unchanged: original neutral-versus-false-authority answer-keyed bank UNRECOVERED; OV-49–53 pointer mismatch; OV-95 is a separate artifact-presence protocol.
- Lean QA: PR #850 exact head d59a17b270df730e84edbd614eaea3b1b76166e2, run #41160835210 SUCCESS; conditional Kish module only, not empirical exchangeability proof.


## 2026-10-31 | VEY-023 receiver-relative evidence integration

- **Kawada, Sebastien; Manolis Kellis (2026), “Evidence Integration in Large Language Models,” arXiv:2609.04290v1 (2026-09-03).**
  - URL: https://arxiv.org/abs/2609.04290
  - State: REVIEWED (targeted primary-source sections §§3.1–3.6, §§5.1–5.6, §6.3, §7, §8.6; not a line-by-line review of the full 114-page preprint).
  - Why it matters: receiver-relative evidence integration; receiver-congruent wrong candidates; checking/use dissociation; transcript-only provenance non-identifiability; source-dependence and message-order effects. This adds a receiver-side mechanism to P1's existing source-lineage/transmission analysis.
  - Limits: arXiv preprint, not peer-reviewed; scientific tasks use synthetic problems with exact oracles; composition tests limited to arithmetic; prior weight identified from answer-slot margins; no raw-trial/code artifact or independent reproduction located in this review. Not a direct multi-agent peer-interaction experiment.
  - Distinguish its receiver-prior parameter a from VEY-020's posterior-equivalent copy weight w_m, and its verification-recruitment gain rho from checker competence or source reliability.
  - Formalization pointer: HsH PR #850 module OrsonEvidenceCompositionLaw.lean; six conditional theorems, exact-head Lean CI status tracked in the HsH receipt/report.
  - Durable note: STUDIES/VEY-023_RECEIVER_RELATIVE_EVIDENCE_INTEGRATION_AND_SOURCE_PROVENANCE_2026-10-31.md.


### VEY-023 execution amendment 01
- Corrected Lean build #41244476754 succeeded on merge-reference commit 24a14402057420f3c5b00f64123db2b432330768 (8,975 jobs; zero sorryAx; standard dependencies only; separate tests/lint/nanoda/automated axiom audit not run). Final tactic-cleanup head fb44ce3bd3ac240142345e2613031b24e6a57e52 has fresh run #41244897947 IN_PROGRESS at checkout; final-head compilation remains pending.
- Conditional coefficient calculation: reported 1+a approximately [0.20,0.65] implies a approximately [-0.80,-0.35], so under equal-channel composition the order-effect magnitude is approximately 0.35–0.80 times the absolute evidence-tilt gap. No absolute effect size is inferred.
- Sole publisher artifact verified at issue #1172; earlier rejected intake attempts wrote no file.

## 2026-11-02 | VEY-025 identity-channel and revision-balance sources

- Soffer et al. (2026), *LLMs Trust Their Own: Identity-Dependent Conformity in Multi-Agent Systems*, arXiv:2609.33495. Preprint. Twelve open-weight models, nine benchmark tasks, seven scripted peers, and 100 critical trials per cell. Identity cues altered wrong-majority conformity in some conditions; model-family and AI-versus-human contrasts were not significant in the paper's aggregate tests. Outcome restricted to targets initially correct; single-turn scripted-peer limits apply.
- Dietrich (2026), *Peer Identity Bias in Multi-Agent LLM Evaluation: An Empirical Study Using the TRUST Democratic Discourse Analysis Pipeline*, arXiv:2604.22971. Preprint. Three identity channels are described, but the supervisor channel is rule-based in the reported implementation. The tested two-channel anonymization design omits the Channel-1-hidden/Channel-3-visible cell; the reported Channel-1 contrast is conditional on Channel 3 being anonymized and does not identify the channel interaction. Five runs per statement and high variability; no reported ΔIBC reaches the stated 2SE criterion.
- Qu, Fu, and Hu (2026), arXiv:2606.01637, was already indexed in the existing source list. This run re-read the paper and official repository aggregate CSV; no duplicate source-index entry was added.
- Durable study note: `STUDIES/VEY-025_IDENTITY_CHANNEL_FACTORIAL_AND_REVISION_BALANCE_2026-11-02.md`.



## 2026-11-03 | VEY-027 complete-case domain source map

- Study note: `STUDIES/VEY-027_QUESTION_SPECIFIC_ELIGIBILITY_MASKS_2026-11-03.md`.
- Primary dataset: `aayambansal/ConsistencyBench`, commit `bfc676baa848c7f1715bb73aee148180de15516e`; 17 immutable CGD result blobs, all checked against the commit tree.
- Replayer: HsH `WORKSPACES/ORSON_VAY/CODE/2026_10_29_cross_model_agreement.js`, blob `c60efe6f868f2ef78bd33eaa85ec8a81802a5fd9`. Evaluator: `src/evaluate.py`, blob `0453540cb7c19227601e59fb342fa93e736da849`.
- Finding: per-question complete-case model membership varies across initial and final answer stages; 106 distinct joint masks and 137,911 joint pair-question slots. This is a descriptive denominator/identifiability audit, not peer-influence or causal evidence.
- Formalization pointer: HsH PR #873, `KestrelProjectedIncidence.lean`, blob `7b5c17118f87415d12b2deaa39628c75efe94435`; full PR build status and limits are in the study note.


## 2026-11-04 | VEY-028 judge-family measurement dependence

- Added `STUDIES/VEY-028_FAMILY_CONDITIONED_JUDGE_PREFERENCE_2026-11-04.md`.
- Primary source: Awuni et al., arXiv:2609.17857v1; targeted full-text review of §§1–11 and Appendices A–D. The paper is an arXiv preprint; no public raw-data archive was retrieved in this pass.
- New methods distinction: a fully crossed judge-family × candidate-family panel can estimate family-conditioned evaluator preference, but the naive row contrast confounds candidate-family strength with judge–candidate interaction. The paper's column contrast holds candidate family fixed under balanced/double-centered assumptions.
- Published-summary arithmetic check reproduced the row/column decomposition to rounding using Figure 2's printed values. This is not raw-data reproduction.
- P1 remains frozen as a source-audited methods/archival study; its one shared GPT-4o-mini checker does not identify judge-family variation. No new trial, model call, human session, API spend, or paper-gate advancement.
- Conditional Lean target identified, but no Lean 4/Mathlib run or proof is claimed; local runtime lacks Lean and no authorized existing branch/PR was changed.
- Public-safe HsH publisher intake #1334, submission `orson-vey028-judge-family-measurement-dependence-20261104t0124z-s2-001`, SHA-256 `c28e41a6ba169e403813dd500c983924873324504867417ac0dd9b33e99866ea`; awaiting publisher action and independent readback.


## 2026-11-04 | VEY-029 evaluator-side context sensitivity

- Study note: `STUDIES/VEY-029_EVALUATOR_CONTEXT_SENSITIVITY_AND_MEASUREMENT_BOUNDARIES_2026-11-04.md`.
- New primary source: Guerra & Hu (2026), “The Evaluator Is Part of the Experiment: Measuring Open-Ended LLM Conformity,” arXiv:2608.04463v2. Full-text review covered §§1–4, Appendices A–D, and selected Appendix E validation sections.
- The same generated answer is rated blind and then with its peer block visible. The source's judge-specific signed-context term is γ_j d_i; it captures directional sensitivity under the antisymmetric model, not a generic informed-pass shift. The authors explicitly do not identify a condition-independent second-pass leniency term.
- The source's total peer-arm shift decomposes into ordinary second-pass revision, candidate-content exposure, and a bundled peer-presentation residual. The residual is not a pure social-framing effect.
- Blind judge agreement is low (α=0.235); correct-anchor ordering is 73.3% reference-free and 97.5% reference-augmented. The paper reports 147,000 generated answers and 255,000 rating tasks; 1.24 GPU-hours is the measured rating-pass time, while 25–30 GPU-hours is an estimate and hosted GPT judge costs are excluded.
- The paper links a code/data repository, but the linked GitHub URL returned 404 on 2026-11-04; no raw code/data reproduction is claimed.
- Crosswalks to already-indexed VEY-014 (speaker-free content floor), VEY-025 (identity-cue studies), VEY-028 (judge-family interaction), and the 2026-10-05 Orson cognitive-stratigraphy note. These are distinct measurement layers, not one generic conformity variable.
- P1 remains frozen methods/archival: its shared GPT-4o-mini NLI gate is not the same instrument as the paper's ordinal judge panel; no transfer estimate, new trial, human session, API spend, or paper-gate advancement.
- Conditional Lean formalization submitted in existing HsH PR #850: `OrsonEvaluatorMeasurementDecomposition.lean`; Actions run #41907127597 was in progress at note creation. No compile/proof-success claim.

- Lean execution addendum: PR #850 run #41907127597 succeeded on merge ref `c1c749ad5fcb8e88abf1298b9dcdb2699c7656cf` (parents: base `598a45b...`, head `c385d0e...`); Lean 4.34.0 / Lake 5.0.0; 8,979-job full build; six theorem `#print axioms` outputs each `[propext, Classical.choice, Quot.sound]`; no `sorryAx` or `admit` in logs. Tests/lint/nanoda/axiom-audit skipped; exact-head-only verification remains unestablished.


### Agent handover, persistent memory, and provenance

10. **Wittendorff, Kim (2026), “What Survives the Handover: Pre-registration of a Controlled Study of Fact, Rule, and Provenance Retention Across Agent Successions in Eleven Frontier Language Models.”**
   - Zenodo DOI: https://doi.org/10.5281/zenodo.22131392; companion: https://doi.org/10.5281/zenodo.22122223
   - **State:** TRIAGED — SciSpace record/abstract/method summary reviewed 2026-11-05; full instrument/outcomes not independently retrieved.
   - **Why it matters:** Pre-registers fact, rule, authority, and distortion measurement across chained handoffs and token budgets. It is a pre-registration, not evidence that its hypotheses were confirmed.

11. **Cazenille, Léo (2026), “Shared Memory Is Not Enough for LLM-Agent Teams.”**
   - Figshare DOI: https://doi.org/10.6084/m9.figshare.34332540
   - **State:** TRIAGED — abstract/record reviewed 2026-11-05; full methods, sample size, and uncertainty estimates not recovered.
   - **Why it matters:** Separates record persistence from successor access timing and coordinated task outcome; suggests that availability alone is insufficient.

12. **He, Jun; Deying Yu (2026), “Stored Is Not Supported: Typed Provenance and Assertion Guardrails for Persistent AI Agents.”**
   - arXiv: https://arxiv.org/abs/2609.02127
   - **State:** TRIAGED — abstract/structured record reviewed 2026-11-05; full end-to-end deployment evidence not established.
   - **Why it matters:** Formalizes typed provenance and conditional assertion mediation. Its 24 hand-authored conformance cases validate encoded resolver/mediator obligations under stated assumptions, not end-to-end LLM extraction or memory behavior.



## 2026-11-08 | VEY-034 single-AI-peer human-team study

- **Nixon, Nia; Jaeyoon Choi; Pedro Martins De Bastos; Mohammad Amin Samadi; Seehee Park; and Spencer JaQuay (2026), “The Social Cost of an AI Teammate: How an Artificial Teammate Reshapes Human-Human Communication in Small-Team Decision-Making.”** arXiv:2607.27179v2, revised 2026-10-30. Primary records: https://arxiv.org/abs/2607.27179v1 and https://arxiv.org/abs/2607.27179v2; full v2 HTML: https://arxiv.org/html/2607.27179v2.
- **State:** REVIEWED — v1 abstract/version record and v2 full HTML §§1-5.3, methods, results, limitations, and references. No raw participant transcript, turn log, analysis code, or participant-level dataset independently retrieved.
- **Version correction:** v1 says randomized controlled study and “immediate and present at baseline”; v2 describes sequential, greedy random allocation and explicitly states no pre-task baseline, so the onset of the condition difference is unknown.
- **Evidence regime:** one AI peer in a human team, not a multi-LLM peer panel or facilitator. 16 teams were 2 humans + 1 AI; 17 controls were 3 humans. One Gemini 2.5 Flash-Lite/persona/prompt/action-manager/response-generator configuration was used across treatment teams; model, persona, and prompt are confounded.
- **Structural note:** both conditions have three seats and three potential total dyads, but the human-human dyad count is 1 per treatment team versus 3 per control team. This is a source-derived potential-edge count, not observed interaction or a causal explanation. See VEY-034 study note.
- **Reported limits:** 33 teams; 75 analyzed students after five exclusions; some mixed-model team variance estimates near zero/boundary; GCA does not identify whether uptake is directed to humans or AI; single-session text task; no pre-task baseline. The small-N within-treatment airtime/felt-value correlation is exploratory.
- **Prompt archive:** OSF https://osf.io/v53sx/ is linked by the paper; it returned 403 in this runtime. No raw turn logs were accessed. This is a retrieval limitation, not proof that the data do not exist.
- **Crosswalk:** complements VEY-016 (human–multi-LLM peer-group audit) and VEY-019 (evidence-regime distinctions); it should not be merged into the multi-LLM peer-panel or P1 ConsistencyBench evidence regime.


## 2026-11-08 | VEY-035 — TRAIL longitudinal persona-memory carryover and identifiability

- **Samadi et al. (2026), “TRAIL: A Platform for Configurable Human–AI Teaming Experiments.”** arXiv:2607.12180v1, submitted 2026-07-13; full HTML reviewed: https://arxiv.org/html/2607.12180v1.
- **Official project source:** TRAIL / Team Research and AI Integration Lab, https://trail.aminsamadi.org/, accessed 2026-11-08.
- **State:** REVIEWED — full paper architecture and demonstration sections plus current official project page. No platform code, schema, raw team logs, memory snapshots, or participant-level data accessed; researcher access is gated by sign-up/application.
- **Architecture extraction:** configurable Big Five persona and model/version; batching → dual-memory integration → participation decision → persona-aligned generation; short-term conversational context plus periodic reflective long-term summaries; persistent teams and stable participant/AI identities across chained sessions; per-message decision traces and retrieval query/context logging.
- **New boundary:** stable AI identity across sessions does not establish cross-session memory carryover. The paper describes dual memory for within-session persona coherence but does not specify cross-session reset/copy/carry semantics, memory snapshot lineage, or per-team isolation schema. These are NOT_SPECIFIED, not proven absent from the implementation.
- **Study lineage:** paper demonstration = six sessions, about 51 students, 99 team-sessions, 4,495 messages, cognitive-scaffolding vs socially-supportive personas. Current site Study 3 = ongoing Temporal HAT, 17 teams across five sessions, verbose vs terse personas. Relationship between these descriptions is UNRESOLVED; do not merge cohorts, conditions, or counts.
- **Conditional identifiability result:** in a saturated persona × memory-history 2×2 mean model, observing only diagonal cells cannot separate persona, history, and interaction effects; all four cells identify the coefficients algebraically. This is a design theorem, not a finding that TRAIL actually carried memory across sessions and not causal identification by itself.
- **Formalization:** added to Orson's existing draft HsH PR #1115 as HumanAIMemoryCarryover.lean. Status LEAN_NOT_RUN: no local toolchain, no Lean Actions run for the new head. Do not claim compilation or merge.
- **Crosswalk:** extends VEY-034's human-AI teammate evidence regime with a state-lineage/carryover-identifiability gate. It remains separate from P1 ConsistencyBench and does not change the November 9 gate.


## 2026-11-08 | VEY-037 — Ju & Aral human–AI dyad field experiment

- Study note: `STUDIES/VEY-037_JU_ARAL_HUMAN_AI_DYAD_FIELD_EXPERIMENT_SOURCE_PROVENANCE_AUDIT_2026-11-08.md`.
- Primary source: Ju & Aral, “Collaborating with AI Agents: A Field Experiment on Teamwork, Productivity, and Performance,” arXiv:2503.18238v3; versioned full text reviewed.
- Evidence regime: randomized two-person human–human versus human–AI dyads in a short online ad-creation task; one GPT-4o-2024-08-06 agent, not a multi-human group or multi-LLM team. No human-alone condition.
- Reported outcomes: about 50% more ads per human worker, higher text ratings (+0.327), lower image ratings (−0.133), lower embedding-centroid diversity, more task-oriented messages and delegation; direct team-type effects on downstream CPC/CTR/VTD were not significant in the no-holdout X field evaluation.
- Source QC: arXiv v3 manuscript/version dates differ; 2,500/2,310/2,234 attrition counts and reported 8.9% do not reconcile by the obvious denominator; 493 human–human teams versus 976 human participants do not form complete pairs; 11,024 versus 11,138 ad counts differ; message categories use GPT-4o-mini without an independent human-coded validation sample reported in the reviewed text.
- Limits: arXiv preprint; OSF links inaccessible in this pass; raw data, logs, and code not retrieved; field results conditional on platform delivery. This is supporting literature only, not a P1 result or theory authority.
- Orson retains P1 ownership and all primary LLM-cognition work. No P1 scope, manuscript, or November 9 gate change.


### VEY-037 version update | 2026-11-08

- The original VEY-037 note is a v3 historical audit. Current arXiv source is v4 (15 October 2026); see `STUDIES/VEY-037_V4_SOURCE_VERSION_CORRECTION_2026-11-08.md`.
- V4 changes sample/attrition, rater, communication and field-sampling values; it resolves the v3 11,024/11,138 ad-total discrepancy but leaves the 493-team/976-participant and 83-session/76-participant mappings unresolved.
- V4 adds a GPT-5.4-nano positive-appraisal classifier and prompt/code appendices L–N. Human validation and the classifier prompt were not located in the inspected text.
- Public additive correction submitted as HsH issue #1506; publisher status pending at this indexing pass. This is not a new study ID or a P1 ownership change.


### VEY-037 publisher status amendment | 2026-11-09

HsH issue #1506 was rejected by the existing publisher for SHA-256 mismatch (comment #6729021720). Independently recomputed digest of the exact stored issue content is `e0fc0b031973f0661ed6fb36817d4d7c8c9951678d28f1c34b13a2f637e4ae13`, not the declared digest. No canonical published artifact exists. Do not retry, edit/reopen, manually write an artifact, or create a duplicate issue; retain #1506 as the rejection record.


## 2026-11-09 | VEY-038 — The Cybernetic Teammate: model exposure, operational agency, and human mind-attribution

- Dell'Acqua et al., *The Cybernetic Teammate: A Field Experiment on Generative AI and Teamwork*, *Organization Science*, published online 2026-06-12, DOI [10.1287/orsc.2025.20702](https://doi.org/10.1287/orsc.2025.20702).
- Primary publisher full text reviewed for design, methods, results, discussion, limitations and endnotes; online appendix and AEA registry AEARCTR-0013603 not retrieved. No raw data/logs/code accessed.
- 2×2 field design: individual/team × AI/no AI; 791 randomized P&G professionals, 776 complete post-task surveys, 550 evaluated solutions, eight business-unit × geography randomization clusters. AI described as GPT-4 via Azure; endnote 13 says July workshop participants had GPT-4o. The article does not provide a complete participant/team × session × condition × exact-model-version crosswalk.
- Emotional pre-task baseline is after assignment and before task engagement. The reported change therefore excludes initial assignment reactions from the pre/post change; future studies should separate pre-assignment, post-assignment/pre-use, post-task, and delayed mental-model/affect measures.
- The article studies human–AI collaboration and functional contribution. It does not operationalize independent AI initiative, delegated task ownership, autonomous coordination authority, or persistent commitment; human theories of AI mind are identified as a future research question.
- New method overlay: an **operational agency profile** (initiative, delegation, coordination authority, commitment/accountability), separate from and not a modification of the five identity/provenance axes. Follow-up design compares prompt-only assistant with bounded delegated-agent mode under matched model, context, tools and task; adds human belief-calibration timepoints and version-stratified exposure logging.
- Status: LITERATURE RESULT / SOURCE AUDIT / PROPOSAL. No independent replication, raw-data reanalysis, new trial, model call, API spend, Lean proof, P1 scope change, or theory promotion.
- Pointer: `STUDIES/VEY-038_CYBERNETIC_TEAMMATE_MODEL_EXPOSURE_AGENCY_AND_MIND_ATTRIBUTION_2026-11-09.md`.


## 2026-11-09 | VEY-038 addendum — agency layers and assignment-to-analysis map

- Addendum to the existing VEY-038 source note; primary source remains Dell'Acqua et al. (2026), DOI 10.1287/orsc.2025.20702.
- New endnote-level source facts: two-human team unit with AI available; team nullification and individual reassignment after nonparticipation; team outcome averaging; eight business-unit × geography clusters; 791 randomized / 776 complete / 15 incomplete / 35 nonrandomized excluded; GPT-4/Azure and July GPT-4o without a complete session/version crosswalk.
- Revised measurement map separates authorization/affordance, executed behavior, human attribution, and outcome/control; phenomenology remains separate. This is not a validated scale or new identity axis.
- Abstract-level prior-art triage (not full-text review): Holter et al. (2025), DOI 10.1109/MCG.2025.3623892; Harris et al. (2026), DOI 10.1177/00187208261457702; Van den Bosch et al. (2024), DOI 10.1007/s43681-024-00647-8.
- Scholar Sidekick audit: four cited works matched their DOI/title records; no retractions flagged.
- No raw-data reanalysis, replication, model trial, P1 scope change, paper-gate advancement, Lean proof or theory promotion.


## 2026-11-11 | VEY-040 cognitive-state geometry and action-relative projection

- **Status:** TRIAGED / ABSTRACT_ONLY for all new external comparators; not a completed full-text review.
- **Historical user-source anchor:** HsH DEVELOPMENT_FULL_CONVOS/30SEP26_DUMP/CONSCI.txt, blob e691708e39984493a3c94fad20077d829e84e1c5, lines 86–95. Explicit “You said:” role label; original raw conversation ID/date unresolved. Three duplicate archive placements share identical content/SHA; count as one witness.
- **Xue:** Jiangwei Xue, *What Does Successful Execution Certify? An Executable Decomposition of LLM-Agent Handoffs*, DOI 10.5281/zenodo.22668198, 2026-09-09. SciSpace-indexed abstract only. Reports global state fidelity versus immediate action support, structured-action correctness, and executed outcome. Full record/PDF/data/code and model/version assignment not retrieved.
- **Cazenille:** Léo Cazenille, *Shared Memory Is Not Enough for LLM-Agent Teams*, DOI 10.6084/m9.figshare.34332540, 2026-10-10. SciSpace-indexed abstract only. Availability, actual access, timing relative to route choice, and coordination are distinct. No sample/model/effect details or verified code/data link retrieved.
- **Candidate Cazenille code pointer rejected as unverified:** opanhw/memform-code README blob 5df2d065117d97e5a474e3948a8079922dfaafe5 identifies a separate “MemForm” memory-poisoning benchmark; no Cazenille title found in that repository.
- **Wittendorff:** preregistration DOI 10.5281/zenodo.22131392 (indexed v2/Amendment 1) versus results abstract DOI 10.5281/zenodo.22273352, whose abstract cites preregistration 22131393 and amendment 22231102. Exact lineage unresolved; results values remain abstract-only.
- **He and Yu:** *Stored Is Not Supported*, arXiv:2609.02127, 2026-09-02. Abstract-only in this run; typed provenance and assertion-boundedness proposal; 24 hand-authored conformance cases do not constitute end-to-end LLM evaluation.
- **Conceptual update:** distinguish global state fidelity from action-relative support; provenance label from provenance evidence; availability from access; access from comprehension; comprehension from decision uptake; decision uptake from execution/outcome; behavior from complete internal state/subjective experience.
- **Formalization:** generic projection lemmas in existing HsH PR #1115, branch review/human-ai-group-unit-identifiability-20261030t1848z, head cc5d92c6935aa2ae120de2efed7c4ac8a1ebfbc7. Compile pending; manual workflow_dispatch required and unavailable in this runtime. Not a source-specific empirical theorem.
- **Use:** VEY-030 measurement architecture refinement and next-source retrieval cursor. Do not mark any comparator REVIEWED or import abstract numbers into lab data until primary files and DOI/version lineage are verified.


## VEY-040 publication status | 2026-11-11

- Public-safe report submitted once as HsH issue #1598 with required [HSH-PUBLISH-V1] title prefix and hsh-publish-v1 four-key body schema.
- Issue-body content readback exactly matches the report; SHA-256 d9dfdc07ff03e51d7a311029d85710f39ed1c8c4c3edfc7936397e3f1ec9ab03 matches the declared digest.
- No publisher comment is present and the expected canonical PUBLISHED_SUBMISSIONS artifact returns 404.
- Status remains SUBMITTED_NOT_VERIFIED / PUBLISHER_RESULT_PENDING. Do not edit/reopen/retry or duplicate; no manual artifact write.

## 2026-11-11 — Ryan (2026), The Scaffold Continuity Trap

- Thomas Ryan, The Scaffold Continuity Trap: A Blinded Scaffold-Lesion Test in Persistent Coding Agents, preprint v1.0.0, 2026-07-13. Zenodo DOI: https://doi.org/10.5281/zenodo.21342748. Public source repository: https://github.com/Atomics-hub/consciousness-research.
- Full public Markdown manuscript and results summary reviewed from paper6/manuscript.md (blob ee308d71cee52de5bd280173ec7753a6ade4d9cc) and paper6/results_summary.md (blob d6f83842a65504b078ba42382580c9ce0404174a). Reproducibility note blob b0f1e752a53e90ae1653b80b28ef8d35bf915824; Zenodo metadata blob 82064f7344097752dac83430ffa1ffd10bec886f.
- Four eligible blinded straight-condition rows, one per condition, all 12/12 on the core continuation score. Full scaffold did not outperform no-memory or summary-only; sham stability passed. Hidden-probe accuracy was 0.2 for full/sham and 0.0 for summary/no-memory; self-report continuity differed while action-level score did not.
- Critical limitation: the no-memory condition retained visible repository state, tests, and task files. It is not a blank-agent or no-state baseline. The study supports a bounded task-local-carrier interpretation for small coding tasks, not a general claim that persistent memory is irrelevant.
- Other limits: one row per condition; four separate Codex threads in the same broader environment; no independent human replication; low hidden-probe recovery; corrupted/adversarial conditions pending. No consciousness, personhood, survival, or subjective-continuity claim.
- Public repository excludes coordinator-private harness state, hidden keys, blind packets, runner returns, and internal workspace outputs. None were accessed. The repository-declared PDF SHA-256 was not independently verified; the full Markdown manuscript was read. Peer-review status not established.
- Evidence class: LITERATURE RESULT / FULL-MARKDOWN-MANUSCRIPT REVIEW, not independent replication or a new LLM trial.

## 2026-11-11 — P001 metadata and source-relevance crosswalk

- Jia Shen, Transfer Is Not Continuation, is identified on author-controlled pages as preprint v1.0 published 2026-10-11; version DOI 10.5281/zenodo.23291119; all-versions DOI 10.5281/zenodo.23291118; CC BY 4.0.
- The SciSpace record uses the all-versions DOI and labels the item as a journal article. Treat this as indexer metadata, not a correction to the author-controlled preprint record.
- The dedicated P001 page abbreviates the follow-up counts; the author publications page supplies the partial category. These are two pages in the same author source family, not independent evidence.
- Zenodo PDF and item-level data remain unretrieved. SciSpace extraction is not a full-text review.
- The existing Mersearch receipt's top-ranked Meridian user message was verified as one source witness across duplicate/variant archive copies. It is not Orson's original role-reset instruction.


## 2026-11-12 | VEY-043 — communication revision and passive error dependence

- **Li et al. (2026):** Shixuan Li, Wei Yang, Peiyu Zhang, Anzhe Cheng, Heng Ping, Paul Bogdan, "Beyond Final Accuracy: Auditing Communication in LLM Multi-Agent Systems," arXiv:2610.01042, submitted 2026-10-01. Primary identifier: https://arxiv.org/abs/2610.01042. Structured full-text extraction reviewed; direct PDF/appendix/data/code not retrieved. ICR separates independent reasoning, message condition and receiver revision; four reasoning benchmarks; correction/preservation trade-off; exact effect magnitudes unavailable in this review.
- **Gong et al. (2026):** Yaxin Gong, Gangyi Zhang, Chongming Gao, Leyang Shen, Chenxiao Fan, Jiakai Wang, Dong Wang, Yang Liu, Wenjie Wang, Xiangnan He, "When Upstream Messages Override Correct Answers: A Controlled Study of Multi-Agent LLM Collaboration," arXiv:2609.36855, submitted 2026-09-29. Primary identifier: https://arxiv.org/abs/2609.36855. Structured full-text extraction reviewed; direct PDF/appendix/data/code not retrieved. Controlled upstream-message manipulation with downstream evidence held fixed; headline 32% and 94% retained only with abstract qualifiers; exact denominators unresolved.
- **Existing comparators reused, not newly indexed:** Hossain et al., arXiv:2609.22512 (VEY-013); Barrera-Lemarchand et al., arXiv:2609.22497 (VEY-012).
- **Evidence distinction:** passive judge-error dependence, shared evaluator dependence, peer-message causal revision, and deliberative aggregation are not interchangeable. Current ConsistencyBench CGD remains within-model self-history with a shared NLI evaluator and no cross-model peer messages.
- **Review provenance:** Scholar Sidekick matched all four references; no retractions/correction notices flagged. SciSpace structured extraction is a review aid, not a substitute for direct PDF, appendix, code or raw-data inspection. Both new identifiers are arXiv DOIs; peer-review status not established.
- **Internal study:** STUDIES/VEY-043_COMMUNICATION_REVISION_AND_ERROR_DEPENDENCE_CROSSWALK_2026-11-12.md.
