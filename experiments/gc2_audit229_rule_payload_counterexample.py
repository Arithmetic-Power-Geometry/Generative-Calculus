#!/usr/bin/env python3
"""Audit 229: unit-count rule augmentation cannot bound capability creation.

A single newly admissible rule may carry an arbitrary monotone Boolean payload.
For any antichain M of subsets of N, define the rule L_M to enable the target
exactly when some E in M is contained in the available augmentation set S.
Starting from the identically-false capability, adding exactly one rule produces
minimal-enabler antichain M. Therefore rule count Delta L=1 does not bound
minimal-enabler count, width, union size, Mobius degree, or truth-table/semantic
complexity unless the model also constrains/charges rule payload.

This is a representation/accounting obstruction, not claimed as GC novelty.
"""
from itertools import combinations


def subsets(n):
    xs = tuple(range(n))
    for r in range(n + 1):
        for c in combinations(xs, r):
            yield frozenset(c)


def capability(S, M):
    return int(any(E <= S for E in M))


def minimal_true_sets(n, M):
    ss = list(subsets(n))
    vals = {S: capability(S, M) for S in ss}
    return {
        S for S in ss if vals[S] and all(not vals[T] for T in ss if T < S)
    }


def mobius(values, T):
    xs = tuple(T)
    return sum(
        (-1) ** (len(T) - len(U)) * values[U]
        for r in range(len(xs) + 1)
        for U in map(frozenset, combinations(xs, r))
    )


def middle_layer(n):
    r = n // 2
    return {frozenset(c) for c in combinations(range(n), r)}


def audit(n):
    # One rule carries the whole middle-layer antichain.
    M = middle_layer(n)
    assert all(not (E < F) for E in M for F in M)
    recovered = minimal_true_sets(n, M)
    assert recovered == M

    ss = list(subsets(n))
    values = {S: capability(S, M) for S in ss}
    coeff = {T: mobius(values, T) for T in ss}
    degree = max((len(T) for T, c in coeff.items() if c), default=0)

    # Delta rule count is exactly one for every n, while antichain size grows.
    delta_L_count = 1
    assert delta_L_count == 1
    assert len(M) == len(list(combinations(range(n), n // 2)))
    return len(M), degree


def main():
    rows = []
    for n in range(2, 13):
        p, degree = audit(n)
        rows.append((n, p, degree))
    print("n,minimal_enablers,mobius_degree,delta_L_count")
    for n, p, d in rows:
        print(f"{n},{p},{d},1")
    assert rows[-1][1] == 924  # C(12,6), still from one rule.
    print("PASS: one rule realizes middle-layer antichains through n=12")
    print("PASS: at n=12, DeltaL_count=1 creates 924 minimal enablers")
    print("BOUNDARY: rule count is not semantic rule capacity")
    print("REQUIREMENT: charge/constrain rule description or implementation payload")


if __name__ == "__main__":
    main()
