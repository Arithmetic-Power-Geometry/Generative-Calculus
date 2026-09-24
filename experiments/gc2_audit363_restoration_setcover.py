"""Exact finite verifier for GC-II Audit 363.

Checks that the minimum number of labels in an unrestricted deterministic
restoration-sufficient observation equals the minimum action-domain set cover.
No external dependencies.
"""
from itertools import product, combinations


def min_action_cover(restore, n_actions):
    n = len(restore)
    if n == 0:
        return 0
    if any(not r for r in restore):
        return None
    for k in range(1, n_actions + 1):
        for chosen in combinations(range(n_actions), k):
            if all(any(a in restore[w] for a in chosen) for w in range(n)):
                return k
    return None


def partition_labels(labels):
    cells = {}
    for w, y in enumerate(labels):
        cells.setdefault(y, []).append(w)
    return list(cells.values())


def sufficient_cells(cells, restore):
    for cell in cells:
        common = set(restore[cell[0]])
        for w in cell[1:]:
            common &= set(restore[w])
        if not common:
            return False
    return True


def min_labels_direct(restore):
    n = len(restore)
    if n == 0:
        return 0
    if any(not r for r in restore):
        return None
    # Enumerate all label maps W -> {0,...,m-1}. Duplicate encodings are harmless.
    for m in range(1, n + 1):
        for labels in product(range(m), repeat=n):
            if len(set(labels)) != m:
                continue
            if sufficient_cells(partition_labels(labels), restore):
                return m
    return None


def exhaustive(max_worlds=4, n_actions=3):
    nonempty = []
    for mask in range(1, 1 << n_actions):
        nonempty.append(tuple(a for a in range(n_actions) if mask & (1 << a)))
    checks = 0
    for n in range(1, max_worlds + 1):
        for restore in product(nonempty, repeat=n):
            cover = min_action_cover(restore, n_actions)
            direct = min_labels_direct(restore)
            assert cover == direct, (restore, cover, direct)
            checks += 1
    return checks


def sanity():
    # One universal action: no discrimination beyond one label.
    assert min_action_cover([{0}, {0, 1}, {0, 2}], 3) == 1
    # Three private actions: full discrimination is required.
    assert min_action_cover([{0}, {1}, {2}], 3) == 3
    # Pairwise overlap need not imply one common action.
    tri = [{0, 1}, {1, 2}, {0, 2}]
    assert min_action_cover(tri, 3) == 2
    assert min_labels_direct(tri) == 2


if __name__ == "__main__":
    sanity()
    checks = exhaustive()
    print({"instances_checked": checks,
           "actions": 3,
           "worlds_up_to": 4,
           "mismatches": 0,
           "theorem": "min_labels == min_action_cover"})
