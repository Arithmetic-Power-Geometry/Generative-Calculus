from itertools import product
import json


def point_and(f, g):
    return tuple(a & b for a, b in zip(f, g))


def point_or(f, g):
    return tuple(a | b for a, b in zip(f, g))


def main():
    funcs = [tuple(bits) for bits in product([0, 1], repeat=4)]
    x = (0, 0, 1, 1)
    y = (0, 1, 0, 1)
    c0 = (0, 0, 0, 0)
    c1 = (1, 1, 1, 1)

    closure = {x, y, c0, c1}
    changed = True
    while changed:
        changed = False
        current = list(closure)
        for f in current:
            for g in current:
                for h in (point_and(f, g), point_or(f, g)):
                    if h not in closure:
                        closure.add(h)
                        changed = True

    outside = sorted(set(funcs) - closure)
    result = {
        "universe": "all Boolean functions f:{0,1}^2->{0,1}",
        "total_functions": 16,
        "internal_library": ["x", "y", "0", "1", "AND", "OR"],
        "internal_extensional_closure_size": len(closure),
        "outside_internal_closure": len(outside),
        "external_tabular_metalanguage_bits_per_function": 4,
        "all_outside_functions_finitely_describable_externally": len(outside),
        "truth_tables_outside": ["".join(map(str, f)) for f in outside],
        "claim_checked": (
            "Internal non-definability does not imply external indescribability; "
            "each excluded 2-input Boolean primitive has a 4-bit truth-table "
            "description in the fixed external metalanguage."
        ),
    }

    assert result["internal_extensional_closure_size"] == 6
    assert result["outside_internal_closure"] == 10
    assert result["all_outside_functions_finitely_describable_externally"] == 10
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
