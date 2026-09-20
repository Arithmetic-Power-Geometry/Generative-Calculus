# GC-II Audit 282 — Bounded query arity does not control persistent capability diversity

Status: **PROVED** for the stated finite typed model. Generic distinguishability/equivalence-class machinery is **IMPORTED/KNOWN**; the GC-II consequence is the no-go for a proposed compression route.

## Question

Audit 281 showed that ordinary dependency treewidth can remain 1 while attainable multiplicative capability certificates are exponential. A natural repair is to measure the *query-relative* interface: perhaps if every externally permitted budget query inspects only a bounded number of typed coordinates, capability diversity becomes compressible.

This is false even at query arity 1.

## Construction

Fix `alpha >= 1` and choose `r > alpha`. Let `d=2m`. For every bit string `sigma in {0,1}^m`, define an attainable typed vector `y^sigma` by independent pairs

- sigma_j=0: pair j is `(r,1)`;
- sigma_j=1: pair j is `(1,r)`.

Thus `|Y_m|=2^m` and all positive coordinates lie in the constant range `[1,r]`.

Permit only unary threshold queries

`Q_i(y) = 1[y_i <= 1]`,  i=1,...,2m.

Each query touches exactly one coordinate.

## Theorem 282A — Unary-query exponential distinguishability

For every distinct `sigma,tau`, there is a unary query `Q_i` such that

`Q_i(y^sigma) != Q_i(y^tau)`.

Hence the joint query-signature map

`Sig(y)=(Q_1(y),...,Q_{2m}(y))`

has exactly `2^m` equivalence classes although every individual query has arity 1.

### Proof

Choose a pair j where sigma_j != tau_j. On one coordinate of that pair, one vector has value 1 and the other value r>1. The corresponding unary threshold query separates them. QED.

## Theorem 282B — Multiplicative certificate obstruction survives unary queries

For any two distinct attainable vectors `a,b`, some coordinate i satisfies `a_i=r` and `b_i=1`. Since `r>alpha`,

`a_i > alpha b_i`,

so `a` does not alpha-cover `b` under the GC-II coordinatewise multiplicative certificate relation. Reversing the vectors gives the opposite-direction obstruction. Therefore every attainable alpha-certificate requires

`|C_alpha(Y_m)| = 2^m = 2^(d/2)`.

## Consequence

Bounded *query arity* is not a sufficient structural parameter for capability-certificate compression. Even singleton observations can collectively expose an unbounded number of independent persistent capability bits.

The failed implication is

`bounded local query scope + bounded dynamic range + local dependency topology => compact global certificate`.

It fails with query arity 1, dependency graph a matching (treewidth 1), positive constant dynamic range, and independent local modules.

The quantity that matters cannot be local query arity alone. Any positive theorem must charge the **joint information capacity / index of the permitted query family on attainable outputs**, or impose a genuine factorization/compression condition on those signatures. Merely renaming the number of equivalence classes as a width would be tautological, so the next target must derive such an index bound from independently checkable operational structure.

## Edge and reduction audit

- `m=0`: one empty output; trivial certificate size 1 if the empty system is admitted.
- `m>=1`: exponential family exactly `2^m`.
- `alpha=1`: any `r>1` works.
- no zero coordinates or vanishing positive scales are used.
- rescaling all coordinates and unary thresholds by a common positive factor preserves the construction.
- independent composition of modules multiplies the number of signatures: `2^m`.
- the construction reduces to Audit 280/281 after forgetting the explicit query family; Audit 282 adds the stronger fact that arity-one external queries already retain every independent bit.

## Prior-art boundary

The abstract use of distinguishing queries/equivalence classes is classical (Myhill–Nerode-style distinguishability and information/communication viewpoints). Constant-query/local access does not in general imply a small global state or code space. No novelty is claimed for that generic phenomenon. The GC-II result is the specific operational falsification of **query-arity-only capability compression** in the typed multiplicative accounting model.

## Status ledger

- Query-arity-only compression: **FALSIFIED**.
- Arity-one exponential query-signature family: **PROVED**.
- Arity-one exponential attainable alpha-certificate family: **PROVED**.
- Generic distinguishability/equivalence mechanism: **IMPORTED/KNOWN**.
- Non-tautological structural bound on joint query-signature index: **OPEN**.
