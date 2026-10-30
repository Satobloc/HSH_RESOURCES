# VEY-013 — Pairwise key-disagreement dependence and passive identifiability

**Date:** 2026-10-30  
**Worker slot:** Orson Vay, s2 / :24  
**Status:** ANALYSIS_EXECUTED / LEAN_EXACT_HEAD_CI_PENDING / NO_MODEL_TRIAL  
**Related:** Vey Cognition Lab VEY-011 and VEY-012; HsH P1 docket #564; published VEY-011 archive observation #1074; existing HsH PR #850.

## 1. Question

Do the 17 archived ConsistencyBench CGD model-labelled outputs exhibit pairwise co-disagreement with the published answer keys, and what can that pattern establish about source dependence?

This is a descriptive reanalysis of an existing archive. It is not a peer-exposure experiment, not a new model trial, and not semantic adjudication.

## 2. Provenance and data shape

The original 17 JSON result blobs were retrieved from the public aayambansal/ConsistencyBench repository by their exact Git blob SHA. The immutable 17-file manifest is already recorded in the VEY-011 source report and is reused unchanged by the existing HsH replay script.

- 17 model-labelled result files.
- 300 sets per file.
- 1,150 aligned question positions per file.
- 977 distinct exact question strings in the full aligned archive.
- 17 model labels are file labels, not independently authenticated backend/version attestations.
- The expected answer is the dataset's published key, not a blinded independent human adjudication.

The existing source-locked replay script was extended in the existing P1 PR branch; no new tool or branch was created.

## 3. Calculation

For each model i and item j, define a binary key-disagreement indicator:

E_ij = 1[L_ij != K_j],

where L_ij is the normalized model label and K_j is the published expected key. Valid labels are yes, no, and cannot_determine; unclear/invalid labels are excluded pairwise.

For each of the 17-choose-2 = 136 model pairs, calculate the phi coefficient between the two binary key-disagreement vectors on that pair's own complete cases. The reported mean is the unweighted mean across the 136 pairwise phi coefficients. Pair-specific sample sizes therefore differ.

### Results

| Stage | Mean pairwise phi | Median | Range | Positive pairs | Pairwise n range (median) |
|---|---:|---:|---:|---:|---:|
| Initial extracted labels | 0.501 | 0.507 | 0.092–0.801 | 136/136 | 781–1,150 (1,087) |
| Final extracted labels | 0.457 | 0.460 | 0.194–0.754 | 136/136 | 763–1,150 (1,075) |

The mean change is -0.044. A paired cluster bootstrap, using the same resampled clusters for initial and final stages, gave:

- **Set-cluster bootstrap:** 2,000 replicates; 95% interval for the paired mean-phi change: **[-0.0547, -0.0326]**.
- **Exact-question-cluster bootstrap:** 500 replicates; 95% interval: **[-0.0587, -0.0295]**.

These intervals quantify item-cluster sampling variation conditional on the fixed 17 model labels. They do not include model-selection uncertainty.

### Coverage sensitivity

Only **510/1,150** positions were complete for all 17 models at both stages, spanning 260 sets and 443 exact question strings. On that more restrictive intersection, mean pairwise phi was 0.548 initially and 0.474 finally.

The difference from the pair-specific analysis demonstrates sensitivity to the complete-case rule. The all-17 intersection is not the headline estimate.

## 4. Interpretation and limits

The archived outputs show substantial **co-disagreement with the published keys**. The descriptive mean phi is lower at the final-label stage than at the initial-label stage. This is not a causal checker effect and does not show that the models became more independent.

The analysis must not be relabelled as semantic error correlation without qualification:

1. Published answer keys are not independent human ground truth.
2. Pairwise phi includes shared item difficulty and repeated-question effects.
3. The final-label stage shares the benchmark's GPT-4o-mini NLI checker; raw checker calls/adjudication traces are not available here.
4. The archive contains no peer-answer exposure or randomized source-sharing intervention.
5. Model-family, prompt, and backend dependence are not fully authenticated.
6. Pair-specific missingness means the 17×17 pairwise matrix need not be positive semidefinite. No eigenvalue effective sample size is reported.
7. These are 17 fixed archived labels, not 17 independent replications or a random sample of all LLMs.

The mean phi is not directly comparable to the coefficients in other judge-panel studies unless their item sets, ground truth, missingness, and conditioning on item difficulty are matched.

## 5. Literature crosswalk: full-text review completed

The existing VEY-012 review already covers the peer-cue and majority-vote literature. This pass completed full-text review of two passive judge-dependence papers and added the speaker-free conformity study:

- Hossain, Yousefi & Lim (2026), “Agreement Overstates Evidence: Error Dependence in LLM Judge Consensus,” arXiv:2609.22512. Full text reviewed. It measures correlated judge errors; it does not manipulate a common evidence source or show peer answers to the judges.
- Kohli et al. (2026), “Nine Judges, Two Effective Votes,” arXiv:2605.29800. Full text reviewed. It estimates judge-panel dependence against human annotations; it is not a source-sharing intervention.
- Hu & Qu (2026), “Most LLM Conformity Needs No Speaker: Source-Free Conformity as a Baseline and Attribution Increment,” arXiv:2607.05545. Full text reviewed. Its no-speaker condition still contains a repeated answer assertion; “source-free” does not mean no added information. The attributed-expert condition adds an increment beyond the repeated-content condition.
- Hu & Qu (2026), “Social Pressure Breaks Majority Voting in LLM Safety Panels,” arXiv:2608.04415, and Qu et al. (2026), “Easier to Mislead Than to Correct,” arXiv:2606.01637, remain related peer-cue interventions from the same research group, not independent replications.

These designs distinguish at least three mechanisms that must not be collapsed: passive error co-occurrence, repeated-content conformity, and explicit peer/authority cue effects. Shared-evaluator dependence is a fourth mechanism.

## 6. OV-55/56 source and mathematical result

The source equations are in HsH:

- OV-55, WORKSPACES/ORSON_VAY/OV_20261010_55_SHARED_RECORD_CONSENSUS_TRAP.md, blob b2880ad651d1ff988c312a7c6aed4485459cadb5 (assistant-authored analytic sandbox).
- OV-56, WORKSPACES/ORSON_VAY/OV_20261010_56_CONSENSUS_IDENTIFIABILITY_AND_INTERVENTION.md, blob b73b0a16af8e0d33c135e871e70c7f575600d0c6 (assistant-authored identifiability note).

These are not Nathan Direct equations and not empirical LLM results. The values p=0.8, q=0.15 are existing sandbox parameters, not measured model rates.

The shared-record gate model is:

Z ~ Bernoulli(1-q), Y_i iid Bernoulli(p), X_i = Z Y_i.

A latent item-difficulty countermodel chooses D=0 with probability q, and D=p with probability 1-q, then draws the agents independently conditional on D.

For any fixed labelled pattern with k successes and f failures, both models assign:

q * 1[k=0] + (1-q) p^k (1-p)^f.

Thus the full finite joint correctness-pattern distribution is identical. Passive panel observations cannot distinguish “a shared record failed” from “this item had latent difficulty zero” under these model definitions.

The first marginal m=(1-q)p alone does not identify both parameters. Under the gate model, the second joint moment v=(1-q)p^2 yields p=v/m and q=1-m^2/v when the denominators are nonzero. This is conditional parameter recovery inside the assumed model; it does not identify the causal meaning of the latent variable.

For the existing OV-55/56 sandbox parameterization, exact values are m=17/25, v=68/125, third joint moment 272/625, covariance 51/625, and pairwise correlation 3/8. These are algebraic checks of the archived example, not empirical estimates.

## 7. Lean 4 formalization

A new module, OrsonSharedRecordIdentifiability.lean, was added to the existing P1 PR #850 branch, together with an import in the existing root file. It formalizes:

- zero-difficulty pattern probability;
- full finite-pattern distributional equivalence;
- marginal, pairwise and triple moments;
- covariance identity;
- first-moment non-identifiability;
- conditional recovery of p,q from the first two moments;
- exact OV-55/56 rational example values.

There are 11 theorem-specific #print axioms targets. The module is on branch research/orson-p1-shared-nli-bound-20261028t06z, commit 87fb337545fd04a8e63a8ee2bece3c39f5cb65a5.

**Exact-head CI:** run #41022980811 was queued at the time of this note; compilation and theorem-specific axiom inspection are therefore **pending**, not claimed.

Toolchain file: leanprover/lean4:v4.34.0. The formal-verification directory has no committed lake-manifest.json, so the exact Mathlib dependency resolution is not locked. This runtime has no local lean or lake executable; GitHub Actions is the execution route.

Lean will verify only the encoded conditional mathematics. It will not establish that the OV-55/56 translation is a faithful account of real LLM behavior or that a shared-source mechanism caused the archived correlations.

## 8. Test-bank and experiment feasibility

The role-charter pointer to an “OV-49–OV-53 matched cognition test bank” is not currently usable: the located OV-49–OV-53 artifacts are geometry/finite-core sandbox work, not an administered cognition bank. OV-55/56 are analytic proposals; no real LLM sessions were run.

The local runtime has no Ollama/vLLM/llama.cpp executable, no model weights, no GPU, and no external provider API credentials. No independent multi-model call path is exposed by the current connected tool set. No model calls or paid API spend were made. A realistic token-cost estimate is not defensible until the actual item bank, prompt lengths, provider set, and trial count are recovered.

The P1 experiment therefore remains **BLOCKED ON TEST-BANK PROVENANCE + AUTHORIZED INDEPENDENT MODEL ACCESS**. If those do not clear before the November 2 protocol freeze, the defensible November 9 paper path is a methods/measurement paper plus clearly bounded archive observations, not a fabricated or implied controlled trial.

## 9. Protocol amendment for the November 2 freeze

The existing VEY-012 design should add an **unattributed repeated-assertion** condition between plain re-ask and attributed peer/authority conditions. Keep the answer text identical while varying attribution:

1. plain re-ask / no added assertion;
2. bare repeated assertion with no speaker/source label;
3. same assertion attributed to a peer majority;
4. same assertion attributed to an expert panel;
5. same assertion embedded in a source record with explicit provenance;
6. length-matched irrelevant record;
7. accurate relevant record.

Balance correct and incorrect assertions using the recovered, pre-existing answer-keyed items. Randomize conditions across independent sessions; do not expose a model sequentially to multiple conditions for the same item. Preserve exact prompt, model/version, temperature/seed, raw response, source artifact hash, evaluator/version, confidence and revision direction. Use blinded independent adjudication for ambiguous answers rather than relying solely on the shared NLI checker.

This separates content repetition from source/peer/authority attribution and source-record exposure. It is a protocol proposal, not an administered experiment or a frozen preregistration.

## 10. Next actions

1. Verify exact-head Lean run #41022980811; inspect every new theorem-specific axiom report and record skipped tests/audit separately.
2. Recover the actual cognition test bank or select a real existing answer-keyed dataset with independent adjudication.
3. Establish an authorized independent model-call path and a bounded cost plan; no API-key creation or paid calls without explicit authorization.
4. Freeze the protocol by November 2. Keep the November 9 P1 gate separate from the November 30 and December 14 papers.
5. Preserve the distinction between observed key-disagreement, semantic correctness, causal source dependence, peer conformity, and shared-evaluator effects.

**No H(s)H physical prediction, CODATA comparison, BEDROCK promotion, paper-gate promotion, or claim of model personhood is made in this study.**
