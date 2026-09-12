#!/usr/bin/env python3
"""Exact finite audit for persistent same-instance local access to parity.

For each n and each observed coordinate subset S, every transcript on |S|<n
has completions of both parities. At |S|=n, parity is determined exactly.
The script emits a compact exact count table; it does not establish novelty.
"""
from __future__ import annotations

import csv
from itertools import combinations, product
from pathlib import Path

OUT = Path("results/gc2_persistent_parity_query_audit.csv")


def parity(bits):
    return sum(bits) & 1


def audit(n: int, k: int):
    ambiguous = 0
    decisive = 0
    total = 0
    for S in combinations(range(n), k):
        for transcript in product((0, 1), repeat=k):
            total += 1
            seen = set()
            free = [i for i in range(n) if i not in S]
            for completion in product((0, 1), repeat=len(free)):
                x = [0] * n
                for i, b in zip(S, transcript):
                    x[i] = b
                for i, b in zip(free, completion):
                    x[i] = b
                seen.add(parity(x))
            if len(seen) == 2:
                ambiguous += 1
            elif len(seen) == 1:
                decisive += 1
            else:
                raise AssertionError("empty completion set")
    return total, ambiguous, decisive


def main():
    OUT.parent.mkdir(parents=True, exist_ok=True)
    rows = []
    # Exhaustive completion enumeration through n=10 is small enough for CI-style use.
    for n in range(2, 11):
        for k in range(0, n + 1):
            total, ambiguous, decisive = audit(n, k)
            expected_ambiguous = total if k < n else 0
            expected_decisive = total if k == n else 0
            if ambiguous != expected_ambiguous or decisive != expected_decisive:
                raise AssertionError((n, k, total, ambiguous, decisive))
            rows.append(
                {
                    "n": n,
                    "k": k,
                    "transcripts": total,
                    "ambiguous_transcripts": ambiguous,
                    "decisive_transcripts": decisive,
                }
            )
    with OUT.open("w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=rows[0].keys())
        w.writeheader()
        w.writerows(rows)
    print(f"wrote {len(rows)} exact cases to {OUT}")


if __name__ == "__main__":
    main()
