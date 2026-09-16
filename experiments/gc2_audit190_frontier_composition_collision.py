"""GC-II Audit 190: exact finite test of closure-conditioned Pareto frontier composition.

Purpose: test whether a putative generative law g -> F_g gains novelty merely from
sequential composition.  In the independent/additive case, feasible cost sets compose
by Minkowski sum and Pareto filtering; this is ordinary Pareto-sum geometry.

The script also exhibits strict failure under compatibility constraints, showing that
no equality law survives without carrying joint/interface structure.
"""
from itertools import product


def dominates(a, b):
    return all(x <= y for x, y in zip(a, b)) and any(x < y for x, y in zip(a, b))


def pareto(points):
    pts = sorted(set(points))
    return tuple(p for p in pts if not any(dominates(q, p) for q in pts if q != p))


def minkowski(A, B):
    return tuple(tuple(x + y for x, y in zip(a, b)) for a, b in product(A, B))


def compatible_sum(A, B, compatible):
    return tuple(tuple(x + y for x, y in zip(a, b))
                 for i, a in enumerate(A) for j, b in enumerate(B)
                 if compatible(i, j))


# Independent additive composition: exact Pareto-sum identity.
A = ((1, 4), (2, 2), (4, 1))
B = ((0, 3), (2, 1), (3, 0))
full = minkowski(A, B)
assert pareto(full) == pareto(minkowski(pareto(A), pareto(B)))

# Compatibility-constrained composition: same marginal frontiers, different global frontier.
# System X allows only aligned witness pairs; System Y only crossed pairs.
C = ((0, 2), (2, 0))
D = ((0, 2), (2, 0))
FX = pareto(compatible_sum(C, D, lambda i, j: i == j))
FY = pareto(compatible_sum(C, D, lambda i, j: i != j))
assert pareto(C) == ((0, 2), (2, 0))
assert pareto(D) == ((0, 2), (2, 0))
assert FX == ((0, 4), (4, 0))
assert FY == ((2, 2),)
assert FX != FY

print({"status": "PASS", "independent_frontier": pareto(full),
       "compatible_X": FX, "compatible_Y": FY})
