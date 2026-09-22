#!/usr/bin/env python3
"""Exact finite verifier for GC-II Audit 321.

Checks heterogeneous-cost instances by exhaustive DP and verifies
P <= V <= (K-1)P. Also checks scaled singleton families attain equality.
Integer arithmetic only.
"""
from functools import lru_cache
from itertools import combinations, product
import csv
import sys


def pairwise_P(k, tests):
    # tests: (mask, cost), binary deterministic test; mask is outcome 1.
    vals = []
    for i, j in combinations(range(k), 2):
        sep = [c for mask, c in tests if ((mask >> i) & 1) != ((mask >> j) & 1)]
        if not sep:
            return None
        vals.append(min(sep))
    return max(vals)


def optimal_V(k, tests):
    full = (1 << k) - 1

    @lru_cache(None)
    def V(cell):
        if cell & (cell - 1) == 0:
            return 0
        cand = []
        for mask, cost in tests:
            yes = cell & mask
            no = cell & (full ^ mask)
            if yes and no:
                cand.append(cost + max(V(yes), V(no)))
        return min(cand) if cand else None

    return V(full)


def singleton_tightness(max_k=9, max_cost=7):
    rows = []
    for k in range(2, max_k + 1):
        for p in range(1, max_cost + 1):
            tests = [(1 << i, p) for i in range(k)]
            P = pairwise_P(k, tests)
            V = optimal_V(k, tests)
            assert P == p
            assert V == (k - 1) * p
            rows.append(("singleton", k, p, P, V, (k - 1) * P))
    return rows


def exhaustive_small():
    # K=3. Include every nontrivial binary partition up to complement once:
    # singleton masks 001,010,100. Assign costs in {1,2,3,4} exhaustively.
    k = 3
    masks = [1, 2, 4]
    rows = []
    checked = 0
    for costs in product(range(1, 5), repeat=len(masks)):
        tests = list(zip(masks, costs))
        P = pairwise_P(k, tests)
        V = optimal_V(k, tests)
        assert P is not None and V is not None
        assert P <= V <= (k - 1) * P, (tests, P, V)
        checked += 1
        rows.append(("exhaustive_K3", k, ":".join(map(str, costs)), P, V, (k - 1) * P))
    return checked, rows


def main(out="gc2_audit321_results.csv"):
    rows = singleton_tightness()
    checked, rows2 = exhaustive_small()
    rows.extend(rows2)
    with open(out, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["family", "K", "cost_parameter", "pairwise_P", "joint_V", "upper_bound"])
        w.writerows(rows)
    print(f"verified {checked} exhaustive heterogeneous K=3 assignments")
    print("verified singleton tightness K=2..9, scale p=1..7")
    print(f"wrote {out}")


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "gc2_audit321_results.csv")
