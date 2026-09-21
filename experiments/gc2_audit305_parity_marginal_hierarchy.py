"""Exact verifier for GC-II Audit 305.

Checks that uniform even- and odd-parity supports on d bits have identical
marginals on every proper coordinate subset while the fixed parity task
separates them exactly.
"""
from fractions import Fraction
from itertools import combinations, product


def support(d, parity):
    return tuple(x for x in product((0, 1), repeat=d) if sum(x) % 2 == parity)


def marginal(support_points, coords):
    out = {}
    n = len(support_points)
    for x in support_points:
        key = tuple(x[i] for i in coords)
        out[key] = out.get(key, Fraction(0)) + Fraction(1, n)
    return out


def parity_task_value(support_points):
    return max(int(sum(x) % 2 == 0) for x in support_points)


def parity_task_expectation(support_points):
    return sum(Fraction(int(sum(x) % 2 == 0), len(support_points)) for x in support_points)


records = []
for d in range(2, 8):
    even = support(d, 0)
    odd = support(d, 1)
    assert len(even) == len(odd) == 2 ** (d - 1)

    checked = 0
    for s in range(0, d):
        for coords in combinations(range(d), s):
            me = marginal(even, coords)
            mo = marginal(odd, coords)
            assert me == mo
            # Every proper marginal is exactly uniform.
            assert len(me) == 2 ** s
            assert set(me.values()) == {Fraction(1, 2 ** s)}
            checked += 1

    assert parity_task_value(even) == 1
    assert parity_task_value(odd) == 0
    assert parity_task_expectation(even) == 1
    assert parity_task_expectation(odd) == 0

    records.append({
        "d": d,
        "support_size_each": len(even),
        "proper_coordinate_subsets_checked": checked,
        "even_task_value": 1,
        "odd_task_value": 0,
    })

print({
    "status": "PASS",
    "dimensions": [r["d"] for r in records],
    "total_proper_coordinate_subsets_checked": sum(r["proper_coordinate_subsets_checked"] for r in records),
    "records": records,
})
