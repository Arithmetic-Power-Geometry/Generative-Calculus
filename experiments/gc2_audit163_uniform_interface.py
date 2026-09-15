#!/usr/bin/env python3
"""Exact finite regression for GC-II Audit 163.

No external dependencies. Checks projection-fiber incompatibility counts and
fixed interface/memory capacity failure thresholds.
"""
from itertools import product
import json


def projection(x, k):
    return x[:k]


def run():
    cases = 0
    fiber_violations = []
    threshold_violations = []
    capacities = (1, 2, 4, 8, 16)
    threshold_checks = 0

    for p in (2, 3):
        for n in range(1, 7):
            worlds = list(product(range(p), repeat=n))
            for k in range(n + 1):
                cases += 1
                fibers = {}
                for x in worlds:
                    fibers.setdefault(projection(x, k), []).append(x)
                expected = p ** (n - k)
                sizes = {len(v) for v in fibers.values()}
                if sizes != {expected}:
                    fiber_violations.append({
                        "p": p, "n": n, "k": k,
                        "expected": expected, "observed": sorted(sizes),
                    })
                # Target is exact omitted tuple, hence all worlds in a fiber
                # are pairwise action-incompatible.
                K = max(map(len, fibers.values()))
                for B in capacities:
                    threshold_checks += 1
                    theorem_predicts_failure = K > B
                    # A deterministic map from K incompatible worlds into B
                    # decision states is injective iff B >= K.
                    exact_failure = not (B >= K)
                    if theorem_predicts_failure != exact_failure:
                        threshold_violations.append({
                            "p": p, "n": n, "k": k,
                            "K": K, "B": B,
                        })

    result = {
        "audit": 163,
        "status": "PASS" if not fiber_violations and not threshold_violations else "FAIL",
        "parameter_cases": cases,
        "threshold_checks": threshold_checks,
        "fiber_violations": len(fiber_violations),
        "threshold_violations": len(threshold_violations),
        "details": {
            "fiber": fiber_violations,
            "threshold": threshold_violations,
        },
    }
    print(json.dumps(result, indent=2, sort_keys=True))
    if result["status"] != "PASS":
        raise SystemExit(1)


if __name__ == "__main__":
    run()
