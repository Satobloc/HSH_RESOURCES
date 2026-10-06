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
  py tools/arxiv_sat_scanner.py --days 30 --date-mode submitted --include-seen
  py tools/arxiv_sat_scanner.py --compare-years 2024,2026 --compare-through 09-08
  py tools/arxiv_sat_scanner.py --compare-years 2024,2026 --lexical-top 100
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
import statistics
from pathlib import Path

API = "https://export.arxiv.org/api/query"
DELAY = 3.1
PAGE_SIZE = 500
MAX_FETCH = 5000
VERSION = "0.7"

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
    "connection_torsion": ("curve_geometry", 2.3, [
        "torsion tensor", "torsion-like tensor", "torsion like tensor",
        "connection torsion", "cartan torsion", "affine torsion", "torsion form",
        "torsion 2-form", "torsion two-form",
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
        "topological defect", "surface defect", "codimension defect",
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
        "renormalization group fixed point", "renormalisation group fixed point",
        "rg fixed point", "infrared fixed point", "ultraviolet fixed point",
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
    ("line_defect_fusion", 3.5, [
        ("filament_defect",), ("topological_selection",),
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

    # Context controls for common false-positive neighborhoods. These remain
    # descriptive only; they never subtract from the structural score.
    "ctl_neighbor_cft": ("neighbor_topic", 1.0, [
        "conformal field theory", "conformal field theories", "defect cft",
        "conformal defect", "conformal defects", "conformal bootstrap",
        "cusp anomalous dimension", "cusp anomalous dimensions", "wilson-fisher",
        "wilson fisher",
    ]),
    "ctl_orthogonal_quantum_critical": ("orthogonal_physics", 1.0, [
        "quantum criticality", "quantum critical point", "deconfined quantum critical",
        "critical bulk", "fuzzy sphere regularization", "fuzzy-sphere regularization",
        "critical phenomena",
    ]),
    "ctl_math_category_geometry": ("mathematical_context", 1.0, [
        "derived category", "homotopy category", "coherent sheaf", "coherent sheaves",
        "morita equivalence", "cw-complex", "cw complex", "asphericity",
        "universal cover", "equivariant ext spectral sequence",
    ]),

    # Broad non-physics STEM language should almost never dominate the selected
    # categories; if it does, category selection or vocabulary is drifting.
    "ctl_nonphysics_ml": ("nonphysics_stem", 1.0, [
        "machine learning", "neural network", "deep learning", "transformer model",
        "graph neural network",
    ]),
    "ctl_nonphysics_bio": ("nonphysics_stem", 1.0, [
        "protein folding", "gene expression", "cell signaling", "cell signalling",
        "genome", "biomolecule", "cell population", "cell populations", "cellular tissue",
        "biological tissue", "myoblast", "myoblasts", "morphogenesis", "organ movement",
        "organ movements",
    ]),
    "ctl_nonphysics_chem": ("nonphysics_stem", 1.0, [
        "catalyst", "catalysis", "electrochemistry", "battery material",
        "chemical reaction network",
    ]),
}


# ----------------------------------------------------------------------
# NEUTRAL LANDSCAPE TOPICS
# ----------------------------------------------------------------------
# These labels are independent of the SAT/H(s)H structural score. Their purpose
# is to describe how the research landscape itself reallocates attention.
TOPIC_F = {
    "quantum_gravity": ["quantum gravity", "loop quantum gravity", "spin foam", "spin network", "causal set", "asymptotic safety"],
    "strings_holography": ["string theory", "superstring", "d-brane", "ads/cft", "gauge/gravity duality", "holography", "holographic"],
    "black_holes": ["black hole", "black-hole", "event horizon", "hawking radiation", "ringdown", "black hole entropy"],
    "gravitational_waves": ["gravitational wave", "gravitational-wave", "waveform", "ringdown", "pulsar timing array", "pta"],
    "cosmology_expansion": ["cosmology", "inflation", "hubble tension", "cosmological constant", "dark energy", "large scale structure", "large-scale structure"],
    "dark_sector": ["dark matter", "dark photon", "hidden sector", "hidden-sector", "axion", "sterile state"],
    "neutrinos_flavor": ["neutrino", "pmns", "flavor mixing", "flavour mixing", "leptonic cp", "neutrino oscillation"],
    "qft_amplitudes": ["scattering amplitude", "scattering amplitudes", "amplitudes", "s-matrix", "s matrix", "bootstrap", "unitarity method"],
    "conformal_defects": ["conformal field theory", "conformal bootstrap", "defect cft", "line defect", "surface defect", "cusp anomalous"],
    "generalized_symmetry": ["higher-form symmetry", "higher form symmetry", "non-invertible symmetry", "noninvertible symmetry", "categorical symmetry", "symmetry defect"],
    "topology_geometry": ["topological", "topology", "holonomy", "monodromy", "fiber bundle", "fibre bundle", "homotopy", "knot", "braid"],
    "emergent_spacetime": ["emergent spacetime", "emergent geometry", "emergent gravity", "induced gravity", "geometry from entanglement", "spacetime emergence"],
    "quantum_information": ["quantum information", "entanglement", "quantum channel", "quantum error correction", "quantum complexity", "quantum resource"],
    "quantum_geometry_phase": ["quantum geometry", "quantum geometric tensor", "berry phase", "geometric phase", "wilczek-zee", "wilczek zee"],
    "topological_matter": ["topological insulator", "topological superconductor", "topological phase", "topological order", "chern", "berry curvature"],
    "quantum_criticality": ["quantum critical", "critical point", "criticality", "wilson-fisher", "wilson fisher", "deconfined quantum critical"],
    "superconductivity": ["superconductivity", "superconductor", "cooper pair", "josephson", "superfluidity"],
    "moire_2d_materials": ["moire", "moiré", "graphene", "two-dimensional material", "2d material", "van der waals", "van der waals"],
    "many_body_condensed": ["many-body", "many body", "strongly correlated", "spin liquid", "hubbard model", "tensor network"],
    "atomic_optical": ["cold atom", "ultracold atom", "rydberg", "optical lattice", "atom interferometer", "quantum optics"],
    "nuclear_neutron_stars": ["nuclear matter", "neutron star", "neutron-star", "dense matter", "nuclear structure", "quark matter"],
    "plasma_space": ["plasma", "magnetohydrodynamic", "magnetic reconnection", "solar wind", "tokamak", "space plasma"],
    "soft_active_matter": ["soft matter", "active matter", "nematic", "topological defect", "active fluid", "biological tissue"],
    "nonlinear_dynamics": ["nonlinear dynamics", "chaos", "soliton", "synchronization", "synchronisation", "bifurcation", "dynamical system"],
    "mathematical_geometry": ["differential geometry", "algebraic geometry", "symplectic geometry", "contact geometry", "riemannian", "lorentzian geometry"],
    "mathematical_topology": ["algebraic topology", "geometric topology", "homotopy", "homology", "knot theory", "manifold topology"],
    "machine_learning_science": ["machine learning", "neural network", "deep learning", "foundation model", "transformer", "artificial intelligence"],
    "precision_measurement": ["precision measurement", "atomic clock", "interferometry", "precision test", "metrology", "quantum sensor"],
}

LEXICAL_STOPWORDS = {
    "the","and","for","with","from","that","this","are","was","were","have","has","had","into","using","use","used","our","we","their","its","which","can","may","also","between","within","through","over","under","than","such","these","those","where","when","while","both","each","all","not","but","more","most","new","show","shows","shown","study","studies","present","results","result","model","models","theory","theories","system","systems","approach","method","methods","analysis","properties","different","based","case","cases","however","provide","provides","find","found","derive","derived","discuss","including","including","towards","toward","via","here","there","been","being","some","any","one","two","three","first","second","high","low","large","small","general","possible","important","work","paper"
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
    primary_in_scope: bool = True

    new_or_updated: bool = True


def norm(s: str) -> str:
    s = html.unescape(s or "").lower()
    s = s.replace("–", "-").replace("—", "-").replace("−", "-")
    s = s.replace("’", "'").replace("“", '"').replace("”", '"')
    return re.sub(r"\s+", " ", s).strip()


def has(term: str, text: str) -> bool:
    """Boundary-aware matching over normalized text.

    v0.4 used substring matching for phrases, so ``normal frame`` matched
    ``orthonormal frame``. This matcher anchors alphanumeric term edges while
    still allowing a simple plural ``s`` for alphabetic terms/phrases.
    """
    t = norm(term)
    if not t:
        return False
    body = re.escape(t)
    prefix = r"(?<![a-z0-9])" if t[0].isalnum() else ""
    if t[-1].isalpha() and not t.endswith("s"):
        suffix = r"(?:(?:s)|(?:es))?(?![a-z0-9])"
    elif t[-1].isalnum():
        suffix = r"(?![a-z0-9])"
    else:
        suffix = ""
    return bool(re.search(prefix + body + suffix, text))


def first_hit(terms: list[str], title: str, abstract: str, used_terms: set[str] | None = None):
    used_terms = used_terms or set()
    for where, text in (("title", title), ("abstract", abstract)):
        for x in terms:
            if norm(x) in used_terms:
                continue
            if has(x, text):
                return x, where
    return None


def score_paper(p: Paper) -> Paper:
    ti, ab = norm(p.title), norm(p.abstract)
    found = {}
    sectors = set()
    total = 0.0

    # Positive structural features. The exact same lexical hit can contribute
    # only once, preventing one phrase (e.g. "line defect") from inflating
    # multiple conceptual features.
    used_positive_terms = set()
    for name, (sector, weight, terms) in F.items():
        hit = first_hit(terms, ti, ab, used_positive_terms)
        if hit is None:
            continue
        term, where = hit
        multiplier = 1.65 if where == "title" else 1.0
        phrase_bonus = 0.35 if len(norm(term).split()) > 1 else 0.0
        total += weight * multiplier + phrase_bonus
        found[name] = (term, where)
        used_positive_terms.add(norm(term))
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
    used_control_terms = set()
    for name, (family, weight, terms) in CONTROL_F.items():
        hit = first_hit(terms, ti, ab, used_control_terms)
        if hit is None:
            continue
        term, where = hit
        ctotal += weight * (1.35 if where == "title" else 1.0)
        cfound[name] = (term, where)
        used_control_terms.add(norm(term))
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


def fetch(
    query: str,
    page_size: int,
    max_fetch: int,
    sort_by_api: str = "submittedDate",
    updated_since: datetime | None = None,
    updated_until: datetime | None = None,
):
    """Fetch pages in descending date order.

    When ``updated_since`` is supplied, the query is sorted by lastUpdatedDate
    and paging stops once the sorted feed crosses the cutoff. This captures
    revisions of older papers, which a submittedDate filter alone cannot do.
    """
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
            "sortBy": sort_by_api,
            "sortOrder": "descending",
        })
        total, page = parse_feed(request(API + "?" + q, last))
        if not page:
            break

        if updated_since is not None:
            keep = []
            crossed_lower = False
            for p in page:
                try:
                    upd = datetime.fromisoformat(p.updated.replace("Z", "+00:00"))
                except ValueError:
                    upd = None
                if upd is not None and updated_until is not None and upd > updated_until:
                    continue
                if upd is not None and upd < updated_since:
                    crossed_lower = True
                    continue
                keep.append(p)
            papers.extend(keep)
            start += len(page)
            print(
                f"Fetched {start} API records; kept {len(papers)} in updated window",
                file=sys.stderr,
            )
            if crossed_lower:
                break
        else:
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
    ap = outdir / f"{stamp}_SAT_HsH_all_scored.csv"

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
        "score", "contrast", "tier", "control_score", "new_or_updated", "primary_in_scope",
        "arxiv_id", "title", "authors", "published", "updated",
        "primary_category", "categories",
        "sector_count", "feature_count", "bundle_count",
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
                "primary_in_scope": p.primary_in_scope,
                "arxiv_id": p.arxiv_id,
                "title": p.title,
                "authors": "; ".join(p.authors),
                "published": p.published,
                "updated": p.updated,
                "primary_category": p.primary_category,
                "categories": "; ".join(p.categories),
                "sector_count": len(p.sectors),
                "feature_count": len(p.features),
                "bundle_count": len(p.bundles),
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

    # Compact full-corpus calibration table: includes every fetched paper,
    # including zero-score and below-threshold papers, so false negatives and
    # threshold behavior can be inspected after each run.
    all_fields = [
        "score", "contrast", "tier", "control_score", "new_or_updated", "primary_in_scope",
        "arxiv_id", "title", "published", "updated", "primary_category",
        "categories", "sector_count", "feature_count", "bundle_count", "sectors", "features", "bundles", "terms",
        "control_families", "control_features", "control_terms", "abs_url", "pdf_url",
    ]
    with ap.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=all_fields)
        w.writeheader()
        for p in sorted(all_papers, key=lambda x: (x.score, x.contrast, x.updated), reverse=True):
            w.writerow({
                "score": p.score,
                "contrast": p.contrast,
                "tier": p.tier,
                "control_score": p.control_score,
                "new_or_updated": p.new_or_updated,
                "primary_in_scope": p.primary_in_scope,
                "arxiv_id": p.arxiv_id,
                "title": p.title,
                "published": p.published,
                "updated": p.updated,
                "primary_category": p.primary_category,
                "categories": "; ".join(p.categories),
                "sector_count": len(p.sectors),
                "feature_count": len(p.features),
                "bundle_count": len(p.bundles),
                "sectors": "; ".join(p.sectors),
                "features": "; ".join(p.features),
                "bundles": "; ".join(p.bundles),
                "terms": "; ".join(p.terms),
                "control_families": "; ".join(p.control_families),
                "control_features": "; ".join(p.control_features),
                "control_terms": "; ".join(p.control_terms),
                "abs_url": p.abs_url,
                "pdf_url": p.pdf_url,
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
        (
            f"Fetched **{meta['fetched']}** records in the requested update window "
            f"(category-query universe: **{meta['available']}**); "
            f"reported **{len(report)}** at score >= **{meta['min_score']}**."
            if meta.get("date_mode") == "updated"
            else f"Fetched **{meta['fetched']}** of **{meta['available']}** records; "
                 f"reported **{len(report)}** at score >= **{meta['min_score']}**."
        ),
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
    return cp, jp, mp, fp, xp, ap


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



def date_chunks(start: datetime, end: datetime, chunk_days: int = 7):
    """Yield inclusive UTC date windows used only to partition large API pulls."""
    cur = start
    while cur <= end:
        nxt = min(cur + timedelta(days=chunk_days) - timedelta(minutes=1), end)
        yield cur, nxt
        cur = nxt + timedelta(minutes=1)


def fetch_submitted_period_batched(
    cats: list[str],
    start: datetime,
    end: datetime,
    page_size: int,
    max_fetch_per_chunk: int,
    api_term: str = "",
    chunk_days: int = 7,
):
    """Fetch a long submitted-date period in small exact windows and deduplicate."""
    by_id: dict[str, Paper] = {}
    windows = list(date_chunks(start, end, chunk_days))
    for idx, (ws, we) in enumerate(windows, 1):
        query = build_query(cats, ws, we, api_term)
        available, papers = fetch(
            query,
            page_size,
            max_fetch_per_chunk,
            sort_by_api="submittedDate",
        )
        if available > max_fetch_per_chunk:
            raise RuntimeError(
                f"Comparison chunk {ws.date()}..{we.date()} contains {available} records, "
                f"above --max-fetch={max_fetch_per_chunk}. Reduce --compare-chunk-days."
            )
        for paper in papers:
            by_id[paper.arxiv_id] = paper
        print(
            f"Comparison window {idx}/{len(windows)}: {ws.date()}..{we.date()} "
            f"-> {len(papers)} records; cumulative {len(by_id)}",
            file=sys.stderr,
        )
    return list(by_id.values())


def category_bucket(p: Paper, cats: list[str]) -> str:
    return p.primary_category if p.primary_category in cats else "__crosslisted__"


def score_corpus(papers: list[Paper], cats: list[str]):
    for p in papers:
        p.new_or_updated = True
        p.primary_in_scope = p.primary_category in cats
        score_paper(p)
    return papers


def compact_all_scored(path: Path, papers: list[Paper], cats: list[str]):
    fields = [
        "score", "contrast", "tier", "control_score", "primary_in_scope", "category_bucket",
        "arxiv_id", "title", "published", "updated", "primary_category", "categories",
        "sector_count", "feature_count", "bundle_count", "sectors", "features", "bundles",
        "control_families", "control_features", "abs_url",
    ]
    with path.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        for p in sorted(papers, key=lambda x: (x.score, x.contrast, x.published), reverse=True):
            w.writerow({
                "score": p.score,
                "contrast": p.contrast,
                "tier": p.tier,
                "control_score": p.control_score,
                "primary_in_scope": p.primary_in_scope,
                "category_bucket": category_bucket(p, cats),
                "arxiv_id": p.arxiv_id,
                "title": p.title,
                "published": p.published,
                "updated": p.updated,
                "primary_category": p.primary_category,
                "categories": "; ".join(p.categories),
                "sector_count": len(p.sectors),
                "feature_count": len(p.features),
                "bundle_count": len(p.bundles),
                "sectors": "; ".join(p.sectors),
                "features": "; ".join(p.features),
                "bundles": "; ".join(p.bundles),
                "control_families": "; ".join(p.control_families),
                "control_features": "; ".join(p.control_features),
                "abs_url": p.abs_url,
            })


def category_counts(papers: list[Paper], cats: list[str]) -> Counter:
    return Counter(category_bucket(p, cats) for p in papers)


def item_counts(papers: list[Paper], attr: str) -> Counter:
    c = Counter()
    for p in papers:
        c.update(getattr(p, attr))
    return c



def topic_tags(p: Paper) -> list[str]:
    ti, ab = norm(p.title), norm(p.abstract)
    tags = []
    for topic, terms in TOPIC_F.items():
        if first_hit(terms, ti, ab) is not None:
            tags.append(topic)
    return tags


def topic_counts(papers: list[Paper]) -> Counter:
    c = Counter()
    for p in papers:
        c.update(topic_tags(p))
    return c


def all_category_counts(papers: list[Paper]) -> Counter:
    """Document prevalence of every arXiv category, including cross-lists."""
    c = Counter()
    for p in papers:
        c.update(set(p.categories))
    return c


def mean_score_for_topic(papers: list[Paper], topic: str) -> tuple[float, float]:
    matched = [p for p in papers if topic in topic_tags(p)]
    if not matched:
        return 0.0, 0.0
    return (
        statistics.fmean(p.score for p in matched),
        sum(p.score >= 8 for p in matched) / len(matched),
    )


def write_topic_comparison(path: Path, year_a: int, a: list[Paper], year_b: int, b: list[Paper]):
    ca, cb = topic_counts(a), topic_counts(b)
    rows = []
    for topic in sorted(set(ca) | set(cb)):
        fa = ca[topic] / len(a) if a else 0.0
        fb = cb[topic] / len(b) if b else 0.0
        ma, ha = mean_score_for_topic(a, topic)
        mb, hb = mean_score_for_topic(b, topic)
        rows.append({
            "topic": topic,
            f"count_{year_a}": ca[topic],
            f"fraction_{year_a}": round(fa, 8),
            f"count_{year_b}": cb[topic],
            f"fraction_{year_b}": round(fb, 8),
            "delta_fraction": round(fb-fa, 8),
            "ratio": safe_ratio(fb, fa),
            f"mean_hsh_score_{year_a}": round(ma, 6),
            f"mean_hsh_score_{year_b}": round(mb, 6),
            f"fraction_hsh_ge8_{year_a}": round(ha, 8),
            f"fraction_hsh_ge8_{year_b}": round(hb, 8),
            "delta_mean_hsh_score": round(mb-ma, 6),
        })
    rows.sort(key=lambda r: r["delta_fraction"], reverse=True)
    with path.open("w", newline="", encoding="utf-8") as f:
        fields = list(rows[0].keys()) if rows else ["topic"]
        w = csv.DictWriter(f, fieldnames=fields); w.writeheader(); w.writerows(rows)
    return rows


def write_crosslist_category_comparison(path: Path, year_a: int, a: list[Paper], year_b: int, b: list[Paper]):
    ca, cb = all_category_counts(a), all_category_counts(b)
    rows=[]
    for cat in sorted(set(ca)|set(cb)):
        fa=ca[cat]/len(a) if a else 0.0
        fb=cb[cat]/len(b) if b else 0.0
        rows.append({
            "category":cat,
            f"document_count_{year_a}":ca[cat], f"document_fraction_{year_a}":round(fa,8),
            f"document_count_{year_b}":cb[cat], f"document_fraction_{year_b}":round(fb,8),
            "delta_fraction":round(fb-fa,8), "ratio":safe_ratio(fb,fa),
        })
    rows.sort(key=lambda r:r["delta_fraction"], reverse=True)
    with path.open("w",newline="",encoding="utf-8") as f:
        fields=list(rows[0].keys()) if rows else ["category"]
        w=csv.DictWriter(f,fieldnames=fields);w.writeheader();w.writerows(rows)
    return rows


def lexical_terms(p: Paper) -> set[str]:
    text = norm(p.title + " " + p.abstract)
    toks = [t.strip("'-") for t in re.findall(r"[a-z][a-z'-]{2,}", text)]
    toks = [t for t in toks if t not in LEXICAL_STOPWORDS and len(t) >= 3]
    out=set(toks)
    for x,y in zip(toks,toks[1:]):
        if x not in LEXICAL_STOPWORDS and y not in LEXICAL_STOPWORDS:
            out.add(x+" "+y)
    return out


def lexical_document_stats(papers: list[Paper]):
    counts=Counter(); score_sum=Counter(); high=Counter()
    for p in papers:
        terms=lexical_terms(p)
        counts.update(terms)
        for term in terms:
            score_sum[term]+=p.score
            if p.score>=8: high[term]+=1
    return counts,score_sum,high


def write_lexical_shift(path: Path, year_a:int, a:list[Paper], year_b:int, b:list[Paper], min_docs:int=20, top_n:int=100):
    ca,sa,ha=lexical_document_stats(a); cb,sb,hb=lexical_document_stats(b)
    candidates=[]
    for term in set(ca)|set(cb):
        if ca[term]+cb[term] < min_docs: continue
        fa=ca[term]/len(a) if a else 0.0; fb=cb[term]/len(b) if b else 0.0
        # Smoothed log2 prevalence ratio for ranking, but raw fractions stay visible.
        pa=(ca[term]+0.5)/(len(a)+1) if a else 0.0
        pb=(cb[term]+0.5)/(len(b)+1) if b else 0.0
        log2_ratio = __import__('math').log2(pb/pa) if pa and pb else 0.0
        candidates.append({
            "term":term,
            f"doc_count_{year_a}":ca[term], f"doc_fraction_{year_a}":round(fa,8),
            f"doc_count_{year_b}":cb[term], f"doc_fraction_{year_b}":round(fb,8),
            "delta_fraction":round(fb-fa,8), "ratio":safe_ratio(fb,fa),
            "log2_ratio_smoothed":round(log2_ratio,6),
            f"mean_hsh_score_{year_a}":round(sa[term]/ca[term],6) if ca[term] else 0.0,
            f"mean_hsh_score_{year_b}":round(sb[term]/cb[term],6) if cb[term] else 0.0,
            f"hsh_ge8_fraction_{year_a}":round(ha[term]/ca[term],8) if ca[term] else 0.0,
            f"hsh_ge8_fraction_{year_b}":round(hb[term]/cb[term],8) if cb[term] else 0.0,
        })
    # Keep strongest increases and decreases by absolute prevalence change, plus ratio movers.
    by_delta=sorted(candidates,key=lambda r:r["delta_fraction"],reverse=True)
    chosen={r["term"]:r for r in by_delta[:top_n] + by_delta[-top_n:]}
    by_ratio=sorted(candidates,key=lambda r:abs(r["log2_ratio_smoothed"]),reverse=True)
    for r in by_ratio[:top_n]: chosen[r["term"]]=r
    rows=sorted(chosen.values(),key=lambda r:r["delta_fraction"],reverse=True)
    with path.open("w",newline="",encoding="utf-8") as f:
        fields=list(rows[0].keys()) if rows else ["term"]
        w=csv.DictWriter(f,fieldnames=fields);w.writeheader();w.writerows(rows)
    return rows


def category_score_decomposition(year_a:int, a:list[Paper], year_b:int, b:list[Paper], cats:list[str]):
    """Exact midpoint decomposition of aggregate mean-score change by primary-category mix vs within-category score change."""
    ca,cb=category_counts(a,cats),category_counts(b,cats)
    cats_all=sorted(set(ca)|set(cb))
    def rate(ps,cat):
        vals=[p.score for p in ps if category_bucket(p,cats)==cat]
        return statistics.fmean(vals) if vals else 0.0
    rows=[]; composition=0.0; within=0.0
    for cat in cats_all:
        wa=ca[cat]/len(a) if a else 0.0; wb=cb[cat]/len(b) if b else 0.0
        ra=rate(a,cat); rb=rate(b,cat)
        comp=(wb-wa)*(ra+rb)/2
        inside=((wa+wb)/2)*(rb-ra)
        composition+=comp; within+=inside
        rows.append({
            "category":cat,
            f"share_{year_a}":round(wa,8), f"share_{year_b}":round(wb,8),
            f"mean_score_{year_a}":round(ra,6), f"mean_score_{year_b}":round(rb,6),
            "composition_contribution":round(comp,8),
            "within_category_contribution":round(inside,8),
            "total_contribution":round(comp+inside,8),
        })
    rows.sort(key=lambda r:abs(r["total_contribution"]),reverse=True)
    return rows,composition,within

def standardized_fraction(
    papers: list[Paper],
    attr: str,
    item: str,
    cats: list[str],
    shared_weights: dict[str, float],
) -> float:
    totals = category_counts(papers, cats)
    hits = Counter()
    for p in papers:
        if item in getattr(p, attr):
            hits[category_bucket(p, cats)] += 1
    value = 0.0
    used_weight = 0.0
    for cat, weight in shared_weights.items():
        n = totals.get(cat, 0)
        if n <= 0:
            continue
        value += weight * (hits.get(cat, 0) / n)
        used_weight += weight
    return value / used_weight if used_weight else 0.0


def shared_category_weights(a: list[Paper], b: list[Paper], cats: list[str]) -> dict[str, float]:
    ca, cb = category_counts(a, cats), category_counts(b, cats)
    common = sorted(set(ca) & set(cb))
    pooled = {k: ca[k] + cb[k] for k in common}
    total = sum(pooled.values())
    return {k: v / total for k, v in pooled.items()} if total else {}


def safe_ratio(b: float, a: float):
    if a == 0:
        return "inf" if b > 0 else "1.0"
    return round(b / a, 6)


def write_pair_comparison(
    path: Path,
    kind: str,
    attr: str,
    year_a: int,
    papers_a: list[Paper],
    year_b: int,
    papers_b: list[Paper],
    cats: list[str],
    shared_weights: dict[str, float],
):
    ca, cb = item_counts(papers_a, attr), item_counts(papers_b, attr)
    names = sorted(set(ca) | set(cb))
    rows = []
    for name in names:
        fa = ca[name] / len(papers_a) if papers_a else 0.0
        fb = cb[name] / len(papers_b) if papers_b else 0.0
        sa = standardized_fraction(papers_a, attr, name, cats, shared_weights)
        sb = standardized_fraction(papers_b, attr, name, cats, shared_weights)
        rows.append({
            "kind": kind,
            "name": name,
            f"count_{year_a}": ca[name],
            f"fraction_{year_a}": round(fa, 8),
            f"count_{year_b}": cb[name],
            f"fraction_{year_b}": round(fb, 8),
            "raw_delta_fraction": round(fb - fa, 8),
            "raw_ratio": safe_ratio(fb, fa),
            f"standardized_fraction_{year_a}": round(sa, 8),
            f"standardized_fraction_{year_b}": round(sb, 8),
            "standardized_delta_fraction": round(sb - sa, 8),
            "standardized_ratio": safe_ratio(sb, sa),
        })
    rows.sort(key=lambda r: (r["standardized_delta_fraction"], r["raw_delta_fraction"]), reverse=True)
    fields = list(rows[0].keys()) if rows else ["kind", "name"]
    with path.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        w.writerows(rows)
    return rows


def corpus_stats(papers: list[Paper]) -> dict:
    scores = [p.score for p in papers]
    return {
        "papers": len(papers),
        "mean_score": round(statistics.fmean(scores), 6) if scores else 0.0,
        "median_score": round(statistics.median(scores), 6) if scores else 0.0,
        "fraction_score_ge_8": round(sum(x >= 8 for x in scores) / len(scores), 8) if scores else 0.0,
        "fraction_score_ge_13": round(sum(x >= 13 for x in scores) / len(scores), 8) if scores else 0.0,
        "fraction_score_ge_20": round(sum(x >= 20 for x in scores) / len(scores), 8) if scores else 0.0,
        "fraction_score_ge_30": round(sum(x >= 30 for x in scores) / len(scores), 8) if scores else 0.0,
        "mean_feature_count": round(statistics.fmean(len(p.features) for p in papers), 6) if papers else 0.0,
        "mean_sector_count": round(statistics.fmean(len(p.sectors) for p in papers), 6) if papers else 0.0,
        "mean_bundle_count": round(statistics.fmean(len(p.bundles) for p in papers), 6) if papers else 0.0,
        "mean_control_score": round(statistics.fmean(p.control_score for p in papers), 6) if papers else 0.0,
    }


def run_year_comparison(args, cats: list[str]):
    raw_years = [x.strip() for x in args.compare_years.split(",") if x.strip()]
    if len(raw_years) != 2:
        raise SystemExit("--compare-years requires exactly two years, e.g. 2024,2026")
    year_a, year_b = map(int, raw_years)
    if year_a == year_b:
        raise SystemExit("--compare-years must contain two different years")

    now = datetime.now(timezone.utc)
    if args.compare_through:
        m, d = map(int, args.compare_through.split("-"))
    else:
        # Use the last complete UTC day, not a partial current day. This keeps
        # the matched historical windows equal in duration and avoids treating
        # today's incomplete arXiv ingest as a real year-to-year difference.
        cutoff = now - timedelta(days=1)
        m, d = cutoff.month, cutoff.day

    corpora: dict[int, list[Paper]] = {}
    periods = {}

    if args.dry_run:
        print(f"comparison={year_a} vs {year_b}")
        print(f"matched_through={m:02d}-{d:02d}")
        print(f"chunk_days={args.compare_chunk_days}")
        for year in (year_a, year_b):
            start = datetime(year, 1, 1, tzinfo=timezone.utc)
            try:
                end = datetime(year, m, d, 23, 59, tzinfo=timezone.utc)
            except ValueError:
                end = datetime(year, m, 28, 23, 59, tzinfo=timezone.utc)
            if year == now.year:
                end = min(end, now)
            print(f"{year}: {start.isoformat()} -> {end.isoformat()}")
            chunks = list(date_chunks(start, end, args.compare_chunk_days))
            print(f"  API chunks: {len(chunks)}")
            if chunks:
                print(f"  first query: {build_query(cats, chunks[0][0], chunks[0][1], args.api_term)}")
                print(f"  last query:  {build_query(cats, chunks[-1][0], chunks[-1][1], args.api_term)}")
        return 0

    for year in (year_a, year_b):
        start = datetime(year, 1, 1, tzinfo=timezone.utc)
        try:
            end = datetime(year, m, d, 23, 59, tzinfo=timezone.utc)
        except ValueError:
            # Handles Feb 29 comparisons against non-leap years conservatively.
            end = datetime(year, m, 28, 23, 59, tzinfo=timezone.utc)
        if year == now.year:
            end = min(end, now)
        if end < start:
            raise SystemExit("Invalid --compare-through date")
        periods[year] = (start, end)
        print(f"Fetching comparison corpus {year}: {start.date()}..{end.date()}", file=sys.stderr)
        papers = fetch_submitted_period_batched(
            cats,
            start,
            end,
            args.page_size,
            args.max_fetch,
            api_term=args.api_term,
            chunk_days=args.compare_chunk_days,
        )
        corpora[year] = score_corpus(papers, cats)

    a, b = corpora[year_a], corpora[year_b]
    weights = shared_category_weights(a, b, cats)
    outdir = args.output_dir / f"compare_{year_a}_vs_{year_b}_through_{m:02d}-{d:02d}"
    outdir.mkdir(parents=True, exist_ok=True)

    all_a = outdir / f"{year_a}_all_scored.csv"
    all_b = outdir / f"{year_b}_all_scored.csv"
    compact_all_scored(all_a, a, cats)
    compact_all_scored(all_b, b, cats)

    comparisons = {}
    specs = [
        ("feature", "features"),
        ("sector", "sectors"),
        ("bundle", "bundles"),
        ("control", "control_features"),
        ("control_family", "control_families"),
    ]
    for kind, attr in specs:
        path = outdir / f"{kind}_comparison_{year_a}_vs_{year_b}.csv"
        comparisons[kind] = write_pair_comparison(
            path, kind, attr, year_a, a, year_b, b, cats, weights
        )

    # Category composition table.
    cat_a, cat_b = category_counts(a, cats), category_counts(b, cats)
    cat_path = outdir / f"category_mix_{year_a}_vs_{year_b}.csv"
    with cat_path.open("w", newline="", encoding="utf-8") as f:
        fields = [
            "category", f"count_{year_a}", f"fraction_{year_a}",
            f"count_{year_b}", f"fraction_{year_b}", "pooled_standard_weight",
        ]
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        for cat in sorted(set(cat_a) | set(cat_b)):
            w.writerow({
                "category": cat,
                f"count_{year_a}": cat_a[cat],
                f"fraction_{year_a}": round(cat_a[cat] / len(a), 8) if a else 0.0,
                f"count_{year_b}": cat_b[cat],
                f"fraction_{year_b}": round(cat_b[cat] / len(b), 8) if b else 0.0,
                "pooled_standard_weight": round(weights.get(cat, 0.0), 8),
            })

    # Additional landscape outputs. These are part of the signal, not nuisance corrections.
    crosslist_path = outdir / f"crosslist_category_mix_{year_a}_vs_{year_b}.csv"
    crosslist_rows = write_crosslist_category_comparison(crosslist_path, year_a, a, year_b, b)

    topic_path = outdir / f"topic_landscape_{year_a}_vs_{year_b}.csv"
    topic_rows = write_topic_comparison(topic_path, year_a, a, year_b, b)

    lexical_path = outdir / f"lexical_landscape_{year_a}_vs_{year_b}.csv"
    lexical_rows = []
    if not args.no_lexical:
        print("Computing unsupervised lexical drift...", file=sys.stderr)
        lexical_rows = write_lexical_shift(
            lexical_path, year_a, a, year_b, b,
            min_docs=args.lexical_min_docs, top_n=args.lexical_top,
        )

    decomp_rows, composition_effect, within_effect = category_score_decomposition(
        year_a, a, year_b, b, cats
    )
    decomp_path = outdir / f"hsh_score_shift_decomposition_{year_a}_vs_{year_b}.csv"
    with decomp_path.open("w", newline="", encoding="utf-8") as f:
        fields = list(decomp_rows[0].keys()) if decomp_rows else ["category"]
        w = csv.DictWriter(f, fieldnames=fields); w.writeheader(); w.writerows(decomp_rows)

    summary = {
        "scanner_version": VERSION,
        "comparison": f"{year_a} vs {year_b}",
        "matched_through": f"{m:02d}-{d:02d}",
        "periods": {
            str(year): {"since": periods[year][0].isoformat(), "until": periods[year][1].isoformat()}
            for year in (year_a, year_b)
        },
        "categories": cats,
        "interpretation": "Raw aggregate change is the primary field-change measure. Category standardization and decomposition are diagnostic lenses only; category/topic composition shifts remain part of the signal.",
        "category_standardization": "Pooled primary-category distribution across categories present in both corpora; reported diagnostically, not used to erase composition change.",
        "mean_score_shift_decomposition": {
            "composition_effect": round(composition_effect, 8),
            "within_category_effect": round(within_effect, 8),
            "total": round(composition_effect + within_effect, 8),
        },
        "stats": {str(year_a): corpus_stats(a), str(year_b): corpus_stats(b)},
        "files": {
            str(year_a): str(all_a),
            str(year_b): str(all_b),
            "category_mix": str(cat_path),
            "crosslist_category_mix": str(crosslist_path),
            "topic_landscape": str(topic_path),
            "lexical_landscape": str(lexical_path) if not args.no_lexical else None,
            "hsh_score_shift_decomposition": str(decomp_path),
        },
    }
    summary_path = outdir / f"comparison_summary_{year_a}_vs_{year_b}.json"
    summary_path.write_text(json.dumps(summary, indent=2), encoding="utf-8")

    # Human-readable report: raw field change is the headline; standardized rates are diagnostic only.
    md = [
        f"# SAT / H(s)H arXiv Comparison: {year_a} vs {year_b}",
        "",
        f"Matched window: **Jan 1–{m:02d}-{d:02d}** in each year.",
        "",
        "Raw prevalence is the headline measure of field change. Category-standardized prevalence is also reported only as a diagnostic decomposition: if the field reallocates attention toward categories where a structure is common, that composition shift is itself part of the result, not something to correct away.",
        "",
        f"- {year_a}: **{len(a)} papers**",
        f"- {year_b}: **{len(b)} papers**",
        "",
        "## Largest RAW positive-feature increases",
        "",
    ]
    positive_rows = comparisons["feature"]
    for row in sorted(positive_rows, key=lambda r: r["raw_delta_fraction"], reverse=True)[:25]:
        md.append(
            f"- `{row['name']}`: {row[f'fraction_{year_a}']:.6f} -> "
            f"{row[f'fraction_{year_b}']:.6f} "
            f"(Δ {row['raw_delta_fraction']:+.6f}; counts "
            f"{row[f'count_{year_a}']} -> {row[f'count_{year_b}']}; "
            f"within-category diagnostic Δ {row['standardized_delta_fraction']:+.6f})"
        )
    md += ["", "## Largest RAW positive-feature decreases", ""]
    for row in sorted(positive_rows, key=lambda r: r["raw_delta_fraction"])[:15]:
        md.append(
            f"- `{row['name']}`: {row[f'fraction_{year_a}']:.6f} -> "
            f"{row[f'fraction_{year_b}']:.6f} "
            f"(Δ {row['raw_delta_fraction']:+.6f})"
        )

    md += ["", "## Topic-landscape movement", ""]
    for row in topic_rows[:20]:
        md.append(
            f"- `{row['topic']}`: {row[f'fraction_{year_a}']:.6f} -> "
            f"{row[f'fraction_{year_b}']:.6f} (Δ {row['delta_fraction']:+.6f}); "
            f"mean H(s)H score {row[f'mean_hsh_score_{year_a}']:.3f} -> {row[f'mean_hsh_score_{year_b}']:.3f}"
        )

    md += ["", "## Primary-category composition: largest shifts", ""]
    cat_rows=[]
    for cat in sorted(set(cat_a)|set(cat_b)):
        fa=cat_a[cat]/len(a) if a else 0.0; fb=cat_b[cat]/len(b) if b else 0.0
        cat_rows.append((fb-fa,cat,fa,fb,cat_a[cat],cat_b[cat]))
    for delta,cat,fa,fb,na,nb in sorted(cat_rows, reverse=True)[:15]:
        md.append(f"- `{cat}`: {fa:.6f} -> {fb:.6f} (Δ {delta:+.6f}; {na} -> {nb})")

    md += [
        "", "## Aggregate H(s)H-score shift decomposition", "",
        f"Mean-score shift attributable to category-composition movement: **{composition_effect:+.6f}**",
        f"Mean-score shift attributable to within-category movement: **{within_effect:+.6f}**",
        f"Total mean-score shift: **{composition_effect + within_effect:+.6f}**",
        "",
        "These are descriptive components of the same field shift. The composition term is not subtracted or treated as confounding.",
    ]

    if lexical_rows:
        md += ["", "## Unsupervised lexical landscape: largest prevalence increases", ""]
        for row in sorted(lexical_rows, key=lambda r:r["delta_fraction"], reverse=True)[:25]:
            md.append(
                f"- `{row['term']}`: {row[f'doc_fraction_{year_a}']:.6f} -> "
                f"{row[f'doc_fraction_{year_b}']:.6f} (Δ {row['delta_fraction']:+.6f}; "
                f"mean H(s)H score {row[f'mean_hsh_score_{year_a}']:.3f} -> {row[f'mean_hsh_score_{year_b}']:.3f})"
            )

    md += ["", "## Control movement", ""]
    for row in sorted(comparisons["control"], key=lambda r:r["raw_delta_fraction"], reverse=True)[:15]:
        md.append(
            f"- `{row['name']}`: {row[f'fraction_{year_a}']:.6f} -> "
            f"{row[f'fraction_{year_b}']:.6f} (Δ {row['raw_delta_fraction']:+.6f})"
        )
    report_path = outdir / f"comparison_report_{year_a}_vs_{year_b}.md"
    report_path.write_text("\n".join(md), encoding="utf-8")

    print(f"Comparison complete: {year_a}={len(a)} papers, {year_b}={len(b)} papers")
    print(f"Report: {report_path}")
    print(f"Summary: {summary_path}")
    print(f"Feature comparison: {outdir / f'feature_comparison_{year_a}_vs_{year_b}.csv'}")
    print(f"All scored {year_a}: {all_a}")
    print(f"All scored {year_b}: {all_b}")
    print(f"Topic landscape: {topic_path}")
    print(f"Cross-list category landscape: {crosslist_path}")
    if not args.no_lexical:
        print(f"Lexical landscape: {lexical_path}")
    print(f"Score-shift decomposition: {decomp_path}")
    return 0

def main():
    ap = argparse.ArgumentParser(
        description="Scan recent arXiv metadata for SAT/H(s)H structural cousins and control baselines."
    )
    ap.add_argument("--days", type=int, default=7)
    ap.add_argument("--since", help="UTC start date YYYY-MM-DD")
    ap.add_argument("--until", help="UTC end date YYYY-MM-DD (inclusive)")
    ap.add_argument(
        "--date-mode",
        choices=["updated", "submitted"],
        default="updated",
        help="updated (default) catches both new papers and revisions; submitted uses an exact submittedDate window",
    )
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
    ap.add_argument(
        "--compare-years",
        default="",
        help="Matched submitted-date comparison, e.g. 2024,2026. Ignores state and compares Jan 1 through --compare-through.",
    )
    ap.add_argument(
        "--compare-through",
        default="",
        help="MM-DD cutoff applied to both comparison years; default is the last complete UTC day.",
    )
    ap.add_argument(
        "--compare-chunk-days",
        type=int,
        default=7,
        help="API partition size for long comparisons; analytical output is aggregated across the entire matched period.",
    )
    ap.add_argument(
        "--lexical-min-docs",
        type=int,
        default=20,
        help="Minimum combined document count for an unsupervised lexical term/phrase to enter the landscape comparison.",
    )
    ap.add_argument(
        "--lexical-top",
        type=int,
        default=100,
        help="Number of strongest lexical increases/decreases/ratio movers retained per comparison lens.",
    )
    ap.add_argument(
        "--no-lexical",
        action="store_true",
        help="Skip unsupervised word/bigram landscape analysis if a faster comparison is desired.",
    )
    args = ap.parse_args()

    if args.list_vocabulary:
        print_vocabulary()
        return 0
    if args.self_test:
        return self_test()

    cats = [x.strip() for x in args.categories.split(",") if x.strip()]
    if args.compare_years:
        if args.compare_chunk_days < 1:
            raise SystemExit("--compare-chunk-days must be >= 1")
        return run_year_comparison(args, cats)

    now = datetime.now(timezone.utc)
    until = min(
        parse_date(args.until) + timedelta(days=1) - timedelta(minutes=1),
        now,
    ) if args.until else now
    since = parse_date(args.since) if args.since else until - timedelta(days=args.days)

    if since >= until:
        raise SystemExit("--since must be before --until/current time")

    if args.date_mode == "submitted":
        query = build_query(cats, since, until, args.api_term)
        api_sort = "submittedDate"
        updated_cutoff = None
    else:
        # arXiv exposes submittedDate as the only date search filter, but it can
        # sort by lastUpdatedDate. We therefore query the category universe,
        # page newest-updated first, and stop locally at ``since``.
        cat_query = " OR ".join(f"cat:{x}" for x in cats)
        query = f"({cat_query})"
        if args.api_term.strip():
            safe = args.api_term.strip().replace('"', r'\"')
            query = f'({query}) AND all:"{safe}"'
        api_sort = "lastUpdatedDate"
        updated_cutoff = since

    if args.dry_run:
        print(f"date_mode={args.date_mode}")
        print(f"sortBy={api_sort}")
        print(query)
        return 0

    if not 1 <= args.page_size <= 2000:
        raise SystemExit("--page-size must be 1..2000")
    if args.max_fetch < 1:
        raise SystemExit("--max-fetch must be >= 1")

    available, papers = fetch(
        query,
        args.page_size,
        args.max_fetch,
        sort_by_api=api_sort,
        updated_since=updated_cutoff,
        updated_until=until if args.date_mode == "updated" else None,
    )
    if len(papers) >= args.max_fetch:
        print(
            f"WARNING: reached --max-fetch={args.max_fetch}. "
            "Use a shorter date window, narrower categories, or --api-term if needed.",
            file=sys.stderr,
        )

    state = load_state(args.state_file)
    for p in papers:
        p.new_or_updated = state.get(p.arxiv_id) != p.updated
        p.primary_in_scope = p.primary_category in cats
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
        "date_mode": args.date_mode,
        "api_sort": api_sort,
        "query": query,
        "available": available,
        "fetched": len(papers),
        "min_score": args.min_score,
        "sort_by": args.sort_by,
        "positive_feature_count": len(F),
        "bundle_count": len(BUNDLES),
        "control_feature_count": len(CONTROL_F),
        "primary_outside_requested_count": sum(not p.primary_in_scope for p in papers),
    }

    cp, jp, mp, fp, xp, apath = outputs(args.output_dir, report, papers, meta)

    if not args.no_state_write:
        save_state(args.state_file, state, papers)

    if args.date_mode == "updated":
        print(f"Fetched {len(papers)} records in update window; reported {len(report)}")
    else:
        print(f"Fetched {len(papers)} of {available}; reported {len(report)}")
    print(f"CSV: {cp}")
    print(f"JSON: {jp}")
    print(f"Markdown: {mp}")
    print(f"Feature prevalence: {fp}")
    print(f"Control prevalence: {xp}")
    print(f"All scored: {apath}")

    for p in report[:20]:
        print(
            f"{p.score:6.2f}  ctl={p.control_score:4.1f}  "
            f"{p.tier:9s}  {p.arxiv_id:16s}  {p.title}"
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
