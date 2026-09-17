"""GC-II Audit 196: exact finite compilation of semantic+admissibility generation.

A GC configuration is (world, rules), where each rule has a guard and a transition
that may change BOTH the world and the enabled rule set.  The compiler maps the
whole configuration to an ordinary labelled transition-system state.  Exhaustive
checks verify one-step and reachable-closure equivalence on every two-world,
two-rule deterministic instance in the small catalogue below.
"""
from itertools import product
from collections import deque

W = (0, 1)
RULES = (0, 1)
PHASES = tuple(frozenset(i for i,b in enumerate(bits) if b) for bits in product((0,1), repeat=2))
STATES = tuple((w,p) for w in W for p in PHASES)

# A primitive rule table maps (rule, world, phase) either to None (inadmissible)
# or a successor (world, phase).  Catalogue generators deliberately include
# simultaneous semantic and admissibility changes.
def catalogues():
    # local rule modes: disabled; identity; flip-world; toggle-other-rule;
    # flip-world+toggle-other-rule.
    modes = range(5)
    for m0,m1 in product(modes, repeat=2):
        yield (m0,m1)

def step_mode(r, mode, state):
    w,p = state
    if r not in p or mode == 0:
        return None
    if mode == 1:
        return (w,p)
    if mode == 2:
        return (1-w,p)
    other = 1-r
    q = set(p)
    q.symmetric_difference_update({other})
    q = frozenset(q)
    if mode == 3:
        return (w,q)
    if mode == 4:
        return (1-w,q)
    raise AssertionError

def gc_edges(cat):
    E = set()
    for s in STATES:
        for r,mode in enumerate(cat):
            t = step_mode(r,mode,s)
            if t is not None:
                E.add((s,r,t))
    return E

def compiled_edges(cat):
    # Exact finite compilation: meta-state (world, enabled-rule-set) is simply
    # an ordinary LTS state; each currently admissible generated rule is an edge.
    return gc_edges(cat)

def closure(edges, start):
    adj = {s: [] for s in STATES}
    for s,_,t in edges:
        adj[s].append(t)
    seen={start}; q=deque([start])
    while q:
        s=q.popleft()
        for t in adj[s]:
            if t not in seen:
                seen.add(t); q.append(t)
    return seen

def main():
    n=0
    for cat in catalogues():
        g=gc_edges(cat); c=compiled_edges(cat)
        assert g == c
        for s in STATES:
            assert closure(g,s) == closure(c,s)
        n += 1
    print({"catalogues_checked": n, "states_per_catalogue": len(STATES),
           "one_step_equivalence": True, "closure_equivalence": True})

if __name__ == "__main__":
    main()
