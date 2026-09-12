# GC-II Audit 095 — Typed Constrained Realization Region Collision

## Scope

This audit follows Audit 094 and tests whether the candidate typed constrained realization region can itself supply the missing GC-II Paper-II breakthrough.

## Candidate

For an operational system X and permitted capability loss epsilon, define

M_X(epsilon) = Pareto { (R_mem, I_update, A_access, L_latency) : there exists a recursive representation Z preserving the specified capability semantics to error <= epsilon }.

The coordinates must be operationally defined in commensurate physical/computational units before scalarization. The Pareto set itself does not assume additivity.

## Proposition 095.1 — Upward closure

STATUS: PROVED conditional on free wasting / nonbinding extra budget.

If a realization with typed cost c is feasible and extra resources may be left unused, every c' >= c coordinatewise is feasible. Hence the feasible realization set is upward closed and M_X(epsilon) is its Pareto boundary when minimal elements exist.

This is a generic resource-feasibility fact, not a GC-II novelty claim.

## Proposition 095.2 — Monotonicity in allowed loss

STATUS: PROVED.

If epsilon_1 <= epsilon_2, every epsilon_1-adequate realization is epsilon_2-adequate. Therefore the feasible region expands monotonically with epsilon. Depending on convention, the Pareto frontier can move weakly toward lower resource cost.

Again this follows directly from nested adequacy constraints.

## Proposition 095.3 — Scalar memory/distortion slices reduce to known decision-centric rate-distortion structure

STATUS: IMPORTED/KNOWN COLLISION.

If I_update, A_access and L_latency are unconstrained or fixed, and R_mem is measured by code rate/state information while capability loss is a decision distortion, the candidate reduces to a decision-centric rate-distortion problem. In particular, 2026 work on agent memory explicitly defines decision loss caused by memory compression and a memory-distortion frontier under a runtime memory budget. Classical rate-distortion and information-bottleneck theory already cover the general rate-versus-relevant-distortion architecture.

Therefore the R_mem-versus-capability-loss projection is not a new GC-II law.

## Proposition 095.4 — Multiple typed coordinates do not create novelty by themselves

STATUS: FALSIFIED as standalone novelty.

Replacing one rate/cost coordinate by a vector of memory, update information, access and latency costs creates a multiobjective constrained realization problem. Pareto regions, multiple resource constraints, rate-distortion-cost regions, finite-state-controller memory constraints, communication/streaming tradeoffs, and thermodynamic information-processing costs already provide neighboring mathematical structures.

A vector-valued feasible region is therefore not by itself a Closure-Escape theorem, No-Free-Capability theorem, or Generative Novelty Gap.

## Fresh collision notes (checked 2026-09-12)

1. Zou et al., arXiv:2605.10870 (May 2026), `Remember the Decision, Not the Description: A Rate-Distortion Framework for Agent Memory`, explicitly measures memory quality by loss in achievable decision quality under compression and defines a memory-distortion frontier. This collides directly with the memory/capability-loss slice.
2. 2026 rate-distortion work continues to develop multi-constraint and memory-aware variants, including finite-blocklength sources with memory and rate-distortion-perception/equivocation regions. Thus adding multiple fidelity/resource axes is not an empty prior-art region.
3. Finite-state controllers for POMDPs already make controller memory an explicit constrained realization device; history-plus-controller-memory can be mapped into an augmented fully observable state representation.
4. Thermodynamic information-processing work continues to derive physical cost laws for memory operations, so attaching physical resource coordinates to representation is not sufficient novelty either.

## Important no-go

A candidate theorem of the form

capability loss <= F(R_mem, I_update, A_access, L_latency)

is not nontrivial merely because F is nonlinear or contains interactions. Without additional structural assumptions, the tightest F can be defined tautologically as the upper envelope of observed/attainable losses. To count as Paper-II science, F must be derived from explicit operational assumptions and must predict or forbid behavior not already encoded in the definition of the feasible set.

STATUS: PROVED as a methodological no-go: envelope-definition alone is tautological; a non-tautological bound requires independent assumptions.

## Consequence for Omega_G

Defining Omega_G as distance from a point to M_X(epsilon), volume between realization regions, or excess capability loss over a scalarized baseline is not presently defensible as a novel invariant. Such quantities inherit the choice of coordinates, normalization, scalarization/metric, and operational boundary. They may be useful diagnostics but do not yet survive the collision gate.

STATUS: OPEN as a useful diagnostic; FALSIFIED as a standalone novelty claim.

## Stronger surviving target

The realization-region route survives only if GC-II can prove a structural inequality or obstruction that couples at least two typed realization resources to capability preservation and that cannot be reduced to standard rate-distortion, information bottleneck, controller-state complexity, communication/streaming complexity, or thermodynamic information-processing bounds.

A legitimate next search target is therefore a finite operational family with all of the following properties:

1. the complete decision-centric memory-distortion frontier is matched between two systems;
2. standard state-count/minimal-automaton complexity is matched;
3. ordinary query/communication complexity summaries relevant to the boundary are matched;
4. yet a typed joint realization constraint (for example memory x access x latency) differs;
5. the difference follows from a proved structural obstruction rather than a coordinate definition;
6. the obstruction yields a quantitative prediction and survives exact finite counterexample search.

This is an OPEN search program, not a claimed result.

## Status table

- M_X(epsilon) definition: DEFINITION / OPEN candidate
- upward closure: PROVED conditional on free wasting
- monotonicity in epsilon: PROVED
- scalar memory/capability-loss slice: IMPORTED/KNOWN rate-distortion collision
- vector/Pareto form as standalone GC-II novelty: FALSIFIED
- nonlinear F without independent assumptions: FALSIFIED as non-tautological theorem strategy
- Omega_G from generic region distance/volume: FALSIFIED as standalone novelty
- structural typed realization obstruction surviving known reductions: OPEN

## Scientific conclusion

Audit 095 removes another easy route. A typed Pareto realization region is mathematically useful bookkeeping, but the bookkeeping itself is not Generative Calculus II. The next valid advance must be an independently derived obstruction or inequality inside that region, with an exact witness and a prior-art separation. Until such a result is found, no breakthrough claim is justified.