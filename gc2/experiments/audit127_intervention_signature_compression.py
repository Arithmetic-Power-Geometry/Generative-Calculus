#!/usr/bin/env python3
"""Exact finite kill test for GC-II Audit 127."""
from itertools import combinations, product
import json

M = 4
signatures = list(product((0, 1), repeat=M))
pairs = list(combinations(signatures, 2))
proper_subsets = [s for r in range(M) for s in combinations(range(M), r)]

subset_rows = []
false_complete = 0
total_collisions = 0
for subset in proper_subsets:
    collisions = 0
    for x, y in pairs:
        if all(x[i] == y[i] for i in subset):
            collisions += 1
    total_collisions += collisions
    if collisions == 0:
        false_complete += 1
    subset_rows.append({"subset": list(subset), "colliding_distinct_pairs": collisions})

result = {
    "m": M,
    "signatures": len(signatures),
    "distinct_unordered_pairs": len(pairs),
    "proper_coordinate_subsets": len(proper_subsets),
    "minimum_collisions_any_proper_subset": min(r["colliding_distinct_pairs"] for r in subset_rows),
    "total_subset_pair_collisions": total_collisions,
    "falsely_complete_proper_subsets": false_complete,
    "fixed_length_bits_required_by_counting": M,
    "status": "PASS" if false_complete == 0 else "FAIL",
    "subsets": subset_rows,
}
print(json.dumps(result, indent=2, sort_keys=True))
