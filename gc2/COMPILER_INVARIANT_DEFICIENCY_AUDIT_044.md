# GC-II Audit 044 — Compiler-Invariant Translator Deficiency Collision

Status date: 2026-09-10
Branch: `gc2-capability-accounting-lab`
Parent audit: 043

## Question

Can the compiler-invariant translator deficiency proposed after Audit 043 define a genuinely new Generative Novelty Gap, rather than a repackaging of established deficiency/simulation/conversion distance?

## Setup

Let S and T be complete compiled operational models with a common conserved reference-obligation family Q. Let Enc(S,T) be the explicitly admissible semantics-preserving translator class after quotienting away generator names, duplicated states, and semantics-identical no-ops. Let d_Q(K(S),T) be a dimensionless worst-case reference-obligation loss of translator K. Define

D_Q(S -> T) = inf_{K in Enc(S,T)} d_Q(K(S),T).

If typed implementation cost c(K) is relevant, do not add incompatible units to d_Q. Instead define the budget-indexed deficiency

D_Q^b(S -> T) = inf { d_Q(K(S),T) : K in Enc(S,T), c(K) <=_B b },

where <=_B is the declared typed resource preorder.

A symmetric version is

Delta_Q^b(S,T) = max(D_Q^b(S -> T), D_Q^b(T -> S)).

## Theorem 044-A — Quotient invariance is obtained by optimization over translators

Assume E:S'->S and F:T->T' are admissible zero-loss, cost-preserving equivalences with admissible inverses. Then

D_Q^b(S' -> T') = D_Q^b(S -> T).

Proof. For any admissible K:S->T, F o K o E is an admissible translator S'->T' with the same reference loss and typed cost. Hence D_Q^b(S'->T') <= D_Q^b(S->T). Applying the inverse equivalences gives the reverse inequality. QED.

Status: **PROVED**.

This is useful: renaming states, duplicating representations, or replacing a model by a cost-preserving equivalent cannot manufacture a positive gap.

## Theorem 044-B — Zero deficiency is exactly approximate/exact simulability at the declared loss level

For fixed b,

D_Q^b(S -> T) = 0

iff for every epsilon>0 there exists an admissible budget-feasible translator K with d_Q(K(S),T)<epsilon. If the finite translator class is closed and the infimum is attained, this reduces to existence of a zero-loss budget-feasible simulation.

Status: **PROVED**.

The statement is immediate from the infimum definition; it is not a new closure-escape theorem.

## Proposition 044-C — The candidate is structurally a generalized directed deficiency

The defining architecture is: minimize worst-case operational loss over an admissible post-processing/simulation/translation class. That is the same mathematical template as directed statistical deficiency and approximate simulation distances. Restricting the translator class or adding a resource-feasibility constraint creates a constrained instance of that template; it does not by itself establish a new mathematical species.

Status: **IMPORTED/KNOWN structural mechanism; standalone GC-II novelty FALSIFIED**.

## Typed-cost sanity check

A scalar expression such as

D_Q + lambda_R R + lambda_I I + lambda_A A + lambda_L L

is dimensionally unjustified unless explicit conversion coefficients and units are supplied. GC-II must retain either:

1. the budget-indexed family D_Q^b; or
2. a Pareto set of tuples (loss,R,I,A,L).

This avoids silently assuming additivity or exchange rates between physical resource, information, interface/action, and rule/logic costs.

Status: **PROVED dimensional requirement**.

## Monotonicity and edge cases

- Budget monotonicity: if b <=_B b', then D_Q^{b'}(S->T) <= D_Q^b(S->T).
- Identity: if the identity translator is admissible and budget-feasible, D_Q^b(S->S)=0.
- Equivalent representations: Theorem 044-A forces equal deficiency.
- Empty translator class: define D=+infinity or leave undefined; do not report a finite novelty score.
- Zero reference family: d_Q is vacuous and D=0, so Q must be nonempty and conserved.
- Unattained infimum: D=0 need not imply an exact translator; finite/compact closure assumptions are required for exact convertibility.
- Composition: if d_Q obeys a triangle inequality and translator costs compose within budgets, then directed deficiencies obey the corresponding compositional upper bound. Without those assumptions no triangle law may be claimed.
- Stochastic translators: allowing them can strictly reduce deficiency; the translator class must therefore be declared before comparison.

## Prior-art collision

Le Cam deficiency compares statistical experiments by minimizing a worst-case discrepancy over Markov kernels; zero deficiency corresponds to an appropriate simulation/informativeness relation. General resource theories similarly characterize convertibility through allowed transformations and, in many settings, complete families of operational monotones. Recent resource-theory results continue to provide necessary-and-sufficient conversion characterizations rather than a unique scalar invariant.

Therefore compiler invariance, translator minimization, directional simulability, and complete-convertibility semantics are all insufficient individually or jointly to establish GC-II novelty.

## Decisive falsification

The Audit-043 proposal that a `compiler-invariant translator deficiency` might itself supply the Paper-II breakthrough is rejected at this abstraction level:

**Any candidate whose entire content is the minimum reference-obligation loss over admissible semantics/cost-preserving translators is a constrained directed deficiency/simulation optimization. Compiler invariance removes representation artifacts but does not create a new capability law.**

Status: **FALSIFIED as standalone breakthrough candidate**.

## What survives

D_Q^b is still valuable infrastructure because it supplies a representation-safe null test. A legitimate GC-II Omega_G must contain information not recoverable from the complete family {D_Q^b}_b plus the matched extensional capability map.

This gives a stronger null principle:

**Deficiency-completeness null principle.** If two systems agree on the conserved reference capability map and on all budget-indexed directed translator deficiencies in both directions for the declared admissible translator class, then any GC-II novelty functional depending only on those data must assign zero separation.

Status: **PROVED as an extensional identity principle; not claimed novel**.

## Next attack — endogenous change of the admissible translator class

The only route not killed by this audit is to make the admissible transformation class itself an accounted operational object rather than fixed background structure. But merely changing the class is again trivial unless its creation has a substrate-relative cost and yields a quantitative theorem.

Next candidate: define a rule-generation operation that changes the admissible translator set A -> A' while conserving the reference evaluator and physical substrate. Seek a lower bound on the minimum typed cost required to enlarge the exact-convertibility relation by a specified amount. The kill test is severe: compare against resource-theory free-operation extension, gate-set synthesis, compiler construction, program synthesis, proof-system extension, advice/preprocessing, and mechanism/interface design.

A breakthrough requires a bound that cannot be reduced to the complexity of describing/installing the newly admitted transformations.

Status: **OPEN**.
