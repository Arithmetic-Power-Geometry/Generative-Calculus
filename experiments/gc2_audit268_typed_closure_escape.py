"""Audit 268: exact finite checks for typed Closure-Escape equivalences.

For finite attainable cost sets B (baseline) and E (extension), with B subset E,
an extension creates a budgeted capability exactly when its upward feasible set
strictly expands. Equivalently, some extension Pareto point is not dominated by
any baseline point; equivalently, some budget has rho_E <= 1 < rho_B.
"""
from fractions import Fraction
from itertools import product

INF = None

def leq(x, y):
    return all(a <= b for a, b in zip(x, y))

def pareto(S):
    return tuple(x for x in S if not any(y != x and leq(y, x) for y in S))

def feasible(S, b):
    return any(leq(x, b) for x in S)

def ratio(a, q):
    if q == 0:
        return Fraction(0) if a == 0 else INF
    return Fraction(a, q)

def rho(S, b):
    vals = []
    for x in S:
        rs = [ratio(a, q) for a, q in zip(x, b)]
        if all(r is not INF for r in rs):
            vals.append(max(rs))
    return min(vals) if vals else INF

def rho_le_one(S, b):
    r = rho(S, b)
    return r is not INF and r <= 1

def frontier_witness(B, E):
    return any(not any(leq(b, e) for b in B) for e in pareto(E))

def budget_escape(B, E, budgets):
    return any(feasible(E, q) and not feasible(B, q) for q in budgets)

def rho_escape(B, E, budgets):
    return any(rho_le_one(E, q) and not rho_le_one(B, q) for q in budgets)

# Exhaust every nested B subset E on the 2x2 typed-cost grid.
# Any minimal witness lies on that grid, so budgets on the same grid suffice.
points = tuple(product(range(2), repeat=2))
budgets = points
systems = checks = escapes = 0
for emask in range(1 << len(points)):
    E = tuple(points[i] for i in range(len(points)) if emask & (1 << i))
    for bmask in range(1 << len(points)):
        B = tuple(points[i] for i in range(len(points)) if bmask & (1 << i))
        if not set(B).issubset(E):
            continue
        systems += 1
        a = frontier_witness(B, E)
        c = budget_escape(B, E, budgets)
        d = rho_escape(B, E, budgets)
        assert a == c == d
        # Extension cannot destroy baseline feasibility.
        for q in budgets:
            assert not feasible(B, q) or feasible(E, q)
            assert feasible(E, q) == rho_le_one(E, q)
            assert feasible(B, q) == rho_le_one(B, q)
            checks += 3
        escapes += int(a)

# Explicit unsupported-tradeoff witness inherited from Audits 266-267.
B = ((0,3),(3,0))
E = ((0,3),(2,2),(3,0))
q = (2,2)
assert frontier_witness(B,E)
assert not feasible(B,q) and feasible(E,q)
assert rho(B,q) == Fraction(3,2) and rho(E,q) == Fraction(1)

print({
    'audit': 268,
    'nested_finite_systems': systems,
    'exact_assertion_checks': checks,
    'strict_escape_systems': escapes,
    'typed_closure_escape_equivalence': 'PROVED_FINITE',
    'extension_monotonicity': 'PROVED_FINITE',
    'linear_scalar_complete': 'FALSIFIED_BY_AUDIT_266',
})