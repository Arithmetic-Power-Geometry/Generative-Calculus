#!/usr/bin/env python3
"""Audit 342: verify exact Möbius interaction accounting on finite reachability systems."""
from itertools import combinations


def closure(n, rel):
    r = set(rel) | {(i, i) for i in range(n)}
    for k in range(n):
        for i in range(n):
            if (i, k) in r:
                for j in range(n):
                    if (k, j) in r:
                        r.add((i, j))
    return r


def novelty(n, baseline, edges):
    return len(closure(n, baseline | set(edges)) - baseline)


def mobius(n, baseline, edges, subset):
    subset = tuple(subset)
    total = 0
    for r in range(len(subset) + 1):
        for t in combinations(subset, r):
            total += (-1) ** (len(subset) - r) * novelty(n, baseline, t)
    return total


def verify_decomposition(n, baseline, edges):
    lhs = novelty(n, baseline, edges)
    rhs = 0
    for r in range(1, len(edges) + 1):
        for s in combinations(edges, r):
            rhs += mobius(n, baseline, edges, s)
    assert lhs == rhs, (n, baseline, edges, lhs, rhs)


def main():
    # Exhaust all reflexive-transitive baselines on 3 labelled states and
    # every subset of up to 3 absent grounded edges.
    cases = 0
    signed = set()
    n = 3
    universe = [(i, j) for i in range(n) for j in range(n)]
    seen = set()
    for mask in range(1 << (n * n)):
        raw = {universe[p] for p in range(n * n) if (mask >> p) & 1}
        b = frozenset(closure(n, raw))
        if b in seen:
            continue
        seen.add(b)
        absent = [e for e in universe if e not in b]
        for m in range(0, min(3, len(absent)) + 1):
            for es in combinations(absent, m):
                verify_decomposition(n, set(b), es)
                cases += 1
                if m >= 2:
                    signed.add((m, mobius(n, set(b), es, es)))

    # Explicit sign witnesses.
    ident = {(i, i) for i in range(3)}
    assert mobius(3, ident, [(0, 1), (1, 2)], [(0, 1), (1, 2)]) == 1
    bneg = closure(3, ident | {(0, 1)})
    assert mobius(3, bneg, [(0, 2), (1, 2)], [(0, 2), (1, 2)]) == -1

    # Arbitrarily high-order witness family checked through k=8.
    for k in range(2, 9):
        n2 = k + 1
        b = {(i, i) for i in range(n2)}
        es = [(i - 1, i) for i in range(1, k + 1)]
        # Endpoint 0->k is absent for every proper subset and present for all edges.
        for r in range(k):
            for s in combinations(es, r):
                assert (0, k) not in closure(n2, b | set(s))
        assert (0, k) in closure(n2, b | set(es))

    print({"status": "PASS", "three_state_cases": cases,
           "distinct_preorders": len(seen), "high_order_checked_through": 8,
           "observed_interaction_signs": sorted({-1 if v < 0 else 0 if v == 0 else 1 for _, v in signed})})


if __name__ == "__main__":
    main()
