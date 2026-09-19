#!/usr/bin/env python3
"""Exact verifier for GC-II Audit 244 replication obstruction."""
from itertools import product
from math import inf


def omega_add(p, g, lists, messages=(0, 1)):
    total = 0
    for z in set(p):
        idx = [i for i, zz in enumerate(p) if zz == z]
        decisions = sorted({g[i] for i in idx})
        if len(decisions) > len(messages):
            return inf
        best = inf
        labels = decisions + [None]
        for vals in product(labels, repeat=len(messages)):
            if any(d not in vals for d in decisions):
                continue
            lab = dict(zip(messages, vals))
            uncovered = sum(
                not any(a in lists[i] and lab[a] == g[i] for a in messages)
                for i in idx
            )
            best = min(best, uncovered)
        total += best
    return total


def replicate(p, g, lists, k):
    return (
        [z for z in p for _ in range(k)],
        [d for d in g for _ in range(k)],
        [set(L) for L in lists for _ in range(k)],
    )


def quotient(p, g, lists):
    seen = set(); qp=[]; qg=[]; ql=[]
    for z,d,L in zip(p,g,lists):
        key=(z,d,tuple(sorted(L)))
        if key not in seen:
            seen.add(key); qp.append(z); qg.append(d); ql.append(set(L))
    return qp,qg,ql


def exhaustive_small():
    # All 1..4-world binary p,g assignments and nonempty lists over two messages.
    checked=0
    options=[{0},{1},{0,1}]
    for n in range(1,5):
        for p in product((0,1), repeat=n):
            for g in product((0,1), repeat=n):
                for ls in product(range(3), repeat=n):
                    lists=[options[j] for j in ls]
                    base=omega_add(p,g,lists)
                    for k in (2,3):
                        rp,rg,rl=replicate(p,g,lists,k)
                        rep=omega_add(rp,rg,rl)
                        assert rep == k*base
                        q0=omega_add(*quotient(p,g,lists))
                        q1=omega_add(*quotient(rp,rg,rl))
                        assert q0 == q1
                    checked += 1
    return checked


def main():
    p=[0,0]; g=[0,1]; lists=[{0},{0}]
    assert omega_add(p,g,lists)==1
    for k in range(1,101):
        assert omega_add(*replicate(p,g,lists,k))==k
    checked=exhaustive_small()
    print('exhaustive_base_instances=', checked)
    print('replication_factors_checked=2,3')
    print('minimal_family_max_k=100')
    print('status=PASS')


if __name__=='__main__':
    main()
