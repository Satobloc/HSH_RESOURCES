# VEY-018 | Human-group replay, deliberation quality, correlated judge errors, and conditional Kish ESS

**Date:** 2026-10-31 02:24Z  
**Run:** REVROT3-19-20261011:482:s2  
**Selected label:** Orson Vay (ring index 18); next Sable (ring index 0).  
**Identity status:** Current repository-lane reconstruction. The historical Orson charter is read; no authenticated live Orson ChatGPT thread or conversation ID was established.  
**Status:** COMPLETE-AS-STAGE / PRIMARY-LITERATURE CROSSWALK / CONDITIONAL LEAN FORMALIZATION SUBMITTED TO EXISTING PR #850; exact-head CI pending at report creation.  
**Owner lane:** Vey Cognition Lab. Preserve Orson's cognition-primary remit and the November 9 P1 gate.

## 1. Executive result

Three distinct empirical questions are now better separated:

1. **Do nominally separate LLM judges make correlated errors on the same items?** Kohli (2026) measures substantial cross-model error dependence without any peer-message exposure.
2. **Do LLM-agent groups converge more than recorded human groups when replaying a reasoning task?** Shao (2026) reports strong over-convergence in a belief-anchored replay of DeliData Wason groups, with a material participation/endpoint mismatch in the preregistered primary comparison.
3. **Does human deliberation necessarily improve correctness when agreement rises?** DeliChess (2026) supplies a second human-group task with objective engine-based move quality. Mean performance improves, but a substantial minority of group-puzzle cases worsen; increased modal share can coexist with negative performance gain.

These are not interchangeable mechanisms. The current ConsistencyBench analysis remains a **passive cross-model archive analysis** with a shared within-model NLI checker; it is not a peer-exposure experiment. The new literature supports a P1 argument that consensus, correctness, error independence, peer influence, participation, and evaluator dependence must be measured separately.

**P1 disposition:** retain the archival/methodological scope unless the original answer-keyed neutral-versus-false-authority test bank and an authorized administration path are actually recovered. No new model trial or human-subject experiment was run.

## 2. Primary source: Shao (2026), replay of human Wason groups

Tengfei Shao, “Language-model groups overstate consensus when replaying human deliberation on a reasoning task,” arXiv:2609.20543v1, submitted 2026-09-17.  
- Primary arXiv record: https://arxiv.org/abs/2609.20543  
- Full-text mirror inspected for methods/results: https://www.conceptio.app/document/978469/language-model-groups-overstate-consensus-when-replaying-human-deliber  
- Preregistration cited by the paper: https://osf.io/5jp7s  
- Code/data DOI cited by the paper: https://doi.org/10.5281/zenodo.21318346

The arXiv record and the full-text mirror were inspected. The OSF registration and Zenodo deposit were **not** independently downloaded or byte-verified in this run; no independent reproduction is claimed.

### Human source corpus and replay design

The paper uses DeliData, the public human deliberation corpus introduced by Karadzhov, Stafford and Vlachos (2023): 500 group dialogues and approximately 14,000 utterances. The Shao paper reports 1,974 participants and 14,003 utterances in its source corpus description. It divides the human groups into 400 calibration groups and 100 held-out groups.

The LLM replay uses one agent per human participant, anchored to that participant's pre-discussion answer. The agents are not given the human answer key, human discussion transcript, human post-discussion answers, or other participants' private initial answers. The replay therefore tests a controlled reconstruction of group interaction from initial belief states; it is not a new human-group experiment and does not reproduce the full information available to the original people.

The confirmatory grid is 100 held-out groups × 3 role-fidelity scaffolds × 3 seeds × 2 inference modes = 1,800 planned cells. The two inference modes are chat and reasoning settings of the same served DeepSeek-V4 Flash build, not two independent model families. Seven reasoner transport failures were excluded rather than backfilled.

### Consensus results and endpoint caveat

The preregistered all-group comparison reports full consensus of 24% for the human carry-forward tracker, 86% for the LLM chat mode, and 96% for the reasoning mode in the selected primary scaffold. The paired differences are +62.0 and +72.0 percentage points.

That confirmatory comparison has a consequential endpoint mismatch: the human tracker carries forward a participant's last answer when the participant does not post a final answer, while the LLM agents are almost always forced to emit a final answer. Human non-posting is about one fifth of participants in the corpus; LLM-agent pass/lurk behavior is much rarer.

The paper therefore reports two **post-unblinding sensitivity analyses**:
- Among 45 groups in which every human participant spoke: human consensus 51.1%, chat 85.2%, reasoning 95.6%; paired gaps +34.1 pp (95% CI 19.3–48.9) and +44.4 pp (29.6–59.3).
- Submit-based comparison across 98 groups: paired gaps +34.0 pp (24.1–44.2) and +43.9 pp (34.0–53.7).

The smaller gaps remain substantial, but they are sensitivity analyses, not the preregistered primary estimands. The paper's abstract and discussion should not be summarized as though the +34/+44 values were the preregistered confirmatory result.

### Correctness is separate from consensus

On the isomorphic Wason reparameterization, reasoning-mode groups reach full consensus in 98.7% of cases, but 74.0% of all groups end in wrong consensus and only 24.7% in correct consensus. This is direct evidence within this task/replay setup that near-unanimity is not a correctness certificate.

The paper also reports a peer-hidden diagnostic on the classic task: chat-mode consensus falls from 87% with peer messages visible to 31% when peer messages are hidden; reasoning-mode consensus falls from 100% to 91%. Treat this as a task-specific diagnostic, not a general causal account of conformity. The high reasoning-mode consensus without peer visibility is itself evidence that direct peer exposure cannot explain all convergence; common model/task priors or shared inference behavior remain possible contributors.

A small subjective-task follow-up (five groups, 20 people) points in the opposite direction, toward under-convergence. It is exploratory and too small to support a generalization.

### Limits

- This is a replay of recorded human groups, not a newly recruited human-versus-LLM experiment.
- The primary consensus comparison is sensitive to human non-posting and endpoint construction; the more comparable analyses are post-unblinding.
- Chat and reasoning are settings of one served model build. A Qwen3-14B cross-family check is limited to the primary arm and the same held-out groups; it is not an independent sample replication.
- The isomorphic task reduces direct surface-template reuse but does not establish culture-free reasoning or remove every learned prior.
- The paper's reported results were not independently recomputed from the Zenodo raw artifacts in this run.

## 3. Primary source: DeliChess (2026), a second human-group benchmark

Xiaochen Zhu, Georgi Karadzhov, Tom Stafford and Andreas Vlachos, “DeliChess: A Multi-party Dialogue Dataset for Deliberation in Chess Puzzle Solving,” arXiv:2606.04987v1, submitted 2026-06-03.  
- Paper: https://arxiv.org/abs/2606.04987  
- Public dataset: https://huggingface.co/datasets/SpaceHunterInf/DeliChess  
- Dataset usage instructions: https://huggingface.co/datasets/SpaceHunterInf/DeliChess/blob/main/USAGE.md  
- Original DeliData paper: https://doi.org/10.1145/3610056  
- DeliData repository copy and license: https://eprints.whiterose.ac.uk/id/eprint/207765/

DeliChess contains 107 dialogues, 321 dialogue–puzzle cases, 7,667 utterances and 1,057 matched pre/post participant–puzzle choices. Groups have two to five active speakers (mean 3.41). Move quality is scored using three Stockfish-derived metrics: Simple, Reciprocal Rank and win/draw/loss probability.

Mean group Reciprocal Rank rises from 0.473 to 0.552 (Δ=0.079; 95% CI 0.051–0.108; q<0.001). But the 321 dialogue–puzzle cases are heterogeneous: 157 improve, 50 are unchanged and 114 decline. Among cases where the final modal share increases, 143 show positive RR gain and 102 show negative RR gain. Increased agreement therefore does not determine the direction of decision-quality change.

The paper defines strict assembly as a final modal answer with better Stockfish rank than every initial answer. It occurs in 19 of 162 eligible cases where nobody initially selected the best candidate; 11 of those 19 end with the best candidate as the unique final mode. These are rare, exploratory observations, not a universal group-reasoning law.

The paper's separate LLM action-selection diagnostic samples 60 dialogue prefixes from 52 dialogues, balanced at ten instances per each of six helpful-action labels. Gemini 3.5 Flash reaches the highest strict accuracy (0.350; κ=0.220; macro-F1=0.319); Gemma 4 31B and Hunyuan HY3 Preview are lower. Few-shot prompting does not consistently improve performance. Because the sample is filtered and balanced, this is not an estimate under the corpus's natural label distribution, and matching one observed helpful human action is not a complete measure of facilitation quality.

Annotation limits: the main corpus has one retained annotation per dialogue. A 12-dialogue reannotation audit reports κ=0.715 for communicative function, 0.923 for epistemic stance and 0.610 for deliberative-agent usefulness. The usefulness label is an application-oriented judgment, not a chess-correctness label.

The public Hugging Face card reports MIT licensing and three CSV artifacts (dialogues, events, utterances); its usage guide warns that the train split is storage-only and that train/test partitioning should be by dialogue_id to prevent leakage. The dataset bytes and manifest were not downloaded or checksum-verified in this run.

The original DeliData paper is peer-reviewed PACM HCI 7(CSCW2), Article 265 (2023), CC BY 4.0. It reports 500 group dialogues and about 14,000 utterances. It is the human source corpus used by the Shao replay, not a new LLM-agent trial.

## 4. Primary source: Kohli (2026), correlated judge errors and Kish effective sample size

Guneet Kohli, “Nine Judges, Two Effective Votes: Correlated Errors Undermine LLM Evaluation Panels,” arXiv:2605.29800v1, submitted 2026-05-28.  
- Primary record: https://arxiv.org/abs/2605.29800  
- Full HTML: https://arxiv.org/html/2605.29800v1

The paper tests nine judges from seven model families on three ChaosNLI datasets (1,000 entropy-stratified items each, with 100 human annotations per item) and a RewardBench pairwise-preference task. It reports mean pairwise error phi 0.391 on MNLI, Kish n_eff=2.18 [2.07, 2.31], eigenvalue n_eff=2.16, and a 24.2% nominal-independence ratio. On MNLI, the panel is 72.0% accurate against the 100-annotator majority label, while the best single judge is 71.8%; the item-aware Condorcet independence prediction is about 94.0%, a 22.0 pp gap [19.5, 24.1]. The cross-dataset n_eff values are 2.18, 2.35 and 2.48. This is a panel-error dependence study without peer-message exposure; it does not test social conformity.

The paper's Kish expression is:

    n_eff = k / (1 + (k - 1) * mean_phi)

The paper explicitly says this form assumes exchangeability (approximately equal pairwise correlations), and checks it against the largest-eigenvalue estimate. The observed pairwise phi values vary substantially (range 0.161–0.603; SD 0.111), so the exchangeability approximation must remain explicit. The eigenvalue result (2.16) is a useful robustness check, not proof that all correlations are equal.

The paper uses the majority of 100 human annotations as its gold label; human disagreement and label validity therefore remain part of the measurement model. It reports that flipping all 28 tied human-majority items changes panel accuracy by at most 0.7 pp and n_eff by at most 1.3%. Twenty-eight parse failures (<0.1% of judgments) are deterministically hash-assigned to a label. The paper's data-availability section identifies public ChaosNLI and RewardBench sources; it does not provide a separately verified raw panel-output bundle in the inspected text. No independent reproduction was performed here.

### Independent arithmetic check from the rounded published summary

Using only the paper's rounded k=9 and mean_phi=0.391:

- Design effect: 1 + 8*0.391 = 4.128.
- n_eff = 9/4.128 = 2.1802325581395349.
- Nominal independence ratio: 2.180232558/9 = 24.2248062%.
- Exchangeable asymptote: 1/0.391 = 2.55754476.

These reproduce the paper's rounded 2.18, 24.2%, and approximately 2.56 ceiling. Because the input phi is rounded, this is a consistency check, not a reanalysis of the underlying nine error vectors.

## 5. Proof-first formalization

A source-conditional Lean 4/Mathlib module was added to the existing Orson PR #850 branch:

- File: FORMAL_VERIFICATION/HsHVerification/OrsonKishEffectiveSampleSize.lean
- Imported by: FORMAL_VERIFICATION/HsHVerification.lean
- Branch: research/orson-p1-shared-nli-bound-20261028t06z
- New file commit: f62a66fcbd2a0794d5239f7eb2df6f8793ff5b15
- Root import commit / current exact head at note creation: 1b40b9f45c0fde4f1ddc9cce84ae45795f101215
- PR: https://github.com/Satobloc/HsH/pull/850
- Exact-head CI run: https://github.com/Satobloc/HsH/actions/runs/41160309297

The module states the equal-variance/common-correlation covariance model explicitly, proves the exchangeable mean-variance identity, derives the independent-equivalent variance using Kish n_eff, proves 1 ≤ n_eff ≤ k for 0 ≤ rho ≤ 1, and checks the rounded nine-judge example. The theorem is conditional on the formalized covariance assumptions. It does not compute phi from raw judge outputs, prove the empirical errors are exchangeable, validate the paper's data, or establish cognitive independence.

**CI status at note creation:** run #41160309297 was PENDING; an earlier run on the file-only commit #41160302620 was IN_PROGRESS. No successful compilation or axiom audit is claimed yet. The separate conversation-JSON content workflow reported failure with zero returned jobs; its cause was not available and it is not the Lean verification workflow. Check the exact-head Lean run and theorem-specific axiom outputs before updating this status.

## 6. P1 synthesis and scope boundary

The current P1 issue #564 asks: “Under what conditions does apparent consensus among LLM workers overstate independent scientific evidence?”

The evidence map now contains distinct regimes:

| Evidence | Interaction regime | What it supports | What it does not support |
|---|---|---|---|
| ConsistencyBench / 17 archived CGD outputs | Passive cross-model archive; shared within-model NLI checker; no peer answer exposure | Source-key match, revision, post-hoc majority and error dependence readouts | Peer pressure, social conformity, causal peer influence |
| Kohli (2026) | Nine-model judge panel; common items/prompt; no peer messages | Correlated errors and effective information loss | Social influence or agent-to-agent deliberation |
| Shao (2026) | LLM replay of recorded human Wason groups with peer interaction | Over-convergence and wrong consensus in a bounded replay task | New human-subject replication or universal model behavior |
| Chen et al. (2026), VEY-016 | Mixed human–LLM peer groups as reported | Direct peer-group interaction evidence | Independently replicated group effects or fully audited per-agent context ancestry |
| Alsobay et al. (2026), VEY-016 | Human groups with one shared LLM facilitator | Human–LLM facilitation effects | Multiple LLM peers |
| DeliChess (2026) | Human-only chess deliberation plus separate LLM action-selection diagnostic | Agreement/quality divergence, minority-knowledge recovery/loss, facilitation-action limits | LLM peer-group behavior |

The P1 paper should distinguish at least:
1. consensus/agreement;
2. correctness against an independently defensible key;
3. pairwise error dependence/effective information;
4. peer-message exposure and influence;
5. participation and final-answer endpoint construction;
6. evaluator/checker dependence.

A useful future experimental factorization remains shared versus disjoint evidence × peer messages hidden versus exposed, with sealed pre-exposure answers and post-exposure revisions. Group/session is the independent replication unit; turns, messages and agent slots are nested observations. Include pass/nonresponse handling and an independently adjudicated correctness outcome. Do not calculate power or prescribe group counts until a real pilot or suitable variance estimates exist.

The original matched neutral-versus-false-authority answer-keyed test bank remains **UNRECOVERED**. The completed Mersearch request orson-cognition-bank-source-recovery-20261030-2236 now has a verified run manifest and compact search receipt, but the detailed raw result collection remains withheld and the selected navigation sources do not identify the original bank. The earlier OV-49–OV-53 pointer mismatch remains: those located artifacts are geometry/finite-core work; OV-55/56/100 are analytical or synthetic, not administered trials.

SciSpace surfaced “Effective Sample Size Under Peer Exposure in Multi-LLM Deliberation” (OSF DOI 10.17605/osf.io/aw9vf) and “DelibSim: Procedural Parity, Outcome Mismatch.” The primary records/full texts were not retrieved in this run; they are unverified leads, not evidence in this synthesis.

## 7. Operational limits and next cursor

- No model API calls, human participants, recruitment, hosting, paid spend, or trial administration.
- No raw Shao Zenodo or DeliChess CSV bytes were downloaded; no independent dataset reanalysis.
- No P1 manuscript edit, PDF/reader acceptance, hostile review closure, or paper-gate advancement.
- No BEDROCK promotion or H(s)H theory change.
- No new tooling or platform. Existing SciSpace, the current HsH Lean project/PR #850, and public datasets were used as the available route.
- GRAIL remains the existing reusable group platform, but its audited main implementation is one shared facilitator, not multi-peer agents (VEY-017).
- The original Orson LLM Cognition Lab thread was sought first; no authenticated current conversation ID or usable live thread was established. This report is repository work, not a cross-thread continuation.
- FIE last reviewed 2026-10-27; the 14-day rereview threshold is not due.
- Unrelated reading break: SAT Mark V/TheTANGLE.txt, lines 1481–1520; next cursor 1521.
- No automation, task ID, schedule, or phase changed. No sixth task.

**Next:** verify exact-head Lean CI #41160309297 and inspect every theorem-specific axiom output; then update the receipt/PR comment. Keep P1 archival/methodological unless the actual answer-keyed bank and authorized administration path are recovered.
