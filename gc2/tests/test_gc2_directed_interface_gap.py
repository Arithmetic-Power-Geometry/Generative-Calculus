import itertools
import math

from gc2.directed_interface_gap import (
    collision_multiplicity,
    composition_bound_holds,
    directed_interface_gap,
    fixed_width_bits,
)


def test_degenerate_and_identity_cases():
    assert collision_multiplicity([], []) == 1
    assert directed_interface_gap([], []) == 0.0
    for x in [(), (0,), (0, 1, 0), (2, 2, 3, 3)]:
        assert collision_multiplicity(x, x) == 1
        assert directed_interface_gap(x, x) == 0.0
        assert fixed_width_bits(x, x) == 0


def test_zero_gap_is_functional_dependence_not_equality():
    x = (0, 0, 1, 1)
    y = ('a', 'a', 'b', 'b')
    assert x != y
    assert directed_interface_gap(x, y) == 0.0
    # Reverse is also zero here because the relabeling is bijective on fibres.
    z = ('same',) * 4
    assert directed_interface_gap(x, z) == 0.0
    assert directed_interface_gap(z, x) == 1.0


def test_exact_bits_match_collision_requirement():
    x = (0, 0, 0, 1, 1)
    y = ('a', 'b', 'c', 'a', 'b')
    assert collision_multiplicity(x, y) == 3
    assert math.isclose(directed_interface_gap(x, y), math.log2(3))
    assert fixed_width_bits(x, y) == 2


def test_exhaustive_triangle_composition_binary_n4():
    reps = list(itertools.product(range(2), repeat=4))
    checked = 0
    for x in reps:
        for y in reps:
            for z in reps:
                assert composition_bound_holds(x, y, z)
                assert directed_interface_gap(x, z) <= directed_interface_gap(x, y) + directed_interface_gap(y, z) + 1e-12
                checked += 1
    assert checked == 4096


def test_relabeling_invariance():
    x = (0, 0, 1, 1, 1)
    y = ('a', 'b', 'a', 'b', 'c')
    xr = tuple({0: 9, 1: 8}[v] for v in x)
    yr = tuple({'a': 'u', 'b': 'v', 'c': 'w'}[v] for v in y)
    assert collision_multiplicity(x, y) == collision_multiplicity(xr, yr)
    assert directed_interface_gap(x, y) == directed_interface_gap(xr, yr)
