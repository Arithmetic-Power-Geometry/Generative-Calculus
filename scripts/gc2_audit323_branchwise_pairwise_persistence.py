#!/usr/bin/env python3
"""Exact checks for GC-II Audit 323 (branchwise class separation).

No floating point is used. Checks:
(1) sharp singleton family V=(K-1)P;
(2) non-hereditary but branchwise class-separating example;
(3) Audit-322 deadlock when persistence fails;
(4) representative-world separation need not reduce decision-class count.
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
        return [(f"is_{i}", P, {x: int(x == i) for x in C}) for i in C]
    return value(states, labels, tests_at)


def nonhereditary_bcsp_example():
    states = (0, 1, 2)
    labels = {x: x for x in states}
    def tests_at(C):
        C = frozenset(C)
        if C == frozenset(states):
            return [("root_is_0", 1, {0: 1, 1: 0, 2: 0})]
        if C == frozenset({1, 2}):
            return [("branch_is_1", 1, {1: 1, 2: 0})]
        return []
    return value(states, labels, tests_at)


def audit322_deadlock():
    states = (0, 1, 2)
    labels = {x: x for x in states}
    def tests_at(C):
        C = frozenset(C)
        if C == frozenset(states):
            return [(f"is_{i}", 1, {x: int(x == i) for x in C}) for i in states]
        return []
    return value(states, labels, tests_at)


def representative_pair_counterexample():
    # Two decision classes, each with two worlds. The test separates a0 from b0,
    # but each outcome still contains both decision classes.
    states = ("a0", "a1", "b0", "b1")
    labels = {"a0": "A", "a1": "A", "b0": "B", "b1": "B"}
    z = {"a0": 0, "a1": 1, "b0": 1, "b1": 0}
    assert z["a0"] != z["b0"]
    children = [{x for x in states if z[x] == y} for y in (0, 1)]
    class_counts = [len({labels[x] for x in ch}) for ch in children]
    assert class_counts == [2, 2]
    return class_counts


def main():
    rows = []
    for K in range(2, 10):
        for P in range(1, 8):
            got = singleton_family(K, P)
            expected = (K - 1) * P
            assert got == expected, (K, P, got, expected)
            rows.append((K, P, got))

    nh = nonhereditary_bcsp_example()
    assert nh == 2, nh
    dead = audit322_deadlock()
    assert dead == inf, dead
    counts = representative_pair_counterexample()

    print("Audit 323 exact checks passed")
    print(f"tight singleton cases: {len(rows)}")
    print("non-hereditary BCSP example: V=2")
    print("Audit-322 nonpersistent example: V=infinity")
    print(f"representative-pair counterexample child class counts: {counts}")


if __name__ == "__main__":
    main()
