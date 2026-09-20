#!/usr/bin/env python3
"""Exact rational verifier for GC-II Audit 275.

Checks multiplicative-bin compression without floating-point arithmetic.
"""
from fractions import Fraction
from itertools import product, combinations


def bucket(v, m, alpha):
    out = []
    for x in v:
        assert x >= m > 0 and alpha > 1
        k = 0
        t = m
        while t * alpha <= x:
            t *= alpha
            k += 1
        out.append(k)
    return tuple(out)


def compress(Y, m, alpha):
    reps = {}
    for y in Y:
        reps.setdefault(bucket(y, m, alpha), y)
    return list(reps.values())


def covered(s, y, alpha):
    return all(si <= alpha * yi for si, yi in zip(s, y))


def verify(Y, m, M, alpha):
    S = compress(Y, m, alpha)
    assert all(m <= x <= M for y in Y for x in y)
    assert all(any(covered(s, y, alpha) for s in S) for y in Y)

    # Count actual multiplicative bins intersecting [m,M] exactly.
    kmax = 0
    t = m
    while t * alpha <= M:
        t *= alpha
        kmax += 1
    assert len(S) <= (kmax + 1) ** len(Y[0])
    return len(S), len(Y)


def main():
    m = Fraction(1)
    M = Fraction(6)
    alpha = Fraction(3, 2)
    total_targets = 0
    total_certificates = 0
    families = 0

    # Whole-grid tests through dimension 4.
    for d in range(1, 5):
        U = list(product([Fraction(i) for i in range(1, 7)], repeat=d))
        s, n = verify(U, m, M, alpha)
        total_certificates += s
        total_targets += n
        families += 1

    # Exhaustive small-family tests in dimensions 1 and 2.
    for d in (1, 2):
        U = list(product([Fraction(i) for i in range(1, 5)], repeat=d))
        for r in range(1, min(4, len(U)) + 1):
            for C in combinations(U, r):
                s, n = verify(list(C), m, Fraction(4), alpha)
                total_certificates += s
                total_targets += n
                families += 1

    # Degenerate M=m: one occupied bin regardless of dimension.
    for d in range(1, 9):
        Y = [tuple(Fraction(5) for _ in range(d))]
        S = compress(Y, Fraction(5), Fraction(7, 5))
        assert len(S) == 1

    # Positive coordinate unit-rescaling preserves coverage relation.
    Y = [(Fraction(1), Fraction(4)), (Fraction(2), Fraction(2)), (Fraction(4), Fraction(1))]
    S = compress(Y, Fraction(1), alpha)
    scales = (Fraction(7), Fraction(11, 3))
    Y2 = [tuple(a*x for a, x in zip(scales, y)) for y in Y]
    S2 = [tuple(a*x for a, x in zip(scales, s)) for s in S]
    for s, s2 in zip(S, S2):
        for y, y2 in zip(Y, Y2):
            assert covered(s, y, alpha) == covered(s2, y2, alpha)

    print("Audit 275 exact verifier: PASS")
    print("families checked:", families)
    print("targets checked:", total_targets)
    print("selected representatives accumulated:", total_certificates)
    print("alpha:", alpha)


if __name__ == "__main__":
    main()
