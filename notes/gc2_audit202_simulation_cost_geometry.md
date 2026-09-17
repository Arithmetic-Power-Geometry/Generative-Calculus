# GC-II Audit 202 — minimum-cost simulation geometry

## Candidate
For operational systems A,B let Sim(A,B) be the admissible simulators that preserve the declared task/interface/error semantics, and let c(s)>=0 be simulator cost. Define

D(A,B) = inf { c(s) : s in Sim(A,B) },

with D(A,B)=+infinity when no simulator exists.

Assume only:
1. identity simulator id_A exists with c(id_A)=0;
2. composability: s in Sim(A,B), t in Sim(B,C) implies t∘s in Sim(A,C);
3. subadditive accounting: c(t∘s) <= c(s)+c(t).

## Theorem (directed simulation-cost triangle)
Under 1–3,

D(A,A)=0,
D(A,C) <= D(A,B)+D(B,C).

Proof: identity gives D(A,A)<=0 and nonnegativity gives equality. For finite right side, choose epsilon-optimal s,t. Composition gives a simulator A->C of cost at most D(A,B)+D(B,C)+2 epsilon. Let epsilon down to zero. Infinite cases are immediate.

Thus D is an extended directed pseudometric / Lawvere-style cost geometry. It need not be symmetric and D(A,B)=0 need not imply A=B.

## Corollary (reversibility gap)
Define

G_rev(A,B)=D(A,B)+D(B,A).

Then G_rev is symmetric, nonnegative, zero on the diagonal, and obeys the triangle inequality. It is a pseudometric; it becomes a metric only after suitable zero-distance quotienting and separation assumptions.

## Edge/counterexample checks
- Noncomposable simulator classes: triangle can fail; theorem is conditional on closure under composition.
- Negative costs: identity/minimum interpretation can fail; excluded.
- Superadditive composition costs: triangle is not guaranteed.
- Infinite distances: extended-value convention handles nonconvertibility.
- Zero-cost distinct systems: G_rev can vanish off diagonal, so calling it a metric without quotienting is false.
- Composition: theorem is explicitly stable under serial composition; no additivity is assumed, only subadditivity.

## Novelty collision
This structure is not GC-specific. Directed costs satisfying identity and triangle are Lawvere/generalized metric structure; resource theories already formulate convertibility as preorders/ordered commutative monoids, and resource-theory work studies operational cost/yield and complete monotone families. Therefore minimum-cost admissible simulation and its simple two-way symmetrization cannot by themselves be claimed as a new Generative Novelty Gap or reversibility invariant.

## Status ledger
- Minimum-cost simulation triangle: PROVED (conditional on 1–3).
- Reversibility-gap pseudometric: PROVED (same assumptions).
- Minimum-cost simulation as intrinsically new GC-II geometry: FALSIFIED by prior-art collision.
- Simple G_rev=D+D^op as novel GC-II invariant: FALSIFIED as generic symmetrization.
- Representation-invariant capability accounting requiring typed resource conversion, task/error preservation, and a nontrivial interaction residual beyond path cost: OPEN.

## Exact check
`experiments/gc2_audit202_simulation_cost_geometry.py` exhaustively enumerates all 64 complete directed 3-node graphs with primitive edge costs in {1,2}; shortest-path closure supplies compositional minimum cost and checks every directed triangle and every triangle of G_rev exactly.
