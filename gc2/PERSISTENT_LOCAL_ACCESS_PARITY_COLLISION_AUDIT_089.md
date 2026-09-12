# GC-II Audit 089 — Persistent Local-Access Parity Collision

## Scope
Branch-only Paper-II audit. GC-I `main` remains frozen.

## Question
Audit 076 proved impossibility for **fresh local-marginal access** and explicitly left persistent same-instance local access unresolved. This audit closes that edge case.

## Model
Let an unknown persistent state be `x in {0,1}^n`. An admissible local action queries one coordinate `i` and receives the actual bit `x_i`; later queries refer to the same persistent instance. The global task is

`PAR_n(x) = x_1 xor ... xor x_n`.

This model is deliberately stronger than fresh-marginal access because cross-query correlations are preserved.

## Theorem 089.1 — Persistent local-access parity threshold

Any deterministic or randomized protocol whose worst-case number of single-coordinate queries is at most `n-1` has worst-case parity error at least `1/2`. Querying all `n` coordinates computes parity exactly. Hence, for error `< 1/2`, the bounded-error randomized and deterministic standard query complexities of parity are exactly `n` in this model.

### Proof
Fix any deterministic decision tree of depth `< n`. Every leaf leaves at least one coordinate unqueried. For every input consistent with the leaf transcript, flipping one unqueried coordinate preserves the entire transcript and flips parity. Therefore the leaf contains equal-size even- and odd-parity completion sets under the uniform input distribution. No leaf label has conditional success greater than `1/2`; the deterministic tree therefore has average success `1/2` under the uniform distribution.

A randomized protocol is a distribution over deterministic trees. Averaging the previous statement shows its success under the uniform distribution is also `1/2`. Consequently it cannot have worst-case success greater than `1/2`. Conversely, reading all `n` bits and XORing them is exact. QED.

## Corollary 089.2 — Projection irreducibility does not create a new translator law here

GC-I's parity-style fact that every strict coordinate projection is compatible with both global parity values becomes, under persistent coordinate access, the ordinary query-complexity statement that all `n` coordinates must be acquired before parity is determined.

Thus the operational local-to-global cost is not an architecture-independent GC invariant. It depends on what is charged:

- if one coordinate read costs one query, the threshold is `n` queries;
- if a parity oracle is admitted, one parity query suffices;
- if the complete state is freely available, the acquisition cost is zero;
- if communication separates coordinates among parties, the relevant lower bound becomes communication complexity;
- if physical `R,I,A,L` costs are required, an implementation map is still needed to translate abstract queries into typed physical costs.

## Exact finite-world check

`experiments/gc2_persistent_parity_query_audit.py` exhaustively enumerates every coordinate subset and every transcript for `n=2,...,10`. For every `k<n`, every transcript has completions of both parity values; for `k=n`, every transcript is decisive.

Generated output: `results/gc2_persistent_parity_query_audit.csv`.

Exact run summary:

- `(n,k)` cases: **63**;
- transcript/subset cases checked: **88,569**;
- ambiguity-rule violations: **0**;
- for every `k<n`: **all** transcripts ambiguous;
- for `k=n`: **all** transcripts decisive.

This is exact finite consistency evidence, not novelty evidence.

## Prior-art collision

The result is standard query/decision-tree complexity in substance. Modern query-complexity literature defines deterministic and randomized protocols exactly as adaptive bit-query decision trees, and parity is a canonical global Boolean function. Parity-query decision trees are an explicitly stronger model in which a linear/parity query may expose the global XOR directly. Work on parity decision trees, Fourier lower bounds, lifting, and randomized-vs-deterministic query complexity confirms that the complexity belongs to established computational-complexity machinery rather than a new GC-specific invariant.

Representative collision points checked in this run:

1. D. Gavinsky, *Unambiguous Parity-Query Complexity*, Random Structures & Algorithms (2025): standard randomized query protocols and stronger parity-query protocols are explicitly formalized.
2. Chistopolskaya & Podolskii, *Parity Decision Tree Complexity is Greater Than Granularity* (2018): parity-decision-tree lower bounds are established via Fourier/granularity methods.
3. Zhang & Shi, *On the parity complexity measures of Boolean functions* (2010): parity decision trees are related to communication complexity and standard Boolean complexity measures.
4. Query-complexity separation literature treats deterministic/randomized decision-tree complexity as a mature model, so reinterpreting the parity threshold as a GC translator cost does not create novelty.

## Edge-case audit

- `n=1`: one coordinate query is necessary and sufficient.
- error `epsilon >= 1/2`: zero queries suffice by guessing.
- repeated queries: cannot reduce the number of distinct coordinates required.
- adaptive order: does not help; any leaf before all coordinates are known retains a parity-flipping completion.
- randomized protocols: covered by the uniform-distribution/Yao-style averaging argument above.
- noisy reads: becomes a noisy-query/statistical-estimation problem; the exact theorem no longer applies verbatim.
- block/local queries of arity `k>1`: complexity changes with the admitted query primitive and again becomes model-relative.
- quantum queries: a different established model; no GC novelty follows from changing the computational boundary.
- typed physical costs: cannot be inferred from abstract query counts without a realization map.

## Status ledger

- Persistent same-instance parity query threshold `n`: **PROVED**.
- Exact finite enumeration through `n=10`: **NUMERICALLY SUPPORTED / exact finite enumeration**.
- Query-complexity interpretation: **IMPORTED/KNOWN**.
- Persistent-local-access parity as a standalone GC-II local-to-global breakthrough: **FALSIFIED**.
- Universal positive typed `R,I,A,L` translator bound from projection irreducibility alone: **FALSIFIED**.

## Consequence for Paper II

The fresh-sample and persistent-instance variants are now both closed:

- fresh proper marginals: parity is completely indistinguishable no matter how many such samples are queried;
- persistent same-instance bit access: parity becomes computable, but exactly as ordinary query complexity, with threshold `n`.

Therefore GC-I projection irreducibility does not, by itself, yield a novel GC-II operational translator theorem. Any surviving Paper-II advance must add a structure not reducible to the chosen observation/query/communication model and must still produce a new quantitative consequence after that model is made explicit.

Next ordered work should return to the remaining Paper-II core: search for a non-tautological closure-level quantitative law that survives complete-boundary comparison and implementation-relative accounting, rather than another parity-derived translator quantity.
