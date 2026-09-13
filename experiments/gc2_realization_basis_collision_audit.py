"""Audit 115: exact finite collision test for realization-cost invariance.

Enumerates all 16 Boolean functions of two variables and computes exact minimum
expression-tree gate cost under two complete bases. Inputs and constants are free.
This is deliberately tiny enough for exhaustive fixed-point verification.
"""
import json
from pathlib import Path

MASK = 0b1111
X, Y, ZERO, ONE = 0b1100, 0b1010, 0, MASK


def unary_not(a):
    return (~a) & MASK


def binary(a, b, op):
    if op == "and": return a & b
    if op == "or": return a | b
    if op == "nand": return (~(a & b)) & MASK
    raise ValueError(op)


def exact_min_cost(ops):
    d = {X: 0, Y: 0, ZERO: 0, ONE: 0}
    changed = True
    while changed:
        changed = False
        items = list(d.items())
        if "not" in ops:
            for a, ca in items:
                z, nc = unary_not(a), ca + 1
                if nc < d.get(z, 10**9):
                    d[z] = nc; changed = True
        for op in ("and", "or", "nand"):
            if op not in ops: continue
            items = list(d.items())
            for a, ca in items:
                for b, cb in items:
                    z, nc = binary(a, b, op), ca + cb + 1
                    if nc < d.get(z, 10**9):
                        d[z] = nc; changed = True
    assert len(d) == 16
    return d


def main():
    aon = exact_min_cost({"and", "or", "not"})
    nand = exact_min_cost({"nand"})
    rows = [{"truth_table": f"{f:04b}", "AON_cost": aon[f], "NAND_cost": nand[f],
             "equal": aon[f] == nand[f]} for f in range(16)]
    out = {
        "functions": 16,
        "different_min_costs": sum(not r["equal"] for r in rows),
        "max_AON_cost": max(aon.values()),
        "max_NAND_cost": max(nand.values()),
        "rows": rows,
        "interpretation": "Semantic function is fixed, but exact minimum realization cost depends on the admissible primitive basis/cost model."
    }
    p = Path("results/gc2_realization_basis_collision_audit.json")
    p.parent.mkdir(exist_ok=True)
    p.write_text(json.dumps(out, indent=2) + "\n")
    print(json.dumps(out, indent=2))

if __name__ == "__main__":
    main()
