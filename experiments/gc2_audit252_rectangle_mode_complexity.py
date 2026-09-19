"""GC-II Audit 252 exact finite verifier.

Checks on X={0,1}x{0,1}:
1. exact minimum rectangle-cover number for all 15 nonempty targets;
2. min-plus rectangle formula against endpoint shortest-path formula for every
   local 2-state directed system with edge costs in {absent,0,1,2};
3. rank-one iff rectangular;
4. zero-set lower-bound witness: any q-mode nonnegative additive exact
   representation induces q rectangles covering F (verified combinatorially by
   exhaustive rectangle-cover search).
No external packages.
"""
from itertools import product, combinations
from math import inf

A=(0,1)
X=tuple(product(A,A))
EDGE=(None,0,1,2)
SUBSETS=({0},{1},{0,1})

def local_dist(c01,c10):
    d=[[0,inf],[inf,0]]
    if c01 is not None: d[0][1]=c01
    if c10 is not None: d[1][0]=c10
    for k in A:
        for i in A:
            for j in A:
                d[i][j]=min(d[i][j],d[i][k]+d[k][j])
    return d

def rectangles_inside(F):
    F=set(F); out=[]
    for s0 in SUBSETS:
        for s1 in SUBSETS:
            R=frozenset(product(s0,s1))
            if R <= F:
                out.append((frozenset(s0),frozenset(s1),R))
    return out

def min_cover(F):
    F=frozenset(F)
    rs=rectangles_inside(F)
    for q in range(1,len(F)+1):
        for C in combinations(rs,q):
            if frozenset().union(*(r[2] for r in C))==F:
                return q,C
    raise AssertionError("singleton cover missing")

def endpoint_value(x,F,d0,d1):
    return min(d0[x[0]][y[0]]+d1[x[1]][y[1]] for y in F)

def cover_value(x,C,d0,d1):
    return min(
        min(d0[x[0]][y] for y in r0)+min(d1[x[1]][y] for y in r1)
        for r0,r1,_ in C
    )

def rectangular(F):
    F=set(F); p0={x[0] for x in F}; p1={x[1] for x in F}
    return F==set(product(p0,p1))

def main():
    targets=[frozenset(X[i] for i in range(4) if mask>>i&1)
             for mask in range(1,16)]
    covers={F:min_cover(F) for F in targets}
    assert all((covers[F][0]==1)==rectangular(F) for F in targets)
    # On 2x2 every nonempty target has cover number 1 or 2.
    assert max(q for q,_ in covers.values())==2

    systems=checks=0
    for e0 in product(EDGE,repeat=2):
        d0=local_dist(*e0)
        for e1 in product(EDGE,repeat=2):
            d1=local_dist(*e1); systems+=1
            for F in targets:
                q,C=covers[F]
                # C is a minimum rectangle cover. Theorem 252.1 says it is
                # enough for every local metric in this operational class.
                for x in X:
                    assert endpoint_value(x,F,d0,d1)==cover_value(x,C,d0,d1)
                    checks+=1

    rank_hist={q:sum(1 for qq,_ in covers.values() if qq==q)
               for q in sorted({qq for qq,_ in covers.values()})}
    print({"targets":len(targets),
           "rectangle_cover_histogram":rank_hist,
           "local_product_systems":systems,
           "exact_value_checks":checks,
           "status":"PASS"})

if __name__=="__main__":
    main()
