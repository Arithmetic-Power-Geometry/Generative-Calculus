"""GC-II Audit 144: exact regression for generated-action interpreter compilation.

Tiny worlds generate fresh integer-labeled action descriptions. Native semantics and
a fixed EXECUTE(d) interpreter are compared exhaustively over deterministic update
rules. This tests the implementation of the proof idea; the theorem is by induction.
"""
from itertools import product
import json
from pathlib import Path

X = (0, 1)
DESCS = (0, 1, 2)
HORIZON = 4

# Enabled sets represented by masks. We exhaustively enumerate a compact family in
# which executing d flips x according to one rule bit and updates the enabled mask
# according to a table indexed by (x,d). This includes creation/deletion/self-renewal.
STARTS = [(x, m) for x in X for m in range(1 << len(DESCS))]
SLOTS = [(x, d) for x in X for d in DESCS]


def native_histories(effect_bits, mask_rule, start):
    frontier = [(start, ())]
    seen = {((), start)}
    for _ in range(HORIZON):
        nxt = []
        for (x, mask), hist in frontier:
            for d in DESCS:
                if (mask >> d) & 1:
                    x2 = x ^ effect_bits[d]
                    m2 = mask_rule[(x, d)]
                    h2 = hist + (d,)
                    seen.add((h2, (x2, m2)))
                    nxt.append(((x2, m2), h2))
        frontier = nxt
    return seen


def compiled_histories(effect_bits, mask_rule, start):
    # Single fixed schema EXECUTE(d); d is data and availability is state-dependent.
    def execute(state, d):
        x, mask = state
        if not ((mask >> d) & 1):
            return None
        return (x ^ effect_bits[d], mask_rule[(x, d)])

    frontier = [(start, ())]
    seen = {((), start)}
    for _ in range(HORIZON):
        nxt = []
        for state, hist in frontier:
            for d in DESCS:
                state2 = execute(state, d)
                if state2 is not None:
                    h2 = hist + (d,)
                    seen.add((h2, state2))
                    nxt.append((state2, h2))
        frontier = nxt
    return seen


def run():
    checks = mismatches = rules = 0
    # 8 effect rules x 8^6 enabled-set update tables = 2,097,152 tables would be
    # excessive for CI. Exhaustively enumerate all effect rules and all 2^6 binary
    # generator choices between two masks (0 and 7), giving 512 rule pairs; this
    # still covers deadlock and full regeneration at every slot.
    for effect_bits in product((0, 1), repeat=len(DESCS)):
        for choices in product((0, 7), repeat=len(SLOTS)):
            mask_rule = dict(zip(SLOTS, choices))
            rules += 1
            for start in STARTS:
                checks += 1
                if native_histories(effect_bits, mask_rule, start) != compiled_histories(effect_bits, mask_rule, start):
                    mismatches += 1
    result = {
        "audit": 144,
        "rules_exhaustively_enumerated": rules,
        "start_state_checks": checks,
        "horizon": HORIZON,
        "history_state_semantics_mismatches": mismatches,
        "status": "PASS" if mismatches == 0 else "COUNTEREXAMPLE_FOUND",
        "scope": "Finite regression for implementation; general fixed-interpreter compilation is proved separately by induction.",
    }
    return result


if __name__ == "__main__":
    result = run()
    print(json.dumps(result, indent=2, sort_keys=True))
    out = Path("results/gc2_audit144_generated_action_interpreter.json")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
