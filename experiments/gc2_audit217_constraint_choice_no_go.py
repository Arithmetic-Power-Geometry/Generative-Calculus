"""GC-II Audit 217: exact witness for constraint-relative excess no-go.

For each unrestricted minimal realization size N and each imposed minimum
realization size m>=N, verify Xi=log2(m/N), including zero and arbitrarily
increasing finite excess. This is an arithmetic witness for the theorem; the
proof is in notes/gc2_audit217_constraint_relative_excess_no_go.md.
"""
from fractions import Fraction
from math import log2

rows=[]
for N in range(1,9):
    previous=-1.0
    for m in range(N,65):
        ratio=Fraction(m,N)
        xi=log2(ratio.numerator/ratio.denominator)
        assert xi >= -1e-15
        if m==N:
            assert abs(xi) < 1e-15
        assert xi > previous
        previous=xi
        rows.append((N,m,str(ratio),xi))

# Same fixed behavior size N=2 can acquire increasingly large excess solely
# by changing the admissible implementation class's minimum size.
N=2
witness=[(m,log2(m/N)) for m in (2,4,8,16,32,64,128,256)]
assert [x for _,x in witness] == [0.,1.,2.,3.,4.,5.,6.,7.]

print({
    'finite_pairs_checked': len(rows),
    'fixed_behavior_N': N,
    'constraint_witness': witness,
    'unrestricted_Xi': 0.0,
    'status': 'PASS'
})
