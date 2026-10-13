#!/usr/bin/env python3
"""Mira audit/extension of Alberr's free tension+bending band spectrum.

Dimensionless odd-sector fixture on x in [-1/2,1/2]:
    eps*u'''' - u'' = mu*u,
    u'' = 0 and u' - eps*u''' = 0 at both ends.

This independently solves the exact characteristic equation in a stable phase
form and extends the small-eps eigenvalue expansion.  It is constitutive
mathematics, not a physical SAT/H(s)H claim.
"""

from __future__ import annotations

import math


PI = math.pi


def determinant_residual(b: float, eps: float) -> float:
    a = math.sqrt(b * b + 1.0 / eps)
    return (
        a**3 * math.tanh(a / 2.0) * math.cos(b / 2.0)
        - b**3 * math.sin(b / 2.0)
    )


def phase_residual(b: float, eps: float) -> float:
    """Equivalent stable root equation for the first odd branch.

    Writing b=pi-delta in the determinant gives
      delta = 2 atan[(b/a)^3 / tanh(a/2)],
    so the root obeys b + delta - pi = 0.
    """
    a = math.sqrt(b * b + 1.0 / eps)
    ratio = (b / a) ** 3 / math.tanh(a / 2.0)
    return b + 2.0 * math.atan(ratio) - PI


def bisect_root(residual, eps: float, iterations: int = 100) -> float:
    lo, hi = 0.0, PI
    flo, fhi = residual(lo, eps), residual(hi, eps)
    assert flo * fhi <= 0.0
    for _ in range(iterations):
        mid = (lo + hi) / 2.0
        fm = residual(mid, eps)
        if fm == 0.0:
            return mid
        if flo * fm <= 0.0:
            hi, fhi = mid, fm
        else:
            lo, flo = mid, fm
    return (lo + hi) / 2.0


def exact_mu(eps: float, use_phase: bool = True) -> float:
    if eps == 0.0:
        return PI**2
    residual = phase_residual if use_phase else determinant_residual
    b = bisect_root(residual, eps)
    return b * b + eps * b**4


def alberr_small_eps(eps: float) -> float:
    return PI**2 + PI**4 * eps - 4.0 * PI**4 * eps**1.5


def extended_small_eps(eps: float) -> float:
    """Power expansion through eps^3, excluding beyond-all-orders terms.

    Let t=sqrt(eps), b=pi-delta, and a^2=b^2+t^-2.  The stable equation gives
      delta = 2*pi^3*t^3 - 3*pi^5*t^5 - 12*pi^5*t^6 + O(t^7)
              + O(exp[-1/t]).
    Substitution into mu=b^2+t^2*b^4 yields
      mu = pi^2 + pi^4 eps - 4 pi^4 eps^(3/2)
           - 2 pi^6 eps^(5/2) + 28 pi^6 eps^3 + O(eps^(7/2))
           + beyond-all-orders boundary-layer terms.
    """
    return (
        alberr_small_eps(eps)
        - 2.0 * PI**6 * eps**2.5
        + 28.0 * PI**6 * eps**3
    )


def large_eps(eps: float) -> float:
    return 12.0 - 2.0 / (35.0 * eps)


def main() -> None:
    print("small-eps extension")
    print("eps,exact,alberr_abs_error,extended_abs_error,improvement_factor")
    for eps in (1e-2, 3e-3, 1e-3, 3e-4, 1e-4):
        exact = exact_mu(eps)
        old_error = abs(alberr_small_eps(eps) - exact)
        new_error = abs(extended_small_eps(eps) - exact)
        print(
            f"{eps:.1e},{exact:.12f},{old_error:.12e},"
            f"{new_error:.12e},{old_error/new_error:.6f}"
        )

    # Coefficient recovery: residuals approach the two derived coefficients.
    target_5 = -2.0 * PI**6
    target_6 = 28.0 * PI**6
    print(f"target_eps5over2_coefficient={target_5:.12f}")
    print(f"target_eps3_coefficient={target_6:.12f}")
    for eps in (1e-3, 3e-4, 1e-4, 3e-5, 1e-5):
        exact = exact_mu(eps)
        recovered_5 = (exact - alberr_small_eps(eps)) / eps**2.5
        five_term = alberr_small_eps(eps) - 2.0 * PI**6 * eps**2.5
        recovered_6 = (exact - five_term) / eps**3
        print(
            f"eps={eps:.1e},recovered_5={recovered_5:.9f},"
            f"recovered_6={recovered_6:.9f}"
        )

    # Independent algebraic/numerical cross-check of the exact root.
    max_root_form_delta = 0.0
    for eps in (1e-4, 1e-3, 1e-2, 0.1, 1.0, 100.0):
        m_phase = exact_mu(eps, use_phase=True)
        m_det = exact_mu(eps, use_phase=False)
        max_root_form_delta = max(max_root_form_delta, abs(m_phase - m_det))
    print(f"max_phase_vs_determinant_mu_delta={max_root_form_delta:.3e}")
    assert max_root_form_delta < 5e-13

    # Negative and limiting controls.
    assert exact_mu(0.0) == PI**2
    large_scaled = 1.0e4 * (exact_mu(1.0e4) - 12.0)
    print(f"eps0_neumann_limit={exact_mu(0.0):.12f}")
    print(
        f"large_eps_scaled_correction={large_scaled:.12f},"
        f"target={-2.0/35.0:.12f}"
    )
    assert abs(exact_mu(1.0e4) - large_eps(1.0e4)) < 2e-11
    print("boundary=asymptotic audit of a constitutive fixture; no physical claim")


if __name__ == "__main__":
    main()
