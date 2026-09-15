#!/usr/bin/env python3
"""GC-II Audit 152: exact coupled-resource witness.

Shows that equality of all four single-axis minima (R,I,A,L) does not determine
joint budget feasibility. This is a boundary test, not a novelty claim.
"""
import itertools, json

S1={(0,2,2,2),(2,0,2,2),(2,2,0,2),(2,2,2,0)}
S2=S1|{(1,1,1,1)}

def axis_min(S,j): return min(v[j] for v in S)
def feasible(S,b): return any(all(x<=y for x,y in zip(v,b)) for v in S)
def pareto(S):
    return {v for v in S if not any(u!=v and all(a<=b for a,b in zip(u,v)) for u in S)}

assert tuple(axis_min(S1,j) for j in range(4)) == (0,0,0,0)
assert tuple(axis_min(S2,j) for j in range(4)) == (0,0,0,0)
assert pareto(S1)==S1 and pareto(S2)==S2

separating=[]
checks=0
for b in itertools.product(range(3), repeat=4):
    checks += 1
    f1,f2=feasible(S1,b),feasible(S2,b)
    if f1!=f2: separating.append((b,f1,f2))
assert separating == [((1,1,1,1),False,True)]

result={
  "status":"PASS",
  "single_axis_minima_S1":[axis_min(S1,j) for j in range(4)],
  "single_axis_minima_S2":[axis_min(S2,j) for j in range(4)],
  "budgets_checked":checks,
  "separating_budgets":[{"budget":list(b),"S1":f1,"S2":f2} for b,f1,f2 in separating],
  "pareto_size_S1":len(pareto(S1)),"pareto_size_S2":len(pareto(S2))
}
print(json.dumps(result,indent=2,sort_keys=True))
