#!/usr/bin/env python3
"""Exact finite verifier for GC-II Audit 243.

Verifies the family in which one unit-cost INFORMATION refinement changes
Omega_add from n/2 to 0. Uses exhaustive message-label enumeration for each
projection fiber; no optimizer or floating point is used.
"""
from itertools import product
from math import inf


def omega_add(p, g, lists, messages=(0, 1)):
    total = 0
    for z in set(p):
        idx = [i for i, zz in enumerate(p) if zz == z]
        decisions = sorted({g[i] for i in idx})
        if len(decisions) > len(messages):
            return inf
        best = inf
        labels = decisions + [None]
        for values in product(labels, repeat=len(messages)):
            if any(d not in values for d in decisions):
                continue
            lab = dict(zip(messages, values))
            uncovered = 0
            for i in idx:
                if not any(a in lists[i] and lab[a] == g[i] for a in messages):
                    uncovered += 1
            best = min(best, uncovered)
        total += best
    return total


def family(n):
    assert n >= 2 and n % 2 == 0
    p0 = [0] * n
    p1 = list(range(n))
    g = [0] * (n // 2) + [1] * (n // 2)
    lists = [{0} for _ in range(n)]
    return omega_add(p0, g, lists), omega_add(p1, g, lists)


def edge_cases():
    # Decision-constant fiber is already feasible.
    assert omega_add([0]*4, [0]*4, [{0}]*4) == 0
    # Full message admissibility is already feasible despite ambiguity.
    assert omega_add([0]*4, [0,0,1,1], [{0,1} for _ in range(4)]) == 0
    # Minimal nontrivial case.
    assert family(2) == (1, 0)


def main():
    edge_cases()
    rows = []
    for n in range(2, 102, 2):
        before, after = family(n)
        assert before == n // 2
        assert after == 0
        efficiency = before - after  # operation cost is exactly 1
        assert efficiency == n // 2
        rows.append((n, before, after, efficiency))
    print("verified_instances=", len(rows))
    print("max_n=", rows[-1][0])
    print("max_verified_unit_cost_efficiency=", rows[-1][3])
    print("status=PASS")


if __name__ == "__main__":
    main()
