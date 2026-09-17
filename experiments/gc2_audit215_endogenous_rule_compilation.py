#!/usr/bin/env python3
"""GC-II Audit 215: exact finite endogenous-rule compilation no-go.

Exhaustively verifies, on all deterministic 2-world/2-rulebook systems with a
binary action alphabet, that treating the current rulebook as part of state
produces a first-order transition system with identical traces and accumulated
costs.  This is a collision test, not evidence of novelty.
"""
from itertools import product

X = range(2)
Q = range(2)
A = range(2)
S = [(x,q) for x in X for q in Q]
SA = [(s,a) for s in S for a in A]
# Two possible next configurations per (configuration,action), keeping the
# physical world flip fixed by action and allowing rulebook persistence/flip.
def world_next(x,a):
    return x ^ a

def build(bits):
    H = {}
    for ((x,q),a), b in zip(SA,bits):
        q2 = q ^ b
        H[((x,q),a)] = (world_next(x,a),q2)
    return H

def compile_first_order(H):
    # Compiler C: configuration (x,q) is an ordinary state; no rule mutation
    # exists at the compiled semantic level.
    return dict(H)

def run(T,s,word):
    trace=[s]
    cost=0
    for a in word:
        ns=T[(s,a)]
        # independently observable unit action cost; compiler preserves it
        cost += 1
        trace.append(ns)
        s=ns
    return tuple(trace),cost

systems=0
checks=0
for bits in product((0,1), repeat=len(SA)):
    H=build(bits)
    C=compile_first_order(H)
    systems += 1
    # all words through length 4
    words=[()]
    for n in range(1,5):
        words.extend(product(A, repeat=n))
    for s in S:
        for w in words:
            assert run(H,s,w)==run(C,s,w)
            checks += 1

print({
    'audit':215,
    'systems_exhausted':systems,
    'trace_cost_checks':checks,
    'max_word_length':4,
    'result':'PASS: exact configuration-state compilation preserved traces and costs',
    'status':'PROVED for enumerated family; general theorem is structural'
})
