"""Exact finite audit for GC-II budgeted operational closure.

Standard-library only.  The test distinguishes naive base-state budgeted
reachability from the correct lifted cumulative-expenditure closure.
"""

from itertools import product, combinations


def base_reach(n, edges, starts, budget):
    """Base states reachable with total scalar path cost <= budget."""
    best = {s: 0 for s in starts}
    changed = True
    while changed:
        changed = False
        for u, v, c in edges:
            if u in best:
                nc = best[u] + c
                if nc <= budget and (v not in best or nc < best[v]):
                    best[v] = nc
                    changed = True
    return set(best)


def lifted_vertices(n, edges, budget):
    """All legal lifted vertices (state, cumulative_spend)."""
    return {(s, r) for s in range(n) for r in range(budget + 1)}


def lifted_closure(n, edges, seed_vertices, budget):
    """Reachability closure on the fixed lifted graph."""
    out = set(seed_vertices)
    changed = True
    while changed:
        changed = False
        for u, v, c in edges:
            for s, r in tuple(out):
                if s == u and r + c <= budget:
                    nxt = (v, r + c)
                    if nxt not in out:
                        out.add(nxt)
                        changed = True
    return out


def all_subsets(items):
    items = tuple(items)
    for mask in range(1 << len(items)):
        yield {items[i] for i in range(len(items)) if mask & (1 << i)}


def test_naive_base_state_idempotence_is_false():
    edges = [(0, 1, 1), (1, 2, 1)]
    first = base_reach(3, edges, {0}, 1)
    second = base_reach(3, edges, first, 1)
    assert first == {0, 1}
    assert second == {0, 1, 2}
    assert second != first


def test_exhaustive_three_state_worlds():
    n = 3
    directed_pairs = [(u, v) for u in range(n) for v in range(n) if u != v]
    world_count = 0
    lifted_checks = 0

    # Each directed non-loop edge: absent, cost 0, or cost 1.
    for coding in product((-1, 0, 1), repeat=len(directed_pairs)):
        edges = [
            (u, v, c)
            for (u, v), c in zip(directed_pairs, coding)
            if c >= 0
        ]
        world_count += 1

        for start in range(n):
            # Base reachability is extensive and monotone in budget.
            prev = set()
            for budget in (0, 1, 2):
                now = base_reach(n, edges, {start}, budget)
                assert start in now
                assert prev <= now
                prev = now

                seed = {(start, 0)}
                cl = lifted_closure(n, edges, seed, budget)
                assert seed <= cl
                assert lifted_closure(n, edges, cl, budget) == cl
                lifted_checks += 1

                # Monotonicity is checked over all subsets of the actually
                # reachable lifted closure. This is exhaustive for that set.
                subsets = list(all_subsets(cl))
                for x in subsets:
                    cx = lifted_closure(n, edges, x, budget)
                    assert x <= cx
                    assert lifted_closure(n, edges, cx, budget) == cx
                for i, x in enumerate(subsets):
                    cx = lifted_closure(n, edges, x, budget)
                    for y in subsets[i:]:
                        if x <= y:
                            cy = lifted_closure(n, edges, y, budget)
                            assert cx <= cy
                        if y <= x:
                            cy = lifted_closure(n, edges, y, budget)
                            assert cy <= cx

    assert world_count == 3 ** 6 == 729
    assert lifted_checks == 729 * 3 * 3


if __name__ == "__main__":
    test_naive_base_state_idempotence_is_false()
    test_exhaustive_three_state_worlds()
    print("GC-II budgeted closure audit: PASS")
    print("worlds: 729; singleton-start/budget cases: 6561")
