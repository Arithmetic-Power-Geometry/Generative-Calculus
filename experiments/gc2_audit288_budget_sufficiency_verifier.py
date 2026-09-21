"""Exact verifier for GC-II Audit 288.

Checks that the complete coordinatewise budget-query family separates every
pair of distinct attainable typed vectors, and that Audit 287's additive
scalar collapses the independent-deposition family.
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


def leq(y, q):
    return all(a <= b for a, b in zip(y, q))


def separating_member_budget(y, yp):
    """Return q in {y,yp} that distinguishes y and yp."""
    if not leq(yp, y):
        q = y
    else:
        assert y != yp and not leq(y, yp)
        q = yp
    assert leq(y, q) != leq(yp, q)
    return q


def verify():
    r = 3
    total_targets = 0
    pair_checks = 0
    scalar_checks = 0
    product_checks = 0

    for m in range(1, 11):
        Y = family(m, r)
        assert len(Y) == 2 ** m
        assert len(set(Y)) == len(Y)
        total_targets += len(Y)

        # Audit 287 scalarization has exactly one image value.
        image = {sum(y) for y in Y}
        assert image == {m * (r + 1)}
        scalar_checks += len(Y)

        # Full typed-budget family separates every distinct pair.
        for i, y in enumerate(Y):
            for yp in Y[i + 1:]:
                q = separating_member_budget(y, yp)
                assert leq(y, q) != leq(yp, q)
                pair_checks += 1

        # Cartesian composition: exact typed-state lower bound multiplies.
        if m > 1:
            prev = family(m - 1, r)
            assert len(Y) == 2 * len(prev)
            product_checks += 1

    print({
        "status": "PASS",
        "r": r,
        "max_modules": 10,
        "max_dimension": 20,
        "targets_checked": total_targets,
        "distinct_pair_budget_separation_checks": pair_checks,
        "collapsed_sum_scalar_checks": scalar_checks,
        "cartesian_composition_checks": product_checks,
        "max_exact_budget_sufficient_states_required": 2 ** 10,
        "max_fixed_length_bits_required": 10,
        "audit287_sum_scalar_states": 1,
        "arithmetic": "integer / exact",
    })


if __name__ == "__main__":
    verify()
