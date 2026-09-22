# GC-II Audit 330 — Exact complete target monotones for finite operational convertibility

## Question
Can finite operational convertibility be characterized by a structured complete family of computable monotones without assuming a total order or additive scalar resource?

## Setting
Let `(X, ->)` be a finite preorder of operational objects/capability states. Reflexivity means `x -> x`; transitivity means conversions compose. Quotient by mutual convertibility, `x ~ y iff x -> y and y -> x`, when antisymmetry is desired.

For every target `t in X`, define the Boolean target monotone

`M_t(x) = 1[x -> t]`.

The codomain is `{0,1}` with the ordinary order.

## Theorem 330.1 — Complete target-monotone representation
For all `x,z in X`,

`x -> z  iff  M_t(x) >= M_t(z) for every t in X`.

### Proof
Forward direction: if `x -> z` and `M_t(z)=1`, then `z -> t`; transitivity gives `x -> t`, so `M_t(x)=1`. If `M_t(z)=0`, the inequality is automatic.

Reverse direction: assume all inequalities. Choose `t=z`. Reflexivity gives `M_z(z)=1`; hence `M_z(x)>=1`, so `M_z(x)=1`, i.e. `x -> z`. QED.

## Corollary 330.2 — quotient compression
`M_t` depends only on the mutual-convertibility class of `t`. Therefore one representative per quotient class is sufficient. If the quotient has `q` classes, a complete Boolean family of size at most `q` always exists.

## Corollary 330.3 — exact capability embedding
Define

`E(x) = { [t] : x -> t }`.

Then

`x -> z iff E(x) superseteq E(z)`.

Thus every finite operational preorder embeds exactly into a subset-inclusion order on its reachable target classes. This is an exact geometric/combinatorial representation, not a scalarization.

## Edge and degeneracy audit
- Empty `X`: vacuous; no pairwise conversion question.
- One quotient class: one constant target monotone suffices (and can be omitted if the sole relation is understood).
- Zero-cost or cyclic implementations do not affect the statement once `->` is already the certified finite-policy convertibility preorder; Audit 329 remains responsible for excluding non-well-founded pseudo-conversions.
- Mutual convertibility produces identical target vectors, exactly as required.
- Relabeling objects permutes coordinates only.
- Composition is the transitivity step in the forward proof.
- No additivity, convexity, topology, probability, or scalar exchange rate is assumed.

## Computational consequence
Given the transitive closure matrix of a finite certified conversion graph, the family is computable directly: columns of the closure matrix are the `M_t`. Conversion comparison becomes coordinatewise dominance of Boolean vectors.

This is complete but not claimed minimal. Finding the smallest separating/complete monotone family is a separate compression problem.

## Prior-art / novelty boundary
**IMPORTED/KNOWN mechanism.** Complete families of monotones are standard in resource theories, and general preorder/order embeddings by principal sets are elementary order theory. Resource-theory literature explicitly defines a complete family by `V -> W iff M_i(V) >= M_i(W)` and warns that complete families may be large. Quantum-resource-theory literature also proves that finite complete monotone families need not exist in important infinite/continuous theories. Audit 330 therefore does **not** claim a new general theorem.

The GC-II value is architectural: it supplies an exact, assumption-light answer to program item (6) for finite certified operational quotients and prevents an unnecessary search for a privileged scalar monotone. It also cleanly interfaces with Audits 326–329: vector/Pareto budget feasibility determines certified conversions; target monotones then give a complete convertibility certificate on the resulting finite preorder.

## Status
- Complete target-monotone criterion: **PROVED / IMPORTED-KNOWN mechanism**.
- One coordinate per quotient class suffices: **PROVED**.
- A single scalar monotone is universally complete: **FALSIFIED in general** (incomparability; see Audit 326 and resource-theory prior art).
- Target family is minimal: **OPEN / not claimed**.
- Polynomial-size complete family for succinct exponentially large operational state spaces: **OPEN**.
- Infinite/continuous GC-II operational spaces: **OPEN**.

## Reproducibility
`experiments/audit330_complete_target_monotones.py` exhaustively enumerates all binary relations on labelled sets of size 1–4, retains exactly the reflexive/transitive relations, and checks the theorem and quotient-column identity using integer/Boolean arithmetic only.
