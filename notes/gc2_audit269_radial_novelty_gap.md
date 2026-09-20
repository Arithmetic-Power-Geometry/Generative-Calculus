# GC-II Audit 269 — Radial Generative Novelty Gap and composition bound

## Scope
Finite conservative typed operational extensions with additive nonnegative costs in `R_+^d`. Let `B subseteq E` be baseline and extension attainable cost sets. `P(E)` denotes the Pareto-minimal extension vectors. The extended max-ratio certificate is `rho_B(q)=min_{b in B} max_i b_i/q_i`, with `0/0=0`, positive/0=`+infinity`, and empty `B` giving `+infinity`.

## Definition: radial Generative Novelty Gap
Define

`Omega_G(B,E) = max(1, max_{e in P(E)} rho_B(e))`.

This is dimensionless. It asks for the worst multiplicative radial budget expansion needed by the baseline to reproduce an extension-efficient typed tradeoff. `+infinity` is allowed.

## Theorem 1: exact quantitative Closure-Escape criterion
For finite conservative extensions,

`Omega_G(B,E) > 1` iff there exists a typed budget feasible under `E` but infeasible under `B`.

Proof. By Audit 268, escape exists iff some `e in P(E)` is not dominated by any baseline vector. By Audit 267, this is equivalent to `rho_B(e)>1`. Taking the maximum and flooring at one gives the claim.

Status: **PROVED** under the stated finite additive nonnegative semantics.

Consequences:
- `Omega_G=1` iff the extension creates no new typed budget capability.
- `Omega_G>1` gives both a novelty witness and a quantitative multiplicative severity.
- `Omega_G=+infinity` records an extension tradeoff requiring a coordinate that the baseline cannot supply at any finite common radial expansion.

## Theorem 2: order monotonicity
For fixed baseline `B`, if `B subseteq E subseteq E'`, then

`Omega_G(B,E) <= Omega_G(B,E')`.

For fixed extension `E`, if `B subseteq B' subseteq E`, then

`Omega_G(B',E) <= Omega_G(B,E)`.

Proof. Baseline enrichment can only decrease `rho`. For extension enrichment, each old Pareto point is either retained or dominated by a new point `e'<=e`; max-ratio difficulty is antitone in the budget, so `rho_B(e')>=rho_B(e)`.

Status: **PROVED**.

## Theorem 3: independent additive composition is max-submultiplicative
For two finite conservative typed systems define independent additive composition by Minkowski sum:

`B = B1 + B2`, `E = E1 + E2`.

Then

`Omega_G(B1+B2, E1+E2) <= max(Omega_G(B1,E1), Omega_G(B2,E2))`.

Proof. Let `alpha=max(Omega_1,Omega_2)`. For every extension-efficient component vector `e_j`, definition of `rho` gives a baseline witness `b_j <= alpha e_j` (with the extended-coordinate convention; finite `alpha` case). Therefore `b1+b2 <= alpha(e1+e2)`. Every composed attainable vector is a sum of component vectors, and replacing dominated component vectors by Pareto-minimal ones can only tighten the extension vector. Hence every composed Pareto vector has baseline radial certificate at most `alpha`. Infinite `alpha` is trivial.

Status: **PROVED** for independent additive/Minkowski composition.

This is a useful non-additive accounting law: independent composition cannot amplify the radial novelty factor beyond the larger component factor. It does **not** apply to coupled composition with cross-module guards, catalysts, shared replenishable resources, information revelation, or rule generation.

## Sharpness
The bound is sharp. If the second component has zero/no novelty and the first has radial gap `alpha`, composition can retain gap `alpha`. Thus the max cannot generally be replaced by a smaller universal bound.

## Invariance and edge audit
- Positive coordinate rescaling: **invariant**, since every ratio `b_i/e_i` is unchanged under coherent unit changes.
- Duplicate/dominated attainable vectors: **invariant** after Pareto reduction.
- Empty baseline with nonempty extension: `Omega_G=+infinity`.
- Degenerate `B=E`: `Omega_G=1` by the floor convention, including a zero vector.
- Zero coordinates: handled by extended ratios.
- Cost scaling by a common positive scalar: invariant.
- Conservative extension is essential to the interpretation; arbitrary replacement systems need a directed two-system comparison instead.
- Nonadditive/stochastic/replenishable semantics: **OPEN**.

## Exact verification
`experiments/gc2_audit269_radial_novelty_gap.py` exhausts all nonempty nested baseline/extension pairs over `{1,2}^2`, checks escape iff `Omega_G>1`, and checks the independent-composition max bound over every ordered pair of those nested systems. Counts: 65 nested systems and 4,225 composition comparisons. It also checks positive coordinate-rescaling invariance and explicit zero-coordinate/empty-baseline edge cases.

## Prior-art collision boundary
The max-ratio / weighted-Tchebycheff scalarization mechanism is **IMPORTED/KNOWN** from multiobjective optimization. Pareto dominance and upper-image reasoning are also established. No claim is made that radial scalarization itself is new. The GC-II candidate contribution is the specific operational interpretation as a Generative Novelty Gap together with the exact Closure-Escape threshold and its max bound under independent additive capability composition. A broader novelty claim requires literature collision checking against set indicators, resource theories, gauge/Minkowski functionals, directed deficiencies, and compositional quantitative semantics.

## Ledger
- `Omega_G` definition: **CONDITIONAL candidate** (semantics fixed; broader usefulness still under test).
- `Omega_G>1` iff finite typed Closure-Escape: **PROVED**.
- Baseline/extension monotonicity: **PROVED**.
- Positive unit-rescaling invariance: **PROVED**.
- Independent additive composition max bound: **PROVED**.
- Max-ratio scalarization mechanism: **IMPORTED/KNOWN**.
- General coupled-composition law: **OPEN**.
- Novelty relative to directed deficiencies/resource-theoretic gauges: **OPEN pending deeper collision check**.
