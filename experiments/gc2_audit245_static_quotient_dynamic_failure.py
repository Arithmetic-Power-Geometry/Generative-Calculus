#!/usr/bin/env python3
"""Exact finite verifier for GC-II Audit 245.

Shows that Audit-244 current-signature quotienting need not preserve
sequential capability when operations distinguish current static clones.
"""
from itertools import product


def feasible(p, g, lists, messages=(0, 1)):
    """Exact fiber-palette feasibility by exhaustive message labeling."""
    for z in set(p):
        idx = [i for i, zz in enumerate(p) if zz == z]
        decisions = sorted({g[i] for i in idx})
        if len(decisions) > len(messages):
            return False
        labels = decisions + [None]
        fiber_ok = False
        for vals in product(labels, repeat=len(messages)):
            lab = dict(zip(messages, vals))
            if all(any(a in lists[i] and lab[a] == g[i] for a in messages)
                   for i in idx):
                fiber_ok = True
                break
        if not fiber_ok:
            return False
    return True


def quotient(p, g, lists):
    seen = set(); qp=[]; qg=[]; ql=[]
    for z,d,L in zip(p,g,lists):
        key=(z,d,tuple(sorted(L)))
        if key not in seen:
            seen.add(key); qp.append(z); qg.append(d); ql.append(set(L))
    return qp,qg,ql


def main():
    # u,v are exact Audit-244 static clones; c requires the opposite decision.
    p=[0,0,0]
    g=[0,0,1]
    L=[{0},{0},{0}]
    assert quotient(p,g,L) == ([0,0],[0,1],[{0},{0}])
    assert not feasible(p,g,L)

    # Unit-cost operation distinguishes the clones: only u gains message 1.
    after=[{0,1},{0},{0}]
    assert not feasible(p,g,after), 'full system must remain infeasible'

    # Naively quotient first, retain u as the decision-0 representative,
    # then apply the representative effect. This predicts false escape.
    qp,qg,qL=quotient(p,g,L)
    q_after=[{0,1},{0}]
    assert feasible(qp,qg,q_after), 'naive static quotient predicts capability'

    # Directly quotienting the true successor keeps u and v separate because
    # their lists have diverged; it remains infeasible.
    ap,ag,aL=quotient(p,g,after)
    assert not feasible(ap,ag,aL)
    assert len(ap)==3

    print('initial_static_clone_pair=u,v')
    print('full_successor_feasible=False')
    print('naive_quotient_successor_feasible=True')
    print('quotient_of_true_successor_feasible=False')
    print('status=PASS: static quotient is not a dynamic congruence')


if __name__=='__main__':
    main()
