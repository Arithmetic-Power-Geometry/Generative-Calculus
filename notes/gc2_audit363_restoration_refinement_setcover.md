# GC-II Audit 363 — Minimum restoration-relevant refinement collapses to set cover

Status: **PROVED reduction; IMPORTED/KNOWN optimization mechanism; proposed unrestricted refinement route FALSIFIED as foundational novelty.**

## Setup

Let `W` be a finite set of latent operational worlds and `A` a finite set of restoration actions. For each world `w`, let nonempty `R(w) ⊆ A` be the actions that correctly restore the required capability context in that world.

An observation/refinement `o: W -> Y` is restoration-sufficient when there exists a deterministic decision rule `pi: Y -> A` such that `pi(o(w)) ∈ R(w)` for every `w`.

For each action `a`, define its restoration domain

`D_a = { w in W : a in R(w) }`.

Let `tau` be the minimum number of domains `D_a` whose union is `W`.

## Theorem 363.1 — Exact minimum-refinement theorem

The minimum possible number of observation labels among all unrestricted deterministic restoration-sufficient refinements is exactly

`N*_obs = tau`.

Consequently, if labels are encoded by fixed-length binary messages, the minimum worst-case message length is

`b*_obs = ceil(log2 tau)`.

### Proof

**Upper bound.** Let actions `a_1,...,a_tau` cover `W`. Assign each world to one covering action and output that action's index as its observation label. The corresponding decision rule selects that action. Every world is restored correctly, so `N*_obs <= tau`.

**Lower bound.** Let a sufficient refinement use `m` labels. Each label `y` has one selected action `pi(y)`. Its entire fiber `o^{-1}(y)` must therefore lie inside `D_{pi(y)}`. The at most `m` actions selected across labels cover all worlds. Hence `tau <= m`, so `N*_obs >= tau`.

Combining the bounds gives `N*_obs = tau`. QED.

## Corollary 363.2 — Full latent-world identification can be arbitrarily wasteful

If one action restores every world, then `tau=1` and no world discrimination is needed, even when `|W|` is arbitrarily large. At the opposite extreme, if each world has a private restoration action, then `tau=|W|` and complete discrimination is necessary.

Thus the relevant quantity is not latent-state entropy/cardinality by itself; it is the action-cover structure induced by the restoration decision.

## Corollary 363.3 — Unrestricted minimum refinement inherits set-cover hardness

Given a set-cover instance with universe `W` and subsets `D_a`, define `R(w)={a : w in D_a}`. Then an observation refinement with at most `k` labels exists iff the set-cover instance has a cover of size at most `k`.

Therefore the unrestricted finite minimum-refinement problem is exactly a set-cover problem under this encoding. This is a classical optimization mechanism, not a GC-II novelty claim.

## Why this matters for Paper II

Audit 362 left open the possibility that the *minimum restoration-decision-relevant observation refinement* might itself provide the missing GC-II invariant. Audit 363 closes that unrestricted route: once arbitrary refinements are allowed and restoration is a one-step deterministic action choice, the exact optimum is simply the minimum action-domain cover.

A genuinely stronger GC-II target must impose structure that cannot be optimized away by arbitrary relabeling, for example:

1. a restricted admissible observation/generator language inherited from GC-I projections;
2. sequential observation costs with state-changing measurements;
3. resource/information/action/rule budgets coupled to the observation process;
4. local projections whose jointly required global decision information cannot be represented by an arbitrary oracle refinement.

The next target should therefore be a **restricted-generator restoration theorem**: characterize or lower-bound the cost of forming a restoration-sufficient partition using only admissible GC-I projections/compositions, then collision-test the result against decision-tree complexity, communication complexity, active diagnosis, CSP/database decomposition, and Blackwell/Le Cam sufficiency.

## Edge and sanity checks

- `|W|=0`: conventionally `tau=0`; the bit formula is not used. Operational instances should normally require nonempty `W`.
- Nonempty `W` with some `R(w)=∅`: restoration is impossible; `tau=∞` and no sufficient refinement exists.
- Duplicate actions with identical domains do not change `tau`.
- Adding a valid restoration action to some `R(w)` cannot increase `tau`.
- Adding worlds can increase or preserve `tau`, never decrease it when old restoration relations are fixed.
- Relabeling worlds or actions preserves `tau`.
- Composition is not assumed additive: independent product tasks may share actions, so cover numbers need not multiply or add without extra hypotheses.

## Novelty discipline

The theorem is useful as a **boundary/falsification result** for GC-II, not as a novelty claim. Minimum set cover and decision-sufficient information compression are established areas. Any Paper-II claim must live in the additional GC-specific restrictions, not in Theorem 363.1 alone.
