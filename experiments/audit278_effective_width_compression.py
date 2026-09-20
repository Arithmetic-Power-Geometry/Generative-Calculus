#!/usr/bin/env python3
"""Exact finite verifier for GC-II Audit 278.

Uses alpha=2 and integer powers, so all cover checks are exact integer comparisons.
It constructs many mode-local families embedded in ambient dimensions larger than
active width, builds one representative per exact-zero/geometric-bin signature,
and verifies alpha-cover and the stated cardinality bound.
"""
from itertools import combinations, product

ALPHA = 2


def sig_value(v):
    if v == 0:
        return (0, 0)
    # Positive test alphabet is powers of two. Separate adjacent powers into
    # separate half-open geometric bins, matching floor(log_2(v/m)).
    return (1, v.bit_length() - 1)


def signature(y, active):
    return tuple(sig_value(y[i]) for i in active)


def covers(s, y):
    return all(si <= ALPHA * yi for si, yi in zip(s, y))


def certificate(mode, active):
    reps = {}
    for y in mode:
        reps.setdefault(signature(y, active), y)
    return list(reps.values())


def theoretical_bound(mode, active):
    out = 1
    for i in active:
        positives = [y[i] for y in mode if y[i] > 0]
        if not positives:
            # only exact-zero symbol is occupied; theorem's coarse bound is >=1
            k = 1
        else:
            mn, mx = min(positives), max(positives)
            ratio = mx // mn
            # test alphabet guarantees power-of-two ratios
            lg = ratio.bit_length() - 1
            k = 2 + lg
        out *= k
    return out


def make_mode(d, active, baseline, alphabet):
    mode = []
    for vals in product(alphabet, repeat=len(active)):
        y = list(baseline)
        for i, v in zip(active, vals):
            y[i] = v
        mode.append(tuple(y))
    return mode


def main():
    families = targets = checks = 0
    # Ambient d grows while active width stays <=3.
    for d in range(2, 8):
        coords = range(d)
        for w in range(0, min(3, d) + 1):
            for active in combinations(coords, w):
                for alphabet in ((1, 2), (0, 1, 2), (0, 1, 2, 4)):
                    # Inactive coordinates are deliberately nonzero and vary by
                    # constructed mode identity, but remain constant within mode.
                    baseline = tuple(8 + 2 * i for i in coords)
                    mode = make_mode(d, active, baseline, alphabet)
                    cert = certificate(mode, active)
                    bound = theoretical_bound(mode, active)
                    assert len(cert) <= bound
                    for y in mode:
                        assert any(covers(s, y) for s in cert)
                        targets += 1
                        checks += len(cert)
                    # locality check
                    aset = set(active)
                    for i in coords:
                        if i not in aset:
                            assert len({y[i] for y in mode}) == 1
                    families += 1

    # Union-of-modes test: different active scopes and inactive baselines.
    for d in range(3, 8):
        modes = []
        for j, active in enumerate(((0,), (1, 2), tuple(range(min(3, d))))):
            active = tuple(i for i in active if i < d)
            baseline = tuple(20 + 3*j + i for i in range(d))
            mode = make_mode(d, active, baseline, (0, 1, 2, 4))
            modes.append((mode, active))
        union_cert = []
        union_bound = 0
        for mode, active in modes:
            c = certificate(mode, active)
            union_cert.extend(c)
            union_bound += theoretical_bound(mode, active)
            for y in mode:
                assert any(covers(s, y) for s in c)
                targets += 1
                checks += len(c)
        assert len(union_cert) <= union_bound
        families += len(modes)

    print({
        "status": "PASS",
        "alpha": ALPHA,
        "mode_families": families,
        "targets_checked": targets,
        "representative_target_checks": checks,
        "max_ambient_dimension": 7,
        "max_active_width": 3,
    })


if __name__ == "__main__":
    main()
