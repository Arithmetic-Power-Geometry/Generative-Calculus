"""Exact finite verifier for GC-II Audit 293. No floating point."""
from itertools import combinations

N = 3
Y = {(x, y) for x in range(N) for y in range(N)}
# (xmin, xmax, ymin, ymax)
RECTS = [
    (2, 2, 0, 2),
    (1, 1, 0, 2),
    (0, 0, 0, 2),
    (2, 2, 1, 2),
    (1, 2, 0, 1),
    (1, 2, 1, 1),
    (0, 2, 0, 0),
]


def points(r):
    x0, x1, y0, y1 = r
    return {(x, y) for x, y in Y if x0 <= x <= x1 and y0 <= y <= y1}


def exact_cover_number(targets, rects):
    if not targets:
        return 0
    sets = [points(r) & targets for r in rects]
    for k in range(1, len(sets) + 1):
        for ids in combinations(range(len(sets)), k):
            if set().union(*(sets[i] for i in ids)) >= targets:
                return k
    return None


def naive_product_greedy(targets, rects):
    """Lexicographic first uncovered; maximize newly covered points."""
    remaining = set(targets)
    used = []
    while remaining:
        p = min(remaining)
        candidates = [r for r in rects if p in points(r)]
        if not candidates:
            return None
        # deterministic tie break by rectangle tuple
        chosen = max(candidates, key=lambda r: (len(points(r) & remaining), r))
        used.append(chosen)
        remaining -= points(chosen)
    return used


def verify():
    # Every action is exactly a product of two discrete intervals.
    for r in RECTS:
        x0, x1, y0, y1 = r
        expected = {(x, y) for x in range(x0, x1 + 1) for y in range(y0, y1 + 1)}
        assert points(r) == expected

    optimum = exact_cover_number(Y, RECTS)
    greedy = naive_product_greedy(Y, RECTS)
    assert optimum == 3
    assert greedy is not None and len(greedy) == 5

    # Degenerate boundaries.
    assert exact_cover_number(set(), RECTS) == 0
    assert exact_cover_number(Y, [(0, 2, 0, 2)]) == 1
    assert exact_cover_number(Y, [(0, 0, 0, 2)]) is None

    print({
        "status": "PASS",
        "grid_targets": len(Y),
        "rectangular_actions": len(RECTS),
        "exact_optimum": optimum,
        "naive_product_greedy": len(greedy),
        "greedy_gap": len(greedy) - optimum,
        "structure": "product of two intervals",
    })


if __name__ == "__main__":
    verify()
