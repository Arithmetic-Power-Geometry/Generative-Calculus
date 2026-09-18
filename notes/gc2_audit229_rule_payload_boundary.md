# GC-II Audit 229 — Rule-payload boundary

## Result

Let `N` be a finite augmentation ground set and let `M` be any antichain in `2^N`. Start from a system whose target capability is identically unavailable. Add one admissible rule `L_M` whose semantics is

`L_M(S)=1 iff there exists E in M with E subseteq S`.

Then the post-augmentation capability has exactly `M` as its family of minimal enabling sets. Thus `Delta L_count = 1` can create an arbitrary monotone Boolean capability presentation.

## Theorem (unit-count impossibility)

In an unrestricted operational-closure formalism in which a rule may encode an arbitrary finite predicate, there is no finite universal upper bound on newly created minimal-enabler count, antichain width, relevant-variable count, or interaction degree as a function of rule count alone.

Proof: choose a growing ground set and encode the desired antichain in the semantics of a single added rule. For maximal-width examples use the middle layer `M_n={E subseteq [n]: |E|=floor(n/2)}`. Then `|M_n|=binom(n,floor(n/2))` while `Delta L_count=1` for every `n`. QED.

## Accounting consequence

A capability-accounting inequality of the form

`Omega_G <= F(Delta R, Delta I, Delta A, Delta L)`

is vacuous or false if the deltas are merely counts and one admissible transformation/rule can contain unbounded semantic payload. A defensible No-Free-Capability theorem therefore needs typed costs/capacities, e.g. description length, circuit size, oracle/query strength, implementation resource, or a restricted rule language. This is a necessary modeling condition, not sufficient novelty.

## Edge cases and checks

- Empty antichain gives no capability; no contradiction.
- `{emptyset}` gives unconditional capability; it shows even zero prerequisites need not mean zero rule payload.
- Monotonicity holds by construction.
- Renaming augmentation coordinates leaves the result invariant.
- Composition is not required: the obstruction occurs in one rule.
- The theorem does not assert Kolmogorov complexity is computable; it only shows raw rule count is insufficient.
- If the rule language has bounded description/circuit complexity, the counterexample may be excluded; quantitative bounds then become conditional on that restriction.

## Prior-art boundary

The antichain/minimal-true-set representation is standard monotone Boolean / Sperner-family structure. Minimal path sets in reliability theory provide the same existential-enabler pattern. Monotone co-design also represents minimal resource solutions by antichains. Accordingly, the counterexample is a boundary result for GC-II, not a novelty claim.

## Ledger

- Arbitrary minimal-enabler antichain from one unrestricted rule: **PROVED**.
- Rule-count-only No-Free-Capability bound: **FALSIFIED** without a payload restriction.
- Raw `Delta L` as a cardinal count measuring generative input: **FALSIFIED**.
- Need for semantic/implementation rule capacity in budgeted operational closure: **PROVED NECESSARY** for any nonvacuous count-based universal bound.
- A GC-specific canonical payload measure invariant under behaviorally equivalent encodings: **OPEN**.
- Quantitative bound using such a canonical payload measure: **OPEN**.

## Reproducibility

Run `python experiments/gc2_audit229_rule_payload_counterexample.py`. The verifier constructs middle-layer antichains for `n=2..12`, reconstructs their minimal true sets exactly, computes the Möbius degree, and confirms that at `n=12` a single rule carries 924 minimal enablers.
