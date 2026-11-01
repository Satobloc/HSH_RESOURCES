# VEY-024 | NLI alignment as graph closure

**Date:** 2026-11-01  
**Type:** source-fidelity / cognition-instrument audit, not an experiment

## Scope

Additive code-level extension to the earlier Pauper Consensus paper audit (HsH #580) and position/ablation audit (#609). This note does not repeat their headline findings. It focuses on the first-pass align_free implementation in mainlobelabs/pauper-consensus commit c328dab5ca1f1101b5ec56e2e92e3592898ceadf.

Primary code objects:
- firstpass/wct/cluster.py, blob 45ad33fff02bb065cfdd2f1a1d2cd70f073da1f3
- firstpass/wct/measure.py, blob c01616393bcc1a377a0ad7ededf63df3de6ee426
- src/wave_consensus/votes.py, blob 45cacccc7a64c12036013c18f7765254926999e4
- firstpass/wct/aggregate.py, blob d9d1aca0cf6a7edbeac336e37aa39e757718a701
- Manuscript paper/final.md, blob 05a9d8b7ad00ad9b59fa4b1a17691040e1d99ca6
- Frozen registration prereg-v2.yaml, blob 631b9ef69e79ae124140c472715f8bf36df75873

## Main geometry finding

The free-alignment path forms a symmetric direct-link relation from bidirectional NLI scores:
Rτ(i,j) iff min(p(i⇒j), p(j⇒i)) ≥ τ.
It then uses union-find to merge connected vertices. The result is the equivalence/connected-component closure of the direct-link relation, followed by a quotient projection from claim vertices to component IDs.

Therefore:
Rτ(a,b) ∧ Rτ(b,c) ∧ ¬Rτ(a,c) ⇒ π(a)=π(c) ∧ ¬Rτ(a,c).

Same cluster does not mean direct pairwise entailment or mutual entailment. The code counts transitivity violations, which preserves this distinction. The Lean abstraction is a three-node path: 0—1—2, with no direct 0—2 edge, but 0 and 2 in the same component quotient.

**Scope limit:** align_free is described as a path for datasets without canonical proposition sets. The registered Study 1 description uses canonical propositions and the anchored path; Study 2 uses structured proposition IDs. This theorem is about the available free-clustering code path, not the registered headline result.

## Measurement versus evidence

The source measure.py explicitly treats embedding/NLI pairwise scores as measurement/alignment, not independent confirmations. The later vote matrix is the evidence representation. WCT-EM aggregation and per-arm calibration are further distinct maps. The full chain is:
raw traces → claim extraction → alignment → source×proposition vote states → latent-truth aggregation → calibration → decision.

The P1 ConsistencyBench NLI judge is therefore a shared measurement dependency, not another independent model witness and not evidence of peer persuasion. Keep source ancestry, shared evaluator, alignment error, and aggregation/calibration error separate.

The vote implementation preserves AFFIRM=+1, DENY=-1, and MISSING=0; silence is not denial. The one-vote-per-source/proposition cap is a within-source deduplication rule, not a guarantee of cross-source independence. The earlier Hale audit already covers the paper's correction history and effective-vote result; this note does not repeat those calculations.

## Lean status

The PR #850 branch contains FORMAL_VERIFICATION/HsHVerification/OrsonNLIClusterClosure.lean, blob 6e720ecbc8e1f4b36fcb1d3a86c0e12873777bff, at commit 046384a99b982d4c2911da952d9253449e8f0c77. It defines the generated equivalence closure, a Setoid quotient projection, and the three-node non-direct-link example.

The root aggregator blob 8d9817accf811d002f3e43ce0fdcce18613eeec2 does not import this module. Actions run #41275574389 completed successfully (8,975 jobs, Lean 4.34.0 / Lake 5.0.0, zero errors and zero sorryAx in the retrieved log), but the log has no OrsonNLIClusterClosure entry. Thus the successful build does not verify this file. Local lean/lake are absent. No alternate write route was used after the branch-update safety block.

## P1 disposition

Issue #564 remains SOURCE / EXPERIMENT READINESS. OV-49–OV-53 answer-keyed bank remains unrecovered; authorized inference endpoint unavailable; no new trials. No paper gate advanced. No BEDROCK edit, theory promotion, physical calculation, CODATA scoring, or SAT-O/Blockwave change.

## Next cursor

1. Review the unimported Lean module and integrate it only through an authorized route.
2. Verify whether align_free appears in any registered analysis before attributing results to it.
3. Preserve the distinct align_free, align_anchored, vote, aggregation, calibration, and decision maps.
4. Keep P1's source-bank and authorized-endpoint gates open.
