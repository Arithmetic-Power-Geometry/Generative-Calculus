#!/usr/bin/env python3
from itertools import product, combinations
import csv
from pathlib import Path

TASKS = ("T1", "T2", "T3")

def subsets():
    out = []
    for r in range(len(TASKS) + 1):
        out.extend(frozenset(c) for c in combinations(TASKS, r))
    return out

def cost_a(S):
    k = len(S)
    if k == 0:
        return (0, 0, 0, 0)
    return (k + 1, k, 0, 0)  # one shared R setup + per-task R/I

def cost_b(S):
    k = len(S)
    if k == 0:
        return (0, 0, 0, 0)
    return (2 * k, k, 0, 0)  # same singleton cost, setup effectively repaid per task

def feasible(c, b):
    return all(x <= y for x, y in zip(c, b))

def main():
    ss = subsets()
    rows = []
    for b in product(range(7), range(4), range(2), range(2)):
        fa = [S for S in ss if feasible(cost_a(S), b)]
        fb = [S for S in ss if feasible(cost_b(S), b)]
        max_a = max(map(len, fa))
        max_b = max(map(len, fb))
        rows.append((*b, int(set(fa) != set(fb)), max_a, max_b, max_a - max_b))

    out = Path("results/gc2_joint_reuse_closure.csv")
    out.parent.mkdir(parents=True, exist_ok=True)
    with out.open("w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["b_R","b_I","b_A","b_L","closure_diff","max_tasks_A","max_tasks_B","cardinality_advantage_A"])
        w.writerows(rows)

    for t in TASKS:
        assert cost_a(frozenset({t})) == cost_b(frozenset({t})) == (2,1,0,0)
    assert len(rows) == 112
    assert sum(r[4] for r in rows) == 16
    assert sum(r[5] > r[6] for r in rows) == 16
    assert sum(r[5] < r[6] for r in rows) == 0
    assert max(r[7] for r in rows) == 1

    print("budgets=112")
    print("different_joint_closures=16")
    print("A_cardinality_advantage=16")
    print("B_cardinality_advantage=0")
    print("max_observed_task_advantage=1")

if __name__ == "__main__":
    main()
