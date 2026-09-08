"""Exact finite audit for GC-II budgeted operational closure.

Standard-library only. Distinguishes naive base-state budgeted reachability
from the correct lifted cumulative-expenditure closure.
"""

from itertools import product


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


def lifted_closure(n, edges, seed_vertices, budget):
    """Reachability closure on the fixed lifted graph."""
    out = set(seed_vertices)
    changed = True
    while changed:
        changed = False
        snapshot = tuple(out)
        for u, v, c in edges:
            for s, r in snapshot:
                if s == u and r + c <= budget:
                    nxt = (v, r + c)
                    if nxt not in out:
                        out.add(nxt)
                        changed = True
    return out


def base_start_subsets(n):
    """All subsets of base states, represented at zero expenditure."""
    for mask in range(1 << n):
        yield {s for s in range(n) if mask & (1 << s)}


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
    singleton_budget_checks = 0
    subset_monotonicity_checks = 0

    # Each directed non-loop edge: absent, cost 0, or cost 1.
    for coding in product((-1, 0, 1), repeat=len(directed_pairs)):
        edges = [
            (u, v, c)
            for (u, v), c in zip(directed_pairs, coding)
            if c >= 0
        ]
        world_count += 1

        # Base reachability: extensivity and monotonicity in budget.
        for start in range(n):
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
                singleton_budget_checks += 1

        # Lifted closure monotonicity is checked exhaustively for all 8
        # zero-expenditure start subsets and every inclusion pair, at each B.
        starts = list(base_start_subsets(n))
        for budget in (0, 1, 2):
            closures = {
                frozenset(x): lifted_closure(n, edges, {(s, 0) for s in x}, budget)
                for x in starts
            }
            for x in starts:
                cx = closures[frozenset(x)]
                seed_x = {(s, 0) for s in x}
                assert seed_x <= cx
                assert lifted_closure(n, edges, cx, budget) == cx
                for y in starts:
                    if x <= y:
                        assert cx <= closures[frozenset(y)]
                        subset_monotonicity_checks += 1

    assert world_count == 3 ** 6 == 729
    assert singleton_budget_checks == 729 * 3 * 3 == 6561
    # Number is intentionally not hard-coded because it is a derived audit
    # count; positivity ensures this block actually executed.
    assert subset_monotonicity_checks > 0


if __name__ == "__main__":
    test_naive_base_state_idempotence_is_false()
    test_exhaustive_three_state_worlds()
    print("GC-II budgeted closure audit: PASS")
    print("worlds: 729; singleton-start/budget cases: 6561")
