"""GC-II Audit 133: exact finite check for universal monotone impossibility.

A nonconstant scalar cannot be guaranteed monotone if the free/admissible
transformation family is left unconstrained.  The two-state enumeration is a
regression witness for the general proof recorded in the audit note.
"""
from itertools import product
import json

X = (0, 1)
transformations = list(product(X, repeat=2))  # f represented by (f(0),f(1))
monotones = [m for m in product((0,1), repeat=2) if m[0] != m[1]]

rows = []
for m in monotones:
    increasing = []
    for f in transformations:
        witnesses = [x for x in X if m[f[x]] > m[x]]
        if witnesses:
            increasing.append({"map": list(f), "witness_states": witnesses})
    rows.append({"candidate_M": list(m), "increasing_free_map_candidates": increasing})

result = {
    "audit": 133,
    "states": 2,
    "deterministic_transformations_checked": len(transformations),
    "nonconstant_binary_scalar_candidates": len(monotones),
    "candidates_with_an_increasing_transformation": sum(bool(r["increasing_free_map_candidates"]) for r in rows),
    "universal_nonconstant_monotones_surviving": sum(not r["increasing_free_map_candidates"] for r in rows),
    "rows": rows,
}
assert result["universal_nonconstant_monotones_surviving"] == 0
print(json.dumps(result, indent=2, sort_keys=True))
