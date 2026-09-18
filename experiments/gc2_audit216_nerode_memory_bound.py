"""GC-II Audit 216: exact finite deterministic memory-bound verifier.

Enumerates every 2-state binary-input Moore machine (64 total), computes
reachable future-equivalence classes by partition refinement, constructs the
quotient, and verifies exact behavior through all words of length <= 6.
No external packages required.
"""
from itertools import product
from collections import deque

A=(0,1)

def reach(delta):
    seen={0}; q=deque([0])
    while q:
        s=q.popleft()
        for a in A:
            t=delta[s][a]
            if t not in seen: seen.add(t); q.append(t)
    return seen

def refine(delta,out,R):
    part={s:out[s] for s in R}
    while True:
        sig={s:(out[s],tuple(part[delta[s][a]] for a in A)) for s in R}
        vals={v:i for i,v in enumerate(sorted(set(sig.values())))}
        new={s:vals[sig[s]] for s in R}
        if all(new[s]==part[s] for s in R): return new
        part=new

def words(n):
    yield ()
    for k in range(1,n+1): yield from product(A, repeat=k)

def trace(delta,out,w):
    s=0; z=[out[s]]
    for a in w: s=delta[s][a]; z.append(out[s])
    return tuple(z)

def check(delta,out):
    R=reach(delta); p=refine(delta,out,R); N=len(set(p.values()))
    # quotient transitions/outputs are well-defined
    classes={c:[s for s in R if p[s]==c] for c in set(p.values())}
    qout={c:out[ss[0]] for c,ss in classes.items()}
    qdelta={}
    for c,ss in classes.items():
        qdelta[c]={}
        for a in A:
            targets={p[delta[s][a]] for s in ss}
            assert len(targets)==1
            qdelta[c][a]=targets.pop()
    q0=p[0]
    for w in words(6):
        s=0; c=q0; t1=[out[s]]; t2=[qout[c]]
        for a in w:
            s=delta[s][a]; c=qdelta[c][a]
            t1.append(out[s]); t2.append(qout[c])
        assert t1==t2
    return len(R),N

total=0; collapsed=0; nontrivial=0
for transbits in product((0,1), repeat=4):
    delta={0:{0:transbits[0],1:transbits[1]},1:{0:transbits[2],1:transbits[3]}}
    for outs in product((0,1), repeat=2):
        out={0:outs[0],1:outs[1]}
        r,n=check(delta,out); total+=1
        if n<r: collapsed+=1
        if n>1: nontrivial+=1
print({'machines':total,'behaviorally_collapsed':collapsed,'N_gt_1':nontrivial,'status':'PASS'})
assert total==64
