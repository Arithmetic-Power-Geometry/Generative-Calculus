#!/usr/bin/env python3
"""Exact finite verifier for GC-II Audit 246.

Verifies that equal fixed-target optimal capability cost need not imply
operational congruence and can be destroyed by conservative action extension.
"""
from heapq import heappush, heappop
from math import inf


def value(states, transitions, goals):
    rev = {s: [] for s in states}
    for s, action, cost, t in transitions:
        assert cost >= 0
        rev[t].append((s, cost, action))
    d = {s: inf for s in states}
    q = []
    for g in goals:
        d[g] = 0
        heappush(q, (0, g))
    while q:
        ds, s = heappop(q)
        if ds != d[s]:
            continue
        for pred, cost, _ in rev[s]:
            nd = ds + cost
            if nd < d[pred]:
                d[pred] = nd
                heappush(q, (nd, pred))
    return d


def enabled(transitions, s):
    return {(a, c) for u, a, c, _ in transitions if u == s}


def main():
    states = {'x', 'y', 'G'}
    goals = {'G'}
    base = [
        ('x', 'a', 1, 'G'),
        ('y', 'b', 1, 'G'),
    ]
    v = value(states, base, goals)
    assert v['x'] == v['y'] == 1
    assert enabled(base, 'x') != enabled(base, 'y')

    # Conservative extension: retain every old transition and add q only at x.
    ext = base + [('x', 'q', 0, 'G')]
    vp = value(states, ext, goals)
    assert vp['x'] == 0
    assert vp['y'] == 1

    print('base_value_x=1')
    print('base_value_y=1')
    print('enabled_signatures_equal=False')
    print('extended_value_x=0')
    print('extended_value_y=1')
    print('status=PASS: fixed-target value equivalence is not a dynamic congruence')


if __name__ == '__main__':
    main()
