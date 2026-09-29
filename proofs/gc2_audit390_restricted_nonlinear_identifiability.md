# GC-II Audit 390 — Restricted identifiability does not imply a linear certificate

## Purpose

Audit 389 gives the exact difference-kernel criterion for identification on a restricted admissible class, then gives a row-space/dual certificate for the unrestricted linear case. This audit stress-tests a tempting but false strengthening: that exact identification on an arbitrary restricted operational class should force a linear observation certificate.

## Counterexample

Let
[
V=mathbb R^2,qquad O(x_1,x_2)=x_1,qquad L(x_1,x_2)=x_2,
]
and restrict admissible descriptions to
[
C={(0,0),(1,1),(2,4)}.
]

The observation values on C are 0,1,2, hence O is injective on C. Therefore L is exactly identifiable from O on C. Explicitly, on O(C),
[
L=gcirc O,qquad g(y)=y^2.
]

### No linear certificate exists

Suppose there were a scalar lambda with L=lambda O on C. At (1,1), lambda=1. At (2,4), lambda=2. Contradiction. Therefore exact restricted identification does not imply a linear certificate.

**Status:** PROVED.

## Audit-389 criterion survives

Here
[
ker O={(0,t):tinmathbb R}.
]
The nonzero differences in C-C have first coordinate in {±1,±2}; therefore
[
(C-C)capker O={0}subseteqker L.
]
Thus Theorem 389.1 correctly certifies exact identification.

By contrast,
[
operatorname{span}(C-C)=mathbb R^2.
]
On that linear span, ker O is not contained in ker L. Hence replacing the actual admissible difference set by its span destroys a valid restricted identifiability result.

**Status:** PROVED.

## Exact finite stability constant

For a scalar decoder on the finite observation set O(C)={0,1,2}, define
[
K_C=max_{x
e yin C}rac{|L(x)-L(y)|}{|O(x)-O(y)|}.
]
The three ratios are
[
1,quad 2,quad 3,
]
so
[
K_C=3.
]
Thus exact restricted identification can be quantitatively stable even when the unrestricted linear certificate problem is infeasible.

**Status:** PROVED.

## General finite-class proposition

Let C be finite, O:C→Y and L:C→R. Then L is exactly identifiable from O on C iff L is constant on every fiber of O. When this holds there is a unique decoder
[
g:O(C)	o L(C)
]
satisfying L=g∘O on C.

If Y is normed, the sharp Lipschitz constant on the observed finite set is
[
K_C=max_{substack{x,yin C\O(x)
e O(y)}}
rac{|L(x)-L(y)|}{|O(x)-O(y)|},
]
with K_C=0 when O(C) is a singleton and L is identifiable.

Proof: fiber constancy makes g well-defined and unique on O(C). The displayed maximum is necessary for every Lipschitz constant and sufficient by its definition. QED.

**Status:** PROVED / mathematically elementary; not a novelty claim.

## Consequence for GC-II

A universal GC-II robustness theory must not require global linear recoverability unless GC operational structure independently implies it. The correct restricted target is a decoder modulus on the actual admissible geometry:
[
|L(x)-L(y)|le
F(|O(x)-O(y)|,Delta R,Delta I,Delta A,Delta L),
qquad x,yin C_{m GC},
]
where F must be derived from explicit admissible transformations/resources/information/interfaces/rules rather than defined retrospectively from the target values.

A merely empirical lookup table or the tautological sharp modulus computed after knowing all L-values is not a Closure-Escape or capability-accounting theorem.

## Stress checks

- Degenerate singleton C: identification is automatic; no scientific content.
- Noninjective O: identification still holds exactly when L is fiber-constant.
- Injective O on C: every target on C is identifiable, showing why identification alone is too weak for GC novelty.
- Linear/convex admissible geometry: additional structure can restore linear certificates; this audit makes no claim against such structured cases.
- Coordinate invariance: any bijective reparameterization of observation values preserves exact identification; metric stability depends on the chosen observation norm/metric.
- Composition: finite fiber factorization alone gives no composition law. Composition-stable decoder moduli remain OPEN.
- Dimensions: K_C has target-units per observation-unit; a multibudget F must respect the units or use explicit nondimensionalization.
- Monotonicity: not applicable to this abstract finite witness; this audit tests the logical strength of the certificate claim, not set-function regularity.

## Prior-art boundary

Factorization through fibers, sufficient statistics/identifiability language, Lipschitz inverse stability, and nonlinear inverse maps are established mathematical ideas. This audit is therefore a boundary/falsification result, not a novelty claim.

Potential GC-II novelty remains only in deriving a non-tautological, computable, composition-stable modulus or translator lower bound from the explicit GC-I operational rules.

## Ledger

| Claim | Status |
|---|---|
| exact restricted identification requires a linear certificate | FALSIFIED |
| Audit-389 difference-kernel criterion | PROVED / SURVIVES |
| spanning C-C preserves restricted identifiability | FALSIFIED |
| nonlinear decoder can exactly identify restricted capability | PROVED / IMPORTED-KNOWN principle |
| finite sharp decoder Lipschitz constant formula | PROVED / IMPORTED-KNOWN |
| unrestricted linear dual certificate is universal robustness measure | FALSIFIED |
| GC-derived computable composition-stable nonlinear modulus | OPEN |
| GC-derived translator lower bound | OPEN |
