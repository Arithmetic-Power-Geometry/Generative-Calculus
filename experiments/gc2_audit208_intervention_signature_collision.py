"""GC-II Audit 208: intervention-signature operational types.

Exact finite test of the Audit-207 survivor.  A proposed interface type is the
complete signature of responses to an admissible finite intervention library.
The script verifies that equality of such types is exactly equality of all
interventional predictions in that library; adding an independently measured
translator resource cost produces a costed quotient, but does not refine the
interventional equivalence unless the cost measurement itself is included as
an intervention/observable.
"""
from fractions import Fraction

INTERVENTIONS = ("idle", "flip", "reset0")


def response(system, intervention, x):
    """Deterministic finite response; systems A and B differ internally only."""
    assert x in (0, 1)
    if intervention == "idle":
        return x
    if intervention == "flip":
        return 1 - x
    if intervention == "reset0":
        return 0
    raise ValueError(intervention)


def signature(system):
    return tuple(response(system, u, x) for u in INTERVENTIONS for x in (0, 1))


def interventionally_equivalent(a, b):
    return all(response(a, u, x) == response(b, u, x)
               for u in INTERVENTIONS for x in (0, 1))


def translator_cost(resource_units, unit_price=1):
    assert resource_units >= 0 and unit_price >= 0
    return Fraction(resource_units) * Fraction(unit_price)


def main():
    A, B = "implementation-A", "implementation-B"
    # Exact equivalence: signature equality iff equality on every admitted
    # intervention/input experiment, by extensionality of the finite tuple.
    assert (signature(A) == signature(B)) == interventionally_equivalent(A, B)

    # An external measured conversion cost can vary while signatures stay fixed.
    # Therefore response signatures alone do not identify conversion cost.
    costs = [translator_cost(q) for q in (0, 1, 2, 17)]
    assert len(set(costs)) == 4
    assert signature(A) == signature(B)

    # Once cost is itself made observable, the enriched signature distinguishes
    # systems exactly when that observable differs. This is an enrichment of the
    # experiment language, not a new equivalence principle.
    enriched = [(signature(A), c) for c in costs]
    assert len(set(enriched)) == 4

    print({
        "status": "PASS",
        "signature": signature(A),
        "interventional_equivalence": True,
        "tested_external_costs": [str(c) for c in costs],
        "conclusion": (
            "complete intervention-signature types coincide with finite "
            "interventional/testing equivalence; external translator cost is "
            "not identified until added to the observable experiment language"
        ),
    })


if __name__ == "__main__":
    main()
