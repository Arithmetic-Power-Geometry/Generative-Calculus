# GC-II Audit 133 — Universal typed-monotone impossibility boundary

## Question
Can bare GC-II operational closure force an unconditional nontrivial typed monotone balance, after Audit 132 showed that nontrivial reversible aggregation may consistently have zero charge?

## Theorem — No universal nonconstant scalar monotone without a restricted free-operation family
Let X be any state space with at least two states and let M:X->R be nonconstant. If the admissible/free transformation family is not independently restricted, there exists a deterministic transformation T and a state x such that M(T(x))>M(x).

### Proof
Because M is nonconstant, choose x,y in X with M(y)>M(x). Define a deterministic transformation T with T(x)=y (and define T arbitrarily elsewhere). If T is admitted as free, then M(T(x))=M(y)>M(x). Therefore M is not monotone under all possible admissible/free transformation families. QED.

The same argument applies componentwise to any proposed typed balance vector whenever at least one claimed nonincreasing component is nonconstant and transformations capable of increasing that component have not been excluded by an independent operational axiom.

## Consequence for GC-II
A statement of the form

    capability expansion => Delta R + Delta I + Delta A + Delta L > 0

cannot be obtained from closure/composition alone if R,I,A,L are merely labels whose free-operation behavior has not been independently specified. Defining 'free' to mean 'does not increase the proposed monotone' makes the result true by construction and is not a No-Free-Capability theorem.

Thus a defensible GC-II accounting law needs at least one independently motivated restriction: a physical conservation/dissipation law, an information-access constraint, an interface/action acquisition rule, a rule-description/implementation constraint, or another operationally measurable preorder fixed before the monotone is proposed.

## Exact finite regression
`experiments/gc2_universal_monotone_impossibility_audit.py` enumerates the four deterministic maps on a two-state space and both nonconstant binary scalar candidates. Each candidate has at least one deterministic transformation that strictly increases it; zero universal nonconstant candidates survive.

## Prior-art collision
This boundary is standard resource-theory logic: resource theories specify free operations, and resource monotones are required to be nonincreasing under those operations. The free-operation structure determines the resource preorder; a monotone is not obtained from unconstrained composition alone. Consequently this theorem is useful as a GC-II falsification gate, not as a novelty claim.

## Status
- theorem above: **PROVED**
- two-state exhaustive regression: **PASS**
- unconditional scalar No-Free-Capability from bare closure: **FALSIFIED**
- resource-theoretic dependence on specified free operations: **IMPORTED/KNOWN**
- GC-II-specific independently grounded typed preorder: **OPEN**

## Next gate
Define R,I,A,L operationally before choosing Omega_G, with independently testable free transformations for each type. Then test whether the intersection preorder has a capability-expansion obstruction not reducible to an ordinary multi-resource theory. Any candidate must survive catalysts, reversible transformations, nonlinear interactions, and complete-family-of-monotones collisions.
