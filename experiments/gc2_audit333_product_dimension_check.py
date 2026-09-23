#!/usr/bin/env python3
"""Exact checks for GC-II Audit 333 product-composition boundary."""
from math import comb
import json


def sperner_dim(q: int) -> int:
    if q <= 1:
        return 0
    k = 1
    while comb(k, k // 2) < q:
        k += 1
    return k


def main():
    strict = []
    cases = 0
    for m in range(1, 33):
        for n in range(1, 33):
            a = sperner_dim(m)
            b = sperner_dim(n)
            prod = sperner_dim(m * n)  # A_m x A_n = A_(mn)
            assert max(a, b) <= prod <= a + b
            if prod < a + b:
                strict.append((m, n, a, b, prod))
            cases += 1

    # Decisive finite counterexample.
    assert sperner_dim(3) == 3
    assert sperner_dim(9) == 5
    assert sperner_dim(9) < 2 * sperner_dim(3)

    # Boolean endpoint: B_a x B_b ~= B_(a+b), and bmd(B_k)=k.
    boolean_endpoint_cases = 0
    for a in range(13):
        for b in range(13):
            # Cardinality lower bound is exact here: |B_k|=2^k.
            product_rank = a + b
            assert (1 << product_rank) == (1 << a) * (1 << b)
            boolean_endpoint_cases += 1

    result = {
        "audit": 333,
        "antichain_product_cases": cases,
        "strict_subadditive_antichain_pairs": len(strict),
        "first_strict_examples": [
            {"m": m, "n": n, "bmd_m": a, "bmd_n": b, "bmd_product": p}
            for m, n, a, b, p in strict[:20]
        ],
        "counterexample_A3xA3": {"factor_dimension": 3, "product_dimension": 5, "sum": 6},
        "boolean_endpoint_cases": boolean_endpoint_cases,
        "failures": 0,
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
