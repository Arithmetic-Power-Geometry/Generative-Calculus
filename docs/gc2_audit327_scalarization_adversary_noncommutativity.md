# GC-II Audit 327 — Scalarization–adversary noncommutativity

## Scope

This audit continues the vector-resource boundary exposed in Audit 326. It asks whether a nonnegative vector resource account may be scalarized *before* adversarial branch aggregation without changing the budget needed for a resolving policy.

The answer is no, even in a one-step finite deterministic model. The discrepancy has an exact dimension-dependent bound.

## Model

Let a fixed admissible action have a finite nonempty outcome set `Y`. For outcome `y`, continuation/resource use is a vector

\[
r_y=(r_{y1},\ldots,r_{yd})\in\mathbb R_+^d.
\]

A coordinatewise resource budget must be safe against every outcome. Its exact robust requirement is therefore

\[
R=\bigvee_{y\in Y} r_y,
\qquad
R_j=\max_{y\in Y}r_{yj}.
\]

For a strictly positive or nonnegative weight vector `w`, compare:

1. **aggregate then scalarize**
\[
A_w=w^\top R=\sum_{j=1}^d w_j\max_y r_{yj},
\]

2. **scalarize then aggregate**
\[
S_w=\max_y w^\top r_y.
\]

Both have the same scalar resource units induced by `w`.

## Theorem 327.1 — exact noncommutativity envelope

For all finite families `r_y in R_+^d` and all `w in R_+^d`,

\[
S_w\le A_w\le q S_w,
\]

where

\[
q=|\{j:w_j>0\}|\le d.
\]

If `S_w=0`, then `A_w=0`. For every `q>=1`, the factor `q` is attainable.

### Proof

For every outcome `y` and coordinate `j`, `r_{yj} <= R_j`. Hence

\[
w^\top r_y\le w^\top R=A_w.
\]

Taking the maximum over `y` gives `S_w <= A_w`.

For each coordinate `j` with `w_j>0`, choose an outcome `y_j` attaining `R_j`. Then

\[
w_jR_j\le w^\top r_{y_j}\le S_w.
\]

Summing over the `q` positively weighted coordinates gives

\[
A_w=\sum_{j:w_j>0}w_jR_j\le qS_w.
\]

If `S_w=0`, nonnegativity implies every positively weighted coordinate is zero for every outcome, so `A_w=0`.

For tightness, take `q` outcomes and, for every positively weighted coordinate `j`, let outcome `j` consume only coordinate `j` with magnitude `1/w_j`:

\[
r_j=(0,\ldots,0,1/w_j,0,\ldots,0).
\]

Then `S_w=1`, while `R_j=1/w_j` on each positively weighted coordinate, so `A_w=q`. QED.

## Corollary 327.2 — scalarization can understate simultaneous robust budget by dimension

With equal weights and `d` outcomes

\[
r_1=(M,0,\ldots,0),\ldots,r_d=(0,\ldots,0,M),
\]

we have

\[
\max_y \sum_j r_{yj}=M,
\qquad
\sum_j\max_y r_{yj}=dM.
\]

Thus scalarizing each branch before taking the adversarial maximum can understate the weighted value of the coordinatewise-safe budget by an exact factor `d`.

This is not a claim that one physical trajectory consumes `dM`: no trajectory in the construction does. The vector `(M,...,M)` is the *simultaneous coordinatewise budget reservation* needed when the same policy must remain feasible under every possible outcome and budgets cannot be transferred across coordinates after the outcome is known.

## Corollary 327.3 — when do the two operations commute?

`A_w=S_w` iff there exists an outcome `y*` that simultaneously attains every coordinate maximum with positive weight:

\[
r_{y^*j}=R_j\quad\text{for all }j\text{ with }w_j>0.
\]

Proof: sufficiency is immediate. For necessity, if `A_w=S_w`, choose an outcome attaining `S_w`. Since every term `w_j(R_j-r_{yj})` is nonnegative and their sum is zero, each term with `w_j>0` is zero.

This gives a precise operational criterion for when scalar resource accounting is safe across adversarial branches.

## Composition and edge-case audit

- **Units:** `r_j` may have different physical units; `w_j` carries reciprocal conversion units so `w_j r_j` has a common scalar unit. Without declared weights, scalarization is undefined rather than canonical.
- **Zero weights:** ignored coordinates cannot contribute; the sharp factor is support size `q`, not ambient dimension.
- **One resource:** `q=1`, so max and scalarization commute exactly.
- **One outcome:** all coordinate maxima occur on that outcome; equality holds.
- **Scaling:** multiplying all resource vectors by `lambda>=0` scales both sides by `lambda`; the ratio is invariant.
- **Adding a common action cost vector:** the one-step inequality remains valid after treating total branch vectors as `c+r_y`. The sharp `q` ratio is a worst-case envelope; a positive common offset can reduce the realized ratio.
- **Monotonicity:** enlarging any branch resource vector cannot decrease either account.
- **Policy recursion:** at a branch-relative Bellman node, coordinatewise robust feasibility uses componentwise maxima after selecting continuation policies. Replacing this by a scalar max before vector aggregation changes the semantics unless the common-maximizer criterion holds at every relevant node.

## Collision / prior-art status

The mathematical mechanism is **IMPORTED/KNOWN territory**: multiobjective dynamic programming, robust optimization, multi-cost model checking, and multicriteria shortest-path methods already distinguish vector/Pareto values from scalarized objectives. This audit does **not** claim novelty for max/sum inequalities or Pareto Bellman methods.

The GC-II contribution retained here is architectural: after Audit 326 proved that exact noncommensurable resource accounting is vector/Pareto-valued, Audit 327 gives an exact quantitative obstruction to moving an arbitrary scalarization inside adversarial outcome aggregation. It therefore constrains any proposed scalar `Delta R` in a GC-II capability bound.

## Consequence for the planned capability law

A proposed law

\[
\Omega_G\le F(\Delta R,\Delta I,\Delta A,\Delta L)
\]

cannot silently interpret `Delta R` as `max_y w^T r_y` when the intended operational semantics is simultaneous coordinatewise robust feasibility. In `d` active resource coordinates this substitution can lose a factor as large as `d`, even before interactions with information, actions/interfaces, or rules are introduced.

A defensible formulation must either:

1. retain `Delta R` as a vector/Pareto object through adversarial aggregation; or
2. declare the scalarization and aggregate the robust vector first; or
3. prove the common-maximizer condition (or another sufficient structural condition) that makes the operations commute.

## Status

- `S_w <= A_w <= q S_w`: **PROVED**.
- Sharpness of factor `q`: **PROVED**.
- Equality/common-maximizer criterion: **PROVED**.
- Universal interchange of scalarization and adversarial vector aggregation: **FALSIFIED**.
- Generic multiobjective/robust-DP mechanism: **IMPORTED/KNOWN**.
- Full Pareto Bellman recursion with branch-dependent admissibility and continuation frontiers: **OPEN for the next audit**.
