#!/usr/bin/env python3
"""Exact finite checks for GC-II Audit 255."""
from math import inf, isinf
import heapq


def distances(n, edges, s):
    adj=[[] for _ in range(n)]
    for u,v,c in edges:
        assert c >= 0
        adj[u].append((v,c))
    d=[inf]*n; d[s]=0
    pq=[(0,s)]
    while pq:
        du,u=heapq.heappop(pq)
        if du != d[u]: continue
        for v,c in adj[u]:
            nd=du+c
            if nd < d[v]:
                d[v]=nd; heapq.heappush(pq,(nd,v))
    return d


def pair_stats(n, edges, x, y):
    f=distances(n,edges,x)[y]
    r=distances(n,edges,y)[x]
    if isinf(f) or isinf(r): return f,r,None,None,None
    g=f-r; a=abs(g); rt=f+r
    alpha=0 if rt==0 else a/rt
    return f,r,g,a,alpha


def main():
    # Equal scalar costs without edgewise reversibility.
    edges=[(0,1,1),(1,2,1),(2,3,1),(3,0,1)]
    f,r,g,a,alpha=pair_stats(4,edges,0,2)
    assert (f,r,g,a,alpha)==(2,2,0,0,0)
    assert (1,0,1) not in edges and (2,1,1) not in edges

    # One-way reachability: derived finite gap intentionally undefined.
    f,r,g,a,alpha=pair_stats(2,[(0,1,1)],0,1)
    assert f==1 and isinf(r) and g is None

    # Composition cancellation: product distances add in independent product.
    # Component 1: f/r=(1,2); component 2: f/r=(2,1).
    f1,r1=1,2; f2,r2=2,1
    g1=f1-r1; g2=f2-r2
    assert g1==-1 and g2==1
    fj=f1+f2; rj=r1+r2; gj=fj-rj
    assert (fj,rj,gj)==(3,3,0)
    assert abs(gj) < abs(g1)+abs(g2)

    # Exhaustive arithmetic stress test over small finite directional costs.
    checks=0
    for f1 in range(4):
      for r1 in range(4):
       for f2 in range(4):
        for r2 in range(4):
          g1=f1-r1; g2=f2-r2
          gj=(f1+f2)-(r1+r2)
          assert gj==g1+g2
          assert abs(gj) <= abs(g1)+abs(g2)
          rt=(f1+f2)+(r1+r2)
          alpha=0 if rt==0 else abs(gj)/rt
          assert 0 <= alpha <= 1
          checks += 1
    print({"status":"PASS","composition_checks":checks,
           "zero_gap_not_structural_reversibility":True,
           "one_way_case_guarded":True})

if __name__=='__main__': main()
