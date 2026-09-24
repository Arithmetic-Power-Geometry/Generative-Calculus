"""Exact finite verifier for GC-II Audit 364.

Checks the minimal-bad-hyperedge cover characterization of restoration-sufficient
nonadaptive restricted observations. Also checks the 3-world counterexample to
naive pair-conflict cover.

No external dependencies.
"""
from itertools import product, combinations


def powerset_nonempty(n):
    for k in range(1, n + 1):
        yield from combinations(range(n), k)


def intersection_nonempty(worlds, restore):
    common = set(restore[worlds[0]])
    for w in worlds[1:]:
        common &= set(restore[w])
    return bool(common)


def minimal_bad_sets(restore):
    n = len(restore)
    bad = []
    for B in powerset_nonempty(n):
        if intersection_nonempty(B, restore):
            continue
        minimal = True
        for i in range(len(B)):
            sub = B[:i] + B[i + 1:]
            if sub and not intersection_nonempty(sub, restore):
                minimal = False
                break
        if minimal:
            bad.append(B)
    return bad


def cells_from_tests(tests, chosen, n):
    cells = {}
    for w in range(n):
        sig = tuple(tests[q][w] for q in chosen)
        cells.setdefault(sig, []).append(w)
    return list(cells.values())


def directly_sufficient(restore, tests, chosen):
    for cell in cells_from_tests(tests, chosen, len(restore)):
        if not intersection_nonempty(tuple(cell), restore):
            return False
    return True


def covers_all_minimal_bad(restore, tests, chosen):
    for B in minimal_bad_sets(restore):
        destroyed = False
        for q in chosen:
            if len({tests[q][w] for w in B}) > 1:
                destroyed = True
                break
        if not destroyed:
            return False
    return True


def naive_pair_conflicts(restore):
    n = len(restore)
    out = []
    for u, v in combinations(range(n), 2):
        if not (set(restore[u]) & set(restore[v])):
            out.append((u, v))
    return out


def counterexample():
    restore = [(0, 1), (1, 2), (0, 2)]
    assert naive_pair_conflicts(restore) == []
    assert minimal_bad_sets(restore) == [(0, 1, 2)]
    assert not directly_sufficient(restore, [], ())


def exhaustive(max_worlds=3, n_actions=3, max_tests=3):
    action_sets = [tuple(a for a in range(n_actions) if mask & (1 << a))
                   for mask in range(1, 1 << n_actions)]
    checks = 0
    for n in range(1, max_worlds + 1):
        # all nonempty restoration sets per world
        for restore in product(action_sets, repeat=n):
            # binary deterministic tests are all bit-vectors except constants are
            # retained deliberately to test degenerate observations
            all_tests = list(product((0, 1), repeat=n))
            # Exhaustive test families up to max_tests, with repetition avoided.
            for m in range(0, min(max_tests, len(all_tests)) + 1):
                for idxs in combinations(range(len(all_tests)), m):
                    tests = [all_tests[i] for i in idxs]
                    for mask in range(1 << m):
                        chosen = tuple(q for q in range(m) if mask & (1 << q))
                        direct = directly_sufficient(restore, tests, chosen)
                        hyper = covers_all_minimal_bad(restore, tests, chosen)
                        assert direct == hyper, (restore, tests, chosen, direct, hyper)
                        checks += 1
    return checks


if __name__ == "__main__":
    counterexample()
    checks = exhaustive()
    print({
        "instances_checked": checks,
        "mismatches": 0,
        "theorem": "restoration-sufficient iff every minimal bad set is split",
        "naive_pair_criterion": "falsified for general set-valued actions",
    })
