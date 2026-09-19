# GC-II Audit 259 — bounded-order regeneration no-go

Status: **PROVED** (finite operational systems); novelty status: **structural GC-II no-go candidate, prior-art collision still required before any novelty claim**.

## Setup
Let `U` be a finite set of required capability atoms and let

\[
C_x(T)=\inf\{c(\pi):\pi:x\leadsto z,\;T\subseteq S(z)\},\qquad T\subseteq U,
\]

with nonnegative path costs and `+infinity` when no such state is reachable.

Audit 258 showed that singleton values do not control a two-atom joint value. The question here is stronger: can all low-order regeneration costs determine or universally upper-bound a higher-order joint requirement?

## Theorem 259.1 — no bounded-order upper accounting
Fix `m >= 2`. For every `K >= 0` there is a finite nonnegative-cost operational system with `m` required atoms `U={a1,...,am}` and source `x` such that

\[
C_x(T)=0\quad\text{for every proper subset }T\subsetneq U,
\]

while

\[
C_x(U)=K.
\]

There is also a member of the same family with `C_x(U)=+infinity` and the identical complete proper-subset profile.

### Construction
Create source `x`. For every proper subset `T subsetneq U`, create a state `z_T` with semantic signature exactly `T` and a zero-cost edge `x -> z_T`. Create one full state `z_U` with signature `U`; for finite `K`, add only the edge `x -> z_U` of cost `K`; for the unreachable version add no edge to `z_U`. No other transitions are present.

Every proper requirement `T` is reachable at zero cost at `z_T`, hence `C_x(T)=0`. The only state containing all of `U` is `z_U`, so the full requirement costs exactly `K`, or is unreachable when its edge is absent. QED.

## Corollary 259.2 — all k-local data can be identical while global cost is arbitrary
For every `k >= 1`, take `m=k+1`. Then two systems can agree on **every** regeneration query of order at most `k`,

\[
(C_x(T))_{|T|\le k},
\]

but have arbitrarily different `(k+1)`-way regeneration cost, including finite-versus-infinite disagreement.

Therefore no finite universal function `F_k` of all order-`<=k` regeneration costs can upper-bound `C_x(U)` over unrestricted finite operational systems:

\[
C_x(U)\not\le F_k\big((C_x(T))_{|T|\le k}\big).
\]

This is stronger than the singleton obstruction of Audit 258: adding all pairwise, triple-wise, or any fixed bounded-order interaction terms still cannot make unrestricted capability accounting complete.

## Consequence for R/I/A/L accounting
A proposed bound

\[
\Omega_G\le F(\Delta R,\Delta I,\Delta A,\Delta L)
\]

cannot be justified merely by enriching coordinate-wise deltas with interactions up to a fixed order unless the generator/target class imposes additional structure. In an unrestricted operational class, genuinely higher-order compatibility can remain invisible to every lower-order marginal regeneration query.

This does **not** prove that useful low-order bounds are impossible under structured assumptions. It identifies the assumption that must do real work: bounded interaction width, decomposability, Helly-type structure, submodularity/closure properties, CSP-width restrictions, or another operational locality condition.

## Checks and edge cases
- `K=0`: all requirements are free; theorem remains true but has no positive gap.
- `K>0`: strict higher-order excess.
- no full edge: `C_x(U)=+infinity`.
- monotonicity is respected: if `T subseteq T'`, then `C_x(T) <= C_x(T')`.
- all edge costs are nonnegative.
- no additivity or semantic atom weighting is assumed.
- the result is invariant to atom renaming.

## Status ledger
- singleton-only universal upper accounting: **FALSIFIED** (Audit 258).
- all proper-subset costs determine full-set cost: **FALSIFIED**.
- fixed bounded-order interaction accounting is universally complete: **FALSIFIED**.
- arbitrary full-set cost with identical lower-order profile: **PROVED**.
- structured locality assumptions yielding finite-order completeness: **OPEN**.
- prior-art collision with marginal/contextuality, database join/decomposability, CSP width, Helly-type theorems, hypergraph acyclicity: **OPEN / required before novelty claim**.

## Next attack
Seek the weakest explicit operational locality condition under which order-`k` regeneration data *does* control global regeneration, and identify whether the sharp parameter is hypergraph width, treewidth, Helly number, or a genuinely GC-specific generator/target coupling invariant.