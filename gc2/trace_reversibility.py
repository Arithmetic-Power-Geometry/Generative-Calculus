"""Finite witnesses for trace-sensitive reversibility in GC-II.

This module intentionally studies a restricted deterministic finite-world model.
It does not claim novelty; it supports falsification tests for endpoint-only
reversibility accounting.
"""
from __future__ import annotations

from dataclasses import dataclass
from heapq import heappop, heappush
from typing import Dict, FrozenSet, Iterable, Mapping, Optional, Sequence, Tuple


@dataclass(frozen=True)
class Edge:
    src: str
    action: str
    dst: str
    cost: int = 0

    def __post_init__(self) -> None:
        if self.cost < 0:
            raise ValueError("edge cost must be nonnegative")


@dataclass
class FiniteWorld:
    labels: Mapping[str, str]
    edges: Sequence[Edge]

    def __post_init__(self) -> None:
        self._out: Dict[str, list[Edge]] = {s: [] for s in self.labels}
        for edge in self.edges:
            if edge.src not in self.labels or edge.dst not in self.labels:
                raise ValueError("every edge endpoint must be a declared state")
            self._out.setdefault(edge.src, []).append(edge)

    def step(self, state: str, action: str) -> str:
        matches = [e for e in self._out.get(state, ()) if e.action == action]
        if len(matches) != 1:
            raise ValueError("action must be uniquely enabled at the supplied state")
        return matches[0].dst

    def min_cost_to_label(self, start: str, target_label: str) -> Optional[int]:
        """Shortest nonnegative cost from start to any state with target_label."""
        if start not in self.labels:
            raise KeyError(start)
        pq: list[Tuple[int, str]] = [(0, start)]
        best: Dict[str, int] = {start: 0}
        while pq:
            cost, state = heappop(pq)
            if cost != best[state]:
                continue
            if self.labels[state] == target_label:
                return cost
            for edge in self._out.get(state, ()):
                new_cost = cost + edge.cost
                if new_cost < best.get(edge.dst, 10**30):
                    best[edge.dst] = new_cost
                    heappush(pq, (new_cost, edge.dst))
        return None

    def future_label_signature(self, start: str, depth: int) -> FrozenSet[str]:
        """Labels reachable within at most ``depth`` transitions, including start."""
        if depth < 0:
            raise ValueError("depth must be nonnegative")
        if start not in self.labels:
            raise KeyError(start)
        frontier = {(start, 0)}
        seen = {(start, 0)}
        labels = {self.labels[start]}
        while frontier:
            state, d = frontier.pop()
            if d == depth:
                continue
            for edge in self._out.get(state, ()):
                labels.add(self.labels[edge.dst])
                item = (edge.dst, d + 1)
                if item not in seen:
                    seen.add(item)
                    frontier.add(item)
        return frozenset(labels)


def canonical_endpoint_cost_pair(world: FiniteWorld, x_state: str, y_label: str, x_label: str) -> Tuple[Optional[int], Optional[int]]:
    """Return endpoint-only forward/reverse costs for a chosen X start and Y label.

    Reverse cost is measured from the unique state reached by action ``f``.
    This deliberate specialization keeps the falsification witness transparent.
    """
    y_state = world.step(x_state, "f")
    return (
        world.min_cost_to_label(x_state, y_label),
        world.min_cost_to_label(y_state, x_label),
    )


def round_trip_residual(world: FiniteWorld, x_state: str, depth: int = 1) -> Tuple[FrozenSet[str], FrozenSet[str]]:
    """Compare bounded future-capability signatures before and after f;r."""
    y_state = world.step(x_state, "f")
    returned = world.step(y_state, "r")
    return (
        world.future_label_signature(x_state, depth),
        world.future_label_signature(returned, depth),
    )


def endpoint_collision_witnesses() -> Tuple[FiniteWorld, FiniteWorld]:
    """Two worlds with identical endpoint costs but different round-trip residuals.

    In the reversible witness, f;r returns to x0. In the degrading witness, f;r
    returns to x1, which has the same endpoint label X but lacks the future G
    capability available from x0.
    """
    reversible = FiniteWorld(
        labels={"x0": "X", "y": "Y", "g": "G"},
        edges=(
            Edge("x0", "f", "y", 1),
            Edge("y", "r", "x0", 1),
            Edge("x0", "probe", "g", 0),
        ),
    )
    degrading = FiniteWorld(
        labels={"x0": "X", "y": "Y", "x1": "X", "g": "G"},
        edges=(
            Edge("x0", "f", "y", 1),
            Edge("y", "r", "x1", 1),
            Edge("x0", "probe", "g", 0),
        ),
    )
    return reversible, degrading
