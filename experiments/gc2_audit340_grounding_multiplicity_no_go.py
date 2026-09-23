#!/usr/bin/env python3
"""Exact verifier for GC-II Audit 340.

Checks the local-grounding versus complete-grounding construction for q=2..64.
No external packages are required.
"""


def transitive_novelty(q, edges):
    reach = [[False] * q for _ in range(q)]
    for i in range(q):
        reach[i][i] = True
    for a, b in edges:
        reach[a][b] = True
    for k in range(q):
        for i in range(q):
            if reach[i][k]:
                for j in range(q):
                    reach[i][j] = reach[i][j] or reach[k][j]
    return sum(reach[i][j] and i != j for i in range(q) for j in range(q))


def main():
    failures = []
    rows = []
    for q in range(2, 65):
        local_edges = {(0, 1)}
        ground_edges = {(i, j) for i in range(q) for j in range(q) if i != j}
        local = transitive_novelty(q, local_edges)
        ground = transitive_novelty(q, ground_edges)
        expected_ground = q * (q - 1)
        ok = local == 1 and ground == expected_ground
        if not ok:
            failures.append({"q": q, "local": local, "ground": ground,
                             "expected_ground": expected_ground})
        rows.append((q, local, ground, ground // local))

    print(f"paired_cases={len(rows)} failures={len(failures)}")
    print(f"largest_case=q={rows[-1][0]} local={rows[-1][1]} "
          f"ground={rows[-1][2]} ratio={rows[-1][3]}")
    if failures:
        for failure in failures[:10]:
            print("FAIL", failure)
        raise SystemExit(1)


if __name__ == "__main__":
    main()
