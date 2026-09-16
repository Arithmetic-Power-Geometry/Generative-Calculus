"""GC-II Audit 185: interface-coupling no-go via generalized query complexity.

Question attacked
-----------------
Audit 184 showed that information quantity alone cannot determine capability
acquisition cost. Can an I-A coupling quantity based on a fixed admissible
information interface provide a new GC-II invariant?

Finite exact model
------------------
Let X be a finite hidden-state set, Y a finite output set, f:X->Y the target
capability, and Q a finite family of admissible deterministic queries
q:X->Z_q. A protocol adaptively chooses q in Q from previous answers and must
output f(x) exactly. Give query q nonnegative cost c(q).

Define C_Q(f) as the minimum worst-case total query cost of an exact protocol.

Theorem (compilation/equivalence)
---------------------------------
C_Q(f) is exactly weighted generalized deterministic decision-tree complexity
for f with query family Q. Proof is definitional but decisive:

(1) Every admissible GC information-acquisition protocol unfolds into a rooted
    decision tree: internal node = chosen q, outgoing edge = observed q(x),
    leaf = output. Exactness says f is constant on the hidden states reaching
    each leaf. Path cost is sum c(q).
(2) Conversely every such weighted generalized decision tree is an admissible
    protocol with identical transcripts, outputs and path costs.

Therefore any proposed I-A coupling scalar defined solely as minimum exact
acquisition cost under a fixed finite query interface is not an independent
GC-II invariant: it is generalized query/decision-tree complexity.

Corollary (zero-cost queries)
-----------------------------
Zero-cost queries do not invalidate the theorem. Quotient X by equality of all
zero-cost-query answers (or permit zero-weight nodes directly). A positive
lower bound requires the target to remain nonconstant on at least one
zero-cost indistinguishability class.

Corollary (interface encoding invariance)
-----------------------------------------
Duplicating/renaming queries or answers leaves C_Q(f) unchanged. Replacing a
query by a cost-preserving decision subtree also leaves the induced protocol
cost unchanged when both directions of simulation are available. Thus the
natural encoding-invariant object is the simulation-equivalence class of the
query model; minimum acquisition cost on that class remains ordinary query
complexity under simulation.

Prior-art boundary
------------------
Generalized decision trees explicitly study models in which internal nodes may
query functions richer than individual input bits; parity decision trees are a
standard example. Hence merely naming the interaction between information and
interface does not create a new invariant.

Status
------
* protocol <-> generalized weighted decision tree: PROVED.
* minimum exact finite I-A acquisition cost as independent GC-II invariant:
  FALSIFIED / IMPORTED-KNOWN mechanism.
* encoding invariance under query renaming/duplication: PROVED.
* cost-preserving mutual query simulation invariance: PROVED.
* genuinely new GC-II coupling requiring resources/rules to change the future
  admissible query family during acquisition: OPEN, but finite Markov versions
  remain subject to Audit 176 product compilation.

This script exhaustively verifies the tree partition semantics for small
Boolean examples and the parity separation used in Audit 184.
"""
from itertools import product


def parity(x):
    return sum(x) & 1


def fibers(xs, queries):
    out = {}
    for x in xs:
        transcript = tuple(q(x) for q in queries)
        out.setdefault(transcript, []).append(x)
    return out


def exact_from_queries(xs, f, queries):
    """Nonadaptive special case: f must be constant on every transcript fiber."""
    return all(len({f(x) for x in fiber}) == 1
               for fiber in fibers(xs, queries).values())


def bit_query(i):
    return lambda x: x[i]


def parity_query(indices):
    indices = tuple(indices)
    return lambda x: sum(x[i] for i in indices) & 1


def verify_parity_interface(n):
    xs = list(product((0, 1), repeat=n))
    bits = [bit_query(i) for i in range(n)]

    # Every proper subset of bit queries leaves an opposite-parity collision.
    for mask in range(1 << n):
        qs = [bits[i] for i in range(n) if (mask >> i) & 1]
        if len(qs) < n:
            assert not exact_from_queries(xs, parity, qs)
    assert exact_from_queries(xs, parity, bits)

    # One admissible global parity query solves the same capability.
    pq = parity_query(range(n))
    assert exact_from_queries(xs, parity, [pq])
    return {"n": n, "bit_interface_cost": n, "parity_interface_cost": 1}


if __name__ == "__main__":
    for n in range(1, 11):
        print(verify_parity_interface(n))
