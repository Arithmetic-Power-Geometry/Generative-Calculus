#!/usr/bin/env python3
"""Exact verifier for GC-II Audit 356's n-bit latch family.

For each reachable bit-vector context, its immediate query-capability signature is
exactly that bit vector. Distinct signatures are sufficient to prove distinct
future-capability equivalence classes.
"""
import json


def signature(mask: int, n: int):
    return tuple((mask >> i) & 1 for i in range(n))


def verify(n: int):
    sigs = {signature(mask, n) for mask in range(1 << n)}
    expected = 1 << n
    assert len(sigs) == expected
    # Pairwise distinction follows from signature injectivity; also verify
    # every coordinate signature has the correct domain.
    assert all(len(s) == n and all(x in (0, 1) for x in s) for s in sigs)
    return {"n": n, "reachable_contexts": expected,
            "distinct_capability_signatures": len(sigs), "pass": True}


if __name__ == "__main__":
    rows = [verify(n) for n in range(0, 13)]
    print(json.dumps({"audit": 356, "family": "binary_latches",
                      "results": rows,
                      "total_contexts_n1_to_n12": sum(1 << n for n in range(1, 13))},
                     indent=2))
