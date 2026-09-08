# GC-II Global Translator Audit 006

## Executive result

This run closes the first genuinely whole-envelope failure mode that the single-target `Omega_G` cannot see.

A family can have **zero taskwise translation gap for every task** while still failing exact conversion under one deterministic translator shared across the whole task family. The obstruction is a collision: two tasks expose the same source-side operational symbol but demand different target-side outcomes.

The mechanism is elementary (functional consistency / pigeonhole coding) and is therefore **not claimed as historically new**. Its GC-II value is that it supplies a precise shared-realization constraint, an exact convertibility criterion, and a quantitative interface lower bound that cannot be reduced to independent single-target reachability.

## Finite shared-translator model

Let `T` be a finite task set. A source envelope exposes one operational symbol `x_t in X` for each task, and the target envelope requires `y_t in Y`.

A globally realizable deterministic translator is one function

`h : X -> Y`

that must satisfy `h(x_t)=y_t` for every task simultaneously.

Taskwise convertibility is weaker: each task may choose its own translator `h_t`. Every singleton task is then trivially convertible whenever its required output is in the translator codomain. The scientific question is whether one shared mechanism realizes the entire family.

## Theorem 1 — Shared-Translator Convertibility Criterion

**Status: PROVED.**

Define the collision fibre

`F_x = { y_t : t in T, x_t=x }`.

Then an exact shared translator exists iff

`|F_x| <= 1 for every x in X`.

### Proof

Necessity: if `h` is a function and `x_t=x_u=x`, then `y_t=h(x)=y_u`. Thus one source symbol cannot demand two distinct target labels.

Sufficiency: if every fibre has at most one demanded label, define `h(x)` to be that unique label on every observed source symbol and arbitrary elsewhere. Then `h(x_t)=y_t` for every task.

This gives a complete finite convertibility criterion for this translator class.

## Corollary — Taskwise-zero / global-positive separation

**Status: PROVED.**

Take two tasks with

`x_1=x_2=x`, `y_1 != y_2`.

Each singleton task has zero translation error under its own translator, but no single shared deterministic `h:X->Y` realizes both tasks. Therefore independent per-task gaps do not determine whole-envelope convertibility.

This is the minimal finite witness sought after `OMEGA_G_AUDIT_005`: whole-envelope novelty must include a shared-realization constraint if it is to detect structure invisible to targetwise reachability.

## Theorem 2 — Exact Auxiliary-Interface Lower Bound

Suppose GC-II is allowed to augment the interface/action channel by an auxiliary code `a(t)` from an alphabet `Q`, and the translator may use

`h : X x Q -> Y`.

Let

`m = max_x |F_x|`.

Then the minimum auxiliary alphabet size permitting exact whole-family conversion is exactly

`q_min = m`.

Equivalently, under fixed-width binary interface augmentation, the minimum number of added interface bits is

`b_min = ceil(log2 m)`.

**Status: PROVED.**

### Proof

Lower bound: choose a source fibre attaining multiplicity `m`. Its `m` distinct target labels must be assigned distinguishable `(x,a)` inputs. Since `x` is fixed throughout the fibre, fewer than `m` code states force two distinct labels to share the same translator input, impossible for a function.

Upper bound: within each source fibre, assign distinct codes `0,...,|F_x|-1` to its distinct demanded target labels. Reuse the same code alphabet across different source fibres. Then `q=m` states suffice and define `h(x,a)` by the corresponding demanded label.

Thus the lower bound and construction coincide.

## Theorem 3 — Minimum Weighted Shared-Translation Error

For nonnegative task weights `w_t`, if exact conversion is not required, the minimum disagreement cost over all deterministic shared translators is

`Err*(h) = sum_x [ sum_{t:x_t=x} w_t - max_y sum_{t:x_t=x, y_t=y} w_t ]`.

**Status: PROVED.**

The optimization separates by source fibre. For each `x`, a deterministic translator chooses one label `y`; the best choice retains the maximum total weight and necessarily loses the remainder. Summing the independent fibre optima proves the formula.

This supplies a finite whole-envelope directed gap for the zero-resource translator specialization, but its mechanism is standard empirical-risk minimization on repeated inputs and is not a novelty claim.

## No-Free-Capability consequence

**Status: PROVED for this explicit shared-translator/interface model; not universal.**

If a collision fibre demands `m>1` distinct target outcomes, then exact whole-family capability cannot be obtained by changing neither the source representation nor the translator input interface. At least `ceil(log2 m)` bits of auxiliary distinguishability are required if the only admissible augmentation is a fixed-width task/interface tag.

This is a non-tautological lower bound because it quantifies the minimum added interface capacity independently of a chosen penalty function.

## Relation to `Omega_G`

The single-target path gap in Audit 005 cannot expose this phenomenon: every target can have `Omega_G=0` separately. A whole-envelope version should therefore minimize augmentation subject to existence of **one shared admissible translator** over the entire envelope.

In the present specialization with interface-bit cost only,

`Omega_G^global = ceil(log2 m)`

for exact conversion under the auxiliary-code model.

This is a first exact whole-envelope specialization, not yet the final GC-II invariant.

## Exhaustive computational audit

Implementation: `gc2/global_translator.py`

Tests: `gc2/tests/test_gc2_global_translator.py`

The test exhausts all paired source/target assignments for task counts `n=1,...,4`, a binary source alphabet and a three-label target alphabet. This is

`6 + 36 + 216 + 1296 = 1554`

paired finite worlds. For every case it checks:

- global convertibility iff maximum collision multiplicity is one;
- exact interface-state formula `q_min=m`;
- constructive sufficiency using exactly `m` interface states;
- direct pigeonhole failure for `q<m` in the worst fibre;
- the minimal two-task taskwise-zero/global-positive witness;
- the exact weighted-error formula on an independent weighted example.

## Edge cases and invariances

- Empty task family: treated as globally convertible; interface requirement defaults to one state / zero added bits.
- One task: always collision-free.
- Relabelling source symbols or target labels leaves collision multiplicities and required interface bits invariant.
- Duplicating a task with the same `(x,y)` does not change exact convertibility or interface-state complexity, though it changes weighted/empirical error if positive weight is added.
- Adding a conflicting task can only weakly increase `m`; hence the interface lower bound is monotone under task-family enlargement.
- Allowing task-dependent translators destroys the obstruction completely, confirming that shared realization is the essential assumption.
- Allowing the translator to observe the full task identity makes the bound vacuous; interface information must therefore be explicitly accounted rather than smuggled into the translator input.

## Prior-art collision assessment

The proof mechanisms collide with known mathematics:

- functional consistency of deterministic mappings;
- pigeonhole/injective coding lower bounds;
- minimum classification error by majority label within identical-feature fibres;
- zero-error source coding / distinguishability ideas in spirit.

Therefore these mechanisms are **IMPORTED/KNOWN ingredients**. The candidate GC-II novelty, if any, must arise only when this shared-translator obstruction is coupled to full task-scale-error-budget envelopes, explicit resource/information/interface/rule augmentation, composition, and translator resource accounting.

## Status update

- Whole-envelope shared-translator convertibility criterion: **PROVED finite specialization**.
- Per-task-zero yet global-nonconvertible witness: **PROVED**.
- Exact interface-state / bit lower bound: **PROVED finite specialization**.
- Restricted No-Free-Capability theorem: **PROVED under explicit shared-translator/interface assumptions**.
- Whole-envelope `Omega_G` specialization: **PROVED for interface-only collision model**.
- Historical novelty / breakthrough claim: **NOT ESTABLISHED**.
- General task-scale-error-budget shared-translator theorem: **OPEN**.

## Next attack

Lift the collision theorem from static symbols to operational traces/envelope tuples and require the translator to preserve error and vector-resource budgets. The immediate target is a dual criterion in which finite families of collision/packing monotones are complete for a structured translator class, followed by tests of composition and triangle behavior for the resulting directed global gap.
