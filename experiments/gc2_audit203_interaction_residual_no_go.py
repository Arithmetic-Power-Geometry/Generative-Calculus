"""Exact checks for GC-II Audit 203 interaction-residual no-go."""
from itertools import combinations
from fractions import Fraction

N = ("R", "I", "A", "L")

def subsets(xs):
    xs = tuple(xs)
    for k in range(len(xs)+1):
        for c in combinations(xs,k):
            yield frozenset(c)

def mobius(v, T):
    T=frozenset(T)
    return sum(((-1)**(len(T)-len(S)))*v[S] for S in subsets(T))

def reconstruct(coeff, S):
    return sum(coeff[T] for T in subsets(S))

# Pure R-I conjunction; A,L irrelevant.
v={S: Fraction(int({"R","I"}.issubset(S))) for S in subsets(N)}
m={T: mobius(v,T) for T in subsets(N)}
assert all(reconstruct(m,S)==v[S] for S in subsets(N))
assert m[frozenset(("R","I"))] == 1
assert all(x==0 for T,x in m.items() if T != frozenset(("R","I")))

# Semantics-preserving regrouping into a single package coordinate X.
Np=("X",)
vp={frozenset():Fraction(0), frozenset(("X",)):Fraction(1)}
mp={T:mobius(vp,T) for T in subsets(Np)}
assert mp[frozenset(("X",))] == 1
assert all(reconstruct(mp,S)==vp[S] for S in subsets(Np))

# Monotone set functions can have negative interaction coefficients.
# OR on R,I is monotone but its pair coefficient is -1.
vor={S:Fraction(int(bool({"R","I"}.intersection(S)))) for S in subsets(("R","I"))}
assert mobius(vor,{"R"})==1 and mobius(vor,{"I"})==1
assert mobius(vor,{"R","I"})==-1

print("Audit 203 exact checks: PASS")
print("4-coordinate nonzero coefficient: m({R,I}) =", m[frozenset(("R","I"))])
print("regrouped nonzero coefficient: m({X}) =", mp[frozenset(("X",))])
print("monotone OR pair interaction =", mobius(vor,{"R","I"}))
