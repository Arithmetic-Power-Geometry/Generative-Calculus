# Audit 032 — Operational local-to-global translator lower bound

## Question
Can the GC-I projection-irreducibility phenomenon be strengthened from a qualitative statement (“proper projections do not determine the whole envelope”) into an operational lower bound on what any exact local-to-global translator must acquire?

## Result
Yes, for an explicit finite family. The result is exact, but the proof mechanism is coding/information theory and is therefore **PROVED / IMPORTED-KNOWN mechanism**, not yet the Paper-II breakthrough.

Let `C <= F_2^n` be a binary linear code with dimension `d` and dual distance `d_perp`. For each coset index (syndrome) `s in F_2^{n-d}`, let `P_s` be the uniform distribution on the coset

\[
C_s=\{x\in F_2^n:Hx=s\},
\]

where `H` is a full-rank parity-check matrix.

For every coordinate set `J` with `|J| < d_perp`, the marginal `(P_s)_J` is uniform on `F_2^{|J|}` and is independent of `s`. Hence every observer restricted to fewer than `d_perp` coordinates sees exactly the same family of local operational statistics for all `2^{n-d}` global worlds.

However the global worlds are mutually distinct: the syndrome task

\[
T_H(x)=Hx
\]

has deterministic value `s` under `P_s`.

Therefore any exact translator which, from the common collection of all `< d_perp`-coordinate local data plus an auxiliary message `M`, must reconstruct which global operational world `P_s` is present, requires at least

\[
\boxed{|M|\ge n-d\ \text{bits}}
\]

in the worst case (and also `H(M) >= n-d` for a uniformly distributed syndrome under zero error).

Equivalently, if the translator receives fewer than `n-d` auxiliary bits, at least two cosets remain compatible with exactly the same local observations and message, so exact whole-envelope reconstruction is impossible.

## Proof
### 1. Local indistinguishability
A standard characterization of dual distance says that a linear code whose dual distance is `d_perp` has uniform projections onto every set of fewer than `d_perp` coordinates. Translation by a coset representative preserves uniformity. Thus for every `s,s'` and every `J` with `|J|<d_perp`,

\[
(P_s)_J=(P_{s'})_J=\mathrm{Unif}(F_2^{|J|}).
\]

Hence even the *complete collection* of all allowed local marginals contains zero information about the syndrome.

### 2. Number of compatible global worlds
There are exactly `2^{n-d}` cosets because `rank(H)=n-d`. They are disjoint and each has a different deterministic value of `T_H`.

### 3. Translator lower bound
An auxiliary message of `m` bits has at most `2^m` values. If `m<n-d`, pigeonhole forces two distinct syndromes to receive the same message. Since their entire allowed local data are also identical, an exact translator receives identical input on two globally different worlds and therefore cannot reconstruct both correctly. Thus `m>=n-d`.

For uniform `S`, local data `L` satisfy `I(S;L)=0`. Zero-error reconstruction from `(L,M)` gives `H(S|L,M)=0`, so

\[
H(S)=I(S;M|L)\le H(M),
\]

and `H(S)=n-d` bits.

## Operational GC interpretation
Treat each coordinate as a locally queryable interface and the syndrome task `T_H` as a whole-envelope task. The family then has:

- identical outcomes for every allowed local query of arity `< d_perp`;
- identical local resource budgets and action availability if those are held fixed across cosets;
- a global task whose exact answer differs across `2^{n-d}` worlds;
- a certified minimum information augmentation of `n-d` bits for any exact translator from the local representation to the global one.

This turns qualitative projection irreducibility into a quantitative augmentation statement:

\[
\boxed{\Delta I_{\rm translator}\ge \log_2 N_{\rm compatible}}
\]

for this family, with `N_compatible=2^{n-d}`.

The bound is not an additive assumption about `R/I/A/L`; it is a zero-error information requirement after local observations have been fixed.

## Edge and degeneracy checks
- `d=n`: one coset, `n-d=0`; the lower bound correctly vanishes.
- `d_perp=1`: there is no nonempty protected local projection; the statement becomes vacuous for positive-arity local observations.
- If the global syndrome task is removed from the operational envelope, distinct cosets may become operationally equivalent and the lower bound need not apply.
- If a permitted interface directly reveals `Hx`, the information is no longer absent from the local representation; the augmentation bound moves into the cost/accounting of that interface.
- Approximate reconstruction requires a rate-distortion/Fano-type reformulation; the exact bound above is zero-error only.
- Randomized translators cannot beat the bound under zero error because identical translator inputs must induce the same output distribution.
- Shared randomness independent of the syndrome does not reduce the zero-error information requirement.
- If the auxiliary message is allowed to encode an oracle for the syndrome at zero accounting cost, the theorem is intentionally defeated; such an oracle is precisely the missing augmentation being priced.

## Composition behavior
For independent blocks `C^(1),...,C^(r)` with independent syndromes, the compatible-world count multiplies and the exact information lower bounds add:

\[
\log_2\prod_i 2^{n_i-d_i}=\sum_i(n_i-d_i).
\]

This additivity is a property of the independent witness family, not a universal GC-II additivity axiom.

## Prior-art collision
The mathematical mechanism is not new: orthogonal arrays / dual-distance coding results give low-order uniformity, and the information lower bound is elementary zero-error counting/entropy. Related marginal/contextuality phenomena also separate locally identical data from incompatible or distinct global completions.

Classification:

- qualitative local-to-global failure: already present in GC-I and neighboring marginal/contextuality theory;
- code-coset parametric amplification: **PROVED**;
- `n-d` exact auxiliary-information lower bound: **PROVED / IMPORTED-KNOWN mechanism**;
- claim that this alone is a GC-II breakthrough: **REJECTED**;
- a lower bound coupling translator information to *budgeted creation of new operational actions/rules/tasks*, surviving reduction to coding, communication complexity, database/CSP width and contextuality: **OPEN**.

## Consequence for Omega_G
This audit gives a defensible component lower bound for any novelty-gap definition that charges missing information required for exact whole-envelope recovery:

\[
\Omega_G(X_{\rm local}\to X_{\rm global})\succeq (0,n-d,0,0)
\]

when coordinates are measured in bits and the other accounting axes are held fixed. It does **not** establish a universal scalar Omega, nor does it license adding bits to physical resource units.

The result also provides a falsification test for proposed `Omega_G`: any purported exact whole-envelope novelty gap that assigns zero information augmentation to this witness family is incomplete unless it explicitly prices an equivalent action/rule/resource augmentation elsewhere.

## Next attack
1. Implement exhaustive small-code witnesses and verify all protected marginals and syndrome separations exactly.
2. Replace free auxiliary bits by an explicit budgeted acquisition protocol and ask whether a tradeoff frontier between `Delta R`, `Delta I`, `Delta A`, and `Delta L` can be proved.
3. Search for a family where the cheapest escape can use qualitatively different augmentation channels (information, action/interface, or rule change), so the theorem is genuinely a coupled Pareto accounting law rather than a renamed information bound.
4. Collision-test that tradeoff against communication complexity, index/network coding, secret sharing, database join dependencies, CSP width, contextuality/marginal extension, and resource theories before any novelty claim.