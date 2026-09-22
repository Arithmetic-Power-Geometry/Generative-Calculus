# GC-II Audit 326 — Vector-Resource Closure-Escape Frontier

## Scope

Audit 325 established an exact scalar charged Closure-Escape value. This audit tests the first open boundary explicitly left there: whether multiple noncommensurable resource budgets can be faithfully collapsed to one scalar value without additional assumptions.

## Vector operational value

Let every admissible action carry a nonnegative resource vector `c(C,u) in R_+^d`. For a resolving policy `pi`, let its branch charge be the componentwise sum of action charges, and define its worst-case resource vector only when the operational model fixes a deterministic branch; in the general adversarial case retain the set of branch vectors. For the deterministic one-branch subclass used below, define the attainable resolving-cost set `A(C)` and its Pareto-minimal frontier `P(C)=Min(A(C))` under the componentwise order.

A budget vector `B` permits escape iff some resolving policy has cost vector `v <= B` componentwise. Thus `P(C)` is a complete budget-feasibility certificate for this subclass.

## Theorem 326.1 — exact Pareto frontier can be exponential even with two resources

For every integer `m>=1`, there is a layered deterministic operational system with `m+1` cells, two actions per layer, two resource coordinates, and exactly `2^m` resolving policies whose resource vectors are all Pareto-minimal.

Construction. At layer `i=0,...,m-1`, either action `a_i` has cost `(2^i,0)` or action `b_i` has cost `(0,2^i)`, and both deterministically advance to layer `i+1`. The last layer is terminal. A policy is identified by a subset `S` of indices on which `a_i` is chosen. Its cost is

`v(S) = ( x(S), T-x(S) )`,

where `x(S)=sum_{i in S}2^i` and `T=2^m-1`.

Binary uniqueness makes all `x(S)` distinct. For two distinct subsets with `x(S)<x(S')`, the first coordinate of `v(S)` is smaller while its second coordinate is larger. Hence neither vector dominates the other. Therefore every one of the `2^m` policies is Pareto-minimal.

**Status: PROVED.**

The construction has only `O(m)` states/actions and two resource dimensions; integer weights have at most `m` bits. Thus exact vector-resource capability accounting can require exponentially many nondominated budget thresholds even in a compact deterministic layered instance.

## Corollary 326.2 — no universal exact scalar threshold without declared scalarization

There is no order-embedding `s:R_+^2 -> R` satisfying

`u <= v componentwise  iff  s(u) <= s(v)`

on all attainable resource vectors of all such systems.

Proof. A total order on real scalars compares every pair. Componentwise resource order contains incomparable pairs, including every distinct pair in the construction above. If `s(u)<s(v)` or `s(v)<s(u)`, the reflected implication falsely asserts componentwise comparability; if `s(u)=s(v)`, both scalar inequalities hold and reflection falsely asserts both componentwise directions. QED.

**Status: PROVED.**

This does not prohibit a declared utility, exchange rate, lexicographic priority, norm, or other scalarization. It proves only that scalarization changes/forgets the native partial-order feasibility relation unless extra structure is imposed.

## Corollary 326.3 — positive weighted sums do not uniquely recover the frontier

For `w=(w1,w2)>0`, every frontier point satisfies

`w dot v(S) = w2*T + (w1-w2)x(S)`.

If `w1>w2`, the unique minimizer is `x=0`; if `w1<w2`, it is `x=T`; if `w1=w2`, all `2^m` frontier points tie. Consequently no interior frontier point is a unique optimizer of any positive linear scalarization.

**Status: PROVED.**

This is a particularly strong warning against replacing vector capability accounting by one weighted sum and then interpreting the result as complete convertibility/budget information.

## Dimensions, edge cases, monotonicity, invariance, composition

- Units: the two coordinates may have different physical/resource units; vector comparison is dimensionally valid coordinatewise. Addition is only within each coordinate. **CHECKED.**
- `m=1`: two incomparable vectors `(1,0)` and `(0,1)`. **CHECKED.**
- Zero resource coordinate values are allowed; replacing every zero by a common positive baseline per layer translates all policy vectors equally and preserves incomparability. **CHECKED.**
- Increasing a budget vector componentwise cannot destroy feasibility. **PROVED.**
- Relabelling layers/actions/resources preserves frontier cardinality. **PROVED.**
- Sequential independent composition combines attainable sets by Minkowski sum before Pareto minimization; frontier cardinalities need not add. **CHECKED; no unrestricted multiplicative/additive law claimed.**
- The theorem concerns exact frontier representation, not approximate Pareto sets. Approximation may be much smaller. **BOUNDARY.**

## Prior-art collision discipline

Multiobjective shortest-path and vector optimization already study Pareto-optimal path sets, nondominated labels, scalarization limitations, and potentially very large/exponential frontiers. Therefore the exponential-Pareto mechanism is **IMPORTED/KNOWN**, not claimed as a new combinatorial theorem. Audit 326's GC-II consequence is narrower: Audit 325's scalar `V` cannot be promoted to a universal multi-resource capability account. Paper II must either retain a Pareto/set-valued operational object or explicitly declare the scalarization/exchange structure.

## Consequence for Omega_G and capability accounting

A candidate bound `Omega_G <= F(Delta R, Delta I, Delta A, Delta L)` cannot silently treat `Delta R` as one scalar when resources are genuinely noncommensurable. At minimum, one must specify either (i) vector/Pareto resource increments and a partial-order bound, or (ii) a declared scalarization whose information loss is part of the model.

This is a decisive falsification of an unrestricted scalar-collapse route, not yet a universal Generative Novelty Gap theorem.

## Status

- Exact two-resource exponential frontier: **PROVED / mechanism IMPORTED-KNOWN**.
- Universal order-faithful scalar threshold for native vector budgets: **FALSIFIED**.
- Completeness of a single positive weighted sum: **FALSIFIED**.
- Pareto/set-valued budget feasibility as the correct exact object in the deterministic subclass: **PROVED**.
- Approximate frontier complexity under bounded dynamic range: **OPEN**.
- Full branch-adversarial vector Bellman/Pareto recursion: **OPEN**.
- Joint `Omega_G` bound over resources, information, interfaces/actions, and rules: **OPEN**.
