#!/usr/bin/env python3
"""Exact verifier for GC-II Audit 282.

Checks that the Audit-281 matching family has exponentially many distinct
signatures under unary threshold queries, while distinct attainable vectors
cannot multiplicatively represent one another when r > alpha.
Integer arithmetic only.
"""
from itertools import product
import json


def vec(bits, r):
    out = []
    for b in bits:
        out.extend((r, 1) if b == 0 else (1, r))
    return tuple(out)


def unary_signature(y, threshold=1):
    return tuple(int(v <= threshold) for v in y)


def covers(rep, target, alpha):
    return all(a <= alpha * b for a, b in zip(rep, target))


def run(max_m=10, alpha=2, r=3):
    assert r > alpha >= 1
    rows = []
    total_targets = 0
    ordered_pairs = 0
    query_collision_pairs = 0
    cover_violations = 0

    for m in range(1, max_m + 1):
        ys = [vec(bits, r) for bits in product((0, 1), repeat=m)]
        sigs = [unary_signature(y) for y in ys]
        assert len(ys) == 2 ** m
        assert len(set(sigs)) == len(ys)

        local_collisions = 0
        local_covers = 0
        for i, a in enumerate(ys):
            assert covers(a, a, alpha)
            for j, b in enumerate(ys):
                if i == j:
                    continue
                ordered_pairs += 1
                if sigs[i] == sigs[j]:
                    local_collisions += 1
                if covers(a, b, alpha):
                    local_covers += 1

        query_collision_pairs += local_collisions
        cover_violations += local_covers
        total_targets += len(ys)
        rows.append({
            "m": m,
            "d": 2 * m,
            "query_arity": 1,
            "unary_queries": 2 * m,
            "targets": len(ys),
            "distinct_query_signatures": len(set(sigs)),
            "required_certificate_size": len(ys),
            "signature_collision_pairs": local_collisions,
            "distinct_pair_cover_violations": local_covers,
        })

    assert query_collision_pairs == 0
    assert cover_violations == 0
    result = {
        "audit": 282,
        "status": "PROVED_BY_ARGUMENT_AND_EXACT_FINITE_CHECK",
        "alpha": alpha,
        "r": r,
        "max_m": max_m,
        "total_targets_checked": total_targets,
        "ordered_distinct_pairs_checked": ordered_pairs,
        "signature_collision_pairs": query_collision_pairs,
        "cover_violations": cover_violations,
        "rows": rows,
    }
    print(json.dumps(result, indent=2))
    return result


if __name__ == "__main__":
    run()
