# GC-II Audit 091 — Singleton-Frontier Incompleteness Under Joint Reuse

## Scope
Branch-only Paper-II audit following Audit 090. GC-I `main` remains frozen.

## Question
If two systems have exactly the same typed cost/frontier for every task considered separately, can their joint budgeted capability closures still differ?

## Construction
Let the task set be \(Q=\{T_1,T_2,T_3\}\). For any subset \(S\subseteq Q\), let \(k=|S|\) and use typed costs \((R,I,A,L)\).

System A (one reusable setup):
- \(c_A(\varnothing)=(0,0,0,0)\).
- For \(k\ge1\), \(c_A(S)=(k+1,k,0,0)\).

System B (setup repaid per task):
- \(c_B(\varnothing)=(0,0,0,0)\).
- For \(k\ge1\), \(c_B(S)=(2k,k,0,0)\).

For every singleton task,
\[
c_A(\{T_i\})=c_B(\{T_i\})=(2,1,0,0).
\]
Thus all singleton typed costs/frontiers are identical.

For budget \(b\), define the joint closure
\[
\mathcal C_X(b)=\{S\subseteq Q:c_X(S)\le b\text{ coordinatewise}\}.
\]

## Proposition — singleton-frontier incompleteness
Equality of all singleton typed frontiers does not imply equality of joint budgeted closure.

### Proof
At budget \(b=(3,2,0,0)\), every two-task subset \(S\) satisfies
\[
c_A(S)=(3,2,0,0)\le b,
\]
while
\[
c_B(S)=(4,2,0,0)\not\le b.
\]
Hence \(\mathcal C_A(b)\ne\mathcal C_B(b)\), despite identical singleton typed frontiers. QED.

## General family
For \(n\) tasks with the same definitions,
\[
c_A(S)=(|S|+1,|S|,0,0),\qquad
c_B(S)=(2|S|,|S|,0,0)
\]
for nonempty \(S\).

At budget \(b_k=(k+1,k,0,0)\), System A can jointly realize \(k\) tasks, whereas System B can realize at most
\[
\left\lfloor\frac{k+1}{2}\right\rfloor.
\]
Thus the hidden joint-capability difference can grow with \(k\); it is not a one-off finite artifact.

## Exact finite check
`experiments/gc2_joint_reuse_closure.py` exhausts budgets
\[
b_R\in\{0,\ldots,6\},\quad
b_I\in\{0,\ldots,3\},\quad
b_A,b_L\in\{0,1\}.
\]

Exact results:
- budgets checked: **112**
- budgets with different joint closures: **16**
- budgets where A has larger maximum feasible task cardinality: **16**
- budgets where B has larger maximum feasible task cardinality: **0**
- maximum observed cardinality advantage in this 3-task experiment: **1**
- singleton typed cost/frontier mismatch: **0**

The CSV is `results/gc2_joint_reuse_closure.csv`.

## Dimension/domain/edge audit
- All four budget coordinates are nonnegative and compared only coordinatewise.
- No physical commensurability between R/I/A/L is assumed.
- Empty task set costs zero in both systems.
- Singleton costs are exactly equal.
- Costs are monotone under set inclusion.
- A exhibits reusable setup/economies of scope; B does not.
- At sufficiently large budgets both systems realize all tasks, so the distinction is budget-indexed rather than absolute.
- The construction is deterministic; no statistical estimation is involved.

## Prior-art collision
This positive separation is **not** a GC-II breakthrough. The mechanism is ordinary joint-cost structure: fixed/shared setup costs, economies of scope, subadditive cost functions, and combinatorial cost sharing already formalize cases where the cost of a bundle cannot be recovered from singleton costs.

In particular, combinatorial cost-sharing models explicitly assign a cost to every combination of services and study subadditive/submodular cost functions. Facility-location and cooperative-cost models likewise capture shared infrastructure costs. Therefore “same singleton costs but different bundle costs” is an established phenomenon, even though it is a useful warning for capability accounting.

## Consequence
Audit 090 showed scalar summaries are incomplete for typed budgets.
Audit 091 now shows that even the **entire collection of singleton typed frontiers** is incomplete for joint capability when reusable/shared structure is allowed.

Therefore GC-II cannot claim novelty merely from replacing scalar scores by per-task vector frontiers. The primitive must include higher-order/joint operational structure (or an equivalent complete representation).

A stronger candidate would need to hold fixed not merely singleton frontiers but the relevant known joint-cost/submodular summaries and still produce an operationally testable difference. Otherwise the effect is imported multi-task optimization.

## Status ledger
- Explicit separation construction: **PROVED**.
- General \(n\)-task growing gap formula: **PROVED**.
- 112-budget finite checker: **NUMERICALLY SUPPORTED / exact enumeration**.
- “Singleton typed frontiers determine joint closure”: **FALSIFIED**.
- Shared-reuse explanation: **IMPORTED/KNOWN mechanism**.
- Standalone GC-II breakthrough status: **NONE**.
