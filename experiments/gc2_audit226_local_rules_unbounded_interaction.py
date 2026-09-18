#!/usr/bin/env python3
"""Audit 226: unary local gates can induce arbitrary-order capability interaction."""
from itertools import combinations


def subsets(n):
    base = tuple(range(n))
    for r in range(n + 1):
        for c in combinations(base, r):
            yield frozenset(c)


def reachable_target(n, enabled):
    # States 0..n; transition i -> i+1 requires augmentation i.
    state = 0
    while state < n and state in enabled:
        state += 1
    return int(state == n)


def mobius(n, values, T):
    total = 0
    items = tuple(T)
    for r in range(len(items) + 1):
        for c in combinations(items, r):
            U = frozenset(c)
            total += (-1) ** (len(T) - len(U)) * values[U]
    return total


def audit(n):
    ss = list(subsets(n))
    values = {S: reachable_target(n, S) for S in ss}
    full = frozenset(range(n))

    # Exact reachability is the n-way conjunction.
    for S in ss:
        assert values[S] == int(S == full)

    coeff = {T: mobius(n, values, T) for T in ss}
    nonzero = {T: x for T, x in coeff.items() if x != 0}
    assert nonzero == {full: 1}

    # Monotonicity.
    for S in ss:
        for T in ss:
            if S <= T:
                assert values[S] <= values[T]

    return len(ss), len(nonzero), max((len(T) for T in nonzero), default=0)


def main():
    total_subsets = 0
    for n in range(1, 11):
        count, nz, degree = audit(n)
        total_subsets += count
        print(f"n={n:2d} subsets={count:4d} nonzero_mobius={nz} interaction_degree={degree}")
    print(f"PASS: exact audits n=1..10; augmentation subsets checked={total_subsets}")
    print("PASS: unary primitive gates admit unbounded global interaction order as n grows")


if __name__ == "__main__":
    main()
