# GC-II Audit 364 — Restricted observation families reduce to conflict-pair cover

## Scope

This audit attacks the surviving target after Audit 363: observation/refinement is no longer an arbitrary oracle partition. A finite family of admissible observations (tests/generators/projections) is fixed in advance.

The result is a **boundary/falsification**, not a novelty claim.

## Setup

Let `W` be a finite set of latent operational worlds and `A` a finite action set. Each world `w` has a nonempty set `R(w) ⊆ A` of restoration actions that are correct in that world.

Let `Q` be a finite family of admissible deterministic observations. Each `q ∈ Q` is a map

`q : W -> Y_q`.

For a chosen nonadaptive observation suite `S ⊆ Q`, worlds `u,v` are observationally equivalent when

`q(u)=q(v)` for every `q ∈ S`.

The suite is restoration-sufficient iff every resulting observation cell has at least one common valid restoration action.

Define the **conflict family**

`C = { {u,v} : R(u) ∩ R(v) = ∅ }`.

For each admissible observation `q`, define its separated-conflict set

`D_q = { {u,v} ∈ C : q(u) != q(v) }`.

## Exact theorem

### Conflict-Pair Cover Theorem

A nonadaptive suite `S ⊆ Q` is restoration-sufficient iff

`⋃_{q∈S} D_q = C`.

Hence the minimum number of admissible observations required for restoration is exactly the minimum set-cover number of universe `C` by the sets `{D_q : q∈Q}` (and the weighted version is exactly weighted set cover when observations have additive acquisition costs).

### Proof

**Necessity.** Suppose a conflict pair `{u,v} ∈ C` is not separated by any selected observation. Then `u` and `v` lie in the same joint-observation cell. Since `R(u)∩R(v)=∅`, that cell has no action valid for both worlds, contradicting restoration sufficiency.

**Sufficiency.** Suppose every conflict pair is separated. Consider any joint-observation cell `B`. If `⋂_{w∈B} R(w)=∅`, it does **not** in general follow that some pair in `B` has disjoint action sets (Helly failure for arbitrary subsets). Therefore the pairwise formulation above is sufficient only under an additional 2-Helly condition on the restoration-action family.

This exposes an important correction: the naive conflict-pair theorem is false for general set-valued restoration actions.

Counterexample:

`R(w1)={a,b}`, `R(w2)={b,c}`, `R(w3)={a,c}`.

Every pair intersects, so `C=∅`, yet the three-way intersection is empty. With no observations, pair-cover would declare success although no common restoration action exists.

## Correct exact formulation

Define the family of **minimal bad world sets**

`B = { B ⊆ W : ⋂_{w∈B}R(w)=∅ and every proper B'⊊B has ⋂_{w∈B'}R(w) != ∅ }`.

For a selected suite `S`, a bad set `B` is destroyed iff at least one selected observation is nonconstant on `B`.

For each observation define

`H_q = { B ∈ B : q is nonconstant on B }`.

Then

`S is restoration-sufficient  <=>  ⋃_{q∈S} H_q = B`.

### Proof

If some minimal bad set `B` remains constant under every selected observation, all members of `B` occupy one joint-observation cell, whose action intersection is empty; the suite fails.

Conversely, if a joint-observation cell has empty action intersection, finiteness gives an inclusion-minimal subset `B` of that cell with empty intersection. Every selected observation is constant on that cell and therefore on `B`, contradicting coverage of all minimal bad sets.

Thus minimum nonadaptive restricted observation is exactly set cover on the hypergraph of minimal restoration obstructions.

## Special cases

1. **Single-valued required action.** Minimal bad sets are conflicting pairs; the result reduces to Test Cover / pair separation.
2. **2-Helly restoration families.** Again only conflict pairs need be covered.
3. **One universally valid action.** `B` is empty and zero observations suffice.
4. **No admissible observation separates some minimal bad set.** Restoration is impossible under the restricted interface.
5. **Weighted observations.** Replace cardinality by total test cost; exact reduction is weighted set cover.

## Prior-art collision

The pairwise special case is directly in the classical Test Cover / binary identification family: tests separate object pairs and a minimum test family is sought. More generally, rough-set decision reducts use discernibility structures to select a minimum attribute subset preserving decision distinctions. Optimal adaptive identification via decision trees is also classical.

Therefore **restricted admissible observations, by themselves, do not establish a GC-II foundational novelty**. The exact minimal-bad-hyperedge formulation is useful bookkeeping for GC-II, but no novelty claim is made without a sharper GC-I-specific structural restriction and a theorem not reducible to known test-cover/reduct/decision-tree machinery.

## Status

- Naive pair-conflict cover for arbitrary set-valued restoration actions: **FALSIFIED**.
- Pair-conflict cover under singleton/2-Helly restoration semantics: **PROVED**.
- Minimal-bad-hyperedge cover theorem: **PROVED**.
- Restricted nonadaptive observation minimization: **IMPORTED/KNOWN mechanism (set cover / test cover / reduct collision)**.
- Restricted observations alone as Paper-II breakthrough: **FALSIFIED**.
- Adaptive restricted observation optimization: **OPEN in GC-II, but strong prior-art collision expected with optimal decision trees / diagnosis**.
- Surviving GC-specific target: prove a quantitative lower bound forced by the *algebra/closure of GC-I admissible generators* that is stronger than generic set-cover/test-cover complexity or identify a genuinely generative obstruction where the observation language itself changes under admissible transformations.

## Audit checks

- Domains: finite `W,A,Q`; all `R(w)` nonempty.
- Degenerate cases: universal action, empty obstruction family, inseparable obstruction.
- Monotonicity: adding observations cannot destroy sufficiency.
- Invariance: relabeling worlds/actions/observation outputs leaves obstruction-cover number unchanged.
- Composition: adding admissible tests can only weakly lower optimum; adding restoration options can delete minimal bad sets and can only weakly lower information need.
- Counterexample search target: explicitly test the 3-world pairwise-intersection/empty-global-intersection obstruction above.

No claim of novelty is made for the classical optimization mechanisms identified here.
