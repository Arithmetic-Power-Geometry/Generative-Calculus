# GC-II Audit 128 — Monotone Intervention Compression Boundary

## Question
After Audit 127 ruled out universal exact compression for unrestricted intervention signatures, does budgeted operational closure itself impose a structural restriction that yields a smaller exact certificate?

## Minimal structural assumption
Let J={1,...,m} be elementary enabling interventions. For a system M define a binary closure response

f_M(S) in {0,1},  S subseteq J,

where f_M(S)=1 means the target capability lies in closure after enabling intervention set S.

Assume only **enabling monotonicity**:

S subseteq T  =>  f_M(S) <= f_M(T).

This assumption is defensible only when added interventions are purely enabling and carry no adverse cost, conflict, or disabling side effect. It must not be silently applied to general budget-coupled systems.

## Theorem 128A — exact antichain certificate
For every monotone response f:P(J)->{0,1}, define the minimal-success family

A_f = { S subseteq J : f(S)=1 and f(T)=0 for every proper T subset S }.

Then A_f is an antichain and

f(S)=1  iff  there exists A in A_f with A subseteq S.

Therefore A_f uniquely determines f, and every antichain A subseteq P(J) uniquely determines a monotone response by upward closure.

### Proof
If A,B in A_f and A proper-subset B, minimality of B is contradicted, so A_f is an antichain. If f(S)=1, repeatedly remove elements while preserving value 1 until a minimal true subset A subseteq S is reached. Conversely, if A in A_f and A subseteq S, monotonicity gives f(S)>=f(A)=1. Uniqueness follows because the minimal true sets are recoverable from f. QED.

Status: **PROVED**.

## Theorem 128B — exact class size and information lower bound
Let D_m be the number of antichains of P(J), equivalently the Dedekind number. The realizable response class under monotonicity alone contains exactly D_m distinct functions. Hence any exact fixed-length binary certificate for the entire monotone class requires at least

ceil(log2 D_m)

bits, and this lower bound is attainable abstractly by indexing the D_m equivalence classes.

Status: **PROVED** (counting consequence; classical object).

For m=5, D_5=7581, so the information-theoretic minimum is 13 bits rather than the 32 bits of a raw truth table. Thus monotonicity genuinely restricts the signature family.

## Theorem 128C — monotonicity alone does not yield a small witness family
The number of minimal-success interventions can be as large as

binom(m, floor(m/2)).

Witness: declare capability successful exactly for sets of size at least ceil(m/2). Its minimal successes are all subsets of size ceil(m/2), forming a maximum antichain (Sperner boundary).

Therefore a certificate that explicitly lists minimal successful interventions remains exponentially large in the worst case: Theta(2^m/sqrt(m)) minimal witnesses.

Status: **PROVED modulo the classical Sperner maximum-antichain theorem; IMPORTED/KNOWN combinatorics**.

## Exact exhaustive regression
`gc2/experiments/audit128_monotone_intervention_antichain.py` enumerates every antichain of the Boolean lattice for m=1,...,5 and reconstructs the associated monotone response from its minimal true sets.

Counts obtained:
- m=1: 3 functions; maximum antichain size 1; 0 reconstruction mismatches.
- m=2: 6 functions; maximum antichain size 2; 0 mismatches.
- m=3: 20 functions; maximum antichain size 3; 0 mismatches.
- m=4: 168 functions; maximum antichain size 6; 0 mismatches.
- m=5: 7581 functions; maximum antichain size 10; 0 mismatches.

The m=5 run therefore checks all 7581 monotone Boolean response functions, not a sample.

Status: **EXHAUSTIVE FINITE VERIFICATION**.

## Dimensional/domain and edge checks
- m=0: two monotone constant functions exist; the response truth table has one entry. The experiment begins at m=1 only to avoid special-case display code.
- f identically 0: A_f is the empty antichain.
- f identically 1: A_f={emptyset}.
- Monotonicity is invariant under permutation of intervention labels.
- Composition by logical OR corresponds to taking minimal elements of A_f union A_g; logical AND corresponds to minimal unions A union B. These are standard monotone-Boolean operations, not a new GC composition law.
- If interventions can consume shared budget, disable rules, conflict, or create adverse side effects, monotonicity may fail and this theorem does not apply.

## Prior-art collision
The antichain/minimal-true-point representation is classical monotone Boolean function theory. Dedekind numbers count monotone Boolean functions and antichains. Minimal monotone DNF is exactly the family of minimal true points, and Sperner theory controls the largest possible antichain. Therefore this structural compression is not new GC-II mathematics.

## Consequence for GC-II
Audit 127's surviving route is partially validated and partially closed:

1. **VALIDATED:** independently imposed monotonicity does shrink the exact response class from all Boolean truth tables to the monotone class and permits exact compression in an information-theoretic sense.
2. **FALSIFIED AS NOVELTY:** that compression is exactly classical antichain/minimal-monotone-DNF structure.
3. **NO STRONG SMALL-CERTIFICATE RESULT:** monotonicity alone still permits exponentially many minimal intervention witnesses.

A viable GC-II breakthrough must therefore derive stronger operational structure than mere monotonicity — for example bounded interaction order, submodularity/convexity justified by the mechanics, bounded treewidth/width, exchange structure, or another independently testable restriction — and then prove a complete capability certificate whose size/complexity improves on the corresponding known representation theory.

## Status ledger
- Monotone response <-> minimal-success antichain: **PROVED / IMPORTED-KNOWN family**.
- Exact monotone-class information lower bound ceil(log2 D_m): **PROVED / IMPORTED-KNOWN counting**.
- Full m<=5 exhaustive reconstruction: **PASS; 0 mismatches**.
- Structural compression from monotonicity: **VALIDATED but NOT NOVEL**.
- Polynomial-size complete certificate from monotonicity alone: **FALSIFIED in witness-list form by maximum antichains**.
- Stronger GC-specific structural restriction yielding new complete compression: **OPEN**.
