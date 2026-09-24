#!/usr/bin/env python3
"""Exact verifier for GC-II Audit 357.

Checks the one-edge bridge family and, exhaustively for all directed graphs on
three labelled vertices, the exact one-edge exposure identity.
"""
from itertools import permutations
import json


def tc(vertices, edges):
    reach = set(edges)
    changed = True
    while changed:
        changed = False
        add = {(a, d) for (a, b) in reach for (c, d) in reach if b == c and a != d}
        add -= reach
        if add:
            reach |= add
            changed = True
    return {(a, b) for (a, b) in reach if a != b}


def bridge(p, q):
    L = [("L", i) for i in range(p)]
    R = [("R", j) for j in range(q)]
    V = L + R
    E0 = {(L[i], L[i + 1]) for i in range(p - 1)} | {(R[j], R[j + 1]) for j in range(q - 1)}
    e = (L[-1], R[0])
    before = tc(V, E0)
    after = tc(V, E0 | {e})
    novel = after - before
    assert len(novel) == p * q
    assert novel == {(x, y) for x in L for y in R}
    return {"p": p, "q": q, "omega": len(novel), "expected": p * q}


def exhaustive_three_vertex_identity():
    V = (0, 1, 2)
    possible = list(permutations(V, 2))
    systems = 0
    insertions = 0
    for mask in range(1 << len(possible)):
        E0 = {possible[i] for i in range(len(possible)) if mask & (1 << i)}
        before = tc(V, E0)
        systems += 1
        for e in possible:
            if e in E0:
                continue
            u, v = e
            pred = {u} | {x for x in V if (x, u) in before}
            succ = {v} | {y for y in V if (v, y) in before}
            predicted = {(x, y) for x in pred for y in succ if x != y} - before
            actual = tc(V, E0 | {e}) - before
            assert actual == predicted
            insertions += 1
    return {"labelled_graphs": systems, "edge_insertions_checked": insertions, "failures": 0}


if __name__ == "__main__":
    rows = [bridge(p, q) for p in range(1, 17) for q in range(1, 17)]
    out = {
        "audit": 357,
        "bridge_cases": len(rows),
        "max_verified_omega": max(r["omega"] for r in rows),
        "three_vertex_exhaustive": exhaustive_three_vertex_identity(),
        "failures": 0,
    }
    print(json.dumps(out, indent=2))
