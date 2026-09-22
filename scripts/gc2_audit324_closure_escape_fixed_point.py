#!/usr/bin/env python3
"""Exact finite checks for GC-II Audit 324.

Checks least-fixed-point escape, greatest trap complement, and agreement with
an independent recursive winning predicate over exhaustive small deterministic
branch-relative systems. No floating point is used.
"""
from functools import lru_cache
from itertools import product


def terminal(C, labels):
    return len({labels[x] for x in C}) <= 1


def children(C, outcome):
    vals = sorted({outcome[x] for x in C})
    return tuple(frozenset(x for x in C if outcome[x] == y) for y in vals)


def fixed_point(states, labels, tests_at):
    cells = [frozenset(x for x in states if mask & (1 << i))
             for mask in range(1, 1 << len(states))
             for i in [0]]
    # rebuild correctly from mask
    cells = [frozenset(states[i] for i in range(len(states)) if mask & (1 << i))
             for mask in range(1, 1 << len(states))]
    W = {C for C in cells if terminal(C, labels)}
    rank = {C: 0 for C in W}
    t = 0
    while True:
        add = set()
        for C in cells:
            if C in W or terminal(C, labels):
                continue
            for _, outcome in tests_at(C):
                ch = children(C, outcome)
                if all(D != C and D in W for D in ch):
                    add.add(C)
                    break
        if not add:
            break
        t += 1
        for C in add:
            rank[C] = t
        W |= add
    return W, rank, set(cells) - W


def recursive_win(C, labels, tests_at):
    @lru_cache(None)
    def win(S):
        if terminal(S, labels):
            return True
        for _, outcome in tests_at(S):
            ch = children(S, outcome)
            if all(D != S and win(D) for D in ch):
                return True
        return False
    return win(frozenset(C))


def exhaustive_three_world_check():
    states = (0, 1, 2)
    labels = {x: x for x in states}
    cells = [frozenset(states[i] for i in range(3) if mask & (1 << i))
             for mask in range(1, 8)]
    unresolved = [C for C in cells if len(C) >= 2]

    # For each cell use two canonical binary tests: isolate min(C), isolate max(C).
    catalog = {}
    for C in unresolved:
        lo, hi = min(C), max(C)
        catalog[C] = [
            ("lo", {x: int(x == lo) for x in C}),
            ("hi", {x: int(x == hi) for x in C}),
        ]

    # Each cell independently chooses availability mask 0..3. This exhausts
    # 4^4 = 256 branch-relative admissibility patterns for the four unresolved cells.
    checked = 0
    for masks in product(range(4), repeat=len(unresolved)):
        avail = dict(zip(unresolved, masks))
        def tests_at(C):
            out = []
            for j, (name, z) in enumerate(catalog.get(C, [])):
                if avail.get(C, 0) & (1 << j):
                    out.append((name, z))
            return out
        W, rank, L = fixed_point(states, labels, tests_at)
        for C in cells:
            assert (C in W) == recursive_win(C, labels, tests_at)
        # Trap property: every action from losing unresolved C has a losing or self child.
        for C in L:
            assert not terminal(C, labels)
            for _, z in tests_at(C):
                ch = children(C, z)
                assert any(D == C or D in L for D in ch)
        checked += 1
    return checked


def bcsp_not_necessary_example():
    # Three decision classes, each represented in both children of the first test.
    # Thus the first action does not lower class count, but each branch is resolvable.
    states = ("a0", "a1", "b0", "b1", "c0", "c1")
    labels = {s: s[0] for s in states}
    root = frozenset(states)
    left = frozenset(("a0", "b0", "c0"))
    right = frozenset(("a1", "b1", "c1"))
    def tests_at(C):
        if C == root:
            return [("split_copy", {s: int(s.endswith("1")) for s in C})]
        if C in (left, right):
            ordered = sorted(C)
            return [("is_first", {s: int(s == ordered[0]) for s in C})]
        if len(C) == 2:
            first = sorted(C)[0]
            return [("finish", {s: int(s == first) for s in C})]
        return []
    W, rank, _ = fixed_point(states, labels, tests_at)
    assert root in W
    root_children = children(root, tests_at(root)[0][1])
    assert all(len({labels[x] for x in D}) == 3 for D in root_children)
    return rank[root]


if __name__ == "__main__":
    n = exhaustive_three_world_check()
    r = bcsp_not_necessary_example()
    print("Audit 324 exact checks passed")
    print("exhaustive branch-relative systems checked:", n)
    print("BCSP-not-necessary resolving example root escape rank:", r)
