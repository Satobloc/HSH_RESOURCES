#!/usr/bin/env python3
from pathlib import Path
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

OUT=Path(__file__).resolve().parent
p=.16
s=np.linspace(0,4*np.pi,1200)
radii=[.55,.10,.02]
rows=[]
fig=plt.figure(figsize=(7.5,6.2))
ax=fig.add_subplot(111,projection="3d")
for i,R in enumerate(radii):
    G=np.c_[R*np.cos(s)+1.4*(i-1),R*np.sin(s),p*s]
    ax.plot(*G.T,label=f"R={R:g}")
    den=R*R+p*p
    rows.append([R,p,R/den,p/den,np.arctan2(R,p),np.degrees(np.arctan2(R,p))])
ax.set_xlabel("x (display offset)"); ax.set_ylabel("y"); ax.set_zlabel("history/axis")
ax.set_title("Near-alignment is geometric, not a carrier-topology change"); ax.legend()
fig.tight_layout(); fig.savefig(OUT/"near_aligned_filament_family.png",dpi=220); plt.close(fig)
pd.DataFrame(rows,columns=["radius","pitch","curvature","torsion","angle_rad","angle_deg"]).to_csv(OUT/"near_aligned_filament_numeric.csv",index=False)

Rq,pq=.15,.03
sq=np.linspace(-.75*np.pi,.75*np.pi,600)
Q=np.c_[Rq*np.cos(sq),Rq*np.sin(sq),pq*sq]
den=Rq*Rq+pq*pq
qrow={"radius":Rq,"pitch":pq,"curvature":Rq/den,"torsion":pq/den,
      "arc_length":np.sqrt(den)*(sq[-1]-sq[0]),
      "endpoint_chord":np.linalg.norm(Q[-1]-Q[0]),"turns":(sq[-1]-sq[0])/(2*np.pi),
      "topological_label":"UNRESOLVED"}
pd.DataFrame([qrow]).to_csv(OUT/"bounded_high_curvature_numeric.csv",index=False)
fig=plt.figure(figsize=(7.2,6.0)); ax=fig.add_subplot(111,projection="3d")
ax.plot(*Q.T,label="open segment"); ax.scatter([Q[0,0],Q[-1,0]],[Q[0,1],Q[-1,1]],[Q[0,2],Q[-1,2]],label="fixed endpoints")
ax.set_title("Short high-curvature open filament with explicit endpoints"); ax.legend()
fig.tight_layout(); fig.savefig(OUT/"bounded_high_curvature_segment.png",dpi=220); plt.close(fig)

z=np.linspace(0,1,500); k=3; t0=.17; Om=1.9
phi=2*np.pi*k*z-Om*t0
C=np.c_[np.zeros_like(z),np.zeros_like(z),z]
D=np.c_[np.cos(phi),np.sin(phi),np.zeros_like(z)]
fig=plt.figure(figsize=(7.3,6.2)); ax=fig.add_subplot(111,projection="3d")
ax.plot(*C.T,label="carrier centerline")
for ii in np.linspace(0,len(z)-1,28,dtype=int):
    tip=C[ii]+.13*D[ii]
    ax.plot([0,tip[0]],[0,tip[1]],[C[ii,2],tip[2]])
ax.set_title("Phase field on a fixed carrier: centerline does not ripple"); ax.legend()
fig.tight_layout(); fig.savefig(OUT/"phase_field_on_fixed_carrier.png",dpi=220); plt.close(fig)
pd.DataFrame([{"k":k,"phase_advance_rad":phi[-1]-phi[0],
               "phase_advance_over_2pi":(phi[-1]-phi[0])/(2*np.pi),
               "max_centerline_displacement":np.max(np.linalg.norm(C[:,:2],axis=1)),
               "max_director_norm_error":np.max(np.abs(np.linalg.norm(D,axis=1)-1))}]).to_csv(OUT/"phase_field_numeric.csv",index=False)
