# GC-II Audit 378 — No-Free-Capability kernel criterion and zero-cost obstruction

## Scope
Branch-only Paper-II audit. GC-I on main is unchanged.

## Question
Can one prove a generic No-Free-Capability theorem of the form

[
Omega_G(J)>0 \Longrightarrow C(J)>0
]

or, for an accounting vector,

[
Omega_G(J)>0 \Longrightarrow Delta(J)\neq 0,
qquad
Delta=(Delta R,Delta I,Delta A,Delta L)?
]

The audit deliberately separates **structural change** (new admissibility, rule, interface, action, information channel, or resource token) from a chosen **numeric cost** assigned to that change.

## Definitions
Fix a baseline operational system O and a class J of admissible interventions. Let

[
Omega:J\to[0,infty]
]

be any faithful capability-novelty score in the minimal sense that (Omega(J)>0) whenever the intervention creates at least one capability counted by the chosen semantics.

Let

[
Delta:J\to D
]

be the accounting map, where (D) is any pointed domain with distinguished zero element 0 (for example (mathbb R_+^4)). Define

[
kerDelta={J:Delta(J)=0},qquad
kerOmega={J:Omega(J)=0}.
]

## Theorem 1 — Exact kernel criterion
The universal No-Free-Capability implication

[
orall J,quad Omega(J)>0Rightarrow Delta(J)
eq0
]

holds **if and only if**

[
oxed{kerDeltasubseteqkerOmega.}
]

### Proof
The implication is logically equivalent to its contrapositive
(Delta(J)=0RightarrowOmega(J)=0) for every intervention (J), which is exactly the stated kernel inclusion. QED.

**Status: PROVED, but logically elementary; not a Paper-II breakthrough.**

## Corollary 1 — Numeric nonnegativity is insufficient
Nonnegative costs alone do not imply No-Free-Capability. Suppose the model permits a newly admitted primitive (a:s\to t) with numeric cost zero and (t) was not reachable from (s) in the baseline system. If the accounting map records only consumed numeric resources and assigns (Delta(a)=0), then

[
Delta(J)=0,qquad Omega(J)>0.
]

Hence the No-Free implication fails.

This counterexample survives any number of resource coordinates: append zeros in every coordinate.

**Status: PROVED / decisive counterexample to a generic positive-cost theorem.**

## Corollary 2 — Strictly positive primitive costs are sufficient only relative to the chosen intervention model
Assume pure augmentation, every closure-changing intervention must use at least one newly admitted primitive, and every newly admitted primitive has accounting vector different from zero with no cancellation possible. Then closure escape implies nonzero accounting.

This is a support-faithfulness assumption, not a consequence of closure itself.

**Status: CONDITIONAL.**

## Corollary 3 — Structural support and quantitative expenditure cannot be conflated
A primitive can be available at zero marginal numeric cost yet change reachability. Therefore an accounting coordinate intended to support No-Free-Capability must be **faithful to structural support changes**, not merely to expenditure.

One safe representation is a pair

[
(chi(J),c(J)),
]

where (chi(J)) records structural support change and (c(J)) records quantitative expenditure. A theorem using only (c(J)) cannot exclude zero-cost capability creation unless positivity is separately assumed.

**Status: PROVED as a modeling requirement.**

## Degenerate and edge cases
- Identity/self-loop augmentation: structural change may occur while (Omega=0); this does not violate No-Free.
- Duplicate primitive: same conclusion.
- Zero-cost cycle that reaches no new counted outcome: (Omega=0).
- Zero-cost edge to a new counted outcome: falsifies positive numeric No-Free.
- Infinite costs: irrelevant to the zero-kernel obstruction.
- Vector budgets: the theorem uses only the distinguished zero vector and is dimension-independent.
- Negative/canceling accounting: excluded above; if allowed, even strictly nonzero primitive charges can sum to zero, creating further counterexamples.
- Observational quotient: (Omega) must be computed after the chosen capability semantics; a newly reachable but observationally equivalent state need not count as novelty.

## Composition audit
For sequential interventions (J_1,J_2), additive numeric cost does not repair the obstruction if either closure-changing intervention can have zero charge. Faithfulness of the accounting kernel is the necessary and sufficient property.

For parallel composition, the same statement holds componentwise: a zero-accounting component that changes capability violates the universal implication.

## Prior-art collision
The generic mechanism is not GC-specific. Resource theories begin by specifying free operations/resources; their basic non-generation principle is imposed through the definition of the free class. Likewise ordinary transition-system/Petri-net reachability can change when the admitted transition relation changes, independently of a positive numerical transition price.

Therefore the statement “new capability requires positive cost” is not derivable merely from operational closure. It requires a faithful choice of what is declared non-free/charged.

**Status: IMPORTED/KNOWN mechanism at the framework level.**

## Consequence for GC-II
A defensible GC-II No-Free theorem cannot simply assert positive scalar expenditure. It must identify an independently motivated GC structural accounting map (Delta_G) and prove

[
kerDelta_GsubseteqkerOmega_G
]

from frozen GC-I envelope/projection structure.

The nontrivial scientific target is therefore:

> derive kernel faithfulness rather than assume it.

A candidate must survive zero-cost actions, zero-cost information, rule/interface changes, duplicate primitives, observational quotients, and compositional cancellation.

## Status ledger
- Exact accounting-kernel criterion: **PROVED**.
- Generic positive numeric No-Free theorem from nonnegative costs: **FALSIFIED**.
- Strict-positive/support-faithful version: **CONDITIONAL**.
- Generic mechanism as GC novelty: **IMPORTED/KNOWN**.
- GC-I-derived kernel-faithfulness theorem: **OPEN**.
