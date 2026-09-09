# GC-II Audit 026 — Budgeted Branching Relation Prior-Art Collision

## Status

- **IMPORTED/KNOWN:** robust branching capability with controller/environment quantifier alternation is already the semantic territory of alternating simulation/refinement and game semantics.
- **IMPORTED/KNOWN:** attaching multidimensional resource vectors and requiring nonnegative residual resources is already the territory of multidimensional energy/resource games.
- **FALSIFIED as a standalone GC-II novelty route:** merely defining a budget-indexed branching simulation/bisimulation on augmented `(s,B,I,A,L)` states does not establish a new GC-II contribution.
- **OPEN:** a theorem in which admissible transformations endogenously change the future information/action/rule structure and yields a quantitative whole-envelope accounting law not reducible to a fixed game graph with resource counters.

## Collision result

Audit 025 showed that flattened action/cost traces are incomplete under branching. The immediate repair suggested in the status ledger was a budget-indexed branching relation on augmented states. That repair is mathematically legitimate but, without stronger structure, is not a credible novelty target.

Consider an augmented transition game with controller choices `u`, adversarial/environment resolutions `v`, state `s`, residual vector budget `B`, and transition cost/update vector `c(s,u,v)`. A robust one-step refinement condition has the generic form

    for every controller choice required at x,
      there exists a matching controller choice at y,
        such that for every admissible environment resolution at y,
          there exists a corresponding resolution at x
            whose successor pair remains related
            and whose resource update respects the budget relation.

This is quantifier-alternating simulation/refinement structure. If residual budgets are carried as counters and edges add integer vectors, the construction is also an energy/resource game specialization. Enlarging the control state to include finite `I,A,L` annotations does not by itself escape that reduction: it simply produces a larger game graph.

Therefore the next GC-II object must not be advertised as new merely because its states contain resources, information, actions/interfaces and rules.

## Exact reduction boundary

For any finite GC-II model in which:

1. `I,A,L` take values in finite sets;
2. the admissible controller/environment moves from an augmented state are fixed by that augmented state;
3. each move has a fixed integer vector resource update;
4. capability is a safety/reachability/alternating-refinement property over the resulting branching graph;

construct a game vertex for every augmented tuple `(s,I,A,L)` and carry `B` as the energy vector. Controller/environment choices become the two players' moves. The GC-II robust capability question is then representable as a finite-state alternating/simulation or multidimensional energy-game question, depending on the observation objective.

This is a representation/reduction statement, not a complexity-equivalence claim for every possible objective.

## What could escape the collision

A stronger GC-II target must use structure that is not merely encoded as a fixed finite game graph plus counters. Candidate directions requiring separate proof are:

- transformations that create/delete/rewrite future transformation rules themselves;
- endogenous creation of new interfaces/actions whose semantics are not pre-enumerated in the initial finite graph;
- transformations that alter the task-scale-error observation algebra or admissibility relation;
- whole-envelope accounting over a family of task/scale/error/budget queries where a single translator must remain valid across the family;
- a quantitative lower bound on the minimum cost of changing the future game/translator structure, rather than merely winning a fixed resource game.

Even these directions must be collision-checked against dynamic games, graph-rewriting systems, self-modifying transition systems, adaptive control, program synthesis, and resource theories before any novelty claim.

## Edge and degeneracy checks

- With no adversarial branching, the relation collapses toward ordinary simulation/reachability.
- With zero-dimensional resources, the resource component disappears and alternating simulation remains.
- With singleton `I,A,L`, the construction reduces to a standard resource-labelled game.
- With deterministic transitions and no environment player, the branching distinction from Audit 025 vanishes.
- Encoding finite endogenous annotations into the vertex label does not create a new semantic class; it only increases state-space size.

## Prior-art collision evidence

Alternating simulation/refinement has long been used for input/output refinement and control-preserving abstraction. Alternating-time logics quantify over strategies against other agents. Multidimensional energy games place integer-vector updates on game edges and require resource levels to remain feasible. Work on energy games also establishes close reductions to simulation problems. Resource-bounded-environment energy games further show that putting vector bounds on both sides of a game is already an explicit studied direction.

Accordingly, GC-II must not claim novelty for `budget + branching + alternating quantifiers` alone.

## Consequence for Paper II

The immediate research priority changes from "define a budget-indexed branching relation" to:

> define the minimum operational cost of *changing the future capability game itself*—its admissible information, interfaces/actions, rules, and whole-envelope task feasibility—and determine whether that dynamic structural cost obeys a nontrivial closure-escape/accounting theorem.

A useful candidate should distinguish two worlds that are equivalent under ordinary fixed-graph alternating/energy-game analysis at the starting representation but differ in the cost of admissibly constructing future game structure. Until such a witness and theorem survive prior-art checks, breakthrough status remains NONE.
