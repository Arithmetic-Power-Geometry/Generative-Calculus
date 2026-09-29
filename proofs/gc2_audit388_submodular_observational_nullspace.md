# GC-II Audit 388 — Submodular observational-nullspace witness

## Purpose

Test whether the bounded-radius complement-query impossibility surviving from the signed Möbius setting disappears after imposing normalization, monotonicity, and submodularity.

## Setup

Let (N) have (n\ge 3) elements. Define the symmetric set functions

[
g_n(S)=\sqrt{|S|/n},
qquad
v_\varepsilon(S)=g_n(S)+\varepsilon\mathbf 1[|S|=1].
]

Set

[
\delta_n=\frac{2\sqrt2-1-\sqrt3}{\sqrt n}>0.
]

Assume (0<\varepsilon\le\delta_n).

For a set function (f), let

[
m_f(T)=\sum_{U\subseteq T}(-1)^{|T|-|U|}f(U)
]

be its Boolean-lattice Möbius transform and define the order-(q) signed tail

[
E_q(f)=\sum_{|T|>q}m_f(T),qquad 1\le q<n.
]

## Theorem 388.1 — normalized monotone submodular collision

For every (n\ge3), every (0<\varepsilon\le\delta_n), and every complement-observation radius (R\le n-2):

1. (g_n) and (v_\varepsilon) are normalized, ([0,1])-valued, monotone, and submodular;
2. they agree on every queried near-full coalition:
   [
   v_\varepsilon(N\setminus A)=g_n(N\setminus A)
   quad\text{for every }|A|\le R;
   ]
3. nevertheless
   [
   E_q(v_\varepsilon)-E_q(g_n)
   =\varepsilon n(-1)^q\binom{n-2}{q-1}.
   ]

Hence bounded-radius complement observations do not identify the signed higher-order Möbius tail even within normalized monotone submodular capabilities.

**Status: PROVED.**

## Proof

### Normalization and range

Both functions vanish at the empty set and equal one at (N). Only singleton values are changed. Since

[
\varepsilon\le\delta_n<\frac{\sqrt2-1}{\sqrt n},
]

the perturbed singleton value remains below the two-element value, so the range remains inside ([0,1]).

### Monotonicity and submodularity

For a cardinality-based set function (f(S)=\phi(|S|)), submodularity is equivalent to nonincreasing discrete increments
[
d_k=\phi(k)-\phi(k-1).
]

The unperturbed sequence (\sqrt{k/n}) is increasing and concave. Under the singleton perturbation, only the first two increments change:

[
d'_1=\frac1{\sqrt n}+\varepsilon,
]

[
d'_2=\frac{\sqrt2-1}{\sqrt n}-\varepsilon,
]

while for (k\ge3),

[
d'_k=\frac{\sqrt k-\sqrt{k-1}}{\sqrt n}.
]

The inequality (d'_1\ge d'_2) is automatic for (\varepsilon>0). The only new binding condition is

[
d'_2\ge d'_3
iff
\varepsilon\le
\frac{2\sqrt2-1-\sqrt3}{\sqrt n}
=\delta_n.
]

All later increments decrease by concavity of the square root. Also (d'_2>0) under this bound, hence every increment is nonnegative. Therefore (v_\varepsilon) is monotone and submodular.

### Exact observation collision

If (|A|\le R\le n-2), then
[
|N\setminus A|\ge2.
]
The perturbation is supported only at singleton coalitions. Therefore
[
v_\varepsilon(N\setminus A)=g_n(N\setminus A).
]

The full permitted observation vectors are identical.

### Exact hidden-tail separation

Let
[
h(S)=\mathbf1[|S|=1].
]
Then (v_\varepsilon=g_n+\varepsilon h). For nonempty (T),

[
m_h(T)
=\sum_{\substack{U\subseteq T\\|U|=1}}
(-1)^{|T|-1}
=|T|(-1)^{|T|-1}.
]

Thus

[
E_q(v_\varepsilon)-E_q(g_n)
=\varepsilon
\sum_{k=q+1}^{n}
\binom nk k(-1)^{k-1}.
]

Using
[
k\binom nk=n\binom{n-1}{k-1}
]
and the alternating partial-sum identity
[
\sum_{j=q}^{n-1}(-1)^j\binom{n-1}{j}
=(-1)^q\binom{n-2}{q-1},
]
we obtain

[
E_q(v_\varepsilon)-E_q(g_n)
=\varepsilon n(-1)^q\binom{n-2}{q-1}.
]

This proves the theorem.

## Corollary 388.2 — polynomial separation

Choose (\varepsilon=\delta_n/2). Then

[
|E_q(v_\varepsilon)-E_q(g_n)|
=
\frac{2\sqrt2-1-\sqrt3}{2}
\sqrt n\binom{n-2}{q-1}.
]

For fixed (q\ge1), this is

[
\Theta(n^{q-1/2}).
]

Thus identical bounded-radius near-full observation records can coexist with polynomially separating signed interaction tails inside the normalized monotone submodular class.

**Status: PROVED.**

## Edge and degeneracy checks

- (n\ge3) is required so that a nontrivial radius (R\le n-2) and the third discrete increment exist.
- (q=n) is excluded because both tails are then zero.
- At (q=n-1), the formula reduces to the difference in the unique order-(n) coefficient.
- At (\varepsilon=0), the pair collapses and the separation vanishes.
- The construction does not contradict positive-Möbius results: its perturbation has alternating signed Möbius coefficients.
- The theorem is an identifiability impossibility for the stated observation operator; it is not a claim that unrestricted value queries cannot recover the set function.

## Prior-art boundary

The ingredients “concave cardinality function implies submodularity” and Boolean-lattice Möbius inversion are imported/known. This audit does not claim novelty for either ingredient. The GC-II-specific surviving target is stronger: derive from GC-I admissible operational composition a non-tautological structural condition that eliminates or quantitatively contracts directions in the kernel of the operational observation map.

## Status ledger

| Claim | Status |
|---|---|
| Concave-cardinality submodularity principle | IMPORTED/KNOWN |
| Boolean-lattice Möbius inversion | IMPORTED/KNOWN |
| (g_n,v_\varepsilon) normalized, monotone, submodular under the stated bound | PROVED |
| Exact bounded-radius complement-observation collision | PROVED |
| Exact residual-separation formula | PROVED |
| Signed-tail identification from these observations under submodularity | FALSIFIED |
| Positive-Möbius Audit-387 certificate invalidated | NO — SURVIVES |
| GC-I-derived composition-stable observation-kernel contraction theorem | OPEN |

## Consequence for Paper II

Submodularity is not the missing structural hypothesis. The next useful theorem search should work directly with the operational observation map and GC-I admissible transformations: characterize when admissible composition intersects its kernel trivially, or prove a quantitative contraction bound on that intersection.
