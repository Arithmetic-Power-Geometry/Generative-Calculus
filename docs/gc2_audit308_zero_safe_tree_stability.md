# GC-II Audit 308 — Zero-safe quantitative stability for tree-structured capability accounts

## Question
Audit 307 proved exact reconstruction from clique marginals for decomposable models even with structural zeros. Does approximate clique agreement remain quantitatively useful without assuming a positive lower bound on separator probabilities?

## Setting
Let `T=(V,E)` be a finite rooted tree, with finite alphabets at every vertex. Let `P,Q` be probability laws that are Markov with respect to the same rooted tree, so

`P(x)=P_r(x_r) prod_{v != r} P(x_v | x_pa(v))`,

and analogously for `Q`. Conditional kernels on zero-probability parent states may be chosen arbitrarily because they carry zero mass.

Write `TV(mu,nu)=1/2 ||mu-nu||_1`. For an edge `(u,v)`, write `P_uv,Q_uv` for its pair marginals and `P_u,Q_u` for the parent marginals.

## Lemma 308.1 — weighted conditional discrepancy without positivity
For any two joint laws `P_UV,Q_UV`, there exist versions of the conditional kernels such that

`sum_u Q_U(u) TV(P_{V|u},Q_{V|u}) <= TV(P_UV,Q_UV) + TV(P_U,Q_U)`.

No lower bound on `P_U(u)` or `Q_U(u)` is required.

### Proof
For each `u`, use

`Q_U(u) |P(v|u)-Q(v|u)| <= |P_U(u)P(v|u)-Q_U(u)Q(v|u)| + |P_U(u)-Q_U(u)| P(v|u)`.

Sum over `v`, then over `u`, and divide by two. On a state with `P_U(u)=0`, choose any version of `P(.|u)`; the displayed inequality remains valid after the same direct triangle bound. QED.

## Theorem 308.2 — zero-safe tree reconstruction stability
For two finite laws Markov with respect to the same rooted tree,

`TV(P,Q) <= TV(P_r,Q_r) + sum_{v != r} [ TV(P_pa(v),v,Q_pa(v),v) + TV(P_pa(v),Q_pa(v)) ].`

### Proof
Couple the two directed factorizations sequentially. The standard telescoping/product-kernel inequality gives

`TV(P,Q) <= TV(P_r,Q_r) + sum_{v != r} E_{Q_pa(v)} TV(P_{v|pa(v)},Q_{v|pa(v)}).`

Apply Lemma 308.1 edge by edge. QED.

This proof never divides by a separator probability and therefore remains valid at structural zeros.

## Corollary 308.3 — uniform local-to-global error law
If every node marginal and every edge marginal differs by at most `epsilon` in total variation, then

`TV(P,Q) <= min(1,(2|E|+1) epsilon)`.

For a tree with `n` vertices this is `min(1,(2n-1)epsilon)`.

Because node marginals are contractions of adjacent edge marginals, one can often eliminate separately supplied node errors. For a nontrivial tree, choosing for each parent any incident edge gives the coarse edge-only consequence

`TV(P,Q) <= min(1,(2|E|+1) max_{e in E} TV(P_e,Q_e))`.

The important point is not constant optimality but **uniform stability without a minimum-mass assumption**.

## Capability consequence
Let `u` be any bounded task with range in `[0,1]`. Then

`|E_P u - E_Q u| <= TV(P,Q)`.

Hence approximate local accounting controls every bounded operational task globally:

`|E_P u-E_Q u| <= TV(P_r,Q_r) + sum_{v != r}[TV(P_pa(v),v,Q_pa(v),v)+TV(P_pa(v),Q_pa(v))]`.

This gives a quantitative, interaction-aware `F` for the tree-structured class. It is not a universal marginal-only law: Audits 304–305 already falsified such a law without structural assumptions.

## Edge and degenerate cases
- One vertex: theorem reduces exactly to `TV(P,Q)<=TV(P_r,Q_r)`.
- Identical local accounts: RHS zero, recovering Audits 306–307 exact completeness.
- Structural zeros: allowed; no inverse separator probability appears.
- Deterministic kernels: allowed.
- `epsilon=0`: exact equality.
- Large RHS: cap by the universal TV bound 1.
- Relabeling finite state symbols leaves every TV term invariant.
- Marginalization cannot increase TV, consistent with monotonicity under forgetting coordinates.

## Composition behavior
For independent products, `TV(P1 x P2,Q1 x Q2) <= TV(P1,Q1)+TV(P2,Q2)`. Thus the bound composes subadditively; additivity is neither assumed nor claimed.

## Novelty / prior-art discipline
The probability inequalities, Markov-tree factorization, total-variation contraction, and telescoping kernel argument are standard/IMPORTED mathematical machinery. No claim is made that these ingredients are new.

The GC-II advance is the boundary statement obtained after Audits 304–307: unrestricted low-order accounts can be completely misleading, while an independently justified tree operational structure yields not only exact completeness but a **zero-safe quantitative local-to-global capability bound**. This is the first current-branch quantitative repair of the failed unrestricted `Omega_G <= F(Delta R,Delta I,Delta A,Delta L)` program that does not require separator positivity.

## Status
- Lemma 308.1: **PROVED**.
- Tree TV stability theorem: **PROVED**.
- Uniform `(2|E|+1) epsilon` corollary: **PROVED**, deliberately coarse.
- Bounded-task capability bound: **PROVED**.
- Need for positive separator lower bound: **FALSIFIED for this TV formulation**.
- Optimal Lipschitz constant: **OPEN**.
- Extension to general decomposable junction trees with sharp constants: **OPEN**.
- Unrestricted fixed-order accounting: remains **FALSIFIED** by Audit 305.
