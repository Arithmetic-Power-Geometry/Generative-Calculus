# GC-II Audit 341 — Exact novelty of one grounded operational edge

## Status

- Single-grounded-edge novelty formula: **PROVED**.
- Exposure-weight upper bound: **PROVED, exact after removing baseline pairs**.
- Claim that one grounded edge has a context-independent capability value: **FALSIFIED**.
- Extension to several mutually composable new edges without interaction terms: **OPEN / generally unsafe**.
- Preorder/transitive-closure mechanism: **IMPORTED/KNOWN**; the GC-II contribution here is its use as an exact semantic accounting bridge.

## Setting

Let `Q` be a finite operational quotient and let `B subseteq Q x Q` be the baseline convertibility preorder (reflexive and transitive). Add exactly one newly admissible grounded macro-transition `e=(u,v)` with `(u,v) notin B`. Let

`B_e = TC(B union {(u,v)})`

be the new operational closure. Define

`Pred_B(u) = {x in Q : (x,u) in B}`

and

`Succ_B(v) = {y in Q : (v,y) in B}`.

The raw pair novelty is

`Omega_pair(e | B) = |B_e \ B|`.

## Theorem 341.1 — single-edge rectangle theorem

For every finite preorder `B` and every absent edge `(u,v)`,

`B_e \ B = (Pred_B(u) x Succ_B(v)) \ B`.

Consequently,

`Omega_pair(e | B) = |(Pred_B(u) x Succ_B(v)) \ B|`

and therefore

`Omega_pair(e | B) <= |Pred_B(u)| |Succ_B(v)| <= q^2`.

### Proof

Every pair in the displayed rectangle is reachable after adding `u->v`: move from `x` to `u` using baseline closure, traverse the new edge once, then move from `v` to `y` using baseline closure. Removing pairs already in `B` gives only novelty.

Conversely, take a pair `(x,y)` in `B_e \ B` and a finite witness path in `B union {(u,v)}`. The witness must use the new edge at least once. Consider its first occurrence. The prefix before it is entirely baseline, hence `x B u`. Consider its last occurrence. The suffix after it is entirely baseline, hence `v B y`. Thus `(x,y)` lies in `Pred_B(u) x Succ_B(v)`. This proves equality. The argument permits cycles and does not assume antisymmetry.

## Corollary 341.2 — exact semantic exposure charge

Define the contextual exposure of a grounded transition by

`X_B(u,v) = |(Pred_B(u) x Succ_B(v)) \ B|`.

Then for a single newly grounded transition,

`Omega_pair(e | B) = X_B(u,v)`.

This is a genuine bridge from a semantic action increment to generated novelty, unlike schema cardinality alone. It also shows why merely charging one grounded edge is still insufficient for a context-independent quantitative law: the same cardinality increment `Delta A_ground=1` can have radically different exposure depending on where the edge is inserted in the baseline closure.

## Sharp context dependence

If `B` is identity only, any absent edge has exposure 1. In a baseline with many predecessors of `u` and many successors of `v`, one edge can expose their Cartesian product (minus already reachable pairs). Hence the capability contribution belongs to the pair `(new transition, baseline operational geometry)`, not to the syntactic transition in isolation.

## Composition behavior and boundary

The theorem is exact for one new grounded edge. For a set of new edges, summing their baseline exposures need not be complete because a path may compose two or more new edges and create a pair lying in none of the single-edge baseline rectangles. Such cross-edge terms are the operational analogue of interaction terms. Therefore Audit 341 does **not** claim additivity.

This identifies a concrete next target for GC-II: a multi-edge expansion indexed by minimal new-edge witness sets/words, with overlap correction or a safe envelope, and a proof of when higher-order interaction terms vanish.

## Edge cases and invariances

- Empty quotient: vacuous; the theorem is stated for an edge, so `q>=2` is implicit.
- Reflexive loops are already in every preorder and therefore cannot be an absent novelty edge.
- Cycles after insertion are allowed.
- Relabelling states preserves both sides.
- Duplicating the syntax/name of the same grounded edge changes neither side.
- Quotient-equivalent representatives should be collapsed before applying the formula.
- Units: `Omega_pair` and `X_B` are counts of ordered operational-class pairs; the equation is dimensionally consistent.

## Exact verification

`experiments/gc2_audit341_single_edge_rectangle.py` enumerates every labelled preorder on `q=1,2,3,4`, every absent directed edge, computes transitive closure after insertion, and compares the exact novelty set with the predicted rectangle-minus-baseline set. It also checks the exposure upper bound and records equality/failure counts.

## Prior-art boundary

The proof uses classical preorder reachability/transitive closure and predecessor/successor sets. No novelty is claimed for that graph/order-theoretic mechanism. The GC-II result is the accounting statement: after Audit 340 showed that schema counts cannot control novelty, one grounded semantic transition admits an exact context-sensitive novelty charge, and the obstruction to extending it additively is precisely multi-transition composition.
