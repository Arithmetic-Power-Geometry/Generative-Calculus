# GC-II Audit 265 — Typed Pareto interface quotient

## Scope
Audit 264 gave the complete contextual quotient for a single scalar path cost. GC-II, however, requires explicit resource/information/action/rule accounting rather than silently scalarising those coordinates. This audit lifts the boundary semantics to a nonnegative typed cost vector and identifies the exact boundary summary for componentwise budget queries. The mechanism is standard multiobjective shortest-path/Pareto theory and is **not claimed as new mathematics**. The GC-II advance is that the previously open canonical typed R/I/A/L contextual quotient is now explicit and proved complete for the stated additive typed semantics.

## Typed operational model
Fix `d>=1` typed coordinates, with the intended GC-II case `d=4` corresponding to `(R,I,A,L)`. Each admissible transition `e` has a nonnegative cost vector

`c(e) in R_+^d`.

For a finite path `p`, typed cost is componentwise additive:

`c(p)=sum_{e in p} c(e)`.

A budget is `b in R_+^d`. A path is budget-admissible exactly when `c(p) <= b` componentwise. No exchange rate between types is assumed.

For boundary states `i,j`, let `A_M(i,j)` be the set of all attainable path-cost vectors from `i` to `j`. Define its upward closure

`U_M(i,j)=A_M(i,j)+R_+^d`,

and its Pareto-minimal frontier `P_M(i,j)=Min A_M(i,j)`.

Because the graph is finite and all coordinates are nonnegative, every cyclic path can have a cycle deleted without increasing any coordinate. Hence every Pareto-minimal cost is realised by a simple path; there are finitely many simple paths, so `P_M(i,j)` is finite and `U_M(i,j)=P_M(i,j)+R_+^d`.

The **typed boundary kernel** is the family `K_M^typed=(P_M(i,j))_{i,j in B}`.

## Theorem 265.1 — typed Pareto-kernel replacement
Let `M,N` have the same labelled boundary `B`. If

`P_M(i,j)=P_N(i,j)` for every `i,j in B`,

then in every external context that touches the module only through `B`, the Pareto frontier of typed path costs between every pair of context-visible states is identical after substituting `M` for `N`.

### Proof
Take any visible-endpoint path through `C[M]` and decompose it into maximal module excursions between boundary states. For each excursion from `i` to `j` with cost vector `v`, some Pareto-minimal `p in P_M(i,j)` satisfies `p<=v`: delete cycles and, among the finite simple-path costs dominated by `v`, choose a minimal one. By kernel equality the same vector `p` is attainable in `N`. Replacing every module excursion this way produces a path in `C[N]` whose total vector is componentwise no larger. Thus every attainable vector in `C[M]` is dominated by one attainable in `C[N]`, giving inclusion of upward closures. Swap `M,N` for the reverse inclusion. Equal upward closures have equal Pareto-minimal frontiers. QED.

## Theorem 265.2 — completeness for typed budget semantics
The following are equivalent:

1. `P_M(i,j)=P_N(i,j)` for every boundary pair.
2. `U_M(i,j)=U_N(i,j)` for every boundary pair.
3. For every boundary-only external context, every visible pair `x,y`, and every typed budget `b`, `x` can reach `y` within budget `b` after gluing `M` iff it can do so after gluing `N`.

### Proof
`1 <=> 2` follows from finiteness of the Pareto antichain and upward closure. `1 => 3` follows from Theorem 265.1 because budget feasibility is exactly membership of `b` in the upward closure. For `3 => 2`, if some boundary pair has different upward closures, choose `b` in their symmetric difference. A zero-cost external source/sink probe attached to that pair makes the budget query distinguish the modules. QED.

Thus the typed Pareto boundary kernel is a complete contextual certificate for additive nonnegative vector-budget capability semantics.

## Corollary 265.3 — no scalarisation is complete in general
A single weighted sum `w dot c` cannot in general replace the typed frontier. Example: module `M` offers boundary costs `(0,2)` and `(2,0)` while `N` offers `(1,1)`. With `w=(1,1)` both have scalar optimum `2`, yet budget `(1,1)` accepts `N` and rejects `M`. Therefore any fixed scalarisation can identify modules that typed operational contexts distinguish.

This is a decisive warning for a scalar `Omega_G`: if R/I/A/L are genuinely nonexchangeable operational budgets, the primitive novelty object must retain a frontier/upward-set structure or explicitly justify a scalar utility/exchange law.

## Corollary 265.4 — typed closure is representation invariant on the quotient
For any visible start/target and typed budget `b`, budgeted operational closure is invariant under replacement by a typed-kernel-equivalent implementation. This supplies the canonical representation quotient needed before defining typed novelty gaps or reversibility defects.

## Composition
When modules are composed only through declared boundaries, their typed kernels compose by min-plus-like concatenation with vector addition followed by Pareto minimisation. Equality of typed kernels is therefore a congruence. Frontier size need not be additive or multiplicative and can grow combinatorially; no compactness claim is made.

## Checks and edge cases
- **Dimensions:** each coordinate retains its own unit; only like coordinates are added and compared. No dimensionally invalid sum across R/I/A/L types is used.
- **Zero vectors/cycles:** allowed. Removing a nonnegative cycle weakly improves cost, so a Pareto representative still has a simple-path witness (zero cycles can be removed without worsening it).
- **Unreachable boundary pairs:** represented by the empty frontier.
- **Degenerate boundary:** valid; empty/singleton boundaries carry correspondingly little transfer information.
- **Monotonicity:** adding admissible transitions can only enlarge attainable/upward sets and can only weakly improve the Pareto frontier.
- **Positive coordinate rescaling:** applying the same positive scale to a coordinate in module, context, and budgets preserves dominance and equivalence.
- **Permutation/renaming of types:** invariant when performed coherently.
- **Composition:** kernel equality is preserved by arbitrary repeated boundary-only gluing.
- **Negative typed costs:** excluded; the cycle-deletion/finiteness argument would require additional hypotheses.
- **Nonadditive resources, replenishment semantics, information revelation, stochastic outcomes, action labels, and rule generation:** not captured merely by additive edge vectors. They require a richer interface semantics and remain open.

## Exact finite verification
`experiments/gc2_audit265_typed_pareto_interface_quotient.py` exhaustively enumerates 729 directed three-state modules with boundary `{0,1}` and edge choices `absent,(0,0),(1,0)`, and 729 one-external-state contexts with visible-edge choices `absent,(0,0),(0,1)`. Each module is replaced by its complete boundary Pareto frontier (parallel frontier edges are retained). For every module/context pair the verifier checks all nine visible ordered-pair Pareto frontiers. This is **4,782,969 exact frontier equalities**. It separately checks the scalarisation collision `(0,2),(2,0)` versus `(1,1)`.

## Prior-art / novelty discipline
Multiobjective shortest-path problems, Pareto-optimal path frontiers, dominance labels, and resource-constrained shortest paths are established fields. The Pareto mechanism and dominance algebra are therefore **IMPORTED/KNOWN**. Audit 265 does not claim them as new. Its role in GC-II is to close a specific semantic gap: it proves exactly what implementation information must survive when capability budgets are typed and nonexchangeable, and it falsifies scalar boundary distance as a complete quotient for that semantics.

## Status ledger
- Finite typed Pareto frontier under finite graph + nonnegative additive vector costs: **PROVED / IMPORTED-KNOWN mechanism**.
- Typed Pareto boundary kernel sufficient for all componentwise-budget contexts: **PROVED / IMPORTED-KNOWN mechanism**.
- Typed Pareto boundary kernel necessary/complete for those contexts: **PROVED**.
- Typed budgeted-closure invariance under kernel-equivalent replacement: **PROVED**.
- Fixed scalarisation as complete R/I/A/L contextual summary: **FALSIFIED**.
- Canonical typed R/I/A/L quotient for additive nonnegative budget semantics: **PROVED**.
- Canonical quotient including nonadditive information, labelled actions, generated rules, stochasticity, or replenishable resources: **OPEN**.
- Nontrivial typed `Omega_G` bound on the richer quotient: **OPEN**.
