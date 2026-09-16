#!/usr/bin/env python3
"""Exact finite verifier for GC-II Audit 192.

Enumerates every monotone map F:2^E -> 2^X for |E|,|X|<=2, constructs
one typed witness per minimal enabler, and verifies exact reconstruction.
Typing is represented explicitly by witness input signatures (bitmasks of
primitive token types) and capability output types.
"""
from itertools import product


def subsets(n):
    return range(1 << n)


def subset(a, b):
    return (a & ~b) == 0


def monotone(table, ne):
    return all(not subset(a, b) or (table[a] & ~table[b]) == 0
               for a in subsets(ne) for b in subsets(ne))


def typed_witnesses(table, ne, nx):
    """Return (input_type_mask, output_capability) witnesses."""
    ws = []
    for x in range(nx):
        xb = 1 << x
        for s in subsets(ne):
            if not (table[s] & xb):
                continue
            if any(t != s and subset(t, s) and (table[t] & xb)
                   for t in subsets(ne)):
                continue
            ws.append((s, x))
    return ws


def closure(witnesses, acquired_mask):
    out = 0
    for input_types, x in witnesses:
        if subset(input_types, acquired_mask):
            out |= 1 << x
    return out


def verify(ne, nx):
    domain = 1 << ne
    codomain = 1 << nx
    monotone_count = checked = 0
    max_witnesses = 0
    for values in product(range(codomain), repeat=domain):
        table = dict(enumerate(values))
        if not monotone(table, ne):
            continue
        monotone_count += 1
        ws = typed_witnesses(table, ne, nx)
        max_witnesses = max(max_witnesses, len(ws))
        assert all(closure(ws, s) == table[s] for s in subsets(ne))
        checked += 1
    return monotone_count, checked, max_witnesses


if __name__ == "__main__":
    for ne in range(3):
        for nx in range(3):
            total, checked, maxw = verify(ne, nx)
            print(f"|E|={ne} |X|={nx}: exact {checked}/{total}; "
                  f"max typed witnesses={maxw}")
