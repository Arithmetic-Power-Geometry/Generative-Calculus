# GC-II Audit 281 — Bounded dependency treewidth alone does not compress capability certificates

## Status

**PROVED (finite typed operational semantics).**

This audit sharpens Audits 277–280.  It tests a natural rescue hypothesis suggested by CSP/database/graphical-model methodology: perhaps bounded treewidth of the local dependency graph is enough to replace ambient objective dimension in an approximate capability certificate bound.  It is not.

## Setup

Fix a multiplicative tolerance `alpha >= 1` and choose `r > alpha`.  Let `m >= 1` and `d=2m`.  Partition the typed output coordinates into disjoint pairs

`P_j={2j-1,2j}`, `j=1,...,m`.

Module `j` independently chooses one of two admissible local transformations:

* choice 0 deposits typed cost `(r,1)` on `P_j`;
* choice 1 deposits typed cost `(1,r)` on `P_j`.

There are no cross-module guards, resources, or state dependencies.  Hence the coordinate dependency graph is exactly the matching

`G_m = disjoint_union_{j=1}^m K_2`.

For `m>=1`, `tw(G_m)=1`: bags `P_j` have size two and may be connected arbitrarily into a decomposition tree; because the pairs are disjoint, the running-intersection condition is immediate.  (If isolated-coordinate conventions are used, they do not change the bound.)

For each bit string `sigma in {0,1}^m`, let `y^sigma` be the resulting typed cost vector.  Thus `|Y_m|=2^m`.

We use the same attainable representative convention as Audits 275–280: an `alpha`-certificate is a subset `C subseteq Y_m` such that for every target `y in Y_m` there exists `c in C` with `c_i <= alpha y_i` for every coordinate `i`.

## Theorem 281.1 — Treewidth-one exponential certificate family

For every finite `alpha>=1`, every `m>=1`, and every `r>alpha`, the operational family above has dependency treewidth one but every attainable `alpha`-certificate has cardinality

`|C| = 2^m = 2^(d/2)`.

### Proof

Take distinct `sigma,tau`.  Some module `j` has `sigma_j != tau_j`.  On one coordinate of `P_j`, `y^sigma` has value `r` while `y^tau` has value `1`.  Since `r>alpha`,

`y^sigma_i = r > alpha * 1 = alpha y^tau_i`.

Therefore `y^sigma` cannot alpha-represent `y^tau`.  Reversing the roles gives the converse obstruction on the other coordinate of the same pair.  Thus no attainable vector alpha-represents any distinct attainable vector.  Every target must occur in the certificate itself, so `|C|=|Y_m|=2^m`.  The dependency graph is a matching and has treewidth one. QED.

## Corollary 281.2 — Several graph-width-only rescue hypotheses fail

The same family has maximum degree one, component size two, no cycles, and a tree decomposition with bags of size two.  Consequently, no uniform certificate-size bound of the form

`|C_alpha(Y)| <= f(alpha, Gamma, tw(G)) * poly(d)`

can hold for this semantics when `Gamma` is a fixed positive dynamic-range bound and the bound ignores the number of independently persistent typed output blocks: choose fixed `r>alpha`, hence fixed `Gamma=r`, while `tw(G)=1` and `|C|=2^(d/2)`.

This statement concerns the explicit typed-output certificate semantics above.  It does **not** claim that treewidth is useless for computation in general; treewidth is a powerful algorithmic parameter when the dynamic-programming state passed through a decomposition captures all information relevant to the query.

## What the counterexample identifies

Audits 279–280 showed that small control separators and even one boundary control state do not suffice, because local choices can be deposited into persistent typed outputs.  Audit 281 shows that replacing those notions by ordinary dependency-treewidth still misses the same phenomenon.  A viable structural theorem must control not only local dependency topology but also how many independently queryable distinctions survive in the external capability interface.

A candidate parameter must therefore charge persistent interface information (or quotient it by the downstream query family).  Merely counting local graph separators is insufficient.

## Edge and invariance checks

* `m=1`: two targets; treewidth one; both representatives are necessary.
* `alpha=1`: any `r>1` works.
* finite `alpha`: choose any rational/integer `r>alpha`.
* no zero coordinates occur.
* positive dynamic range is constant (`Gamma=r`) for fixed alpha/r.
* independent positive unit rescaling of each typed coordinate preserves every ratio and the non-cover relation.
* adding dominated attainable vectors cannot remove the private-witness obstruction among the displayed vectors unless new attainable representatives capable of covering multiple targets are explicitly introduced; the theorem is for the constructed attainable set.

## Novelty / prior-art boundary

**IMPORTED/KNOWN:** treewidth and tree decompositions; exponentially large nondominated/approximate Pareto phenomena as objective dimension grows; decomposition methods in CSP/database/multiobjective optimization.

**GC-II result:** the exact operational no-go obtained by combining a treewidth-one local dependency system with persistent typed capability outputs: bounded ordinary dependency treewidth, even together with constant local degree and constant dynamic range, does not by itself bound attainable multiplicative capability-certificate size.

This is a structural falsification, not a claim that the underlying graph-theoretic or Pareto ingredients are new.

## Next target

Define a **query-relative persistent interface width**: the maximum number (or log-number) of inequivalent partial-output summaries across a decomposition cut under the downstream budget-query family.  Test whether bounded such width plus bounded positive log-scale range yields an FPT-style certificate/decision procedure.  Before promoting it, collision-test against Myhill–Nerode style state complexity, communication complexity, database/CSP width, branching programs, and multiobjective dynamic programming.
