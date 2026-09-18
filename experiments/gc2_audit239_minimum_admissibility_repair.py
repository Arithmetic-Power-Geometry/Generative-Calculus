#!/usr/bin/env python3
"""Audit 239: exact minimum incidence-addition repair for admissible translators.
No external dependencies.
"""
from itertools import product


def feasible(p, g, lists, alphabet):
    choices = [tuple(L) for L in lists]
    if any(not c for c in choices):
        return False
    for msgs in product(*choices):
        seen = {}
        ok = True
        for i, a in enumerate(msgs):
            key = (p[i], a)
            if key in seen and seen[key] != g[i]:
                ok = False; break
            seen[key] = g[i]
        if ok:
            return True
    return True if not p else False


def omega_formula(p, g, lists, alphabet):
    """Minimum number of world-message incidences to add to reach feasibility.
    Assumes alphabet is nonempty when worlds exist. Labels are fiber-local.
    """
    if p and not alphabet:
        return float('inf')
    total = 0
    for z in sorted(set(p)):
        idx = [i for i in range(len(p)) if p[i] == z]
        decisions = sorted({g[i] for i in idx})
        best = len(idx)
        # lambda_z: messages -> decisions or unused
        for lab in product(decisions + [None], repeat=len(alphabet)):
            amap = dict(zip(alphabet, lab))
            deficit = sum(
                1 for i in idx
                if not any(a in lists[i] and amap[a] == g[i] for a in alphabet)
            )
            best = min(best, deficit)
        total += best
    return total


def omega_bruteforce(p, g, lists, alphabet):
    """Enumerate incidence supersets; return minimum additions reaching feasibility."""
    missing = [(i,a) for i in range(len(p)) for a in alphabet if a not in lists[i]]
    best = float('inf')
    for bits in product((0,1), repeat=len(missing)):
        k = sum(bits)
        if k >= best:
            continue
        aug = [set(L) for L in lists]
        for bit, (i,a) in zip(bits, missing):
            if bit:
                aug[i].add(a)
        if feasible(p,g,aug,alphabet):
            best = k
    return best


def exhaustive_small():
    alphabet = (0,1)
    all_lists = (set(), {0}, {1}, {0,1})
    checked = 0
    for n in range(0,4):
        for p in product((0,1), repeat=n):
            for g in product((0,1), repeat=n):
                for ls in product(all_lists, repeat=n):
                    a = omega_formula(p,g,ls,alphabet)
                    b = omega_bruteforce(p,g,ls,alphabet)
                    assert a == b, (p,g,ls,a,b)
                    assert (a == 0) == feasible(p,g,ls,alphabet)
                    # One-incidence monotonicity/Lipschitz check.
                    for i in range(n):
                        for m in alphabet:
                            if m not in ls[i]:
                                aug = [set(L) for L in ls]; aug[i].add(m)
                                c = omega_formula(p,g,aug,alphabet)
                                assert c <= a
                                assert a - c <= 1
                    checked += 1
    return checked


if __name__ == '__main__':
    checked = exhaustive_small()
    print({'status':'PASS','instances':checked,
           'claim':'formula equals exact minimum incidence-addition repair; zero iff feasible; single-addition 1-Lipschitz'})
