#!/usr/bin/env python3
"""Exact finite verifier for GC-II Audit 350.

Exhausts all directed 3-state operational graphs in which each possible
non-self edge is absent or has integer acquisition cost 1, 2, or 3.
For every ordered source-target pair and budgets 0..6, compares direct
subset-enabling semantics with the min-plus shortest-path threshold.
"""
from itertools import product
from math import inf
import json

N = 3
MAX_BUDGET = 6
EDGES = [(i, j) for i in range(N) for j in range(N) if i != j]


def reachable(n, chosen, s, t):
    adj = [[] for _ in range(n)]
    for u, v in chosen:
        adj[u].append(v)
    seen = {s}
    stack = [s]
    while stack:
        u = stack.pop()
        for v in adj[u]:
            if v not in seen:
                seen.add(v)
                stack.append(v)
    return t in seen


def brute_enabled(n, edge_cost, s, t, budget):
    edges = list(edge_cost)
    for mask in range(1 << len(edges)):
        cost = sum(edge_cost[edges[i]] for i in range(len(edges)) if (mask >> i) & 1)
        if cost > budget:
            continue
        chosen = [edges[i] for i in range(len(edges)) if (mask >> i) & 1]
        if reachable(n, chosen, s, t):
            return True
    return False


def bellman_minplus(n, edge_cost, s):
    d = [inf] * n
    d[s] = 0
    for _ in range(n - 1):
        nd = d[:]
        for (u, v), c in edge_cost.items():
            nd[v] = min(nd[v], d[u] + c)
        d = nd
    return d


def main():
    cases = failures = configurations = 0
    for values in product(range(4), repeat=len(EDGES)):
        # 0 means absent; 1..3 are nonnegative/positive acquisition costs.
        edge_cost = {e: c for e, c in zip(EDGES, values) if c}
        configurations += 1
        for s in range(N):
            d = bellman_minplus(N, edge_cost, s)
            for t in range(N):
                if s == t:
                    continue
                for budget in range(MAX_BUDGET + 1):
                    cases += 1
                    direct = brute_enabled(N, edge_cost, s, t, budget)
                    threshold = d[t] <= budget
                    if direct != threshold:
                        failures += 1
                        raise AssertionError((edge_cost, s, t, budget, direct, d[t]))
    out = {
        "audit": 350,
        "states": N,
        "edge_assignments": "absent or cost in {1,2,3}",
        "configurations": configurations,
        "ordered_source_target_pairs_per_configuration": N * (N - 1),
        "budgets": list(range(MAX_BUDGET + 1)),
        "exact_cases": cases,
        "failures": failures,
    }
    print(json.dumps(out, indent=2))


if __name__ == "__main__":
    main()
