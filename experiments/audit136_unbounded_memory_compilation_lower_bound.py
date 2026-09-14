#!/usr/bin/env python3
"""GC-II Audit 136: exact finite-horizon witnesses for unbounded memory demand.

Language L = {0^n 1^n : n >= 0}. Prefixes 0^i are pairwise future-distinguishable:
for i < j, suffix 1^i accepts 0^i 1^i and rejects 0^j 1^i.
The script checks this directly for every horizon N <= MAX_N and freezes counts.
"""

import json
from pathlib import Path

MAX_N = 128
OUT = Path("results/audit136_unbounded_memory_compilation_lower_bound.json")


def in_language(word: str) -> bool:
    i = 0
    while i < len(word) and word[i] == "0":
        i += 1
    j = i
    while j < len(word) and word[j] == "1":
        j += 1
    return j == len(word) and i == len(word) - i


def run():
    horizon_rows = []
    total_pair_checks = 0
    total_failures = 0

    for nmax in range(1, MAX_N + 1):
        checks = 0
        failures = 0
        for i in range(nmax + 1):
            for j in range(i + 1, nmax + 1):
                suffix = "1" * i
                left = in_language("0" * i + suffix)
                right = in_language("0" * j + suffix)
                checks += 1
                if not (left and not right):
                    failures += 1
        total_pair_checks += checks
        total_failures += failures
        horizon_rows.append(
            {
                "max_prefix_index": nmax,
                "pairwise_distinguishable_prefixes": nmax + 1,
                "required_exact_states_lower_bound": nmax + 1,
                "pair_checks": checks,
                "failures": failures,
            }
        )

    result = {
        "language": "{0^n 1^n : n >= 0}",
        "max_horizon_checked": MAX_N,
        "horizons_checked": MAX_N,
        "total_pair_checks": total_pair_checks,
        "total_failures": total_failures,
        "largest_exact_state_lower_bound_checked": MAX_N + 1,
        "theorem_status": "PROVED analytically; finite regression PASS" if total_failures == 0 else "REGRESSION FAILURE",
        "rows": horizon_rows,
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({k: v for k, v in result.items() if k != "rows"}, indent=2))
    return result


if __name__ == "__main__":
    run()
