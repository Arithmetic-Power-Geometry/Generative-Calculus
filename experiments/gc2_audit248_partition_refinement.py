#!/usr/bin/env python3
"""Exact finite checks for GC-II Audit 248 fixed-generator congruence."""
from math import inf
from heapq import heappush, heappop
import random


def refine(states, ops, goals, enabled, succ, cost):
    color = {x: int(x in goals) for x in states}
    while True:
        keys = {}
        for x in states:
            sig = [int(x in goals)]
            for o in ops:
                en = enabled.get((x,o), False)
                sig.append((o, en, cost.get((x,o)) if en else None,
                            color[succ[(x,o)]] if en else None))
            keys[x] = tuple(sig)
        palette = {k:i for i,k in enumerate(sorted(set(keys.values()), key=repr))}
        new = {x: palette[keys[x]] for x in states}
        same_partition = all((color[x] == color[y]) == (new[x] == new[y])
                             for x in states for y in states)
        color = new
        if same_partition:
            return color


def values(states, ops, goals, enabled, succ, cost):
    rev = {x: [] for x in states}
    for x in states:
        for o in ops:
            if enabled.get((x,o), False):
                rev[succ[(x,o)]].append((x, cost[(x,o)]))
    d = {x: inf for x in states}; q=[]
    for g in goals:
        d[g]=0; heappush(q,(0,g))
    while q:
        du,u=heappop(q)
        if du != d[u]: continue
        for v,c in rev[u]:
            nd=du+c
            if nd<d[v]: d[v]=nd; heappush(q,(nd,v))
    return d


def random_check(seed=248, trials=5000):
    rng=random.Random(seed)
    for _ in range(trials):
        n=rng.randint(1,7); states=tuple(range(n)); ops=('R','I','A','L')[:rng.randint(1,4)]
        goals={x for x in states if rng.random()<.3}
        enabled={}; succ={}; cost={}
        for x in states:
            for o in ops:
                en=rng.random()<.65; enabled[(x,o)]=en
                if en:
                    succ[(x,o)]=rng.choice(states); cost[(x,o)]=rng.randint(0,4)
        col=refine(states,ops,goals,enabled,succ,cost)
        val=values(states,ops,goals,enabled,succ,cost)
        for x in states:
            for y in states:
                if col[x]==col[y]:
                    assert val[x]==val[y]
                    assert (x in goals)==(y in goals)
                    for o in ops:
                        assert enabled[(x,o)]==enabled[(y,o)]
                        if enabled[(x,o)]:
                            assert cost[(x,o)]==cost[(y,o)]
                            assert col[succ[(x,o)]]==col[succ[(y,o)]]
    return trials


def extension_split_demo():
    states=('x','y','G'); ops=('a',); goals={'G'}
    en={('x','a'):True,('y','a'):True,('G','a'):False}
    su={('x','a'):'G',('y','a'):'G'}; co={('x','a'):2,('y','a'):2}
    c=refine(states,ops,goals,en,su,co); assert c['x']==c['y']
    # Add a state-selective generator q: Audit 247 says the class may split.
    ops2=('a','q'); en2=dict(en); su2=dict(su); co2=dict(co)
    for s in states: en2[(s,'q')]=False
    en2[('x','q')]=True; su2[('x','q')]='G'; co2[('x','q')]=0
    c2=refine(states,ops2,goals,en2,su2,co2); assert c2['x']!=c2['y']


if __name__=='__main__':
    print('random_finite_systems_checked=', random_check())
    extension_split_demo()
    print('extension_split_demo=PASS')
    print('status=PASS')
