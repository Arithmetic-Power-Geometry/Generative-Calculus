# GC-II Audit 249 — Type-factorization fails under coupled capability goals

Status: **PROVED no-go; generic product-state mechanism IMPORTED/KNOWN; GC-specific interaction law OPEN**

## Motivation

Audit 248 gives the exact coarsest cost/goal congruence for a fixed deterministic generator language. A tempting GC-II shortcut is to compute separate R/I/A/L signatures and combine them, hoping capability accounting factorizes whenever the generator dynamics factorize by type. This audit tests that claim.

## Product operational model

Let the operational state be a product

\[
X=X_1\times\cdots\times X_m,
\]

with typed operation families `O_j`. Assume the strongest favorable locality conditions:

1. an operation in `O_j` reads/enables only from coordinate `x_j`;
2. it changes only `x_j`;
3. its cost depends only on `x_j`;
4. operations on distinct coordinates commute whenever both are enabled.

Thus the transition dynamics contain no cross-type interaction.

For each coordinate let `~_j` be any equivalence computed solely from that coordinate's local transition structure, enabledness and costs. The product signature identifies

\[
x\sim_{\times}y\iff x_j\sim_j y_j\quad\forall j.
\]

## Theorem 249.1 — goal-saturation criterion

The product signature can be a valid Audit-248 capability congruence only if the goal set `F` is saturated under `~_x`:

\[
x\sim_{\times}y\Longrightarrow [x\in F]=[y\in F].
\]

This condition is necessary even when all typed dynamics are perfectly independent.

### Proof

Audit 248 initializes refinement by goal membership. Any cost/goal congruence must therefore preserve the predicate `1_F`. If one product-equivalent pair has opposite goal status, the product signature merges states that Audit 248 separates at depth zero. Hence it is not a capability congruence. QED.

## Minimal exact counterexample

Take two binary coordinates `R,I in {0,1}` and no operations at all. Therefore every coordinate has identical empty local transition structure; if local signatures ignore the global goal, all values of each coordinate may be locally collapsed.

Choose the coupled goal

\[
F=\{(0,0),(1,1)\},
\]

i.e. `R XOR I = 0`.

Then `(0,0)` and `(0,1)` have the same factorized transition information under the collapsed local signatures, but the first is a goal and the second is not. Their exact capability values are respectively `0` and `+infinity` because there are no operations.

Thus independent typed dynamics do **not** imply independent capability accounting.

## Stronger interaction consequence

Cross-type interaction can enter through at least three logically distinct locations:

- generator dynamics/preconditions/effects;
- costs/resources;
- the capability target itself.

Therefore a proposed law

\[
\Omega_G\le F(\Delta R,\Delta I,\Delta A,\Delta L)
\]

cannot justify additive or product-separable structure merely from typed-local operations. The target predicate must also be shown to decompose appropriately. Nonlinear interaction terms are not optional bookkeeping when the goal couples types.

## Positive boundary

If `F` is saturated under the proposed product equivalence, goal membership itself creates no immediate obstruction. This is only a necessary boundary, not a claim that product factorization is sufficient: successor structure must still satisfy the Audit-248 congruence conditions.

A stronger sufficient theorem would require both (i) product-local transition semantics and (ii) a target decomposition compatible with the product quotient. That route is standard product-transition/bisimulation territory and is not claimed as novelty here.

## Edge and degeneracy checks

- Empty operation language: counterexample already works, so sequencing is not the cause.
- Zero costs: irrelevant; no transition is needed for the separation.
- One coordinate: no cross-type claim remains.
- Universal or empty goal: goal saturation holds trivially.
- Rectangular goals: may satisfy a suitable product quotient, but only when each local equivalence also respects the relevant local goal predicate.
- Coupled XOR/equality goal: gives the minimal binary obstruction.
- Adding commuting local operations does not repair an unsaturated product quotient because goal membership is tested at refinement depth zero.

## Prior-art collision

The mathematical mechanism is generic: product transition systems, bisimulation/congruence, compositional verification and factored planning already require compatibility between abstractions and the property/goal being preserved. Audit 248 itself is standard deterministic bisimulation/partition refinement. Therefore the goal-saturation criterion is **not** claimed as a new generic theorem.

The GC-II value is a falsification of a specific accounting shortcut: typed R/I/A/L independence at the generator level is insufficient to justify separable capability accounting.

## Ledger

- Independent typed dynamics imply factorized capability accounting for arbitrary goals: **FALSIFIED**.
- Goal saturation is necessary for a product signature to be a capability congruence: **PROVED**.
- Cross-type interaction can arise solely from the capability target: **PROVED**.
- Generic product/congruence mechanism: **IMPORTED/KNOWN**.
- GC-specific minimal interaction statistic sufficient for quantitative capability accounting: **OPEN**.
- Non-ad-hoc conditions yielding a useful R/I/A/L decomposition theorem: **OPEN**.
