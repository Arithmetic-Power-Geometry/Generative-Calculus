# GC-II Audit 179 — Unit-invariance no-go for raw capability-accounting bounds

Status: **PROVED boundary theorem; novelty claim for an unnormalised raw bound FALSIFIED.**

## Question
Can a universal quantitative GC-II law be written directly as

\[
\Omega_G \le F(\Delta R,\Delta I,\Delta A,\Delta L)
\]

when the four increments are heterogeneous operational quantities and no calibration/normalisation has been fixed?

## Theorem (independent-unit rescaling no-go)
Let \(x=(x_1,\ldots,x_m)\in(0,\infty)^m\) denote positive raw coordinates whose numerical values may be independently rescaled by a change of units,
\(x_j\mapsto \alpha_j x_j\), \(\alpha_j>0\). Let \(\Omega\) be dimensionless and invariant under these unit changes. Suppose a proposed universal upper bound has the same numerical right-hand side in every admissible unit system:

\[
\Omega \le F(x_1,\ldots,x_m).
\]

If the bound itself is required to be unit-invariant without additional dimensional constants or reference scales, then on the strictly positive orthant

\[
F(\alpha_1x_1,\ldots,\alpha_mx_m)=F(x_1,\ldots,x_m)
\quad\forall\alpha_j>0,
\]

and therefore \(F\) is constant there.

### Proof
For arbitrary \(x,y\in(0,\infty)^m\), choose \(\alpha_j=y_j/x_j\). Independent rescaling maps \(x\) to \(y\). Unit invariance gives \(F(y)=F(x)\). Since \(x,y\) were arbitrary positive vectors, \(F\) is constant on the positive orthant. QED.

The same argument applies separately to every support stratum when zero coordinates are allowed: absent additional structure, a unit-invariant raw-coordinate law can at most distinguish which independently-scalable coordinates vanish; it cannot encode their magnitudes.

## Consequence for GC-II
A nontrivial numerical capability-accounting law cannot be claimed from raw heterogeneous \(\Delta R,\Delta I,\Delta A,\Delta L\) alone if their scales are independently conventional. At least one of the following must be supplied:

1. common physical dimensions that permit dimensionless ratios;
2. characteristic/reference scales \(R_*,I_*,A_*,L_*\), giving \(\rho=\Delta R/R_*\), etc.;
3. empirically or operationally fixed exchange rates/calibration constants;
4. a vector/Pareto-valued law rather than scalar aggregation;
5. a dimensional output \(\Omega_G\) with a declared dimension matrix and dimensionally homogeneous F.

This is a dimensional-analysis restriction, not a new GC theorem in isolation. It is the GC-II admissibility gate for any future quantitative bound.

## Nonlinear interactions
Nonlinearity does not evade the theorem. Terms such as \(\Delta R\Delta I\), \(\Delta R/(1+\Delta I)\), or arbitrary neural/polynomial F remain unit-dependent unless combined into dimensionless groups using quantities with compensating dimensions. Once reference scales are fixed, nonlinear interaction terms are legitimate, e.g.

\[
\Omega_G\le f(\rho,\iota,\alpha,\lambda,\rho\iota,\rho\lambda,\ldots),
\]

but the scientific burden moves to justifying the scales and proving/estimating f.

## Edge/degenerate checks
- Zero increments: independent rescaling preserves zero; support strata can differ.
- Negative increments: if signed changes are meaningful, positive unit rescaling preserves sign, so F may also depend on sign strata; magnitude still cannot be used without scale.
- Dimensionless coordinates: the no-go does not apply to a coordinate already defined intrinsically as dimensionless.
- Shared units: coordinates sharing a unit may yield invariant ratios; independent-rescaling assumption must not be imposed on them.
- Discrete action counts: if A is literally a dimensionless count, it is not freely unit-rescalable and may enter F directly.
- Information: bits versus nats differ by a fixed conversion; a numerical law must declare the convention or use a normalized ratio.

## Collision check
This boundary is an instance of classical dimensional homogeneity/Buckingham-Pi reasoning: meaningful laws must reduce dimensional variables to dimensionless groups. Therefore **do not claim novelty for the no-go itself**.

## Ledger
- Raw heterogeneous scalar F without calibration: **FALSIFIED as a nontrivial universal quantitative law**.
- Independent-rescaling theorem above: **PROVED / IMPORTED-KNOWN dimensional-analysis mechanism**.
- Normalized dimensionless GC coordinates: **OPEN**.
- Empirically calibrated nonlinear interaction law: **OPEN**.
- Universal GC-specific Omega_G bound after normalization: **OPEN**.

## Next experiment/theory gate
Define operational reference scales from the closure model itself rather than arbitrary external normalization (candidate: minimum nonzero admissible increment, baseline closure budget, or task-conditioned support-function scale). Then test whether the resulting dimensionless coordinates are invariant under representation changes and whether any bound is stronger than generic monotonicity/resource-theory inequalities.
