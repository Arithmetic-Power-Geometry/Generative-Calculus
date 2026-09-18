#!/usr/bin/env python3
"""Audit 227: depth-one unary alternatives induce arbitrary-order capability interaction.

System: start s, target t, and n parallel one-step transitions s->t. Transition i
is enabled iff augmentation i is present. Hence target reachability is OR_n.
The Mobius coefficient of every nonempty T is (-1)^(|T|+1), so interaction
degree is n although operational depth and primitive gate arity are both 1.
"""
from itertools import combinations


def subsets(n):
    base = tuple(range(n))
    for r in range(n + 1):
        for c in combinations(base, r):
            yield frozenset(c)


def mobius(values, T):
    items = tuple(T)
    total = 0
    for r in range(len(items) + 1):
        for c in combinations(items, r):
            U = frozenset(c)
            total += (-1) ** (len(T) - len(U)) * values[U]
    return total


def audit(n):
    ss = list(subsets(n))
    # n parallel unary-enabled edges from start directly to target.
    values = {S: int(bool(S)) for S in ss}
    coeff = {T: mobius(values, T) for T in ss}

    assert coeff[frozenset()] == 0
    for T in ss:
        if T:
            assert coeff[T] == (-1) ** (len(T) + 1)

    # Monotonicity and exact one-step reachability.
    for S in ss:
        assert values[S] == int(len(S) >= 1)
        for T in ss:
            if S <= T:
                assert values[S] <= values[T]

    degree = max((len(T) for T, x in coeff.items() if x), default=0)
    support = sum(x != 0 for x in coeff.values())
    assert degree == n
    assert support == 2**n - 1
    return len(ss), support, degree


def main():
    checked = 0
    for n in range(1, 13):
        count, support, degree = audit(n)
        checked += count
        print(f"n={n:2d} subsets={count:5d} mobius_support={support:5d} degree={degree}")
    print(f"PASS: exact audits n=1..12; augmentation subsets checked={checked}")
    print("PASS: depth=1 and unary primitive gates admit unbounded interaction degree")
    print("PASS: Mobius support is maximally dense on all nonempty subsets")


if __name__ == "__main__":
    main()
