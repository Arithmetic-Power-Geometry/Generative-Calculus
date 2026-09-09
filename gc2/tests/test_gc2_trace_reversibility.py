from gc2.trace_reversibility import (
    canonical_endpoint_cost_pair,
    endpoint_collision_witnesses,
    round_trip_residual,
)


def test_endpoint_cost_pair_collides_but_round_trip_capability_differs():
    reversible, degrading = endpoint_collision_witnesses()

    pair_r = canonical_endpoint_cost_pair(reversible, "x0", "Y", "X")
    pair_d = canonical_endpoint_cost_pair(degrading, "x0", "Y", "X")

    assert pair_r == (1, 1)
    assert pair_d == (1, 1)

    before_r, after_r = round_trip_residual(reversible, "x0", depth=1)
    before_d, after_d = round_trip_residual(degrading, "x0", depth=1)

    assert before_r == after_r
    assert before_d != after_d
    assert "G" in before_d
    assert "G" not in after_d


def test_depth_zero_cannot_detect_future_capability_loss():
    _, degrading = endpoint_collision_witnesses()
    before, after = round_trip_residual(degrading, "x0", depth=0)
    assert before == after == frozenset({"X"})


def test_endpoint_label_itself_is_preserved_in_degrading_cycle():
    _, degrading = endpoint_collision_witnesses()
    y = degrading.step("x0", "f")
    returned = degrading.step(y, "r")
    assert degrading.labels["x0"] == degrading.labels[returned] == "X"


def test_nonnegative_cost_guard():
    from gc2.trace_reversibility import Edge
    import pytest

    with pytest.raises(ValueError):
        Edge("a", "bad", "b", -1)
