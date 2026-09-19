"""Audit 262: exact verifier for one-edge GC-II novelty sensitivity.

Exhaustively enumerates all directed 3-state baseline graphs with edge status
absent or cost in {0,1,2}; for every source, nonempty target, absent edge, and
inserted cost in {0,1,2}, checks
 V_{G+e}(x,F)=min(V_G(x,F), d_G(x,u)+k+V_G(v,F)).
Also checks generator monotonicity and the explicit two-edge synergy example.
"""
from itertools import product
from math import inf

N=3
PAIRS=[(i,j) for i in range(N) for j in range(N) if i!=j]
CHOICES=[None,0,1,2]

def floyd(edges):
    d=[[inf]*N for _ in range(N)]
    for i in range(N): d[i][i]=0
    for (u,v),c in edges.items(): d[u][v]=min(d[u][v],c)
    for k in range(N):
        for i in range(N):
            for j in range(N):
                if d[i][k]+d[k][j] < d[i][j]:
                    d[i][j]=d[i][k]+d[k][j]
    return d

def val(d,x,F): return min(d[x][f] for f in F)

checks=0
for assignment in product(CHOICES, repeat=len(PAIRS)):
    E={p:c for p,c in zip(PAIRS,assignment) if c is not None}
    d=floyd(E)
    absent=[p for p in PAIRS if p not in E]
    for mask in range(1,1<<N):
        F={i for i in range(N) if mask>>i & 1}
        for x in range(N):
            base=val(d,x,F)
            for u,v in absent:
                for k in (0,1,2):
                    E2=dict(E); E2[(u,v)]=k
                    d2=floyd(E2)
                    got=val(d2,x,F)
                    rhs=min(base,d[x][u]+k+val(d,v,F))
                    assert got==rhs, (E,F,x,(u,v,k),got,rhs)
                    assert got<=base
                    checks+=2

# Explicit contextual-synergy collision, using a four-state helper.
def fw4(edges):
    n=4; d=[[inf]*n for _ in range(n)]
    for i in range(n): d[i][i]=0
    for (u,v),c in edges.items(): d[u][v]=min(d[u][v],c)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                d[i][j]=min(d[i][j],d[i][k]+d[k][j])
    return d
base={(0,3):10}
e1={(0,1):0}; e2={(1,3):0}
V=lambda e: fw4(e)[0][3]
assert V(base)==10
assert V({**base,**e1})==10
assert V({**base,**e2})==10
assert V({**base,**e1,**e2})==0

print({"audit":262,"exact_identity_and_monotonicity_checks":checks,"synergy_example":"passed"})
