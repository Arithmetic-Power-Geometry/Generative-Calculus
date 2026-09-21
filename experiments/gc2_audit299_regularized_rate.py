#!/usr/bin/env python3
"""Exact finite checks for GC-II Audit 299. No external packages."""
from fractions import Fraction
from itertools import combinations, product


def cover_number(universe, sets):
    U = set(universe)
    if not U:
        return 0
    for k in range(1, len(sets) + 1):
        for idx in combinations(range(len(sets)), k):
            covered = set()
            for i in idx:
                covered |= sets[i]
            if U <= covered:
                return k
    return None


def power_instance(Y, A, k):
    U = set(product(Y, repeat=k))
    actions = []
    for inds in product(range(len(A)), repeat=k):
        actions.append(set(product(*[A[i] for i in inds])))
    return U, actions


def triangle_checks():
    Y = (0, 1, 2)
    A = ({0, 1}, {0, 2}, {1, 2})
    Ns = []
    certs = []
    for k in (1, 2, 3):
        U, actions = power_instance(Y, A, k)
        N = cover_number(U, actions)
        Ns.append(N)

        # Exact product fractional primal: every action weight 1/2^k.
        xp = Fraction(1, 2**k)
        for y in U:
            containing = sum(y in S for S in actions)
            assert containing * xp == 1
        primal_value = len(actions) * xp

        # Exact product fractional dual: every target weight 1/2^k.
        zd = Fraction(1, 2**k)
        for S in actions:
            assert len(S) * zd == 1
        dual_value = len(U) * zd
        expected = Fraction(3**k, 2**k)
        assert primal_value == dual_value == expected
        assert Fraction(N, 1) >= expected
        certs.append(str(expected))

    assert Ns == [2, 3, 5]
    # Audit-298 submultiplicativity visible at k=2.
    assert Ns[1] < Ns[0] ** 2
    return Ns, certs


def degenerate_checks():
    # Universal action: exact and fractional account number are one.
    assert cover_number({0, 1, 2}, [{0, 1, 2}]) == 1
    # Empty target universe is handled outside logarithmic regularization.
    assert cover_number(set(), []) == 0


if __name__ == "__main__":
    Ns, certs = triangle_checks()
    degenerate_checks()
    print({
        "triangle_integer_cover_N_k_k1_to_k3": Ns,
        "triangle_fractional_Nf_k_exact": certs,
        "triangle_fractional_base": "3/2",
        "universal_action_check": "PASS",
        "empty_universe_check": "PASS",
        "status": "PASS",
    })
