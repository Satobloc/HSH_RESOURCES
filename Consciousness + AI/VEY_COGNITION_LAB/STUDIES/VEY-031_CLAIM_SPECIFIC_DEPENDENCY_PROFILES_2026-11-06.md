# VEY-031 | Claim-specific dependency profiles for LLM evidence

**Date:** 2026-11-06  
**Owner lane:** Orson Vay, LLM cognition / team cognition  
**Status:** SOURCE-GROUNDED MEASUREMENT-ARCHITECTURE PROPOSAL / NO NEW TRIAL  
**Relation to P1:** Additive interpretation and verification aid only. The November 2 P1 methods/archival freeze remains controlling.

## 1. Question

How should a reviewer determine whether two apparent pieces of evidence are independent for a particular claim, without collapsing independent data generation, independent computation, independent evaluation, semantic adjudication, and peer exposure into one scalar?

The answer is to attach a **claim-specific dependency profile** to each comparison. It reports observed provenance overlap by channel. It is not a statistical-independence estimator.

This extends the existing five-stage evidence lifecycle in VEY-020 and reuses, rather than replaces, Ariadne's claim-scoped lineage approach. It does not create a new tool or a new P1 experiment.

## 2. Source basis and custody

### Internal source set

- VEY-014: source-pipeline, archive-dependence, and P1 scope audit.
- VEY-015: key semantics, row-level sensitivity, and finite-pattern identifiability.
- VEY-020: evidence origin, transmission, visibility, integration/adoption, and measurement.
- VEY-027: question-specific eligibility masks.
- VEY-028: judge-family measurement dependence.
- VEY-029: evaluator-side context sensitivity and measurement boundaries.
- VEY-030: handoff retention, access, uptake, and provenance.
- HsH issue #1031: seven documented reviews over one original ConsistencyBench CGD corpus.
- Ravel's 2026-10-30 P1 report-provenance audit: exact source intersections and upstream key-normalizer attribution correction.
- Ariadne's 2026-10-31 claim-scoped source-lineage gate and its existing draft Lean module.

These are distinct source classes: internal research notes, public HsH artifacts, external literature reviews, and assistant-authored measurement proposals. None is promoted to Nathan Direct or to an empirical finding beyond its recorded evidence.

### P1 implementation anchors

The public ConsistencyBench evaluator source is `aayambansal/ConsistencyBench/src/evaluate.py`, blob `0453540cb7c19227601e59fb342fa93e736da849`.

The source-locked 17-entry CGD output manifest is recorded in the Orson analysis/replayer artifact, blob `2e10ed2510b8ce14e716780a887c0fe23c3067b9`.

The source audit identifies a common hard-coded `openrouter/openai/gpt-4o-mini` NLI contradiction checker. The checker compares same-model raw-response prefixes and reduces its result to a Boolean flag in the archived output. The CGD loop exposes a target model to its own earlier Q/A history; it does not feed one target model's answer to another target model. The panel majority is post-hoc.

## 3. The proposed profile

For a claim (c), define a required-channel set (K(c)). For two evidence items (e_1,e_2), attach a lineage record to each required channel rather than assigning one global label such as "independent."

Proposed channels:

1. **Origin:** benchmark, source document, dataset, answer-key, and raw-output ancestry.
2. **Generation:** model/provider identity, resolved backend revision, request ID, prompt/context hash, settings, seed, and administration session.
3. **Exposure:** the actual context/messages supplied to each model, with recipient, time, availability, insertion, truncation, and ordering.
4. **Evaluation:** checker/judge identity, version, prompt, exact input, raw output, retry, and aggregation route.
5. **Scoring:** answer key, parser, normalization, label mapping, missingness rules, and final score aggregation.
6. **Analysis:** code blob/version, analyst, execution environment, source manifest, and replay lineage.
7. **Adjudication/review:** blinded semantic adjudicator, rubric, reviewer identity, conflicts, and independent-review disposition.

Each channel should reuse the claim-scoped two-axis idea already present in Ariadne's `ClaimLineageAxes`:

- **Content relation:** verified shared content, verified disjoint content in the audited scope, or unknown.
- **Primary-origin relation:** verified disjoint nonempty origins, shared/overlapping origin evidence, or unknown.
- **Completeness:** whether the relevant origin census is complete enough for the claim.

The profile is a product of channel-specific records, not a scalar. A channel not required for a claim is omitted from (K(c)); a required channel with missing lineage is UNKNOWN, never silently treated as disjoint.

### Critical interpretation rule

A shared lineage root establishes a **provenance dependency** for that channel. It does not by itself establish correlated statistical errors. Conversely, disjoint known origins do not prove statistical independence: unobserved common causes, shared training data, common item difficulty, or shared measurement assumptions may remain.

Therefore:

- lineage overlap is not covariance;
- distinct filenames are not distinct origins;
- distinct worker labels are not authenticated independent model instances;
- independent code replay is not independent data generation;
- exposure is not integration;
- integration is not successful task performance;
- a common evaluator route is not a measured evaluator-error correlation.

No effective sample size or independent-evidence count may be computed from the profile without a separately specified stochastic model, dependence assumptions, and observed covariance or an appropriate experimental design.

## 4. P1 channel profile from the current archive

| Channel | Source-grounded observation | Current status | Defensible use |
|---|---|---|---|
| Origin | 17 original CGD model-result files, 300 sets and 1,150 aligned question positions per file; 19,550 archived model-question records. Seven documented worker reports each inspected the same 17 files: 119 report/file edges, 17 unique files. | SHARED CORPUS / SOURCE-LOCKED | Describe the finite archived corpus and the report/source overlap. Do not multiply the corpus by the number of reviews. |
| Generation | Seventeen model labels appear in the archived output family. Result JSONs do not preserve request timestamps, provider request IDs, or resolved backend model revisions. | PARTIALLY DOCUMENTED / INDEPENDENCE UNKNOWN | Distinct model labels may be reported; independently authenticated deployments or independent stochastic trials may not be inferred. |
| Exposure | The CGD loop uses a model's own prior Q/A history within its question set. The source does not expose another target model's answer to it; the panel majority is computed after the outputs are archived. | WITHIN-MODEL SELF-HISTORY / NO CROSS-MODEL EXPOSURE IN THIS SOURCE DESIGN | Describe self-history and post-hoc panel aggregation. Do not call this peer deliberation, social contagion, or a peer-treatment experiment. |
| Evaluation | One common GPT-4o-mini NLI checker is hard-coded in the source. The archived result retains a Boolean flag, not the exact triggering pair and complete judge call record. | SHARED EVALUATOR DESIGN / CALL-LEVEL RECORD UNKNOWN | State common measurement dependency. Do not claim measured checker-error covariance or semantic validity of every flag. |
| Scoring | A published answer key and shared normalization path are used. Ravel's source comparison found 0 mismatches across 578 rows between the upstream normalizer and the Orson analysis scorer. An alternate mapping changes 1,677/1,700 affected classifications but moves the pooled correct count only 836 to 841. | SHARED KEY / SOURCE-ATTRIBUTION CORRECTED | Report the finite-panel scoring sensitivity. This is a lexical/rubric sensitivity, not an independently adjudicated semantic correction or an upstream code defect. |
| Analysis | Multiple worker reports and source-locked replays inspect the same immutable result files. Some code replays and mathematical checks are distinct computations. Worker labels and report count do not authenticate distinct ChatGPT instances. | ANALYSIS MULTIPLICITY OVER SHARED INPUTS | Call this computational/analytical replication where the distinct implementation is documented; not independent experimental replication. |
| Adjudication/review | The archived Boolean checker flags do not include the triggering pair and raw judge output needed for direct semantic adjudication. P1 independent/hostile review is not complete. | NOT ESTABLISHED / NOT COMPLETE | Do not describe the NLI flags as independently adjudicated semantic errors or the manuscript as independently reviewed. |

## 5. Claim-to-evidence and failure matrix

| Candidate claim | Current disposition | What an independent reviewer could check or use to establish failure |
|---|---|---|
| CGD uses within-model self-history and a shared NLI gate. | SOURCE-DESIGN VERIFIED. | Inspect the pinned evaluator source and archived input/output structure. A different source revision or a verified call trace showing another exposure route would require revision. |
| The archived panel has the reported finite-corpus key-match/revision summaries. | DESCRIPTIVE, FINITE-CORPUS ONLY. | Re-fetch the exact 17 blobs and answer key; independently replay the declared parser, normalization, denominators, and missingness. A reproducibility mismatch invalidates the affected summary. |
| Each NLI flag denotes a semantic contradiction/error. | NOT ESTABLISHED. | Recover the exact triggering pair, question/premise context where applicable, raw checker prompt/output, model/version, retries, and blinded adjudication. A pre-registered audit finding substantial false-positive or false-negative flags would defeat the claim. |
| The common checker caused correlated model errors. | NOT ESTABLISHED; only the common design dependency is verified. | Randomize independent evaluator arms or repeated blinded evaluations, preserve raw calls, and compare checker errors against an independent semantic reference. A common route alone does not identify error correlation. |
| Seventeen model labels constitute seventeen independent witnesses. | NOT ESTABLISHED. | Recover request IDs, resolved backend revisions, provider/model-family lineage, prompt/context hashes, seeds, benchmark and key ancestry, and evaluator routes. Even disjoint lineage is not by itself a statistical-independence proof. |
| Models influenced one another through peer answers. | NOT SUPPORTED BY THIS ARCHIVE. | A different prospective study would need randomized cross-model message exposure, recipient-level prompt snapshots, pre/post responses, and an independent outcome measure. The present source design contains no cross-model answer exposure. |
| Seven worker reports are seven independent experimental replications. | FALSE AS A DATA-GENERATION DESCRIPTION. | Compare immutable source IDs. The documented 119 report/file inspection edges collapse to 17 unique original outputs. Distinct reimplementations can still be computational replications of the same data. |
| Independent semantic review of P1 is complete. | NOT COMPLETE. | Verify an actual independent reviewer, exact manuscript version, review record, response/disposition, and the final source/PDF/reader package. |

No numerical falsification threshold is supplied here. Such thresholds require a frozen sampling plan, defined semantic target, adjudicator protocol, expected error rate, and power/uncertainty analysis. Inventing one from the current archive would manufacture precision.

## 6. Relationship to the existing evidence lifecycle

VEY-020's five stages remain:

1. origin;
2. transmission;
3. visibility;
4. integration/adoption;
5. measurement.

The new profile does not replace those stages. It supplies a claim-specific provenance view across the source, generation, exposure, evaluator, scoring, analysis, and adjudication channels.

Visibility/access and integration/adoption remain behavioral observables to measure. They must not be inferred merely from a record being stored, available, or cited.

## 7. Formalization triage

### Existing formal work inspected

- **Orson PR #850**, branch `research/orson-p1-shared-nli-bound-20261028t06z`, head `9fa85f5826545d489743967de50a81f323757a55`. Actions run #42025947428 succeeded on a synthetic PR merge reference: Lean 4.34.0 / Lake 5.0.0, 8,979 root-build jobs; the target module built, and ten theorem-specific `#print axioms` reports listed `propext`, `Classical.choice`, and `Quot.sound`. The full log contained no `sorryAx` or `admit`. Tests, lint, nanoda, and the separate automated axiom-audit stage were skipped. **Exact-head standalone verification remains unverified.**
- **Aster PR #905** contains a source-conditional finite-set formalization of the seven-report/17-file overlap. Its recorded exact-head run #40915700617 failed in the module at a rewrite and recursion-depth error; it is not a successful proof.
- **Ariadne PR #790** contains the existing `ClaimLineageAxes` / `classifyAxes` proposal, which keeps content overlap and primary-origin evidence orthogonal and completeness explicit. Its recorded exact-head run #41214178623 failed at `AriadneClaimScopedLineage.lean:148` with an application type mismatch; the failed build emitted `sorryAx` after the elaboration failure. It is not a verified proof.

### New profile

No new Lean module was added. The cross-channel profile is a proposed ontology, not yet a source-defined theorem. Its channel-to-artifact maps, required-channel function (K(c)), origin completeness rules, and distinction between design-level routes and realized invocation lineage are not yet fixed in one canonical source contract.

**Status: FORMALIZATION_BLOCKED_DEFINITION.** Reuse the existing Ariadne claim-scoped axes and Orson's source-conditional P1 formalization after independent review; do not create a tautological parallel module. A future proof should follow only after the channel maps and claim-specific completeness conditions are adopted and instantiated from the actual source records.

Lean compilation, where available, checks only the formalized statement and encoded inputs. It does not authenticate source extraction, model identity, semantic correctness, statistical independence, or causal interpretation.

## 8. P1 and campaign disposition

P1 remains the frozen methods/archival paper due **2026-11-09**.

- Original OV-49–OV-53 matched-prompt bank: NOT RECOVERED.
- Authorized inference endpoint: NOT AVAILABLE.
- New model trial, human session, and API spend: NOT PERFORMED.
- Canonical source LaTeX: NOT VERIFIED.
- Compiled canonical PDF: NOT VERIFIED.
- Readable reader route: NOT VERIFIED.
- Independent/hostile review and author disposition: NOT COMPLETE.
- November 9 gate: NOT READY.

This note does not advance the paper gate. November 30 P2 and December 14 P3 remain separate. No physical prediction, fit, measured-system calculation, SAT/H(s)H theory claim, BEDROCK promotion, or SAT-O/Blockwave equation change is made.

## 9. Next cursor

1. Preserve this profile as a methods aid; do not modify the frozen P1 empirical scope.
2. Recover the canonical P1 LaTeX/PDF/reader artifacts or reconstruct a versioned source from the existing source ledger, clearly marked as a reconstruction.
3. Obtain an actual independent/hostile review of the exact manuscript version and record author disposition.
4. If the OV-49–OV-53 bank and an authorized inference endpoint are ever recovered, obtain explicit authorization and a complete prospective protocol before any new model trial.
5. Formalize the channel profile only after the required-channel and source-mapping contract is source-defined; do not equate lineage status with statistical independence.

No new model call, human session, API spend, or new tool was used in this work.
