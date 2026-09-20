"""Exact verifier for GC-II Audit 277.

Checks the fixed-factor middle-layer construction using integer arithmetic.
No floating-point tolerances are used.
"""
from itertools import combinations
from math import comb
from fractions import Fraction


def vector(d, support, r):
    support = set(support)
    return tuple(r if i in support else 1 for i in range(d))


def alpha_covers(s, y, alpha):
    return all(Fraction(si, yi) <= alpha for si, yi in zip(s, y))


def verify(max_d=12, alpha=Fraction(3, 2), r=2):
    assert Fraction(r, 1) > alpha >= 1
    families = 0
    ordered_pair_checks = 0
    private_target_checks = 0
    for d in range(1, max_d + 1):
        k = d // 2
        supports = list(combinations(range(d), k))
        Y = [vector(d, S, r) for S in supports]
        assert len(Y) == comb(d, k)
        families += 1

        # Every distinct representative fails to alpha-cover the target.
        for i, s in enumerate(Y):
            assert alpha_covers(s, s, alpha)
            private_target_checks += 1
            for j, y in enumerate(Y):
                if i == j:
                    continue
                ordered_pair_checks += 1
                assert not alpha_covers(s, y, alpha), (d, i, j, s, y)

    return {
        "status": "PASS",
        "max_dimension": max_d,
        "alpha": str(alpha),
        "r": r,
        "families": families,
        "private_target_checks": private_target_checks,
        "ordered_pair_checks": ordered_pair_checks,
    }


if __name__ == "__main__":
    print(verify())
