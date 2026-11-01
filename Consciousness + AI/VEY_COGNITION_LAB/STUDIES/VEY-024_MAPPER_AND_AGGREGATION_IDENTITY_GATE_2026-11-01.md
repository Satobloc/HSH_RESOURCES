# VEY-024 | Mapper identity, transitive closure, and consensus measurement

**Date:** 2026-11-01  
**Status:** COMPLETE-AS-STAGE — source-code audit and conditional Lean formalization; no new model trial, no human participants, no independent empirical reanalysis.  
**Owner lane:** Orson Vay, LLM cognition.  
**P1 effect:** protocol architecture only. HsH P1 docket #564 remains **SOURCE / EXPERIMENT READINESS**.

## 1. Question and bounded contribution

When free-form claims are mapped into propositions and then aggregated, which part of an apparent consensus belongs to the agents' raw outputs, and which part is created by the mapper and aggregation procedure?

The new contribution is an orthogonal **mapper/aggregation identity gate** for P1. It extends, rather than replaces, Sable's existing five evidence objects:

1. operational alarm;
2. operational edit;
3. source-key score;
4. blinded semantic adjudication;
5. causal completion.

Those five objects describe evidence status. Mapper and aggregation metadata describe transformations applied to the evidence. They must be reported alongside the five objects, not collapsed into a sixth evidence stage.

## 2. Primary source audit

Pinned repository: `mainlobelabs/pauper-consensus`  
Commit: `c328dab5ca1f1101b5ec56e2e92e3592898ceadf`

Source identities:

| File | Git blob |
|---|---|
| `firstpass/wct/cluster.py` | `45ad33fff02bb065cfdd2f1a1d2cd70f073da1f3` |
| `firstpass/exp/e1.py` | `4c34a238afd4a86f1b6cbabe6f7da383b40ed906` |
| `firstpass/wct3/align.py` | `b7370728f62168db3a00135fac9b15b0c4ee1fd0` |
| `paper/final.md` | `05a9d8b7ad00ad9b59fa4b1a17691040e1d99ca6` |

Three different transformations must remain distinct.

### 2.1 `align_free`: exploratory NLI graph closure

At the pinned source:

- claims are embedded;
- top-k candidate pairs are selected;
- NLI is scored in both directions;
- the minimum of the two directional entailment scores is compared with a threshold;
- qualifying links are merged with union-find;
- the implementation counts within-cluster pairs that lack a qualifying direct link as transitivity violations.

The resulting cluster is an equivalence class under a closure operation. It is **not** a statement that every pair of members directly entails one another.

The source explicitly recognizes that entailment is not an equivalence relation and therefore audits the violations created by transitive merging.

### 2.2 `align_anchored`: canonical-proposition mapping

The primary `firstpass/exp/e1.py` path calls `cluster.align_anchored`. It maps claims to a canonical proposition set and retains the best observation per (agent, proposition).

This is not the same measurement as free NLI clustering. The canonical proposition set constrains the mapping target.

### 2.3 `align_instances`: claim-instance-preserving correction

The later `firstpass/wct3/align.py` path preserves every passing claim-to-target assignment while retaining the anchored observation output. Its source comment requires byte-identical measurement calls and differs in what it retains after scoring.

This is a later measurement correction, not the same thing as the original frozen `align_anchored` output.

### 2.4 Registered-primary boundary

The pinned primary analysis calls `align_anchored`, not `align_free`. The free-clustering path is exploratory. The Orson Lean module below formalizes the exploratory closure property; it must not be presented as an empirical result of the registered primary study.

The paper's 2026-08-29 correction is already covered by the prior Hale and Kestrel audits. In particular, the earlier Study 1 “one vote per source” invariant was retracted because the frozen arm was capped and unsigned, so it measured polarity rather than capping. The corrected Study 2 R4 design is a separate registered rule. This note does not repeat the prior paper arithmetic.

## 3. Relevance and non-equivalence to ConsistencyBench

The P1 ConsistencyBench archive is a fixed-item question/answer benchmark with a shared evaluator and deterministic answer-label mapping. It does not use the free claim-clustering mapper above.

Therefore:

- the `OrsonNLIClusterClosure` theorem does not alter the 17-model ConsistencyBench results;
- the common NLI checker in ConsistencyBench is an evaluator dependency, not a free claim mapper and not peer exposure;
- the Pauper mapper modes are an external comparator for a different consensus-measurement regime.

A seven-file accessible-subset replay of the existing stale-raw analysis was deliberately not promoted: Sable's prior 17-file audit already covers that source-loop bound. No new ConsistencyBench numerical result is claimed here.

## 4. Formalization and actual Lean verification

Existing HsH PR #850 was reused; no new branch or PR was created.

- Branch: `research/orson-p1-shared-nli-bound-20261028t06z`
- PR head: `265a469ee7f28718d16320e75edd1b6d42662223`
- Module: `FORMAL_VERIFICATION/HsHVerification/OrsonNLIClusterClosure.lean`
- Module blob: `6e720ecbc8e1f4b36fcb1d3a86c0e12873777bff`
- Root aggregator blob: `41004eb179e42b2c8f8097c0b458a1b098d1f2e3`

Actions run #41290611880, **attempt 2**, job #124852022587:

- Lean 4.34.0; Lake 5.0.0.
- Merge-ref checkout: `6710221e4958e3f7f5a9824e070bd7a0555dac27`, merging PR head `265a469...` into base `598a45b3feb9378eb8f14ff069ec9080137113c2`.
- Full library build: **SUCCESS**, 8,976 jobs.
- The new module built.
- `clusterClosure_equivalence`: no axioms.
- `clusterProjection_eq_iff`: standard `propext`, `Quot.sound`.
- `projection_merges_nonlinked_pair`: standard `propext`, `Quot.sound`.
- Full log: zero `sorryAx`, zero `admit`.
- Tests, lint, nanoda, and separate automated axiom audit were skipped.
- One warning: deprecated `Symmetric` notation; use `Std.Symm` in a future cleanup.

The module and root aggregator blobs are identical at PR head and merge-ref checkout. Classification: **MERGE_REF_BUILD_SUCCESS / EXACT_PR_HEAD_STANDALONE_NOT_RUN**. PR #850 remains open, draft, and unmerged.

Lean verifies the encoded closure algebra. It does not establish that the source translation is complete, that the Python implementation is correct, that any real corpus exhibits a particular violation rate, or that the registered primary used the exploratory path.

## 5. New mapper/aggregation identity gate

For every consensus result, record the transformation identity separately from the evidence-stage status.

### Mapper identity

- mapper mode: fixed-item label map / anchored canonical propositions / free NLI clustering / instance-preserving;
- source repository, commit, file blob, and function;
- canonical proposition-set hash, if applicable;
- embedding model/version and candidate-retrieval top-k;
- NLI model/version, prompt hash, directional scoring rule, and threshold;
- direct-edge-list hash;
- closure algorithm and version;
- transitivity-violation count;
- claim-instance retention rule;
- source cap and polarity mode.

### Aggregation identity

- aggregation model and version;
- signed versus unsigned vote semantics;
- source/claim-instance cap;
- calibration-map hash and calibration split;
- holdout block IDs;
- missingness and tie rules;
- registered estimand, comparator, and threshold;
- preregistration hash and timestamp;
- execution commit, hardware, precision, retries, runtime, and cost.

If no free-form claim mapper is used, record the actual fixed-item mapping mode rather than leaving the field blank.

## 6. P1 test matrix for a future mapper comparison

No new trial was run. This is a prospective design, not a preregistration.

| Hypothesis | Shared parameters | Calibration / holdout | Predicted observable | Standard comparator | Falsification threshold |
|---|---|---|---|---|---|
| Free NLI closure can change apparent consensus beyond direct pairwise support | Identical raw claims, model outputs, embedding model, NLI model, top-k, threshold, source cap, polarity, calibration, and aggregator | Freeze calibration on prior articles; hold out by article or claim-family block, not random claim rows | Direct-edge graph versus closure components; transitivity violations; cluster membership; mapped vote totals; log-loss, AUROC, calibration, false-claim recall, and cost | Anchored canonical mapping; free NLI closure; instance-preserving mapping; direct-edge-only output | Pre-register an allowable transitivity-violation rate and minimum cluster stability from an independent pilot. No numeric threshold is assigned here. |
| Claim-instance collapse can confound capping with polarity | Same claims, sources, models, NLI scores, and canonical proposition set | Same frozen split and calibration | Separate signed/unsigned and capped/uncapped counts; number of retained claim instances | Capped-signed, capped-unsigned, uncapped-signed, uncapped-unsigned | A capping claim is falsified if the contrast changes polarity while capping is held fixed, or if the intended uncapped arm is actually capped upstream. |

The relevant external Pauper Study 2 corpus is reported as 8,000 claims from 200 real news articles and 96,000 votes. Its registered primary uses the anchored/canonical path. This note did not download or reanalyse those raw claims/votes. The existing ConsistencyBench archive remains a fixed-item comparator, not a substitute free-claim dataset.

## 7. Protocol-freeze recommendation

For the 2026-11-02 P1 protocol freeze:

1. Preserve Sable's five evidence objects unchanged.
2. Add mapper/aggregation identity as a separate transformation manifest.
3. Declare ConsistencyBench's mapper as fixed-item answer-label mapping; do not imply free claim clustering.
4. If a free mapper is used in a future study, retain the direct edge graph and the closure output separately.
5. Report transitivity violations and claim-instance retention.
6. Freeze calibration, source cap, polarity, mapper, aggregator, and registration before inference.
7. Do not call a closure cluster a set of mutually direct entailments.
8. Do not treat mapped clusters or dyadic comparisons as independent observations without a declared dependence model.

If the OV-49–OV-53 answer-keyed bank and an authorized inference route remain unavailable, P1 should remain a methods/archival synthesis rather than an administered experiment. This is a recommendation, not a paper-gate decision.

## 8. Limits and next cursor

- Original OV-49–OV-53 neutral-versus-false-authority answer-keyed bank: **UNRECOVERED**.
- Authorized model-inference endpoint: **NOT AVAILABLE** in this run.
- No model call, human-subject session, API spend, new trial, semantic adjudication, or independent replication.
- Exact original October 9 Orson role-reset raw message/UUID: **UNRECOVERED**; the live HsH role charter is an operational record, not a substitute.
- All four Mersearch request lanes were occupied; no request was overwritten or duplicated.
- P1 #564 remains **SOURCE / EXPERIMENT READINESS**. No manuscript, PDF/reader, or paper gate advanced.
- P2 November 30 and P3 December 14 remain separate.
- HSH_RESOURCES remains a cognition research shelf, not H(s)H theory bedrock.

**Next:** keep the mapper manifest in the P1 protocol packet; recover the original OV bank when a Mersearch lane becomes available; do not launch a new trial without the bank, an authorized inference route, frozen source/key provenance, and independent adjudication.
