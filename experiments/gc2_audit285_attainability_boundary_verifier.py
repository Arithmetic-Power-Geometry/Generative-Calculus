"""Exact verifier for GC-II Audit 285.

Shows an exponential internal-vs-external directed-cover separation.
Exponent coordinates are integers: gap=2, rho=1.
"""
from itertools import product


def family(m, gap=2):
    out = []
    for bits in product((0, 1), repeat=m):
        y = []
        for b in bits:
            y.extend((gap, 0) if b else (0, gap))
        out.append(tuple(y))
    return out


def covers(center, target, rho):
    return all(c - y <= rho for c, y in zip(center, target))


def verify():
    target_checks = 0
    internal_pair_checks = 0
    external_cover_checks = 0

    gap = 2
    rho = 1
    for m in range(1, 11):
        Y = family(m, gap)
        assert len(Y) == 2 ** m

        # Internal centers: every center covers only itself.
        for i, y in enumerate(Y):
            target_checks += 1
            count = 0
            for j, s in enumerate(Y):
                if covers(s, y, rho):
                    count += 1
                    assert i == j
                elif i != j:
                    internal_pair_checks += 1
            assert count == 1

        C_internal = len(Y)
        assert C_internal == 2 ** m

        # External synthetic center z=(rho,...,rho) covers all targets.
        z = (rho,) * (2 * m)
        for y in Y:
            assert covers(z, y, rho)
            external_cover_checks += 1
        C_external = 1
        assert C_internal // C_external == 2 ** m

        # Boundary check: when rho reaches gap, an attainable center covers all.
        s0 = Y[0]
        assert all(covers(s0, y, gap) for y in Y)

    print({
        "status": "PASS",
        "max_modules": 10,
        "max_dimension": 20,
        "targets_checked": target_checks,
        "internal_distinct_noncover_checks": internal_pair_checks,
        "external_cover_checks": external_cover_checks,
        "max_internal_external_ratio": 2 ** 10,
        "arithmetic": "integer exponent / exact",
    })


if __name__ == "__main__":
    verify()
