#!/usr/bin/env python3
"""Exact verifier for GC-II Audit 325.

Finite deterministic cells, positive integer costs, branch-relative admissibility.
Checks equivalence between recursive minimax value and budgeted winning sets.
No external dependencies.
"""
from functools import lru_cache
from itertools import product

INF = 10**9


def children(cell, test):
    buckets = {}
    for x in cell:
        y = test[x]
        buckets.setdefault(y, set()).add(x)
    return tuple(frozenset(v) for v in buckets.values())


def value(root, labels, tests, admissible, costs):
    @lru_cache(None)
    def V(cell):
        cell = frozenset(cell)
        if len({labels[x] for x in cell}) <= 1:
            return 0
        best = INF
        for u in admissible.get(cell, ()):
            ch = children(cell, tests[u])
            # Positive costs plus strict child shrinkage avoid recursive cycles.
            if any(k == cell for k in ch):
                continue
            q = max(V(k) for k in ch)
            if q < INF:
                best = min(best, costs[(cell, u)] + q)
        return best
    return V(frozenset(root))


def win(root, budget, labels, tests, admissible, costs):
    @lru_cache(None)
    def W(cell, b):
        cell = frozenset(cell)
        if len({labels[x] for x in cell}) <= 1:
            return True
        for u in admissible.get(cell, ()):
            c = costs[(cell, u)]
            if c > b:
                continue
            ch = children(cell, tests[u])
            if any(k == cell for k in ch):
                continue
            if all(W(k, b-c) for k in ch):
                return True
        return False
    return W(frozenset(root), budget)


def exhaustive_three_world_check():
    worlds = (0, 1, 2)
    root = frozenset(worlds)
    labels = {x: x for x in worlds}
    # Three singleton tests.
    tests = {u: {x: int(x == u) for x in worlds} for u in worlds}
    cells = [frozenset(s) for mask in range(1, 8)
             for s in [[x for x in worlds if mask & (1 << x)]]]
    unresolved = [c for c in cells if len(c) >= 2]

    checked = 0
    # For each unresolved cell choose any subset of locally meaningful tests.
    # 2^(3*4)=4096 branch-relative admissibility tables.
    slots = [(c, u) for c in unresolved for u in worlds]
    for bits in product((0, 1), repeat=len(slots)):
        adm = {c: [] for c in unresolved}
        for bit, (c, u) in zip(bits, slots):
            if bit:
                adm[c].append(u)
        adm = {c: tuple(us) for c, us in adm.items()}
        costs = {(c, u): 1 + ((sum(c) + u) % 3)
                 for c in unresolved for u in adm[c]}
        v = value(root, labels, tests, adm, costs)
        max_b = 10
        for b in range(max_b + 1):
            w = win(root, b, labels, tests, adm, costs)
            assert w == (v <= b), (adm, v, b, w)
        checked += 1
    return checked


def tight_chain_check(max_k=8):
    rows = []
    for k in range(2, max_k + 1):
        worlds = tuple(range(k))
        root = frozenset(worlds)
        labels = {x: x for x in worlds}
        tests = {u: {x: int(x == u) for x in worlds} for u in worlds}
        # Singleton tests admissible at every unresolved cell, cost 1.
        cells = [frozenset(x for x in worlds if mask & (1 << x))
                 for mask in range(1, 1 << k)]
        unresolved = [c for c in cells if len(c) >= 2]
        adm = {c: tuple(worlds) for c in unresolved}
        costs = {(c, u): 1 for c in unresolved for u in worlds}
        v = value(root, labels, tests, adm, costs)
        assert v == k - 1, (k, v)
        rows.append((k, v))
    return rows


if __name__ == "__main__":
    n = exhaustive_three_world_check()
    rows = tight_chain_check()
    print(f"PASS: {n} branch-relative admissibility systems")
    print("tight singleton values:", rows)
