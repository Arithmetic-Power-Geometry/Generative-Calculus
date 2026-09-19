# GC-II Audit 252 — Exact rectangle-mode complexity of typed capability accounting

## Scope
This audit continues Audits 249–251 under the deliberately restricted but exact regime of independent typed coordinates. It asks what remains when the capability target is not rectangular.

Let the finite state space be

\[X=\prod_{j=1}^m X_j.\]

Assume typed operations are coordinate-local, have nonnegative local costs, and have no cross-type enabling, effects, synchronization, or shared cost. Let \(d_j(a,b)\) be the induced minimum local cost from \(a\) to \(b\), possibly \(+\infty\). For nonempty target \(F\subseteq X\),

\[V_F(x)=\min_{y\in F}\sum_j d_j(x_j,y_j).\]

This is the exact capability cost in the independent regime.

## Definition: target rectangle-mode complexity
A nonempty rectangle is \(R=\prod_j R_j\) with nonempty \(R_j\subseteq X_j\). Define

\[\rho(F)=\min\{q:F=R^1\cup\cdots\cup R^q,\;R^k\subseteq F\text{ rectangles}\}.\]

For two coordinates this is the standard 1-rectangle covering number / Boolean rank of the indicator matrix of F. For more coordinates it is the corresponding hyperrectangle-cover / Boolean tensor-rank notion. Therefore the combinatorial invariant itself is IMPORTED/KNOWN; GC-II novelty is not claimed for rectangle covering.

## Theorem 252.1 — exact min-plus rectangle accounting
For every rectangle cover \(F=\bigcup_{k=1}^q R^k\), with \(R^k=\prod_j R_j^k\),

\[
V_F(x)=\min_{1\le k\le q}\sum_{j=1}^m d_j(x_j,R_j^k),
\qquad
d_j(a,S)=\min_{b\in S}d_j(a,b).
\]

### Proof
Distance to a union is the minimum of distances to its members. For a rectangle, independent local dynamics imply

\[
\min_{y\in R^k}\sum_jd_j(x_j,y_j)
=\sum_j\min_{y_j\in R_j^k}d_j(x_j,y_j),
\]

because the endpoint coordinates can be selected independently. Taking the minimum over the covering rectangles gives the claim. No finiteness beyond finite state spaces is needed; extended nonnegative costs are allowed. QED.

## Theorem 252.2 — rectangle cover number is the exact universal mode count
Consider accounting representations of the form

\[
V_F(x)=\min_{1\le k\le q}\sum_j v_{jk}(x_j),\qquad v_{jk}\ge0,
\]

required to work for every independent typed system on the fixed product state space and target F. Then the smallest universally sufficient q is exactly \(\rho(F)\).

### Upper bound
Theorem 252.1 applied to a minimum rectangle cover gives q=\(\rho(F)\).

### Lower bound
The operational class contains the zero-operation system. There,

\[V_F(x)=0\text{ on }F,\qquad V_F(x)=+\infty\text{ outside }F.\]

For one nonnegative additive mode \(h_k(x)=\sum_jv_{jk}(x_j)\), its zero set is

\[
Z_k=\prod_j\{a\in X_j:v_{jk}(a)=0\},
\]

a rectangle (or empty). Since the zero set of \(\min_k h_k\) is \(\bigcup_kZ_k\), exactness forces the nonempty \(Z_k\) to cover F and none may contain a point outside F. Thus q is at least \(\rho(F)\). Together with the upper bound, q=\(\rho(F)\). QED.

## Consequences
1. Audit 250 is exactly the rank-one boundary: \(\rho(F)=1\) iff F is rectangular.
2. Target coupling need not destroy exact typed accounting; it changes the algebra from one additive law to a min-plus envelope of additive laws.
3. \(\rho(F)\) is a structural interaction count: it is the minimum number of separable capability modes required uniformly over the independent operational class.
4. This does **not** solve general GC-II accounting. Generator coupling, shared prerequisites, state-dependent cross-effects, and endogenous target changes can invalidate the independent-distance premise.
5. \(\rho(F)\) is dimensionless. The terms \(d_j\) retain the chosen cost units, so the formula is dimensionally consistent.

## Edge/degenerate cases
- F empty: capability is unreachable everywhere; exclude from rho or set rho(empty)=0 by convention. The theorem above assumes F nonempty.
- F=X: rho=1 and V=0.
- Singleton F: rho=1.
- Unreachable local endpoints: +infinity is allowed and min-plus identities remain valid.
- Zero-cost cycles: already absorbed by shortest-path pseudodistances; no problem.
- Duplicate/overlapping rectangles: allowed but never improve the minimum cover count.
- Coordinate relabeling: rho and the formula are invariant.
- State replication inside a coordinate can change raw rectangle structure unless replication is quotient-preserving; no intrinsic-world claim is made here.

## Composition behavior
For Cartesian targets F x G on disjoint coordinate blocks, rho(F x G) <= rho(F)rho(G) by taking products of cover rectangles. Equality is not asserted: Boolean-rank/rectangle-cover theory has nontrivial product behavior, so multiplicativity must not be assumed.

## Prior-art collision boundary
Rectangle covering / Boolean rank and its communication-complexity interpretation are established. In particular, the rectangle covering number is the minimum number of 1-rectangles covering the 1 entries of a Boolean matrix, and its logarithm is nondeterministic communication complexity. Accordingly:

- rectangle cover number / Boolean rank: IMPORTED/KNOWN;
- generic min-plus envelope algebra: IMPORTED/KNOWN mechanism;
- Theorems 252.1–252.2: PROVED here as the exact boundary induced by the GC-II independent typed-capability model, not claimed as invention of Boolean rank;
- extension to coupled generators as a useful complete GC capability invariant: OPEN.

## Status ledger
- Exact min-plus rectangle formula: **PROVED**.
- rho(F) sufficient number of additive modes: **PROVED**.
- rho(F) necessary for universal exact nonnegative min-of-additive accounting over the independent class: **PROVED**.
- Audit-250 rectangular theorem recovered at rho=1: **PROVED**.
- Rectangle cover / Boolean rank itself: **IMPORTED/KNOWN**.
- Multiplicativity under composition: **OPEN / not assumed**.
- Same invariant complete under coupled R/I/A/L generators: **OPEN**.

## Scientific significance for Paper II
The correct restricted accounting law is not generally additive. It is a finite tropical/min-plus envelope of additive typed costs, and the exact number of modes required in the worst operational case is controlled by target rectangle-cover complexity. This isolates target coupling quantitatively while keeping generator coupling separate. The next attack should determine whether bounded generator interaction converts this exact independent formula into a controlled approximation or requires a second interaction invariant.