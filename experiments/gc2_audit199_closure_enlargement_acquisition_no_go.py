"""GC-II Audit 199: exact finite counterexample.

Strict capability-closure enlargement need not change a complete acquisition
experiment or its optimal cost.
"""
from itertools import product

W = (0, 1)
Q = ("probe",)
# deterministic response reveals the world; same kernel in both systems
P = {(w, "probe"): w for w in W}
COST = {"probe": 1}
TASK = {0: 0, 1: 1}
EPSILON = 0

# Operational closures differ strictly.
C0 = frozenset({"x"})
C1 = frozenset({"x", "y"})


def acquisition_signature():
    """Canonical finite signature of all acquisition-relevant components."""
    return (W, Q, tuple(sorted(P.items())), tuple(sorted(COST.items())),
            tuple(sorted(TASK.items())), EPSILON)


def worst_case_one_probe_error(decoder):
    return max(int(decoder[P[(w, "probe")]] != TASK[w]) for w in W)


def exact_min_cost():
    # Enumerate all binary decoders after the sole probe.
    feasible = []
    for outputs in product((0, 1), repeat=2):
        decoder = {0: outputs[0], 1: outputs[1]}
        if worst_case_one_probe_error(decoder) <= EPSILON:
            feasible.append(COST["probe"])
    # Zero-query constant decisions are infeasible for this two-world task.
    for a in (0, 1):
        assert max(int(a != TASK[w]) for w in W) == 1
    return min(feasible)


def main():
    assert C0 < C1
    E0 = acquisition_signature()
    E1 = acquisition_signature()
    assert E0 == E1
    ac0 = exact_min_cost()
    ac1 = exact_min_cost()
    assert ac0 == ac1 == 1
    # Response distinguishability is unchanged exactly.
    assert P[(0, "probe")] != P[(1, "probe")]
    print("strict_closure_enlargement", sorted(C0), "->", sorted(C1))
    print("complete_experiment_equal", E0 == E1)
    print("minimum_acquisition_cost", ac0, ac1)
    print("RESULT: unrestricted closure-enlargement => acquisition-change is FALSIFIED")


if __name__ == "__main__":
    main()
