#!/usr/bin/env python3
"""GC-II Audit 138: exact memory + side-information distinguishability bound.

For N exact continuation classes, S persistent controller states, and Q possible
fresh side-information transcripts, an exact encoding into (state, transcript)
pairs exists iff N <= S*Q. This finite exhaustive regression checks the criterion
for N,S,Q in 1..64 and records tight cases. The theorem itself is counting, not
established by this experiment.
"""

import json
import math
from pathlib import Path

MAX_N = 64
MAX_S = 64
MAX_Q = 64


def exact_pair_encoding_exists(n: int, s: int, q: int) -> bool:
    """Constructive existence test: N labels inject into S x Q iff capacity suffices."""
    if min(n, s, q) < 1:
        raise ValueError("n, s, q must be positive")
    if n > s * q:
        return False
    # Explicit canonical injection c -> (c // q, c % q).
    pairs = [(c // q, c % q) for c in range(n)]
    return len(set(pairs)) == n and all(0 <= a < s and 0 <= b < q for a, b in pairs)


def main() -> None:
    total = feasible = infeasible = violations = tight = 0
    max_log_error = 0.0
    tight_examples = []

    for n in range(1, MAX_N + 1):
        for s in range(1, MAX_S + 1):
            for q in range(1, MAX_Q + 1):
                total += 1
                predicted = n <= s * q
                actual = exact_pair_encoding_exists(n, s, q)
                feasible += int(predicted)
                infeasible += int(not predicted)
                violations += int(predicted != actual)

                if predicted:
                    # Equivalent logarithmic capability-accounting form.
                    lhs = math.log2(n)
                    rhs = math.log2(s) + math.log2(q)
                    max_log_error = max(max_log_error, max(0.0, lhs - rhs))

                if n == s * q:
                    tight += 1
                    if len(tight_examples) < 12:
                        tight_examples.append({"N": n, "S": s, "Q": q})

    result = {
        "audit": 138,
        "claim_checked": "Exact N-class discrimination via S persistent states and Q side-information transcripts exists iff N <= S*Q.",
        "ranges": {"N": [1, MAX_N], "S": [1, MAX_S], "Q": [1, MAX_Q]},
        "total_parameter_triples": total,
        "feasible_triples": feasible,
        "infeasible_triples": infeasible,
        "criterion_violations": violations,
        "tight_triples": tight,
        "max_log_form_violation_bits": max_log_error,
        "tight_examples": tight_examples,
        "status": "PASS" if violations == 0 and max_log_error <= 1e-12 else "FAIL",
        "interpretation": [
            "The exact finite counting frontier is multiplicative: N <= S*Q.",
            "In bits: log2 N <= log2 S + log2 Q.",
            "Tight encodings show no universally positive extra nonlinear interaction penalty can be required without additional structure.",
            "This is a counting/coding result and is not claimed as novel GC mathematics."
        ]
    }

    out = Path("results") / "audit138_memory_sideinfo_capacity_bound.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
