# GC-II Resource–Interface Nonsubstitution Audit 008

## Scope

This audit asks whether extra resource budget alone can repair a whole-envelope shared-translator obstruction. It deliberately uses the weakest model in which the question is well posed and records the exact boundary of the result.

Status: **PROVED (restricted finite specialization)**. Novelty status: **IMPORTED/KNOWN neighborhood / not promoted as a breakthrough** because the core obstruction is deterministic functional consistency / zero-error distinguishability. The GC-II value is the explicit separation of augmentation channels and the resulting no-substitution statement.

## Operational model

Let `T` be a finite task family. Each task `t` has:

- a source operational symbol `x_t in X`;
- a required target label `y_t in Y`;
- a nonnegative resource requirement `r_t in R_+^d`.

A context supplies vector budget `B in R_+^d`. A shared deterministic translator receives the source symbol and, optionally, an auxiliary interface symbol `a_t in [q]`. Resource augmentation changes only the budget from `B` to `B+DeltaR`; by definition in this audit it does **not** change the source observation `x_t`, target label `y_t`, admissible rule class, or interface alphabet.

A task is resource-feasible when `r_t <= B` coordinatewise. Let

`T_B = {t in T : r_t <= B}`.

Define the budget-restricted collision multiplicity

`m_B(X->Y) = max_x |{y_t : t in T_B, x_t=x}|`,

with value `1` for an empty feasible task set.

## Theorem 1 — exact budget-restricted interface requirement

For fixed budget `B`, the minimum auxiliary interface alphabet size required for one deterministic translator to realize every task in `T_B` is exactly

`q_min(B) = m_B(X->Y)`.

Proof. Necessity: fix an `X`-fibre. For a fixed interface symbol `a`, determinism permits only one output `h(x,a)`. Therefore `q` interface symbols can realize at most `q` distinct required labels in that fibre, so `q >= m_B`. Sufficiency: within each fibre assign distinct interface symbols to its distinct required labels; reuse symbols across fibres. Then define `h(x,a)` accordingly. QED.

This is the budget-filtered version of the exact auxiliary-interface theorem in `GLOBAL_TRANSLATOR_AUDIT_006.md`.

## Theorem 2 — resource monotonicity of interface demand

If `B <= B'` coordinatewise, then

`m_B(X->Y) <= m_B'(X->Y)`.

Proof. `T_B subseteq T_B'`. For every source fibre, the set of target labels visible at `B` is a subset of the set visible at `B'`. Taking maximum cardinality preserves the inequality. QED.

Thus, in this separable model, increasing resources cannot reduce the interface alphabet required to realize **all newly feasible tasks**. It can expose additional collisions and therefore increase interface demand.

## Corollary 3 — No R-for-A substitution under observation invariance

Suppose a target family already contains a source fibre with `m_B >= 2`. If the interface alphabet remains `q=1`, then no resource-only augmentation `DeltaR >= 0` that leaves `X,Y` and the translator observation unchanged can make all tasks in `T_B` jointly realizable.

More generally, if `q < m_B`, no such resource-only augmentation repairs the existing collision.

This is a genuine channel-separation statement but only under the explicit observation-invariance assumption. It must **not** be generalized to systems where added compute can synthesize new observations, query memory, change an interface, or alter the rule class; in those systems an intervention nominally called `R` also changes `I/A/L` and the theorem's premise fails.

## Theorem 4 — exact fixed-width interface lower bound at budget B

The minimum fixed-width auxiliary binary interface is

`b_min(B) = ceil(log_2 m_B(X->Y))`.

Hence any context with interface capacity `b < b_min(B)` has a strictly positive whole-family closure escape even if every member of `T_B` is individually solvable by a task-specific translator.

## Edge and degenerate cases

- Empty `T_B`: convention `m_B=1`, so zero auxiliary bits are required.
- One target label per source fibre: `m_B=1`; a shared translator exists without auxiliary interface.
- Infinite resource budget: the theorem reduces to the static whole-family shared-interface theorem on all tasks.
- Zero resource requirements: same reduction occurs immediately.
- Resource augmentation that changes `x_t`: outside scope; resource/interface substitution can then occur and must be modeled as a coupled channel intervention.
- Stochastic translators or nonzero error: outside this exact theorem; the corresponding rate/error frontier is an open extension.

## Composition behavior

The theorem is invariant under bijective relabeling of source or target alphabets. It is not invariant under coarsening of target labels, because coarsening changes the operational task. It is monotone in budget as above and monotone nonincreasing under source refinement: if `X'` refines `X`, every `X'` fibre lies inside an `X` fibre, so `m_B(X'->Y) <= m_B(X->Y)`.

This yields the expected direction: additional *observational distinction* can lower interface demand, whereas pure budget enlargement cannot under the audit's separation assumptions.

## Prior-art collision assessment

The functional-consistency and auxiliary-alphabet arguments sit close to zero-error information theory, confusability/characteristic graphs, functional compression, deterministic simulation, and sufficient-statistic/refinement ideas. The monotonicity statement is elementary once budget filtering is introduced. Therefore:

- exact algebra: **PROVED**;
- GC-II channel interpretation: **PROVED in this restricted model**;
- universal No-Free-Capability theorem: **OPEN**;
- novelty of the underlying combinatorial bound: **NOT CLAIMED**.

## Consequence for the breakthrough program

A universal claim that `DeltaR` can compensate for `DeltaA` is false without a coupling mechanism. Conversely, a universal claim that resources and interfaces never substitute is also false when extra resources can construct/refine observations. Any defensible GC-II capability-accounting bound must therefore encode **cross-channel coupling terms** or an intervention-dependency graph, not merely four independent increments.

This narrows step (5): seek `Omega_G <= F(DeltaR,DeltaI,DeltaA,DeltaL; C)` with explicit coupling structure, and seek lower bounds conditional on which channels are observation-preserving.
