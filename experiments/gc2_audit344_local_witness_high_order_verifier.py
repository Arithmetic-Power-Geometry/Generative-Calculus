"""Exact verifier for GC-II Audit 344.

Parallel two-edge routes show that constant minimal-witness size does not bound
Möbius interaction order. Pure Python, no external dependencies.
"""
from itertools import combinations
import json
from pathlib import Path


def powerset(items):
    items = tuple(items)
    for r in range(len(items) + 1):
        yield from combinations(items, r)


def reaches_st(subset, m):
    chosen = set(subset)
    return any((2*i in chosen and 2*i+1 in chosen) for i in range(m))


def mobius_top(m):
    edges = tuple(range(2*m))
    total = 0
    for S in powerset(edges):
        if reaches_st(S, m):
            total += (-1) ** (len(edges) - len(S))
    return total


def minimal_witnesses(m):
    edges = tuple(range(2*m))
    wins = []
    for S in powerset(edges):
        if not reaches_st(S, m):
            continue
        ss = set(S)
        if all(not reaches_st(tuple(ss - {e}), m) for e in ss):
            wins.append(tuple(sorted(S)))
    return wins


def main():
    rows = []
    failures = []
    for m in range(1, 9):
        ws = minimal_witnesses(m)
        top = mobius_top(m)
        expected_ws = [tuple((2*i, 2*i+1)) for i in range(m)]
        expected_top = (-1) ** (m + 1)
        ok = (ws == expected_ws and top == expected_top and
              max(map(len, ws)) == 2 and len(set().union(*map(set, ws))) == 2*m)
        rows.append({
            "m": m,
            "states": m + 2,
            "new_edges": 2*m,
            "minimal_witness_count": len(ws),
            "max_minimal_witness_size": max(map(len, ws)),
            "witness_union_rank": 2*m,
            "top_interaction_order": 2*m,
            "top_mobius_coefficient": top,
            "expected_coefficient": expected_top,
            "ok": ok,
        })
        if not ok:
            failures.append({"m": m, "witnesses": ws, "top": top})

    result = {
        "audit": 344,
        "family": "m pairwise-disjoint two-edge s-t routes",
        "cases": len(rows),
        "subset_evaluations": sum(2 ** (2*m) for m in range(1, 9)),
        "failures": len(failures),
        "rows": rows,
        "failure_details": failures,
    }
    out = Path("results/gc2_audit344_local_witness_high_order_results.json")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))
    assert not failures


if __name__ == "__main__":
    main()
