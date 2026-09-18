#!/usr/bin/env python3
"""Audit 228: minimal enabling certificates bound interaction degree, but generically.

For a monotone capability indicator f:2^N->{0,1}, let M be its antichain of
minimal enabling sets. Then f(S)=1 iff some E in M satisfies E subseteq S.
Consequently f depends only on U=union(M), so every Mobius coefficient indexed
by T not subseteq U vanishes and deg_M(f) <= |U| <= sum_E |E| <= p*r when
there are p minimal enablers of size at most r.

This is a Boolean/hypergraph certificate fact, not GC-specific. The bound is
tight: p singleton minimal enablers give OR_p and degree p (=p*r for r=1).
"""
from itertools import combinations


def subsets(n):
    base = tuple(range(n))
    for r in range(n + 1):
        for c in combinations(base, r):
            yield frozenset(c)


def mobius(values, T):
    items = tuple(T)
    return sum(
        (-1) ** (len(T) - len(U)) * values[U]
        for r in range(len(items) + 1)
        for U in map(frozenset, combinations(items, r))
    )


def capability(S, minimal_enablers):
    return int(any(E <= S for E in minimal_enablers))


def audit_family(n, minimal_enablers):
    ss = list(subsets(n))
    # Require an antichain: these are genuinely minimal certificates.
    assert all(not (E < F) for E in minimal_enablers for F in minimal_enablers)
    values = {S: capability(S, minimal_enablers) for S in ss}
    coeff = {T: mobius(values, T) for T in ss}
    U = frozenset().union(*minimal_enablers) if minimal_enablers else frozenset()
    for T, c in coeff.items():
        if not T <= U:
            assert c == 0
    degree = max((len(T) for T, c in coeff.items() if c), default=0)
    assert degree <= len(U)
    p = len(minimal_enablers)
    r = max((len(E) for E in minimal_enablers), default=0)
    assert len(U) <= sum(map(len, minimal_enablers)) <= p * r
    return degree, len(U), p, r


def main():
    checked = 0
    # Exhaust all antichains of nonempty subsets for n<=4.
    for n in range(1, 5):
        nonempty = [S for S in subsets(n) if S]
        for mask in range(1 << len(nonempty)):
            fam = [nonempty[i] for i in range(len(nonempty)) if mask >> i & 1]
            if any(E < F for E in fam for F in fam):
                continue
            degree, u, p, r = audit_family(n, fam)
            assert degree <= u <= p * r
            checked += 1

    # Tight family: p singleton enablers => OR_p, degree p = p*r.
    for p in range(1, 13):
        fam = [frozenset([i]) for i in range(p)]
        degree, u, q, r = audit_family(p, fam)
        assert (degree, u, q, r) == (p, p, p, 1)

    print(f"PASS: exhaustive antichain families n=1..4 checked={checked}")
    print("PASS: deg_M(f) <= |union minimal enablers| <= p*r")
    print("PASS: singleton-enabler OR_p family makes bound tight for r=1")
    print("BOUNDARY: certificate bound is generic monotone Boolean/hypergraph structure")


if __name__ == "__main__":
    main()
