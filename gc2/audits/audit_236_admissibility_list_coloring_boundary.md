# GC-II Audit 236 — Admissibility-Constrained Translators Collapse to List Coloring

Status: PROVED (finite deterministic one-way exact model); novelty boundary: reduction IMPORTED/KNOWN graph mechanism; unrestricted fiber scalar is no longer complete.

## Setup
Let W be finite, p:W->P the decoder side-information/projection, and g:W->G the required exact decision. Fix a finite message alphabet M. Unlike Audits 234–235, each world w has an explicit nonempty admissible-message set L(w) subseteq M, representing interface/action/rule constraints. A translator is a map m:W->M such that (i) m(w) in L(w), and (ii) a decoder D satisfies D(p(w),m(w))=g(w) for every w.

Let H_{p,g} have vertex set W and edge ww' exactly when p(w)=p(w') and g(w)!=g(w'), as in Audits 234–235.

## Theorem 236.1 (exact constrained-translator criterion)
An exact admissible translator exists iff H_{p,g} has a proper list coloring c with c(w) in L(w).

### Proof
Necessity: if ww' is an edge, the decoder sees the same p-value but must output different g-values. Hence m(w)!=m(w'). Together with admissibility m(w) in L(w), m is a proper list coloring.

Sufficiency: let c be a proper list coloring. For each observed pair (z,a), all worlds w with p(w)=z and c(w)=a must have the same g(w); otherwise two such worlds would be adjacent and have equal colors. Define D(z,a) to be this common g-value on observed pairs (arbitrary elsewhere). Then D(p(w),c(w))=g(w) exactly and c(w) is admissible.

Thus constrained exact translation and list coloring are the same feasibility problem for this model.

## Corollary 236.2 (Audit-235 scalar A ceases to be complete)
A=max_z |g(p^{-1}(z))| is still a necessary unconstrained message-alphabet lower bound, but it does not determine feasibility once L is present.

Counterexample: W={u,v}, p(u)=p(v)=z, g(u)!=g(v), so A=2. Let M={0,1} and L(u)=L(v)={0}. Then no exact translator exists although |M|=A. Replacing L(v) by {1} makes translation feasible without changing p,g,A, or |M|.

Therefore admissibility is not a perturbation of the fiber-ambiguity scalar: its incidence pattern matters.

## Corollary 236.3 (structured constraints can restore computational hardness)
Each H_{p,g} is still a disjoint union of complete multipartite graphs. Nevertheless, list-coloring difficulty can already occur on complete bipartite graphs, which are a subfamily obtained from one p-fiber with two g-values. Hence the polynomial closed form of Audit 235 does not extend to arbitrary per-world admissibility lists unless additional structure is imposed on L.

This is a boundary result, not a GC novelty claim: list coloring is established graph theory, and NP-completeness results are known even for bipartite and complete-bipartite restrictions. Paper II must cite that literature rather than claim the hardness mechanism.

## Accounting consequence
The correct constrained state descriptor cannot be only (p,g,A). At minimum it must retain the admissibility incidence relation

    E_L = {(w,a): a in L(w)}.

Two systems with identical p, g, A and alphabet size can differ in exact reachability solely through E_L. Therefore any Omega_G or capability-accounting law that charges only counts Delta A or Delta L but ignores which worlds/actions are admissibly coupled remains vulnerable to the semantic-payload obstruction of Audits 229–230.

## Checks
- Domain: finite W,P,G,M; L(w) nonempty for operational worlds. Empty lists correctly make feasibility fail.
- Degenerate p injective: H has no edges, so feasibility reduces to choosing any allowed message independently per world.
- Decision-constant fibers: same reduction; no within-fiber conflicts.
- Unconstrained L(w)=M: list coloring reduces to ordinary coloring and Audit 235 is recovered exactly.
- Relabeling invariance: simultaneous bijective relabeling of worlds/messages/projection/decision symbols preserves feasibility.
- Monotonicity: enlarging any L(w) cannot destroy feasibility; deleting allowed messages can.
- Composition: no additive/multiplicative law is claimed. Sequential interfaces alter lists and side information and require explicit semantics.

## Ledger
- Exact admissibility-constrained translator <=> list coloring of H_{p,g}: PROVED.
- Fiber ambiguity A as complete invariant under arbitrary admissibility constraints: FALSIFIED.
- Arbitrary admissibility restores nontrivial computational structure even though H is complete-multipartite by fibers: PROVED; complexity mechanism IMPORTED/KNOWN.
- List-coloring/hardness as GC-II novelty: FALSIFIED.
- A GC-specific law for how admissible transformations/resources/information/interfaces generate or relax E_L under budget: OPEN.

## Next breakthrough gate
Do not merely add more generic constraints. Formalize a budgeted operational closure in which R,I,A,L induce E_L through explicit typed operations, then ask whether changes to the admissibility incidence structure obey a GC-specific monotone, conservation inequality, or closure-escape law. Any candidate must be tested against list coloring, CSP/homomorphism, communication complexity, resource theories, and simulation preorders before novelty is claimed.
