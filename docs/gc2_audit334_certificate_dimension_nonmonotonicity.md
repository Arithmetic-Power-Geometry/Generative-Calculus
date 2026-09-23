# GC-II Audit 334 — Exact-certificate dimension is not a capability monotone

## Scope
Audits 330–333 identified the minimum number of unrestricted Boolean monotones needed to characterize a finite convertibility quotient with the classical 2-dimension `dim_2(P)`: the least `k` for which `P` embeds order-reflectingly into the Boolean lattice `B_k`.

This audit asks whether that exact certificate size can itself be used as a scalar measure of *amount of capability*. The operational order is relation inclusion: an extension `P <= Q` on the same states adds allowed conversions/comparabilities and never removes an old conversion.

## Theorem 334.1 — certificate dimension is nonmonotone under capability extension
**Status: PROVED.**

There exist finite posets `P <= Q` with `dim_2(Q) > dim_2(P)`, and there also exist finite posets `P' <= Q'` with `dim_2(Q') < dim_2(P')`.

### Arbitrarily large increase
Let `P=A_q`, the `q`-element antichain, and let `Q=C_q`, any total chain on the same labelled elements. Every relation of `A_q` is present in `C_q`, so this is a pure capability extension.

By Sperner's theorem,

`dim_2(A_q) = min{k : binom(k,floor(k/2)) >= q}`.

By Boolean-lattice height,

`dim_2(C_q)=q-1`.

Hence for `q>=8`, capability extension strictly increases exact Boolean certificate dimension, and the gap

`(q-1) - min{k : binom(k,floor(k/2)) >= q}`

is unbounded. Since the antichain threshold is `Theta(log q)`, the multiplicative separation is unbounded as well.

### Strict decrease without quotient collapse
Take the three-element antichain `A_3`. Its 2-dimension is 3. Add exactly the two comparabilities `a<c` and `b<c`, leaving `a || b`. The resulting `V_3` embeds in `B_2` as

`a -> {1}, b -> {2}, c -> {1,2}`,

so `dim_2(V_3)<=2`. It cannot embed in `B_1`, which has only two elements, hence `dim_2(V_3)=2<3`.

Thus the decrease is not an artifact of merging mutually convertible states: both systems are antisymmetric posets on the same three distinct states.

## Corollary 334.2 — no novelty gap from raw certificate-count difference
**Status: PROVED.**

Neither

`dim_2(Q)-dim_2(P)`

nor its positive part can be a faithful scalar capability novelty measure under relation inclusion. A genuine capability extension may make the difference positive, zero, or negative. In particular, interpreting additional certificate coordinates as additional capability confuses *description complexity of the order* with *capability amount*.

This does not invalidate Audits 330–333: 2-dimension remains an exact complexity measure for a complete Boolean certificate of a fixed convertibility order. It only blocks its use as an order-monotone `Omega_G`.

## Domain, edge, invariance, and composition checks
- `q=1`: both antichain and chain have dimension 0.
- Small `q` need not show the increasing direction; the theorem uses the infinite family `q>=8` and exact thresholds.
- The `A_3 -> V_3` decrease preserves all states and antisymmetry.
- Relabelling states preserves 2-dimension and relation inclusion up to isomorphism.
- Product composition from Audit 333 remains valid; nonmonotonicity concerns extension of the order relation, not Cartesian product.
- The result is dimensionless and has no unit-conversion issue.

## Exact verification
`experiments/audit334_certificate_dimension_nonmonotonicity.py` uses exact integer binomial coefficients. It checks `q=1..4096`, verifies the antichain and chain formulas, records every sign of `dim_2(C_q)-dim_2(A_q)`, verifies the explicit `A_3 -> V_3` two-bit embedding and proves one-bit impossibility by cardinality, and checks that the increasing gap is unbounded over the tested family.

## Prior-art collision
**Underlying mathematics: IMPORTED/KNOWN.**

2-dimension is the classical minimum Boolean-lattice/inclusion embedding dimension of a poset. Sperner's theorem gives the antichain capacity of `B_k`, while the height of `B_k` gives the chain obstruction. Bit-vector/inclusion encodings of partial orders are established.

No claim is made that these order-theoretic facts are new. The GC-II result is the accounting boundary exposed by combining them with the operational extension semantics: exact certificate complexity is not itself a capability monotone and therefore cannot serve as `Omega_G` without additional operational structure.

## Ledger
- 2-dimension as exact unrestricted Boolean certificate size: **PROVED / IMPORTED-KNOWN** (Audit 332).
- Monotonicity of 2-dimension under added conversions: **FALSIFIED**.
- Arbitrarily large increase under extension: **PROVED**.
- Strict decrease under extension without quotient collapse: **PROVED**.
- Raw certificate-count difference as universal scalar `Omega_G`: **FALSIFIED**.
- Operationally constrained monotones whose *values* are capability-monotone while their certificate complexity is separately tracked: **OPEN**.
