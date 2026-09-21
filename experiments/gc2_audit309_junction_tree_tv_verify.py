"""Exact rational checks for GC-II Audit 309.

Checks the A-B-C junction tree C1={A,B}, C2={B,C}, S={B} on a
finite family including structural zeros. No floating-point tolerance is used.
"""
from fractions import Fraction as F
from itertools import product


def norm(row):
    s = sum(row)
    return None if s == 0 else tuple(F(x, s) for x in row)


def tv(p, q):
    keys = set(p) | set(q)
    return sum(abs(p.get(k, F(0))-q.get(k, F(0))) for k in keys) / 2


def marginal(p, coords):
    out = {}
    for x, px in p.items():
        key = tuple(x[i] for i in coords)
        out[key] = out.get(key, F(0)) + px
    return out


def model(root_b, a_given_b, c_given_b):
    p = {}
    for a,b,c in product(range(2), repeat=3):
        p[(a,b,c)] = root_b[b] * a_given_b[b][a] * c_given_b[b][c]
    return p


# Small exact catalogue: deterministic, uniform and biased rows; root rows include zeros.
rows = [norm(x) for x in [(1,0),(0,1),(1,1),(1,2),(2,1)]]
roots = rows
models = []
for rb in roots:
    for a0 in rows:
        for a1 in rows:
            for c0 in rows:
                for c1 in rows:
                    models.append(model(rb, (a0,a1), (c0,c1)))

# Deduplicate exact laws, then use a deterministic stride to keep CI/runtime modest.
uniq = list({tuple(sorted(p.items())): p for p in models}.values())
sample = uniq[::max(1, len(uniq)//256)][:256]
checked = 0
for p in sample:
    for q in sample:
        lhs = tv(p,q)
        pab, qab = marginal(p,(0,1)), marginal(q,(0,1))
        pbc, qbc = marginal(p,(1,2)), marginal(q,(1,2))
        pb, qb = marginal(p,(1,)), marginal(q,(1,))
        rhs = tv(pab,qab) + tv(pbc,qbc) + tv(pb,qb)
        assert lhs <= rhs, (lhs, rhs)
        # Bounded task indicators are automatically controlled by TV; verify all atoms.
        for x in product(range(2), repeat=3):
            assert abs(p[x]-q[x]) <= lhs
        checked += 1

print({"unique_models": len(uniq), "sample_models": len(sample),
       "ordered_pairs_checked": checked, "status": "PASS"})
