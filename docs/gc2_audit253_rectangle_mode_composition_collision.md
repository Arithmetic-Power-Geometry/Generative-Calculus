# GC-II Audit 253 — Rectangle-mode composition: submultiplicative, not multiplicative

## Scope

This audit stress-tests the open composition question left by Audit 252 for the target rectangle-mode complexity

\[
\rho(F)=\min\left\{q:F=\bigcup_{k=1}^q \prod_j F_j^{(k)}\right\},
\]

where every covering rectangle is contained in the capability target `F`.

Status labels are deliberately conservative.

## 1. Product composition

Let `F subset X x Y` and `G subset U x V`. Their independent product target is naturally represented, after regrouping coordinates, by

\[
F\boxtimes G=\{((x,u),(y,v)):(x,y)\in F,\ (u,v)\in G\}.
\]

For two-coordinate targets this is exactly the support of the Kronecker product of their 0/1 incidence matrices.

## 2. Universal upper bound

**Proposition 253.1 (submultiplicativity). — PROVED.**

\[
\boxed{\rho(F\boxtimes G)\le \rho(F)\rho(G).}
\]

### Proof

Take minimum internal rectangle covers

\[
F=\bigcup_{i=1}^{r} A_i\times B_i,
\qquad
G=\bigcup_{j=1}^{s} C_j\times D_j,
\]

with `r=rho(F)` and `s=rho(G)`. Then

\[
F\boxtimes G
=
\bigcup_{i=1}^{r}\bigcup_{j=1}^{s}
(A_i\times C_j)\times(B_i\times D_j).
\]

Every displayed set is a rectangle contained in the product target. Hence at most `rs` rectangles suffice. QED.

The same argument extends to finitely many independent products.

## 3. Multiplicativity is false

**Candidate 253.2.**

\[
\rho(F\boxtimes G)=\rho(F)\rho(G)
\quad\text{for all finite targets.}
\]

**Status: FALSIFIED / IMPORTED-KNOWN counterexamples.**

The parameter in Audit 252 is the Boolean rank / biclique-cover number of the target incidence matrix. Under product composition it becomes Boolean rank of a Kronecker product. Existing literature explicitly establishes strict submultiplicativity for this parameter. In particular, Valerie L. Watts, *Boolean rank of Kronecker products*, Linear Algebra and its Applications 336 (2001), 261–264, gave a strict example for the crown/complement-of-identity family at `n=4`; later work by Ishay Haviv and Michal Parnas, *Upper Bounds on the Boolean Rank of Kronecker Products*, Discrete Applied Mathematics 318 (2022), 82–96, develops broader strict upper bounds and records the earlier question/counterexample history.

Therefore the multiplicativity question left OPEN in Audit 252 must not be presented as a GC-II conjectural law. It is already false in the imported rectangle-cover mathematics.

## 4. Consequence for capability accounting

Audit 252 proved that `rho(F)` is the exact minimum number of nonnegative additive typed modes required universally for an independent-generator target `F`. Combining that result with Proposition 253.1 gives

\[
\boxed{
q_{\min}^{\rm universal}(F\boxtimes G)
\le
q_{\min}^{\rm universal}(F)\,
q_{\min}^{\rm universal}(G).
}
\]

But equality need not hold. Thus two independently composed capability specifications can admit a joint exact min-plus accounting description with **strictly fewer modes than the naive product of their individually minimal mode counts**.

This is a useful structural warning: mode complexity is not an extensive or multiplicative capability currency.

## 5. Asymptotic regularization

For repeated independent composition define

\[
\rho_\infty(F)=\inf_{n\ge1}\rho(F^{\boxtimes n})^{1/n}.
\]

Submultiplicativity implies that `log rho(F^{boxtimes n})` is subadditive, so by Fekete's lemma the limit of the nth roots exists and equals the infimum above (for nonempty finite targets).

**Status: PROVED as a direct consequence of submultiplicativity + IMPORTED/KNOWN subadditive-limit machinery.**

This regularized quantity is a mathematically coherent candidate for asymptotic accounting mode growth, but it is **not claimed as a novel GC invariant**: asymptotic rank/subrank regularization and Kronecker-product asymptotics are established ideas.

## 6. Prior-art collision boundary

- Rectangle cover / Boolean rank: **IMPORTED/KNOWN**.
- Strict nonmultiplicativity of Boolean rank under Kronecker product: **IMPORTED/KNOWN**.
- Submultiplicativity proof specialized to Audit-252 target modes: **PROVED**, but elementary.
- Asymptotic regularization: **IMPORTED/KNOWN mechanism**.
- Any claim that GC-II target-mode complexity is multiplicative: **FALSIFIED**.
- Any claim that strict composition savings are uniquely generative-calculus phenomena: **FALSIFIED as a novelty claim**.

The remaining GC-specific question is not whether rectangle-mode complexity has exotic composition behavior; known Boolean-rank theory already answers that. The stronger target is to identify an operational coupling quantity involving both generator dynamics and capability geometry that survives the earlier no-go audits and is not merely a renamed matrix-factorization invariant.

## 7. Ledger

| Claim | Status |
|---|---|
| `rho(F boxtimes G) <= rho(F) rho(G)` | PROVED |
| universal exact multiplicativity of `rho` | FALSIFIED |
| strict submultiplicativity exists | IMPORTED/KNOWN |
| exact Audit-252 universal mode interpretation of `rho` | PROVED previously |
| asymptotic root limit exists | PROVED / IMPORTED-KNOWN machinery |
| `rho` is an extensive capability currency | FALSIFIED |
| GC-specific dynamic+target interaction invariant | OPEN |

## 8. References used for collision check

1. V. L. Watts, “Boolean rank of Kronecker products,” *Linear Algebra and its Applications* 336 (2001), 261–264.
2. I. Haviv and M. Parnas, “Upper Bounds on the Boolean Rank of Kronecker Products,” *Discrete Applied Mathematics* 318 (2022), 82–96. Preprint: arXiv:2102.07486.
3. Standard Fekete subadditivity lemma for the regularized limit.
