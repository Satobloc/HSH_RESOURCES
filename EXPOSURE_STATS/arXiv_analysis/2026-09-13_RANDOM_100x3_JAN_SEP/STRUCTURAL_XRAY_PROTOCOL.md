# Structural SATity X-ray — blinded abstract protocol

## Purpose

This pass is deliberately **not** a vocabulary, branding, or numerical-nearness test. The target is the deeper fingerprint Nathan specified: **structure, philosophy, foundations, and explanatory architecture**.

The source corpus is the fixed-seed random arXiv sample in this directory: 100 physics abstracts from Jan–Sep of each of 2024, 2025, and 2026.

## Blind design

1. Pool all 300 papers.
2. Replace year/arXiv identity with opaque IDs (`XR001` … `XR300`).
3. Shuffle with a separately recorded deterministic seed.
4. Score **title + abstract only** in the first pass. Do not expose year, arXiv ID, authors, dates, or categories to the scorer.
5. Preserve a private key from blind ID to original record.
6. Reveal years only after all first-pass scores are frozen.
7. Aggregate by year after unblinding.

This prevents the scorer from unconsciously rating a paper as more SAT-like merely because it is known to be newer.

## What counts

A feature receives `Y` only when the title/abstract gives affirmative structural evidence. Otherwise it receives `N` in the mechanical first pass. Absence from an abstract is therefore **not** a claim that the full paper rejects or lacks the feature. This experiment measures the *visible conceptual surface of a random abstract corpus*.

## Structural/foundational dimensions

The dimensions below are distilled from the SAT/H(s)H fingerprint checklist, especially its high-level compound, epistemic, anti-fitting, measurement/readout, quantization, worldtube, and relation-to-established-physics sections. SAT-specific proper nouns, historical accidents, project administration, and numerical constants are excluded.

### History / readout architecture

- **X01 COMPLETE_HISTORY** — complete histories/worldlines/worldtubes are treated as explanatory objects, not mere bookkeeping.
- **X02 LOCAL_AS_READOUT** — an observed/local object or state is explicitly a projection, section, intersection, boundary readout, coarse-graining, or reduced description of a larger structure.
- **X03 CARRIER_READOUT_SEPARATION** — underlying carrier/state and measurement/observer/readout map are explicitly distinguished.
- **X04 FINITE_EXTENT** — finite-core, extended-object, worldtube, boundary, support, or non-pointlike structure is load-bearing.
- **X05 MEASUREMENT_GEOMETRY** — measurement/resolution/kernel/observer geometry materially affects what is inferred.

### Geometry / topology as explanation

- **X06 GEOMETRY_FIRST** — geometry/topology is used as an explanatory mechanism rather than merely a calculational background.
- **X07 MORPHOLOGY_IDENTITY** — identity/state/species/phase is encoded by morphology, topology, orientation, twist, winding, chirality, braid, defect, etc.
- **X08 HOLONOMY_PHASE** — holonomy/geometric phase/closed-loop transport is structurally important.
- **X09 BRAID_KNOT_LINK** — braids, knots, links, anyons, string-nets, or equivalent topological organization are load-bearing.
- **X10 CHIRALITY_ORIENTATION** — handedness/orientation/parity is used as a physical differentiator.
- **X11 RECURSIVE_NESTED** — recursive, hierarchical, nested, multiscale repetition of a common structural grammar is explicit.
- **X12 BIFURCATION_TRANSITION** — discrete physical behavior is explained through bifurcation, topology change, branch change, singular transition, or structural instability.

### Emergence / unification

- **X13 EMERGENT_QUANTIZATION** — discreteness/quantization emerges from continuous geometry, topology, constraints, dynamics, or collective behavior rather than being assumed primitive.
- **X14 EMERGENT_SPACETIME_CAUSALITY** — spacetime, metric, signature, causal structure, or dimensionality is emergent/induced/effective.
- **X15 EMERGENT_PARTICLE_PROPERTIES** — particle-like properties or effective degrees of freedom emerge from deeper collective/geometric/topological structure.
- **X16 VACUUM_MATTER_CONTINUUM** — vacuum/background/medium and matter/excitations are treated as regimes or states of one structural system.
- **X17 FORCE_REGIME_UNIFICATION** — conventionally distinct interactions are presented as regimes/projections/limits of a common mechanism.
- **X18 CROSS_SECTOR_GRAMMAR** — the same structural mechanism is explicitly used across conventionally separate physical sectors or scales.

### Dynamics and representation

- **X19 FULL_VS_EFFECTIVE** — full/fundamental description is explicitly distinguished from an effective/reduced/emergent one.
- **X20 REPRESENTATION_NOT_ONTOLOGY** — the work explicitly distinguishes model/representation from literal ontology, or stresses empirical equivalence/underdetermination.
- **X21 UNIVERSALITY_VS_DYNAMICS** — distinguishes ability to represent/fits states from a stronger claim that dynamics select the observed states.
- **X22 STANDARD_LIMIT_RECOVERY** — a novel framework explicitly requires recovery of an established theory/limit rather than replacing successful physics wholesale.

### Constraint / falsification / anti-fitting philosophy

- **X23 FAIL_RIGID** — the construction is tightly constrained, parameter-poor, overdetermined, or emphasizes non-adjustability/falsifiability.
- **X24 ANTI_TUNING** — explicitly rejects or penalizes ad hoc fitting/free parameters/corrections introduced solely for agreement.
- **X25 NULL_NEGATIVE_RESULTS** — null results, exclusions, failed mechanisms, no-go results, or ruled-out parameter regions are treated as substantive outputs.
- **X26 PREDICTIVE_CROSSCHECK** — emphasizes independent/cross-sector prediction, consistency checks, or constraints not used in calibration.
- **X27 PROVENANCE_PRIOR_ART** — explicitly distinguishes derivation/source/prior-art/dependency or carefully maps relation to earlier frameworks.
- **X28 FORMALISM_NOT_TRUTH** — mathematical consistency/formal proof/computation is explicitly treated as insufficient by itself for physical truth.

### Established-physics stance

- **X29 TRANSLATE_NOT_REJECT** — established successful physics is retained/recovered/reinterpreted rather than broadly discarded.
- **X30 MODULAR_STANDARD_MATH** — standard mathematical machinery from multiple domains is deliberately combined/adapted as a toolbox rather than replaced with private formalism.

## Primary outputs

For every blind paper:

`blind_id, X01 ... X30, total_Y`

After unblinding:

- prevalence of each X-feature by year;
- total structural-X score distribution by year;
- differences 2025−2024, 2026−2025, 2026−2024;
- bootstrap intervals for prevalence differences;
- subfield-aware sensitivity check using the retained arXiv categories **only after primary blind scoring**;
- list of strongest positive exemplars for each feature, selected only after scores are frozen.

## Interpretation guard

A rise in a feature means it became more visible in this random abstract sample. It does **not**, by itself, establish influence from SAT/H(s)H, novelty loss, or a field-wide historical trend. Structural convergence, ancestry, deliberate import, and coincidence are separate questions.
