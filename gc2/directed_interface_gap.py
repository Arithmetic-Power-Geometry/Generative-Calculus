"""Finite whole-envelope directed interface gap.

For task-indexed representations X=(x_t) and Y=(y_t), define
m(X->Y)=max_x |{y_t : x_t=x}| and d_I(X,Y)=log2 m.
This equals the log alphabet size needed by the exact shared-translator
interface theorem.  It is a restricted finite specialization, not a claim
of mathematical novelty; it collides with conditional Hartley/support-size
quantities and zero-error coding ideas.
"""
from __future__ import annotations

from collections import defaultdict
from math import log2
from typing import Hashable, Sequence


def collision_multiplicity(source: Sequence[Hashable], target: Sequence[Hashable]) -> int:
    if len(source) != len(target):
        raise ValueError("source and target must index the same tasks")
    if not source:
        return 1
    fibres: dict[Hashable, set[Hashable]] = defaultdict(set)
    for x, y in zip(source, target):
        fibres[x].add(y)
    return max(len(v) for v in fibres.values())


def directed_interface_gap(source: Sequence[Hashable], target: Sequence[Hashable]) -> float:
    """log2 of exact auxiliary alphabet requirement in the shared translator model."""
    return log2(collision_multiplicity(source, target))


def fixed_width_bits(source: Sequence[Hashable], target: Sequence[Hashable]) -> int:
    """Exact fixed-width binary interface requirement ceil(log2 m)."""
    m = collision_multiplicity(source, target)
    return (m - 1).bit_length()


def composition_bound_holds(x: Sequence[Hashable], y: Sequence[Hashable], z: Sequence[Hashable]) -> bool:
    """Exact multiplicative composition law m(X->Z)<=m(X->Y)m(Y->Z)."""
    if not (len(x) == len(y) == len(z)):
        raise ValueError("all representations must index the same tasks")
    return collision_multiplicity(x, z) <= collision_multiplicity(x, y) * collision_multiplicity(y, z)
