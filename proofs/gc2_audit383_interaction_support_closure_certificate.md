# GC-II Audit 383 — Interaction-Support Closure Certificate

## Target
Paper-II items (2), (3), and (5): after Audit 382 proved that singleton or bounded-order marginal accounting cannot control pure higher-order synergy, identify the weakest exact structural assumption under which a compact accounting bound is possible, and collision-test it against known set-function machinery.

## Setup
Let N be a finite set of intervention channels and let v:2^N -> R be a normalized capability set function, v(empty)=0. Define its Boolean-lattice Möbius coefficients
m(T)=sum_{S subseteq T} (-1)^(|T|-|S|) v(S).

Define the interaction support
H(v)={T subseteq N, T nonempty : m(T) != 0}
and interaction rank
rho(v)=max{|T|:T in H(v)}, with rho(v)=0 for v=0.

For q>=0 define the observed q-skeleton D_q(v)={v(S): |S|<=q}.

## Theorem 383.1 — exact closure under bounded interaction rank
If rho(v)<=q, then D_q(v) determines v on every subset of N exactly. In particular,
v(N)=sum_{nonempty T subseteq N, |T|<=q} m(T),
where each m(T) is computable only from values v(S) with S subseteq T and therefore |S|<=q.

### Proof
Möbius inversion gives v(A)=sum_{T subseteq A}m(T). Under rho(v)<=q all terms with |T|>q vanish. For every surviving T, m(T) uses only v(S), S subseteq T, hence only the q-skeleton. Therefore the displayed expression reconstructs v(A), including A=N. QED.

## Theorem 383.2 — sharp necessity for unrestricted exact reconstruction
Fix q<|N|. If no restriction is imposed on Möbius coefficients of order >q, then D_q cannot determine v(N), even within monotone nonnegative set functions.

### Proof
Use Audit 382's pure synergy family: v_M(S)=0 for every proper subset S of N and v_M(N)=M. For all M>=0 these functions have identical q-skeleton but distinct v_M(N). QED.

Thus bounded interaction rank is not merely sufficient: some constraint on the unseen higher-order interaction sector is logically necessary for exact reconstruction from bounded-order observations.

## Corollary 383.3 — quantitative residual certificate
Without exact bounded rank,
v(N)=V_q+E_q,
V_q:=sum_{nonempty T subseteq N, |T|<=q}m(T),
E_q:=sum_{T subseteq N, |T|>q}m(T).

Hence any independently justified bound
|E_q|<=epsilon_q
implies
|v(N)-V_q|<=epsilon_q.
For monotone v this statement still needs the absolute residual assumption: monotonicity alone does not control the signs or magnitude of individual Möbius coefficients.

## Candidate GC interpretation
A viable GC-II theorem can no longer merely posit "synergy." It must derive from frozen GC-I envelope/projection structure either

1. an interaction-rank certificate rho(v)<=q; or
2. a residual certificate |E_q|<=epsilon_q;

without evaluating all high-order coalitions.

Only that derivation would be GC-specific. The reconstruction theorem itself is classical Möbius/pseudo-Boolean structure.

## Closure-Escape reformulation
Define the q-observational equivalence class
[v]_q={w:D_q(w)=D_q(v)}.
The total capability v(N) is identifiable from q-local observations on a model class C iff evaluation at N is constant on every [v]_q intersect C.

For the class C_q={v:rho(v)<=q}, Theorem 383.1 proves identifiability. For unrestricted monotone set functions, Theorem 383.2 proves non-identifiability.

This is an exact operational/geometric criterion, but not yet a GC-II Closure-Escape breakthrough because it is equivalent to injectivity of a restricted linear observation map.

## Edge and degeneration audit
- q=0: only the zero-rank class is reconstructible.
- q=|N|: reconstruction is tautological.
- v=0: rho=0 and every reconstruction is exact.
- Pure k-way AND synergy: rho=k, so every q<k skeleton fails.
- Negative Möbius coefficients: allowed; exact theorem unchanged.
- Monotonicity: not needed for sufficiency.
- Relabeling channels: rho and support cardinalities are invariant.
- Scaling v by alpha!=0: support and rho unchanged; coefficient magnitudes scale by alpha.
- Composition: rank need not remain bounded under arbitrary nonlinear composition, so no closure claim is made without a specified composition law.

## Prior-art collision ledger
- Möbius inversion / Harsanyi dividends: IMPORTED/KNOWN.
- k-additive games, defined by vanishing Möbius coefficients above order k: IMPORTED/KNOWN.
- Unique multilinear representation of pseudo-Boolean functions and polynomial degree: IMPORTED/KNOWN.
- Higher-order interactions/hypergraph encodings: IMPORTED/KNOWN.
- GC-derived reason that operational capability functions must have bounded interaction rank or controlled residual: OPEN.

Therefore "interaction rank" is not claimed as a new mathematical invariant. Its value here is as a falsification gate: any proposed GC capability-accounting theorem based on low-order increments must supply a noncircular GC structural reason that high-order interaction mass vanishes or is bounded.

## Status ledger
- Exact q-skeleton reconstruction under rho(v)<=q: PROVED / IMPORTED-KNOWN mechanism.
- Necessity of constraining unseen high-order sector: PROVED.
- Monotonicity alone as such a constraint: FALSIFIED by Audit 382.
- Interaction rank as GC-II novelty: FALSIFIED AS NOVEL.
- q-observational injectivity criterion: PROVED / generic linear identifiability.
- GC-I envelope/projection -> bounded interaction rank: OPEN.
- GC-I envelope/projection -> quantitative residual bound: OPEN.

## Next falsification experiment
Construct finite operational systems from Audit 381, compute their induced capability set functions exactly, and search for matched pairs with identical low-order skeletons and ordinary reachability/cost/confusability summaries but different high-order Möbius support. Then test whether any frozen GC-I envelope statistic predicts rho(v) or E_q without inspecting the hidden coalitions. A successful predictor must be checked against pseudo-Boolean degree, hypergraph rank, CSP width, database acyclicity, and contextuality before any novelty claim.
