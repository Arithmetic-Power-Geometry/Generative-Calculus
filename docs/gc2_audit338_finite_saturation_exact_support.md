# GC-II Audit 338 — Finite Saturation and Exact Support Criterion

## Question
Audit 335 showed that one reusable schema can create quadratically many new ordered-pair capabilities. Audits 336–337 introduced reuse horizon `h` and transition topology `M`. Is `h` an independent unbounded accounting coordinate on a finite operational quotient?

## Setup
Let `Q` be a finite baseline operational quotient with `q=|Q|`. After absorbing arbitrary baseline motion before and after each newly admitted transformation, let `M in {0,1}^{q x q}` be the adjacency matrix of the resulting new macro-transition relation. Let `B in {0,1}^{q x q}` encode baseline reachability. Work over the Boolean semiring for reachability. Define

`S_h = I OR M OR M^2 OR ... OR M^h`.

Define depth-h raw pair novelty by

`Omega_pair^(h) = |{(x,z): B[x,z]=0 and S_h[x,z]=1}|`.

(If reflexive baseline reachability is included, the `I` term contributes no novelty.)

## Theorem 338A — Exact support criterion
For every `h>=0`,

`Omega_pair^(h) = |supp(S_h) \ supp(B)|`.

Equivalently, a baseline-novel ordered pair `(x,z)` is available within at most `h` new macro-steps iff `(S_h)[x,z]=1` over the Boolean semiring.

### Proof
By induction on path length, `(M^ell)[x,z]=1` iff there exists a directed macro-walk of exactly `ell` steps from `x` to `z`. Boolean union over `ell=0,...,h` is therefore exactly reachability by at most `h` macro-steps. Removing baseline-supported pairs leaves precisely the novel pairs. QED.

Status: **PROVED**. The matrix/reachability mechanism is **IMPORTED/KNOWN** graph theory; the role here is to make the GC-II novelty object exact rather than merely bounded.

## Theorem 338B — Finite saturation
For every finite quotient with `q>=1`,

`S_h = S_(q-1)` for every `h>=q-1` at the level of Boolean support. Consequently,

`Omega_pair^(h) = Omega_pair^(q-1)` for all `h>=q-1`.

### Proof
If `z` is reachable from `x`, choose a shortest directed walk. A shortest walk cannot repeat a vertex: deleting the segment between two occurrences of a repeated vertex produces a shorter walk with the same endpoints. Hence every reachable distinct pair has a simple path with at most `q-1` edges. Reflexive pairs are already represented by `I`. Thus no new support can first appear after depth `q-1`. QED.

Status: **PROVED**.

## Corollary 338C — Horizon is not an independent asymptotic coordinate on finite quotients
Audit 336's horizon can always be replaced by

`h_eff = min(h,q-1)`.

Therefore the finite raw-pair accounting problem does **not** require an independently unbounded reuse-depth coordinate once the operational quotient size is fixed. Audit 335's successor family saturates exactly at `h=q-1`.

Status: **PROVED**.

## Corollary 338D — Exact computational criterion for closure escape in raw pair novelty
There is positive raw novelty by depth `h` iff

`supp(S_h) \ supp(B) != empty`.

Full finite-horizon pair novelty is computable exactly by Boolean transitive-closure support, while Audits 336–337 are upper envelopes useful when the full topology is unavailable.

Status: **PROVED / IMPORTED-KNOWN computational mechanism**.

## Edge and degenerate cases
- `q=1`: `q-1=0`; no distinct ordered-pair novelty exists after quotienting; saturation is immediate.
- `h=0`: only `I` is available; with reflexive baseline closure, novelty is zero.
- self-loops: cannot postpone first reachability of a distinct target; they are removable from a shortest witness.
- cycles: repeated vertices are removable from a shortest reachability witness, so cycles do not defeat the `q-1` bound.
- disconnected topology: unreachable pairs remain absent for every horizon.
- relabelling: simultaneous row/column permutation preserves support cardinality and saturation depth.
- duplicated syntactic rules: if they induce the same macro relation, `M` is unchanged.

## Composition behavior
For serial composition of macro relations `M1,M2`, Boolean matrix multiplication gives the exact support of two-step composed capability. For repeated reuse of one relation, Boolean powers give exact step-indexed capability. No additive capability assumption is used.

## Prior-art boundary
Finite directed reachability, Boolean matrix powers, transitive closure, and the existence of simple path witnesses of length at most `q-1` are classical graph-theoretic facts (**IMPORTED/KNOWN**). No novelty is claimed for those facts. The GC-II contribution of this audit is architectural: it closes the apparent extra unbounded `h` degree of freedom introduced after Audit 335 and identifies the exact finite operational object that raw pair novelty depends on.

## Consequence for the Paper-II program
The failed universal law

`Omega_G <= F(Delta R, Delta I, Delta A, Delta L)`

cannot be repaired merely by appending an unconstrained reuse horizon. For finite raw pair novelty, `h` saturates at `q-1`; the irreducible missing information is instead opportunity-space size and/or macro-transition geometry (or a principled compressed invariant of them). A scientifically meaningful next target is therefore a bridge theorem from charged operational changes to restrictions on the support/growth geometry of `M`, rather than another free scalar coordinate.
