#!/usr/bin/env python3
"""Exact exhaustive check for GC-II Audit 313.

Enumerates all complete directed 3-state primitive graphs with edge costs in
{0,1,2,3}; computes exact integer APSP distances; verifies that zero triangle
circulation of A=d-d^T is equivalent to potential representability.
"""
from itertools import product

N = 3
EDGES = [(i, j) for i in range(N) for j in range(N) if i != j]


def apsp(weights):
    d = [[0 if i == j else weights[(i, j)] for j in range(N)] for i in range(N)]
    for k in range(N):
        for i in range(N):
            for j in range(N):
                d[i][j] = min(d[i][j], d[i][k] + d[k][j])
    return d


def audit_one(values):
    weights = dict(zip(EDGES, values))
    d = apsp(weights)
    A = [[d[i][j] - d[j][i] for j in range(N)] for i in range(N)]
    circulation = A[0][1] + A[1][2] + A[2][0]
    h = [A[0][v] for v in range(N)]
    potential_exact = all(
        A[i][j] == h[j] - h[i]
        for i in range(N) for j in range(N)
    )
    return circulation == 0, potential_exact


def main():
    checked = 0
    for values in product(range(4), repeat=len(EDGES)):
        zero_circ, exact = audit_one(values)
        assert zero_circ == exact, values
        checked += 1
    print({"assignments_checked": checked, "failures": 0})


if __name__ == "__main__":
    main()
