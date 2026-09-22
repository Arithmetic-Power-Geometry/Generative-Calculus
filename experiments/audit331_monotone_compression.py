#!/usr/bin/env python3
"""Exact checks for GC-II Audit 331."""
from itertools import combinations
from math import comb
import json


def leq(a,b):
    return all(x <= y for x,y in zip(a,b))


def kmin(q):
    k=0
    while comb(k,k//2) < q:
        k += 1
    return k


def constant_weight_codes(k,q):
    w=k//2
    out=[]
    for S in combinations(range(k),w):
        v=tuple(1 if i in S else 0 for i in range(k))
        out.append(v)
        if len(out)==q:
            return out
    return out


def verify_antichain(q):
    # Target witness sets D(x,z) are singleton {z}; hence every z is forced.
    forced=set()
    for x in range(q):
        for z in range(q):
            if x != z:
                forced.add(z)
    target_ok=(len(forced)==q)

    k=kmin(q)
    codes=constant_weight_codes(k,q)
    incomparable=True
    for i in range(q):
        for j in range(q):
            if i != j and (leq(codes[i],codes[j]) or leq(codes[j],codes[i])):
                incomparable=False
    lower_ok = (k==0 or comb(k-1,(k-1)//2) < q)
    upper_ok = comb(k,k//2) >= q
    return {
        "q":q,
        "target_min":len(forced),
        "boolean_min":k,
        "middle_layer_capacity":comb(k,k//2),
        "target_requirement_ok":target_ok,
        "sperner_lower_ok":lower_ok,
        "constructed_codes_incomparable":incomparable,
        "sperner_upper_ok":upper_ok,
    }


def main():
    rows=[verify_antichain(q) for q in range(2,21)]
    failures=sum(not all((r["target_requirement_ok"],r["sperner_lower_ok"],r["constructed_codes_incomparable"],r["sperner_upper_ok"])) for r in rows)
    print(json.dumps({"audit":331,"method":"exact antichain witness sets plus constant-weight Boolean codes","rows":rows,"failures":failures},indent=2))

if __name__ == "__main__":
    main()
