# GC-II Audit 356 — capability quotient and exact translator state lower bound

## Status

**PROVED / IMPORTED-KNOWN MINIMIZATION MECHANISM / OPERATIONAL LOWER-BOUND BRIDGE.**

GC-I on `main` is unchanged. This audit follows Audit 355 and asks whether exact state augmentation can be irreducibly large even when the source description is factored and compact.

## Capability equivalence

For an operational state `z`, let `Fut(z)` denote its complete future capability behavior: the set of all finite action/observation continuations together with the target-capability outcomes they induce. Define

`z ~cap z'  iff  Fut(z) = Fut(z')`.

An exact deterministic capability translator is any state abstraction `tau: Z -> S` from which all future capability answers are recoverable under every continuation. Exactness requires

`tau(z)=tau(z')  =>  z ~cap z'`.

Hence every translator state lies inside one capability-equivalence class.

## Theorem — Capability-Quotient Lower Bound

Let `Ncap = |Z / ~cap|`. Every exact deterministic capability translator has at least `Ncap` states:

`|S| >= Ncap`.

### Proof

Choose one representative from each `~cap` class. If an exact translator mapped two representatives from different classes to the same translator state, exactness would force them to have identical future capability behavior, contradicting their inequivalence. Thus the translator is injective on class representatives. QED.

This is the operational form of the classical distinguishability/minimal-state argument; the mechanism is not claimed as new automata theory.

## Exponential factored family

For each `n >= 1`, consider `n` independent binary latches `b_1,...,b_n`. The source state is the factored vector

`b in {0,1}^n`.

Provide `n` query actions `q_i`. From state `b`, action `q_i` reaches success iff `b_i=1`; otherwise it reaches failure. (Equivalently, capability `C_i` is available iff `b_i=1`.) All `2^n` bit vectors are reachable by ordinary set/reset actions, each described locally per latch.

For distinct vectors `b != b'`, choose coordinate `i` with `b_i != b'_i`. Query `q_i` yields different capability outcomes. Therefore

`b !~cap b'`.

Hence

`Ncap = 2^n`

and every exact deterministic capability translator must have

`|S| >= 2^n`.

The source is factored using `n` binary variables plus `O(n)` local set/reset/query rules, while any *explicit-state* exact translator has exponentially many distinguishable states.

## What this proves — and what it does not

It proves a representation-independent lower bound on the **number of states of any exact deterministic finite-state translator** preserving all future capability answers. It does **not** prove that the capability relation lacks a compact symbolic/intensional representation: the bit vector itself is an `n`-bit symbolic representation. Therefore this is a state-count lower bound, not a bit-complexity, circuit-size, formula-size, or program-description lower bound.

That distinction blocks an invalid stronger claim. Exponentially many semantic states can still be encoded in `n` bits.

## Relation to Audit 355

Audit 355 proved that finite endogenous admissibility compiles to ordinary reachability but left the compilation cost open. Audit 356 gives an exact lower bound for explicit exact translators:

`minimum translator states = at least number of future-capability equivalence classes`.

The latch family realizes `2^n` classes from an `O(n)` factored operational description. Thus finite compilation is semantically possible but can require exponential explicit state expansion.

## Edge / domain / composition audit

- `n=0`: one empty context; lower bound is one state.
- `n=1`: two contexts separated by `q_1`.
- Unreachable contexts: excluded if the quotient is taken over reachable states; the construction makes all bit vectors reachable.
- Relabelling bits or query names preserves the quotient cardinality.
- Adding capabilities cannot merge two states already separated by an existing query, although changing the observation/target semantics can alter the quotient.
- Sequential composition is already included because `Fut(z)` quantifies over all finite continuations.
- Nondeterministic systems require a chosen capability semantics (may/must/probabilistic); the theorem remains valid once `Fut` is defined accordingly, but this audit's sharp family is deterministic.

## Prior-art collision

The lower-bound mechanism is classical Myhill–Nerode / automaton minimization: states with different future suffix behavior are distinguishable and cannot be merged in an exact deterministic automaton. Therefore the quotient theorem is classified **IMPORTED/KNOWN MECHANISM**. The GC-II value is to connect Audit 355's augmented operational state directly to future-capability distinguishability and to delimit exactly what kind of irreducibility remains after finite compilation.

Public anchor inspected 2026-09-24:

- Cornell CS 4120, DFA minimization / Myhill–Nerode: reachable states with different accepted suffix sets must remain distinct in a minimal DFA: https://www.cs.cornell.edu/courses/cs4120/2026sp/notes/leximpl/

## Classification

- Capability-equivalence quotient: **PROVED** as defined.
- Exact deterministic translator state lower bound `|S| >= |Z/~cap|`: **PROVED / IMPORTED-KNOWN mechanism**.
- `O(n)` factored latch family with `2^n` pairwise capability-distinguishable contexts: **PROVED**.
- Polynomial explicit-state exact compilation for all compact factored systems: **FALSIFIED**.
- Exponential bit/circuit/formula/program-size lower bound: **NOT PROVED; OPEN**.
- Claim that Audit 356 alone is a foundational novelty beyond automata/state minimization: **FALSIFIED by prior-art collision**.

## Paper-II consequence

This strengthens GC-I projection irreducibility operationally only at the explicit-state level. A genuinely stronger Paper-II theorem must constrain the translator representation class and prove a lower bound on symbolic description/circuit/communication/query complexity, or exploit a GC-specific compositional requirement that classical Myhill–Nerode minimization does not already settle.
