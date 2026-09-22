"""Exact verifier for GC-II Audit 328.

No external packages. Compares Pareto Bellman recursion with direct complete-policy
enumeration on deterministic finite AND-OR trees using exact integer vectors.
"""
from itertools import product
import random


def dominates(a, b):
    return all(x <= y for x, y in zip(a, b))


def pmin(vs):
    q = sorted(set(vs))
    return tuple(v for v in q if not any(w != v and dominates(w, v) for w in q))


def vmax(vs):
    d = len(vs[0])
    return tuple(max(v[j] for v in vs) for j in range(d))


def add(a, b):
    return tuple(x + y for x, y in zip(a, b))

# Node = None (terminal) or list of actions; action=(cost, tuple(children)).
def bellman(node, d):
    if node is None:
        return ((0,) * d,)
    candidates = []
    for cost, children in node:
        fronts = [bellman(ch, d) for ch in children]
        if any(not f for f in fronts):
            continue
        for choice in product(*fronts):
            candidates.append(add(cost, vmax(choice)))
    return pmin(candidates)


def enumerate_policies(node, d):
    """Direct enumeration: intentionally does not Pareto-prune child policies."""
    if node is None:
        return ((0,) * d,)
    out = []
    for cost, children in node:
        sets = [enumerate_policies(ch, d) for ch in children]
        if any(not s for s in sets):
            continue
        for choice in product(*sets):
            out.append(add(cost, vmax(choice)))
    return tuple(out)


def rnd_tree(depth, d, rng):
    if depth == 0 or rng.random() < .25:
        return None
    actions = []
    for _ in range(rng.randint(1, 2)):
        cost = tuple(rng.randint(0, 3) for _ in range(d))
        children = tuple(rnd_tree(depth - 1, d, rng) for _ in range(rng.randint(1, 2)))
        actions.append((cost, children))
    return actions


def perm(v, p):
    return tuple(v[i] for i in p)


def transform_tree(node, p=None, scale=None):
    if node is None:
        return None
    ans = []
    for c, children in node:
        if p is not None:
            c = perm(c, p)
        if scale is not None:
            c = tuple(c[i] * scale[i] for i in range(len(c)))
        ans.append((c, tuple(transform_tree(x, p, scale) for x in children)))
    return ans


def main():
    rng = random.Random(328)
    checked = 0
    for d in (1, 2, 3):
        for _ in range(300):
            t = rnd_tree(3, d, rng)
            B = bellman(t, d)
            E = pmin(enumerate_policies(t, d))
            assert B == E, (d, B, E)

            # Budget equivalence on a small integer grid.
            for b in product(range(7), repeat=d):
                lhs = any(dominates(r, b) for r in B)
                rhs = any(dominates(r, b) for r in E)
                assert lhs == rhs

            # Coordinate permutation invariance.
            p = tuple(reversed(range(d)))
            BP = bellman(transform_tree(t, p=p), d)
            assert BP == pmin(perm(r, p) for r in B)

            # Positive diagonal rescaling invariance.
            s = tuple(i + 2 for i in range(d))
            BS = bellman(transform_tree(t, scale=s), d)
            assert BS == pmin(tuple(r[i] * s[i] for i in range(d)) for r in B)
            checked += 1

    print({"audit": 328, "trees_checked": checked, "status": "PASS"})


if __name__ == "__main__":
    main()
