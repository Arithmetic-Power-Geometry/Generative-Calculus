# Audit 099 — Weighted Process-Semantics No-Go

## Question
Can a typed budget obstruction remain after two finite GC-II systems are matched by ordinary process semantics, provided the semantics preserves the four typed charges `(R,I,A,L)` and task/error labels?

## Status

- Typed weighted-trace preservation => finite-horizon budgeted-closure preservation: **PROVED**.
- Typed cost-preserving bisimulation => typed weighted-trace preservation: **PROVED** (finite systems, exact edge matching).
- Residual closure gap after complete typed weighted process semantics: **FALSIFIED** for the model below.
- Claim that vector-valued path budgets themselves constitute GC-II novelty: **FALSIFIED / IMPORTED-KNOWN**.
- A GC-II breakthrough requiring structure not representable by the complete operational state/transition/cost/output law: **OPEN**, but must specify that extra structure independently rather than omit it from the semantics.

## Model
Let a finite typed operational system be

`X=(S,s0,U,E,c,o)`

where `S` is a finite state set, `s0` the initial state, `U` action/interface labels, `E subset S x U x S` the admissible transition relation, `c:E -> R_+^4` gives the typed charge vector `(R,I,A,L)`, and `o:S -> O` gives task-relevant observations/outcomes. A finite execution `rho=e1...ek` has cumulative charge

`C(rho)=sum_j c(ej)`

and labelled trace consisting of its action/output sequence together with `C(rho)`. A budget `B in R_+^4` accepts exactly executions with `C(rho) <= B` coordinatewise. Error/task predicates may be any predicates measurable from the preserved labelled trace/outcome law.

## Theorem 099A — Typed weighted-trace closure invariance
If systems `X` and `Y` have exactly the same finite labelled weighted traces from their initial states through horizon `T`, including action labels, task/output labels, error-relevant outcomes, and cumulative typed charge vectors, then for every typed budget `B`, every task predicate `q`, and every error threshold `epsilon` defined on those traces,

`C_X(q,epsilon,B,T) = C_Y(q,epsilon,B,T)`.

### Proof
Membership in finite-horizon budgeted closure is an existential (or, for stochastic variants, measure-based) statement over admissible executions satisfying: (i) the task/output condition, (ii) the error condition, and (iii) the coordinatewise budget predicate `C(rho)<=B`. By hypothesis the complete trace objects on which all three predicates depend are identical between systems. Therefore the accepted execution sets, or their preserved probability laws in the stochastic extension, are identical. Hence their attainable task/error sets are identical. QED.

This is not a novelty theorem; it is an invariance/no-go statement identifying what cannot produce the desired GC-II residual.

## Theorem 099B — Cost-preserving bisimulation suffices
Suppose a relation `~` relates the two initial states and whenever `s~t`, every transition `s -u,c-> s'` is matched by `t -u,c-> t'` with identical typed vector `c`, identical task-relevant output/error label, and `s'~t'`, and conversely. Then all finite labelled weighted traces coincide, hence Theorem 099A applies.

### Proof
Induct on trace length. Length zero follows from related initial outputs. For the induction step, exact action/cost/output matching extends every matched prefix by the same typed charge and label in both directions. Thus finite weighted trace sets coincide. Apply Theorem 099A. QED.

## Dimension/domain checks
`R,I,A,L` need not share physical units. No scalar addition across coordinates is used. Only same-coordinate accumulation and coordinatewise comparison with `B` occur. Therefore the construction is dimensionally meaningful for heterogeneous resources. If a resource is non-additive (peak memory, bottleneck latency, reusable capacity), replace `sum` on that coordinate by its explicitly declared path-composition operator. The invariance proof still goes through whenever the weighted trace records the resulting composed value exactly.

## Edge and degenerate cases
- `T=0`: closure is determined by the initial output and zero charge; preserved.
- Zero-cost cycles: do not invalidate finite-horizon invariance; infinite-horizon semantics needs the chosen limit/fairness convention to be included.
- Unreachable states: irrelevant because the theorem concerns traces from `s0`.
- Nondeterminism: preserved because trace sets are matched in both directions.
- Stochastic transitions: requires preservation of the full relevant trace probability law, not merely support.
- Negative/replenishable resources: coordinatewise budget semantics must be stated carefully; the theorem remains an identity result if the exact path resource trajectory, not only its terminal sum, is preserved whenever prefix feasibility matters.
- History dependence: compile history into state (Audit 093) before applying the theorem.
- Rule modification: compile the active rule state into the operational state (Audit 088) before applying the theorem.

## Composition and invariance
The result is explicitly composition-sensitive: sequential composition is already contained in the trace law. Renaming states preserves closure. Adding unreachable states preserves closure. Any quotient that preserves the complete typed weighted traces preserves finite-horizon closure. A quotient that preserves only unweighted traces need not preserve closure.

## Prior-art collision
This route is strongly occupied by quantitative/weighted transition systems, multi-priced/timed automata, resource-constrained path finding, and multiobjective temporal path theory. Recent examples include Scoones, Shirmohammadi & Worrell (CSL 2025) on reachability for multi-priced timed automata; Ahmadi et al. (AAAI 2025) on resource-constrained pathfinding with vector resource limits; and Marica, Thielen & Wittmann (SAND 2026) on multiobjective temporal shortest paths. These literatures already treat path/process feasibility with multiple quantitative coordinates. Therefore merely attaching `(R,I,A,L)` to transitions and imposing a vector budget cannot support a GC-II breakthrough claim.

## Decisive consequence
The target proposed after Audit 098 — a typed budget obstruction that survives *complete typed cost-preserving process semantics* — is impossible by definition for finite-horizon closure when all task/error-relevant information is included in that semantics. Any claimed residual must therefore do one of two things:

1. expose an independently motivated operational variable omitted from the purportedly complete semantics, in which case the semantics was incomplete; or
2. change the scientific target from extensional closure separation to a different invariant, e.g. the complexity/size of realizing, translating, learning, verifying, or synthesizing an equivalent capability semantics.

The second route is the only non-tautological survivor identified by this audit. It still requires collision checks against automata minimization, succinctness, simulation/bisimulation complexity, communication/streaming lower bounds, circuit/branching-program complexity, and synthesis complexity.

## GC-II novelty gate after Audit 099
Do **not** claim a breakthrough from a closure difference once complete task-relevant typed process semantics differs: that is representation of the difference, not explanation. A viable Paper-II theorem must instead prove an independent lower bound on the cost of *constructing or translating* capability-equivalent semantics, or another invariant not extensionally encoded by the closure object itself.
