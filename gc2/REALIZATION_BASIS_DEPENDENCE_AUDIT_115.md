# GC-II Audit 115 — Realization-Basis Dependence No-Go

## Target
Test the surviving Audit-114 proposal: couple semantic expansion to typed realization burden under a fixed external boundary, while demanding basis/refactoring invariance.

## Definitions
Let `Sem(r)` denote the operational semantics realized by implementation `r`. For an admissible realization class `R_B` fixed by boundary `B`, with typed nonnegative cost vector `c_B(r)`, define the Pareto realization set

`P_B(s) = Min_{<=} { c_B(r) : r in R_B, Sem(r)=s }`.

For scalarization `lambda >= 0`, define

`C_{B,lambda}(s) = inf_{r in R_B: Sem(r)=s} lambda · c_B(r)`.

This is quotient-invariant under refactorings that preserve both semantics and typed cost, but not under arbitrary changes of primitive basis or cost accounting.

## Proposition 115.1 — Realization Optimization Absorption
**Status: PROVED / IMPORTED-KNOWN mechanism.**

Once `(R_B, Sem, c_B)` is independently fixed, computing `C_{B,lambda}(s)` is exactly minimum-cost implementation/synthesis in that realization model. The proof is definitional: feasible points are precisely implementations realizing `s`; the objective is precisely their realization cost. Thus the generic construction does not by itself yield a new GC-II law. Depending on `R_B`, it instantiates minimum circuit size, multiplicative/energy complexity, exact circuit synthesis, program synthesis, network design, or resource-constrained planning.

This is not a claim that all such optimization problems are easy or mutually reducible. It is a novelty collision: the generic minimum-realization functional is already the standard optimization template of the chosen implementation model.

## Proposition 115.2 — Basis-Invariance Impossibility Without a Translation Convention
**Status: PROVED.**

There is no exact, nontrivial minimum gate-count functional that is simultaneously (i) defined by minimum realization cost and (ii) invariant under arbitrary complete primitive-basis changes with unit gate costs.

Proof by counterexample: consider two complete Boolean bases with free inputs/constants: `B1={AND,OR,NOT}` and `B2={NAND}`. The function `AND(x,y)` has cost 1 in B1 but cost 2 in B2 (`NAND` followed by self-`NAND`). Conversely `NAND(x,y)` has cost 2 in B1 but 1 in B2. Therefore exact realization cost is boundary/basis-relative. QED.

A translation theorem can relate costs across bases, but then the constants/distortion are properties of the chosen compiler/bases; they do not produce exact basis independence.

## Exact finite checker
`experiments/gc2_realization_basis_collision_audit.py` exhaustively computes expression-tree minimum gate costs for all 16 Boolean functions of two variables under the two bases above. The independently frozen output is in `results/gc2_realization_basis_collision_audit.json`.

Result: 16/16 functions reachable in both complete bases; 8/16 have different exact minimum costs; maximum minimum cost is 4 under AND/OR/NOT and 5 under NAND-only. This is a finite counterexample to exact basis-independent realization burden, not evidence of a new invariant.

## Prior-art collision
Boolean circuit complexity already defines complexity of a function as minimum circuit size over a specified basis; multiplicative and energy complexity similarly minimize selected gate/resource measures. Minimum Circuit Size asks for the smallest circuit representing a fixed Boolean function. Exact synthesis work, including 2026 T-count synthesis, optimizes implementation cost under a fixed gate library and equivalence relation. Resource-constrained shortest-path/planning formulations likewise optimize typed costs over admissible realization paths.

## Consequences for Omega_G
Rejected candidate:

`Omega_G(s;B) := C_{B,lambda}(s)` as a generic GC-II novelty measure.

It is useful capability accounting, but without an additional theorem it is implementation complexity relative to B.

Also rejected: demanding exact invariance under arbitrary basis replacement while retaining exact physical/implementation cost. A basis change can alter the physically admissible primitives and therefore legitimately alter cost.

## Surviving target
The next scientifically defensible target must be a **comparison law across realization boundaries**, not another minimum-cost definition. Seek a theorem of the form

`dist(P_B(s), T_{B'->B} P_{B'}(s)) <= Phi(kappa(B,B'), semantic_defect, interface_defect)`

where the translator `T` and distortion `kappa` are independently operationally defined, and then identify a residual that cannot be removed by any admissible translator. The residual must be tested against simulation/interpretation overhead, compiler invariance, circuit reductions, resource-theory conversion rates, and algorithmic-information invariance theorems.

A breakthrough would require a nonzero, quotient-stable residual with an independently derived lower bound and a capability consequence not already equivalent to standard simulation overhead or implementation complexity.

## Status ledger
- Minimum typed realization functional: **IMPORTED/KNOWN template**.
- Realization Optimization Absorption: **PROVED**.
- Exact basis-independent minimum gate cost: **FALSIFIED**.
- Finite two-variable collision checker: **PROVED computationally by exhaustive fixed point**.
- Cross-boundary translator residual: **OPEN**.
- Nontrivial GC-II quantitative bound from that residual: **OPEN**.

## Kill rule
Do not claim novelty from `min cost over implementations realizing semantics`. Do not claim basis invariance by simply quotienting syntax. Any next candidate must specify two independently meaningful boundaries, admissible translators between them, and prove that a residual survives optimal translation.
