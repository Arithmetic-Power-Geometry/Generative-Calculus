# GC-II Audit 108 — Higher-order structure beyond path/transition-monoid semantics

Status date: 2026-09-13
Branch scope: `gc2-capability-accounting-lab` only. GC-I/main is frozen.

## Question

Audit 107 left open whether a quotient-invariant higher-order capability quantity, not reconstructible from complete one-dimensional path/transition-monoid semantics, could supply the GC-II breakthrough.

## Candidate

Let a system admit actions/events `a,b` and suppose the ordinary interleaving transition semantics contains both words `ab` and `ba`. A tempting higher-order witness is whether these two executions are merely two sequential paths or are faces of one genuine concurrent 2-cell. More generally, one can attach higher cells witnessing compatible simultaneous/independent execution and define a capability witness from the resulting cubical/precubical structure.

This genuinely contains information that an ordinary transition monoid need not contain: the 1-skeleton records paths and compositions, while a 2-cell records a relation between executions (true concurrency/independence). Thus the direction survives Audit 107's narrow path-monoid reconstruction test.

## Exact separation lemma

**Lemma (1-skeleton insufficiency).** There exist two finite higher-dimensional operational structures with identical labelled 1-skeletons, hence identical ordinary finite paths and transition-monoid action on vertices, but different higher-dimensional structure.

**Construction.** Take four vertices `00,10,01,11` with labelled edges

- `00 -a-> 10`, `01 -a-> 11`,
- `00 -b-> 01`, `10 -b-> 11`.

System X contains only this square boundary. System Y contains the same boundary plus a 2-cell whose four faces are those edges. Their labelled transition graphs are identical, so all graph paths and the induced transformations of vertices agree. But Y explicitly represents `a` and `b` as one concurrent square whereas X does not.

Status: **PROVED** (finite explicit construction).

## Collision / no-go

This separation is not a GC-II breakthrough. Higher-dimensional automata (HDAs), precubical sets, event structures, pomsets, true-concurrency semantics, history-preserving/hereditary-history-preserving bisimulation, and directed topology were developed precisely to retain concurrency/independence information discarded by interleaving transition systems. Current 2026 HDA work continues to characterize ST and hereditary history-preserving semantics using interval ipomsets and higher-dimensional structure.

Therefore:

> **Higher-dimensional escape no-go.** Showing that a capability invariant is not reconstructible from an ordinary transition monoid is insufficient for novelty whenever the missing datum is concurrency, independence, higher cells, partial-order execution, or homotopy of executions; these are already first-class semantics in established true-concurrency/HDA/process theory.

This does **not** prove that every possible higher-order GC invariant is known. It establishes a required collision gate: any candidate must be compared against at least event structures/pomsets, HDA/precubical semantics, ST/hhp bisimulation, and directed-topological execution invariants before being labelled novel.

## Consequence for Omega_G

A candidate such as

`Omega_G = (# higher cells gained)`

fails immediately as a quotient-invariant capability measure: subdivision/refinement or presentation choices can alter raw cell counts without necessarily altering observable true-concurrency behaviour. Likewise, defining Omega_G as 'information missing from the 1-skeleton' merely measures a chosen representational truncation.

A defensible Omega_G must therefore be invariant under an independently justified behavioural equivalence and must imply a quantitative operational consequence (task feasibility, minimal boundary resource, unavoidable translator cost, etc.) not already implied by standard true-concurrency semantics.

## Stronger surviving target

The next target is **not** 'higher order than paths'. It is:

1. choose a fixed operational equivalence at least as discriminating as the relevant true-concurrency/history-preserving semantics;
2. define Omega_G on equivalence classes, not presentations;
3. derive Omega_G independently from budgeted closure rather than from a missing-data residual;
4. prove a quantitative capability-accounting inequality or convertibility obstruction;
5. exhibit a finite witness pair that standard reachability, Blackwell/deficiency, resource monotones, ordinary transition monoids, and established true-concurrency/HDA invariants do not already decide;
6. adversarially search for counterexamples and reductions before making a novelty claim.

## Status ledger

- Identical transition monoid / different higher-dimensional concurrency structure: **PROVED**.
- Higher-dimensional structure can carry information absent from ordinary path semantics: **PROVED / IMPORTED-KNOWN mechanism**.
- Raw higher-cell count as quotient-invariant capability: **FALSIFIED**.
- 'Beyond transition monoid' alone as GC-II novelty criterion: **FALSIFIED**.
- True-concurrency/higher-dimensional semantics as standalone GC-II breakthrough: **FALSIFIED / IMPORTED-KNOWN**.
- Quantitative Omega_G surviving true-concurrency behavioural quotient and prior-art collision: **OPEN**.

## Prior-art gate used in this audit

Representative established/current directions checked: higher-dimensional automata; precubical/presheaf semantics; interval pomsets; ST traces; history-preserving and hereditary history-preserving bisimulation; directed execution spaces/topology. The literature collision is structural, not merely terminological.

## Kill rule added

Do not promote a GC-II candidate merely because ordinary labelled transition/path semantics cannot reconstruct it. First lift the comparator to the strongest relevant established semantics (true concurrency, contextual/sheaf, distributed, probabilistic, resource, or higher-dimensional as appropriate). Novelty can only be assessed after that lift.
