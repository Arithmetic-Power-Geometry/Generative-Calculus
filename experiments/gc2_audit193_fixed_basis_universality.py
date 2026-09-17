"""GC-II Audit 193: fixed reusable AND/OR basis still realizes every finite monotone closure map.

Exact exhaustive check for |E|,|X| <= 2.  For each monotone set-valued map
F:2^E -> 2^X, each output capability x is compiled to its monotone DNF:
OR over inclusion-minimal enabling sets T of AND_{e in T} e.
Only the fixed reusable primitives AND, OR, TRUE, FALSE are used.
"""
from itertools import product


def subsets(n):
    return list(range(1 << n))


def leq(a, b):
    return (a & b) == a


def is_monotone_table(table, n):
    ss = subsets(n)
    return all(not leq(a, b) or table[a] <= table[b] for a in ss for b in ss)


def minimal_true_sets(table, n):
    mins = []
    for s in subsets(n):
        if not table[s]:
            continue
        if all(not table[t] for t in subsets(n) if t != s and leq(t, s)):
            mins.append(s)
    return mins


def eval_fixed_basis_dnf(mins, s):
    # OR_T AND_{e in T} e; empty conjunction is TRUE, empty OR is FALSE.
    return int(any(leq(t, s) for t in mins))


def verify_scalar(n):
    ss = subsets(n)
    checked = 0
    for bits in product((0, 1), repeat=len(ss)):
        table = dict(zip(ss, bits))
        if not is_monotone_table(table, n):
            continue
        mins = minimal_true_sets(table, n)
        assert all(eval_fixed_basis_dnf(mins, s) == table[s] for s in ss)
        checked += 1
    return checked


def verify_set_valued(n, m):
    # A set-valued monotone map is exactly m coordinatewise monotone Boolean maps.
    scalar = verify_scalar(n)
    return scalar ** m


if __name__ == "__main__":
    expected_scalar = {0: 2, 1: 3, 2: 6}
    for n in range(3):
        got = verify_scalar(n)
        assert got == expected_scalar[n], (n, got)
        print(f"n={n}: scalar monotone maps verified={got}")
    for n in range(3):
        for m in range(3):
            print(f"|E|={n}, |X|={m}: set-valued maps covered={verify_set_valued(n,m)}")
    print("PASS: fixed reusable AND/OR basis is extensionally universal for all tested finite monotone closures.")
