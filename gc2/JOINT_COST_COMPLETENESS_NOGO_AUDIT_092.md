# GC-II Audit 092 — Joint-Cost Completeness No-Go

## Scope
Branch-only Paper-II audit following Audit 091. GC-I `main` remains frozen.

## Question
Can GC-II obtain a new closure invariant by holding fixed the complete known higher-order joint-cost structure and then seeking a different budgeted joint capability closure?

## Setup
Let Q be a finite task set. Let the typed joint-cost map of system X be

c_X : 2^Q -> R_+^4,

with coordinates (R,I,A,L), c_X(empty)=0, and feasibility under typed budget b defined coordinatewise:

C_X(b) = { S subseteq Q : c_X(S) <= b }.

This is deliberately the same finite deterministic boundary used in Audit 091. No scalarization is introduced.

## Theorem — complete joint-cost closure determination
If

c_A(S)=c_B(S) for every S subseteq Q,

then

C_A(b)=C_B(b) for every typed budget b.

### Proof
For each S and b, membership in C_X(b) is exactly the predicate c_X(S)<=b coordinatewise. Equality of c_A(S) and c_B(S) therefore gives identical membership truth values for every S. Hence the closures are equal for every b. QED.

## Corollary — Möbius-complete representation
For any scalar coordinate f:2^Q->R, define its Möbius coefficients

m_f(T)=sum_{U subseteq T} (-1)^(|T|-|U|) f(U).

Then

f(S)=sum_{T subseteq S} m_f(T).

Applying this independently to R,I,A,L shows that the complete collection of all-order interaction coefficients is equivalent to the complete typed set function c_X. Therefore two systems with identical all-order Möbius/Harsanyi-style coefficients on this boundary cannot have different typed joint closures.

## What this falsifies
The post-Audit-091 strategy "hold fixed all relevant known joint-cost summaries and seek a closure difference" splits into two cases:

1. The summaries are complete for c_X. Then a closure separation is impossible by the theorem.
2. The summaries are incomplete. Then a separation may exist, but its first explanation is simply information omitted by the summary; it is not automatically a new generative invariant.

Thus no novelty follows merely from moving from singleton costs to pairwise, k-wise, submodular, or even all-order interaction summaries. At all orders, the representation is complete and the target difference vanishes.

## Boundary of the no-go
This theorem does NOT say all operational capability is a static set-cost function. It says that if the operational boundary really is exhausted by the finite deterministic map c_X(S), then its budgeted closure contains no additional hidden invariant.

A surviving GC-II target must therefore alter what is operationally asked while keeping the boundary explicit—for example sequential/path-dependent realizability, adaptive information acquisition, stochastic/history-dependent constraints, or intervention-conditioned composition. But merely adding such structure is not novelty: it must then survive reductions to dynamic programming, MDP/POMDP theory, reusable-resource allocation, stochastic scheduling, communication complexity, and process/resource theories.

## Prior-art collision note
This no-go is intentionally not claimed as a new external theorem. Cooperative/combinatorial cost models already use characteristic/set functions over coalitions or service bundles; Möbius/Harsanyi decompositions are invertible representations of set functions. Recent 2026 work also studies combinatorial allocation of reusable resources with endogenous deterioration, reinforcing that reusable, bundled, history-sensitive allocation is an active established area rather than an automatic GC novelty source.

## Dimension/domain/edge audit
- R,I,A,L remain typed nonnegative coordinates; no addition across unlike units is required.
- Empty set normalization is explicit but not needed for the main implication.
- Monotonicity or submodularity is not required.
- Degenerate zero-cost tasks are allowed.
- The theorem holds for every budget, including zero and arbitrarily large budgets.
- The implication is invariant under relabeling of tasks and coordinates.
- The theorem is finite-domain exact; extensions to infinite task families require appropriate representation/measurability/computability assumptions.

## Consequence for Omega_G
Any Omega_G defined solely from c_X and b is a functional of the already complete joint-cost object. It may be useful as a summary, but cannot by itself witness information absent from c_X. A non-tautological GC-II novelty gap must depend on an operational distinction not already encoded in the declared complete boundary, while avoiding the mistake of comparing against a theory complete on that enlarged same boundary.

## Status ledger
- Complete joint-cost closure determination: **PROVED**.
- All-order Möbius representation completeness on finite Q: **IMPORTED/KNOWN**.
- "Complete joint costs equal but typed joint closure differs": **FALSIFIED**.
- Pairwise/k-wise incomplete summaries: **OPEN as useful approximations, not novelty claims**.
- Static set-cost boundary as Paper-II breakthrough source: **EXHAUSTED / no standalone breakthrough**.
- Next target: sequential/path-dependent closure residual after explicit collision checks: **OPEN**.
