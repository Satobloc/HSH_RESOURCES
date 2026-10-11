# Meridian | Independent hostile comparative review 1/6 | 11 October 2026
**Scope:** private HSH_RESOURCES review of Paper A against randomly assigned Miller comparator Paper B. **SANDBOXED.**

## Mandatory verdict

**Paper A is WORSE as a contribution to original theoretical physics, derivational depth, and mathematical novelty.** Its advertised pitch equations and tabulated numbers are *correct* within the supplied conventional approximations, but the transformations are deterministic repackagings of known radial decay and orbital-frequency laws. Its 4D embedding lies in a **three-dimensional affine subspace**, so it establishes no intrinsically four-dimensional structure, new dynamics, or empirical discriminator. **Paper B is stronger as a substantial field-theoretic pedagogical derivation, not because of venue or title.** Miller also states that his self-dual theories are non-unitary and do not provide a unitary completion of general quantum gravity.

**Publication dispositions:** A **REJECT** as a new-physics/original theoretical-physics PRD research claim; **MAJOR REFRAME/REVISION** as a mathematical-methodology or educational note with reproducible benchmarks. B **READY TO CIRCULATE AS A SPECIALIST REVIEW/LECTURE NOTE**, subject to normal expert checking; **NOT** established as a novel unitary quantum-gravity theory. These are independent absolute judgments on different intended genres, not a rating by arXiv status.

## Source integrity and access
- **Paper A, complete original source:** Nathan McKnight, *Cross-Scale Geometric Representation of Classical Inspirals: Four-Dimensional Helical Embeddings and Mass-Substitution Fingerprints*, 11 Oct 2026, `reviews/2026-10-11_HELICAL_SCALING/PAPER_A_FULL_SOURCE.tex`, Git blob `551922f8956c8991b210ae53e60811b59b0e3232`, 244 lines, ~22,096 chars. Read complete RevTeX manuscript, every section, its table and appendix. Built PDF not accessible, but this is full prose and mathematics. Equations referred to by LaTeX labels `eq:G`, `eq:E`, `eq:X`, `eq:common`, `eq:descriptors`, `eq:pG`, `eq:pE`, `eq:phaseMap`, `eq:timeMap`, `eq:S`, `eq:fps`, etc. Source figures require regeneration.
- **Paper A companion:** `reviews/2026-10-11_HELICAL_SCALING/reproduce.py`, Git blob `11f1820540f9cd38757fcd116566cb0a9dd6cfd8`, 5,398 chars; inspected throughout. Four symbolic assertions, CSV table and four generated figures. All main numeric rows independently recomputed in Python/SciPy. I did not claim to execute the repository script itself.
- **Paper B, actual primary source:** Noah Miller, *The facts on quantum self-dual Einstein gravity and self-dual Yang-Mills theory*, arXiv 2608.26242v1, 26 Aug 2026, 128-page original archived `OUTSIDE RESEARCH LIBRARY/CONTEMPORARY RESEARCH/2608.26242v1.pdf`; full text provided through existing `derived/text/82f00f0d12716ea7218f386a405b1aa1b9de2230cb089270c592aa594780fed8.txt`. Manifest reports 128 pages and ~226,045 nonspace characters. Retrieved complete 128-page extraction, inspected introduction, theory summaries, lightcone derivations, loop-amplitude sections, celestial discussion, covariant formulations and proof appendices. The review below does **not** purport to independently validate every specialized 128-page loop integral. For page references below, `extract p.N` is source-PDF extracted page N (usually printed article page N-2). For Paper A there is **no verified PDF pagination**, so use exact section/formula names instead. 
- **Mersearch provenance:** request `2026-10-11-orson-morrow-inspiral-package-001`, output folder in HsH `indexes/mersearch_requests/`, verifies three-root search, pinned Mersearch 1.0 commit `89933c358b67ccbfbbaa680aadeb1f35d22d91b2`, SHA-typed corpus snapshots. The newly delivered manuscript was then retrieved from HSH_RESOURCES separately; its presence cannot be backdated to the Mersearch run snapshot. Do not rewrite other workers' requests. Hypothesis H proper and directly Schreiber-authored sources not used.

## I. Independent analytic checks of Paper A

### Canonical formulas and dimensions
A gives from quadrupole gravitational circular-inspiral and Kepler laws
```
rdot_G = -[64 G³ M m(M+m)/(5c⁵)]/r³;
phi_dot_G = sqrt(G(M+m)/r³).
```
Define beta=r phi_dot/c, nu=M m/(M+m)², pitch P=|rdot|/(r phi_dot). Algebra gives
`P_G=(64/5) nu beta^5`, with no dropped (M+m) factors. Verified independently. Leading quadrupole radiation reaction only, not a valid full two-body dynamics at strong field, or an independent SAT prediction.

For charges K=|qQ|/(4π epsilon0), attractive Coulomb circular orbit E=-K/(2r) and Larmor power q² a²/(6π epsilon0 c³), dE/dr=K/(2r²), and a=K/(m r²) imply
```
rdot_E= -q² K/(3π epsilon0 c³ m² r²);
phi_dot_E=sqrt(K/(m r³));
P_E=(4/3)|q/Q| beta³.
```
Exact within the stipulated classical, fixed-source, radiation-balanced approximation. The radiated orbital power is not a model of a stationary quantum electron.

Dimensional sanity: in rdot=-a r^-n, a has L^(n+1)/T and b in phi_dot=b r^-3/2 has L^3/2/T. A's appendix dimensions are correct.

### Independent mass-substitution table
Using SciPy SI constants and A's values M=1.98847e30 kg, Earth m=5.9722e24 kg, r_G0=1AU, r_E0=5.29177210903e-11 m, e and m_e from SciPy, I obtain:

| Map | beta0 | P0 | formal T0 (s) | formal N0 (turns) |
|---|---:|---:|---:|---:|
| A G/electron | 9.935253998e-5 | 5.6764235744e-80 | 2.2120296722e85 | 1.1215156234e78 |
| B G/Earth | 9.935268918e-5 | 3.7215237435e-25 | 3.3739939304e30 | 1.7106427803e23 |
| C E/electron | 7.29735256186e-3 | 5.18125210055e-7 | 1.5561774658e-11 | 2.04783116775e5 |
| D E/Earth | 2.84998553418e-30 | 3.08650300079e-89 | 6.6888247304e98 | 3.4376540495e87 |

All rows reproduce manuscript values to displayed precision. They are **formal endpoint continuations**, not a physically coherent four-regime experiment or observational predictions. In the gravitational case, the orbiting-mass substitution scarcely changes initial orbital velocity: the relative change in beta0 between electron and Earth is ~1.5017e-6, even though the normalizations change by ~55 orders. The fingerprint vector is mainly a derivative of the source equations.

### Normalized maps
Integrating dr/dt=-a r^-n, dphi/dt=b r^-3/2 yields
`T0=r0^(n+1)/[(n+1)a]`,
`Phi0=b r0^(n-1/2)/[a(n-1/2)]`,
`f_phi(x)=1-x^(n-1/2)`,
`u(x)=1-x^(n+1)`.
For n_G=3,n_E=2, equal normalized winding yields x_E=x_G^(5/3); equal elapsed fraction yields x_E=x_G^(4/3). Under phase map, u_E-u_G=x_G^4(1-x_G), whose derivative x_G^3(4-5x_G)=0 at x_G=4/5; maximum 256/3125=0.08192. **Correct algebra.** It says nothing about equality of physical scales, exact phases, time delay or similarity of embedding curvature.

### Logarithmic fingerprints
At fixed central parameters:
```
f_G=(-3,1+m/(M+m),-3/2,m/[2(M+m)]);
f_E=(-2,-2,-3/2,-1/2).
```
Verified. From log P=log F-log r-log Omega, dlog P/dlog r=(dlogF/dlogr)-1-(dlogOmega/dlogr), so -5/2 and -3/2 respectively. This is **coordinate-/parameter-dependent bookkeeping**, not an intrinsic geometric invariant, as Paper A correctly warns.

Damped oscillator: m xdd+gamma xd+kx=0 and gamma²<4km imply r=r0 exp(-gamma t/(2m)), omega_d=sqrt(k/m-gamma²/(4m²)); f_D=(1,-1,0,-1/2+gamma²/(8m² omega_d²)) and radial log pitch slope 0. Verified independently. This makes explicit why a common helical depiction does **not** imply dynamical similarity.

## II. Strongest counterexamples and overlooked edges

**1. The 4D novelty bottleneck (decisive).** A's Eq `eq:X`: `X(t)=(ct,r cos(phi),r sin(phi),0)` lies for all times in the proper affine subspace `x_3=0` of `R⁴`, isometrically `R³`. Its third generalized Frenet curvature is identically zero, which A correctly states. A can be computed entirely with `R³` circular/spiral differential geometry. Thus the word “four-dimensional” describes one redundant ambient coordinate, not a new 4D behavior. **Shortest rejection:** every 4D scalar diagnostic reduces to standard 3D curve geometry; the remaining distinct formulas are already algebraic consequences of Peters/Kepler/Larmor. No independent geometrical invariant, experimentally measurable discrepancy or 4D nontriviality has been established. This is an originality argument, not a claim Eq X is false.

**2. Exact local timelike failure of formal Coulomb continuation.** If the same X(t) were interpreted as a physical Minkowski history `eta=(-+++)` with w=ct, it would be timelike only when `beta²[1+P²]<1`. For |q/Q|=1, `P_E=(4/3)beta³`, giving null bound `beta²+(16/9)beta⁸=1`. Solve: `beta_crit=0.8129429803`, and for an electron `r_crit=K/(m_e c² beta_crit²)=4.26394526e-15 m = 8.05769e-5 r_Bohr`. The formal trajectory beyond that radius becomes spacelike; the source model's nonrelativistic Larmor approximation has already failed earlier. The paper **does explicitly disclaim** physical continuation to zero, so this is not a covert contradiction. But any stronger SAT worldline claim or treating `T0,N0` as physical is killed. Mark the admissible domain on figures/controls.

**3. Intrinsic asymptotic approximation, independently tested.** A defines `h=kappa/abs(tau)`, `S=(1/kappa) d h/dsigma`, and claims `S~P/2` for beta,P much smaller than 1. I independently differentiated the Euclidean Frenet curvature and torsion of Eq X using the actual time-dependent r(t), phi(t), including angular acceleration. At electron Coulomb initial values beta=.00729735256, P=5.1812521e-7, n=2, `S/(P/2)=1.000026625`: accurate. At beta=.1,P=.03,n=2, ratio 1.01176952. At beta=.5,P=.1,n=3, ratio 1.31643792: significant departure. **The equation is not an exact scale-crossing law.** Paper A labels it asymptotic, so retain with quantified error envelope.

**4. No independent cross-sector control.** The four cases hold masses fixed *within* each model but use completely different central sources and orbital radii *between* models. One cannot infer a tested universal mass scaling across gravity and EM from the four numbers. Even matching beta merely compares algebraic functions at a common coordinate argument. Author already makes several correct limitations explicit; novelty nevertheless remains unproven.

**5. Third-system control is analytically valid but weak.** Oscillator proves only that a distinct radial law yields a distinct exponent; no independent data, no matched physical source/response, and no fixed k,gamma example tested for both substituted masses. It is a mathematical sanity counterexample, not an independent test of an SAT hypothesis.

## III. Comparator B: actual technical substance and caveats

Miller is a **128-page pedagogical study** of quantum *self-dual sectors*, not ordinary, unitary and phenomenologically complete quantum gravity. Primary source extraction:
- Extract pp.4–5, Eq (1.1) self-duality F=i *F and R=i *R; (1.2) and (1.3) lightcone cubic actions `S_SDYM=-∫ tr[barPhi(Box Phi + i sqrt(2)g[partial_u Phi,partial_w Phi])]`, `S_SDG=-∫ barphi(Box phi - kappa/2 {partial_u phi,partial_w phi})`. Explains self-dual amplitudes are truncated helicity channels and emphasizes **non-unitarity** (extract p.5). Don't mistake the tagline “finite quantum gravity” for full Einstein quantum gravity.
- Extract pp.9–11 Eqs (2.2)–(2.22): derives Yang-Mills EOM from the self-duality constraint and Bianchi identity; analogue for Ricci flatness. In signature (1,3), Hodge star squared on 2-forms is -1, so nontrivial real self-dual solutions require complexification, explicit nonphysical reality limitation; (2,2)/(4,0) allow real eigenvalue ±1.
- Extract pp.15–16 Eqs (4.5)–(4.12): lightcone gauge fixing, Faddeev-Popov ghost decoupling under chosen conditions and derivation of cubic SDYM action by truncating full YM.
- Extract pp.17–24, Sec.5: expansion/truncation of Einstein-Hilbert and derivation of self-dual gravity cubic action; explicitly notes tedious gauge algebra and boundary assumptions.
- Extract pp.27–36: polarization conventions, lightcone Feynman rules, Berends-Giele current recursion and (conditional/distributional) one-minus tree amplitude vanishing.
- Extract pp.38–61: rational finite one-loop all-plus amplitude properties, collinear limits, double-off-shell calculations and Bern-Dixon-Perelstein-Rozowsky graviton expression. These are concrete mathematical scattering observables absent from A; I have not independently reproduced the full loop integrals.
- Extract pp.62–78: classical self-dual solutions and celestial current/symmetry discussion. Boundaries of scope visible.
- Extract pp.82–94, App B: covariant first-order SDYM/SDG actions, connections/tetrads, gauge fixing and a deliberately labelled “slightly hand-wavy” supplementary finiteness argument. Eqs (B.29)–(B.52) draw a defined line from Palatini/tetrad gravity to the self-dual truncation.
- Extract pp.95–117 appendices C–H: color ordering, Schouten-based recursion, double-off-shell currents, cyclic invariance, and classical perturbiner/S-matrix relationships; references pp.118–128. Complete extracted source retrieved; specialized proofs sampled for review rather than certified line-by-line.

**B's weaknesses:** enormous tutorial footprint, relies on established SDYM/SDG research, and its physical action is *nonunitary* and complex-valued for nontrivial (1,3) self-duality. Its claimed one-loop UV/IR finiteness cannot be exported to unitary Einstein gravity or Standard Model matter, and not every citation-specific result is new. Those limitations are expressly acknowledged and are not licenses to inflate A's scientific novelty.

## IV. Head-to-head judgment by eight independent axes

| Axis | Better | Reason |
|---|---|---|
| (1) Algebra actually supplied | **B** | B derives lightcone YM/Einstein action reductions and nontrivial currents, amplitudes and loops (extract pp.15–24, 27–61). A's correct algebra follows from two supplied ODEs (Secs. Canonical equations, Geometric response laws). |
| (2) Verified quantitative implementation / accessible rerun | **A** | A ships `reproduce.py`, four numerically reproducible extreme mass-substitution cases, explicit constants and four figure outputs; B gives mathematical derivations without comparable turnkey end-user numerical fixture. A script inspected; four rows independently reproduced, not claimed that script was run here. |
| (3) Novel contribution beyond textbooks/literature | **B** | Though review-oriented, B supplies detailed gaps/derivation exposition and extensive cross-checks (Secs 4–13, Apps B–H); A's power exponents and normalized maps are direct algebraic consequences of the input models, with no new predictive law. B not thereby classified a new QG discovery. |
| (4) Physical interpretation and explicit limits | **TIE** | A carefully disclaims quantum electron, r→0 endpoint, 4D physical dynamical claims and mismatched-family constants. B explicitly restricts to nonunitary self-dual sectors and complex Lorentzian solutions (extract pp.5,11). Both avoid their worst possible overclaims when actually read. |
| (5) Generality/derivational mechanism | **B** | B obtains a restricted but actual theory-level gauge/covariant action and helicity-sector consequences (extract pp.9–24,82–94); A does not derive source interactions or new equations of motion. |
| (6) Direct empirical discrimination from competing physics | **INCOMPARABLE** | A computes physically meaningful standard classical orbital ratios but proposes no new discriminator; B recovers QFT one-loop amplitude channels in a deliberately nonunitary self-dual subsector and similarly does not claim direct physical detection of a new gravity theory. Contrasting these observational targets is a category error; neither produces a verified new discriminating prediction. |
| (7) Source fidelity and priority discrimination | **B** | B extensively names antecedent derivations, limitations, appendix-level proofs and references (through extract pp.118–128). A cites Peters, Jackson, Maggiore but demonstrates no distinct established research gap addressed by its trivial 3D subset embedding and exponent correspondence. |
| (8) Expository economy for the stated small task | **A** | A's compact four-map controlled algorithm is accessible and teachable; B's comprehensive 128-page review has quite different educational goals. Better for a quick teaching exercise, not stronger as original physics. |

The score is **B better on 4 axes; A better on 2; tie 1; incomparable 1**. This is an aid to analysis, NOT a mechanical acceptance threshold; original physical derivations matter more than ease of visualization.

## V. Highest-value repair path for Paper A

1. **Retitle and reposition** as “A reproducible coordinate-normalized comparison of classical circular inspiral laws” or analogous. Explicitly state `X_3=0` and no intrinsic 4D novelty in abstract, introduction and caption. Do not imply Euclidean 4D embedding itself is new physics or uniquely SAT.
2. **Add mathematical uniqueness / nontriviality test.** Exhibit a genuinely 4D invariant or provably useful new algorithm that cannot be recovered from the 3D planar worldline and known ODEs. If none exists, embrace a clean educational methodology paper rather than making an original-theory claim. Test whether identifiability survives arbitrary monotone time reparameterizations, redefinitions of r, and independent angular baseline normalization.
3. **Separate within-family one-variable controls from across-family contrasts** with an input table fixing M,Q,r0 and showing which are held constant. State that two wildly formal test masses do not themselves furnish new physical data. Use SI uncertainties only if a real measurement comparison is actually attempted.
4. **Domain-gate all four examples** using adiabaticity, weak field, nonrelativity and timelikeness criteria. Show C's illustrative Minkowski timelike cutoff beta=.81294298 at r=4.26394526e-15m as a sharp sanity bound but warn its classical nonrelativistic approximation breaks earlier. Mark all T0 and N0 as unavailable physically well before r=0.
5. **Quantify intrinsic asymptotic error**, e.g. exact numeric Frenet evaluation vs S≈P/2 for beta,P grid, and show h/tau singularities and parameter dependence. At beta=.5,P=.1 the claimed approximation differs by 31.6%.
6. **Strong alternative null comparisons:** include at least one canonical spiral with identical P(beta) but physically different forces, or two models with distinct P(beta) yet Euclidean-similar curves after permitted coordinate/time changes. The former would prove the pitch law cannot independently identify interactions. Any inference to GR↔QM or HsH needs its own conserved 4D object, not a map between normalizations.
7. **Better citations** for the specific leading quadrupole and Larmor domains; correct typography `Na\"ive` typo in conclusion; provide PDF+code with four compiled figures, tests and script dependencies, and state bibliographic search limits before declaring novelty.
8. **Empirical gate, only if aiming at PRD:** pre-register one held-out orbital decay observable or direct 4D core/timesheet geometry mapped to an independently measurable discrepancy with error budget, rather than claiming visual identity from normalized self-plots.

## VI. One shortest desk-review-safe abstract (proposed)

“We give a reproducible comparison of leading-order gravitational quadrupole and classical Coulomb–Larmor circular inspirals by evaluating the same two distinct orbiting masses in each equation family. Representing these prescribed planar motions as time-extended curves X=(ct,r cos phi,r sin phi,0), we derive the dimensionless pitch relations P_G=(64/5)nu beta^5 and P_E=(4/3)|q/Q|beta^3 and the distinct nonlinear correspondences between their normalized winding and elapsed-time profiles. The embeddings lie in a three-dimensional affine subspace of Euclidean four-space and neither add physical dimensions nor unify the interactions. Four numerical fixtures and a damped-oscillator counterexample illustrate how coordinate-specified scaling responses can be compared without implying shared dynamics. The calculations are a controlled analysis and teaching procedure for established approximations, not novel physical predictions.”

**Review completion:** both primary full-text sources retrieved, A fully inspected and independently numerically reproduced; B text accessible in full and relevant theory, caveat, derivation and appendix sections inspected, **not a claim that all 128 pages' loop calculations were independently proven**. No results imputed from arXiv authority, no restricted unpublished comparator quoted outside this private repository.

**Reviewer: Meridian ◈**
