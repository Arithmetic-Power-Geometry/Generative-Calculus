"""Audit 265: exact checks for the typed Pareto interface quotient.

Enumerates finite two-coordinate nonnegative vector-cost modules and contexts,
replaces each module by its boundary Pareto frontier, and checks equality of
all visible Pareto frontiers after gluing. Also checks a fixed-scalarisation
collision.
"""
from itertools import product

B=(0,1)
VISIBLE=(0,1,3)
MODULE_PAIRS=[(i,j) for i in range(3) for j in range(3) if i!=j]
CONTEXT_PAIRS=[(i,j) for i in VISIBLE for j in VISIBLE if i!=j]
MCHOICES=[None,(0,0),(1,0)]
CCHOICES=[None,(0,0),(0,1)]

def pareto(vectors):
    vals=set(vectors)
    return tuple(sorted(v for v in vals if not any(
        w!=v and w[0]<=v[0] and w[1]<=v[1] for w in vals)))

def path_vectors(n, multiedges, s, t):
    if s==t:
        return [(0,0)]
    out=[]
    def dfs(u, seen, acc):
        if u==t:
            out.append(acc)
            return
        for (a,b), costs in multiedges.items():
            if a==u and b not in seen:
                for c in costs:
                    dfs(b, seen|{b}, (acc[0]+c[0],acc[1]+c[1]))
    dfs(s,{s},(0,0))
    return out

def merge(a,b):
    out={e:list(cs) for e,cs in a.items()}
    for e,cs in b.items():
        out.setdefault(e,[]).extend(cs)
    return out

contexts=[]
for assignment in product(CCHOICES, repeat=len(CONTEXT_PAIRS)):
    contexts.append({p:[c] for p,c in zip(CONTEXT_PAIRS,assignment)
                     if c is not None})

checks=0
modules=0
for assignment in product(MCHOICES, repeat=len(MODULE_PAIRS)):
    M={p:[c] for p,c in zip(MODULE_PAIRS,assignment) if c is not None}
    K={}
    for i in B:
        for j in B:
            if i!=j:
                frontier=pareto(path_vectors(3,M,i,j))
                if frontier:
                    K[(i,j)]=list(frontier)
    for C in contexts:
        G=merge(M,C)
        H=merge(K,C)
        for x in VISIBLE:
            for y in VISIBLE:
                assert pareto(path_vectors(4,G,x,y)) == pareto(path_vectors(4,H,x,y))
                checks+=1
    modules+=1

# A fixed scalarisation w=(1,1) cannot preserve typed budget semantics.
frontier_M=pareto([(0,2),(2,0)])
frontier_N=pareto([(1,1)])
assert min(sum(v) for v in frontier_M)==min(sum(v) for v in frontier_N)==2
budget=(1,1)
feasible_M=any(v[0]<=budget[0] and v[1]<=budget[1] for v in frontier_M)
feasible_N=any(v[0]<=budget[0] and v[1]<=budget[1] for v in frontier_N)
assert not feasible_M and feasible_N

assert modules==729
assert len(contexts)==729
assert checks==4782969
print({"audit":265,"modules":modules,"contexts":len(contexts),
       "visible_frontier_equalities":checks,
       "scalarisation_collision":"passed"})
