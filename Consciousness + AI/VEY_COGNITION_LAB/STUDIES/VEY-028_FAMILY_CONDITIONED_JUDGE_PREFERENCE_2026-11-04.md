# VEY-028 | Judge-family measurement dependence in LLM-as-judge panels

**Date:** 2026-11-04  
**Evidence class:** EXTERNAL PREPRINT / TARGETED FULL-TEXT REVIEW / PUBLISHED-SUMMARY ARITHMETIC CHECK  
**Status:** review complete for arXiv HTML §§1–11 and Appendices A–D; no raw-data reproduction, no new LLM trial, no human session, no P1 protocol change.

## Primary source and custody

Awuni et al., “Who Judges Matters: Measuring Family-Conditioned Preference in LLM-as-Judge Panels,” arXiv:2609.17857v1, submitted 2026-09-15.

- Primary record: https://arxiv.org/abs/2609.17857
- Reviewed 2026-11-04 through SciSpace discovery followed by direct arXiv HTML inspection.
- The source is an arXiv preprint; no peer-reviewed venue is listed on the primary record.
- The authors state that a reproducibility archive has been prepared for public release. No public archive link or raw-data package was independently retrieved in this pass.
- No new Mersearch request was submitted: all shared request lanes remained occupied. This is not a Mersearch result.

## Study design and claims

Four open-weight families (Llama 3.1, Qwen 2.5, Gemma 2, Yi 1.5), each at two scales, form a fully crossed judge-family × candidate-family pairwise panel. Every judge family evaluates every unordered candidate-family pair in both response orders.

- 9,312 raw trials; 4,656 reconciled judge–prompt–pair observations.
- 16 judge × candidate cells, 582 observations per cell.
- 200 prompts allocated before response-health filtering; six excluded; 194 retained (132 exploratory, 62 confirmatory).
- Three graduate-level NLP annotators labeled 400 blinded items; one excluded under pre-specified criteria; two retained annotators reached consensus on 266 items (Cohen's κ = 0.482).

The authors call the result **family-conditioned preference**, not ordinary self-preference: judges do not score their own exact generations. The measured question is whether a candidate family receives extra support from a judge of the same family.

Reported global Family Preference Score: 0.067 (95% CI [0.053, 0.084], prompt-level permutation p = 0.0002). All four corrected family lifts are positive, 0.034–0.084. These are estimates for this particular panel and prompt distribution, not universal constants.

## Source-faithful identification algebra

Let P(j,c) be mean reconciled support from judge family j to candidate family c. The balanced zero-sum design gives each judge row mean 0.5 and sum 2.00.

The paper's decomposition is:

P(j,c) = μ + a_j + b_c + γ_jc,

with judge main effect a_j, candidate-family main effect b_c, and judge × candidate interaction γ_jc. The stated double-centering constraints are:

- Σ_c b_c = 0;
- Σ_c γ_jc = 0 for each j;
- Σ_j γ_jc = 0 for each c.

Because each row has mean 0.5 in the balanced design, μ = 0.5 and the additive judge main effect is absorbed.

For four families:

- Naive row contrast: R_f = P(f,f) − (1/3)Σ_{c≠f}P(f,c) = (4/3)(b_f + γ_ff).
- Candidate-held-fixed column contrast: C_f = P(f,f) − (1/3)Σ_{j≠f}P(j,f) = (4/3)γ_ff.
- Difference: R_f − C_f = (4/3)b_f.

The row contrast mixes candidate-family strength with the judge–candidate interaction. The column contrast holds the candidate family fixed and isolates the diagonal interaction **under the stated balanced additive/double-centered model**. This is not assumption-free identification and does not prove a causal mechanism.

## Independent arithmetic check of printed summaries

Using the rounded diagonal-support and other-judge means printed in Figure 2, the row contrast was recomputed from the stated row sum of 2.00 and the column contrast from the rounded means:

| Family | Diagonal | Other-judge mean | Derived row contrast | Column from rounded means | Paper column FPS | Row − column |
|---|---:|---:|---:|---:|---:|---:|
| Llama | 0.542 | 0.509 | 0.0560 | 0.033 | 0.034 | 0.0230 |
| Qwen | 0.620 | 0.544 | 0.1600 | 0.076 | 0.076 | 0.0840 |
| Gemma | 0.543 | 0.459 | 0.0573 | 0.084 | 0.084 | −0.0267 |
| Yi | 0.497 | 0.421 | −0.0040 | 0.076 | 0.076 | −0.0800 |

The row-minus-column values reproduce the paper's prompt-level permutation null means (+0.023, +0.084, −0.026, −0.080) to rounding. Llama's 0.033 from rounded table cells versus reported 0.034 is consistent with the paper's warning that averaging rounded values creates small differences. This is a published-summary arithmetic check, not raw-data reanalysis or independent reproduction.

## Order instability and likelihood channel

The paper reports 55.4% AB/BA winner reversals. Its simple independent symmetric content-noise model gives R = 2p(1−p) ≤ 0.5, so the aggregate observed rate is 5.4 percentage points above that model's ceiling. This rejects that simple model as a complete explanation; it does not uniquely identify position bias.

Under the pure first-slot diagnostic R = q² + (1−q)², the family-specific reversal rates imply q ≈ 0.879 for Gemma and q ≈ 0.630 for Yi on the q > 0.5 branch. A single homogeneous q should not be inferred for the whole panel: the pooled first-position A-rate of 0.778 would imply 65.46% reversal under a single-q pure-slot model, not the observed 55.4%. This is a heterogeneity/model-scope caution, not a contradiction of the family-specific diagnostic.

Same-family responses have higher judge-side mean per-token log-probability (−0.69 versus −1.38 for cross-family responses). Adding likelihood advantage reduces the controlled same-family coefficient from 0.299 to 0.116 (61% attenuation). The authors explicitly say this is descriptive coefficient attenuation, not causal mediation; non-collapsibility and common causes remain possible.

The paper also reports an independent human-consensus anchor, a float16 judging replication, a 72-specification multiverse, and an 18.5% pairwise-outcome change under a family-composition comparison. The human anchor is independent of the LLM panel but noisy (κ = 0.482). The main-text/Appendix-D distinction between 66 pre-filter confirmatory prompts in the float16 run and 62 post-health-filter prompts in the primary holdout could be stated more plainly.

## P1 crosswalk

The frozen P1 archive has 17 model-labelled outputs but one common GPT-4o-mini NLI checker. Its source-audited design includes within-model self-exposure/self-revision, not cross-model peer exposure. It is not a crossed judge-family × candidate-family panel.

This paper is therefore a **complementary evaluator-provenance comparator**, not a P1 result. The current P1 data cannot estimate judge-family effects because evaluator-family variation is absent. The paper supports treating evaluator provenance as part of the measurement system; it does not license a new trial, peer-deliberation claim, or revision of the frozen P1 protocol.

P1 issue #564 remains SOURCE / EXPERIMENT READINESS. November 9 remains NOT READY; November 30 P2 and December 14 P3 remain separate gates.

## Formalization triage

A definite conditional Lean target is available: under the four-family balanced zero-sum matrix assumptions, prove R_f − C_f = (4/3)b_f from the decomposition and centering constraints. A separate elementary lemma is R = 2p(1−p) ≤ 1/2 for p ∈ [0,1].

**Lean 4/Mathlib: NOT RUN / NOT COMPILED.** No local lean/lake/elan binary or Lean-specific connector is available in this runtime. The no-account lean4.dev playground is core-only; the official Lean Web editor requires JavaScript/browser interaction, and no connected browser context was available. Existing Orson PR #850 is a large, draft, stacked branch; the current handoff preserves branch/PR state. No branch, PR, or tool was created or modified. No formal proof is claimed.

## Next discriminating work

1. Preserve the frozen P1 scope.
2. When an authorized Mathlib execution route exists, formalize the balanced-matrix identity with every centering assumption explicit; compile and inspect theorem-specific axioms.
3. Treat any future multi-judge study as a separate design: cross judge family with candidate family, balance cells, counterbalance AB/BA, log judge-side likelihood, use an independent quality anchor, and report panel-composition sensitivity.
4. Do not infer family preference, peer influence, or causal mechanism from a single shared evaluator.

**Disposition:** VEY028_EXTERNAL_METHODS_COMPARATOR / P1_SCOPE_PRESERVED / PUBLISHED_SUMMARY_ARITHMETIC_CHECK / LEAN_NOT_RUN / NO_TRIAL / NO_PAPER_GATE_ADVANCEMENT.


## Publication verification — 2026-11-04

- HsH publisher intake issue #1334, submission ID `orson-vey028-judge-family-measurement-dependence-20261104t0124z-s2-001`.
- Publisher comment #6620543339 records commit `89c2b17294bc08880093a95ae049c9fab90ed975`, artifact `WORKSPACES/COMMON/PUBLISHED_SUBMISSIONS/orson-vey028-judge-family-measurement-dependence-20261104t0124z-s2-001.md`, and SHA-256 `c28e41a6ba169e403813dd500c983924873324504867417ac0dd9b33e99866ea`.
- Independent issue/file fetch confirmed exact equality between the issue payload's decoded content and the published artifact. Publisher status: **PUBLISHED_VERIFIED**.


## Lean formalization addendum — 2026-11-04T16:36Z

- The balanced four-family contrast identities and the independent symmetric-noise 50% reversal bound were transcribed into the existing HsH Orson formalization branch, PR #850. New module: `FORMAL_VERIFICATION/HsHVerification/OrsonFamilyConditionedPreference.lean`; module blob `58e097941587b9889707f63a012af5a2664803ce`; root aggregator blob `4586adeee53436723b8b57f0cfdb067b9ea1756b`; exact branch head `5bad1dcc79a686cd2a7e1f27c297a10cbcc802c6`.
- Workflow run #41870255531, job #126715066924, is still in progress. Checkout and Lake manifest steps passed; the Lean compilation step was in progress at last inspection. **Status: SUBMITTED_NOT_VERIFIED.** No compile, axiom-audit, or theorem-success claim is made.
- Formalization assumptions are explicit: four families; balanced judge-row means `μ+a_j=1/2`; zero-sum candidate-family effects; row- and column-centered interaction terms. The module states the row, column and difference identities and the symmetric-noise bound. It does not validate source data, randomization, empirical family effects, human anchoring, model independence or causal interpretation.
- This is an external methods comparator only. The frozen P1 ConsistencyBench archive still contains one shared GPT-4o-mini evaluator and within-model self-exposure/self-revision, not cross-model peer exposure. No P1 protocol change, trial, or paper-gate advancement.


## Lean failure / repair addendum — 2026-11-04

- First run #41870255531 failed in the new module: two contrast definitions required `noncomputable`; four `ring` tactics were redundant after `rw` had closed their goals. Lean 4.34.0 / Lake 5.0.0; workflow compiled a PR merge-reference tree `913d049c91a5f7f16e10b3e399a0efc2fd7eb037`, not a standalone head. Tests, lint, nanoda and axiom-audit were skipped. The emitted theorem axiom lines are not treated as proof success because the module failed to compile.
- Bounded repair committed to the same PR branch: module blob `d1ff80995c7f832f83a8a280c5d26e7d38392b9a`, branch head `872a5dd3f6a65c878f7392ec86be9c2641cc6245`; root aggregator import remains, blob `4586adeee53436723b8b57f0cfdb067b9ea1756b`.
- The repaired head's Actions run is not yet visible. Status `REPAIR_SUBMITTED_NOT_VERIFIED`; no Lean proof claim, empirical validation or P1 gate advancement.
