#!/usr/bin/env python3
"""Meridian Run 146: coupled filament-timesheet/string-bridge diagnostics."""
from pathlib import Path
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

OUT=Path(__file__).resolve().parent

# 1. Guitar string -> moving sheet helix
A=k=omega=1.0
v_sheet=0.72
Omega=k*v_sheet-omega
t=np.linspace(0,8*np.pi/abs(Omega),1800)
x=A*np.cos(Omega*t); y=A*np.sin(Omega*t); q=v_sheet*t
fig=plt.figure(figsize=(7.2,6.0)); ax=fig.add_subplot(111,projection="3d")
ax.plot(x,y,q)
ax.set_xlabel("transverse x"); ax.set_ylabel("transverse y"); ax.set_zlabel("timesheet propagation coordinate q")
ax.set_title("Moving-sheet trace of a straight transversely vibrating filament")
fig.tight_layout(); fig.savefig(OUT/"guitar_string_timesheet_trace.png",dpi=220); fig.savefig(OUT/"guitar_string_timesheet_trace.svg"); plt.close(fig)
trace_pitch=2*np.pi*v_sheet/abs(Omega)

# 2. Sheet flex
lb=1.0
r=np.logspace(-2,2,800); xv=r/lb
Fbar=(1-(1+xv)*np.exp(-xv))/xv**2
Fnewt=1/xv**2
ratio=Fbar/Fnewt
fig,ax=plt.subplots(figsize=(7.6,5.2))
ax.loglog(xv,Fbar,label="tension+bending sheet")
ax.loglog(xv,Fnewt,linestyle="--",label="pure 1/r² far-field law")
ax.axvline(1.0,linestyle=":",label="bending scale ℓ_b")
ax.set_xlabel("r / ℓ_b"); ax.set_ylabel("dimensionless force magnitude")
ax.set_title("Sheet-flex force: inverse-square far field with short-scale crossover"); ax.legend()
fig.tight_layout(); fig.savefig(OUT/"sheet_flex_inverse_square_crossover.png",dpi=220); fig.savefig(OUT/"sheet_flex_inverse_square_crossover.svg"); plt.close(fig)

# 3. Mean angle coupling
beta=np.linspace(0,np.deg2rad(89.5),500); psis=np.deg2rad([0,15,30,45,60,75])
fig,ax=plt.subplots(figsize=(7.6,5.2))
for psi in psis:
    favg=1-(np.cos(beta)**2*np.cos(psi)**2 + 0.5*np.sin(beta)**2*np.sin(psi)**2)
    ax.plot(np.degrees(beta),favg,label=f"sheet tilt ψ={np.degrees(psi):.0f}°")
ax.set_xlabel("helix tangent angle β to long axis"); ax.set_ylabel("mean angular-resistance factor ⟨sin²θ⟩")
ax.set_title("Orientation dependence of the minimal SAT angular coupling"); ax.legend()
fig.tight_layout(); fig.savefig(OUT/"helix_sheet_angle_coupling.png",dpi=220); fig.savefig(OUT/"helix_sheet_angle_coupling.svg"); plt.close(fig)

# 4. Tilt threshold / root count
R=1.0; p=0.45
phis=np.linspace(-6*np.pi,6*np.pi,8000)
cases=[0.5,1.0,1.5]
bvals=np.linspace(-5,5,301)
fig,ax=plt.subplots(figsize=(7.6,5.2))
for mu in cases:
    a=mu*p/R
    f=p*phis-a*R*np.cos(phis)
    counts=[]
    for b in bvals:
        g=f-b
        counts.append(np.count_nonzero(g[:-1]*g[1:]<0))
    ax.plot(bvals,counts,label=f"μ=|tanψ|R/p={mu:g}")
ax.set_xlabel("sheet offset b"); ax.set_ylabel("number of helix-sheet intersections in plotted window")
ax.set_title("Tilt threshold: single-valued trace versus fold/multiple intersections"); ax.legend()
fig.tight_layout(); fig.savefig(OUT/"tilted_sheet_intersection_multiplicity.png",dpi=220); fig.savefig(OUT/"tilted_sheet_intersection_multiplicity.svg"); plt.close(fig)

# 5. Chirality-selective sampling
cf=1.0; vr=np.linspace(0,1.5,500); omega0=cf*k
OmL=np.abs(k*vr-omega0); OmR=np.abs(k*vr+omega0)
fig,ax=plt.subplots(figsize=(7.6,5.2))
ax.plot(vr/cf,OmL/omega0,label="co-propagating sampled frequency")
ax.plot(vr/cf,OmR/omega0,label="counter-propagating sampled frequency")
ax.axvline(1.0,linestyle="--",label="v_sheet = c_f")
ax.set_xlabel("v_sheet / c_f"); ax.set_ylabel("|Ω_trace| / ω")
ax.set_title("Moving timesheet acts as a chirality-selective sampler"); ax.legend()
fig.tight_layout(); fig.savefig(OUT/"moving_sheet_chiral_sampling.png",dpi=220); fig.savefig(OUT/"moving_sheet_chiral_sampling.svg"); plt.close(fig)

summary=pd.DataFrame([
    {"quantity":"guitar_trace_Omega","value":Omega,"units":"1/time"},
    {"quantity":"guitar_trace_pitch","value":trace_pitch,"units":"q-units/turn"},
    {"quantity":"sheet_force_ratio_at_r_eq_lb","value":float(1-2/np.e),"units":"fraction of 1/r^2"},
    {"quantity":"tilt_uniqueness_threshold_mu","value":1.0,"units":"dimensionless"},
    {"quantity":"co_propagating_trace_frequency_at_v_eq_cf","value":0.0,"units":"omega"},
    {"quantity":"counter_propagating_trace_frequency_at_v_eq_cf","value":2.0,"units":"omega"},
])
summary.to_csv(OUT/"run146_numeric_summary.csv",index=False)
print(summary.to_string(index=False))
