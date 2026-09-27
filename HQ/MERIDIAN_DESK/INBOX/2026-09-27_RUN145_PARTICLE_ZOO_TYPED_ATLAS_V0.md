# Particle Zoo Typed Atlas v0 — source/context diagnostic

**Status:** SANDBOXED / worker-facing spec  
**Run:** Meridian 145 — 2026-09-27

## Source layers

1. **Historical Zoo baseline:** `SAT Mark V/SATv THE PARTICLE ZOO.txt`.
   - flavor is explicitly a resonance mode;
   - e/μ/τ share the broad lepton-filament family;
   - quark flavors share the broad short/high-curvature filament family;
   - bosons are ripples/transitions;
   - baryons are three-filament braids.

2. **March 2026 Worldlines formalization:** `SAT 2026 PRE HsH/SAT 2026 PARTICLE TYPES — Worldlines.txt`.
   - adds specific coiling-order/intersection language;
   - places neutrino in a “Boson Sector” and makes e/μ/τ higher nesting orders;
   - also contains legacy lattice/constants/other machinery now controlled or downgraded elsewhere;
   - therefore this file is genealogy/context, not automatic current authority.

3. **Nathan-authored later topology conversation:** `HsH AHA TOPOLOGY.txt`.
   - recovered context includes Nathan describing an electron as a single first-order filament coil and suggesting quark geometry may be similar with packing differences;
   - treat this as direct Nathan context requiring exact turn-level provenance before canonical promotion.

## Typed-state rule

Use

\[
X=(C,F,G,E,B,P)
\]

with carrier/object class C, framing/topological/boundary data F, differential geometry G, excitation/resonance/phase E, binding/composition B, and persistence/event class P. Do not collapse these fields into a single `topology` label.

## Atlas v0

| label | C carrier | F framing/topology | G geometry | E excitation | B binding | P persistence |
|---|---|---|---|---|---|---|
| electron | persistent filament | generic twist/handedness language only | singly curved / stable angular deviation | baseline lepton resonance state | independent | persistent |
| muon/tau | persistent filament | same broad lepton family | tighter curve and/or faster twist in baseline source | heavier harmonic / resonance | independent | unstable persistent |
| neutrino | filament in baseline; later source retypes sector | possibly open/leaky, not fixed | near-aligned / near-parallel | not fixed | non-composite | coherent/persistent in baseline |
| quark | short filament segment | topology-dependent boundary constraints; phase/braid-parity language | short high-curvature/high-angle | flavor = resonance mode | composite-required in baseline | persistent constituent |
| photon | ripple/transition on bundle | not fixed | carrier geometry not specified as displaced | phase-alignment ripple | propagation along aligned bundles | transient |
| gluon | internal ripple | braid context | not fixed | confined internal mode | confined to quark thread | transient/confined |
| W/Z | local reconfiguration event | not fixed | steep angular transition | high-energy transition | mediating/reconfiguring | short-lived |
| Higgs | stabilization/structural event | not fixed | not fixed | structural stabilization | supports stable configuration | event |
| proton/neutron | 3-filament composite | three-braid + compatibility language | bundle geometry | internal mode not uniquely fixed | 3 quark filaments | persistent composite |
| pion/kaon/meson | 2-constituent bundle | loop/tension language | short bundle | not fixed | quark-antiquark | unstable composite |

## Three new diagnostics

### A — near-alignment
For
\[
\gamma_R(s)=(R\cos s,R\sin s,ps),
\]
the tangent angle to the axis is
\[
\theta=\arctan(R/p).
\]
At fixed p=0.16, reducing R from 0.55 to 0.10 to 0.02 reduces the calculated angle from 73.78° to 32.01° to 7.13°, while the carrier remains an interval.

- 🟢 “near-aligned” is implementable as a metric/differential-geometric state.
- 🟡 this does not assign a neutrino parameter value.
- ❌ topology alone cannot encode this distinction.

### B — bounded high-curvature segment
Representative:
\[
q(s)=(0.15\cos s,0.15\sin s,0.03s),
\qquad s\in[-0.75\pi,0.75\pi].
\]
Calculated: κ=6.410256, τ=1.282051, arclength=0.720857, endpoint chord=0.254923, turns=0.75.

- 🟢 “short/high-curvature segment” is geometrically implementable.
- 🟡 endpoints can be marked/fixed explicitly.
- ❌ particle-specific open-braid/topological class remains `UNRESOLVED` until endpoint tangent/framing/closure/environment rules are specified.

### A — phase field on fixed carrier
Use a straight carrier
\[
\gamma(z)=(0,0,z)
\]
and a normal director
\[
d(z,t)=(\cos(2\pi kz-\Omega t),\sin(2\pi kz-\Omega t),0).
\]
At k=3, the phase advances 6π while the carrier centerline displacement remains exactly zero.

- 🟢 a “phase ripple” can be represented without pretending the centerline itself spatially ripples.
- 🟢 director-norm regression error was 1.1×10^-16.
- 🟡 whether SAT/H(s)H intends this normal-bundle interpretation is a model question.
- ❌ do not promote this representative into photon/gluon identity without the missing readout/dynamics.

## Recommendation

Implement the Zoo as a **typed state machine / geometry registry**, not a lookup from particle name to knot type. Topological invariants should be optional fields whose domain conditions are checked before evaluation.

Next source task: recover exact Nathan-level definitions or corrections for endpoint/framing rules, the intended distinction between electron/quark first-order coils, and whether phase ripples live on centerlines, worldtube boundaries, frames, or timesheet/intersection variables.
