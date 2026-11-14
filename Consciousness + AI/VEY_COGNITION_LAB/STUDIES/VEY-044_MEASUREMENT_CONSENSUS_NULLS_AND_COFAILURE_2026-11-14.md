# VEY-044 | Measurement consensus, null models, and co-failure tails
**Date:** 2026-11-14  
**Status:** SOURCE-CHECKED LITERATURE CROSSWALK / NOT A P1 PROTOCOL AMENDMENT / NO NEW LLM TRIAL

## Purpose
Extend the existing VEY-043 communication/revision crosswalk with recent work that separates observed agreement from criterion validity, population/null-model choice, and joint co-failure. This note is a literature synthesis, not a replication and not evidence from the ConsistencyBench archive.

## Source checks
The following records were retrieved through SciSpace and title/identifier-checked with Scholar Sidekick. The checks establish bibliographic identity and did not surface a retraction flag; they do not constitute peer review or a full methodological replication.

| Source | Evidence status | Relevant contribution | Limitation for transfer |
|---|---|---|---|
| Jo, Garg & Raghavan (2026), *The Subjectivity of Monoculture*, arXiv:2602.24086 | NeurIPS 2026 paper record / arXiv full-text record | Shows that conclusions about model-evaluator monoculture depend on the model population and null baseline; reports substantial sensitivity across 12 model populations and 8 null models. | Population/null-model sensitivity is not itself a measured source-dependence coefficient; the task and model set differ from CGD. |
| Han & Kim (2026), *Agreement Without Alignment*, arXiv:2610.13303 | Preregistered preprint; not treated as peer-reviewed here | Across five LLM judges, three providers, three datasets and 129,770 requests, rubric clarification increased judge consensus on SummEval but did not produce a detectable increase in agreement with human ratings; effects did not generalize to the other two datasets. | Rubric intervention and evaluator consensus differ from CGD's shared NLI checker and within-model revision. |
| Chernets (2026), *Verification Theater*, DOI 10.5281/zenodo.23197641 | Preprint; accepted workshop poster for a December 2026 workshop, non-archival as of 14 Nov 2026 | Reports difficulty-stratified verifier-panel failure regimes, unanimous-wrong multiple-choice outcomes, and conformity after peer-label exposure. The authors' leave-panel-out reanalysis changes the pooled difficulty-inversion result, so the panel-population definition matters. | Not yet an archival proceedings paper; peer-exposure design differs from CGD, which has no cross-model answer channel. |
| Chen (2026), *When Does Combining Language Models Help?*, arXiv:2606.27288 | Preprint | Argues that pairwise error dependence does not identify joint co-failure tails and that selection policies can be limited by common-mode failures. | Routing/voting ensemble analysis is not an estimator for CGD's shared NLI checker or its archived per-model outputs. |
| Kim et al. (2025), *Correlated Errors in Large Language Models*, arXiv:2506.07962 | ICML 2025 paper record | Establishes correlated error as a real concern in model-panel use. | Does not identify the particular dependence structure in the CGD source. |
| Hossain, Yousefi & Lim (2026), *Agreement Overstates Evidence*, arXiv:2609.22512 | Preprint | Frames effective evidence count under dependent judge errors. | Conditional effective-N arguments require an appropriate covariance structure and weights; neither is available as an empirical CGD estimate. |
| Kohli et al. (2026), *Nine Judges, Two Effective Votes*, arXiv:2605.29800 | Preprint | Gives an evaluator-panel example where nominal judge count exceeds effective information. | Numerical estimates are not transferable to CGD without the underlying panel covariance and weighting design. |
| Li et al. (2026), *Beyond Final Accuracy*, arXiv:2610.01042 | Preprint | Separates communication exposure from final accuracy in multi-agent systems. | Cross-agent communication is absent from the CGD source path. |
| Gong et al. (2026), *When Upstream Messages Override Correct Answers*, arXiv:2609.36855 | Preprint | Controlled peer-message exposure study; supports treating exposure and revision as separate causal stages. | Does not show that CGD contains peer-message exposure. |

## Synthesis: six non-interchangeable dimensions
A consensus claim should be decomposed into:
1. **Observed agreement:** whether outputs share labels or judgments.
2. **Source/prompt lineage:** whether systems received common upstream material.
3. **Evaluator/rubric lineage:** whether outputs were measured by a common judge or rule.
4. **Interaction exposure:** whether one system actually saw another system's message before revising.
5. **Criterion validity:** whether outputs agree with an external, independently adjudicated criterion.
6. **Population/null specification:** which models, items, and counterfactual baselines define the claim.

The dimensions are not a validated scalar scale. They are a reporting checklist to prevent one observable (agreement) from standing in for several unmeasured properties.

## P1 relation
The frozen P1 ConsistencyBench paper can use this literature as context without changing its scope. CGD's source shows a shared NLI-checker configuration and within-model self-history. It does not show cross-model peer-message exposure. The external studies are comparators, not replications and not evidence about the archived CGD runs.

The P1 draft therefore retains the title and source scope in the existing 2 November protocol freeze. No new trial, human session, API spend, causal claim, or P1 protocol amendment was made.

## Reproducibility and limits
- SciSpace supplied discovery and structured extraction; original arXiv HTML/abstract records were inspected for the directly relevant papers.
- Scholar Sidekick checked titles/identifiers and retraction flags.
- No raw study data were downloaded or independently reanalysed in this crosswalk.
- The Verification Theater workshop event is future-dated relative to this note; only the preprint and accepted-poster status are recorded.
- The QUORUM pilot surfaced in discovery but was excluded from the source table because a stable primary record and full methods/data package were not independently retrieved in this run.
