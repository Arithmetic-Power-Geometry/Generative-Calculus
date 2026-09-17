"""GC-II Audit 200: exact finite check of the decision-critical TV bound.

For two worlds requiring opposite binary decisions, if one policy has error <= eps
in each world, then TV(P0,P1) >= 1-2 eps. This script exhaustively checks the
finite binary-transcript case on a rational grid and records tight witnesses.
"""
from fractions import Fraction

GRID = [Fraction(i, 20) for i in range(21)]

def tv_bernoulli(p0, p1):
    return abs(p0-p1)

checked = feasible = tight = 0
for p0 in GRID:  # Pr[transcript=1 | world 0]
    for p1 in GRID:  # Pr[transcript=1 | world 1]
        for d0 in (0,1):  # action on transcript 0
            for d1 in (0,1):  # action on transcript 1
                # required decision is world label
                err0 = (1-p0)*(d0 != 0) + p0*(d1 != 0)
                err1 = (1-p1)*(d0 != 1) + p1*(d1 != 1)
                eps = max(err0, err1)
                checked += 1
                if eps <= Fraction(1,2):
                    feasible += 1
                    bound = 1 - 2*eps
                    tv = tv_bernoulli(p0,p1)
                    assert tv >= bound
                    if tv == bound:
                        tight += 1

print({"checked": checked, "feasible_eps_le_half": feasible, "tight": tight})
