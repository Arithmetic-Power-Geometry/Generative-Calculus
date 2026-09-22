#!/usr/bin/env python3
"""Exact integer checks for GC-II Audit 327.

Verifies S <= A <= q*S on exhaustive small nonnegative vector families,
plus the sharp coordinate-concentrated construction.
"""
from itertools import product
import json


def accounts(vectors, weights):
    d = len(weights)
    R = tuple(max(v[j] for v in vectors) for j in range(d))
    A = sum(weights[j] * R[j] for j in range(d))
    S = max(sum(weights[j] * v[j] for j in range(d)) for v in vectors)
    q = sum(w > 0 for w in weights)
    return S, A, q


def exhaustive(d, outcomes, vmax, wmax):
    all_vecs = list(product(range(vmax + 1), repeat=d))
    failures = 0
    cases = 0
    for weights in product(range(wmax + 1), repeat=d):
        for fam in product(all_vecs, repeat=outcomes):
            S, A, q = accounts(fam, weights)
            cases += 1
            if not (S <= A and (q == 0 and A == S == 0 or q > 0 and A <= q * S)):
                failures += 1
                raise AssertionError((weights, fam, S, A, q))
    return cases, failures


def sharpness(max_d=8):
    out = []
    for d in range(1, max_d + 1):
        weights = (1,) * d
        fam = []
        for j in range(d):
            v = [0] * d
            v[j] = 7
            fam.append(tuple(v))
        S, A, q = accounts(fam, weights)
        assert S == 7 and A == 7 * d and q == d
        out.append({"d": d, "S": S, "A": A, "ratio": d})
    return out


if __name__ == "__main__":
    # 3^6 vector-family assignments * 2^3 weight assignments = 5832 cases.
    cases, failures = exhaustive(d=3, outcomes=2, vmax=2, wmax=1)
    result = {
        "audit": 327,
        "exhaustive_model": {"dimensions": 3, "outcomes": 2, "coordinate_values": [0,1,2], "weight_values": [0,1]},
        "cases_checked": cases,
        "failures": failures,
        "sharpness": sharpness(8),
        "arithmetic": "exact integers only",
        "status": "NUMERICALLY SUPPORTED; theorem separately PROVED in docs/gc2_audit327_scalarization_adversary_noncommutativity.md"
    }
    print(json.dumps(result, indent=2))
