"""GC-II Audit 322: exact non-hereditary admissibility counterexample.

Three decision-critical worlds 0,1,2. At the root all singleton tests are
admissible. On every unresolved proper cell no test is admissible. Thus every
pair has a finite root witness, but no adaptive policy resolves all worlds.
"""
from functools import lru_cache
from math import inf

WORLDS = frozenset(range(3))
TESTS = tuple(range(3))  # u_i(x)=1 iff x=i
COST = {u: 1 for u in TESTS}


def outcome(u, x):
    return int(x == u)


def admissible(cell):
    # Explicit cell-relative, non-hereditary authorization rule.
    return TESTS if cell == WORLDS else ()


def pairwise_root_bound():
    vals = []
    for x in WORLDS:
        for y in WORLDS:
            if x < y:
                sep = [COST[u] for u in admissible(WORLDS)
                       if outcome(u, x) != outcome(u, y)]
                vals.append(min(sep) if sep else inf)
    return max(vals)


@lru_cache(None)
def V(cell_tuple):
    cell = frozenset(cell_tuple)
    if len(cell) <= 1:
        return 0
    best = inf
    for u in admissible(cell):
        children = []
        for z in (0, 1):
            child = frozenset(x for x in cell if outcome(u, x) == z)
            if child:
                children.append(child)
        if len(children) <= 1:
            continue
        tail = max(V(tuple(sorted(c))) for c in children)
        best = min(best, COST[u] + tail)
    return best


def main():
    P = pairwise_root_bound()
    joint = V(tuple(sorted(WORLDS)))
    assert P == 1
    assert joint == inf
    # Every possible first test has a singleton solved branch and an unresolved
    # two-world branch with no admissible continuation.
    for u in TESTS:
        neg = frozenset(x for x in WORLDS if outcome(u, x) == 0)
        pos = frozenset(x for x in WORLDS if outcome(u, x) == 1)
        assert len(pos) == 1 and len(neg) == 2
        assert admissible(neg) == ()
        assert V(tuple(sorted(neg))) == inf
    print({"K": 3, "P_root": P, "V_joint": "infinity",
           "all_first_moves_deadlock": True})


if __name__ == "__main__":
    main()
