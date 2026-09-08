"""Deterministic GC-II finite audit.

Tests only mathematically explicit finite constructions.  No novelty claim is implied.
"""
from itertools import product, combinations
import heapq
import math
import random

SEED = 20260908


def parity_relation(m, parity):
    return {x for x in product((0, 1), repeat=m) if sum(x) % 2 == parity}


def projection(relation, coordinates):
    coordinates = tuple(coordinates)
    return {tuple(x[i] for i in coordinates) for x in relation}


def parity_projection_audit(m):
    even = parity_relation(m, 0)
    odd = parity_relation(m, 1)
    for k in range(1, m):
        for S in combinations(range(m), k):
            assert projection(even, S) == projection(odd, S)

    reconstructed = set()
    for x in product((0, 1), repeat=m):
        if all(
            tuple(x[i] for i in S) in projection(even, S)
            for S in combinations(range(m), m - 1)
        ):
            reconstructed.add(x)
    assert reconstructed == set(product((0, 1), repeat=m))
    assert even != odd
    return {
        "m": m,
        "relation_size": len(even),
        "reconstruction_size": len(reconstructed),
        "binary_xor_tree_depth": math.ceil(math.log2(m)),
        "binary_xor_gate_count": m - 1,
    }


def dijkstra(n, adjacency, source):
    dist = [math.inf] * n
    dist[source] = 0
    queue = [(0, source)]
    while queue:
        d, u = heapq.heappop(queue)
        if d != dist[u]:
            continue
        for v, w in adjacency[u]:
            nd = d + w
            if nd < dist[v]:
                dist[v] = nd
                heapq.heappush(queue, (nd, v))
    return dist


def reachable_transport_audit(trials=20_000):
    rng = random.Random(SEED)
    checked_memberships = 0
    reachable_pairs = 0
    for _ in range(trials):
        n = rng.randint(3, 8)
        adjacency = [[] for _ in range(n)]
        for u in range(n):
            for v in range(n):
                if u != v and rng.random() < 0.30:
                    adjacency[u].append((v, rng.randint(0, 9)))
        x, y = rng.sample(range(n), 2)
        dx = dijkstra(n, adjacency, x)
        if math.isinf(dx[y]):
            continue
        reachable_pairs += 1
        c_xy = dx[y]
        dy = dijkstra(n, adjacency, y)
        B = rng.randint(0, 20)
        R_y = {t for t, d in enumerate(dy) if d <= B}
        R_x_shifted = {t for t, d in enumerate(dx) if d <= B + c_xy}
        assert R_y <= R_x_shifted
        checked_memberships += len(R_y)
    return reachable_pairs, checked_memberships


def subadditivity_counterexample():
    """Shows why a composition-cost assumption is essential.

    If x->y costs 1 and y->t costs 1 but the allowed composed realization x->t
    is charged 3 (superadditive), then t is in R_y(1) but not R_x(2).
    """
    c_xy = 1
    c_yt = 1
    composed_cost_x_t = 3
    B = 1
    assert c_yt <= B
    assert composed_cost_x_t > B + c_xy
    return True


def main():
    rows = [parity_projection_audit(m) for m in range(2, 11)]
    pairs, memberships = reachable_transport_audit()
    subadditivity_counterexample()
    print("PARITY_ROWS", rows)
    print("TRANSPORT_REACHABLE_PAIRS", pairs)
    print("TRANSPORT_MEMBERSHIPS_CHECKED", memberships)
    print("SUBADDITIVITY_COUNTEREXAMPLE", "PASS")
    print("ALL_TESTS_PASS")


if __name__ == "__main__":
    main()
