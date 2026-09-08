import itertools
from gc2.fibre_refinement import conflict_pairs, is_sufficient, min_refinement


def additive(weights):
    return lambda S: sum(weights[i] for i in S)


def test_taskwise_zero_global_positive_refinement_cost():
    x = [0, 0]
    y = [0, 1]
    features = [[0, 1]]
    value, chosen = min_refinement(x, y, features, additive([3]))
    assert value == 3
    assert chosen == frozenset({0})


def test_joint_refinement_can_be_necessary():
    # Three conflicts; neither binary feature alone resolves all of them.
    x = [0, 0, 0]
    y = [0, 1, 2]
    features = [[0, 1, 1], [0, 0, 1]]
    assert not is_sufficient(x, y, features, {0})
    assert not is_sufficient(x, y, features, {1})
    assert is_sufficient(x, y, features, {0, 1})
    value, chosen = min_refinement(x, y, features, additive([1, 1]))
    assert value == 2 and chosen == frozenset({0, 1})


def test_nonlinear_cross_channel_penalty_is_supported():
    x = [0, 0, 0]
    y = [0, 1, 2]
    features = [[0, 1, 1], [0, 0, 1]]
    # Superadditive interaction: selecting both costs 1+1+2.
    def cost(S):
        return len(S) + (2 if S == frozenset({0, 1}) else 0)
    value, _ = min_refinement(x, y, features, cost)
    assert value == 4


def test_exhaustive_criterion_small_binary_worlds():
    # Exhaustively compare direct functional consistency after feature selection
    # with conflict-pair coverage for all 3-trace binary x/y/features.
    vals = list(itertools.product([0, 1], repeat=3))
    for x in vals:
        for y in vals:
            for f in vals:
                for chosen in [frozenset(), frozenset({0})]:
                    sufficient = is_sufficient(x, y, [f], chosen)
                    signatures = [(x[i], f[i] if 0 in chosen else None) for i in range(3)]
                    direct = all(not (signatures[i] == signatures[j] and y[i] != y[j])
                                 for i in range(3) for j in range(i + 1, 3))
                    assert sufficient == direct


def test_no_conflicts_requires_zero_refinement():
    value, chosen = min_refinement([0, 1], [0, 1], [], lambda S: 0)
    assert value == 0 and chosen == frozenset()
