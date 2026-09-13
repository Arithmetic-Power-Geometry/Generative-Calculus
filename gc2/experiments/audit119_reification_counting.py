"""Exact finite check for GC-II Audit 119.

For M=1..64, enumerate all fixed codeword lengths L around ceil(log2 M)
and verify the pigeonhole feasibility criterion M <= 2**L. This is not a
proof substitute; it is an executable edge-case regression for the theorem.
"""
from __future__ import annotations
import json
import math
from pathlib import Path

rows=[]
violations=[]
for M in range(1,65):
    optimum=math.ceil(math.log2(M)) if M>1 else 0
    for L in range(0,8):
        feasible=M <= (1 << L)
        predicted=L >= optimum
        row={"M":M,"L":L,"feasible":feasible,"predicted":predicted,"optimum":optimum}
        rows.append(row)
        if feasible != predicted:
            violations.append(row)

result={
    "audit":119,
    "semantic_family_sizes_checked":64,
    "length_cases_checked":len(rows),
    "violations":len(violations),
    "max_M":64,
    "claim":"fixed-length injective binary reification has optimum ceil(log2 M)",
}
out=Path(__file__).with_name("audit119_reification_counting_results.json")
out.write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
print(json.dumps(result,indent=2))
assert not violations
