# GC-II Audit 224 — Capability-set boundary

Status: decisive falsification / prior-art boundary.

## Candidate under test

Audit 223 left open a change of mathematical object: instead of charging more for one fixed task, compare how added resources, information, actions, or rules change the set of operational tasks that can be instantiated, after quotienting behaviorally equivalent presentations.

## Operational definition

Let S denote an operational specification (resources, information channels, admissible actions/interfaces, rules, and a budget B). Let Q be a behaviorally quotiented universe of operational tasks/relations. Define

Cap_B(S) = {q in Q : q is realizable from S within budget B}.

For an augmentation S -> S', define the raw task-set novelty increment

N_B(S,S') = Cap_B(S') \ Cap_B(S).

A scalar candidate could be obtained from cardinality, measure, weighted value, or a monotone of this set difference.

## Theorem 224.1 — reachable-task-set factorization

Suppose operational specifications form a preorder (S, >=) where S' >= S means that S' can simulate S without exceeding the matched admissibility/budget convention, and tasks are resources/targets in the same operational theory. Then Cap_B(S) is exactly the reachable-target set (principal lower image, with the budget included in the resource object or conversion relation). Therefore any invariant that depends only on Cap_B(S), Cap_B(S'), and set operations on them factors through the ordinary resource-convertibility preorder.

Proof. By definition q belongs to Cap_B(S) iff there exists an admissible conversion/realization from S to q within B. This is precisely membership of q in the set of targets reachable from S under the budgeted conversion relation. If two specifications have identical reachable-target sets, every function of those sets assigns them the same value. Conversely, no statistic of the reachable-target set can recover mechanism information erased by the convertibility relation. QED.

## Corollary 224.2 — raw task-set expansion is not intrinsically GC novelty

If S' supplies additional ordinary resources/free operations so that Cap_B(S) is a proper subset of Cap_B(S'), then N_B(S,S') is nonempty, but this is simply an expansion of the reachable set in a resource theory. Positivity of |N_B|, a weighted size, or any inclusion monotone cannot by itself certify a Generative Calculus novelty gap.

## Corollary 224.3 — complete task indicators are complete but tautological

For each task q define M_q(S)=1[q in Cap_B(S)]. The family {M_q}_q completely determines Cap_B(S), and inclusion Cap_B(S) subseteq Cap_B(S') is equivalent to M_q(S)<=M_q(S') for every q. Thus a complete monotone family always exists at this extensional level, but it is merely the characteristic function of reachability and provides no structured/computable compression.

This directly constrains Paper-II item (6): completeness alone is not enough. A scientifically nontrivial result must establish a finite, efficiently computable, dual, or otherwise structured family under independently justified assumptions.

## Edge, monotonicity, invariance, and composition checks

- No augmentation: S'=S gives N_B empty.
- Redundant augmentation: S' may differ syntactically while Cap_B(S')=Cap_B(S); raw novelty is zero, correctly respecting behavioral quotienting.
- Resource monotonicity: if S' simulates S under the same budget convention, Cap_B(S) subseteq Cap_B(S').
- Budget monotonicity: for B<=B', Cap_B(S) subseteq Cap_B'(S), assuming feasibility is monotone in available budget.
- Zero-cost transformations are handled by the conversion relation; they do not alter the theorem.
- Infinite task universes make cardinality differences potentially infinite or noninformative; this does not affect set factorization.
- Relabeling tasks by a bijection preserves inclusion and transports Cap_B equivariantly.
- Parallel composition does not imply additive novelty: Cap(S tensor T) can contain synergistic targets absent from either marginal capability set. Hence no additive accounting law is assumed.
- Catalysis/context dependence can enlarge reachable sets without being visible in single-resource comparisons; this is already resource-theoretic structure and does not invalidate factorization when catalysts/context are included in the operational conversion relation.
- If budget is path-dependent, augment the resource/conversion object with remaining budget or use a budget-indexed preorder; the statement then applies at each B.

## Prior-art collision

General resource theories take convertibility/preorders as central objects, and monotones characterize or obstruct allowed transitions. Existing abstract work explicitly maps resources to sets of resources ordered by inclusion and constructs monotones from such set-valued maps. Complete monotone families and questions about whether distinct free-operation sets generate the same transitions are established topics. Consequently, Cap_B as a set of realizable targets is not a defensible standalone GC-II invention.

Program synthesis gives a second collision: for a fixed grammar/action language and specification class, realizability asks whether an implementation exists for a target specification; the collection of realizable specifications is again an extensional target set. Merely calling its expansion generative novelty does not escape synthesis/realizability theory.

## Status ledger

- budgeted capability set Cap_B(S): PROVED to be a reachable-target set under the stated operational semantics
- monotonicity under simulation/resource augmentation: PROVED under matched budget/admissibility conventions
- characteristic task indicators as a complete family: PROVED but tautological
- raw task-set expansion as GC-specific Omega_G: FALSIFIED
- resource convertibility / set-valued monotones / complete monotones: IMPORTED/KNOWN boundary
- synthesis realizability-set interpretation: IMPORTED/KNOWN boundary
- finite/computable/dual compression of task convertibility under special GC structure: OPEN
- mechanism-sensitive invariant surviving equality of all reachable task sets: OPEN

## Consequence for Paper II

Do not define Omega_G as the number, measure, or weighted value of newly realizable tasks alone. Audits 204-224 now eliminate both fixed-task cost gaps and raw reachable-task-set expansion as standalone novelty claims.

The next viable target must distinguish systems with the same extensional budgeted capability sets while using operationally meaningful structure not removable by simulation/behavioral quotienting. A sharper candidate is a **capability-generation law**: the transformation of capability sets under controlled changes in resource, information, action/interface, and rule coordinates, including interaction/synergy terms. The test is whether two systems can have identical Cap_B at a baseline point and identical one-coordinate response curves, yet provably different joint response under combined augmentations. Such a separation would target higher-order capability interaction rather than ordinary reachability. It must immediately be collision-tested against supermodularity/submodularity, contextual resource theories, catalysis, interaction information, cooperative games, and production functions before any novelty claim.