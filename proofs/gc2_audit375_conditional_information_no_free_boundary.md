# GC-II Audit 375 — Conditional-information no-free-capability boundary

**Scope.** GC-II branch only. GC-I foundations on `main` are unchanged.

## Question

Can the projection/interface program yield a nontrivial No-Free-Capability theorem merely by charging acquired information?

## Operational model

Let

- `G` be the hidden global operational state/world;
- `X` be all information supplied free by the permitted proper projections;
- `T` be the complete charged interface transcript acquired after observing `X`;
- `Y` be the translator/controller output used to select the required capability/action.

The implementation assumption is only the conditional Markov property

[
G \longrightarrow (X,T) \longrightarrow Y,
]

i.e. after the free projection and acquired transcript are fixed, the output has no additional access to the hidden global state.

All logarithms below are base 2.

## Theorem 375.1 — conditional no-free-information inequality

Every such implementation satisfies

[
I(G;Y\mid X) \le I(G;T\mid X).
]

### Proof

By conditional data processing applied at each value of `X`, processing `T` into `Y` cannot increase information about `G`. Averaging over `X` gives the displayed inequality. QED.

**Status:** PROVED, but the mechanism is IMPORTED/KNOWN (data processing).

## Corollary 375.2 — exact capability-class recovery

Let `C=c(G,X)` be the capability-equivalence class that must be selected exactly, and suppose `Y=C` almost surely. Then

[
I(G;T\mid X) \ge I(G;C\mid X)=H(C\mid X).
]

Thus the charged transcript must carry at least the conditional entropy of the required capability label beyond the free projection.

For a projection fiber with `N` equiprobable required classes,

[
I(G;T\mid X=x)\ge \log_2 N.
]

This recovers the deterministic class-count bound of Audit 374 in the uniform zero-error case.

**Status:** PROVED; not novel.

## Corollary 375.3 — approximate recovery

If `C` has at most `N` values and an estimator from `Y` has error probability `p_e`, Fano's inequality gives

[
H(C\mid Y,X)\le h_2(p_e)+p_e\log_2(N-1).
]

Hence

[
I(G;T\mid X)
\ge I(C;Y\mid X)
\ge H(C\mid X)-h_2(p_e)-p_e\log_2(N-1).
]

The right-hand side is clipped at zero when used as a nonnegative lower bound.

**Status:** PROVED from standard data processing + Fano; IMPORTED/KNOWN mechanism.

## Edge/degenerate checks

1. **No projection deficit:** if `H(C|X)=0`, the lower bound is zero, as required.
2. **Exact recovery:** `p_e=0` reduces to `I(G;T|X)>=H(C|X)`.
3. **One capability class:** `N=1` is trivial and must be handled separately; no information is required.
4. **Free side channel:** if hidden class information is added to `X`, the bound correctly collapses; therefore no unconditional translator lower bound follows from projection irreducibility alone.
5. **Randomized translator:** the Markov proof still applies; private randomness cannot create information about `G`.
6. **Interactive transcript:** interaction does not invalidate the inequality once the complete transcript is represented by `T`; optimizing transcript information is an information-complexity problem.
7. **Units:** all quantities are bits, so the bound is dimensionally consistent.
8. **Composition:** no additivity is asserted. Conditional mutual information can exhibit redundancy/synergy under composition, so an additive GC law cannot be inferred from this theorem.

## Collision audit

The result is not a new GC invariant. Its proof engine is the classical data-processing inequality. The approximate form is the standard Fano converse. Once `T` is an interactive communication transcript, minimizing its information revelation is within information complexity. Therefore neither conditional mutual information nor the Fano lower bound can serve, by itself, as a novel `Omega_G`.

Blackwell/Le Cam comparison also warns against identifying a single scalar information quantity with complete decision informativeness: decision-theoretic comparison is a preorder over experiments/channels, not generally captured by one mutual-information number.

## Decisive conclusion

The route

[
\text{projection deficit} \Rightarrow
\text{assume required information }\kappa \Rightarrow
I(G;T|X)\ge\kappa
]

is mathematically valid but scientifically circular as a GC-II breakthrough if `\kappa` is inserted as an assumption.

The surviving problem is stronger:

> derive a nonzero quantitative requirement directly from GC-I envelope/projection structure and a specified charged operational interface, without assuming the required information/query/action deficit in advance.

Any successful theorem must expose a GC-specific bridge from geometric/projection obstruction to operational cost, then survive reduction to Myhill–Nerode state complexity, communication/information complexity, Blackwell–Le Cam comparison, resource theory, and ordinary reachability.

## Status ledger

| Candidate | Status |
|---|---|
| Conditional data-processing no-free inequality | PROVED / IMPORTED-KNOWN |
| Exact conditional-entropy lower bound | PROVED / IMPORTED-KNOWN |
| Fano approximate-recovery lower bound | PROVED / IMPORTED-KNOWN |
| Conditional information cost as `Omega_G` | FALSIFIED as novelty |
| Unconditional projection-irreducibility => positive information cost | FALSIFIED without charged-interface assumptions |
| GC-I geometry => independently derived operational cost | OPEN / PRIORITY |

