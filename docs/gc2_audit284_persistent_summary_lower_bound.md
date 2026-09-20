# GC-II Audit 284 — Persistent capability-summary lower bound

## Scope

Audit 283 identified multiplicative capability certificates with internal directed covers in log space. This audit translates that geometry into an operational memory lower bound. The counting mechanism is classical and is not claimed as a new information-theoretic theorem.

## Setup

Let `H` be a finite set of completed operational histories and let `y(h) in R_{>0}^d` be the typed capability/cost vector deposited by history `h`. Write `Y={y(h):h in H}`.

A post-hoc persistent summary has a finite state set `Sigma`, encoder `sigma:H -> Sigma`, and attainable decoder `D:Sigma -> Y`. It is `alpha`-faithful (`alpha >= 1`) when

`D(sigma(h))_i <= alpha y(h)_i`

for every history `h` and every typed coordinate `i`.

The key operational restriction is explicit: after the history is discarded, the decoder has access only to the persistent summary state. This is stronger than merely bounding the controller state while generation is still occurring.

Let `C_alpha(Y)` be the minimum attainable internal alpha-certificate cardinality from Audit 283.

## Theorem 284.1 — persistent-summary lower bound

Every alpha-faithful persistent summary satisfies

`|Sigma| >= C_alpha(Y)`.

Consequently, any fixed-length binary persistent summary requires

`k >= ceil(log_2 C_alpha(Y))`

bits.

### Proof

The image `S=D(Sigma)` is a subset of `Y` and has cardinality at most `|Sigma|`. For each `y in Y`, choose a history `h` with `y(h)=y`. Alpha-faithfulness gives `D(sigma(h))_i <= alpha y_i` for every coordinate, so `S` is an attainable internal alpha-certificate for `Y`. Therefore `C_alpha(Y) <= |S| <= |Sigma|`. A `k`-bit summary has at most `2^k` states, giving `2^k >= C_alpha(Y)` and the logarithmic bound. QED.

Status: PROVED.

## Corollary 284.2 — directed packing lower bound

Let `P subseteq Y` have the property that no attainable center in `Y` alpha-covers two distinct points of `P`. Then every alpha-faithful persistent summary has at least `|P|` states and at least `ceil(log_2 |P|)` fixed-length bits.

This is the ordinary packing-to-cover counting argument in the directed internal geometry of Audit 283.

Status: PROVED; generic packing/counting mechanism IMPORTED/KNOWN.

## Corollary 284.3 — independent deposition requires linear persistent bits

Use the Audit-280 family with `d=2m`. Each of `m` independent modules deposits either `(r,1)` or `(1,r)` into its own coordinate pair, with `r>alpha`. There are `2^m` attainable outputs. Every attainable center alpha-covers only itself: two distinct outputs differ on some pair, and in one direction a coordinate has `r > alpha*1`; in the reverse direction the complementary coordinate gives the same obstruction.

Hence

`C_alpha(Y_m)=2^m`

and every alpha-faithful post-hoc persistent summary requires

`|Sigma| >= 2^m`, equivalently `k >= m=d/2` bits.

Status: PROVED.

This resolves the apparent tension in Audits 280–282. The generator may have constant transient/control boundary state while independent local modules write into persistent typed outputs. But if those outputs are later discarded and replaced by a summary that must preserve alpha-faithful capability accounting, the summary must retain linear information in this family.

## Stronger operational statement

The lower bound is independent of how the outputs were generated. It applies to AI capability ledgers, robot/autonomous-system capability records, distributed-system summaries, or experiment-result ledgers whenever: (i) the final typed vectors form `Y`; (ii) the original history/output is no longer available; (iii) all subsequent accounting is mediated by a finite persistent state; and (iv) the decoded representative must be attainable and alpha-faithful coordinatewise.

If any of these assumptions is relaxed, the theorem must be rechecked. In particular, external/oracle access to the discarded history invalidates the finite-state bottleneck, and allowing arbitrary non-attainable decoder centers changes the relevant cover number.

## Dimensions, invariance, composition, edge cases

- `alpha` is dimensionless; independent positive unit changes leave the bound invariant by Audit 283.
- `alpha=1` yields the exact attainable-summary lower bound.
- Empty `Y` needs no state under the zero-certificate convention; an implemented machine may still conventionally have one null state.
- Duplicate histories producing the same vector do not increase the bound.
- Zero coordinates require the support-stratified treatment of Audits 275–276; this audit states the log-geometric version only for strictly positive coordinates.
- Under independent product families, Audit 283 gives certificate submultiplicativity, but no general additive lower bound on summary bits is claimed without a packing/product condition.
- The theorem is monotone in tolerance because `C_alpha` is nonincreasing in `alpha`.

## Prior-art collision status

The proof pattern is classical. Myhill-Nerode lower bounds force distinguishable histories/prefixes into different machine states, and streaming lower bounds similarly turn a distinguishing set into a lower bound on memory configurations and hence the logarithm of that set into a bit lower bound. Therefore the state-counting/information argument is IMPORTED/KNOWN and must not be advertised as a new complexity theorem.

The GC-II-specific contribution is the bridge: Audit 283's directed multiplicative capability geometry supplies the distinguishability/packing object, while this audit states exactly when that geometric entropy becomes an operational persistent-memory requirement. It also explains why earlier bounds on transient controller state, treewidth, or local query arity failed.

## Status ledger

- alpha-faithful persistent-summary state lower bound: PROVED
- bit lower bound `ceil(log2 C_alpha)`: PROVED
- directed-packing corollary: PROVED / mechanism IMPORTED/KNOWN
- Audit-280 family requires `d/2` persistent summary bits: PROVED
- generic automata/streaming distinguishability-to-memory method: IMPORTED/KNOWN
- claim that transient controller memory must obey the same lower bound: FALSIFIED by Audit 280
- nontrivial upper bound from operational write restrictions: OPEN

## Next attack

Seek a matching constructive theorem: if the operational system is allowed at most `k` persistent bits and every future accounting query is mediated only by those bits, characterize exactly which directed log-cover families can be represented, then test lossy/randomized summaries. Collision-check immediately against one-way communication complexity, streaming sketches, rate-distortion theory, approximate sufficient statistics, and automata minimization.