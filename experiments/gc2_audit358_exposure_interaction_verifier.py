#!/usr/bin/env python3
"""Exact verifier for GC-II Audit 358.

Exhaustively checks the exposure-interaction normal form on all three-vertex
systems where every possible non-self edge is baseline, newly added, or absent.
"""
from itertools import permutations
import json


def tc(vertices, edges):
    reach = set(edges)
    while True:
        add = {
            (a, d)
            for (a, b) in reach
            for (c, d) in reach
            if b == c and a != d
        } - reach
        if not add:
            break
        reach |= add
    return {(a, b) for (a, b) in reach if a != b}


def exposure_prediction(vertices, baseline, additions):
    t0 = tc(vertices, baseline)
    new_edges = tuple(sorted(additions))
    m = len(new_edges)
    if m == 0:
        return set(), 0, set()

    # H: after new edge i, baseline dynamics can position the system at the
    # tail of new edge j. Identity positioning is included explicitly.
    h = {
        (i, j)
        for i, (_, vi) in enumerate(new_edges)
        for j, (uj, _) in enumerate(new_edges)
        if vi == uj or (vi, uj) in t0
    }
    hstar = tc(tuple(range(m)), h) | {(i, i) for i in range(m)}

    predicted = set()
    sum_bound = 0
    for i, j in hstar:
        ui = new_edges[i][0]
        vj = new_edges[j][1]
        pred = {ui} | {x for x in vertices if (x, ui) in t0}
        succ = {vj} | {y for y in vertices if (vj, y) in t0}
        rectangle = {(x, y) for x in pred for y in succ if x != y}
        predicted |= rectangle
        sum_bound += len(pred) * len(succ)

    return predicted - t0, sum_bound, hstar


def exhaustive_three_vertex():
    vertices = (0, 1, 2)
    possible = tuple(permutations(vertices, 2))
    systems = 0
    single_edge_cases = 0
    max_omega = 0

    # Ternary encoding: 0 absent, 1 baseline, 2 newly added.
    for code in range(3 ** len(possible)):
        z = code
        baseline = set()
        additions = set()
        for edge in possible:
            state = z % 3
            z //= 3
            if state == 1:
                baseline.add(edge)
            elif state == 2:
                additions.add(edge)

        t0 = tc(vertices, baseline)
        actual = tc(vertices, baseline | additions) - t0
        predicted, bound, _ = exposure_prediction(vertices, baseline, additions)
        assert actual == predicted
        assert len(actual) <= bound

        if len(additions) == 1:
            single_edge_cases += 1
            u, v = next(iter(additions))
            pred = {u} | {x for x in vertices if (x, u) in t0}
            succ = {v} | {y for y in vertices if (v, y) in t0}
            audit357 = {(x, y) for x in pred for y in succ if x != y} - t0
            assert actual == audit357

        max_omega = max(max_omega, len(actual))
        systems += 1

    return {
        "ternary_systems": systems,
        "expected_ternary_systems": 3 ** len(possible),
        "single_edge_reductions_checked": single_edge_cases,
        "max_omega": max_omega,
        "failures": 0,
    }


if __name__ == "__main__":
    out = {
        "audit": 358,
        "theorem": "exposure-interaction normal form",
        "three_vertex_exhaustive": exhaustive_three_vertex(),
        "failures": 0,
    }
    print(json.dumps(out, indent=2, sort_keys=True))
