# GC-II Audit 219 — behavior-matched translator residual no-go

## Target
Audit 218 left open a residual translator quantity

\[
\Xi_{\rm GC}=T_{\rm GC}-T_{\rm behavior}
\]

under exactly the same physical architecture. This note tests whether strict positivity can follow from hidden GC mechanism/projection structure while the required externally observable behavior is held fixed.

## Operational setup
Fix an architecture \(\mathcal A\) (input placement, allowed interfaces, communication links, rounds, and cost convention). Let \(R\subseteq X\times Y\times Z\) be the complete externally required input/output relation. Let

\[
T_{\mathcal A}(R)=\inf\{c(P):P\text{ is an }\mathcal A\text{-protocol solving }R\}.
\]

A GC implementation \(G\) may possess latent states, generators, provenance, projections, rule histories, or closure structure. Define its operational specification \(R_G\) to contain exactly what the experimenter requires the translator to reproduce.

## Theorem 219.1 — behavior-matched residual collapse
If the GC translator is required to reproduce **exactly the same operational relation** as the behavioral comparator, i.e. \(R_G=R\), and both optimizations range over the same architecture \(\mathcal A\), then

\[
\boxed{T_{\rm GC}=T_{\rm behavior}=T_{\mathcal A}(R)}
\]

and therefore

\[
\boxed{\Xi_{\rm GC}=0.}
\]

### Proof
Under the hypotheses, the feasible protocol set in both minimizations is

\[
\mathsf P_{\mathcal A}(R)=\{P:P\text{ is an }\mathcal A\text{-protocol solving }R\}.
\]

The cost functional is also identical. The two infima are consequently the same. QED.

This is not an asymptotic statement and needs no finiteness, determinism, additivity, or rank assumption.

## Corollary 219.2 — hidden mechanism cannot force positive excess
Suppose two systems have identical externally required relation \(R\) but different hidden generative mechanisms. If the translator is not required to preserve or expose that hidden mechanism, no positive translator excess can be inferred solely from the hidden difference. Any protocol solving \(R\) is admissible for both tasks.

Status: **PROVED**.

## The only escape and its cost
To obtain \(T_{\rm GC}>T_{\rm behavior}\), the GC task must require additional operational content. Write an enriched relation

\[
\widetilde R_G\subseteq X\times Y\times (Z\times W),
\]

where \(W\) can encode, for example, provenance, a rule witness, an intervention trace, a certificate, or a projection-consistency witness. Forgetting \(W\) gives the behavioral relation \(R\).

Then

\[
T_{\mathcal A}(\widetilde R_G)\ge T_{\mathcal A}(R)
\]

because any protocol solving the enriched task solves the projected task after discarding \(W\).

But the excess

\[
\Delta_{\mathcal A}(\widetilde R_G\to R)
:=T_{\mathcal A}(\widetilde R_G)-T_{\mathcal A}(R)
\]

is now the complexity increase caused by changing the operational relation. It is not, without an additional theorem, evidence of a new GC-specific complexity notion: communication/search complexity already permits relational outputs and witnesses.

Status: monotonicity under output-forgetting **PROVED**; GC-specific novelty of the resulting excess **OPEN / prior-art collision required**.

## Edge and degeneracy audit
- Constant behavior: both matched costs are zero whenever the architecture permits zero-communication constant output; residual is zero.
- Impossible behavior: if both feasible sets are empty, both extended-real costs are \(+\infty\); the subtraction \(+\infty-(+\infty)\) is undefined, so \(\Xi\) must not be used there.
- Zero-cost nontrivial protocols: equality of feasible sets still gives equality of costs.
- Randomized/quantum/nondeterministic variants: the theorem survives provided the model, error criterion, and feasible protocol class are matched on both sides.
- Different architecture, error tolerance, rounds, observables, or output requirements invalidate the matched-comparator premise and cannot be attributed to GC structure alone.
- Composition: equality survives any composition operation for which both sides use the same composed feasible protocol class and cost functional.

## Consequence for the Paper-II search
The Audit-218 target `T_GC - T_behavior > 0` is **FALSIFIED as an intrinsic residual when “behavior” means the complete operational specification under the same architecture**.

A defensible survivor must therefore identify an experimentally mandated GC observable that is absent from ordinary endpoint behavior and then prove something stronger than generic relational/search complexity. Candidate structure must survive compilation into the operational relation itself. The next tests should focus on whether *families of interventions with shared latent consistency constraints* impose a joint realization obstruction not reducible to solving each induced relation separately; collisions to check include contextuality/marginal consistency, database join/decomposability, CSP width, distributed synthesis, and communication complexity of relations.

## Ledger
- Behavior-matched residual collapse: **PROVED**.
- Positive residual from hidden GC mechanism alone: **FALSIFIED**.
- Output-forgetting monotonicity for enriched operational relation: **PROVED**.
- Generic relational/witness complexity mechanism: **IMPORTED/KNOWN boundary**.
- Joint cross-intervention consistency obstruction beyond ordinary relational complexity: **OPEN**.
