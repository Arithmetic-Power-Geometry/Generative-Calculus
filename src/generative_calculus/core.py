from __future__ import annotations

from dataclasses import dataclass
from itertools import combinations, product
from typing import Iterable, Mapping, Sequence
import heapq
import math
import numpy as np


def dominates(a: Sequence[float], b: Sequence[float]) -> bool:
    """Return True when cost vector ``a`` is coordinate-wise no worse than ``b``."""
    if len(a) != len(b):
        raise ValueError("vectors must have the same dimension")
    return all(float(x) <= float(y) for x, y in zip(a, b))


def pareto_frontier(points: Iterable[Sequence[float]]) -> list[tuple[float, ...]]:
    pts = sorted({tuple(map(float, p)) for p in points})
    if not pts:
        return []
    d = len(pts[0])
    if any(len(p) != d for p in pts):
        raise ValueError("all points must have the same dimension")
    return sorted(p for p in pts if not any(q != p and dominates(q, p) for q in pts))


def feasible(frontier: Iterable[Sequence[float]], budget: Sequence[float]) -> bool:
    return any(dominates(p, budget) for p in frontier)


def feasible_tasks(task_frontiers: Mapping[str, Iterable[Sequence[float]]], budget: Sequence[float]) -> list[str]:
    return sorted(t for t, f in task_frontiers.items() if feasible(f, budget))


def blackwell_binary_deficiency(source_acc: float, target_acc: float) -> float:
    """Exact minimax total-variation deficiency for symmetric binary experiments."""
    s, t = float(source_acc), float(target_acc)
    if not (0.5 <= s <= 1.0 and 0.5 <= t <= 1.0):
        raise ValueError("accuracies must lie in [0.5, 1]")
    return max(0.0, t - s)


def marginal_incompleteness_example(low: float = 1.0, high: float = 3.0, b: float | None = None):
    """Canonical two-resource envelope with equal coordinate minima and different joint feasibility."""
    low, high = float(low), float(high)
    if high < low:
        raise ValueError("high must be >= low")
    if b is None:
        b = low
    A = pareto_frontier([(low, high), (high, low)])
    B = pareto_frontier([(low, low)])
    mA = tuple(min(p[i] for p in A) for i in range(2))
    mB = tuple(min(p[i] for p in B) for i in range(2))
    budget = (float(b), float(b))
    gap = min(float(np.linalg.norm(np.asarray(p) - np.asarray(mA))) for p in A)
    return {
        "A": A,
        "B": B,
        "marginal_A": mA,
        "marginal_B": mB,
        "budget": budget,
        "A_feasible": feasible(A, budget),
        "B_feasible": feasible(B, budget),
        "coupling_gap": gap,
    }


def equality_costs(n: int, epsilon: float = 1 / 3) -> dict[str, float]:
    """Transparent communication-complexity validation proxies for Equality."""
    n = int(n)
    epsilon = float(epsilon)
    if n < 1 or not (0 < epsilon < 0.5):
        raise ValueError("n>=1 and 0<epsilon<1/2 required")
    det = n + 1
    rand = int(np.ceil(np.log2(1 / epsilon))) + 1
    return {
        "n": n,
        "epsilon": epsilon,
        "deterministic_bits": det,
        "public_randomized_proxy_bits": rand,
        "ratio": det / rand,
    }


def hierarchy_costs(n_values=(8, 16, 32, 64), max_k: int = 5):
    return [
        {"n": int(n), "k": k, "cost": int(n) ** k}
        for n in n_values
        for k in range(1, int(max_k) + 1)
    ]


def parity_envelopes(m: int) -> tuple[set[tuple[int, ...]], set[tuple[int, ...]]]:
    """Even/odd parity compatibility envelopes used in projection-irreducibility tests."""
    m = int(m)
    if m < 2:
        raise ValueError("m must be >=2")
    even, odd = set(), set()
    for x in product((0, 1), repeat=m):
        (even if sum(x) % 2 == 0 else odd).add(tuple(x))
    return even, odd


def coordinate_projection(relation: Iterable[Sequence[int]], indices: Sequence[int]) -> set[tuple[int, ...]]:
    idx = tuple(int(i) for i in indices)
    return {tuple(row[i] for i in idx) for row in relation}


def proper_projection_agreement(m: int) -> bool:
    """Verify that parity envelopes agree on every proper coordinate projection."""
    even, odd = parity_envelopes(m)
    coords = range(m)
    for r in range(1, m):
        for S in combinations(coords, r):
            if coordinate_projection(even, S) != coordinate_projection(odd, S):
                return False
    return even != odd


def parity_projection_profile(m: int) -> list[dict[str, int | bool]]:
    even, odd = parity_envelopes(m)
    rows = []
    for r in range(1, m + 1):
        agreements = 0
        total = 0
        for S in combinations(range(m), r):
            total += 1
            agreements += coordinate_projection(even, S) == coordinate_projection(odd, S)
        rows.append({"projection_order": r, "agreeing": agreements, "total": total, "all_agree": agreements == total})
    return rows


def generative_order_parity(m: int) -> int:
    """For parity envelopes, the minimum projection order that distinguishes them is m."""
    if not proper_projection_agreement(m):
        raise AssertionError("parity construction lost its projection property")
    return int(m)


def support_function(points: Iterable[Sequence[float]], directions: np.ndarray) -> np.ndarray:
    """Support function of the convex hull of finite points, sampled at given directions."""
    P = np.asarray(list(points), dtype=float)
    D = np.asarray(directions, dtype=float)
    if P.ndim != 2 or D.ndim != 2 or P.shape[1] != D.shape[1]:
        raise ValueError("point and direction dimensions must agree")
    return np.max(P @ D.T, axis=0)


def convex_reconstruction_identity(
    K0: Iterable[Sequence[float]],
    K1: Iterable[Sequence[float]],
    t: float = 0.6,
    steps: int = 100,
    n_directions: int = 720,
) -> dict[str, float]:
    """Numerically validate the support-function Fundamental-Theorem sector.

    The path K_s=(1-s)K0+sK1 is represented by support functions. Because
    h_s=(1-s)h_0+s h_1, integrating the constant derivative h_1-h_0 must
    reconstruct h_t. The returned error is floating-point validation only;
    the mathematical identity is exact under the stated convex path.
    """
    t = float(t)
    if not (0 <= t <= 1) or steps < 1 or n_directions < 8:
        raise ValueError("0<=t<=1, steps>=1, n_directions>=8 required")
    theta = np.linspace(0, 2 * np.pi, n_directions, endpoint=False)
    dirs = np.column_stack((np.cos(theta), np.sin(theta)))
    h0 = support_function(K0, dirs)
    h1 = support_function(K1, dirs)
    derivative = h1 - h0
    dt = t / steps
    reconstructed = h0.copy()
    for _ in range(steps):
        reconstructed = reconstructed + derivative * dt
    exact = (1 - t) * h0 + t * h1
    return {
        "t": t,
        "steps": int(steps),
        "directions": int(n_directions),
        "max_abs_error": float(np.max(np.abs(reconstructed - exact))),
        "mean_abs_error": float(np.mean(np.abs(reconstructed - exact))),
    }


def cyclic_reversal_cost(n: int) -> dict[str, int | float]:
    """Closed bijective cycle showing microscopic bijectivity != cheap operational reversal."""
    n = int(n)
    if n < 1:
        raise ValueError("n must be >=1")
    period = 2 ** n
    return {
        "n": n,
        "period": period,
        "forward_cost": 1,
        "reverse_via_forward_cost": period - 1,
        "asymmetry_ratio": period - 1,
    }


def exact_program_qubits(generator_count: int) -> int:
    """No-programming corollary: qubits needed to host g orthogonal exact programs."""
    g = int(generator_count)
    if g < 1:
        raise ValueError("generator_count must be >=1")
    return int(math.ceil(math.log2(g))) if g > 1 else 0


@dataclass(frozen=True)
class WeightedEdge:
    target: str
    cost: float


def shortest_costs(graph: Mapping[str, Sequence[tuple[str, float]]], start: str) -> dict[str, float]:
    nodes = set(graph)
    for outs in graph.values():
        nodes.update(v for v, _ in outs)
    if start not in nodes:
        raise ValueError("start state missing from graph")
    dist = {s: math.inf for s in nodes}
    dist[start] = 0.0
    pq: list[tuple[float, str]] = [(0.0, start)]
    while pq:
        d, u = heapq.heappop(pq)
        if d != dist[u]:
            continue
        for v, w in graph.get(u, ()):  # terminal states are allowed
            w = float(w)
            if w < 0:
                raise ValueError("resource costs must be nonnegative")
            nd = d + w
            if nd < dist[v]:
                dist[v] = nd
                heapq.heappush(pq, (nd, v))
    return dist


def reachable_task_envelope(
    graph: Mapping[str, Sequence[tuple[str, float]]],
    task_at: Mapping[str, str],
    start: str,
    budget: float,
) -> set[str]:
    dist = shortest_costs(graph, start)
    return {task_at[s] for s, d in dist.items() if s in task_at and d <= float(budget)}


def reachable_transport_audit(
    graph: Mapping[str, Sequence[tuple[str, float]]],
    task_at: Mapping[str, str],
    max_budget: int = 10,
) -> list[dict[str, object]]:
    """Exhaustively audit E_y(B) subset E_x(B+c_xy) on a finite weighted system."""
    rows: list[dict[str, object]] = []
    for x in graph:
        dx = shortest_costs(graph, x)
        for y, cxy in dx.items():
            if math.isinf(cxy):
                continue
            for B in range(int(max_budget) + 1):
                Ey = reachable_task_envelope(graph, task_at, y, B)
                Ex = reachable_task_envelope(graph, task_at, x, B + cxy)
                rows.append({
                    "x": x,
                    "y": y,
                    "min_cost_x_to_y": cxy,
                    "budget_B": B,
                    "Ey_count": len(Ey),
                    "Ex_shifted_count": len(Ex),
                    "transport_holds": Ey.issubset(Ex),
                })
    return rows


def canonical_reachability_system():
    graph = {
        "A": [("B", 2), ("C", 5)],
        "B": [("C", 1), ("D", 4)],
        "C": [("D", 1), ("E", 5)],
        "D": [("E", 2)],
        "E": [("A", 7)],
    }
    task_at = {s: f"T_{s}" for s in graph}
    return graph, task_at
