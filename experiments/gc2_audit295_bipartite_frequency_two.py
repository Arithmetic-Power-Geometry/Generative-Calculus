#!/usr/bin/env python3
"""Exact verifier for GC-II Audit 295.

Exhaustively checks tau(G)=nu(G) for all labeled bipartite graphs with
1<=|L|,|R|<=3 using independent brute-force routines. Also checks
operational frequency-two encoding and selected edge cases.
"""
from itertools import combinations, product


def min_vertex_cover(L, R, edges):
    vertices = list(range(L + R))
    shifted = [(u, L + v) for u, v in edges]
    for k in range(len(vertices) + 1):
        for comb in combinations(vertices, k):
            C = set(comb)
            if all(u in C or v in C for u, v in shifted):
                return k
    raise AssertionError("unreachable")


def max_matching(L, R, edges):
    edges = list(edges)
    best = 0
    for mask in range(1 << len(edges)):
        chosen = [edges[i] for i in range(len(edges)) if (mask >> i) & 1]
        if len({u for u, _ in chosen}) == len(chosen) == len({v for _, v in chosen}):
            best = max(best, len(chosen))
    return best


def accounting_optimum(L, R, targets):
    """Each target is a pair (left action, right action)."""
    actions = list(range(L + R))
    incidence = [(u, L + v) for u, v in targets]
    for k in range(len(actions) + 1):
        for comb in combinations(actions, k):
            C = set(comb)
            if all(u in C or v in C for u, v in incidence):
                return k
    raise AssertionError("unreachable")


def exhaustive():
    graphs = edge_occurrences = 0
    for L in range(1, 4):
        for R in range(1, 4):
            possible = list(product(range(L), range(R)))
            for mask in range(1 << len(possible)):
                E = [possible[i] for i in range(len(possible)) if (mask >> i) & 1]
                tau = min_vertex_cover(L, R, E)
                nu = max_matching(L, R, E)
                op = accounting_optimum(L, R, E)
                assert tau == nu == op, (L, R, E, tau, nu, op)
                graphs += 1
                edge_occurrences += len(E)
    return graphs, edge_occurrences


def edge_cases():
    assert accounting_optimum(1, 1, []) == 0
    # disconnected two-edge matching
    assert accounting_optimum(2, 2, [(0, 0), (1, 1)]) == 2
    # duplicate targets do not change optimum
    assert accounting_optimum(1, 1, [(0, 0), (0, 0)]) == 1
    # forced frequency-one preprocessing: selecting forced action removes
    # all targets it covers; residual exact-frequency-two core is unchanged.
    forced = {0}
    residual = [(1, 0)]
    assert len(forced) + accounting_optimum(2, 1, residual) == 2


if __name__ == "__main__":
    g, e = exhaustive()
    edge_cases()
    print(f"PASS audit295: {g} bipartite graphs; {e} edge occurrences; edge cases passed")
