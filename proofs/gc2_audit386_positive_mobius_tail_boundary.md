# GC-II Audit 386 — Positive Möbius mass does not make proper low-order accounting predictive

## Question

Audit 385 showed that normalization, monotonicity and submodularity do not control the signed higher-order Möbius residual because large positive and negative coefficients may cancel. A natural rescue is to forbid cancellation entirely.

Let (N) be finite, (v:2^N\to[0,1]), (v(\varnothing)=0), (v(N)=1), with Möbius transform
[
m(T)=\sum_{U\subseteq T}(-1)^{|T|-|U|}v(U),
qquad
v(S)=\sum_{T\subseteq S}m(T).
]
Assume
[
m(T)\ge 0\quad\text{for every nonempty }T.
]

For truncation order (q<|N|), define
[
V_q=\sum_{1\le |T|\le q}m(T),
qquad
E_q=\sum_{|T|>q}m(T).
]

## Proposition 1 — cancellation-free residual identity

Under the assumptions above,
[
V_q+E_q=\sum_{\varnothing\ne T\subseteq N}m(T)=v(N)=1,
]
hence
[
\boxed{E_q=1-V_q},\qquad \boxed{0\le E_q\le1}.
]

**Status: PROVED.**

This eliminates the combinatorial cancellation explosion of Audit 385.

## Proposition 2 — the bound is exactly tight

For every (n=|N|\ge2) and every (q<n), define the unanimity/conjunction capability
[
u_N(S)=\mathbf 1[N\subseteq S].
]
Since (S\subseteq N), equivalently (u_N(S)=\mathbf1[S=N]).

Its Möbius transform is
[
m(N)=1,qquad m(T)=0\quad(T\ne N).
]
Therefore it satisfies normalization, monotonicity and nonnegative Möbius mass, but
[
u_N(S)=0\quad\text{for all }|S|\le q,
]
while
[
u_N(N)=1.
]
Thus
[
V_q=0,qquad \boxed{E_q=1}.
]

Consequently no universal constant (c<1) can satisfy (E_q\le c) for all normalized nonnegative-Möbius capabilities when (q<n), even when every capability value through order (q) is known exactly.

**Status: PROVED / decisive falsification of the proposed rescue.**

## Operational realization

The witness is not dependent on a high-arity primitive. It is computed by binary AND composition:
[
z_2=x_1\land x_2,qquad z_k=z_{k-1}\land x_k.
]
A balanced binary tree gives logarithmic depth. Thus binary locality, determinism and acyclicity do not prevent the full unit capability mass from residing at order (n).

This reuses the mechanism established in Audit 384; it is not a novelty claim.

## Edge and degeneration checks

- (q=0): (V_0=0), (E_0=1).
- (q=n-1): the witness still gives (V_{n-1}=0), (E_{n-1}=1).
- (q=n): (E_n=0), as required.
- (n=1): there is no proper positive truncation order; the no-go statement is restricted to (q<n).
- Composition: binary AND composition preserves the witness while moving the externally visible interaction to arbitrary order.
- Scaling is unnecessary: the counterexample is already normalized to unit range.

## Prior-art boundary

Nonnegative Möbius mass for normalized capacities is standard belief-function / totally-monotone-capacity machinery, and unanimity games are standard basis objects in cooperative-game/capacity theory. Neither is claimed as GC-II novelty.

**Status: IMPORTED/KNOWN machinery.**

## Consequence for Paper II

Audits 385 and 386 now bracket the accounting obstruction:

1. signed high-order mass can generate large truncation residuals through cancellation;
2. forbidding cancellation still permits the entire normalized capability mass to be concentrated at an unseen order.

Therefore a useful GC-II accounting theorem must constrain **where interaction mass may reside across orders**, not merely its sign, total magnitude, output normalization, primitive locality, treewidth, monotonicity or submodularity.

A surviving target is a GC-I-derived, composition-aware tail-localization certificate (C_q(G)) such that
[
\sum_{|T|>q}|m(T)|\le C_q(G)
]
or, more weakly,
[
|E_q|\le C_q(G),
]
where (C_q(G)) is computable without exhaustive coalition evaluation and is not merely a renaming of known pseudo-Boolean degree, (k)-additivity, higher-order monotonicity, graphical width, or a standard resource-theory monotone.

**Status: OPEN.**

## Status ledger

| Claim | Status |
|---|---|
| Nonnegative Möbius mass removes signed cancellation explosion | PROVED |
| Normalization + nonnegative Möbius mass implies useful proper-low-order prediction | FALSIFIED |
| Universal (E_q<c<1) for (q<n) under those assumptions | FALSIFIED |
| Full unit capability can be hidden at an unseen order | PROVED |
| Möbius/belief-function/unanimity machinery | IMPORTED/KNOWN |
| GC-I-derived composition-stable tail-localization certificate | OPEN |
