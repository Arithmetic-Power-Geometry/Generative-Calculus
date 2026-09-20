#!/usr/bin/env python3
"""Exact verifier for GC-II Audit 274.

Checks the Boolean middle-layer family, its antichain property, exact
cardinality, and the private-budget witness property showing irredundancy.
No floating-point arithmetic is used.
"""

from itertools import product
from math import comb


def leq(x, y):
    return all(a <= b for a, b in zip(x, y))


def middle_layer(d):
    k = d // 2
    return [x for x in product((0, 1), repeat=d) if sum(x) == k]


def verify_dimension(d):
    A = middle_layer(d)
    expected = comb(d, d // 2)
    assert len(A) == expected

    # Pairwise incomparability.
    pair_checks = 0
    for i, x in enumerate(A):
        for j, y in enumerate(A):
            if i == j:
                continue
            pair_checks += 1
            assert not leq(x, y)

    # At budget q=a, exactly one frontier generator is feasible: a itself.
    private_checks = 0
    for a in A:
        feasible = [x for x in A if leq(x, a)]
        private_checks += len(A)
        assert feasible == [a]

    return len(A), pair_checks, private_checks


def main():
    total_vectors = 0
    total_pair_checks = 0
    total_private_checks = 0
    rows = []
    for d in range(1, 13):
        m, pairs, private = verify_dimension(d)
        total_vectors += m
        total_pair_checks += pairs
        total_private_checks += private
        rows.append((d, m))

    print("Audit 274 exact verifier: PASS")
    print("middle-layer sizes:", rows)
    print("vectors checked:", total_vectors)
    print("ordered incomparability checks:", total_pair_checks)
    print("private-budget feasibility checks:", total_private_checks)


if __name__ == "__main__":
    main()
