"""Exact verifier for GC-II Audit 326.

No floating point is used.  For m layers, enumerate all 2^m policies,
construct (x, 2^m-1-x), and verify pairwise incomparability and the
positive-weighted-sum classification for representative integer weights.
"""
from itertools import combinations
import json


def dominates(u, v):
    return all(a <= b for a, b in zip(u, v)) and u != v


def audit(m):
    T = (1 << m) - 1
    pts = [(x, T - x) for x in range(1 << m)]
    distinct = len(set(pts)) == (1 << m)
    incomparable = all(
        not dominates(u, v) and not dominates(v, u)
        for u, v in combinations(pts, 2)
    )
    # Representative positive weights cover the three sign cases w1-w2.
    weighted = {}
    for w in [(2, 1), (1, 2), (1, 1)]:
        vals = [w[0] * x + w[1] * y for x, y in pts]
        best = min(vals)
        argmins = [i for i, z in enumerate(vals) if z == best]
        weighted[str(w)] = len(argmins)
    assert distinct and incomparable
    assert weighted['(2, 1)'] == 1
    assert weighted['(1, 2)'] == 1
    assert weighted['(1, 1)'] == (1 << m)
    return {
        'm': m,
        'policies': 1 << m,
        'pareto_frontier': 1 << m,
        'pairwise_incomparable': True,
        'weighted_sum_argmin_counts': weighted,
    }


if __name__ == '__main__':
    out = {
        'audit': 326,
        'model': 'two-resource layered deterministic closure escape',
        'cases': [audit(m) for m in range(1, 13)],
        'status': 'exact integer verification; theorem separately PROVED',
    }
    print(json.dumps(out, indent=2))
