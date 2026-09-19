#!/usr/bin/env python3
"""Exact verifier for GC-II Audit 261.

Builds the unary-visible-effect construction and computes exact shortest
regeneration costs by Dijkstra. No external dependencies.
"""
from heapq import heappush, heappop
from math import inf


def build(m, K, finite=True):
    U = (1 << m) - 1
    start = ("s", 0, 0)
    states = {start}
    edges = []

    # Proper-task branches: branch i can accumulate U\{i} only.
    for i in range(m):
        missing = 1 << i
        atoms = [j for j in range(m) if j != i]
        prev = (f"b{i}", 0, 0)
        states.add(prev)
        edges.append((start, prev, 0))  # control-only branch choice
        mask = 0
        for step, j in enumerate(atoms, 1):
            mask2 = mask | (1 << j)
            nxt = (f"b{i}", step, mask2)
            states.add(nxt)
            edges.append((prev, nxt, 0))
            assert (mask ^ mask2).bit_count() == 1
            prev, mask = nxt, mask2
        assert mask == U ^ missing

    if finite:
        prev = ("g", 0, 0)
        states.add(prev)
        edges.append((start, prev, K))  # costed control-only gate
        mask = 0
        for step, j in enumerate(range(m), 1):
            mask2 = mask | (1 << j)
            nxt = ("g", step, mask2)
            states.add(nxt)
            edges.append((prev, nxt, 0))
            assert (mask ^ mask2).bit_count() == 1
            prev, mask = nxt, mask2
        assert mask == U

    # Verify every transition changes <=1 visible atom.
    for u, v, c in edges:
        assert c >= 0
        assert (u[2] ^ v[2]).bit_count() <= 1
    return start, states, edges


def profile(m, K, finite=True):
    start, states, edges = build(m, K, finite)
    adj = {s: [] for s in states}
    for u, v, c in edges:
        adj[u].append((v, c))
    dist = {s: inf for s in states}
    dist[start] = 0
    pq = [(0, start)]
    while pq:
        d, u = heappop(pq)
        if d != dist[u]:
            continue
        for v, c in adj[u]:
            nd = d + c
            if nd < dist[v]:
                dist[v] = nd
                heappush(pq, (nd, v))
    out = {}
    for T in range(1 << m):
        out[T] = min((d for s, d in dist.items() if (s[2] & T) == T), default=inf)
    return out


def run():
    checks = 0
    finite_cases = 0
    unreachable_cases = 0
    for m in range(2, 8):
        U = (1 << m) - 1
        for K in range(0, 51):
            p = profile(m, K, True)
            for T in range(U):
                assert p[T] == 0
                checks += 1
            assert p[U] == K
            checks += 1
            finite_cases += 1

            q = profile(m, K, False)
            for T in range(U):
                assert q[T] == 0
                checks += 1
            assert q[U] == inf
            checks += 1
            unreachable_cases += 1

            # Requirement monotonicity.
            for A in range(1 << m):
                for B in range(1 << m):
                    if A & ~B == 0:
                        assert p[A] <= p[B]
                        checks += 1

    print({
        "m_values": list(range(2, 8)),
        "K_values": [0, 50],
        "finite_cases": finite_cases,
        "unreachable_cases": unreachable_cases,
        "exact_assertion_checks": checks,
        "unary_visible_effect_no_go": "PROVED",
        "status": "PASS",
    })


if __name__ == "__main__":
    run()
