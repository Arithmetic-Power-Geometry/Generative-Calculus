from itertools import product
from collections import defaultdict
import json
from pathlib import Path

X = range(3)
Y = range(3)
TASKS = list(product([0, 1], repeat=3))
ENCODERS = list(product(Y, repeat=3))
GARBLINGS = list(product(Y, repeat=3))


def optimal_binary_accuracy(mapping, task):
    buckets = defaultdict(list)
    for x, z in enumerate(mapping):
        buckets[z].append(task[x])
    correct = 0
    for vals in buckets.values():
        ones = sum(vals)
        zeros = len(vals) - ones
        correct += max(zeros, ones)
    return correct / len(mapping)


def main():
    total_checks = 0
    violations = 0
    strict_losses = 0
    max_loss = 0.0

    for f in ENCODERS:
        for g in GARBLINGS:
            gf = tuple(g[f[x]] for x in X)
            for task in TASKS:
                before = optimal_binary_accuracy(f, task)
                after = optimal_binary_accuracy(gf, task)
                total_checks += 1
                if after > before + 1e-12:
                    violations += 1
                if after < before - 1e-12:
                    strict_losses += 1
                max_loss = max(max_loss, before - after)

    result = {
        "state_count": 3,
        "signal_count": 3,
        "binary_tasks": len(TASKS),
        "deterministic_encoders": len(ENCODERS),
        "deterministic_garblings": len(GARBLINGS),
        "decision_checks": total_checks,
        "data_processing_violations": violations,
        "strict_decision_losses": strict_losses,
        "maximum_accuracy_loss": max_loss,
        "interpretation": "Deterministic post-processing never improves optimal binary decision accuracy in this exhaustive finite audit. This is a consistency check for Blackwell/data-processing monotonicity, not evidence of GC-II novelty."
    }

    out = Path("results/gc2_blackwell_witness_collision_summary.json")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
