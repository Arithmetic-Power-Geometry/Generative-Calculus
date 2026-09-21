"""GC-II Audit 303: exact finite checks for task-relative novelty criteria.

No external packages required. Exhausts capability subsets on universes up to size 4
and all 1D feature maps into {-1,0,1}. Verifies indicator-task set escape and
linear-task convex-hull escape criteria.
"""
from itertools import combinations, product


def nonempty_subsets(xs):
    xs = tuple(xs)
    for r in range(1, len(xs) + 1):
        for c in combinations(xs, r):
            yield frozenset(c)


def indicator_gap(base, aug):
    # Tasks u_y(x)=1[x=y], independently fixed by the common capability universe.
    return max((1 if y in aug else 0) - (1 if y in base else 0) for y in base | aug)


def linear_gap_1d(base, aug, phi):
    # Normalized directions d in {-1,+1}; support-function advantage.
    return max(
        max(d * phi[y] for y in aug) - max(d * phi[y] for y in base)
        for d in (-1, 1)
    )


def hull_escape_1d(base, aug, phi):
    lo, hi = min(phi[y] for y in base), max(phi[y] for y in base)
    return any(phi[y] < lo or phi[y] > hi for y in aug)


def main():
    pair_checks = 0
    feature_checks = 0
    for n in range(1, 5):
        Y = tuple(range(n))
        subsets = tuple(nonempty_subsets(Y))
        for base in subsets:
            for aug in subsets:
                gap = indicator_gap(base, aug)
                escape = bool(aug - base)
                assert (gap > 0) == escape
                pair_checks += 1
                for vals in product((-1, 0, 1), repeat=n):
                    phi = dict(zip(Y, vals))
                    lgap = linear_gap_1d(base, aug, phi)
                    hescape = hull_escape_1d(base, aug, phi)
                    assert (lgap > 0) == hescape
                    feature_checks += 1
    print({"indicator_pair_checks": pair_checks,
           "linear_feature_checks": feature_checks,
           "status": "all_exact_checks_passed"})


if __name__ == "__main__":
    main()
