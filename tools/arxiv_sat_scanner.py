#!/usr/bin/env python3
"""arXiv structural scanner for SAT / H(s)H.

Retrieves recent arXiv metadata from selected categories, then scores titles and
abstracts locally for structural co-occurrence using a deliberately broad
SAT/H(s)H-to-standard-physics vocabulary.

Important:
  * A high structural score means "worth inspecting", not "supports SAT/H(s)H".
  * Controls are reported separately and do NOT reduce the structural score.
  * The scanner is intended for literature navigation and trend calibration.
  * Standard library only.

Examples:
  py tools/arxiv_sat_scanner.py --days 30 --include-seen
  py tools/arxiv_sat_scanner.py --days 7
  py tools/arxiv_sat_scanner.py --days 14 --min-score 12
  py tools/arxiv_sat_scanner.py --self-test
  py tools/arxiv_sat_scanner.py --list-vocabulary
"""
from __future__ import annotations

import argparse
import csv
import html
import json
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from collections import Counter, defaultdict
from dataclasses import asdict, dataclass, field
from datetime import datetime, timedelta, timezone
from pathlib import Path

API = "https://export.arxiv.org/api/query"
DELAY = 3.1
PAGE_SIZE = 500
MAX_FETCH = 5000
VERSION = "0.4"

# Broad enough to catch structural cousins without pulling all of arXiv.
CATEGORIES = [
    "gr-qc", "hep-th", "hep-ph", "hep-lat", "hep-ex", "quant-ph", "math-ph",
    "nucl-th", "nucl-ex",
    "astro-ph.CO", "astro-ph.HE", "astro-ph.GA", "astro-ph.SR", "astro-ph.IM",
    "cond-mat.stat-mech", "cond-mat.str-el", "cond-mat.mes-hall",
    "cond-mat.quant-gas", "cond-mat.supr-con", "cond-mat.soft",
    "nlin.PS", "nlin.CD",
    "physics.gen-ph", "physics.class-ph", "physics.optics", "physics.atom-ph",
    "physics.flu-dyn", "physics.plasm-ph", "physics.space-ph",
    "math.DG", "math.GT", "math.SG", "math.QA", "math.AT", "math.MP",
]

# feature: (sector, weight, alternatives)
# Each feature can score at most once per paper. Terms are intentionally
# redundant: the goal is recall first, followed by cross-sector specificity.
F = {
    # ------------------------------------------------------------------
    # WORLDLINE / WORLDTUBE / CURVE PRIMITIVES
    # ------------------------------------------------------------------
    "worldline": ("worldtube", 2.7, [
        "worldline", "world line", "spacetime trajectory", "relativistic trajectory",
        "particle trajectory in spacetime", "worldline formalism", "world-line formalism",
    ]),
    "worldtube": ("worldtube", 3.2, [
        "worldtube", "world tube", "finite-radius worldtube", "finite radius worldtube",
        "tubular worldtube", "world-tube", "world tube geometry",
    ]),
    "tubular_neighborhood": ("worldtube", 2.8, [
        "tubular neighborhood", "tubular neighbourhood", "tube around a curve",
        "thickened curve", "finite-core tube", "finite core tube", "ribbon neighborhood",
    ]),
    "filament_defect": ("worldtube", 1.6, [
        "filament", "filamentary", "line defect", "line-like defect", "linelike defect",
        "stringlike defect", "string-like defect", "one-dimensional defect", "1d defect",
    ]),
    "curve_congruence": ("worldtube", 2.0, [
        "congruence of curves", "worldline congruence", "worldline bundle",
        "family of worldlines", "curve ensemble", "worldline ensemble", "bundle of curves",
    ]),
    "extended_object": ("worldtube", 1.2, [
        "extended object", "stringlike degree of freedom", "string-like degree of freedom",
        "one-dimensional extended object", "finite-size particle", "finite size particle",
    ]),

    # ------------------------------------------------------------------
    # FRAMED CURVES / NORMAL BUNDLES / ELASTIC GEOMETRY
    # ------------------------------------------------------------------
    "framed_curve": ("curve_geometry", 2.6, [
        "framed curve", "curve framing", "moving frame", "frenet-serret",
        "frenet serret", "bishop frame", "parallel frame", "material frame",
    ]),
    "normal_bundle": ("curve_geometry", 3.0, [
        "normal bundle", "normal frame", "normal connection", "normal-bundle",
        "transverse bundle", "orthogonal bundle", "normal plane bundle",
    ]),
    "curve_curvature": ("curve_geometry", 2.1, [
        "worldline curvature", "curve curvature", "extrinsic curvature of a curve",
        "curvature vector", "bending energy", "curvature energy", "rigid particle",
        "extrinsic-curvature particle", "extrinsic curvature particle",
    ]),
    "curve_torsion": ("curve_geometry", 2.5, [
        "curve torsion", "frenet torsion", "geometric torsion", "curvature and torsion",
        "torsion of a curve", "torsion action", "torsional curve", "twist connection",
    ]),
    "elastic_curve": ("curve_geometry", 2.1, [
        "elastic curve", "elastica", "elastic rod", "kirchhoff rod", "cosserat rod",
        "rod theory", "bending stiffness", "string rigidity", "rigid string",
        "wormlike chain", "worm-like chain",
    ]),
    "boundary_modes": ("curve_geometry", 2.7, [
        "boundary mode", "boundary modes", "surface mode", "tube boundary mode",
        "boundary excitation", "edge mode", "edge excitation", "surface excitation",
    ]),
    "flex_mode": ("curve_geometry", 2.4, [
        "flexural mode", "flex mode", "bending mode", "transverse mode",
        "transverse oscillation", "normal mode of a curve", "curvature wave",
    ]),
    "twist_mode": ("curve_geometry", 2.5, [
        "twist mode", "torsional mode", "torsional excitation", "frame rotation mode",
        "chiral frame mode", "twist wave", "rotational mode",
    ]),
    "kink_phase_slip": ("curve_geometry", 2.6, [
        "phase slip", "phase-slip", "kink soliton", "sine-gordon kink",
        "sine gordon kink", "topological kink", "phase kink", "phase discontinuity",
    ]),
    "helix": ("curve_geometry", 2.7, [
        "helical worldline", "helical trajectory", "helical curve", "space curve helix",
        "superhelix", "superhelical", "nested helix", "iterated helix",
        "higher-dimensional helix", "higher dimensional helix", "screw symmetry",
    ]),
    "quasiperiodic_curve": ("curve_geometry", 1.9, [
        "quasi-periodic orbit", "quasiperiodic orbit", "multifrequency curve",
        "multi-frequency curve", "fourier-parametrized curve", "fourier parametrized curve",
        "nested modes", "mode hierarchy",
    ]),

    # ------------------------------------------------------------------
    # FOLIATION / PROJECTION / INTERSECTION / OBSERVABLES
    # ------------------------------------------------------------------
    "foliation": ("projection", 2.5, [
        "foliation", "foliation leaf", "observer foliation", "preferred foliation",
        "spacetime foliation", "cauchy foliation", "adm slicing", "spacetime slicing",
    ]),
    "hypersurface": ("projection", 2.1, [
        "cauchy hypersurface", "cauchy surface", "spacelike hypersurface",
        "timelike hypersurface", "resolving hypersurface", "hypersurface normal",
        "slice of spacetime", "spacetime slice",
    ]),
    "timelike_vector": ("projection", 2.0, [
        "unit timelike vector", "timelike vector field", "timelike congruence",
        "aether field", "æther field", "einstein-aether", "einstein-æther",
        "khronon", "clock field", "clock form",
    ]),
    "projection": ("projection", 1.8, [
        "geometric projection", "dimensional reduction", "projected observable",
        "projection-dependent observable", "projection dependent observable",
        "pullback to hypersurface", "spatial projection", "projection geometry",
    ]),
    "intersection": ("projection", 2.7, [
        "hypersurface intersection", "brane intersection", "intersecting branes",
        "defect intersection", "intersection of defects", "worldline intersection",
        "worldtube intersection", "intersection geometry",
    ]),
    "section_bundle": ("projection", 1.9, [
        "section of a bundle", "bundle section", "local section", "gauge section",
        "local trivialization", "local trivialisation", "pullback bundle",
    ]),
    "observer_access": ("projection", 1.4, [
        "observer-dependent", "observer dependent", "operational observable",
        "observer-accessible", "observer accessible", "relational observable",
    ]),
    "projection_loss": ("projection", 2.0, [
        "projection artifact", "projection artefact", "information loss under projection",
        "non-injective projection", "noninjective projection", "quotient map",
        "dimensional collapse", "rank collapse",
    ]),

    # ------------------------------------------------------------------
    # HOLONOMY / PHASE / CONNECTIONS
    # ------------------------------------------------------------------
    "holonomy": ("holonomy", 3.2, [
        "holonomy", "gauge holonomy", "relative holonomy", "holonomy group",
        "holonomy constraint", "nontrivial holonomy", "non-trivial holonomy",
    ]),
    "wilson_loop": ("holonomy", 2.7, [
        "wilson loop", "wilson line", "wilson-loop", "wilson-line",
        "path-ordered exponential", "path ordered exponential",
    ]),
    "parallel_transport": ("holonomy", 2.2, [
        "parallel transport", "parallel-transport", "connection transport",
        "transport around a loop", "closed-loop transport", "closed loop transport",
    ]),
    "geometric_phase": ("holonomy", 2.7, [
        "geometric phase", "berry phase", "hannay angle", "aharonov-bohm",
        "aharonov bohm", "pancharatnam phase", "wilczek-zee", "wilczek zee",
    ]),
    "monodromy": ("holonomy", 2.2, [
        "monodromy", "monodromy matrix", "monodromy group", "phase monodromy",
        "nontrivial monodromy", "non-trivial monodromy",
    ]),
    "compact_phase": ("holonomy", 2.7, [
        "compact phase", "compact scalar", "angular field", "periodic scalar",
        "periodic phase", "phase modulus", "compact boson", "circle-valued field",
        "circle valued field",
    ]),
    "phase_locking": ("holonomy", 2.2, [
        "phase locking", "phase-locking", "phase locked", "phase-locked",
        "phase synchronization", "phase synchronisation", "phase closure",
    ]),
    "bohr_sommerfeld": ("holonomy", 2.4, [
        "bohr-sommerfeld", "bohr sommerfeld", "periodic boundary condition",
        "periodic boundary conditions", "closure quantization", "closure quantisation",
    ]),

    # ------------------------------------------------------------------
    # TOPOLOGY / LINKING / BRAIDING / DEFECTS
    # ------------------------------------------------------------------
    "winding": ("topology", 2.1, [
        "winding number", "winding sector", "topological winding", "winding mode",
        "winding invariant", "integer winding",
    ]),
    "linking": ("topology", 2.5, [
        "linking number", "topological linking", "link invariant", "linked loops",
        "linking integral", "gauss linking", "linking topology",
    ]),
    "braid": ("topology", 3.0, [
        "braid group", "braiding", "braided", "braid statistics", "braid topology",
        "braid representation", "anyon braid", "braid relation",
    ]),
    "knot": ("topology", 2.9, [
        "knot theory", "knotted soliton", "knotted field", "knot invariant",
        "knot topology", "knot class", "topological knot",
    ]),
    "hopf": ("topology", 3.0, [
        "hopf link", "hopfion", "hopf invariant", "hopf charge", "hopf map",
        "hopf fibration", "hopf soliton", "hopf texture",
    ]),
    "borromean": ("topology", 3.3, [
        "borromean", "borromean rings", "borromean link", "brunnian",
        "brunnian link", "brunnian topology", "three-component link",
    ]),
    "torus_knot": ("topology", 2.7, [
        "torus knot", "toroidal knot", "torus-knot", "knot on a torus",
        "toroidal winding", "toroidal braid",
    ]),
    "topological_defect": ("topology", 2.3, [
        "topological defect", "line defect", "surface defect", "codimension defect",
        "domain wall", "vortex defect", "defect network", "topological obstruction",
    ]),
    "topological_soliton": ("topology", 2.5, [
        "topological soliton", "skyrmion", "hopfion", "vortex soliton",
        "solitonic defect", "topological texture", "soliton topology",
    ]),
    "homotopy": ("topology", 2.0, [
        "homotopy class", "homotopy invariant", "homotopy group", "homotopic",
        "homotopy obstruction", "topological sector",
    ]),
    "superselection": ("topology", 1.7, [
        "superselection sector", "superselection rule", "topological sector",
        "sector decomposition", "topological charge sector",
    ]),
    "nonpenetration": ("topology", 2.0, [
        "non-penetration", "nonpenetration", "self-avoidance", "self avoidance",
        "excluded volume", "topological exclusion", "impenetrability constraint",
    ]),

    # ------------------------------------------------------------------
    # GAUGE / BUNDLE / GENERALIZED SYMMETRY / CONSTRAINTS
    # ------------------------------------------------------------------
    "fiber_bundle": ("gauge", 2.2, [
        "fiber bundle", "fibre bundle", "principal bundle", "vector bundle",
        "associated bundle", "bundle connection", "bundle geometry",
    ]),
    "gauge_connection": ("gauge", 2.3, [
        "gauge connection", "connection one-form", "connection 1-form",
        "covariant derivative", "gauge potential as connection", "spin connection",
    ]),
    "cartan_geometry": ("gauge", 2.4, [
        "cartan geometry", "cartan connection", "einstein-cartan", "einstein cartan",
        "riemann-cartan", "riemann cartan", "poincare gauge", "poincaré gauge",
    ]),
    "discrete_symmetry": ("gauge", 1.9, [
        "z3 symmetry", "z_3 symmetry", "z(3) symmetry", "triality",
        "discrete gauge symmetry", "center symmetry", "centre symmetry",
        "discrete charge",
    ]),
    "higher_form_symmetry": ("gauge", 2.7, [
        "higher-form symmetry", "higher form symmetry", "p-form symmetry",
        "p form symmetry", "generalized global symmetry", "generalised global symmetry",
        "one-form symmetry", "1-form symmetry",
    ]),
    "noninvertible_symmetry": ("gauge", 2.8, [
        "non-invertible symmetry", "noninvertible symmetry", "categorical symmetry",
        "fusion category symmetry", "topological symmetry defect", "symmetry defect",
    ]),
    "anomaly_inflow": ("gauge", 2.5, [
        "anomaly inflow", "anomaly matching", "'t hooft anomaly", "t hooft anomaly",
        "defect anomaly", "anomaly cancellation", "anomaly obstruction",
    ]),
    "brst_constraints": ("gauge", 1.9, [
        "brst quantization", "brst quantisation", "brst charge", "dirac-bergmann",
        "dirac bergmann", "dirac bracket", "constraint closure", "second-class constraint",
        "second class constraint",
    ]),
    "topological_selection": ("gauge", 2.4, [
        "topological selection rule", "topological constraint", "selection rule from topology",
        "topological obstruction", "fusion rule", "topological fusion rule",
    ]),

    # ------------------------------------------------------------------
    # EMERGENT METRIC / GRAVITY / CONTINUUM KINEMATICS
    # ------------------------------------------------------------------
    "emergent_metric": ("emergence", 3.4, [
        "emergent metric", "metric emergence", "induced metric", "effective metric",
        "composite metric", "coarse-grained metric", "coarse grained metric",
        "metric from correlations", "metric from correlators", "metric reconstruction",
    ]),
    "emergent_spacetime": ("emergence", 3.0, [
        "emergent spacetime", "spacetime emergence", "emergent geometry",
        "pregeometric", "pre-geometric", "pregeometry", "pre-geometry",
        "geometry from microscopic", "spacetime from microscopic",
    ]),
    "emergent_gravity": ("emergence", 2.8, [
        "emergent gravity", "induced gravity", "entropic gravity", "analogue gravity",
        "analog gravity", "effective gravity", "gravity from microstructure",
    ]),
    "tangent_correlator": ("emergence", 3.0, [
        "tangent correlator", "tangent correlation", "tangent covariance",
        "metric from tangent", "inverse metric from correlation", "co-metric",
        "cometric", "ensemble metric",
    ]),
    "strain_shear_vorticity": ("continuum", 2.2, [
        "strain tensor", "shear tensor", "vorticity tensor", "expansion tensor",
        "expansion shear vorticity", "kinematic decomposition", "strain scalar",
        "shear scalar", "vorticity scalar",
    ]),
    "elastic_spacetime": ("continuum", 2.3, [
        "elastic spacetime", "spacetime elasticity", "metric elasticity",
        "elastic gravity", "elastic medium gravity", "vector-tensor gravity",
        "vector tensor gravity",
    ]),
    "geodesic_deviation": ("continuum", 1.8, [
        "geodesic deviation", "jacobi field", "congruence deviation",
        "raychaudhuri equation", "raychaudhuri", "geodesic congruence",
    ]),
    "frame_dragging": ("continuum", 1.6, [
        "frame dragging", "frame-dragging", "gravitomagnetic", "gravitomagnetism",
        "lense-thirring", "lense thirring",
    ]),
    "preferred_frame_gravity": ("continuum", 2.1, [
        "einstein-aether", "einstein-æther", "horava-lifshitz", "hořava-lifshitz",
        "preferred-frame gravity", "preferred frame gravity", "preferred foliation gravity",
    ]),
    "signature_emergence": ("emergence", 2.4, [
        "signature change", "signature-change", "emergent lorentzian",
        "lorentzian emergence", "euclidean to lorentzian", "euclidean-to-lorentzian",
        "induced lorentzian metric",
    ]),

    # ------------------------------------------------------------------
    # QUANTIZATION / PARTICLE GEOMETRY / CONFINEMENT
    # ------------------------------------------------------------------
    "geometric_quantization": ("quantization", 2.6, [
        "geometric quantization", "geometric quantisation", "topological quantization",
        "topological quantisation", "holonomy quantization", "holonomy quantisation",
        "quantization from topology", "quantisation from topology",
    ]),
    "collective_mode_boson": ("particle", 1.8, [
        "collective mode", "collective excitation", "normal mode", "emergent boson",
        "bosonic collective mode", "gauge excitation", "quasiparticle mode",
    ]),
    "geometric_mass": ("particle", 2.2, [
        "geometric mass", "mass from geometry", "topological mass", "mass from topology",
        "projection-induced mass", "projection induced mass", "orientation-dependent mass",
        "orientation dependent mass", "emergent inertial mass",
    ]),
    "misalignment_mass": ("particle", 2.6, [
        "misalignment angle", "angular misalignment", "mass from misalignment",
        "inertial response from misalignment", "orientation misalignment",
        "projection resistance", "orientation-dependent inertia",
    ]),
    "chirality": ("particle", 2.0, [
        "geometric chirality", "chirality", "handedness", "chiral asymmetry",
        "parity asymmetry", "parity violation", "chiral geometry",
    ]),
    "spin_geometry": ("particle", 2.0, [
        "spin geometry", "spin from geometry", "geometric spin", "spin connection",
        "spinor phase", "frame rotation", "zitterbewegung", "zittbewegung",
    ]),
    "clifford_spinor": ("particle", 2.2, [
        "clifford algebra", "dirac spinor", "spinor geometry", "geometric algebra",
        "gamma matrices", "clifford bundle", "spin structure",
    ]),
    "confinement": ("particle", 2.6, [
        "color confinement", "colour confinement", "topological confinement",
        "confining flux tube", "flux-tube confinement", "flux tube confinement",
        "center vortex", "centre vortex", "y-string", "y string",
    ]),
    "flux_tube": ("particle", 2.2, [
        "flux tube", "flux-tube", "string tension", "center flux", "centre flux",
        "vortex line", "vortex tube",
    ]),
    "particle_topology": ("particle", 2.4, [
        "topological particle model", "particle as topology", "particle topology",
        "topological model of particles", "topological particle", "topological preon",
        "braid model of particles",
    ]),
    "neutrino_photon": ("particle", 2.2, [
        "neutrino-photon", "neutrino photon", "photon-neutrino", "photon neutrino",
        "radiative neutrino", "neutrino electromagnetic", "neutrino-photon coupling",
    ]),
    "dark_projection": ("particle", 2.0, [
        "dark state", "sterile state", "decoupled state", "dark sector projection",
        "projection into dark sector", "hidden-sector projection", "hidden sector projection",
        "geometric dark matter",
    ]),

    # ------------------------------------------------------------------
    # TORUS / HOPF / SPHERE / SHELL / 4D GEOMETRY
    # ------------------------------------------------------------------
    "toroidal_flow": ("global_geometry", 2.3, [
        "toroidal flow", "torus flow", "toroidal phase space", "flow on a torus",
        "torus dynamics", "toroidal dynamics", "invariant torus",
    ]),
    "contact_symplectic": ("global_geometry", 1.9, [
        "contact geometry", "symplectic geometry", "contact structure",
        "reeb flow", "hamiltonian flow on torus", "contact dynamics",
    ]),
    "s3_geometry": ("global_geometry", 2.2, [
        "3-sphere", "three-sphere", "s^3 geometry", "s3 geometry",
        "hypersphere", "hyperspherical geometry", "hyperspherical coordinates",
        "closed frw", "closed friedmann",
    ]),
    "embedded_torus": ("global_geometry", 2.3, [
        "embedded torus", "torus embedding", "toroidal embedding",
        "embedded 3-torus", "embedded three-torus", "embedded t^3",
        "toroidal hypersurface", "torus hypersurface",
    ]),
    "so4_geometry": ("global_geometry", 2.2, [
        "so(4)", "so(4) rotation", "four-dimensional rotation", "4d rotation",
        "rotation in four dimensions", "rotation in 4d", "quaternionic rotation",
    ]),
    "regular_4d_polytope": ("global_geometry", 1.8, [
        "24-cell", "24 cell", "d4 lattice", "d_4 lattice", "f4 root system",
        "f_4 root system", "regular 4-polytope", "regular four-polytope",
        "four-dimensional polytope",
    ]),
    "finsler_indicatrix": ("global_geometry", 1.8, [
        "finsler indicatrix", "finsler geometry", "randers metric",
        "unit tangent sphere", "indicatrix geometry", "anisotropic norm",
    ]),

    # ------------------------------------------------------------------
    # CAUSALITY / WORMHOLES / ENTANGLEMENT / HOLOGRAPHY
    # ------------------------------------------------------------------
    "causal_geometry": ("causality", 1.9, [
        "causal structure", "causal geometry", "light cone", "light-cone structure",
        "null propagation", "null congruence", "causal front", "causal network",
    ]),
    "causal_diamond": ("causality", 2.0, [
        "causal diamond", "causal diamonds", "diamond region", "causal interval",
        "alexandrov interval", "causal domain",
    ]),
    "wormhole": ("causality", 2.6, [
        "einstein-rosen", "einstein rosen", "er bridge", "wormhole throat",
        "wormhole geometry", "traversable wormhole", "nontraversable wormhole",
        "non-traversable wormhole",
    ]),
    "entanglement_geometry": ("causality", 2.3, [
        "entanglement geometry", "geometry from entanglement", "spacetime from entanglement",
        "entanglement builds geometry", "entanglement and geometry",
        "entanglement-induced geometry", "entanglement induced geometry",
    ]),
    "entanglement_wedge": ("causality", 1.9, [
        "entanglement wedge", "bulk reconstruction", "holographic reconstruction",
        "causal wedge", "subregion duality",
    ]),
    "vacuum_entanglement": ("causality", 1.5, [
        "vacuum entanglement", "entanglement harvesting", "squeezed vacuum",
        "vacuum correlations", "vacuum resource",
    ]),
    "retrocausal_boundary": ("causality", 1.8, [
        "retrocausal", "two-boundary", "two boundary", "advanced-retarded",
        "advanced retarded", "two-state vector", "transactional interpretation",
    ]),

    # ------------------------------------------------------------------
    # SCALE / RG / EFFECTIVE-ACTION LANGUAGE
    # ------------------------------------------------------------------
    "coarse_graining": ("scale", 1.5, [
        "coarse-graining", "coarse graining", "coarse-grained", "coarse grained",
        "multiscale", "multi-scale", "scale hierarchy", "hierarchical modes",
    ]),
    "rg_flow": ("scale", 1.3, [
        "renormalization group", "renormalisation group", "rg flow", "beta function",
        "fixed point", "infrared fixed point", "ultraviolet fixed point",
    ]),
    "effective_action_geometry": ("scale", 1.9, [
        "geometric effective action", "effective action for curves",
        "worldline effective action", "defect effective action", "brane effective action",
        "extrinsic curvature action", "rigidity action",
    ]),
    "scale_rotation": ("scale", 2.0, [
        "scale-rotation", "scale rotation", "coupled scale and rotation",
        "radial scale factor and rotation", "rotation-scale dynamics",
        "scale factor dynamics",
    ]),
    "self_similarity": ("scale", 1.5, [
        "self-similar", "self similar", "scale invariant geometry",
        "scale-invariant geometry", "recursive geometry", "nested hierarchy",
    ]),

    # ------------------------------------------------------------------
    # COSMOLOGY / PHENOMENOLOGY / RESIDUALS
    # ------------------------------------------------------------------
    "strain_cosmology": ("phenomenology", 2.0, [
        "shear-driven expansion", "strain-driven expansion", "anisotropic-stress-driven",
        "anisotropic stress driven", "geometric inflation", "effective friedmann equation",
    ]),
    "birefringence_phase": ("phenomenology", 1.8, [
        "cosmic birefringence", "polarization rotation", "polarisation rotation",
        "achromatic phase shift", "non-dispersive phase shift", "nondispersive phase shift",
    ]),
    "precision_clock": ("phenomenology", 1.5, [
        "clock anisotropy", "clock drift", "orientation-dependent clock",
        "orientation dependent clock", "precision clock test", "lorentz violation clock",
    ]),
    "interferometry_phase": ("phenomenology", 1.5, [
        "atom interferometer", "atom interferometry", "mach-zehnder",
        "mach zehnder", "interferometric phase shift", "precision interferometry",
    ]),
    "gw_residual": ("phenomenology", 1.5, [
        "gravitational wave echo", "gravitational-wave echo", "gw echo",
        "phase residual", "waveform residual", "ringdown residual", "post-merger residual",
        "post merger residual",
    ]),
    "anomalous_trajectory": ("phenomenology", 1.4, [
        "anomalous acceleration", "non-gravitational acceleration",
        "non gravitational acceleration", "trajectory anomaly", "orbital residual",
        "astrometric residual",
    ]),
}

# Structural combinations that matter more than isolated vocabulary.
# (label, bonus, AND-groups of OR-feature names)
BUNDLES = [
    ("worldtube_framed_geometry", 6.0, [
        ("worldtube", "tubular_neighborhood"), ("framed_curve", "normal_bundle"),
        ("curve_curvature", "curve_torsion", "elastic_curve"),
    ]),
    ("worldline_projection_geometry", 5.0, [
        ("worldline", "worldtube"), ("foliation", "hypersurface"),
        ("projection", "intersection"),
    ]),
    ("normal_bundle_mode_system", 5.5, [
        ("normal_bundle",), ("flex_mode", "twist_mode", "kink_phase_slip"),
        ("framed_curve", "curve_curvature", "curve_torsion"),
    ]),
    ("holonomy_quantization", 5.5, [
        ("holonomy", "wilson_loop", "parallel_transport"),
        ("geometric_phase", "compact_phase", "phase_locking"),
        ("geometric_quantization", "bohr_sommerfeld"),
    ]),
    ("holonomy_topology", 4.5, [
        ("holonomy", "wilson_loop"), ("winding", "linking", "braid", "knot", "hopf"),
    ]),
    ("braided_particle_geometry", 6.0, [
        ("braid", "linking", "knot", "hopf", "borromean"),
        ("chirality", "confinement", "geometric_mass", "particle_topology"),
    ]),
    ("topological_confinement", 5.0, [
        ("confinement", "flux_tube"), ("braid", "linking", "topological_defect", "winding"),
    ]),
    ("emergent_metric_from_structure", 6.5, [
        ("emergent_metric",), ("tangent_correlator", "strain_shear_vorticity", "timelike_vector"),
        ("coarse_graining", "curve_congruence", "fiber_bundle"),
    ]),
    ("emergent_spacetime_topology", 5.5, [
        ("emergent_spacetime", "emergent_gravity"),
        ("holonomy", "topological_defect", "braid", "entanglement_geometry"),
    ]),
    ("defect_generalized_symmetry", 5.0, [
        ("topological_defect",), ("higher_form_symmetry", "noninvertible_symmetry"),
        ("anomaly_inflow", "topological_selection"),
    ]),
    ("gauge_holonomy_bundle", 4.5, [
        ("fiber_bundle", "gauge_connection", "cartan_geometry"),
        ("holonomy", "wilson_loop", "parallel_transport"),
    ]),
    ("hyperhelix_projection", 6.0, [
        ("helix", "quasiperiodic_curve"), ("worldline", "framed_curve"),
        ("curve_torsion", "curve_curvature"), ("foliation", "projection"),
    ]),
    ("particle_as_intersection", 5.0, [
        ("intersection",), ("foliation", "hypersurface"),
        ("worldline", "worldtube", "filament_defect"),
    ]),
    ("torus_holonomy_flow", 5.0, [
        ("toroidal_flow", "embedded_torus", "torus_knot"),
        ("holonomy", "geometric_phase", "winding"),
    ]),
    ("hopf_torus_particle", 5.0, [
        ("hopf",), ("toroidal_flow", "embedded_torus", "contact_symplectic"),
        ("particle_topology", "braid", "linking"),
    ]),
    ("s3_so4_solver_geometry", 4.5, [
        ("s3_geometry",), ("so4_geometry", "scale_rotation"),
    ]),
    ("wormhole_worldtube_geometry", 4.5, [
        ("wormhole",), ("worldline", "worldtube", "filament_defect", "causal_geometry"),
    ]),
    ("causal_entanglement_geometry", 4.5, [
        ("causal_geometry", "causal_diamond"), ("entanglement_geometry", "entanglement_wedge"),
    ]),
    ("geometric_mass_chirality", 4.0, [
        ("geometric_mass", "misalignment_mass"), ("chirality", "spin_geometry", "clifford_spinor"),
    ]),
    ("projection_dark_sector", 3.5, [
        ("projection", "intersection"), ("dark_projection",),
    ]),
    ("constraint_topology", 3.5, [
        ("brst_constraints", "topological_selection"), ("holonomy", "topological_defect", "discrete_symmetry"),
    ]),
    ("scale_recursive_geometry", 3.5, [
        ("coarse_graining", "self_similarity"), ("helix", "curve_congruence", "toroidal_flow"),
    ]),
]

# ----------------------------------------------------------------------
# CONTROLS
# ----------------------------------------------------------------------
# Controls are NOT "anti-H(s)H" terms. They estimate background language and
# false-positive pressure. They are recorded separately and never subtracted.
CONTROL_F = {
    # Generic theoretical-physics vocabulary: expected almost everywhere.
    "ctl_generic_eft": ("generic_physics", 1.0, [
        "effective field theory", "eft", "effective theory", "low-energy effective",
        "low energy effective",
    ]),
    "ctl_generic_action": ("generic_physics", 1.0, [
        "lagrangian", "hamiltonian", "action principle", "equations of motion",
        "variational principle",
    ]),
    "ctl_generic_symmetry": ("generic_physics", 1.0, [
        "symmetry breaking", "spontaneous symmetry breaking", "continuous symmetry",
        "global symmetry", "local symmetry",
    ]),
    "ctl_generic_perturbation": ("generic_physics", 1.0, [
        "perturbation theory", "perturbative", "loop correction", "one-loop", "two-loop",
    ]),
    "ctl_generic_numerics": ("generic_physics", 1.0, [
        "numerical simulation", "numerical analysis", "monte carlo", "finite element",
        "finite difference", "numerically solve",
    ]),
    "ctl_generic_statistics": ("generic_physics", 1.0, [
        "statistical significance", "bayesian inference", "likelihood analysis",
        "parameter estimation", "confidence interval",
    ]),

    # Neighboring topics that can make a paper sound relevant without matching
    # the actual structural grammar.
    "ctl_neighbor_quantum_gravity": ("neighbor_topic", 1.0, [
        "quantum gravity", "loop quantum gravity", "spin foam", "spin network",
        "causal set", "causal dynamical triangulation",
    ]),
    "ctl_neighbor_string": ("neighbor_topic", 1.0, [
        "string theory", "superstring", "string compactification", "d-brane", "d brane",
        "ads/cft", "gauge/gravity duality",
    ]),
    "ctl_neighbor_black_hole": ("neighbor_topic", 1.0, [
        "black hole", "black-hole", "event horizon", "hawking radiation",
        "black hole entropy", "ringdown",
    ]),
    "ctl_neighbor_dark": ("neighbor_topic", 1.0, [
        "dark matter", "dark energy", "dark photon", "hidden sector", "axion",
        "weakly interacting massive",
    ]),
    "ctl_neighbor_neutrino": ("neighbor_topic", 1.0, [
        "neutrino oscillation", "neutrino mass", "neutrino mixing", "pmns",
        "sterile neutrino", "leptonic cp",
    ]),
    "ctl_neighbor_standard_model": ("neighbor_topic", 1.0, [
        "standard model", "electroweak", "higgs boson", "qcd", "yang-mills",
        "yang mills", "supersymmetry",
    ]),
    "ctl_neighbor_cosmology": ("neighbor_topic", 1.0, [
        "inflation", "hubble tension", "cosmological constant", "large scale structure",
        "large-scale structure", "cmb", "baryon acoustic oscillation",
    ]),

    # Orthogonal physics controls: same broad arXiv neighborhoods, different
    # structural content. Useful for estimating topical leakage.
    "ctl_orthogonal_superconductivity": ("orthogonal_physics", 1.0, [
        "superconductivity", "superconductor", "cooper pair", "josephson junction",
        "superconducting gap",
    ]),
    "ctl_orthogonal_magnetism": ("orthogonal_physics", 1.0, [
        "ferromagnet", "antiferromagnet", "magnetic ordering", "magnon",
        "spin glass",
    ]),
    "ctl_orthogonal_materials": ("orthogonal_physics", 1.0, [
        "graphene", "moire material", "moiré material", "two-dimensional material",
        "2d material", "band structure", "electronic structure",
    ]),
    "ctl_orthogonal_plasma": ("orthogonal_physics", 1.0, [
        "plasma turbulence", "magnetohydrodynamic", "magnetohydrodynamics",
        "tokamak", "solar wind", "magnetic reconnection",
    ]),
    "ctl_orthogonal_fluid": ("orthogonal_physics", 1.0, [
        "fluid turbulence", "navier-stokes", "navier stokes", "reynolds number",
        "boundary layer", "fluid flow",
    ]),
    "ctl_orthogonal_nuclear": ("orthogonal_physics", 1.0, [
        "nuclear shell model", "nuclear structure", "nuclear reaction",
        "neutron-rich nuclei", "neutron rich nuclei", "fission",
    ]),
    "ctl_orthogonal_atomic": ("orthogonal_physics", 1.0, [
        "atomic spectroscopy", "atomic transition", "rydberg atom", "cold atom",
        "ultracold atom", "optical lattice",
    ]),

    # Broad non-physics STEM language should almost never dominate the selected
    # categories; if it does, category selection or vocabulary is drifting.
    "ctl_nonphysics_ml": ("nonphysics_stem", 1.0, [
        "machine learning", "neural network", "deep learning", "transformer model",
        "graph neural network",
    ]),
    "ctl_nonphysics_bio": ("nonphysics_stem", 1.0, [
        "protein folding", "gene expression", "cell signaling", "cell signalling",
        "genome", "biomolecule",
    ]),
    "ctl_nonphysics_chem": ("nonphysics_stem", 1.0, [
        "catalyst", "catalysis", "electrochemistry", "battery material",
        "chemical reaction network",
    ]),
}

ATOM = "{http://www.w3.org/2005/Atom}"
ARXIV = "{http://arxiv.org/schemas/atom}"
OS = "{http://a9.com/-/spec/opensearch/1.1/}"


@dataclass
class Paper:
    arxiv_id: str
    title: str
    authors: list[str]
    abstract: str
    published: str
    updated: str
    primary_category: str
    categories: list[str]
    abs_url: str
    pdf_url: str
    doi: str = ""
    journal_ref: str = ""

    score: float = 0.0
    tier: str = "low"
    sectors: list[str] = field(default_factory=list)
    features: list[str] = field(default_factory=list)
    terms: list[str] = field(default_factory=list)
    bundles: list[str] = field(default_factory=list)

    control_score: float = 0.0
    control_families: list[str] = field(default_factory=list)
    control_features: list[str] = field(default_factory=list)
    control_terms: list[str] = field(default_factory=list)
    contrast: float = 0.0

    new_or_updated: bool = True


def norm(s: str) -> str:
    s = html.unescape(s or "").lower()
    s = s.replace("–", "-").replace("—", "-").replace("−", "-")
    s = s.replace("’", "'").replace("“", '"').replace("”", '"')
    return re.sub(r"\s+", " ", s).strip()


def has(term: str, text: str) -> bool:
    t = norm(term)
    if not t:
        return False
    # Phrases and punctuation-heavy scientific tokens use substring matching.
    if any(ch in t for ch in " -_^()/") or " " in t:
        return t in text
    return bool(re.search(rf"(?<![a-z0-9]){re.escape(t)}(?![a-z0-9])", text))


def first_hit(terms: list[str], title: str, abstract: str):
    hit = next((x for x in terms if has(x, title)), None)
    if hit is not None:
        return hit, "title"
    hit = next((x for x in terms if has(x, abstract)), None)
    if hit is not None:
        return hit, "abstract"
    return None


def score_paper(p: Paper) -> Paper:
    ti, ab = norm(p.title), norm(p.abstract)
    found = {}
    sectors = set()
    total = 0.0

    # Positive structural features.
    for name, (sector, weight, terms) in F.items():
        hit = first_hit(terms, ti, ab)
        if hit is None:
            continue
        term, where = hit
        multiplier = 1.65 if where == "title" else 1.0
        phrase_bonus = 0.35 if len(norm(term).split()) > 1 else 0.0
        total += weight * multiplier + phrase_bonus
        found[name] = (term, where)
        sectors.add(sector)

    # Cross-sector bundles.
    p.bundles = []
    for label, bonus, groups in BUNDLES:
        if all(any(feature in found for feature in group) for group in groups):
            total += bonus
            p.bundles.append(label)

    # Reward independent structural sectors: orthogonal convergence matters.
    d = len(sectors)
    if d >= 8:
        total += 10.0
    elif d == 7:
        total += 8.5
    elif d == 6:
        total += 7.0
    elif d == 5:
        total += 5.5
    elif d == 4:
        total += 4.0
    elif d == 3:
        total += 2.5
    elif d == 2:
        total += 1.0

    # Very generic isolated hits should not become "interesting" by themselves.
    generic_positive = {"coarse_graining", "rg_flow", "collective_mode_boson"}
    if found and set(found) <= generic_positive:
        total *= 0.35

    p.score = round(total, 2)
    p.sectors = sorted(sectors)
    p.features = sorted(found)
    p.terms = [f"{k}:{v[0]} ({v[1]})" for k, v in sorted(found.items())]

    # Separate controls. These never alter p.score.
    cfound = {}
    cfamilies = set()
    ctotal = 0.0
    for name, (family, weight, terms) in CONTROL_F.items():
        hit = first_hit(terms, ti, ab)
        if hit is None:
            continue
        term, where = hit
        ctotal += weight * (1.35 if where == "title" else 1.0)
        cfound[name] = (term, where)
        cfamilies.add(family)

    p.control_score = round(ctotal, 2)
    p.control_families = sorted(cfamilies)
    p.control_features = sorted(cfound)
    p.control_terms = [f"{k}:{v[0]} ({v[1]})" for k, v in sorted(cfound.items())]

    # Contrast is a calibration field only. The main ranking remains score.
    p.contrast = round(p.score - 0.35 * p.control_score, 2)

    p.tier = (
        "very-high" if p.score >= 30
        else "high" if p.score >= 20
        else "medium" if p.score >= 13
        else "watch" if p.score >= 8
        else "low"
    )
    return p


def txt(e, tag):
    n = e.find(tag)
    return re.sub(r"\s+", " ", n.text).strip() if n is not None and n.text else ""


def parse_feed(data: bytes):
    root = ET.fromstring(data)
    total = int(txt(root, OS + "totalResults") or 0)
    out = []
    for e in root.findall(ATOM + "entry"):
        eid = txt(e, ATOM + "id")
        aid = eid.rstrip("/").split("/")[-1]
        authors = [txt(a, ATOM + "name") for a in e.findall(ATOM + "author")]
        cats = [c.attrib.get("term", "") for c in e.findall(ATOM + "category") if c.attrib.get("term")]
        pn = e.find(ARXIV + "primary_category")
        primary = pn.attrib.get("term", "") if pn is not None else ""

        abs_url, pdf = eid, ""
        for link in e.findall(ATOM + "link"):
            href = link.attrib.get("href", "")
            if link.attrib.get("rel") == "alternate" and href:
                abs_url = href
            if link.attrib.get("title") == "pdf" or link.attrib.get("type") == "application/pdf":
                pdf = href

        out.append(Paper(
            aid,
            txt(e, ATOM + "title"),
            authors,
            txt(e, ATOM + "summary"),
            txt(e, ATOM + "published"),
            txt(e, ATOM + "updated"),
            primary,
            cats,
            abs_url,
            pdf,
            txt(e, ARXIV + "doi"),
            txt(e, ARXIV + "journal_ref"),
        ))
    return total, out


def build_query(cats: list[str], since: datetime, until: datetime, api_term: str = "") -> str:
    cat_query = " OR ".join(f"cat:{x}" for x in cats)
    stamp = lambda d: d.astimezone(timezone.utc).strftime("%Y%m%d%H%M")
    query = f"({cat_query}) AND submittedDate:[{stamp(since)} TO {stamp(until)}]"
    if api_term.strip():
        # Advanced/manual narrowing for very long historical searches.
        safe = api_term.strip().replace('"', r'\"')
        query = f'({query}) AND all:"{safe}"'
    return query


def request(url: str, last: list[float]) -> bytes:
    elapsed = time.monotonic() - last[0]
    if last[0] and elapsed < DELAY:
        time.sleep(DELAY - elapsed)

    last[0] = time.monotonic()
    req = urllib.request.Request(
        url,
        headers={
            "User-Agent": f"HSH-arXiv-Structural-Scanner/{VERSION}",
            "Accept": "application/atom+xml",
        },
    )

    for attempt in range(4):
        try:
            with urllib.request.urlopen(req, timeout=60) as r:
                return r.read()
        except (urllib.error.HTTPError, urllib.error.URLError, TimeoutError) as ex:
            if isinstance(ex, urllib.error.HTTPError) and ex.code not in {429, 500, 502, 503, 504}:
                raise
            if attempt == 3:
                raise
            time.sleep(max(DELAY, 2 ** attempt))
    raise RuntimeError("unreachable")


def fetch(query: str, page_size: int, max_fetch: int):
    papers = []
    start = 0
    total = 0
    last = [0.0]

    while start < max_fetch:
        n = min(page_size, max_fetch - start)
        q = urllib.parse.urlencode({
            "search_query": query,
            "start": start,
            "max_results": n,
            "sortBy": "submittedDate",
            "sortOrder": "descending",
        })
        total, page = parse_feed(request(API + "?" + q, last))
        if not page:
            break
        papers.extend(page)
        start += len(page)
        print(f"Fetched {len(papers)}/{min(total, max_fetch)}", file=sys.stderr)
        if start >= total:
            break
    return total, papers


def load_state(path: Path) -> dict[str, str]:
    if not path.exists():
        return {}
    try:
        d = json.loads(path.read_text(encoding="utf-8"))
        return {str(k): str(v) for k, v in d.get("papers", {}).items()}
    except Exception:
        return {}


def save_state(path: Path, state: dict[str, str], papers: list[Paper]):
    for p in papers:
        state[p.arxiv_id] = p.updated
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps({
        "scanner_version": VERSION,
        "last_run_utc": datetime.now(timezone.utc).isoformat(),
        "papers": state,
    }, indent=2, sort_keys=True), encoding="utf-8")


def prevalence(papers: list[Paper]):
    feat = Counter()
    sector = Counter()
    bundle = Counter()
    control = Counter()
    control_family = Counter()

    for p in papers:
        feat.update(p.features)
        sector.update(p.sectors)
        bundle.update(p.bundles)
        control.update(p.control_features)
        control_family.update(p.control_families)

    return {
        "features": feat,
        "sectors": sector,
        "bundles": bundle,
        "controls": control,
        "control_families": control_family,
    }


def write_prevalence_csv(path: Path, counts: Counter, total: int, kind: str):
    with path.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=["kind", "name", "count", "fraction"])
        w.writeheader()
        for name, count in counts.most_common():
            w.writerow({
                "kind": kind,
                "name": name,
                "count": count,
                "fraction": round(count / total, 6) if total else 0.0,
            })


def outputs(outdir: Path, report: list[Paper], all_papers: list[Paper], meta: dict):
    outdir.mkdir(parents=True, exist_ok=True)
    stamp = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H%M%SZ")
    stem = outdir / f"{stamp}_SAT_HsH_arxiv_scan"

    jp = stem.with_suffix(".json")
    cp = stem.with_suffix(".csv")
    mp = stem.with_suffix(".md")
    fp = outdir / f"{stamp}_SAT_HsH_feature_prevalence.csv"
    xp = outdir / f"{stamp}_SAT_HsH_control_prevalence.csv"

    prev = prevalence(all_papers)
    meta["feature_prevalence"] = dict(prev["features"])
    meta["sector_prevalence"] = dict(prev["sectors"])
    meta["bundle_prevalence"] = dict(prev["bundles"])
    meta["control_prevalence"] = dict(prev["controls"])
    meta["control_family_prevalence"] = dict(prev["control_families"])

    jp.write_text(json.dumps({
        "scan": meta,
        "results": [asdict(p) for p in report],
    }, indent=2, ensure_ascii=False), encoding="utf-8")

    fields = [
        "score", "contrast", "tier", "control_score", "new_or_updated",
        "arxiv_id", "title", "authors", "published", "updated",
        "primary_category", "categories",
        "sectors", "features", "bundles", "terms",
        "control_families", "control_features", "control_terms",
        "abstract", "abs_url", "pdf_url", "doi", "journal_ref",
    ]
    with cp.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        for p in report:
            w.writerow({
                "score": p.score,
                "contrast": p.contrast,
                "tier": p.tier,
                "control_score": p.control_score,
                "new_or_updated": p.new_or_updated,
                "arxiv_id": p.arxiv_id,
                "title": p.title,
                "authors": "; ".join(p.authors),
                "published": p.published,
                "updated": p.updated,
                "primary_category": p.primary_category,
                "categories": "; ".join(p.categories),
                "sectors": "; ".join(p.sectors),
                "features": "; ".join(p.features),
                "bundles": "; ".join(p.bundles),
                "terms": "; ".join(p.terms),
                "control_families": "; ".join(p.control_families),
                "control_features": "; ".join(p.control_features),
                "control_terms": "; ".join(p.control_terms),
                "abstract": p.abstract,
                "abs_url": p.abs_url,
                "pdf_url": p.pdf_url,
                "doi": p.doi,
                "journal_ref": p.journal_ref,
            })

    write_prevalence_csv(fp, prev["features"], len(all_papers), "feature")
    write_prevalence_csv(xp, prev["controls"], len(all_papers), "control")

    md = [
        "# SAT / H(s)H arXiv Structural Scan",
        "",
        "> Literature-navigation heuristic only. Structural similarity is not confirmation,",
        "> and control vocabulary is a calibration baseline rather than a negative score.",
        "",
        f"Scanner version: **{VERSION}**",
        f"Fetched **{meta['fetched']}** of **{meta['available']}** records; "
        f"reported **{len(report)}** at score >= **{meta['min_score']}**.",
        "",
        "## Calibration summary",
        "",
        f"Positive vocabulary: **{len(F)} features** across "
        f"**{len(set(v[0] for v in F.values()))} sectors**.",
        f"Structural bundles: **{len(BUNDLES)}**.",
        f"Controls: **{len(CONTROL_F)} features** across "
        f"**{len(set(v[0] for v in CONTROL_F.values()))} families**.",
        "",
        "Most common positive features in the fetched corpus:",
    ]
    for name, count in prev["features"].most_common(12):
        md.append(f"- `{name}`: {count}/{len(all_papers)}")
    md += ["", "Most common controls in the fetched corpus:"]
    for name, count in prev["controls"].most_common(12):
        md.append(f"- `{name}`: {count}/{len(all_papers)}")
    md += ["", "## Ranked papers", ""]

    for i, p in enumerate(report, 1):
        md += [
            f"### {i}. [{p.title}]({p.abs_url})",
            "",
            f"**Score:** {p.score} ({p.tier}) · **Contrast:** {p.contrast} · "
            f"**Control:** {p.control_score} · **Primary:** `{p.primary_category}` · "
            f"**{'NEW/UPDATED' if p.new_or_updated else 'seen'}**",
            "",
            f"**Sectors:** {', '.join(p.sectors) or '—'}",
            "",
            f"**Bundles:** {', '.join(p.bundles) or '—'}",
            "",
            f"**Features:** {', '.join(p.features) or '—'}",
            "",
            f"**Controls:** {', '.join(p.control_features) or '—'}",
            "",
            p.abstract,
            "",
        ]
    mp.write_text("\n".join(md), encoding="utf-8")
    return cp, jp, mp, fp, xp


def print_vocabulary():
    grouped = defaultdict(list)
    for name, (sector, weight, terms) in F.items():
        grouped[sector].append((name, weight, terms))

    print("# POSITIVE STRUCTURAL VOCABULARY")
    for sector in sorted(grouped):
        print(f"\n[{sector}]")
        for name, weight, terms in sorted(grouped[sector]):
            print(f"{name}  weight={weight}")
            for term in terms:
                print(f"  - {term}")

    cgrouped = defaultdict(list)
    for name, (family, weight, terms) in CONTROL_F.items():
        cgrouped[family].append((name, weight, terms))

    print("\n# CONTROL VOCABULARY")
    for family in sorted(cgrouped):
        print(f"\n[{family}]")
        for name, weight, terms in sorted(cgrouped[family]):
            print(f"{name}  weight={weight}")
            for term in terms:
                print(f"  - {term}")


def self_test():
    cases = [
        (
            "strong structural cousin",
            "Holonomy and framed worldtubes in emergent metric geometry",
            (
                "We study a finite-radius worldtube around a framed curve with a normal bundle. "
                "Parallel transport and Wilson-loop holonomy quantize winding and linking sectors. "
                "A coarse-grained emergent metric is reconstructed from tangent correlations and "
                "strain of a timelike congruence, while observables arise by hypersurface projection."
            ),
        ),
        (
            "generic neighboring theory",
            "Effective field theory of dark matter near black holes",
            (
                "We construct an effective field theory for dark matter around a black hole, "
                "derive equations of motion, and perform parameter estimation."
            ),
        ),
        (
            "orthogonal condensed matter control",
            "Superconductivity and magnetic ordering in moire materials",
            (
                "Monte Carlo simulations study superconductivity, Cooper pairing, band structure, "
                "and antiferromagnetic order in a two-dimensional material."
            ),
        ),
        (
            "topological but not obviously HsH",
            "Higher-form symmetry and anomaly inflow on topological defects",
            (
                "We analyze higher-form symmetry, non-invertible symmetry, anomaly inflow, "
                "topological defects and fusion rules in a gauge theory."
            ),
        ),
    ]

    print("Self-test (no network):")
    for label, title, abstract in cases:
        p = Paper("TEST", title, [], abstract, "", "", "", [], "", "")
        score_paper(p)
        print(
            f"{label:38s} score={p.score:6.2f} control={p.control_score:4.2f} "
            f"contrast={p.contrast:6.2f} sectors={len(p.sectors):2d} bundles={len(p.bundles):2d}"
        )
        print(f"  features: {', '.join(p.features) or '—'}")
        print(f"  controls: {', '.join(p.control_features) or '—'}")
    return 0


def parse_date(s: str) -> datetime:
    return datetime.strptime(s, "%Y-%m-%d").replace(tzinfo=timezone.utc)


def main():
    ap = argparse.ArgumentParser(
        description="Scan recent arXiv metadata for SAT/H(s)H structural cousins and control baselines."
    )
    ap.add_argument("--days", type=int, default=7)
    ap.add_argument("--since", help="UTC start date YYYY-MM-DD")
    ap.add_argument("--until", help="UTC end date YYYY-MM-DD (inclusive)")
    ap.add_argument("--categories", default=",".join(CATEGORIES))
    ap.add_argument("--api-term", default="", help="Optional extra all-field API phrase for long historical scans")
    ap.add_argument("--min-score", type=float, default=8.0)
    ap.add_argument("--page-size", type=int, default=PAGE_SIZE)
    ap.add_argument("--max-fetch", type=int, default=MAX_FETCH)
    ap.add_argument("--sort-by", choices=["score", "contrast", "updated"], default="score")
    ap.add_argument("--output-dir", type=Path, default=Path("DATA/arxiv_scans"))
    ap.add_argument("--state-file", type=Path, default=Path("DATA/arxiv_scans/.arxiv_sat_state.json"))
    ap.add_argument("--include-seen", action="store_true")
    ap.add_argument("--no-state-write", action="store_true")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--list-vocabulary", action="store_true")
    ap.add_argument("--self-test", action="store_true")
    args = ap.parse_args()

    if args.list_vocabulary:
        print_vocabulary()
        return 0
    if args.self_test:
        return self_test()

    now = datetime.now(timezone.utc)
    until = min(
        parse_date(args.until) + timedelta(days=1) - timedelta(minutes=1),
        now,
    ) if args.until else now
    since = parse_date(args.since) if args.since else until - timedelta(days=args.days)

    if since >= until:
        raise SystemExit("--since must be before --until/current time")

    cats = [x.strip() for x in args.categories.split(",") if x.strip()]
    query = build_query(cats, since, until, args.api_term)

    if args.dry_run:
        print(query)
        return 0

    if not 1 <= args.page_size <= 2000:
        raise SystemExit("--page-size must be 1..2000")
    if args.max_fetch < 1:
        raise SystemExit("--max-fetch must be >= 1")

    available, papers = fetch(query, args.page_size, args.max_fetch)
    if available > args.max_fetch:
        print(
            f"WARNING: {available} records available; truncated at {args.max_fetch}. "
            "Use a shorter date window, narrower categories, or --api-term for exhaustive history.",
            file=sys.stderr,
        )

    state = load_state(args.state_file)
    for p in papers:
        p.new_or_updated = state.get(p.arxiv_id) != p.updated
        score_paper(p)

    report = [
        p for p in papers
        if p.score >= args.min_score and (args.include_seen or p.new_or_updated)
    ]

    if args.sort_by == "contrast":
        report.sort(key=lambda p: (p.contrast, p.score, p.updated), reverse=True)
    elif args.sort_by == "updated":
        report.sort(key=lambda p: (p.updated, p.score), reverse=True)
    else:
        report.sort(key=lambda p: (p.score, p.contrast, p.updated), reverse=True)

    meta = {
        "scanner_version": VERSION,
        "scan_utc": datetime.now(timezone.utc).isoformat(),
        "since": since.isoformat(),
        "until": until.isoformat(),
        "categories": cats,
        "api_term": args.api_term,
        "query": query,
        "available": available,
        "fetched": len(papers),
        "min_score": args.min_score,
        "sort_by": args.sort_by,
        "positive_feature_count": len(F),
        "bundle_count": len(BUNDLES),
        "control_feature_count": len(CONTROL_F),
    }

    cp, jp, mp, fp, xp = outputs(args.output_dir, report, papers, meta)

    if not args.no_state_write:
        save_state(args.state_file, state, papers)

    print(f"Fetched {len(papers)} of {available}; reported {len(report)}")
    print(f"CSV: {cp}")
    print(f"JSON: {jp}")
    print(f"Markdown: {mp}")
    print(f"Feature prevalence: {fp}")
    print(f"Control prevalence: {xp}")

    for p in report[:20]:
        print(
            f"{p.score:6.2f}  ctl={p.control_score:4.1f}  "
            f"{p.tier:9s}  {p.arxiv_id:16s}  {p.title}"
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
