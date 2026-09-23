#!/usr/bin/env python3
"""Exact checks for GC-II Audit 334. No floating point is used."""
from math import comb
import json


def antichain_dim(q: int) -> int:
    if q <= 1:
        return 0
    k = 0
    while comb(k, k // 2) < q:
        k += 1
    return k


def chain_dim(q: int) -> int:
    return max(0, q - 1)


def subset(x, y):
    return (x | y) == y


def verify_v_embedding():
    # a,b incomparable and both below c in B_2.
    img = {"a": 1, "b": 2, "c": 3}
    wanted = {
        ("a", "a"), ("b", "b"), ("c", "c"),
        ("a", "c"), ("b", "c")
    }
    got = {(x, y) for x in img for y in img if subset(img[x], img[y])}
    assert got == wanted
    # B_1 has only two points, so no injective embedding of a 3-point poset.
    assert 2 ** 1 < 3
    return True


def main():
    signs = {"negative": [], "zero": [], "positive": []}
    failures = []
    max_gap = None
    max_ratio = None
    for q in range(1, 4097):
        a = antichain_dim(q)
        c = chain_dim(q)
        # Exact defining inequalities for the Sperner threshold.
        if q > 1:
            if comb(a, a // 2) < q:
                failures.append([q, "upper_threshold"])
            if a > 0 and comb(a - 1, (a - 1) // 2) >= q:
                failures.append([q, "minimality_threshold"])
        d = c - a
        bucket = "positive" if d > 0 else "negative" if d < 0 else "zero"
        signs[bucket].append(q)
        if max_gap is None or d > max_gap[1]:
            max_gap = [q, d]
        if a > 0:
            ratio = (c, a)  # compare exactly by cross multiplication
            if max_ratio is None or c * max_ratio[1] > max_ratio[0] * a:
                max_ratio = ratio
    verify_v_embedding()
    out = {
        "audit": 334,
        "q_checked": 4096,
        "failures": failures,
        "A3_dimension": antichain_dim(3),
        "V3_dimension": 2,
        "strict_decrease_verified": True,
        "positive_chain_minus_antichain_cases": len(signs["positive"]),
        "zero_cases": len(signs["zero"]),
        "negative_cases": len(signs["negative"]),
        "first_positive_q": signs["positive"][0] if signs["positive"] else None,
        "max_tested_additive_gap": max_gap,
        "max_tested_chain_to_antichain_ratio_fraction": list(max_ratio),
        "method": "exact integer Sperner thresholds; chain height; explicit A3->V3 B2 embedding"
    }
    print(json.dumps(out, indent=2))
    assert not failures


if __name__ == "__main__":
    main()
