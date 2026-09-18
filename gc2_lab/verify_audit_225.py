"""Exact verifier for GC-II Audit 225 higher-order interaction boundary."""
from itertools import combinations

N = ("R", "I", "A", "L")
subsets = [frozenset(c) for r in range(len(N)+1) for c in combinations(N, r)]


def mobius(v, T):
    T = frozenset(T)
    total = 0
    elems = tuple(T)
    for r in range(len(elems)+1):
        for U in combinations(elems, r):
            total += (-1) ** (len(T)-r) * v[frozenset(U)]
    return total


def reconstruct(m, S):
    return sum(m[T] for T in subsets if T <= S)

# Ordinary finite capability sets. A has singleton-gated tasks only;
# B adds one task gated by conjunction R&I.
def caps_A(S):
    out = set()
    if "R" in S: out.add("q_R")
    if "I" in S: out.add("q_I")
    return out


def caps_B(S, k=1):
    out = caps_A(S)
    if {"R", "I"} <= set(S):
        out |= {f"q_RI_{j}" for j in range(k)}
    return out

vA = {S: len(caps_A(S)) for S in subsets}
vB = {S: len(caps_B(S)) for S in subsets}
mA = {T: mobius(vA, T) for T in subsets}
mB = {T: mobius(vB, T) for T in subsets}

assert vA[frozenset()] == vB[frozenset()] == 0
for i in N:
    assert vA[frozenset([i])] == vB[frozenset([i])]
assert vA[frozenset(["R", "I"])] == 2
assert vB[frozenset(["R", "I"])] == 3
assert mA[frozenset(["R", "I"])] == 0
assert mB[frozenset(["R", "I"])] == 1
for S in subsets:
    assert reconstruct(mA, S) == vA[S]
    assert reconstruct(mB, S) == vB[S]

# Arbitrarily large conjunction-only interaction while singleton responses stay fixed.
for k in range(0, 101):
    vk = {S: len(caps_B(S, k=k)) for S in subsets}
    assert vk[frozenset(["R"])] == 1
    assert vk[frozenset(["I"])] == 1
    assert mobius(vk, frozenset(["R", "I"])) == k

print("Audit 225 exact checks passed: Möbius inversion and k=0..100 conjunction gaps.")
