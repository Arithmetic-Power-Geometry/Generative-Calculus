# GC-II Audit 325 — Budgeted Closure-Escape Value

## Scope

This audit strengthens Audit 324 from a qualitative finite-escape test to an exact quantitative capability-accounting object for finite deterministic operational cells with branch-relative admissibility.

Status labels below distinguish GC-II consequences from imported dynamic-programming machinery.

## Operational model

Let `C` be a finite information cell. A decision map `g` partitions worlds into decision classes. A cell is terminal when `g` is constant on it.

At each nonterminal cell `C`, the currently admissible action set is `Adm(C)`. Each action `u` has nonnegative cost `c(C,u)` in one fixed resource unit and deterministic observation map `Z_u`. For outcome `y`,

`C_{u,y} = {x in C : Z_u(x)=y}`.

Admissibility and cost may depend on the reached cell. No hereditary catalogue is assumed.

A policy resolves `C` when every outcome branch reaches a terminal cell after finitely many actions. Its worst-case accumulated cost is the maximum branch cost.

Define the exact Closure-Escape value

`V(C) = inf_pi sup_branch Cost_pi(branch)`,

with `V(C)=+infinity` if no finite resolving admissible policy exists.

## Theorem 325.1 — exact Bellman value

For every terminal cell, `V(C)=0`. For every nonterminal finite cell,

`V(C) = inf_{u in Adm(C)} [ c(C,u) + max_{y:C_{u,y} nonempty} V(C_{u,y}) ]`,

where the value is interpreted as the least extended-nonnegative solution consistent with finite resolving policies. An action whose outcome can remain forever in an unresolved zero-progress cycle cannot create a spurious finite value merely by satisfying an algebraic fixed-point equality.

**Status: PROVED / Bellman minimax mechanism IMPORTED-KNOWN.**

Proof. Any resolving policy has a first admissible action `u`. After outcome `y`, its continuation is a resolving policy for `C_{u,y}`, so its worst-case cost is at least `c(C,u)+max_y V(C_{u,y})`. Taking the infimum over first actions gives the lower bound. Conversely, for any first action whose children have finite values, concatenate epsilon-optimal child policies; in the finite attained-cost case choose optimal child policies. This gives the reverse inequality. The least-solution qualification excludes non-well-founded self-supporting zero-cost cycles. QED.

## Theorem 325.2 — budget/value equivalence

For budget `B>=0`, define `Win(B)` as the cells possessing a resolving admissible policy whose worst-case accumulated cost is at most `B`. Then

`C in Win(B)  iff  V(C)<=B`.

For strictly positive integer costs and integer budget `b`, the sets are computed exactly by

`Win(0) = {terminal cells}`,

and, for `b>=1`, a nonterminal cell `C` belongs to `Win(b)` iff there exists `u in Adm(C)` with `c(C,u)<=b` such that every nonempty child satisfies

`C_{u,y} in Win(b-c(C,u))`.

**Status: PROVED.**

This is a quantitative version of Audit 324: qualitative Closure Escape is equivalent to `V(C)<infinity`; budgeted Closure Escape is equivalent to crossing the value threshold.

## Corollary 325.3 — exact operational novelty deficit at budget B

For a target decision task on cell `C`, define the budget-relative escape deficit

`Omega_B(C) = max(0, V(C)-B)`

when `V(C)<infinity`, and `Omega_B(C)=+infinity` otherwise.

Then

`Omega_B(C)=0  iff  C in Win(B)`.

This quantity has the same units as the charged operational cost and is invariant under relabelling worlds, actions, and outcomes that preserves the operational transition/cost structure.

**Status: PROVED as a task-relative operational deficit; OPEN as a universal Generative Novelty Gap.**

Important: this audit does **not** identify `Omega_B` with the full Paper-II `Omega_G`. It is a controlled candidate component. Calling it universal novelty would be unjustified because it is task-, cost-model-, and interface-relative.

## Monotonicity and edge cases

1. Budget monotonicity: `B1<=B2` implies `Win(B1) subseteq Win(B2)` and `Omega_{B2}(C)<=Omega_{B1}(C)`. **PROVED.**
2. Adding admissible actions cannot increase `V`. **PROVED.**
3. Increasing any action cost while holding the transition/admissibility system fixed cannot decrease `V`. **PROVED.**
4. Terminal cells have `V=0` and zero deficit for every nonnegative budget. **PROVED.**
5. An unresolved cell with no admissible action has `V=+infinity`. **PROVED.**
6. Zero-cost unresolved cycles require least-fixed-point/well-founded semantics; naive algebraic Bellman equations can admit false finite solutions. **DECISIVE EDGE CASE.**
7. Rescaling every cost and budget by `lambda>0` rescales finite `V` and `Omega_B` by `lambda`. **PROVED; dimensional consistency.**
8. Parallel/vector resource budgets are not represented by this scalar value without a declared scalarization. **OPEN / no scalar-collapse claim.**

## Composition warning

No additive law `V(C1 x C2)=V(C1)+V(C2)` is claimed. Shared actions, correlated outcomes, interfaces, and branch-relative admissibility can create subadditive or superadditive behavior depending on the composition rule. Therefore a Paper-II capability bound cannot assume additive decomposition merely from this scalar Bellman value.

**Status: additive composition law — OPEN in structured subclasses, false as an unrestricted assumption.**

## Relation to Audit 324

Audit 324 proved the finite qualitative equivalence between resolving policies, a least winning fixed point, descending escape rank, and absence of an adversarial closure-trap kernel. Audit 325 assigns the exact minimum worst-case charged cost to the winning region and makes budget crossing computationally explicit.

The qualitative escape rank and quantitative value are different invariants: rank counts well-founded resolution depth; value charges actions. Equal rank need not imply equal value, and equal value need not imply equal rank.

## Prior-art collision discipline

The minimax Bellman recursion, AND-OR dynamic programming, shortest/worst-case policy cost, and budgeted reachability mechanisms are established in dynamic programming, planning, diagnosis, and game/reachability theory. They are **IMPORTED/KNOWN mechanisms**. The defensible GC-II contribution here is the placement of an exact charged value on the branch-relative Closure-Escape object developed in Audits 319–324, plus the explicit warning that this value is only a task-relative candidate component of `Omega_G`.

## Current boundary

- Exact scalar-cost budgeted closure value: **PROVED**.
- `V<infinity` iff qualitative Closure Escape: **PROVED**.
- Budget threshold `V<=B` iff budgeted winning policy exists: **PROVED**.
- `Omega_B=max(0,V-B)` as a task-relative charged deficit: **PROVED**.
- `Omega_B` as the universal Generative Novelty Gap: **OPEN / NOT CLAIMED**.
- Vector-resource Pareto value, information acquisition costs, interface/action expansion, and rule changes in one joint theorem: **OPEN**.
- Non-additive quantitative bound `Omega_G <= F(Delta R,Delta I,Delta A,Delta L)`: **OPEN**.
