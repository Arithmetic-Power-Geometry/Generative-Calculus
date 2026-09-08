from __future__ import annotations

from dataclasses import dataclass
from itertools import combinations, product
from math import inf
from typing import Iterable, Sequence


@dataclass(frozen=True)
class Edge:
    u: int
    v: int
    cost: tuple[int, ...]
    info: frozenset[str] = frozenset()
    actions: frozenset[str] = frozenset()
    rules: frozenset[str] = frozenset()


@dataclass(frozen=True)
class Context:
    budget: tuple[int, ...]
    info: frozenset[str] = frozenset()
    actions: frozenset[str] = frozenset()
    rules: frozenset[str] = frozenset()


def _add(a: Sequence[int], b: Sequence[int]) -> tuple[int, ...]:
    return tuple(x + y for x, y in zip(a, b))


def _sub(a: Sequence[int], b: Sequence[int]) -> tuple[int, ...]:
    return tuple(x - y for x, y in zip(a, b))


def _positive_part(a: Sequence[int]) -> tuple[int, ...]:
    return tuple(max(0, x) for x in a)


def _leq(a: Sequence[int], b: Sequence[int]) -> bool:
    return all(x <= y for x, y in zip(a, b))


def enabled(edge: Edge, context: Context) -> bool:
    return (
        edge.info <= context.info
        and edge.actions <= context.actions
        and edge.rules <= context.rules
    )


def reachable_states(
    n_states: int,
    edges: Sequence[Edge],
    starts: Iterable[int],
    context: Context,
) -> set[int]:
    """Projected reachability of the lifted cumulative-resource closure."""
    del n_states  # retained for an explicit finite-world signature
    zero = (0,) * len(context.budget)
    seen = {(s, zero) for s in starts}
    queue = list(seen)
    while queue:
        u, used = queue.pop()
        for edge in edges:
            if edge.u != u or not enabled(edge, context):
                continue
            nxt_used = _add(used, edge.cost)
            item = (edge.v, nxt_used)
            if _leq(nxt_used, context.budget) and item not in seen:
                seen.add(item)
                queue.append(item)
    return {state for state, _ in seen}


def nonlinear_augmentation_penalty(
    delta_budget: Sequence[int],
    delta_info: frozenset[str],
    delta_actions: frozenset[str],
    delta_rules: frozenset[str],
) -> int:
    """Positive-definite monotone penalty with a resource--gate interaction term."""
    continuous = sum(delta_budget)
    discrete = len(delta_info) + len(delta_actions) + len(delta_rules)
    return continuous + discrete + continuous * discrete


def omega_path_formula(
    edges: Sequence[Edge],
    starts: Iterable[int],
    context: Context,
    target: int,
    max_steps: int,
) -> float:
    """Exact finite path formula for the candidate Generative Novelty Gap.

    Omega_G is the minimum nonlinear augmentation penalty needed to make the
    target reachable.  For a path p, the minimal augmentation is determined by
    positive resource-budget excess and by the union of missing information,
    action/interface, and rule requirements on p.
    """
    best = inf
    zero = (0,) * len(context.budget)
    stack = [
        (s, zero, frozenset(), frozenset(), frozenset(), 0)
        for s in starts
    ]
    while stack:
        u, used, req_i, req_a, req_l, depth = stack.pop()
        if u == target:
            db = _positive_part(_sub(used, context.budget))
            best = min(
                best,
                nonlinear_augmentation_penalty(
                    db,
                    req_i - context.info,
                    req_a - context.actions,
                    req_l - context.rules,
                ),
            )
        if depth == max_steps:
            continue
        for edge in edges:
            if edge.u != u:
                continue
            stack.append(
                (
                    edge.v,
                    _add(used, edge.cost),
                    req_i | edge.info,
                    req_a | edge.actions,
                    req_l | edge.rules,
                    depth + 1,
                )
            )
    return best


def _subsets(items: frozenset[str]) -> list[frozenset[str]]:
    seq = tuple(items)
    return [
        frozenset(choice)
        for k in range(len(seq) + 1)
        for choice in combinations(seq, k)
    ]


def omega_bruteforce_augmentation(
    n_states: int,
    edges: Sequence[Edge],
    starts: Iterable[int],
    context: Context,
    target: int,
    max_extra: int,
    universe_info: frozenset[str],
    universe_actions: frozenset[str],
    universe_rules: frozenset[str],
) -> float:
    """Independent finite audit by explicit context-augmentation enumeration."""
    best = inf
    for db in product(range(max_extra + 1), repeat=len(context.budget)):
        for di in _subsets(universe_info - context.info):
            for da in _subsets(universe_actions - context.actions):
                for dl in _subsets(universe_rules - context.rules):
                    augmented = Context(
                        _add(context.budget, db),
                        context.info | di,
                        context.actions | da,
                        context.rules | dl,
                    )
                    if target in reachable_states(n_states, edges, starts, augmented):
                        best = min(
                            best,
                            nonlinear_augmentation_penalty(db, di, da, dl),
                        )
    return best
