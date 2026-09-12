"""Controlled GC-II AI capability-accounting experiment.

Two toy agents have identical unconstrained task coverage and identical conventional
uniform scalar cost for every task, but different typed (R,I,A,L) cost vectors.
We exhaust the finite budget cube {0,1,2}^4 and compare their feasible task closures.

This is a controlled structural experiment, not an empirical claim about deployed AI.
"""
from itertools import product
import csv
from pathlib import Path

AGENT_A = {
    "T1": (2, 0, 0, 0),
    "T2": (0, 2, 0, 0),
    "T3": (0, 0, 2, 0),
    "T4": (0, 0, 0, 2),
}

AGENT_B = {
    "T1": (1, 1, 0, 0),
    "T2": (0, 1, 1, 0),
    "T3": (0, 0, 1, 1),
    "T4": (1, 0, 0, 1),
}


def feasible(cost, budget):
    return all(c <= b for c, b in zip(cost, budget))


def closure(agent, budget):
    return tuple(task for task, cost in agent.items() if feasible(cost, budget))


def main():
    # Conventional scalar check: each task costs exactly 2 under weight (1,1,1,1).
    for task in AGENT_A:
        assert sum(AGENT_A[task]) == sum(AGENT_B[task]) == 2
    assert set(AGENT_A) == set(AGENT_B)

    rows = []
    different = a_more = b_more = equal_count = 0
    for budget in product(range(3), repeat=4):
        ca = closure(AGENT_A, budget)
        cb = closure(AGENT_B, budget)
        different += ca != cb
        if len(ca) > len(cb):
            a_more += 1
        elif len(cb) > len(ca):
            b_more += 1
        else:
            equal_count += 1
        rows.append({
            "R": budget[0], "I": budget[1], "A": budget[2], "L": budget[3],
            "agent_A_count": len(ca), "agent_B_count": len(cb),
            "agent_A_tasks": ";".join(ca), "agent_B_tasks": ";".join(cb),
            "closure_equal": int(ca == cb),
        })

    assert len(rows) == 81
    assert different == 65
    assert a_more == 18
    assert b_more == 35
    assert equal_count == 28

    out = Path("results/gc2_ai_typed_budget_closure.csv")
    out.parent.mkdir(parents=True, exist_ok=True)
    with out.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=rows[0].keys())
        w.writeheader()
        w.writerows(rows)

    print({
        "budgets": len(rows),
        "different_closures": different,
        "agent_A_more_tasks": a_more,
        "agent_B_more_tasks": b_more,
        "equal_task_count": equal_count,
        "uniform_scalar_cost_per_task": 2,
    })


if __name__ == "__main__":
    main()
