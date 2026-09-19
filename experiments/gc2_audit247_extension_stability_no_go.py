#!/usr/bin/env python3
"""Exact finite checks for GC-II Audit 247's extension-stability no-go."""
from heapq import heappush, heappop
from math import inf


def values(states, edges, goals):
    rev = {s: [] for s in states}
    for u, a, c, v in edges:
        assert c >= 0
        rev[v].append((u, c))
    d = {s: inf for s in states}
    q = []
    for g in goals:
        d[g] = 0
        heappush(q, (0, g))
    while q:
        du, u = heappop(q)
        if du != d[u]:
            continue
        for v, c in rev[u]:
            nd = du + c
            if nd < d[v]:
                d[v] = nd
                heappush(q, (nd, v))
    return d


def check_positive_family(limit=100):
    # For every v=1..limit, x and y initially have equal positive goal cost v.
    # A conservative zero-cost extension only at x separates their values.
    for v in range(1, limit + 1):
        states = {'x', 'y', 'G'}
        base = [('x', 'a', v, 'G'), ('y', 'b', v, 'G')]
        d = values(states, base, {'G'})
        assert d['x'] == d['y'] == v
        ext = base + [('x', 'q_x', 0, 'G')]
        dp = values(states, ext, {'G'})
        assert dp['x'] == 0 and dp['y'] == v


def check_infinite_case():
    states = {'x', 'y', 'G'}
    base = []
    d = values(states, base, {'G'})
    assert d['x'] == d['y'] == inf
    ext = [('x', 'q_x', 0, 'G')]
    dp = values(states, ext, {'G'})
    assert dp['x'] == 0 and dp['y'] == inf


def check_zero_boundary():
    states = {'x', 'y', 'G'}
    base = [('x', 'a', 0, 'G'), ('y', 'b', 0, 'G')]
    d = values(states, base, {'G'})
    ext = base + [('x', 'q_x', 0, 'G')]
    dp = values(states, ext, {'G'})
    assert d['x'] == d['y'] == dp['x'] == dp['y'] == 0


if __name__ == '__main__':
    check_positive_family()
    check_infinite_case()
    check_zero_boundary()
    print('positive_equal_value_cases_checked=100')
    print('infinite_gap_case=PASS')
    print('zero_gap_boundary=PASS_not_separated_by_nonnegative_scalar_value')
    print('status=PASS')
