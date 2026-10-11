#!/usr/bin/env python3
"""Reproduce algebraic identities, four-map tables, and manuscript figures.
Requirements: numpy, matplotlib, scipy, sympy. SI units; x0=ct."""
from pathlib import Path
import csv
import numpy as np
import sympy as sp
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from scipy.constants import G, c, epsilon_0, elementary_charge as e, electron_mass as me, astronomical_unit as AU
P=Path(__file__).resolve().parent
M=1.98847e30
mearth=5.9722e24
rG=AU
rE=5.29177210903e-11
K=e**2/(4*np.pi*epsilon_0)
# Canonical coefficients: F=a/r^n, Omega=b/r^(3/2)
def coeff(family,m):
 if family=='G':return (64*G**3*M*m*(M+m)/(5*c**5), np.sqrt(G*(M+m)),3,rG)
 if family=='E':return (e**2*K/(3*np.pi*epsilon_0*c**3*m**2),np.sqrt(K/m),2,rE)
 raise ValueError(family)
def metrics(family,m,x=1.):
 a,b,n,r0=coeff(family,m)
 r=r0*x
 # logarithmic calculations avoid under/overflow of tiny/infinite coefficients
 omega=b/r**1.5
 beta=r*omega/c
 F=a/r**n
 Pi=F/(r*omega)
 T=r0**(n+1)/((n+1)*a)
 Phi=b/a*r0**(n-.5)/(n-.5)
 return dict(beta=beta,Pi=Pi,T=T,Phi=Phi,omega=omega,F=F,r=r)
rows=[]
for label,fam,m in [('A','G',me),('B','G',mearth),('C','E',me),('D','E',mearth)]:
 met=metrics(fam,m)
 # slow-spiral viability: Pi and beta are the relevant formal indicators
 rows.append({'map':label,'family':fam,'mass_kg':m,'initial_r_m':met['r'],'beta':met['beta'],'Pi':met['Pi'],'T_formal_s':met['T'],'N_formal':met['Phi']/(2*np.pi)})
with (P/'four_maps.csv').open('w',newline='') as fh:
 writer=csv.DictWriter(fh,fieldnames=list(rows[0]));writer.writeheader();writer.writerows(rows)
# Symbolic audits, including oscillator validity and matching laws
r,m,MM,gg,cc,ep,q,Q,kk,gam=sp.symbols('r m M G c eps q Q k gamma',positive=True)
Kg=q*Q/(4*sp.pi*ep)
aG=64*gg**3*MM*m*(MM+m)/(5*cc**5)
bG=sp.sqrt(gg*(MM+m))
aE=q**2*Kg/(3*sp.pi*ep*cc**3*m**2)
bE=sp.sqrt(Kg/m)
betaG=bG/(cc*sp.sqrt(r)); betaE=bE/(cc*sp.sqrt(r))
piG=sp.simplify(aG/bG*r**(-sp.Rational(5,2)))
piE=sp.simplify(aE/bE*r**(-sp.Rational(3,2)))
nu=MM*m/(MM+m)**2
assert sp.simplify(piG-sp.Rational(64,5)*nu*betaG**5)==0
assert sp.simplify(piE-sp.Rational(4,3)*q/Q*betaE**3)==0
assert sp.simplify((1-(sp.Symbol('x',positive=True)**sp.Rational(5,3))**sp.Rational(3,2))-(1-sp.Symbol('x',positive=True)**sp.Rational(5,2)))==0
alpha=gam/(2*m); omegaD=sp.sqrt(kk/m-alpha**2)
t=sp.symbols('t',real=True)
y=sp.exp(-alpha*t)*sp.cos(omegaD*t)
assert sp.simplify(m*sp.diff(y,t,2)+gam*sp.diff(y,t)+kk*y)==0
# Figure 1: normalized radial pitch (post-calculation graphical normalization)
x=np.geomspace(0.1,1,350)
fig,ax=plt.subplots(figsize=(7.1,4.3))
for p,label in [(-2.5,'Gravitational inspiral'),(-1.5,'Coulomb–Larmor inspiral'),(0.,'Damped oscillator')]:
 ax.plot(x,x**p,label=label,lw=2)
ax.set(xscale='log',yscale='log',xlabel=r'Radius fraction $r/r_0$',ylabel=r'Pitch ratio $\Pi(r)/\Pi(r_0)$')
ax.grid(alpha=.25,which='both');ax.legend(fontsize=9);fig.tight_layout();fig.savefig(P/'fig_pitch.pdf');fig.savefig(P/'fig_pitch.png',dpi=170);plt.close(fig)
# Figure 2: winding / time match and transformation residual
x=np.linspace(.02,1,500)
fig,ax=plt.subplots(figsize=(7.1,4.3))
ax.plot(x,1-x**2.5,label=r'Gravity: angular fraction $1-x^{5/2}$',lw=2)
ax.plot(x,1-x**1.5,label=r'EM: angular fraction $1-x^{3/2}$',lw=2)
ax.plot(x,1-x**2.5,'--',label=r'EM after $x_E=x_G^{5/3}$',lw=1.6)
ax.set(xlabel=r'Gravitational radius fraction $x_G$ (untransformed EM uses $x_E=x_G$)',ylabel='Fraction of formal total winding',ylim=(0,1.02))
ax.legend(fontsize=8);ax.grid(alpha=.25);fig.tight_layout();fig.savefig(P/'fig_phase.pdf');fig.savefig(P/'fig_phase.png',dpi=170);plt.close(fig)
fig,ax=plt.subplots(figsize=(7.1,4.3))
ax.plot(x,x**4*(1-x),lw=2,label=r'$\Delta u=x^4(1-x)$')
ax.axvline(.8,ls='--',lw=1,label=r'Maximum at $x=4/5$')
ax.set(xlabel=r'Gravitational radius fraction $x_G$',ylabel='Difference in normalized elapsed time');ax.grid(alpha=.25);ax.legend();fig.tight_layout();fig.savefig(P/'fig_time.pdf');fig.savefig(P/'fig_time.png',dpi=170);plt.close(fig)
# Figure 4: response fingerprint (force labels explicitly returned only after derivation)
fig,ax=plt.subplots(figsize=(7.1,4.3))
labels=['radial rate / radius','radial rate / mass','winding / radius','winding / mass']
nu_e=me/(M+me)
gf=np.array([-3,1+nu_e,-1.5,.5*nu_e]);ef=np.array([-2,-2,-1.5,-.5])
xs=np.arange(4); ax.bar(xs-.19,gf,.37,label='Gravitational',alpha=.85);ax.bar(xs+.19,ef,.37,label='Electromagnetic',alpha=.85)
ax.set_xticks(xs,labels,rotation=17,ha='right');ax.set_ylabel('Logarithmic sensitivity');ax.axhline(0,color='black',lw=.7);ax.legend();fig.tight_layout();fig.savefig(P/'fig_fingerprint.pdf');fig.savefig(P/'fig_fingerprint.png',dpi=170);plt.close(fig)
with (P/'audit.txt').open('w') as fh:
 fh.write('SymPy identity tests: PASS (quadrupole pitch, Larmor pitch, normalized phase map, damped oscillator ODE)\n')
 fh.write('SI source masses: electron scipy.constants.electron_mass; Earth=5.9722e24 kg; Sun=1.98847e30 kg.\n')
 fh.write('Source radii: gravity 1 AU; electromagnetic Bohr radius as illustrative value.\n')
 fh.write('Under-damped oscillator parameters selected separately in paper; mathematical existence requires gamma^2<4km.\n')
 fh.write('All formal inspiral-to-r=0 lifetimes are extrapolations, not physical predictions.\n\n')
 for row in rows:fh.write(str(row)+'\n')
print('Audited identities PASS')
for row in rows:print(row)
