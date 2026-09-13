#!/usr/bin/env python3
"""Exact finite witness for GC-II Audit 124.

Shows that standalone observational equivalence can fail under an admitted
context, while contextual equivalence detects the distinction. Also checks
congruence for a small context monoid closed under composition.
"""
from itertools import product
import json

# Implementations are states 0,1,2. Observation merges 0 and 1.
states = (0, 1, 2)
obs = {0: 0, 1: 0, 2: 1}

# Unary contexts represented as tuples f(0),f(1),f(2).
I = (0, 1, 2)
R = (0, 2, 2)  # reveals distinction between 0 and 1
K = (2, 2, 2)
contexts = (I, R, K)

def apply(f, x):
    return f[x]

def compose(f, g):
    # f after g
    return tuple(f[g[x]] for x in states)

def standalone_eq(x, y):
    return obs[x] == obs[y]

def contextual_eq(x, y):
    return all(obs[apply(c, x)] == obs[apply(c, y)] for c in contexts)

# Verify context family closure.
closure_failures = []
for f, g in product(contexts, repeat=2):
    h = compose(f, g)
    if h not in contexts:
        closure_failures.append((f, g, h))

# Verify contextual equivalence is preserved by each admitted context.
congruence_failures = []
for x, y in product(states, repeat=2):
    if contextual_eq(x, y):
        for d in contexts:
            if not contextual_eq(apply(d, x), apply(d, y)):
                congruence_failures.append((x, y, d))

result = {
    "states": len(states),
    "contexts": len(contexts),
    "context_composition_checks": len(contexts) ** 2,
    "context_closure_failures": len(closure_failures),
    "standalone_witness": {
        "p": 0,
        "q": 1,
        "standalone_equivalent": standalone_eq(0, 1),
        "reveal_outputs": [obs[apply(R, 0)], obs[apply(R, 1)]],
        "contextually_equivalent": contextual_eq(0, 1),
    },
    "ordered_state_pair_checks": len(states) ** 2,
    "congruence_failures": len(congruence_failures),
    "status": "PASS" if not closure_failures and not congruence_failures else "FAIL",
}
print(json.dumps(result, indent=2, sort_keys=True))
assert result["standalone_witness"]["standalone_equivalent"] is True
assert result["standalone_witness"]["contextually_equivalent"] is False
assert not closure_failures
assert not congruence_failures
