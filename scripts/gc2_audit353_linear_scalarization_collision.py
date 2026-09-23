#!/usr/bin/env python3
"""Exact checks for GC-II Audit 353."""
import json

A = {(0, 3), (3, 0)}
B = A | {(2, 2)}


def scalar_profile(C, a, b):
    return min(a*x + b*y for x, y in C)


def feasible(C, budget):
    u, v = budget
    return any(x <= u and y <= v for x, y in C)


def pareto_minimal(C, p):
    x, y = p
    return not any((u <= x and v <= y and (u, v) != p) for u, v in C)


def symbolic_case_check(a, b):
    # For nonnegative weights, (2,2) can never improve on both endpoints.
    assert a >= 0 and b >= 0
    endpoint = min(3*a, 3*b)
    middle = 2*a + 2*b
    if a <= b:
        assert endpoint == 3*a
        assert middle >= 4*a >= 3*a
    else:
        assert endpoint == 3*b
        assert middle >= 4*b >= 3*b
    return scalar_profile(A, a, b) == scalar_profile(B, a, b)


def main():
    failures = []
    checks = 0
    for a in range(0, 101):
        for b in range(0, 101):
            checks += 1
            if not symbolic_case_check(a, b):
                failures.append([a, b])

    budget = (2, 2)
    result = {
        "audit": 353,
        "system_A": sorted(A),
        "system_B": sorted(B),
        "weight_grid": "integer weights 0..100 in each coordinate",
        "weight_pairs_checked": checks,
        "scalar_profile_failures": len(failures),
        "middle_vector_pareto_minimal_in_B": pareto_minimal(B, (2, 2)),
        "separating_budget": budget,
        "A_feasible_at_separating_budget": feasible(A, budget),
        "B_feasible_at_separating_budget": feasible(B, budget),
        "symbolic_proof": "case a<=b or b<=a proves equality for every nonnegative real weight pair",
        "claim_scope": "linear weighted-sum scalarization profile is incomplete for exact componentwise budget feasibility"
    }
    assert not failures
    assert result["middle_vector_pareto_minimal_in_B"]
    assert not result["A_feasible_at_separating_budget"]
    assert result["B_feasible_at_separating_budget"]
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
