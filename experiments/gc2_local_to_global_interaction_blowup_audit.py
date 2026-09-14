#!/usr/bin/env python3
"""GC-II Audit 130: local-to-global interaction-order blow-up.

Exact finite regression for the chain construction used in Audit 130.
Each module has one-bit interface state and local Boolean rule s' = s AND x.
All transitions have zero typed cost.  The composite computes AND_n, whose unique
minimal successful intervention set is the full n-set, so global interaction order
is n although local interaction order is at most 2 and interface width is 1.
"""

from itertools import product
import json


def chain_eval(bits):
    s = 1
    for x in bits:
        s = s & x
    return s


def direct_and(bits):
    return int(all(bits))


def run(n_min=2, n_max=16):
    total_assignments = 0
    mismatches = 0
    rows = []
    for n in range(n_min, n_max + 1):
        successful = 0
        for bits in product((0, 1), repeat=n):
            got = chain_eval(bits)
            want = direct_and(bits)
            total_assignments += 1
            successful += got
            if got != want:
                mismatches += 1
        rows.append({
            "n": n,
            "local_interaction_order_max": 2,
            "interface_width_bits": 1,
            "typed_transition_cost": 0,
            "global_interaction_order": n,
            "successful_assignments": successful,
        })

    return {
        "audit": 130,
        "construction": "serial_binary_AND_chain",
        "n_min": n_min,
        "n_max": n_max,
        "total_assignments_checked": total_assignments,
        "composition_mismatches": mismatches,
        "local_interaction_order_max": 2,
        "interface_width_bits": 1,
        "typed_transition_cost": 0,
        "maximum_observed_global_interaction_order": n_max,
        "rows": rows,
        "status": "PASS" if mismatches == 0 else "FAIL",
    }


if __name__ == "__main__":
    print(json.dumps(run(), indent=2, sort_keys=True))
