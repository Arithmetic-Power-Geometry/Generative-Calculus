"""Exact verifier for GC-II Audit 306.

Exhaustively checks a finite family of strictly positive binary A-B-C Markov
chains.  The joint is reconstructed exactly from clique marginals AB and BC
(and their common separator marginal B) using rational arithmetic.
"""
from fractions import Fraction
from itertools import product


def normalize(weights):
    total = sum(weights)
    return tuple(Fraction(w, total) for w in weights)


checked = 0
for root_weights in product((1, 2), repeat=4):
    p_ab_seed = normalize(root_weights)
    for c_given_b0_weights in product((1, 2), repeat=2):
        for c_given_b1_weights in product((1, 2), repeat=2):
            k_c_given_b = (
                normalize(c_given_b0_weights),
                normalize(c_given_b1_weights),
            )

            p = {}
            for a, b, c in product((0, 1), repeat=3):
                p[a, b, c] = p_ab_seed[2 * a + b] * k_c_given_b[b][c]

            p_ab = {
                (a, b): sum(p[a, b, c] for c in (0, 1))
                for a, b in product((0, 1), repeat=2)
            }
            p_bc = {
                (b, c): sum(p[a, b, c] for a in (0, 1))
                for b, c in product((0, 1), repeat=2)
            }
            p_b = {
                b: sum(p[a, b, c] for a, c in product((0, 1), repeat=2))
                for b in (0, 1)
            }

            assert all(v > 0 for v in p_b.values())
            reconstructed = {
                (a, b, c): p_ab[a, b] * p_bc[b, c] / p_b[b]
                for a, b, c in product((0, 1), repeat=3)
            }
            assert reconstructed == p
            assert sum(reconstructed.values()) == 1
            checked += 1

print({
    "status": "PASS",
    "model": "binary chain A-B-C",
    "strictly_positive_models_checked": checked,
    "arithmetic": "exact Fraction",
    "identity": "P(ABC)=P(AB)P(BC)/P(B)",
})
