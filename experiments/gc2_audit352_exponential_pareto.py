#!/usr/bin/env python3
"""Exact verifier for GC-II Audit 352.

Constructs the k-stage two-resource layered family and independently checks:
1. exactly 2^k distinct path-cost vectors;
2. every vector is Pareto minimal;
3. every vector has constant coordinate sum 2^k-1;
4. the direct construction equals the predicted frontier {(x,C-x): 0<=x<=C}.

No randomization is used.
"""
from itertools import product
import json


def dominates(p, q):
    """True iff p <= q componentwise and p != q."""
    return p != q and p[0] <= q[0] and p[1] <= q[1]


def path_vectors(k):
    out = []
    for bits in product((0, 1), repeat=k):
        r1 = 0
        r2 = 0
        for i, choose_a in enumerate(bits):
            w = 1 << i
            if choose_a:
                r1 += w
            else:
                r2 += w
        out.append((r1, r2))
    return out


def pareto_minimal(vectors):
    uniq = sorted(set(vectors))
    return [q for q in uniq if not any(dominates(p, q) for p in uniq)]


def verify(max_k=12):
    rows = []
    failures = 0
    for k in range(1, max_k + 1):
        vectors = path_vectors(k)
        frontier = pareto_minimal(vectors)
        C = (1 << k) - 1
        predicted = [(x, C - x) for x in range(C + 1)]
        checks = {
            "path_count": len(vectors) == (1 << k),
            "distinct_count": len(set(vectors)) == (1 << k),
            "constant_sum": all(a + b == C for a, b in vectors),
            "all_nondominated": len(frontier) == (1 << k),
            "predicted_frontier": frontier == predicted,
        }
        ok = all(checks.values())
        failures += 0 if ok else 1
        rows.append({
            "k": k,
            "vertices": k + 1,
            "operational_choices": 2 * k,
            "paths": 1 << k,
            "pareto_vectors": len(frontier),
            "constant_sum": C,
            "checks": checks,
            "ok": ok,
        })
    return {
        "audit": 352,
        "max_k": max_k,
        "families_checked": max_k,
        "largest_frontier": 1 << max_k,
        "failures": failures,
        "rows": rows,
    }


if __name__ == "__main__":
    print(json.dumps(verify(), indent=2))
