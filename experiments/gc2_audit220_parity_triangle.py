#!/usr/bin/env python3
"""Exact verifier for GC-II Audit 220 parity-triangle obstruction."""
from itertools import product

D = (0, 1)
R = {
    ("x", "y"): {(0, 0), (1, 1)},
    ("y", "z"): {(0, 0), (1, 1)},
    ("x", "z"): {(0, 1), (1, 0)},
}


def projection(ctx, rel, overlap):
    idx = [ctx.index(v) for v in overlap]
    return {tuple(t[i] for i in idx) for t in rel}


def pairwise_overlap_consistent():
    contexts = list(R)
    for i, a in enumerate(contexts):
        for b in contexts[i + 1:]:
            overlap = tuple(v for v in a if v in b)
            if projection(a, R[a], overlap) != projection(b, R[b], overlap):
                return False
    return True


def satisfies(assignment, active_contexts):
    return all(tuple(assignment[v] for v in ctx) in R[ctx] for ctx in active_contexts)


assert pairwise_overlap_consistent()
all_assignments = [dict(zip(("x", "y", "z"), bits)) for bits in product(D, repeat=3)]
full = list(R)
witnesses = [a for a in all_assignments if satisfies(a, full)]
assert witnesses == []

# Constraint-deletion minimality for this explicit witness.
for removed in full:
    active = [ctx for ctx in full if ctx != removed]
    ws = [a for a in all_assignments if satisfies(a, active)]
    assert ws, f"removing {removed} should restore feasibility"

print("pairwise_overlap_consistent=True")
print("global_witness_count=0")
print("constraint_deletion_minimal=True")
print("assignments_checked=8")
