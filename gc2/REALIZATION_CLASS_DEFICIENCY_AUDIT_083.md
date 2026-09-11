# GC-II Audit 083 — Realization-Class Closure Deficiency

## Scope
Branch-only Paper-II audit. GC-I foundations on `main` remain frozen.

## Inspected parent
`0129d6c6d3a336f209cdcf0e854e6f39a04f1e0d` (Audit 082).

## Candidate inherited from Audit 082
For a declared class `P` of physically admissible realizations,

\[
\Omega_{\mathcal P}(S\to q;B,\epsilon)
=\inf_{\rho\in\mathcal P}\;\inf_{h\in H_\rho(S\to q,\epsilon)} C_\rho(h).
\]

The hope was that a positive lower bound surviving all semantics-equivalent realizations might define a representation-independent GC-II closure deficiency.

## Result
**FALSIFIED as a standalone breakthrough invariant in this form.**

### 1. Quantifier audit — PROVED
The displayed object is not minimax. It is a nested infimum:

\[
\inf_{\rho\in\mathcal P}\inf_h C_\rho(h)
=\inf_{(\rho,h)\in\mathfrak F} C(\rho,h),
\]

where `F` is the feasible set of realization-history pairs. It is therefore simply the least implementation cost over the declared realization class. Calling it minimax would be mathematically incorrect unless an adversarial/supremum quantifier is introduced explicitly.

### 2. Class-enlargement monotonicity — PROVED
If `P_1 subseteq P_2`, then

\[
\Omega_{\mathcal P_2}\preceq \Omega_{\mathcal P_1}
\]

coordinatewise for scalar costs, or by upper-set inclusion for Pareto frontiers. Proof: enlarging the feasible realization set cannot increase an infimum. Consequently any strictly positive lower bound is conditional on exclusions encoded in `P`.

### 3. Zero-collapse theorem — PROVED
If `P` contains one admissible realization `rho_0` and history `h_0` that solves the task within `(B,epsilon)` with zero charged cost, then

\[
\Omega_{\mathcal P}=0.
\]

More generally, if there is a sequence `(rho_n,h_n)` with charged cost tending to zero, then the infimum is zero even when no zero-cost realization is attained. Thus positivity cannot follow from capability semantics alone; it must follow from physical restrictions defining the realization class.

### 4. Reparameterization invariance is insufficient — PROVED
Quotienting semantics-preserving recompilations removes duplicate descriptions but does not create a new lower bound. If two inequivalent physical realizations implement the same task at costs `c_1` and `c_2`, the quotient still selects the cheaper admissible physical realization. The numerical value remains a property of `(task, physical class, ledger, boundary conditions)`.

### 5. Pareto correction — PROVED
For typed costs `C in R_+^d`, a single vector `inf` can be ill-defined under the product order. The mathematically correct object is the nondominated lower frontier

\[
F_{\mathcal P}(S\to q)=\operatorname{Pareto}\{C_\rho(h):\rho\in\mathcal P,\ h\in H_\rho\}.
\]

Any scalar quantity requires an explicitly declared scalarization or order. This prevents silently combining incommensurate `R,I,A,L` coordinates.

## Collision check
The surviving mathematical structure is ordinary constrained implementation/resource optimization once `P`, the ledger, and boundary conditions are fixed. Complexity-constrained quantum thermodynamics already derives work/complexity tradeoffs for restricted process classes (Faist et al., PRX Quantum 6, 010346, 2025). Yadav, Caravelli & Wolpert (PNAS Nexus 5, pgag116, 2026) derive entropy-production lower bounds for physical systems running computer programs, explicitly tying cost to the physical process. Badhani & Das (APS Open Science 1, 000092, 2026) give an operational channel resource theory in which thermodynamic work capacity is characterized by a channel free-energy quantity under specified Gibbs-preserving superchannels. Zhao, Zhang & Preskill (npj Quantum Information 12, 137, 2026) additionally show that learning needed for optimal erasure can be implemented reversibly without a fundamental energy cost, reinforcing the danger of assigning positive cost to an abstract computational ingredient without a physical restriction.

These results do not prove the GC-II no-go theorem above, but they collide strongly with novelty of the generic idea that minimizing physical cost over an allowed implementation class is a new capability invariant.

## Edge-case audit
- `P` singleton: reduces to ordinary implementation optimization.
- `P` contains a free realization: zero collapse.
- Infimum not attained: positive-per-realization costs can still converge to zero.
- Empty feasible class: deficiency is infeasible/+infinity, not evidence of finite novelty.
- Ledger coordinate omitted: cost can move into the uncharged coordinate/boundary.
- Reversible implementation: logical task structure alone does not force dissipation.
- Precomputation/advice: online cost may collapse unless preparation is inside the boundary.
- Catalysts/ancillas: gross use and net consumption must be separately typed.
- Randomization: error criterion and expectation/worst-case convention must be explicit.
- Amortization: per-instance cost may vanish even when one-time setup is positive.

## Consequence for Paper II
The Audits 072–083 now support a stronger negative boundary:

> A capability-level quantity cannot acquire an architecture-independent positive physical lower bound merely by taking an infimum over a declared realization class. Positivity is inherited from the physical restrictions defining that class; enlarging the class can only lower the optimum and may drive it to zero.

This is a useful GC-II no-go theorem family, but not yet the requested positive breakthrough.

## Next surviving target
**OPEN — Relative closure deficiency between two systems under one common realization class.**

Absolute implementation cost is too class-dependent. The next defensible object should cancel shared realization overhead by comparing systems inside the same physical class, e.g. a directed relative deficiency

\[
\delta_{\mathcal P}(S\Vert T;q)
=\sup_{\lambda\in\Lambda}\left[V_{\lambda,\mathcal P}(S,q)-V_{\lambda,\mathcal P}(T,q)\right]_+,
\]

where each `V_lambda` is a dimensionally valid scalarized optimal value under identical task, boundary, error, and implementation rules. The next audit must determine whether this merely reduces to directed deficiency, simulation distance, regret, resource monotones, or Blackwell/Le Cam comparison. A GC-II claim is permitted only if a residual survives those reductions and exact finite counterexample search.

## Status table
| Claim | Status |
|---|---|
| Audit-082 expression is a minimax | FALSIFIED |
| Nested-infimum collapse | PROVED |
| Class-enlargement monotonicity | PROVED |
| Zero-collapse theorem | PROVED |
| Pareto-frontier correction | PROVED |
| Absolute realization-class deficiency is standalone GC-II novelty | FALSIFIED |
| Relative common-class closure deficiency | OPEN |
| GC-II positive breakthrough | OPEN / NOT ESTABLISHED |
