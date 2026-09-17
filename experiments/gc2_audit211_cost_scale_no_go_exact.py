"""GC-II Audit 211: exact no-go for closure-only absolute coercivity.

If the operational transition graph is fixed but every positive primitive cost is
scaled by lambda>0, reachability/convertibility and path ordering are unchanged,
while every minimum positive implementation cost scales by lambda. Therefore no
strict positive absolute lower bound can be derived from scale-free closure
structure alone. A physical currency/unit anchor is required.
"""
from fractions import Fraction as F
from itertools import permutations

# Tiny directed operational system: s->a->t (cost 2+3), s->b->t (4+2).
edges = {
    ('s','a'): F(2), ('a','t'): F(3),
    ('s','b'): F(4), ('b','t'): F(2),
}

def path_cost(path, scale=F(1)):
    return sum(scale * edges[(u,v)] for u,v in zip(path,path[1:]))

paths = [('s','a','t'), ('s','b','t')]
base_order = sorted(paths, key=lambda p: path_cost(p))
assert path_cost(base_order[0]) == 5

for lam in [F(1), F(1,2), F(1,10), F(1,1000), F(17,13)]:
    # Same graph and same cheapest-path ordering under positive rescaling.
    assert sorted(paths, key=lambda p: path_cost(p,lam)) == base_order
    assert path_cost(base_order[0],lam) == lam * F(5)

# Any proposed positive closure-only absolute lower bound L is violated by a
# sufficiently small positive scale lambda, without changing convertibility.
for L in [F(1,100), F(1), F(7), F(1000)]:
    lam = L / F(10) / F(5)
    assert lam > 0
    assert path_cost(base_order[0],lam) < L

# Zero/nonzero status is preserved for lambda>0; what fails is absolute scale.
assert all(path_cost(p,F(1,1000000)) > 0 for p in paths)
print('Audit 211 PASS: scale-free closure cannot imply a positive absolute cost bound')
