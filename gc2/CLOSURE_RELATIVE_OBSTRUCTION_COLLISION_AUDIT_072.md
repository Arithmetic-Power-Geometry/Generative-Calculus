# GC-II Audit 072 — Closure-Relative Implementation Obstruction Collision

## Scope
Branch-only Paper-II audit. GC-I `main` is frozen.

## Candidate inherited from Audit 071
Seek systems whose one-shot endpoint behaviors and free-randomized convex closures coincide, but whose future task-scale-error-budget closures under composition differ unless a typed augmentation crosses a growing lower bound:

\[
\Omega_{\rm CRIO}^{(n)}(S\to T)
=\operatorname{Min}_{\rm Pareto}\{\Delta:\mathcal C^{\rm comp}_{Q_n}(T)
\subseteq \mathcal C^{\rm comp}_{Q_n}(\operatorname{Augment}_{\Delta}(S))\}.
\]

## Result
**Status: FALSIFIED as a generic standalone novelty source.**

### Proposition 072.1 — Fixed-composition closure is an ordinary conversion preorder
Fix an operational model M specifying: objects/systems, free transformations, composition/tensor product, allowed catalysts/ancillas/randomness, error convention, and typed augmentation costs. Define

\[
S\succeq_{M,n,\epsilon,B}T
\iff
\mathcal C_{Q_n,\epsilon,B}^{\rm comp}(T)
\subseteq
\mathcal C_{Q_n,\epsilon,B}^{\rm comp}(S).
\]

Then this is simply a model-relative simulation/convertibility preorder on the chosen composite objects. If the model is closed under composition, replacing S by S^{\otimes n} (or the model's sequential/parallel composite) makes the n-copy question an ordinary conversion question in the enlarged object space. Adding catalysts or sublinear assistance similarly changes the allowed conversion relation rather than producing a logically new kind of order.

**Proof.** Reflexivity follows from identity simulation. Transitivity follows by composing the witnessing simulators/transformations, with the model's error and budget composition rule. All future task witnesses can be bundled into the operational specification of the composite object. Thus a discrepancy invisible at one copy but visible at n copies is activation/nonmultiplicativity of the conversion preorder under composition, not by itself a new generative invariant. QED.

This does not claim that computing the preorder is easy or that a finite monotone family always exists.

### Proposition 072.2 — Endpoint equality does not force compositional equality
Equality of a restricted one-shot endpoint summary E(S)=E(T) does not imply equality of composite closures unless E is a congruence for the composition law:

\[
E(S)=E(T)\;\not\Rightarrow\;E(S\otimes U)=E(T\otimes U).
\]

Hence a CRIO example obtained merely by choosing an endpoint quotient that is not compositionally complete demonstrates insufficiency of that quotient, not a new physical law. A valid GC-II claim would need to specify why the quotient is operationally canonical and still fails after every ordinary completion already represented by known conversion theory.

### Proposition 072.3 — Growing n-copy gaps are not sufficient novelty evidence
Nonadditivity, nonmultiplicativity, activation, catalysis, exact-vs-asymptotic gaps, and degeneration-vs-exact gaps already produce one-copy/composite separations. In tensor complexity, rank and border rank can be nonmultiplicative/submultiplicative under tensor product; border rank may differ from rank, and current work explicitly studies degeneration order/error degree. Strassen-type asymptotic spectra characterize asymptotic convertibility in broad preordered-semiring settings. Therefore a growing \Omega_CRIO^{(n)} is not novel merely because it emerges only under composition.

## Fresh collision check — 11 Sep 2026
1. Christandl, Jensen & Zuiddam showed tensor rank is not multiplicative under tensor product when border-rank phenomena intervene.
2. Christandl, Gesmundo & Jensen showed border rank itself can be strictly submultiplicative.
3. Ganesh, Koiran & Oliveira (10 Aug 2026) study quantitative degeneration order/error degree, i.e. the cost/complexity hidden behind approximate algebraic degeneration.
4. Alman & Li (20 May 2026) explicitly use Strassen's asymptotic-spectrum machinery to turn degeneration data into quantitative asymptotic-rank bounds.
5. Resource-theory literature contains exact/asymptotic conversion, activation and catalytic conversion phenomena; these are ordinary enrichments of the conversion preorder once the allowed transformations are fixed.

## Edge-case and invariant audit
- **n=1:** CRIO reduces to ordinary model-relative closure deficiency.
- **Free universal simulator:** obstruction vanishes.
- **Impossible augmentation:** frontier may contain infinity; this is feasibility, not automatically novelty.
- **Composition congruence:** if the chosen operational equivalence is a congruence and S,T are equivalent in the complete compositional theory, no CRIO separation remains.
- **Noncongruence:** a separation can be manufactured by an incomplete endpoint quotient; reject as breakthrough evidence.
- **Catalysts:** must be declared free/charged. Otherwise apparent gaps are accounting artifacts.
- **Approximation:** exact and approximate closures can differ; border-rank/degeneration and channel/resource theories already warn against conflating them.
- **Dimensions:** R,I,A,L remain typed Pareto coordinates; no scalar addition is assumed.
- **Monotonicity:** enlarging allowed augmentation cannot worsen the Pareto frontier; enlarging target task family cannot improve it.
- **Composition:** no additivity or multiplicativity assumption is licensed.

## Consequence for Paper II
Do **not** claim

\[
\text{same one-shot endpoints} + \text{different composite closure} + \text{growing augmentation cost}
\]

as the GC-II breakthrough. Without a stronger invariant this is compatible with known activation, catalysis, nonmultiplicativity, asymptotic-spectrum and degeneration phenomena.

## Surviving target — Boundary-Stable Novelty Defect
The remaining target must compare systems only after completing the ordinary conversion theory. Define an operational equivalence \equiv_* that identifies systems whenever they are mutually convertible under the declared free transformations, arbitrary declared catalysts/ancillas/randomness, and the declared asymptotic/approximate completion. Then seek a task family and *physical accounting boundary change* J such that

\[
S\equiv_* T
\quad\text{but}\quad
\Omega_{\rm BSND}(S,T;J)>0,
\]

where the positive typed gap cannot be removed by re-encoding, ordinary catalysts, amortization, free randomization, asymptotic completion, or replacing the systems by equivalent realizations.

This is **OPEN**. It is intentionally hard: if \equiv_* already contains every operationally relevant transformation, a positive gap risks contradiction or hidden model change. The next audit must determine whether BSND is impossible by definition (a no-go theorem) or whether a precisely defined accounting-boundary morphism creates a mathematically nontrivial relative invariant. The attack should connect this directly to GC-I's task-scale-error-budget envelope rather than invent another endpoint metric.

## Status ledger
- Generic closure-relative implementation obstruction as novel invariant: **FALSIFIED**.
- Fixed-composition closure induces ordinary simulation/convertibility preorder: **PROVED** under explicit closure assumptions.
- Restricted endpoint equality implies compositional equality: **FALSIFIED** without congruence.
- Composition-only growing gaps as novelty evidence: **IMPORTED/KNOWN architecture**.
- Boundary-Stable Novelty Defect after full ordinary conversion completion: **OPEN**.