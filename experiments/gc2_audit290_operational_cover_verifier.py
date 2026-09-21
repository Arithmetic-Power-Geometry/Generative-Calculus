"""Exact finite verifier for GC-II Audit 290. No floating point."""
from itertools import combinations


def cover_number(Y, feasible):
    A=list(feasible)
    for k in range(1,len(A)+1):
        for C in combinations(A,k):
            if set().union(*(feasible[a] for a in C)) >= set(Y):
                return k
    return float('inf')


def verify():
    Y={1,2,3}
    F={"a12":{1,2}, "a23":{2,3}, "a13":{1,3}}
    # Every pair has a common feasible decoder action.
    pair_checks=0
    for u,v in combinations(Y,2):
        assert any({u,v} <= S for S in F.values())
        pair_checks += 1
    # But no common witness exists for all three; exact account needs two states.
    assert not any(Y <= S for S in F.values())
    assert cover_number(Y,F)==2

    # Degenerate one-state case.
    F1={**F,"all":set(Y)}
    assert cover_number(Y,F1)==1

    # Monotonicity under enlarging feasible sets / tolerance abstraction.
    F2={a:set(S) for a,S in F.items()}
    F2["a12"].add(3)
    assert cover_number(Y,F2) <= cover_number(Y,F)

    # Missing target => infeasible.
    assert cover_number({1,2,3,4},F)==float('inf')

    print({"status":"PASS","targets":3,"actions":3,"pairwise_common_witness_checks":pair_checks,
           "exact_cover_number":2,"graph_clique_shortcut":"FALSIFIED","arithmetic":"exact/set"})

if __name__=='__main__': verify()
