#!/usr/bin/env python3
"""GC-II Audit 120: joint-closure geometry under monotone resource reparameterization.

Exhaustively enumerates all nonempty subsets of the 3x3 resource grid and all
coordinatewise strictly increasing relabelings of the three resource levels into
{0,1,2,3,4}. It verifies that product-order dominance and Pareto-front membership
are invariant, while Euclidean convex-hull area generally is not.
"""
from itertools import combinations
import json

GRID = [(i, j) for i in range(3) for j in range(3)]
LEVEL_MAPS = list(combinations(range(5), 3))


def dominates(a, b):
    return a[0] <= b[0] and a[1] <= b[1] and a != b


def pareto(points):
    return tuple(sorted(p for p in points if not any(dominates(q, p) for q in points)))


def hull_area(points):
    pts = sorted(set(points))
    if len(pts) < 3:
        return 0.0

    def cross(o, a, b):
        return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

    lower = []
    for p in pts:
        while len(lower) >= 2 and cross(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)
    upper = []
    for p in reversed(pts):
        while len(upper) >= 2 and cross(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)
    hull = lower[:-1] + upper[:-1]
    return abs(sum(
        hull[i][0] * hull[(i + 1) % len(hull)][1]
        - hull[(i + 1) % len(hull)][0] * hull[i][1]
        for i in range(len(hull))
    )) / 2.0


def run():
    cases = dominance_violations = pareto_violations = area_changed = 0
    witness = None

    for lx in LEVEL_MAPS:
        for ly in LEVEL_MAPS:
            mx = dict(enumerate(lx))
            my = dict(enumerate(ly))

            def transform(p):
                return (mx[p[0]], my[p[1]])

            for mask in range(1, 1 << len(GRID)):
                source = [GRID[k] for k in range(len(GRID)) if (mask >> k) & 1]
                target = [transform(p) for p in source]
                cases += 1

                if any(
                    dominates(source[a], source[b]) != dominates(target[a], target[b])
                    for a in range(len(source))
                    for b in range(len(source))
                    if a != b
                ):
                    dominance_violations += 1

                if {transform(p) for p in pareto(source)} != set(pareto(target)):
                    pareto_violations += 1

                area_source = hull_area(source)
                area_target = hull_area(target)
                if abs(area_source - area_target) > 1e-12:
                    area_changed += 1
                    if witness is None:
                        witness = {
                            "source": source,
                            "target": target,
                            "source_area": area_source,
                            "target_area": area_target,
                            "x_levels": lx,
                            "y_levels": ly,
                            "source_pareto": pareto(source),
                            "target_pareto": pareto(target),
                        }

    result = {
        "audit": 120,
        "grid_points": len(GRID),
        "nonempty_subsets_per_transform": (1 << len(GRID)) - 1,
        "strict_level_maps_per_coordinate": len(LEVEL_MAPS),
        "coordinate_transform_pairs": len(LEVEL_MAPS) ** 2,
        "cases": cases,
        "dominance_violations": dominance_violations,
        "pareto_violations": pareto_violations,
        "convex_hull_area_changed_cases": area_changed,
        "witness": witness,
    }
    print(json.dumps(result, indent=2))
    assert cases == 51100
    assert dominance_violations == 0
    assert pareto_violations == 0
    assert area_changed == 39846
    return result


if __name__ == "__main__":
    run()
