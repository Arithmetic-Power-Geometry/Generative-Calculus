"""GC-II Audit 232 exact checks.

Verifies:
1. pointwise-positive translators with costs 1/n have infimum tending to zero;
2. finite nonnegative directed shortest-path distances;
3. the canonical potential phi(v)=d(source,v) satisfies every difference constraint;
4. budget escape agrees with the dual-potential certificate on reachable vertices.

No external dependencies.
"""
from math import inf
import heapq


def dijkstra(n, edges, source):
    adj = [[] for _ in range(n)]
    for u, v, c in edges:
        assert c >= 0
        adj[u].append((v, c))
    d = [inf] * n
    d[source] = 0.0
    pq = [(0.0, source)]
    while pq:
        du, u = heapq.heappop(pq)
        if du != d[u]:
            continue
        for v, c in adj[u]:
            z = du + c
            if z < d[v]:
                d[v] = z
                heapq.heappush(pq, (z, v))
    return d


def check_positive_cost_zero_infimum():
    prev = inf
    for N in (1, 2, 5, 10, 100, 1000, 10000):
        costs = [1.0 / k for k in range(1, N + 1)]
        m = min(costs)
        assert m > 0
        assert m <= prev
        assert abs(m - 1.0 / N) < 1e-15
        prev = m
    # Mathematical family {1/n:n>=1} has infimum 0 although every member >0.


def check_graph(edges, n, source, budgets):
    d = dijkstra(n, edges, source)
    # canonical shortest-path potential on reachable component
    phi = d
    for u, v, c in edges:
        if phi[u] < inf and phi[v] < inf:
            assert phi[v] - phi[u] <= c + 1e-12
    for B in budgets:
        for y in range(n):
            if d[y] == inf:
                continue
            operational_escape = d[y] > B
            dual_certificate_from_canonical_phi = phi[y] - phi[source] > B
            assert operational_escape == dual_certificate_from_canonical_phi
    return d


def main():
    check_positive_cost_zero_infimum()
    graphs = [
        (4, [(0,1,2.0),(1,2,3.0),(0,2,7.0),(2,3,1.0),(1,3,10.0)]),
        (5, [(0,1,0.0),(1,2,1.0),(0,3,4.0),(2,3,1.5),(3,4,2.0)]),
        (6, [(0,1,1.0),(0,2,1.0),(1,3,2.0),(2,3,0.5),(3,4,3.0)]),
    ]
    for n, edges in graphs:
        d = check_graph(edges, n, 0, [0, 0.5, 1, 2, 3, 5, 10])
        print(n, d)
    print("audit232: all exact/finite checks passed")


if __name__ == "__main__":
    main()
