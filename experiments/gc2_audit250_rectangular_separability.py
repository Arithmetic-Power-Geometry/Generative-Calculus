"""GC-II Audit 250: exact finite verifier for rectangular separability boundary."""
from itertools import product, combinations
from math import inf
import heapq

# Two binary typed coordinates. Exhaust all 16 targets and classify rectangles.
Xj = ((0, 1), (0, 1))
X = list(product(*Xj))


def is_rectangle(F):
    if not F:
        return False  # excluded convention in theorem
    projections = [set(x[j] for x in F) for j in range(2)]
    return set(product(*projections)) == set(F)


def no_op_value(F, x):
    return 0 if x in F else inf


def has_nonnegative_additive_representation_no_ops(F):
    """For 0/+inf no-op value, additive nonnegative representation iff zero set is rectangular."""
    # Exhaust local zero sets Z0,Z1; values 0/+inf suffice for existence.
    subsets = []
    for vals in Xj:
        ss = []
        for mask in range(1 << len(vals)):
            ss.append({vals[i] for i in range(len(vals)) if mask & (1 << i)})
        subsets.append(ss)
    for Z0 in subsets[0]:
        for Z1 in subsets[1]:
            zero = set(product(Z0, Z1))
            if zero == set(F):
                return True
    return False

# Necessity/exact classification on every nonempty target.
nonempty = 0
rectangles = 0
for mask in range(1, 1 << len(X)):
    F = {X[i] for i in range(len(X)) if mask & (1 << i)}
    nonempty += 1
    r = is_rectangle(F)
    a = has_nonnegative_additive_representation_no_ops(F)
    assert r == a, (F, r, a)
    rectangles += int(r)

# Sufficiency stress test: exhaust many independent local weighted directed graphs.
# Each coordinate has two states; each directed toggle can be absent or have cost 0,1,2.
choices = (None, 0, 1, 2)


def local_dist(start, targets, c01, c10):
    if start in targets:
        return 0
    edge = c01 if start == 0 else c10
    other = 1 - start
    if edge is not None and other in targets:
        return edge
    return inf


def global_dist(start, F, edges):
    pq = [(0, start)]
    best = {start: 0}
    while pq:
        d, x = heapq.heappop(pq)
        if d != best[x]:
            continue
        if x in F:
            return d
        for j in range(2):
            ybit = 1 - x[j]
            c = edges[j][0] if x[j] == 0 else edges[j][1]
            if c is None:
                continue
            y = list(x); y[j] = ybit; y = tuple(y)
            nd = d + c
            if nd < best.get(y, inf):
                best[y] = nd
                heapq.heappush(pq, (nd, y))
    return inf

rect_targets = []
for mask in range(1, 1 << len(X)):
    F = {X[i] for i in range(len(X)) if mask & (1 << i)}
    if is_rectangle(F):
        rect_targets.append(F)

checks = 0
for c01_0, c10_0, c01_1, c10_1 in product(choices, repeat=4):
    edges = ((c01_0, c10_0), (c01_1, c10_1))
    for F in rect_targets:
        F0 = {x[0] for x in F}; F1 = {x[1] for x in F}
        for x in X:
            lhs = global_dist(x, F, edges)
            ds = [local_dist(x[0], F0, *edges[0]), local_dist(x[1], F1, *edges[1])]
            rhs = inf if inf in ds else sum(ds)
            assert lhs == rhs, (edges, F, x, lhs, rhs)
            checks += 1

# Explicit Audit-249 nonrectangle witness.
F_xor0 = {(0, 0), (1, 1)}
assert not is_rectangle(F_xor0)
assert not has_nonnegative_additive_representation_no_ops(F_xor0)

print("Audit 250 exact verifier PASS")
print("nonempty targets classified:", nonempty)
print("rectangular targets:", rectangles)
print("independent weighted-graph equality checks:", checks)
print("Audit-249 equality/XOR target correctly classified nonrectangular")
