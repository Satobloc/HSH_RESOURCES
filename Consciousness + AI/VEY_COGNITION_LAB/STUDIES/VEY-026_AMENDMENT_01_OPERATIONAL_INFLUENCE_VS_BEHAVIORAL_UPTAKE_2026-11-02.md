# VEY-026 Amendment 01 | Operational influence allocation versus behavioral uptake

**Date:** 2026-11-02  
**Status:** PRIMARY-SOURCE CLARIFICATION / BIBLIOGRAPHIC CORRECTION / NO NEW EXPERIMENT  
**Supersedes:** No. This supplements the immutable VEY-026 issue #1262 artifact.  
**P1 docket:** HsH issue #564, still OPEN / SOURCE–EXPERIMENT READINESS.

## 1. Bibliographic correction

The arXiv record for Liu et al., *Social Networks of LLM Agents*, arXiv:2607.03695v1, lists the v1 submission timestamp as **2026-07-04 03:59:08 UTC**, not July 7. The July 7 date in VEY-026 is corrected here. The source is an arXiv preprint; peer-review status is not established by this record.

Primary source: https://arxiv.org/abs/2607.03695

## 2. Clarify what the paper's “realized-influence” operator measures

The paper's terminology is retained, but its operational status needs sharper description.

- Section 3.2 distinguishes the visible exposure graph W-bar from the realized-influence matrix C(t). C's row entries are the weights with which an agent aggregates other agents' beliefs, and its support is constrained by exposure.
- Sections 4.1 and 12.2 construct C from the exposure matrix, social-power weights, and a context-width rule: C(beta) = Gamma_beta(W-bar elementwise-multiplied by pi).
- Appendix 12.3 states that beta is a simulation-harness knob, not a parameter of the language model. The harness orders peers by C-weight and inserts them into each prompt until 90% of the row's normalized influence mass is covered; lower-ranked peers are withheld.

Therefore C is best described as a **harness-constructed context-allocation / aggregation operator**. It operationalizes the paper's realized-influence model, but it is not a direct measurement of internal attention, latent cognition, or the causal effect of each individual message. The observed behavioral quantity is the subsequent declared belief/update in the event log. The paper compares that behavior with a proxy update rule.

This does not invalidate the paper's controlled operator-arm results. Its beta, equalizer, and adversary-off interventions support claims about those specified harness policies and benchmark outcomes. It does mean that C alone must not be relabeled as independently observed per-message uptake. A per-source causal uptake estimate would require a receiver-level exposure contrast or other counterfactual design, in addition to recording C.

## 3. The proxy–LLM bridge is conditional and partly in-sample

Appendix 7 makes the distinction explicit:

1. The delta-rational residual is computable per emission from the event log.
2. The anchoring lambda_i values are not prespecified; they are fitted separately for each agent by least squares over the same run.
3. The uniform delta_T is the maximum residual after that per-agent fit, not a quantile.
4. A finite run supports the bridge bound only through its observed horizon T. Extending the bound beyond T requires a further uniform-residual assumption.
5. The reported 254/254 zero-violation result is therefore a conditional, in-sample best-fit ceiling check, not an independent out-of-sample prediction test.

The paper itself states that the unanchored DeGroot case lambda = 1 makes the bridge bound vacuous; the relation between proxy ESS and collective accuracy in that regime is empirical, not a theorem mapping ESS to accuracy.

The mathematical bridge remains a valid conditional theorem under its stated assumptions. The limitation concerns what the fitted residual check establishes empirically.

## 4. Agent count is not independent-model-family count

In the main experiments, each agent is Qwen2.5-7B-Instruct by default. The paper explicitly says the network is one model instantiated as n agents sharing weights, differing in persona, private information, and position. The controlled ESS topology table uses n=12 agents and 24 seeds; those are not 12 independent model families or 24 independent model replications.

The paper's cross-family check is narrower: Llama-3.1-8B is substituted for Qwen-7B in the HiddenBench 2x2 experiment, with five seeds. It does not establish broad cross-family replication across every benchmark and condition.

The reported q_T-based N_eff values are proxy-weight concentration results for the specified model/harness runs. They are not empirical covariance estimates across independent foundation-model families.

## 5. P1 consequence

The HsH ConsistencyBench archive remains a different object: a fixed-item 17-model panel with no peer-to-peer answer exposure. Its shared NLI checker is an evaluator dependency. It is not a peer-exposure graph, a realized-influence measurement, or evidence of social convergence.

For any future interaction study, preserve these separate records:

- **Exposure opportunity:** which messages were available to each recipient, with timestamps.
- **Harness allocation:** which messages were actually inserted into each prompt, with weights and truncation/coverage rules.
- **Observed receiver response:** pre/post belief or answer state.
- **Behavioral uptake:** a separately defined response change or source-specific causal contrast; do not infer it from allocation weights alone.
- **Source ancestry:** shared upstream documents, retrieval results, prompts, labels, and evidence roots.
- **Measurement/aggregation:** evaluator, mapper, calibration, tie/missingness policy, and aggregation identity.
- **Dependence model:** the covariance matrix or declared approximation used for any ESS calculation.

The VEY-026 covariance-aware formula remains an assistant-derived conditional identity under normalized weights, equal marginal variance, and common off-diagonal correlation. No P1 covariance matrix or aggregation-weight vector has been recovered, so no empirical covariance-aware ESS is available.

## 6. Formalization status correction

Existing HsH PR #850 was extended in place; no new branch or PR was created.

- The prior Lean 4.34.0 run #41437884107 built merge commit `95199aba6d08fa7087e4ee574addec9ba03c4bab`, containing PR head `559f88555235a2b5cad613b089b9caada952a5e7`.
- It failed in `OrsonKishEffectiveSampleSize.lean` at the uniform-weight specialization: `ring` did not close the final polynomial identity.
- The proof suggestion was `ring_nf`. The existing PR branch was patched to use `ring_nf`, commit `f595f7d0a18c5f95b36f56e1cbc6c5f64ca48010`, module blob `ec982070441970bbd95077b6fedd523204d21a67`.
- New workflow run #41440160916 is now in progress on the updated PR head. Until its complete log and checked-out merge SHA are read, compilation remains PENDING. No proof-pass claim is made here.

Lean checks only the formalized conditional algebra. It does not validate the source translation, the harness's behavioral interpretation, covariance assumptions, or P1 evidence.

## 7. Disposition

- P1 issue #564 remains OPEN / SOURCE–EXPERIMENT READINESS.
- Original OV-49–OV-53 bank remains unrecovered; no authorized inference endpoint is available.
- No model call, human-subject session, new HsH trial, API spend, or independent replication occurred.
- No manuscript, PDF, reader, reviewer sign-off, or paper-gate status changed.
- November 9 P1, November 30 P2, and December 14 P3 remain separate gates.
- This amendment is a methodological clarification, not a new experiment or a theory result.
