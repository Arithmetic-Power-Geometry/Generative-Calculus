"""GC-II Audit 160: exact local-to-global translator information lower bound.

For X=[p]^n and projection pi_k retaining the first k coordinates, exact
reconstruction of x from pi_k(x) plus a translator message requires at least
ceil(log2 p^(n-k)) bits in a worst-case fixed-length binary message.  The
checker exhausts small finite worlds and verifies the fiber cardinalities.

Status: theorem PROVED by pigeonhole/injectivity; mechanism IMPORTED/KNOWN
(information/communication complexity), so not independent GC-II novelty.
"""
from itertools import product
from math import ceil, log2


def audit(p: int, n: int, k: int):
    assert p >= 2 and 0 <= k <= n
    fibers = {}
    for x in product(range(p), repeat=n):
        y = x[:k]
        fibers.setdefault(y, []).append(x)
    sizes = {len(v) for v in fibers.values()}
    expected = p ** (n-k)
    assert sizes == {expected}
    lower_bits = ceil(log2(expected)) if expected > 1 else 0
    return {
        "p": p, "n": n, "k": k,
        "fiber_size": expected,
        "minimum_fixed_binary_message_bits": lower_bits,
        "information_lower_bound_bits": (n-k)*log2(p),
    }


if __name__ == "__main__":
    rows=[]
    for p in (2,3):
        for n in range(1,7):
            for k in range(n+1):
                rows.append(audit(p,n,k))
    assert len(rows) == 54
    assert audit(2,6,0)["minimum_fixed_binary_message_bits"] == 6
    assert audit(2,6,6)["minimum_fixed_binary_message_bits"] == 0
    assert audit(3,6,0)["fiber_size"] == 729
    print("PASS", len(rows), "finite parameter cases; 0 violations")
