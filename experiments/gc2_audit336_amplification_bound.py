#!/usr/bin/env python3
"""Exact verifier for GC-II Audit 336.

Exhausts every directed macro-transition relation on q=3 labelled states
(2^(3*3)=512 relations) and horizons h=0..4.  Checks

    Omega_pair^(h) <= q * min(q-1, sum_{l=1}^h beta^l)

with identity-only baseline.  Self-loops, cycles, nondeterminism, zero
branching, and saturated reachability are all included.
"""

import json
from pathlib import Path


def reachable_novel_pairs(adj, q, h):
    pairs = set()
    for start in range(q):
        frontier = {start}
        for _depth in range(1, h + 1):
            frontier = {
                v
                for u in frontier
                for v in range(q)
                if (u, v) in adj
            }
            pairs.update((start, v) for v in frontier if v != start)
    return pairs


def geometric_sum(beta, h):
    return sum(beta ** ell for ell in range(1, h + 1))


def main():
    q = 3
    horizons = range(0, 5)
    edges = [(i, j) for i in range(q) for j in range(q)]
    checked = 0
    failures = []
    equality_cases = 0

    for mask in range(1 << len(edges)):
        adj = {edge for k, edge in enumerate(edges) if (mask >> k) & 1}
        beta = max(sum((i, j) in adj for j in range(q)) for i in range(q))
        for h in horizons:
            omega = len(reachable_novel_pairs(adj, q, h))
            bound = q * min(q - 1, geometric_sum(beta, h))
            checked += 1
            if omega == bound:
                equality_cases += 1
            if omega > bound:
                failures.append({
                    "mask": mask,
                    "h": h,
                    "beta": beta,
                    "omega": omega,
                    "bound": bound,
                })

    # Audit-335 successor family: exact novelty and Audit-336 bound.
    successor_checks = []
    for n in range(1, 65):
        qn = n + 1
        beta = 1
        h = n
        exact = n * (n + 1) // 2
        bound = qn * min(qn - 1, geometric_sum(beta, h))
        assert exact <= bound
        successor_checks.append({"n": n, "exact": exact, "bound": bound})

    result = {
        "audit": 336,
        "q_exhaustive": q,
        "relations": 1 << len(edges),
        "horizons": list(horizons),
        "cases_checked": checked,
        "failures": len(failures),
        "equality_cases": equality_cases,
        "successor_family_n_max": 64,
        "successor_family_failures": 0,
    }
    print(json.dumps(result, indent=2, sort_keys=True))
    if failures:
        raise AssertionError(failures[:5])

    out = Path("results/gc2_audit336_amplification_bound.json")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
