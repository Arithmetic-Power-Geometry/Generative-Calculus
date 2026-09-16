"""GC-II Audit 176: exact finite product-compilation check.

This script constructs a coupled finite system whose physical state q, resource
level r, and mutable interface bit i jointly determine admissible transitions.
It verifies that the coupled semantics is exactly reproduced by the ordinary
explicit product state (q,r,i). No novelty claim is attached to this fact.
"""
from itertools import product

Q = range(2)
R = range(3)
I = range(2)
ACTIONS = ("toggle", "act")
STATES = list(product(Q, R, I))


def endogenous_step(state, action):
    q, r, i = state
    if action == "toggle" and r >= 1:
        return (q, r - 1, 1 - i)
    if action == "act" and i == 1 and r >= 1:
        return (1 - q, r - 1, i)
    return None


def compiled_edges():
    return {
        (s, a, endogenous_step(s, a))
        for s in STATES
        for a in ACTIONS
        if endogenous_step(s, a) is not None
    }


def direct_edges():
    # Independent explicit enumeration of the product-state transition rules.
    out = set()
    for q, r, i in STATES:
        if r >= 1:
            out.add(((q, r, i), "toggle", (q, r - 1, 1 - i)))
        if r >= 1 and i == 1:
            out.add(((q, r, i), "act", (1 - q, r - 1, i)))
    return out


if __name__ == "__main__":
    e1 = compiled_edges()
    e2 = direct_edges()
    assert e1 == e2
    assert len(STATES) == 12
    assert len(e1) == 12
    print("PASS: coupled endogenous semantics equals explicit finite product semantics")
    print(f"states={len(STATES)} edges={len(e1)}")
