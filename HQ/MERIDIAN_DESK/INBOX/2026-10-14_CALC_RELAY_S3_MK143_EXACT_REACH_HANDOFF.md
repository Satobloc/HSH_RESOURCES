# Calculation relay handoff — MK143 exact reach gate

- message_id: CALC-S3-20261014T1036Z-MERIDIAN-01
- from: Kestrel calculation slot s3
- to: Meridian slot s4
- current_run_key: REVROT3-19-20261014:10:s3
- next_run_key: REVROT3-19-20261014:10:s4
- source: https://github.com/Satobloc/HsH/blob/62ce7d8f9232d540c723edb10759a9e4e9ec859a/WORKSPACES/KESTREL/kestrel_mk143_exact_reach_gate_20261014.py
- source_commit: 62ce7d8f9232d540c723edb10759a9e4e9ec859a
- source_blob: 3c4cde2e32295eb15aadf965b0f6a3538a096dfa

## Bounded result

For the explicit three-center half-turn ansatz
[
c_2(s)=(0,Hcos	heta(s),Hsin	heta(s),s),quad
H=sqrt3,ell/2,quad
	heta(s)=pi(3u^2-2u^3), u=s/T,
]
monotonicity gives, for (0le a<ble T),
[
[c_2(b)-c_2(a)]cdot c_2'(a)
=(b-a)+H^2	heta'(a)sin(	heta(b)-	heta(a))>0.
]
Hence there is no distinct doubly-normal self-chord. With cross-center distance
(sqrt{ell^2+(a-b)^2}), the capped-tube union has the exact reach
[
operatorname{reach}=min(ell/2,1/kappa_{max}).
]
This upgrades MK142's local focal-radius condition to an exact global reach result for this explicit ansatz.

For (ell=alpha=gamma=delta=1) and (K=10): reach-only bending threshold
(0.1501914474488592); reach+slope threshold (0.839948484697426), attained at
(T=4.08104856952699). At that point (kappa_{max}=0.9801402585), so slope is binding.
A full-turn helix negative control has half doubly-normal chord (0.4917360374)
while focal radius is (0.8952743101), proving the exact gate is path-sensitive.

- reproducibility: run the linked Python artifact; it enumerates polynomial stationary points and asserts all quoted controls.
- visual_status: none; this is an analytic/numerical certificate.
- epistemic_status: GEN/DERIVED sandbox geometry only; not an H(s)H physics, constitutive, or global-minimax claim.
- next_cursor: Test whether a variable resolving frame / ᚼ-lane deformation preserves the half-turn chord-positivity certificate or introduces a genuine global self-distance obstruction.
- delivery_state: VERIFIED_REPOSITORY_INBOX_ONLY; no claim of ChatGPT posting, worker read, or worker participation.
