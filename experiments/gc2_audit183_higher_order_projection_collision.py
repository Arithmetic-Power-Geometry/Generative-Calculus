"""GC-II Audit 183: exact higher-order projection collision.

For n>=2, E_n and O_n are the even- and odd-parity subsets of {0,1}^n.
Every proper coordinate projection of either relation is the full Boolean cube,
while the n-way relations are disjoint. This is an exact finite witness that
all proper observable projections can agree while global capability differs.

Status: mathematical separation PROVED; GC-specific novelty FALSIFIED because
this is a classical marginal/join/contextuality-type local-to-global failure.
"""
from itertools import product, combinations


def parity_relation(n, bit):
    return {x for x in product((0, 1), repeat=n) if sum(x) % 2 == bit}


def projection(rel, coords):
    return {tuple(x[i] for i in coords) for x in rel}


def verify(n):
    even, odd = parity_relation(n, 0), parity_relation(n, 1)
    assert even.isdisjoint(odd)
    assert len(even) == len(odd) == 2 ** (n - 1)
    for k in range(n):
        for coords in combinations(range(n), k):
            pe, po = projection(even, coords), projection(odd, coords)
            expected = set(product((0, 1), repeat=k))
            assert pe == po == expected
    return {"n": n, "proper_projections_equal": True,
            "global_relations_equal": even == odd,
            "relation_size": len(even)}


if __name__ == "__main__":
    for n in range(2, 11):
        print(verify(n))
