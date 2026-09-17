"""GC-II Audit 202: exact finite checks for minimum-cost simulation geometry.

Status target:
- directed minimum simulation cost obeys identity/triangle when simulators compose
  and costs are subadditive;
- the symmetric reversibility gap d(A,B)+d(B,A) is therefore a pseudometric
  (after quotienting zero-cost equivalence as needed).

This script exhaustively checks these statements on every directed weighted graph
with 3 vertices and edge costs in {1,2}, with zero-cost identities. Shortest-path
closure is the minimum compositional simulation cost.
"""
from itertools import product
from math import inf

N = 3
pairs = [(i,j) for i in range(N) for j in range(N) if i != j]
checked_graphs = 0
checked_triangles = 0

for weights in product((1,2), repeat=len(pairs)):
    d = [[0 if i == j else inf for j in range(N)] for i in range(N)]
    for (i,j), w in zip(pairs, weights):
        d[i][j] = w

    # Floyd-Warshall = closure under composed simulators.
    for k in range(N):
        for i in range(N):
            for j in range(N):
                d[i][j] = min(d[i][j], d[i][k] + d[k][j])

    # Directed identity and triangle inequality.
    for i in range(N):
        assert d[i][i] == 0
    for i in range(N):
        for j in range(N):
            for k in range(N):
                assert d[i][k] <= d[i][j] + d[j][k]
                checked_triangles += 1

    # Symmetric reversibility gap.
    g = [[d[i][j] + d[j][i] for j in range(N)] for i in range(N)]
    for i in range(N):
        assert g[i][i] == 0
        for j in range(N):
            assert g[i][j] == g[j][i]
            for k in range(N):
                assert g[i][k] <= g[i][j] + g[j][k]

    checked_graphs += 1

print({"graphs": checked_graphs, "directed_triangle_checks": checked_triangles,
       "status": "PASS"})
