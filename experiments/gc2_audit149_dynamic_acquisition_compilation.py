"""GC-II Audit 149: dynamic acquisition grammar compilation boundary.

Exhaustively verifies that a finite hidden-world acquisition process in which each
query can change which queries are subsequently available is represented exactly
by its belief/history state.  No third-party packages required.
"""
from itertools import product
import json

# Two hidden worlds {0,1}, two query names {0,1}, horizon 3.
# A rule table entry for (world, enabled-mask, query) is (answer,new-mask),
# but only enabled queries are executable. We enumerate a controlled complete
# family where answer is binary and the new mask is one of 0..3.
# To keep exhaustive size modest, transition semantics are parameterized by
# four bits: answers a_q(w), and two 2-bit masks m_q(answer).

def histories_direct(ans, nxt, h=3):
    out = {(w, 3, ()): (w, 3) for w in (0,1)}
    frontier = [(w,3,()) for w in (0,1)]
    for _ in range(h):
        nf=[]
        for w,mask,hist in frontier:
            for q in (0,1):
                if mask & (1<<q):
                    a=ans[q][w]
                    nm=nxt[q][a]
                    nh=hist+((q,a),)
                    out[(w,nm,nh)]=(w,nm)
                    nf.append((w,nm,nh))
        frontier=nf
    return set(out)

def histories_compiled(ans,nxt,h=3):
    # Compiler state is (belief-compatible hidden world for validation,
    # enabled-mask, observation history); transition is the ordinary
    # state-dependent action transition on this augmented state.
    states={(w,3,()) for w in (0,1)}
    allstates=set(states)
    for _ in range(h):
        ns=set()
        for w,mask,hist in states:
            for q in (0,1):
                if mask & (1<<q):
                    a=ans[q][w]
                    nm=nxt[q][a]
                    ns.add((w,nm,hist+((q,a),)))
        allstates |= ns
        states=ns
    return allstates

def main():
    systems=checks=mismatches=0
    # 4 answer bits and 4 masks (2 bits each): 16*256 = 4096 systems.
    for abits in product((0,1), repeat=4):
        ans=((abits[0],abits[1]),(abits[2],abits[3]))
        for masks in product(range(4), repeat=4):
            nxt=((masks[0],masks[1]),(masks[2],masks[3]))
            systems += 1
            d=histories_direct(ans,nxt)
            c=histories_compiled(ans,nxt)
            checks += len(d | c)
            if d != c:
                mismatches += 1
                raise AssertionError((ans,nxt,d^c))
    result={"audit":149,"systems":systems,"history_state_checks":checks,
            "mismatches":mismatches,"horizon":3,
            "status":"PASS" if mismatches==0 else "FAIL"}
    print(json.dumps(result,indent=2,sort_keys=True))

if __name__ == "__main__":
    main()
