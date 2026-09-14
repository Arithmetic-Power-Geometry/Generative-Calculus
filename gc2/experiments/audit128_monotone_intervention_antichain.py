import json
import math
from pathlib import Path


def enumerate_antichains(n: int):
    elems = list(range(1 << n))
    comparable = [[False] * (1 << n) for _ in elems]
    for a in elems:
        for b in elems:
            comparable[a][b] = ((a & b) == a) or ((a & b) == b)

    out = []

    def rec(cands, chosen):
        if not cands:
            out.append(tuple(chosen))
            return
        v = cands[0]
        rec(cands[1:], chosen)
        rec([u for u in cands[1:] if not comparable[v][u]], chosen + [v])

    rec(elems, [])
    return out


def minimal_true_points(n: int, antichain):
    true_points = [
        x for x in range(1 << n)
        if any((a & x) == a for a in antichain)
    ]
    mins = []
    for x in true_points:
        if not any(y != x and (y & x) == y for y in true_points):
            mins.append(x)
    return tuple(sorted(mins))


def main():
    rows = []
    total_functions = 0
    total_mismatches = 0

    for n in range(1, 6):
        antichains = enumerate_antichains(n)
        mismatches = sum(
            tuple(sorted(A)) != minimal_true_points(n, A)
            for A in antichains
        )
        row = {
            "m": n,
            "monotone_functions": len(antichains),
            "raw_truth_table_bits": 1 << n,
            "exact_class_index_bits": math.ceil(math.log2(len(antichains))),
            "max_minimal_success_witnesses": max(map(len, antichains)),
            "reconstruction_mismatches": mismatches,
        }
        rows.append(row)
        total_functions += len(antichains)
        total_mismatches += mismatches

    result = {
        "audit": 128,
        "rows": rows,
        "total_functions_checked_m1_to_m5": total_functions,
        "total_reconstruction_mismatches": total_mismatches,
        "m5_exhaustive": rows[-1]["monotone_functions"] == 7581,
        "status": "PASS" if total_mismatches == 0 else "FAIL",
    }

    output = Path("gc2/results/audit128_monotone_intervention_antichain.json")
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
