# GC-II Audit 070 — Physical Indivisibility / Convexification Collision

Status date: 2026-09-11
Branch: `gc2-capability-accounting-lab`
Parent audit: 069

## Question

Audit 069 isolated a possible obstruction

\[
\Xi_G(S,T)=\mathbf 1\{\operatorname{conv}K_S\succeq\operatorname{conv}K_T\;\land\;K_S\nsucceq K_T\},
\]

where the convexified closure appears sufficient but the physically admissible nonconvex closure is not. Does this provide a distinctive GC-II novelty source?

## Result

**FALSIFIED as a standalone novelty source.**

The phenomenon is a generic convexification / integrality / randomization gap. It occurs whenever a relaxation admits convex mixtures that the original implementation class cannot physically realize. The indicator above detects the existence of such a gap, but does not identify a specifically generative phenomenon.

### Proposition 070.1 — Convexification false-positive criterion (PROVED)

Let `K_S` and `K_T` be subsets of a common real vector space of task-performance vectors and suppose dominance is set inclusion. Then

\[
K_T\subseteq \operatorname{conv}K_S,\qquad K_T\nsubseteq K_S
\]

is necessary and sufficient for convexification of `S` to certify at least one target performance vector that `S` cannot implement exactly.

**Proof.** If the two displayed conditions hold, choose `y in K_T\\K_S`; then `y` is certified by `conv K_S` but is not physically implementable in `K_S`. Conversely, any target falsely certified by convexification belongs to `K_T cap conv K_S` but not to `K_S`, yielding the two conditions. QED.

This is set geometry, not a new capability theorem.

### Proposition 070.2 — Free randomization collapse (PROVED)

If the admissible implementation rules permit arbitrary external classical randomization among any finite collection of implementations in `K_S`, with the performance representation affine under randomization and no charged randomization resource, then the operationally achievable set contains `conv K_S`. If `K_S` was defined as the complete operational set, it is therefore convex and `Xi_G=0`.

Hence a nonzero `Xi_G` requires at least one of:

1. randomization is forbidden;
2. randomness/correlation is charged;
3. the performance map is non-affine under mixing;
4. mixtures require unavailable shared correlation or synchronization;
5. the task is single-shot/indivisible so ensemble mixing does not implement the requested object;
6. the implementation class contains logical/integer constraints not closed under mixing.

Each item is already a familiar source of nonconvexity in optimization, game/strategy theory, distributed implementation, or resource theories.

## Exact finite counterexample

Take

\[
K_S=\{(1,0),(0,1)\},\qquad K_T=\{(1/2,1/2)\}.
\]

Then

\[
(1/2,1/2)\in\operatorname{conv}K_S,\qquad (1/2,1/2)\notin K_S,
\]

so `Xi_G=1`. But one fair random bit choosing the two implementations realizes the target *in expectation*. Thus the obstruction is exactly the difference between a pure/indivisible implementation and its randomized convex relaxation. If expectation is the task semantics and free randomness is admitted, the gap vanishes. If exact single-shot realization is demanded, it remains. Neither case by itself establishes new GC-II mathematics.

## Collision audit

- **Integer/nonconvex optimization:** convex relaxations and integrality/duality gaps already formalize the difference between a discrete feasible set and its convex relaxation.
- **Randomized versus deterministic strategies:** convex mixing of pure strategies is standard; whether the mixture is physically available depends on randomness/correlation assumptions.
- **Resource theories:** convexification by classical randomness is an explicit modeling choice. For example, convex Gaussian resource theories enlarge Gaussian states/operations to convex mixtures precisely because classical randomness is treated as accessible; this changes distillation possibilities.
- **Quantum/resource convertibility:** pure/mixed and convex-roof constructions already expose distinctions introduced by convexification. General resource theories can require infinite/discontinuous monotone families for complete convertibility; nonconvexity does not by itself solve that problem.
- **Correlation/shared randomness:** when correlated mixing is required across separated components, its implementation cost belongs to correlation/communication complexity rather than to convex geometry alone.

## Dimensional/domain audit

`Xi_G` is dimensionless because it is Boolean. A scalar geometric distance such as `dist(K_T,K_S)` is meaningful only after choosing a norm/metric on a common performance space; it cannot be universally converted to typed physical `(R,I,A,L)` costs. Therefore Audit 069's warning remains: do not sum or identify geometrical deficiency with heterogeneous physical resources without an implementation map.

## Composition and monotonicity

`Xi_G` is not a satisfactory resource monotone in general. Adding free randomization can discontinuously send it from 1 to 0. Tensor/composite systems can create or remove the obstruction depending on whether correlation between component randomizers is free. Thus it is rule-relative rather than an invariant of the endpoint performance sets alone.

## Stronger surviving target

The potentially useful remainder is **charged convexification complexity** rather than convexification failure:

\[
\Gamma_G(y\mid S,M)
=\operatorname{Min}_{\rm Pareto}\{(\Delta R,\Delta I,\Delta A,\Delta L):
 y\in K_{\operatorname{Augment}_\Delta(S;M)}\},
\]

restricted to targets `y in conv(K_S)\\K_S`.

But this is **OPEN**, and it is not automatically novel. The next kill test must ask whether the minimum cost of physically implementing a convex decomposition reduces to known quantities: randomness complexity, common information/correlation complexity, communication complexity, integer extension/implementation complexity, purification/ancilla cost, or ordinary resource cost.

A stronger breakthrough candidate would require a family where:

1. convexified task behavior is identical;
2. all ordinary endpoint resource monotones and task losses agree;
3. exact physical realization nevertheless requires a growing typed augmentation;
4. the lower bound is invariant under equivalent decomposition/encoding;
5. it is not merely entropy of the mixing variable, support size, communication/common randomness, integrality gap, or state-description complexity;
6. a matching construction achieves the bound.

No such family is claimed here.

## Status ledger

- Convexification false-positive criterion — **PROVED**.
- Free-randomization collapse — **PROVED** under stated affine/free-randomness assumptions.
- `Xi_G` as standalone GC-II novelty — **FALSIFIED**.
- Generic nonconvexity/integrality/randomization gap — **IMPORTED/KNOWN**.
- Charged convexification complexity `Gamma_G` — **OPEN**.
- Representation-independent growing typed lower bound beyond correlation/randomness/communication/integrality theory — **OPEN**.

## Scientific conclusion

GC-II should not claim that the mere difference between a physical nonconvex closure and its convex hull is new. Convexification can erase implementation constraints, but that fact is established mathematics. The only defensible next frontier is the *typed physical cost of making a convexly available behavior exactly realizable*, after quotienting out ordinary randomization, correlation, communication, and integrality explanations.
