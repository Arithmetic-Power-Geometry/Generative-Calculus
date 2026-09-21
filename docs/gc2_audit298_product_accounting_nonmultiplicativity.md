# GC-II Audit 298 — Product accounting is submultiplicative, not multiplicative

## Target
Test composition behavior of the exact finite worst-case capability-account number from Audits 290–297. In particular, determine whether independent interfaces force multiplicative account size.

## Product operational instance
Let finite feasible accounting instances `I_1=(Y_1,A_1,B_1)` and `I_2=(Y_2,A_2,B_2)` have exact minimum feasible-action cover numbers `N_1,N_2`.

Define their strict product instance by

- targets `Y = Y_1 x Y_2`;
- decoder actions `A = A_1 x A_2`;
- product feasibility

`B(a_1,a_2) = B_1(a_1) x B_2(a_2)`.

This corresponds to a conjunctive independent interface: a product decoder is valid exactly when both component decoders are valid.

Let `N_x` denote the minimum number of product actions whose feasible rectangles cover `Y_1 x Y_2`.

## Theorem 298.1 — universal product sandwich
For every pair of finite feasible nonempty instances,

`max(N_1,N_2) <= N_x <= N_1 N_2`.

### Proof
Upper bound: take optimal component covers `C_1,C_2`. The Cartesian action family `C_1 x C_2` has `N_1 N_2` rectangles and covers every `(y_1,y_2)`.

Lower bound: let `C` be any product-action cover. Project its first action coordinates. For any fixed `y_2 in Y_2` and every `y_1 in Y_1`, some `(a_1,a_2) in C` covers `(y_1,y_2)`, hence `y_1 in B_1(a_1)`. Thus the first-coordinate projection of `C` covers `Y_1`, so `|C| >= N_1`. Symmetrically `|C| >= N_2`. Minimize over `C`. QED.

## Theorem 298.2 — multiplicativity is false
There exist two identical component instances with `N_1=N_2=2` but `N_x=3<4=N_1N_2`.

Take each target set as `{0,1,2}` and the three feasible action sets

`S_0={0,1}, S_1={0,2}, S_2={1,2}`.

No single action covers all three targets, while any two distinct actions cover them, so each component has `N=2`.

In the product, the three diagonal rectangles

`S_0 x S_0`, `S_1 x S_1`, `S_2 x S_2`

cover all nine target pairs: for any `(i,j)`, at least one of the three two-element sets contains both `i` and `j`. Hence `N_x<=3`.

Two rectangles cannot cover the product. Each rectangle has area four. The union of two rectangles therefore has cardinality at most eight, strictly below the nine product targets. Hence `N_x>=3`. Therefore `N_x=3`.

Thus

`N(I x I)=3 < 4=N(I)^2`.

## Derived invariant candidate — composition compression gain
Define

`Gamma_x(I_1,I_2) = (N_1 N_2)/N_x`.

For nonempty feasible strict products, Theorem 298.1 gives

`1 <= Gamma_x <= min(N_1,N_2)`.

`Gamma_x=1` means no account compression from joint product coding; `Gamma_x>1` records exact joint-cover reuse. This is dimensionless and invariant under relabeling of targets/actions. It is NOT yet proposed as a new universal GC invariant: its relation to known direct-product and rectangle-cover parameters must be collision-checked before any novelty claim.

For the triangle instance, `Gamma_x=4/3` exactly.

## Edge and degenerate cases
- Empty target factors are excluded from the sandwich statement because the conventional cover number is zero and projection arguments become vacuous.
- Infeasible factors (uncovered targets) are excluded; their account number is infinite/undefined under the finite convention.
- If `N_1=1` or `N_2=1`, the sandwich forces `N_x=max(N_1,N_2)`, hence multiplicativity holds in that special case.
- Duplicate actions do not affect any cover number.
- The theorem concerns strict Cartesian product actions and conjunctive feasibility. Cross-coupled joint actions can violate these bounds and require separate treatment.

## Monotonicity / composition behavior
The result proves that exact account number is generally submultiplicative under strict product composition, but not multiplicative. Consequently fixed-length account bits satisfy

`ceil(log2 max(N_1,N_2)) <= ceil(log2 N_x) <= ceil(log2(N_1N_2))`.

The triangle collision shows that adding component bit lower bounds is not generally exact for joint accounting.

## Prior-art collision status
The combinatorics are rectangle/set-cover and direct-product phenomena and are therefore treated as **IMPORTED/KNOWN territory unless a stronger GC-specific statement survives dedicated prior-art review**. No novelty is claimed for generic rectangle covering or submultiplicative cover parameters.

The GC-II consequence is nevertheless decisive: an additive capability-accounting law under independent composition cannot be assumed from the exact operational cover semantics. Interaction/compression terms are mathematically necessary even before physical or informational coupling is introduced. This directly supports Paper-II item (5)'s instruction not to assume additivity.

## Status
- Product sandwich: **PROVED**.
- Exact multiplicativity `N_x=N_1N_2`: **FALSIFIED**.
- Triangle strict-compression witness `2 x 2 -> 3`: **PROVED**.
- `Gamma_x` bounds and triangle value: **PROVED**.
- Generic rectangle/direct-product mathematics: **IMPORTED/KNOWN territory**.
- Novelty of `Gamma_x` as a GC invariant: **OPEN / NOT CLAIMED**.
- Characterization of equality `N_x=N_1N_2`: **OPEN**.
- Asymptotic regularized rate `lim_k (1/k) log N(I^{x k})`: **OPEN**.

## Paper-II consequence
Any quantitative law for `Omega_G <= F(Delta R,Delta I,Delta A,Delta L)` must allow non-additive interaction terms under composition. Even the exact finite operational account number itself exhibits strict joint compression under a completely uncoupled Cartesian interface.