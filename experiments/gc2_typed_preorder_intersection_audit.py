"""GC-II Audit 134: exact finite check for typed-preorder intersection closure.

Enumerates all transformation monoids on a two-state space and verifies that
all ordered pair and triple intersections are again transformation monoids.
The finite check is a regression witness for the general intersection theorem.
"""
from itertools import product
import json

X = (0, 1)
MAPS = list(product(X, repeat=2))
IDENTITY = (0, 1)


def compose(f, g):
    """Return f after g."""
    return tuple(f[g[x]] for x in X)


def is_transformation_monoid(family):
    family = set(family)
    return IDENTITY in family and all(
        compose(f, g) in family for f in family for g in family
    )


monoids = []
for mask in range(1 << len(MAPS)):
    family = {MAPS[i] for i in range(len(MAPS)) if (mask >> i) & 1}
    if is_transformation_monoid(family):
        monoids.append(family)

pair_checks = 0
triple_checks = 0
failures = 0
distinct_intersections = set()

for a in monoids:
    for b in monoids:
        joint = frozenset(a & b)
        pair_checks += 1
        distinct_intersections.add(joint)
        failures += int(not is_transformation_monoid(joint))

for a in monoids:
    for b in monoids:
        for c in monoids:
            joint = frozenset(a & b & c)
            triple_checks += 1
            distinct_intersections.add(joint)
            failures += int(not is_transformation_monoid(joint))

result = {
    "audit": 134,
    "states": len(X),
    "deterministic_maps": len(MAPS),
    "transformation_monoids": len(monoids),
    "monoid_sizes": sorted(len(m) for m in monoids),
    "ordered_pair_intersections_checked": pair_checks,
    "ordered_triple_intersections_checked": triple_checks,
    "distinct_intersection_monoids_seen": len(distinct_intersections),
    "intersection_closure_failures": failures,
}

assert len(monoids) == 6
assert pair_checks == 36
assert triple_checks == 216
assert failures == 0
print(json.dumps(result, indent=2, sort_keys=True))
