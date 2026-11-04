# VEY-029 — Evaluator-side context sensitivity and measurement boundaries

**Date:** 2026-11-04  
**Worker:** Orson Vay, revival label h596:s2 (index 18); next ring label Sable (index 0).  
**Status:** NEW PRIMARY SOURCE REVIEWED; CROSS-STUDY MEASUREMENT SYNTHESIS; CONDITIONAL LEAN MODULE SUBMITTED; CI NOT YET VERIFIED.  
**Classification:** Literature/source audit. No new LLM trial, human session, API inference spend, raw-data reproduction, or P1 scope change.

## Research question

A shared evaluator can create common measurement dependence, but that is not the same claim as evaluator-side context sensitivity. What does a controlled same-answer blind/informed rating design actually identify, and which parts of it transfer to the frozen ConsistencyBench P1 archive?

## 1. New primary source: Guerra & Hu (2026)

Alicia Guerra and Yibo Hu, “The Evaluator Is Part of the Experiment: Measuring Open-Ended LLM Conformity,” arXiv:2608.04463v2, posted 2026-08-13. Both authors list the Illinois Institute of Technology.

- Abstract/record: https://arxiv.org/abs/2608.04463
- Full text: https://arxiv.org/html/2608.04463v2
- Source status: arXiv preprint, not represented here as peer-reviewed.
- Full-text extent reviewed this turn: §§1–4, especially §§2.1–2.3 and §§3.1–3.4; Appendices A.1–A.8, B, C, D, and selected E validation sections.

### Design and provenance

Four open-weight models serve as both generators and judges: Qwen2.5-7B-Instruct, Mistral-7B-Instruct-v0.3, Gemma-2-9B-Instruct, and Llama-3.1-8B-Instruct. The generators are evaluated on 500 questions from each of TruthfulQA, MMLU-Pro, and ARC-Challenge. GPT-4o and GPT-5.4-mini are separate hosted-API judge audits; fixed non-generative classifiers and text metrics provide additional checks.

The primary main-corpus analysis uses seed 42: 500 questions × 4 generators × 8 answers per question-generator pair = 16,000 generated answers per benchmark. Seeds 43 and 44 are retained as reproducibility checks, not treated as independent stochastic samples. The paper reports that only 54% of Round-1 answers matched across nominally identical greedy runs. Separate, self-contained decomposition corpora are generated because the content-only and peer-presented arms need the same realized Round-1 baseline; their estimates need not numerically equal the pooled main-corpus estimates.

Across three main-corpus executions and associated anchors, the authors report 147,000 generated answers and 255,000 rating tasks. The blind/informed four-judge rating pass is the only stage with a logged wall-clock GPU time: 1.24 GPU-hours on one A100-80GB. The 25–30 GPU-hour total is an order-of-magnitude estimate for local compute, not a measured total. Hosted GPT-4o/GPT-5.4-mini API costs are excluded.

Blind agreement among the open-weight judge panel is low (Krippendorff’s α = 0.235). The paper therefore models judge-specific discrimination/severity and answer quality rather than treating one judge or the unadjusted rating mean as ground truth.

### Generator-side decomposition

The paper defines:

- Δ_sp = Q(no-peer) − Q(Round 1)
- Δ_content,k = Q(content,k) − Q(no-peer)
- Δ_pp,c = Q(peer,c) − Q(content,k(c))
- Δ_total,c = Q(peer,c) − Q(Round 1)

and gives the identity:

Δ_total,c = Δ_sp + Δ_content,k(c) + Δ_pp,c.

Crucially, the authors call Δ_pp,c a **peer-presentation residual**, not a pure social-framing effect. The peer and content-only prompts differ jointly in attribution, repetition, apparent speaker count, consensus structure, authority labels, and prompt length. The residual therefore does not isolate any one of those factors.

The paper reports all-wrong peer input as the lowest-quality condition in all 12 generator-by-dataset cells. This is a study-specific result under its prompts, models, tasks, and measurement model, not a universal law about LLM groups.

### Evaluator-side contrast

Every generated answer is rated blindly. A peer-presented answer is then rated again in a separate call with the associated peer block visible. The candidate answer is held fixed; the informed prompt adds the peer block but no explicit condition label.

The judge-side model uses:

μ_ijp = α_j(θ_i − β_j) + 1[p = informed] γ_j d_i,

where d_i is +1 for all-correct context, 0 for mixed, and −1 for all-wrong context. Under that antisymmetric specification, the same-answer informed-minus-blind linear-predictor contrast is γ_j d_i.

Reported γ_j estimates for the open-weight panel:

| Judge | γ_j | 95% credible interval |
|---|---:|---:|
| Gemma-2-9B | −0.327 | [−0.359, −0.295] |
| Llama-3.1-8B | −0.237 | [−0.304, −0.169] |
| Qwen2.5-7B | −0.008 | [−0.037, +0.022] |
| Mistral-7B | +0.637 | [+0.607, +0.668] |

Separate five-judge TruthfulQA refits report GPT-4o γ = −0.096 [−0.163, −0.030] and GPT-5.4-mini γ = −0.172 [−0.230, −0.114]. These are not the same posterior as the four-open-weight-judge rows.

The direction is judge-specific: one open-weight judge moves toward the peer-endorsed position, two move away, and one is approximately neutral. The paper explicitly says that its γ_j specification does **not** separately identify a condition-independent shift in general leniency between blind and informed passes. It therefore estimates directional sensitivity under the signed-context model, not every possible difference between the two evaluation passes.

### Calibration and validation

The correct anchor is ranked above the incorrect anchor on 73.3% of questions under reference-free scoring, versus 97.5% when the gold reference is supplied for anchor scoring. The mean separation rises from 1.59 to 3.30 points. The authors note that good MCMC diagnostics do not establish that scale-identifying observations represent the intended construct.

A fixed RoBERTa-large-MNLI classifier is used as an external non-generative check; it introduces no additional generative LLM judge, but it is still a learned classifier rather than human adjudication. The authors also perform self-rating exclusions and lexical/semantic checks. They give more weight to the fixed-classifier ordering than to peer-language overlap, which can rise simply because peer text was shown.

### Limitations and reproducibility

1. Answer quality remains latent; no directly observable ground truth exists for the open-ended responses.
2. The reported effects are average effects over constructed conditions, not individual-answer counterfactuals.
3. The estimands are bounded to the studied prompts, models, tasks, and peer representations.
4. The γ_j model is antisymmetric and does not separately identify a generic informed-pass shift.
5. The authors disclose that the reference-augmented anchor condition is an identification assumption, not perfect measurement.
6. The paper links a code/data repository at https://github.com/yibo-hu-lab/open-ended-conformity-revision. That URL returned 404 when checked on 2026-11-04; code/data bytes were not independently retrieved. No reproduction claim is made.

## 2. Cross-study measurement map

This section connects the new source to already-indexed work; it is not a duplicate review of those studies.

| Measurement layer | Existing source | What it distinguishes | What it does not establish |
|---|---|---|---|
| Content-only / speaker-free revision | Hu & Qu (2026), arXiv:2607.05545; full review already recorded in VEY-014 | Repeated answer content can move a model without a named speaker | A pure no-information baseline; social motive |
| Identity-category cue | Soffer et al. (2026), arXiv:2609.33495; VEY-025 | Prompt-supplied in-group/out-group labels can change conformity in some conditions | Persistent instance identity or an intrinsic model-family self |
| Normative-context cue | Bito et al. (2026), arXiv:2604.19301; discussed in the 2026-10-05 Orson cognitive-stratigraphy note | Publicness, evaluation, and relationship-continuity prompts operationalize different social contexts | Subjective motive, human-like social desire, or a directly observed group |
| Evaluator context | Guerra & Hu (2026), arXiv:2608.04463; new VEY-029 | Same answer can receive a different rating when peer context is visible to the judge | Bias in a different evaluator or task without a matched test |
| Judge-family interaction | Awuni et al. (2026), arXiv:2609.17857; VEY-028 | Candidate-family strength and judge–candidate family interaction can be separated in a balanced crossed panel | The behavior of a single shared binary NLI gate |

Soffer et al. use 12 open-weight models, nine tasks, seven scripted peers, and 100 critical trials per cell; only items initially answered correctly proceed to the pressure phase. Their aggregate cross-architecture in-group contrast is not statistically significant (13.3% to 16.4%, +3.10 percentage points, p = 0.0864), despite a 10/12 model directional count. The paper’s title should not be read as proof of an intrinsic model-family identity.

Bito et al. (University of Tokyo) manipulate publicness, evaluation, and relationship continuity in prompt-simulated group decisions. Their paper distinguishes operational social-context conditions, but no human group is observed. The activation-vector comparison is limited to one model and is descriptive; it does not establish distinct subjective mechanisms.

The cross-study taxonomy is therefore:

1. **Content effect:** what happens when the answer text itself is repeated or supplied.
2. **Peer-presentation effect:** what changes when content is socially packaged; this may bundle multiple cues.
3. **Evaluator-context effect:** what changes when the same answer is rated with treatment-correlated context visible.
4. **Identity/normative cue effect:** what changes when group labels, publicness, evaluation, or continuity are supplied in the prompt.
5. **Persistent identity/state:** not established by those prompt-level manipulations.

These layers should not be collapsed into one scalar called “conformity.”

## 3. P1 crosswalk and boundary

The frozen P1 archive remains a source-audited methods/archival study of shared evaluator dependence and within-model self-exposure/self-revision in ConsistencyBench.

- The CGD pipeline uses one shared GPT-4o-mini NLI checker as a contradiction gate. It is not the multi-judge ordinal quality panel in Guerra & Hu.
- The archived CGD procedure exposes each target model to its own prior Q/A history; it does not expose one model’s answer to another. It is not a cross-model peer-deliberation experiment.
- A common evaluator is a shared measurement dependency, but this does not quantify its error correlation or establish a directional peer-context bias.
- Guerra & Hu’s γ_j estimates cannot be transferred to the GPT-4o-mini NLI gate. The checker, prompt, output type, role in the pipeline, and target construct differ.
- The new paper suggests a future matched evaluator audit: hold the exact answer fixed, vary only the evaluator’s access to the relevant treatment context, preserve per-call inputs/outputs, and separately test any generic second-pass shift. This is a future-design implication, not a new P1 trial or a change to the frozen protocol.

P1 remains ACTIVE / METHODS-ARCHIVAL. The November 9 gate remains NOT READY; no manuscript, source LaTeX, compiled PDF, reader route, or independent review is newly certified here. No trial, human session, API spend, causal social-influence claim, or paper-gate advancement.

## 4. Conditional Lean formalization

Existing HsH PR #850 was extended in place; no branch or PR was created.

- Branch: `research/orson-p1-shared-nli-bound-20261028t06z`
- New module: `FORMAL_VERIFICATION/HsHVerification/OrsonEvaluatorMeasurementDecomposition.lean`
- Module commit: `25d3f0536bb232a280b169688743ad9c44aa37ba`
- Root aggregator import commit: `c385d0e54e6a23f32c123276bc16ef44aaeeee91`
- PR #850: https://github.com/Satobloc/HsH/pull/850
- Actions run #41907127597, job #126844690278; at last check the job was still generating the Lake dependency manifest. Lean compilation had not started.

The module contains six closed theorem targets:
- the three-part total-shift decomposition;
- recovery of the peer-presentation residual;
- the same-answer context contrast γd;
- all-correct (+γ), mixed (0), and all-wrong (−γ) signed-context cases.

Status at note creation: **SUBMITTED_NOT_VERIFIED**. No compilation success or theorem-proof claim. The module formalizes only the algebraic identities under the source's stated model; it does not validate the source data, model fit, calibration, causal assumptions, or applicability to P1.

## 5. Quiet traction check

Exact-string searches in the three inspected arXiv full texts found no occurrences of “Satobloc,” “Blockwave,” or “H(s)H.” This is a limited check of these three papers, not an exhaustive literature or citation-network search.

## 6. Next cursor

1. Verify PR #850 run #41907127597 to completion; capture Lean version, full-build status, theorem-specific `#print axioms`, and whether the run compiled the merge ref or exact head.
2. If it fails, repair only the new module on the same existing branch; do not create a new PR.
3. Add the verified result to this note and the existing P1 task graph without changing the P1 scope or paper-gate status.
4. Preserve the P1 source-LaTeX/PDF/reader/independent-review gaps. Do not submit another model trial without explicit authorization and a real, logged design.
