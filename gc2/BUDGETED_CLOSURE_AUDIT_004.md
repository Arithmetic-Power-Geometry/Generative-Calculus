# GC-II Budgeted Operational Closure Audit 004

Date: 2026-09-08
Branch: `gc2-capability-accounting-lab`

## Executive result

A naive budgeted reachability map on base world-states is **not a closure operator** in general. The failure is idempotence: applying the same budget again silently refreshes the budget. This is not a notation issue; it changes the mathematics of every proposed Closure-Escape or No-Free-Capability theorem.

The repair is to lift the operational state by cumulative resource expenditure (or an equivalent remaining-budget coordinate). On the lifted state space, admissible transformations update cumulative expenditure and are blocked once any resource coordinate exceeds the total budget. Reachability closure on this lifted graph is extensive, monotone, and idempotent.

Status of the naive base-state closure claim: **FALSIFIED**.

Status of lifted budgeted operational closure: **PROVED for finite typed worlds with nonnegative vector resource increments; computationally exhaustively checked on the finite audit family described below.**

## 1. Typed finite operational world

A finite operational world is a tuple

`W = (S, T, Q, R, I, A, L, Gamma)`

where:

- `S` is a finite set of physical/computational world states;
- `T` is a finite task set;
- `Q` is a set of task scales and error tolerances;
- `R` is a resource space `N^d` with componentwise order;
- `I` specifies information available to an operation;
- `A` specifies admissible interfaces/actions;
- `L` specifies admissible rules/laws;
- `Gamma` is the set of admissible transformations.

Each transformation `g in Gamma` has typed source and target states, an information/interface/rule admissibility predicate, and a nonnegative vector increment

`c(g) in N^d`.

A path `p = g_1 ... g_k` is admissible exactly when every transformation is type-compatible and admissible under `(I,A,L)`. Its resource cost is

`C(p) = sum_j c(g_j)`.

The nonnegativity assumption is essential for the finite cumulative-budget semantics used here.

## 2. Naive base-state map and decisive counterexample

For a base-state set `X subseteq S` and budget `B in N^d`, define

`Reach_B(X) = { y in S : there exists x in X and an admissible path x -> y with C(p) <= B }`.

It is tempting to call `Reach_B` a closure operator. In general this is false.

Take the one-resource world

`x --1--> y --1--> z`

and budget `B=1`. Then

`Reach_1({x}) = {x,y}`,

but

`Reach_1(Reach_1({x})) = {x,y,z}`.

Thus

`Reach_B(Reach_B(X)) != Reach_B(X)`.

The second application has refreshed the budget. Therefore any GC-II theorem that uses repeated base-state budget closure without tracking expenditure is ill-posed.

## 3. Lifted operational state

Fix total budget `B in N^d`. Define the lifted state space

`S_B^+ = { (s,r) : s in S, 0 <= r <= B }`,

where `r` records cumulative resource expenditure.

Every admissible base transformation `g:s->s'` with cost `c(g)` induces

`(s,r) -> (s', r+c(g))`

iff `r+c(g) <= B` componentwise and the information/interface/rule predicates remain admissible.

For `X subseteq S_B^+`, define

`Cl_B^+(X)`

as ordinary graph reachability in this lifted graph, including zero-length paths.

## 4. Lifted Closure Theorem

**Theorem 004-A (Finite lifted budgeted operational closure).** For every finite typed operational world with nonnegative vector transformation costs and fixed total budget `B`, `Cl_B^+` is a closure operator on subsets of `S_B^+`:

1. Extensivity: `X subseteq Cl_B^+(X)`.
2. Monotonicity: `X subseteq Y => Cl_B^+(X) subseteq Cl_B^+(Y)`.
3. Idempotence: `Cl_B^+(Cl_B^+(X)) = Cl_B^+(X)`.

**Proof.** `Cl_B^+` is ordinary reachability closure in a fixed directed graph. Extensivity follows from zero-length paths. Monotonicity follows because every path starting in `X` also starts in `Y` when `X subseteq Y`. For idempotence, if `v` is reachable from some `u` already reachable from `X`, concatenating the two lifted paths gives a lifted path from `X` to `v`; cumulative expenditure is part of the vertex state, so no budget is refreshed. The reverse inclusion follows from extensivity. QED.

The theorem is elementary graph-reachability mathematics; it is **not claimed as novel**. Its importance is that it fixes the object on which GC-II's later novelty-gap and closure-escape statements must be formulated.

## 5. Budget monotonicity

If `B <= B'`, every lifted trajectory feasible under `B` embeds into the `B'` lifted graph. After projecting away the expenditure coordinate,

`pi_S Cl_B^+(X x {0}) subseteq pi_S Cl_B'^+(X x {0})`.

Status: **PROVED** under the same nonnegative-cost assumptions.

## 6. Composition law without budget refresh

If a lifted state `(y,r)` is reachable from `(x,0)` and `(z,r')` is reachable from `(y,r)` in the same fixed lifted graph, then `(z,r')` is already in `Cl_B^+({(x,0)})` by path concatenation. This is exactly the idempotence mechanism and is the correct resource-accounted replacement for repeated base-state closure.

## 7. Exact finite audit

`gc2/tests/test_gc2_budgeted_closure.py` performs:

- the explicit three-state falsification above;
- exhaustive enumeration of all directed three-state worlds in which each non-loop edge is absent, cost 0, or cost 1 (`3^6 = 729` worlds);
- all singleton starts and budgets `B=0,1,2`, giving `6,561` singleton-start/budget cases;
- base reachability extensivity and budget monotonicity checks;
- lifted closure extensivity and idempotence checks;
- lifted monotonicity for **every inclusion pair among all 8 zero-expenditure start subsets** at each budget in every world, giving `59,049` inclusion checks.

The exact audit completed with no violations in a local execution of the committed logic.

The test uses only the Python standard library.

## 8. Consequences for the Paper-II program

1. **Operational closure is no longer OPEN at the finite formal-definition level.** A defensible object is now available: lifted reachability with explicit cumulative vector expenditure and typed admissibility.
2. A candidate `Omega_G` should compare capabilities outside the projection of `Cl_B^+`, not outside a repeatedly refreshed base-state `Reach_B`.
3. A Closure-Escape theorem must state whether escape occurs in the lifted world or only after projection to base states/tasks.
4. A No-Free-Capability theorem must quantify admissible changes in `Gamma`, `I`, `A`, and `L`; changing any of these can change the lifted graph even when the numerical resource budget is unchanged.
5. Resource coordinates that can be negative, replenished, borrowed, or generated require an extended state variable and cannot be folded into the present nonnegative cumulative-cost theorem without extra assumptions.

## Status ledger

- Naive base-state budget closure as a closure operator: **FALSIFIED**.
- Lifted finite budgeted operational closure: **PROVED**.
- Novelty claim for the closure theorem itself: **IMPORTED/KNOWN mechanism (graph reachability)**.
- Usefulness for GC-II architecture: **VALIDATED**.
- Generative Novelty Gap `Omega_G`: **OPEN**, now with a corrected domain.
- Closure-Escape theorem: **OPEN**, now with a corrected closure object.
- Breakthrough status: **NONE YET**.
