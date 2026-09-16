"""Audit 178: exact finite check for interpreter-relative recovery product compilation.

No external dependencies.  The direct semantics and explicitly compiled product graph
must return the same minimum recovery cost.
"""
from heapq import heappush, heappop
from math import inf

# Operational states encode (mode, resource).  Recovery target is capability signature 'A'.
S = {"damaged0", "damaged1", "safe", "restored"}
signature = {"damaged0": "B", "damaged1": "B", "safe": "A", "restored": "A"}

# Interpreter memory q in {0,1}: q=1 means diagnostic information has been acquired.
Q = {0, 1}
q0 = 0

# (s,q) -> [(s',q',cost,label)] exactly defines K-admissible recovery semantics.
step = {
    ("damaged0", 0): [("damaged1", 1, 2, "diagnose"), ("safe", 0, 7, "fallback")],
    ("damaged0", 1): [("restored", 1, 3, "repair")],
    ("damaged1", 0): [("safe", 0, 7, "fallback")],
    ("damaged1", 1): [("restored", 1, 3, "repair")],
    ("safe", 0): [], ("safe", 1): [],
    ("restored", 0): [], ("restored", 1): [],
}


def direct_recovery(start_s, target_sig):
    """Dijkstra directly over interpreter semantics, without pre-building product edges."""
    pq = [(0, start_s, q0)]
    best = {(start_s, q0): 0}
    while pq:
        d, s, q = heappop(pq)
        if d != best[(s, q)]:
            continue
        if signature[s] == target_sig:
            return d
        for sp, qp, c, _ in step[(s, q)]:
            nd = d + c
            if nd < best.get((sp, qp), inf):
                best[(sp, qp)] = nd
                heappush(pq, (nd, sp, qp))
    return inf


def compiled_recovery(start_s, target_sig):
    """Build P_K=SxQ explicitly, then solve ordinary shortest path."""
    vertices = {(s, q) for s in S for q in Q}
    edges = {v: [] for v in vertices}
    for v in vertices:
        for sp, qp, c, label in step[v]:
            assert (sp, qp) in vertices
            assert c >= 0
            edges[v].append(((sp, qp), c, label))

    start = (start_s, q0)
    pq = [(0, start)]
    best = {start: 0}
    while pq:
        d, v = heappop(pq)
        if d != best[v]:
            continue
        if signature[v[0]] == target_sig:
            return d, len(vertices), sum(map(len, edges.values()))
        for w, c, _ in edges[v]:
            nd = d + c
            if nd < best.get(w, inf):
                best[w] = nd
                heappush(pq, (nd, w))
    return inf, len(vertices), sum(map(len, edges.values()))


if __name__ == "__main__":
    direct = direct_recovery("damaged0", "A")
    compiled, nv, ne = compiled_recovery("damaged0", "A")
    assert direct == compiled == 5
    assert direct_recovery("safe", "A") == 0
    print({"direct_recovery_cost": direct, "compiled_recovery_cost": compiled,
           "product_vertices": nv, "product_edges": ne, "status": "PASS"})
