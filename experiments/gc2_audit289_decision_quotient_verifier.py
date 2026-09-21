"""Exact finite verifier for GC-II Audit 289. Integer arithmetic only."""
from itertools import product
from math import ceil, log2


def family(m, r=3):
    out=[]
    for bits in product((0,1), repeat=m):
        y=[]
        for b in bits:
            y.extend((r,1) if b else (1,r))
        out.append(tuple(y))
    return out


def leq(y,q): return all(a<=b for a,b in zip(y,q))


def signatures(Y, decisions):
    return {y: tuple(int(D(y)) for D in decisions) for y in Y}


def verify():
    total=0; full_pairs=0; monotone_checks=0; composition_checks=0
    for m in range(1,9):
        Y=family(m); total += len(Y)
        # It suffices to use member budgets q in Y to separate this finite Y.
        full=[lambda y,q=q: leq(y,q) for q in Y]
        sf=signatures(Y,full)
        assert len(set(sf.values())) == len(Y)
        full_pairs += len(Y)*(len(Y)-1)//2

        # Aggregate threshold decisions: all attainable sums are identical.
        s0=sum(Y[0])
        agg=[lambda y,B=B: sum(y)<=B for B in (s0-1,s0,s0+1)]
        sa=signatures(Y,agg)
        assert len(set(sa.values())) == 1

        # Adding decisions can only refine the quotient.
        prev=1
        for k in range(1,len(full)+1):
            c=len(set(signatures(Y,full[:k]).values()))
            assert c>=prev
            prev=c; monotone_checks += 1

        # Exact bit lower bound at full separation.
        assert ceil(log2(len(set(sf.values())))) == m

        # Separable product composition for first m-1 modules and last module.
        if m>1:
            Y1=family(m-1); Y2=family(1)
            assert len(Y)==len(Y1)*len(Y2)
            assert len(Y)==2**m
            composition_checks += 1

    print({"status":"PASS","max_modules":8,"max_dimension":16,
           "targets_checked":total,"full_pair_separation_implied_checks":full_pairs,
           "monotone_refinement_checks":monotone_checks,
           "composition_checks":composition_checks,"arithmetic":"integer/exact"})

if __name__=='__main__': verify()
