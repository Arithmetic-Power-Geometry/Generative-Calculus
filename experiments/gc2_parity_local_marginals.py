"""Exact finite check for GC-II Audit 076.

Enumerate even/odd parity distributions and verify that every proper
coordinate marginal is identical. Uses exact rational arithmetic.
"""
from fractions import Fraction
from itertools import combinations, product
from pathlib import Path
import csv


def parity_distribution(n: int, parity: int):
    states = [x for x in product((0, 1), repeat=n) if sum(x) % 2 == parity]
    w = Fraction(1, len(states))
    return {x: w for x in states}


def marginal(dist, indices):
    out = {}
    for x, w in dist.items():
        key = tuple(x[i] for i in indices)
        out[key] = out.get(key, Fraction(0, 1)) + w
    return out


def max_abs_difference(a, b):
    keys = set(a) | set(b)
    return max((abs(a.get(k, 0) - b.get(k, 0)) for k in keys), default=Fraction(0, 1))


def run(n_min=2, n_max=8):
    rows = []
    for n in range(n_min, n_max + 1):
        even = parity_distribution(n, 0)
        odd = parity_distribution(n, 1)
        for k in range(1, n):
            worst = Fraction(0, 1)
            for inds in combinations(range(n), k):
                worst = max(worst, max_abs_difference(marginal(even, inds), marginal(odd, inds)))
            rows.append((n, k, worst))
            assert worst == 0, (n, k, worst)
    return rows


if __name__ == "__main__":
    rows = run()
    out = Path(__file__).resolve().parents[1] / "results" / "gc2_parity_local_marginals.csv"
    out.parent.mkdir(parents=True, exist_ok=True)
    with out.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["n", "k", "max_abs_marginal_difference"])
        for n, k, d in rows:
            writer.writerow([n, k, f"{float(d):.1f}"])
    print(f"verified {len(rows)} (n,k) cases; all proper-marginal differences are exactly zero")
