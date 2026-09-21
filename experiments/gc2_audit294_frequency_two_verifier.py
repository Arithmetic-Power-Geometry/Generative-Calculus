"""Exact finite verifier for GC-II Audit 294. No floating point."""
from itertools import combinations


def min_vertex_cover(n, edges):
    edges = set(edges)
    if not edges:
        return 0
    for k in range(n + 1):
        for chosen in combinations(range(n), k):
            C = set(chosen)
            if all(u in C or v in C for u, v in edges):
                return k
    raise AssertionError("unreachable")


def accounting_instance(n, edges):
    """Targets are edges; actions are vertices; zero loss iff incident."""
    targets = tuple(sorted(edges))
    feasible = {v: {e for e in targets if v in e} for v in range(n)}
    return targets, feasible


def min_action_cover(n, edges):
    targets, feasible = accounting_instance(n, edges)
    if not targets:
        return 0
    T = set(targets)
    for k in range(n + 1):
        for chosen in combinations(range(n), k):
            covered = set().union(*(feasible[v] for v in chosen)) if chosen else set()
            if covered >= T:
                return k
    return None


def verify_graph(n, edges):
    targets, feasible = accounting_instance(n, edges)
    # Every simple edge-target has exactly two zero-loss decoder actions.
    for e in targets:
        assert sum(e in feasible[v] for v in range(n)) == 2
    tau = min_vertex_cover(n, edges)
    acc = min_action_cover(n, edges)
    assert tau == acc
    return tau


def verify_frequency_one_boundary():
    # Abstract frequency-one set system: each target has one unique action.
    targets = {0, 1, 2, 3}
    feasible = {"a": {0, 2}, "b": {1}, "c": {3}}
    frequency = {y: sum(y in S for S in feasible.values()) for y in targets}
    assert all(f == 1 for f in frequency.values())
    # All nonempty actions are forced.
    assert len([S for S in feasible.values() if S]) == 3


def verify():
    graph_count = 0
    edge_target_count = 0
    equality_checks = 0
    max_tau = 0
    # Exhaust all labeled simple graphs through n=5: 1+2+8+64+1024 = 1099.
    for n in range(1, 6):
        possible = list(combinations(range(n), 2))
        for mask in range(1 << len(possible)):
            edges = {possible[i] for i in range(len(possible)) if (mask >> i) & 1}
            tau = verify_graph(n, edges)
            graph_count += 1
            edge_target_count += len(edges)
            equality_checks += 1
            max_tau = max(max_tau, tau)

    # Explicit degenerate / structural boundaries.
    assert verify_graph(0, set()) == 0
    assert verify_graph(5, set()) == 0  # isolated vertices only
    assert verify_graph(4, {(0, 1), (2, 3)}) == 2  # disconnected
    assert verify_graph(3, {(0, 1), (1, 2), (0, 2)}) == 2  # odd cycle
    verify_frequency_one_boundary()

    print({
        "status": "PASS",
        "labeled_simple_graphs_n_le_5": graph_count,
        "edge_targets_checked": edge_target_count,
        "vertex_cover_accounting_equalities": equality_checks + 4,
        "target_frequency": 2,
        "max_vertex_cover_seen": max_tau,
        "frequency_one_boundary": "PASS",
    })


if __name__ == "__main__":
    verify()
