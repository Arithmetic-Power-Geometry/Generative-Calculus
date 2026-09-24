# GC-II Audit 358 — exposure–interaction normal form for multi-operation closure gain

Status: PROVED where stated. Reachability/transitive-closure machinery is IMPORTED/KNOWN. No claim is made that the underlying graph-theoretic decomposition is itself novel.

## 1. Setting

Let `V` be a finite operational state set. Let `E0` be the baseline admissible transition relation and `E+` a finite set of newly grounded transitions, disjoint from `E0`. Write

\[
T_0=TC(E_0),\qquad T_+=TC(E_0\cup E_+),\qquad
\Delta T=T_+\setminus T_0,
\]

with non-reflexive transitive closure. The closure novelty count is

\[
\Omega_G=|\Delta T|.
\]

For a vertex `u`, define the reflexively completed baseline predecessor/successor exposures

\[
P_0(u)=\{u\}\cup\{x:(x,u)\in T_0\},\qquad
S_0(u)=\{u\}\cup\{y:(u,y)\in T_0\}.
\]

Audit 357 proved the one-new-edge identity. The present audit asks for the exact nonlinear interaction law for an arbitrary finite family of new operations.

## 2. New-operation interaction graph

Index the new transitions as

\[
e_i=(u_i,v_i),\qquad i=1,\dots,m.
\]

Define a directed interaction graph `H` on the new-operation indices by

\[
i\to_H j
\iff
v_i=u_j\;\text{ or }\;(v_i,u_j)\in T_0.
\]

Thus an arc in `H` means that, after using new operation `i`, baseline dynamics alone can position the system to use new operation `j`. Let `H*` denote reflexive transitive reachability on this interaction graph.

## 3. Exposure–Interaction Theorem

### Theorem 358.1 — PROVED

For every finite directed operational system,

\[
\boxed{
\Delta T
=
\left[
\bigcup_{(i,j)\in H^*}
P_0(u_i)\times S_0(v_j)
\right]\setminus T_0,
}
\]

with diagonal pairs omitted when capability is defined non-reflexively.

### Proof

Take `(x,y)` in `Delta T`. Choose an `x`-to-`y` path in `E0 union E+`. Because `(x,y)` is not in `T0`, the path uses at least one new edge. Let `e_i` be its first new edge and `e_j` its last. The prefix before `e_i` uses only baseline edges, hence `x in P0(u_i)`. Between consecutive new edges the path uses only baseline edges, so the sequence of new-edge indices is a walk in `H`; therefore `(i,j) in H*`. The suffix after `e_j` uses only baseline edges, hence `y in S0(v_j)`. This proves inclusion in the right-hand side.

Conversely, suppose `x in P0(u_i)`, `y in S0(v_j)`, and `(i,j) in H*`. A witnessing walk in `H` expands by definition into a path alternating new edges with baseline paths. Prepend a baseline path from `x` to `u_i` when needed and append one from `v_j` to `y` when needed. This yields an `x`-to-`y` path in `E0 union E+`. Removing `T0` leaves exactly the novel pairs. QED.

## 4. Quantitative capability-accounting bound

Define the exposure sizes

\[
p_i=|P_0(u_i)|,\qquad s_i=|S_0(v_i)|.
\]

By the union bound, Theorem 358.1 gives

\[
\boxed{
\Omega_G
\le
\sum_{(i,j)\in H^*}p_i s_j.
}
\]

This is generally not an equality because exposure rectangles can overlap and can contain baseline-reachable pairs. It is nevertheless a valid geometry-aware upper bound with explicit nonlinear interaction through `H*`.

A slightly sharper exact expression is the cardinality of the union after baseline subtraction; the sum is retained only as a simple computable bound.

### Corollary 358.2 (noninteracting additions) — PROVED

If `H` has no arcs between distinct new operations, then `H*` contains only `(i,i)` and

\[
\Delta T
=
\left[\bigcup_i P_0(u_i)\times S_0(v_i)\right]\setminus T_0,
\qquad
\Omega_G\le\sum_i p_i s_i.
\]

### Corollary 358.3 (single operation) — PROVED

For `m=1`, Theorem 358.1 reduces exactly to Audit 357:

\[
\Delta T=[P_0(u)\times S_0(v)]\setminus T_0.
\]

## 5. Why this repairs the failed four-delta bound

Audit 357 falsified every system-size-independent bound depending only on aggregate `(Delta R, Delta I, Delta A, Delta L)` under the tested semantics. Audit 358 identifies two missing structural quantities:

1. **exposure**: how much baseline closure is upstream/downstream of each new operation (`p_i,s_i`);
2. **interaction**: which new operations can activate one another through baseline capability (`H*`).

Thus a capability increment is not accounted for solely by how much was added. Its effect depends on where the additions attach to the existing closure and how the additions compose through it.

This is an exact finite-world statement, not a claim that exposure and interaction are universal physical resources. A future GC-II bound must justify how these structural terms relate to typed resource/information/action/rule increments.

## 6. Edge cases, invariance, and composition checks

- `E+=empty`: `H*=empty`, the union is empty, and `Delta T=empty`.
- Redundant new edge already implied by `T0`: allowed if `E+` is edge-disjoint but closure-redundant; baseline subtraction makes its contribution empty.
- Cycles among new operations: handled by transitive reachability in `H`; repeated traversal creates no additional endpoint class beyond `H*`.
- Strongly connected baseline regions: handled automatically because their members share baseline reachability exposures up to the appropriate endpoint sets.
- Relabeling vertices or new-edge indices preserves `Omega_G`, the rectangle union, and the bound.
- Adding a new operation can create new pairs in `H*`; therefore interaction is nonlinear and need not equal the sum of isolated one-edge effects.
- The theorem is dimensionless at the counting level. If capability pairs carry weights/units, the cardinality formula must be replaced by the corresponding measure; no dimensional mixing is asserted here.

## 7. Exact finite-world verification

`experiments/gc2_audit358_exposure_interaction_verifier.py` independently computes baseline and augmented transitive closures and the theorem's interaction-graph prediction.

It exhaustively checks every three-vertex assignment of each of the six possible non-self directed edges to one of three states: baseline, newly added, or absent. This is `3^6 = 729` complete `(E0,E+)` systems. It checks exact set equality, not only cardinality, and also checks the sum bound and the single-edge reduction.

## 8. Prior-art collision boundary

The decomposition is built entirely from standard directed reachability and incremental transitive-closure ideas. Dynamic transitive closure and delta maintenance are established topics, and incremental transitive-closure systems explicitly return the set of source-target pairs whose reachability changes after an insertion. Therefore:

- transitive closure / reachability: IMPORTED/KNOWN;
- incremental delta-reachability machinery: IMPORTED/KNOWN;
- interaction-graph path decomposition as generic graph theory: treated conservatively as IMPORTED/KNOWN unless a stronger literature audit establishes otherwise;
- its role as the exact structural repair of Audit 357's failed aggregate-only GC-II accounting law: PROVED within this audit chain, but not by itself claimed as foundational novelty.

## 9. Ledger

- Exact multi-operation exposure–interaction normal form: PROVED.
- Geometry-aware upper bound `Omega_G <= sum_(i,j in H*) p_i s_j`: PROVED.
- Reduction to Audit 357 for one new operation: PROVED.
- Aggregate-only four-delta bound: remains FALSIFIED under Audit 357 semantics.
- Generic graph-theoretic machinery: IMPORTED/KNOWN.
- Bound of exposure/interaction purely from `(Delta R,Delta I,Delta A,Delta L)` without baseline structure: FALSIFIED by Audit 357.
- Operational theorem connecting exposure/interaction to GC-I projection irreducibility or typed generation costs: OPEN.
- Representation-independent lower bound for computing the interaction certificate: OPEN.
