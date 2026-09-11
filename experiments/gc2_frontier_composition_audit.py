from itertools import product, permutations
import csv
from pathlib import Path

NODES = (0, 1, 2)
LABELS = ((1, 3), (2, 2), (3, 1))
WEIGHTS = ((1, 0), (0, 1), (1, 1), (1, 2), (2, 1))
EDGES = tuple((u, v) for u in NODES for v in NODES if u != v)
TRIPLES = ((0, 2, 1), (0, 1, 2), (1, 2, 0))


def simple_paths(s, t):
    mids = [v for v in NODES if v not in (s, t)]
    out = [(s, t)]
    for r in range(1, len(mids) + 1):
        for seq in permutations(mids, r):
            out.append((s,) + seq + (t,))
    return out


PATHS = {(s, t): simple_paths(s, t) for s in NODES for t in NODES if s != t}


def path_cost(path, costs):
    return tuple(sum(costs[e][i] for e in zip(path, path[1:])) for i in range(2))


def scalar_distance(s, t, w, costs):
    return min(
        sum(w[i] * path_cost(p, costs)[i] for i in range(2))
        for p in PATHS[(s, t)]
    )


def main():
    assignments = 0
    tests = 0
    violations = 0
    positive_slack = 0
    zero_slack = 0
    max_slack = 0

    for values in product(LABELS, repeat=len(EDGES)):
        costs = dict(zip(EDGES, values))
        assignments += 1
        for s, t, y in TRIPLES:
            for w in WEIGHTS:
                direct = scalar_distance(s, t, w, costs)
                via = scalar_distance(s, y, w, costs) + scalar_distance(y, t, w, costs)
                slack = via - direct
                tests += 1
                if slack < 0:
                    violations += 1
                elif slack == 0:
                    zero_slack += 1
                else:
                    positive_slack += 1
                max_slack = max(max_slack, slack)

    out = Path("results/gc2_frontier_composition_audit.csv")
    out.parent.mkdir(parents=True, exist_ok=True)
    with out.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([
            "assignments", "scalarization_tests", "triangle_slack_violations",
            "zero_slack", "positive_slack", "max_slack"
        ])
        writer.writerow([
            assignments, tests, violations, zero_slack, positive_slack, max_slack
        ])

    print(f"assignments={assignments}")
    print(f"scalarization_tests={tests}")
    print(f"triangle_slack_violations={violations}")
    print(f"zero_slack={zero_slack}")
    print(f"positive_slack={positive_slack}")
    print(f"max_slack={max_slack}")


if __name__ == "__main__":
    main()
