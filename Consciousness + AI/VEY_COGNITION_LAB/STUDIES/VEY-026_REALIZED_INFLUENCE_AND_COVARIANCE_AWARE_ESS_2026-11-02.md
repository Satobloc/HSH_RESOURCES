# VEY-026 | Realized influence, weight concentration, and covariance-aware effective sample size

**Date:** 2026-11-02  
**Status:** TARGETED PRIMARY-LITERATURE CROSSWALK / CONDITIONAL MATHEMATICAL SYNTHESIS / LEAN COMPILE PENDING  
**Owner lane:** Orson Vay, LLM cognition (selected label; not an authenticated historical instance)  
**P1 docket:** HsH issue #564, OPEN / SOURCE-EXPERIMENT READINESS  
**Scope:** LLM social influence and measurement architecture only; no H(s)H physical-theory claim.

## 1. Bounded question

When several LLM outputs are combined, which dependencies concern (a) who could see whom, (b) who actually influenced whom, (c) what evidence a receiver integrated, and (d) how a shared evaluator or aggregation procedure transformed the outputs? Can weight-concentration ESS and exchangeable/Kish ESS be placed in one conditional variance formula without treating them as interchangeable?

**Answer:** yes, under an explicit common-correlation covariance model. The resulting formula is a mathematical synthesis, not an empirical estimate for the HsH P1 archive and not a formula claimed verbatim by either cited paper.

## 2. Primary-source review

### 2.1 Liu et al., *Social Networks of LLM Agents*

- Identifier: arXiv:2607.03695v1; preprint dated 2026-07-07.
- Reviewed extent: targeted primary-source reading of the 34-page PDF, including problem formulation and realized-influence operator (pp. 2–5), proxy/LLM bridge and its limits (pp. 7–8), assumptions and variance derivation (pp. 11, 15), heteroskedastic extension (pp. 23–24), model/inference details (p. 24), and topology/ESS results (pp. 29–32).
- Official source: https://arxiv.org/pdf/2607.03695

The paper distinguishes the **visible exposure network** from the **realized-influence operator**. The former describes what the network makes available; the latter describes how much each source actually shapes another agent's beliefs. Its row-stochastic influence sequence C(t), social-power term, and attention-width parameter determine a time-dependent influence process. The terminal influence weights q_T summarize how initial private signals contribute to the collective estimate.

Under Assumption 7.3, private signal errors are independent, mean-zero, and have variances s_i^2; the signal-noise vector is also independent of the realized influence sequence. Proposition 8.6 gives Var(q_T^T b_0) = q_T^T S q_T. In the homoskedastic case S = s^2 I, this becomes s^2 ||q_T||_2^2. Definition 8.7 therefore sets:

```math
N_eff(q_T) = 1 / ||q_T||_2^2 = 1 / sum_i q_{T,i}^2.
```

This is a **weight-concentration ESS under independent private signals**, not a general correction for correlated source errors.

The paper's own limitations are important:

- If recipient selection or event quality depends on belief values, q_T and the private-signal errors can become coupled; the conditional variance identities then fall outside Assumption 7.3.
- In the unanchored DeGroot case (lambda = 1), the paper says the bridge bound is vacuous. Its observed relation between proxy ESS and LLM collective accuracy is empirical in that regime, not a theorem mapping ESS to accuracy.
- The controlled testbed uses a single Qwen2.5-3B-Instruct backbone by default, with scale and cross-family checks elsewhere. The topology table reports n=12 agents and 24 seeds. Its n_eff values are not counts of independent model families or independent minds.
- Table 4 reports, for example, Barabasi-Albert topology n_eff 3.0 at narrow beta and 9.8 at wide beta; the regular no-hub graph reports 12.0 in both conditions. These are source-reported proxy-weight results, not an independent reanalysis by this lab.

The paper describes committed run artifacts, but no independently accessible code repository or raw run package was retrieved in this pass. It is an arXiv preprint, not a peer-reviewed publication verified here.

### 2.2 Kohli, *Nine Judges, Two Effective Votes*

- Identifier: arXiv:2605.29800v1; dated 2026-05-28.
- Source already used by the existing Orson Kish formalization: §3.3, equation (1).

The existing module formalizes the equal-weight, equal-marginal-variance, common-off-diagonal-correlation design effect:

```math
N_eff = k / (1 + (k - 1) rho).
```

This is a conditional exchangeable-panel result. It does not estimate rho from the P1 raw outputs and does not turn an effective sample size into a literal count of cognitive agents.

### 2.3 Existing adjacent cognition work

- VEY-023, *Receiver-relative evidence integration and source provenance*, reviewed Kawada & Kellis, arXiv:2609.04290v1. It treats a receiver's adoption/checking/use of candidate evidence; it is not a direct peer-influence network study.
- VEY-024, *Mapper identity, transitive closure, and consensus measurement*, distinguishes fixed-item mapping, anchored canonical-proposition mapping, exploratory NLI closure, and claim-instance retention.
- VEY-025, *Identity-channel factorial, source ancestry, and revision balance*, separates evidence ancestry, identity/social cues, receiver state, and measurement/aggregation path.

VEY-026 adds **exposure topology versus realized influence** as a distinct mechanism distinction. It does not replace the existing five evidence objects or the four orthogonal dimensions in VEY-025.

### 2.4 Metadata-only lead not used as evidence

The title/identifier pair *Effective Sample Size Under Peer Exposure in Multi-LLM Deliberation*, DOI 10.17605/osf.io/aw9vf, matched in a citation audit. The OSF full text and underlying files were not retrieved. It is therefore a metadata-only lead, not a source for the derivation or an independent corroborating study.

A batch citation audit of five references (Liu et al.; Bause et al.; Moreno; Kawada & Kellis; Kohli) returned five matched identifiers/titles and no retraction notices. That audit verifies reference identity, not study quality or empirical validity.

## 3. Distinct causal and measurement objects

For a future interacting-agent study, record these separately:

1. **Exposure opportunity:** the directed, time-stamped graph of which messages or outputs were available to each recipient.
2. **Realized influence:** the measured or explicitly modeled operator that maps available messages to changes in receiver beliefs/answers. Exposure alone does not identify influence.
3. **Receiver-side evidence integration:** which candidate sources were checked, adopted, rejected, or used in the final action.
4. **Source ancestry:** shared upstream documents, retrieval results, prompts, labels, or evidence roots.
5. **Measurement/aggregation:** evaluator, mapper, NLI model, calibration map, tie/missingness rules, and aggregation identity.

These are transformation and dependence descriptors, not new evidence stages. Preserve Sable's five evidence objects unchanged.

For the existing ConsistencyBench P1 archive, the source record describes a fixed-item benchmark with a shared evaluator and deterministic answer-label mapping. The 17-model panel did not expose models to one another's answers. Therefore:

- peer exposure = NONE in the archived benchmark;
- realized peer influence = NOT APPLICABLE, not a measured zero;
- shared evaluator = PRESENT;
- mapper = fixed-item answer-label mapping;
- free-form claim clustering = NOT USED in this benchmark.

The shared NLI checker is an evaluator dependency, not peer exposure or the free NLI claim mapper audited in VEY-024. The P1 panel cannot support claims of peer influence, social convergence, or collective intelligence.

## 4. Assistant-derived covariance-aware ESS

Let q_i be nonnegative normalized aggregation/influence weights, sum_i q_i = 1, and H = sum_i q_i^2. Let source estimates X_i have equal marginal variance sigma^2 and common off-diagonal correlation rho, with 0 <= rho <= 1:

```math
Sigma = sigma^2 [(1-rho) I + rho 11^T].
```

For theta_hat = q^T X:

```math
Var(theta_hat) / sigma^2
  = q^T [ (1-rho) I + rho 11^T ] q
  = (1-rho) sum_i q_i^2 + rho (sum_i q_i)^2
  = rho + (1-rho) H.
```

Define the variance-equivalent effective sample size relative to one marginal variance:

```math
N_eff^(weighted, exchangeable)
  = 1 / [rho + (1-rho) H].
```

This formula connects two special cases:

- **Independent source errors:** rho = 0 gives N_eff = 1/H, the weight-concentration ESS in Liu et al.
- **Uniform weights:** q_i = 1/k gives H = 1/k and therefore N_eff = k / [1 + (k-1)rho], the existing Kish exchangeable-panel formula.

Under the stated assumptions, positive common correlation reduces the variance-equivalent ESS relative to the independent weight-concentration value. This is a conditional model identity, not a measured correlation or a universal ESS definition.

For a non-exchangeable covariance matrix, the appropriate variance is q^T Sigma q. A scalar weight-concentration value alone is insufficient; any covariance-aware ESS must declare its reference marginal variance and the actual covariance model.

## 5. Formalization in existing HsH PR #850

The existing Orson PR was reused; no new branch or PR was created.

- Branch: `research/orson-p1-shared-nli-bound-20261028t06z`
- Pre-update head: `e0959eea92c0061510305031e90d976176b55a98`
- New commit: `b6f6108077e4d81e285ed968c317f65b620e32c6`
- Updated module: `FORMAL_VERIFICATION/HsHVerification/OrsonKishEffectiveSampleSize.lean`
- New module blob: `bcc9e15ca2d2c2bf7da21f77f79b0f03ab99c6aa`
- Root aggregator already imports this module; no root change was needed.

The new conditional Lean targets are: normalized variance-factor reduction; the rho=0 weight-concentration case; the H=1/k Kish case; uniform-vector concentration; and the finite-vector uniform specialization.

The commit was independently read back from the existing PR branch. No new workflow run was visible at the first check. **Compilation of this extension is pending.** The previous VEY-025 merge-reference build #41420522501 predates this commit and does not verify these new declarations. Local Lean/Lake are unavailable in this runtime.

The formalization does not prove the covariance model, source translation, empirical exchangeability, the validity of q for a real system, or any P1 result.

## 6. P1 disposition and protocol consequence

P1 issue #564 remains **SOURCE / EXPERIMENT READINESS**.

- Original OV-49–OV-53 neutral-versus-false-authority answer-keyed cognition bank: UNRECOVERED.
- Authorized model-inference endpoint: NOT AVAILABLE.
- No model call, human-subject session, new HsH trial, API spend, or independent replication.
- No empirical covariance matrix or per-item aggregation-weight vector is available for the P1 archive; no covariance-aware numeric ESS is computed.
- The local three-page P1 LaTeX/PDF draft described in prior notes was not found in the inspected repository/P1 docket surfaces. Its exact wording, compilation, PDF and reader status remain unaudited.
- No manuscript edit, PDF/reader completion, independent paper review, paper-gate advancement, or author sign-off occurred.

**Protocol recommendation for the November 2 freeze:** retain the source-reanalysis/methods-only P1 path if the original bank and authorized inference route remain unavailable. For any future interaction experiment, log the exposure graph, actual recipient visibility, realized-influence/readout weights, source ancestry, receiver pre/post state, evaluator/mapper/aggregator identity, and a declared covariance model. This is a recommendation, not a paper-gate decision.

P1 November 9, P2 November 30, and P3 December 14 remain separate gates. HSH_RESOURCES is a cognition research shelf, not H(s)H theory BEDROCK.

## 7. Reproducibility, limits, and return cursor

- External primary-source reading was targeted, not a systematic review.
- No raw SNLA run artifacts or code repository were independently retrieved.
- The OSF DOI lead remains metadata-only.
- All four shared Mersearch request lanes remained occupied; no request was created, overwritten, or duplicated.
- Existing Mathlib/Lean PR #850 and installed SciSpace were reused. No new tool, dependency, fork, paid service, or inference endpoint was introduced.
- The source-level and formalization findings are research/methods results only; no physical analogy, SAT/H(s)H theory claim, or BEDROCK promotion follows.

**Next:** verify a workflow run on exact new PR commit `b6f6108077e4d81e285ed968c317f65b620e32c6`; inspect the module's theorem-specific `#print axioms` output and full build log. If no run appears, do not claim compilation. Keep the P1 protocol recommendation distinct from the November 9 paper gate.
