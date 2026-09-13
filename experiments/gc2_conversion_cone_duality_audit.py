#!/usr/bin/env python3
"""GC-II Audit 121: exact finite test of conversion-cone / dual-monotone equivalence.

For every primitive integer generator pair u,v in [-3,3]^2 with det(u,v)>0,
and every integer test point x in [-5,5]^2, compare:

  primal membership: x in cone(u,v)
  dual test:         n_u·x >= 0 and n_v·x >= 0

where n_u=(-u_y,u_x) and n_v=(v_y,-v_x) are the two extreme rays of the
dual cone in the 2D pointed-polyhedral case.

No floating-point arithmetic or external solver is used.
"""

from itertools import product
from math import gcd
import json
from pathlib import Path


def det(a, b):
    return a[0] * b[1] - a[1] * b[0]


def dot(a, b):
    return a[0] * b[0] + a[1] * b[1]


def primitive_vectors(bound=3):
    out = []
    for x, y in product(range(-bound, bound + 1), repeat=2):
        if (x, y) == (0, 0):
            continue
        if gcd(abs(x), abs(y)) == 1:
            out.append((x, y))
    return out


def main():
    vecs = primitive_vectors(3)
    cones = [(u, v) for u in vecs for v in vecs if det(u, v) > 0]
    points = list(product(range(-5, 6), repeat=2))

    mismatches = []
    boundary = interior = outside = 0
    cases = 0

    for u, v in cones:
        n_u = (-u[1], u[0])
        n_v = (v[1], -v[0])
        for x in points:
            primal = det(u, x) >= 0 and det(x, v) >= 0
            dual = dot(n_u, x) >= 0 and dot(n_v, x) >= 0
            cases += 1
            if primal:
                if det(u, x) == 0 or det(x, v) == 0:
                    boundary += 1
                else:
                    interior += 1
            else:
                outside += 1
            if primal != dual:
                mismatches.append({
                    "u": u,
                    "v": v,
                    "x": x,
                    "dual_extremes": [n_u, n_v],
                    "primal": primal,
                    "dual": dual,
                })

    result = {
        "audit": 121,
        "generator_coordinate_bound": 3,
        "test_point_coordinate_bound": 5,
        "primitive_vectors": len(vecs),
        "pointed_2d_cones": len(cones),
        "test_points_per_cone": len(points),
        "total_membership_cases": cases,
        "interior_cases": interior,
        "boundary_cases": boundary,
        "outside_cases": outside,
        "primal_dual_mismatches": len(mismatches),
        "first_mismatches": mismatches[:10],
        "arithmetic": "exact_integer",
        "claim_scope": "2D pointed polyhedral cones; computational regression only",
    }

    out = Path("gc2/results/AUDIT_121_conversion_cone_duality.json")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))

    if mismatches:
        raise SystemExit("FAIL: primal/dual equivalence mismatch detected")


if __name__ == "__main__":
    main()
