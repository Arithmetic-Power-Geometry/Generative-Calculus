"""GC-II Audit 141: exact C5 strong-product confusability regression.

Tests whether a positive composition distinguishability gap can arise entirely
inside classical zero-error information theory.
"""
from itertools import combinations, product
from math import log2
import json


def c5_adj(i, j):
    return i != j and ((i - j) % 5 in (1, 4))


def strong_adj(x, y):
    if x == y:
        return False
    return all(a == b or c5_adj(a, b) for a, b in zip(x, y))


def is_independent(combo, edges):
    return all((min(i, j), max(i, j)) not in edges for i, j in combinations(combo, 2))


def main():
    vertices = list(product(range(5), repeat=2))
    edges = {
        (i, j) for i in range(len(vertices)) for j in range(i + 1, len(vertices))
        if strong_adj(vertices[i], vertices[j])
    }

    # alpha(C5)=2: every nonadjacent pair is independent and no independent triple exists.
    c5_edges = {(i, j) for i in range(5) for j in range(i + 1, 5) if c5_adj(i, j)}
    alpha_c5 = 0
    for r in range(1, 6):
        if any(is_independent(c, c5_edges) for c in combinations(range(5), r)):
            alpha_c5 = r
        else:
            break

    # To establish alpha(C5 strong-square)=5, find a 5-set and exhaustively rule out 6-sets.
    witness5 = next(c for c in combinations(range(25), 5) if is_independent(c, edges))
    independent6 = sum(1 for c in combinations(range(25), 6) if is_independent(c, edges))
    assert independent6 == 0
    alpha_square = 5
    assert alpha_c5 == 2

    ratio = alpha_square / (alpha_c5 ** 2)
    gap_bits = log2(ratio)
    result = {
        "status": "PASS",
        "alpha_C5": alpha_c5,
        "alpha_C5_strong_square": alpha_square,
        "product_baseline": alpha_c5 ** 2,
        "composition_ratio": ratio,
        "composition_gap_bits": gap_bits,
        "strong_square_vertices": 25,
        "strong_square_edges": len(edges),
        "independent_6_sets": independent6,
        "witness_5": [vertices[i] for i in witness5],
        "interpretation": "Positive distinguishability synergy under composition occurs in classical zero-error confusability theory; it is not by itself a GC-II novelty invariant."
    }
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
