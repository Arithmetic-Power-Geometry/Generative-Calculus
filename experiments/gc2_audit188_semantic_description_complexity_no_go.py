"""GC-II Audit 188: semantic-description cost is not a computable intrinsic novelty gap.

Question
--------
Audit 187 leaves genuine acquisition of non-definitional operational semantics open.
A natural candidate is the shortest description/program that generates the new
transformation semantics relative to the old operational system.

Candidate
---------
Fix a universal interpreter U and background operational description G. For a
new finite/computable transformation T define

    K_U(T | G) = min{|p| : U(p,G) computes T}.

This is representation-stable only in the usual algorithmic-information sense:
for universal interpreters U,V,

    |K_U(T|G) - K_V(T|G)| <= c_{U,V},

where the additive constant is independent of T but depends on the interpreters.
Thus the natural shortest-semantic-description route is conditional Kolmogorov
complexity, not a new GC invariant.

No-go theorem
-------------
There is no total computable procedure that returns K_U(T|G) for every
computable finite transformation encoding T and background G. Otherwise, fixing
G to a constant and encoding arbitrary finite strings x as constant-output
transformations T_x would compute K_U(x) up to a fixed compiler constant; with a
canonical universal machine formulation the usual diagonal/noncomputability
argument applies directly. Therefore an exact computable Omega_G defined as
minimal universal semantic-description length is impossible in general.

Finite-world counting check
---------------------------
For n states there are n^n deterministic unary transformations. Any injective
fixed-length code for all of them needs at least ceil(log2(n^n)) bits. This is a
finite counting lower bound only; it does NOT establish individual Kolmogorov
complexity or novelty.

Boundary cases
--------------
* A fixed restricted DSL can make minimum description length computable by finite
  enumeration, but then the quantity is explicitly DSL-relative and collides
  with circuit/formula/program-size complexity.
* Universal languages remove asymptotic language dependence only up to additive
  compiler constants; exact values remain machine-relative.
* Description length is not acquisition effort: learning an unknown semantic
  object additionally depends on the observation/query interface and target
  class, colliding with exact learning/oracle-identification lower bounds.
* Randomized/approximate acquisition needs separate error and distributional
  assumptions; this audit makes no claim about them.
* A physical primitive may have a short description yet high construction cost,
  or a long table description yet be supplied as an oracle. Hence semantic
  description length alone cannot yield No-Free-Capability.

Status
------
* shortest universal semantic-description candidate: IMPORTED/KNOWN mechanism
  (conditional Kolmogorov complexity).
* exact computability of that candidate in general: FALSIFIED.
* finite counting lower bound for transformation representation: PROVED.
* semantic description length alone as GC-II capability-acquisition law: FALSIFIED.
* joint law coupling semantic specification, evidence/query interface, physical
  realization, admissibility change, and achieved closure: OPEN.

The executable check below verifies the finite transformation count and coding
lower bound for small n. It intentionally does not pretend to compute K.
"""

from itertools import product
from math import ceil, log2


def transformations(n):
    return list(product(range(n), repeat=n))


def counting_bound(n):
    count = n ** n
    bits = ceil(log2(count)) if count > 1 else 0
    return count, bits


def verify(max_n=6):
    rows = []
    for n in range(1, max_n + 1):
        ts = transformations(n)
        count, bits = counting_bound(n)
        assert len(ts) == count
        assert (2 ** bits) >= count
        if bits > 0:
            assert (2 ** (bits - 1)) < count
        rows.append({"n_states": n, "transformations": count,
                     "fixed_length_lower_bound_bits": bits})
    return rows


if __name__ == "__main__":
    for row in verify():
        print(row)
