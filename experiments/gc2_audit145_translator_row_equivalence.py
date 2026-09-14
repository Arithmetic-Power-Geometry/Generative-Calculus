"""Audit 145: exact deterministic local-to-global translator characterization.

Exhaust all Boolean functions f:XxY->{0,1} for |X|=|Y|=2 and 3 where
feasible, and verify that the minimum message alphabet equals the number of
distinct residual rows. For 3x3 this is all 2^9=512 Boolean functions.
"""
from itertools import product
from math import ceil, log2
import json


def rows(bits, nx, ny):
    return [tuple(bits[x*ny:(x+1)*ny]) for x in range(nx)]


def residual_count(bits, nx, ny):
    return len(set(rows(bits, nx, ny)))


def partition_assignments(nx, k):
    # message labels 0..k-1; surjectivity not required
    yield from product(range(k), repeat=nx)


def feasible_with_k_messages(bits, nx, ny, k):
    rs = rows(bits, nx, ny)
    for msg in partition_assignments(nx, k):
        ok = True
        for a in range(nx):
            for b in range(a+1, nx):
                if msg[a] == msg[b] and rs[a] != rs[b]:
                    ok = False
                    break
            if not ok:
                break
        if ok:
            return True
    return False


def exact_min_messages(bits, nx, ny):
    for k in range(1, nx+1):
        if feasible_with_k_messages(bits, nx, ny, k):
            return k
    raise AssertionError("unreachable")


def run():
    checked = 0
    violations = []
    hist = {}
    for nx, ny in [(1,1),(2,2),(2,3),(3,2),(3,3)]:
        cells = nx*ny
        for bits in product((0,1), repeat=cells):
            r = residual_count(bits, nx, ny)
            m = exact_min_messages(bits, nx, ny)
            b = 0 if r == 1 else ceil(log2(r))
            checked += 1
            hist[str((nx,ny,r,b))] = hist.get(str((nx,ny,r,b)), 0) + 1
            if m != r:
                violations.append({"nx":nx,"ny":ny,"bits":bits,"R":r,"min_messages":m})
    result = {
        "audit": 145,
        "claim": "minimum exact deterministic one-way translator messages equals distinct residual rows",
        "functions_checked": checked,
        "violations": len(violations),
        "status": "PASS" if not violations else "FAIL",
        "scope": "all Boolean functions on 1x1, 2x2, 2x3, 3x2, and 3x3 finite domains",
        "histogram": hist,
    }
    print(json.dumps(result, indent=2, sort_keys=True))
    assert not violations


if __name__ == "__main__":
    run()
