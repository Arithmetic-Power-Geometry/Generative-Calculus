from itertools import product
from math import inf, isclose


def dominates(a, b):
    return all(x <= y for x, y in zip(a, b))


def pareto(S):
    return [x for x in S if not any(y != x and dominates(y, x) for y in S)]


def rho(B, q):
    if not B:
        return inf
    vals = []
    for b in B:
        r = 0.0
        feasible_ratio = True
        for bi, qi in zip(b, q):
            if qi == 0:
                if bi > 0:
                    feasible_ratio = False
                    break
                ri = 0.0
            else:
                ri = bi / qi
            r = max(r, ri)
        if feasible_ratio:
            vals.append(r)
    return min(vals) if vals else inf


def omega(B, E):
    if not E:
        return 1.0
    return max(1.0, max(rho(B, e) for e in pareto(E)))


def escape(B, E):
    return any(not any(dominates(b, e) for b in B) for e in E)


def minkowski(A, C):
    return list(set(tuple(x + y for x, y in zip(a, c)) for a in A for c in C))


def subsets_nonempty(grid):
    out = []
    for mask in range(1, 1 << len(grid)):
        out.append([grid[i] for i in range(len(grid)) if (mask >> i) & 1])
    return out


def main():
    grid = list(product([1, 2], repeat=2))
    sets = subsets_nonempty(grid)
    nested = [(B, E) for E in sets for B in sets if set(B) <= set(E)]
    assert len(nested) == 65

    for B, E in nested:
        assert (omega(B, E) > 1.0) == escape(B, E)
        scale = (3, 5)
        Bs = [tuple(x*s for x, s in zip(b, scale)) for b in B]
        Es = [tuple(x*s for x, s in zip(e, scale)) for e in E]
        assert isclose(omega(B, E), omega(Bs, Es))

    comparisons = 0
    for B1, E1 in nested:
        for B2, E2 in nested:
            lhs = omega(minkowski(B1, B2), minkowski(E1, E2))
            rhs = max(omega(B1, E1), omega(B2, E2))
            assert lhs <= rhs + 1e-12
            comparisons += 1
    assert comparisons == 4225

    assert omega([], [(1, 1)]) == inf
    assert omega([(0, 0)], [(0, 0)]) == 1.0
    assert rho([(0, 1)], (0, 1)) == 1.0
    assert rho([(1, 0)], (0, 1)) == inf

    # Sharpness: composition with a zero-cost identity component preserves the gap.
    B1, E1 = [(2, 2)], [(2, 2), (1, 1)]
    B2 = E2 = [(0, 0)]
    assert omega(B1, E1) == 2.0
    assert omega(minkowski(B1, B2), minkowski(E1, E2)) == 2.0

    print({"nested_systems": len(nested), "composition_comparisons": comparisons, "status": "PASS"})


if __name__ == "__main__":
    main()
