# Meridian Run 146 — coupled filament–timesheet / string bridge

**Status:** SANDBOXED / derivational spec, not a physical claim  
**Date:** 2026-09-27  
**Visual status:** A — calculated geometry/numeric diagnostics succeeded

## Source constraints actually used

Internal: Nathan's `SAT ALL TOGETHER SYNTHESIS.txt`; `MORE_PYTHON/timesheet_proj.py`; `🧱SAT ST.txt` as historical precursor only; `WORKSPACES/WORLDTUBE_LAB/FINITE_CORE_TANGENCY_PACKET_002.md`; current H(s)H status file confirming ᚼ as live solver machinery. External comparison: Akama (1988) induced string action; Battye & Carter (1995) relativistic membrane/string perturbations; Capovilla & Guven (1998) extended objects with edges; Ishibashi (2023) closed-string pants decomposition; de Vega & Sanchez (1995) classical string splitting. No equivalence is asserted.

## 1. Minimal geometry

Use four coordinates `X=(x1,x2,x3,q)`, with `q` the SAT propagation coordinate that becomes the Minkowski time-normal direction in the flat readout. Let

`Σ_τ : F(X,τ)=q-c_Σ τ-h(x,τ)=0`.

Flat limit: `h=0`, `q=c_Σ τ`.

A filament/tube center carrier is `Γ(s,τ)=(u(s,τ),q(s,τ))`. The readout operator is

`I_{Στ}[Γ]=Γ(s*,τ)` where `F(Γ(s*,τ),τ)=0`.

This keeps **carrier geometry** distinct from **intersection trace**.

## 2. Minimal ᚼ nesting operator

One explicit normal-plane nesting step can be written

`H_{r,k,φ,Π}[Γ](s)=Γ(s)+r[cos(ks+φ)N1(s)+sin(ks+φ)N2(s)]`,

with `(N1,N2)` a transported normal-plane frame. Recursive hypersuperhelices satisfy `Γ_{j+1}=H_j[Γ_j]`.

For small nested amplitudes the moving normal frames linearize and the recursion becomes a Fourier-like mode sum plus `O(r_i r_j k_i k_j)` corrections. Therefore **free string-mode superposition is naturally the linearized limit of recursive hypersuperhelix geometry**; the genuinely H(s)H-specific part begins with the nonlinear moving-frame terms.

## 3. Exact guitar-string → helix trace theorem

Take an almost straight filament

`u_x=A cos(ks-ωτ)`,  
`u_y=A sin(ks-ωτ)`,  
`q=s`.

A flat moving sheet `q=v_Σ τ` samples `s*=v_Σ τ`, giving

`γ(τ)=(A cos Ωτ, A sin Ωτ, v_Σ τ)`

with

`Ω = k v_Σ - ω`.

Thus the readout is **exactly a circular helix** whenever `Ω≠0`, even though the material carrier is not helical. Pitch per turn:

`P_trace = 2π v_Σ / |k v_Σ - ω|`.

For a multimode field, sampled frequencies are `Ω_j=k_j v_Σ-ω_j`. Commensurate `Ω_j` close/repeat; irrational ratios give quasiperiodic traces.

This directly supports the user's "guitar-string model" as a mathematically coherent branch.

## 4. Does slicing commute with ᚼ?

Generally `I_Σ∘H ≠ H∘I_Σ`.

Exact commuting case: flat sheet, purely transverse ᚼ displacement, and unchanged longitudinal coordinate `q=s`. Then `s*=v_Στ` is unchanged.

For a longitudinal perturbation or tilted/flexed sheet, linearization gives

`δs* = -(n·δΓ)/(n·∂_sΓ)`.

The denominator is the incidence factor. It becomes ill-conditioned at tangency, exactly where the existing finite-core quadratic contact law takes over.

## 5. Minimal angular coupling

Let `T` be local filament tangent and `n` the sheet normal. Define `cosθ=n·T`, with `θ=0` normal incidence. Smallest even resistance function with minimum at normal incidence:

`f(θ)=sin²θ=1-(n·T)²`.

Take local angular energy `U_θ=(K_θ/2)sin²θ`. The aligning torque magnitude is

`|τ_θ|=K_θ|sinθ cosθ|=(K_θ/2)|sin2θ|`.

**Important:** angle-only coupling on a perfectly flat homogeneous sheet produces alignment torque but no long-range translational force. A Newtonian branch requires an actual sheet deformation field or other nonuniform mediator.

## 6. Helix orientation and mean load

If local helix tangent makes internal pitch angle `β` to its long axis, while the long axis is tilted by `ψ` relative to the sheet normal, then averaging around one turn gives

`<sin²θ> = 1 - cos²β cos²ψ - (1/2) sin²β sin²ψ`.

At `ψ=0`, this reduces to `sin²β`.

This creates a hard consistency condition: if this branch is to recover Newtonian gravity, arbitrary orientation dependence must either be part of the body's fixed inertial/rest state or average away in the weak-field low-velocity limit.

## 7. Coil-squash parameter

For `Γ(φ)=(R cosφ,R sinφ,pφ)`, arc length per radian is `ℓ=sqrt(R²+p²)`. If the filament is approximately inextensible over the squash time scale,

`R δR + p δp = 0`, hence `δR=-(p/R)δp`.

Axial compression widens the coil.

Let `K_sq` be effective pitch stiffness and `P_c` the local compressive generalized load. Define

`Π_sq=P_c/(K_sq p0)`.

Small deformation:

`S_coil := -δp/p0 ≈ Π_sq f(θ)`.

This is a parameterization, not an absolute prediction; `K_sq` and the coupling scale are not yet derived.

## 8. Sheet flex gives a Newtonian-like far field

Let the timesheet normal displacement be `h(x,t)` with

`E_Σ = (1/2)∫d³x [ρ_Σ hdot² + T_Σ|∇h|² + B_Σ(∇²h)²]`.

With point-like integrated coil loads `q_i`,

`ρ_Σ hddot + η_Σ hdot - T_Σ∇²h + B_Σ∇⁴h = Σ_i q_i δ³(x-x_i)`.

Static long-wave limit:

`-T_Σ∇²h = q δ³(x)`

so

`h(r)=q/(4π T_Σ r)`.

A second coil coupled by `U=-q_j h` feels

`F_ij = -(q_i q_j/(4πT_Σ)) rhat/r²`.

Thus the inverse-square law is the Green-function consequence of a scalar normal-displacement field living on a **3D** sheet; it is not manually inserted.

To recover the Newtonian weak-field form one requires `q_i=α m_i`, yielding

`G = α²/(4π T_Σ)`.

That proportionality is a hard equivalence-principle condition.

With bending stiffness, `ℓ_b=sqrt(B_Σ/T_Σ)` and

`h(r)=q[1-exp(-r/ℓ_b)]/(4πT_Σ r)`.

The force becomes

`F(r)=|q1 q2|/[4πT_Σ r²] × [1-(1+r/ℓ_b)e^{-r/ℓ_b}]`.

Far field is `1/r²`; short range is softened. Finite B3/B2/S2 carrier size smooths it further.

Long-wave sheet speed: `c_Σ=sqrt(T_Σ/ρ_Σ)`. If this is meant to carry the gravitational/time-sheet disturbance, the first calibration is `c_Σ=c`. A literal viscosity `η_Σ` is much more constrained because it introduces attenuation/preferred-medium behavior; the "syrup" analogy is safer for damping intuition than as the origin of static gravity.

## 9. Exact tilt threshold

For static helix `Γ(φ)=(R cosφ,R sinφ,pφ)` and tilted moving plane `q-a x=v_Σt`, `a=tanψ`, intersection requires

`pφ-aR cosφ=v_Σt`.

The left side is globally monotone if `p>|a|R`, so the exact single-trace condition is

`|tanψ| R/p < 1`, equivalently `|tanψ tanβ|<1`.

At equality a fold/tangency begins; beyond it the same sheet can intersect the helix in multiple places. This is a **readout multiplicity transition**, not automatically particle creation.

Near the fold, the centerline singularity is replaced by the current finite-core law

`n·y + αs + (1/2)A_rel s² = 0`,

with crossover

`Λ=|α|/sqrt(|A_rel| ρ_eff)`.

## 10. String-theory assignments

### A — vibrating filament / free-string-like field
If `u_tt-c_f²u_ss=0` and `s` is periodic, the field has the same classical left/right decomposition as a free closed-string transverse field after rescaling. This is a defensible **structural correspondence** only. It does not yet import Virasoro constraints, quantum mass-shell relations, target dimension, or gauge charges.

### B — intersection trace is the string
A closed one-parameter trace cannot generally reconstruct the two-parameter worldsheet. Therefore `closed trace ≠ complete closed-string state` without an additional injective reconstruction rule.

### C — finite tube/support is primary
A literal closed-string spatial section is `S¹`. A full isotropic H(s)H B3 core sliced by a 3D timesheet generically gives bulk/S2-type readout, not `S¹`. Literal string identification therefore favors extra selected structure: a B2 support with boundary `S¹`, a distinguished cylindrical sub-surface `S¹×I`, or an effective boundary mode. If one `S¹` evolves into two, the 2D history has pair-of-pants topology—the genuine standard topology match to closed-string splitting/joining.

### D — material hypersuperhelix is the string
Strongest claim. Requires a true 2D worldsheet, periodic string coordinate, Polyakov/Nambu-Goto or declared effective-string dynamics, Virasoro constraints, quantum level matching, physical string tension `T_s=1/(2πα')`, and a target-metric/signature map from SAT/H(s)H to Lorentzian string theory.

## 11. Repair to old SAT↔ST precursor

Do **not** retain the old statement that open-string `sin(nσ)` and `cos(nσ)` profiles are interchangeable by an ordinary phase choice. Neumann and Dirichlet endpoint conditions are genuinely different. Also, standard ST gauge charges are not obtained merely by declaring holonomy of an arbitrary projected loop to be U(1)/SU(2)/SU(3); any SAT holonomy dictionary requires separate derivation.

## 12. Moving sheet is chirality-selective

For `ω=c_f k`, a co-propagating wave sampled at `s=v_Στ` has `Ω_L=k v_Σ-ω`; the counter-propagating wave has `Ω_R=k v_Σ+ω`. At `v_Σ=c_f`:

`Ω_L=0`, `Ω_R=2ω`.

So a sheet moving at the filament wave speed freezes one travelling phase and doubles the sampled frequency of the opposite one. This is exact kinematics, not yet a physical chirality explanation.

## Run diagnostics

Demonstration parameters `A=k=ω=1`, `v_Σ=0.72` give `Ω=-0.28`, trace pitch `16.156762`. At `r=ℓ_b`, the tension+bending force is `1-2/e = 0.264241` of the pure asymptotic `1/r²` magnitude. Tilt fold threshold is exactly `μ=|tanψ|R/p=1`. At `v_Σ=c_f`, sampled frequencies are `0` and `2ω` for co-/counter-propagating modes.

## Verdict

- 🟢 guitar-string→helix trace: exact.
- 🟢 ᚼ/slicing commutator structure: exact to stated linearization, with an exact commuting special case.
- 🟢 angle factor and torque: exact for the chosen minimal quadratic interaction.
- 🟢 sheet-flex `1/r → 1/r²` far field: exact for the stated scalar tension model.
- 🟢 tilt fold criterion: exact for helix + plane.
- 🟡 absolute squash magnitude: constitutive constants missing.
- 🟡 Newtonian normalization: requires deriving `q∝m` rather than fitting it.
- 🟡 actual ST identity: requires a selected S1-supporting structure or full worldsheet constraints.
- ❌ do not call the scalar sheet model GR; it currently reaches only a Newtonian-like limit.

## Next cursor

Highest-value next test is the **mass/load map**: derive whether the SAT inertial quantity from coil geometry is automatically proportional to integrated sheet load `q`. If yes, the same geometry would tie inertia, Newtonian source strength, and reciprocal sheet flex with one coupling rather than three independent assumptions.