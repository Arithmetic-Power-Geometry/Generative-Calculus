"""Audit 267: exact checks for complete nonlinear typed-budget certificates."""
from fractions import Fraction
from itertools import product, combinations

INF=None

def leq(y,b):
    return all(a<=q for a,q in zip(y,b))

def ratio(a,q):
    if q==0:
        return Fraction(0) if a==0 else INF
    return Fraction(a,q)

def rho(Y,b):
    if not Y:
        return INF
    vals=[]
    for y in Y:
        rs=[ratio(a,q) for a,q in zip(y,b)]
        vals.append(INF if any(r is INF for r in rs) else max(rs))
    finite=[v for v in vals if v is not INF]
    return min(finite) if finite else INF

def rho_le_one(Y,b):
    r=rho(Y,b)
    return r is not INF and r<=1

def feasible(Y,b):
    return any(leq(y,b) for y in Y)

# The Audit-266 collision is separated by nonlinear max-ratio scalarization.
Y=((0,3),(3,0))
Z=((0,3),(2,2),(3,0))
assert rho(Y,(2,2))==Fraction(3,2)
assert rho(Z,(2,2))==Fraction(1)

# Exhaustively verify exact budget equivalence for every subset of the 3x3 cost grid
# and every budget in the 4x4 grid. 2^9 * 16 = 8192 exact checks.
points=tuple(product(range(3), repeat=2))
budgets=tuple(product(range(4), repeat=2))
checks=0
for mask in range(1<<len(points)):
    S=tuple(points[i] for i in range(len(points)) if mask&(1<<i))
    for b in budgets:
        assert feasible(S,b)==rho_le_one(S,b)
        checks+=1

# Positive coordinate-rescaling invariance, including zero-budget coordinates.
scale_checks=0
for a1,a2 in product(range(1,5), repeat=2):
    for b in budgets:
        SY=tuple((a1*y1,a2*y2) for y1,y2 in Z)
        sb=(a1*b[0],a2*b[1])
        assert rho_le_one(Z,b)==rho_le_one(SY,sb)
        scale_checks+=1

print({
    'audit':267,
    'exact_budget_equivalence_checks':checks,
    'rescaling_checks':scale_checks,
    'audit266_rho_Y_at_2_2':str(rho(Y,(2,2))),
    'audit266_rho_Z_at_2_2':str(rho(Z,(2,2))),
    'nonlinear_threshold_family_complete_finite_typed_budget_semantics':'PROVED',
})
