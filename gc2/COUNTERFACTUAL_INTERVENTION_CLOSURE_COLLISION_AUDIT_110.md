# GC-II Audit 110 — Counterfactual Intervention Closure Collision

## Question
Can the post-Audit-109 survivor be made novel by defining capability as the minimum typed cost required to expand the admissible intervention/context family until a previously unavailable operational distinction becomes realizable?

## Result
**Decisive collision in the fixed-distinction regime.** If each admissible intervention has a fixed cost and resolves a fixed subset of currently unresolved operational distinctions, minimum-cost intervention closure is exactly weighted set cover (equivalently weighted hitting set after dualization). Thus the generic construction is not a new GC-II law.

Let `U` be the finite set of distinctions required by a target capability and let intervention `i` expose `S_i subseteq U` at cost `c_i >= 0`. Define

`C*(U) = min { sum_{i in J} c_i : union_{i in J} S_i contains U }`.

This is the weighted set-cover objective by identity of feasible sets and objective. In the causal-identification specialization, modern optimal experiment-design work explicitly reduces minimum-cost intervention selection to minimum hitting set and proves NP-completeness in the general problem. In active automata learning, distinguishing experiments/queries and adaptive distinguishing sequences are likewise established machinery.

## Exact finite audit
`experiments/gc2_intervention_closure_hitting_set_audit.py` independently computes (a) minimum intervention-closure cardinality and (b) minimum set-cover cardinality for every nonempty family of nonempty subsets of universes of size 1 through 4.

Exact local run before commit:

- total families checked: **32,902**
- solvable families: **32,412**
- equality violations: **0**

The checker contains assertions for these totals and zero violations.

## Theorem 110.1 — Fixed intervention closure = set cover
For finite `U`, fixed intervention effects `S_i`, and nonnegative intervention costs `c_i`, the minimum cost of expanding the available intervention family sufficiently to realize all distinctions in `U` equals the optimum of weighted set cover on `(U,{S_i},c)`.

**Status: PROVED / IMPORTED-KNOWN mechanism.** Proof is definitional equivalence of feasible intervention subsets and set covers, not a new theorem source.

## Corollary 110.2 — Static Omega_G collision
Any proposed `Omega_G` defined solely as the minimum cost of a static family of interventions whose fixed distinction sets cover a target unresolved-distinction set is a set-cover/hitting-set quantity. Nonlinear post-processing of this optimum does not create a new operational invariant.

**Status: FALSIFIED as standalone GC-II novelty.**

## Adaptive extension
If intervention outcomes change the remaining hypothesis/distinction set and later intervention choice depends on earlier outcomes, the object becomes an adaptive experiment/query policy or decision tree. This escapes static set cover but collides with active learning, adaptive experiment design, causal intervention design, and sequential decision theory. Therefore adaptivity alone is not sufficient novelty.

**Status: IMPORTED/KNOWN mechanism; GC-II novelty OPEN only beyond these reductions.**

## Edge/degenerate checks
- `U=empty`: optimum is zero.
- no covering intervention family: target closure is unreachable (`+infinity`/undefined depending codomain convention).
- zero-cost interventions: allowed; no positive No-Free-Capability theorem follows without an independent positivity assumption.
- duplicate/aliased interventions: do not alter the optimum; raw action/intervention cardinality remains non-invariant.
- monotonicity: enlarging the available intervention family cannot increase optimum cost; enlarging the required distinction set cannot decrease it.
- composition: independent subproblems are additive only when interventions cannot jointly cover distinctions across components; generic additivity is false.
- weighted typed budgets: scalarization produces weighted cover; a Pareto/vector budget produces multiobjective cover/packing structure rather than a new conservation law by itself.

## Prior-art collision gate
This route must be treated as known unless a candidate survives at least:

1. weighted set cover / hitting set and submodular cover;
2. optimal causal experiment design and intervention identification;
3. active automata learning, distinguishing sequences, and query complexity;
4. adaptive experimental design / sequential decision policies;
5. Blackwell comparison when interventions merely alter informativeness;
6. resource-theoretic monotones when intervention cost is itself declared a resource.

## Surviving target
The next viable object cannot be merely “minimum intervention cost to expose a distinction.” A candidate must have **endogenous intervention effects**: executing an intervention must change the future *space of admissible interventions/distinctions itself*, and the proposed quantitative obstruction must remain after compiling that process into (i) adaptive decision trees/policies, (ii) causal experiment design, (iii) active query learning, and (iv) ordinary resource-constrained reachability. The key kill test is whether the full endogenous process admits a faithful polynomial-overhead reduction to one of those models. If yes, the route is not the GC-II breakthrough.

## Status ledger
- fixed finite intervention closure formulation: **PROVED**
- equality with weighted set cover/hitting set: **PROVED / IMPORTED-KNOWN**
- exact exhaustive finite checker: **NUMERICALLY SUPPORTED (exact enumeration)**
- static intervention-cost `Omega_G`: **FALSIFIED as standalone novelty**
- adaptivity as novelty by itself: **FALSIFIED / IMPORTED-KNOWN mechanism**
- endogenous intervention-space deformation with irreducible quantitative consequence: **OPEN**
