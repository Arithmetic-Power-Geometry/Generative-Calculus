#!/usr/bin/env python3
"""Exact finite verifier for GC-II Audit 351.

Enumerates all 3-state directed systems with six possible non-self edges,
each absent or carrying one of three nonnegative 2-resource costs. Compares
direct simple-path budget feasibility with the Pareto-frontier certificate.
"""
from itertools import product
import json

N = 3
ARCS = [(i, j) for i in range(N) for j in range(N) if i != j]
OPTIONS = [None, (1, 0), (0, 1), (1, 1)]
BUDGETS = list(product(range(4), repeat=2))


def simple_path_costs(edges, s, t):
    ans = []
    def dfs(v, seen, cost):
        if v == t:
            ans.append(cost)
            return
        for (a, b), c in edges.items():
            if a == v and b not in seen:
                dfs(b, seen | {b}, (cost[0] + c[0], cost[1] + c[1]))
    dfs(s, {s}, (0, 0))
    return ans


def pareto_min(vectors):
    vs = set(vectors)
    return sorted(v for v in vs if not any(
        u != v and u[0] <= v[0] and u[1] <= v[1] for u in vs
    ))


def leq(x, b):
    return x[0] <= b[0] and x[1] <= b[1]


def main():
    systems = comparisons = failures = multi_frontiers = 0
    max_frontier = 0
    for assignment in product(OPTIONS, repeat=len(ARCS)):
        systems += 1
        edges = {a: c for a, c in zip(ARCS, assignment) if c is not None}
        for s, t in ARCS:
            costs = simple_path_costs(edges, s, t)
            frontier = pareto_min(costs)
            if len(frontier) > 1:
                multi_frontiers += 1
            max_frontier = max(max_frontier, len(frontier))
            for budget in BUDGETS:
                direct = any(leq(c, budget) for c in costs)
                certificate = any(leq(p, budget) for p in frontier)
                comparisons += 1
                if direct != certificate:
                    failures += 1
                    raise AssertionError((edges, s, t, budget, costs, frontier))

    result = {
        "audit": 351,
        "states": N,
        "systems": systems,
        "ordered_pairs_per_system": len(ARCS),
        "budgets_per_pair": len(BUDGETS),
        "comparisons": comparisons,
        "failures": failures,
        "multi_frontier_instances": multi_frontiers,
        "max_frontier_cardinality_observed": max_frontier,
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
