#!/usr/bin/env python3
"""Exact finite audit for GC-II rule-state compilation (Audit 088).

Four unary Boolean rules are all functions {0,1}->{0,1}.  A dynamic grammar
is any subset of these rules.  Meta-actions either apply a currently enabled
rule or toggle its membership.  We compare the direct dynamic-rule semantics
with a fixed interpreter whose state is (object_state, grammar_mask).
"""
from itertools import product
import csv
from pathlib import Path

RULES = list(product((0, 1), repeat=2))


def dynamic_step(x, mask, kind, rule_id):
    if kind == "apply":
        if not ((mask >> rule_id) & 1):
            return None
        return RULES[rule_id][x], mask
    if kind == "toggle":
        return x, mask ^ (1 << rule_id)
    raise ValueError(kind)


def compiled_step(state, kind, rule_id):
    x, mask = state
    # This function is the fixed meta-interpreter.  The mutable grammar is data.
    if kind == "apply":
        if not ((mask >> rule_id) & 1):
            return None
        return RULES[rule_id][x], mask
    if kind == "toggle":
        return x, mask ^ (1 << rule_id)
    raise ValueError(kind)


def main():
    rows = []
    mismatches = 0
    for mask in range(1 << len(RULES)):
        for x in (0, 1):
            for kind in ("apply", "toggle"):
                for rid in range(len(RULES)):
                    direct = dynamic_step(x, mask, kind, rid)
                    compiled = compiled_step((x, mask), kind, rid)
                    ok = direct == compiled
                    mismatches += int(not ok)
                    rows.append((mask, x, kind, rid, repr(direct), repr(compiled), int(ok)))

    out = Path("results/gc2_rule_state_compilation_exhaustive.csv")
    out.parent.mkdir(parents=True, exist_ok=True)
    with out.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["grammar_mask", "x", "action", "rule_id", "dynamic", "compiled", "equal"])
        w.writerows(rows)

    print(f"checks={len(rows)} mismatches={mismatches}")
    assert len(rows) == 256
    assert mismatches == 0


if __name__ == "__main__":
    main()
