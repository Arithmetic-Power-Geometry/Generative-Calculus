# GC-II Audit 171 — Compositional Witness-Evaluation No-Go

Status date: 2026-09-16
Branch scope: `gc2-capability-accounting-lab` only. GC-I/main unchanged.

## Objective

Attack Audit 170's surviving gate: determine whether a witness evaluator that respects alternative choice and sequential composition can define a genuinely new GC-II capability invariant, or whether those axioms force ordinary semiring/path-algebra semantics.

## Formal setup

Let `E` be the set of primitive admissible transformation labels. Let `E*` be finite words (sequential witnesses), with empty word `epsilon`. Let `N<E>` denote the free noncommutative semiring of finite formal sums of words with natural-number coefficients. Operationally:

- a word `e1...ek` is one sequential capability-generation witness;
- `P + Q` denotes alternative derivations/witnesses;
- `P Q` denotes sequential concatenation/distributive composition;
- `0` denotes no witness;
- `1` denotes the empty witness.

If witness identity/order is intentionally quotiented, replace `N<E>` by the corresponding quotient semiring. The theorem below then applies to the quotient exactly when the evaluator respects the quotient relations.

## Representation theorem — exact scope

Let `K=(K,oplus,otimes,0_K,1_K)` be any semiring. Suppose an evaluator

`V : N<E> -> K`

satisfies, for all formal witness expressions `P,Q`,

1. `V(0)=0_K`;
2. `V(1)=1_K`;
3. `V(P+Q)=V(P) oplus V(Q)`;
4. `V(PQ)=V(P) otimes V(Q)`.

Then `V` is a semiring homomorphism. Moreover it is uniquely determined by the primitive edge values `v(e)=V(e)`.

Conversely, every assignment `v:E->K` extends uniquely to such an evaluator on the free noncommutative semiring.

### Proof

The four displayed laws are exactly preservation of the semiring constants and operations, hence `V` is a semiring homomorphism. For uniqueness, every word is a finite product of generators and every formal witness expression is a finite sum of such words; repeated use of (3)-(4) determines its image from the generator images. Existence is given explicitly by mapping a word `e1...ek` to `v(e1) otimes ... otimes v(ek)` (empty word to `1_K`) and a formal sum to the corresponding `oplus`-sum, with multiplicity. The semiring laws guarantee well-defined evaluation.

**Status: PROVED, but mathematically IMPORTED/KNOWN as the universal property of a free semiring/free algebra.**

## Strong no-go consequence

Any proposed GC-II witness score whose semantics consists only of:

- assigning values to primitive admissible transformations;
- combining alternatives by one associative additive operation;
- combining sequential witnesses by one associative multiplicative operation;
- obeying distributivity and the standard identities;

is not a new algebraic species of capability accounting. It is a semiring/path-algebra evaluation. Choosing tropical/min-plus, Boolean, counting, probability-like, symbolic/provenance, matrix, language, or other semiring targets changes the interpretation, not this structural fact.

Therefore the candidate statement

`new compositional witness score => new generative invariant`

is **FALSIFIED** under these axioms.

## Quantale extension

If alternatives form arbitrary joins rather than only finite sums, and sequential composition preserves those joins in each argument, the same structure is a quantale/quantaloid-style path semantics rather than an escape from established algebra. Thus replacing finite alternatives by complete joins does not rescue novelty.

**Status: IMPORTED/KNOWN structural extension.**

## Important boundary: what the theorem does NOT cover

The theorem does not say every operational capability observable is a semiring homomorphism. It identifies the exact escape conditions. A candidate can leave the theorem's scope only by violating at least one structural assumption, for example:

- context-dependent composition: the value of `PQ` is not determined by `V(P),V(Q)` alone;
- non-distributive interaction between alternatives and sequence;
- history-dependent enabling in which witness composition requires hidden state not represented in the algebra;
- concurrency/synchronization requiring a genuinely different composition operator or higher-dimensional object;
- global constraints over sets of witnesses (competition, shared bottlenecks, exclusion, correlated failure) that are not homomorphic under ordinary alternative/sequence operations;
- endogenous creation of new primitive operations/observables, so the generator set itself changes under execution.

However, Audit 162 applies immediately: if the apparently hidden context/history can be compiled into an exact sufficient augmented state while retaining ordinary path composition, then the apparent escape collapses back to standard path semantics on the enlarged state space. Therefore a credible GC-II residual must survive sufficient-state compilation as well as this semiring no-go.

## Exact independence/counterexample checks

The assumptions are substantive rather than cosmetic.

### Drop multiplicative preservation

Let `K=N` and define `V(P)` as the number of distinct primitive labels appearing anywhere in `P`. Then generally `V(PQ)` is not determined by `V(P),V(Q)` because overlap matters. Example: `P=a`, `Q=a` gives diversity 1, while `P=a`, `Q=b` gives diversity 2 although the two input scalar values are `(1,1)` in both cases. Thus no binary scalar `otimes` on these values can represent composition. This escapes the theorem, but it is merely information loss: retaining the set of labels as the value restores compositionality by set union.

### Drop distributivity/context independence

A score that penalizes reuse of a resource across a whole witness can make the score of a concatenation depend on which resource identities occurred in each factor, not merely their scalar scores. Again, enriching the value with sufficient provenance/resource state can restore a standard compositional algebra. This is not yet novelty.

### Quotient caution

If parallel transformations are operationally indistinguishable, the free algebra must first be quotiented by that equivalence. An evaluator that distinguishes identified generators is not well-defined on the operational quotient and fails Audit 164 operational invariance.

## Relation to Paper-II targets

1. Budgeted operational closure remains the base operational object.
2. A scalar `Omega_G` obtained solely as a compositional path evaluation is structurally non-novel.
3. Closure-Escape cannot be established merely by selecting a new semiring score.
4. No-Free-Capability bounds inherited from such scores remain instances of ordinary path/resource monotonicity unless an additional theorem couples them nontrivially.
5. Nonlinear `F(Delta R,Delta I,Delta A,Delta L)` does not escape when its future-relevant state is compilable (Audit 162).
6. Complete finite convertibility via unrestricted monotones remains Audit 167/order-theoretic.
7. Local-to-global translator lower bounds remain a separate possible route.
8. Reversibility-gap candidates based only on forward/backward semiring path costs remain directed-distance/path-algebra constructions.
9. Finite counterexample search should now target observables that fail scalar compositionality but cannot be repaired by finite sufficient-state/provenance enrichment without a provable complexity blow-up.
10. Applications should be postponed until such a residual survives the theorem/prior-art gates.

## Prior-art collision boundary

The core theorem is deliberately not claimed as new. Free semirings/free algebras have the universal property that generator assignments extend uniquely to homomorphisms. Weighted automata/path algebra already multiply transition weights along paths and add over alternative paths. Provenance semirings explicitly use addition for alternative derivations and multiplication for joint/sequential dependency structure; polynomial provenance is universal for broad commutative settings. Complete-join versions are quantale/quantaloid territory.

Hence this audit is a **decisive falsification of a novelty route**, not a breakthrough claim.

## Status ledger

| Candidate | Status | Reason |
|---|---|---|
| Finite alternative/sequence representation theorem | PROVED / IMPORTED-KNOWN | free-semiring universal property |
| Unique extension from primitive transformation values | PROVED / IMPORTED-KNOWN | universal property |
| Arbitrary-join extension | IMPORTED/KNOWN | quantale/quantaloid structure |
| New semiring-valued witness score as GC-II breakthrough | FALSIFIED | structural relabeling |
| Scalar diversity/context score as escape | FALSIFIED as sufficient evidence | loss repaired by richer value in simple examples |
| Non-compilable contextual witness interaction | OPEN | must defeat sufficient-state augmentation and prior art |
| Complexity of minimal sufficient compositional enrichment | OPEN | promising only if quantitative lower bound is new |
| GC-I local-to-global translator lower bound linked to enrichment size | OPEN | strongest next bridge candidate |

## Next exact attack

Define the **minimal sufficient compositional enrichment size** `C_G(n)` for a family of projected GC-I worlds: the least number of states/bits in any operationally admissible enrichment that makes the target witness evaluator compositional and exact. Seek a family for which `C_G(n)` grows exponentially (or its bit complexity linearly) under a fixed local projection/interface, and derive the lower bound from GC-I proper-projection irreducibility rather than from a generic arbitrary communication problem. Then collision-test the resulting theorem against Myhill-Nerode/state complexity, communication complexity, branching programs/OBDDs, automata minimization, CSP/database width, distributed synthesis, and sufficient-statistic lower bounds. If it reduces directly to one of those, mark it IMPORTED/KNOWN rather than novel.