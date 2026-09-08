from itertools import permutations


def step(state, primitive):
    table = {
        ("s0", "I"): "sI",
        ("s0", "A"): "sA",
        ("sA", "I"): "goal",
        ("sI", "A"): "dead",
    }
    return table.get((state, primitive), state)


def run(word):
    state = "s0"
    for primitive in word:
        state = step(state, primitive)
    return state


def delta(word):
    return (0, word.count("I"), word.count("A"), 0)


def test_same_aggregate_delta_different_capability():
    assert delta(("A", "I")) == delta(("I", "A")) == (0, 1, 1, 0)
    assert run(("A", "I")) == "goal"
    assert run(("I", "A")) == "dead"


def test_nonlinear_function_of_delta_cannot_recover_order():
    def nonlinear_F(d):
        r, i, a, l = d
        return r + i + a + l + i * a + r * l
    assert nonlinear_F(delta(("A", "I"))) == nonlinear_F(delta(("I", "A")))
    assert (run(("A", "I")) == "goal") != (run(("I", "A")) == "goal")


def test_commuting_subclass_restores_path_independence():
    def commuting_step(state, primitive):
        i, a = state
        if primitive == "I":
            i = 1
        elif primitive == "A":
            a = 1
        return (i, a)

    endpoints = set()
    for word in set(permutations(("I", "A"))):
        state = (0, 0)
        for primitive in word:
            state = commuting_step(state, primitive)
        endpoints.add(state)
    assert endpoints == {(1, 1)}


def test_empty_and_singleton_edge_cases():
    assert delta(()) == (0, 0, 0, 0)
    assert run(()) == "s0"
    assert delta(("I",)) == (0, 1, 0, 0)
    assert delta(("A",)) == (0, 0, 1, 0)
