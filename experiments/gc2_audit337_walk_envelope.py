#!/usr/bin/env python3
"""Exact finite verification for GC-II Audit 337.

Exhausts all 2^(3*3)=512 directed macro-transition relations on three
labelled operational classes and horizons h=0..4.  Uses integer arithmetic.
"""
import json
from pathlib import Path

Q = 3
HMAX = 4


def adjacency(mask):
    a = [set() for _ in range(Q)]
    for i in range(Q):
        for j in range(Q):
            if (mask >> (i * Q + j)) & 1:
                a[i].add(j)
    return a


def distinct_reachable(a, h):
    total = 0
    for s in range(Q):
        frontier = {s}
        seen = set()
        for _ in range(h):
            nxt = set()
            for u in frontier:
                nxt.update(a[u])
            seen.update(nxt - {s})
            frontier = nxt
        total += len(seen)
    return total


def walk_envelope(a, h):
    total = 0
    for s in range(Q):
        v = [0] * Q
        v[s] = 1
        walks = 0
        for _ in range(h):
            nv = [0] * Q
            for u, multiplicity in enumerate(v):
                if multiplicity:
                    for z in a[u]:
                        nv[z] += multiplicity
            walks += sum(nv)
            v = nv
        total += min(Q - 1, walks)
    return total


def audit336_envelope(a, h):
    if h == 0:
        return 0
    beta = max(len(row) for row in a)
    geometric = sum(beta ** ell for ell in range(1, h + 1))
    return Q * min(Q - 1, geometric)


def main():
    cases = equality = failures = strict_improvements = 0
    for mask in range(1 << (Q * Q)):
        a = adjacency(mask)
        for h in range(HMAX + 1):
            omega = distinct_reachable(a, h)
            walk = walk_envelope(a, h)
            old = audit336_envelope(a, h)
            cases += 1
            if omega > walk:
                failures += 1
            if omega == walk:
                equality += 1
            if walk < old:
                strict_improvements += 1
    result = {
        "audit": 337,
        "q_exhaustive": Q,
        "relations": 1 << (Q * Q),
        "horizons": list(range(HMAX + 1)),
        "cases_checked": cases,
        "equality_cases": equality,
        "failures": failures,
        "strict_improvements_over_audit336": strict_improvements,
    }
    out = Path("results/gc2_audit337_walk_envelope.json")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))
    if failures:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
