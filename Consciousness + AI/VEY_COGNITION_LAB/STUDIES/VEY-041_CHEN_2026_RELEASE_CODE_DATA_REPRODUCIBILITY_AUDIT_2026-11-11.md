# VEY-041 — Chen et al. (2026) peer-group release, repeated-measures, and figure-reproduction audit

**Date:** 2026-11-11  
**Status:** PUBLIC SOURCE / CODE / PROCESSED-DATA AUDIT COMPLETE; DESCRIPTIVE REAGGREGATION COMPLETE; AUTHOR-LEVEL RECONCILIATION OPEN.  
**Evidence class:** LITERATURE RESULT + PUBLIC-REPOSITORY REPLAY + SOURCE-CODE AUDIT. Not an independent replication, human-subject experiment, or model trial.  
**Relationship:** Additive to VEY-016. Do not duplicate VEY-016's already-established group/session replication limitation.

## Question

Does the public code/data snapshot for Lin Chen et al., “AI agents reshape consensus formation in human groups,” reproduce the paper's reported adoption-willingness contrasts, and do the released records permit the repeated-measures and group-level uncertainty checks required for stronger inference?

## Source lock

### Manuscript

- Lin Chen, Ziyi Liu, Xia Hu, Yong Li, “AI agents reshape consensus formation in human groups,” arXiv:2609.02122, v1 first posted 2026-09-02.
- Full HTML: https://arxiv.org/html/2609.02122
- The source reports eight conditions, 127 human participants, 24 total participant/agent slots per session, and 40 rounds of randomized pairwise interaction.
- The supplementary information describes nine sampled interaction rounds for the personalized questionnaire and the M5 regression sample of 495 observations.
- The manuscript reports an H3 adoption-willingness gap of +0.884 (p=0.010).
- The paper describes persistence in prose as similarity between rounds r and r+1, while the displayed formula uses r and r-1. This is an indexing discrepancy; its practical effect is unresolved.

### Public code/data repository

- Repository: https://github.com/tsinghua-fib-lab/human-ai-consensus
- Main commit: `74b79b65f221a01ba9c6744dc4f107741fcd8908`
- Commit date: 2026-05-16T22:38:38Z.
- The arXiv v1 was posted 108.28 days later. The repository is therefore not a contemporaneous, version-pinned release of the arXiv v1. This chronology does not prove the data are wrong; it creates a version-reconciliation requirement.

### Exact public processed CSVs

| File | Git blob | Rows | Expected humans × 9 |
|---|---|---:|---:|
| A2 | `9ea458f5ba92fb0aedccfffbf497fb01a8f92ddf` | 108 | 12 × 9 |
| A3 | `36330599372bd4ddabbb98b973326260e28e07ee` | 144 | 16 × 9 |
| A4 | `29eb49d6143217d4101269446a0f79bf3cdbab4c` | 189 | 21 × 9 |
| A5 | `7ffbd3e6c22093016163aee5280a018fc3f50e62` | 54 | 6 × 9 |
| **Total** | | **495** | **55 × 9** |

The CSV header is exactly: `round,you,peer,judged_ai,willingness`. It contains no stable participant/respondent ID or session ID. The total row count matches the reported 55 humans in A2–A5 times nine sampled interactions, but the rows cannot be linked to respondents for participant-clustered inference.

Round counts are nonuniform in A3 and A4. Because participant identifiers are absent, the release does not allow us to distinguish sampling variation, repeated same-round records, missing records, or export duplication. No error is inferred from the imbalance alone. Exact duplicate row values occur once in each of A3 and A4; without IDs they cannot be classified as duplicate participants.

## Scripted descriptive reaggregation

The public figure script `plot_ai_penalty_with_controls_with_centrality_distance.py` (blob `3c6edacc0a9de94535eb8b38598fda6701d5e198`) maps A2=50%, A3=33.3%, A4=12.5%, A5=75%. Its H1/H2/H3 adoption-willingness gap is calculated as the pooled row mean for `judged_ai=1` minus the pooled row mean for `judged_ai=0`.

Reaggregation of the exact A2–A5 CSVs gives:

| Stage | Rows | Judged AI n / mean | Judged human n / mean | Raw row-mean gap |
|---|---:|---:|---:|---:|
| H1, 12.5% (A4) | 189 | 65 / 3.3077 | 124 / 3.7097 | -0.4020 |
| H2, 33.3% + 50% (A3+A2) | 252 | 117 / 2.7265 | 135 / 3.2519 | -0.5254 |
| H3, 75% (A5) | 54 | 34 / 3.6471 | 20 / 3.3000 | **+0.3471** |

The public repository's row-mean calculation therefore yields +0.3471 for H3, not the manuscript's +0.884. This is an unresolved reproduction/version discrepancy, not evidence of fabrication or proof that the manuscript's result is false. Plausible explanations include a different data/code vintage or a different aggregation estimand; neither is established. No p-value was recomputed because the CSV lacks respondent IDs and the rows are repeated observations.

## Repeated-measures and reproducibility findings

### 1. Participant-clustered uncertainty is not recoverable from the released CSVs

The 495 rows represent 55 humans × 9 sampled interactions, not 495 independent people. The CSVs omit participant IDs. The paper's M5 uses OLS with HC3 heteroskedasticity-consistent standard errors; HC3 does not by itself account for within-participant dependence. The public CSV release does not permit participant-clustered standard errors to be reconstructed.

For score contributions (u_i=x_i\hat\epsilon_i), the cluster sandwich “meat” depends on the unknown partition:
[
M(\mathcal G)=\sum_{g\in\mathcal G}\left(\sum_{i\in g}u_i\right)\left(\sum_{i\in g}u_i\right)^\top.
]
Two compatible partitions can yield different (M). For two scores (u,v), separate clusters give (uu^\top+vv^\top); one merged cluster gives ((u+v)(u+v)^\top), adding (uv^\top+vu^\top). Without respondent IDs, the cluster covariance is not identified from the released table except in special cases where those cross terms vanish. This is a proof sketch, not a Lean-checked theorem.

### 2. Public early/late significance code uses an unpaired test on repeated individuals

The public script `plot_adoption_persistence_dynamics_by_pair_type.py` (blob `9db50b000284dd980b478b0a456f37f6e586cbd8`) constructs each individual's early and late window means from the same per-individual matrix, appends both values, then calls `scipy.stats.ttest_ind(e_arr, l_arr, equal_var=False)`. The comparison is within the same individuals, so an unpaired Welch test ignores the pairing. A paired test or a repeated-measures/mixed model is the appropriate family of analysis, subject to the study's session-level limitations.

The function docstring says “Welch t-test, Human vs Agent at each time point,” but the actual significance code tests Early vs Late within each role. This is a code-comment mismatch.

The script loads `adoption_series_dict_with_individual_results.pkl` and `persistence_series_dict_with_individual_results.pkl`. Those intermediate files are present in the repository, but the full 40-entry repository tree contains no Python generator for them. The figure can consume precomputed intermediates, but the transformation from raw trackers to those intermediates is not reproducible from the published repository alone.

### 3. Group/session replication remains the limiting unit

The supplementary condition counts (24, 21, 16, 12, 6, 16, 16, 16 humans) plus complementary agent slots fill eight 24-member sessions and strongly imply one session per condition. The inference is source-level, not a Lean theorem. The manipulated agent proportion/trait/model capability is session-level; participant rows and rounds are nested observations. Without multiple independent sessions per condition, between-session variance cannot be estimated and condition effects remain inseparable from session-specific effects.

### 4. Outcome dependence remains

As already recorded in VEY-016, the same all-MiniLM-L6-v2 embedding system supplies similarity feedback/payoff and the primary embedding-based consensus measure. This measures convergence under the task's reward metric, not independent semantic truth or decision accuracy. It is not repeated here as a new finding.

## Formalization status

Existing HsH PR #1115 was reused; no new branch or PR was created.

- The earlier module `HumanAIGroupsSessionConfounding.lean` compiled on exact commit `c029318b96a07fc433ed16a9082cb2e7b29002ea`.
- Actions run #41115603417, job #124268909008; Lean 4.34.0 / Lake 5.0.0; 8,973 build jobs; SUCCESS.
- `eachConditionHas24Slots` reports no axioms. Count theorems report `propext`; conditional identifiability theorems report `propext`, `Classical.choice`, and `Quot.sound`. No `sorryAx` appeared in the captured theorem output.
- The theorem is conditional on one treatment level occurring in exactly one group/session. It does not prove the source's one-session-per-condition interpretation or validate the published statistics.
- Current PR #1115 head `cc5d92c6935aa2ae120de2efed7c4ac8a1ebfbc7` has no associated pull-request workflow runs. `HumanAIMemoryCarryover.lean` and `ObservableProjection.lean` remain LEAN_NOT_RUN. The cluster-covariance non-identifiability proof sketch above is not formalized or compiled.

## Disposition and next evidence required

- Keep VEY-016 as the original mixed human–multi-LLM group study audit; VEY-041 is an additive release/code/data reproducibility audit.
- Do not claim the manuscript is falsified. Record the H3 +0.3471 vs +0.884 discrepancy as unresolved.
- Request or recover a version-pinned code/data snapshot corresponding to arXiv v1, with stable respondent and session identifiers or sufficient cluster-level statistics.
- Recover the generator for the individual-level adoption/persistence intermediates and reconcile the persistence indexing convention.
- Recompute early/late contrasts with paired or mixed-effects methods and participant/session structure where the source permits.
- For future experiments, randomize at the group/session level with multiple independent groups per condition; preserve per-agent model/version, prompt/context, source exposure, and request/response lineage; use an independent outcome measure not identical to the interaction reward.
- No new human-subject experiment, model trial, API spend, paper manuscript, PDF, reader, independent review, P1 scope change, or paper-gate advancement occurred. P1 remains frozen METHODS / ARCHIVAL and NOT READY.
