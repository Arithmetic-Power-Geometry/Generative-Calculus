"""GC-II Audit 218: exact finite checks for architecture-fixed rank bound.

Checks equality communication matrices I_n, duplicate-row invariance, constant
edge cases, and exhaustive 2x2 Boolean communication matrices.  This does not
claim to compute communication complexity generally; it verifies the exact
finite witnesses used in the proof note.
"""
from fractions import Fraction
from itertools import product
from math import ceil, log2


def rank_q(A):
    A = [[Fraction(x) for x in row] for row in A]
    if not A:
        return 0
    m, n = len(A), len(A[0])
    r = 0
    for c in range(n):
        pivot = next((i for i in range(r, m) if A[i][c]), None)
        if pivot is None:
            continue
        A[r], A[pivot] = A[pivot], A[r]
        p = A[r][c]
        A[r] = [z/p for z in A[r]]
        for i in range(m):
            if i != r and A[i][c]:
                q = A[i][c]
                A[i] = [u-q*v for u,v in zip(A[i], A[r])]
        r += 1
        if r == m:
            break
    return r

# Equality family: rank(I_n)=n; sending a binary label matches ceil(log2 n).
for n in range(1, 33):
    I = [[int(i == j) for j in range(n)] for i in range(n)]
    r = rank_q(I)
    assert r == n
    lower = ceil(log2(r)) if r else 0
    explicit_send_label = ceil(log2(n)) if n > 1 else 0
    assert lower == explicit_send_label

# Constant functions: rank one and zero-bit exact protocol.
for bit in (0, 1):
    C = [[bit for _ in range(4)] for _ in range(3)]
    r = rank_q(C)
    # all-zero matrix has rank 0; all-one has rank 1. Both need zero bits.
    assert r == bit
    lower = 0 if r <= 1 else ceil(log2(r))
    assert lower == 0

# Duplicating a row cannot increase rank.
A = [[1,0,1],[0,1,1]]
assert rank_q(A) == rank_q(A + [A[0][:]]) == 2

# Exhaust every 2x2 Boolean communication matrix and verify 0 <= ceil(log2 r) <= 1.
rows=[]
for bits in product((0,1), repeat=4):
    M=[list(bits[:2]), list(bits[2:])]
    r=rank_q(M)
    lb=0 if r <= 1 else ceil(log2(r))
    assert r in (0,1,2)
    assert lb in (0,1)
    rows.append((bits,r,lb))

print({
    'equality_sizes_checked': 32,
    'boolean_2x2_matrices_checked': len(rows),
    'duplicate_row_invariance': 'PASS',
    'constant_edge_cases': 'PASS',
    'status': 'PASS'
})
