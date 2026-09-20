"""Audit 266: exact regression checks for incompleteness of all linear typed prices.

The theorem itself is analytic (see notes/gc2_audit266_linear_monotone_incompleteness.md).
This script checks nondominance, finite budget separation, and a large exact integer
weight grid for the fixed unsupported-Pareto-point counterexample.
"""
from fractions import Fraction

Y=((0,3),(3,0))
Z=((0,3),(2,2),(3,0))

def dominates(a,b):
    return all(x<=y for x,y in zip(a,b)) and a!=b

def pareto(S):
    return tuple(sorted(x for x in set(S) if not any(dominates(y,x) for y in set(S))))

def feasible(S,b):
    return any(all(x<=q for x,q in zip(y,b)) for y in S)

def scalar(S,w):
    return min(sum(Fraction(a)*Fraction(b) for a,b in zip(y,w)) for y in S)

assert pareto(Y)==tuple(sorted(Y))
assert pareto(Z)==tuple(sorted(Z))
assert (2,2) in pareto(Z)
assert not feasible(Y,(2,2))
assert feasible(Z,(2,2))

# Exhaustive small-budget behaviour: ensure there really is operational separation.
distinguishing=[]
for b1 in range(5):
    for b2 in range(5):
        if feasible(Y,(b1,b2)) != feasible(Z,(b1,b2)):
            distinguishing.append((b1,b2))
assert (2,2) in distinguishing

# Exact rational arithmetic over a large nonnegative integer-weight grid.
# Analytic proof covers every real w>=0; this is a regression/falsification check.
weight_checks=0
for w1 in range(101):
    for w2 in range(101):
        if w1==0 and w2==0:
            continue
        w=(w1,w2)
        assert scalar(Y,w)==scalar(Z,w)==3*min(w1,w2)
        weight_checks+=1

# Explicit symbolic-case inequalities sampled exactly: when w1<=w2,
# (3,0) is no worse than (2,2); symmetric for w2<=w1.
case_checks=0
for w1 in range(101):
    for w2 in range(101):
        if w1<=w2:
            assert 3*w1 <= 2*w1+2*w2
        if w2<=w1:
            assert 3*w2 <= 2*w1+2*w2
        case_checks+=1

print({
    "audit":266,
    "pareto_Y":pareto(Y),
    "pareto_Z":pareto(Z),
    "distinguishing_budgets_0_to_4":distinguishing,
    "exact_nonzero_weight_checks":weight_checks,
    "case_inequality_checks":case_checks,
    "all_linear_prices_complete_for_typed_budget_semantics":"FALSIFIED",
})
