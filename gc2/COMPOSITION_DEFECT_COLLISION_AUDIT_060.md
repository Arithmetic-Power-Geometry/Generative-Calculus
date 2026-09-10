# GC-II Audit 060 — Composition-Defect Frontier Collision

Status date: 2026-09-11
Branch: `gc2-capability-accounting-lab`
Parent audit: 059

## Question

Can the discrepancy between independently composed task–scale–error–budget closures and the closure of a physically coupled composite provide a nontrivial Generative Novelty Gap Omega_G?

## Candidate

Let C(S;q,s,eps,b) denote the feasible capability closure of substrate S for obligation q at scale s, error tolerance eps, and typed budget b=(R,I,A,L). For two substrates S,T define the independent product closure C(S) tensor C(T), and let C(S ||_Gamma T) denote the closure after an explicitly declared coupling Gamma (shared interfaces, communication, catalysts, information sources, synchronization, or rule installation).

A naive composition defect is any set/frontier difference

    D_G(S,T;Gamma) = C(S ||_Gamma T) \ (C(S) tensor C(T))

or a typed minimum augmentation needed to reproduce one closure from the other.

## Exact finite compilation theorem

Assume S,T,Gamma are finite explicit operational systems and every shared object is represented in the state and charged in the declared typed accounting. Construct the product state z=(s,t,g), where g is the complete coupling/interface state. Every admissible independent or coupled step is then an edge of a finite labelled transition system on z, with the same typed edge cost and evaluator label. Therefore the coupled closure is exactly ordinary reachability/viability in this enlarged system.

Status: PROVED by direct product-state construction.

This theorem does not say the coupled closure equals the Cartesian product closure. It says that any difference is an interaction effect inside an ordinary explicit composed process unless an additional invariant is proved.

## Null-coupling theorem

If Gamma introduces no cross-system transition, no shared state, no correlated initial resource, no shared evaluator constraint, and budgets/evaluators factor componentwise, then

    C(S ||_0 T) = C(S) tensor C(T).

Hence any nonzero defect requires a declared failure of at least one factorization assumption.

Status: PROVED by interleaving/product reachability.

## Boundary-accounting lemma

For a closed explicit finite substrate, every newly reachable joint capability absent from the null product must be witnessed by at least one of: (i) a cross transition/action; (ii) shared/correlated initial state or information; (iii) a shared catalyst/resource; (iv) a coupled evaluator/obligation; or (v) a changed admissible-rule set. If none occurs, the null-coupling theorem applies.

Status: PROVED as the contrapositive of factorization.

This is a useful No-Free-Capability statement but is not by itself a novel mathematical mechanism.

## Collision analysis

1. Process calculi already distinguish parallel composition from interacting composition through synchronization/channels and hiding; interaction changes reachable behavior.
2. Resource theories already contain activation, catalysis, correlated catalysis, superactivation, and regularized/asymptotic nonadditivity. A composite becoming useful when factors are not is therefore not uniquely generative.
3. Information theory already contains multivariate synergy/high-order interdependence, where joint variables contain task-relevant information absent from individual variables.
4. Communication and distributed computation explicitly quantify gains/costs induced by cross-system information exchange.
5. Network coding and shared randomness/correlation can change joint achievable regions.
6. General process theories and monoidal/categorical frameworks already formalize sequential and parallel process composition.
7. Some generalized quantum-process frameworks even have no-go results for natural composition rules, so failure of naive compositionality is itself not unprecedented.

Therefore a scalar or Pareto 'composition defect' defined only as joint-minus-product capability is representation-sensitive and collides with established interaction/synergy/nonadditivity architectures.

## Exact kill test

If a proposed D_G can be reproduced by (a) augmenting the product state with the declared coupling state Gamma and (b) evaluating ordinary reachability/optimization on that augmented process, while its nonzero value is fully attributable to declared cross transitions/shared resources/correlations/evaluator coupling, then D_G is not a standalone GC-II novelty invariant.

Finite explicit systems satisfy this kill test.

## Edge cases

- Gamma=0 with factorized evaluator/budget: D_G=empty/zero.
- Shared free random seed: any apparent gain must charge or explicitly declare the correlation; otherwise it is an accounting artifact.
- Catalyst returned marginally unchanged but correlated: correlations remain part of the final physical state and must be accounted for.
- Coupled evaluator with uncoupled dynamics can create apparent synergy solely by changing the task; this is not capability creation.
- Unlimited communication collapses some distributed restrictions by assumption and cannot count as free novelty.
- Nonadditive typed costs do not evade the product-state compilation; they only alter edge/path valuation.
- Infinite/computable systems may add undecidability or complexity but universal simulation alone does not establish GC novelty.

## Classification

- Finite explicit product-state compilation: PROVED.
- Null-coupling factorization theorem: PROVED.
- Boundary-accounting lemma: PROVED.
- Joint-minus-product composition defect as standalone breakthrough: FALSIFIED.
- Generic synergy/nonadditivity/activation: IMPORTED/KNOWN architecture.
- A GC-specific invariant not reducible to explicit interaction accounting: OPEN.

## Surviving target

The next candidate must not merely measure that coupling helps. It must compare two systems after *all declared coupling resources and interaction traces have been matched* and still expose an operationally testable difference tied specifically to task–scale–error–budget structure.

A sharper target is **counterfactual coupling equivalence**. Let two composites have identical component closures, identical typed boundary-exchange traces under every admissible intervention, identical evaluator/task family, and identical coupling-resource budgets. Ask whether their full achievable capability frontiers can nevertheless differ. If yes, define the minimal order of intervention/history required to distinguish them and seek a lower bound that grows with system size.

Before any novelty claim this must be collision-tested against bisimulation/process semantics, causal models/process tensors, contextuality, nonlocal games, communication complexity, hidden-state realization theory, and system identification. If equality of all admissible intervention traces already implies operational equivalence, the candidate collapses and should be falsified.
