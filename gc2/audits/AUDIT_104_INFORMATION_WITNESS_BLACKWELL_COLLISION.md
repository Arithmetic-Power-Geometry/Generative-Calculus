# GC-II Audit 104 — Information-Witness / Blackwell Collision

## Scope
Branch-only Paper-II audit. GC-I foundations on `main` remain frozen.

## Candidate attacked
Audit 103 left a narrower route: fix an operational realization boundary independently, then seek a capability-creation lower bound tied to a conserved operational or physical witness that cannot be removed by interpreter choice.

The first natural witness class is **task-relevant distinguishability / information**. This audit asks whether a No-Free-Capability theorem obtained only from monotonicity of information under admissible post-processing can constitute a GC-II breakthrough.

## Fixed-boundary model
Let `Theta` be a finite latent task/state set. A realization boundary exposes an experiment/channel

\[
E(y\mid \theta),\qquad \theta\in\Theta,\; y\in\mathcal Y.
\]

A free admissible transformation is a state-independent Markov kernel

\[
K(z\mid y),
\]

producing the post-processed experiment

\[
E'(z\mid\theta)=\sum_y K(z\mid y)E(y\mid\theta).
\]

For prior `pi`, action set `A`, and bounded utility `u(theta,a)`, define decision capability

\[
V_{\pi,u}(E)=\sup_{\delta:\mathcal Y\to\Delta(A)}
\mathbb E_{\theta\sim\pi,\,y\sim E,\,a\sim\delta(\cdot\mid y)}[u(\theta,a)].
\]

This is deliberately fixed-boundary: the latent states, channel boundary, free transformation class, and utility family are declared independently of the particular representation of `E`.

## Theorem 1 — Decision capability cannot increase under free garbling

**Status: PROVED / IMPORTED-KNOWN mechanism.**

If `E'=K E` for a state-independent Markov kernel `K`, then for every prior `pi`, action set, and bounded utility,

\[
\boxed{V_{\pi,u}(E')\le V_{\pi,u}(E).}
\]

### Proof
Take any decision rule `delta'` acting on `z`. Compose it with `K` to obtain a randomized decision rule on `y`,

\[
\delta(a\mid y)=\sum_z \delta'(a\mid z)K(z\mid y).
\]

The joint law of `(theta,a)` generated from `E` followed by this composed rule is exactly the law generated from `E'=KE` followed by `delta'`. Therefore every utility attainable after garbling was already attainable before garbling. Taking the supremum gives the inequality. QED.

This is the operational core of Blackwell comparison of statistical experiments and ordinary data-processing monotonicity.

## Corollary 1 — Information-monotone No-Free-Capability is not GC-specific

Suppose a proposed GC-II witness `W(E)` is monotone under the declared free kernels,

\[
W(K E)\le W(E),
\]

and capability is defined only through decision performance obtainable from `E`. Then any theorem of the form

\[
\Delta V>0\Longrightarrow \Delta W>0
\]

or

\[
\Delta V>0\Longrightarrow \text{a non-free information source entered the boundary}
\]

is either:

1. a consequence of Blackwell/data-processing theory; or
2. true by the definition of the chosen free transformations and therefore not yet a new quantitative law.

**Classification: FALSIFIED as a standalone GC-II breakthrough route.**

The result may remain useful as a consistency constraint, but renaming information, distinguishability, Bayes risk, deficiency, or an `f`-divergence as a generative witness does not create a new theorem.

## Corollary 2 — Scalar Omega_G from decision-information loss collides with deficiency

If one defines a novelty/capability gap solely from the worst decision-performance loss between two experiments, e.g.

\[
\Omega_G(E,F)=\sup_{\pi,u}\bigl[V_{\pi,u}(E)-V_{\pi,u}(F)\bigr]_+,
\]

then the construction lies directly in the comparison-of-experiments / deficiency family. Approximate comparison by maximal decision-risk loss is already the purpose of Le Cam/Torgersen deficiency machinery.

**Classification: FALSIFIED as standalone novelty.**

A GC-II `Omega_G` must therefore contain additional operational structure not recoverable from the experiment/channel comparison alone.

## Exact finite audit

`experiments/gc2_blackwell_witness_collision.py` performs an exhaustive deterministic finite check with:

- 3 latent states;
- 3 signal symbols;
- all `3^3 = 27` deterministic encoders `f:X->Y`;
- all `3^3 = 27` deterministic garblings `g:Y->Z`;
- all `2^3 = 8` binary classification tasks on the latent states;
- uniform prior;
- optimal deterministic decoding after each observation.

Total decision comparisons:

\[
27\times27\times8=5832.
\]

Recorded exact results:

- data-processing violations: **0**;
- strict decision losses after garbling: **864**;
- maximum optimal-accuracy loss: **1/3**.

The generated summary is stored in `results/gc2_blackwell_witness_collision_summary.json`.

This experiment is a consistency check for the theorem, not evidence of novelty.

## Edge and degenerate cases

- **Invertible relabeling:** equality holds for every decision problem.
- **Constant garbling:** all signal distinctions may collapse; decision value reduces toward prior-only performance.
- **Zero-information channel:** post-processing cannot create information about `theta`.
- **Randomized garbling:** the proof already covers stochastic kernels.
- **Different priors:** the inequality holds prior-by-prior.
- **Different utilities/actions:** the inequality holds for every bounded decision problem.
- **Approximate simulation:** collision strengthens to statistical-experiment deficiency rather than escaping it.
- **Quantum/generalized experiments:** analogous data-processing/resource-order structures already exist; merely enlarging the channel category does not establish GC-II novelty.

## Prior-art collision

The collision is direct, not superficial.

- Blackwell comparison ranks experiments by performance across all decision problems and characterizes loss of informativeness through garbling/randomization criteria.
- Le Cam/Torgersen deficiency quantifies approximate loss between experiments by worst decision-theoretic consequences.
- Information divergences satisfy data-processing monotonicity under Markov kernels; modern work continues to derive generalized information-processing relations.
- 2026 work on prior-free Blackwell comparison shows the comparison-of-information-structures program remains active, but does not create a distinct GC-II mechanism merely by changing the evaluation convention.

Representative sources used for this collision check:

1. Torgersen, E. (1991). *Comparison of Statistical Experiments*. Cambridge University Press.
2. Williamson, R. C., & Cranko, Z. (2022). *Information Processing Equalities and the Information-Risk Bridge*. arXiv:2207.11987.
3. Rosenthal, M. (2026). *Prior-free Blackwell*. Economic Theory Bulletin, 14, Article 4.

## Classification

- Fixed-boundary decision-value monotonicity under garbling: **PROVED / IMPORTED-KNOWN mechanism**.
- Exhaustive finite consistency audit: **NUMERICALLY SUPPORTED / exact enumeration**.
- Information/distinguishability witness as standalone No-Free-Capability breakthrough: **FALSIFIED**.
- `Omega_G` defined only through worst decision-value loss / experiment deficiency: **FALSIFIED as standalone novelty**.
- Fixed physical flux or operational witness not equivalent to information monotonicity: **OPEN**.

## Consequence for the Paper-II search

The remaining route must be stronger than `information cannot increase under post-processing`.

A defensible next candidate must simultaneously satisfy:

1. the realization boundary is fixed independently;
2. the witness is operationally measurable and has a composition law;
3. witness increase is not merely a restatement of Blackwell order, data processing, divergence contraction, majorization, thermodynamic monotonicity, or generic resource-theory monotones;
4. the theorem couples **creation of new admissible transformations/actions** to a quantitatively required external witness flux;
5. the bound yields a task-scale-error-budget consequence not obtainable by coordinate renaming into a standard complexity/resource inequality.

A promising-but-unproved direction is therefore a **boundary flux theorem for action-set expansion**, where the resource entering the boundary is independently measured and the conclusion concerns newly realizable transformations rather than only better inference about a fixed latent state. That direction remains **OPEN** and requires collision checks against thermodynamic resource theories, catalytic resource theories, control/reachability, and information-to-work conversion before any novelty claim.
