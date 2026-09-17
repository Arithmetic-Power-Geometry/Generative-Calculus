"""Exact verifier for GC-II Audit 204.

Enumerates every set partition of N={R,I,A,L}. For representative Boolean
capability functions it computes the Mobius coefficients induced on unions of
partition blocks and the absolute mass of coefficients involving >=2 blocks.
The one-block coarsening must make this mass exactly zero.
"""
from fractions import Fraction
from itertools import combinations

N = tuple("RIAL")


def partitions(items):
    if not items:
        yield ()
        return
    first, rest = items[0], items[1:]
    for p in partitions(rest):
        yield (frozenset([first]),) + p
        for i in range(len(p)):
            yield p[:i] + (p[i] | {first},) + p[i+1:]


def canonical(p):
    return tuple(sorted((tuple(sorted(b)) for b in p)))


def all_partitions(items):
    seen = set()
    for p in partitions(items):
        c = canonical(p)
        if c not in seen:
            seen.add(c)
            yield tuple(frozenset(b) for b in c)


def subsets(seq):
    for r in range(len(seq)+1):
        for c in combinations(range(len(seq)), r):
            yield frozenset(c)


def mobius_on_partition(v, p):
    idx = tuple(range(len(p)))
    vals = {}
    for S in subsets(idx):
        union = frozenset().union(*(p[i] for i in S)) if S else frozenset()
        vals[S] = Fraction(v(union))
    m = {}
    for T in subsets(idx):
        total = Fraction(0)
        for S in subsets(tuple(T)):
            total += (-1) ** (len(T)-len(S)) * vals[S]
        m[T] = total
    return m


def interaction_mass(v, p):
    m = mobius_on_partition(v, p)
    return sum((abs(x) for T, x in m.items() if len(T) >= 2), Fraction(0))


functions = {
    "four_way_and": lambda S: int(set(N).issubset(S)),
    "or": lambda S: int(bool(S)),
    "RI_and": lambda S: int({"R", "I"}.issubset(S)),
    "parity": lambda S: len(S) % 2,
    "constant": lambda S: 1,
}

ps = list(all_partitions(N))
assert len(ps) == 15  # Bell number B_4
one_block = [p for p in ps if len(p) == 1]
assert len(one_block) == 1

for name, v in functions.items():
    masses = [(interaction_mass(v, p), p) for p in ps]
    minimum = min(x for x, _ in masses)
    top_mass = interaction_mass(v, one_block[0])
    assert top_mass == 0
    assert minimum == 0
    print(name, "fine=", interaction_mass(v, tuple(frozenset([x]) for x in N)),
          "one_block=", top_mass, "minimum=", minimum)

print("PASS: unrestricted semantics-preserving coarsening trivializes higher-order interaction mass.")
