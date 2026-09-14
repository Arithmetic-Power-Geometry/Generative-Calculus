"""GC-II Audit 148: exact finite check for separator-acquisition lower bound.

For residue worlds R_r={x in Z_q^n: sum(x)=r mod q}, verify that no proper
coordinate-query subset determines r, while the full coordinate set does.
"""
from itertools import product, combinations
import json


def signatures(q, n, subset):
    seen = {}
    collision = False
    for x in product(range(q), repeat=n):
        sig = tuple(x[i] for i in subset)
        r = sum(x) % q
        old = seen.get(sig)
        if old is None:
            seen[sig] = r
        elif old != r:
            collision = True
            break
    return collision


def run():
    subset_checks = 0
    proper_collisions = 0
    full_separates = 0
    violations = []
    cases = 0
    for q in range(2, 6):
        for n in range(2, 7):
            cases += 1
            for k in range(n + 1):
                for subset in combinations(range(n), k):
                    subset_checks += 1
                    collision = signatures(q, n, subset)
                    if k < n:
                        if collision:
                            proper_collisions += 1
                        else:
                            violations.append([q, n, list(subset), "proper_subset_separates"])
                    else:
                        if not collision:
                            full_separates += 1
                        else:
                            violations.append([q, n, list(subset), "full_subset_collides"])
    result = {
        "audit": 148,
        "q_range": [2, 5],
        "n_range": [2, 6],
        "parameter_cases": cases,
        "subset_checks": subset_checks,
        "proper_subset_collision_checks_passed": proper_collisions,
        "full_set_separation_checks_passed": full_separates,
        "violations": len(violations),
        "violation_examples": violations[:10],
        "status": "PASS" if not violations else "FAIL",
    }
    print(json.dumps(result, indent=2))
    return result


if __name__ == "__main__":
    run()
