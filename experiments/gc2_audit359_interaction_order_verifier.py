#!/usr/bin/env python3
"""Exact verifier for GC-II Audit 359.

Exhaustively checks minimum generated-operation order on all three-vertex
systems where every possible non-self edge is baseline, generated, or absent.
"""
from collections import deque
from itertools import permutations
import json

INF = 10**9


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


def zero_one_dist(vertices, baseline, additions, source):
    adj = {v: [] for v in vertices}
    for u, v in baseline:
        adj[u].append((v, 0))
    for u, v in additions:
        adj[u].append((v, 1))
    dist = {v: INF for v in vertices}
    dist[source] = 0
    dq = deque([source])
    while dq:
        u = dq.popleft()
        du = dist[u]
        for v, w in adj[u]:
            nd = du + w
            if nd < dist[v]:
                dist[v] = nd
                if w == 0:
                    dq.appendleft(v)
                else:
                    dq.append(v)
    return dist


def h_distances(m, h):
    adj = {i: [] for i in range(m)}
    for i, j in h:
        adj[i].append(j)
    all_dist = {}
    for s in range(m):
        dist = {i: INF for i in range(m)}
        dist[s] = 0
        q = deque([s])
        while q:
            u = q.popleft()
            for v in adj[u]:
                if dist[v] == INF:
                    dist[v] = dist[u] + 1
                    q.append(v)
        all_dist[s] = dist
    return all_dist


def formula_orders(vertices, baseline, additions):
    t0 = tc(vertices, baseline)
    new_edges = tuple(sorted(additions))
    m = len(new_edges)
    if m == 0:
        return {}, t0

    pred = []
    succ = []
    for u, v in new_edges:
        pred.append({u} | {x for x in vertices if (x, u) in t0})
        succ.append({v} | {y for y in vertices if (v, y) in t0})

    h = {
        (i, j)
        for i, (_, vi) in enumerate(new_edges)
        for j, (uj, _) in enumerate(new_edges)
        if vi == uj or (vi, uj) in t0
    }
    hd = h_distances(m, h)

    out = {}
    for x in vertices:
        for y in vertices:
            if x == y or (x, y) in t0:
                continue
            best = INF
            for i in range(m):
                if x not in pred[i]:
                    continue
                for j in range(m):
                    if y in succ[j] and hd[i][j] < INF:
                        best = min(best, 1 + hd[i][j])
            if best < INF:
                out[(x, y)] = best
    return out, t0


def exhaustive_three_vertex():
    vertices = (0, 1, 2)
    possible = tuple(permutations(vertices, 2))
    systems = 0
    pair_checks = 0
    positive_layers_seen = set()
    max_order = 0

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

        formula, t0 = formula_orders(vertices, baseline, additions)
        direct = {}
        for x in vertices:
            dist = zero_one_dist(vertices, baseline, additions, x)
            for y in vertices:
                if x == y:
                    continue
                pair_checks += 1
                if (x, y) in t0:
                    assert dist[y] == 0
                    continue
                if dist[y] < INF:
                    direct[(x, y)] = dist[y]
                    assert 1 <= dist[y] <= len(additions)
                    positive_layers_seen.add(dist[y])
                    max_order = max(max_order, dist[y])

        assert direct == formula

        # Disjoint layer decomposition and total novelty.
        layers = {}
        for pair, k in formula.items():
            layers.setdefault(k, set()).add(pair)
        union = set().union(*layers.values()) if layers else set()
        assert len(union) == sum(len(s) for s in layers.values())
        actual_novel = tc(vertices, baseline | additions) - t0
        assert union == actual_novel
        systems += 1

    return {
        "ternary_systems": systems,
        "expected_ternary_systems": 3 ** len(possible),
        "ordered_pair_checks": pair_checks,
        "positive_layers_seen": sorted(positive_layers_seen),
        "max_order_seen": max_order,
        "failures": 0,
    }


if __name__ == "__main__":
    out = {
        "audit": 359,
        "theorem": "minimum generated-operation interaction-order formula",
        "three_vertex_exhaustive": exhaustive_three_vertex(),
        "failures": 0,
    }
    print(json.dumps(out, indent=2, sort_keys=True))
