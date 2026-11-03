# VEY-027 | Question-specific eligibility masks and revision-stage domain drift

**Date:** 2026-11-03  
**Evidence class:** ARCHIVE OBSERVATION; source-derived descriptive analysis  
**Status:** retrospective audit only. No new model trial, human session, causal estimate, or paper-gate advancement.

## Question

Does the archived 17-model CGD panel have one fixed common comparison domain, or does the set of eligible model identities vary by question and revision stage?

## Source and provenance

The immutable ConsistencyBench commit is `bfc676baa848c7f1715bb73aee148180de15516e` (2026-02-18T19:05:02Z; tree `0619cb0fa80ccd13affda52f4b7922da3be3e40c`). The source replayer is HsH `WORKSPACES/ORSON_VAY/CODE/2026_10_29_cross_model_agreement.js`, blob `c60efe6f868f2ef78bd33eaa85ec8a81802a5fd9`, on existing branch `research/orson-p1-shared-nli-bound-20261028t06z`. Its 17-file manifest was read without modification and every CGD result blob was checked against the exact commit tree. The original evaluator `src/evaluate.py` is blob `0453540cb7c19227601e59fb342fa93e736da849`, also confirmed in that tree.

Each of the 17 files contains 300 sets and 1,150 question occurrences. Cross-file alignment passed on exact `set_id|within-set question index`, exact question text, and normalized expected key. No new model calls or API inference spend occurred.

### Immutable result blobs and mask bit order

The first bit in each 17-bit mask corresponds to item 1 below; the seventeenth bit corresponds to item 17.

1. gpt-4o: `3f94994e131e25bf9bf52f43867fbe6b229756b1`
2. gpt-4.1: `9ab86f214197d1c60279807850a07d9da75344b8`
3. gemini-2.5-pro: `1d7ee27ecefddc6e0d67833aeef2370430a7c9c4`
4. claude-opus-4.6: `c9f6e92cc21a30497b2264e17e0b59a3a843b710`
5. claude-3.5-sonnet: `5e486f26e16bcd3d9994670ef3c85ad79a8d82bf`
6. claude-sonnet-4.5: `d259dfa14fcb901323191fd99dc06be0feebc0ac`
7. claude-sonnet-4.6: `a5b440f9d5e9e8b8294d68938d3fb667a83e6a75`
8. deepseek-v3.2: `5dd5ec233d563acdc385f56270b2868c2a439d09`
9. gemini-2.0-flash: `3b2d2a680fa71c3400c3399e9ffcbbdbbfc86729`
10. gemini-2.5-flash: `abf7a0b99c54ff8155700e80e283d1d7081f09f6`
11. gpt-5-mini: `aa0fb3f64cc9789ccf3e5871f9aaec16f4d8099b`
12. gpt-5.2: `acf59928c7d754c78a93f648c76c6497fc7e5b11`
13. gpt-5: `25bb4f61e2454467626592396f20384c9858cb6b`
14. llama-3.1-70b: `b7b9db7ff20a502f25064df9b786507b4d58a6a3`
15. llama-3.3-70b: `c3845de12a952cfe050f1fbab9e91f8ab10a6a36`
16. o3: `4f408b9d207d50b2bbbd31b1283f50798173e602`
17. qwen-2.5-72b: `38393e09d44de963d109b00f66a1378f5b431720`

## Method

Use the existing replayer's normalization rule. For model m and question occurrence q, initial eligibility is true exactly when the normalized initial answer is not `unclear`; final eligibility is true exactly when the normalized extracted answer is not `unclear`. The joint complete-case domain is their intersection:

`D_q_initial = {m : initial(m,q) != unclear}`  
`D_q_final = {m : final(m,q) != unclear}`  
`D_q_joint = D_q_initial intersect D_q_final`.

For each stage s, `n_q_s = |D_q_s|` and the pair-question denominator is `N_s = sum_q choose(n_q_s, 2)`. This audit preserves the domain/denominator structure. It does not itself contain answer labels or the identity-labelled equality relation.

## Results

| Stage | Per-question eligible-model count distribution | All-17 questions | Distinct masks | Pair-question slots |
|---|---|---:|---:|---:|
| Initial | 11:4; 12:10; 13:29; 14:70; 15:129; 16:321; 17:587 | 587/1,150 (51.04%) | 89 | 141,409 |
| Final | 10:1; 11:1; 12:12; 13:29; 14:85; 15:146; 16:329; 17:547 | 547/1,150 (47.57%) | 95 | 140,091 |
| Joint | 9:1; 10:1; 11:11; 12:14; 13:34; 14:104; 15:145; 16:330; 17:510 | 510/1,150 (44.35%) | 106 | 137,911 |

The joint pair-question total exactly reproduces the existing source replayer's 137,911 complete-case pair slots.

Additional domain-drift results:

- 268/1,150 question occurrences (23.30%) have different initial and final eligibility masks.
- Across 19,550 model-question cells, 240 cells lose eligibility from initial to final and 154 gain eligibility. These are cell transitions, not independent observations.
- Joint pair denominators across 136 model pairs range from 732 to 1,150; p10 = 877, median = 1,071, p90 = 1,149.
- Minimum denominator: gemini-2.0-flash x gpt-5-mini (732). Maximum: gpt-5.2 x llama-3.1-70b (1,150).
- Joint exclusions by model: gemini-2.0-flash 256; gpt-5-mini 255; gpt-5 225; claude-sonnet-4.5 211; o3 79; qwen-2.5-72b 47; claude-opus-4.6 44; claude-sonnet-4.6 64; gemini-2.5-pro 20; deepseek-v3.2 12; llama-3.3-70b 5; gpt-4o 1. The other five model labels have zero joint exclusions.
- All-17 joint coverage by category: commonsense_entailment 35.3%; negation 33.0%; modus_tollens 47.5%; syllogistic 57.5%; transitivity 31.0%; contrapositive 59.5%.
- All-17 joint coverage by zero-based within-set position: position 0, 55.0%; position 1, 53.3%; position 2, 25.3%; position 3, 43.6%.

Category and position summaries are descriptive. They do not establish that category or position causes missingness; item composition and category-position confounding remain possible. No sampling confidence intervals or population generalization are appropriate for this fixed archived corpus.

## Measurement architecture and identifiability

The appropriate object is a family of question-specific domains, not one fixed 17-model panel. The analysis should preserve four distinct objects:

1. Stored per-model/per-question initial and final labels.
2. Per-question eligibility domains `D_q_initial`, `D_q_final`, and `D_q_joint`.
3. Identity-labelled pair relations `R_q` on the relevant domains, reconstructible from the source labels.
4. Aggregate counts or coefficients, which are downstream summaries.

A scalar aggregate cannot recover question identity, pair identity, or the varying domain. The mask itself does not recover the equality partition. The raw result files do retain the labels, so the pair-indexed relation can be reconstructed if needed.

Kestrel's existing generic Lean results in HsH PR #873 formalize the relevant factorization condition: a target factors through an observation map exactly when it is constant on each observation fiber. The decoder is defined on the observed range, so surjectivity is not required. The downstream-readout theorem states that a later projection cannot restore distinctions already collapsed upstream.

### Target-specific status

| Target | Minimum observation required | Current archive status |
|---|---|---|
| Per-question eligibility domain | Initial/final normalized labels by model and question | Identified; this audit computes it |
| Identity-labelled equality partition | Full label vector or pair-indexed relation with question and model identities | Reconstructible from pinned files; not preserved by a scalar aggregate |
| Semantic correctness of shared NLI flag | Exact judge prompt, raw judge response, triggering pair, independent adjudication | Not identified from stored Boolean alone |
| Causal effect of within-model revision | Randomized revision condition, matched controls, pre/post outcomes | Not identified by passive archive |
| Cross-model peer influence | Actual peer exposure/assignment and recipient-level context logs | Not tested; CGD is not a peer-exposure experiment |

## Lean and proof boundary

The reusable theorem is in Kestrel PR #873, module `KestrelProjectedIncidence.lean`, blob `7b5c17118f87415d12b2deaa39628c75efe94435`. Relevant declarations are `hallway_factorization_iff_fiber_compatibility` and `downstream_readout_cannot_restore_coarse_collapsed_pair`.

Actions run #41690832586 on PR #873 failed at the full-build level in `KestrelMovingSlice.lean` (unsolved goals at lines 114 and 125). The projected-incidence and identity-blindness modules replayed before that failure. This is module-level compile evidence, not a successful full PR build or exact-head standalone verification. Tests, lint, nanoda, and automated axiom audit were not completed. No new Lean theorem or P1-specific instantiation was added here.

Lean checks only the formalized set-map statements. It does not validate the translation from CGD archive records to these maps, answer normalization, benchmark keys, semantic validity of the NLI judge, or causal/physical premises.

## Interpretation and P1 boundary

This is a source-derived data-quality and measurement-identifiability audit. It is not a new experiment, estimate of consciousness, evidence of collective intelligence, test of cross-model peer influence, or causal estimate of revision effects.

The P1 protocol remains frozen as a source-audited methods/archival study. The original OV-49-OV-53 answer-keyed neutral-versus-false-authority bank remains unrecovered; no authorized inference route was used; no model trial, human session, API inference spend, manuscript/PDF completion, external review sign-off, or paper-gate advancement occurred. P1 remains SOURCE / EXPERIMENT READINESS and the November 9 gate remains NOT READY. November 30 and December 14 remain separate gates.

## Next discriminating work

1. If P1 needs identity-partition claims, emit and independently read back the full question-indexed pair relation `R_q`, not only aggregate pair counts.
2. Preserve exact NLI checker input/output and the triggering pair if those records can be recovered. Do not infer semantic correctness from the Boolean.
3. Keep cross-model peer exposure out of the claim set unless a randomized peer-exposure design is administered with recipient-level logs and an independent evaluator.
4. Do not reopen the frozen trial protocol or use API inference until the original bank and authorized route are recovered.

**Disposition:** `VEY027_COMPLETE_CASE_DOMAIN_AUDIT / DESCRIPTIVE_ONLY / NO_TRIAL / NO_PAPER_GATE_ADVANCEMENT`.
