"""GC-II Audit 234: exact one-shot zero-error local-to-global translator bound.

For a finite world set W, a projection p(w) available to the decoder, and a
required global decision g(w), define the confusability graph H with an edge
between worlds having the same projection but different required decisions.
Any deterministic one-way translator message m(w) that permits exact recovery
of g(w) from (p(w),m(w)) must be a proper coloring of H. Conversely every
proper coloring is a valid message alphabet. Therefore the minimum number of
messages is chi(H), and the worst-case fixed-length payload is
ceil(log2 chi(H)) bits.

This is a concrete calibrated bridge from GC-I projection collision to an
operational translator lower bound, but the mechanism is standard zero-error
communication/source coding with decoder side information; it is not claimed
as GC novelty.
"""
from itertools import product
from math import ceil, log2


def edges(worlds, proj, decision):
    return {(u, v) for i, u in enumerate(worlds) for v in worlds[i+1:]
            if proj[u] == proj[v] and decision[u] != decision[v]}


def chromatic_number(worlds, E):
    if not worlds:
        return 0
    for k in range(1, len(worlds) + 1):
        for colors in product(range(k), repeat=len(worlds)):
            c = dict(zip(worlds, colors))
            if all(c[u] != c[v] for u, v in E):
                return k
    raise AssertionError("unreachable")


def translator_valid(worlds, proj, decision, msg):
    # Decoder must assign one decision to each observable pair (projection,msg).
    seen = {}
    for w in worlds:
        key = (proj[w], msg[w])
        if key in seen and seen[key] != decision[w]:
            return False
        seen[key] = decision[w]
    return True


def brute_min_messages(worlds, proj, decision):
    # Exhaustively search message alphabets. Intended only for tiny exact cases.
    for k in range(1, len(worlds) + 1):
        for labels in product(range(k), repeat=len(worlds)):
            msg = dict(zip(worlds, labels))
            if translator_valid(worlds, proj, decision, msg):
                return k
    raise AssertionError("unreachable")


def check_case(proj_values, decisions):
    worlds = tuple(range(len(proj_values)))
    proj = dict(enumerate(proj_values))
    decision = dict(enumerate(decisions))
    E = edges(worlds, proj, decision)
    chi = chromatic_number(worlds, E)
    mstar = brute_min_messages(worlds, proj, decision)
    assert chi == mstar
    bits = 0 if chi <= 1 else ceil(log2(chi))
    return chi, bits, len(E)


def main():
    # Degenerate/lossless case: projection already determines decision.
    assert check_case((0, 1), (0, 1)) == (1, 0, 0)

    # Binary collision: one hidden decision bit is necessary and sufficient.
    assert check_case((0, 0), (0, 1)) == (2, 1, 1)

    # Three incompatible global decisions behind one local view.
    assert check_case((0, 0, 0), (0, 1, 2)) == (3, 2, 3)

    # Exhaust all 4-world binary projections and binary required decisions.
    checked = 0
    for p in product(range(2), repeat=4):
        for g in product(range(2), repeat=4):
            chi, bits, _ = check_case(p, g)
            assert chi in (1, 2)
            assert bits in (0, 1)
            checked += 1

    # Multi-decision collision gives >1 bit even though projection arity is one.
    chi, bits, _ = check_case((0, 0, 0, 0), (0, 1, 2, 3))
    assert chi == 4 and bits == 2

    print("audit234: exact confusability/translator equivalence passed")
    print("exhaustive four-world binary cases:", checked)


if __name__ == "__main__":
    main()
