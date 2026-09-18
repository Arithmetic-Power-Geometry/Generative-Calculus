#!/usr/bin/env python3
"""Exact finite-world verifier for GC-II Audit 221.

Exhaustively checks deterministic 2-state/2-action dynamic systems through H=3.
Each state-action pair is either disabled or transitions to state 0/1, giving
3^(2*2)=81 systems. Costs are 0/1 and all 2^4=16 cost tables are checked.
For every system/cost table, all budgets B=0..3 are checked. Dynamic execution
and the explicit static time-unrolled relation must return exactly the same
(action,state,cost) trajectories.
"""
from itertools import product

S = (0, 1)
A = (0, 1)
H = 3
PAIRS = tuple(product(S, A))


def dynamic_runs(trans, cost, s0, B):
    out = set()
    def rec(t, s, actions, states, total):
        if t == H:
            out.add((actions, states, total))
            return
        for a in A:
            nxt = trans[(s, a)]
            if nxt is None:
                continue
            nt = total + cost[(s, a)]
            if nt <= B:
                rec(t + 1, nxt, actions + (a,), states + (nxt,), nt)
    rec(0, s0, (), (s0,), 0)
    return out


def static_unrolled_runs(trans, cost, s0, B):
    """Brute-force assignments to time-indexed S_1..S_H,A_0..A_H-1."""
    out = set()
    for actions in product(A, repeat=H):
        for tail in product(S, repeat=H):
            states = (s0,) + tail
            total = 0
            ok = True
            for t in range(H):
                s, a, sn = states[t], actions[t], states[t + 1]
                if trans[(s, a)] != sn:
                    ok = False
                    break
                total += cost[(s, a)]
            if ok and total <= B:
                out.add((actions, states, total))
    return out


systems = 0
instances = 0
trajectories_compared = 0
# transition code: -1 disabled, 0/1 next state
for tcode in product((-1, 0, 1), repeat=len(PAIRS)):
    trans = {p: (None if v == -1 else v) for p, v in zip(PAIRS, tcode)}
    systems += 1
    for ccode in product((0, 1), repeat=len(PAIRS)):
        cost = dict(zip(PAIRS, ccode))
        for s0 in S:
            for B in range(H + 1):
                d = dynamic_runs(trans, cost, s0, B)
                u = static_unrolled_runs(trans, cost, s0, B)
                assert d == u
                instances += 1
                trajectories_compared += len(d)

assert systems == 81
assert instances == 81 * 16 * 2 * 4
print(f"systems={systems}")
print(f"instances={instances}")
print(f"dynamic_static_equal=True")
print(f"feasible_trajectories_compared={trajectories_compared}")
print("zero_cost_edges_included=True")
print("disabled_actions_included=True")
