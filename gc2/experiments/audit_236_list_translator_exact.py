#!/usr/bin/env python3
"""Exact finite verifier for GC-II Audit 236.

Exhaustively compares admissibility-constrained exact translator feasibility
against list-coloring feasibility for all binary p,g assignments on four worlds
and every nonempty list assignment over a two-message alphabet.
"""
from itertools import product

W = range(4)
M = (0, 1)
NONEMPTY_LISTS = ((0,), (1,), (0, 1))


def translator_feasible(p, g, lists):
    for msg in product(M, repeat=len(W)):
        if any(msg[w] not in lists[w] for w in W):
            continue
        decoder = {}
        ok = True
        for w in W:
            key = (p[w], msg[w])
            if key in decoder and decoder[key] != g[w]:
                ok = False
                break
            decoder[key] = g[w]
        if ok:
            return True
    return False


def list_coloring_feasible(p, g, lists):
    edges = [(u, v) for u in W for v in W if u < v and p[u] == p[v] and g[u] != g[v]]
    for c in product(M, repeat=len(W)):
        if any(c[w] not in lists[w] for w in W):
            continue
        if all(c[u] != c[v] for u, v in edges):
            return True
    return False


def ambiguity(p, g):
    return max(len({g[w] for w in W if p[w] == z}) for z in set(p))


def main():
    checked = 0
    same_A_opposite_feasibility = False
    for p in product((0, 1), repeat=len(W)):
        for g in product((0, 1), repeat=len(W)):
            A = ambiguity(p, g)
            seen = set()
            for lists in product(NONEMPTY_LISTS, repeat=len(W)):
                t = translator_feasible(p, g, lists)
                l = list_coloring_feasible(p, g, lists)
                assert t == l, (p, g, lists, t, l)
                seen.add(t)
                checked += 1
            if A == 2 and seen == {False, True}:
                same_A_opposite_feasibility = True
    assert same_A_opposite_feasibility
    print({"status": "PASS", "instances": checked,
           "theorem": "translator feasibility == list-coloring feasibility",
           "fiber_ambiguity_complete_under_lists": False})


if __name__ == "__main__":
    main()
