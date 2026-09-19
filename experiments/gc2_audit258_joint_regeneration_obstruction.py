#!/usr/bin/env python3
"""Exact checks for GC-II Audit 258: singleton regeneration is incomplete."""
from math import inf, isinf
import heapq


def regen_cost(n, edges, sig, source, target_atoms):
    adj=[[] for _ in range(n)]
    for u,v,c in edges:
        assert c >= 0
        adj[u].append((v,c))
    d=[inf]*n
    d[source]=0
    pq=[(0,source)]
    while pq:
        du,u=heapq.heappop(pq)
        if du != d[u]:
            continue
        if target_atoms <= sig[u]:
            return du
        for v,c in adj[u]:
            nd=du+c
            if nd < d[v]:
                d[v]=nd
                heapq.heappush(pq,(nd,v))
    return inf


def check_instance(K=None):
    # 0=s, 1=u(a), 2=v(b), 3=t(a,b)
    sig=[frozenset(),frozenset({'a'}),frozenset({'b'}),frozenset({'a','b'})]
    edges=[(0,1,0),(0,2,0)]
    if K is not None:
        edges.append((0,3,K))
    ca=regen_cost(4,edges,sig,0,frozenset({'a'}))
    cb=regen_cost(4,edges,sig,0,frozenset({'b'}))
    cab=regen_cost(4,edges,sig,0,frozenset({'a','b'}))
    assert ca == 0 and cb == 0
    if K is None:
        assert isinf(cab)
    else:
        assert cab == K
        assert cab-max(ca,cb) == K
    return ca,cb,cab


def main():
    unreachable=check_instance()
    finite=[]
    for K in range(1,101):
        ca,cb,cab=check_instance(K)
        finite.append((K,ca,cb,cab,cab-max(ca,cb)))

    # The same singleton vector (0,0) supports arbitrary joint cost K.
    assert len({(r[1],r[2]) for r in finite}) == 1
    assert {r[3] for r in finite} == set(range(1,101))

    # Monotonicity sanity check: adding a cheaper joint edge can only decrease cost.
    sig=[frozenset(),frozenset({'a'}),frozenset({'b'}),frozenset({'a','b'})]
    for hi in range(1,21):
        base=[(0,1,0),(0,2,0),(0,3,hi)]
        old=regen_cost(4,base,sig,0,frozenset({'a','b'}))
        for lo in range(hi+1):
            new=regen_cost(4,base+[(0,3,lo)],sig,0,frozenset({'a','b'}))
            assert new <= old

    print({
        'status':'PASS',
        'unreachable_joint':isinf(unreachable[2]),
        'finite_K_checked':100,
        'singleton_vector':[0,0],
        'joint_cost_range':[1,100],
        'conclusion':'no finite universal bound from singleton regeneration costs alone'
    })


if __name__ == '__main__':
    main()
