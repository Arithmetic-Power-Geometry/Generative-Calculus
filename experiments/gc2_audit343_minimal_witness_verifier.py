from itertools import product
import json


def tc(n, edges):
    r = set(edges) | {(i, i) for i in range(n)}
    changed = True
    while changed:
        changed = False
        add = {(a, d) for a, b in r for c, d in r if b == c}
        if not add <= r:
            r |= add
            changed = True
    return r


def labelled_preorders(n):
    off = [(i, j) for i in range(n) for j in range(n) if i != j]
    out = []
    for mask in range(1 << len(off)):
        r = {(i, i) for i in range(n)}
        r |= {off[k] for k in range(len(off)) if (mask >> k) & 1}
        if tc(n, r) == r:
            out.append(r)
    return out


def subsets(items):
    items = list(items)
    for mask in range(1 << len(items)):
        yield frozenset(items[i] for i in range(len(items)) if (mask >> i) & 1)


def mobius(vals, universe):
    out = {}
    for t in subsets(universe):
        out[t] = sum(((-1) ** (len(t) - len(u))) * vals[u] for u in subsets(t))
    return out


def run(n=3):
    coefficient_cases = 0
    failures = 0
    unique_witness_pairs = 0
    unique_witness_failures = 0
    ps = labelled_preorders(n)
    for b in ps:
        absent = frozenset(p for p in product(range(n), repeat=2) if p not in b)
        ss = list(subsets(absent))
        vals = {s: len(tc(n, b | set(s)) - b) for s in ss}
        direct = mobius(vals, absent)
        full_novel = tc(n, b | set(absent)) - b
        witness = {}
        for p in full_novel:
            successful = [s for s in ss if p in tc(n, b | set(s)) - b]
            mins = [s for s in successful if not any(t < s for t in successful)]
            witness[p] = mins
            if len(mins) == 1:
                unique_witness_pairs += 1
        for t in ss:
            predicted = 0
            if t:
                for mins in witness.values():
                    m = len(mins)
                    for kmask in range(1, 1 << m):
                        chosen = [mins[i] for i in range(m) if (kmask >> i) & 1]
                        union = frozenset().union(*chosen)
                        if union == t:
                            predicted += (-1) ** (len(chosen) + 1)
            coefficient_cases += 1
            if predicted != direct[t]:
                failures += 1
        # Pairwise unique-witness check: its own Mobius spectrum is one point mass.
        for p, mins in witness.items():
            if len(mins) != 1:
                continue
            w = mins[0]
            gp = {s: int(p in tc(n, b | set(s)) - b) for s in ss}
            jp = mobius(gp, absent)
            for t, value in jp.items():
                expected = int(t == w)
                if value != expected:
                    unique_witness_failures += 1
    return {
        "n": n,
        "labelled_preorders": len(ps),
        "subset_coefficient_cases": coefficient_cases,
        "witness_union_formula_failures": failures,
        "unique_witness_pairs_checked": unique_witness_pairs,
        "unique_witness_spectrum_failures": unique_witness_failures,
    }


if __name__ == "__main__":
    print(json.dumps(run(), indent=2, sort_keys=True))
