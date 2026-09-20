"""Exact verifier for GC-II Audit 283.

Checks the multiplicative-cover/log-directed-cover equivalence without
floating point by representing positive costs as powers of a common integer
base b.  If y_i=b**e_i, then alpha=b**r and multiplicative coverage is exactly
max_i(e_s_i-e_y_i) <= r.
"""
from itertools import product, combinations


def covers_exp(s, y, r):
    return all(a - b <= r for a, b in zip(s, y))


def directed_radius(s, y):
    return max((a - b for a, b in zip(s, y)), default=0)


def min_certificate(Y, r):
    Y = tuple(dict.fromkeys(Y))
    if not Y:
        return 0
    for k in range(1, len(Y) + 1):
        for S in combinations(Y, k):
            if all(any(covers_exp(s, y, r) for s in S) for y in Y):
                return k
    raise AssertionError("finite set must cover itself")


def verify():
    families = 0
    points = 0
    pair_checks = 0
    monotonicity_checks = 0
    product_checks = 0

    # Exhaust all nonempty subsets of the 2D exponent grid {0,1}^2.
    grid = list(product(range(2), repeat=2))
    for mask in range(1, 1 << len(grid)):
        Y = [grid[i] for i in range(len(grid)) if mask & (1 << i)]
        families += 1
        points += len(Y)
        for r in range(3):
            for s in Y:
                for y in Y:
                    pair_checks += 1
                    assert covers_exp(s, y, r) == (directed_radius(s, y) <= r)
        sizes = [min_certificate(Y, r) for r in range(3)]
        assert sizes[0] >= sizes[1] >= sizes[2]
        monotonicity_checks += 2

    # Unit invariance is translation invariance in exponent coordinates.
    shifts = [(3, 5), (7, 2)]
    for mask in range(1, 1 << len(grid)):
        Y = [grid[i] for i in range(len(grid)) if mask & (1 << i)]
        for shift in shifts:
            Z = [tuple(v + shift[i] for i, v in enumerate(y)) for y in Y]
            for r in range(3):
                assert min_certificate(Y, r) == min_certificate(Z, r)

    # Product-family submultiplicativity on small one-dimensional families.
    one_d = [((0,),), ((1,),), ((0,), (1,)), ((0,), (2,))]
    for Y in one_d:
        for Z in one_d:
            P = [y + z for y in Y for z in Z]
            for r in range(3):
                lhs = min_certificate(P, r)
                rhs = min_certificate(Y, r) * min_certificate(Z, r)
                assert lhs <= rhs
                product_checks += 1

    print({
        "status": "PASS",
        "families": families,
        "points": points,
        "pair_equivalence_checks": pair_checks,
        "monotonicity_checks": monotonicity_checks,
        "product_checks": product_checks,
        "arithmetic": "integer exponent / exact",
    })


if __name__ == "__main__":
    verify()
