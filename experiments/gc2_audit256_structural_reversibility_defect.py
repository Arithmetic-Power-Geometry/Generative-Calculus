#!/usr/bin/env python3
"""Exact finite checks for GC-II Audit 256."""
from math import inf, isinf
import heapq


def kappa_edges(edges):
    """edges: iterable of (u,v,type,cost). Return (u,v,kappa)."""
    sig={(u,v,t) for u,v,t,c in edges}
    return [(u,v,0 if (v,u,t) in sig else 1) for u,v,t,c in edges]


def dist(n, weighted_edges, s):
    adj=[[] for _ in range(n)]
    for u,v,w in weighted_edges:
        assert w >= 0
        adj[u].append((v,w))
    d=[inf]*n; d[s]=0
    pq=[(0,s)]
    while pq:
        du,u=heapq.heappop(pq)
        if du != d[u]: continue
        for v,w in adj[u]:
            nd=du+w
            if nd < d[v]:
                d[v]=nd; heapq.heappush(pq,(nd,v))
    return d


def structural_defect(n, edges, x, y):
    ke=kappa_edges(edges)
    f=dist(n,ke,x)[y]; r=dist(n,ke,y)[x]
    return inf if isinf(f) or isinf(r) else f+r


def product_edges(n1,e1,n2,e2):
    out=[]
    idx=lambda a,b:a*n2+b
    for a,b,t,c in e1:
        for z in range(n2): out.append((idx(a,z),idx(b,z),"1:"+t,c))
    for a,b,t,c in e2:
        for z in range(n1): out.append((idx(z,a),idx(z,b),"2:"+t,c))
    return out


def main():
    # Audit-255 equal-cost directed cycle: scalar asymmetry 0, structural defect 4.
    cyc=[(0,1,"A",1),(1,2,"A",1),(2,3,"A",1),(3,0,"A",1)]
    monetary=[(u,v,c) for u,v,t,c in cyc]
    assert dist(4,monetary,0)[2] == dist(4,monetary,2)[0] == 2
    assert structural_defect(4,cyc,0,2)==4

    # Bidirected but unequal monetary costs: structural defect zero.
    bi=[(0,1,"R",1),(1,0,"R",7)]
    assert structural_defect(2,bi,0,1)==0

    # Wrong-type reverse does not count as typed inverse.
    wrong=[(0,1,"R",1),(1,0,"I",1)]
    assert structural_defect(2,wrong,0,1)==2

    # One-way reachability remains infinite.
    assert isinf(structural_defect(2,[(0,1,"A",0)],0,1))

    # Exhaustive independent-product additivity over all nonempty directed
    # 2-state edge subsets, with one type and arbitrary irrelevant money cost.
    base=[(0,1,"A",1),(1,0,"A",2)]
    systems=[]
    for mask in range(1,4):
        systems.append([base[i] for i in range(2) if mask & (1<<i)])
    checks=0
    for e1 in systems:
      for e2 in systems:
        d1=structural_defect(2,e1,0,1)
        d2=structural_defect(2,e2,0,1)
        ep=product_edges(2,e1,2,e2)
        dp=structural_defect(4,ep,0,3)
        if isinf(d1) or isinf(d2):
            assert isinf(dp)
        else:
            assert dp==d1+d2
        checks += 1

    print({"status":"PASS","audit255_collision_separated":True,
           "typed_reverse_checked":True,"product_checks":checks})


if __name__=="__main__": main()
