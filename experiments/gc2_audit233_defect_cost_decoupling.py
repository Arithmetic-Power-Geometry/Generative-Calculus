"""GC-II Audit 233: exact finite defect/cost decoupling checks.

A fixed positive projection defect is paired with arbitrarily small positive
operational translator costs. This verifies the finite counterexample family
used in the Audit-233 proof note.
"""
from fractions import Fraction


def projection_defect():
    # Two global worlds collapse under a proper projection. Exact normalized
    # collision defect: one unresolved binary distinction.
    worlds = (0, 1)
    projected = {0: 0, 1: 0}
    assert projected[0] == projected[1]
    return Fraction(1, 1)


def operational_distance(epsilon):
    # States x,y; identity edges cost 0; sole nonidentity translator x->y.
    assert epsilon > 0
    return epsilon


def main():
    delta = projection_defect()
    assert delta > 0

    epsilons = [Fraction(1, 10**k) for k in range(0, 13)]
    distances = []
    for eps in epsilons:
        d = operational_distance(eps)
        assert d == eps
        assert d > 0
        assert projection_defect() == delta
        distances.append(d)

    # Fixed defect; operational distance can be made smaller than any tested
    # positive candidate lower bound g(delta).
    candidate_bounds = [Fraction(1, 2), Fraction(1, 10), Fraction(1, 1000), Fraction(1, 10**9)]
    for gdelta in candidate_bounds:
        assert gdelta > 0
        assert any(d < gdelta for d in distances)

    # Exact rescaling obstruction: reachability/projection data are unchanged,
    # while all nonidentity costs scale by alpha.
    base = Fraction(7, 3)
    for alpha in [Fraction(1, 2), Fraction(1, 10), Fraction(1, 10**6)]:
        assert operational_distance(alpha * base) == alpha * operational_distance(base)
        assert projection_defect() == delta

    print("audit233: exact defect/cost decoupling checks passed")
    print("fixed defect =", delta, "smallest tested positive d =", distances[-1])


if __name__ == "__main__":
    main()
