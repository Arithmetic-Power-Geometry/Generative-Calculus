#!/usr/bin/env python3
"""Exact rational verifier for GC-II Audit 276.

Checks support-safe multiplicative compression with exact zeros.
"""
from fractions import Fraction
from itertools import product, combinations


def symbol(x, m, alpha):
    if x == 0:
        return -1
    assert x >= m > 0 and alpha > 1
    k = 0
    t = m
    while t * alpha <= x:
        t *= alpha
        k += 1
    return k


def cell(v, mins, alpha):
    return tuple(symbol(x, m, alpha) for x, m in zip(v, mins))


def compress(Y, mins, alpha):
    reps = {}
    for y in Y:
        reps.setdefault(cell(y, mins, alpha), y)
    return list(reps.values())


def covered(s, y, alpha):
    return all(si <= alpha * yi for si, yi in zip(s, y))


def positive_bins(m, M, alpha):
    kmax = 0
    t = m
    while t * alpha <= M:
        t *= alpha
        kmax += 1
    return kmax + 1


def verify(Y, mins, maxs, alpha):
    d = len(mins)
    assert Y and all(len(y) == d for y in Y)
    for y in Y:
        for x, m, M in zip(y, mins, maxs):
            assert x == 0 or m <= x <= M
    S = compress(Y, mins, alpha)
    assert all(any(covered(s, y, alpha) for s in S) for y in Y)
    bound = 1
    for m, M in zip(mins, maxs):
        bound *= positive_bins(m, M, alpha) + 1  # exact zero symbol
    assert len(S) <= bound
    # Any representative covering a zero target coordinate must also be zero there.
    for y in Y:
        for s in S:
            if covered(s, y, alpha):
                assert all(yi != 0 or si == 0 for si, yi in zip(s, y))
    return len(S), len(Y), bound


def main():
    alpha = Fraction(3, 2)
    families = targets = selected = 0

    # Whole zero-inclusive grids through dimension 4.
    for d in range(1, 5):
        U = list(product([Fraction(i) for i in range(0, 5)], repeat=d))
        s, n, _ = verify(U, [Fraction(1)] * d, [Fraction(4)] * d, alpha)
        families += 1; targets += n; selected += s

    # Exhaustive small families in dimensions 1 and 2.
    for d in (1, 2):
        U = list(product([Fraction(i) for i in range(0, 4)], repeat=d))
        for r in range(1, min(4, len(U)) + 1):
            for C in combinations(U, r):
                s, n, _ = verify(list(C), [Fraction(1)] * d, [Fraction(3)] * d, alpha)
                families += 1; targets += n; selected += s

    # All-zero vector must survive as its own support cell.
    for d in range(1, 9):
        zero = tuple(Fraction(0) for _ in range(d))
        Y = [zero, tuple(Fraction(1) for _ in range(d))]
        S = compress(Y, [Fraction(1)] * d, alpha)
        assert zero in S
        assert any(covered(s, zero, alpha) for s in S)
        assert all(not covered(s, zero, alpha) for s in S if s != zero)

    # Coordinate-specific ranges and unit rescaling preserve coverage.
    Y = [(Fraction(0), Fraction(4)), (Fraction(2), Fraction(0)),
         (Fraction(2), Fraction(4)), (Fraction(1), Fraction(2))]
    mins = [Fraction(1), Fraction(2)]
    maxs = [Fraction(2), Fraction(4)]
    S = compress(Y, mins, alpha)
    scales = [Fraction(7), Fraction(11, 3)]
    Y2 = [tuple(a*x for a, x in zip(scales, y)) for y in Y]
    S2 = [tuple(a*x for a, x in zip(scales, s)) for s in S]
    for s, s2 in zip(S, S2):
        for y, y2 in zip(Y, Y2):
            assert covered(s, y, alpha) == covered(s2, y2, alpha)

    # Unresolved positive scales: number of occupied cells grows with N.
    for N in range(1, 40):
        YN = [(Fraction(1, 2**j),) for j in range(N + 1)]
        # With alpha=2 and a floor adapted to the smallest positive value,
        # every scale is a distinct bin: no uniform bound independent of scale range.
        SN = compress(YN, [Fraction(1, 2**N)], Fraction(2))
        assert len(SN) == N + 1

    print("Audit 276 exact verifier: PASS")
    print("families checked:", families)
    print("targets checked:", targets)
    print("selected representatives accumulated:", selected)
    print("alpha:", alpha)


if __name__ == "__main__":
    main()
