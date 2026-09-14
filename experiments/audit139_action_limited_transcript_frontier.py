#!/usr/bin/env python3
"""GC-II Audit 139: action-limited transcript capacity frontier.

Exact finite regression for the theorem candidate
    N <= S * Q * b**A
where N is the number of exact continuation/capability classes, S persistent
memory states, Q fresh side-information transcripts, A adaptive actions/queries,
and each action has at most b possible outcomes.

The script checks the equivalent logarithmic inequality and boundary cases on a
finite parameter grid. It does not claim novelty; the mechanism is decision-tree
/query-complexity counting.
"""
import json
import math
from pathlib import Path

result = {
    "audit": 139,
    "status": "PROVED_BOUNDARY_IMPORTED_KNOWN",
    "claim": "Exact identification requires N <= S*Q*b^A; equivalently log2 N <= log2 S + log2 Q + A log2 b.",
    "ranges": {"S": [1, 16], "Q": [1, 16], "b": [1, 8], "A": [0, 6]},
    "checks": 0,
    "feasible": 0,
    "infeasible": 0,
    "tight": 0,
    "violations": 0,
    "max_capacity": 0,
}

for S in range(1, 17):
    for Q in range(1, 17):
        for b in range(1, 9):
            for A in range(0, 7):
                cap = S * Q * (b ** A)
                result["max_capacity"] = max(result["max_capacity"], cap)
                # Probe the exact threshold plus nearby/degenerate values.
                for N in sorted({1, max(1, cap - 1), cap, cap + 1}):
                    result["checks"] += 1
                    product_ok = N <= cap
                    log_ok = math.log2(N) <= (
                        math.log2(S) + math.log2(Q) + A * math.log2(b) + 1e-12
                    )
                    if product_ok:
                        result["feasible"] += 1
                    else:
                        result["infeasible"] += 1
                    if N == cap:
                        result["tight"] += 1
                    if product_ok != log_ok:
                        result["violations"] += 1

assert result["violations"] == 0
out = Path("results/gc2_audit139_action_limited_frontier.json")
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
