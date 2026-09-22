# GC-II Audit 332 — Exact Boolean monotone dimension boundary

## Scope
This audit continues the finite convertibility-certificate program after Audit 331.  It does **not** claim that Boolean-lattice embeddings or poset 2-dimension are new.  The purpose is to identify exactly what GC-II's unrestricted Boolean monotone count measures, and to prevent width or state-count heuristics from being mistaken for an intrinsic capability dimension.

## Setting
Let `(Q, <=)` be the finite partial order obtained by quotienting a finite operational convertibility preorder by mutual convertibility.  A Boolean monotone is a map `m: Q -> {0,1}` satisfying `x <= y => m(x) <= m(y)`.  A family `m_1,...,m_k` is **complete** when

`x <= y  iff  m_i(x) <= m_i(y) for every i`.

Write `bmd(Q)` for the minimum size of a complete Boolean-monotone family.

## Theorem 332.1 — exact representation
`bmd(Q)` is exactly the minimum `k` for which `Q` order-embeds into the Boolean lattice `B_k=(2^[k], subseteq)`.

### Proof
Given a complete family, map

`phi(x)={i : m_i(x)=1}`.

Monotonicity gives `x<=y => phi(x) subseteq phi(y)`.  Completeness gives the converse, so `phi` is an order embedding.  Conversely, from any order embedding `phi:Q -> B_k`, each coordinate indicator `m_i(x)=1[i in phi(x)]` is monotone, and reflection of subset inclusion makes the coordinate family complete.  Therefore the two minima coincide.  QED.

This parameter is classical order-theoretic territory (often called Boolean/2-dimension under closely related conventions).  Status of the mechanism: **IMPORTED/KNOWN**.  Status of the GC-II identification: **PROVED**.

## Corollary 332.2 — universal information lower bound
If `q=|Q|`, then

`bmd(Q) >= ceil(log2 q)`

because `B_k` has only `2^k` elements.  This lower bound is generally not tight because order structure, not only cardinality, constrains embeddings.

## Theorem 332.3 — chain extremum
For a chain `C_q` of `q>=1` quotient states,

`bmd(C_q)=q-1`.

### Proof
A longest chain in `B_k` has `k+1` elements, hence an embedding of `C_q` requires `k>=q-1`.  Equality is attained by the prefix chain

`emptyset subset {1} subset {1,2} subset ... subset {1,...,q-1}`.

QED.

Thus even width one can require a linear number of exact Boolean coordinates.

## Audit-331 comparison
For the `q`-element antichain `A_q`, Audit 331 established

`bmd(A_q)=min{k : binom(k,floor(k/2)) >= q}`

by Sperner's theorem.  Hence two opposite order geometries behave very differently:

* chain: `bmd=q-1`;
* antichain: `bmd=Theta(log q)`.

Therefore neither the number of quotient states nor width alone determines the minimum complete Boolean capability account.

## Decisive falsification
Candidate claim: **small width implies a small exact Boolean capability certificate.**

FALSIFIED.  The chain family has width `1` for every `q`, but `bmd(C_q)=q-1`, unbounded and linear in `q`.

A second tempting claim, **high incomparability necessarily requires more Boolean coordinates than high comparability**, is also FALSIFIED by the chain/antichain comparison: the maximally incomparable antichain needs only logarithmically many coordinates, while a total chain needs linearly many.

## Edge and invariance checks
* `q=1`: `bmd=0`; the empty coordinate family represents the one-element order.
* `q=2` chain: one coordinate is necessary and sufficient.
* Quotient invariance: duplicating mutually convertible representatives before quotienting does not change `bmd`.
* Relabelling invariance: `bmd` depends only on order isomorphism class.
* Composition warning: no additive law `bmd(P x Q)=bmd(P)+bmd(Q)` is asserted here; product behavior remains to be audited rather than assumed.

## Consequence for Paper II
A finite complete convertibility criterion can be represented by Boolean monotones exactly when the quotient order embeds into a Boolean lattice, but the minimum coordinate count is a structural embedding parameter.  GC-II must not call raw target-monotone count, width, or `ceil(log2 q)` the intrinsic capability dimension without additional operational restrictions.

The scientifically stronger next question is not existence of complete monotones (already classical), but the minimum dimension when coordinates must themselves be **operationally realizable, computable under a resource bound, local to an interface, or stable under composition**.

## Status ledger
- Complete Boolean monotones <=> Boolean-lattice order embedding: **PROVED / mechanism IMPORTED-KNOWN**.
- `bmd(C_q)=q-1`: **PROVED / classical mechanism**.
- Audit-331 antichain formula: **PROVED / Sperner mechanism IMPORTED-KNOWN**.
- Width alone bounds exact Boolean certificate dimension by a function independent of `q`: **FALSIFIED**.
- Cardinality lower bound `ceil(log2 q)`: **PROVED**, generally non-tight.
- Operationally constrained Boolean-monotone dimension: **OPEN**.
- Product/composition law: **OPEN**.
