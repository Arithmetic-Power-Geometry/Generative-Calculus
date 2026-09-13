#!/usr/bin/env python3
"""Exact finite checker for GC-II Audit 126."""
from itertools import product
import json

mechanisms = list(product((0, 1), repeat=2))  # f[j]
ordered_pairs = 0
factual_equal = 0
intervention_separated = 0
full_equal = 0
criterion_mismatches = 0

for f in mechanisms:
    for g in mechanisms:
        ordered_pairs += 1
        factual = f[0] == g[0]
        signature_equal = f == g
        omega = max(abs(f[j] - g[j]) for j in (0, 1))
        if factual:
            factual_equal += 1
            if f[1] != g[1]:
                intervention_separated += 1
            else:
                full_equal += 1
        if (omega == 0) != signature_equal:
            criterion_mismatches += 1

result = {
    "mechanisms": len(mechanisms),
    "ordered_pairs": ordered_pairs,
    "factually_equivalent_pairs": factual_equal,
    "intervention_separated_among_factual_pairs": intervention_separated,
    "fully_interventionally_equivalent_among_factual_pairs": full_equal,
    "signature_criterion_mismatches": criterion_mismatches,
    "status": "PASS" if criterion_mismatches == 0 else "FAIL",
}
print(json.dumps(result, indent=2, sort_keys=True))
