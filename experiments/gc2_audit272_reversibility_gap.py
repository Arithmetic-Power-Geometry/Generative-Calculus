"""Exact finite audit for GC-II Audit 272 round-trip reversibility gap."""
from itertools import combinations
from fractions import Fraction

INF = None

def pareto(S):
    return frozenset(x for x in S if not any(y != x and all(a <= b for a,b in zip(y,x)) for y in S))

def M(X,Y):
    """Exact directed dilation; None denotes +infinity."""
    if not Y: return Fraction(0)
    if not X: return INF
    worst = Fraction(0)
    for y in Y:
        best = INF
        for x in X:
            ratios=[]
            feasible=True
            for a,b in zip(x,y):
                if b==0:
                    if a>0: feasible=False; break
                    ratios.append(Fraction(0))
                else:
                    ratios.append(Fraction(a,b))
            if feasible:
                r=max(ratios, default=Fraction(0))
                if best is INF or r<best: best=r
        if best is INF: return INF
        worst=max(worst,best)
    return worst

def omega(X,Y):
    m=M(X,Y)
    return INF if m is INF else max(Fraction(1),m)

def leq_mul(a,b,c):
    """Check a <= b*c in extended nonnegative rationals."""
    if c is INF or b is INF: return True
    if a is INF: return False
    return a <= b*c

def rg_zero(X,Y):
    return omega(X,Y)==1 and omega(Y,X)==1

def mink(A,B):
    return frozenset(tuple(x+y for x,y in zip(a,b)) for a in A for b in B)

def main():
    U=[(0,0),(0,1),(1,0),(1,1)]
    sets=[frozenset(c) for r in range(0,len(U)+1) for c in combinations(U,r)]
    # quotient identity and directed multiplicative triangle
    triples=0
    for X in sets:
      for Y in sets:
        assert rg_zero(X,Y) == (pareto(X)==pareto(Y))
        for Z in sets:
            assert leq_mul(omega(X,Z),omega(X,Y),omega(Y,Z))
            assert leq_mul(omega(Z,X),omega(Z,Y),omega(Y,X))
            triples+=1

    # Coherent positive coordinate rescaling preserves both directions.
    scale_checks=0
    for X in sets:
      for Y in sets:
        for s in [(2,3),(3,5)]:
            DX=frozenset((s[0]*x[0],s[1]*x[1]) for x in X)
            DY=frozenset((s[0]*y[0],s[1]*y[1]) for y in Y)
            assert omega(X,Y)==omega(DX,DY)
            assert omega(Y,X)==omega(DY,DX)
            scale_checks+=1

    # Independent additive composition bound, checked multiplicatively:
    # each composed direction <= max(component directions), hence RG product
    # <= product of both component round-trip products.
    nonempty=[S for S in sets if S]
    comp=0
    for X1 in nonempty:
      for Y1 in nonempty:
       for X2 in nonempty:
        for Y2 in nonempty:
            Cx=mink(X1,X2); Cy=mink(Y1,Y2)
            f=omega(Cx,Cy); r=omega(Cy,Cx)
            f1,f2=omega(X1,Y1),omega(X2,Y2)
            r1,r2=omega(Y1,X1),omega(Y2,X2)
            assert f <= max(f1,f2)
            assert r <= max(r1,r2)
            assert f*r <= (f1*r1)*(f2*r2)
            comp+=1

    print({"sets":len(sets),"triangle_triples":triples,
           "unit_rescaling_checks":scale_checks,
           "composition_checks":comp,"status":"PASS"})

if __name__ == "__main__": main()
