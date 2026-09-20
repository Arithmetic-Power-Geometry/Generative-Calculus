"""Exact verifier for GC-II Audit 286.

Checks that arbitrary synthetic centers cannot conservatively alpha-cover two
members of the independent-deposition family when r > alpha.
Integer arithmetic only.
"""
from itertools import product


def family(m, r):
    out = []
    for bits in product((0, 1), repeat=m):
        y = []
        for b in bits:
            y.extend((r, 1) if b else (1, r))
        out.append(tuple(y))
    return out


def conservative_common_center_exists(y, yp, alpha):
    """A common arbitrary center exists iff coordinate intervals intersect."""
    for a, b in zip(y, yp):
        lower = max(a, b)
        upper = min(alpha * a, alpha * b)
        if lower > upper:
            return False
    return True


def verify():
    alpha = 2
    r = 3
    targets = 0
    pair_checks = 0
    self_checks = 0
    boundary_checks = 0

    for m in range(1, 11):
        Y = family(m, r)
        assert len(Y) == 2 ** m
        targets += len(Y)

        for i, y in enumerate(Y):
            assert conservative_common_center_exists(y, y, alpha)
            self_checks += 1
            for j in range(i + 1, len(Y)):
                assert not conservative_common_center_exists(y, Y[j], alpha)
                pair_checks += 1

        # Sharp boundary for this family: at r=alpha a shared local center
        # (r,r) exists for either orientation, and the global all-r center
        # covers every target.
        Y_boundary = family(m, alpha)
        z = (alpha,) * (2 * m)
        for y in Y_boundary:
            assert all(a <= c <= alpha * a for a, c in zip(y, z))
            boundary_checks += 1

    print({
        "status": "PASS",
        "alpha": alpha,
        "r": r,
        "max_modules": 10,
        "max_dimension": 20,
        "targets_checked": targets,
        "self_cover_checks": self_checks,
        "distinct_pair_incompatibility_checks": pair_checks,
        "sharp_boundary_cover_checks": boundary_checks,
        "max_required_centers": 2 ** 10,
        "arithmetic": "integer / exact",
    })


if __name__ == "__main__":
    verify()
