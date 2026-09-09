# GC-II Audit 025 — Trace Completeness Fails Under Branching Choice

## Status

- **PROVED (restricted finite model):** equality of complete action/cost trace sets does not imply equality of robust future capability under nondeterministic branching.
- **IMPORTED/KNOWN mechanism:** the separating phenomenon is the classical distinction between linear-time trace semantics and branching-time semantics/process equivalences.
- **FALSIFIED as a complete GC-II route:** any whole-envelope invariant based only on the set of realized action/cost traces, even at unbounded horizon, is insufficient in the presence of nondeterministic or adversarial choice.
- **OPEN:** a GC-specific budgeted branching capability equivalence/distortion whose observations include task-scale-error-budget feasibility plus R/I/A/L state changes, and whose quantitative laws are not reducible to standard bisimulation/simulation or energy-game machinery.

## Minimal exact witness

Let `p` delay its choice:

    p --a--> p1
    p1 --b--> T
    p1 --c--> T

Let `q` commit during `a`:

    q --a--> qb --b--> T
     \-a--> qc --c--> T

Every edge has cost 0. From both starts the complete action/cost trace language is exactly

    {epsilon, a, ab, ac}.

Therefore every signature retaining only complete action/cost traces agrees, not merely to a chosen finite horizon but for the full finite behavior.

However, after executing `a`, robust capability differs. Define

    Guaranteed(s,a) = intersection_{t in Succ(s,a)} Enabled(t).

Then

    Guaranteed(p,a) = {b,c},
    Guaranteed(q,a) = emptyset.

Thus an environment/controller that must retain the option to choose either `b` or `c` *after observing completion of a* succeeds from `p` and cannot guarantee success from `q`.

## Proposition — trace-set incompleteness

There exist finite nondeterministic labelled transition systems x,y such that

    Tr_cost(x) = Tr_cost(y)

but

    Cap_robust(x) != Cap_robust(y).

### Proof

Use the witness above. The trace languages are both exactly `{epsilon,a,ab,ac}` with the same edge costs. Yet after the common prefix `a`, `p` has a single successor enabling both `b` and `c`, while `q` has two possible successors, one enabling only `b` and the other only `c`. Hence the intersection of enabled actions over all post-`a` resolutions is `{b,c}` for `p` and empty for `q`. Therefore the robust future capabilities differ despite complete trace equality. QED.

## Checks

### Domains and dimensions

The witness uses finite states, a finite action alphabet, and scalar nonnegative edge cost. Scalar cost is a one-dimensional specialization of a GC vector-resource annotation, so failure in this restriction is enough to refute universal completeness of trace-only signatures.

### Edge cases

- Horizon 0: both starts expose only the empty trace.
- Horizon 1: both expose `{epsilon,a}`.
- Horizon >=2: both expose the complete set `{epsilon,a,ab,ac}`; equality therefore persists at arbitrarily large horizons.
- Adding identical vector costs to corresponding `a,b,c` edges preserves the collision.
- Adding endpoint labels does not repair the collision if corresponding terminal/intermediate states receive equal coarse labels.

### Monotonicity

Increasing trace horizon cannot separate the states because both terminate after depth 2 and their complete trace sets are already identical.

### Composition behavior

The difference is specifically compositional/branching: the point at which choice is resolved affects what a later controller can still select, even though the flattened set of complete traces is unchanged.

## Prior-art collision

The mechanism is classical. The linear-time/branching-time spectrum distinguishes trace equivalence from stronger ready/failure/simulation/bisimulation notions precisely because flattened traces forget branching structure. Weighted/quantitative transition-system literature also studies bisimulation with costs/weights. Energy games and simulation games already couple transitions with multidimensional resource levels. Therefore neither the witness nor the generic remedy "use branching semantics" is claimed as GC-II novelty.

Relevant prior-art families checked in this audit:

- labelled-transition trace/ready/failure/bisimulation semantics;
- weighted labelled transition systems and quantitative bisimulation;
- simulation preorders;
- multidimensional energy/resource games.

## Consequence for Paper II

The GC-II whole-envelope state cannot be summarized by any object of the form

    set{(action trace, accumulated cost/resource annotation)}

when future capability includes robust controllability after intermediate observations. A viable object must preserve branching conditional structure: what actions/interfaces/rules remain available *after each possible history and resolution*, under residual budgets and information state.

A safe next formal target is therefore a budget-indexed branching relation on augmented states `(s,B,I,A,L)` with task-scale-error observations. But simply defining bisimulation/simulation on that enlarged state space would be imported machinery. A publishable GC-II result must prove a genuinely new accounting law, separation, or complexity consequence that essentially uses the coupled R/I/A/L whole-envelope structure.

## Reproducibility

Executable witness: `gc2/branching_capability.py`.
Regression tests: `gc2/tests/test_gc2_branching_capability.py`.

No empirical or novelty claim is made beyond the exact finite falsification stated above.
