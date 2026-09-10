# GC-II Audit 052 — Finite Explicit Collapse / No-Go Theorem

Status date: 2026-09-10
Branch: `gc2-capability-accounting-lab`
Parent audit: 051

## Purpose

The preceding audits repeatedly found that individual GC-II mechanisms — budgeted closure, endogenous information, changing interfaces, changing rules, evaluator evolution, provenance, branching, history-dependent obligations, and structural rewriting — can be compiled into ordinary operational state once all relevant variables are explicit. This audit proves the common theorem behind those reductions.

The theorem is valuable as a no-go/boundary result. It is NOT claimed as a historically novel state-augmentation construction.

## Finite explicit GC-II world

A finite explicit GC-II world is a tuple

    W=(X,B,I,A,L,E,K,Q,T,c)

where:

- X is a finite physical/internal state set;
- B is a finite or finitely discretized residual resource-budget state;
- I is a finite information/evidence state;
- A is a finite interface/action-availability state;
- L is a finite rule/law state;
- E is a finite evaluator/reference-obligation state;
- K is a finite provenance/certificate state;
- Q is a finite obligation/generator state;
- T is an explicit transition/rewrite relation whose guards and updates may depend on every component above;
- c assigns each admissible transition a typed cost vector (R,I,A,L) or another declared finite-dimensional nonnegative cost object.

Branching, nondeterminism, controller/environment ownership, history dependence, endogenous obligation generation, evaluator updates, rule installation/deletion, interface creation/deletion, evidence updates, and replenishment are permitted provided their semantics are explicitly represented in the finite tuple.

Define the augmented configuration space

    Z = X × B × I × A × L × E × K × Q.

A configuration z∈Z contains every variable whose value can affect future admissibility, cost, reference evaluation, or generated obligations.

## Theorem 052-A — Exact finite operational compilation

For every finite explicit GC-II world W there exists a finite labelled weighted transition system (or, with controller/environment ownership, a finite weighted game graph) G_W on vertex set Z such that:

1. every admissible GC-II one-step transition corresponds to exactly one edge of G_W with the same action/owner label and typed cost;
2. every path/run of W corresponds to exactly one path/run of G_W, and conversely;
3. residual-budget feasibility is preserved exactly;
4. generated obligations, evaluator state, provenance state, information state, interface/action availability and law/rule state along corresponding histories are identical componentwise;
5. any reference success/failure predicate that is a function of explicit configuration/history state is preserved;
6. controller-versus-environment branching semantics are preserved by retaining transition ownership;
7. therefore every exact finite-horizon or unbounded finite-state reachability, safety, viability, reference-certified closure, and explicit-game capability question in W is equivalent to the corresponding question on G_W.

### Proof

Create one graph vertex for each z∈Z. For every admissible GC-II transition z --u,c--> z' allowed by T, create one edge z --u,c--> z'. If the semantics assign the choice to a controller or environment, copy that ownership to the edge/vertex convention used by the game representation.

Because Z stores every future-relevant variable, transition guards and updates evaluated from z are exactly the same guards and updates used in W. Hence one-step correspondence holds. Induction on run length gives a bijection between finite runs while preserving every configuration component and every edge label/cost. Infinite runs correspond by equality of all finite prefixes. Budget feasibility is preserved because the residual budget itself is a state component (or equivalently because cumulative typed costs are copied exactly). Reference evaluation and generated obligations are preserved because E and Q are copied exactly. Branching quantifiers are preserved because ownership is copied exactly. Thus all listed extensional operational questions are invariant under the compilation. QED.

Status: PROVED by explicit construction.

## Corollary 052-B — Finite semantic novelty no-go

Let Ω be any proposed GC-II novelty/capability quantity satisfying both:

- extensionality: Ω depends only on admissible operational histories, typed costs/budgets, branching ownership, and conserved reference outcomes;
- representation invariance: semantics-preserving relabellings/compilations do not change Ω.

Then for every finite explicit W,

    Ω(W) = Ω(G_W).

Therefore none of the following, singly or jointly, can establish a new semantic class merely by being present:

- endogenous obligations;
- dynamic evaluators;
- provenance/certificates;
- dynamic interfaces/actions;
- dynamic rules/laws;
- replenishing resource variables;
- finite structural graph rewriting;
- finite self-modification;
- explicit branching/nondeterminism;
- any finite combination of the above.

Any claimed breakthrough based only on those ingredients is killed by exact compilation unless it proves a property not invariant under the compilation or imposes additional structure on admissible representations/costs.

Status: PROVED as a consequence of 052-A.

## Corollary 052-C — Closure-Escape reduction

Let C_ref⊂Z be the configurations satisfying a conserved reference obligation. For seed z0 and declared budget convention b,

    z∈Cl_W^b(z0)

iff z is reachable from z0 by a budget-feasible path in G_W. Hence

    Cl_W^b(z0)∩C_ref ≠ ∅

iff ordinary budgeted accepting-state reachability holds in G_W.

Thus finite explicit Closure-Escape is operationally meaningful, but the *existence* of such a closure/reachability equivalence cannot itself be the GC-II breakthrough.

Status: PROVED.

## Corollary 052-D — Where a nontrivial Ω_G can still live

The theorem does NOT imply that all useful quantitative GC-II accounting is trivial. It implies that a representation-invariant Ω_G for finite explicit worlds must be a property of the compiled operational object plus its declared cost/reference structure, not of the syntactic story used to describe it.

Therefore a serious GC-II candidate must derive a new theorem about one or more of:

1. a restricted physically justified cost geometry not reducible to arbitrary edge weights;
2. a new invariant of families of compiled operational systems under a specified composition law;
3. a substrate-relative law-extension cost that remains nonzero after minimization over all semantics/cost-preserving interpreters;
4. a theorem coupling task-scale-error envelopes to admissible transformations in a way that produces a quantitative bound not already implied by weighted reachability, games, simulation/deficiency, communication/query complexity, control/viability, or ordinary resource theory;
5. an infinite/open-ended limit where no finite explicit compilation suffices — but only if the result is not merely ordinary computability/undecidability/universal simulation.

## Strong No-Free-Capability formulation that survives the theorem

A defensible statement is conditional on a *closed declared substrate*.

Let G_W include every admissible zero-cost operation and every explicitly installed rule/interface/information source. If target reference capability C_ref is not reachable from z0 in G_W, then no sequence composed solely of those already-admissible transitions can realize C_ref.

Equivalently, any realized closure escape must correspond to at least one of:

- consumption of positive declared resource budget;
- acquisition of exogenous information/evidence not already present in the closed model;
- installation/activation of a transformation not previously admissible;
- change of reference/evidence semantics (which must not be counted as genuine reference capability gain unless explicitly allowed).

This is exact bookkeeping, not a historical novelty claim. Its value is as a falsification guardrail: any claimed “free capability creation” in a closed finite model is either already in the closure or hides an undeclared boundary crossing.

Status: PROVED from closure of the transition relation; mechanism mathematically elementary/known.

## Dimension/domain checks

- Typed R,I,A,L costs are never summed without an explicit conversion/scalarization law.
- If B is continuous and uncountable, this finite theorem does not directly apply; a symbolic/hybrid abstraction needs separate proof.
- Infinite information/rule/provenance states require a computable-state or measurable-state generalization and may introduce ordinary undecidability or analysis issues.
- Zero-cost cycles are permitted; they do not invalidate the compilation, only termination-based horizon bounds.
- Replenishment is permitted if residual resources are explicit state variables.
- Randomness can be represented by probabilistic edges; the exact target then becomes an MDP/stochastic game rather than a deterministic graph.
- Continuous probability kernels require a non-finite extension.
- Hidden external oracles invalidate the closed-substrate premise and must be charged as imported capability.

## Composition behavior

For independent finite worlds W1 and W2 with declared product composition, the compiled configuration graph of the product is isomorphic to the corresponding synchronous/asynchronous product (according to the declared composition rule) of G_W1 and G_W2. Thus product behavior is preserved rather than created by the GC syntax.

This means any claimed nonadditivity or activation under composition must be tested against ordinary product-system/resource-theory phenomena before being labeled novel.

## Prior-art / collision classification

The proof mechanism is standard state augmentation/product-state compilation. Finite-state verification, games, dynamic epistemic models, graph rewriting systems, weighted automata, MDPs, and resource-aware planning all use versions of this idea. Higher-order process/resource theories likewise treat transformations themselves as objects acted on by higher-order maps.

Therefore:

- exact finite compilation: PROVED, mechanism IMPORTED/KNOWN;
- “dynamic rules/interfaces/evaluators/provenance imply a new semantic class”: FALSIFIED;
- finite explicit Closure-Escape equivalence: PROVED, not sufficient for novelty;
- closed-substrate No-Free-Capability bookkeeping: PROVED, elementary/known mechanism;
- GC-II historical breakthrough: NOT YET ESTABLISHED by this theorem.

## Breakthrough significance

Although the construction is not historically novel, the no-go theorem is strategically strong for GC-II because it collapses a large search tree at once. It tells us exactly what *cannot* constitute the breakthrough. Future work should stop inventing more finite state variables and calling their interaction generative novelty.

The next target should be a theorem that remains nontrivial after this quotient:

    finite GC syntax
      -> exact compiled operational object
      -> semantics/cost-preserving compiler quotient
      -> compare task-scale-error-budget composition families.

The candidate quantity should be defined only after the first two quotients, so it cannot be inflated by state augmentation, renaming, provenance encoding, evaluator encoding, or rule syntax.

## Next concrete attack

Define an operational family {G(theta)} with a conserved task-scale-error envelope E(theta,b) and a physically justified typed cost structure. Search for a composition law ⊗ and an invariant J satisfying all of:

1. J is zero under cost/reference-preserving simulation equivalence;
2. J is unchanged by exact finite compilation and compiler relabelling;
3. J is zero for independent product composition;
4. J becomes positive only when composition changes the *attainable task-scale-error frontier* beyond what either factor and all known simulation/resource monotones predict;
5. a parametric finite family gives an exact lower bound on the additional typed augmentation needed to reproduce that frontier;
6. deleting the task-scale-error coupling collapses the lower bound;
7. the result survives explicit collision checks against activation/catalysis, superactivation, direct-sum violations, communication complexity, control synergy, contextuality and higher-order resource theories.

Until such a result is proved, label candidates OPEN rather than BREAKTHROUGH.
