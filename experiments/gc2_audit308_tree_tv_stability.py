"""Exact finite verifier for GC-II Audit 308.

Builds the same finite family of binary A-B-C Markov chains used around Audit
307, compares every ordered pair, and checks the zero-safe TV bound using
fractions only. No floating tolerance is used.
"""
from fractions import Fraction
from itertools import product


def tv(p, q):
    keys = set(p) | set(q)
    return sum(abs(p.get(k, 0) - q.get(k, 0)) for k in keys) / 2


def dists2():
    out = []
    for a, b in product((0, 1, 2), repeat=2):
        if a == b == 0:
            continue
        s = a + b
        x = (Fraction(a, s), Fraction(b, s))
        if x not in out:
            out.append(x)
    return out


def dists4():
    out = []
    for ws in product((0, 1), repeat=4):
        if not any(ws):
            continue
        s = sum(ws)
        out.append(tuple(Fraction(w, s) for w in ws))
    return out


def model(seed_ab, k0, k1):
    ker = (k0, k1)
    p = {(a,b,c): seed_ab[2*a+b] * ker[b][c]
         for a,b,c in product((0,1), repeat=3)}
    ab = {(a,b): sum(p[a,b,c] for c in (0,1))
          for a,b in product((0,1), repeat=2)}
    bc = {(b,c): sum(p[a,b,c] for a in (0,1))
          for b,c in product((0,1), repeat=2)}
    b = {b: sum(p[a,b,c] for a,c in product((0,1), repeat=2))
         for b in (0,1)}
    return p, ab, bc, b


binary = dists2()
models = [model(s,k0,k1) for s in dists4() for k0 in binary for k1 in binary]
checked = 0
for P in models:
    for Q in models:
        p, pab, pbc, pb = P
        q, qab, qbc, qb = Q
        lhs = tv(p,q)
        # Root the chain at the AB clique and add the B->C conditional step.
        rhs = tv(pab,qab) + tv(pbc,qbc) + tv(pb,qb)
        assert lhs <= rhs
        checked += 1

print({"status":"PASS", "models":len(models), "ordered_pairs":checked,
       "arithmetic":"exact Fraction", "bound":"TV(ABC)<=TV(AB)+TV(BC)+TV(B)"})
