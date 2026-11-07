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


## Error-path collapse and verification amendment | 2026-11-07T21:22Z

The pinned `call_model` source (lines 129–171) retries once and then returns the literal string `[ERROR]` after a second exception. The NLI wrapper (lines 306–328) converts the response to a Boolean by checking whether `CONTRADICTORY` occurs in the response text; a nonempty `[ERROR]` string therefore maps to `False`. The archived record does not retain the raw checker output or a separate error state.

This is a **source-level potential false-negative path**, not an observed failure count. No evidence was recovered that any of the 17 archived runs actually encountered this path. The correct output type for a future measurement pipeline is at least `CONTRADICTORY / NON_CONTRADICTORY / ERROR_OR_UNKNOWN`, with the error status excluded from the non-contradiction denominator.

Additional prospective test: inject timeout, rate-limit, malformed, empty, and successful responses into a local parser test; verify that failures remain distinct from a valid negative verdict. This is a parser/unit test, not a new model trial or empirical observation. The falsification condition is direct: if the pinned implementation or a separately logged runtime trace preserves an explicit error state instead of mapping it to false, the silent-collapse claim does not apply to that path.

### Lean verification

PR #850 Actions run `42415082103`, job `128531318905`, completed SUCCESS. The workflow checked out merge reference `dc12f2b3dfc5c6088289f5533c0de5ded60fa591`, which merges PR head `78a08c506916cbaa9371100258f5b555c943405f` into base `598a45b3feb9378eb8f14ff069ec9080137113c2`. Lean 4.34.0 / Lake 5.0.0; full root build completed 8,983 jobs; `OrsonCGDProjectionGate` built at 8981/8983. No `sorryAx` or `admit` string occurred in the captured job log.

The theorem-specific `#print axioms` output reports `propext`, `Classical.choice`, and `Quot.sound` for the checker-invariance and prefix-projection statements; the repair-view update/ignore-current-raw statements and archived-trigger non-identifiability statement report no axioms. The separate axiom-audit stage, tests, lint, and nanoda stages were skipped. This is a successful **merge-reference build containing the PR head**, not an exact-head standalone build or a global axiom audit.

The Lean module does not formalize the `[ERROR] -> False` branch. That remains a pinned-source control-flow observation; the formalized theorems cover checker/repair projection, dual-history invariance, prefix dependence, and archive non-injectivity only.


## Publication status correction | 2026-11-07T21:35Z

Public-safe content was submitted in issue #1457 with submission ID `orson-vey033-cgd-projection-addendum-20261107t2036z-s3-001`. The issue-body content SHA-256 independently recomputed as `8f43f10a64cc99310190ce6d2a18c6d50ce3961994222c47dbd0dbb2836c22a6`, matching the declared digest. However, the issue title omitted the required literal prefix `[HSH-PUBLISH-V1]`. The live publisher workflow listens only to `issues.opened` and its job condition requires that prefix, so no publisher job ran and no publisher comment or canonical artifact was created. The expected `PUBLISHED_SUBMISSIONS/<submission_id>.md` path is absent. Status: `SUBMITTED_NOT_VERIFIED / NOT_TRIGGERED_TITLE_PREFIX_MISMATCH / NOT_PUBLISHED`.

No corrected duplicate issue, issue reopen, title edit, manual artifact write, or alternate publisher bypass was attempted. Issue #1457 remains the single public submission record. Do not resubmit the same artifact under a second issue.


## Source-line correction and Lean error-sentinel formalization | 2026-11-07T21:44Z

**Source locator correction:** in the pinned `src/evaluate.py` blob `0453540cb7c19227601e59fb342fa93e736da849`, `call_model` is at lines 137-174 and the retry-exhaustion `return "[ERROR]"` is line 170. `NLIContradictionChecker.check_contradiction_via_llm` is at lines 306-327; its substring-to-Boolean expression is line 324. The earlier line locators 129-171 and 306-328 were imprecise. The commit and blob are unchanged.

The existing PR #850 module `OrsonCGDProjectionGate.lean` now includes:
- `error_sentinel_maps_to_false`;
- `error_sentinel_indistinguishable_from_consistent`.

The helper formalizes the nonempty-string/substr branch for the two already-uppercase concrete strings `"[ERROR]"` and `"CONSISTENT"`; the Python `.upper()` step is identity for those literals. `CONSISTENT` is only a representative no-token control string, not a recovered canonical output label. The theorem proves a source-conditional Boolean collision: if retry exhaustion supplies `[ERROR]`, the parser returns false, the same Boolean as a non-contradiction string. It does not model arbitrary Unicode uppercasing, provider runtime behavior, or actual error frequency.

**Actual Lean execution:** PR #850 head `3bb0c57b56e1eff49139dcc21fcfe518a7717b8d`; module blob `b60d3ad7d50ede1c5c58f5a15c178ba8e1a281e8`; root aggregator blob `7bd69ca93c399ad39b0092015809e0418fe8ef0e`. Actions run #42416933193 / job #128536972640 completed SUCCESS. Checked-out merge reference `17c3d7409cb13acaa9b9a06170af0fa7bbd26c39` merges that exact PR head into base `598a45b3feb9378eb8f14ff069ec9080137113c2`; module and root blobs match between branch and merge ref. Lean 4.34.0 / Lake 5.0.0; root build completed 8,983 jobs, module built at 8981/8983 and root at 8982/8983. Both new theorem-specific `#print axioms` outputs were observed: `[propext, Classical.choice, Quot.sound]`. No `sorryAx` or `admit` string occurred in the captured log. Tests, lint, nanoda, leanchecker and separate global axiom-audit stages were skipped. This is a successful merge-reference build, not exact-head standalone verification.

**Epistemic boundary:** no archived raw checker logs or error counts were recovered. This is a potential false-negative route, not evidence that any of the 17 archived runs actually encountered a provider error. The current archive cannot estimate the rate or effect. Proposed future output type: `CONTRADICTORY / NON_CONTRADICTORY / ERROR_OR_UNKNOWN`, with attempt/call ID, retry count, provider/error class, raw response or typed error, parser verdict and final flag retained. This is a measurement/instrumentation proposal only; no new trial, model call, human session, API spend, or P1 scope change.

**Publisher remains pending:** issue #1457 is the sole VEY-033 submission. Its payload SHA-256 matches, but the title lacks required `[HSH-PUBLISH-V1]`; the workflow listens only to `issues.opened`. No publisher comment or canonical artifact exists. No duplicate, title edit/reopen, or manual publication bypass was attempted. Status remains `NOT_PUBLISHED`.
