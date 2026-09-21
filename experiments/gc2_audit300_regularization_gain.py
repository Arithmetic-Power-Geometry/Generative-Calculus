"""Exact sanity checks for GC-II Audit 300.

No external solver is used. The examples have analytic fractional optima with
explicit primal/dual certificates.
"""
from fractions import Fraction
from math import log2


def gain(n_int: int, n_frac: Fraction) -> float:
    assert n_int >= 1 and n_frac >= 1 and Fraction(n_int, 1) >= n_frac
    return log2(n_int / float(n_frac))


def triangle():
    # Targets are edges 01,02,12; actions are vertices 0,1,2.
    # Integer cover = 2. Fractional primal x_v=1/2 has value 3/2.
    # Fractional dual z_e=1/2 has value 3/2, proving optimality.
    n = 2
    nf = Fraction(3, 2)
    n2 = 3  # exact Audit-298 square cover number
    nf2 = nf * nf
    g = gain(n, nf)
    g_product = gain(n2, nf2)
    assert nf2 == Fraction(9, 4)
    assert g_product < 2 * g
    # Identity G(IxI)=2G(I)-log2(N^2/N2)
    rhs = 2 * g - log2((n * n) / n2)
    assert abs(g_product - rhs) < 1e-12
    return {
        "N": n,
        "N_f": str(nf),
        "G_bits": g,
        "N_square": n2,
        "N_f_square": str(nf2),
        "G_square_bits": g_product,
        "strict_subadditivity": True,
    }


def odd_cycle(k: int):
    # C_(2k+1): vertex-cover accounting instance from Audits 294-296.
    # tau=k+1. Fractional vertex cover x_v=1/2 and matching-dual weights
    # z_e=1/2 give LP value (2k+1)/2.
    assert k >= 1
    m = 2 * k + 1
    n = k + 1
    nf = Fraction(m, 2)
    assert Fraction(n, 1) >= nf
    return m, n, nf, gain(n, nf)


def main():
    t = triangle()
    print("triangle", t)
    rows = [odd_cycle(k) for k in range(1, 11)]
    for row in rows:
        print("odd_cycle", row)
    # Bipartite frequency-two instances are integral by Audits 295-296.
    # Representative C4: tau=nu=2=N_f, hence zero regularization gain.
    assert gain(2, Fraction(2, 1)) == 0.0
    print("C4 gain bits", 0.0)
    print("PASS")


if __name__ == "__main__":
    main()
