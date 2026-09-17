"""GC-II Audit 214: full budgeted closure filtration is exactly the threshold-cost function.

Let X be a finite state set with admissible directed transformations carrying
nonnegative costs.  Define d(x,y) as minimum path cost (infinity if unreachable)
and C_B(x)={y:d(x,y)<=B}. Then

    d(x,y) = inf { B>=0 : y in C_B(x) }

(with inf empty = infinity), while conversely C_B(x) is the B-sublevel set of d.
Thus the complete budget-indexed generative-closure filtration and the directed
shortest-path cost geometry contain exactly the same information. Coupling raw
cost geometry to *all* budgeted closure changes therefore cannot, by itself,
produce information beyond the induced directed cost distance.

Status:
  filtration -> threshold-cost reconstruction: PROVED
  threshold-cost -> filtration reconstruction: PROVED
  equivalence including unreachable/zero-cost cases: PROVED
  directed shortest-path/Lawvere-style cost geometry: IMPORTED/KNOWN mechanism
  full budgeted-closure filtration as intrinsically new Omega_G: FALSIFIED
  structure beyond threshold reachability (e.g. path multiplicity, rule provenance,
  intervention dependence, endogenous rule creation): OPEN
"""
from fractions import Fraction as F
from heapq import heappush, heappop
from math import inf
from itertools import product


def apsp(n, edges):
    out=[[] for _ in range(n)]
    for u,v,w in edges:
        assert F(w)>=0
        out[u].append((v,F(w)))
    D=[]
    for s in range(n):
        d=[inf]*n; d[s]=F(0); q=[(F(0),s)]
        while q:
            du,u=heappop(q)
            if du!=d[u]: continue
            for v,w in out[u]:
                z=du+w
                if d[v] is inf or z<d[v]:
                    d[v]=z; heappush(q,(z,v))
        D.append(tuple(d))
    return tuple(D)


def closure(D,x,B):
    B=F(B)
    return frozenset(y for y,z in enumerate(D[x]) if z is not inf and z<=B)


def reconstruct_from_filtration(D,x,y):
    # In a finite graph, every finite shortest-path value is itself a threshold.
    thresholds=sorted({z for row in D for z in row if z is not inf})
    hits=[B for B in thresholds if y in closure(D,x,B)]
    return min(hits) if hits else inf

# Hand cases: zero-cost escape, asymmetric reachability, alternative cheaper path.
edges=[(0,1,F(0)),(1,2,F(3,2)),(0,2,F(5)),(2,3,F(2))]
D=apsp(4,edges)
assert D[0][1]==0 and D[0][2]==F(3,2) and D[0][3]==F(7,2)
assert D[3][0] is inf
for x,y in product(range(4),repeat=2):
    assert reconstruct_from_filtration(D,x,y)==D[x][y]
for B in (F(0),F(1),F(3,2),F(2),F(7,2),F(100)):
    assert closure(D,0,B)==frozenset(y for y in range(4) if D[0][y] is not inf and D[0][y]<=B)

# Exhaustive directed 3-state graph family. Each ordered nonloop edge is absent,
# zero-cost, or unit-cost: 3^6=729 exact graphs.
pairs=[(u,v) for u in range(3) for v in range(3) if u!=v]
for labels in product((-1,0,1), repeat=len(pairs)):
    E=[(u,v,F(w)) for (u,v),w in zip(pairs,labels) if w>=0]
    D=apsp(3,E)
    for x,y in product(range(3),repeat=2):
        assert reconstruct_from_filtration(D,x,y)==D[x][y]

print('Audit 214 PASS: full budgeted closure filtration <=> directed threshold-cost geometry on all 729 exact finite graphs')
