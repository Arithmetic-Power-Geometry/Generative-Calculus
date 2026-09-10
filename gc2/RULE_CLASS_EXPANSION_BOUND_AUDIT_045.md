# GC-II Audit 045 — Rule-Class Expansion Bound Falsification

Status date: 2026-09-10
Branch: `gc2-capability-accounting-lab`
Parent audit: 044

## Question

Can GC-II obtain a nontrivial No-Free-Capability law by making the admissible transformation class itself an accounted operational object, and lower-bounding the typed cost required to enlarge exact convertibility by a specified amount?

## Setup

Let X be a finite family of operational states and let A be the currently admissible translator/rule class. For budget b, write

C_A^b = {(x,y) in X x X : y is exactly reachable/convertible from x using A within typed budget b}.

A rule-generation or installation operation changes A to A'. A naive expansion score is

E(A,A') = |C_{A'}^b \ C_A^b|.

Let k(A -> A') be the typed installation cost. No scalarization of R,I,A,L is assumed.

## Counterexample family

For every n >= 1 construct states x_1,...,x_n,y_1,...,y_n and a single parameterized primitive rule

g(i): x_i -> y_i,  i in {1,...,n}.

The physical substrate and transition semantics already support g; the initial admissibility policy A simply does not expose g to the translator class. Let A' = A union {g}. Charge one unit in one declared installation coordinate (for example one interface/rule-enablement token) and zero in the other coordinates.

Then

k(A -> A') = (0,0,0,1)

under the chosen typed convention, while

E(A,A') >= n.

Since n is arbitrary, there is no substrate-independent finite function F of installation cost alone satisfying

E(A,A') <= F(k(A -> A'))

for all finite operational systems.

The same construction works with any fixed positive scalar installation cost k_0: one generic rule can unlock arbitrarily many state pairs. With a Boolean enable/disable flag of zero marginal cost it is even stronger: positive convertibility expansion can occur at zero marginal installation cost whenever the enabling infrastructure is already present.

Status: **PROVED counterexample family**.

## Why this is not rescued by counting rules

Counting newly installed rule names is representation-dependent. One parameterized rule g(i) may be expanded syntactically into n separate rules, or n rules may be compressed into one schema. Therefore neither |A'\A| nor raw description count is compiler invariant.

A description-length charge also does not yield the desired universal conservation law: a short algorithmic rule can act on an exponentially or unboundedly large domain. At best one obtains model-relative description/synthesis complexity, not a bound on the cardinality of newly convertible pairs.

Status: **PROVED representation objection**.

## Stronger exponential witness

Let X contain all n-bit strings and add the single generic rule

flip(i): toggle bit i,  1 <= i <= n.

From a fixed origin 0^n, enabling this one rule schema makes all 2^n bit strings reachable by composition (assuming the ordinary per-use execution budget permits n flips). Thus a rule description of O(log n) to O(1) schema complexity under a fixed interpreter can induce exponentially many reachable outcomes. The exact encoding length depends on the declared machine model, so no encoding-independent numerical description claim is made; the exponential reachability statement itself is exact.

Status: **PROVED reachability witness; description-size interpretation MODEL-RELATIVE**.

## Edge and composition checks

- n=0: no expansion; the witness is intentionally nontrivial only for n>=1.
- Zero installation cost: possible only if the substrate already contains the dormant rule/interface; this does not violate physical conservation because execution can still carry positive cost.
- Positive execution cost: does not repair an installation-only bound. It instead moves the relevant accounting to the horizon- and task-dependent execution budget.
- Finite budget: choose b large enough for the stated conversions; alternatively the independent x_i->y_i witness needs only one rule application per pair.
- Composition: generic rules can amplify reachability combinatorially under repeated composition; therefore expansion is not additive in number or installation cost of generators.
- Monotonicity: A subseteq A' implies C_A^b subseteq C_A'^b only when adding rules does not remove old admissible behavior or alter budgets; this assumption is explicit here.
- Invariance: renaming or macro-expanding g does not change C, confirming that raw rule count is not an operational invariant.

## Collision with known theory

This failure mode is expected from generator/gate-set and proof-system viewpoints. A finite generating set can generate a very large or infinite closure under composition. Gate synthesis studies the cost of implementing targets from a declared gate set; recent exact-synthesis work even encodes bounded synthesis as SAT and proves optimal gate count by exhaustive length search. Proof complexity likewise distinguishes proof systems and extension rules; adding abbreviating/extension mechanisms can change proof representation and complexity without constituting a new physical capability law.

Therefore `amount of convertibility relation newly exposed per installed rule/cost` is not a theory-independent conserved quantity.

Status: **IMPORTED/KNOWN structural collision; standalone novelty FALSIFIED**.

## Decisive result

The post-Audit-044 candidate is false at the proposed level of generality:

**There is no universal substrate-independent upper bound on exact-convertibility expansion that depends only on the typed cost of enlarging the admissible rule class. A single fixed-cost generic rule can unlock arbitrarily many conversions.**

Equivalently, no nontrivial universal lower bound on installation cost can be inferred from the cardinality of newly convertible pairs alone.

Status: **FALSIFIED as standalone No-Free-Capability / Omega_G route**.

## What survives

Rule generation must still be accounted, but the quantity requiring accounting cannot be raw convertibility-set growth. A defensible GC-II quantity must condition on the actual demand distribution or obligation family and on execution horizon/budget.

The strongest next candidate is a **demand-weighted capability frontier shift**. For conserved reference demands q in Q with a declared measure mu and typed budget b, define a task loss L_q and compare the Pareto frontier of achievable vectors before and after a rule extension. Any proposed Omega_G should measure only improvements on conserved demands, not cardinality of latent conversions.

The next kill test is severe: determine whether every such demand-weighted frontier shift is already exactly a value-of-information/value-of-control, resource-theoretic monotone improvement, decision-theoretic Bayes-risk reduction, or constrained optimization sensitivity quantity. If yes, this route is also not GC-specific.

Status: **OPEN**.
