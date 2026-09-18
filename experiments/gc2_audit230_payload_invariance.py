#!/usr/bin/env python3
"""Exact finite checks for GC-II Audit 230."""

presentations = ["a0", "a1", "b0", "b1", "b2", "c0"]
q = {"a0": "A", "a1": "A", "b0": "B", "b1": "B", "b2": "B", "c0": "C"}

h1 = {"A": 0, "B": 1, "C": 2}
h2 = {"A": 2, "B": 1, "C": 0}

def lift(h):
    return {x: h[q[x]] for x in presentations}

def invariant(P):
    return all((q[x] != q[y]) or (P[x] == P[y])
               for x in presentations for y in presentations)

def factor(P):
    out = {}
    for x in presentations:
        cls = q[x]
        if cls in out:
            assert out[cls] == P[x]
        else:
            out[cls] = P[x]
    return out

P1, P2 = lift(h1), lift(h2)
assert invariant(P1) and invariant(P2)
assert factor(P1) == h1
assert factor(P2) == h2
assert P1["a0"] < P1["c0"]
assert P2["a0"] > P2["c0"]

# Exhaustively verify factorization for every {0,1}-valued invariant payload.
classes = sorted(set(q.values()))
count = 0
for mask in range(1 << len(classes)):
    h = {c: (mask >> i) & 1 for i, c in enumerate(classes)}
    P = lift(h)
    assert invariant(P)
    assert factor(P) == h
    count += 1

print({
    "presentations": len(presentations),
    "behavioral_classes": len(classes),
    "binary_invariant_payloads_checked": count,
    "ordering_reversal_verified": True,
    "factorization_verified": True,
})
