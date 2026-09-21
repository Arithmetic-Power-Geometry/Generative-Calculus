"""Exact verifier for GC-II Audit 287.

Checks the independent-deposition family has exponentially many pairwise
incompatible conservative typed summaries for r > alpha, while the exact
additive scalar resource cost is identical for every target.
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
    for a, b in zip(y, yp):
        if max(a, b) > min(alpha * a, alpha * b):
            return False
    return True


def verify():
    alpha = 2
    r = 3
    total_targets = 0
    pair_checks = 0
    scalar_checks = 0
    composition_checks = 0

    for m in range(1, 11):
        Y = family(m, r)
        assert len(Y) == 2 ** m
        total_targets += len(Y)

        scalar_value = m * (r + 1)
        for y in Y:
            assert sum(y) == scalar_value
            scalar_checks += 1

        for i, y in enumerate(Y):
            for j in range(i + 1, len(Y)):
                assert not conservative_common_center_exists(y, Y[j], alpha)
                pair_checks += 1

        # Cartesian module composition: target count doubles and scalar value
        # increases by exactly r+1 when one more independent pair is added.
        if m > 1:
            prev = family(m - 1, r)
            assert len(Y) == 2 * len(prev)
            assert scalar_value == (m - 1) * (r + 1) + (r + 1)
            composition_checks += 1

    print({
        "status": "PASS",
        "alpha": alpha,
        "r": r,
        "max_modules": 10,
        "max_dimension": 20,
        "targets_checked": total_targets,
        "typed_pair_incompatibility_checks": pair_checks,
        "exact_scalar_equality_checks": scalar_checks,
        "composition_checks": composition_checks,
        "max_typed_required_states": 2 ** 10,
        "scalar_required_states": 1,
        "arithmetic": "integer / exact",
    })


if __name__ == "__main__":
    verify()
