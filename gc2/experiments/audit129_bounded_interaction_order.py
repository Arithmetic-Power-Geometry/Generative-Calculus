#!/usr/bin/env python3
"""Audit 129: exhaustive bounded-interaction-order certificate test.

Enumerates every family of nonempty subsets of [6] of size <=2, retains exactly
antichains, reconstructs the induced monotone response, and verifies that the
family is exactly the set of minimal successful interventions.
"""
from itertools import combinations
from math import comb
import json

M, K = 6, 2
CANDIDATES = [frozenset(c) for r in range(1, K + 1) for c in combinations(range(M), r)]
DOMAIN = [frozenset(c) for r in range(M + 1) for c in combinations(range(M), r)]


def is_antichain(fam):
    return all(not (a < b or b < a) for a, b in combinations(fam, 2))


def response(fam, s):
    return any(a <= s for a in fam)


def minimal_successes(fam):
    good = [s for s in DOMAIN if response(fam, s)]
    return set(s for s in good if not any(t < s and response(fam, t) for t in DOMAIN))


def main():
    antichains = failures = order_violations = 0
    max_certificate = 0
    size_distribution = {}
    n = len(CANDIDATES)
    for mask in range(1 << n):
        fam = [CANDIDATES[i] for i in range(n) if (mask >> i) & 1]
        if not is_antichain(fam):
            continue
        antichains += 1
        size_distribution[len(fam)] = size_distribution.get(len(fam), 0) + 1
        max_certificate = max(max_certificate, len(fam))
        recovered = minimal_successes(fam)
        if recovered != set(fam):
            failures += 1
        if any(len(a) > K for a in recovered):
            order_violations += 1

    result = {
        "audit": 129,
        "m": M,
        "k": K,
        "candidate_witnesses": n,
        "candidate_families_before_antichain_filter": 1 << n,
        "bounded_rank_antichains": antichains,
        "reconstruction_failures": failures,
        "interaction_order_violations": order_violations,
        "maximum_certificate_size": max_certificate,
        "binom_m_k": comb(M, K),
        "size_distribution": size_distribution,
        "status": "PASS" if failures == 0 and order_violations == 0 and max_certificate == comb(M, K) else "FAIL",
    }
    print(json.dumps(result, indent=2, sort_keys=True))
    assert result["status"] == "PASS"


if __name__ == "__main__":
    main()
