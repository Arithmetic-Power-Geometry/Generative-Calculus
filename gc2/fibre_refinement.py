"""Exact finite shared-translator fibre-refinement audit.

Known combinatorial core: weighted hitting set.  The GC-II role is to make
R/I/A/L refinements explicit and test the boundary before stronger claims.
"""
from itertools import combinations


def conflict_pairs(observations, targets):
    """Pairs indistinguishable initially but requiring distinct outputs."""
    n = len(observations)
    if len(targets) != n:
        raise ValueError("observations and targets must have equal length")
    return frozenset((i, j) for i in range(n) for j in range(i + 1, n)
                     if observations[i] == observations[j] and targets[i] != targets[j])


def separated_pairs(feature):
    """Pairs distinguished by one candidate refinement feature."""
    return frozenset((i, j) for i in range(len(feature)) for j in range(i + 1, len(feature))
                     if feature[i] != feature[j])


def is_sufficient(observations, targets, features, chosen):
    conflicts = conflict_pairs(observations, targets)
    covered = set()
    for k in chosen:
        covered.update(separated_pairs(features[k]))
    return conflicts.issubset(covered)


def min_refinement(observations, targets, features, cost):
    """Brute-force exact minimum set-function cost sufficient for translation.

    cost is any callable on a frozenset of feature indices. It may be nonlinear.
    Returns (minimum_cost, one_minimizer). Raises ValueError if impossible.
    """
    m = len(features)
    n = len(observations)
    if any(len(f) != n for f in features):
        raise ValueError("every feature must have one value per trace")
    best = None
    best_set = None
    for r in range(m + 1):
        for comb in combinations(range(m), r):
            S = frozenset(comb)
            if is_sufficient(observations, targets, features, S):
                c = cost(S)
                if best is None or c < best:
                    best, best_set = c, S
    if best is None:
        raise ValueError("candidate refinements cannot separate all conflicts")
    return best, best_set
