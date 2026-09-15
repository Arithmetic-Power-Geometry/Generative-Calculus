# GC-II Audit 165 — Admissible Identification Cost Collision

Status date: 2026-09-15

## Scope

GC-I on `main` remains frozen. Starting from Audit 164, this audit tests the proposed GC-II residual: replace oracle enrichment by an enrichment that must itself be acquired through admissible R/I/A/L operations, and define the least operational cost needed to make a target capability quantity identifiable.

## Formalization

Let `M` be a finite hypothesis/model class, `B_b` the behavior available at budget `b`, and `Q : M -> Y` the target capability quantity. Let `E` be a family of admissible experiments/actions. An adaptive policy `pi` maps the current transcript to a next admissible experiment or STOP. Each experiment has a nonnegative operational cost `c(e,h)` (which may depend on history and may encode resource, information, interface/action, and law restrictions through admissibility and state augmentation).

A policy Q-identifies M when every model N consistent with the terminal transcript has `Q(N)=Q(M)`. Define

`AIC_Q(M;b) = inf_pi Cost_pi(M)`

where the infimum ranges over admissible policies that Q-identify M from the initial information B_b. A worst-case version is

`AIC_Q^wc(b) = inf_pi sup_M Cost_pi(M)`.

This is a valid operational quantity. It separates the pure cardinality lower bound of Audit 164 from the cost of physically acquiring the distinctions.

## Proposition 165.1 — Zero / Infinity criterion

1. If Q already factors through B_b, then `AIC_Q^wc(b)=0` (assuming STOP has zero cost).
2. If there exist M,N with `Q(M) != Q(N)` that remain observationally indistinguishable under every admissible finite experiment policy, then `AIC_Q^wc(b)=+infinity`.

Proof: (1) no experiment is needed. (2) any terminal transcript shared by M,N fails the Q-identification condition, so no admissible identifying policy exists.

Status: **PROVED**.

## Proposition 165.2 — Monotonicity under admissible enrichment

If budget b' weakly enlarges the set of admissible policies relative to b without increasing the cost of any common policy, then

`AIC_Q^wc(b') <= AIC_Q^wc(b)`.

Proof: the feasible policy set at b is contained in that at b'. Taking an infimum over a superset cannot increase the optimum.

Status: **PROVED**.

Important: this is only monotonic under a precise nesting assumption. A scalar budget label by itself does not imply monotonicity if changing budget also changes costs or rules non-monotonically.

## Proposition 165.3 — Cardinality lower bound is not a cost lower bound without a channel/cost assumption

Audit 164 gives a required number of terminal distinctions. It does **not** imply a positive lower bound on operational acquisition cost unless admissible experiments have bounded distinguishing power per unit cost.

Counterexample: suppose one admissible zero-cost experiment outputs the exact Q-class. Then arbitrarily many Q-classes are identified at zero operational cost.

Thus a bound such as `AIC >= log2 k_Q(F)` is dimensionally and mathematically invalid unless cost is explicitly denominated in bits or linked to information gain by an assumption.

Status: **PROVED by counterexample**.

## Proposition 165.4 — Conditional information-per-cost lower bound

Suppose every admissible experiment, conditional on every history, can refine the relevant uncertainty by at most `rho * c` bits under a specified worst-case information measure, where rho has units bits/cost. If a B_b-fiber contains k pairwise Q-distinct classes that must be separated, then every identifying policy obeys the conditional bound

`Cost >= log2(k)/rho`.

This is not universal: it depends on the per-cost distinguishing-capacity assumption and on the chosen information notion.

Status: **CONDITIONAL**.

## Collision test

The central construction `minimum cost of adaptively choosing admissible experiments until the target is identified` is not a new mathematical mechanism. It is a direct instance of active/sequential hypothesis testing or optimal/adaptive experimental design with action costs and constraints. Related literatures explicitly optimize experiment/action choice for identification, including heterogeneous action costs; causal intervention design likewise optimizes minimum intervention cost for identifiability. Blackwell/Le Cam theory supplies comparison/deficiency notions for experiments, although the sequential constrained-control layer is more directly covered by active experiment design/testing.

Therefore the proposed residual from Audit 164 does not survive the prior-art gate merely by requiring enrichment to be operationally obtainable.

## Exact reduction

Given a finite GC-II instance above, construct an active identification problem whose hypotheses are M, whose actions are the admissible GC experiments, whose observations are their GC outcomes, whose action costs are the GC operational costs, and whose terminal equivalence classes are the Q-level sets. A policy is feasible and Q-identifying in GC iff it is feasible and class-identifying in the active testing instance, with identical path cost. Hence the optimal values coincide exactly.

Conversely, any finite active hypothesis-identification problem with action costs embeds in this GC formalization by taking R/I/A/L state to encode the action availability, observation kernel, accumulated resources/cost, and transition rules.

Status: **PROVED as a finite formal reduction under the stated encoding**.

## Consequence for Omega_G

Defining Omega_G as the least admissible cost of acquiring enough evidence to identify a capability quantity does not establish an independent GC-II invariant. In the finite effective setting it is an active identification / experiment-design optimum under a change of vocabulary.

This is a decisive falsification of the immediate Audit-164 residual as a breakthrough route.

## What remains genuinely open

A GC-II-specific residual would need structure not erased by the exact reduction above. Candidate requirements must be stated before claiming novelty, for example a theorem coupling *capability creation* and *identification* such that the act of measuring/intervening changes the reachable capability closure and the target Q itself in a way that cannot be represented as ordinary controlled belief/state augmentation. But Audits 153–162 already show that finite/effective endogenous changes are generally absorbable into augmented state, so this route faces a strong no-go barrier.

A more promising scientific contribution may be the accumulated GC-II **reduction/no-go map**: under effective sufficient-state semantics, a broad family of proposed generative quantities collapses respectively to reachability/repair, simulation/resource conversion, communication/synthesis, active identification, or becomes non-identifiable. A new theorem could characterize this collapse class formally rather than proposing another metric.

## Ledger

- Admissible identification cost definition: **VALID but mechanism IMPORTED/KNOWN**.
- Zero/infinity criterion: **PROVED**.
- Monotonicity under nested admissibility: **PROVED**.
- Universal `log k` operational-cost lower bound: **FALSIFIED without a capacity-per-cost assumption**.
- Information-per-cost lower bound: **CONDITIONAL**.
- Finite reduction to active hypothesis identification / experiment design: **PROVED under stated encoding**.
- Audit-164 budget-indexed admissible-identification residual as independent Omega_G novelty: **FALSIFIED**.
- General GC-II reduction/no-go classification theorem: **OPEN**.
