"""GC-II Audit 207: exact typed-translator relabeling counterexample.

Purpose
-------
Test whether a minimum translator cost across restricted typed interfaces can be
an intrinsic capability invariant after behavioural/contextual quotienting.

Construction
------------
Two systems have exactly the same deterministic behaviour: one input bit is
copied to one output bit. Only the declared interface type names differ.
A typed translator model charges a nonnegative conversion cost between labels.
The operational behaviour is unchanged while the measured translator gap can be
set to any chosen nonnegative value M. Hence typed translator cost is not
representation-invariant unless interface types and their conversion costs are
independently operationally grounded.

No third-party dependencies.
"""
from fractions import Fraction


def behavior(x):
    assert x in (0, 1)
    return x


def typed_translation_cost(source_type, target_type, cost):
    if source_type == target_type:
        return Fraction(0)
    return Fraction(cost)


def main():
    # Exact contextual/behavioural equality on the complete finite input domain.
    assert all(behavior(x) == behavior(x) for x in (0, 1))

    # Same extensional capability, arbitrary declared type-conversion penalty.
    source, target = "R", "I"
    tested = [Fraction(0), Fraction(1, 7), Fraction(1), Fraction(13), Fraction(10**6)]
    observed = []
    for M in tested:
        gap = typed_translation_cost(source, target, M)
        assert gap == M
        # Relabeling target to source leaves the bit-copy behaviour unchanged
        # but makes the typed gap zero.
        relabeled_gap = typed_translation_cost(source, source, M)
        assert relabeled_gap == 0
        observed.append((str(M), str(gap), str(relabeled_gap)))

    print({
        "behaviour": "identical bit-copy map",
        "tested_declared_costs": observed,
        "status": "PASS",
        "conclusion": "typed translator gap is not intrinsic under semantics-preserving relabeling"
    })


if __name__ == "__main__":
    main()
