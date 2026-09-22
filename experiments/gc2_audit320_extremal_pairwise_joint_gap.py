#!/usr/bin/env python3
"""Exact verifier for GC-II Audit 320.

Computes the optimal worst-case decision-tree depth for the singleton-test
construction. Integer arithmetic only; no numerical tolerance.
"""
from functools import lru_cache
import csv
import sys


def optimal_depth_singletons(k: int) -> int:
    tests = tuple(1 << i for i in range(k))
    full = (1 << k) - 1

    @lru_cache(None)
    def V(cell: int) -> int:
        if cell == 0:
            raise ValueError("empty cell is unreachable")
        if cell & (cell - 1) == 0:
            return 0
        candidates = []
        for t in tests:
            yes = cell & t
            no = cell & ~t
            if yes and no:
                candidates.append(1 + max(V(yes), V(no)))
        if not candidates:
            raise RuntimeError("unresolved cell has no useful test")
        return min(candidates)

    return V(full)


def main(max_k: int = 16, out: str = "gc2_audit320_results.csv") -> None:
    rows = []
    for k in range(2, max_k + 1):
        v = optimal_depth_singletons(k)
        p = 1
        expected = k - 1
        assert v == expected, (k, v, expected)
        rows.append((k, p, v, v / p, expected))
    with open(out, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["K", "pairwise_P", "joint_V", "ratio_V_over_P", "theorem_K_minus_1"])
        w.writerows(rows)
    print(f"verified K=2..{max_k}; all V=K-1; wrote {out}")


if __name__ == "__main__":
    max_k = int(sys.argv[1]) if len(sys.argv) > 1 else 16
    out = sys.argv[2] if len(sys.argv) > 2 else "gc2_audit320_results.csv"
    main(max_k, out)
