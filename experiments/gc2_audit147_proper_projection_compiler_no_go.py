#!/usr/bin/env python3
"""GC-II Audit 147: proper-local-projection compiler no-go.

For q-ary residue worlds R_r={x in Z_q^n : sum_i x_i = r mod q}, every
(n-1)-coordinate projection is the full cube Z_q^(n-1), independent of r,
while the q global worlds are pairwise disjoint. Hence any exact compiler whose
input is only the family of proper projections receives identical input on q
different global relations and cannot reconstruct which world generated it,
regardless of its internal augmented-state cardinality.
"""
from itertools import product
import json


def audit(q_min=2, q_max=6, n_min=2, n_max=7):
    cases = []
    projection_checks = 0
    equality_checks = 0
    disjoint_checks = 0
    join_checks = 0
    violations = []

    for q in range(q_min, q_max + 1):
        for n in range(n_min, n_max + 1):
            universe = list(product(range(q), repeat=n))
            relations = []
            projections = []
            for r in range(q):
                relation = {x for x in universe if sum(x) % q == r}
                relations.append(relation)
                local = []
                for j in range(n):
                    p = {x[:j] + x[j + 1:] for x in relation}
                    local.append(p)
                    projection_checks += 1
                    if len(p) != q ** (n - 1):
                        violations.append(["projection_not_full", q, n, r, j, len(p)])
                projections.append(local)

            for r in range(1, q):
                equality_checks += 1
                if projections[r] != projections[0]:
                    violations.append(["local_views_differ", q, n, r])

            for a in range(q):
                for b in range(a + 1, q):
                    disjoint_checks += 1
                    if not relations[a].isdisjoint(relations[b]):
                        violations.append(["global_worlds_overlap", q, n, a, b])

            joined = {
                x for x in universe
                if all((x[:j] + x[j + 1:]) in projections[0][j] for j in range(n))
            }
            join_checks += 1
            if len(joined) != q ** n:
                violations.append(["join_not_full_cube", q, n, len(joined)])

            cases.append({
                "q": q,
                "n": n,
                "global_universe": q ** n,
                "one_world_size": q ** (n - 1),
                "join_of_proper_projections": len(joined),
                "spurious_factor": len(joined) / len(relations[0]),
                "missing_information_bits": __import__("math").log2(q),
            })

    return {
        "status": "PASS" if not violations else "FAIL",
        "q_range": [q_min, q_max],
        "n_range": [n_min, n_max],
        "parameter_cases": len(cases),
        "projection_checks": projection_checks,
        "local_view_equality_checks": equality_checks,
        "pairwise_disjointness_checks": disjoint_checks,
        "join_checks": join_checks,
        "total_checks": projection_checks + equality_checks + disjoint_checks + join_checks,
        "violations": violations,
        "largest_case": cases[-1],
        "cases": cases,
    }


if __name__ == "__main__":
    print(json.dumps(audit(), indent=2, sort_keys=True))
