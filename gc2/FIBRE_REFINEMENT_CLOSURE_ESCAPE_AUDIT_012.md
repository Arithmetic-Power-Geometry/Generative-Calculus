# GC-II Fibre-Refinement Closure-Escape Audit 012

## Status
**PROVED — restricted finite specialization / IMPORTED-KNOWN combinatorial core.** No novelty claim is made for hitting set, set cover, partition refinement, or functional consistency.

## Purpose
Audit the first nontrivial extension suggested by Audit 011: the translator-visible partition is no longer fixed. Admissible R/I/A/L augmentations may expose features that refine observations, and the problem is to determine the minimum augmentation needed to escape a shared-translator obstruction.

## Finite model
Let Q={1,...,n} be required operational traces. Each trace i has initial translator-visible observation x_i and required target y_i. Define the conflict universe

C = {{i,j}: x_i=x_j and y_i != y_j}.

Let E={1,...,m} be candidate admissible refinements. A refinement e can represent additional computation/resource-derived preprocessing, acquired information, an interface/action observation, or a rule-authorized disclosure. It exposes feature f_e(i). Define its separation set

S_e = {{i,j} in C : f_e(i) != f_e(j)}.

For J subseteq E, the augmented translator observes (x_i,(f_e(i))_{e in J}). Let F(J)>=0 be an arbitrary set-function augmentation penalty. F need not be additive; cross-channel interaction terms are allowed.

## Theorem 1 — Exact Closure-Escape / Conflict-Hitting Equivalence
A deterministic shared translator exists after choosing refinements J iff

C subseteq union_{e in J} S_e.

Equivalently, every initially confusable pair demanding different outputs must be separated by at least one selected admissible refinement.

### Proof
If a conflict pair {i,j} is not covered, then x_i=x_j and every selected feature agrees, so the augmented observations are identical while y_i != y_j; no deterministic function can satisfy both. Conversely, if every conflict is covered, any two traces with identical augmented observation cannot be a conflict and therefore demand the same target. Defining the translator fibrewise gives a valid shared translator. QED.

This gives three equivalent criteria in the restricted model:
1. **Operational:** one shared translator exists after J.
2. **Geometric/partition:** the common refinement of the initial observation partition and selected feature partitions refines the target-label partition.
3. **Computational/combinatorial:** J hits every conflict in C.

## Corollary 1 — Exact finite novelty/refinement gap
Define

Omega_ref(Q) = min { F(J) : J subseteq E, C subseteq union_{e in J} S_e },

with Omega_ref=+infinity when no candidate family separates every conflict.

Then, for positive-definite F (F(empty)=0 and F(J)>0 for nonempty J),

Omega_ref(Q)=0 iff the unaugmented shared translator already exists.

Thus this restricted Closure-Escape statement is non-tautological in the sense that feasibility is certified by a concrete partition/hitting condition and the minimum escape cost is independently computable from admissible refinements.

## Corollary 2 — Restricted No-Free-Capability theorem
If C is nonempty, F is positive-definite, and exact shared translation becomes possible, every sufficient augmentation has strictly positive cost. Hence Omega_ref(Q)>0.

The assumptions are necessary: if a nonempty refinement is assigned zero cost, a collision can be repaired at zero penalty.

## Corollary 3 — Quantitative capability-accounting bound
For every sufficient J,

Omega_ref(Q) <= F(J).

If refinements are typed R/I/A/L and J induces increments (Delta R,Delta I,Delta A,Delta L), this is the exact restricted form of the requested accounting bound. Nonlinear interactions are permitted because F is a set function rather than a sum.

## Computational criterion
For additive positive costs, computing Omega_ref is weighted hitting set on conflict pairs. Therefore the unrestricted candidate-refinement optimization inherits NP-hardness from weighted hitting set/set cover. This is a complexity boundary, not a GC-II novelty claim. Exact brute force is appropriate only for small finite audits; SAT/ILP formulations are natural for larger instances.

## Edge cases and invariances
- C empty: Omega_ref=F(empty)=0.
- No candidate separates some conflict: Omega_ref=+infinity.
- Duplicate traces: harmless unless they share augmented observation and demand distinct targets.
- Relabeling trace indices, observation symbols, target symbols, or feature values by bijections leaves feasibility invariant.
- Vector resource dimensions are not scalarized here; resource-derived refinements may carry vector feasibility constraints before entering E.
- Monotonicity in available refinements: adding candidates cannot increase the minimum cost if the old cost function is preserved on old subsets.
- Composition: no triangle inequality follows for nonlinear F; Audit 010 remains controlling.

## Exact executable audit
`gc2/fibre_refinement.py` implements conflict construction, sufficiency, and exact minimum set-function optimization. `gc2/tests/test_gc2_fibre_refinement.py` includes exhaustive three-trace binary checks comparing conflict coverage with direct functional consistency, plus joint-refinement, nonlinear-penalty, zero-conflict, and positive-gap witnesses.

## Prior-art collision boundary
The equivalence is mathematically the same core as partition refinement plus hitting set / test selection / feature selection for separating conflicting pairs. It is therefore **not** a breakthrough. Its value for GC-II is architectural: it gives an exact bridge from operational closure escape to a geometric partition criterion and a computational optimization criterion while retaining explicit R/I/A/L typing and nonlinear accounting.

## Consequence for Paper II
A genuinely stronger target must now go beyond static candidate features. The next candidate should allow refinements themselves to be *generated by admissible operational transformations under vector budgets*, so that the conflict hypergraph is endogenous to reachable computation/information/action/rule traces. Any novelty claim must survive comparison with adaptive test selection, decision trees, active feature acquisition, communication complexity, and experiment design.
