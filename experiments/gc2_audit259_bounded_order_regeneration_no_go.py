#!/usr/bin/env python3
"""Exact verifier for GC-II Audit 259: bounded-order regeneration is incomplete."""
from itertools import combinations
from math import inf, isinf
import heapq


def powerset(items):
    items=tuple(items)
    for r in range(len(items)+1):
        for c in combinations(items,r):
            yield frozenset(c)


def regen_cost(n, edges, sig, source, target):
    adj=[[] for _ in range(n)]
    for u,v,c in edges:
        assert c >= 0
        adj[u].append((v,c))
    d=[inf]*n; d[source]=0
    pq=[(0,source)]
    while pq:
        du,u=heapq.heappop(pq)
        if du != d[u]: continue
        if target <= sig[u]: return du
        for v,c in adj[u]:
            nd=du+c
            if nd < d[v]:
                d[v]=nd; heapq.heappush(pq,(nd,v))
    return inf


def instance(m,K):
    U=frozenset(range(m))
    proper=[T for T in powerset(U) if T != U]
    sig=[frozenset()] + proper + [U]
    source=0
    full=len(sig)-1
    edges=[]
    for i,T in enumerate(proper, start=1):
        edges.append((source,i,0))
    if K is not None:
        edges.append((source,full,K))
    return U,sig,edges,source


def profile(m,K):
    U,sig,edges,s=instance(m,K)
    return {T:regen_cost(len(sig),edges,sig,s,T) for T in powerset(U)}


def main():
    checks=0
    positive_cases=0
    # Verify dimensions m=2..7 and arbitrary finite full costs K=0..25.
    for m in range(2,8):
        U=frozenset(range(m))
        unreachable=profile(m,None)
        assert isinf(unreachable[U])
        for T,v in unreachable.items():
            if T != U:
                assert v == 0
            checks += 1
        for K in range(26):
            p=profile(m,K)
            assert p[U] == K
            for T,v in p.items():
                if T != U:
                    assert v == 0
                checks += 1
            if K>0: positive_cases += 1

        # Strong collision: every proper-subset query agrees between K=1 and K=25,
        # while the full-set value differs.
        p1,p25=profile(m,1),profile(m,25)
        for T in powerset(U):
            if T != U:
                assert p1[T] == p25[T] == 0
        assert p1[U] == 1 and p25[U] == 25

        # Monotonicity C(T)<=C(T') whenever T subseteq T'.
        p=profile(m,7)
        subsets=list(p)
        for A in subsets:
            for B in subsets:
                if A <= B:
                    assert p[A] <= p[B]

    print({
        'status':'PASS',
        'm_checked':[2,7],
        'finite_K_checked':[0,25],
        'profile_value_checks':checks,
        'positive_instances':positive_cases,
        'unreachable_full_set_checked':True,
        'conclusion':'all proper-subset regeneration costs can be fixed while full-set cost is arbitrary or infinite'
    })


if __name__ == '__main__':
    main()
