# GC-II Directed Interface Gap Audit 007

## Scope and status

This note strengthens the finite shared-translator specialization only. It does **not** claim a new universal Generative Calculus invariant.

Status: **PROVED (restricted finite specialization)** for the algebra below; **IMPORTED/KNOWN collision risk** for the underlying support-size information quantity; **OPEN** for a genuinely GC-specific resource-accounted reversibility invariant.

## Definition

Let a finite task set `T` carry two task-indexed operational representations `X=(x_t)` and `Y=(y_t)`. Define

`m(X -> Y) = max_x |{ y_t : x_t = x }|`,

with `m(empty -> empty)=1`, and define the directed shared-interface gap

`d_I(X,Y) = log_2 m(X -> Y)`.

By the exact auxiliary-interface theorem in `GLOBAL_TRANSLATOR_AUDIT_006.md`, `m(X->Y)` is exactly the minimum auxiliary alphabet size required to make `Y` a deterministic function of `(X,a)` under one shared translator. The exact fixed-width binary requirement is `ceil(log_2 m)`.

## Theorem 1: zero-gap criterion

`d_I(X,Y)=0` iff `Y` is a deterministic function of `X` on the observed task family.

Proof: `d_I=0` iff `m=1`; this says every `X`-fibre contains at most one `Y` value, exactly the functional-consistency criterion. QED.

Important degeneracy: zero gap does **not** imply `X=Y`; it is a directed pseudodistance-like quantity and collapses deterministic recodings.

## Theorem 2: exact composition / triangle law

For three representations on the same task set,

`m(X -> Z) <= m(X -> Y) m(Y -> Z)`

and therefore

`d_I(X,Z) <= d_I(X,Y) + d_I(Y,Z)`.

Proof: fix an `X` fibre. It contains at most `m(X->Y)` distinct `Y` values. For each such `Y` value there are at most `m(Y->Z)` distinct `Z` values. Their union therefore has size at most the product. Maximize over `X`. Taking `log_2` gives the triangle law. QED.

Thus this restricted gap has identity (`d_I(X,X)=0`), nonnegativity, relabeling invariance, and directed triangle behavior. It is generally asymmetric.

## Reversibility candidate and collision

A tempting reversibility asymmetry is

`rho_I(X,Y) = d_I(X,Y) - d_I(Y,X)`

or the nonnegative magnitude `|rho_I|`.

This is **not promoted** as a GC-II invariant. The primitive `log max conditional support size` is closely related to conditional Hartley / order-zero information and zero-error distinguishability. The shared-interface theorem itself collides with confusability-graph / functional compression mechanisms. Hence relabeling this quantity as a new invariant would overclaim novelty.

The useful GC-II lesson is structural: any eventual reversibility gap must include operational resource budgets, admissible transformations, error tolerance, and/or one-global-translator constraints in a way not reducible to conditional support size.

## Exhaustive computational audit

`gc2/tests/test_gc2_directed_interface_gap.py` checks:

- empty and identity degeneracies;
- zero gap under non-identical deterministic recoding;
- explicit asymmetry;
- exact fixed-width bit requirement;
- relabeling invariance;
- all `16^3 = 4096` triples of length-four binary task representations for the multiplicative composition and logarithmic triangle laws.

The tests are designed to run in the branch CI. No empirical result is claimed until CI passes.

## Prior-art collision assessment

High collision risk. The quantity is a maximum conditional support-size measure, while exact distinguishability by side information is classical territory in zero-error information theory, graph coloring/graph entropy, functional compression, and deterministic simulation. Accordingly:

- algebraic properties above: **PROVED**;
- exact shared-interface interpretation: **PROVED in our restricted model**;
- mathematical novelty of the primitive quantity: **NOT CLAIMED / IMPORTED-KNOWN neighborhood**;
- GC-II reversibility-gap breakthrough: **OPEN**.

## Next attack

Replace static task symbols by lifted operational traces carrying vector resource expenditure and admissibility gates `(I,A,L)`. Seek a two-way minimal augmentation pair whose asymmetry survives quotienting by deterministic recodings and cannot be represented by conditional support size alone. Test composition under explicit resource accounting; a failure of triangle behavior without a composition-cost assumption should be recorded rather than repaired by definition.
