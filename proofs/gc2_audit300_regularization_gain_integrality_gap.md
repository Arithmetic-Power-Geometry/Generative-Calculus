# GC-II Audit 300 — Regularization gain is exactly the set-cover integrality gap

## Scope

Branch-only continuation of Audits 290–299. GC-I is untouched.

Let a finite feasible-action accounting instance be `I=(Y,A,B)`, where every target in the nonempty finite set `Y` is contained in at least one feasible-action set `B(a)`. Let

- `N(I)` be the minimum number of actions whose feasible sets cover `Y`;
- `N_f(I)` be the optimum of the standard fractional cover LP;
- `R_1(I)=log_2 N(I)` be the one-shot fixed-length accounting cost;
- `R_inf(I)=lim_{k->infinity} k^{-1} log_2 N(I^{x k})` be the regularized exact product-accounting rate.

Audit 299 proved `R_inf(I)=log_2 N_f(I)`.

## Theorem 300.1 — exact regularization-gain identity

Define

`G_reg(I) := R_1(I)-R_inf(I)`.

Then

`G_reg(I) = log_2( N(I) / N_f(I) )`.

Equivalently, if `IG(I)=N(I)/N_f(I)` is the standard set-cover LP integrality gap of the operational feasible-action hypergraph, then

`2^{G_reg(I)} = IG(I)`.

### Proof

Substitute Audit 299's exact identity `R_inf(I)=log_2 N_f(I)` into the definition:

`G_reg = log_2 N - log_2 N_f = log_2(N/N_f)`.

No additional assumption is used beyond finite nonempty coverability. QED.

Status: **PROVED**, conditional only on the already-proved Audit-299 theorem.

## Corollary 300.2 — zero gain criterion

`G_reg(I)=0` iff `N(I)=N_f(I)`.

Thus every integral feasible-action incidence class (including the bipartite frequency-two class of Audits 295–296) has no asymptotic regularization gain. Conversely, every positive LP integrality gap produces strict exact block-accounting compression.

Status: **PROVED**.

## Corollary 300.3 — universal finite-target upper bound

Classical set-cover LP theory gives

`N(I) <= H_|Y| N_f(I)`,

hence

`0 <= G_reg(I) <= log_2 H_|Y| <= log_2(1+ln |Y|)`.

The quantity is dimensionless. It is invariant under relabeling targets/actions and under duplicate removal that leaves the feasible-action set system unchanged.

Status of the inequality after importing the classical harmonic integrality-gap bound: **PROVED via IMPORTED/KNOWN theory**.

## Corollary 300.4 — unbounded family-level one-shot penalty

Known set-cover constructions have LP integrality gap growing on the order of `ln |Y|`. Therefore there exist finite operational-accounting families `I_n` for which

`N(I_n)/N_f(I_n) = Theta(ln |Y_n|)`

and consequently

`G_reg(I_n) = Theta(log log |Y_n|)` bits.

This is not a new combinatorial integrality-gap theorem. The GC-II consequence is that exact independent block accounting can have an unbounded additive per-copy advantage over one-shot accounting across a growing family, even though each block is required to be represented exactly.

Status: **IMPORTED/KNOWN construction + PROVED operational consequence**.

## Composition behavior

From Audit 299, `N_f(I x J)=N_f(I)N_f(J)`. Hence the asymptotic rate is additive:

`R_inf(I x J)=R_inf(I)+R_inf(J)`.

The one-shot rate is only subadditive because `N(I x J)<=N(I)N(J)`. Therefore

`G_reg(I x J) = G_reg(I)+G_reg(J) - log_2( N(I)N(J)/N(I x J) )`.

The last term is nonnegative by Audit 298. Thus

`G_reg(I x J) <= G_reg(I)+G_reg(J)`.

So regularization gain is **subadditive**, not additive in general. Equality holds whenever the integer cover number is multiplicative for the pair.

Status: **PROVED**.

### Triangle collision

For the Audit-298 triangle instance, `N=2`, `N_f=3/2`, and `N(I x I)=3`. Therefore

`G_reg(I)=log_2(4/3)`,

while

`G_reg(I x I)=log_2(3/(9/4))=log_2(4/3) < 2 log_2(4/3)`.

This is an exact counterexample to additivity of `G_reg`.

Status: **PROVED**.

## Edge and degenerate cases

- Empty `Y`: excluded because `log N` is undefined when the conventional empty cover number is zero. It can be handled separately with zero operational rate.
- Uncoverable target: excluded; both exact accounting and the fractional LP are infeasible.
- Universal action: `N=N_f=1`, hence `G_reg=0`.
- Integral incidence polyhedron: `N=N_f`, hence zero gain.
- Relabeling: all quantities unchanged.
- Duplicate identical actions: no change in either optimum.
- Cartesian powers: `R_inf` remains additive by fractional multiplicativity.

## Prior-art collision audit

The generic objects are not new: set cover, fractional cover, LP duality, integrality gaps, harmonic upper bounds, and asymptotically logarithmic gap constructions are established optimization/combinatorics. Closely related product/rectangle-cover quantities also occur in communication complexity and graph/hypergraph covering theory. Therefore **do not claim invention of the integrality gap, fractional cover, or its classical asymptotics**.

The defensible GC-II statement is an operational identification: once worst-case capability accounting is reduced to the feasible-action hypergraph (Audit 290) and repeated exact accounting is regularized (Audit 299), the entire one-shot-versus-asymptotic penalty is exactly the logarithm of the incidence integrality gap. This turns LP integrality into a directly interpretable capability-accounting compression obstruction.

## Status table

| Claim | Status |
|---|---|
| `G_reg=log_2(N/N_f)` | PROVED |
| `G_reg=0` iff integer/fractional optima agree | PROVED |
| `G_reg<=log_2 H_|Y|` | PROVED via IMPORTED/KNOWN |
| family-level `Theta(log log |Y|)` bit penalty exists | IMPORTED/KNOWN gap + PROVED consequence |
| `G_reg` additive under products | FALSIFIED |
| `G_reg` subadditive under products | PROVED |
| generic integrality-gap machinery is GC-II novelty | FALSIFIED / NOT CLAIMED |
| extension to evolving budgeted operational closures | OPEN |

## Paper-II consequence

The correct static exact accounting hierarchy is now:

1. one-shot exact cost: `log_2 N`;
2. asymptotic exact product rate: `log_2 N_f`;
3. regularization penalty: `log_2(N/N_f)`.

This is a clean separation between integer operational realization and fractional/asymptotic accounting. It should not be promoted as a new set-cover theorem; its value is the exact operational interpretation and its use as a boundary condition for any proposed `Omega_G` accounting law.
