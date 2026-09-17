"""GC-II Audit 212: exact no-go for reference-normalized cost as intrinsic Omega_G.

Audit 211 showed that absolute costs are not identifiable from scale-free closure.
A natural repair is to normalize target cost by an operational reference/currency:
    Omega_q(x->y) = C*(x->y) / C*(q).
This removes global unit rescaling, but the value remains reference-relative.
Unless GC closure itself canonically identifies a reference process (or a physical
currency is supplied independently), the same target capability admits arbitrary
positive normalized values under equally admissible reference choices.

Status:
  global-scale invariance of the ratio: PROVED
  reference-choice invariance: FALSIFIED
  dimensionless ratio as intrinsic Omega_G: FALSIFIED
  currency-relative operational value: IMPORTED/KNOWN mechanism
  canonical closure-derived currency: OPEN
"""
from fractions import Fraction as F

# Same target transition in every model.
target_cost = F(6)

# Three admissible reference processes, all positive and independently measurable.
references = {
    'q_fast': F(2),
    'q_equal': F(6),
    'q_slow': F(30),
}

def omega(target, reference):
    assert reference > 0
    return target / reference

assert omega(target_cost, references['q_fast']) == F(3)
assert omega(target_cost, references['q_equal']) == F(1)
assert omega(target_cost, references['q_slow']) == F(1,5)

# Global positive rescaling cancels exactly: Audit-211's unit problem is repaired.
for lam in [F(1,1000), F(1,7), F(1), F(13,5), F(10**6)]:
    for r in references.values():
        assert omega(lam*target_cost, lam*r) == omega(target_cost, r)

# But reference choice can realize any prescribed positive rational normalized value
# without changing the target capability: choose reference cost C(q)=C(target)/z.
for z in [F(1,10**6), F(1,17), F(1), F(19,7), F(10**6)]:
    reference_cost = target_cost / z
    assert reference_cost > 0
    assert omega(target_cost, reference_cost) == z

# Degenerate reference: zero-cost currency cannot normalize a positive target.
try:
    omega(target_cost, F(0))
    raise AssertionError('zero reference should be rejected')
except AssertionError:
    pass

print('Audit 212 PASS: normalization removes global scale but not reference arbitrariness')
