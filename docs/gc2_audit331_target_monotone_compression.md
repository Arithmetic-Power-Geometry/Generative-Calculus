# GC-II Audit 331 — Exact compression boundary for finite complete Boolean monotones

## Question
Audit 330 gave one Boolean target monotone per convertibility class. Is that family minimal, and when can it be compressed?

## Setting
Let `(X, ->)` be a finite preorder after quotienting mutual convertibility when convenient. Write

`R(x) = {t in X : x -> t}`

and for target `t`, `M_t(x)=1[x -> t]`.

For a selected target set `T subseteq X`, use only `{M_t : t in T}`.

## Theorem 331.1 — exact selected-target completeness criterion
The selected target family is complete iff

`for every x,z with x !-> z, there exists t in T with z -> t and x !-> t`.

Equivalently, define the witness set

`D(x,z)=R(z) \ R(x)`

for every ordered non-convertible pair `(x,z)`. Then `T` is complete iff it is a hitting set for all nonempty sets `D(x,z)`.

### Proof
If `x -> z`, transitivity gives `M_t(x)>=M_t(z)` for every target, hence for every selected target. For a non-conversion `x !-> z`, completeness requires at least one selected coordinate with `M_t(x)<M_t(z)`, which for Boolean target monotones is exactly `x !-> t` and `z -> t`, i.e. `t in D(x,z)`. Conversely such a witness for every non-conversion makes coordinatewise dominance equivalent to convertibility. QED.

Thus minimum target-monotone compression is exactly a finite hitting-set problem over the operational witness hypergraph `{D(x,z): x !-> z}`.

## Theorem 331.2 — Audit-330 target bound is worst-case tight
For a `q`-element antichain preorder, every complete family consisting only of target monotones requires all `q` targets.

### Proof
For an antichain, `R(z)={z}`. For every `x != z`, `D(x,z)={z}`. Any hitting set must therefore contain every `z`. Hence the minimum selected-target family has size exactly `q`. QED.

So the `q`-coordinate target construction in Audit 330 cannot be improved in the worst case *within the target-monotone class*.

## Theorem 331.3 — target monotones can nevertheless be exponentially nonminimal among arbitrary Boolean monotones
For the same `q`-element antichain, the minimum number `k` of arbitrary Boolean monotones in a complete family is

`k_min(q) = min { k : binom(k, floor(k/2)) >= q }`.

### Proof
On an antichain every Boolean function is monotone because the only required comparisons are reflexive. A complete `k`-monotone family assigns each object a bit vector in `{0,1}^k`; since distinct antichain elements must remain mutually non-convertible, their vectors must be pairwise incomparable under coordinatewise order. Sperner's theorem bounds such an antichain of bit vectors by `binom(k,floor(k/2))`, proving necessity. Conversely choose any `q` distinct vectors of Hamming weight `floor(k/2)`; they are pairwise incomparable and therefore give a complete Boolean representation. QED.

Consequently target monotones can require `q` coordinates while unrestricted Boolean complete monotones require only `Theta(log q)` coordinates on this family.

## Capability-accounting implication
A complete convertibility certificate and a compact complete certificate are different objects. Audit 330's principal-target coordinates are canonical and directly computable, but they can be exponentially redundant. The correct compression problem depends on the allowed monotone class. For target monotones it is a witness-hypergraph hitting set; for arbitrary Boolean monotones it becomes an order-embedding/compression problem.

This prevents GC-II from treating the number of Audit-330 target coordinates as an intrinsic capability dimension.

## Edge / invariance audit
- `q=1`: zero coordinates suffice if the unique relation is understood; one constant target coordinate is canonical but redundant.
- Relabeling `X` only relabels witness-hypergraph vertices and hyperedges.
- Mutual-convertibility quotienting should precede dimension claims; otherwise duplicate target columns inflate counts artificially.
- No resource scalarization, probability, topology, additivity, or convexity is assumed.
- Composition enters through transitivity in Theorem 331.1.
- The antichain construction has no hidden cost/admissibility issue: it concerns the already-certified finite convertibility preorder produced after the operational Closure-Escape layer.

## Prior-art / novelty boundary
**IMPORTED/KNOWN mechanisms.** Hitting set is classical combinatorial optimization; Sperner's theorem and embeddings of finite posets into Boolean lattices are classical order theory. General resource theory also recognizes complete families of monotones. Audit 331 therefore does not claim these mechanisms as new.

The GC-II advance is architectural and falsificatory: it proves that the canonical target family from Audit 330 is exact but not an intrinsic dimension, gives its exact compression criterion, and supplies a sharp family where target coordinates are exponentially less compact than unrestricted Boolean monotones.

## Status
- Selected-target completeness iff witness-hypergraph hitting: **PROVED**.
- `q` target coordinates worst-case necessary within target monotones: **PROVED TIGHT**.
- Audit-330 target count as intrinsic minimum capability dimension: **FALSIFIED**.
- Antichain unrestricted-Boolean minimum via Sperner bound: **PROVED / IMPORTED-KNOWN mechanism**.
- General minimum unrestricted Boolean complete-family size for arbitrary finite preorders: **OPEN here; order-embedding literature must be used rather than reinvented**.
- Operationally meaningful compressed families constrained by computability/locality/cost: **OPEN**.

## Reproducibility
`experiments/audit331_monotone_compression.py` checks the exact antichain target requirement and constructs/verifies the Sperner-optimal Boolean codes for `q=2..20` using exact integer/Boolean arithmetic.