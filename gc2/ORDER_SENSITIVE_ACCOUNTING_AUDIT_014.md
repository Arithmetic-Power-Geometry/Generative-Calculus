# GC-II Audit 014 — Order-sensitive capability accounting

## Status

**DECISIVE FALSIFICATION** of a universal capability-accounting law that depends only on aggregate increments `(Delta R, Delta I, Delta A, Delta L)` when admissible transformations are state dependent or noncommuting.

This is a boundary theorem, not a novelty claim. State-dependent action availability, planning with preconditions, affordances, and noncommuting transition systems are mature neighboring mechanisms.

## Setup

Let an operational world have states `s0, sI, sA, goal, dead`. Two augmentation transformations are available:

- `i` (information acquisition): from `s0` it moves to `sI`; from `sA` it moves to `goal`.
- `a` (interface/action acquisition): from `s0` it moves to `sA`; from `sI` it moves to `dead`.

Both sequences `ia` and `ai` consume exactly the same aggregate augmentation vector

`Delta = (Delta R, Delta I, Delta A, Delta L) = (0,1,1,0)`.

Yet

- `a` followed by `i`: `s0 -> sA -> goal`, so the target is reachable;
- `i` followed by `a`: `s0 -> sI -> dead`, so the target is not reached.

Thus equal aggregate increments do not determine capability.

## Proposition 1 — aggregate-vector insufficiency

Let `Phi_sigma` denote the operational state obtained by applying an admissible augmentation word `sigma`, and let `Delta(sigma)` be its aggregate R/I/A/L increment vector. If there exist words `sigma,tau` with

`Delta(sigma)=Delta(tau)` but `Cap(Phi_sigma) != Cap(Phi_tau)`,

then no function `G(Delta R,Delta I,Delta A,Delta L)` can exactly characterize capability for that class of worlds.

### Proof

If such a `G` existed, equality of aggregate vectors would imply

`G(Delta(sigma))=G(Delta(tau))`.

Exact characterization would then force equal capability, contradicting the assumed witness. QED.

The five-state construction above is an explicit witness.

## Corollary — scalar/vector F cannot be universal

A bound of the form

`Omega_G <= F(Delta R,Delta I,Delta A,Delta L)`

remains a valid *upper bound for a specified sufficient augmentation plan* when already proved under its hypotheses. But `F` of aggregate deltas alone cannot in general be an exact capability law, nor can it decide whether an arbitrary ordering of those deltas realizes the target.

A general GC-II accounting object therefore needs at least one of:

1. an ordered augmentation trace/path;
2. a state-dependent transformation operator;
3. a sufficient statistic that quotients traces only when they are operationally equivalent.

## Proposition 2 — when aggregate accounting is restored

Suppose augmentation transformations act on operational states and satisfy, on the reachable domain:

1. **commutation:** `T_e T_f = T_f T_e` for every pair of augmentation primitives;
2. **path-independent cost/accounting:** the accumulated augmentation descriptor depends only on the multiset/count vector of primitives;
3. **capability extensionality:** capability depends only on the resulting operational state.

Then any two augmentation words with the same primitive-count vector induce the same final state and hence the same capability.

### Proof

Any two finite words with the same multiplicities differ by a finite sequence of adjacent swaps. Pairwise commutation preserves the resulting state under every adjacent swap. Therefore the two words have identical final states. Capability extensionality gives identical capability. QED.

This identifies a precise boundary: aggregate R/I/A/L accounting is justified only after proving an appropriate commutation/path-independence condition or an equivalent quotient theorem.

## Composition and edge-case audit

- Empty word: well defined; zero aggregate augmentation.
- One primitive: no order issue.
- Commuting primitives: order obstruction disappears.
- Noncommuting primitives: aggregate equality need not imply state or capability equality.
- Degenerate equal-capability endpoints: noncommuting states may still be capability-equivalent; the obstruction requires a capability-separating witness.
- Monotonicity in aggregate deltas is not sufficient: two paths with the same delta can differ before any monotonic comparison is available.
- Nonlinear interaction terms in `F` do not repair lost order information if `F` receives only the aggregate vector.

## Relation to the GC-II program

This result changes step (5). The strongest defensible target is no longer a universal static formula of four aggregate deltas. It is an **ordered/path-dependent capability-accounting functional**

`Omega_G <= F[sigma; Delta R,Delta I,Delta A,Delta L]`

or a quotient of augmentation traces by an operational equivalence relation. A static `F(Delta)` can then appear as a theorem for commuting/path-independent subclasses.

It also sharpens the prospective breakthrough direction: quantify the irreducible value of augmentation order, or characterize exactly when order can be quotiented away, while checking collision with planning, trace monoids/partial-order reduction, resource theories, and noncommutative dynamics.

## Prior-art collision note

The mechanism itself is **IMPORTED/KNOWN neighborhood**. Classical planning uses state-dependent action preconditions; affordance models make action availability state dependent; partial-order reduction explicitly distinguishes independent/commuting from dependent transitions. Therefore no novelty is claimed for noncommutativity itself.

Potential GC-II novelty, if any, must come from a capability-accounting theorem coupling ordered R/I/A/L transformations to whole-envelope translation/reconstruction, not from the observation that action order can matter.
