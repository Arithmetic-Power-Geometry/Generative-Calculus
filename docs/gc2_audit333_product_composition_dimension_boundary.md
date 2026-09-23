# GC-II Audit 333 — Product composition boundary for exact Boolean capability accounts

## Scope
This audit closes the product/composition question left OPEN by Audit 332. It concerns the finite convertibility quotient poset and its exact Boolean-monotone dimension `bmd`, already identified in Audit 332 with classical poset 2-dimension (minimum rank of a Boolean lattice admitting an order embedding). The order-theoretic mechanism is **IMPORTED/KNOWN**; the purpose here is to determine what composition laws GC-II may and may not assert.

## Setting
For finite posets `P,Q`, let `P x Q` carry the coordinatewise product order. Let `bmd(P)` be the least `k` such that `P` order-embeds into the Boolean lattice `B_k=(2^[k], subseteq)`.

Operationally, `P x Q` models independent juxtaposition of two quotient capability systems when convertibility is componentwise.

## Theorem 333.1 — universal product sandwich
For nonempty finite posets `P,Q`,

`max(bmd(P), bmd(Q)) <= bmd(P x Q) <= bmd(P)+bmd(Q)`.

### Upper bound
Take order embeddings `f:P->B_a` and `g:Q->B_b`, with `a=bmd(P)`, `b=bmd(Q)`. Relabel the Boolean coordinates so the two ground sets are disjoint. Define

`h(p,q)=f(p) union (a shifted copy of g(q))`.

Then `h(p,q) subseteq h(p',q')` iff both `f(p) subseteq f(p')` and `g(q) subseteq g(q')`, iff `p<=p'` and `q<=q'`. Hence `P x Q -> B_(a+b)` is an order embedding.

### Lower bound
Fix any `q0 in Q`. The slice `P x {q0}` is an induced subposet isomorphic to `P`; similarly `{p0} x Q` is isomorphic to `Q`. Restricting any Boolean-lattice embedding of `P x Q` to either slice yields an embedding of that factor. Therefore the product dimension is at least the larger factor dimension. QED.

Status: **PROVED / classical embedding mechanism**.

## Theorem 333.2 — additivity is false
The candidate composition law

`bmd(P x Q)=bmd(P)+bmd(Q)`

is **FALSIFIED**.

Let `A_q` denote the `q`-element antichain. The product `A_m x A_n` is the `mn`-element antichain, because coordinatewise comparability is equality in both factors. By Audit 331 / Sperner,

`bmd(A_q)=s(q):=min{k : binom(k,floor(k/2)) >= q}`.

For `m=n=3`,

`bmd(A_3)=3`, while `bmd(A_3 x A_3)=bmd(A_9)=5`.

Thus

`5 < 3+3=6`.

Independent composition can therefore share Boolean certificate coordinates; exact coordinate counts are not generally extensive.

## Theorem 333.3 — both universal bounds are sharp
The lower bound is attained whenever one factor is the singleton poset `1`: `P x 1` is isomorphic to `P`, hence

`bmd(P x 1)=bmd(P)=max(bmd(P),0)`.

The upper bound is attained on Boolean lattices. Since `B_a x B_b` is isomorphic to `B_(a+b)`, and `bmd(B_k)=k`,

`bmd(B_a x B_b)=a+b`.

To see `bmd(B_k)=k`, the identity gives the upper bound, while cardinality gives `bmd(B_k)>=log2|B_k|=k`.

Therefore no uniformly stronger bound depending only on the two factor dimensions can replace either side of the sandwich.

Status: **PROVED SHARP**.

## Corollary 333.4 — no universal additive capability-dimension accounting
Any GC-II capability account that uses unrestricted exact Boolean-monotone dimension must not assume an additive composition rule. The valid universal statement is the sharp interval

`max(a,b) <= bmd(P x Q) <= a+b`.

The realized value depends on order structure, not only on the pair `(a,b)`.

Indeed factors with the same dimensions can behave differently under products: Boolean-lattice factors attain the upper endpoint, while antichain products can be strictly subadditive.

## Edge cases and invariances
- Singleton factor: dimension zero and exact lower-bound equality.
- Relabelling: all statements are invariant under order isomorphism.
- Mutual-convertibility duplication before quotienting: irrelevant to `bmd`.
- Product associativity: repeated use gives `max_i bmd(P_i) <= bmd(prod_i P_i) <= sum_i bmd(P_i)`.
- No superadditivity or exact additivity is assumed.
- No claim is made that 2-dimension or its product behavior is new.

## Prior-art collision boundary
Audit 332 already identified `bmd` with classical poset 2-dimension / inclusion embedding into a Boolean lattice. Boolean lattices are themselves Cartesian products of two-element chains, and product posets use coordinatewise order. These are standard order-theoretic constructions. Accordingly the embedding proof and Sperner antichain mechanism are **IMPORTED/KNOWN**. GC-II's validated contribution here is architectural: it rules out an unjustified extensive composition axiom for the proposed capability-accounting layer and supplies the exact sharp universal replacement.

## Verification
`experiments/gc2_audit333_product_dimension_check.py` checks the antichain thresholds exactly for `m,n=1,...,32`, verifies the sandwich for those products, records all strict-subadditive pairs, verifies the explicit `(3,3)` counterexample, and checks Boolean-lattice upper-endpoint constructions for ranks `0,...,12`.

## Status ledger
- Product sandwich `max <= bmd(P x Q) <= sum`: **PROVED**.
- Upper and lower bounds sharp: **PROVED**.
- Universal additivity under independent product composition: **FALSIFIED**.
- Antichain product formula via Sperner threshold: **PROVED / IMPORTED-KNOWN mechanism**.
- Boolean-lattice endpoint construction: **PROVED / IMPORTED-KNOWN mechanism**.
- Operationally constrained product dimension (locality/computation/resource-limited coordinates): **OPEN**.
- Whether additional physically motivated interface constraints force an additive or approximately additive law: **OPEN**.
