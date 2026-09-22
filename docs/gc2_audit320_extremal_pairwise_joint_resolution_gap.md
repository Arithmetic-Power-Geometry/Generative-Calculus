# GC-II Audit 320 — Extremal pairwise-to-joint resolution gap

## Scope
This audit sharpens Audit 319 inside a deliberately restricted finite deterministic subclass. It does **not** claim novelty for optimal decision-tree theory. The GC-II purpose is to determine exactly how badly pairwise closure-escape accounting can underestimate the cost of one policy that resolves all decision-critical worlds.

## Model
Let `B` be a finite set of `K >= 2` currently possible worlds. Assume every world requires a distinct terminal decision. An admissible deterministic test `u` has unit cost and a finite outcome partition of `B`. A test is useful on a current cell `C` only if it has at least two nonempty outcome cells on `C`.

Let `V(C)` be the minimum worst-case number of tests needed to identify the true world. Then

`V(C)=0` for `|C|=1`, and otherwise

`V(C) = 1 + min_u max_y V(C ∩ u^{-1}(y))`,

where the minimum ranges over useful admissible tests.

Define the pairwise witness cost

`P(B)=max_{x != x'} min_{u: u(x) != u(x')} 1`.

Thus whenever every pair is separable, `P(B)=1`.

## Theorem 320.1 — universal finite upper bound
If every pair of distinct worlds in `B` is separated by at least one admissible unit-cost test, then

`V(B) <= K-1`.

### Proof
Induct on `K`. The result is trivial for `K=1`. For `K>1`, choose any two distinct worlds. Pairwise separability supplies a test that separates them, hence induces at least two nonempty cells `C_1,...,C_q`, each of size at most `K-1`. Every pair inside each `C_j` remains separable because the global test family separates every pair. By induction, `V(C_j) <= |C_j|-1 <= K-2`. Execute the chosen test and then an optimal strategy in the observed cell. The worst-case cost is at most `1+(K-2)=K-1`. QED.

Status: **PROVED**.

## Theorem 320.2 — the bound is tight
For every `K >= 2`, there exists a unit-cost binary-test system with `P(B)=1` and

`V(B)=K-1`.

### Construction
Let `B={1,...,K}`. For each `i`, provide the singleton test

`u_i(x)=1[x=i]`.

Every pair `i != j` is separated by `u_i`, so `P(B)=1`.

### Lower bound
Consider any adaptive policy. Until a singleton test returns `1`, a `0` outcome eliminates only the tested singleton. An adversary can answer `0` for the first `K-1` distinct singleton tests while remaining consistent with the unique untested world. Therefore some root-to-leaf path has length at least `K-1`.

### Upper bound
Test any `K-1` singleton hypotheses sequentially. A positive answer identifies the world; if all are negative, the last world is identified by elimination. Hence `V(B)<=K-1`.

Therefore `V(B)=K-1`. QED.

Status: **PROVED**.

## Corollary 320.3 — exact extremal distortion of pairwise accounting
Within the unit-cost deterministic identification subclass with `K` distinct decision classes and complete pairwise separability,

`1 <= V(B)/P(B) <= K-1`,

and the upper endpoint is attained for every `K>=2`.

Thus

`sup V(B)/P(B) = K-1`.

Status: **PROVED**.

This strictly sharpens Audit 319's hypercube family, where the ratio was only `log_2 K`. Pairwise witness accounting can miss a factor linear in the number of decision-critical classes, and that linear factor is the largest possible in this restricted unit-cost setting.

## Why this matters for GC-II
A pairwise closure-escape catalogue answers an existential question separately for each incompatible pair. A resolver must solve a different problem: compose admissible distinctions into one policy whose every possible branch terminates at a decision-homogeneous cell. The singleton construction isolates the resulting **composition burden** without resource heterogeneity, stochasticity, hidden transformations, or continuous geometry.

Consequently a nontrivial Generative Novelty Gap or capability-accounting functional cannot generally be reduced to the maximum cheapest pairwise witness. The missing term is global policy/partition complexity.

## Edge and degeneration checks
- `K=1`: no incompatible pair; `V=0`; `P` is not used.
- `K=2`: one singleton test suffices; `V=P=1`.
- Duplicate/useless tests do not change either theorem.
- Multi-outcome tests can lower `V`; Theorem 320.1 remains valid because only one separating test is needed in the induction.
- The tightness construction deliberately restricts the admissible family to singleton tests. Adding a balanced test can destroy tightness by lowering `V`.
- If pairwise separability fails, exact resolution is impossible for distinct decision labels and `V=+infinity`; the finite ratio statement does not apply.
- With non-unit costs, `K-1` is not dimensionally meaningful without a cost normalization; no such extension is claimed here.

## Prior-art collision discipline
The recurrence is standard optimal decision-tree machinery; sequential singleton identification and adversarial worst-case depth are also classical. These mechanisms are **IMPORTED/KNOWN**. The result is retained in GC-II as an exact boundary/falsification result for a proposed capability-accounting reduction, not as a claim that decision-tree complexity itself is new.

## Status ledger
- Pairwise witness lower bound `P<=V`: **PROVED** (Audit 319).
- Universal constant-factor reduction `V<=C P`: **FALSIFIED** (Audit 319).
- Exact `K`-class unit-cost extremal ratio `sup V/P=K-1`: **PROVED** (this audit).
- Pairwise witness catalogue as complete capability account: **FALSIFIED**.
- Extension to heterogeneous costs/resources/state-dependent admissibility: **OPEN**.
- Structural conditions forcing logarithmic or constant pairwise-to-joint distortion: **OPEN**.
