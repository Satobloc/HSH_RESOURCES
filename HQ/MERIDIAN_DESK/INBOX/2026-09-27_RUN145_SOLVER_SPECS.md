# Meridian Run 145 — Solver Specs

Status: SANDBOXED / tested machinery only.  
Date: 2026-09-27.

## A. Two-rate palindromic recurrence

### Status
- 🟢 Exact recurrence identity and cosine-root discriminant derived analytically.
- 🟢 Answer-blind lag rule selected before examining recovery error: maximize the minimum exact discriminant over the declared gap grid subject to at least 40 windows.
- 🟢 Deterministic noisy benchmark completed: 120 trials per gap/stride, seed 260927.
- 🟢 Δω=0.10 survives at selected L=30: median relative error 0.6900%.
- 🟡 Δω=0.03 is degraded: 9.2520%.
- ❌ Under this acquisition/noise model, Δω=0.01 and 0.003 are not reliably resolved.
- 🟡 Numerical implementation is shared ordinary least squares with palindromic structure; no TLS claim.
- 🟡 Resolution frontier is configuration-specific, not universal.

### Mathematical core
For sample lag τ=LΔt and rates ω,ν,

\[
c_{n+4L}-s_1c_{n+3L}+s_2c_{n+2L}-s_1c_{n+L}+c_n=0,
\]

\[
s_1=2[\cos(\omega\tau)+\cos(\nu\tau)],\qquad
s_2=2+4\cos(\omega\tau)\cos(\nu\tau).
\]

\[
\Delta_q(\tau)=
4\sin^2\!\left(\frac{(\omega+\nu)\tau}{2}\right)
\sin^2\!\left(\frac{(\omega-\nu)\tau}{2}\right),
\]

and near τ=0,

\[
\Delta_q(\tau)\sim\frac{(\omega^2-\nu^2)^2}{4}\tau^4.
\]

**Theory-facing use:** recover paired rotation rates from controlled 4D/SO(4)-type trajectory samples before handing them to ᚼ/frame-history machinery.

**External use:** paired-oscillation reconstruction / identifiability benchmark where the palindromic recurrence applies.

**Recommendation:** retain analytic recurrence/discriminant as stable mathematics; keep numerical resolution statements bound to the declared acquisition/estimator. Next test a structured TLS/Prony-family estimator and altered noise/window configurations without answer-tuning.

---

## B. Particle Zoo typed topology/geometry

Controlling historical source freshly read: `SAT_THEORY_ARCHIVE_2023-25/SAT Mark V/SATv THE PARTICLE ZOO.txt`.

### Source-derived discriminator
The source assigns **flavor to resonance mode**, places quark flavors in one broad short/high-curvature filament class, places e/μ/τ in one broad lepton-filament class with heavier harmonics/tighter curve or faster twist, assigns bosons to ripple/transition objects, and baryons to three braided quark filaments.

Therefore a source-faithful particle-label map cannot depend on carrier topology alone.

Use typed state

\[
X=(C,F,G,E,B,P),
\]

with carrier/object class C, framing/topological data F, differential geometry G, excitation/phase E, binding/composition B, and persistence/event class P.

Let π_C retain only carrier topology/class. The source distinguishes labels through E and/or G while holding the broad carrier class fixed, so source-level labeling does **not** factor injectively through π_C.

### Calculated representative

\[
\gamma_n(s)=\bigl(R\cos(ns),R\sin(ns),ps\bigr),\qquad s\in[0,4\pi],
\]

with

\[
\kappa_n=\frac{Rn^2}{R^2n^2+p^2},\qquad
\tau_n=\frac{pn}{R^2n^2+p^2}.
\]

All n have interval carrier topology while the geometric invariants change.

The three-strand representative

\[
\beta_j(z)=\left(R_b\cos(2\pi z+2\pi j/3),R_b\sin(2\pi z+2\pi j/3),z\right)
\]

has equal matched-z strand separation `sqrt(3) R_b`; the numerical regression spread was `8.9e-16`.

### Status
- 🟢 Original Zoo source recovered and used directly.
- 🟢 Typed-state/non-injectivity constraint follows from source definitions.
- 🟢 Harmonic filament family built, run and numerically measured.
- 🟢 Three-strand braid representative built and regression checked.
- 🟡 Exact particle-specific parameters are not fixed by the recovered Zoo file.
- 🟡 Open-strand braid topology requires explicit endpoint/boundary/framing conventions.
- ❌ Do not assign a unique knot/braid invariant to every particle until those conventions are recovered or Nathan specifies them.
- ❌ Do not treat a phase ripple as spatial displacement without a readout map.

### Similar-use literature — context, not equivalence
- Bilson-Thompson, Hackett & Kauffman, *Particle Topology, Braids, and Braided Belts*, DOI 10.1063/1.3237148.
- Finkelstein, *The Elementary Particles as Quantum Knots in Electroweak Theory*, DOI 10.1142/S0217751X0703707X.
- Asselmeyer-Maluga, *Braids, 3-Manifolds, Elementary Particles*, DOI 10.3390/SYM11101298.

**Theory-facing value:** prevents the Zoo from collapsing geometry, framing, excitation and binding into a single overloaded “topology” field.

**External value:** a general design rule for filament/braid taxonomies: separate topological equivalence class from metric geometry, framing, internal mode and composition before claiming classification.
