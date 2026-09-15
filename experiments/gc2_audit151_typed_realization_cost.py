"""GC-II Audit 151: exact synthesis costs for all two-input Boolean functions.

Shows that identical extensional capability / residual quotient can have different
minimum typed realization costs solely because the primitive interface library differs.
This is a controlled collision test, not a novelty claim.
"""
from collections import deque
import json

MASK = 0b1111
X = 0b1100
Y = 0b1010
LIBRARIES = {
    "NAND": {"NAND"},
    "AON": {"AND", "OR", "NOT"},
    "XAN": {"XOR", "AND", "NOT"},
}


def exact_costs(lib, max_gates=8):
    initial = frozenset((X, Y))
    queue = deque([(initial, 0)])
    seen = {initial: 0}
    best = {X: 0, Y: 0}
    while queue:
        state, depth = queue.popleft()
        if depth >= max_gates:
            continue
        vals = list(state)
        outputs = set()
        if "NOT" in lib:
            outputs.update(MASK ^ a for a in vals)
        for a in vals:
            for b in vals:
                if "AND" in lib: outputs.add(a & b)
                if "OR" in lib: outputs.add(a | b)
                if "NAND" in lib: outputs.add(MASK ^ (a & b))
                if "XOR" in lib: outputs.add(a ^ b)
        for out in outputs:
            best.setdefault(out, depth + 1)
            nxt = frozenset((*vals, out))
            if nxt not in seen:
                seen[nxt] = depth + 1
                queue.append((nxt, depth + 1))
    return best


def main():
    costs = {name: exact_costs(lib) for name, lib in LIBRARIES.items()}
    assert all(len(v) == 16 for v in costs.values())
    xor = X ^ Y
    assert costs["NAND"][xor] == 4
    assert costs["AON"][xor] == 4
    assert costs["XAN"][xor] == 1
    result = {
        "status": "PASS",
        "functions_exactly_synthesized_per_library": {k: len(v) for k, v in costs.items()},
        "xor_truth_table": format(xor, "04b"),
        "xor_min_gate_cost": {k: v[xor] for k, v in costs.items()},
        "all_costs": {k: {format(f, "04b"): c for f, c in sorted(v.items())} for k, v in costs.items()},
    }
    print(json.dumps(result, indent=2, sort_keys=True))

if __name__ == "__main__":
    main()
