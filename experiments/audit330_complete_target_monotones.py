#!/usr/bin/env python3
"""Exact exhaustive audit for GC-II Audit 330."""
from itertools import product
import json


def is_preorder(R, n):
    for i in range(n):
        if not R[i*n+i]:
            return False
    for i in range(n):
        for j in range(n):
            if R[i*n+j]:
                for k in range(n):
                    if R[j*n+k] and not R[i*n+k]:
                        return False
    return True


def verify(R, n):
    # M_t(x)=R[x,t]. Check R[x,z] iff all_t M_t(x)>=M_t(z).
    for x in range(n):
        for z in range(n):
            rhs = all(R[x*n+t] >= R[z*n+t] for t in range(n))
            if bool(R[x*n+z]) != rhs:
                return False, "completeness"
    # Mutually convertible targets have identical columns.
    for a in range(n):
        for b in range(n):
            if R[a*n+b] and R[b*n+a]:
                if any(R[x*n+a] != R[x*n+b] for x in range(n)):
                    return False, "quotient_column"
    return True, None


def main():
    rows=[]
    total_preorders=0
    for n in range(1,5):
        relations=0; preorders=0; failures=0
        for bits in product((0,1), repeat=n*n):
            relations += 1
            if not is_preorder(bits,n):
                continue
            preorders += 1
            ok,_=verify(bits,n)
            failures += (not ok)
        total_preorders += preorders
        rows.append({"n":n,"relations_checked":relations,"preorders":preorders,"failures":failures})
    out={"audit":330,"method":"exhaustive labelled binary relations; exact Boolean arithmetic","rows":rows,"total_preorders_verified":total_preorders,"total_failures":sum(r["failures"] for r in rows)}
    print(json.dumps(out,indent=2))

if __name__ == "__main__":
    main()
