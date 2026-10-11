# Meridian | Exact Euclidean Frenet geometry repair | 11 October 2026

**Classification:** SANDBOXED, independent mathematical addendum to private hostile review 1/6. This is a constructive mathematical repair, NOT a new SAT physical law. Primary input is the exact complete 244-line McKnight manuscript \`reviews/2026-10-11_HELICAL_SCALING/PAPER_A_FULL_SOURCE.tex\` (blob \`551922f8956c8991b210ae53e60811b59b0e3232\`), especially its 'Intrinsic Euclidean differential geometry' and 'Common four-dimensional geometric representation' sections.

## 1. Exact formula, without the slow-pitch approximation

For \(\dot r=-ar^{-n}\), \(\dot\phi=br^{-3/2}\), \(X(t)=(ct,r\cos\phi,r\sin\phi,0)\), \(\beta=r\dot\phi/c\), \(\Pi=|\dot r|/(r\dot\phi)\), define

\[
H=1+\beta^2(1+\Pi^2),\quad
A=1+n\Pi^2,\quad B=\frac{\Pi}{2},
\]
\[
W=A^2+B^2+\beta^2(A+\Pi B)^2,\qquad
Z=1+\frac{5n}{2}\Pi^2+\frac{n(2n+1)}{4}\Pi^4.
\]

The exact Euclidean Frenet curvature \(\kappa\), signed torsion \(\tau\), and scale-free ratio \(h=\kappa/|\tau|\), for the stated positive \(\dot\phi\) and \(n\in\{2,3\}\), are

\[
\boxed{\kappa=\frac{\beta^2}{r}\frac{\sqrt W}{H^{3/2}},\qquad
\tau=\frac{\beta}{r}\frac{Z}{W},\qquad
h=\frac{\beta W^{3/2}}{H^{3/2}Z}.}
\]

Proof: differentiate polar frame \(e_r,e_\phi\), giving
\[
V=(c,-c\beta\Pi,c\beta),
\]
\[
A_{\mathrm{vec}}=\frac{c^2\beta^2}{r}(0,-(1+n\Pi^2),-\Pi/2),
\]
\[
J=\frac{c^3\beta^3}{r^2}\big(0,-\Pi[3/2+n(2n+1)\Pi^2],-[1+(3n/2+3/4)\Pi^2]\big).
\]
Then \(\|V\|^2=c^2H\); \(\|V\times A_{\mathrm{vec}}\|^2=c^6\beta^4 W/r^2\); \(\det(V,A_{\mathrm{vec}},J)=c^6\beta^5 Z/r^3\). Apply standard 3D Frenet formulas inside the actual affine 3-space \((ct,x,y)\). The third 4D generalized Frenet curvature remains ZERO.

## 2. Exact correction to the manuscript's asymptotic S≈Π/2

Let \(\sigma\) be Euclidean arclength and \(\mathcal S=(1/\kappa)\,dh/d\sigma\). From \(dr/d\sigma=-\beta\Pi/\sqrt H\), \(d\beta/d\ln r=-\beta/2\), \(d\Pi/d\ln r=-(n-1/2)\Pi\), chain rule gives
\[
\boxed{\frac{\mathcal S}{\Pi/2}
=\frac{W}{\sqrt H Z}
\left[
\beta\frac{\partial\ln h}{\partial\beta}
+(2n-1)\Pi\frac{\partial\ln h}{\partial\Pi}
\right].}
\]
All derivatives are taken using the explicit algebraic \(h(\beta,\Pi,n)\) above; there is no numerical differentiation required. In the limit \(\Pi\to0^+\), \(\kappa\to \beta^2/[r(1+\beta^2)]\), \(\tau\to\beta/[r(1+\beta^2)]\), \(h\to\beta\), but \(\mathcal S/(\Pi/2)\to\sqrt{1+\beta^2}\). Thus the manuscript's \(\mathcal S\simeq\Pi/2\) needs **both** \(\Pi\ll1\) **and** \(\beta\ll1\), exactly as its prose states. A low pitch alone is insufficient when the azimuthal velocity is appreciable relative to c.

The small-\(\Pi\) curvature-to-torsion ratio has the explicit local expansion
\[
h=\beta\left[1+\left(\frac n2+\frac{3}{8(1+\beta^2)}\right)\Pi^2+O(\Pi^4)\right].
\]
This gives a constructive error-control route, not a fabricated universal constant.

## 3. Independent numerical controls (dimensionless r=c=1)
| n | β | Π | κ | τ | h | exact S/(Π/2) |
|---:|---:|---:|---:|---:|---:|---:|
|2|0.00729735256|5.1812521e-7|5.324851882922e-5|0.007296963986786|0.007297352560003|1.000026625325|
|3|0.5|0.1|0.2057766443713|0.4039663275319|0.5093905861623|1.316437921651|
|3|0.5|1e-8|0.2|0.4|0.5|1.118033988750|
|2|0.1|0.03|0.009919824197859|0.09907569656764|0.1001236886696|1.011769519648|
|2|0.01|0.005|9.999531267138e-5|0.009999187533205|0.01000034376186|1.000237519059|
|3|0.8|0.01|0.3903487137958|0.487851521441|0.800138354889|1.28266967469|

Computed independently using analytic tangent/acceleration/jerk and high-precision differentiation, then a second independent closed-form logarithmic-derivative implementation verified against four fixture values. A Class P curve chart and runnable independent script were produced in the companion ChatGPT task session.

## 4. Scientific interpretation
- This repairs an **asymptotic Euclidean curve-diagnostic statement**, NOT the paper's gravitational or Coulomb equations.
- The exact derivation remains inside a 3-dimensional affine subspace of Euclidean R4 and gives no physically new 4D torsion mode. Do not relabel 3D Frenet torsion as H(s)H hyperhelical worldtube torsion.
- The Euclidean arclength/curvature are **not Lorentz invariants**. For physical SAT centerline claims, separately check \(\eta(\dot X,\dot X)=-c^2+\dot r^2+r^2\dot\phi^2\) and source approximation domains.
- If promoting into the author's paper, state the exact analytic correction and illustrate its error envelope rather than suggesting the original asymptotic formula was wrong within its advertised domain.

**Reviewer:** Meridian ◈
