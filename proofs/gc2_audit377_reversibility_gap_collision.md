# GC-II Audit 377 — Reversibility-gap collision with directed metric geometry

## Scope
Branch-only Paper-II audit. GC-I foundations are unchanged.

## Setup
Fix one operational model with state/configuration set X. Let admissible protocols compose by concatenation and let protocol cost be nonnegative and additive under concatenation. Define the optimal directed conversion cost

\[
d(x,y):=\inf\{c(\pi):\pi:x\leadsto y\}\in[0,\infty],
\]

with d(x,y)=+infinity when y is unreachable from x. The empty protocol has cost 0.

## Theorem 1 — Optimal operational cost is an extended Lawvere metric
For all x,y,z:

1. d(x,x)=0.
2. d(x,z) <= d(x,y)+d(y,z).

Proof. The first claim follows from the empty protocol and nonnegativity. For the second, concatenate epsilon-optimal x->y and y->z protocols and let epsilon -> 0. If either term is infinite the inequality is immediate. QED.

**Status: PROVED, but the mathematical mechanism is IMPORTED/KNOWN.**

## Theorem 2 — Round-trip reversibility gap is ordinary symmetrization
Define

\[
\rho(x,y):=d(x,y)+d(y,x).
\]

Then rho is symmetric, rho(x,x)=0, and

\[
\rho(x,z)\le \rho(x,y)+\rho(y,z).
\]

Proof. Symmetry and the diagonal are immediate. Apply the directed triangle inequality to d(x,z) through y and independently to d(z,x) through y, then add. QED.

Thus rho is an extended pseudometric. On any finite-valued quotient that identifies x~y iff d(x,y)=d(y,x)=0, rho is a metric.

The alternative
\[
\rho_\infty(x,y)=\max\{d(x,y),d(y,x)\}
\]
is likewise the standard max symmetrization of a Lawvere/quasi-metric.

**Status: PROVED / IMPORTED-KNOWN.**

## Theorem 3 — A raw forward/backward difference is not an intrinsic GC invariant
The candidate
\[
A(x,y)=|d(x,y)-d(y,x)|
\]
is symmetric but is not, in general, a metric and is cost-unit dependent. Under a harmless change of units c' = lambda c with lambda>0,

\[
d'=\lambda d,\qquad A'=\lambda A,\qquad \rho'=\lambda\rho.
\]

Therefore neither A nor rho is dimensionless or normalization-independent.

A scale-free repair for finite nonnegative costs,
\[
a(x,y)=\frac{|d(x,y)-d(y,x)|}{d(x,y)+d(y,x)},
\]
when the denominator is positive, is invariant under positive rescaling, but it discards absolute difficulty: (1,2) and (100,200) have the same value 1/3. It also requires conventions at (0,0) and for infinite costs.

**Status: normalization-independent raw gap — FALSIFIED.**

## Degenerate and edge cases
- x=y: rho=0 and A=0.
- Distinct mutually zero-cost states: rho=0, so quotienting is required for separation.
- One-way reachability: rho may be infinite.
- Zero-cost cycles: collapse under mutual-zero quotient.
- Nonattained infima: Theorem 1 still holds by epsilon-optimal concatenation.
- Negative protocol costs: excluded; otherwise zero/negative cycles destroy the intended cost semantics.
- Noncompositional or history-dependent accounting: triangle inequality need not hold; this must be modeled explicitly rather than silently called a conversion distance.
- Vector-valued costs: no scalar d exists until an order/scalarization is fixed; different scalarizations can induce different reversibility gaps.

## Prior-art collision
The structure d(x,x)=0 plus the directed triangle inequality is exactly generalized/Lawvere metric geometry; asymmetry is allowed and standard symmetrizations recover (pseudo)metrics. Resource theories also already quantify irreversibility through forward/reverse conversion rates, formation-versus-distillation gaps, and cost/irreversibility tradeoffs.

Therefore a GC-II quantity called a "reversibility gap" is not novel merely because it compares forward and backward operational conversion cost.

## Consequence for Paper II
Target (8) survives only if GC supplies an independently defined envelope/projection obstruction that is not a function merely of d(x,y) and d(y,x), and that separates matched systems having the same directed conversion-cost matrix (or at minimum the same classical symmetrizations and forward/reverse rate summaries).

A strong next falsification test is therefore:

> Construct two finite operational systems with identical directed optimal-cost matrix d but different GC envelope/projection structure. Any proposed reversibility invariant determined solely by d must collide on this pair. A genuinely GC-specific invariant must separate them for a reason traceable to the frozen GC-I structure and must prove an operational consequence beyond ordinary directed metric/resource-theory irreversibility.

## Status ledger
- Optimal operational cost forms an extended Lawvere metric: **PROVED / IMPORTED-KNOWN**.
- Sum/max round-trip gaps are standard symmetrizations: **PROVED / IMPORTED-KNOWN**.
- Raw difference as normalization-independent invariant: **FALSIFIED**.
- Generic forward/backward reversibility gap as GC-II novelty: **FALSIFIED AS NOVEL**.
- GC-envelope-specific reversibility invariant with additional predictive content: **OPEN**.
