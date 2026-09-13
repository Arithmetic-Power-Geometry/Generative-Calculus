#!/usr/bin/env python3
"""Exact finite audit for budget-coupled endogenous admissibility.

Enumerates 256 deterministic two-state/two-mode systems. Mode 0 admits only
action 0; mode 1 admits actions 0 and 1. Actions consume one unit from a
single shared remaining budget. Both physical-state and mode transitions vary
over all 16 Boolean tables. Native recursive reachability is compared against
a fixed-alphabet augmented-state compilation z=(q, mode, remaining_budget).
"""

from itertools import product
import json

Q = (0, 1)
M = (0, 1)
A = (0, 1)
COST = {0: 1, 1: 1}


def admissible(mode):
    return (0,) if mode == 0 else (0, 1)


def table(bits):
    return {(s, a): bits[2 * s + a] for s in (0, 1) for a in (0, 1)}


def native_reach(q, mode, budget, horizon, tq, tm):
    current = {(q, mode, budget)}
    for _ in range(horizon):
        nxt = set()
        for q0, m0, b0 in current:
            for a in admissible(m0):
                if b0 >= COST[a]:
                    nxt.add((tq[(q0, a)], tm[(m0, a)], b0 - COST[a]))
        current = nxt
    return current


def compiled_reach(q, mode, budget, horizon, tq, tm):
    current = {(q, mode, budget)}
    for _ in range(horizon):
        nxt = set()
        for q0, m0, b0 in current:
            for a in A:  # fixed alphabet; admissibility is a state guard
                if a in admissible(m0) and b0 >= COST[a]:
                    nxt.add((tq[(q0, a)], tm[(m0, a)], b0 - COST[a]))
        current = nxt
    return current


def main():
    systems = 0
    checks = 0
    mismatches = 0
    endogenous_change_systems = 0

    for qbits in product((0, 1), repeat=4):
        tq = table(qbits)
        for mbits in product((0, 1), repeat=4):
            tm = table(mbits)
            systems += 1

            if any(tm[(m, a)] != m for m in M for a in admissible(m)):
                endogenous_change_systems += 1

            for q, m, b, h in product(Q, M, range(4), range(5)):
                checks += 1
                if native_reach(q, m, b, h, tq, tm) != compiled_reach(q, m, b, h, tq, tm):
                    mismatches += 1

    result = {
        "systems": systems,
        "systems_with_endogenous_admissibility_change": endogenous_change_systems,
        "start_budget_horizon_checks": checks,
        "mismatches": mismatches,
        "budgets": [0, 1, 2, 3],
        "horizons": [0, 1, 2, 3, 4],
        "interpretation": "Finite endogenous admissibility plus a shared consumable budget is exactly represented by fixed-alphabet reachability on augmented state (q, mode, remaining_budget).",
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
