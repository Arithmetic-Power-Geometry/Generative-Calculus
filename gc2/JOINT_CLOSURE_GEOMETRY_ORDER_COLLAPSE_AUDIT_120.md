# GC-II Audit 120 — Joint-Closure Geometry Order-Collapse

## Target

Test the surviving post-Audit-119 proposal: whether the *shape* of an attainable multi-resource capability set can yield a representation-independent GC-II obstruction that survives admissible resource-coordinate changes and does not reduce to Pareto/vector optimization, majorization, or ordinary resource monotones.

## Setup

Let an attainable finite resource set be

\[
K\subseteq \mathbb R^d,
\]

with the product order

\[
x\preceq y \iff x_i\le y_i\quad\forall i.
\]

Take admissible coordinate changes to include independent strictly increasing bijections/relabelings

\[
\Phi(x_1,\ldots,x_d)
=(\phi_1(x_1),\ldots,\phi_d(x_d)).
\]

This is the natural invariance class if units/scales of distinct resources are not physically privileged beyond their ordering.

## Theorem 120.1 — Product-order invariance

For every such \(\Phi\),

\[
 x\preceq y \iff \Phi(x)\preceq \Phi(y).
\]

### Proof

Each \(\phi_i\) is strictly increasing, so

\[
x_i\le y_i \iff \phi_i(x_i)\le \phi_i(y_i)
\]

for every coordinate. Taking the conjunction over all coordinates proves the claim. Strict dominance is preserved for the same reason. **Status: PROVED.**

## Corollary 120.2 — Pareto-front invariance

If \(P(K)\) denotes the set of nondominated points of \(K\), then

\[
P(\Phi(K))=\Phi(P(K)).
\]

Thus any invariant depending only on dominance/Pareto incidence survives, but it is already an order-theoretic/multiobjective object. **Status: PROVED.**

## Theorem 120.3 — Metric geometry is not intrinsic under the same invariance class

Euclidean distances, slopes, angles, convex-hull volume/area, curvature surrogates, and coordinate-additive scalarizations are generally not invariant under independent strictly increasing coordinate transformations.

A minimal witness is

\[
K=\{(0,0),(0,1),(1,0)\}.
\]

Under \(\phi_x(0,1)=(0,1)\) and \(\phi_y(0,1)=(0,2)\), the Pareto structure is unchanged, while convex-hull area changes from \(1/2\) to \(1\). Hence a purported representation-independent GC-II quantity cannot simultaneously (i) permit arbitrary monotone resource reparameterization and (ii) depend on ordinary metric shape without additional physically justified structure. **Status: PROVED BY COUNTEREXAMPLE.**

## Order-collapse conclusion

Under coordinatewise strictly increasing resource reparameterizations, the robust information carried by a finite attainable set is its induced product-order structure (and invariants derived from that structure), not its raw Euclidean geometry. Consequently:

1. A GC-II invariant built only from nondominance/Pareto incidence collides with established multiobjective/vector optimization.
2. A GC-II invariant built from metric/convex geometry is representation-dependent unless a narrower transformation group or physical metric is independently justified.
3. Simply quotienting by all monotone coordinate changes does not create a new geometric law; it collapses the candidate toward order-isomorphism data.

This is a **decisive falsification of unrestricted joint-closure geometry as standalone GC-II novelty**, not a claim that all physically structured closure geometry is impossible.

## Exhaustive finite check

`experiments/gc2_joint_closure_order_invariance_audit.py` exhaustively enumerates:

- every nonempty subset of the \(3\times3\) grid: 511 sets;
- every strictly increasing relabeling of three levels into \(\{0,1,2,3,4\}\): 10 maps per coordinate;
- all 100 coordinate-map pairs;
- total set/transformation cases: **51,100**.

Frozen output:

- dominance violations: **0**;
- Pareto-front violations: **0**;
- cases where convex-hull area changed: **39,846 / 51,100**.

Result file: `gc2/results/AUDIT_120_joint_closure_order_invariance.json`.

## Prior-art collision gate

The basic collision is with Pareto/multiobjective and vector optimization: feasible outcome sets are characterized through product-order dominance and Pareto/efficient frontiers; strictly increasing scalarizations preserve efficiency structure. Vector optimization additionally studies upper images and geometric duality. Majorization/resource theories likewise encode convertibility through order/monotone structures rather than arbitrary Euclidean coordinates.

Representative sources checked for this audit:

- Bokrantz & Fredriksson, *Necessary and sufficient conditions for Pareto efficiency in robust multiobjective optimization*, arXiv:1308.4616.
- Augusto et al., *Multiobjective Optimization Involving Quadratic Functions*, Journal of Optimization (2014).
- Buscemi & Gour, *Quantum relative Lorenz curves*, Physical Review A 95, 012110 (2017), showing majorization/Lorenz-order methods as resource-conversion criteria.

## Status ledger

| Candidate/result | Status |
|---|---|
| Product-order preservation under independent monotone coordinates | **PROVED** |
| Pareto-front preservation | **PROVED** |
| Euclidean shape invariance under the same transformations | **FALSIFIED** |
| Unrestricted joint-closure metric geometry as standalone GC-II novelty | **FALSIFIED** |
| Pareto/order-only residual | **IMPORTED/KNOWN family** |
| Geometry under independently justified physical metric / restricted transformation group | **OPEN** |

## Next surviving target

The only scientifically defensible continuation is to impose *independently motivated physical structure* on resource coordinates rather than choose it to save the theorem. The next gate should test whether a capability obstruction survives under a physically justified conversion geometry (for example a cone/gauge induced by admissible resource conversions) and whether the resulting invariant is more than a standard ordered-vector-space/resource-theory monotone, Minkowski gauge, support function, or multiobjective upper image.

No claim of breakthrough is made in this audit.
