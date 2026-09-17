"""GC-II Audit 206 exact finite check.

Enumerate every deterministic 2-state Moore machine with two actions and binary
outputs. Verify that equality under all finite action experiments (represented
by the stabilized observational partition) equals deterministic bisimulation.
No third-party dependencies.
"""
from itertools import product


def refine(delta, out, n=2, actions=2):
    # Initial partition: directly observable output.
    cls = tuple(out)
    while True:
        sig = []
        for s in range(n):
            sig.append((out[s],) + tuple(cls[delta[s][a]] for a in range(actions)))
        ids = {}
        nxt = []
        for x in sig:
            if x not in ids:
                ids[x] = len(ids)
            nxt.append(ids[x])
        nxt = tuple(nxt)
        # Compare induced equivalence, not arbitrary class labels.
        old_eq = tuple(cls[i] == cls[j] for i in range(n) for j in range(n))
        new_eq = tuple(nxt[i] == nxt[j] for i in range(n) for j in range(n))
        if old_eq == new_eq:
            return nxt
        cls = nxt


def bounded_words(actions, depth):
    yield ()
    for k in range(1, depth + 1):
        yield from product(range(actions), repeat=k)


def obs(delta, out, s, word):
    for a in word:
        s = delta[s][a]
    return out[s]


def main():
    n, actions = 2, 2
    machines = 0
    pair_checks = 0
    for trans_flat in product(range(n), repeat=n * actions):
        delta = tuple(tuple(trans_flat[s * actions:(s + 1) * actions]) for s in range(n))
        for out in product((0, 1), repeat=n):
            machines += 1
            cls = refine(delta, out, n, actions)
            # For n=2, depth n-1 is sufficient after the direct-output layer.
            words = tuple(bounded_words(actions, n - 1))
            for s in range(n):
                for t in range(n):
                    pair_checks += 1
                    testing = all(obs(delta, out, s, w) == obs(delta, out, t, w) for w in words)
                    bisim = cls[s] == cls[t]
                    assert testing == bisim, (delta, out, s, t, testing, bisim)
    print({"machines": machines, "ordered_pair_checks": pair_checks, "status": "PASS"})


if __name__ == "__main__":
    main()
