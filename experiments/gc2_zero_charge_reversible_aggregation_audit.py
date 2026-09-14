#!/usr/bin/env python3
"""GC-II Audit 132: zero-charge reversible capability-expanding aggregation.

Exact finite counterexample to any claim that operational closure alone forces a
strictly positive charge for every capability-expanding aggregation.
"""
import json
from itertools import product


def toffoli(x, y, z):
    return (x, y, z ^ (x & y))


def main():
    states = list(product((0, 1), repeat=3))
    images = [toffoli(*s) for s in states]
    bijective = len(set(images)) == len(states) and set(images) == set(states)
    involutive = all(toffoli(*toffoli(*s)) == s for s in states)

    # Ancilla z=0: the third output computes conjunction while retaining inputs.
    ancilla_cases = []
    mismatches = 0
    for x, y in product((0, 1), repeat=2):
        out = toffoli(x, y, 0)
        expected = x & y
        ok = out == (x, y, expected)
        mismatches += int(not ok)
        ancilla_cases.append({"x": x, "y": y, "out": list(out), "expected_and": expected, "ok": ok})

    # Abstract GC accounting is permitted to assign zero charge unless a positive
    # operational/physical monotone is independently postulated or derived.
    assigned_charge = 0
    capability_expands = any(c["expected_and"] == 1 for c in ancilla_cases)

    result = {
        "audit": 132,
        "states_checked": len(states),
        "ancilla_cases_checked": len(ancilla_cases),
        "bijective": bijective,
        "involutive": involutive,
        "and_mismatches": mismatches,
        "assigned_charge": assigned_charge,
        "capability_expands": capability_expands,
        "positive_charge_forced_by_bare_operational_closure": False,
        "status": "PASS" if bijective and involutive and mismatches == 0 and capability_expands else "FAIL",
        "cases": ancilla_cases,
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
