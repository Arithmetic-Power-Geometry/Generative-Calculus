# GC-II Audit 166 — Unrestricted Reduction/No-Go Classification Completeness Fails

Status date: 2026-09-16
Branch scope: `gc2-capability-accounting-lab` only. GC-I/main unchanged.

## Question

Can the accumulated Audits 153–165 be promoted to a theorem saying that every effective capability-accounting construction necessarily reduces to one of a fixed list of known families (reachability/repair, resource/simulation conversion, communication/synthesis, active identification, or non-identifiability)?

## Result

**FALSIFIED in unrestricted form.**

Let `B(M)` denote complete operational behavior under the chosen admissible contexts, and let `Q(M)` be an effective capability quantity.

Audit 164 gives the exact observational dichotomy:

1. If `B(M)=B(N)` but `Q(M) != Q(N)`, then `Q` is not identifiable from `B`.
2. If `B(M)=B(N) => Q(M)=Q(N)`, then there exists a factor `q` on behavioral equivalence classes such that

   `Q = q o B`.

This factorization does **not** imply that `q` belongs to any fixed finite catalog of semantic mechanisms. Even for a finite behavior encoding `b`, one may define an arbitrary effective invariant `q(b)` (for example, any computable predicate or integer-valued function of the canonical behavior code). Such a quantity is operationally identifiable by construction, yet membership in reachability, conversion, communication/synthesis, or active-identification form does not follow without additional restrictions on the syntax, algebra, compositionality, admissible queries, or reduction notion.

Therefore the implication

`effective + operationally identifiable => reducible to one of K named families`

is invalid absent a representation theorem for the permitted class of quantities.

## Proof sketch

Take a canonical effective encoding `enc(B(M))` of finite operational behavior. Let `f : {0,1}* -> N` be any total computable function and define

`Q_f(M) = f(enc(B(M)))`.

Then `Q_f` is constant on behavioral-equivalence classes and hence operationally identifiable. But identifiability alone supplies only the factorization through the quotient; it supplies no structural property forcing `f` into a fixed semantic subclass. A proposed finite-family completeness theorem must therefore either (i) define a family broad enough to contain every computable quotient function, becoming vacuous, or (ii) impose substantive structural axioms and prove a representation theorem from those axioms.

This is the same conceptual warning that appears in full-abstraction theory: fixing observational equivalences makes fully abstract maps extremely easy to obtain, so full abstraction/factorization by itself carries limited structural content. The GC-II classification program must not confuse quotient factorization with a mechanism classification.

## Edge cases and checks

- Constant `Q`: identifiable; trivially factors through behavior; does not identify a unique mechanism.
- Injective behavior encoding: every effective `Q` on models is behavior-identifiable, again defeating mechanism inference from identifiability alone.
- Non-injective behavior encoding: realization-dependent `Q` can be non-identifiable, reproducing Audit 164.
- Finite model class: the argument is strongest, because every table-valued function on behavioral classes is computable.
- Infinite effective class: the counterargument still applies to arbitrary total computable functions of canonical behavior codes where such codes exist.
- Composition: adding a compositionality axiom narrows the class, but does not by itself establish the proposed five-family completeness; a separate representation theorem is required.
- Monotonicity: likewise narrows the class but still permits many monotone functions on a preorder.

## Prior-art collision boundary

The core quotient/factorization mechanism is **IMPORTED/KNOWN** from observational equivalence and full abstraction. In particular, full abstraction studies preservation/reflection of observational equivalence, and prior work explicitly warns that with fixed equivalences fully abstract functions almost always exist. Thus GC-II should not claim the bare factorization principle as novel.

## Ledger

| Candidate | Status | Reason |
|---|---|---|
| Operational identifiability dichotomy | PROVED / IMPORTED mechanism | Audit 164 factorization |
| Every identifiable effective `Q` reduces to five named mechanisms | FALSIFIED | arbitrary effective quotient functions |
| Fixed finite catalog completeness without structural axioms | FALSIFIED | quotient factorization has unrestricted codomain functions |
| Classification after explicit structural axioms | OPEN | requires a non-vacuous representation theorem |
| Axiomatic capability-accounting representation theorem | OPEN | strongest surviving positive direction |

## Consequence for Paper II

Do **not** claim a universal five-family Reduction/No-Go Classification Theorem. The scientifically defensible next step is narrower and potentially stronger: specify axioms that a genuine capability-accounting functional should satisfy (operational invariance, budget monotonicity, normalization, composition law/inequality, refinement behavior, and possibly continuity/effectivity), then determine whether those axioms force a representation or dual form. Only a representation theorem with nontrivial uniqueness/separation content could turn the audit sequence into a positive GC-II theorem rather than a taxonomy.

## Next gate

Search for the weakest non-vacuous axiom set under which a capability functional admits a representation by operational closure witnesses or dual monotones. Stress-test independence of each axiom with finite countermodels before attempting novelty claims. Compare directly with ordered commutative monoids/resource theories, utility/measurement representation theorems, Lawvere metrics, simulation metrics, and convex duality.
