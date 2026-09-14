#!/usr/bin/env python3
"""GC-II Audit 140: raw transcript-support deficit is not capability sufficient.

Enumerates every deterministic binary sensor f:{0,1}x{0,1}->{0,1}, where the first
bit is the task/capability class and the second is a nuisance variable.  The proposed
raw support deficit D = log2(b)-log2(|T_realizable|) is compared with exact class
identifiability, defined by disjoint class-conditioned transcript supports.
"""
import itertools
import json
import math
from pathlib import Path

records = []
for outputs in itertools.product((0, 1), repeat=4):
    supports = {0: set(), 1: set()}
    for c in (0, 1):
        for nuisance in (0, 1):
            supports[c].add(outputs[2 * c + nuisance])
    global_support = set(outputs)
    deficit = math.log2(2) - math.log2(len(global_support))
    exact = supports[0].isdisjoint(supports[1])
    records.append({
        "outputs": list(outputs),
        "class_supports": {str(c): sorted(supports[c]) for c in (0, 1)},
        "global_support_size": len(global_support),
        "raw_deficit_bits": deficit,
        "exact_identifiable": exact,
    })

maximal_support = [r for r in records if r["global_support_size"] == 2]
maximal_exact = [r for r in maximal_support if r["exact_identifiable"]]
maximal_inexact = [r for r in maximal_support if not r["exact_identifiable"]]

result = {
    "audit": 140,
    "status": "FALSIFIED_RAW_SUPPORT_DEFICIT",
    "claim_falsified": "D_G = log2(nominal transcript capacity) - log2(global realizable transcript support) is sufficient to measure exact task capability.",
    "sensor_count": len(records),
    "maximal_global_support_count": len(maximal_support),
    "maximal_support_exact_count": len(maximal_exact),
    "maximal_support_inexact_count": len(maximal_inexact),
    "same_D_zero_both_exact_and_inexact": bool(maximal_exact and maximal_inexact),
    "informative_witness": maximal_exact[0],
    "uninformative_or_confounded_witness": maximal_inexact[0],
    "violations": 0 if (maximal_exact and maximal_inexact) else 1,
}

assert result["sensor_count"] == 16
assert result["maximal_global_support_count"] == 14
assert result["maximal_support_exact_count"] == 2
assert result["maximal_support_inexact_count"] == 12
assert result["same_D_zero_both_exact_and_inexact"]
assert result["violations"] == 0

out = Path("results/gc2_audit140_transcript_support_counterexample.json")
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
