"""Exact finite audit for GC-II Audit 270: staged novelty triangle."""
from itertools import product
from math import inf, log, isclose

U = list(product((1, 2), repeat=2))


def rho(X, y):
    if not X:
        return inf
    vals = []
    for x in X:
        ratios = []
        for xi, yi in zip(x, y):
            if yi == 0:
                ratios.append(0.0 if xi == 0 else inf)
            else:
                ratios.append(xi / yi)
        vals.append(max(ratios))
    return min(vals)


def omega(X, Y):
    return max([1.0] + [rho(X, y) for y in Y])


def main():
    triples = 0
    sharp = 0
    scale = (3, 5)

    # Four labels encode: outside E, E-only, C, B, hence B subset C subset E.
    for labels in product(range(4), repeat=len(U)):
        B = [U[i] for i, q in enumerate(labels) if q == 3]
        C = [U[i] for i, q in enumerate(labels) if q >= 2]
        E = [U[i] for i, q in enumerate(labels) if q >= 1]
        if not B:
            continue

        bc, ce, be = omega(B, C), omega(C, E), omega(B, E)
        assert be <= bc * ce + 1e-12
        assert log(be) <= log(bc) + log(ce) + 1e-12

        Bs = [tuple(v*s for v, s in zip(x, scale)) for x in B]
        Cs = [tuple(v*s for v, s in zip(x, scale)) for x in C]
        Es = [tuple(v*s for v, s in zip(x, scale)) for x in E]
        assert isclose(omega(Bs, Cs), bc)
        assert isclose(omega(Cs, Es), ce)
        assert isclose(omega(Bs, Es), be)

        triples += 1
        if be > 1 and isclose(be, bc * ce):
            sharp += 1

    assert triples == 175
    assert sharp == 83

    # Exact one-dimensional sharpness family: B={ab}, C={b}, E={1}.
    for a in range(1, 21):
        for b in range(1, 21):
            B, C, E = [(a*b,)], [(b,)], [(1,)]
            assert omega(B, C) == a
            assert omega(C, E) == b
            assert omega(B, E) == a*b

    # Extended-value and zero-coordinate edge cases.
    assert omega([], [(1, 1)]) == inf
    assert omega([(0, 1)], [(0, 1)]) == 1.0
    assert omega([(1, 0)], [(0, 1)]) == inf

    print({"nested_triples": triples, "sharp_grid_cases": sharp,
           "sharp_family_cases": 400, "status": "PASS"})


if __name__ == "__main__":
    main()
