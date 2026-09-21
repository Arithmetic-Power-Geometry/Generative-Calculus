#!/usr/bin/env python3
"""Exact finite verifier for GC-II Audit 296.

Uses integer/brute-force combinatorics and fractions only; no floating point.
Checks all labelled bipartite graphs with side sizes 1..3 and explicit odd cycles.
"""
from fractions import Fraction
from itertools import combinations


def min_vertex_cover(vertices, edges):
    V=list(vertices)
    for k in range(len(V)+1):
        for C in combinations(V,k):
            S=set(C)
            if all(u in S or v in S for u,v in edges):
                return k
    raise AssertionError("no cover")


def max_matching(vertices, edges):
    E=list(edges)
    best=0
    for mask in range(1<<len(E)):
        used=set(); ok=True; n=0
        for i,(u,v) in enumerate(E):
            if mask>>i & 1:
                if u in used or v in used:
                    ok=False; break
                used.add(u); used.add(v); n+=1
        if ok: best=max(best,n)
    return best


def all_bipartite_graphs(p,q):
    L=[f'L{i}' for i in range(p)]
    R=[f'R{j}' for j in range(q)]
    possible=[(u,v) for u in L for v in R]
    for mask in range(1<<len(possible)):
        E=[e for i,e in enumerate(possible) if mask>>i & 1]
        yield L+R,E


def check_bipartite_exhaustive():
    graphs=edges_seen=0
    for p in range(1,4):
        for q in range(1,4):
            for V,E in all_bipartite_graphs(p,q):
                tau=min_vertex_cover(V,E)
                nu=max_matching(V,E)
                assert tau==nu, (V,E,tau,nu)
                graphs+=1; edges_seen+=len(E)
    return graphs,edges_seen


def check_odd_cycles():
    rows=[]
    for n in range(3,14,2):
        V=list(range(n)); E=[(i,(i+1)%n) for i in range(n)]
        tau=min_vertex_cover(V,E)
        # x_v=1/2 is primal feasible; z_e=1/2 is dual feasible.
        # Equal values certify the fractional optimum by weak duality.
        p=sum((Fraction(1,2) for _ in V), Fraction(0))
        d=sum((Fraction(1,2) for _ in E), Fraction(0))
        assert p==d==Fraction(n,2)
        assert tau==(n+1)//2
        assert Fraction(tau,1)-p==Fraction(1,2)
        rows.append((n,tau,p))
    return rows


def check_degenerate():
    assert min_vertex_cover(['a','b'],[])==0
    assert max_matching(['a','b'],[])==0
    # duplicate feasibility pairs must be deduplicated before simple-graph matching
    E=[('a','b'),('a','b')]
    assert min_vertex_cover(['a','b'],E)==1
    assert max_matching(['a','b'],list(set(E)))==1


if __name__=='__main__':
    check_degenerate()
    g,e=check_bipartite_exhaustive()
    odd=check_odd_cycles()
    print(f'PASS bipartite graphs={g}, accumulated edge occurrences={e}')
    for n,tau,frac in odd:
        print(f'PASS C_{n}: exact={tau}, fractional={frac}, additive_gap={Fraction(tau)-frac}')
