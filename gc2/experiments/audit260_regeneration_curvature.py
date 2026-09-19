#!/usr/bin/env python3
"""Exact checks for GC-II Audit 260.
No external dependencies.
"""
from itertools import combinations


def mobius_2(c):
    return c[3] - c[1] - c[2] + c[0]


def is_monotone(c):
    # masks 0,1(a),2(b),3(ab)
    return c[0] <= c[1] <= c[3] and c[0] <= c[2] <= c[3]


def submodular(c):
    return c[1] + c[2] >= c[3] + c[0]


def supermodular(c):
    return c[1] + c[2] <= c[3] + c[0]


def run():
    checks = 0
    positive_interactions = 0
    negative_interactions = 0
    for K in range(1, 1001):
        complement = (0, 0, 0, K)
        substitute = (0, K, K, K)

        assert is_monotone(complement)
        assert is_monotone(substitute)
        checks += 2

        assert not submodular(complement)
        assert supermodular(complement)
        checks += 2

        assert submodular(substitute)
        assert not supermodular(substitute)
        checks += 2

        mc = mobius_2(complement)
        ms = mobius_2(substitute)
        assert mc == K
        assert ms == -K
        positive_interactions += int(mc > 0)
        negative_interactions += int(ms < 0)
        checks += 2

        # positive rescaling invariance, lambda=2,3,5
        for lam in (2, 3, 5):
            cc = tuple(lam*v for v in complement)
            ss = tuple(lam*v for v in substitute)
            assert not submodular(cc) and supermodular(cc)
            assert submodular(ss) and not supermodular(ss)
            assert mobius_2(cc) == lam*K
            assert mobius_2(ss) == -lam*K
            checks += 4

    print({
        "K_values": 1000,
        "exact_assertion_checks": checks,
        "positive_pair_interactions": positive_interactions,
        "negative_pair_interactions": negative_interactions,
        "universal_submodularity": "FALSIFIED",
        "universal_supermodularity": "FALSIFIED",
        "status": "PASS",
    })


if __name__ == "__main__":
    run()
