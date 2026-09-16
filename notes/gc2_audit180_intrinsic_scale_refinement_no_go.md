# GC-II Audit 180 — Representation-refinement no-go for atomic intrinsic scales

Status: **PROVED boundary theorem; minimum-nonzero-increment normalization FALSIFIED.**

## Target after Audit 179
Audit 179 showed that raw heterogeneous accounting coordinates cannot support a nontrivial unit-invariant universal scalar law without intrinsic scales. A natural proposal is to derive each scale from the operational presentation itself, for example the minimum positive admissible resource increment.

## Definition
For an additive nonnegative resource coordinate R on primitive admissible transformations E, define

\[
R_{\min}(G)=\min\{r(e):e\in E,\ r(e)>0\}.
\]

For an execution p with total resource expenditure \(R(p)=\sum_{e\in p}r(e)\), define the normalized coordinate

\[
\rho_{\min}(p;G)=R(p)/R_{\min}(G).
\]

## Theorem (refinement instability)
Minimum-positive-increment normalization is not invariant under behavior- and cost-preserving refinement of the primitive action representation.

### Proof
Take a system G containing a primitive edge e from x to y with cost c>0. Construct G_k by replacing e with a chain of k primitive edges through k-1 fresh internal states, each edge having cost c/k. Hide the fresh internal states at the original interface boundary. The external transformation x->y and its total additive cost remain c.

In G,

\[
R_{\min}(G)\le c.
\]

For the one-edge system consisting only of e, \(R_{\min}(G)=c\), hence \(\rho_{\min}(x\to y;G)=1\).

In its k-refinement, \(R_{\min}(G_k)=c/k\), while the externally observed x->y execution still costs c. Therefore

\[
\rho_{\min}(x\to y;G_k)=c/(c/k)=k.
\]

The same external capability with the same total resource expenditure receives arbitrarily large normalized value solely by subdividing its implementation description. QED.

## Stronger consequence
Any proposed intrinsic scale that depends on the granularity of primitive transitions rather than an observational equivalence class is suspect. An adversary can often refine, coarsen, or introduce silent internal actions without changing externally visible closure while changing the scale.

Thus a GC-II normalization must pass at least:
1. physical unit rescaling invariance;
2. cost-preserving edge/action subdivision invariance;
3. insertion/removal of zero-cost silent internal states;
4. behaviorally equivalent state splitting/merging where the declared interface cannot observe the split.

## Surviving candidate: task-relative closure scale
For a fixed externally specified task x->y and additive resource coordinate, define

\[
R_*(x,y)=\inf_{p:x\leadsto y}R(p).
\]

When \(0<R_*(x,y)<\infty\), the ratio

\[
\rho(p\mid x,y)=R(p)/R_*(x,y)
\]

is invariant under change of physical units and under cost-preserving subdivision of paths. This is mathematically sound, but it is a relative shortest-path/stretch quantity and therefore **IMPORTED/KNOWN mechanism**, not a GC-II novelty claim. It also fails as a universal normalization when the optimum is zero or the task is unreachable.

## Edge checks
- k=1: identity refinement, ratio remains 1.
- k>1: normalized value grows exactly k in the single-edge construction.
- c=0: excluded from minimum-positive scale; zero-cost systems may leave R_min undefined.
- additional cheaper edges: choose c to be the unique minimum or refine the globally minimum positive edge; instability persists.
- nonnegative additive costs: proof requires only preservation of total cost under subdivision.
- vector resources: argument applies coordinatewise to any positive coordinate.
- integer indivisible physical quanta: refinement by c/k may be physically inadmissible; then the scale is tied to an independently justified physical quantum, not derived purely from abstract closure.

## Ledger
- Minimum positive admissible increment as intrinsic universal scale: **FALSIFIED**.
- Refinement-instability theorem: **PROVED**.
- Task-relative minimum closure cost as unit/refinement invariant scale for positive finite optimum: **PROVED / IMPORTED-KNOWN mechanism**.
- Universal normalization across zero/unreachable tasks: **OPEN**.
- Representation-invariant multi-coordinate GC accounting law stronger than shortest-path/resource monotonicity: **OPEN**.

## Next gate
Move from presentation-level atomic scales to scales defined on observational equivalence classes of complete operational behaviors. Test task-relative support/gauge normalizations under refinement, composition, zero-cost directions and Pareto tradeoffs. Any scalarization must then be collision-checked against shortest-path stretch, Minkowski gauges, multiobjective optimization and resource-theory monotones before novelty is claimed.