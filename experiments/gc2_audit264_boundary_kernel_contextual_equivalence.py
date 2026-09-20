"""Audit 264: exact finite checks for boundary-kernel contextual equivalence.

Enumerates all directed 3-state modules with boundary {0,1}, one private state 2,
and edge status absent or cost in {0,1,2}. Replaces each module by its boundary
distance kernel. Glues every one-external-state context on visible states {0,1,3}
whose edges are absent or cost 0/2, then checks all visible ordered distances.
"""
from itertools import product
from math import inf

B=(0,1)
VISIBLE=(0,1,3)
MODULE_PAIRS=[(i,j) for i in range(3) for j in range(3) if i!=j]
CONTEXT_PAIRS=[(i,j) for i in VISIBLE for j in VISIBLE if i!=j]
MCHOICES=[None,0,1,2]
CCHOICES=[None,0,2]

def floyd(n, edges):
    d=[[inf]*n for _ in range(n)]
    for i in range(n): d[i][i]=0
    for (u,v),c in edges.items(): d[u][v]=min(d[u][v],c)
    for k in range(n):
        for i in range(n):
            if d[i][k]==inf: continue
            for j in range(n):
                d[i][j]=min(d[i][j],d[i][k]+d[k][j])
    return d

def merge(a,b):
    out=dict(a)
    for e,c in b.items(): out[e]=min(out.get(e,inf),c)
    return out

contexts=[]
for assignment in product(CCHOICES, repeat=len(CONTEXT_PAIRS)):
    contexts.append({p:c for p,c in zip(CONTEXT_PAIRS,assignment) if c is not None})

checks=0
modules=0
for assignment in product(MCHOICES, repeat=len(MODULE_PAIRS)):
    M={p:c for p,c in zip(MODULE_PAIRS,assignment) if c is not None}
    dm=floyd(3,M)
    K={}
    for i in B:
        for j in B:
            if i!=j and dm[i][j]<inf: K[(i,j)]=dm[i][j]
    for C in contexts:
        dM=floyd(4,merge(M,C))
        dK=floyd(4,merge(K,C))
        for x in VISIBLE:
            for y in VISIBLE:
                assert dM[x][y]==dK[x][y]
                checks+=1
    modules+=1

# Necessity probe: unequal 0->1 boundary kernels are externally distinguishable.
M1={(0,1):1}
M2={(0,1):2}
probe={(3,0):0}  # external source 3; target is visible boundary state 1
assert floyd(4,merge(M1,probe))[3][1]==1
assert floyd(4,merge(M2,probe))[3][1]==2

assert modules==4096
assert len(contexts)==729
assert checks==26873856
print({"audit":264,"modules":modules,"contexts":len(contexts),
       "visible_distance_equalities":checks,"necessity_probe":"passed"})
