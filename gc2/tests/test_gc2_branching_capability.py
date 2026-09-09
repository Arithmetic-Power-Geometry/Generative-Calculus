from gc2.branching_capability import early_vs_late_choice_witness


def test_trace_sets_match_through_terminal_depth():
    world, p, q = early_vs_late_choice_witness()
    assert world.action_cost_traces(p, 0) == world.action_cost_traces(q, 0)
    assert world.action_cost_traces(p, 1) == world.action_cost_traces(q, 1)
    assert world.action_cost_traces(p, 2) == world.action_cost_traces(q, 2)
    # Both systems terminate after two actions, so equality persists thereafter.
    assert world.action_cost_traces(p, 5) == world.action_cost_traces(q, 5)


def test_branching_capability_differs_after_a():
    world, p, q = early_vs_late_choice_witness()
    assert world.robust_post_action_set(p, "a") == frozenset({"b", "c"})
    assert world.robust_post_action_set(q, "a") == frozenset()


def test_exact_trace_language_is_epsilon_a_ab_ac():
    world, p, q = early_vs_late_choice_witness()
    expected = frozenset({
        (),
        (("a", 0),),
        (("a", 0), ("b", 0)),
        (("a", 0), ("c", 0)),
    })
    assert world.action_cost_traces(p, 10) == expected
    assert world.action_cost_traces(q, 10) == expected
