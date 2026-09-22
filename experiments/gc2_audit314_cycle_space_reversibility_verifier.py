#!/usr/bin/env python3
"""Exact verifier for GC-II Audit 314.

Enumerates all antisymmetric directions on K4 with independent upper-triangle
entries in {-1,0,1}; embeds them in positive directed primitive costs; computes
all-pairs shortest paths exactly with Fraction; verifies that the optimal-cost
asymmetry equals the prescribed field. It also computes, by exact rational
Gaussian elimination, the rank of the root-triangle circulation map for K_n,
n=2,...,8, and checks rank=(n-1)(n-2)/2.
"""
from fractions import Fraction
from itertools import product, combinations


def floyd(c):
    n=len(c)
    d=[row[:] for row in c]
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if d[i][k]+d[k][j] < d[i][j]:
                    d[i][j]=d[i][k]+d[k][j]
    return d


def rank_q(mat):
    a=[[Fraction(x) for x in row] for row in mat]
    if not a: return 0
    R,C=len(a),len(a[0]); r=0
    for c in range(C):
        p=next((i for i in range(r,R) if a[i][c]),None)
        if p is None: continue
        a[r],a[p]=a[p],a[r]
        q=a[r][c]
        a[r]=[x/q for x in a[r]]
        for i in range(R):
            if i!=r and a[i][c]:
                q=a[i][c]
                a[i]=[a[i][j]-q*a[r][j] for j in range(C)]
        r+=1
        if r==R: break
    return r


def circulation_matrix(n,root=0):
    edges=list(combinations(range(n),2))
    idx={e:k for k,e in enumerate(edges)}
    def coeff(u,v):
        if u<v: return idx[(u,v)],1
        return idx[(v,u)],-1
    rows=[]
    others=[v for v in range(n) if v!=root]
    for x,y in combinations(others,2):
        row=[0]*len(edges)
        for u,v in ((root,x),(x,y),(y,root)):
            k,s=coeff(u,v); row[k]+=s
        rows.append(row)
    return rows


def exhaustive_k4():
    n=4; M=Fraction(10); lam=Fraction(1)
    edges=list(combinations(range(n),2)); checked=0
    for vals in product((-1,0,1), repeat=len(edges)):
        a=[[Fraction(0) for _ in range(n)] for _ in range(n)]
        for (i,j),v in zip(edges,vals):
            a[i][j]=Fraction(v); a[j][i]=-Fraction(v)
        c=[[Fraction(0) if i==j else None for j in range(n)] for i in range(n)]
        for i in range(n):
            for j in range(n):
                if i!=j: c[i][j]=M+lam*a[i][j]/2
        d=floyd(c)
        for i in range(n):
            for j in range(n):
                if d[i][j]-d[j][i] != lam*a[i][j]:
                    raise AssertionError((vals,i,j,d[i][j],d[j][i],a[i][j]))
        checked+=1
    return checked


def main():
    checked=exhaustive_k4()
    print(f"K4 exact realizability cases: {checked}")
    for n in range(2,9):
        beta=(n-1)*(n-2)//2
        r=rank_q(circulation_matrix(n))
        assert r==beta,(n,r,beta)
        print(f"K{n}: root-triangle rank={r}, beta={beta}")
    print("PASS: all exact checks succeeded")

if __name__=='__main__': main()
