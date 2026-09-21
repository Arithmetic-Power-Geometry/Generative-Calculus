"""Exact verifier for GC-II Audit 307.

Enumerates finite binary A-B-C Markov chains including structural zeros and
checks exact reconstruction from AB and BC clique marginals.  Uses Fraction;
no floating-point tolerance is involved.
"""
from fractions import Fraction
from itertools import product


def distributions2():
    """All binary distributions with integer weights in {0,1,2}, excluding 0,0."""
    out = []
    for w0, w1 in product((0, 1, 2), repeat=2):
        if w0 == w1 == 0:
            continue
        s = w0 + w1
        p = (Fraction(w0, s), Fraction(w1, s))
        if p not in out:
            out.append(p)
    return out


def distributions4():
    """All 4-state distributions from weights in {0,1}, excluding all-zero."""
    out = []
    for ws in product((0, 1), repeat=4):
        if not any(ws):
            continue
        s = sum(ws)
        out.append(tuple(Fraction(w, s) for w in ws))
    return out


binary = distributions2()
checked = 0
zero_separator_models = 0
for p_ab_seed in distributions4():
    for k0 in binary:
        for k1 in binary:
            kernel = (k0, k1)
            p = {}
            for a, b, c in product((0, 1), repeat=3):
                p[a, b, c] = p_ab_seed[2 * a + b] * kernel[b][c]

            p_ab = {(a, b): sum(p[a, b, c] for c in (0, 1))
                    for a, b in product((0, 1), repeat=2)}
            p_bc = {(b, c): sum(p[a, b, c] for a in (0, 1))
                    for b, c in product((0, 1), repeat=2)}
            p_b = {b: sum(p[a, b, c] for a, c in product((0, 1), repeat=2))
                   for b in (0, 1)}

            reconstructed = {}
            for a, b, c in product((0, 1), repeat=3):
                if p_b[b] == 0:
                    reconstructed[a, b, c] = Fraction(0)
                else:
                    reconstructed[a, b, c] = p_ab[a, b] * p_bc[b, c] / p_b[b]

            assert reconstructed == p
            assert sum(reconstructed.values()) == 1
            if any(p_b[b] == 0 for b in (0, 1)):
                zero_separator_models += 1
            checked += 1

print({
    "status": "PASS",
    "model": "binary chain A-B-C",
    "models_checked": checked,
    "models_with_zero_separator_state": zero_separator_models,
    "arithmetic": "exact Fraction",
    "reconstruction": "0 on P(B)=0 branches; P(AB)P(BC)/P(B) otherwise",
})
