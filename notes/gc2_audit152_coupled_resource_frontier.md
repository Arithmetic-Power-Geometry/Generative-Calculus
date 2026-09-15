# GC-II Audit 152 — Coupled resource frontier boundary

## Candidate tested
Audit 151 left a stronger gate: seek two operational systems with identical extensional capability and identical minimum cost on each single axis R, I, A, L, but different feasibility under a coupled admissibility budget.

Represent each exact realization by its nonnegative typed cost vector c=(R,I,A,L). Let U be the attainable cost set and define joint budget feasibility by existence of c in U with c <= b componentwise.

## Exact witness
System S1 has four exact realizations with cost vectors

(0,2,2,2), (2,0,2,2), (2,2,0,2), (2,2,2,0).

System S2 has the same four realizations plus (1,1,1,1).

Both systems therefore have identical single-axis minima:

min R = min I = min A = min L = 0.

Yet under joint budget b=(1,1,1,1), S1 is infeasible while S2 is feasible. All five displayed vectors are Pareto-nondominated in their respective sets. Hence single-axis accounting provably fails to determine coupled feasibility.

The checker exhaustively evaluates all 3^4=81 budgets in {0,1,2}^4. Exactly one budget separates the systems: (1,1,1,1). It also checks equality of all four marginal minima and nondominance of every listed realization.

## What this proves — and what it does not
This proves that four scalar single-axis minima are an incomplete capability-accounting summary. The missing object is at least the joint attainable-cost upper set / Pareto frontier, not an additive scalar assembled from the four minima.

However, this is not a GC-II novelty result. Multiobjective and resource-constrained shortest-path/optimization theory explicitly retains nondominated resource vectors and Pareto-optimal solutions; joint resource constraints can distinguish systems with identical coordinatewise minima. Thus defining Omega_G merely as the discrepancy exposed by a coupled budget would repackage standard multi-resource Pareto geometry.

## Ledger
- Same extensional target + identical R/I/A/L single-axis minima + different coupled feasibility: **PROVED**.
- Exact 81-budget regression: **PASS**.
- Sufficiency of four single-axis minima for capability accounting: **FALSIFIED**.
- Pareto-frontier / joint attainable-resource mechanism: **IMPORTED/KNOWN**.
- Coupled-budget separation alone as a nontrivial Generative Novelty Gap: **FALSIFIED**.
- Candidate requiring history-dependent cross-resource conversion/admissibility not representable by an ordinary joint attainable-cost set on complete realizations: **OPEN**.

## Consequence for Omega_G
Do not define Omega_G from coordinatewise minima alone. Any representation-invariant finite-world accounting must at minimum preserve the downward feasibility region (equivalently the nondominated attainable-cost frontier, with orientation adjusted to the cost convention). A genuinely new candidate must distinguish systems even after this full static frontier is matched.

## Next gate
Construct two systems with identical extensional capability and identical complete Pareto frontier of total (R,I,A,L) realization costs, but different capability under sequentially released budgets or endogenous resource conversion. Then test whether the separation survives reductions to resource-constrained planning/MDPs, Petri nets/vector-addition systems, multi-resource scheduling, and process resource theories. If it does not, record another boundary rather than claiming novelty.
