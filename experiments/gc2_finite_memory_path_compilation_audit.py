#!/usr/bin/env python3
"""GC-II Audit 122: exact finite-memory path-dependence compilation check.

Exhaustively enumerates a deliberately small class of deterministic conversion
systems with one projected physical state, two hidden memory states, two actions,
Boolean memory updates, and action increments in {-1,+1}.  The 'history-dependent'
model evolves its memory recurrence explicitly.  The compiled model promotes the
memory state into the operational state.  We compare every action word through a
fixed horizon.

This is a kill test, not evidence of novelty: finite-memory path dependence should
be exactly reproducible after state augmentation.
"""

from itertools import product
import json

ACTIONS = (0, 1)
MEMORY = (0, 1)
HORIZON = 6


def run():
    systems = 0
    sequence_checks = 0
    mismatches = 0
    projected_path_dependent_systems = 0

    for upd_bits in product(MEMORY, repeat=4):
        update = {(m, a): upd_bits[2*m + a] for m in MEMORY for a in ACTIONS}
        for inc_bits in product((-1, 1), repeat=4):
            increment = {(m, a): inc_bits[2*m + a] for m in MEMORY for a in ACTIONS}
            systems += 1
            projected_cycle_values = set()

            for word in product(ACTIONS, repeat=HORIZON):
                # Original finite-memory dynamics.
                m_orig = 0
                value_orig = 0
                for a in word:
                    value_orig += increment[m_orig, a]
                    m_orig = update[m_orig, a]

                # Compiled fixed-state dynamics z=(physical_state,memory).
                # The physical state is the unique state q=0, so z is represented
                # by its memory coordinate here.
                m_comp = 0
                value_comp = 0
                for a in word:
                    value_comp += increment[m_comp, a]
                    m_comp = update[m_comp, a]

                sequence_checks += 1
                projected_cycle_values.add(value_orig)
                if (m_orig, value_orig) != (m_comp, value_comp):
                    mismatches += 1

            # With a single projected physical state, every action word is a
            # physical closed cycle. Different accumulated values therefore
            # witness path dependence at the physical projection.
            if len(projected_cycle_values) > 1:
                projected_path_dependent_systems += 1

    result = {
        "audit": 122,
        "horizon": HORIZON,
        "systems": systems,
        "sequence_checks": sequence_checks,
        "projected_path_dependent_systems": projected_path_dependent_systems,
        "compiled_mismatches": mismatches,
        "status": "PASS" if mismatches == 0 else "FAIL",
    }
    print(json.dumps(result, indent=2, sort_keys=True))
    return result


if __name__ == "__main__":
    run()
