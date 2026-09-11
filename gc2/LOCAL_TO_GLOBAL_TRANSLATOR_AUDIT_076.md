# GC-II Audit 076 — Operational Local-to-Global Translator Collision

## Scope
Branch-only Paper-II audit. GC-I `main` remains frozen.

## Candidate inherited from Audit 075

Operational Local-to-Global Translator Lower Bound:

Lambda_G(n,k,epsilon) = Min_Pareto { Delta : a protocol using admissible local interfaces of order at most k plus typed augmentation Delta realizes the n-part global task to error epsilon }.

The intended strengthening over GC-I projection irreducibility was a quantitative operational price for crossing from locally indistinguishable states to a global task distinction.

## Result

**Status: FALSIFIED as a standalone GC-II novelty source in the canonical fresh-local-marginal model.** A clean transcript-indistinguishability theorem is PROVED, but its content reduces to standard oracle indistinguishability / k-wise-marginal structure; any positive typed augmentation bound remains architecture-relative.

### Definition 076.1 — Fresh local-marginal interface

Let theta in {0,1} index two n-part distributions P_theta. An admissible local query chooses I subseteq [n], |I| <= k, possibly as a function of the previous transcript, and receives a fresh draw Y ~ (P_theta)_I. Repeated queries need not use the same subset. Internal randomness and adaptive query choice are allowed.

### Theorem 076.1 — Adaptive transcript indistinguishability

Suppose every admissible query a has the same response kernel under the two worlds:

K_a(.|theta=0) = K_a(.|theta=1).

Then every finite adaptive randomized protocol built only from those queries has exactly the same transcript distribution under theta=0 and theta=1. Consequently, with equal priors, no terminal decision rule can distinguish the worlds with error below 1/2.

**Proof.** Induct on transcript length. The empty-transcript law is identical. If the prefix law is identical, the protocol's conditional distribution over the next query, being a function of that prefix and internal randomness, is identical. By hypothesis the conditional response kernel to that query is also identical. Therefore the joint law of the extended transcript is identical. Induction gives equality for the complete transcript, and any terminal decision is a post-processing of identical laws. QED.

### Proposition 076.2 — Parity witness

Let P_0 be uniform on n-bit strings of even parity and P_1 uniform on n-bit strings of odd parity. For every proper subset I subset [n],

(P_0)_I = (P_1)_I = Uniform({0,1}^{|I|}).

Hence for every k<n, Theorem 076.1 applies: unlimited adaptive fresh k-local marginal queries cannot distinguish P_0 from P_1 at all. The exact Bayes error remains 1/2.

**Proof.** Fix a proper subset assignment x_I. At least one coordinate lies outside I. Exactly half of completions have even parity and half have odd parity; each parity class therefore contributes the same probability 2^{-|I|}. QED.

### Corollary 076.3 — Interface-order threshold in this model

If augmentation is restricted to adding fresh-marginal interfaces of maximum arity r, the parity witness remains impossible for every r<n. An n-ary parity-sensitive observation can distinguish the two supports exactly. Thus the minimum observation order for this specific witness/model is n.

This threshold is mathematically valid but **not claimed novel**: it is a reformulation of the fact that the even/odd parity distributions agree on all proper marginals, equivalently that the distinguishing information lives in an n-way correlation/Fourier component.

### Theorem 076.4 — No architecture-independent typed translator lower bound

Local indistinguishability alone does not determine a positive lower bound in R,I,A,L. Take the same parity witness and the same local interface family. In architecture H_1 add a zero-cost global parity-sensitive primitive; in H_2 assign that primitive typed cost c>0; in H_3 forbid it entirely. The local data are identical in all three architectures, while the translator frontier respectively contains 0, depends on c, or is infeasible.

Therefore there is no universal function of (n,k,epsilon) and local indistinguishability alone that yields a nonzero physical Lambda_G in typed units.

**Status: PROVED by construction.**

## Exact finite-world exhaustive check

`experiments/gc2_parity_local_marginals.py` enumerates P_0 and P_1 exactly for n=2,...,8 and every 1<=k<n, projects onto every k-subset, and records the maximum absolute marginal difference. `results/gc2_parity_local_marginals.csv` contains 28 cases; every recorded difference is exactly 0.0.

This computation checks the finite witness implementation; it is not evidence for novelty and is not needed for the analytic proof.

## Prior-art collision

The surviving mathematics collides directly with established areas:

1. **k-wise independence / marginal indistinguishability.** Proper marginals can agree while a higher-order parity constraint differs globally; this is standard higher-order dependence structure.
2. **Query complexity and oracle indistinguishability.** If every allowed oracle response has the same law in two worlds, adaptive querying cannot distinguish them; parity and XOR are canonical hard structures in query-complexity lower bounds and XOR lemmas.
3. **Communication/distributed computation.** When local views reside at different parties and the translator is communication, the required augmentation becomes an ordinary communication-complexity quantity.
4. **Fourier analysis of Boolean functions.** Parity occupies the top-degree Fourier component, so invisibility to all proper coordinate marginals is not a new invariant.
5. **Marginal/contextuality/database/CSP formulations.** Local consistency failing to determine a global object is already a major established theme; recasting it as a closure gap does not by itself create novelty.

Useful collision references checked in this audit include Viola & Wigderson, *Norms, XOR Lemmas, and Lower Bounds for Polynomials and Protocols*, Theory of Computing 4 (2008), DOI 10.4086/toc.2008.v004a007; Brody et al., *A Strong XOR Lemma for Randomized Query Complexity*, Theory of Computing 19 (2023), DOI 10.4086/toc.2023.v019a011; and standard k-wise-independence literature.

## Edge and counterexample audit

- k=0: no observations; indistinguishability is trivial.
- k=n: the proper-marginal hypothesis ends; a parity-sensitive n-way observation can distinguish exactly.
- epsilon >= 1/2: no augmentation is needed for binary guessing with equal priors.
- epsilon < 1/2 and only fresh proper marginals: infeasible regardless of query count.
- Unequal priors: optimal error becomes min(pi_0,pi_1), again unchanged by identical transcript laws.
- Adaptive queries: covered by Theorem 076.1.
- Randomized translators: covered; internal randomness cannot separate identical response laws.
- Nonadditive typed costs: irrelevant to the impossibility theorem; once a distinguishing augmentation is admitted, its cost is model-relative.
- Same-instance local access: **not** covered by Definition 076.1. If several local reads can address the same persistent global instance, their joint transcript may reveal information absent from fresh marginals. That interface must be modeled separately.
- Noisy local kernels: theorem still holds when the two induced kernels are exactly equal. Approximate equality leads to ordinary total-variation/Le Cam-style accumulation bounds rather than a new GC invariant.
- Re-encoding: transported isomorphically, transcript equality is invariant.
- Composition: independent repetitions of identical transcript channels remain identical; richer cross-copy interfaces change the operational model.

## Consequence for Paper II

The local-to-global program yields a useful rigor statement but not the requested standalone breakthrough:

- Projection/local-marginal irreducibility can imply absolute impossibility under a precisely restricted interface.
- It does **not** imply a universal positive typed physical cost.
- Once the augmentation architecture is specified, its price is an ordinary query/communication/design/resource quantity unless an additional theorem survives those reductions.

Accordingly, Lambda_G should be retained as an application-specific accounting object, not marketed as new foundational mathematics on the parity witness.

## Next target — Reversibility-gap invariant

Proceed to Paper-II item (8). Define forward and return frontiers under the *same* operational grammar and test whether any path-sensitive remainder survives ordinary irreversibility, entropy production, resource-theory conversion loss, hysteresis, and computational uncomputation.

A candidate must distinguish:

1. endpoint conversion asymmetry already captured by a preorder,
2. ordinary thermodynamic dissipation,
3. model-relative implementation cost,
4. genuinely closure-level irrecoverability after quotienting by reversible re-encodings and declared free resources.

No breakthrough claim is made here.

## Status ledger

- Adaptive transcript indistinguishability theorem: **PROVED**.
- Parity all-proper-marginal witness: **PROVED**.
- Exhaustive n<=8 parity marginal check: **NUMERICALLY SUPPORTED / exact finite enumeration**.
- Minimum arity n for the parity witness in the fresh-marginal interface model: **PROVED but IMPORTED/KNOWN in substance**.
- Universal positive typed Lambda_G from local indistinguishability alone: **FALSIFIED**.
- Operational Local-to-Global Translator Lower Bound as standalone GC-II novelty: **FALSIFIED**.
- Reversibility-gap invariant: **OPEN**.
