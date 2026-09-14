"""GC-II Audit 146: finite dynamic translator compilation no-go.

Exhaustively enumerate every deterministic 3-state/2-action translator whose
state-action entry is either disabled or moves to one of 3 states at cost 0/1.
Compare exact shortest-path cost on the augmented operational state graph with
brute-force simple action sequences. With non-negative edge costs, an optimal
reachable path has a simple representative, hence length <= |Q|-1.
"""
from itertools import product
from collections import Counter
import heapq
import json
import math
from pathlib import Path

N_STATES = 3
N_ACTIONS = 2
START = 0
TARGET = 2
OPTIONS = [None] + [(nxt, cost) for nxt in range(N_STATES) for cost in (0, 1)]


def graph_optimum(table):
    dist = [math.inf] * N_STATES
    dist[START] = 0
    pq = [(0, START)]
    while pq:
        d, state = heapq.heappop(pq)
        if d != dist[state]:
            continue
        for action in range(N_ACTIONS):
            edge = table[state * N_ACTIONS + action]
            if edge is None:
                continue
            nxt, cost = edge
            nd = d + cost
            if nd < dist[nxt]:
                dist[nxt] = nd
                heapq.heappush(pq, (nd, nxt))
    return dist[TARGET]


def brute_simple_optimum(table):
    best = math.inf
    for length in range(N_STATES):
        for actions in product(range(N_ACTIONS), repeat=length):
            state = START
            cost = 0
            visited = {START}
            valid = True
            for action in actions:
                edge = table[state * N_ACTIONS + action]
                if edge is None:
                    valid = False
                    break
                nxt, edge_cost = edge
                cost += edge_cost
                state = nxt
                if state in visited and state != TARGET:
                    valid = False
                    break
                visited.add(state)
            if valid and state == TARGET:
                best = min(best, cost)
    return best


def main():
    total = mismatches = reachable = zero_cost = 0
    cost_hist = Counter()
    for table in product(OPTIONS, repeat=N_STATES * N_ACTIONS):
        graph = graph_optimum(table)
        brute = brute_simple_optimum(table)
        total += 1
        same = (math.isinf(graph) and math.isinf(brute)) or graph == brute
        if not same:
            mismatches += 1
        if not math.isinf(graph):
            reachable += 1
            cost_hist[int(graph)] += 1
            if graph == 0:
                zero_cost += 1

    result = {
        "audit": 146,
        "model": "deterministic finite dynamic translator; 3 states, 2 state-dependent actions, edge costs in {0,1}",
        "systems_exhaustively_checked": total,
        "reachable_systems": reachable,
        "unreachable_systems": total - reachable,
        "zero_cost_reachable_systems": zero_cost,
        "minimum_cost_histogram": dict(sorted(cost_hist.items())),
        "shortest_path_vs_simple_sequence_mismatches": mismatches,
        "status": "PASS" if mismatches == 0 else "FAIL",
        "claim_scope": "finite fully observed augmented operational state; deterministic transitions; nonnegative additive costs",
    }
    print(json.dumps(result, indent=2))
    out = Path("results/gc2_audit146_dynamic_translator_shortest_path.json")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    if mismatches:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
