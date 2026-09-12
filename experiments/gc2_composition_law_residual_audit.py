from itertools import product, combinations
import csv
from pathlib import Path

STATES = (0, 1)
ACTIONS = ("a", "b")
FUNCS = list(product(STATES, repeat=2))


def trace2(fa, fb):
    trans = {"a": fa, "b": fb}
    out = {}
    for u in ACTIONS:
        s = trans[u][0]
        for v in ACTIONS:
            out[u + v] = trans[v][s]
    return tuple(sorted(out.items()))


def main():
    systems = []
    for fa in FUNCS:
        for fb in FUNCS:
            one_step = (fa[0], fb[0])
            systems.append((fa, fb, one_step, trace2(fa, fb)))

    groups = {}
    for system in systems:
        groups.setdefault(system[2], []).append(system)

    rows = []
    separating_pairs = 0
    for sig in sorted(groups):
        for x, y in combinations(groups[sig], 2):
            differ = x[3] != y[3]
            separating_pairs += int(differ)
            rows.append(
                {
                    "one_step_a": sig[0],
                    "one_step_b": sig[1],
                    "system1_fa": "".join(map(str, x[0])),
                    "system1_fb": "".join(map(str, x[1])),
                    "system2_fa": "".join(map(str, y[0])),
                    "system2_fb": "".join(map(str, y[1])),
                    "length2_trace_maps_differ": int(differ),
                }
            )

    assert len(systems) == 16
    assert len(rows) == 24
    assert separating_pairs == 18

    out = Path("results/gc2_composition_law_residual_audit.csv")
    out.parent.mkdir(parents=True, exist_ok=True)
    with out.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)

    print("deterministic systems:", len(systems))
    print("same-one-step unordered pairs:", len(rows))
    print("pairs separated at length 2:", separating_pairs)
    print("pairs not separated at length 2:", len(rows) - separating_pairs)


if __name__ == "__main__":
    main()
