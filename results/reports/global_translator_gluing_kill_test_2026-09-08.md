# Global-translator gluing kill test

Status: **IMPORTED/KNOWN mathematical skeleton; GC-scoped negative result**. This is a falsification constraint, not a breakthrough claim.

## Question

If every task in a source world can be translated separately into a target world with the same stated resource overhead, does that imply the existence of one globally faithful translator for the whole embodied operational envelope?

## Minimal finite obstruction

Let source world B have one admissible protocol `p` that simultaneously realizes two tasks `T1` and `T2` at zero cost. Let target world A have exactly two zero-cost protocols: `a1` realizes `T1` but not `T2`, while `a2` realizes `T2` but not `T1`. Assume a faithful protocol translation must assign each source protocol to one target protocol and preserve every task-realization relation carried by that source protocol.

Taskwise simulation succeeds: for `T1`, choose `p -> a1`; for `T2`, choose `p -> a2`. But no single global protocol map exists, because the unique source protocol `p` would have to map to one target protocol realizing both `T1` and `T2`, and A has none.

Thus

`forall T, exists translator f_T` does not imply `exists one translator f, forall T`.

Equivalently, independent taskwise feasibility is not sufficient for whole-envelope translation when protocol identity is shared across tasks.

## Boundary and prior-art warning

The logical skeleton is the elementary failure of exchanging universal and existential quantifiers, and it is closely related to constraint-satisfaction consistency/gluing obstructions. It is therefore **not** a GC-native breakthrough theorem by itself. In categorical language, analogous local-to-global compatibility questions are also classical.

## Use as a kill test

Any proposed GC translation metric or spectrum that aggregates independently optimized per-task translators without enforcing a jointly realizable global translator is incomplete for the stated notion of faithful whole-envelope translation.

A stronger candidate must quantify the cost or impossibility of **global translator compatibility** while surviving reductions to ordinary CSP consistency, sheaf/contextuality gluing, categorical naturality, and standard process simulation.

## Breakthrough decision

No breakthrough. This note narrows the search space and identifies the precise quantifier-order obstruction that future translation-spectrum candidates must not ignore.
