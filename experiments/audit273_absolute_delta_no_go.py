"""Audit 273: additive-delta accounting versus multiplicative novelty.

Exact Fraction arithmetic.  Verifies the normalized upper bound on a finite
2-D grid and the fixed-delta unbounded family.
"""
from fractions import Fraction
from itertools import combinations, product


def pareto(S):
    return [x for x in S if not any(y != x and all(y[i] <= x[i] for i in range(len(x))) for y in S)]


def rho(B, e):
    return min(max(b[i] / e[i] for i in range(len(e))) for b in B)


def omega(B, E):
    P = pareto(E)
    return max([Fraction(1)] + [rho(B, e) for e in P])


def covered_additively(B, E, delta):
    return all(any(all(b[i] <= e[i] + delta[i] for i in range(len(e))) for b in B) for e in pareto(E))


# Exhaustive positive-grid verification of
# Omega <= 1 + max_i Delta_i / m_i,
# m_i = min_{e in P(E)} e_i.
U = [(Fraction(a), Fraction(b)) for a in range(1, 4) for b in range(1, 4)]
subsets = []
for r in range(1, 4):
    subsets.extend([list(c) for c in combinations(U, r)])

checks = 0
for B in subsets:
    for E in subsets:
        P = pareto(E)
        for delta in product((Fraction(0), Fraction(1), Fraction(2)), repeat=2):
            if not covered_additively(B, E, delta):
                continue
            m = [min(e[i] for e in P) for i in range(2)]
            bound = 1 + max(delta[i] / m[i] for i in range(2))
            assert omega(B, E) <= bound
            checks += 1

assert checks == 120270

# Fixed absolute improvement Delta=1 but unbounded multiplicative novelty:
# E_n={(1/n,1)}, B_n={(1+1/n,1)}.  Omega=n+1.
for n in range(1, 1001):
    e = (Fraction(1, n), Fraction(1))
    b = (Fraction(1, 1) + Fraction(1, n), Fraction(1))
    B, E = [b], [e]
    delta = (Fraction(1), Fraction(0))
    assert covered_additively(B, E, delta)
    assert omega(B, E) == n + 1

# Tight normalized bound in one active coordinate.
for n in range(1, 1001):
    m, d = Fraction(1, n), Fraction(3, n)
    E = [(m, Fraction(1))]
    B = [(m + d, Fraction(1))]
    delta = (d, Fraction(0))
    assert omega(B, E) == 1 + d / m

print({"status": "PASS", "exhaustive_bound_checks": checks,
       "unbounded_family_checks": 1000, "tightness_checks": 1000})
