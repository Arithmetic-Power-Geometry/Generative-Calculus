from __future__ import annotations

from collections import defaultdict
from math import ceil, log2
from typing import Hashable, Mapping

Task = Hashable
Symbol = Hashable
Label = Hashable


def collision_fibres(source: Mapping[Task, Symbol], target: Mapping[Task, Label]):
    if set(source) != set(target):
        raise ValueError("source and target must have exactly the same task domain")
    fibres: dict[Symbol, set[Label]] = defaultdict(set)
    for t, x in source.items():
        fibres[x].add(target[t])
    return dict(fibres)


def globally_convertible(source: Mapping[Task, Symbol], target: Mapping[Task, Label]) -> bool:
    return all(len(labels) <= 1 for labels in collision_fibres(source, target).values())


def collision_multiplicity(source: Mapping[Task, Symbol], target: Mapping[Task, Label]) -> int:
    fibres = collision_fibres(source, target)
    return max((len(v) for v in fibres.values()), default=1)


def min_interface_states(source: Mapping[Task, Symbol], target: Mapping[Task, Label]) -> int:
    return collision_multiplicity(source, target)


def min_interface_bits(source: Mapping[Task, Symbol], target: Mapping[Task, Label]) -> int:
    q = min_interface_states(source, target)
    return 0 if q <= 1 else ceil(log2(q))


def construct_interface_code(source: Mapping[Task, Symbol], target: Mapping[Task, Label]):
    fibres: dict[Symbol, dict[Label, int]] = {}
    for x, labels in collision_fibres(source, target).items():
        fibres[x] = {y: i for i, y in enumerate(sorted(labels, key=repr))}
    code = {t: fibres[source[t]][target[t]] for t in source}
    translator = {(source[t], code[t]): target[t] for t in source}
    return code, translator


def translate_all(source: Mapping[Task, Symbol], code: Mapping[Task, int], translator: Mapping[tuple[Symbol, int], Label]):
    return {t: translator[(source[t], code[t])] for t in source}


def min_weighted_shared_translation_error(
    source: Mapping[Task, Symbol],
    target: Mapping[Task, Label],
    weights: Mapping[Task, float] | None = None,
) -> float:
    if set(source) != set(target):
        raise ValueError("source and target must have exactly the same task domain")
    if weights is None:
        weights = {t: 1.0 for t in source}
    if set(weights) != set(source):
        raise ValueError("weights must have exactly the same task domain")
    total_error = 0.0
    by_x: dict[Symbol, dict[Label, float]] = defaultdict(lambda: defaultdict(float))
    for t, x in source.items():
        w = float(weights[t])
        if w < 0:
            raise ValueError("weights must be nonnegative")
        by_x[x][target[t]] += w
    for masses in by_x.values():
        total = sum(masses.values())
        total_error += total - max(masses.values(), default=0.0)
    return total_error
