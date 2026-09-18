#!/usr/bin/env python3
"""Exact verifier for GC-II Audit 237.

Exhibits two translator systems with identical first-order admissibility
marginals but opposite exact feasibility.
"""
from itertools import product

G = (0, 1, 0)  # one projection fiber
M = (0, 1)
F = ((0,), (0,), (1,))
T = ((0,), (1,), (0,))


def feasible(lists):
    for msg in product(M, repeat=3):
        if any(msg[w] not in lists[w] for w in range(3)):
            continue
        if all(G[u] == G[v] or msg[u] != msg[v]
               for u in range(3) for v in range(u + 1, 3)):
            return True
    return False


def signature(lists):
    row_degrees = tuple(sorted(len(L) for L in lists))
    col_degrees = tuple(sorted(sum(a in L for L in lists) for a in M))
    incidences = sum(row_degrees)
    ambiguity = len(set(G))
    return incidences, row_degrees, col_degrees, ambiguity


def main():
    assert signature(F) == signature(T) == (3, (1, 1, 1), (1, 2), 2)
    assert feasible(F) is False
    assert feasible(T) is True
    print({
        "status": "PASS",
        "shared_signature": signature(F),
        "F_feasible": feasible(F),
        "T_feasible": feasible(T),
        "conclusion": "first-order admissibility marginals are not capability-complete",
    })


if __name__ == "__main__":
    main()
