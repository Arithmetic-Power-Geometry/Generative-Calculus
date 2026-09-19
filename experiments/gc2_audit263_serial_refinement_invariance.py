"""Audit 263: exhaustive checks for private serial-refinement invariance.

Enumerates all directed 3-state graphs with edge status absent or cost in {0,1,2},
refines each present non-loop edge with every nonnegative integer split of its cost,
and checks all original-state pair distances and all nonempty original-state target values.
Also checks an exposed-helper counterexample.
"""
from itertools import product
from math import inf

N=3
PAIRS=[(i,j) for i in range(N) for j in range(N) if i!=j]
CHOICES=[None,0,1,2]

def floyd(n, edges):
    d=[[inf]*n for _ in range(n)]
    for i in range(n): d[i][i]=0
    for (u,v),c in edges.items(): d[u][v]=min(d[u][v],c)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                d[i][j]=min(d[i][j],d[i][k]+d[k][j])
    return d

def val(d,x,F): return min(d[x][f] for f in F)

checks=0
for assignment in product(CHOICES, repeat=len(PAIRS)):
    E={p:c for p,c in zip(PAIRS,assignment) if c is not None}
    d=floyd(N,E)
    for (u,v),k in list(E.items()):
        for a in range(k+1):
            b=k-a; z=N
            R=dict(E); del R[(u,v)]
            R[(u,z)]=a; R[(z,v)]=b
            dr=floyd(N+1,R)
            for x in range(N):
                for y in range(N):
                    assert d[x][y]==dr[x][y]
                    checks+=1
            for mask in range(1,1<<N):
                F={i for i in range(N) if mask>>i & 1}
                for x in range(N):
                    assert val(d,x,F)==val(dr,x,F)
                    checks+=1

# Boundary: exposing helper z changes behavior, so this is not pure refactoring.
# Original: u=0,v=1,t=2, edges 0->1 cost2 and 0->2 cost10.
base={(0,1):2,(0,2):10}
assert floyd(3,base)[0][2]==10
ref={(0,3):1,(3,1):1,(0,2):10,(3,2):0}
assert floyd(4,ref)[0][2]==1

print({"audit":263,"serial_refinement_checks":checks,"exposed_helper_boundary":"passed"})