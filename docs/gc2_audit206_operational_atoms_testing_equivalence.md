# GC-II Audit 206 — universal operational atoms collapse to testing/contextual equivalence

## Status

- Operational atom equivalence defined by preservation under every admissible experiment: **PROVED equivalent by definition to contextual/testing equivalence for that experiment language**.
- Equality with bisimulation without additional expressiveness assumptions: **FALSIFIED**.
- Equality with bisimulation for finite deterministic output-labelled transition systems with all finite action tests available: **PROVED**.
- Universal-experiment indistinguishability as a new GC-II invariant: **FALSIFIED / IMPORTED-KNOWN mechanism**.
- Restricted typed experiment families with independently charged translations: **OPEN**.

## Setup

Let a typed operational component `x` be placed in admissible experimental contexts `E in X`. Each experiment returns an observable law `Obs(E[x])` containing every quantity declared operationally visible (terminal task result, transcript law, resource consumption, interface events, and rule/admissibility events). Define

`x ≡_X y  iff  Obs(E[x]) = Obs(E[y]) for every E in X`.

Free fusion of two atoms was proposed in Audit 205 only when replacing them by the fused component leaves every admissible task/probe/cost experiment unchanged. Therefore free fusion is exactly membership in `≡_X`.

## Proposition 1 — contextual/testing collapse

For any fixed admissible experiment language `X`, the proposed interventionally defined operational equivalence is observational/contextual equivalence with respect to `X`; when contexts are explicitly tests, it is testing equivalence.

**Proof.** Both relations identify exactly those components that no context/test in `X` distinguishes by the declared observables. No additional GC structure appears in the relation. QED.

This is not merely terminological. Any scalar or set-valued invariant obtained only by quotienting components under all such experiments factors through the quotient `Components / ≡_X`; it cannot distinguish systems already identified by the established testing relation.

## Proposition 2 — bisimulation is not automatic

The implication `testing/contextual equivalence => bisimulation` is not valid for an arbitrary experiment language. Bisimulation is branching-sensitive, while a restricted test language can observe only traces, terminal outcomes, or other coarser behavior. Hence Audit 205's proposed test must not state that universal operational equivalence *is* bisimulation without proving that the chosen experiment language is characteristic for bisimulation.

## Proposition 3 — deterministic finite characteristic case

Consider a finite deterministic Moore-style transition system `(S,A,δ,o)` with finite action alphabet `A`, deterministic transition `δ:S×A->S`, and observable output `o:S->O`. Let experiments be all finite action words and let the observation of word `w` be the output reached after `w`. Define

`s ≡ t  iff  o(δ*(s,w)) = o(δ*(t,w)) for every w in A*`.

Then `s ≡ t` iff `s` and `t` are bisimilar under output-respecting deterministic bisimulation.

**Proof.** If `s≡t`, the empty word gives `o(s)=o(t)`. For every action `a` and suffix `w`, equality for `aw` gives equality of the observations from `δ(s,a)` and `δ(t,a)` under every suffix; hence successors are again equivalent. Thus `≡` is a bisimulation. Conversely, bisimulation induction on word length preserves equal outputs after every word. QED.

For `n` states, partition refinement stabilizes in at most `n-1` strict refinements, so finite-depth signatures suffice to decide this relation.

## Edge and composition checks

- Empty experiment family makes every component equivalent: correct but operationally degenerate.
- An experiment family containing direct state identity makes equivalence collapse to identity: also correct and shows dependence on declared observables.
- Enlarging the experiment family can only refine equivalence; it cannot merge previously distinguishable components.
- If contexts are closed under composition, contextual equivalence is a congruence by construction.
- Costs can be included in `Obs`; doing so refines the testing relation but does not change the structural conclusion.
- Probabilistic observations replace equality of outputs by equality of induced laws; this enters the established probabilistic testing/bisimulation spectrum rather than escaping it.

## Prior-art collision

Observational/contextual equivalence is classically defined by interchangeability in every observable context. Process theory separately studies trace, testing, simulation and bisimulation equivalences; probabilistic systems have corresponding testing and bisimulation spectra. Therefore the Audit-205 attempt to make factorization operational by quantifying over every admissible experiment does not create a new invariant merely from that quantification.

## Consequence for Omega_G

Do **not** define `Omega_G` as distance from universal operational equivalence or as a residual surviving its quotient. Without extra typed structure this is an established testing/contextual quotient. The remaining potentially GC-specific object must compare *restricted, physically admissible typed experiment languages* and charge the translators that move information/capability across `R/I/A/L` interfaces. A candidate must remain nonzero after quotienting by contextual equivalence and must not reduce to a standard simulation/testing distance.

Exact finite verifier: `experiments/gc2_audit206_operational_atoms_testing_equivalence.py`.
