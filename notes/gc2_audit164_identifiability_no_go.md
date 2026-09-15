# GC-II Audit 164 — Operational Identifiability No-Go

Status date: 2026-09-15

## Scope

GC-I on `main` remains frozen. This audit asks whether the sequence of GC-II metric failures can be turned into a positive theorem about which capability-accounting quantities are identifiable from operational behavior.

## Setup

Let `M` be a class of operational systems and let

`B : M -> O`

be the complete observation/behavior map available to an auditor. Define observational equivalence

`M ~_B N  iff  B(M)=B(N)`.

A proposed capability-accounting quantity is a map

`Q : M -> Y`.

Call `Q` *operationally identifiable from B* when there exists `q : im(B) -> Y` such that

`Q = q o B`.

Equivalently, Q is constant on every observational fiber of B.

## Theorem 164.1 — Operational Identifiability / Factorization

The following are equivalent:

1. Q is operationally identifiable from B.
2. For every M,N, `B(M)=B(N)` implies `Q(M)=Q(N)`.
3. Q factors uniquely through the quotient/image of B: there is a unique `q : im(B) -> Y` with `Q=q o B`.

### Proof

(1)->(2): if Q=q o B and B(M)=B(N), then Q(M)=q(B(M))=q(B(N))=Q(N).

(2)->(3): for o in im(B), choose any M with B(M)=o and define q(o)=Q(M). Condition (2) makes this independent of representative. Then Q=q o B. Uniqueness follows because every o in im(B) has a preimage.

(3)->(1): immediate.

Status: **PROVED**.

## Corollary 164.2 — No Behavioral Estimator Can Recover a Fiber-Varying Quantity

If there exist M,N with B(M)=B(N) but Q(M) != Q(N), then no estimator, algorithm, learned predictor, monotone family, or exact statistic whose input is only B(M) can recover Q on all systems.

Proof: identical input B(M)=B(N) forces the same output, contradicting the two required Q values.

Status: **PROVED**.

This is stronger than saying a particular formula fails: it rules out *every* behavior-only recovery method for that Q under the chosen observation semantics.

## Corollary 164.3 — Minimal Observable Enrichment Criterion

Let E : M -> Z be an added observable and write B_E(M)=(B(M),E(M)). Then Q becomes identifiable after enrichment iff

`B(M)=B(N) and E(M)=E(N)  =>  Q(M)=Q(N)`.

Thus an enrichment is sufficient exactly when it separates every Q-discordant pair remaining inside a B-fiber.

For finite M this yields an exact combinatorial problem: within each B-fiber, form the partition induced by Q. Any sufficient E must refine the fiber at least to that Q-partition.

Status: **PROVED**.

## Quantitative finite lower bound

For a finite B-fiber F define

`k_Q(F) = | { Q(M) : M in F } |`.

Any deterministic enrichment alphabet capable of making Q identifiable on F must have at least k_Q(F) distinguishable values on F. Therefore its worst-fiber information capacity obeys

`log2 |range(E)| >= max_F log2 k_Q(F)`

when a single finite alphabet is used globally.

The bound is tight as a pure identification bound by taking E to encode the Q-class inside each B-fiber. This does **not** claim that such an E is physically/admissibly obtainable; operational acquisition constraints are a separate problem.

Status: **PROVED (finite deterministic setting)**.

## Stress tests / edge cases

- If B is injective, every Q is identifiable. Correct.
- If Q is constant, zero enrichment is required. Correct.
- If B is constant, Q is identifiable iff Q is constant. Correct.
- Relabeling M or O by bijections does not change the factorization criterion. **Invariant**.
- Composition: if Q factors through B and B factors through a richer observation C, Q also factors through C. **Monotone under observational enrichment**.
- Coarsening observations can destroy identifiability; it cannot create identification of a previously fiber-varying Q unless the domain/quantity also changes. **Checked by factorization**.
- The theorem is domain/codomain agnostic; no dimensional inconsistency occurs because it asserts equality/factorization, not addition of heterogeneous R/I/A/L units.

## Relation to GC-II candidate Omega_G

This theorem creates a hard gate:

> A purported intrinsic Generative Novelty Gap inferred solely from an operational semantics B is scientifically meaningful as an operational invariant only if Omega_G is constant on B-equivalence classes.

Therefore any proposed Omega_G that depends on hidden realization details discarded by B is non-identifiable without explicitly enriching the observable interface. Conversely, merely quotienting away those details can make Omega_G identifiable but may collapse it to a known behavioral/resource/simulation quantity.

This explains the repeated Audit 153–163 dichotomy: preserve enough structure and many candidate costs become ordinary operational costs; quotient the structure away and realization-dependent candidates become unidentifiable.

## Novelty boundary

The factorization theorem itself is **IMPORTED/KNOWN in mathematical substance**: it is the elementary quotient/factorization criterion behind observational equivalence and identifiability. Full-abstraction theory likewise studies coincidence/preservation/reflection of observational and semantic equivalence. Statistical identifiability likewise treats observationally equivalent parameter points through quotient classes.

Therefore **do not claim Theorem 164.1 alone as a new mathematical breakthrough**.

Potential GC-II-specific residual, still OPEN:

1. Define a *budget-indexed family* of behavior maps B_b generated by explicit R/I/A/L operational closure.
2. Characterize the least admissible enrichment needed to make a capability quantity identifiable simultaneously across budgets and compositions.
3. Require the enrichment itself to be obtainable through admissible transformations, not an oracle label for Q.
4. Seek a separation between pure information lower bound `log k_Q(F)` and *operational acquisition cost* under the R/I/A/L rules.
5. Test whether that separation reduces to experiment design, active identification, Blackwell/Le Cam deficiency, communication complexity, or constrained sensing/control.

Until those collision checks survive, status remains **OPEN**, not breakthrough.

## Ledger

- Operational identifiability iff fiber constancy iff factorization: **PROVED / mechanism IMPORTED-KNOWN**.
- Behavior-only recovery of a fiber-varying quantity: **FALSIFIED universally**.
- Finite enrichment cardinality lower bound: **PROVED / counting mechanism IMPORTED-KNOWN**.
- Oracle Q-class enrichment as physical acquisition model: **FALSIFIED as an assumption**; it is only a mathematical tightness witness.
- Budget-indexed admissible-identification residual: **OPEN**.
- New Omega_G from this audit: **OPEN; none validated yet**.
