from gc2.trace_reversibility import Edge, FiniteWorld


def test_reachable_label_signature_collides_despite_action_difference():
    world = FiniteWorld(
        labels={"x0": "X", "x1": "X", "g": "G"},
        edges=(Edge("x0", "a", "g", 0), Edge("x1", "b", "g", 0)),
    )
    for depth in range(0, 8):
        assert world.future_label_signature("x0", depth) == world.future_label_signature("x1", depth)

    assert world.step("x0", "a") == "g"
    try:
        world.step("x1", "a")
    except ValueError:
        pass
    else:
        raise AssertionError("x1 must not support action a")


def test_horizon_growth_cannot_repair_collision():
    world = FiniteWorld(
        labels={"x0": "X", "x1": "X", "g": "G"},
        edges=(Edge("x0", "a", "g", 2), Edge("x1", "b", "g", 2)),
    )
    assert all(
        world.future_label_signature("x0", h) == world.future_label_signature("x1", h)
        for h in range(20)
    )
