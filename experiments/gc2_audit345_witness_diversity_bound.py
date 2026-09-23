#!/usr/bin/env python3
"""Exact checks for GC-II Audit 345.

Checks the sharp parallel-route family and the complementary serial-chain
family. Uses exact integer subset enumeration; no randomness or external deps.
"""
from itertools import combinations
import json


def mobius_top_from_minimal_witnesses(n, witnesses):
    """Top Möbius coefficient of monotone OR-of-witnesses function."""
    total = 0
    full = (1 << n) - 1
    for s in range(1 << n):
        g = any(all(s & (1 << e) for e in w) for w in witnesses)
        if g:
            total += (-1) ** (n - s.bit_count())
    return total


def parallel(m):
    witnesses = [{2*i, 2*i+1} for i in range(m)]
    n = 2*m
    lam = 2
    nu = m
    rho = len(set().union(*witnesses))
    top = mobius_top_from_minimal_witnesses(n, witnesses)
    return {"family":"parallel", "m":m, "lambda":lam, "nu":nu,
            "rho":rho, "lambda_times_nu":lam*nu,
            "top_order":n, "top_coefficient":top,
            "expected_top_coefficient":(-1)**(m+1),
            "pass": rho <= lam*nu and rho == lam*nu and top == (-1)**(m+1)}


def serial(k):
    witnesses = [set(range(k))]
    lam, nu, rho = k, 1, k
    top = mobius_top_from_minimal_witnesses(k, witnesses)
    return {"family":"serial", "k":k, "lambda":lam, "nu":nu,
            "rho":rho, "lambda_times_nu":lam*nu,
            "top_order":k, "top_coefficient":top,
            "expected_top_coefficient":1,
            "pass": rho <= lam*nu and rho == lam*nu and top == 1}


def main():
    # m<=8 entails at most 2^16 exact subsets, matching Audit 344's scale.
    rows = [parallel(m) for m in range(1,9)]
    rows += [serial(k) for k in range(1,17)]
    out = {"audit":345, "cases":len(rows),
           "failures":sum(not r["pass"] for r in rows), "rows":rows}
    print(json.dumps(out, indent=2))
    assert out["failures"] == 0

if __name__ == "__main__":
    main()
