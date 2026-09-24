"""Exact verifier for GC-II Audit 362.

No external dependencies.  Exhaustively checks the one-step common-action
criterion for all observation maps, nonempty restoration-action sets, and
observation-based policies for n<=3 worlds and two actions.  Also checks the
adaptive three-world counterexample.
"""
from itertools import product


def direct_one_step(obs, restore, n_actions):
    labels = sorted(set(obs))
    # Enumerate all policies label -> action.
    for choices in product(range(n_actions), repeat=len(labels)):
        pi = dict(zip(labels, choices))
        if all(pi[obs[w]] in restore[w] for w in range(len(obs))):
            return True
    return False


def intersection_criterion(obs, restore):
    for label in set(obs):
        fiber = [w for w, z in enumerate(obs) if z == label]
        common = set(restore[fiber[0]])
        for w in fiber[1:]:
            common &= set(restore[w])
        if not common:
            return False
    return True


def adaptive_solvable(C, restore, sensors, memo=None):
    if memo is None:
        memo = {}
    key = tuple(sorted(C))
    if key in memo:
        return memo[key]
    if not C:
        return True
    common = set(restore[next(iter(C))])
    for w in C:
        common &= set(restore[w])
    if common:
        memo[key] = True
        return True
    # pessimistic provisional value prevents recursion through nonprogressing cycles
    memo[key] = False
    for sensor in sensors:
        cells = {}
        for w in C:
            cells.setdefault(sensor[w], set()).add(w)
        children = list(cells.values())
        if len(children) < 2:
            continue
        if all(adaptive_solvable(child, restore, sensors, memo) for child in children):
            memo[key] = True
            return True
    return False


def exhaustive():
    checks = 0
    action_subsets = [(0,), (1,), (0, 1)]
    for n in range(1, 4):
        # Canonical labels 0..n-1; this includes duplicate encodings of partitions,
        # harmless for an exact exhaustive consistency check.
        for obs in product(range(n), repeat=n):
            for restore in product(action_subsets, repeat=n):
                d = direct_one_step(obs, restore, 2)
                c = intersection_criterion(obs, restore)
                checks += 1
                assert d == c, (n, obs, restore, d, c)
    return checks


def counterexample():
    restore = [{0}, {0, 1}, {1}]
    # Sensor leaves w0 and w1 indistinguishable but separates w2.
    sensors = [(0, 0, 1)]
    assert adaptive_solvable({0, 1, 2}, restore, sensors)
    # No common action initially.
    assert not (set(restore[0]) & set(restore[1]) & set(restore[2]))
    # Yet worlds 0 and 1 remain observationally merged.
    assert sensors[0][0] == sensors[0][1]
    return True


if __name__ == "__main__":
    checks = exhaustive()
    counterexample()
    print({"one_step_instances_checked": checks,
           "mismatches": 0,
           "adaptive_counterexample_verified": True})
