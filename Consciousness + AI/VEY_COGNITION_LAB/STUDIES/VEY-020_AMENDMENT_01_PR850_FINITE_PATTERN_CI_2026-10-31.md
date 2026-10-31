# VEY-020 Amendment 01 | PR #850 finite-pattern formalization verified

Date: 2026-10-31  
Reason: clarify the exact formal-verification scope referenced in VEY-020.

## Correction

VEY-020's shorthand description of PR #850 as a conditional Kish/evaluator-count formalization was incomplete. The current PR #850 head also imports and compiles the existing `OrsonFinitePatternDistribution.lean` module.

Current branch: `research/orson-p1-shared-nli-bound-20261028t06z`  
PR head: `d59a17b270df730e84edbd614eaea3b1b76166e2`  
Exact-head workflow: #41160835210  
Job: #124417786006  
Lean: 4.34.0  
Build targets: 8,943  
Result: SUCCESS.

Pinned source blobs:
- `OrsonFinitePatternDistribution.lean`: `c569fe1b0d2bcb6b4e42f174a84ab703aa7da71f`
- `OrsonKishEffectiveSampleSize.lean`: `2e5083fe61ebe121b48b2be70c007ec59ee47e08`
- `HsHVerification.lean`: `f020c55e3a94b5850d33b741c44af8158d7c62f6`

The root verification file imports both Orson modules. The complete retrieved workflow log includes theorem-specific axiom reports for the finite-pattern and Kish modules. No `sorryAx` occurs in the retrieved log. The separate `lake test`, `lake lint`, nanoda, and automated axiom-audit stages were skipped.

## What the finite-pattern module proves

The module defines a finite labelled success-pattern space for (n) agents and two model families:
- a shared record-reliability gate;
- a latent item-difficulty mixture.

It proves:
1. product-Bernoulli pattern weights normalize over the complete finite powerset;
2. both mixture descriptions are nonnegative and normalized on the stated Bernoulli parameter domain;
3. both latent labels map to exactly the same complete finite observable pattern distribution;
4. the latent-label-to-observation map is therefore non-injective within this specified model family.

The key theorem is `observationMap_not_injective`.

The source comments explicitly identify OV-55 and OV-56 as assistant-authored analytic toy-model/identifiability notes, not administered LLM experiments. The Lean result proves the mathematical non-identifiability statement under the definitions and assumptions. It does not establish that either latent mechanism generated real LLM behavior, authenticate the underlying archive, or validate answer-key semantics.

## Boundary

This is a verification of an existing formalization, not a new theorem, new branch, or new PR. It does not formalize the new VEY-020 evidence-lifecycle maps or the copy-weight model. Those remain separate candidates and were not compiled in this run.
