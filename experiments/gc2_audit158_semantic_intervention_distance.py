"""GC-II Audit 158: finite regression for a semantic intervention hemimetric.

World: a capability closure is a subset of {0,1,2,3}.  The directed intervention
cost d(A,B)=|B\\A| is the minimum number of missing capabilities that must be
adjoined to make B reachable from A.  This is deliberately simple: the audit
checks the algebraic boundary, not a novelty claim.
"""
from itertools import product
import json

U = tuple(range(4))
closures = [frozenset(i for i in U if (mask >> i) & 1) for mask in range(1 << len(U))]

def d(a, b):
    return len(b - a)

zero_preorder_violations = 0
triangle_violations = 0
for a, b in product(closures, repeat=2):
    # zero directed distance iff target closure is already contained in source.
    zero_preorder_violations += int((d(a,b) == 0) != (b <= a))
for a, b, c in product(closures, repeat=3):
    triangle_violations += int(d(a,c) > d(a,b) + d(b,c))

result = {
    "audit": 158,
    "closures": len(closures),
    "ordered_pairs": len(closures)**2,
    "ordered_triples": len(closures)**3,
    "zero_preorder_violations": zero_preorder_violations,
    "triangle_violations": triangle_violations,
    "status": "PASS" if zero_preorder_violations == triangle_violations == 0 else "FAIL",
}
print(json.dumps(result, indent=2, sort_keys=True))
