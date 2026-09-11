#!/usr/bin/env python3
"""Exact exhaustive audit for GC-II finite edge-potential integrability.

Enumerates all labelings of complete bidirected graphs on n=2,3,4 with
edge labels in {-1,0,1}. A labeling is integrable iff there exists Phi with
w(u,v)=Phi(v)-Phi(u) on every directed edge.
"""
from itertools import product
import csv
from pathlib import Path

VALUES = (-1, 0, 1)
OUT = Path("results/gc2_integrability_exhaustive.csv")


def audit_n(n: int):
    edges = [(i, j) for i in range(n) for j in range(n) if i != j]
    total = 0
    integrable = 0
    defect_hist = {}

    for labels in product(VALUES, repeat=len(edges)):
        total += 1
        w = dict(zip(edges, labels))
        # Fix gauge Phi(0)=0. Edges 0->j determine every other potential.
        phi = [0] + [w[(0, j)] for j in range(1, n)]
        defects = [w[(i, j)] - (phi[j] - phi[i]) for i, j in edges]
        max_abs_defect = max(abs(d) for d in defects)
        defect_hist[max_abs_defect] = defect_hist.get(max_abs_defect, 0) + 1
        if max_abs_defect == 0:
            integrable += 1

    return {
        "n": n,
        "directed_edges": len(edges),
        "assignments_checked": total,
        "integrable_assignments": integrable,
        "nonintegrable_assignments": total - integrable,
        "defect_histogram": ";".join(f"{k}:{defect_hist[k]}" for k in sorted(defect_hist)),
    }


def main():
    rows = [audit_n(n) for n in (2, 3, 4)]
    OUT.parent.mkdir(parents=True, exist_ok=True)
    with OUT.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)

    for row in rows:
        print(row)


if __name__ == "__main__":
    main()
