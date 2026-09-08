from itertools import product

from generative_calculus.gc2_global_translator import (
    collision_multiplicity,
    construct_interface_code,
    globally_convertible,
    min_interface_bits,
    min_interface_states,
    min_weighted_shared_translation_error,
    translate_all,
)


def test_min_interface_formula_exhaustive_small_worlds():
    # Exhaust all source/target assignments for n=1..4 tasks over binary source and 3 target labels.
    for n in range(1, 5):
        tasks = tuple(range(n))
        for xs in product(range(2), repeat=n):
            source = dict(zip(tasks, xs))
            for ys in product(range(3), repeat=n):
                target = dict(zip(tasks, ys))
                m = collision_multiplicity(source, target)
                assert min_interface_states(source, target) == m
                assert globally_convertible(source, target) == (m == 1)
                code, translator = construct_interface_code(source, target)
                assert max(code.values(), default=0) < m
                assert translate_all(source, code, translator) == target
                if m > 1:
                    x_star = max(
                        set(source.values()),
                        key=lambda x: len({target[t] for t in tasks if source[t] == x}),
                    )
                    fibre_tasks = [t for t in tasks if source[t] == x_star]
                    labels = {target[t] for t in fibre_tasks}
                    assert len(labels) == m
                    q = m - 1
                    for assignment in product(range(q), repeat=m):
                        assert len(set(assignment)) < m


def test_individual_zero_gap_but_global_positive_gap():
    source = {"t1": "same", "t2": "same"}
    target = {"t1": 0, "t2": 1}
    assert globally_convertible({"t1": "same"}, {"t1": 0})
    assert globally_convertible({"t2": "same"}, {"t2": 1})
    assert not globally_convertible(source, target)
    assert min_interface_states(source, target) == 2
    assert min_interface_bits(source, target) == 1
    assert min_weighted_shared_translation_error(source, target) == 1.0


def test_weighted_error_exact_formula():
    source = {0: "x", 1: "x", 2: "x", 3: "z"}
    target = {0: "a", 1: "a", 2: "b", 3: "c"}
    weights = {0: 3.0, 1: 2.0, 2: 4.0, 3: 7.0}
    assert min_weighted_shared_translation_error(source, target, weights) == 4.0
