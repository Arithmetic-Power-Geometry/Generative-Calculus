# GC-II Endpoint Reversibility Insufficiency Audit 019

## Status

- Endpoint-only reversibility classifier based only on `(Omega_G(X->Y), Omega_G(Y->X))`: **FALSIFIED as complete in the finite labelled-state specialization**.
- Existence of a finite witness with identical endpoint costs but different post-cycle future capability: **PROVED by construction**.
- Trace-sensitive residual-capability quantity as a universal invariant: **OPEN**.
- Novelty of the mechanism: **IMPORTED/KNOWN neighborhood**; no breakthrough claim.

## Question

Can reversibility of a GC-II conversion be determined completely from the two directed endpoint costs alone?

Consider any proposed classifier

`H(Omega_G(X->Y), Omega_G(Y->X))`.

If two operational worlds have the same ordered endpoint-cost pair but one restores future capability after the round trip and the other does not, then no such `H` can be complete across that class of worlds.

## Finite deterministic witness

States carry observable endpoint labels. The forward action is `f`, the reverse action is `r`, and both cost one unit.

### World R: capability-restoring cycle

- `x0` has label `X`.
- `y` has label `Y`.
- `g` has label `G`.
- `x0 --f/1--> y`.
- `y --r/1--> x0`.
- `x0 --probe/0--> g`.

Hence the forward and reverse endpoint costs are

`Omega_end(X->Y)=1`, `Omega_end(Y->X)=1`.

After `f;r`, the system returns to `x0`. Its one-step future reachable-label signature is unchanged.

### World D: capability-degrading cycle

- `x0` has label `X`.
- `y` has label `Y`.
- `x1` also has label `X`.
- `g` has label `G`.
- `x0 --f/1--> y`.
- `y --r/1--> x1`.
- `x0 --probe/0--> g`.
- `x1` has no transition to a `G`-labelled state.

The endpoint costs are again

`Omega_end(X->Y)=1`, `Omega_end(Y->X)=1`.

The endpoint label after the cycle is still `X`; therefore endpoint-label accounting reports the same round trip as in World R. But the one-step future signature changes from `{X,Y,G}` at `x0` to `{X}` at `x1`.

Thus the worlds collide on the full endpoint-only input pair while differing on future capability restoration.

## Proposition: endpoint-pair incompleteness

Let a model class contain the two finite worlds above. No function

`H : (R_+ union {infinity})^2 -> C`

whose arguments are only the directed endpoint conversion costs can be a complete classifier of round-trip restoration of future capability on that class.

### Proof

The two worlds have identical input pair `(1,1)`. Any function of that pair alone must return the same value on both worlds. Yet World R restores the bounded future-capability signature after `f;r`, while World D does not. Therefore the classifier cannot distinguish restoration from degradation. QED.

## Edge and degeneracy checks

1. **Same endpoint label is preserved.** The degrading witness does not win by changing the externally named endpoint: both `x0` and `x1` carry label `X`.
2. **Equal forward/reverse costs are not enough.** Both worlds have exactly `(1,1)`.
3. **Depth zero is intentionally blind.** At future depth zero, both pre-cycle and post-cycle signatures are `{X}` in World D. A reversibility test must therefore specify what future operational behavior it promises to preserve.
4. **No negative-cost artifact.** The implementation rejects negative edge costs.
5. **No triangle-inequality assumption is used.** The witness is independent of the previously falsified metric route for nonlinear Omega_G.
6. **The result is representation-relative.** If endpoint identity is refined so that `x0` and `x1` are distinct targets and Omega_G is defined over those fully resolved states, the collision may disappear. The theorem therefore targets coarse endpoint-only accounting, not an omniscient state representation.

## Consequence for GC-II

A defensible reversibility object must preserve enough operational information to distinguish states that share endpoint labels and directional costs but differ in future capability. The minimum requirement is a specified future-behavior equivalence or pseudometric. A candidate trace-sensitive residual is

`Gamma_trace(X,Y) = inf_{sigma:X=>Y, tau:Y=>X} D_future(X, tau o sigma(X))`,

where `D_future` is zero only when the chosen whole-envelope future behavior is equivalent. This remains **OPEN** until the behavior class, depth/budget treatment, composition law, invariance properties, and computability are fixed.

## Prior-art collision boundary

The mechanism is adjacent to classical state minimization / future equivalence, bisimulation, hidden-state observability, hysteresis, and coarse-grained irreversibility. Consequently, the finite witness is a boundary/falsification result, not a novelty claim. GC-II would need a stronger theorem in which the residual distortion is tied essentially to coupled R/I/A/L transformations, task-scale-error-vector-budget envelopes, or a new quantitative lower/upper bound not reducible to ordinary state equivalence.

## Reproducible artifacts

- `gc2/trace_reversibility.py`
- `gc2/tests/test_gc2_trace_reversibility.py`

The regression test checks the exact `(1,1)` endpoint collision, restoration in World R, loss of future `G` capability in World D, depth-zero degeneracy, endpoint-label preservation, and the nonnegative-cost guard.
