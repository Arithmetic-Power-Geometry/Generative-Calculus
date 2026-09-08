# GC-II Generative Novelty Gap Audit 005

## Scope and status

This note defines and stress-tests a finite operational candidate for the Generative Novelty Gap on the corrected lifted cumulative-resource closure. The result is a **PROVED finite-model reduction**, not a claim of historical novelty. The mathematical mechanism collides substantially with resource-constrained shortest-path and minimum-augmentation ideas, so the breakthrough status remains **OPEN / NONE YET**.

## Operational context

A finite world is a directed graph with states `s` and admissible transformations `e=(u,v)`. Each transformation carries:

- a nonnegative vector resource cost `c(e) in N^d`;
- an information requirement `I(e)`;
- an interface/action requirement `A(e)`;
- a rule requirement `L(e)`.

A base operational context is

`C=(B, I0, A0, L0)`,

where `B in N^d` is the available cumulative resource budget and the remaining components are currently available information, interfaces/actions, and rules. A path is executable exactly when its cumulative resource use does not exceed `B` and every edge requirement is contained in the corresponding available set. Reachability is evaluated on the lifted state `(s,r)` so that spent resources are not refreshed.

## Candidate gap

For a target state `y`, define an augmentation

`Delta=(Delta B, Delta I, Delta A, Delta L) >= 0`

with set components interpreted by union. Let `F(Delta)` be a positive-definite monotone augmentation penalty. The implemented stress test deliberately uses a nonlinear interaction penalty

`F = ||Delta B||_1 + |Delta I| + |Delta A| + |Delta L| + ||Delta B||_1 (|Delta I|+|Delta A|+|Delta L|)`.

The candidate Generative Novelty Gap is

`Omega_G(y | C) = min_Delta { F(Delta) : y is reachable from the seed set under C + Delta }`.

This definition does **not** assume additive capability accounting: the interaction term makes joint resource-and-gate augmentation cost strictly nonadditive.

## Exact Path-Deficit Theorem

**Status: PROVED for the stated finite deterministic model.**

For any finite path `p` from a seed to `y`, let

- `c(p)` be its cumulative vector resource cost;
- `I(p), A(p), L(p)` be the unions of its edge requirements.

Define its operational deficit relative to `C` by

`D_C(p)=([c(p)-B]_+, I(p)\I0, A(p)\A0, L(p)\L0)`.

Then

`Omega_G(y | C) = min_{p: seed -> y} F(D_C(p))`.

### Proof

Fix a path `p`. Any augmentation that makes `p` executable must provide at least the positive componentwise resource excess `[c(p)-B]_+` and must add every missing information, action/interface, and rule requirement used by `p`. Therefore every feasible augmentation enabling `p` has penalty at least `F(D_C(p))` by monotonicity of `F`. Conversely, augmentation by exactly `D_C(p)` makes every requirement on `p` available and raises the resource budget exactly enough to cover `c(p)`, so it enables `p`. Thus `F(D_C(p))` is the minimum augmentation penalty for that path. Minimizing over all seed-to-target paths proves the formula.

## Closure-Escape equivalence

**Status: PROVED finite-model criterion.** If `F(Delta)=0` iff `Delta=0`, then the following are equivalent:

1. `Omega_G(y|C)=0`;
2. some seed-to-`y` path has zero operational deficit;
3. `y` lies in the projected lifted budgeted operational closure under `C`.

This is a correct Closure-Escape criterion for the finite model, but by itself it is not yet the desired breakthrough theorem because its core path/reachability structure is close to mature constrained-path theory.

## Monotonicity

If `C'` weakly dominates `C` by increasing resource budget and adding information, interfaces/actions, and rules, then

`Omega_G(y|C') <= Omega_G(y|C)`.

This follows pathwise because every deficit component weakly decreases under context enlargement and `F` is monotone.

## Nonlinear capability-accounting upper bound

Whenever a concrete augmentation `Delta` makes `y` reachable,

`Omega_G(y|C) <= F(Delta)`.

For the implemented nonlinear `F`, this gives an explicit finite capability-accounting bound with an interaction term between resource increase and discrete information/interface/rule augmentation. This is a valid upper bound, not yet a universal law.

## Exhaustive audit

Independent implementations were compared:

1. brute-force enumeration of all bounded context augmentations; and
2. the exact path-deficit formula above.

Audit family:

- three states in a chain `0 -> 1 -> 2`;
- each of the two edges independently takes one of 24 types: resource cost in `{0,1,2}` and every subset of one binary information, action, and rule gate;
- 576 distinct worlds;
- base resource budgets in `{0,1,2}` and all eight base gate-availability combinations;
- 13,824 world/context cases.

Results:

- path formula versus independent augmentation enumeration: **0 mismatches**;
- `Omega_G=0` iff target is in lifted budgeted closure: **0 violations**;
- monotonicity under simultaneous context strengthening: **0 violations**;
- explicit nonlinear interaction case: one extra resource unit plus one missing information gate has `F=1+1+1*1=3`, confirming the implementation is not additive.

The executable audit is `gc2/tests/test_gc2_omega_gap.py`; implementation is `gc2/omega_gap.py`.

## Edge and degenerate cases

- Target already in seed set: `Omega_G=0` via the empty path.
- Zero-cost edges: permitted; lifted closure remains correct because resource use is cumulative and nonnegative.
- Impossible target: `Omega_G=+infinity` if no path exists even after allowed gate augmentation.
- Empty gate universes: reduction specializes to a resource-budget excess shortest-path problem.
- Zero resource dimension: reduction specializes to missing-information/interface/rule augmentation.
- If `F` is not positive definite, `Omega_G=0` need not characterize closure membership; positive definiteness is therefore necessary for the zero-gap Closure-Escape equivalence.
- If edge resource costs can be negative or replenishment is allowed, the current proof and finite path search require modification; those cases remain OPEN.

## Prior-art collision check

The resource component strongly overlaps the resource-constrained shortest-path literature, which studies paths under one or more cumulative resource budgets and has mature exact/approximation algorithms. Beasley and Christofides (1989) give an integer-programming and Lagrangian treatment for multiple resource constraints; later work studies multicriteria approximation. Statistical deficiency/Le Cam distance also provides a mature precedent for directed simulation gaps between experiments, though the present finite path-deficit object is not a statistical experiment deficiency.

Accordingly:

- **Exact path-deficit theorem:** PROVED in this operational model.
- **Closure-Escape zero-gap criterion:** PROVED in this operational model.
- **Nonlinear augmentation upper bound:** PROVED by the definition/path reduction.
- **Historical novelty / breakthrough claim:** OPEN; currently **not established** because of strong constrained-path/augmentation collisions.

## Next attack

The surviving route is to make `Omega_G` whole-envelope and translator-sensitive rather than single-target reachability-sensitive: require one globally realizable translator to reproduce a family of task/scale/error/resource profiles simultaneously, then search for matched low-order summaries with a provable global translation gap. That is where standard shortest-path reductions may cease to be complete.
