# GC-II Audit 359 — Minimum generated-operation order

## Scope

Audit 358 gives an exact exposure–interaction normal form for the new reachability created by a finite set of generated operations. This audit asks a sharper accounting question: for each newly enabled ordered capability `(x,y)`, how many generated operations are *actually necessary* in the cheapest witness, when baseline operations are free for this count?

The result is an exact stratification of closure novelty by interaction order. The underlying shortest-path mechanism is classical and is **IMPORTED/KNOWN**; the purpose here is to make the nonlinear interaction order explicit and auditable inside the GC-II accounting model.

## Setting

Let `V` be finite, `E0` the baseline directed operations, `E+={e_1,...,e_m}` the generated operations, and

`T0 = TC(E0)`, `T+ = TC(E0 union E+)`.

For `e_i=(u_i,v_i)` define baseline predecessor/successor exposures

`P_i = {u_i} union {x : (x,u_i) in T0}`,

`S_i = {v_i} union {y : (v_i,y) in T0}`.

Define the generated-operation interaction graph `H` on indices `1,...,m` by

`i ->_H j` iff `v_i=u_j` or `(v_i,u_j) in T0`.

Let `d_H(i,j)` be ordinary directed shortest-path distance in `H`, with `d_H(i,i)=0` and infinity if unreachable.

For any ordered pair `(x,y)` define its **generated-operation order**

`kappa(x,y) = min { number of E+ edges used by P : P is an x->y path in E0 union E+ }`,

with infinity if no path exists. For pairs already in `T0`, `kappa=0`.

## Theorem 359.1 — Exact interaction-order formula

For every `(x,y) notin T0`,

`kappa(x,y) = min_{i,j : x in P_i, y in S_j} [1 + d_H(i,j)]`,

where the minimum over an empty/infinite set is infinity.

### Proof

Take any `x->y` witness using at least one generated operation. List its generated operations in occurrence order `e_{i_1},...,e_{i_k}`. Before the first generated operation, only baseline operations occur, hence `x in P_{i_1}`. Between consecutive generated operations only baseline operations occur after deleting empty baseline segments, hence `i_r ->_H i_{r+1}`. After the final generated operation only baseline operations occur, hence `y in S_{i_k}`. Thus `d_H(i_1,i_k) <= k-1`, so the right-hand side is at most `k`. Minimizing over witnesses gives RHS <= `kappa`.

Conversely, choose `i,j` attaining a finite RHS and a shortest `H` path `i=i_1 -> ... -> i_k=j`, where `k=1+d_H(i,j)`. Membership `x in P_i` supplies a baseline-only prefix from `x` to `u_i`; every `H` arc supplies a baseline-only connector from the head of one generated operation to the tail of the next (possibly the empty connector when the vertices coincide); and `y in S_j` supplies a baseline-only suffix. Concatenation gives an `x->y` witness using exactly `k` generated operations. Hence `kappa <=` RHS. Equality follows.

## Corollary 359.2 — Exact novelty stratification

Define

`Delta T_k = {(x,y) : (x,y) notin T0 and kappa(x,y)=k}`,

`Omega_G^(k) = |Delta T_k|`.

Then the layers are disjoint and

`T+ \ T0 = disjoint_union_{k=1}^m Delta T_k`,

so

`Omega_G = |T+ \ T0| = sum_{k=1}^m Omega_G^(k)`.

The maximum finite `k` is at most `m`: a shortest path in the `m`-vertex interaction graph can be chosen simple. This is a structural upper bound on the nonlinear generated-operation depth, not a bound on the magnitude of `Omega_G`.

## Corollary 359.3 — Audit 358 recovered with order information

Audit 358 records whether `(x,y)` belongs to at least one exposure rectangle indexed by a reachable pair `(i,j)` in `H`. Audit 359 refines that Boolean statement by assigning the minimum number `1+d_H(i,j)` of generated operations required. Forgetting the order label and taking the union of all finite layers recovers the Audit-358 normal form.

## Edge and degenerate cases

- `E+=empty`: there are no positive-order layers and `Omega_G=0`.
- Baseline-reachable pair: `kappa=0`, so it is excluded from novelty even if a generated witness also exists.
- One generated operation: every novel pair has order 1, reproducing Audit 357.
- Redundant generated operation: it can contribute no novel pair; no positivity is inferred merely from `m>0`.
- Cycles in `E0` or `E+`: allowed. Minimum order is still well-defined because edge charges are nonnegative integers and a shortest interaction witness can be made simple in `H`.
- Self reachability is excluded consistently with Audits 357–358; the verifier compares only distinct ordered vertices.

## Dimensional and composition audit

`kappa` and the layer index `k` are dimensionless counts. `Omega_G^(k)` is a count of ordered capabilities. Adding generated operations cannot increase `kappa` for any pair, but it may move a pair from a higher layer to a lower layer; therefore individual layer counts are **not monotone** under extension, while total reachable novelty is monotone for a fixed baseline. Serial composition can add generated-operation order; parallel alternatives take a minimum, so additivity is neither assumed nor generally valid.

## Prior-art collision

Assign weight 0 to baseline edges and weight 1 to generated edges. Then `kappa(x,y)` is exactly a binary-weight shortest-path distance. The algorithmic mechanism is therefore classical 0–1 shortest path / 0–1 BFS, not a new shortest-path theorem. Dynamic transitive-closure literature likewise studies reachability under edge insertions. Accordingly:

- binary-weight shortest-path mechanism: **IMPORTED/KNOWN**;
- exact GC-II interaction-order formula as a reformulation/refinement of Audit 358: **PROVED**, but not claimed as foundational external novelty;
- claim that all generated capability is first-order: **FALSIFIED** by any serial family requiring two or more generated operations;
- use of the stratification as a GC-specific bridge to semantic generation variables `(Delta R, Delta I, Delta A, Delta L)`: **OPEN**.

## Reproducibility target

`experiments/gc2_audit359_interaction_order_verifier.py` exhaustively enumerates every three-vertex assignment in which each non-self edge is baseline, generated, or absent (`3^6=729` systems). It independently computes `kappa` by binary-weight shortest paths and by the exposure/interaction formula above, verifies equality pairwise, verifies the disjoint layer decomposition, and checks the `m` upper bound.
