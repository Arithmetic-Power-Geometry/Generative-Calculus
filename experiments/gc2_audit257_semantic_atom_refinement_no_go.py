#!/usr/bin/env python3
"""Exact finite checks for GC-II Audit 257."""
from itertools import product
from math import inf, isinf
import heapq


def edge_loss(sig, u, v, weights=None):
    lost = sig[u] - sig[v]
    if weights is None:
        return len(lost)
    return sum(weights[a] for a in lost)


def dist(n, edges, sig, source, weights=None):
    adj=[[] for _ in range(n)]
    for u,v in edges:
        adj[u].append((v,edge_loss(sig,u,v,weights)))
    d=[inf]*n; d[source]=0
    pq=[(0,source)]
    while pq:
        du,u=heapq.heappop(pq)
        if du != d[u]:
            continue
        for v,w in adj[u]:
            nd=du+w
            if nd < d[v]:
                d[v]=nd; heapq.heappush(pq,(nd,v))
    return d


def defect(n, edges, sig, x, y, weights=None):
    a=dist(n,edges,sig,x,weights)[y]
    b=dist(n,edges,sig,y,weights)[x]
    return inf if isinf(a) or isinf(b) else a+b


def clone_signature(sig,k):
    return [{(a,r) for a in s for r in range(k)} for s in sig]


def main():
    # Exhaust all 3-state annotations by two atoms and all nonempty directed-edge subsets.
    n=3
    possible_edges=[(u,v) for u in range(n) for v in range(n) if u!=v]
    atoms=(0,1)
    subsets=[frozenset(a for bit,a in enumerate(atoms) if mask&(1<<bit)) for mask in range(4)]
    checks=0
    positive=0
    for states in product(subsets, repeat=n):
        sig=list(states)
        for mask in range(1,1<<len(possible_edges)):
            edges=[e for i,e in enumerate(possible_edges) if mask&(1<<i)]
            for x in range(n):
                for y in range(x+1,n):
                    d=defect(n,edges,sig,x,y)
                    for k in (2,3):
                        sk=clone_signature(sig,k)
                        dk=defect(n,edges,sk,x,y)
                        if isinf(d):
                            assert isinf(dk)
                        else:
                            assert dk == k*d
                            # Unit original weights, split equally among aliases.
                            wk={(a,r):1.0/k for a in atoms for r in range(k)}
                            dw=defect(n,edges,sk,x,y,wk)
                            assert abs(dw-d) < 1e-12
                            if d>0:
                                positive += 1
                        checks += 1
    print({"status":"PASS","systems":len(subsets)**n*((1<<len(possible_edges))-1),
           "pair_k_checks":checks,"positive_finite_checks":positive,
           "raw_scaling":"exact","weighted_split_invariance":"exact"})


if __name__=="__main__":
    main()
