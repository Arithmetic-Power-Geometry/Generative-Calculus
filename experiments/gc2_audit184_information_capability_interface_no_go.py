"""GC-II Audit 184: information-to-capability interface no-go.

Question attacked
-----------------
Can a universal No-Free-Capability / capability-accounting law use only an
amount of acquired information Delta I to lower-bound the operational work
needed to unlock a global capability?

Exact witness
-------------
Task: compute parity of an unknown x in {0,1}^n exactly.

Interface B (bit queries): query x_i. Every exact deterministic protocol has
worst-case query cost n. Adversary proof: if a leaf is reached after querying
fewer than n coordinates, flip an unqueried bit; the transcript is unchanged
but parity flips, so the leaf cannot be correct on both inputs.

Interface P (parity queries): query XOR over any subset. One query of [n]
computes the same task.

Thus the answer is one bit in both models, while acquisition work is n versus
1. Consequently Delta I measured only as output/Shannon bit amount cannot
support a universal acquisition-cost or capability-gain law independent of the
admissible information interface A. Any defensible GC-II law must be
interface-relative or contain an explicit interaction term coupling I and A.

Status
------
* n-bit lower bound in bit-query model: PROVED / IMPORTED-KNOWN.
* one-query parity-interface upper bound: PROVED / IMPORTED-KNOWN.
* interface-independent law from Delta I alone: FALSIFIED.
* genuinely GC-specific I-A interaction invariant: OPEN.
"""
from itertools import product


def parity(x):
    return sum(x) & 1


def bit_query_transcript(x, queried):
    return tuple(x[i] for i in queried)


def verify_adversary(n):
    """Exhaustively verify every proper queried-coordinate set has a collision
    with identical transcript and opposite parity."""
    assert n >= 1
    universe = tuple(range(n))
    xs = list(product((0, 1), repeat=n))
    for mask in range(1 << n):
        queried = tuple(i for i in universe if (mask >> i) & 1)
        if len(queried) == n:
            continue
        buckets = {}
        for x in xs:
            t = bit_query_transcript(x, queried)
            buckets.setdefault(t, set()).add(parity(x))
        assert all(vals == {0, 1} for vals in buckets.values())
    return {
        "n": n,
        "bit_query_exact_worst_case": n,
        "parity_query_exact_worst_case": 1,
        "answer_bits": 1,
        "interface_separation": n,
    }


if __name__ == "__main__":
    for n in range(1, 11):
        print(verify_adversary(n))
