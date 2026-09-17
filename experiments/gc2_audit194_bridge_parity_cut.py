"""GC-II Audit 194: exact bridge-parity cut verifier.

Checks that zero S->T communication cannot compute XOR exactly when T holds b
and S holds a, while the one-bit protocol sending a is exact.
"""
from itertools import product

INPUTS = list(product((0, 1), repeat=2))

def target(a, b):
    return a ^ b

# With zero S->T bits, T's output may depend only on b.
zero_bit_candidates = [dict(zip((0, 1), vals)) for vals in product((0, 1), repeat=2)]
zero_bit_exact = []
for g in zero_bit_candidates:
    ok = all(g[b] == target(a, b) for a, b in INPUTS)
    if ok:
        zero_bit_exact.append(g)

assert zero_bit_exact == [], "A zero-bit exact protocol unexpectedly exists"

# One-bit construction: S sends m=a; T outputs m XOR b.
def one_bit_protocol(a, b):
    m = a
    return m ^ b

assert all(one_bit_protocol(a, b) == target(a, b) for a, b in INPUTS)

print("inputs_checked=4")
print("zero_bit_candidate_decoders=4")
print("zero_bit_exact_protocols=0")
print("one_bit_protocol_exact=True")
print("optimal_cross_cut_bits=1")
