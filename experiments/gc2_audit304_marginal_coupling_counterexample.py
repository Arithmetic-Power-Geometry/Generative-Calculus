"""Exact finite collision test for GC-II Audit 304.

Enumerates nonempty supports on two binary coordinates, groups them by exact
one-coordinate marginals, and finds equal-marginal pairs with different value
for the independently fixed equality task u(r,i)=1[r=i].
"""
from fractions import Fraction
from itertools import combinations

PTS = ((0, 0), (0, 1), (1, 0), (1, 1))


def supports():
    for mask in range(1, 1 << len(PTS)):
        yield tuple(PTS[j] for j in range(len(PTS)) if mask & (1 << j))


def marginals(s):
    n = len(s)
    r1 = Fraction(sum(r for r, _ in s), n)
    i1 = Fraction(sum(i for _, i in s), n)
    return r1, i1


def equality_value(s):
    # Operational reachable-set value: best equality-task capability in support.
    return max(int(r == i) for r, i in s)


def expectation_value(s):
    # Also record uniform-support expected value as a secondary collision check.
    return Fraction(sum(int(r == i) for r, i in s), len(s))


all_s = list(supports())
groups = {}
for s in all_s:
    groups.setdefault(marginals(s), []).append(s)

reach_collisions = []
expectation_collisions = []
for m, group in groups.items():
    for a, b in combinations(group, 2):
        if equality_value(a) != equality_value(b):
            reach_collisions.append((m, a, b, equality_value(a), equality_value(b)))
        if expectation_value(a) != expectation_value(b):
            expectation_collisions.append((m, a, b, expectation_value(a), expectation_value(b)))

C0 = ((0, 1), (1, 0))
C1 = ((0, 0), (1, 1))
assert marginals(C0) == marginals(C1) == (Fraction(1, 2), Fraction(1, 2))
assert equality_value(C0) == 0
assert equality_value(C1) == 1
assert expectation_value(C0) == 0
assert expectation_value(C1) == 1
assert reach_collisions
assert expectation_collisions

print({
    "supports": len(all_s),
    "marginal_groups": len(groups),
    "reachable_value_collisions": len(reach_collisions),
    "expectation_value_collisions": len(expectation_collisions),
    "explicit_witness": {
        "baseline": C0,
        "augmented": C1,
        "marginals": tuple(str(x) for x in marginals(C0)),
        "baseline_equality_value": equality_value(C0),
        "augmented_equality_value": equality_value(C1),
    },
})
