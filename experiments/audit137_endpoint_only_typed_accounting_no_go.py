"""Audit 137: endpoint-only typed accounting cannot bound exact continuation memory.

Witness family: L={0^n1^n}.  For finite horizon K, prefixes 0^0,...,0^K
are pairwise future-distinguishable: for i<j, continuation 1^i accepts 0^i
and rejects 0^j.  We deliberately hold endpoint deltas (R,I_external,A,L)
at zero.  This does NOT claim internal/persistent memory is free; rather it shows
that a bound omitting such memory cannot be universal.
"""
from __future__ import annotations

import json
import math
from pathlib import Path

KS = [1, 2, 4, 8, 16, 32, 64, 128, 256]


def in_language_0n1n(s: str) -> bool:
    n0 = 0
    while n0 < len(s) and s[n0] == "0":
        n0 += 1
    return s == ("0" * n0 + "1" * n0)


def audit_horizon(K: int) -> dict:
    pair_checks = 0
    failures = 0
    for i in range(K + 1):
        for j in range(i + 1, K + 1):
            z = "1" * i
            accepted_i = in_language_0n1n("0" * i + z)
            accepted_j = in_language_0n1n("0" * j + z)
            pair_checks += 1
            if not (accepted_i and not accepted_j):
                failures += 1
    return {
        "K": K,
        "continuation_classes_lower_bound": K + 1,
        "memory_bits_lower_bound": math.ceil(math.log2(K + 1)),
        "endpoint_delta_R": 0,
        "endpoint_delta_I_external": 0,
        "endpoint_delta_A": 0,
        "endpoint_delta_L": 0,
        "pair_checks": pair_checks,
        "failures": failures,
    }


def main() -> None:
    rows = [audit_horizon(K) for K in KS]
    result = {
        "audit": 137,
        "family": "L={0^n1^n}",
        "interpretation": (
            "I_external excludes continuation-sufficient persistent memory; "
            "if memory is charged inside I, the no-go becomes a memory lower bound instead."
        ),
        "rows": rows,
        "total_pair_checks": sum(r["pair_checks"] for r in rows),
        "total_failures": sum(r["failures"] for r in rows),
        "max_K": max(KS),
        "max_classes_lower_bound": max(KS) + 1,
        "max_memory_bits_lower_bound": math.ceil(math.log2(max(KS) + 1)),
        "status": {
            "endpoint_only_finite_bound": "FALSIFIED",
            "continuation_memory_lower_bound": "PROVED",
            "novelty": "IMPORTED/KNOWN",
        },
    }
    out = Path("results/audit137_endpoint_only_typed_accounting_no_go.json")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    assert result["total_failures"] == 0
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
