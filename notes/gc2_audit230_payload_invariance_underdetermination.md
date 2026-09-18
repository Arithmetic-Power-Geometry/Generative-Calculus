# GC-II Audit 230 — Behavioral invariance does not determine payload

## Result

Audit 229 showed that raw object counts cannot measure generative input when one rule/action/interface may hide arbitrarily large semantic payload. A tempting repair is to demand a payload measure that is invariant under behaviorally equivalent encodings. This audit shows that invariance alone is far too weak.

Let `X` be a set of operational presentations and let `~` be behavioral equivalence. Write `Q=X/~` and `q:X->Q` for the quotient map. A scalar payload `P:X->R` is behaviorally invariant iff `x~y => P(x)=P(y)`.

### Quotient-factorization theorem

`P` is behaviorally invariant iff there exists a function `h:Q->R` such that

`P = h o q`.

Proof. If `P` is invariant, define `h([x])=P(x)`; invariance makes this well-defined and gives `P=h o q`. Conversely every composition `h o q` is constant on equivalence classes. QED.

### Consequence

Behavioral invariance by itself imposes no ordering, scale, additivity, monotonicity, coding interpretation, or operational meaning on payload: all such choices are hidden in the arbitrary function `h`. If `Q` contains at least two classes, two invariant payloads can reverse their ordering. If `Q` is finite, any permutation of assigned payload values produces another equally invariant measure.

Therefore the phrase "canonical behaviorally invariant payload" cannot be justified by quotient invariance alone. Additional axioms are mathematically necessary before a capability-accounting bound can use such a quantity non-vacuously.

## What additional structure might be defensible?

Candidate restrictions must be stated explicitly and collision-tested:

1. a fixed operational description language and minimum description length;
2. a fixed circuit/gate model and minimum implementation size;
3. a task-relative information or communication cost;
4. an operational simulation preorder plus normalized monotones;
5. an explicit reference distribution/measure over behavioral classes.

Each changes the theorem class. None follows merely from behavioral equivalence.

## Complexity boundary

A universal shortest-description route leads directly toward Kolmogorov complexity: it is invariant across universal description systems only up to an additive machine-dependent constant and is not computable. A finite Boolean-circuit route leads toward the Minimum Circuit Size Problem (MCSP), an established meta-complexity problem. Thus these are imported candidate accounting technologies, not GC-II novelty by themselves.

## Edge cases and checks

- One behavioral class: every invariant payload is constant; it carries no discriminative accounting information.
- Two or more classes: invariant measures can disagree arbitrarily on class ordering.
- Renaming or duplicating presentations within one class leaves every quotient-factorized measure unchanged.
- Composition is not addressed by invariance; it must be imposed as a separate axiom (subadditivity, additivity, monotonicity, etc.).
- Dimensional consistency is not supplied by invariance; the codomain and units must be fixed independently.
- The theorem does not claim that no useful canonical measure can exist. It proves only that behavioral invariance cannot select one without extra structure.

## Ledger

- Quotient-factorization characterization of behavioral invariance: **PROVED / elementary known mathematics**.
- Behavioral invariance alone determines a canonical payload: **FALSIFIED**.
- Behavioral invariance alone determines payload ordering or scale: **FALSIFIED**.
- Universal shortest-description complexity as a GC-specific construction: **IMPORTED/KNOWN**.
- Exact computable universal shortest-description payload: **FALSIFIED in the Kolmogorov-complexity route**.
- Fixed-model minimum circuit payload: **IMPORTED/KNOWN / computationally nontrivial**.
- GC-specific payload axioms derived from GC-I projection structure: **OPEN**.
- No-Free-Capability theorem after explicit payload axioms: **OPEN**.

## Reproducibility

Run `python experiments/gc2_audit230_payload_invariance.py`. The finite verifier constructs quotient classes with duplicate presentations, checks factorization, and exhibits invariant payload assignments with reversed class orderings.