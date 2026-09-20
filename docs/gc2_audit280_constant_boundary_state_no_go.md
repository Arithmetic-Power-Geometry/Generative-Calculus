# GC-II Audit 280 — Constant boundary-state complexity still does not imply compact multiplicative capability certificates

## Status

**PROVED (finite operational construction).**

This audit stress-tests the conjecture left open by Audit 279: whether bounding the number of distinguishable states transmitted across every sequential boundary is sufficient to replace ambient dimension in an approximate capability-certificate bound.

It is not.

## Construction

Fix an approximation factor `alpha >= 1` and choose `r > alpha`. Let `d=2m`. Partition the typed coordinates into `m` adjacent pairs `(2j-1,2j)`.

At pair `j`, the operational system makes one local binary choice:

- choice 0 emits costs `(r,1)` on that pair;
- choice 1 emits costs `(1,r)` on that pair.

The next pair is independent of all previous choices. Thus the control state passed from one completed pair to the next can be a single constant state `q`; equivalently the boundary-state cardinality is `B=1`. If the implementation exposes within-pair phase, a fixed two-state controller suffices; in either representation `B=O(1)` independent of `m`.

The attainable family is

`Y_m = { y^sigma : sigma in {0,1}^m }`,

where every pair contains exactly one coordinate equal to `r` and one equal to `1`. Hence `|Y_m|=2^m=2^(d/2)` and all coordinates lie in the constant positive range `[1,r]`.

## Theorem — constant-state exponential certificate lower bound

For every fixed `alpha >= 1` and `r>alpha`, any attainable alpha-cover of `Y_m` by members of `Y_m` has cardinality exactly `2^m`.

### Proof

Take distinct `sigma,tau`. They differ on some pair `j`. On one coordinate of that pair, `y^sigma_i=r` while `y^tau_i=1`. Therefore

`y^sigma_i = r > alpha = alpha y^tau_i`,

so `y^sigma` does not alpha-cover `y^tau` under the GC-II directed multiplicative domination criterion `s <= alpha y` coordinatewise. Reversing the roles gives the same conclusion. Thus no distinct attainable vector can represent another; every target requires itself. Therefore every attainable alpha-certificate contains all `2^m` vectors. QED.

## Consequence

A bound on separator variable count (Audit 279) is insufficient, but even replacing it by a bound on the number of distinguishable boundary control states is still insufficient. Exponentially many mutually non-covering capability outputs can be accumulated by repeated independent local choices without transmitting any growing control memory across pair boundaries.

Therefore a positive local-to-global compression theorem must control not only boundary-state information but also the **persistent output/cost information deposited across completed modules** (or impose a compositional summary that forgets it safely). In particular, a theorem parameterized only by `(B,w,alpha,Gamma)` cannot be valid if the number of independent modules is unrestricted and their typed outputs remain globally queryable.

The missing structural quantity is closer to persistent interface/output width, factor count, or a decomposability condition on the query semantics—not merely finite-state control width.

## Edge cases and checks

- `m=0`: singleton empty output; no lower-bound content.
- `m>=1`: exactly `2^m` attainable outputs.
- `alpha=1`: any `r>1` works.
- all costs are strictly positive; zero-support discontinuity is irrelevant.
- dynamic range is constant `Gamma=r`, independent of `d`.
- the construction is monotone in the sense relevant to cost accumulation: completed pair costs are never erased.
- independent positive unit rescaling of coordinates preserves the private-witness argument when applied coherently.
- no probabilistic, asymptotic, or floating-point assumption is used.

## Prior-art collision note

The combinatorial ingredients are not claimed as new: finite-state/regular systems can generate exponentially many length-n words, and exponential antichain growth is known even for regular languages; multiobjective optimization likewise has exponentially large Pareto sets. The GC-II contribution of this audit is the negative operational implication for the proposed capability-accounting theorem: **constant control-state boundary complexity does not imply compact multiplicative capability certification when independent local choices leave persistent typed outputs.**

## Ledger

- `constant boundary-state cardinality => compact alpha-certificate`: **FALSIFIED**.
- constant-state, constant-dynamic-range exponential family: **PROVED**.
- necessity of additionally controlling persistent output/query structure for the proposed theorem family: **PROVED as a requirement against this counterfamily**.
- a sufficient compositional/decomposability condition: **OPEN**.
