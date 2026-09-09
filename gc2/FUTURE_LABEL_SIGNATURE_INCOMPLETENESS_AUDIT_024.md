# GC-II Audit 024 — Reachable-label signatures are incomplete

## Status
**PROVED finite counterexample / DECISIVE FALSIFICATION of the current signature as a whole-envelope invariant.**

## Claim tested
The helper `future_label_signature(q,h)`, which records only the set of endpoint labels reachable within horizon `h`, was being used as a bounded proxy for future capability in the reversibility experiments. The question is whether equality of these signatures is sufficient for equality of operational future capability.

## Counterexample
Let two states `x0,x1` have the same visible label `X`, and let `g` have label `G`.

- from `x0`, action `a` is enabled and reaches `g`;
- from `x1`, action `b` is enabled and reaches `g`;
- there are no other outgoing transitions.

For every horizon `h >= 1`,

`future_label_signature(x0,h) = future_label_signature(x1,h) = {X,G}`.

At horizon zero both signatures are `{X}`. Thus the reachable-label signatures agree at **every** horizon.

Nevertheless the operational interfaces differ: `a` is feasible at `x0` and infeasible at `x1`, while `b` is feasible at `x1` and infeasible at `x0`. For the prescribed task "execute action a and reach G", `x0` succeeds and `x1` fails. Hence equality of all reachable-label signatures does not imply equality of future operational capability.

## Consequence
A reversibility residual based only on reachable endpoint-label sets can return zero for a genuinely capability-changing round trip. Therefore it must not be described as a whole-envelope reversibility invariant.

Any defensible GC-II future signature must preserve at least the relevant labelled transition/interface structure and, for the intended theory, task, scale, error, vector-budget, information, action/interface, rule and cost semantics. Candidate exact finite notions include trace-language equivalence with costs/budgets or an appropriate labelled/budgeted bisimulation; these mechanisms have mature prior art and are not themselves a novelty claim.

## Edge cases
1. If actions are intentionally quotiented away and capability means only existential endpoint reachability, the old signature may be adequate for that deliberately weaker semantics.
2. Increasing the horizon does not repair the witness: equality holds for all horizons.
3. Adding endpoint costs to the signature still does not repair action identity unless the action-labelled traces themselves are represented.
4. This falsification does not invalidate the earlier endpoint-cost insufficiency witness; it shows that its current diagnostic is weaker than the intended whole-envelope notion.

## Paper-II implication
The next reversibility object must compare future **operational behaviours**, not merely reachable labels. Before claiming a quantitative cycle-distortion theorem, GC-II must specify the observational semantics under which two future behaviours are considered equivalent.
