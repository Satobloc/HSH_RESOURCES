# VEY-019 — Five Evidence Regimes and Consensus Measurement Audit

**Date:** 2026-10-31 06:12Z  
**Status:** COMPLETE-AS-STAGE — source-grounded synthesis, primary-source checks, published-count arithmetic, Mersearch provenance audit, and exact-head Lean CI verification.  
**Evidence class:** LITERATURE SYNTHESIS + SOURCE/MEASUREMENT AUDIT + CONDITIONAL FORMALIZATION QA.  
**Owner lane:** Vey Cognition Lab / Orson Vay. This is repository work, not an authenticated continuation of an original Orson ChatGPT thread.

## Executive result

The literature now contains at least five distinct empirical or analytical regimes relevant to consensus and collective cognition. They should not be collapsed into a single “multi-agent consensus” evidence class:

1. Correlated LLM-judge errors without peer interaction (Kohli).
2. LLM groups replaying human deliberation (Shao).
3. Mixed human–LLM populations interacting as peers through repeated pairwise exchange (Chen).
4. Human-only group deliberation with engine-scored decision quality (DeliChess).
5. Human groups with a designated LLM facilitator (Alsobay).

The current ConsistencyBench archive is a sixth, narrower object: passive cross-model outputs evaluated through a shared question-blind checker, with a post-hoc panel majority. It is not a peer-exposure or shared-source intervention.

The key methodological conclusion is that **convergence, correctness/quality, error dependence, peer exposure, participation, evaluator dependence, source lineage, and replication unit are separate observables**. Consensus alone does not identify truth, independent information, causal influence, or cognitive ownership.

The original answer-keyed neutral-versus-false-authority test bank remains **UNRECOVERED**. No model trial, human-subject experiment, or P1 manuscript has been created in this pass.

## 1. Evidence regimes

### 1.1 Correlated LLM judges: Kohli (2026)

**Primary source:** Guneet Kohli, “Nine Judges, Two Effective Votes: Correlated Errors Undermine LLM Evaluation Panels,” arXiv:2605.29800v1, 28 May 2026.  
https://arxiv.org/abs/2605.29800  
Full HTML: https://arxiv.org/html/2605.29800v1

The paper studies nine judges from seven model families on three ChaosNLI datasets and RewardBench. For MNLI, it reports mean pairwise error phi = 0.391, Kish n_eff = 2.18 [2.07, 2.31], eigenvalue n_eff = 2.16, and a 24.2% independence ratio. The nine-judge panel scores 72.0%, barely above the best individual at 71.8%; its item-aware Condorcet prediction is approximately 94%, a 22.0 percentage-point gap.

The paper explicitly says the Kish expression assumes approximate exchangeability and compares it with an eigenvalue diagnostic that does not. The pairwise phi range is 0.161–0.603, so the panel is not literally equicorrelated. The effective-sample-size interpretation is a design-effect summary of these judges’ binary error vectors on these items, not a literal count of independent cognitive agents and not a universal panel constant.

**Reference-label qualification:** the “gold” label is the majority of 100 human annotations. The paper itself notes that, on high-entropy items, this can be a plurality preference rather than a uniquely correct answer. The bootstrap interval captures item-sample uncertainty for this selected panel, not judge-selection uncertainty. The paper also reports 28 tied top labels across its three datasets; the underlying ChaosNLI tie resolution uses Python Counter insertion order, with a sensitivity check reported.

### 1.2 LLM replay of human deliberation: Shao (2026)

**Primary source:** Tengfei Shao, “Language-model groups overstate consensus when replaying human deliberation on a reasoning task,” arXiv:2609.20543v1.  
https://arxiv.org/abs/2609.20543  
Full-text mirror inspected: https://www.conceptio.app/document/978469/language-model-groups-overstate-consensus-when-replaying-human-deliber

The study replays 100 held-out DeliData Wason groups with one agent per human participant. The chat and reasoning conditions are two inference settings of the same served DeepSeek build, not independent model replications. Agents are force-elicited for final answers; the human carry-forward tracker retains a silent participant’s last answer. The paper therefore distinguishes 24.0% human full consensus under carry-forward scoring from 52.0% using submitted answers and 57.0% among participants who posted, versus 86% chat and 96% reasoning agent consensus in the primary replay.

Participation-matched comparisons are post-unblinding sensitivity analyses, not the preregistered confirmatory endpoint: among 45 all-participant groups, human consensus is 51.1%, versus 85.2% chat and 95.6% reasoning. A second submit-based route over 98 groups gives similar gaps but does not fully equalize endpoints.

On the isomorphic Wason task, 74.0% of all reasoning-mode groups reach consensus on a wrong answer and 24.7% on a correct answer. The no-peer diagnostic hides messages on the classic task only; it is not a general causal account of over-convergence. The paper explicitly labels the “beliefs as revisable premises” explanation a hypothesis.

This is evidence about simulation fidelity and endpoint alignment, not a new human experiment or a general theory of LLM group cognition.

### 1.3 Mixed human–LLM peer population: Chen et al. (2026)

**Primary source:** Lin Chen, Ziyi Liu, Xia Hu, and Yong Li, “AI agents reshape consensus formation in human groups,” arXiv:2609.02122v1, first posted 2 September 2026.  
https://arxiv.org/abs/2609.02122  
Public figure-reproduction repository: https://github.com/tsinghua-fib-lab/human-ai-consensus

This is a direct mixed human–LLM peer-participant study as reported. Participants occupy 24-member populations and repeatedly describe the same tangram over 40 rounds of randomized pairwise communication. The eight reported conditions sum to 127 human participants and 65 LLM-agent slots, 192 seats total. Because each session is reported as 24 members, the counts strongly imply one session per condition; the paper does not separately state a replicated session count. Treat this as a source-level inference, not a verified design fact.

The main model is Qwen2.5-VL-32B-Instruct, with a smaller 7B comparison. The primary consensus score is embedding similarity using all-MiniLM-L6-v2, which is also used for the feedback/payoff shown during the task. This is semantic convergence under the task’s own feedback metric, not independent truth, factual accuracy, or decision quality. The experiment uses one tangram stimulus, random pairings, and one model family at two sizes. The public figure-reproduction package does not expose per-agent request IDs or separate context histories.

The earlier VEY-016 audit records that the processed A2–A5 files are pickle files, not CSVs. Its prior row-count reconciliation was not re-extracted in this pass and is not presented here as a fresh data reproduction.

This study closes any broad claim that mixed human groups with multiple LLM peer participants have never been studied. It does not establish independently replicated group-level treatment effects, auditable per-agent context ancestry, independent primary-outcome adjudication, cross-family replication, or unrestricted group-chat dynamics.

### 1.4 Human-only deliberation with external decision scoring: DeliChess (2026)

**Primary source:** Xiaochen Zhu et al., “DeliChess: A Multi-party Dialogue Dataset for Deliberation in Chess Puzzle Solving,” arXiv:2606.04987v1.  
https://arxiv.org/abs/2606.04987

The dataset contains 107 human dialogues, 7,667 genuine utterances, and 365 distinct active-speaker identifiers. Each dialogue covers three puzzles, producing 321 dialogue–puzzle cases; the 321 cases are nested within 107 dialogues, not 321 independent groups. Stockfish 17.1 supplies an external move-quality ranking.

Mean group reciprocal-rank performance rises from 0.473 to 0.552 after deliberation, Δ = 0.079, 95% CI [0.051, 0.108]. The 321 cases are heterogeneous: 157 improve, 50 are unchanged, and 114 decline. Among cases where final modal share increases, 143 have positive RR gain and 102 have negative RR gain. Thus 41.63% of the increased-modal-share cases still lose RR quality. Modal share is not unanimity, and neither is a substitute for the engine-scored outcome.

Strict assembly occurs in 19 of 162 eligible cases (11.73%); 11 of those 19 end with the Stockfish-best candidate as the unique final mode. The paper’s process-feature associations are descriptive: no annotation-proportion feature has a reliable independent association after adjustment for dialogue length and baseline RR. The study reports one final annotation per dialogue; its 12-dialogue reannotation is a targeted audit, not corpus-wide independent annotation. Fine-grained process analyses are explicitly non-causal.

This is a human-human deliberation benchmark with an objective engine-scored outcome, not an LLM peer-group experiment.

### 1.5 Human groups with a designated LLM facilitator: Alsobay et al. (2026)

**Accessible primary preprint:** https://arxiv.org/abs/2508.08242  
**Reported publication:** PACM HCI 10(6), CSCW059, DOI 10.1145/3816907.

The study includes 1,475 participants in 281 five-person groups, with 70 groups per condition, and a GPT-4o facilitator. It is a replicated human-group experiment with an LLM facilitator, not a multi-LLM peer population. The prior VEY-016 audit reports increased unique factual information sharing but no significant improvement in optimal decision rate. Use the accessible arXiv preprint as the independently inspectable source; journal-page access was not independently confirmed in the earlier audit.

### 1.6 Current ConsistencyBench P1 evidence

The archived evaluator source blob 0453540cb7c19227601e59fb342fa93e736da849 supports a passive cross-model answer-panel interpretation. A common question-blind GPT-4o-mini NLI checker compares same-model raw answers; other models’ answers are not fed to the models; the panel majority is post-hoc. This supports an evaluator/source-pipeline audit, not causal peer influence, shared-source exposure, or deliberative revision.

## 2. P1 measurement stack: do not collapse the constructs

| Construct | What is observed | What it does not establish by itself |
|---|---|---|
| Convergence | Similarity, modal share, unanimity, consensus rate | Correctness, truth, quality, or independent information |
| Correctness / decision quality | Answer key, human adjudication, engine score, task outcome | Why a group converged or whether interaction caused improvement |
| Error dependence | Correlation of judge error indicators; effective sample size | Number of independent “minds” or independence on another task |
| Peer exposure / influence | Which participant saw which message, when, and what changed afterward | Causal influence without a controlled exposure contrast |
| Participation / missingness | Passes, nonresponse, carry-forward, forced final answer | Equivalent endpoints across groups with different participation |
| Evaluator / measurement coupling | Shared checker, shared embedding/reward model, post-hoc majority | Independent validation of the outcome |
| Source lineage / agent state | Model/version, prompt, evidence bundle, context ancestry, request IDs | Independent replication unless state and exposure are actually separated |
| Replication unit | Group/session, participant, round, utterance, agent slot | Independent sample size when nested observations are counted as groups |

A suitable future design should separately log initial answer, evidence/source bundle, prompt/model version, peer-visible messages, exposure order, participation/pass state, post-exposure answer, group/session identity, and an outcome adjudicator independent of the intervention feedback. Group/session is the independent treatment-replication unit when the intervention is assigned at group level; turns, utterances, and agent slots are nested observations.

## 3. Scripted arithmetic checks from published summaries

The following checks use published rounded inputs/counts, not raw-data reanalysis.

- Kohli rounded-input Kish value: 9 / (1 + 8 × 0.391) = 2.180232558, matching the reported 2.18 and the exact rational 375/172 in the Lean module. The reported eigenvalue estimate is 2.16.
- DeliChess RR case counts: 157/321 improve (48.91%), 50/321 unchanged (15.58%), 114/321 decline (35.51%).
- Increased-modal-share subset: 102/(143+102) = 41.63% have negative RR gain.
- DeliChess strict assembly: 19/162 = 11.73% of eligible cases; 11/19 = 57.89% produce the Stockfish-best candidate as unique final mode.

Reproduction snippet:

~~~python
from fractions import Fraction

k = 9
phi = Fraction(391, 1000)
kish = Fraction(k, 1) / (1 + (k - 1) * phi)

rr_up, rr_same, rr_down = 157, 50, 114
modal_up_positive, modal_up_negative = 143, 102

print(float(kish))
print({"RR_up_pct": 100 * rr_up / 321,
       "RR_same_pct": 100 * rr_same / 321,
       "RR_down_pct": 100 * rr_down / 321,
       "negative_RR_given_modal_share_increase_pct":
           100 * modal_up_negative / (modal_up_positive + modal_up_negative)})
~~~

No uncertainty interval was recomputed from raw observations. The published DeliChess confidence interval and Kohli bootstrap interval remain the source values.

## 4. Original test-bank provenance audit

The completed Mersearch request orson-cognition-bank-source-recovery-20261030-2236 has a verified run manifest and compact receipt, but its detailed raw result collection remains withheld. The request returned 718,805 hits over 608 paths. Its most frequent broad terms were name:*OV* (515,754) and path:*ORSON* (108,787), together 86.89% of hits. Target-specific counts were sparse: answer key 20, matched cognition 2, false-authority 2, test bank 2, authority framing 1. These counts may overlap; they are not distinct-source counts.

A raw JSON audit of the Mersearch sample locators found that the cited SAT Overview — raw.json locator d2abbdc8-1794-41ba-8e11-a6f111a6617e is a tool-role message, not a Nathan Direct user message. The 224 user-role messages in that raw conversation contain no direct user message matching the target neutral/false-authority/answer-key/test-bank phrases. The inspected Orson Free Build — raw.json export likewise did not reveal the target bank. This is a bounded source-fidelity correction, not proof that the bank is absent elsewhere. File/path-level search hits must not be treated as message-level author verification.

The role-charter pointer to OV-49–OV-53 remains mismatched: those located artifacts are geometry/finite-core work. OV-54 is an assistant-authored review note saying a proposed test was prepared but not executed. OV-55/56/OV-100 are analytical or synthetic models. OV-95 is a separate 24-case artifact-presence calibration protocol, not the requested neutral-versus-false-authority answer-keyed bank. Do not substitute these artifacts or silently edit the charter pointer.

**Disposition:** original neutral-versus-false-authority answer-keyed bank **UNRECOVERED**. The exact raw October 9 role-reset user message and its originating conversation/message UUID also remain unverified; the current role charter and October 26 direct reinforcement are live controls, not substitutes for that missing original source.

## 5. Conditional Lean result: exact-head CI verified

Existing HsH PR #850 now has a successful exact-head build:

- PR head: d59a17b270df730e84edbd614eaea3b1b76166e2.
- Exact-head workflow run: 41160835210.
- Job: 124417786006.
- Lean 4.34.0 / Mathlib v4.34.0.
- Full build: 8,973 jobs, success.
- Module: FORMAL_VERIFICATION/HsHVerification/OrsonKishEffectiveSampleSize.lean.
- Module blob: 2e5083fe61ebe121b48b2be70c007ec59ee47e08.

The module proves the Kish design-effect identity under equal marginal variance and common off-diagonal correlation, bounds the effective sample size for correlation in [0,1], and checks the rounded k=9, phi=0.391 example exactly. Its eight named theorem targets have theorem-specific #print axioms output; no sorryAx appears in the full job log. The reported dependencies are standard Lean axioms (propext, Classical.choice, Quot.sound). Automated tests, lint, nanoda and the separate axiom-audit stages were skipped.

This is a genuine compiled conditional mathematical result. It does not calculate phi from the nine judges’ raw outputs, establish empirical exchangeability, validate the underlying dataset, or prove that the panel contains literally two independent cognitive agents. The equal-variance/common-correlation model is the formalized condition; the paper’s empirical exchangeability claim remains an interpretation supported by its separate eigenvalue diagnostic.

PR #850 remains draft/unmerged. No new Lean code or PR was created in this pass.

## 6. P1 disposition and next gates

- P1 issue #564 remains **SOURCE / EXPERIMENT READINESS**, target 9 November 2026.
- The protocol freeze remains 2 November 2026.
- No authorized model-inference route or original answer-keyed bank was recovered.
- No model calls, human participants, new trial, power calculation, P1 manuscript, PDF/reader, or independent hostile review occurred.
- If the original bank and an authorized trial route are not recovered before the freeze, the defensible P1 route is an explicitly limited archival/methodological paper. It must not claim the missing neutral-versus-false-authority experiment was administered.
- Do not calculate power or prescribe group counts without pilot variance or suitable empirical estimates.
- P2 (30 November) and P3 (14 December) are unchanged. No paper gate advanced.

## 7. Next source cursor

1. When a Mersearch lane is genuinely free, run a narrow query without broad name:*OV* / path:*ORSON* OR clauses; preserve the raw manifest and record-level author/message IDs.
2. Recover the exact October 9 role-reset raw conversation and the original D1 TeX/PDF/reader source chain.
3. Keep OV-95 as its own artifact-presence protocol; do not relabel it as the missing authority-framing bank.
4. At the 2 November freeze, record the P1 scope decision explicitly. If the bank/authorized trial path is still absent, keep P1 methodological and archival.
5. Preserve the successful PR #850 exact-head CI receipt; do not duplicate the run or merge the draft without the existing review gate.

## Source register

- Kohli 2026: https://arxiv.org/abs/2605.29800 ; https://arxiv.org/html/2605.29800v1
- Shao 2026: https://arxiv.org/abs/2609.20543 ; OSF preregistration cited by paper: https://osf.io/5jp7s
- Chen et al. 2026: https://arxiv.org/abs/2609.02122 ; code/data: https://github.com/tsinghua-fib-lab/human-ai-consensus
- DeliChess 2026: https://arxiv.org/abs/2606.04987 ; dataset: https://huggingface.co/datasets/SpaceHunterInf/DeliChess
- Alsobay et al.: https://arxiv.org/abs/2508.08242 ; DOI 10.1145/3816907
- Existing source audits: VEY-014, VEY-016, VEY-017, VEY-018 in this lab.
- Existing P1 publisher record: HsH issue #1132, already PUBLISHED_VERIFIED; no duplicate submission made.
