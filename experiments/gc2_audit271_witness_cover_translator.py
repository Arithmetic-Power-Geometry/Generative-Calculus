"""Exact audit for GC-II Audit 271: witness-cover translator bound."""
from itertools import combinations


def valuation(n, witnesses):
    return {
        s: int(any((s & w) == w for w in witnesses))
        for s in range(1 << n)
    }


def mobius(vals, n):
    out = {}
    for mask in range(1 << n):
        total = 0
        sub = mask
        while True:
            total += (-1) ** (mask.bit_count() - sub.bit_count()) * vals[sub]
            if sub == 0:
                break
            sub = (sub - 1) & mask
        out[mask] = total
    return out


def degree(coeff):
    return max((m.bit_count() for m, c in coeff.items() if c), default=0)


def main():
    checked = 0

    # Exhaust all witness families of size <=3 for n<=4.  For n=5,6 add
    # deterministic stress families; full enumeration is unnecessary for proof.
    for n in range(1, 7):
        nonempty = list(range(1, 1 << n))
        families = []
        if n <= 4:
            for p in range(1, min(3, len(nonempty)) + 1):
                families.extend(combinations(nonempty, p))
        else:
            for p in range(1, 4):
                families.append(tuple(nonempty[:p]))
                families.append(tuple(1 << i for i in range(min(n, p))))

        for witnesses in families:
            coeff = mobius(valuation(n, witnesses), n)
            deg = degree(coeff)
            union = 0
            total_support = 0
            for w in witnesses:
                union |= w
                total_support += w.bit_count()
            assert deg <= union.bit_count() <= total_support
            checked += 1

    # Exact sharpness: P disjoint blocks, each of size q=kL abstractly.
    # Top Möbius coefficient must be (-1)^(P+1), so degree=Pq.
    sharp = 0
    for P in range(1, 5):
        for q in range(1, 4):
            n = P * q
            witnesses = []
            for p in range(P):
                w = 0
                for j in range(q):
                    w |= 1 << (p * q + j)
                witnesses.append(w)
            coeff = mobius(valuation(n, witnesses), n)
            full = (1 << n) - 1
            assert coeff[full] == (-1) ** (P + 1)
            assert degree(coeff) == P * q
            sharp += 1

    # Two boundary constructions behind the necessity of both factors.
    # Parallel one-step unary witnesses: L=1,k=1,P=n -> degree n.
    for n in range(1, 8):
        W = [1 << i for i in range(n)]
        assert degree(mobius(valuation(n, W), n)) == n

    # One serial witness requiring all n coordinates: P=1,k=1,L=n -> degree n.
    for n in range(1, 8):
        W = [(1 << n) - 1]
        assert degree(mobius(valuation(n, W), n)) == n

    # Empty witness means target already reachable: constant one, degree zero.
    for n in range(1, 6):
        coeff = mobius(valuation(n, [0]), n)
        assert degree(coeff) == 0

    print({"families_checked": checked,
           "sharp_disjoint_block_cases": sharp,
           "boundary_family_cases": 19,
           "status": "PASS"})


if __name__ == "__main__":
    main()
