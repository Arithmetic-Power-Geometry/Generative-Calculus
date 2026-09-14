# GC-II Audit 135 — Task-indexed higher-order escape collapses under tagging

## Target
Test the surviving Audit-134 route: whether making admissibility/free transformations task-indexed is, by itself, an operational structure beyond a fixed resource theory/preorder.

## Setup
Let `T` be a task set and `X` an operational state space. For each task `t`, let `F_t` be the admissible transformation family on `X` (identity-containing and composition-closed when a preorder is desired). Define native task-indexed convertibility

`(t,x) >=_native (t,y)` iff there exists `f in F_t` with `f(x)=y`.

Construct the tagged state space `Z=T x X`. Lift each task-specific transformation to a partial/tag-preserving transformation

`f~_t(t,x)=(t,f(x))`.

(Outside the matching tag it may be left undefined, or completed by identity; either convention preserves the same within-tag reachability.)

## Theorem — Task-Index Compilation
For fixed task tags,

`(t,x) >=_native (t,y)` iff `(t,x) >=_tagged (t,y)`.

### Proof
Forward: a native witness `f in F_t` lifts to `f~_t`, which maps `(t,x)` to `(t,y)`.

Reverse: every tag-preserving lifted witness acting at tag `t` is induced by some `f in F_t`; projecting its second component gives `f(x)=y`.

Thus task indexing alone changes representation, not the convertibility relation. If task changes themselves are operational actions, include the task/mode variable in the state and their transition rule in the enlarged transformation system; the same compilation applies provided the continuation-relevant mode is explicit.

## Exact finite regression
`experiments/audit135_task_tag_compilation.py` enumerates all deterministic maps on a two-state space, all identity-containing composition-closed transformation monoids (6 total), all 36 ordered pairs assigned to two task tags, both source states, and both tasks. It performs 144 native-vs-tagged reachability comparisons. Expected exact result: 0 mismatches.

## Prior-art collision gate
This construction is an augmented-state/tagging reduction. It does not evade process resource theories: dynamical resource theories already treat channels as resource objects and superchannels as transformations; multi-time process resource theories use superprocesses and explicitly make utility depend on an agent's available controls. Therefore task-indexing or moving one categorical level upward is not sufficient novelty.

Relevant collision classes: dynamic/process resource theories, superchannels/superprocesses, simulation/testing preorders, contextual equivalence, augmented-state compilation.

## Status
- Task-Index Compilation theorem: **PROVED**.
- Two-task/two-state exhaustive regression: **NUMERICALLY SUPPORTED (exact exhaustive finite class)**.
- Task indexing alone as a route beyond fixed resource theory: **FALSIFIED**.
- Process/superprocess resource machinery: **IMPORTED/KNOWN**.
- Surviving GC-II gate: **OPEN** — any higher-order candidate must contain a measurable obstruction that is not removable by finite/history-state augmentation or ordinary process-resource conversion.

## Scientific consequence
Do not claim novelty from `task-dependent free sets`, `task-dependent admissibility`, `channels as resources`, or `transformations of transformations` alone. The next candidate must survive an explicit compilation test: attempt to encode every continuation-relevant task/rule/history variable into state and compare the resulting reachability/convertibility structure exactly.
