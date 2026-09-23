# GC-II Audit 340 — Grounding-multiplicity no-go for cardinality-only capability accounting

## Scope

This audit attacks the open bridge left by Audits 335–339. GC-I remains unchanged. The question is whether finite quotient size plus cardinality-style charged deltas can control raw Generative Novelty Gap when a newly admitted action/rule schema is parameterized over an interface domain.

## Setup

Let `Q_q={0,...,q-1}`, `q>=2`, with baseline reachability equal to identity. Count a newly admitted parameterized action schema once at schema level. Thus two extensions may have the same `(Delta R,Delta I,DeltaA,DeltaL)` cardinalities while differing in how many grounded state pairs the schema denotes.

Define raw saturated pair novelty

`Omega_pair = |{(x,y): x!=y and y is reachable from x after the extension}|`.

## Theorem 340.1 — grounding multiplicity is not controlled by schema cardinality

For every `q>=2`, there exist two extensions on the same quotient `Q_q` with the same schema-cardinality charge

`(Delta R,Delta I,DeltaA,DeltaL)=(0,0,1,1)`

but with

`Omega_pair(E_local)=1`

and

`Omega_pair(E_ground)=q(q-1)`.

Hence the ratio of raw novelty between extensions with identical `q` and identical cardinality-style four-coordinate charge is `q(q-1)`, which is unbounded as `q` grows.

### Construction and proof

`E_local` admits one action schema whose operational grounding contains only `0 -> 1`. Its transitive closure adds exactly that one nonidentity ordered pair.

`E_ground` admits one parameterized action schema `jump(target)` available at every source and with `target` ranging over `Q_q`; operationally its grounding contains every ordered pair `x -> y`, `x!=y`. Its closure therefore adds all `q(q-1)` nonidentity ordered pairs.

Both extensions add one schema and one rule family under schema-cardinality accounting, with no separately charged resource or information increment in this abstract construction. Yet their generated operational relations differ by the stated factor. QED.

## Corollary 340.2 — what the four-delta bridge must measure

A universal informative bound cannot be derived from `q` plus mere counts of newly admitted action/rule *schemas*. A bridge must additionally constrain at least one semantic quantity that controls grounding, for example:

- admissibility-domain size;
- parameter-domain cardinality;
- number of distinct grounded macro-transitions induced after baseline closure;
- an equivalent semantic/interface measure that upper-bounds these.

This is stronger than Audit 335's reuse-depth counterexample: even after `q` is supplied explicitly and finite-horizon saturation is handled by Audits 338–339, schema cardinality alone still fails to determine operational amplification.

## Important boundary

This theorem does **not** say that no function of `(q,DeltaR,DeltaI,DeltaA,DeltaL)` can upper-bound novelty at all: the trivial bound `q(q-1)` always does. It says that cardinality-style deltas provide no nontrivial discrimination between the two constructed extensions. Nor does it rule out a four-coordinate theory whose coordinates are semantic capacities rather than counts. Indeed, the result specifies a requirement for such a theory: `DeltaA` or `DeltaL` must charge grounding/domain capacity if it is expected to control raw novelty.

## Verification

`experiments/gc2_audit340_grounding_multiplicity_no_go.py` constructs both families, computes exact transitive closure, and checks `q=2,...,64`. There are 63 paired cases and zero failures. At `q=64`, the identical schema-count charge permits novelty 1 versus 4032.

## Edge/invariance/composition audit

- `q=2`: local novelty is 1 and full grounding novelty is 2; separation already exists.
- Identity/self transitions are excluded from novelty because they are baseline-reachable.
- Relabelling states preserves both novelty counts.
- Duplicating syntax without changing the grounded relation changes neither result.
- Closure cannot enlarge the complete grounding beyond `q(q-1)`.
- The local construction has no hidden compositional amplification: its only nonidentity edge is `0->1`.
- The theorem concerns schema-cardinality accounting. If every grounded transition is separately charged, the counterexample no longer has equal charge; that is precisely the semantic distinction exposed here.

## Prior-art boundary

Parameterized actions and their ground instances are standard in planning, transition systems, logic/program semantics, databases, CSPs and model checking; succinct representations can denote large explicit transition structures. The mechanism is therefore **IMPORTED/KNOWN**. No novelty is claimed for grounding explosion itself. The GC-II result is the accounting no-go: a capability law that charges only schema counts cannot infer operational novelty from those counts, even when quotient size is known.

Collision classes: reachability/viability (direct), complexity/succinct representations (direct mechanism), CSP/database grounding (direct mechanism), resource theories/simulation preorders (convertibility interpretation), information theory/thermodynamics/Blackwell-Le Cam/majorization/GPTs/contextuality (no theorem novelty asserted from them).

## Status

- Grounding-multiplicity separation: **PROVED**.
- Nontrivial discrimination by `q` plus schema-cardinality four-deltas alone: **FALSIFIED**.
- Grounding/succinct-representation mechanism: **IMPORTED/KNOWN**.
- Semantic-capacity reinterpretation of `DeltaA`/`DeltaL`: **OPEN**.
- Tight representation-stable bridge from charged deltas to the Audit-339 novelty spectrum: **OPEN**.

## Scientific consequence

The Paper-II accounting program now has a sharper design constraint. The four coordinates can survive only if at least the action/interface/rule coordinates are defined semantically enough to charge the operational domain they unlock. Raw counts of schemas are insufficient. A promising next target is therefore a representation-stable `DeltaA_eff` based on newly enabled grounded macro-transition support (or a compressed capacity measure with a proved support bound), followed by a non-tautological inequality linking that capacity to the novelty-distance spectrum.