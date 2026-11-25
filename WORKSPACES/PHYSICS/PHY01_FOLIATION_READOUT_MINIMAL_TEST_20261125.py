#!/usr/bin/env python3
"""
Minimal geometric checks for PHY-01 accumulated readout traces.

This script demonstrates two distinct families of 3D leaves in R^4:
  1. parallel affine hyperplanes w = lambda;
  2. concentric 3-sphere wavefronts ||X|| = rho.

In both cases, a 1D curve intersects each leaf at one point. A chosen
identification of each leaf with a reference 3-space turns that sequence
of points into a path, which can be circular.

This is a comparison model only. It does not assert the native SAT metric,
timesheet family, transport rule, or H(s)H finite-core geometry.
Requires Python 3.10+ and NumPy.
"""

from __future__ import annotations

import json
import math
from typing import Any

import numpy as np
from numpy.typing import NDArray


FloatArray = NDArray[np.float64]


def parallel_leaf_readout(
    parameter: FloatArray, radius: float, wave_number: float, z0: float
) -> tuple[FloatArray, FloatArray]:
    """Return ambient points p(lambda) and affine reference coordinates q(lambda)."""
    phase = wave_number * parameter
    q = np.column_stack(
        (radius * np.cos(phase), radius * np.sin(phase), np.full_like(parameter, z0))
    )
    p = np.column_stack((q, parameter))
    return p, q


def radial_wavefront_readout(
    radius_parameter: FloatArray, wave_number: float
) -> tuple[FloatArray, FloatArray]:
    """Return points on concentric S^3 leaves and their radial pullbacks to S^3_1."""
    phase = wave_number * radius_parameter
    q = np.column_stack(
        (np.cos(phase), np.sin(phase), np.zeros_like(radius_parameter), np.zeros_like(radius_parameter))
    )
    p = radius_parameter[:, None] * q
    return p, q


def rotate_reference_coordinates(
    q: FloatArray, parameter: FloatArray, wave_number: float
) -> FloatArray:
    """
    Apply a parameter-dependent inverse rotation to the parallel-leaf readout.

    This changes only the identification of successive leaves with the
    reference space. It demonstrates why the displayed trace is not invariant
    under arbitrary parameter-dependent re-identifications.
    """
    phase = wave_number * parameter
    c, s = np.cos(phase), np.sin(phase)
    x = c * q[:, 0] + s * q[:, 1]
    y = -s * q[:, 0] + c * q[:, 1]
    return np.column_stack((x, y, q[:, 2]))


def run_checks() -> dict[str, Any]:
    """Run numerical consistency checks and return a JSON-serializable summary."""
    radius = 2.0
    wave_number = 0.15  # inverse length
    z0 = 0.4
    parameter = np.linspace(0.0, 20.0 * math.pi / wave_number, 10_001)

    # Parallel leaves: each ambient point has w=lambda; q is a circle in R^3.
    p_parallel, q_parallel = parallel_leaf_readout(
        parameter, radius, wave_number, z0
    )
    assert np.allclose(p_parallel[:, 3], parameter)
    assert np.allclose(
        np.sqrt(q_parallel[:, 0] ** 2 + q_parallel[:, 1] ** 2), radius
    )
    assert np.allclose(q_parallel[:, 2], z0)

    # A parameter-dependent inverse rotation makes the same readout stationary.
    q_rotated = rotate_reference_coordinates(
        q_parallel, parameter, wave_number
    )
    assert np.allclose(q_rotated[:, 0], radius)
    assert np.allclose(q_rotated[:, 1], 0.0, atol=1e-12)
    assert np.allclose(q_rotated[:, 2], z0)

    # Radial leaves: ||p(rho)||=rho and radial pullback q lies on unit S^3.
    rho = np.linspace(0.1, 20.0 * math.pi / wave_number, 10_001)
    p_radial, q_radial = radial_wavefront_readout(rho, wave_number)
    assert np.allclose(np.linalg.norm(p_radial, axis=1), rho)
    assert np.allclose(np.linalg.norm(q_radial, axis=1), 1.0)
    assert np.allclose(
        q_radial[:, 0] ** 2 + q_radial[:, 1] ** 2, 1.0
    )

    # Ordinary Lorentzian (-+++) control, w=ct, beta_z=0.
    # Timelike iff (R k)^2 < 1; curvature is only for this comparator.
    dimensionless_speed = radius * wave_number
    timelike_margin = 1.0 - dimensionless_speed**2
    if timelike_margin <= 0.0:
        raise ValueError("Chosen helix is not timelike in the Lorentzian control.")
    gamma_squared = 1.0 / timelike_margin
    proper_curvature = radius * wave_number**2 / timelike_margin
    period = 2.0 * math.pi / wave_number

    return {
        "scope": "illustrative geometry only; not a native SAT/H(s)H solution",
        "parameters": {
            "R_length_units": radius,
            "k_inverse_length_units": wave_number,
            "z0_length_units": z0,
            "sample_count": int(parameter.size),
        },
        "parallel_leaf_readout": {
            "maximum_circle_radius_error": float(
                np.max(
                    np.abs(
                        np.sqrt(q_parallel[:, 0] ** 2 + q_parallel[:, 1] ** 2)
                        - radius
                    )
                )
            ),
            "period_length_units": period,
            "maximum_deviation_after_inverse_rotation": float(
                np.max(np.abs(q_rotated - np.array([radius, 0.0, z0])))
            ),
        },
        "radial_wavefront_readout": {
            "maximum_leaf_radius_error": float(
                np.max(np.abs(np.linalg.norm(p_radial, axis=1) - rho))
            ),
            "maximum_unit_sphere_error": float(
                np.max(np.abs(np.linalg.norm(q_radial, axis=1) - 1.0))
            ),
            "reference_trace_is_great_circle": True,
        },
        "lorentzian_minkowski_control": {
            "dimensionless_speed_Rk": dimensionless_speed,
            "timelike_margin": timelike_margin,
            "gamma_squared": gamma_squared,
            "proper_curvature_inverse_length_units": proper_curvature,
        },
        "generic_transverse_intersection_dimension": 1 + 3 - 4,
        "checks": "PASS",
    }


if __name__ == "__main__":
    try:
        print(json.dumps(run_checks(), indent=2, sort_keys=True))
    except (AssertionError, ValueError, FloatingPointError) as exc:
        raise SystemExit(f"Readout geometry check failed: {exc}") from exc
