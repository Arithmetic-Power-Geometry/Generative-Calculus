"""GC-II Audit 186: no-go for interface-generation cost as a generic breakthrough.

Question
--------
Audit 185 left open the cost of *generating/changing* admissible interfaces.
Does charging for interface updates escape ordinary query/protocol complexity?

Finite dynamic model
--------------------
Let sigma be a finite maintained state. An UPDATE u changes sigma and incurs
cost c_U(u). A QUERY q reads the current sigma and incurs cost c_Q(q). The
answer depends on the current state. A finite adaptive GC controller may
interleave updates and queries.

Compilation theorem
-------------------
Any such finite Markov interface-generation system is a dynamic data structure:
maintained GC state = data-structure memory/state; interface-generating action =
update; capability request = query. Conversely, any finite dynamic data
structure is such a GC operational system. The operation sequence and its
update/query costs are preserved exactly.

Therefore a scalar that charges only for maintaining/generating a finite
query interface and then using it is, without additional structure, a dynamic
update-query complexity measure. This is not a new GC-II invariant.

Prior-art collision
-------------------
Fredman-Saks and subsequent cell-probe work explicitly study representations
under modifications (updates) and questions (queries), including lower bounds
and update-query tradeoffs. Thus moving from fixed Q (Audit 185) to dynamically
maintained Q does not by itself escape established complexity theory.

Exact toy collision
-------------------
Maintain n bits initially zero. update(i,b) changes bit i. query_parity returns
XOR of all maintained bits. The same operation trace is represented both as
(1) GC interface generation/use and (2) a dynamic data structure. The script
checks trace and answer identity exhaustively for all short traces.

Status
------
* finite Markov interface generation -> dynamic data structure: PROVED
  (compilation/equivalence; mechanism IMPORTED/KNOWN).
* generic update/query accounting as independent GC-II breakthrough: FALSIFIED.
* finite dynamic update/query tradeoff: IMPORTED/KNOWN.
* capability generation that changes the *space of admissible future
  transformations* in a way not representable by a fixed finite Markov state:
  OPEN.
* uniform-family lower bound that jointly charges description/representation
  growth plus R/I/A/L and survives data-structure/circuit/communication
  reductions: OPEN.

This file is intentionally an exact falsification note, not a novelty claim.
"""
from itertools import product


def gc_run(n, ops):
    state = [0] * n
    out = []
    for op in ops:
        if op[0] == "u":
            _, i, b = op
            state[i] = b
        else:
            out.append(sum(state) & 1)
    return tuple(out), tuple(state)


def ds_run(n, ops):
    memory = [0] * n
    answers = []
    for op in ops:
        if op[0] == "u":
            _, i, b = op
            memory[i] = b
        else:
            answers.append(sum(memory) % 2)
    return tuple(answers), tuple(memory)


def verify(n=3, max_len=5):
    alphabet = [("q",)] + [("u", i, b) for i in range(n) for b in (0, 1)]
    checked = 0
    for length in range(max_len + 1):
        for ops in product(alphabet, repeat=length):
            assert gc_run(n, ops) == ds_run(n, ops)
            checked += 1
    return {"n": n, "max_len": max_len, "traces_checked": checked}


if __name__ == "__main__":
    print(verify())
