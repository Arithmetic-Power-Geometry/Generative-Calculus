#!/usr/bin/env python3
"""Exact verifier for GC-II Audit 341.

Enumerate every labelled preorder on q<=4 and every absent directed edge.
Verify that adding one edge creates exactly
(Pred_B(u) x Succ_B(v)) \ B.
"""
from itertools import product
import json
from pathlib import Path


def closure(n, rel):
    r = set(rel)
    r.update((i, i) for i in range(n))
    changed = True
    while changed:
        changed = False
        add = {(a, d) for (a, b) in r for (c, d) in r if b == c and (a, d) not in r}
        if add:
            r |= add
            changed = True
    return r


def is_preorder(n, rel):
    return all((i, i) in rel for i in range(n)) and closure(n, rel) == rel


def verify(max_q=4):
    summary = {"max_q": max_q, "preorders": 0, "edge_cases": 0, "failures": 0,
               "identity_exposure_failures": 0, "max_exposure": 0, "by_q": {}}
    examples = []
    for n in range(1, max_q + 1):
        pairs = [(i, j) for i in range(n) for j in range(n)]
        diag = {(i, i) for i in range(n)}
        off = [p for p in pairs if p not in diag]
        qpre = qcases = qfail = 0
        for bits in product((0, 1), repeat=len(off)):
            B = diag | {e for e, bit in zip(off, bits) if bit}
            if not is_preorder(n, B):
                continue
            qpre += 1
            summary["preorders"] += 1
            for u, v in off:
                if (u, v) in B:
                    continue
                qcases += 1
                summary["edge_cases"] += 1
                Be = closure(n, B | {(u, v)})
                actual = Be - B
                pred = {x for x in range(n) if (x, u) in B}
                succ = {y for y in range(n) if (v, y) in B}
                predicted = {(x, y) for x in pred for y in succ} - B
                exposure = len(predicted)
                summary["max_exposure"] = max(summary["max_exposure"], exposure)
                ok = actual == predicted and len(actual) <= len(pred) * len(succ)
                if not ok:
                    qfail += 1
                    summary["failures"] += 1
                    examples.append({"q": n, "edge": [u, v], "B": sorted(B),
                                     "actual": sorted(actual), "predicted": sorted(predicted)})
        # identity baseline must give exposure exactly one for every absent edge
        I = diag
        for u, v in off:
            pred = {x for x in range(n) if (x, u) in I}
            succ = {y for y in range(n) if (v, y) in I}
            if len(({(x, y) for x in pred for y in succ} - I)) != 1:
                summary["identity_exposure_failures"] += 1
        summary["by_q"][str(n)] = {"preorders": qpre, "absent_edge_cases": qcases, "failures": qfail}
    summary["examples"] = examples[:10]
    return summary


if __name__ == "__main__":
    out = verify()
    path = Path("results/gc2_audit341_single_edge_rectangle.json")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(out, indent=2) + "\n")
    print(json.dumps(out, indent=2))
    if out["failures"] or out["identity_exposure_failures"]:
        raise SystemExit(1)
