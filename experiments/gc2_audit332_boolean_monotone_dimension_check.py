"""Exact checks for GC-II Audit 332.

No external packages. Verifies the chain lower/upper boundary from Boolean-lattice
height and the Audit-331 antichain boundary from the middle-binomial capacity.
All arithmetic is exact integers.
"""
from math import comb, ceil, log2


def chain_bmd(q: int) -> int:
    assert q >= 1
    return q - 1


def antichain_bmd(q: int) -> int:
    assert q >= 1
    if q == 1:
        return 0
    k = 1
    while comb(k, k // 2) < q:
        k += 1
    return k


def check_chain_embedding(q: int) -> None:
    k = chain_bmd(q)
    masks = [(1 << i) - 1 for i in range(q)]
    assert len(set(masks)) == q
    for i in range(q):
        for j in range(q):
            subset = (masks[i] & ~masks[j]) == 0
            assert subset == (i <= j)
    if q >= 2:
        # Height(B_{k-1})=(k-1)+1=k<q, proving k-1 coordinates cannot suffice.
        assert k < q


def main() -> None:
    rows = []
    for q in range(1, 65):
        check_chain_embedding(q)
        kc = chain_bmd(q)
        ka = antichain_bmd(q)
        info_lb = 0 if q == 1 else ceil(log2(q))
        assert kc >= info_lb
        assert ka >= info_lb
        # Check the defining minimality inequalities for the antichain formula.
        if q >= 2:
            assert comb(ka, ka // 2) >= q
            if ka > 0:
                assert comb(ka - 1, (ka - 1) // 2) < q
        rows.append((q, kc, ka, info_lb))

    print("q,chain_bmd,antichain_bmd,ceil_log2_q")
    for row in rows:
        print(",".join(map(str, row)))
    print(f"checked={len(rows)}; failures=0")


if __name__ == "__main__":
    main()
