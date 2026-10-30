# VEY-014 | P1 source-pipeline, archive-dependence, and protocol-scope audit

**Date:** 2026-10-30  
**Run:** `REVROT3-19-20261011:467:s1`  
**Selection:** Orson Vay, index 18; next ring identity Sable, index 0.  
**Identity status:** Current assistant reconstruction in the selected Orson specialist lane. No original Orson ChatGPT thread access or historical-instance continuity is authenticated.  
**Disposition:** Source audit complete; P1 scope correction recommended; no new model trial; exact-head Lean compilation pending.

This is an internal research/protocol note, not a manuscript, not a preregistration, and not a claim of an administered experiment.

## 1. Executive result

The original ConsistencyBench implementation establishes a narrower and more precise data-generating process than the phrase “multi-agent scientific review” suggests.

The archived CGD run contains:

1. A model-specific initial answer to a benchmark question.
2. A **shared, hard-coded GPT-4o-mini NLI checker** that compares raw answers from the same model's earlier and current questions.
3. A revision prompt that gives the model contextual question/premise information and the checker result.
4. A post-hoc comparison of the 17 model-labelled outputs against a published answer key and against panel-majority summaries.

The model calls do **not** receive other models' answers. The panel majority is computed after the answers exist. The common checker is a shared evaluator, not a peer agent and not a shared scientific evidence source.

Therefore the archive supports a source/evaluator-pipeline audit and a descriptive reanalysis of agreement measures. It does not identify a causal peer-influence effect, a shared-source intervention, or semantic error dependence. It is a logical-reasoning benchmark, not a scientific-review trial.

The HsH agent archive adds a second, real workflow layer: multiple worker-labelled analyses and reviews repeatedly inspect the same 17 immutable output blobs. That is evidence of **analysis multiplicity over a common empirical substrate**, not 17 new model trials per reviewer. Aster's earlier source-ancestry audit recorded 119 receipt/file inspection edges collapsing to 17 distinct original output files. The ratio is a provenance diagnostic, not an independence estimator.

## 2. Exact primary implementation source

**Repository:** `aayambansal/ConsistencyBench`  
**Path:** `src/evaluate.py`  
**Git blob:** `0453540cb7c19227601e59fb342fa93e736da849`  
**Read:** exact blob content, 327 lines.

Relevant source regions:

- Lines 82-95: `CGD_REPAIR_PROMPT` includes the prior question, prior answer, relation/premise, and current question.
- Lines 181-209: the model is called with the question prompt; `reasoning_ref` is retained as output metadata rather than supplied as model input.
- Lines 238-289: `evaluate_cgd` obtains the current raw response, checks it against earlier raw responses from the same model's question set, optionally requests a revision, and stores initial response, initial extraction, contradiction flag, revision response, final extraction, and `reasoning_ref`.
- Lines 296-327: `NLIContradictionChecker` constructs a prompt from **Response 1** and **Response 2**, without the question or premise, and calls the hard-coded route `openrouter/openai/gpt-4o-mini`.

### 2.1 Pipeline details that matter

**Question-blind checker.** The NLI checker receives two raw answer strings. It does not receive the question, the question-set premise, or the published answer key. It can therefore flag a textual contradiction without deciding whether either answer is correct in context.

**Contextual repair prompt.** When a contradiction is flagged, the revision model receives the prior question, prior extracted answer, the relationship/premise, and the current question. The checker and the revision model therefore operate on different information sets.

**Stale-initial / final-label split.** The loop appends `(question, final_answer, raw_response)` to its prior-QA list. A later checker call receives `prev_raw`, which is the earlier initial raw response, while the repair prompt receives `prev_answer`, which is the earlier final extracted label. This is the source-level basis for the previously reported stale-initial-evidence/final-label repair-context split. It is not a new finding, but it is now independently tied to the exact primary implementation blob.

**Checker audit trail.** The result record stores the Boolean `contradiction_detected`, not the raw NLI response text or a full checker-call trace. The archived outputs therefore do not permit independent re-adjudication of the checker decision from its original generated explanation.

**No peer-answer input.** The checker compares a model's own prior/current responses. No other model's answer is passed to the model or checker in this function. The 17-model majority is computed downstream. It is an ex-post statistic, not a causal input.

**Common instrument.** All model routes share the same hard-coded NLI checker route. This is a common measurement/revision instrument and a plausible source of correlated measurement error. The archive does not contain a randomized checker ablation, so the causal contribution of that checker cannot be estimated.

## 3. Evidence units and dependency layers

Keep these units separate:

| Layer | Observable object | What it can support | What it cannot support alone |
|---|---|---|---|
| Benchmark | Question and published `expected` key | Key-match rates | Human-validated semantic truth |
| Model route | One of 17 model-labelled CGD JSON files | Descriptive route-labelled outputs | Verified backend deployment identity |
| Checker | Shared GPT-4o-mini Boolean contradiction flag | Pipeline description and association | Independent adjudication or causal checker effect |
| Revision | Initial and revised answer labels | Transition counts and key-match changes | Peer influence, absent peer exposure |
| Panel | Post-hoc majority over model labels | Majority coverage and key-match summaries | Deliberative consensus or a peer-treatment effect |
| HsH worker archive | Worker-labelled reports/receipts reading the same source blobs | Provenance and analytical-dependence graph | Independent model trials or independent datasets |

The existing source-locked reanalysis is based on 17 exact CGD output blobs, each with 300 sets and 1,150 aligned question positions, for 19,550 model-question records. The original benchmark is larger; this CGD output subset must not be described as the entire benchmark.

The current VEY-011 and VEY-013 results remain unchanged:

- Complete-case individual published-key match: 68.02% to 71.79% (+3.77 percentage points).
- Alignment to the fixed leave-one-out **initial** strict majority: 81.63% to 79.38% (-2.25 percentage points).
- Question-level strict panel-majority key match among covered positions: 69.55% to 77.83%; the all-question correct-majority fraction rises by 7.83 points.
- Mean pairwise phi of published-key disagreement: 0.501 initially and 0.457 after revision across 136 model pairs.

These are three different readouts. None should be called “the consensus score.” The fixed initial majority is computed from the archive and was not shown to the models. The pairwise phi is co-disagreement with a published key, not semantic error correlation against independently adjudicated truth. Pair-specific missingness, common items, the common checker, and model-family relationships remain relevant dependencies.

## 4. P1 interpretation and scope correction

The current issue #564 question is valuable, but the present data do not support the broadest causal reading of “shared-source errors and apparent consensus in multi-agent scientific review.”

A defensible P1 is an **archival/methodological case study of evidence dependence in an AI-assisted research workflow**, with two nested empirical layers:

1. **Benchmark layer:** 17 model-labelled outputs from one reasoning benchmark, one common evaluator, repeated/common items, and post-hoc panel summaries.
2. **Research-workflow layer:** multiple HsH worker-labelled analyses that inspect the same 17 immutable output blobs and the same evaluator source. The report count is not the dataset count.

A suitable working title is:

> **Agreement Is Not One Thing: Key Accuracy, Post-hoc Panel Majority, and Within-Model Revision Under a Shared NLI Checker**

A broader workflow-oriented alternative is:

> **Report Count Is Not Evidence Count: A Source-Lineage Audit of an AI-Assisted Research Workflow**

The manuscript may compare both layers, but must not treat worker reports as independent model responses or the 17 route labels as 17 independently authenticated deployments.

### Required language

Prefer:

- “published-key match” over unqualified “correctness”;
- “post-hoc panel majority” over “peer consensus”;
- “within-model revision under a shared NLI checker” over “peer influence”;
- “co-disagreement with published keys” over “semantic error dependence”;
- “common evaluator” over “shared evidence source,” unless a common source record is actually manipulated;
- “worker-labelled analysis artifacts” over “independent agents,” unless model-instance identity is authenticated.

Do not claim the ConsistencyBench run is a scientific-review experiment. It is a logical-reasoning benchmark.

## 5. Separate mechanisms, separate estimands

The paper should distinguish at least five mechanisms:

1. **Passive model-error dependence:** different model outputs fail on the same items, potentially because of shared training data, architecture, item difficulty, or benchmark construction.
2. **Common-evaluator dependence:** multiple model outputs are revised or scored through one shared checker.
3. **Common-content/source exposure:** models receive the same external evidence or source record.
4. **Peer-message exposure:** models receive another agent's answer or a message representing a peer majority.
5. **Authority attribution:** the same content is labelled as coming from an expert, institution, or high-status source.

These mechanisms can coexist, but they are not interchangeable. A source-sharing treatment does not automatically measure peer pressure. A peer cue can change individual response marginals without increasing residual pairwise error dependence. A shared checker can change revisions without models ever seeing one another.

### External primary literature crosswalk

- **Kim et al. (2025), “Correlated Errors in Large Language Models,” ICML/PMLR 267.** Peer-reviewed evidence on passive cross-model error dependence. It is not a shared-source or peer-exposure intervention.  
  https://proceedings.mlr.press/v267/kim25e.html

- **Hossain, Yousefi & Lim (2026), “Agreement Overstates Evidence: Error Dependence in LLM Judge Consensus,” arXiv:2609.22512.** Preprint; passive judge-error dependence, not a source-sharing intervention.  
  https://arxiv.org/abs/2609.22512

- **Kohli et al. (2026), “Nine Judges, Two Effective Votes,” arXiv:2605.29800.** Preprint; panel dependence evaluated against human annotations. Not a source-sharing intervention.  
  https://arxiv.org/abs/2605.29800

- **Kuai et al. (2026), “A Statistical Framework for Auditing Behavioral Dependence and Induced Bias in LLM Judges,” arXiv:2604.07650.** Preprint; dependence metrics and judge bias. The authors do not identify a single causal origin for dependence.  
  https://arxiv.org/abs/2604.07650

- **Hu & Qu (2026), “Social Pressure Breaks Majority Voting in LLM Safety Panels,” arXiv:2608.04415.** Preprint; controlled peer-label cue exposure. The “peer” content is inserted prompt text, not a live exchange of independently generated peer answers. Their wrong-cue condition shifts individual false-alarm rates; the reported panel collapse is consistent with an independence prediction from those shifted marginals. The solo-versus-silent-peer comparison also shows that re-query/presence effects need their own control.  
  https://arxiv.org/abs/2608.04415

- **Hu & Qu (2026), “Most LLM Conformity Needs No Speaker,” arXiv:2607.05545.** Preprint; repeated content without speaker attribution still changes responses, with attribution adding an increment. The source-free arm is not a no-information control.  
  https://arxiv.org/abs/2607.05545

- **Qu et al. (2026), “Easier to Mislead Than to Correct,” arXiv:2606.01637.** Preprint; peer-majority and authority cues. It is from a related research group to the Hu & Qu studies, not an independent replication.  
  https://arxiv.org/abs/2606.01637

Do not compare the numerical coefficients in these papers directly with VEY-013's pair-specific key-disagreement phi. Their tasks, ground truth, missingness, item-difficulty conditioning, and interventions differ.

## 6. Original cognition-bank locator correction

The Orson role-charter pointer to an “OV-49–OV-53 matched cognition test bank” does not resolve to that artifact in the accessible archive.

The located OV-49–OV-53 materials are geometry/finite-core sandbox work. The OV-54 cross-read review gate explicitly records this mismatch. OV-55/56 are assistant-authored analytical toy-model notes; they are not records of administered LLM trials.

Other cognition-related artifacts are distinct:

- OV-77 describes a 52-prompt archive-identifiability design. Its local package is referenced by the note but was not located in the current HsH repository or Library listing.
- OV-95 describes a 24-case artifact-presence calibration. Its package exists in the Library, but it is not the requested neutral-versus-false-authority answer-keyed bank.
- OV-96, OV-98, and OV-99 are scorer, power, and counterbalancing gates.
- OV-100 is a shared-source authority-gate analytical model, not an administered trial.

Therefore the specific matched neutral-versus-false-authority cognition bank remains **UNRECOVERED**. Do not substitute OV-77, OV-95, or OV-100 without an explicit protocol decision. Do not edit the role charter's source pointer automatically; preserve this discrepancy for Nathan/Orson reconciliation.

## 7. Protocol decision for the November 2 freeze

Unless an authorized model-access route and the actual answer-keyed test bank are recovered before the freeze, P1 should proceed as a clearly limited archival/methodological manuscript. No synthetic OV model may be presented as an administered LLM trial.

The separate VEY-004 controlled study remains queued. Its protocol should orthogonally distinguish:

- no added content;
- repeated content without a named speaker;
- correct versus incorrect peer-label content;
- expert/authority attribution;
- common-source versus disjoint-source evidence;
- independent versus shared evaluator.

Use actual peer outputs only if they are actually generated and recorded; otherwise label the stimulus “inserted peer-message text.” Include a silent-peer/re-query control, blinded human semantic adjudication, predeclared item/model/session exclusions, and item- and model-family-clustered inference. Do not collapse all factors into one contrast.

The current runtime has no connected external model provider, model weights, local inference runtime, or authorized provider credentials for a new multi-model trial. No new LLM calls were made and no paid API was used.

## 8. Manuscript and review gate

The prior Orson handoff records a three-page D1 PDF and TeX under a previous runtime-local directory, with a reader-patched derivative also mentioned. The current HsH repository and Library searches did not recover those bytes. The local path is not mounted in this run. The D1 was explicitly described as unreviewed and not the final November 9 paper.

Consequently:

- no current PDF byte-for-byte verification;
- no current reader rendering verification;
- no independent/hostile review completion;
- no manuscript acceptance or publication claim.

The Nov 9 P1 gate remains open. The P1 must include actual primary sources, an independent/hostile review, and a readable PDF/reader. The Nov 30 P2 and Dec 14 P3 gates are unchanged.

## 9. Lean 4 / Mathlib repair status

PR #850 remains open and draft. This run edited only Orson's existing module:

`FORMAL_VERIFICATION/HsHVerification/OrsonSharedRecordIdentifiability.lean`

Repair commits:

- Initial repair: `852cb0c92d75f18b1d788a34d7286af1745f3017`
- Factor-nonzero repair: `89c5b66df723e63f5a8770217888cb0ac211a54b`
- Current module blob after the second repair: `deba2631c6ca2dba2ef9180fc41416237cd99806`

The first repair corrected:
- multiplication grouping in the zero-difficulty pattern factor;
- the noncomputable real-valued correlation definition;
- the interpretation of the pattern theorem as pointwise expression equality, not a complete finite PMF or normalization proof;
- a nondegenerate-variance domain theorem;
- validity of the alternative gate-parameter pair in the non-identifiability witness.

Exact-head CI #41046923313 then failed on the two moment-recovery proofs because a nonzero product hypothesis was not split into nonzero factors. The second repair now derives `1-q ≠ 0` and `p ≠ 0` before `field_simp`.

**Current status: REPAIR_COMMITTED_NOT_COMPILED.** No new Lean run was observed for exact head `89c5b66...`. The workflow file supports `workflow_dispatch`, but the available GitHub connector exposes rerun of existing jobs and no dispatch action. Rerunning #41046923313 would compile the old head, not this repair. A permitted owner must dispatch the existing Lean workflow against the exact current PR head.

A separate conversation-JSON-content workflow failed without exposing job records. It is not Lean evidence. Preserve both the earlier failed compiler logs and the current pending state.

Even after compilation, Lean will verify only the encoded algebraic statements. It will not establish empirical source dependence, semantic correctness, or causal influence.

## 10. Mersearch, tooling, and scope discipline

The Mersearch worker guide and all four shared request lanes were inspected. Lane 1 (Mercer spin-precession request), lane 3 (chemistry), and lane 4 (superconductors) have run manifests and compact receipts. Lane 2 (optics) has no manifest/receipt at the expected path and remains pending/unverified. The request files' `status: requested` field is request metadata, not execution proof. No lane was overwritten and no new Mersearch request was issued.

This selected Orson turn stayed within the protected cognition remit; no SAT-O/Blockwave physics search or physical calculation was undertaken. Existing Lean/Mathlib, Math Hopper guidance, GitHub workflows, and SciSpace were inspected before any software proposal. No new software, dependency, or plugin was installed.

FIE was last fully revisited on 2026-10-27; the 14-day revisit threshold has not arrived.

## 11. Decisions and open items

| Item | Status |
|---|---|
| ConsistencyBench evaluator source read by exact blob | COMPLETE |
| Common checker / no-peer-input distinction | ESTABLISHED from source |
| HsH report multiplicity vs 17 raw source files | EXISTING source-ancestry audit; do not count as independent trials |
| P1 archive/methods scope recommendation | READY FOR PROTOCOL DECISION |
| OV-49–53 cognition-bank pointer | MISMATCH CONFIRMED |
| Requested neutral/false-authority answer-keyed bank | UNRECOVERED |
| OV-77 package | NOT LOCATED in current repo/Library |
| OV-95 package | PRESENT, DIFFERENT study |
| New LLM trial | NOT RUN |
| Human semantic adjudication | NOT DONE |
| D1 TeX/PDF/reader bytes | NOT RECOVERED in current runtime |
| PR #850 current repair | COMMITTED, COMPILATION PENDING |
| Independent/hostile P1 reviewer | NOT CONFIRMED |
| Nov 2 protocol freeze | OPEN |
| Nov 9 P1 paper gate | OPEN |

**Recommended disposition:** keep P1 alive as a source-grounded archival/methodological paper, but remove causal peer-influence and shared-source claims from the empirical results unless a separate controlled experiment is actually run. Preserve VEY-004 as the future intervention study. Do not promote OV-55/56 or OV-100 from analytical models to empirical findings.
