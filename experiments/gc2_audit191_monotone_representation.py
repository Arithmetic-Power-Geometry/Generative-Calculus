#!/usr/bin/env python3
"""Exact finite checks for GC-II Audit 191.

Enumerates every monotone set-valued map F:2^E -> 2^X for |E|<=2, |X|<=2
and verifies that the minimal-enabler operational construction reproduces F
exactly. No randomness or floating point is used.
"""
from itertools import product


def subsets(n):
    return tuple(range(1 << n))


def is_subset(a, b):
    return (a & ~b) == 0


def monotone(table, ne):
    ss = subsets(ne)
    return all(not is_subset(a, b) or (table[a] & ~table[b]) == 0
               for a in ss for b in ss)


def minimal_enablers(table, ne, nx):
    out = {x: [] for x in range(nx)}
    for x in range(nx):
        bit = 1 << x
        for s in subsets(ne):
            if not (table[s] & bit):
                continue
            if all(not (is_subset(t, s) and t != s and (table[t] & bit))
                   for t in subsets(ne)):
                out[x].append(s)
    return out


def reconstructed(enablers, s, nx):
    mask = 0
    for x in range(nx):
        if any(is_subset(t, s) for t in enablers[x]):
            mask |= 1 << x
    return mask


def check(ne, nx):
    domain = 1 << ne
    codomain = 1 << nx
    total = good = 0
    for vals in product(range(codomain), repeat=domain):
        table = dict(enumerate(vals))
        if not monotone(table, ne):
            continue
        total += 1
        en = minimal_enablers(table, ne, nx)
        assert all(reconstructed(en, s, nx) == table[s] for s in subsets(ne))
        good += 1
    return total, good


if __name__ == "__main__":
    for ne in range(3):
        for nx in range(3):
            total, good = check(ne, nx)
            print(f"|E|={ne} |X|={nx}: verified {good}/{total} monotone maps")
