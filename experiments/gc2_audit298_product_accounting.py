#!/usr/bin/env python3
"""Exact finite verifier for GC-II Audit 298.
No external packages. Exhaustively computes set-cover numbers by enumeration.
"""
from itertools import combinations, product


def cover_number(universe, sets):
    U = set(universe)
    if not U:
        return 0
    for k in range(1, len(sets) + 1):
        for idx in combinations(range(len(sets)), k):
            covered = set()
            for i in idx:
                covered |= set(sets[i])
            if U <= covered:
                return k
    return None


def product_instance(Y1, A1, Y2, A2):
    Y = {(x, y) for x in Y1 for y in Y2}
    A = [{(x, y) for x in s for y in t} for s in A1 for t in A2]
    return Y, A


def triangle_witness():
    Y = {0, 1, 2}
    A = [{0, 1}, {0, 2}, {1, 2}]
    N = cover_number(Y, A)
    Yp, Ap = product_instance(Y, A, Y, A)
    Np = cover_number(Yp, Ap)
    assert N == 2
    assert Np == 3
    assert Np < N * N
    return N, Np, len(Yp), len(Ap)


def exhaustive_small_sandwich():
    checked_pairs = 0
    strict = 0
    instances = []
    for n in (1, 2, 3):
        Y = set(range(n))
        nonempty_subsets = [set(c) for r in range(1, n + 1) for c in combinations(Y, r)]
        # every nonempty family of nonempty subsets; retain feasible instances only
        for mask in range(1, 1 << len(nonempty_subsets)):
            A = [nonempty_subsets[i] for i in range(len(nonempty_subsets)) if (mask >> i) & 1]
            N = cover_number(Y, A)
            if N is not None:
                instances.append((Y, A, N))

    # Full Cartesian pair audit is still small for n<=3.
    for Y1, A1, N1 in instances:
        for Y2, A2, N2 in instances:
            Yp, Ap = product_instance(Y1, A1, Y2, A2)
            Np = cover_number(Yp, Ap)
            assert Np is not None
            assert max(N1, N2) <= Np <= N1 * N2
            checked_pairs += 1
            if Np < N1 * N2:
                strict += 1
    return len(instances), checked_pairs, strict


if __name__ == "__main__":
    N, Np, targets, actions = triangle_witness()
    ni, pairs, strict = exhaustive_small_sandwich()
    print({
        "triangle_component_N": N,
        "triangle_product_N": Np,
        "triangle_product_targets": targets,
        "triangle_product_actions": actions,
        "feasible_component_instances": ni,
        "ordered_instance_pairs_checked": pairs,
        "strict_submultiplicative_pairs": strict,
        "status": "PASS",
    })
