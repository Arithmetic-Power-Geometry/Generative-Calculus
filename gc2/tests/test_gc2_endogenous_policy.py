from itertools import product


def min_worst_case_depth(targets, tests):
    """Exact finite deterministic adaptive-test depth by recursion on trace fibres."""
    traces = tuple(range(len(targets)))

    def solve(fibre, remaining):
        if len({targets[t] for t in fibre}) <= 1:
            return 0
        best = float("inf")
        for j in remaining:
            buckets = {}
            for t in fibre:
                buckets.setdefault(tests[j][t], []).append(t)
            # A test that does not refine this fibre cannot help.
            if len(buckets) <= 1:
                continue
            rest = tuple(k for k in remaining if k != j)
            child = max(solve(tuple(v), rest) for v in buckets.values())
            best = min(best, 1 + child)
        return best

    return solve(traces, tuple(range(len(tests))))


def test_three_trace_pairwise_separable_but_not_one_step_global():
    targets = (0, 1, 2)
    tests = (
        (1, 0, 0),  # isolate trace 0
        (0, 1, 0),  # isolate trace 1
        (0, 0, 1),  # isolate trace 2
    )
    # Every pair is separated by at least one available action.
    for i in range(3):
        for j in range(i + 1, 3):
            assert any(test[i] != test[j] for test in tests)
    # But every single binary action leaves a target-impure branch.
    for test in tests:
        buckets = {}
        for t, outcome in enumerate(test):
            buckets.setdefault(outcome, []).append(t)
        assert any(len({targets[t] for t in fibre}) > 1 for fibre in buckets.values())
    assert min_worst_case_depth(targets, tests) == 2


def test_binary_information_lower_bound_small_exhaustive():
    # Exhaust all binary tests on 3 traces. Whenever a test family can identify
    # three distinct targets, one test is impossible and exact depth is >= 2.
    targets = (0, 1, 2)
    all_tests = tuple(product((0, 1), repeat=3))
    checked = 0
    for i in range(len(all_tests)):
        for j in range(i + 1, len(all_tests)):
            family = (all_tests[i], all_tests[j])
            depth = min_worst_case_depth(targets, family)
            if depth < float("inf"):
                checked += 1
                assert depth >= 2
    assert checked > 0


def test_degenerate_pure_target_needs_no_information():
    assert min_worst_case_depth((7, 7, 7), ((1, 0, 0),)) == 0
