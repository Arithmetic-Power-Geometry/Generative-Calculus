# GC-II Audit 350 — Budgeted Closure-Escape Equivalence and Scalar Complete Threshold

## Status

- Exact equivalence between budgeted operational closure escape, a feasible witness, min-plus distance, and layered-state reachability: **PROVED / IMPORTED-KNOWN mechanisms**.
- For one ordered capability pair under additive nonnegative grounded-operation costs, the minimum enabling budget `B*` is a complete scalar threshold for every budget query: **PROVED**.
- Exponential enumeration of minimal witnesses/cuts is unnecessary for deciding a single budget query on an explicit finite graph: **PROVED / IMPORTED-KNOWN algorithmic consequence**.
- Claim that these classical shortest-path equivalences alone constitute foundation-level novelty: **NOT CLAIMED**.

## Setup

Start from the finite baseline-contracted operational graph of Audits 348–349. Vertices are operational equivalence classes after all zero-charge baseline motion has been contracted/closed. Each newly admissible grounded operation `e=(u,v)` has acquisition charge `c(e) >= 0`. For an ordered pair `(s,t)`, `s != t`, and budget `b >= 0`, define the budgeted operational closure

`Cl_b(s) = {v : there exists an s-v operational walk whose total new-operation charge is <= b}`.

The Generative Novelty Gap for the pair at budget `b` is the indicator

`Omega_G(s,t;b) = 1[t in Cl_b(s) and (s,t) not in B]`.

For a globally novel pair in the contracted graph, this is simply `1[t in Cl_b(s)]`.

Define

`B*(s,t) = inf { total charge(P) : P is an operational s-t path }`,

with `B*=+infinity` when no path exists.

## Theorem — Budgeted Closure-Escape Equivalence

For every finite explicit operational graph with nonnegative edge charges and every `s != t`, the following are equivalent:

1. **Operational:** `t in Cl_b(s)`.
2. **Witness:** there exists an admissible finite `s-t` witness whose total charge is at most `b`.
3. **Geometric:** the weighted directed distance satisfies `d_c(s,t) <= b`.
4. **Computational:** the min-plus shortest-path value satisfies `B*(s,t) <= b`.
5. **Layered reachability (integer charges):** in the resource-expanded graph with states `(v,r)`, `0 <= r <= b`, and transition `(u,r)->(v,r+c(e))` whenever `r+c(e)<=b`, some `(t,r)` is reachable from `(s,0)`.

Consequently,

`Omega_G(s,t;b) = 1[B*(s,t) <= b]`

for a baseline-novel pair.

### Proof

(1) and (2) are identical after expanding the definition of budgeted closure. Any finite walk with nonnegative costs can have directed cycles deleted without increasing total charge, so a successful witness has a simple-path representative. The minimum charge over those representatives is exactly the weighted directed distance, giving (2) iff (3). The min-plus path recurrence computes that same minimum, giving (3) iff (4). For integer charges, augmenting each vertex by accumulated resource converts cost accumulation into ordinary reachability, giving (2) iff (5).

No equivalence uses cardinality of syntactic rule schemas; all charges live on grounded operational transitions after quotienting duplicate syntax.

## Corollary 1 — one scalar is complete for a one-budget/one-pair question

For fixed `(s,t)` and fixed charge semantics, the entire family of budget decisions is determined by one extended-real number:

`available_b(s,t) iff b >= B*(s,t)`.

Thus Audit 349's complete cut family is structurally informative but not required as an explicitly enumerated decision representation for this restricted model. `B*` is a complete scalar threshold for all `b`.

This does **not** imply a universal scalar complete monotone for multi-pair convertibility, vector resources, nonadditive budgets, contextual admissibility, information-dependent actions, or stochastic transformations.

## Corollary 2 — exact No-Free-Capability criterion

For a baseline-novel reachable pair,

`B*(s,t) > 0`

iff every admissible `s-t` witness has strictly positive total charge.

Therefore a No-Free-Capability theorem is valid exactly under a semantic charging condition excluding zero-total-cost escape witnesses. Merely counting new schemas, actions, rules, or interfaces cannot establish it (Audits 335 and 340).

## Corollary 3 — closure escape has a polynomial decision oracle in the explicit additive model

With nonnegative explicit edge charges, one budget query can be decided by a shortest-path algorithm without enumerating the potentially exponential minimal-witness or minimal-cut clutters. For integer budgets the layered construction is also exact, though pseudo-polynomial in the numeric budget if materialized directly.

This is a complexity separation between **representation of every minimal explanation/obstruction** and **decision of one capability threshold**. It is not a claim that shortest paths are new.

## Edge, dimensional, monotonicity, and composition audit

- `c(e)` and `b` must share the same resource unit; `B*` has that unit. `Omega_G` is dimensionless.
- `b=0`: escape occurs exactly when a zero-total-charge witness exists.
- Unreachable pair: `B*=+infinity`, so no finite budget enables it.
- `s=t`: excluded from novelty because the empty path is baseline available.
- Zero-cost cycles do not invalidate the theorem; cycle deletion preserves or lowers cost.
- Relabelling vertices/operations preserves `B*` when charges are transported.
- Duplicating syntax for the same grounded transition changes nothing after operational quotienting.
- Increasing budget cannot remove capability: `Cl_b(s) subseteq Cl_b'(s)` for `b<=b'`.
- Increasing any edge charge cannot decrease `B*`; adding an admissible edge cannot increase `B*`.
- Disjoint mandatory serial modules add thresholds. Alternative parallel modules take the minimum. Shared/nonadditive resources need not obey either law.

## Exact finite verification

`experiments/gc2_audit350_budgeted_closure_escape.py` exhausts every directed three-state graph where each of the six possible non-self edges is either absent or has integer charge 1, 2, or 3. For every ordered source-target pair and every budget 0 through 6 it compares direct subset-enabling semantics against the min-plus threshold.

Result: 4,096 weighted graph configurations; 172,032 exact pair-budget cases; **zero failures**. Machine-readable output is in `results/gc2_audit350_budgeted_closure_escape.json`.

## Prior-art collision check

Weighted shortest paths, Bellman/min-plus recurrences, state-space/resource expansion, and reachability are classical **IMPORTED/KNOWN** mechanisms. Resource theories and simulation/reachability frameworks likewise already use convertibility preorders. This audit therefore makes no novelty claim for those ingredients.

The GC-II value is architectural: it isolates a maximal tractable submodel in which Closure-Escape, No-Free-Capability, and complete finite budget convertibility collapse to one exact threshold, thereby identifying precisely where Paper-II novelty must live: semantic construction of the operational quotient/charges, multi-resource or nonadditive coupling, contextual/information-dependent admissibility, interaction across multiple capability targets, or lower bounds showing that those richer structures cannot be compressed to this scalar model.

## Next target

Attempt a separation theorem: construct the smallest exact pair of systems with identical scalar thresholds `B*(s,t)` for all individual target pairs but different joint/multi-target generative capability under shared resources, information, or action coupling. If successful, this would prove where scalar shortest-path accounting ceases to be complete and motivate a genuinely GC-II multi-capability invariant rather than repackaging classical path theory.
