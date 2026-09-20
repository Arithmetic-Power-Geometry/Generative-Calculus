#!/usr/bin/env python3
"""Exact verifier for GC-II Audit 280.

Checks the paired-choice family at alpha=2, r=3.  No floating point is used.
"""
from itertools import product

ALPHA = 2
R = 3
MAX_M = 10

def family(m):
    out = []
    for bits in product((0, 1), repeat=m):
        v = []
        for b in bits:
            v.extend((R, 1) if b == 0 else (1, R))
        out.append(tuple(v))
    return out

def covers(s, y):
    return all(si <= ALPHA * yi for si, yi in zip(s, y))

def main():
    targets = 0
    ordered_distinct_pairs = 0
    for m in range(1, MAX_M + 1):
        ys = family(m)
        assert len(ys) == 2 ** m
        assert len(set(ys)) == len(ys)
        assert all(min(y) == 1 and max(y) == R for y in ys)
        for i, s in enumerate(ys):
            assert covers(s, s)
            targets += 1
            for j, y in enumerate(ys):
                if i == j:
                    continue
                ordered_distinct_pairs += 1
                assert not covers(s, y), (m, i, j, s, y)
    print({
        "audit": 280,
        "status": "PASS",
        "alpha": ALPHA,
        "r": R,
        "pairs_min": 1,
        "pairs_max": MAX_M,
        "dimension_max": 2 * MAX_M,
        "targets_checked": targets,
        "ordered_distinct_pairs_checked": ordered_distinct_pairs,
        "arithmetic": "exact integer",
    })

if __name__ == "__main__":
    main()
