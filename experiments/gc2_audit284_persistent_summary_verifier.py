"""Exact verifier for GC-II Audit 284.

Uses exponent coordinates.  The Audit-280 family has m independent modules;
each deposits either (g,0) or (0,g).  Radius rho<g corresponds to an
alpha smaller than the multiplicative separation.  Every distinct pair then
fails directed coverage in both directions, so every attainable representative
covers only itself and C_alpha=2**m.
"""
from itertools import product


def family(m, gap=2):
    out = []
    for bits in product((0, 1), repeat=m):
        z = []
        for b in bits:
            z.extend((gap, 0) if b else (0, gap))
        out.append(tuple(z))
    return out


def covers_exp(s, y, rho):
    return all(a - b <= rho for a, b in zip(s, y))


def ceil_log2(n):
    if n <= 1:
        return 0
    return (n - 1).bit_length()


def verify():
    pair_checks = 0
    target_checks = 0
    state_bound_checks = 0

    # gap=2, rho=1 gives exact integer-exponent separation.
    for m in range(1, 11):
        Y = family(m, gap=2)
        assert len(Y) == 2 ** m
        assert len(set(Y)) == len(Y)

        for i, y in enumerate(Y):
            target_checks += 1
            covering_centers = 0
            for j, s in enumerate(Y):
                if i != j:
                    pair_checks += 1
                    assert not covers_exp(s, y, rho=1)
                if covers_exp(s, y, rho=1):
                    covering_centers += 1
            assert covering_centers == 1

        # Since every attainable center covers exactly one target,
        # the minimum internal certificate is the whole family.
        C = len(Y)
        assert C == 2 ** m
        assert ceil_log2(C) == m

        # Any k<m fixed-length summary has fewer states than C.
        for k in range(m):
            assert 2 ** k < C
            state_bound_checks += 1
        assert 2 ** m == C
        state_bound_checks += 1

    # Tolerance monotonicity sanity check on the same family:
    # once rho reaches the gap, one center can cover every target.
    for m in range(1, 7):
        Y = family(m, gap=2)
        s = Y[0]
        assert all(covers_exp(s, y, rho=2) for y in Y)

    print({
        "status": "PASS",
        "max_modules": 10,
        "max_dimension": 20,
        "targets_checked": target_checks,
        "ordered_distinct_pair_checks": pair_checks,
        "state_bound_checks": state_bound_checks,
        "arithmetic": "integer exponent / exact",
    })


if __name__ == "__main__":
    verify()
