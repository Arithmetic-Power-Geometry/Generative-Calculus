# GC-II Audit 316 — Robust finite-precision reversibility lower bound

## Status

- Finite-precision worst-case reconstruction lower bound: **PROVED**.
- Dependence on cycle rank `beta=(n-1)(n-2)/2`: **PROVED**.
- Metric-packing mechanism: **IMPORTED/KNOWN**.
- Claim of novelty for generic metric entropy / rate-distortion: **NOT MADE**.
- Extension to stochastic/noisy average-case encoders: **OPEN**.

## Question

Audit 315 proved that exact continuous Euclidean summaries cannot compress the directional-reversibility quotient below cycle rank. Exactness and continuity still leave open a more operational question: how many finite bits are necessary if reconstruction is only required to be accurate to tolerance `epsilon`?

## Operational domain

Let

`beta = (n-1)(n-2)/2`

and use the root-triangle circulation coordinates from Audits 313–315. Audit 314's strict direct-edge construction, sharpened in Audit 315, shows that the operationally realizable quotient contains a nonempty open subset of `R^beta`. Therefore there exist a center `c` and `rho>0` such that the closed `l_infinity` cube

`K = c + [-rho,rho]^beta`

is operationally realizable.

The scale `rho` is not universal: it belongs to the chosen strictly feasible operational neighborhood. The theorem below is conditional only on such a certified cube, whose existence is already guaranteed locally by the strict realization construction.

## Theorem — robust finite-code lower bound

Let an encoder

`E: K -> {1,...,M}`

be arbitrary; no continuity, linearity, measurability, or computational assumption is imposed. Let a decoder

`D: {1,...,M} -> R^beta`

satisfy the uniform worst-case guarantee

`||D(E(x))-x||_infinity <= epsilon` for every `x in K`.

For `0 < epsilon < rho/2`,

`M >= ( floor(rho/(2 epsilon)) + 1 )^beta`.

Consequently any fixed-length binary representation with `b` bits obeys

`b >= beta log_2( floor(rho/(2 epsilon)) + 1 )`.

In particular, at fixed relative accuracy `epsilon/rho`, the necessary bit count is `Omega(beta)=Omega(n^2)`.

### Proof

Along each coordinate of `K`, choose

`m = floor(rho/(2 epsilon)) + 1`

values separated by `4 epsilon`, starting at `c_i-rho`. Because `(m-1)4epsilon <= 2rho`, all selected values lie in the coordinate interval. Their Cartesian product gives `m^beta` operationally realizable points.

Any two distinct selected points have `l_infinity` distance at least `4 epsilon`. If two such points `x,y` shared the same codeword, then the decoder would output the same `z=D(E(x))=D(E(y))`; by the triangle inequality,

`||x-y||_infinity <= ||x-z||_infinity + ||z-y||_infinity <= 2 epsilon`,

contradicting their separation. Hence all packing points require distinct codewords, so `M>=m^beta`. Taking base-2 logarithms proves the bit bound.

The deliberately conservative `4 epsilon` packing avoids boundary/equality ambiguity. Sharper constants are possible but are not scientifically material to the dimension scaling.

## Stronger interpretation relative to Audit 315

Audit 315 needed continuity because exact real-valued set-theoretic encodings can be pathological. This audit removes that loophole for finite precision: **even a completely discontinuous encoder cannot beat the packing lower bound if a uniform epsilon reconstruction guarantee is required**.

Thus the surviving statement is not merely topological:

`robust finite-precision directional accounting requires information proportional to cycle rank`.

For complete `n`-state networks,

`beta=(n-1)(n-2)/2`,

so fixed-relative-accuracy accounting requires quadratically many bits in `n` up to a constant depending on the requested relative resolution.

## Edge, domain, and invariance checks

- `n=2`: `beta=0`; the bound is vacuous, consistent with no cycle degree of freedom.
- `n=3`: `beta=1`; the result reduces to ordinary scalar interval quantization.
- `n>=4`: multiple independent cycle coordinates force multiplicative packing growth.
- `epsilon >= rho/2`: the displayed conservative packing bound is intentionally not asserted; coarse reconstruction may use very few codewords.
- Translation of the circulation cube changes `c` but not the packing count.
- Coherent positive rescaling sends `(rho,epsilon)` to `(alpha rho,alpha epsilon)` and preserves the relative-accuracy bound.
- State relabeling changes the circulation basis but not `beta`; norm constants can change under a different basis, not the quadratic dimension scaling.
- The theorem concerns the directional quotient only. Lossless or robust accounting of the symmetric burden field can require additional information.
- No composition law is needed for the information lower bound. Under the additive-cost composition considered in Audits 313–315, circulation coordinates add, but this theorem does not extrapolate that assumption to arbitrary physical composition.

## Collision / prior-art audit

The proof is a standard packing/covering-number argument from metric entropy and information theory: an epsilon-accurate decoder must distinguish sufficiently separated source points. Euclidean packing, quantization, rate-distortion, and compressed-sensing literatures contain this generic mechanism. Therefore the packing lemma and its logarithmic code-size consequence are **IMPORTED/KNOWN**, not GC-II novelty.

Johnson–Lindenstrauss-type embeddings do not invalidate the result: they preserve pairwise distances for finite point clouds with distortion and a target dimension depending logarithmically on cloud size; here the demand is uniform reconstruction of every point in a full `beta`-dimensional operational cube from a finite codebook. Likewise compressed sensing gains require structural restrictions such as sparsity; the present lower bound is explicitly for the unrestricted locally full-dimensional cycle quotient.

The GC-II-specific bridge is the operational realizability result of Audits 314–315: the metric packing is not performed in an abstract vector space disconnected from the model. A full-dimensional cube of cycle coordinates is realized by valid shortest-path conversion systems.

## Scientific boundary after Audits 312–316

- Single normalized reversibility scalar as complete invariant: **FALSIFIED**.
- Universal state-potential representation: **FALSIFIED**.
- Exact linear compression below cycle rank: **IMPOSSIBLE**.
- Exact continuous nonlinear compression below cycle rank: **IMPOSSIBLE**.
- Robust finite-precision arbitrary encoding with sub-cycle-rank information at fixed relative accuracy: **IMPOSSIBLE in the stated worst-case finite-code model**.
- Generic packing mechanism: **IMPORTED/KNOWN**.
- Average-case/source-distribution rate-distortion bound: **OPEN**.
- Sparse/constrained operational subclasses with lower intrinsic dimension: **OPEN and explicitly compatible with this theorem**.

## Next target

Move back up the Paper-II priority stack: connect this robust irreducibility result to the budgeted operational-closure / Closure-Escape program. Seek a theorem showing when an attempted local translator must either (i) carry at least the relevant cycle/interaction information budget, (ii) invoke additional admissible information/resources/interfaces, or (iii) fail to preserve a specified family of conversion decisions. Any such theorem must be reduced against communication complexity, sufficient statistics, Blackwell/Le Cam deficiency, CSP/database width, and standard information bottleneck/data-processing results before a novelty claim.