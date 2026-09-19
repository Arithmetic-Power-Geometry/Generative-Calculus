"""GC-II Audit 251 exact finite verifier.

Exhaustively checks all nonempty targets on X={0,1}x{0,1}, and all local
2-state directed systems whose two directed non-loop edges independently have
cost in {absent,0,1,2}. Verifies endpoint and minimum-rectangle formulas.
No external packages.
"""
from itertools import product, combinations
from math import inf

A=(0,1)
X=tuple(product(A,A))
EDGE=(None,0,1,2)

def local_dist(c01,c10):
    d=[[0, inf],[inf,0]]
    if c01 is not None: d[0][1]=c01
    if c10 is not None: d[1][0]=c10
    # Floyd-Warshall (also protects future generalization)
    for k in A:
        for i in A:
            for j in A:
                d[i][j]=min(d[i][j],d[i][k]+d[k][j])
    return d

def rectangles_inside(F):
    F=set(F); out=[]
    subsets=[{0},{1},{0,1}]
    for r0 in subsets:
        for r1 in subsets:
            R=set(product(r0,r1))
            if R and R <= F:
                out.append((frozenset(r0),frozenset(r1),frozenset(R)))
    return out

def rectangle_rank(F):
    F=frozenset(F)
    if not F: return 0
    rs=rectangles_inside(F)
    for q in range(1,len(F)+1):
        for C in combinations(rs,q):
            U=frozenset().union(*(r[2] for r in C))
            if U==F: return q
    raise AssertionError("singleton cover missing")

def best_rectangle_formula(x,F,d0,d1):
    vals=[]
    for R0,R1,_ in rectangles_inside(F):
        a=min(d0[x[0]][y] for y in R0)
        b=min(d1[x[1]][y] for y in R1)
        vals.append(a+b)
    return min(vals)

def endpoint_formula(x,F,d0,d1):
    return min(d0[x[0]][y[0]]+d1[x[1]][y[1]] for y in F)

def is_rectangular(F):
    F=set(F)
    if not F: return False
    p0={x[0] for x in F}; p1={x[1] for x in F}
    return F==set(product(p0,p1))

def main():
    targets=[]
    for mask in range(1,1<<len(X)):
        targets.append(frozenset(X[i] for i in range(len(X)) if mask>>i & 1))
    assert len(targets)==15
    ranks={F:rectangle_rank(F) for F in targets}
    assert all((ranks[F]==1)==is_rectangular(F) for F in targets)
    rectangular=sum(is_rectangular(F) for F in targets)
    assert rectangular==9

    systems=0; checks=0
    for e0 in product(EDGE,repeat=2):
        d0=local_dist(*e0)
        for e1 in product(EDGE,repeat=2):
            d1=local_dist(*e1); systems+=1
            for F in targets:
                for x in X:
                    v=endpoint_formula(x,F,d0,d1)
                    vr=best_rectangle_formula(x,F,d0,d1)
                    assert v==vr,(e0,e1,F,x,v,vr)
                    checks+=1
    print({
        "targets":len(targets),
        "rectangular_targets":rectangular,
        "local_product_systems":systems,
        "value_checks":checks,
        "max_rectangle_rank":max(ranks.values()),
        "status":"PASS"
    })

if __name__=="__main__": main()
