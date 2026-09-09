"""Branching-structure witnesses for GC-II capability accounting.

Restricted finite nondeterministic transition systems used to falsify overly
coarse trace-only future signatures.  The mechanism is classical process
semantics; this module makes the boundary executable for the GC-II program.
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, FrozenSet, Mapping, Sequence, Tuple


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
class NDWorld:
    labels: Mapping[str, str]
    edges: Sequence[Edge]

    def __post_init__(self) -> None:
        self._out: Dict[str, list[Edge]] = {s: [] for s in self.labels}
        for edge in self.edges:
            if edge.src not in self.labels or edge.dst not in self.labels:
                raise ValueError("every edge endpoint must be a declared state")
            self._out[edge.src].append(edge)

    def action_cost_traces(self, start: str, max_depth: int) -> FrozenSet[Tuple[Tuple[str, int], ...]]:
        """All action/cost traces of length at most max_depth, including empty."""
        if start not in self.labels:
            raise KeyError(start)
        if max_depth < 0:
            raise ValueError("max_depth must be nonnegative")
        traces: set[Tuple[Tuple[str, int], ...]] = {()}
        frontier: list[tuple[str, Tuple[Tuple[str, int], ...]]] = [(start, ())]
        for _ in range(max_depth):
            nxt: list[tuple[str, Tuple[Tuple[str, int], ...]]] = []
            for state, prefix in frontier:
                for edge in self._out.get(state, ()):
                    trace = prefix + ((edge.action, edge.cost),)
                    traces.add(trace)
                    nxt.append((edge.dst, trace))
            frontier = nxt
        return frozenset(traces)

    def successors(self, state: str, action: str) -> FrozenSet[str]:
        if state not in self.labels:
            raise KeyError(state)
        return frozenset(e.dst for e in self._out.get(state, ()) if e.action == action)

    def enabled_actions(self, state: str) -> FrozenSet[str]:
        if state not in self.labels:
            raise KeyError(state)
        return frozenset(e.action for e in self._out.get(state, ()))

    def robust_post_action_set(self, start: str, prefix_action: str) -> FrozenSet[str]:
        """Actions guaranteed enabled after every resolution of prefix_action.

        This is a minimal adversarial/robust capability semantics: if the world
        can nondeterministically resolve the prefix to several states, only an
        action enabled in every such state is guaranteed available afterwards.
        """
        succ = self.successors(start, prefix_action)
        if not succ:
            return frozenset()
        it = iter(succ)
        common = set(self.enabled_actions(next(it)))
        for state in it:
            common.intersection_update(self.enabled_actions(state))
        return frozenset(common)


def early_vs_late_choice_witness() -> tuple[NDWorld, str, str]:
    """Return a classic trace-equivalent but branching-distinct pair.

    late state p performs a then reaches one state where both b and c remain
    available. early state q performs a but nondeterministically commits to a
    b-only or c-only state.  Both have exactly traces epsilon,a,ab,ac (with
    identical zero costs), but their guaranteed post-a action sets differ.
    """
    world = NDWorld(
        labels={
            "p": "S", "p1": "M", "pb": "T", "pc": "T",
            "q": "S", "qb": "M", "qc": "M", "qbt": "T", "qct": "T",
        },
        edges=(
            Edge("p", "a", "p1"),
            Edge("p1", "b", "pb"),
            Edge("p1", "c", "pc"),
            Edge("q", "a", "qb"),
            Edge("q", "a", "qc"),
            Edge("qb", "b", "qbt"),
            Edge("qc", "c", "qct"),
        ),
    )
    return world, "p", "q"
