# GC-II Audit 077 — Reversibility-Gap Collision and No-Go

## Scope
Branch-only Paper-II audit. GC-I `main` remains frozen.

## Candidate inherited from Audit 076

Let a fixed operational grammar M define admissible transformations between systems and a typed nonnegative cost vector c(p) in R_+^d (d=4 for the GC ledger R,I,A,L). For endpoints S,T define the Pareto forward and return frontiers

F_M(S,T) = Min_Pareto { c(p) : p is an admissible path S -> T },
F_M(T,S) = Min_Pareto { c(q) : q is an admissible path T -> S }.

A tempting GC-II reversibility gap is a scalar or vector constructed from the round trip, e.g. forward cost + return cost, a difference of directional costs, or failure of exact recovery after a forward transformation.

## Result

**Status: FALSIFIED as a standalone GC-II novelty source under a fixed operational grammar.**

### Theorem 077.1 — Round-trip reduction

For any fixed grammar M with additive path ledger under sequential composition, the attainable round-trip cost set is

C_rt(S,T) = {a+b : a in C_M(S,T), b in C_M(T,S)}.

Its Pareto frontier is therefore

F_rt(S,T) = Min_Pareto( F_M(S,T) + F_M(T,S) ),

where + is the Minkowski sum.

**Proof.** Every round trip factors into an admissible S->T path and an admissible T->S path, so its ledger is a+b. Conversely, concatenating any admissible forward and return paths gives an admissible round trip with ledger a+b. Removing dominated elements before or after Minkowski addition leaves the same Pareto-minimal set because all coordinates are ordered by the positive orthant. QED.

Thus the round-trip frontier contains no information beyond the two ordinary directed conversion frontiers.

### Corollary 077.2 — Scalar reversibility gaps collapse to directed conversion costs

For any nonnegative weight w, let

d_w(S,T) = inf_p w·c(p).

Then the weighted round-trip gap is exactly

g_w(S,T) = d_w(S,T) + d_w(T,S).

It is symmetric, nonnegative, vanishes whenever both directions have zero weighted cost, and obeys the triangle inequality whenever d_w is the ordinary directed shortest-path/quasimetric induced by the grammar. Hence g_w is just the standard symmetrization of a directed conversion cost, not a new invariant.

### Theorem 077.3 — Endpoint recoverability is preorder equivalence

Ignore charged cost and ask only whether exact conversion exists. Define S >=_M T iff an admissible S->T transformation exists. Then exact mutual recoverability is

S ~_M T iff S >=_M T and T >=_M S.

This is precisely the equivalence relation induced by the simulation/resource preorder. Failure to return is ordinary conversion asymmetry.

### Theorem 077.4 — No architecture-independent reversibility gap

Fix the same endpoint objects S,T. Construct three grammars: M1 has zero-cost maps both ways; M2 charges c>0 only on T->S; M3 forbids T->S. Endpoint descriptions can be identical while the proposed gap is respectively zero, positive/model-dependent, or infinite/infeasible. Therefore no universal positive reversibility gap follows from endpoints alone.

**Status: PROVED by construction.**

## Path-sensitive variants

A stronger proposal might compare return cost after a *specific forward history* p rather than only after reaching endpoint T. This does not rescue standalone novelty automatically.

1. If the operational state at T is sufficient for all future admissible behavior, return cost cannot depend on hidden details of p; path dependence is absent.
2. If two histories reaching the reported same T have different future return possibilities, then T was not a sufficient operational state. Augmenting state by the physically retained memory/environment record restores an ordinary state-space conversion problem.
3. If the record is deliberately coarse-grained away, the apparent irreversibility is relative to that coarse-graining and collides with established coarse-grained entropy-production/irreversibility theory.

This is the same sufficient-state pressure already identified in Audit 067, now applied to reversibility.

## Thermodynamic and computational collision

A physical positive return cost is not generically GC-specific:

- stochastic thermodynamics quantifies irreversibility through entropy production and forward/backward path asymmetry;
- Landauer-style thermodynamics of information relates logically irreversible transformations and information erasure to physical work/heat constraints under explicit assumptions;
- reversible computation/uncomputation studies the cost of retaining and removing computational history;
- resource theories define reversible versus irreversible interconversion through forward/distillation and reverse/formation rates, including catalytic and asymptotic variants;
- hysteresis and dissipative control already encode path-dependent return losses in physical dynamical systems.

Recent collision checks strengthen rather than weaken this conclusion: 2026 work on bound magic and PPT entanglement with catalysis proves irreversibility that survives catalytic assistance in specific quantum resource theories, while 2026 reviews of stochastic irreversibility treat entropy production, time-reversal asymmetry, and coarse-graining as established central objects.

## Edge/counterexample audit

- S=T: zero-length path gives zero ordinary conversion cost; any positive cycle cost measures the chosen nontrivial cycle, not endpoint irreversibility.
- One direction forbidden: return gap is infinite/infeasible; this is preorder asymmetry.
- Zero-cost reversible encoding: quotienting by free equivalence leaves the result invariant.
- Catalysts/ancillas: if declared admissible, include them in M; the theorem applies to the enlarged conversion relation.
- Approximation epsilon>0: replace exact path sets by epsilon-conversion sets; the same factorization holds with explicit error-composition law. Any nontrivial phenomenon then comes from that law, not from naming the sum a reversibility gap.
- Nonadditive sequential costs: Theorem 077.1 requires additive ledger. With a declared composition operator Phi(a,b), the round-trip set becomes {Phi(a,b)}. This is still determined by directional frontiers plus the model's composition law unless hidden history affects Phi; then the state/ledger is incomplete.
- Negative/resource-generating coordinates: excluded here; the Pareto simplification requires the nonnegative resource order. Such models need their own ordered monoid and can invalidate the frontier-pruning step without creating novelty by itself.
- Stochastic paths: replace costs by the chosen risk functional/distributional order; path-space irreversibility then collides directly with stochastic thermodynamics and statistical decision theory.
- Coarse-graining: may create apparent directional asymmetry; not invariant under refinement unless explicitly proved.
- Composition/tensor powers: asymptotic reversibility/irreversibility is already a central resource-theory question; regularization can change one-shot gaps.

## Consequence for Paper II

A generic invariant of the form

"cost to go S->T plus/difference cost to return T->S"

should **not** be marketed as new GC-II mathematics. Under fixed rules it reduces to ordinary directed conversion frontiers; under thermodynamic/path-space semantics it collides with established irreversibility; under history dependence it either requires a richer operational state or explicit coarse-graining.

The useful GC-II contribution here is a no-go discipline: any claimed reversibility novelty must survive quotienting by ordinary conversion preorder, reversible re-encodings, sufficient-state completion, declared catalysts, asymptotic regularization, and known entropy-production/computational-erasure quantities.

## Surviving target

The next admissible target is not another generic reversibility scalar. Return to the core Paper-II program and seek a theorem coupling **closure escape to typed augmentation** that cannot be reconstructed from directional conversion frontiers alone. A candidate must depend on the full task-scale-error-budget closure while remaining invariant under sufficient-state completion and ordinary simulation equivalence.

One precise open direction is a **closure-curvature / nonintegrability test**: determine whether a family of infinitesimal/finite typed augmentations around a loop can produce a path-independent potential after quotienting ordinary conversion. If every consistent finite model admits such a potential, that yields a no-go theorem; if not, any residual holonomy-like object must be proved operationally observable and collision-tested against thermodynamic cycles, geometric phases, noncommutative resource conversion, and control-theoretic holonomy before any novelty claim.

No breakthrough claim is made for this surviving direction.

## Status ledger

- Round-trip frontier factorization: **PROVED** under additive nonnegative typed ledger.
- Weighted round-trip scalar as symmetrized directed conversion cost: **PROVED**.
- Exact endpoint recoverability as preorder equivalence: **PROVED / IMPORTED-KNOWN in substance**.
- Universal endpoint-only positive reversibility gap: **FALSIFIED**.
- Generic path-sensitive reversibility as standalone GC-II novelty: **FALSIFIED** without additional structure.
- Thermodynamic/resource/computational irreversibility collision: **IMPORTED/KNOWN**.
- Reversibility-gap invariant as standalone Paper-II breakthrough: **FALSIFIED**.
- Closure-curvature/nonintegrability remainder after ordinary conversion quotient: **OPEN**.
