# GC-II Audit 279 — Separator width alone does not control capability-certificate size

## Status

- Claim that bounded operational separator width alone implies a compact alpha-capability certificate: **FALSIFIED**.
- Constant-width serial construction with exponential alpha-certificate requirement: **PROVED**.
- Need for an additional bound on separator/boundary-state complexity (or an equivalent information parameter): **PROVED necessary for any theorem of this form**.
- Sequential finite-state counting mechanism: **IMPORTED/KNOWN**.
- GC-II consequence for dependency-width accounting: **CONDITIONAL contribution**.

## Question left by Audit 278

Audit 278 proved compression when attainable vectors are explicitly partitioned into modes in which only `w` coordinates vary. The next hoped-for step was to derive such compression merely from small separator width in an operational dependency graph/hypergraph.

That implication is false.

## Construction

Fix `alpha >= 1`, choose a rational `r > alpha`, let `d >= 1`, and put `k=floor(d/2)`. Consider a serial finite-state operational process with stages `i=1,...,d`. Its boundary state is a counter `c` recording how many high-cost coordinates have been selected so far. At stage `i` choose a local bit `x_i in {0,1}` and update

`c_i = c_{i-1} + x_i`,

starting at `c_0=0` and accepting exactly when `c_d=k`.

The emitted typed cost vector is

`y_i = r` if `x_i=1`, and `y_i=1` if `x_i=0`.

Thus the attainable accepted set is exactly

`Y_d = { y^T : T subseteq [d], |T|=k }`,

where `y_i^T=r` for `i in T` and `1` otherwise.

Operationally, each stage communicates with the remainder only through the single counter state. The stage graph is a path, and every transition is local to the incoming counter, one local choice, and the outgoing counter. Hence separator *variable count* is constant (one finite-state interface), even though the counter alphabet has `k+1` relevant values.

## Theorem (constant separator-width exponential certificate family)

For every fixed finite `alpha >= 1` and every `d`, the serial process above has separator variable-width one, but every attainable alpha-representative certificate `S subseteq Y_d` has

`|S| = binom(d,floor(d/2)) = Theta(2^d/sqrt(d))`.

### Proof

Take distinct equal-cardinality supports `S,T`. Since `|S|=|T|` and `S != T`, there exists `i in S\T`. At that coordinate,

`y_i^S = r > alpha = alpha y_i^T`.

Therefore `y^S` cannot alpha-cover `y^T`. Since this holds for every distinct pair, every target has only itself as an attainable alpha-representative. All `binom(d,k)` targets are therefore necessary.

The operational implementation is serial and uses one counter-valued boundary variable at each cut, proving that bounded separator variable-count alone does not control certificate size.

## What exactly failed

The separator is narrow in *number of variables* but not in information capacity. At the middle of the chain the counter can take `k+1=Theta(d)` values. A theorem parameterized only by separator variable-count ignores this boundary alphabet.

This gives a necessary correction to the target proposed in Audit 278. A defensible structural compression theorem must control not only separator width but also boundary-state complexity, e.g. a bound `B` on the number of distinguishable boundary states (or `log B` boundary information), together with scale range and approximation tolerance.

The audit does **not** prove that bounded `B` is sufficient in full generality. It proves that omitting such a parameter makes the proposed separator-width theorem false.

## Edge cases and checks

- `d=1`, `k=0`: the accepted set is a singleton; the lower bound is one.
- `alpha=1`: choose any `r>1`; the exact-certificate case is included.
- No zero coordinates occur.
- Positive dynamic range is the constant `r`.
- The lower bound is invariant under coherent positive rescaling of coordinates.
- The construction is deterministic apart from the explicit local binary choice.
- There is no additive-resource assumption behind the lower bound; the emitted vector merely records typed local costs.
- The result concerns attainable representatives. Synthetic unattainable representatives are outside the GC-II certificate semantics used in Audits 274–278.

## Relation to earlier audits

Audit 277 established the ambient-dimensional approximate-certificate barrier directly in objective space. Audit 279 realizes the same hard family by a serial local operational process. Therefore small graph/separator width does not by itself eliminate Audit 277's obstruction. Audit 278 remains valid because its stronger mode-local hypothesis bounds which objective coordinates can vary jointly; the present serial counter process violates that hypothesis.

Audit 271 likewise remains valid: local gate arity and short interfaces do not prevent globally high-order capability structure when information can propagate through state.

## Prior-art collision note

Sequential counters, finite-state dynamic programming on paths, and cardinality constraints are standard. Sperner middle-layer antichains and multiplicative Pareto separation are also established mechanisms. None is claimed as new mathematics. The GC-II-specific candidate contribution is the operational no-go statement: dependency/separator width measured only by variable count is insufficient for capability-accounting compression because a narrow interface can carry growing state information.

## Next target

Replace raw separator width by an information-sensitive structural parameter. A plausible target is: for a tree/path decomposition with at most `B` distinguishable operational boundary states per separator, local typed-cost active width at most `w`, bounded positive log-scale range `Gamma`, and `N` bags, derive an attainable alpha-certificate bound polynomial in `N` and exponential only in `w`, `log B`, and `log_alpha Gamma`. Before attempting a proof, search for constant-`B` counterexamples involving nondeterministic path multiplicity, hidden guards, or nonlocal output coupling.
