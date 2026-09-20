#!/usr/bin/env python3
"""Exact verifier for GC-II Audit 281.

Checks the treewidth-one matching construction and the private-target
multiplicative certificate obstruction using integer arithmetic.
"""
from itertools import product
import json


def vec(bits, r):
    out = []
    for b in bits:
        out.extend((r, 1) if b == 0 else (1, r))
    return tuple(out)


def covers(rep, target, alpha):
    return all(a <= alpha * b for a, b in zip(rep, target))


def run(max_m=10, alpha=2, r=3):
    assert r > alpha >= 1
    rows = []
    total_targets = 0
    ordered_distinct = 0
    violations = 0
    for m in range(1, max_m + 1):
        ys = [vec(bits, r) for bits in product((0, 1), repeat=m)]
        assert len(set(ys)) == 2 ** m
        local_violations = 0
        for i, a in enumerate(ys):
            assert covers(a, a, alpha)
            for j, b in enumerate(ys):
                if i == j:
                    continue
                ordered_distinct += 1
                if covers(a, b, alpha):
                    local_violations += 1
        violations += local_violations
        total_targets += len(ys)
        rows.append({
            "m": m,
            "d": 2 * m,
            "dependency_graph": "matching",
            "treewidth": 1,
            "targets": len(ys),
            "required_certificate_size": len(ys),
            "distinct_pair_cover_violations": local_violations,
        })
    assert violations == 0
    result = {
        "audit": 281,
        "status": "PROVED_BY_ARGUMENT_AND_EXACT_FINITE_CHECK",
        "alpha": alpha,
        "r": r,
        "max_m": max_m,
        "total_targets_checked": total_targets,
        "ordered_distinct_pairs_checked": ordered_distinct,
        "violations": violations,
        "rows": rows,
    }
    print(json.dumps(result, indent=2))
    return result


if __name__ == "__main__":
    run()
