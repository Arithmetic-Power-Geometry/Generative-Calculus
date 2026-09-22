"""Exact verifier for GC-II Audit 319.

Verifies the hypercube family in Theorem 319.2 using an exact subset Bellman
recurrence for deterministic unit-cost coordinate tests. No floating point.
"""
from functools import lru_cache


def solve(m: int) -> tuple[int, int]:
    states = tuple(range(1 << m))
    tests = tuple(range(m))

    def outcome(x: int, j: int) -> int:
        return (x >> j) & 1

    # Distinct state = distinct decision label.
    pairwise = 0
    for x in states:
        for y in states:
            if x >= y:
                continue
            sep = [1 for j in tests if outcome(x, j) != outcome(y, j)]
            if not sep:
                raise AssertionError("distinct states were not separable")
            pairwise = max(pairwise, min(sep))

    @lru_cache(None)
    def V(B: tuple[int, ...]) -> int:
        if len(B) <= 1:
            return 0
        best = None
        for j in tests:
            b0 = tuple(x for x in B if outcome(x, j) == 0)
            b1 = tuple(x for x in B if outcome(x, j) == 1)
            if not b0 or not b1:  # non-useful test
                continue
            val = 1 + max(V(b0), V(b1))
            best = val if best is None else min(best, val)
        if best is None:
            raise AssertionError("unresolved inseparable belief set")
        return best

    return pairwise, V(states)


def main() -> None:
    rows = []
    for m in range(1, 9):
        P, joint = solve(m)
        expected = m
        assert P == 1
        assert joint == expected
        rows.append((m, 1 << m, P, joint, joint / P))

    print("m,N,pairwise_lower_bound,joint_resolution_cost,ratio")
    for row in rows:
        print(",".join(map(str, row)))


if __name__ == "__main__":
    main()
