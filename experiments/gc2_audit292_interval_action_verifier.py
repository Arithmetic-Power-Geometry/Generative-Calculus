"""Exact exhaustive verifier for GC-II Audit 292. No floating point."""
from itertools import combinations


def cover_number(n, intervals):
    if n == 0:
        return 0
    U = set(range(n))
    sets = [set(range(l, r + 1)) for l, r in intervals]
    for k in range(1, len(sets) + 1):
        for chosen in combinations(range(len(sets)), k):
            if set().union(*(sets[j] for j in chosen)) >= U:
                return k
    return None


def greedy_number(n, intervals):
    if n == 0:
        return 0
    i = 0
    used = 0
    while i < n:
        candidates = [(r, l) for l, r in intervals if l <= i <= r]
        if not candidates:
            return None
        r, _ = max(candidates)
        used += 1
        i = r + 1
    return used


def verify():
    checked = 0
    feasible = 0
    infeasible = 0
    # Exhaust every interval family for ordered universes n <= 4.
    # n=4 has 10 possible nonempty intervals and 2^10=1024 families.
    for n in range(0, 5):
        all_intervals = [(l, r) for l in range(n) for r in range(l, n)]
        for mask in range(1 << len(all_intervals)):
            family = [iv for j, iv in enumerate(all_intervals) if mask & (1 << j)]
            opt = cover_number(n, family)
            got = greedy_number(n, family)
            assert got == opt, (n, family, got, opt)
            checked += 1
            if opt is None:
                infeasible += 1
            else:
                feasible += 1

    # Explicit degeneracies: duplicates, nesting, singleton, universal, gaps.
    cases = [
        (4, [(0, 3)], 1),
        (4, [(0, 1), (0, 1), (2, 3)], 2),
        (4, [(0, 3), (1, 2), (2, 2)], 1),
        (4, [(0, 0), (1, 1), (2, 2), (3, 3)], 4),
        (4, [(0, 1), (3, 3)], None),
        (0, [], 0),
    ]
    for n, family, expected in cases:
        assert greedy_number(n, family) == expected
        assert cover_number(n, family) == expected

    print({
        "status": "PASS",
        "exhaustive_interval_families_n_le_4": checked,
        "feasible": feasible,
        "infeasible": infeasible,
        "explicit_degeneracy_cases": len(cases),
        "criterion": "common-order interval feasibility",
        "algorithm": "leftmost-uncovered / farthest-right greedy",
    })


if __name__ == "__main__":
    verify()
