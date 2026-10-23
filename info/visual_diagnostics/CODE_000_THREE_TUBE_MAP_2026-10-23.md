# CODE 000 | Three identifiable finite tubes | 2026-10-23

**Status:** SANDBOX / executed geometric diagnostic. Not a Kerr solution, QCD derivation, QED derivation, or established vacuum-fluid law.

**Intent.** Audit the diagram following Nathan's October 23 notebook image: THREE persistent red/green/blue strands, longitudinal **w** (fourth spatial axis), three separate circular cross-sections, and schematically induced medium vortices. Do not mistake a color-changing two-strand rendering for a three-strand braid. Kerr rings, ergosurfaces, horizons, and string vibration modes are visual annotations, not results of this toy parameterization.

**Imported mathematics:** smooth curves, Euclidean distances, tubular cross sections, fixed-phase 3-strand helix. These are standard geometric tools.

**Constructed mapping:** for strand i=0,1,2, let
```
theta_i(w) = 2*pi*(2.5)*w/10 + 2*pi*i/3
p_i(w) = (1.03*cos(theta_i), 1.03*sin(theta_i), w)
tube radius = 0.34
w in [0, 10]
```
Pairwise center separation at each common w: sqrt(3)*1.03 = **1.7840123318**. Minimum same-w surface clearance: **1.1040123318 > 0**. Independent color ID maintained for every w. Inspection executed by Python/NumPy/Matplotlib, image visually inspected within the initiating thread.

**What the calculation does not establish:** 4D disjointness across *different* w values, confinement, Kerr consistency, braid stability under dynamics, vortex production, Maxwell/QCD equivalence. The projected x-y-w geometry is a diagnostic view of a 4-spatial-coordinate model (the other spatial coordinate is suppressed). The external vortex icons are illustrative, not outputs of Navier–Stokes.

**Reproduction fragment** (NumPy):
```python
import numpy as np
R,a,H,turns=1.03,.34,10.,2.5
w=np.linspace(0,H,240)
P=np.array([np.stack([R*np.cos(2*np.pi*turns*w/H+2*np.pi*i/3),
                      R*np.sin(2*np.pi*turns*w/H+2*np.pi*i/3),
                      w],axis=-1) for i in range(3)])
for i in range(3):
  for j in range(i+1,3):
    assert np.min(np.linalg.norm(P[i,:,:2]-P[j,:,:2],axis=1))>2*a
print(np.sqrt(3)*R-2*a)
```

**Source lineage:** Nathan's hand-drawn three-intertwined-Kerr-worldtube + gravity well/time surface/Kelvin vortices/responsive medium notebook visual of 2026-10-23, followed by three corrected AI illustrative renders in same conversation. All proposed associations retain their speculative mapping status.

**Follow-up:** construct four-spatial embedding and surface sections with independently specified Kerr-sourced quantities; audit topology separately from rendered crossing appearance; if a medium PDE is prescribed, distinguish imposed circulation from computed circulation.
