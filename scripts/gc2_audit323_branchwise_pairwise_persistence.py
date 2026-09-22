#!/usr/bin/env python3
"""Exact checks for GC-II Audit 323.

No floating point is used. The script verifies:
(1) the sharp singleton family V=(K-1)P;
(2) a non-hereditary but branchwise-persistent three-class example;
(3) the Audit-322 deadlock when branchwise persistence fails.
"""
from functools import lru_cache
from math import inf


def value(states, labels, tests_at):
    states = frozenset(states)

    @lru_cache(None)
    def V(C):
        C = frozenset(C)
        if len({labels[x] for x in C}) <= 1:
            return 0
        best = inf
        for name, cost, outcome in tests_at(C):
            children = {}
            for x in C:
                children.setdefault(outcome[x], set()).add(x)
            # Ignore non-progress self loops; they cannot improve nonnegative-cost optimum.
            if any(frozenset(ch) == C for ch in children.values()):
                continue
            worst = max(V(frozenset(ch)) for ch in children.values())
            best = min(best, cost + worst)
        return best

    return V(states)


def singleton_family(K, P):
    states = tuple(range(K))
    labels = {x: x for x in states}

    def tests_at(C):
        out = []
        for i in C:
            outcome = {x: int(x == i) for x in C}
            out.append((f"is_{i}", P, outcome))
        return out

    return value(states, labels, tests_at)


def nonhereditary_bpp_example():
    states = (0, 1, 2)
    labels = {x: x for x in states}

    def tests_at(C):
        C = frozenset(C)
        if C == frozenset(states):
            # Root catalogue disappears after the first observation.
            return [("root_is_0", 1, {0: 1, 1: 0, 2: 0})]
        if C == frozenset({1, 2}):
            # Fresh branch-only test: not hereditary from root.
            return [("branch_is_1", 1, {1: 1, 2: 0})]
        return []

    return value(states, labels, tests_at)


def audit322_deadlock():
    states = (0, 1, 2)
    labels = {x: x for x in states}

    def tests_at(C):
        C = frozenset(C)
        if C == frozenset(states):
            return [
                (f"is_{i}", 1, {x: int(x == i) for x in C})
                for i in states
            ]
        return []

    return value(states, labels, tests_at)


def main():
    rows = []
    for K in range(2, 10):
        for P in range(1, 8):
            got = singleton_family(K, P)
            expected = (K - 1) * P
            assert got == expected, (K, P, got, expected)
            rows.append((K, P, got))

    nh = nonhereditary_bpp_example()
    assert nh == 2, nh

    dead = audit322_deadlock()
    assert dead == inf, dead

    print("Audit 323 exact checks passed")
    print(f"tight singleton cases: {len(rows)}")
    print("non-hereditary branchwise-persistent example: V=2")
    print("Audit-322 nonpersistent example: V=infinity")


if __name__ == "__main__":
    main()
