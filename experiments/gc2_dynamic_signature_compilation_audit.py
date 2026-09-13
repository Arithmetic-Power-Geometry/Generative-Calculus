"""Audit 118: exhaustive bounded dynamic-signature compilation test.

A dynamic-signature machine has a finite control state q and a currently active
subset S of a fixed action universe A. Executing an active action may change
both q and S. The compilation reifies S into ordinary state (q, mask(S)) and
uses one fixed action alphabet A. We exhaustively compare finite action-history
semantics for all tiny deterministic machines in the parameter families below.
"""
from itertools import product
import json
from pathlib import Path

HORIZON = 5
FAMILIES = [(1, 1), (2, 1), (1, 2)]


def configs(nq, na):
    return [(q, mask) for q in range(nq) for mask in range(1 << na)]


def enabled_slots(nq, na):
    return [
        (q, mask, a)
        for q, mask in configs(nq, na)
        for a in range(na)
        if (mask >> a) & 1
    ]


def dynamic_histories(rule, nq, na, start, horizon):
    frontier = [(start, ())]
    histories = {()}
    for _ in range(horizon):
        nxt_frontier = []
        for (q, mask), trace in frontier:
            for a in range(na):
                if (mask >> a) & 1:
                    nxt = rule[(q, mask, a)]
                    nxt_trace = trace + (a,)
                    histories.add(nxt_trace)
                    nxt_frontier.append((nxt, nxt_trace))
        frontier = nxt_frontier
    return histories


def compiled_histories(rule, nq, na, start, horizon):
    # Fixed alphabet; signature availability is represented entirely in state.
    transition = {}
    for q, mask in configs(nq, na):
        transition[(q, mask)] = {
            a: rule[(q, mask, a)]
            for a in range(na)
            if (mask >> a) & 1
        }

    frontier = [(start, ())]
    histories = {()}
    for _ in range(horizon):
        nxt_frontier = []
        for state, trace in frontier:
            for a, nxt in transition[state].items():
                nxt_trace = trace + (a,)
                histories.add(nxt_trace)
                nxt_frontier.append((nxt, nxt_trace))
        frontier = nxt_frontier
    return histories


def run():
    families = []
    total_machines = 0
    total_start_checks = 0
    total_mismatches = 0

    for nq, na in FAMILIES:
        states = configs(nq, na)
        slots = enabled_slots(nq, na)
        machine_count = len(states) ** len(slots)
        mismatches = 0
        start_checks = 0

        for outputs in product(states, repeat=len(slots)):
            rule = dict(zip(slots, outputs))
            for start in states:
                start_checks += 1
                d = dynamic_histories(rule, nq, na, start, HORIZON)
                c = compiled_histories(rule, nq, na, start, HORIZON)
                if d != c:
                    mismatches += 1

        families.append({
            "control_states": nq,
            "action_universe_size": na,
            "compiled_states": len(states),
            "enabled_rule_slots": len(slots),
            "machines_exhaustively_enumerated": machine_count,
            "start_state_checks": start_checks,
            "horizon": HORIZON,
            "history_semantics_mismatches": mismatches,
        })
        total_machines += machine_count
        total_start_checks += start_checks
        total_mismatches += mismatches

    result = {
        "audit": 118,
        "claim_tested": "bounded dynamic signatures compile exactly into fixed-signature state machines",
        "families": families,
        "totals": {
            "machines_exhaustively_enumerated": total_machines,
            "start_state_checks": total_start_checks,
            "history_semantics_mismatches": total_mismatches,
        },
        "status": "SUPPORTED_BY_EXHAUSTIVE_FINITE_TEST" if total_mismatches == 0 else "COUNTEREXAMPLE_FOUND",
        "scope_note": "This experiment validates the finite bounded-vocabulary compilation only; it does not prove claims about genuinely unbounded fresh semantic primitives.",
    }
    return result


if __name__ == "__main__":
    result = run()
    print(json.dumps(result, indent=2, sort_keys=True))
    out = Path("results/gc2_dynamic_signature_compilation_audit.json")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
