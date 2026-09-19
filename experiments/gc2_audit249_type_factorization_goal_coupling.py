"""GC-II Audit 249: exact verifier for target-induced failure of type factorization."""
from itertools import product
from math import inf

X = list(product((0, 1), repeat=2))
F = {(0, 0), (1, 1)}  # equality / XOR=0 target

# No operations: all states have the same local transition signature.
def local_signature(_bit):
    return ()

def product_signature(x):
    return (local_signature(x[0]), local_signature(x[1]))

def value(x):
    return 0 if x in F else inf

# Find all pairs merged by the type-factorized dynamic signature but separated by goal/value.
collisions = []
for x in X:
    for y in X:
        if product_signature(x) == product_signature(y) and ((x in F) != (y in F)):
            collisions.append((x, y, value(x), value(y)))

assert collisions, "Expected target-induced factorization collision"
assert ((0, 0), (0, 1), 0, inf) in collisions

# Exhaustively verify the goal-saturation necessity for every goal subset on this 4-state space:
# any merged pair with different goal status invalidates the proposed quotient at refinement depth 0.
all_goal_sets = 0
unsaturated = 0
for mask in range(1 << len(X)):
    G = {X[i] for i in range(len(X)) if mask & (1 << i)}
    all_goal_sets += 1
    bad = any(
        product_signature(x) == product_signature(y) and ((x in G) != (y in G))
        for x in X for y in X
    )
    if bad:
        unsaturated += 1
        assert any(((x in G) != (y in G)) for x in X for y in X)

# With the fully collapsed signature, only empty and universal goals are saturated.
assert all_goal_sets == 16
assert unsaturated == 14

print("Audit 249 exact verifier PASS")
print("states:", len(X))
print("goal subsets checked:", all_goal_sets)
print("unsaturated under collapsed product signature:", unsaturated)
print("minimal collision:", ((0, 0), (0, 1), 0, inf))
