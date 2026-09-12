"""Exact Audit 097 checker: even/odd realization sets have identical proper projections."""
from itertools import product, combinations
import csv
from pathlib import Path


def project(rel, coords):
    return {tuple(x[i] for i in coords) for x in rel}


def run(n_min=3, n_max=7):
    rows = []
    for n in range(n_min, n_max + 1):
        cube = list(product((0, 1), repeat=n))
        even = {x for x in cube if sum(x) % 2 == 0}
        odd = set(cube) - even
        checked = 0
        mismatches = 0
        for r in range(n):
            for coords in combinations(range(n), r):
                checked += 1
                if project(even, coords) != project(odd, coords):
                    mismatches += 1
        rows.append({
            "n": n,
            "even_size": len(even),
            "odd_size": len(odd),
            "proper_projection_subsets_checked": checked,
            "projection_mismatches": mismatches,
            "global_sets_equal": even == odd,
            "global_intersection_size": len(even & odd),
        })
    return rows


if __name__ == "__main__":
    rows = run()
    out = Path("results/gc2_proper_projection_parity_audit.csv")
    out.parent.mkdir(parents=True, exist_ok=True)
    with out.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)
    for row in rows:
        print(row)
    assert all(r["projection_mismatches"] == 0 for r in rows)
    assert all(not r["global_sets_equal"] for r in rows)
    assert all(r["global_intersection_size"] == 0 for r in rows)
