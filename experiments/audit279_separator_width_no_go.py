#!/usr/bin/env python3
"""Exact verifier for GC-II Audit 279.

Checks the serial exact-k counter construction and pairwise alpha-separation
of all accepted typed-cost vectors. Uses integer arithmetic with alpha=2,r=3.
"""
from itertools import combinations
from math import comb

ALPHA = 2
R = 3


def vectors(d):
    k = d // 2
    out = []
    for T in combinations(range(d), k):
        support = frozenset(T)
        y = tuple(R if i in support else 1 for i in range(d))
        out.append((support, y))
    return k, out


def accepted_by_serial_counter(bits, k):
    c = 0
    for bit in bits:
        assert bit in (0, 1)
        c += bit
    return c == k


def alpha_covers(s, y):
    return all(si <= ALPHA * yi for si, yi in zip(s, y))


def main():
    total_targets = 0
    ordered_distinct_pairs = 0
    for d in range(1, 13):
        k, ys = vectors(d)
        assert len(ys) == comb(d, k)
        for support, y in ys:
            bits = tuple(1 if i in support else 0 for i in range(d))
            assert accepted_by_serial_counter(bits, k)
            assert alpha_covers(y, y)
        for i, (_, s) in enumerate(ys):
            for j, (_, y) in enumerate(ys):
                if i == j:
                    continue
                ordered_distinct_pairs += 1
                assert not alpha_covers(s, y)
        total_targets += len(ys)

    assert total_targets == 1911
    assert ordered_distinct_pairs == 1151364
    print({
        "audit": 279,
        "status": "PASS",
        "alpha": ALPHA,
        "r": R,
        "dimensions": [1, 12],
        "targets_checked": total_targets,
        "ordered_distinct_pairs_checked": ordered_distinct_pairs,
        "arithmetic": "exact integer",
    })


if __name__ == "__main__":
    main()
