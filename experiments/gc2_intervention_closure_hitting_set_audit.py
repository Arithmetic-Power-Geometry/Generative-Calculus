"""GC-II Audit 110: exact finite intervention-closure / hitting-set collision.

For a finite set U of unresolved operational distinctions, each admissible
intervention i resolves a fixed subset S_i of U. The minimum number of
interventions needed to make every distinction available is exactly minimum
set cover (equivalently hitting set after dualization).

This script exhaustively checks all nonempty intervention families over
universes of size 1..4. No randomness or external dependencies.
"""
from itertools import combinations


def min_intervention_closure(universe, interventions):
    """Direct exhaustive closure cost."""
    for k in range(len(interventions) + 1):
        for idxs in combinations(range(len(interventions)), k):
            resolved = set()
            for i in idxs:
                resolved |= interventions[i]
            if resolved >= universe:
                return k
    return None


def min_set_cover(universe, sets):
    """Independent exhaustive minimum-set-cover formulation."""
    best = None
    n = len(sets)
    for mask in range(1 << n):
        k = mask.bit_count()
        if best is not None and k >= best:
            continue
        covered = set()
        for i, s in enumerate(sets):
            if (mask >> i) & 1:
                covered.update(s)
        if universe <= covered:
            best = k
    return best


def main():
    cases = 0
    solvable = 0
    violations = 0
    by_m = []
    for m in range(1, 5):
        universe = set(range(m))
        possible = [
            {j for j in range(m) if (mask >> j) & 1}
            for mask in range(1, 1 << m)
        ]
        local_cases = local_violations = 0
        for family_mask in range(1, 1 << len(possible)):
            family = [
                possible[i]
                for i in range(len(possible))
                if (family_mask >> i) & 1
            ]
            a = min_intervention_closure(universe, family)
            b = min_set_cover(universe, family)
            cases += 1
            local_cases += 1
            if a is not None:
                solvable += 1
            if a != b:
                violations += 1
                local_violations += 1
        by_m.append((m, local_cases, local_violations))

    print("AUDIT_110_INTERVENTION_CLOSURE_HITTING_SET")
    print(f"cases={cases}")
    print(f"solvable={solvable}")
    print(f"violations={violations}")
    for m, n, v in by_m:
        print(f"universe={m}, families={n}, violations={v}")
    assert cases == 32902
    assert solvable == 32412
    assert violations == 0


if __name__ == "__main__":
    main()
