#!/usr/bin/env python3
"""Exact exhaustive verification for GC-II Audit 338.

Exhausts every directed relation on q=1..4 labelled states and checks that
Boolean reachability support has saturated by horizon q-1.  Also checks the
exact support criterion by comparing Boolean powers with direct bounded BFS.
"""
import json
from pathlib import Path


def adjacency(mask, q):
    return [[bool((mask >> (i*q+j)) & 1) for j in range(q)] for i in range(q)]


def bool_product(a, b, q):
    out = [[False]*q for _ in range(q)]
    for i in range(q):
        for k in range(q):
            if a[i][k]:
                for j in range(q):
                    out[i][j] |= b[k][j]
    return out


def direct_bounded_reach(a, q, h):
    out = [[i == j for j in range(q)] for i in range(q)]
    for s in range(q):
        frontier = {s}
        for _ in range(h):
            frontier = {z for u in frontier for z in range(q) if a[u][z]}
            for z in frontier:
                out[s][z] = True
    return out


def power_union(a, q, h):
    out = [[i == j for j in range(q)] for i in range(q)]
    power = [row[:] for row in a]
    for _ in range(1, h+1):
        for i in range(q):
            for j in range(q):
                out[i][j] |= power[i][j]
        power = bool_product(power, a, q)
    return out


def main():
    relations = cases = failures = 0
    by_q = {}
    for q in range(1, 5):
        qrels = 1 << (q*q)
        qfail = 0
        for mask in range(qrels):
            a = adjacency(mask, q)
            horizon_max = q + 2
            supports = []
            for h in range(horizon_max + 1):
                p = power_union(a, q, h)
                d = direct_bounded_reach(a, q, h)
                cases += 1
                if p != d:
                    failures += 1
                    qfail += 1
                supports.append(sum(v for row in p for v in row))
            if any(supports[h] != supports[q-1] for h in range(q-1, horizon_max+1)):
                failures += 1
                qfail += 1
        relations += qrels
        by_q[str(q)] = {"relations": qrels, "failures": qfail}
    result = {
        "audit": 338,
        "q_exhaustive": [1,2,3,4],
        "relations_checked": relations,
        "horizon_cases_checked": cases,
        "failures": failures,
        "by_q": by_q,
    }
    out = Path("results/gc2_audit338_finite_saturation.json")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))
    if failures:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
