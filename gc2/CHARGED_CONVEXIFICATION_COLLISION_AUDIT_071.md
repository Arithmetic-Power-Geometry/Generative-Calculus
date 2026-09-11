# GC-II Audit 071 — Charged Convexification Collision

## Scope
Branch-only Paper-II audit. GC-I `main` is frozen.

## Candidate inherited from Audit 070
For a target `y` lying in the formal convex hull of a physically realizable set but not in the set itself,

\[
\Gamma_G(y\mid S,M)=\operatorname{Min}_{\rm Pareto}\{\Delta:\;y\in K_{\operatorname{Augment}_{\Delta}(S;M)}\}.
\]

The question is whether the typed physical cost of realizing a formally convexified point is, by itself, a new GC-II invariant.

## Result
**Status: FALSIFIED as a standalone novelty source.**

### Proposition 071.1 — Convexification-as-synthesis reduction
Assume a finite explicit operational model in which each primitive implementation `s` induces an observable law `P_s`, and a target convexified behavior is

\[
P_y=\sum_{s\in S}\lambda_sP_s,\qquad \lambda_s\ge 0,\quad \sum_s\lambda_s=1.
\]

If an augmentation can realize `P_y` by selecting/coordination among primitive implementations, then the augmentation problem is an exact or approximate synthesis problem for the selector/correlation variable. Its minimum added randomness, communication, shared correlation, memory, or computation is therefore model-relative synthesis complexity. In particular, the existence of a positive cost does not establish a distinct generative phenomenon.

**Proof sketch.** Introduce selector `W` with `Pr(W=s)=lambda_s`. Conditional on `W=s`, execute primitive `s`. Any distributed or constrained implementation of this construction must physically create, transmit, share, store, or compute sufficient coordination to induce the required joint law. Conversely, any admissible exact synthesis protocol for the required selector/joint law yields an implementation of the convex mixture. Hence, once the implementation architecture and charged operations are fixed, the convexification-realization problem reduces to an exact/approximate channel or distribution synthesis problem, possibly with additional ordinary resource constraints. QED.

This is a reduction statement, not a claim that every synthesis model has the same closed-form optimum.

### Proposition 071.2 — No universal positive convexification charge
There is no representation-independent universal lower bound `Gamma_G(y)>0` that follows merely from `y in conv(K_S) \ K_S`.

**Construction.** Take the same primitive set and target mixture in two accounting models. In `M_free`, an external random selector with distribution `lambda` is a free admissible primitive; then the added charged cost is zero. In `M_charged`, the selector must be generated/stored/communicated internally and at least one designated charged coordinate can be positive. The observable target and formal convex-hull relation are identical. Thus positivity and magnitude are not determined by convex geometry alone. QED.

### Corollary 071.3 — Exactness penalty is imported structure
If GC-II distinguishes exact realization from approximate convexification, that distinction is not by itself novel. Exact common-information and exact channel-synthesis theory already studies the extra coordination rate required for exact generation, and exact requirements can exceed approximate ones.

## Fresh collision check (11 Sep 2026)
The collision became stronger, not weaker. Lei Yu's 26 Aug 2026 preprint *Exact Common Information and Exact Channel Synthesis for Correlated Gaussian Sources* reports exact formulas for correlated Gaussian exact common information and the complete shared-randomness/communication admissible region, with a strict exactness penalty for positive correlation. Earlier exact-common-information work already defines the minimum common randomness needed for exact distributed generation and gives multiletter characterizations. Distributed channel synthesis already characterizes communication/common-randomness tradeoffs.

Relevant sources checked:
- Lei Yu, *Exact Common Information and Exact Channel Synthesis for Correlated Gaussian Sources*, arXiv:2608.26012 (2026-08-26).
- Kumar, Li & El Gamal, *Exact Common Information*, arXiv:1402.0062.
- Cuff, *Distributed Channel Synthesis*, IEEE Transactions on Information Theory / arXiv:1208.4415.

## Edge-case and invariant audit
- **Degenerate target:** if `y in K_S`, `Gamma_G=0` under any sane augmentation convention.
- **Free randomness:** convexification charge can vanish.
- **No randomness interface:** exact realization can be impossible, giving an infinite coordinate/frontier rather than a finite novelty gap.
- **Approximation:** allowing error can sharply change the optimum; exact-vs-approximate penalties are already known in synthesis theory.
- **Dimensions:** `R,I,A,L` remain typed coordinates; no scalar addition is assumed.
- **Monotonicity:** enlarging the admissible augmentation set cannot increase the Pareto minimum; tightening exactness/error tolerance cannot improve feasibility.
- **Composition:** selector costs can amortize or share resources across repeated tasks, so additivity must not be assumed.
- **Encoding invariance:** the convex relation alone does not fix physical cost; an implementation/accounting model is indispensable.

## Consequence for Paper II
Do **not** claim

\[
\text{formal convexifiability} + \text{positive physical realization cost}
\]

as the GC-II breakthrough. It is scientifically useful accounting, but it collides with exact synthesis/common-information/randomness/communication complexity and is model-relative.

## Surviving target
A stronger candidate must couple capability accounting to something synthesis theory does not already quotient away. The next target is:

### Closure-relative implementation obstruction
Seek two systems for which all ordinary endpoint behavior/synthesis targets and all free-randomized convex closures coincide, yet their **future task-scale-error-budget closure under composition** differs unless a typed augmentation crosses a growing lower bound:

\[
\Omega_{\rm CRIO}^{(n)}
=\inf_{\Delta}\{\Delta:\;\mathcal C^{\rm comp}_{Q_n}(T_n)
\subseteq
\mathcal C^{\rm comp}_{Q_n}(\operatorname{Augment}_{\Delta}(S_n))\}.
\]

This is **OPEN**, not a breakthrough claim. It must be killed against amortized channel simulation, interactive/common randomness complexity, catalytic resource theories, asymptotic spectra, tensor-rank/border-rank phenomena, and ordinary composition complexity. A surviving theorem must show a lower bound that cannot be expressed solely as the cost of synthesizing a fixed target distribution/channel or selecting among fixed primitive implementations.

## Status ledger
- Generic charged convexification complexity as novel GC-II invariant: **FALSIFIED**.
- Convexification-as-synthesis reduction under explicit selector architecture: **PROVED**.
- Universal positive charge from convex geometry alone: **FALSIFIED**.
- Exact-vs-approximate realization penalty: **IMPORTED/KNOWN**.
- Closure-relative implementation obstruction `Omega_CRIO`: **OPEN**.
