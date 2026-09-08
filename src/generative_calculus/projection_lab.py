from __future__ import annotations

from itertools import combinations, product
from math import log2
from typing import Iterable, Sequence


def checksum_envelope(q: int, m: int, residue: int) -> set[tuple[int, ...]]:
    """Return the mod-q checksum class {x in Z_q^m : sum(x)=residue mod q}.

    This is a finite stress-test family for whole-envelope reconstruction.  The
    combinatorial skeleton is the classical single-parity-check / orthogonal-
    array construction; the GC use is explicitly not a historical novelty
    claim.
    """
    q, m, residue = int(q), int(m), int(residue)
    if q < 2:
        raise ValueError("q must be >= 2")
    if m < 2:
        raise ValueError("m must be >= 2")
    residue %= q
    return {
        tuple(x)
        for x in product(range(q), repeat=m)
        if sum(x) % q == residue
    }


def coordinate_projection(
    relation: Iterable[Sequence[int]], indices: Sequence[int]
) -> set[tuple[int, ...]]:
    idx = tuple(int(i) for i in indices)
    return {tuple(row[i] for i in idx) for row in relation}


def checksum_family(q: int, m: int) -> list[set[tuple[int, ...]]]:
    """All q disjoint checksum envelopes, which partition Z_q^m."""
    return [checksum_envelope(q, m, r) for r in range(int(q))]


def all_strict_projections_identical(q: int, m: int) -> bool:
    """Verify equality of every nonempty strict coordinate projection.

    For each strict coordinate set S, every checksum class projects onto the
    full cube Z_q^|S|.  Hence all q whole envelopes remain indistinguishable
    under every strict coordinate projection.
    """
    q, m = int(q), int(m)
    fam = checksum_family(q, m)
    for r in range(1, m):
        for S in combinations(range(m), r):
            projections = [coordinate_projection(E, S) for E in fam]
            target = set(product(range(q), repeat=r))
            if any(P != target for P in projections):
                return False
    return True


def checksum_projection_audit(q: int, m: int) -> dict[str, int | float | bool]:
    """Machine-readable audit of the q-way projection ambiguity construction."""
    q, m = int(q), int(m)
    fam = checksum_family(q, m)
    union = set().union(*fam)
    pairwise_disjoint = all(
        fam[i].isdisjoint(fam[j])
        for i in range(q)
        for j in range(i + 1, q)
    )
    expected_universe_size = q**m
    expected_class_size = q ** (m - 1)
    return {
        "q": q,
        "m": m,
        "number_of_whole_envelopes": q,
        "class_size": expected_class_size,
        "partition_complete": len(union) == expected_universe_size,
        "pairwise_disjoint": pairwise_disjoint,
        "all_strict_projections_identical": all_strict_projections_identical(q, m),
        "minimum_distinguishing_projection_order": m,
        "whole_label_information_bits": log2(q),
    }
