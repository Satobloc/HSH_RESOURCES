#!/usr/bin/env python3
"""Meridian Run 145 - reproducible recurrence + Particle Zoo geometry diagnostics."""
from pathlib import Path
import json
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

OUT = Path(__file__).resolve().parent
SEED = 260927
rng = np.random.default_rng(SEED)

# --- recurrence benchmark ---
omega = 1.1
gaps = np.array([0.10, 0.03, 0.01, 0.003], dtype=float)
dt = 0.025
times = np.arange(-2.0, 2.0 + 1e-12, dt)
noise_sigma = 1e-4
a_amp, b_amp = 1.2, 0.65
strides = np.arange(1, 31, dtype=int)
trials = 120

def exact_signal(nu):
    return np.column_stack([
        a_amp*np.cos(omega*times),
        a_amp*np.sin(omega*times),
        b_amp*np.cos(nu*times),
        b_amp*np.sin(nu*times),
    ])

def noisy_signal(nu):
    return exact_signal(nu) + rng.normal(scale=noise_sigma, size=(len(times), 4))

def palindromic_fit_gap(X, L):
    N = len(X) - 4*L
    if N < 8:
        return np.nan, np.nan, np.nan
    rows, rhs = [], []
    for n in range(N):
        for j in range(4):
            rows.append([X[n+3*L,j] + X[n+L,j], -X[n+2*L,j]])
            rhs.append(X[n+4*L,j] + X[n,j])
    A, b = np.asarray(rows), np.asarray(rhs)
    s1, s2 = np.linalg.lstsq(A, b, rcond=None)[0]
    roots = np.roots([1.0, -s1/2.0, (s2-2.0)/4.0])
    if np.max(np.abs(np.imag(roots))) > 1e-7:
        return np.nan, s1, s2
    q = np.clip(np.real(roots), -1.0, 1.0)
    rates = np.sort(np.arccos(q)/(L*dt))
    return abs(rates[1]-rates[0]), s1, s2

def exact_discriminant(gap, L):
    nu = omega-gap
    tau = L*dt
    return 4*np.sin((omega+nu)*tau/2.0)**2 * np.sin(gap*tau/2.0)**2

admissible = np.array([L for L in strides if len(times)-4*L >= 40], dtype=int)
scores = np.array([min(exact_discriminant(g, L) for g in gaps) for L in admissible])
L_star = int(admissible[np.argmax(scores)])

rows = []
for gap in gaps:
    nu = omega-gap
    for L in strides:
        errs = []
        for _ in range(trials):
            est, _, _ = palindromic_fit_gap(noisy_signal(nu), int(L))
            if np.isfinite(est):
                errs.append(abs(est-gap)/gap)
        rows.append({
            "gap": gap, "stride": int(L), "valid_trials": len(errs),
            "median_relative_error": float(np.median(errs)) if errs else np.nan,
            "p95_relative_error": float(np.quantile(errs, .95)) if errs else np.nan,
            "exact_discriminant": exact_discriminant(gap, int(L)),
        })
df = pd.DataFrame(rows)
df.to_csv(OUT/"recurrence_benchmark.csv", index=False)
df[df.stride==L_star].to_csv(OUT/"recurrence_selected_stride.csv", index=False)

fig, ax = plt.subplots(figsize=(8.4, 5.2))
for gap in gaps:
    sub = df[df.gap==gap]
    ax.plot(sub.stride, sub.median_relative_error, marker="o", markersize=3, label=f"Δω = {gap:g}")
ax.axvline(L_star, linestyle="--", label=f"answer-blind L* = {L_star}")
ax.set_yscale("log")
ax.set_xlabel("Sampling stride L")
ax.set_ylabel("Median relative gap error")
ax.set_title("Two-rate recurrence resolution versus sampling stride")
ax.legend()
fig.tight_layout()
fig.savefig(OUT/"recurrence_resolution_frontier.png", dpi=220)
fig.savefig(OUT/"recurrence_resolution_frontier.svg")
plt.close(fig)

fig, ax = plt.subplots(figsize=(8.4, 5.2))
for gap in gaps:
    ax.plot(strides, [exact_discriminant(gap,int(L)) for L in strides],
            marker="o", markersize=3, label=f"Δω = {gap:g}")
ax.axvline(L_star, linestyle="--", label=f"answer-blind L* = {L_star}")
ax.set_yscale("log")
ax.set_xlabel("Sampling stride L")
ax.set_ylabel("Exact cosine-root discriminant Δq")
ax.set_title("Exact lag-conditioned discriminant")
ax.legend()
fig.tight_layout()
fig.savefig(OUT/"recurrence_exact_discriminant.png", dpi=220)
fig.savefig(OUT/"recurrence_exact_discriminant.svg")
plt.close(fig)

# --- Particle Zoo representative geometry ---
s = np.linspace(0.0, 4*np.pi, 1600)
R, pitch = 0.55, 0.11

def helix_mode(n):
    return np.column_stack([R*np.cos(n*s), R*np.sin(n*s), pitch*s])

def helix_invariants(n):
    den = R*R*n*n + pitch*pitch
    return (R*n*n/den, pitch*n/den, np.sqrt(den)*(s[-1]-s[0]))

mode_rows = []
fig = plt.figure(figsize=(8.0, 6.3))
ax = fig.add_subplot(111, projection="3d")
for n in (1,2,3):
    G = helix_mode(n)
    Gv = G.copy()
    Gv[:,0] += 1.6*(n-2)  # display-only separation
    ax.plot(Gv[:,0], Gv[:,1], Gv[:,2], label=f"mode {n}")
    kappa, torsion, length = helix_invariants(n)
    mode_rows.append({"mode":n, "carrier_domain":"interval", "radius":R,
                      "pitch_parameter":pitch, "curvature":kappa,
                      "torsion":torsion, "arc_length":length})
ax.set_xlabel("x (display-offset)")
ax.set_ylabel("y")
ax.set_zlabel("history/axis")
ax.set_title("Same carrier topology, different harmonic geometry")
ax.legend()
fig.tight_layout()
fig.savefig(OUT/"zoo_same_topology_different_geometry.png", dpi=220)
fig.savefig(OUT/"zoo_same_topology_different_geometry.svg")
plt.close(fig)
pd.DataFrame(mode_rows).to_csv(OUT/"zoo_harmonic_geometry.csv", index=False)

z = np.linspace(0.0, 1.0, 1800)
Rb = 0.65
strands = []
for j in range(3):
    phi = 2*np.pi*z + 2*np.pi*j/3
    strands.append(np.column_stack([Rb*np.cos(phi), Rb*np.sin(phi), z]))

fig = plt.figure(figsize=(7.2, 6.2))
ax = fig.add_subplot(111, projection="3d")
for j, B in enumerate(strands):
    ax.plot(B[:,0], B[:,1], B[:,2], label=f"strand {j+1}")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("axial/history coordinate")
ax.set_title("Exact three-strand full-twist braid representative")
ax.legend()
fig.tight_layout()
fig.savefig(OUT/"zoo_three_strand_braid.png", dpi=220)
fig.savefig(OUT/"zoo_three_strand_braid.svg")
plt.close(fig)

pair_rows=[]
for i in range(3):
    for j in range(i+1,3):
        d=np.linalg.norm(strands[i]-strands[j],axis=1)
        pair_rows.append({"pair":f"{i+1}-{j+1}",
                          "min_distance":float(d.min()),
                          "max_distance":float(d.max()),
                          "mean_distance":float(d.mean())})
pd.DataFrame(pair_rows).to_csv(OUT/"zoo_braid_distances.csv", index=False)

manifest={"seed":SEED,
          "recurrence":{"omega":omega,"gaps":gaps.tolist(),"dt":dt,
                        "samples":len(times),"noise_sigma":noise_sigma,
                        "trials":trials,"answer_blind_stride":L_star},
          "zoo_geometry":{"harmonic_family":{"R":R,"pitch_parameter":pitch,"modes":[1,2,3]},
                          "braid":{"radius":Rb,"strands":3,"turns":1}}}
(OUT/"run_manifest.json").write_text(json.dumps(manifest,indent=2))
print("answer-blind stride", L_star)
print(df[df.stride==L_star][["gap","valid_trials","median_relative_error","p95_relative_error"]].to_string(index=False))
