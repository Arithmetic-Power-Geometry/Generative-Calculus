from itertools import product, combinations
import json


def project(rel, idx):
    return {tuple(x[i] for i in idx) for x in rel}


def main():
    even = [x for x in product((0, 1), repeat=4) if sum(x) % 2 == 0]
    odd = [x for x in product((0, 1), repeat=4) if sum(x) % 2 == 1]

    checks = []
    all_equal = True
    for k in (1, 2, 3):
        for idx in combinations(range(4), k):
            pe = sorted(project(even, idx))
            po = sorted(project(odd, idx))
            equal = pe == po
            all_equal = all_equal and equal
            checks.append({"dimension": k, "coordinates": idx, "equal": equal, "projection_size": len(pe)})

    result = {
        "ambient_dimension": 4,
        "even_relation_size": len(even),
        "odd_relation_size": len(odd),
        "full_relations_equal": set(even) == set(odd),
        "all_proper_coordinate_projections_equal": all_equal,
        "number_of_proper_projection_checks": len(checks),
        "proper_projection_mismatches": sum(not c["equal"] for c in checks),
        "checks": checks,
    }
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
