"""GC-II Audit 150: exact residual-state lower-bound regression.

Witness language L_n = {w in {0,1}*: the n-th symbol from the right is 1}.
For all distinct n-bit prefixes x,y, the first differing coordinate j is exposed
by appending 0^(j-1). Thus the 2^n prefixes are pairwise residual-distinct.

This is deliberately a collision/boundary test: the phenomenon is the classical
Myhill-Nerode / NFA-to-DFA exponential state-complexity witness, not claimed as
new GC mathematics.
"""
from itertools import product
import json


def accepts(s: str, n: int) -> bool:
    return len(s) >= n and s[-n] == "1"


def verify(n: int):
    prefixes = ["".join(p) for p in product("01", repeat=n)]
    pair_checks = 0
    failures = []
    for a_idx, x in enumerate(prefixes):
        for y in prefixes[a_idx + 1:]:
            pair_checks += 1
            j = next(k for k, (u, v) in enumerate(zip(x, y), start=1) if u != v)
            z = "0" * (j - 1)
            if accepts(x + z, n) == accepts(y + z, n):
                failures.append({"x": x, "y": y, "j": j, "z": z})
    return {
        "n": n,
        "residual_witnesses": len(prefixes),
        "required_exact_deterministic_states_lower_bound": 2 ** n,
        "pair_checks": pair_checks,
        "failures": len(failures),
    }


if __name__ == "__main__":
    rows = [verify(n) for n in range(1, 11)]
    result = {
        "audit": 150,
        "family": "nth-symbol-from-right",
        "status": "PASS" if all(r["failures"] == 0 for r in rows) else "FAIL",
        "cases": rows,
        "total_pair_checks": sum(r["pair_checks"] for r in rows),
        "interpretation": (
            "Exact sufficient-state quotient can grow exponentially relative to a succinct "
            "operational specification, but this witness is classical Myhill-Nerode/state "
            "complexity and therefore does not establish GC-II novelty."
        ),
    }
    print(json.dumps(result, indent=2))
