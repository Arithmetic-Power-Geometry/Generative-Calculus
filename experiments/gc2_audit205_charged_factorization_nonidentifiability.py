"""Exact verifier for GC-II Audit 205.

Claim tested: charging fusion/splitting prevents Audit-204 trivialization only after
an operational cost model is fixed. The same capability semantics can yield
incompatible regularized interaction values under different admissible cost
models, so the value is not intrinsic to capability semantics alone.
"""
from fractions import Fraction
from itertools import combinations

N = tuple("RIAL")


def partitions(items):
    if not items:
        yield ()
        return
    first, rest = items[0], items[1:]
    for p in partitions(rest):
        yield (frozenset([first]),) + p
        for i in range(len(p)):
            yield p[:i] + (p[i] | {first},) + p[i+1:]


def canonical(p):
    return tuple(sorted(tuple(sorted(b)) for b in p))


def all_partitions(items):
    seen = set()
    for p in partitions(items):
        c = canonical(p)
        if c not in seen:
            seen.add(c)
            yield tuple(frozenset(b) for b in c)


def subsets(seq):
    for r in range(len(seq)+1):
        for c in combinations(range(len(seq)), r):
            yield frozenset(c)


def mobius(v, p):
    idx = tuple(range(len(p)))
    vals = {}
    for S in subsets(idx):
        U = frozenset().union(*(p[i] for i in S)) if S else frozenset()
        vals[S] = Fraction(v(U))
    out = {}
    for T in subsets(idx):
        out[T] = sum(((-1)**(len(T)-len(S))*vals[S]
                      for S in subsets(tuple(T))), Fraction(0))
    return out


def J(v, p):
    return sum((abs(x) for T, x in mobius(v,p).items() if len(T)>=2), Fraction(0))


P = list(all_partitions(N))
assert len(P) == 15
fine = tuple(frozenset([x]) for x in N)
top = next(p for p in P if len(p)==1)

functions = {
    "AND4": lambda S: int(set(N).issubset(S)),
    "OR4": lambda S: int(bool(S)),
    "RI_AND": lambda S: int({"R","I"}.issubset(S)),
    "PARITY": lambda S: len(S)%2,
}

for name,v in functions.items():
    j0 = J(v,fine)
    assert J(v,top) == 0
    # Model FREE: every regrouping is zero cost -> Audit-204 collapse.
    K_free = min(J(v,p) for p in P)
    assert K_free == 0

    # Model LOCKED: any departure from the fine operational atoms costs M>j0.
    M = j0 + 1
    def c_locked(p): return Fraction(0) if p == fine else M
    K_locked = min(J(v,p)+c_locked(p) for p in P)
    assert K_locked == j0

    # Same v, same partitions; only cost semantics changed.
    print(name, "J_fine=", j0, "K_free=", K_free, "K_locked=", K_locked)

print("PASS: charged factorization avoids trivialization only relative to an explicit operational cost model; capability semantics alone do not identify the regularized value.")