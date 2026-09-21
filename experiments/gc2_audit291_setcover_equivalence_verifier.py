"""Exact finite verifier for GC-II Audit 291. No floating point."""
from itertools import combinations


def cover_number(universe, sets):
    labels = list(sets)
    if not universe:
        return 0
    for k in range(1, len(labels) + 1):
        for chosen in combinations(labels, k):
            if set().union(*(sets[a] for a in chosen)) >= set(universe):
                return k
    return float("inf")


def accounting_from_setcover(universe, sets):
    # epsilon=0 and binary loss: feasible states of action a are exactly sets[a].
    loss = {(u, a): (0 if u in members else 1)
            for a, members in sets.items() for u in universe}
    feasible = {a: {u for u in universe if loss[(u, a)] <= 0}
                for a in sets}
    return loss, feasible


def verify():
    instances = [
        ({1, 2, 3}, {"a12": {1, 2}, "a23": {2, 3}, "a13": {1, 3}}),
        ({1, 2, 3, 4}, {"a": {1, 2}, "b": {3}, "c": {4}, "d": {2, 3, 4}}),
        ({1, 2, 3}, {"all": {1, 2, 3}}),
        ({1, 2, 3}, {"a": {1}, "b": {2}}),  # infeasible / uncovered target
        (set(), {"a": set()}),                 # empty-universe convention
    ]
    checks = 0
    for universe, sets in instances:
        loss, feasible = accounting_from_setcover(universe, sets)
        assert feasible == sets
        assert cover_number(universe, feasible) == cover_number(universe, sets)
        assert all(v in (0, 1) for v in loss.values())
        checks += 1

    # Exhaust every nonempty family over universes n <= 3.
    exhaustive = 0
    for n in range(1, 4):
        U = set(range(n))
        subsets = [set(i for i in range(n) if mask & (1 << i))
                   for mask in range(1 << n)]
        for family_mask in range(1, 1 << len(subsets)):
            S = {str(j): subsets[j] for j in range(len(subsets))
                 if family_mask & (1 << j)}
            _, F = accounting_from_setcover(U, S)
            assert cover_number(U, F) == cover_number(U, S)
            exhaustive += 1

    print({"status": "PASS", "hand_instances": checks,
           "exhaustive_families_n_le_3": exhaustive,
           "loss": "binary exact", "epsilon": 0,
           "equivalence": "SET_COVER <-> finite operational accounting"})


if __name__ == "__main__":
    verify()
