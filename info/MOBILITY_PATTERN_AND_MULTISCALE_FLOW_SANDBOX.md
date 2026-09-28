# Mobility Pattern + Multiscale Flow Sandbox

Status: exploratory / hypothesis-generation only
Date added: 2026-09-28
Repository role: methods/resources support, not theory authority

## Governing caution

This note records testable ideas and experiment designs. Correlation, predictability, low-dimensional structure, recurrence, or successful forecasting do **not** by themselves establish mechanism, ontology, causation, or SAT/H(s)H correspondence.

Search silence is not evidence of absence; likewise, pattern discovery in a large feature space requires held-out tests, null models, multiple-comparison control, and explicit effect-size reporting.

## Core observational proposition

Large collections of trajectories and state observations can reveal stable predictive regularities even when the underlying mechanism is unknown or disputed. The useful object is therefore not merely a trajectory but a hierarchy:

raw trajectories -> observables -> modes -> operators -> relations among operators -> invariants

Candidate mathematical toolkits include:

- human-mobility modeling / computational social science;
- dynamical systems and attractor reconstruction;
- Koopman operator methods;
- dynamic mode decomposition;
- tensor decompositions / latent-factor models;
- graph, hypergraph, and simplicial-complex representations;
- topological data analysis / persistent homology;
- sheaf methods for local-to-global consistency;
- category-theoretic or higher-structural descriptions when mappings among representations become the object of study.

These are neighboring formalisms, not evidence for one another.

## "Track the jaguar, track the gazelle" principle

Any observable that systematically follows people, vehicles, infrastructure demand, or environmental response can function as a coarse proxy for latent human-flow vectors even when it is not itself a person tracker. Examples include aggregate transit demand, traffic speeds, brake-light or deceleration waves, pedestrian counts, anonymized mobility matrices, energy demand, cellular load, and other public aggregate signals.

The research question is not "can we identify individuals?" but rather:

> What coarse collective structures remain measurable after removing individual identity and minimizing privacy risk?

## Citizen-scale experiment family

### 1. Recurrent-attractor test

Use a modest trajectory dataset (personal history if explicitly exported by the owner, or a public aggregate mobility dataset).

Measure:
- repeated destinations / route motifs;
- residence times;
- transition probabilities;
- temporal periodicity;
- recurrence under different coarse-graining scales.

Null comparison:
- time-shuffled trajectories;
- destination-preserving random walks;
- matched Markov surrogates.

Output:
- effect sizes and uncertainty;
- forecast accuracy on held-out intervals;
- largest spatial/temporal scale at which no detectable structure remains above data LoD.

### 2. Propagating-disturbance experiment

Model an observable analogous to brake-light waves on a highway: local perturbation -> neighboring response -> possible long-range propagation.

Candidate public data:
- loop-detector traffic speeds;
- public road-sensor feeds;
- transit headways;
- aggregated pedestrian counts;
- synthetic agent-based traffic when live data are unavailable.

Measure:
- disturbance propagation velocity;
- spatial attenuation;
- persistence time;
- bifurcation with density;
- whether a perturbation crosses a threshold from local decay to system-scale propagation.

A deer crossing a highway is a useful conceptual impulse input: the biological cause is incidental to the downstream dynamical question.

### 3. Cross-observable vector test

Construct several coarse observables over the same region/time window, e.g. traffic, transit, weather, event schedule, aggregate mobility, and energy demand.

Build latent composite vectors from each source independently, then ask whether their dominant modes align, lag, anticorrelate, or remain independent.

Require:
- preregistered feature set where possible;
- held-out periods;
- explicit control for common drivers such as time of day and weather;
- multiple-comparison correction;
- reporting of negative results and detection limits.

A useful negative result is of the form:

> No correlation of class X is detectable above magnitude Y at spatial resolution A and temporal resolution B in dataset D.

That constrains locally possible effect magnitude without requiring a mechanism.

### 4. Representation-invariance test

Represent the same data as:
- trajectories;
- transition graph;
- spectral/time-frequency modes;
- latent state vectors;
- topological summaries.

Ask which predictive structures survive transformations among representations. This is where categorical/sheaf-like language may become useful, but only after concrete mappings are specified.

## Privacy / ethics boundary

Prefer public aggregate data, synthetic data, or personal data deliberately exported by its owner. Avoid designing individual-surveillance workflows or re-identification pipelines. The scientifically interesting questions here are collective dynamics, predictability, scale dependence, and invariants, none of which require covert tracking of identifiable people.

## Multiscale flow conjecture — separate exploratory branch

Nathan proposed a broader intuition: as one moves across scales, contingent biological behavior may give way to stronger circulation/oscillation/flow regularities; examples invoked included atmospheric circulation, mantle/core convection, planetary magnetic structures, orbital motion, molecular agitation, and helical/oscillatory geometry.

This should be decomposed into falsifiable subclaims rather than treated as one thesis. Candidate questions:

1. At which scales do circulation/oscillation modes explain a large fraction of variance?
2. Do coarse-grained flows become more predictable with scale, and under what systems/conditions?
3. When does a helical or rotational representation add predictive power over ordinary state-space descriptions?
4. Are observed helical forms consequences of boundary conditions / conservation laws / forcing, or merely convenient visual parameterizations?

## Planetary branch — chronology and test discipline

A separate speculative idea raised in conversation concerned whether a major energetic event could substantially alter planetary internal circulation, volatile release, magnetic-field behavior, and long-term habitability.

Important chronology constraint: the canonical Moon-forming giant-impact / Theia event is an early-Solar-System event (~4.5 billion years ago), not an event ~1 billion years ago. Any hypothesis invoking a ~1 Ga "kick" therefore needs a different identified event and independent geological/geochemical evidence.

The Earth/Venus/Mars comparison should not assume similar present internal architecture merely from similar bulk size. Relevant variables include composition, water inventory, oxidation state, mantle rheology, crustal regime, heat budget, core state, rotation history, atmospheric escape, solar forcing, and tectonic/convective history.

Potential testable subquestions:
- Can known impact energies measurably reconfigure mantle/core circulation for geologically long intervals?
- What volatile-release signatures would such an event leave?
- What isotope/geochemical/mineralogical records could distinguish impact-triggered degassing from secular cooling or tectonic causes?
- Does a proposed mechanism predict Earth/Venus/Mars observables quantitatively rather than narratively?

## Immediate next steps

1. Locate 2–3 public aggregate mobility datasets with different spatial and temporal resolutions.
2. Choose one deliberately small personal-history dataset only if Nathan wants to export/use it.
3. Implement a minimal recurrent-attractor + null-model notebook.
4. Add a disturbance-propagation notebook using traffic or synthetic flow data.
5. Report effect sizes and detection limits before mechanism speculation.
6. Keep the planetary-flow branch in a separate hypothesis ledger until quantitatively constrained.

## What this note does not establish

- that human collective behavior is deterministic;
- that predictable patterns imply a particular ontology;
- that helical/rotational representations are physically privileged;
- that SAT/H(s)H explains mobility, biology, geophysics, or planetary evolution;
- that Theia or any later impact explains Earth's divergence from Venus or Mars.

It records a research program for finding, quantifying, and constraining patterns while preserving the distinction between observation and mechanism.
