# VEY-033 | CGD checker/repair projections, dual-history state, and trigger-lineage loss

**Date:** 2026-11-07  
**Status:** Source-grounded implementation audit plus source-conditional Lean formalization. No new LLM trial, human session, API spend, or P1 scope change.  
**Relation:** Additive to VEY-032 and the frozen P1 methods/archival protocol; not a replacement and not a new empirical result.

## Question

Does the Consistency-Guided Decoding (CGD) implementation use one coherent, premise-aware revision state, or does it pass different lossy views of the interaction to the checker, repair call, and archived result?

## Pinned primary source

- Repository: `aayambansal/ConsistencyBench`
- Commit: `bfc676baa848c7f1715bb73aee148180de15516e`
- File: `src/evaluate.py`
- Blob: `0453540cb7c19227601e59fb342fa93e736da849`
- Relevant source ranges: `evaluate_cgd` lines 238–292; `NLIContradictionChecker` lines 299–328; `run_evaluation` lines 448–520.

The exact pinned-commit fetch reproduced the same evaluator blob. The source file is therefore identified by immutable commit and blob, not by a moving default-branch URL.

## Source-derived implementation map

### 1. Checker projection

Inside `evaluate_cgd`, the NLI call receives `prev_raw` and the current `raw_response`. The checker prompt inserts only the first 500 characters of each response. It receives neither the previous question, the current question, nor the question-set premise, despite asking whether the responses contradict one another “given the same premises.”

Define the source-derived abstraction:

[
C(x) = (\operatorname{prefix}_{500}(x_{\mathrm{prevRaw}}),
        \operatorname{prefix}_{500}(x_{\mathrm{currentRaw}})).
]

This is a question/premise-blind, prefix-limited view. Any difference confined to the suffix after character 500 is invisible to this checker input. Distinct question/premise contexts with the same two raw-response prefixes produce the same checker input.

The checker call hardcodes `openrouter/openai/gpt-4o-mini`, temperature 0, and max_tokens 10. Its `model_id` parameter is not used to select the checker. The return value is a Boolean derived from whether the response contains the substring `CONTRADICTORY`.

### 2. Repair projection

When the first prior pair is flagged, the repair prompt receives:

- the previous question;
- the previous **final extracted answer**;
- a relationship string containing the question-set premise;
- the current question.

It does not receive the current first-pass raw response or current first-pass extracted label. The loop breaks at the first flagged prior pair, so the repair is conditioned on that first match rather than an exhaustive or ranked set of contradictions.

Define:

[
R(x)=(q_{\mathrm{prev}},a_{\mathrm{prev,final}},p,q_{\mathrm{current}}).
]

The checker and repair therefore operate on different projections of the same interaction. (C) omits questions and premise; (R) omits the current raw response and current initial label.

### 3. Dual-history state

After an optional repair, the history list appends:

[
(q_{t},a_{t,\mathrm{final}},r_{t,\mathrm{raw}}).
]

The second field is the final extracted answer; the third field is the original raw response. On later questions, the checker reads the third field (`prev_raw`), while the repair prompt reads the second (`prev_answer`).

Thus a revision updates the repair-facing answer but does not replace the checker-facing raw history. The implementation carries two distinct histories:

- **judge history:** original raw response;
- **repair history:** final extracted answer.

This is a source-level state asymmetry. It does not by itself establish that the asymmetry changes accuracy, flag rates, or semantic consistency.

### 4. Checker-instance scope

`run_evaluation` constructs an `NLIContradictionChecker` once for a particular model/strategy run and reuses it over that run's question sets. It is not one global mutable checker object shared across all 17 target-model runs. “Shared evaluator” is accurate at the level of the hardcoded endpoint/configuration and measurement rule, not as a claim of shared conversational state or one persistent judge instance.

### 5. Archived-result projection

The CGD result record preserves question, expected answer, initial response, initial extracted answer, the Boolean contradiction flag, revision response, final extracted answer, and reasoning reference. It does not preserve the triggering prior pair, the exact checker prompt, raw checker output, call ID, retry history, or resolved backend revision.

Consequently, two distinct full checker traces can map to the same archived result record. The Boolean flag and revision response do not uniquely identify which prior answer caused the repair. The existing archive cannot reconstruct the exact flag-to-revision path.

## Why this matters for P1

The existing VEY-032 conclusion remains intact: the archive has one common checker configuration, within-model self-history, and no cross-model answer exposure in the inspected CGD path. The new finding refines what “checker flag” means:

- it is a binary result from a truncated raw-answer pair, not a verified premise-relative contradiction;
- it is not an auditable record of the exact triggering pair;
- a prior revision does not replace the original raw answer in subsequent checker comparisons;
- the repair call sees a richer and different context from the checker that triggered it.

The frozen E1 statistic remains descriptive and answer-key-relative. E2 semantic validity remains NOT IDENTIFIED; E3 causal revision efficacy remains NOT IDENTIFIED. No P1 estimand or numerical result is changed.

## Source-conditional Lean formalization

A new module was added to the existing Orson P1 PR #850 branch:

- `FORMAL_VERIFICATION/HsHVerification/OrsonCGDProjectionGate.lean`
- Module blob: `5ae200ec6e640be02f9e186dab3e29fec44d608e`
- Root aggregator blob after import: `7bd69ca93c399ad39b0092015809e0418fe8ef0e`
- Branch: `research/orson-p1-shared-nli-bound-20261028t06z`
- Root-import commit: `78a08c506916cbaa9371100258f5b555c943405f`

The module formalizes seven conditional statements:

1. checker input is invariant under changes to questions, premise, and final answer when raw responses are fixed;
2. checker input remains on the original raw answer after a prior-answer revision;
3. repair input tracks the revised final answer;
4. repair input ignores the current raw first-pass response;
5. the 500-character prefix depends only on the first 500 characters;
6. identical checker views can correspond to different repair contexts;
7. the archived-result projection does not identify the triggering pair.

These theorems check the stated Lean abstraction only. They do not prove that the Python source was executed as read, that the abstraction faithfully translates every runtime detail, that the NLI verdicts are semantically correct, or that the asymmetry changes empirical outcomes.

At initial submission, the PR-triggered workflow run was pending. No compile-success claim is made until its actual job log and theorem-specific output are read. Local `lean`, `lake`, and `elan` are unavailable.

## Prospective test matrix (not authorized or administered)

| Hypothesis | Shared parameters | Calibration | Holdout | Predicted observable | Standard comparator | Falsification rule |
|---|---|---|---|---|---|---|
| H1: context/truncation projection materially changes checker behavior | Same exact answer pairs, target-model version, checker version/settings, and item order | Freeze a premise-aware adjudication rubric and judge prompt on a separate set of premise clusters | Unseen premise clusters and at least one held-out model family; score identical answers in both conditions | Flag flips and false-positive/false-negative rates against independent double adjudication | Current question-blind prefix-500 checker vs full-context/full-response checker | If the holdout difference lies wholly within a preregistered equivalence margin (\pm\epsilon), no material context/truncation effect is supported for that task; otherwise report the bounded difference |
| H2: dual-history state materially changes later flags or revisions | Same generator, question set, checker endpoint, prompts, and answer extraction | Calibrate the logging/parser and semantic rubric on disjoint premise clusters | Unseen premise clusters and held-out model family | Later-position flag rate, revision rate, final answer-key match, and independently adjudicated semantic consistency | Current original-raw judge history vs final-answer judge history vs no-revision control | If all paired holdout contrasts lie within preregistered (\pm\epsilon), no material state-history effect is supported for that task; otherwise report the task-bounded effect |
| H3: trigger-lineage instrumentation is necessary for unique attribution | Same CGD procedure and model/provider settings; preserve call ordering | Validate trace parser against known synthetic log schemas only, not as empirical observations | New instrumented runs with frozen prompt hashes and request IDs | Fraction of flags with a unique triggering pair and reproducible checker prompt/output | Current Boolean-only archive vs full trace with trigger pair, raw judge input/output, call ID, retry, and backend revision | If the instrumented record cannot uniquely recover the trigger pair, the proposed logging contract fails; if the current archived fields uniquely recover it for every eligible flag, the claimed archive non-identifiability is falsified |

No numerical (\epsilon), power, or sample size is supplied: those require a separately authorized design, calibration data, a defined semantic target, and a frozen inferential unit. The present archive cannot estimate these contrasts because the raw checker inputs/outputs and triggering pairs were not retained.

## Disposition

- P1 remains frozen to methods/archival scope; November 9 remains NOT READY pending canonical manuscript source, readable PDF/reader, independent review, and author disposition.
- No new LLM call, human session, API spend, or peer-exposure trial occurred.
- No claim of cross-model peer influence is introduced.
- No P1 protocol freeze, BEDROCK theory, paper gate, task ID, cadence, or branch ownership was changed.
- The existing PR #850 remains OPEN / DRAFT / UNMERGED. Exact-head verification is separate from a successful merge-reference build.
