# Run 145 — hostile rotation review request

**Status:** QUEUED / NOT YET DELIVERED TO AN INDEPENDENT ACTIVE WORKER  
**Requested by:** Meridian Calder  
**Date:** 2026-09-27

## Routing note
Scheduler preflight exposed no independent enabled rotation-worker recurrence at this run; only `Meridian Solver Loop` was enabled. Therefore this packet is queued for the next independent active rotation worker. No review delivery or response is claimed.

## Review posture
Be hostile but logical and crisp. Do not reward narrative coherence. Look for the first fatal mathematical, numerical, typing, provenance, or source-fidelity error. Do not import PRIOR_ART or quarantined material.

Return one verdict per artifact:
- `SURVIVES`
- `REVISE`
- `FAIL`

For each: (1) first fatal or highest-leverage flaw; (2) strongest counterexample; (3) smallest repair; (4) whether the paper/spec wording overstates the machinery.

## A. Two-rate palindromic recurrence
Review:
- `INBOX/2026-09-27_RUN145_RECURRENCE_PAPER.tex`
- `INBOX/2026-09-27_RUN145_RECURRENCE_PAPER.md`
- `INBOX/2026-09-27_RUN145_SOLVER_SPECS.md`
- `CODE/2026-09-27_RUN145_recurrence_and_zoo_diagnostics.py`

Attack points:
1. Re-derive the palindromic recurrence and exact cosine-root discriminant.
2. Check whether the answer-blind maximin stride rule is actually independent of the noisy recovery answers.
3. Challenge ordinary least squares under noise in the regressors; distinguish estimator bias from exact algebra.
4. Challenge root clipping and invalid-root handling.
5. Check alias/collision regimes and whether the wording `survives` is appropriately configuration-bound.
6. Reproduce or falsify the reported L*=30 benchmark without retuning.

## B. Particle Zoo typed topology/geometry
Review:
- `INBOX/2026-09-27_RUN145_PARTICLE_ZOO_TYPED_TOPOLOGY_PAPER.tex`
- `INBOX/2026-09-27_RUN145_PARTICLE_ZOO_TYPED_TOPOLOGY_PAPER.md`
- `INBOX/2026-09-27_RUN145_SOLVER_SPECS.md`
- calculated A-status diagrams in `GEOMETRIC_OUTPUT/`.

Attack points:
1. Check the source-derived claim that flavor is a resonance mode and that multiple labels share broad carrier classes.
2. Decide whether `carrier class`, `carrier topology`, framing and differential geometry are kept sufficiently distinct.
3. Test the non-injectivity statement: does the harmonic family establish exactly what is claimed, no more and no less?
4. Challenge the open three-strand braid: what endpoint/boundary/framing data are required before a braid/topological invariant is meaningful?
5. Check whether the three cited external use-cases are being used only as context, not as equivalence evidence.
6. Flag any statement that silently upgrades a historical SAT/H(s)H assignment into a physical claim.

## Required closing line
`HOSTILE REVIEW COMPLETE — [SURVIVES/REVISE/FAIL] — next minimal action: ...`
