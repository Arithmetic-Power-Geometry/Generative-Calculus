from itertools import product

from gc2.omega_gap import (
    Context,
    Edge,
    omega_bruteforce_augmentation,
    omega_path_formula,
    reachable_states,
)


def _edge(u, v, kind):
    cost, req_i, req_a, req_l = kind
    return Edge(
        u,
        v,
        (cost,),
        frozenset({'i'}) if req_i else frozenset(),
        frozenset({'a'}) if req_a else frozenset(),
        frozenset({'l'}) if req_l else frozenset(),
    )


def test_omega_exact_path_formula_exhaustive_three_state_chain():
    kinds = [
        (cost, req_i, req_a, req_l)
        for cost in (0, 1, 2)
        for req_i, req_a, req_l in product((0, 1), repeat=3)
    ]
    cases = 0
    for first in kinds:
        for second in kinds:
            edges = [_edge(0, 1, first), _edge(1, 2, second)]
            for budget in (0, 1, 2):
                for has_i, has_a, has_l in product((0, 1), repeat=3):
                    context = Context(
                        (budget,),
                        frozenset({'i'}) if has_i else frozenset(),
                        frozenset({'a'}) if has_a else frozenset(),
                        frozenset({'l'}) if has_l else frozenset(),
                    )
                    brute = omega_bruteforce_augmentation(
                        3,
                        edges,
                        {0},
                        context,
                        2,
                        max_extra=4,
                        universe_info=frozenset({'i'}),
                        universe_actions=frozenset({'a'}),
                        universe_rules=frozenset({'l'}),
                    )
                    path = omega_path_formula(edges, {0}, context, 2, max_steps=2)
                    assert brute == path
                    assert (path == 0) == (
                        2 in reachable_states(3, edges, {0}, context)
                    )

                    stronger = Context(
                        (budget + 1,),
                        context.info | {'i'},
                        context.actions | {'a'},
                        context.rules | {'l'},
                    )
                    stronger_gap = omega_path_formula(
                        edges, {0}, stronger, 2, max_steps=2
                    )
                    assert stronger_gap <= path
                    cases += 1

    assert len(kinds) ** 2 == 576
    assert cases == 13_824


def test_nonlinear_interaction_is_not_additive():
    edge = Edge(0, 1, (1,), info=frozenset({'i'}))
    context = Context((0,))
    # One resource unit plus one missing information item has penalty
    # 1 + 1 + 1*1 = 3, not the additive value 2.
    assert omega_path_formula([edge], {0}, context, 1, max_steps=1) == 3
