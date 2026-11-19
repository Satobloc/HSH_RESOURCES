# VEY-043 Addendum 01 — denominator reconciliation and break-even message gate

**Date:** 2026-11-19  
**Owner lane:** Orson Vay / Vey Cognition Lab  
**Status:** SOURCE-VERIFIED FULL-TEXT ADDENDUM / SUMMARY-STATISTIC RECONSTRUCTION / ASSISTANT FORMALIZATION SUBMITTED / NO MODEL TRIAL / NO P1 PROTOCOL CHANGE  
**Relation to prior work:** Additive to VEY-043 (2026-11-12). This is not a new literature discovery and does not duplicate VEY-043's original crosswalk.

## Question

Can the denominator distinctions and the paper's stated 66% / 94% break-even detector-precision thresholds be reconstructed from the full arXiv text and published summary tables, and can the conditional decision rule be stated precisely enough for Lean formalization?

## Primary source and review extent

Yaxin Gong, Gangyi Zhang, Chongming Gao, Leyang Shen, Chenxiao Fan, Jiakai Wang, Dong Wang, Yang Liu, Wenjie Wang, and Xiangnan He, “When Upstream Messages Override Correct Answers: A Controlled Study of Multi-Agent LLM Collaboration,” arXiv:2609.36855v1, submitted 2026-09-29.

- Primary URL: https://arxiv.org/abs/2609.36855
- Full arXiv HTML reviewed: experimental design, §§3.2–3.6, chain-of-thought diagnosis, discussion, and relevant Appendix A.1, A.8, A.10–A.11, A.18–A.22, A.25–A.26.
- Model manifest and prompt templates are present in the HTML.
- Direct PDF, raw per-item outputs, experiment code, and a separately downloadable dataset were not acquired in this pass.
- No model API calls, human sessions, raw-data reanalysis, or independent replication were performed.

The paper is a preprint. Its own discussion limits generality to the tested models, benchmarks, oracle-quality evidence, discrete verifiable answers, and two-node handoffs. Open-ended generation, iterative debate, and longer chains remain untested.

## 1. Denominator reconciliation

The earlier VEY-043 note correctly retained the headline results but could not recover their exact denominators from the structured extraction then available. The full HTML resolves the distinction:

| Quantity | Numerator / denominator | Meaning |
|---|---:|---|
| Correct-to-wrong transitions, all 25 cells | 297 / 2,667 | Five receivers × five benchmarks, including DROP |
| Correct-to-wrong transitions, 21-cell adoption audit | 279 | Population for the upstream-correctness/adoption audit |
| Transitions in that 21-cell audit where upstream answer was wrong | 250 / 279 | 89.6%, reported as 90% |
| Specific wrong-answer adoption audit | 77 / 82 | 93.9%, reported as 94% |
| Four non-DROP benchmarks | 274 / 2,184 | Separate population; do not substitute for the all-25-cell denominator |

The 77/82 figure is conditional on the audited harmful subset. It is not 94% of all messages, all transitions, or all 2,667 items. The 297/2,667 rate is 11.1%; the highest single-cell rate is 32%. These denominators answer different questions and must remain separate.

## 2. Controls that narrow, but do not identify, the mechanism

The paper's full text adds several useful controls to the original VEY-043 crosswalk:

- **Conclusion reversal:** with receiver evidence fixed, corrupting a correct upstream conclusion lowers accuracy and correcting a wrong conclusion restores it across all 11 tested cells. The content manipulation is causal within those item/receiver conditions.
- **Minimal-edit control:** changing only the final answer and one conclusion sentence, while retaining at least 0.90 token overlap, produces significant correct-to-wrong flips in four of six LBM/HotpotQA cells after the stated Bonferroni correction; BIRD shows no significant effect in its three tested receiver cells.
- **Source-label control:** the same erroneous message under teammate, unverified-tool, unlabeled, and evidence-priority framing shows no significant pairwise differences among the labeled conditions in the adequately powered HotpotQA comparisons. All labeled conditions exceed the matched-hidden baseline. Kimi and LBM comparisons are underpowered or inconclusive in places. This does not prove social framing is irrelevant in general; it says the tested source labels did not explain the observed displacement.
- **Matched-review control:** both branches receive the same second-review structure; the hidden branch receives a neutral placeholder. Message exposure still produces more correct-to-wrong transitions (for example, BIRD gpt-4o-mini 17 vs 2, p<0.001; deepseek 9 vs 0, p=0.004). This narrows the second-attempt explanation.
- **Delayed receipt:** forming an answer before seeing the peer message does not reliably protect it from later substitution.
- **Evidence-priority instruction:** explicitly telling the receiver to prioritize evidence does not reliably eliminate the effect.
- **Chain-of-thought traces:** two annotators label 60 traces with AC1=0.98; strong-model traces often cite relevant evidence while adopting the peer's wrong answer. This is an annotation of generated traces, not direct access to internal reasoning. The paper itself notes that it cannot distinguish internal replacement of evidence-based reasoning from excessive weighting of the peer message.

The safest behavioral description is **message-content-sensitive answer displacement under the tested handoff conditions**. “Social conformity” is a possible explanatory family, not an established internal mechanism. The source-label controls make a simple teammate-deference explanation insufficient.

The paper reports a weighted mean message value with evidence of -0.6 percentage points (95% CI [-4.1,+3.3]), because helpful and harmful transitions nearly cancel in aggregate. Aggregate near-zero value does not mean no item-level effect.

## 3. Break-even detector precision: assistant reconstruction

Let:

- p = precision among messages flagged by a proposed error detector;
- g > 0 = benefit from removing a flagged message when it is actually wrong;
- c > 0 = loss from removing a flagged message when it is actually correct.

Under this two-outcome, constant-conditional-effect abstraction, expected net change per flagged message is:

E(p,g,c) = p*g - (1-p)*c.

Therefore:

E(p,g,c) ≥ 0  iff  p ≥ c/(g+c).

This is an assistant-reconstructed decision rule, not a theorem claimed by the paper. It assumes the two conditional effects can be represented by g and c; it omits heterogeneity, intervention cost, detector recall, calibration error, and uncertainty in estimated effects.

The detector precision p is not the same quantity as the upstream-error prevalence. Prevalence affects the precision a detector can achieve through its sensitivity/specificity, but the algebraic break-even threshold is determined by the conditional gain and false-positive cost once those are specified.

### Summary-statistic reconstruction

The paper's Table 1 gives message-removal gain on upstream-wrong items; Table 9 gives the unconditional message-removal effect on all with-evidence items. The upstream-wrong counts in Table 1 and total counts in Table 9 supply the mixture weight.

For upstream-wrong prevalence q, conditional gain g, and unconditional effect A, the implied removal effect on upstream-correct items is:

A = q*g - (1-q)*c

so:

c = (q*g - A)/(1-q).

Using the published rounded table entries:

| Benchmark | q | g (pp) | A (pp) | Implied c (pp) | Reconstructed p* |
|---|---:|---:|---:|---:|---:|
| BIRD | 92/150 = 61.33% | +10.9 | -1.3 | 20.6517 | 65.45% |
| L2W | 16/120 = 13.33% | +1.7 | -21.8 | 25.4154 | 93.73% |

The paper states approximately 66% for BIRD and 94% for L2W. The L2W reconstruction closely matches. BIRD's 65.45% is close to the stated approximate 66%; the unrounded bootstrap quantities used in the paper's threshold calculation are not available from the published one-decimal table entries, so the small difference is left unresolved rather than forced to match.

A sensitivity check allowing each one-decimal reported effect (g and A) to vary by ±0.05 percentage points gives arithmetic-only threshold ranges of approximately 65.30–65.61% for BIRD and 93.55–93.91% for L2W. These are **not confidence intervals**; they quantify only rounding sensitivity. No uncertainty propagation across the paper's paired bootstrap replicates is possible without the joint replicate outputs/covariance.

The result explains why unconditional message removal is net-harmful even when removal helps on the upstream-wrong stratum: removing correct messages is costly. It does not establish that any deployed detector reaches the required precision.

## 4. Conditional formalization submitted

HsH PR #2130, “Orson future methods: selective message-gating threshold”:
https://github.com/Satobloc/HsH/pull/2130

- Branch: `research/orson-selective-message-gate-20261119t2124z`
- Corrected source head: `918815a905d96f9c070fa90a6d66fcda1e8fa601`
- Module: `FORMAL_VERIFICATION/HsHVerification/SelectiveMessageGate.lean`
- Root import: `FORMAL_VERIFICATION/HsHVerification.lean`
- The module states the conditional threshold equivalence and encodes the rounded BIRD/L2W summary-statistic reconstructions as exact rational arithmetic.

First exact PR build:
- Run: https://github.com/Satobloc/HsH/actions/runs/44618869420
- Job: 135894786697
- Merge-source commit: `6b752dfe446303d8055c2e06e9a979c88ead04ea`
- Lean 4.34.0, Lake 5.0.0, Mathlib resolved revision `5ed2965256430c3649e86755f9576b54eca72435`.

The first build failed because a declaration doc-comment immediately preceded executable `#eval` commands. The theorem statements and rational expressions did elaborate far enough to print:
- thresholds: 5989/9150 and 3304/3525;
- percentage thresholds: 11978/183 and 13216/141;
- expected net at each threshold: 0 and 0.

The parser error was corrected by changing the comment to an ordinary block comment. The corrected head has not received a fresh exact-head workflow readback. Therefore the PR status is **LEAN_FAILED on the first head / LEAN_UNTESTED on the corrected head**, not LEAN_VERIFIED. The failed build's theorem-specific `#print axioms` output listed propext, Classical.choice, and Quot.sound; this is diagnostic output from a failed module build, not a successful proof certificate.

The runner generated a transient Lake dependency manifest. No committed `lake-manifest.json` or manifest SHA was retained. The workflow log does record the resolved revisions of mathlib and its eight direct/transitive packages; reproducibility is therefore bounded by those logged revisions and the pinned Lean toolchain, not by a preserved manifest artifact.

## 5. Separate prior MemOps proof closure

The earlier HsH PR #2112 was corrected and subsequently received a successful exact-head Lean workflow:

- PR: https://github.com/Satobloc/HsH/pull/2112
- Head: `ea298e2fb5cc0ff2dbd41812596d5e8c6003bc35`
- Module blob: `5b431136469647b8e3f5e7c0135ca8a5e1f730e3`
- Run: https://github.com/Satobloc/HsH/actions/runs/44618618439
- Job: 135893909762
- Workflow merge-source commit: `24716770657c1aa4986e53b20c50b98cf3b7ad98`
- Lean 4.34.0 / Lake 5.0.0 / Mathlib revision `5ed2965256430c3649e86755f9576b54eca72435`.

The module proves target-local Update/Forget preservation and a finite Remember→Forget / empty-history collision under an explicitly assistant-reconstructed two-target semantics. Executable outputs were `some (none, none)`, `some (none, none)`, and `true`. The five theorem-specific axiom reports list `propext` only. Tests, lint, nanoda, leanchecker and the global axiom audit were skipped. The paper itself does not supply this transition calculus; the formalization remains a method-level model, not a claim about actual LLM memory or product Memory.

The generated Lake manifest was transient. The workflow log records mathlib commit `5ed2965256430c3649e86755f9576b54eca72435`, plausible `118aa17ee84656b8bd727fef7c458ee8c833385c`, LeanSearchClient `ddf04cf3949fa556442341e87d47f9f6e6074707`, importGraph `e928b72544873815af278d38681b31c0293588e3`, ProofWidgets4 `106ff4fafc74ef4ac99d81dbf3ab399118f497a5`, aesop `355695d523e41d0554926416cba2a2b3544fbbc9`, Qq `6a489d9af5d0c47e5b259e2e8bcdfc1811b5a259`, batteries `f2effa3d803fda822b1f97b806c47cf2adfbcbc2`, and Cli `e92c9f15fdfacc8536f31cfb3b7ad26c3c8cd204`.

## 6. Factory Floor gate

The existing Factory Floor authority now requires a precise object-specific geometric plot, independent hostile fidelity review, and display of that plot with the submitted file before admission.

The MemOps projection proof is an abstract method-level state/provenance result, not a measured geometric system; no object-specific plot or independent hostile geometry review exists. It is therefore **NOT_FACTORY_FLOOR_ELIGIBLE**. A provenance-complete HsH FACTORY_HANDOFF_PENDING packet is prepared; no direct Factory Floor write, issue, Floor ID, LIVE, ARTIFACTS, WEBSITE, or BEDROCK promotion is claimed.

The selective-message-gate theorem remains unverified on its corrected head and is not eligible for a Factory handoff.

## 7. Research implication and next discriminator

A future controlled detector study should report, separately by benchmark and receiver:

- detector precision and recall on a held-out item set;
- calibration and confidence intervals for precision;
- the conditional benefit of removing a wrong message and cost of removing a correct one;
- intervention cost and any receiver-replacement effect;
- source-label, evidence-priority, delayed-receipt, and matched-review controls;
- exact item denominators and paired uncertainty.

A conservative gate would require the lower confidence bound for detector precision to exceed the estimated break-even threshold, not merely the point estimate. This is a proposed design, not an administered experiment or authorized P1 protocol change.

## P1 and project boundary

P1 issue #564 remains OPEN / NOT READY. The ConsistencyBench CGD protocol remains frozen to its existing archival/self-revision scope. PR #850 is untouched. No cross-model peer-exposure data were added to P1, no LLM or human trial was run, no API spend occurred, no manuscript was changed, and no November 30 / December 14 paper gate advanced.

This addendum is a literature-result and source-summary calculation with an assistant-reconstructed conditional formalization. It is not an independent measurement, raw-data replication, accepted P1 result, physical prediction, or H(s)H theory promotion.
