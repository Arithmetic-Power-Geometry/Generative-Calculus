# GC-II Audit 090 — Controlled AI Typed-Budget Closure Baseline

## Scope
Branch-only Paper-II application experiment. GC-I `main` remains frozen.

## Question
Can two AI agents that look identical under an ordinary unconstrained benchmark and a conventional scalar resource score nevertheless have different GC-style typed budget closures?

## Controlled construction
Use four task labels T1..T4 and typed nonnegative cost vectors `(R,I,A,L)`.

Agent A:
- T1: (2,0,0,0)
- T2: (0,2,0,0)
- T3: (0,0,2,0)
- T4: (0,0,0,2)

Agent B:
- T1: (1,1,0,0)
- T2: (0,1,1,0)
- T3: (0,0,1,1)
- T4: (1,0,0,1)

Both agents:
1. solve all four tasks when budgets are unconstrained;
2. have identical uniform scalar cost `R+I+A+L=2` for every task.

For a budget `b=(b_R,b_I,b_A,b_L)`, define the exact budgeted task closure

`C_X(b) = {q : c_X(q) <= b coordinatewise}`.

The experiment exhausts every budget in `{0,1,2}^4`.

## Exact result
The executable artifact `experiments/gc2_ai_typed_budget_closure.py` and CSV `results/gc2_ai_typed_budget_closure.csv` give:

- total budgets: **81**
- budgets with different task closures: **65**
- budgets where Agent A enables more tasks: **18**
- budgets where Agent B enables more tasks: **35**
- budgets with equal task count: **28**
- unconstrained task coverage: identical
- uniform scalar cost per task: identical (=2)

All counts are exact finite enumeration, not simulation estimates.

## Interpretation
This is a useful application sanity check but **not a GC-II breakthrough**.

A single benchmark success score or a single scalar cost can erase information that a typed partial order retains. That phenomenon is standard multiobjective/Pareto reasoning. The experiment therefore supports the practical need for typed closure accounting, but it cannot be used as a novelty theorem.

## Dimensional/domain audit
- R,I,A,L are treated as abstract typed budget coordinates, not as physically commensurate quantities.
- No illegal scalar addition is used in the closure definition; scalar `R+I+A+L` appears only as the deliberately lossy conventional baseline.
- Costs and budgets are nonnegative integers.
- Feasibility uses coordinatewise dominance.
- Degenerate budget (0,0,0,0): both closures empty.
- Maximal budget (2,2,2,2): both closures contain all tasks.
- Budget monotonicity holds by construction: if b<=b' coordinatewise, then C_X(b) subseteq C_X(b').

## Prior-art collision
The mechanism is ordinary loss under scalarization of a vector-valued/multiobjective feasible region. Pareto frontiers and support/scalarization methods are mature optimization machinery. Therefore the experiment is classified as application validation only.

Related collision neighborhoods to retain for later AI experiments:
- multiobjective optimization / Pareto dominance;
- constrained MDPs and resource-constrained planning;
- AI benchmark aggregation and capability profiles;
- decision-theoretic comparison under task families;
- resource theories and convertibility preorders.

## Status ledger
- Exact finite experiment: **NUMERICALLY SUPPORTED / exact enumeration**.
- Typed-budget closure distinction despite equal unconstrained coverage and equal uniform scalar cost: **PROVED by explicit finite construction**.
- Claim that scalar benchmark equality implies typed closure equality: **FALSIFIED**.
- Standalone novelty of the phenomenon: **IMPORTED/KNOWN mechanism**.
- GC-II breakthrough status: **NONE**.

## Consequence for the next application test
The next AI experiment must be stronger than scalar-vs-vector bookkeeping. It should keep the same typed marginal cost/frontier summaries fixed and search for a difference caused by shared translators, sequential composition, branching, or whole-envelope obligations. A positive result is useful only if it survives reduction to ordinary MDP/POMDP, multiobjective planning, simulation, communication/query complexity, and known benchmark-profile effects.
