# GC-II Audit 085 — Typed Closure Separation No-Go Under Complete Operational Comparison

## Scope
Branch-only Paper-II audit. GC-I on `main` remains frozen. Inspected parent: `be7be45ac73e6e4c515ed948234c556615048db4` (Audit 084).

## Question inherited from Audit 084
Can two finite operational systems agree under the imported comparison structures being quotiented out—simulation/reachability, complete decision comparison, and complete resource monotones—yet differ in their complete task–scale–error–budget closure with an operational consequence?

## Result
**FALSIFIED under complete operational comparison.** A separating witness of the stated form cannot exist if the imported comparison family is genuinely complete for the same admissible transformations and the same operational boundary.

### Theorem 1 — Complete-comparison closure no-go (PROVED)
Let `X` be an operational system and let

\[
\mathcal C(X):(q,s,\varepsilon,B)\mapsto \mathcal A_X(q,s,\varepsilon,B)
\]

be its complete GC closure, where `A_X` is the attainable outcome/action/performance set under the declared admissible transformations and typed budget `B=(R,I,A,L)`.

Suppose a comparison family `D` is **operationally complete for this same boundary**, meaning

\[
D(S)=D(T)
\iff
\mathcal A_S(q,s,\varepsilon,B)=\mathcal A_T(q,s,\varepsilon,B)
\quad\forall(q,s,\varepsilon,B).
\]

Then

\[
D(S)=D(T)\Longrightarrow \mathcal C(S)=\mathcal C(T).
\]

Hence there is no residual GC closure distinction with an operational consequence after quotienting by a comparison family that is already complete for the full closure domain.

**Proof.** Equality of `D` implies equality of every attainable set by completeness. The closure is exactly the indexed collection of those attainable sets. Therefore the closures are equal. QED.

This is logically elementary but decisive: a proposed separating pair can survive only by showing that the imported family is *not* complete for the enlarged GC index domain or operational boundary.

### Corollary 1 — Blackwell escape requires an enlarged domain (PROVED)
For finite statistical experiments, comparison across all decision problems characterizes Blackwell informativeness/garbling. Therefore a GC distinction cannot survive while simultaneously claiming equality under all decision problems on the same experiment boundary. A residual can arise only when GC adds something outside that boundary: e.g. typed physical budgets, endogenous interface construction, scale coupling, persistent state, composition constraints, or another explicitly modeled operation. Once added, the comparison theory must be rerun on that enlarged object; the distinction is not automatically a new invariant.

### Corollary 2 — Complete monotone escape is impossible by definition (PROVED)
If `{M_i}` is a complete family for convertibility under the same free transformations, agreement on every `M_i` fixes the convertibility relation. Therefore a claimed residual convertibility distinction after quotienting a genuinely complete monotone family is contradictory. In some resource theories finite complete families do not exist; that fact motivates infinite/operational characterizations but does not create a GC residual by itself.

### Theorem 2 — Restricted-family residual theorem (PROVED)
Let `D_0` be only a restricted imported descriptor family. If

\[
D_0(S)=D_0(T),\qquad \mathcal C(S)\ne\mathcal C(T),
\]

then the closure difference proves only that `D_0` is incomplete for `C`. It does **not** by itself establish a new law or invariant.

A novelty claim requires an additional theorem showing that the residual obeys a nontrivial structure (bound, conservation/monotonicity law, unavoidable augmentation, composition law, or complexity separation) not already supplied by the enlarged comparison theory.

## Stress audit
- Identical systems: closures equal.
- Complete operational equivalence: residual impossible.
- Restricted binary losses: residual may exist, but only demonstrates restricted-family incompleteness.
- Finite scalarizations of a nonconvex typed frontier: residual may exist because scalarizations are incomplete.
- All appropriate support functionals: recover the closed convex hull, not arbitrary nonconvex attainable structure without extra assumptions.
- Hidden memory/catalyst/environment: if continuation-relevant, it belongs in the operational state; otherwise apparent residuals are boundary mismatch.
- Scale index: a scale-specific comparison cannot be declared complete across scales unless cross-scale behavior is included.
- Error index: exact and approximate convertibility must not be conflated.
- Typed budget: comparisons using a scalar budget are not complete for a genuinely partially ordered `(R,I,A,L)` ledger unless a completeness theorem is supplied.

## Prior-art collision boundary
Blackwell comparison already equates universal decision superiority with garbling for finite experiments. Modern resource theory explicitly uses complete monotone families/operational tasks to characterize convertibility, and recent work gives universal resource-certification constructions in broad quantum settings. Thus “find a difference invisible to a complete operational comparison” is internally inconsistent; only incompleteness or boundary enlargement can generate the apparent residual.

## Consequence for Paper II
The Audit-084 search target was too strong. Exact exhaustive enumeration for a pair that agrees under *complete* imported operational comparison yet differs operationally would search for a contradiction.

The scientifically viable target is now:

**Boundary-Lift Separation Problem (OPEN).** Find the *minimal explicit enlargement* of the operational boundary from `B0` to `B1` such that systems equivalent under a comparison theory complete on `B0` become inequivalent on `B1`, and prove a quantitative law for the extra capability that is not merely the ordinary comparison theory reapplied to `B1`.

Candidate lifts must be tested in this order:
1. endogenous creation/modification of the admissible interface/action set;
2. coupled task–scale–error–typed-budget constraints that cannot be represented as a fixed decision problem on `B0`;
3. composition where the admissible grammar itself is a state variable;
4. only then physical application models.

The burden is no longer to produce a mysterious residual after complete quotienting. It is to prove a **minimal boundary-lift theorem** plus a quantitative consequence.

## Status
| Claim | Status |
|---|---|
| Separating witness after genuinely complete same-boundary operational comparison | FALSIFIED |
| Complete-comparison closure no-go | PROVED |
| Restricted descriptor residual implies descriptor incompleteness | PROVED |
| Blackwell universal decision comparison on its native finite-experiment boundary | IMPORTED/KNOWN |
| Complete resource-monotone characterization principle | IMPORTED/KNOWN |
| Boundary enlargement can create new distinctions | PROVED as a logical possibility; novelty not implied |
| Minimal Boundary-Lift Separation theorem with irreducible quantitative law | OPEN |
| GC-II positive breakthrough | OPEN / NOT ESTABLISHED |

No numerical experiment is claimed in this audit: under the complete-same-boundary hypothesis the requested separating witness is ruled out analytically, so exhaustive search for it would be scientifically misdirected.