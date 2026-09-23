# GC-II Audit 349 — Complete cut monotones and exact budget threshold

## Status

- Finite capability availability admits a complete family of binary obstruction monotones indexed by minimal operation cuts: **PROVED / IMPORTED-KNOWN mechanism**.
- Minimum nonnegative acquisition budget equals minimum weighted minimal-witness cost: **PROVED / IMPORTED-KNOWN shortest-path mechanism**.
- These results satisfy a structured finite complete convertibility criterion, but do **not** establish a small or polynomial monotone basis: **PROVED with complexity caveat**.
- A foundation-level novelty claim from these facts alone: **NOT CLAIMED**.

## Setup

Use Audit 348's finite baseline-contracted directed operational graph `G=(V,E)` for one ordered pair `(s,t)`, with `s != t`. `P_st` is the clutter of inclusion-minimal new-operation witness sets and `C_st=b(P_st)` the clutter of inclusion-minimal operation cuts. A supplied operation set is `S subseteq E`.

For each minimal cut `C in C_st`, define the binary cut monotone

`m_C(S) = 1[C intersects S]`.

Order supplied sets by inclusion. Then every `m_C` is monotone nondecreasing.

## Theorem 1 — complete finite cut-monotone criterion

The capability `s -> t` is available under `S` iff

`m_C(S)=1 for every C in C_st`.

Equivalently,

`available(S) = min_{C in C_st} m_C(S)`

in the nondegenerate reachable case.

### Proof

By Audit 348, failure occurs iff the missing set `D=E\\S` contains a minimal cut `C`. This is equivalent to existence of `C in C_st` with `C subseteq E\\S`, i.e. `C intersects S = empty`. Negating gives availability iff every minimal cut intersects `S`, exactly the stated criterion.

Thus the cut family is a complete set of finite binary monotones for this one-pair convertibility question. Dually, availability is equivalent to existence of `W in P_st` with `W subseteq S`.

## Theorem 2 — exact nonnegative budget threshold

Assign every new grounded operation `e` a finite acquisition cost `c_e >= 0`. For `S subseteq E`, let

`cost(S)=sum_{e in S} c_e`.

Define the minimum enabling budget

`B*(s,t)=min { cost(S) : S enables s -> t }`.

Then

`B*(s,t)=min_{W in P_st} sum_{e in W} c_e`.

### Proof

Every enabling `S` contains at least one minimal witness `W subseteq S`. Nonnegative costs imply `cost(W)<=cost(S)`, hence the optimum can be chosen minimal. Conversely every `W in P_st` enables the capability. Taking minima proves equality.

For unit costs, `B*` is exactly the minimum number of newly grounded operations in a witness. In a baseline-contracted edge graph this is the shortest `s-t` path length measured in new edges.

## Why nonnegative costs are necessary

If negative acquisition costs are admitted, an optimal enabling set may strictly contain a minimal witness merely to collect negative-cost irrelevant operations. The witness-threshold identity then fails as stated. Thus `c_e>=0` is a genuine assumption, not notation.

Zero-cost edges are allowed. If a zero-cost witness exists then `B*=0`; therefore a strict No-Free-Capability statement additionally requires that every witness contain positive total charged cost. Under that explicit condition, `B*>0`. No stronger universal no-free theorem is claimed here.

## Edge cases and invariance

- If the pair is unreachable even with all `E`, `P_st` is empty and `B*=+infinity`; the cut criterion is handled separately rather than by an empty minimum convention.
- If `s=t`, the empty path gives baseline availability and is outside novelty accounting.
- Duplicate syntax denoting one grounded operation is quotient-identified before forming `E`.
- Vertex/operation relabelling preserves the criterion and budget threshold when costs are transported with edges.
- Adding a positive-cost irrelevant operation cannot lower `B*`; adding a zero-cost irrelevant operation leaves it unchanged.
- Lowering any `c_e` cannot increase `B*`; enlarging the admissible operation set cannot increase the minimum enabling budget.
- Under disjoint serial composition of two mandatory capability modules, witness costs add. Under alternative parallel modules, the threshold is the minimum of module thresholds. General shared-edge composition need not be additive.

## Complexity and prior-art caution

The criterion is exact but can be exponentially large because `C_st` can be exponentially large relative to a compact graph. Minimal-cut/path duality, monotone Boolean minterms/maxterms, and nonnegative shortest-path optimization are classical mechanisms. They are therefore **IMPORTED/KNOWN**. This audit does not claim that GC-II invented complete monotones or shortest paths.

The scientifically relevant consequence for Paper II is narrower: GC-II now has an explicit, exact finite complete-convertibility representation and a dimensionally valid budget threshold against which any proposed compressed semantic accounting law must be tested. A claimed low-dimensional family must preserve the same yes/no boundary for all `S`, and a claimed quantitative resource charge must dominate or recover `B*` under stated assumptions.

## Next target

Seek conditions on the operational graph or on `(Delta R, Delta I, Delta A, Delta L)` under which the complete cut family admits a provably smaller representation, approximation with certified error, or dual optimization oracle without explicit blocker enumeration. Any such result must be separated from classical max-flow/min-cut, shortest-path, hypergraph transversal, simulation-preorder, and resource-theory results.