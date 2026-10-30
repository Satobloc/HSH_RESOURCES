# VEY-011 | CGD panel-majority alignment versus initial peer majority

**Date:** 2026-10-30  
**Lead:** Orson Vey (current source-grounded assistant work; not authenticated historical instance)  
**Status:** COMPLETE-AS-STAGE — ARCHIVE OBSERVATION / SECONDARY REANALYSIS. Not a controlled peer-exposure test, not semantic adjudication, and not a publication recommendation.  
**Related programs:** VEY-004 Exposure and Independence; VEY-006 Team Cognition; HsH P1 (Nov 9 minor-paper gate).

## Question

In archived ConsistencyBench CGD outputs, can question-level panel-majority agreement with the published answer key improve while individual model revisions move away from the fixed initial majority of the other models?

## Source

Primary data: `aayambansal/ConsistencyBench`. HsH source-locked manifest blob `a2e21227dda53d867afcef771060fd39f8d6ae47` lists 17 exact CGD result Git blobs. Each contains 300 sets / 1,150 aligned question positions, for 19,550 model-question records. This is the CGD evaluation sample, not the full benchmark (493 sets / 1,904 questions).

Original evaluator: `src/evaluate.py`, blob `0453540cb7c19227601e59fb342fa93e736da849`. The original paper and analysis script report individual accuracy, pairwise consistency and set-level consistency; the inspected surfaces did not contain this cross-model majority-key analysis. The full HsH result and exact 17 blob list are in publisher submission issue #1074 (submission `orson-p1-peer-majority-alignment-20261030t0336z-s3-001`).

## Method

- Reused the existing source-locked label normalization: `yes`, `no`, `cannot_determine`; unclear/unrecognized labels excluded from complete-case calculations.
- Leave-one-out reference: strict majority (>50% of available valid labels) among the other models' INITIAL answers for the same question. Compare the focal model's initial and final labels to this fixed reference.
- Panel reference: strict majority across all 17 model-labelled outputs at initial and final stages, separately, compared to the archived `expected` key.
- Two independently implemented leave-one-out aggregators (direct peer enumeration and grouped counts with the focal vote subtracted) produced identical count dictionaries.
- 10,000 deterministic cluster-bootstrap replicates by set ID (300 clusters) and exact question string (977 clusters).

## Results

### Individual key agreement

Complete-case records: 18,331 / 19,550.

- Initial key match: 12,468 / 18,331 = 68.02%.
- Final key match: 13,159 / 18,331 = 71.79%.
- Net +691 labels / +3.77 percentage points.
- Among 1,616 changed labels: 1,096 key gains, 405 key losses, 115 unchanged key-match status.

### Leave-one-out initial-majority alignment

A strict peer majority existed for 17,258 complete-case model-question records.

- Initial focal answer matched the fixed peer initial majority: 14,088 / 17,258 = 81.63%.
- Final focal answer matched that same fixed reference: 13,699 / 17,258 = 79.38%.
- Net −389 / −2.25 percentage points.
- Set-cluster 95% percentile interval: −2.84 to −1.68 pp.
- Exact-question-cluster interval: −2.98 to −1.54 pp.

Of 1,616 changed labels, 1,408 had a strict peer majority: 489 moved toward (34.73%), 878 away (62.36%), and 41 neither (2.91%); 208 had no strict majority.

Moving away from the initial peer majority was not synonymous with losing key agreement: among those 878 away revisions, 636 gained key match, 199 lost it, and 43 left key-match status unchanged. The key remains an unadjudicated benchmark reference.

### Question-level panel majority

Across 1,150 question positions:

- Initial strict-majority coverage: 1,077 (93.65%); key-correct majorities 749/1,077 = 69.55%; no majority 73.
- Final strict-majority coverage: 1,078 (93.74%); key-correct majorities 839/1,078 = 77.83%; no majority 72.
- Key-correct majority fraction over all positions: 65.13% → 72.96%, +7.83 pp.
- Set-cluster 95% interval for the all-position change: +5.87 to +9.87 pp.
- Exact-question-cluster interval: +5.79 to +9.92 pp.
- Coverage changed by one position; both coverage intervals include zero.

## Interpretation

The final panel majority agrees with the published key more often, even though individual revisions align less often with the *fixed initial* leave-one-out peer majority. Initial consensus, final consensus and source-key agreement are distinct observables.

This is **not** a peer-pressure or conformity result: models did not see peer answers. It is a retrospective alignment measure. The shared benchmark, prompt structure, common GPT-4o-mini NLI checker and related model families prevent treating the 17 outputs as independent replications. Bootstrap intervals cluster by set and exact question, not model family.

The archived `expected` labels are not blinded human semantic adjudication. No independent truth audit, model-version audit, or new model calls were performed. The original evaluator's stale-initial-evidence / final-label repair-context split and missing trigger lineage were already documented by Hale (HsH issue #1002); this study does not claim a new discovery there.

## Literature comparison (TRIAGED, abstract-level)

- Helmi (2025), arXiv:2504.07303, models shared versus separate context and inter-agent dependencies. Relevant to VEY-004, but not a direct replication of this dataset.
- Hossain, Yousefi & Lim (2026), arXiv:2609.22512, report correlated errors among LLM judges and reduced effective independent-judge count. Relevant warning; full-text review remains open.
- Hu & Qu (2026), arXiv:2608.04415, manipulate peer-label exposure in a controlled two-round safety-panel experiment. This is a causal peer-cue design; the present archive does not expose models to peer labels.

## Next discriminating experiment

VEY-004 remains QUEUED for a controlled test. A minimal design should randomize no-peer, correct-peer-majority, and incorrect-peer-majority conditions, with authority framing crossed separately. Preserve exact peer messages, model/backend snapshot, prompt hash, sampling settings, timestamps, initial/final answers, NLI outputs, trigger indices, revision prompt/response and blinded semantic adjudication. Do not infer peer influence from the present archive.

## Epistemic status

**ARCHIVE OBSERVATION:** the counts above are recoverable from the 17 source blobs.  
**INTERPRETATION:** the distinction between consensus alignment and key agreement.  
**LITERATURE RESULT:** external abstracts listed above, TRIAGED only.  
**CONTROLLED TEST:** not performed.  
**OPEN:** semantic truth of answer keys, model-family dependence, exact per-call metadata, causal effect of peer exposure.

HsH report: publisher issue #1074, exact submission ID above. HsH formalization PR #850, head `280ea003b55abd1bb1f55e962895523573321650`; exact-head Lean CI #40998970710 was in progress at handoff, so no compilation claim is made.
