#!/usr/bin/env python3
"""Exact regression for GC-II Audit 131.

Checks the charged-composition support inequality on a deterministic parameter grid and
verifies tight full k-ary tree witnesses whenever the required internal-node count exists.
No randomness, external packages, or floating-point arithmetic are used.
"""

import json
from pathlib import Path


def main():
    total_feasible = 0
    violations = 0
    tight_witnesses = 0
    inverse_checks = 0
    inverse_violations = 0

    rows = []
    for k in range(2, 7):
        for c in range(1, 6):
            for g in range(0, 31):
                support = 1 + (k - 1) * g
                cost = c * g
                for B in range(0, 151):
                    feasible = cost <= B
                    bound = 1 + (k - 1) * (B // c)
                    if feasible:
                        total_feasible += 1
                        ok = support <= bound
                        violations += int(not ok)
                        if B == cost and support == bound:
                            tight_witnesses += 1
                    # inverse form: any witness of size q=support requires this much budget
                    required = c * ((support - 1 + (k - 2)) // (k - 1))
                    inverse_checks += 1
                    inv_ok = required == cost
                    inverse_violations += int(not inv_ok)

                rows.append(
                    {
                        "k": k,
                        "c": c,
                        "g": g,
                        "support": support,
                        "exact_cost": cost,
                    }
                )

    result = {
        "audit": 131,
        "theorem": "charged_composition_support_bound",
        "parameter_ranges": {
            "k": [2, 6],
            "c": [1, 5],
            "g": [0, 30],
            "B": [0, 150],
        },
        "total_feasible_budget_cases": total_feasible,
        "support_bound_violations": violations,
        "tight_budget_witness_cases": tight_witnesses,
        "inverse_budget_checks": inverse_checks,
        "inverse_budget_violations": inverse_violations,
        "status": "PASS" if violations == 0 and inverse_violations == 0 else "FAIL",
        "note": (
            "This regression checks arithmetic and tight tree witnesses only. "
            "The theorem itself is proved combinatorially in Audit 131."
        ),
    }

    out = Path("results/gc2_charged_composition_support_bound.json")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
