#!/usr/bin/env python3
"""Exact finite audit for GC-II coupled-index nonseparability.

Enumerates every Boolean response f:{0,1}^4->{-1,+1}.  The Walsh-Hadamard
basis is an exact hierarchical interaction basis on the four-index product
space.  We verify exact reconstruction and record the maximum interaction
order required by each of the 65,536 functions.

This is a representation/completeness audit, not evidence of GC-II novelty.
"""

from collections import Counter
import csv
from pathlib import Path

NVAR = 4
NPTS = 1 << NVAR
NFUN = 1 << NPTS
OUT = Path("results/gc2_coupled_index_walsh_summary.csv")


def popcount(x: int) -> int:
    return x.bit_count()


def values(mask: int):
    return [1 if ((mask >> x) & 1) else -1 for x in range(NPTS)]


def walsh_numerators(vals):
    # coefficient a_S = numerator[S] / 2^n
    nums = []
    for subset in range(NPTS):
        total = 0
        for x, fx in enumerate(vals):
            chi = -1 if (popcount(subset & x) & 1) else 1
            total += fx * chi
        nums.append(total)
    return nums


def reconstruct_scaled(nums, x: int) -> int:
    # Returns 2^n * reconstructed f(x), staying entirely in integers.
    total = 0
    for subset, num in enumerate(nums):
        chi = -1 if (popcount(subset & x) & 1) else 1
        total += num * chi
    return total


def main():
    degree_counts = Counter()
    reconstruction_failures = 0
    pure_full_order = 0

    for mask in range(NFUN):
        vals = values(mask)
        nums = walsh_numerators(vals)

        for x, fx in enumerate(vals):
            if reconstruct_scaled(nums, x) != NPTS * fx:
                reconstruction_failures += 1
                break

        degree = max((popcount(s) for s, num in enumerate(nums) if num), default=0)
        degree_counts[degree] += 1

        if nums[-1] != 0 and all(nums[s] == 0 for s in range(1, NPTS - 1)):
            pure_full_order += 1

    OUT.parent.mkdir(parents=True, exist_ok=True)
    with OUT.open("w", newline="", encoding="utf-8") as fh:
        writer = csv.writer(fh)
        writer.writerow(["metric", "value"])
        writer.writerow(["n_variables", NVAR])
        writer.writerow(["functions_enumerated", NFUN])
        writer.writerow(["reconstruction_failures", reconstruction_failures])
        writer.writerow(["pure_full_order_functions", pure_full_order])
        for degree in range(NVAR + 1):
            writer.writerow([f"max_interaction_degree_{degree}", degree_counts[degree]])

    assert reconstruction_failures == 0
    assert sum(degree_counts.values()) == NFUN
    print(f"enumerated={NFUN}")
    print(f"reconstruction_failures={reconstruction_failures}")
    print("degree_counts=" + repr(dict(sorted(degree_counts.items()))))
    print(f"pure_full_order_functions={pure_full_order}")
    print(f"wrote={OUT}")


if __name__ == "__main__":
    main()
