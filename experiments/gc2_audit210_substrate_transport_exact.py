"""GC-II Audit 210: exact checks for substrate lower-bound transport."""
from fractions import Fraction as F


def transported_bound(L, alpha, beta):
    assert alpha > 0 and L >= 0 and beta >= 0
    return max(F(0), (L-beta)/alpha)

# Exact rational edge/scale checks.
cases = [
    (F(10), F(2), F(0), F(5)),
    (F(10), F(2), F(4), F(3)),
    (F(3), F(7), F(3), F(0)),
    (F(1), F(3), F(2), F(0)),
    (F(17), F(1,2), F(2), F(30)),
]
for L,a,b,want in cases:
    got = transported_bound(L,a,b)
    assert got == want, (L,a,b,got,want)

# Exhaustive finite implication check on a rational grid:
# L <= CP <= alpha*CG+beta => CG >= transported bound.
grid = [F(i,2) for i in range(13)]
for L in grid:
  for alpha in (F(1,2),F(1),F(2),F(3)):
    for beta in grid:
      B = transported_bound(L,alpha,beta)
      for CG in grid:
        for CP in grid:
          if L <= CP <= alpha*CG+beta:
            assert CG >= B

# Necessity of the cost-domination gate: strict positive substrate LB
# can coexist with zero GC cost if no relation between the two costs is imposed.
L, CG, CP = F(5), F(0), F(5)
assert L <= CP and CG == 0

print("Audit 210 PASS: exact transport implication; no bound without cost domination")
