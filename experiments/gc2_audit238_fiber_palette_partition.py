#!/usr/bin/env python3
"""Audit 238 exact verifier: translator brute force == fiber-palette criterion.
No external dependencies.
"""
from itertools import product


def translator_feasible(p, g, lists, alphabet):
    n = len(p)
    choices = [tuple(lists[i]) for i in range(n)]
    if any(not c for c in choices):
        return False
    for msgs in product(*choices):
        seen = {}
        ok = True
        for i in range(n):
            key = (p[i], msgs[i])
            if key in seen and seen[key] != g[i]:
                ok = False
                break
            seen[key] = g[i]
        if ok:
            return True
    return False


def palette_feasible(p, g, lists, alphabet):
    # Directly enumerate per-fiber labelings lambda_z: M -> decisions U {unused}.
    for z in sorted(set(p)):
        idx = [i for i in range(len(p)) if p[i] == z]
        decisions = sorted({g[i] for i in idx})
        labels = decisions + [None]
        fiber_ok = False
        for lab in product(labels, repeat=len(alphabet)):
            amap = dict(zip(alphabet, lab))
            if all(any(amap[a] == g[i] for a in lists[i]) for i in idx):
                fiber_ok = True
                break
        if not fiber_ok:
            return False
    return True


def exhaustive_four_world_binary():
    alphabet = (0, 1)
    nonempty_lists = ({0}, {1}, {0, 1})
    checked = 0
    for p in product((0, 1), repeat=4):
        for g in product((0, 1), repeat=4):
            for ls in product(nonempty_lists, repeat=4):
                a = translator_feasible(p, g, ls, alphabet)
                b = palette_feasible(p, g, ls, alphabet)
                assert a == b, (p, g, ls, a, b)
                checked += 1
    return checked


def edge_cases():
    assert translator_feasible([], [], [], (0,))
    assert palette_feasible([], [], [], (0,))
    assert not translator_feasible((0,), (0,), (set(),), (0,))
    assert not palette_feasible((0,), (0,), (set(),), (0,))
    # Same fiber, incompatible decisions, same singleton list: impossible.
    p=(0,0); g=(0,1); ls=({0},{0})
    assert not translator_feasible(p,g,ls,(0,1))
    assert not palette_feasible(p,g,ls,(0,1))
    # Separate singleton messages: feasible.
    ls=({0},{1})
    assert translator_feasible(p,g,ls,(0,1))
    assert palette_feasible(p,g,ls,(0,1))


if __name__ == '__main__':
    edge_cases()
    checked = exhaustive_four_world_binary()
    print({'status':'PASS', 'instances':checked,
           'claim':'translator feasibility equals fiber-palette feasibility'})
