# GC-II Audit 235 — Fiber-Ambiguity Collapse of the Audit-234 Translator Graph

Status: PROVED (finite deterministic one-way model); novelty boundary: graph-theoretic mechanism IMPORTED/KNOWN, simplification elementary.

## Setup
Let W be a finite world set, P the projection alphabet, G the required decision/capability alphabet, p:W->P, and g:W->G. The decoder knows p(w). A deterministic one-way translator sends m(w) in an alphabet M and the decoder must recover g(w) exactly from (p(w),m(w)).

Audit 234 defined H_{p,g} on W by joining w,w' iff p(w)=p(w') and g(w)!=g(w').

For a projection value z define the decision ambiguity

    a(z) = | { g(w) : w in W, p(w)=z } |,

and A = max_z a(z), with A=0 for W empty.

## Theorem (exact fiber-ambiguity translator law)
For nonempty W,

    chi(H_{p,g}) = A,
    M* = A,
    B* = ceil(log2 A).

### Proof
Fix a fiber F_z={w:p(w)=z}. Partition F_z by equal g-value. Two vertices in F_z are adjacent exactly when they lie in different parts. Hence H[F_z] is a complete a(z)-partite graph and chi(H[F_z])=a(z). There are no edges between different p-fibers, so H is the disjoint union of these complete multipartite graphs. Chromatic number of a disjoint union is the maximum chromatic number of a component, giving chi(H)=max_z a(z)=A.

Operationally, necessity is immediate: within a fixed z, worlds with different required g-values must receive different messages. Sufficiency: enumerate the distinct g-values independently inside each z-fiber using labels 1,...,a(z); labels can be reused across fibers because the decoder already knows z. Therefore exactly A messages suffice.

## Consequences
1. Positive local-to-global bit cost occurs iff A>=2, equivalently iff some projection fiber contains decision-incompatible worlds.
2. Audit 234's graph-coloring representation is correct but unnecessarily general for this exact model. Its graph belongs to the disjoint-union-of-complete-multipartite class, so generic chromatic-number hardness does not apply.
3. Computing B* requires only grouping worlds by p and counting distinct g-values in each group; it is polynomial/linear-time up to dictionary/set costs in an explicit finite table.
4. The bound is invariant under relabeling worlds, projection symbols, and decision symbols.
5. Degenerate cases: if g is constant on every p-fiber then A=1 and B*=0; if p is constant then A=|g(W)|; if p is injective then A=1; if W is empty, no operational message is required and the logarithmic formula should be handled by convention rather than log2(0).

## Composition warning
The scalar A is not a complete invariant for arbitrary sequential/compositional translator systems: composition can alter the side information, decision map, admissible message structure, or correlations. No multiplicative/additive law is claimed without explicit product semantics.

## Novelty / collision boundary
The coloring interpretation is neighboring zero-error source coding / characteristic-confusability graph theory (Witsenhausen/Korner and later functional compression). The collapse above follows from the special equivalence-fiber structure and is elementary graph theory. It should not be presented as a new graph-coloring theorem.

## Scientific correction to Audit 234
Retain Audit 234 as a correct exact verifier/result, but Paper II should state the sharper closed form A=max_z |g(p^{-1}(z))| rather than imply that a general graph-coloring optimization is needed. The scientifically interesting GC-II target must therefore arise only when GC operational constraints make messages/actions structured, partial, interactive, distributed, noisy, budgeted, or generated endogenously. In the unrestricted deterministic one-way finite model, the translator accounting problem is completely solved by fiber ambiguity.
