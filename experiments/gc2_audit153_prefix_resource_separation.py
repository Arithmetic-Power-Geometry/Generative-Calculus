"""Audit 153: static net-cost frontier does not determine sequential feasibility.

Exact finite checker. No external dependencies.
"""
from itertools import product, permutations
import json


def feasible(trace, initial=(0,0,0,0)):
    stock=list(initial)
    for delta in trace:
        stock=[x+d for x,d in zip(stock,delta)]
        if any(x < 0 for x in stock):
            return False
    return True


def add(trace):
    return tuple(sum(step[j] for step in trace) for j in range(4))

# Four typed resources R,I,A,L. Each witness has exactly the same action multiset
# and hence the same total/net vector; only precedence differs.
# produce_j adds one unit; consume_j removes one unit.
witnesses=[]
checks=0
for j,name in enumerate("RIAL"):
    plus=tuple(1 if k==j else 0 for k in range(4))
    minus=tuple(-1 if k==j else 0 for k in range(4))
    good=(plus,minus)
    bad=(minus,plus)
    assert add(good)==add(bad)==(0,0,0,0); checks += 1
    assert feasible(good) and not feasible(bad); checks += 1
    witnesses.append({"axis":name,"good":good,"bad":bad,"net":add(good)})

# Exhaust all two-step +/- unit pairs over the four axes and verify feasibility
# directly from every prefix. This checks the generic prefix criterion.
deltas=[]
for j in range(4):
    for s in (-1,1):
        deltas.append(tuple(s if k==j else 0 for k in range(4)))
exhaustive=0
for a,b in product(deltas, repeat=2):
    tr=(a,b)
    stock=[0,0,0,0]
    expected=True
    for step in tr:
        stock=[x+d for x,d in zip(stock,step)]
        expected &= all(x>=0 for x in stock)
    assert feasible(tr)==expected
    exhaustive += 1

out={
  "audit":153,
  "claim":"equal static net-cost frontier does not determine sequential feasibility",
  "witness_axes":4,
  "witness_assertions":checks,
  "exhaustive_two_step_traces":exhaustive,
  "violations":0,
  "status":"PASS",
  "novelty_status":"IMPORTED/KNOWN mechanism; not GC-II novelty"
}
print(json.dumps(out, indent=2))
