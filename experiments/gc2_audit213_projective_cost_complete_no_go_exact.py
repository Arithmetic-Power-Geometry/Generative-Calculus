"""GC-II Audit 213: projectivized cost data are complete up to scale, but not new capability structure.

Audit 212 left open replacing a scalar currency-normalized Omega_G by a
reference-free family of ratios/cross-ratios.  For a finite family of n>=2
strictly positive operational costs c=(c_0,...,c_{n-1}), define all pairwise
ratios r_ij=c_i/c_j.  These data are invariant under global positive rescaling.
Moreover they determine the entire positive cost vector up to exactly that
rescaling: if c_i/c_j=d_i/d_j for every i,j, then d=lambda*c for one lambda>0.
Thus passing from costs to all ratios is exactly projectivization of the positive
cost vector.  It removes the unit gauge but creates no additional capability
information. Cross-ratios c_i c_l/(c_j c_k) are functions of the pairwise ratios
and are therefore no richer.

Status:
  global-scale invariance of pairwise ratios: PROVED
  completeness up to positive scale: PROVED
  cross-ratios add information beyond pairwise ratios: FALSIFIED
  projective positive-cone geometry: IMPORTED/KNOWN mechanism
  projectivized costs as intrinsically new GC capability invariant: FALSIFIED
  coupling projective cost geometry to closure changes beyond raw cost data: OPEN
"""
from fractions import Fraction as F
from itertools import product


def ratios(c):
    assert len(c) >= 2 and all(x > 0 for x in c)
    return tuple(tuple(c[i] / c[j] for j in range(len(c))) for i in range(len(c)))


def cross_ratio(c, i, j, k, l):
    assert all(x > 0 for x in c)
    return c[i] * c[l] / (c[j] * c[k])

# Exact scale invariance.
c = (F(2), F(3), F(5), F(11))
r = ratios(c)
for lam in (F(1,101), F(1,7), F(1), F(13,5), F(10**6)):
    assert ratios(tuple(lam*x for x in c)) == r

# Reconstruction from ratios after choosing any gauge c_0=1.
reconstructed = tuple(r[i][0] for i in range(len(c)))
assert reconstructed == tuple(x/c[0] for x in c)

# Cross-ratios are products of pairwise ratios: (c_i/c_j)*(c_l/c_k).
for i,j,k,l in product(range(4), repeat=4):
    assert cross_ratio(c,i,j,k,l) == r[i][j] * r[l][k]

# Exhaustive finite rational collision test: equal complete ratio matrices imply
# positive proportionality, and proportional vectors have equal ratio matrices.
vals = [F(1), F(2), F(3), F(1,2), F(3,2)]
vectors = list(product(vals, repeat=3))
for a in vectors:
    ra = ratios(a)
    for b in vectors:
        same = ra == ratios(b)
        lam = b[0] / a[0]
        proportional = all(b[i] == lam*a[i] for i in range(3))
        assert same == proportional

# Boundary discipline: zero coordinates lie outside this positive projective chart.
for bad in ((F(0),F(1)), (F(1),F(0))):
    try:
        ratios(bad)
        raise RuntimeError('zero coordinate should be rejected')
    except AssertionError:
        pass

print('Audit 213 PASS: all positive cost ratios = cost vector modulo global scale; cross-ratios add no information')
